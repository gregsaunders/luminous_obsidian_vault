import { App, Plugin, PluginSettingTab, Setting, TFile, Notice } from "obsidian";

// ---------------------
// Plugin Settings Interface
// ---------------------
interface FolderFrontMatterSettings {
    rootDir: string;
    attributeName: string;
}

const DEFAULT_SETTINGS: FolderFrontMatterSettings = {
    rootDir: "Projects",
    attributeName: "folder"
};

// ---------------------
// Settings Tab
// ---------------------
class FolderFrontMatterSettingTab extends PluginSettingTab {
    plugin: FolderFrontMatterPlugin;

    constructor(app: App, plugin: FolderFrontMatterPlugin) {
        super(app, plugin);
        this.plugin = plugin;
    }

    display(): void {
        const { containerEl } = this;
        containerEl.empty();

        containerEl.createEl("h2", { text: "Folder Front Matter Settings" });

        new Setting(containerEl)
            .setName("Root Directory")
            .setDesc("Only files below this directory will get the front matter attribute.")
            .addText(text => text
                .setValue(this.plugin.settings.rootDir)
                .onChange(async (value) => {
                    this.plugin.settings.rootDir = value.trim();
                    await this.plugin.saveSettings();
                }));

        new Setting(containerEl)
            .setName("Front Matter Attribute Name")
            .setDesc("The key name to insert into the front matter (e.g. 'folder').")
            .addText(text => text
                .setValue(this.plugin.settings.attributeName)
                .onChange(async (value) => {
                    this.plugin.settings.attributeName = value.trim() || "folder";
                    await this.plugin.saveSettings();
                }));
    }
}

// ---------------------
// Main Plugin Class
// ---------------------
export default class FolderFrontMatterPlugin extends Plugin {
    settings: FolderFrontMatterSettings;

    async onload() {
        await this.loadSettings();

        // Add settings tab
        this.addSettingTab(new FolderFrontMatterSettingTab(this.app, this));

        // Register file event handlers
        this.registerEvent(this.app.vault.on("create", (abstractFile) => {
            if (abstractFile instanceof TFile) {
                this.handleFileEvent(abstractFile);
            }
        }));
        
        this.registerEvent(this.app.vault.on("modify", (abstractFile) => {
            if (abstractFile instanceof TFile) {
                this.handleFileEvent(abstractFile);
            }
        }));

        this.registerEvent(this.app.vault.on("rename", (abstractFile, oldPath) => {
            if (abstractFile instanceof TFile) {
                this.handleFileEvent(abstractFile);
            }
        }));
                
        // Add a command to manually re-process all files
        this.addCommand({
            id: 'update-all-folder-frontmatter',
            name: 'Update All Folder Frontmatter',
            callback: async () => {
                await this.updateAllRelevantFiles();
                new Notice('All relevant files updated with folder front matter.');
            }
        });

        // On layout ready, process existing files
        this.app.workspace.onLayoutReady(() => {
            this.updateAllRelevantFiles().catch(console.error);
        });
    }

    async loadSettings() {
        this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
    }

    async saveSettings() {
        await this.saveData(this.settings);
    }

    /**
     * Update all markdown files under the rootDir that don't have the attribute or need refreshing.
     */
    async updateAllRelevantFiles() {
        const files = this.app.vault.getMarkdownFiles();
        for (const file of files) {
            if (this.isInRootDir(file)) {
                await this.ensureFolderFrontMatter(file);
            }
        }
    }

    /**
     * Check if file is under the configured root directory.
     */
    private isInRootDir(file: TFile): boolean {
        const rootDir = this.settings.rootDir.replace(/\\/g, "/");
        const filePath = file.path;
        return filePath.startsWith(rootDir + "/") || filePath === rootDir;
    }

    /**
     * Handles file creation/modification events and ensures the folder attribute is set.
     */
    private async handleFileEvent(file: TFile) {
        if (!this.isMarkdownFile(file)) return;
        if (!this.isInRootDir(file)) return;
        await this.ensureFolderFrontMatter(file);
    }

    /**
     * Check if file is a markdown file.
     */
    private isMarkdownFile(file: TFile): boolean {
        return file.extension === "md";
    }

    /**
     * Ensure the folder attribute is set in the front matter of the file.
     */
    private async ensureFolderFrontMatter(file: TFile) {
        const folderPath = this.getRelativeFolderPath(file);
        const attrName = this.settings.attributeName;

        const originalContent = await this.app.vault.read(file);
        const { content: newContent, changed } = this.updateFrontMatter(originalContent, attrName, folderPath);

        if (changed) {
            await this.app.vault.modify(file, newContent);
        }
    }

    /**
     * Returns the relative folder path inside the rootDir.
     * - If file is directly under rootDir: returns ""
     * - If file is under subfolders: returns the full path (e.g. "90 days/Finance").
     */
    private getRelativeFolderPath(file: TFile): string {
        const rootDir = this.settings.rootDir.replace(/\\/g, "/");
        const parts = file.path.split("/");
        // Remove filename
        parts.pop();
        // Remove the root directory if it matches
        if (parts.length > 0 && parts[0] === rootDir) {
            parts.shift();
        }
        // Join what's left. If nothing is left, it's directly under rootDir, so return ""
        return parts.join("/");
    }

    /**
     * Update the front matter of the file content with the given attribute/value.
     * If attribute doesn't exist, it adds it. If it exists but differs, update it.
     * If no front matter block, create one.
     */
    private updateFrontMatter(content: string, key: string, value: string): { content: string; changed: boolean } {
        const frontMatterRegex = /^---\n([\s\S]*?)\n---\n?/;
        let changed = false;
        let newContent = content;

        // Always quote the value to handle empty strings and spaces properly
        const newLine = `${key}: "${value}"`;

        const match = content.match(frontMatterRegex);
        if (match) {
            const frontMatterLines = match[1].split("\n");
            let keyPresent = false;
            const updatedLines = frontMatterLines.map(line => {
                const [foundKey, ...rest] = line.split(":");
                if (foundKey && foundKey.trim().toLowerCase() === key.toLowerCase()) {
                    keyPresent = true;
                    const currentVal = rest.join(":").trim().replace(/^"|"$/g, '');
                    if (currentVal !== value) {
                        changed = true;
                        return newLine;
                    }
                }
                return line;
            });

            if (!keyPresent) {
                updatedLines.push(newLine);
                changed = true;
            }

            if (changed) {
                newContent = content.replace(frontMatterRegex, `---\n${updatedLines.join("\n")}\n---\n`);
            }

        } else {
            // No front matter block, create one
            newContent = `---\n${newLine}\n---\n${content}`;
            changed = true;
        }

        return { content: newContent, changed };
    }

    onunload() {
        // Cleanup if needed
    }
}
