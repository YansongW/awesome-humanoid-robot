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
    "market_segment": "companies",
    "application_scenario": "companies",
    "business_model": "companies",
    "regulation": "companies",
    "certification": "benchmarks",
}
