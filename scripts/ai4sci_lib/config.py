"""Configuration for the AI4Sci literature pipeline."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"
SCHEMA_DIR = ROOT / "data" / "schema" / "v1"
STAGING_DIR = ROOT / ".staging"
STAGING_RESEARCH_DIR = STAGING_DIR / "research"
STAGING_RELATIONSHIPS_DIR = STAGING_DIR / "data" / "relationships"
STAGING_REVIEW_DIR = STAGING_DIR / "review"
STAGING_REJECTED_DIR = STAGING_DIR / "rejected"
WORKSTREAMS_DIR = ROOT / "scripts" / "ai4sci_workstreams"

DEFAULT_LLM_MODEL = os.getenv("AI4SCI_MODEL", "kimi-latest")
DEFAULT_LLM_BASE_URL = os.getenv("AI4SCI_BASE_URL", "https://api.moonshot.cn/v1")
DEFAULT_LLM_API_KEY = os.getenv("AI4SCI_API_KEY") or os.getenv("OPENAI_API_KEY")

HUMANOID_KEYWORDS = [
    "humanoid",
    "bipedal",
    "biped",
    "loco-manipulation",
    "locomanipulation",
    "whole-body",
    "whole body",
    "human-like robot",
    "embodied ai",
    "embodied intelligence",
    "robot mass production",
    "robot manufacturing",
    "actuator",
    "reducer",
    "harmonic drive",
    "planetary roller screw",
    "servo motor",
    "torque density",
    "rare earth",
    "neodymium",
    "supply chain",
    "bill of materials",
    "vla",
    "vision-language-action",
    "world model",
    "world action model",
    "sim-to-real",
    "humanoid benchmark",
]

DOMAIN_MAP = {
    "raw material": "01_raw_materials",
    "component": "02_components",
    "manufacturing": "03_manufacturing_processes",
    "assembly": "04_assembly_integration_testing",
    "mass production": "05_mass_production",
    "design": "06_design_engineering",
    "ai model": "07_ai_models_algorithms",
    "software": "08_software_middleware",
    "dataset": "09_data_datasets",
    "benchmark": "10_evaluation_benchmarks",
    "application": "11_applications_markets",
    "policy": "12_policy_regulation_ethics",
}

LAYER_MAP = {
    "01_raw_materials": "upstream",
    "02_components": "upstream",
    "03_manufacturing_processes": "upstream",
    "04_assembly_integration_testing": "midstream",
    "05_mass_production": "midstream",
    "06_design_engineering": "midstream",
    "07_ai_models_algorithms": "intelligence",
    "08_software_middleware": "intelligence",
    "09_data_datasets": "intelligence",
    "10_evaluation_benchmarks": "validation_markets",
    "11_applications_markets": "validation_markets",
    "12_policy_regulation_ethics": "validation_markets",
}

# Theoretical-depth axis used for cross-layer knowledge-chain validation.
# Ordered from most concrete/system-level to most abstract/foundational.
THEORETICAL_DEPTH_ORDER = ["system", "method", "formalism", "principle", "foundation"]

# Allowed relationship types between theoretical-depth levels.
# These are directional from source depth to target depth.
CROSS_LAYER_RELATIONSHIPS: dict[tuple[str, str], list[str]] = {
    # System -> method
    ("system", "method"): ["requires", "uses", "enables", "instantiates", "integrates", "is_based_on", "constrains", "produces"],
    # System -> formalism
    ("system", "formalism"): ["requires", "uses", "formalizes", "is_based_on"],
    # System -> component/material
    ("system", "component"): ["integrates", "requires", "uses", "produces"],
    ("system", "material"): ["requires", "consumes", "uses"],
    # Method -> system (e.g. a technology enables a robot)
    ("method", "system"): ["enables", "requires", "produces", "constrains", "integrates", "instantiates", "addresses", "uses_dataset"],
    # Method -> method
    ("method", "method"): ["builds_on", "is_based_on", "extends", "uses", "instantiates", "is_alternative_to"],
    # Method -> formalism
    ("method", "formalism"): ["formalizes", "uses", "requires", "is_based_on", "solves"],
    # Method -> algorithm
    ("method", "algorithm"): ["uses", "solves", "instantiates", "requires"],
    # Method -> foundation
    ("method", "foundation"): ["has_prerequisite", "is_based_on", "derived_from"],
    # Formalism -> equation
    ("formalism", "equation"): ["includes", "uses", "formalizes"],
    # Formalism -> algorithm
    ("formalism", "algorithm"): ["solves", "uses", "requires"],
    # Formalism -> foundation
    ("formalism", "foundation"): ["has_prerequisite", "is_based_on", "derived_from"],
    # Equation -> operator/variable/constant
    ("equation", "operator"): ["uses"],
    ("equation", "variable"): ["uses"],
    ("equation", "constant"): ["uses"],
    # Equation -> principle
    ("equation", "principle"): ["derived_from", "is_based_on"],
    # Formalism -> principle
    ("formalism", "principle"): ["derived_from", "is_based_on"],
    # Principle -> foundation
    ("principle", "foundation"): ["has_prerequisite", "derived_from", "is_based_on"],
    # Algorithm -> algorithm
    ("algorithm", "algorithm"): ["builds_on", "is_based_on", "extends", "uses", "instantiates"],
    # Algorithm -> formalism
    ("algorithm", "formalism"): ["is_based_on", "uses", "requires"],
    # Algorithm -> principle/foundation
    ("algorithm", "principle"): ["is_based_on", "derived_from"],
    ("algorithm", "foundation"): ["has_prerequisite"],
    # Component -> material
    ("component", "material"): ["requires", "consumes", "uses", "sources_from"],
    # Component -> component
    ("component", "component"): ["is_part_of", "is_subsystem_of", "integrates", "requires", "uses"],
    # Material -> material
    ("material", "material"): ["is_part_of", "sources_from", "is_substitute_for"],
    # Generic same-depth links
    ("system", "system"): ["is_part_of", "is_subsystem_of", "integrates", "enables", "requires", "constrains", "is_alternative_to"],
    ("foundation", "foundation"): ["has_prerequisite", "is_based_on", "derived_from"],
    ("principle", "principle"): ["derived_from", "is_based_on", "has_prerequisite"],
}

TYPE_TO_SUBDIR = {
    "paper": "papers",
    "dataset": "datasets",
    "benchmark": "benchmarks",
    "technology": "technologies",
    "component": "components",
    "material": "materials",
    "company": "companies",
    "oem": "companies",
    "tier1_supplier": "companies",
    "tier2_supplier": "companies",
    "component_manufacturer": "companies",
    "material_supplier": "companies",
    "software_vendor": "companies",
    "research_institution": "companies",
    "standards_body": "companies",
    "industry_consortium": "companies",
    "robot_system": "components",
    "software_platform": "technologies",
    "tool_equipment": "technologies",
    "facility": "technologies",
    "patent": "papers",
    "report": "papers",
    "standard": "benchmarks",
    "concept": "papers",
    "method": "methods",
    "formalism": "formalisms",
    "equation": "equations",
    "operator": "operators",
    "variable": "operators",
    "constant": "operators",
    "algorithm": "methods",
    "approximation": "methods",
    "theorem": "principles",
    "principle": "principles",
    "foundation": "foundations",
    "market_segment": "companies",
    "application_scenario": "companies",
    "business_model": "companies",
    "regulation": "companies",
    "certification": "benchmarks",
}
