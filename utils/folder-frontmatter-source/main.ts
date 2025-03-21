import { App, Plugin, PluginSettingTab, Setting, TFile, Notice } from "obsidian";

// ---------------------
// Types and Interfaces
// ---------------------
interface FolderFrontMatterSettings {
    rootDir: string;
    attributeName: string;
}

type FrontMatterResult = {
    content: string;
    changed: boolean;
};

const DEFAULT_SETTINGS: FolderFrontMatterSettings = {
    rootDir: "Projects",
    attributeName: "folder"
};

// ---------------------
// File Processor Service
// ---------------------
class FileProcessor {
    constructor(private settings: FolderFrontMatterSettings) {}

    isMarkdownFile(file: TFile): boolean {
        return file.extension === "md";
    }

    isInRootDir(file: TFile): boolean {
        const rootDir = this.normalizePath(this.settings.rootDir);
        const filePath = file.path;
        return filePath.startsWith(`${rootDir}/`) || filePath === rootDir;
    }

    getRelativeFolderPath(file: TFile): string {
        const rootDir = this.normalizePath(this.settings.rootDir);
        const parts = file.path.split("/");
        parts.pop(); // Remove filename
        
        if (parts.length > 0 && parts[0] === rootDir) {
            parts.shift(); // Remove root directory if it matches
        }
        
        return parts.join("/");
    }

    private normalizePath(path: string): string {
        return path.replace(/\\/g, "/");
    }
}

// ---------------------
// Front Matter Service
// ---------------------
class FrontMatterService {
    private readonly frontMatterRegex = /^---\n([\s\S]*?)\n---\n?/;

    updateFrontMatter(content: string, key: string, value: string): FrontMatterResult {
        const match = content.match(this.frontMatterRegex);
        
        if (match) {
            return this.updateExistingFrontMatter(content, match, key, value);
        }
        
        return this.createNewFrontMatter(content, key, value);
    }

    private updateExistingFrontMatter(
        content: string, 
        match: RegExpMatchArray, 
        key: string, 
        value: string
    ): FrontMatterResult {
        const frontMatterLines = match[1].split("\n");
        const newLine = this.createFrontMatterLine(key, value);
        let keyPresent = false;
        let changed = false;

        const updatedLines = frontMatterLines.map(line => {
            const [foundKey, ...rest] = line.split(":");
            if (foundKey?.trim().toLowerCase() === key.toLowerCase()) {
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

        if (!changed) {
            return { content, changed: false };
        }

        const newContent = content.replace(
            this.frontMatterRegex, 
            `---\n${updatedLines.join("\n")}\n---\n`
        );
        return { content: newContent, changed: true };
    }

    private createNewFrontMatter(content: string, key: string, value: string): FrontMatterResult {
        const newLine = this.createFrontMatterLine(key, value);
        return {
            content: `---\n${newLine}\n---\n${content}`,
            changed: true
        };
    }

    private createFrontMatterLine(key: string, value: string): string {
        return `${key}: "${value}"`;
    }
}

// ---------------------
// Settings Tab
// ---------------------
class FolderFrontMatterSettingTab extends PluginSettingTab {
    constructor(app: App, private plugin: FolderFrontMatterPlugin) {
        super(app, plugin);
    }

    display(): void {
        const { containerEl } = this;
        containerEl.empty();
        
        this.createHeader();
        this.createRootDirSetting();
        this.createAttributeNameSetting();
    }

    private createHeader(): void {
        this.containerEl.createEl("h2", { text: "Folder Front Matter Settings" });
    }

    private createRootDirSetting(): void {
        new Setting(this.containerEl)
            .setName("Root Directory")
            .setDesc("Only files below this directory will get the front matter attribute.")
            .addText(text => text
                .setValue(this.plugin.settings.rootDir)
                .onChange(async (value) => {
                    this.plugin.settings.rootDir = value.trim();
                    await this.plugin.saveSettings();
                }));
    }

    private createAttributeNameSetting(): void {
        new Setting(this.containerEl)
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
    private fileProcessor: FileProcessor;
    private frontMatterService: FrontMatterService;

    async onload() {
        console.log('Loading Folder Front Matter plugin...');
        await this.loadSettings();
        console.log('Settings loaded:', this.settings);
        this.initializeServices();
        this.registerSettingsTab();
        this.registerEventHandlers();
        this.registerCommands();
        this.processExistingFiles();
        console.log('Folder Front Matter plugin loaded successfully.');
    }

    private initializeServices(): void {
        this.fileProcessor = new FileProcessor(this.settings);
        this.frontMatterService = new FrontMatterService();
    }

    private registerSettingsTab(): void {
        this.addSettingTab(new FolderFrontMatterSettingTab(this.app, this));
    }

    private registerEventHandlers(): void {
        this.registerFileEvents();
    }

    private registerFileEvents(): void {
        // Register create event
        this.registerEvent(
            this.app.vault.on('create', async (file) => {
                try {
                    if (file instanceof TFile) {
                        // Add small delay to allow other operations to complete
                        await new Promise(resolve => setTimeout(resolve, 100));
                        await this.handleFileEvent(file);
                    }
                } catch (error) {
                    console.error(`Error handling create event for ${file.path}:`, error);
                }
            })
        );

        // Register modify event
        this.registerEvent(
            this.app.vault.on('modify', async (file) => {
                try {
                    if (file instanceof TFile) {
                        await this.handleFileEvent(file);
                    }
                } catch (error) {
                    console.error(`Error handling modify event for ${file.path}:`, error);
                }
            })
        );

        // Register rename event - includes oldPath parameter
        this.registerEvent(
            this.app.vault.on('rename', async (file, oldPath) => {
                try {
                    if (file instanceof TFile) {
                        // Add small delay to allow other operations to complete
                        await new Promise(resolve => setTimeout(resolve, 100));
                        await this.handleFileEvent(file);
                    }
                } catch (error) {
                    console.error(`Error handling rename event for ${file.path}:`, error);
                }
            })
        );
    }

    private registerCommands(): void {
        this.addCommand({
            id: 'update-all-folder-frontmatter',
            name: 'Update All Folder Frontmatter',
            callback: async () => {
                await this.updateAllRelevantFiles();
                new Notice('All relevant files updated with folder front matter.');
            }
        });
    }

    private processExistingFiles(): void {
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

    async updateAllRelevantFiles() {
        const files = this.app.vault.getMarkdownFiles();
        const relevantFiles = files.filter(file => this.fileProcessor.isInRootDir(file));
        
        await Promise.all(
            relevantFiles.map(file => this.ensureFolderFrontMatter(file))
        );
    }

    private async handleFileEvent(file: TFile) {
        // Skip if file shouldn't be processed
        if (!this.shouldProcessFile(file)) {
            return;
        }

        // Using a more concise single log entry
        console.log(`Processing: ${file.path} (folder: ${this.fileProcessor.getRelativeFolderPath(file)})`);
        await this.ensureFolderFrontMatter(file);
    }

    private shouldProcessFile(file: TFile): boolean {
        return this.fileProcessor.isMarkdownFile(file) && 
               this.fileProcessor.isInRootDir(file);
    }

    private async ensureFolderFrontMatter(file: TFile) {
        try {
            // Verify file still exists and is accessible
            if (!await this.app.vault.adapter.exists(file.path)) {
                console.log(`File no longer exists: ${file.path}`);
                return;
            }

            const folderPath = this.fileProcessor.getRelativeFolderPath(file);
            const originalContent = await this.app.vault.read(file);
            
            const { content: newContent, changed } = this.frontMatterService.updateFrontMatter(
                originalContent,
                this.settings.attributeName,
                folderPath
            );

            if (changed) {
                // Verify file still exists before modifying
                if (await this.app.vault.adapter.exists(file.path)) {
                    await this.app.vault.modify(file, newContent);
                    console.log(`Updated front matter for ${file.path} [${this.settings.attributeName}: "${folderPath}"]`);
                }
            }
        } catch (error) {
            console.error(`Error processing front matter for ${file.path}:`, error);
        }
    }
}
