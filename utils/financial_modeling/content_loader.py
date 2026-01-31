"""
Content Loader for Luminous Wetland Financial Model

Loads externalized documentation content from YAML files and provides
structured access for the Excel generator. Uses pydantic for schema validation.

Design Principles:
- Single Source of Truth: NO fallbacks to embedded content
- Fail Fast: Validate structure before any Excel writing begins
- Path Safety: Uses Path(__file__).parent for reliable resolution
"""

from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import yaml

from pydantic import BaseModel, Field, ValidationError, field_validator


# =============================================================================
# PYDANTIC MODELS - Schema Definitions
# =============================================================================

class GlossaryTerm(BaseModel):
    """A single glossary term with definition and optional context."""
    term: str
    definition: str
    context: Optional[str] = None
    related_sheets: Optional[List[str]] = None
    source: Optional[str] = None
    units: Optional[str] = None


class GlossaryContent(BaseModel):
    """Global glossary content file structure."""
    terms: List[GlossaryTerm]


class DataSource(BaseModel):
    """A single data source citation."""
    citation: str
    url: Optional[str] = None
    notes: Optional[str] = None


class DataSourcesContent(BaseModel):
    """Global data sources content file structure."""
    sources: List[Union[str, DataSource]]


class ChangeLogEntry(BaseModel):
    """A single change log entry."""
    version: str
    date: str
    changes: str


class ChangeLogContent(BaseModel):
    """Global change log content file structure."""
    entries: List[ChangeLogEntry]


class TableDefinition(BaseModel):
    """A table structure for embedding in sheets (legacy, use TableDocumentation)."""
    headers: List[str]
    rows: List[Union[List[Any], Dict[str, Any]]]


class TableDocumentation(BaseModel):
    """Full metadata for table documentation with inline and reference content.

    Inline (above table):
        - title: Brief title displayed above table
        - description: 1-2 sentence explanation

    Reference section (bottom of sheet):
        - purpose: Why this table exists
        - assumptions: Key assumptions affecting interpretation
        - data_source: Where the data comes from
        - related_tables: Cross-references to related tables

    Table structure (optional - only needed when YAML drives data):
        - headers: Column headers
        - rows: Row data (can be omitted if Python generates the data)
    """
    table_name: str
    title: Optional[str] = None
    description: Optional[str] = None
    # Extended metadata for reference section
    purpose: Optional[str] = None
    assumptions: Optional[str] = None
    data_source: Optional[str] = None
    related_tables: Optional[List[str]] = None
    # Table structure (optional - only used when YAML drives table data)
    headers: Optional[List[str]] = None
    rows: Optional[List[Union[List[Any], Dict[str, Any]]]] = None


class SectionContent(BaseModel):
    """A section within a sheet (e.g., for Instructions)."""
    id: str
    title: str
    intro: Optional[str] = None
    content: Optional[List[str]] = None
    table: Optional[Union[TableDefinition, TableDocumentation]] = None
    source: Optional[str] = None  # Reference to global content file
    subsections: Optional[List['SectionContent']] = None
    source_citation: Optional[str] = None
    project: Optional[str] = None


class ContextBox(BaseModel):
    """A context/explanation box for calculation sheets."""
    title: str
    content: str  # Multi-line string (YAML | block)


class ColumnDescription(BaseModel):
    """Description of a column in a calculation sheet."""
    name: str
    description: str


class SheetContent(BaseModel):
    """Content structure for a sheet."""
    sheet_id: str
    title: str
    sections: Optional[List[SectionContent]] = None
    context_box: Optional[ContextBox] = None
    columns: Optional[Dict[str, str]] = None  # Column name -> description
    # NEW: Standardized tables dictionary with full documentation
    tables: Optional[Dict[str, TableDocumentation]] = None
    # LEGACY: Keep for backward compatibility during migration
    value_scenarios: Optional[Dict[str, Any]] = None
    model_scenarios: Optional[Dict[str, Any]] = None
    checks: Optional[Dict[str, Any]] = None
    navigation: Optional[List[Dict[str, str]]] = None
    kpis: Optional[List[Dict[str, Any]]] = None


# =============================================================================
# CONTENT LOADER
# =============================================================================

class ContentNotFoundError(Exception):
    """Raised when a required content file is not found."""
    pass


class ContentValidationError(Exception):
    """Raised when content fails schema validation."""
    pass


class ContentLoader:
    """
    Loads and validates content from YAML files.

    Usage:
        loader = ContentLoader()
        glossary = loader.get_glossary()
        instructions = loader.load_sheet_content("3_instructions")
    """

    def __init__(self, content_dir: Optional[Path] = None):
        """
        Initialize the content loader.

        Args:
            content_dir: Path to content directory. If None, uses sibling 'content/' folder.

        Raises:
            FileNotFoundError: If content directory does not exist.
        """
        if content_dir is None:
            self.base_dir = Path(__file__).parent / "content"
        else:
            self.base_dir = Path(content_dir)

        if not self.base_dir.exists():
            raise FileNotFoundError(
                f"FATAL: Content directory not found at {self.base_dir}\n"
                f"The content/ folder must exist alongside the generator script.\n"
                f"Run from: {Path(__file__).parent}"
            )

        self._cache: Dict[str, Any] = {}

    def _load_yaml(self, file_path: Path) -> Dict[str, Any]:
        """
        Load and parse a YAML file.

        Args:
            file_path: Path to the YAML file.

        Returns:
            Parsed YAML content as dict.

        Raises:
            ContentNotFoundError: If file does not exist.
            ContentValidationError: If YAML is malformed.
        """
        if not file_path.exists():
            raise ContentNotFoundError(
                f"Content file not found: {file_path}\n"
                f"Expected at: {file_path.resolve()}"
            )

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise ContentValidationError(
                f"Invalid YAML syntax in {file_path.name}:\n{e}"
            )

    def _validate(self, data: Dict, model: type, filename: str) -> BaseModel:
        """
        Validate data against a pydantic model.

        Args:
            data: Raw dict from YAML.
            model: Pydantic model class.
            filename: Source filename for error messages.

        Returns:
            Validated pydantic model instance.

        Raises:
            ContentValidationError: If validation fails.
        """
        try:
            return model(**data)
        except ValidationError as e:
            errors = []
            for err in e.errors():
                loc = " -> ".join(str(x) for x in err['loc'])
                errors.append(f"  {loc}: {err['msg']}")
            raise ContentValidationError(
                f"Schema validation failed for {filename}:\n" + "\n".join(errors)
            )

    # -------------------------------------------------------------------------
    # Global Content Loaders
    # -------------------------------------------------------------------------

    def load_global_content(self, name: str) -> Dict[str, Any]:
        """
        Load a global content file (glossary, data_sources, etc.).

        Args:
            name: Content name without extension (e.g., 'glossary').

        Returns:
            Parsed and cached content dict.
        """
        cache_key = f"global/{name}"
        if cache_key not in self._cache:
            file_path = self.base_dir / "global" / f"{name}.yaml"
            self._cache[cache_key] = self._load_yaml(file_path)
        return self._cache[cache_key]

    def get_glossary(self) -> List[GlossaryTerm]:
        """
        Get validated glossary terms.

        Returns:
            List of GlossaryTerm objects.
        """
        data = self.load_global_content("glossary")
        validated = self._validate(data, GlossaryContent, "glossary.yaml")
        return validated.terms

    def get_data_sources(self) -> List[Union[str, DataSource]]:
        """
        Get data source citations.

        Returns:
            List of citation strings or DataSource objects.
        """
        data = self.load_global_content("data_sources")
        validated = self._validate(data, DataSourcesContent, "data_sources.yaml")
        return validated.sources

    def get_change_log(self) -> List[ChangeLogEntry]:
        """
        Get change log entries.

        Returns:
            List of ChangeLogEntry objects.
        """
        data = self.load_global_content("change_log")
        validated = self._validate(data, ChangeLogContent, "change_log.yaml")
        return validated.entries

    # -------------------------------------------------------------------------
    # Sheet Content Loaders
    # -------------------------------------------------------------------------

    def load_sheet_content(self, sheet_id: str) -> SheetContent:
        """
        Load and validate content for a specific sheet.

        Args:
            sheet_id: Sheet identifier (e.g., '3_instructions', '12_calc_value').

        Returns:
            Validated SheetContent object.
        """
        cache_key = f"sheets/{sheet_id}"
        if cache_key not in self._cache:
            file_path = self.base_dir / "sheets" / f"{sheet_id.lower()}.yaml"
            data = self._load_yaml(file_path)
            self._cache[cache_key] = self._validate(data, SheetContent, f"{sheet_id}.yaml")
        return self._cache[cache_key]

    def get_context_box(self, sheet_id: str) -> Optional[ContextBox]:
        """
        Get the context box for a calculation sheet.

        Args:
            sheet_id: Sheet identifier.

        Returns:
            ContextBox if defined, None otherwise.
        """
        content = self.load_sheet_content(sheet_id)
        return content.context_box

    def get_column_descriptions(self, sheet_id: str) -> Dict[str, str]:
        """
        Get column descriptions for a sheet.

        Args:
            sheet_id: Sheet identifier.

        Returns:
            Dict mapping column names to descriptions.
        """
        content = self.load_sheet_content(sheet_id)
        return content.columns or {}

    def get_section(self, sheet_id: str, section_id: str) -> SectionContent:
        """
        Get a specific section from a sheet's content.

        Args:
            sheet_id: Sheet identifier.
            section_id: Section ID within the sheet.

        Returns:
            SectionContent object.

        Raises:
            ContentNotFoundError: If section not found.
        """
        content = self.load_sheet_content(sheet_id)
        if content.sections:
            for section in content.sections:
                if section.id == section_id:
                    return section
        raise ContentNotFoundError(
            f"Section '{section_id}' not found in {sheet_id}.yaml"
        )

    def get_table_docs(self, sheet_id: str) -> Dict[str, TableDocumentation]:
        """
        Get all table documentation for a sheet.

        Args:
            sheet_id: Sheet identifier.

        Returns:
            Dict mapping table keys to TableDocumentation objects.
        """
        content = self.load_sheet_content(sheet_id)
        return content.tables or {}

    def get_table_doc(self, sheet_id: str, table_key: str) -> TableDocumentation:
        """
        Get documentation for a specific table.

        Args:
            sheet_id: Sheet identifier.
            table_key: Table key within the tables dict.

        Returns:
            TableDocumentation object.

        Raises:
            ContentNotFoundError: If table not found.
        """
        tables = self.get_table_docs(sheet_id)
        if table_key in tables:
            return tables[table_key]
        raise ContentNotFoundError(
            f"Table '{table_key}' not found in {sheet_id}.yaml"
        )

    # -------------------------------------------------------------------------
    # Validation
    # -------------------------------------------------------------------------

    def validate_all(self) -> bool:
        """
        Validate all content files exist and are parseable.

        Call this before starting workbook generation to fail fast.

        Returns:
            True if all content is valid.

        Raises:
            ContentNotFoundError: If any required file is missing.
            ContentValidationError: If any file fails validation.
        """
        # Required global files
        required_global = ['glossary', 'data_sources', 'change_log']
        for name in required_global:
            self.load_global_content(name)

        # Required sheet files (renumbered per Phase 0 migration)
        required_sheets = [
            '0_cover', '1_toc', '3_instructions', '4_assumptions', '6_scenarios', '7_servicemodels',
            '8_calc_timeline', '10_calc_stochastic', '12_calc_value', '13_calc_costs',
            '14_calc_sim', '15_pl_monthly', '16_pl_annual', '17_cashflow',
            '18_uniteconomics', '19_sensitivity', '20_dashboard', '21_checks'
        ]
        for sheet_id in required_sheets:
            self.load_sheet_content(sheet_id)

        return True

    def clear_cache(self):
        """Clear the content cache (useful for testing)."""
        self._cache.clear()


# =============================================================================
# MODULE-LEVEL INSTANCE
# =============================================================================

# Create a default loader instance for convenience
# This will be initialized when the module is imported
_default_loader: Optional[ContentLoader] = None


def get_loader() -> ContentLoader:
    """
    Get the default ContentLoader instance.

    Returns:
        ContentLoader instance, creating one if needed.
    """
    global _default_loader
    if _default_loader is None:
        _default_loader = ContentLoader()
    return _default_loader


if __name__ == "__main__":
    # Quick validation when run directly
    print(f"Content directory: {Path(__file__).parent / 'content'}")
    try:
        loader = ContentLoader()
        loader.validate_all()
        print("All content files validated successfully!")
    except (ContentNotFoundError, ContentValidationError) as e:
        print(f"Validation failed:\n{e}")
