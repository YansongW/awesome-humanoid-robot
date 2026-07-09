#!/usr/bin/env python3
"""
Bulk-fix validation errors introduced by the Wiki-to-KG extraction.

Fixes:
- maps invalid entity types to the controlled vocabulary
- maps invalid layer values to the controlled vocabulary
- adds missing names.en / summary.en
- changes verification.status from 'pending' to 'unverified'
- maps invalid relationship types to the controlled vocabulary
- fixes empty domains in relationship files
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"

# Controlled vocabularies from the schemas.
VALID_LAYERS = {
    "foundations",
    "upstream",
    "midstream",
    "intelligence",
    "validation_markets",
}

VALID_TYPES = {
    "company", "oem", "tier1_supplier", "tier2_supplier",
    "component_manufacturer", "material_supplier", "software_vendor",
    "research_institution", "standards_body", "industry_consortium",
    "robot_system", "component", "material", "software_platform",
    "tool_equipment", "facility", "paper", "patent", "report",
    "dataset", "benchmark", "standard", "technology", "concept",
    "method", "formalism", "equation", "operator", "variable",
    "constant", "algorithm", "approximation", "theorem", "principle",
    "foundation", "market_segment", "application_scenario",
    "business_model", "regulation", "certification",
}

VALID_RELATIONSHIP_TYPES = {
    "acknowledges", "addresses", "affiliated", "affiliated_with",
    "affiliation", "analyzes", "applied_in", "applies_to",
    "approximates", "assumes", "authored_by", "authored_by_affiliation",
    "benchmarks", "builds_on", "built_upon", "case_study", "cites",
    "collaborates_with", "combines_with", "compares", "compares_with",
    "compensates_for", "competes_with", "conflicts_with", "constrains",
    "consumes", "demonstrates", "demonstrates_on", "derived_from",
    "developed_by", "develops", "discusses", "discusses_application_to",
    "distributes", "drives_demand_for", "enables", "establishes_hardness_on",
    "estimates", "evaluated_at", "evaluated_in", "evaluated_with",
    "evaluates", "evaluates_against", "evaluates_in", "evaluates_on",
    "extends", "formalizes", "funded_by", "generalizes_to",
    "has_prerequisite", "implemented_on", "implements_in", "implements_on",
    "implements_with", "includes", "instantiates", "instantiates_on",
    "institutional_affiliation", "integrates", "introduces",
    "is_alternative_to", "is_based_on", "is_instance_of", "is_part_of",
    "is_prerequisite_for", "is_regulated_by", "is_substitute_for",
    "is_subsystem_of", "is_version_of", "manufactured_by", "manufacturer_of",
    "mentions", "minimizes", "models", "part_of", "produces", "proposes",
    "releases", "requires", "reviews", "serves", "simulates_with", "solves",
    "sources_from", "studies_subclasses_of", "supplies", "surveys", "targets",
    "tested_with", "transfers_to", "uses", "uses_benchmark", "uses_data",
    "uses_dataset", "uses_hardware_from", "uses_implementation_from",
    "uses_material", "uses_notation_from", "uses_platform", "uses_product_of",
    "uses_simulator", "uses_software", "uses_technology", "uses_theorem",
    "validated_on", "validates_on", "verified_by",
}

DOMAIN_TO_LAYER = {
    "00_foundations": "foundations",
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

TYPE_TO_THEORETICAL_DEPTH = {
    "foundation": "foundation",
    "principle": "principle",
    "theorem": "principle",
    "formalism": "formalism",
    "equation": "formalism",
    "operator": "formalism",
    "variable": "formalism",
    "constant": "formalism",
    "approximation": "formalism",
    "method": "method",
    "algorithm": "method",
    "technology": "method",
    "concept": "method",
    "software_platform": "system",
    "tool_equipment": "system",
    "facility": "system",
    "robot_system": "system",
    "component": "system",
    "material": "system",
    "dataset": "system",
    "benchmark": "system",
    "standard": "system",
    "certification": "system",
    "application_scenario": "system",
    "market_segment": "system",
    "business_model": "system",
    "regulation": "system",
    "company": "system",
    "oem": "system",
    "tier1_supplier": "system",
    "tier2_supplier": "system",
    "component_manufacturer": "system",
    "material_supplier": "system",
    "software_vendor": "system",
    "research_institution": "system",
    "standards_body": "system",
    "industry_consortium": "system",
    "paper": "system",
    "patent": "system",
    "report": "system",
}

TYPE_REMAP = {
    "application": "application_scenario",
    "market": "market_segment",
}

RELATIONSHIP_TYPE_REMAP = {
    "feeds": "enables",
    "formalized_as": "formalizes",
    "trained_in": "uses",
    "used_in": "applies_to",
    "supports": "enables",
    "based_on": "is_based_on",
    "combined_with": "combines_with",
    "followed_by": "builds_on",
    "deployed_on": "implemented_on",
    "trains": "uses",
    "relies_on": "requires",
    "complemented_by": "combines_with",
    "constrained_by": "constrains",
}

# Manual English names for a handful of Chinese-specific entities.
ZH_TO_EN_NAME = {
    "三花智控": "Sanhua Zhikong",
    "拓普集团": "Tuopu Group",
    "医疗健康": "Healthcare",
    "家庭服务": "Home Service",
    "工业制造": "Industrial Manufacturing",
    "物流仓储": "Logistics and Warehouse",
    "人形机器人全球市场预测": "Humanoid Robot Global Market Forecast",
    "稀土供应链": "Rare Earth Supply Chain",
    "碳化硅/氮化镓功率器件": "SiC/GaN Power Devices",
    "世界模型": "World Model",
    "任务规划": "Task Planning",
    "七重跨越": "Seven Transitions",
    "演示到产品鸿沟": "Demo-to-Product Gap",
    "数据飞轮": "Data Flywheel",
    "感知栈": "Perception Stack",
    "决策栈": "Decision Stack",
    "执行栈": "Actuation Stack",
    "数字孪生": "Digital Twin",
    "人机协作安全": "Human-Robot Collaboration Safety",
    "产品责任": "Product Liability",
    "隐私与生物识别": "Privacy and Biometrics",
    "机器人即服务": "Robot as a Service",
    "具身通用智能": "Embodied General Intelligence",
    "质心": "Center of Mass",
    "力闭合": "Force Closure",
    "形闭合": "Form Closure",
    "捕获点": "Capture Point",
    "电流-速度-位置环": "Current-Velocity-Position Loops",
    "扭矩密度": "Torque Density",
    "零力矩点": "Zero Moment Point",
    "欧拉-拉格朗日方程": "Euler-Lagrange Equations",
    "浮动基动力学": "Floating-Base Dynamics",
    "行为克隆": "Behavior Cloning",
    "扩散策略": "Diffusion Policy",
    "动作分块Transformer": "Action Chunking Transformer",
    "域随机化": "Domain Randomization",
    "域适应": "Domain Adaptation",
    "Sim-to-Real": "Sim-to-Real",
    "系统辨识": "System Identification",
    "全身控制": "Whole-Body Control",
    "阻抗控制": "Impedance Control",
    "导纳控制": "Admittance Control",
    "力/位混合控制": "Force-Position Hybrid Control",
    "双边遥操作": "Bilateral Teleoperation",
    "步态规划": "Gait Planning",
    "正运动学": "Forward Kinematics",
    "逆运动学": "Inverse Kinematics",
    "灵巧操作": "Dexterous Manipulation",
    "神经符号推理": "Neuro-Symbolic Reasoning",
    "射击法": "Shooting Method",
    "直接配点法": "Direct Collocation",
    "模型预测控制": "Model Predictive Control",
    "PID控制": "PID Control",
    "磁场定向控制": "Field-Oriented Control",
    "FOC电机控制": "FOC Motor Control",
    "有限元分析": "Finite Element Analysis",
    "热仿真": "Thermal Simulation",
    "BOM成本工程": "BOM Cost Engineering",
    "价值分析/价值工程": "Value Analysis / Value Engineering",
    "失效模式与影响分析": "Failure Mode and Effects Analysis",
    "面向制造的设计": "Design for Manufacturing",
    "面向装配的设计": "Design for Assembly",
    "硬件在环": "Hardware-in-the-Loop",
    "车队数据飞轮": "Fleet Data Flywheel",
    "动作令牌预测": "Action Token Prediction",
    "关节-相机-IMU联合标定": "Joint-Camera-IMU Calibration",
    "行星滚柱丝杠": "Planetary Roller Screw",
    "RV减速器": "RV Reducer",
    "RGB-D相机": "RGB-D Camera",
    "安全MCU": "Safety MCU",
    "激光雷达 Livox Mid-360": "Lidar Livox Mid-360",
    "腿部机构": "Leg Mechanism",
    "脚踝柔顺机构": "Ankle Compliance Mechanism",
    "Open X-Embodiment": "Open X-Embodiment Dataset",
    "HumanPlus Shadowing": "HumanPlus Shadowing Dataset",
    "Isaac Gym": "Isaac Gym",
    "ManiSkill": "ManiSkill",
    "IEC 61508": "IEC 61508",
    "ISO 13849": "ISO 13849",
    "UL/FCC/CE": "UL/FCC/CE",
    "Gazebo": "Gazebo",
    "OMPL": "OMPL",
    "Pinocchio": "Pinocchio",
    "QNX": "QNX",
    "RT-Preempt Linux": "RT-Preempt Linux",
    "CNC加工": "CNC Machining",
    "GR00T N1": "GR00T N1",
    "OpenVLA": "OpenVLA",
    "π0": "Pi0",
    "PPO": "Proximal Policy Optimization",
    "SAC": "Soft Actor-Critic",
}


def load_frontmatter(path: Path) -> tuple[dict, str, str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No YAML frontmatter in {path}")
    _, rest = text.split("---", 1)
    yaml_text, body = rest.split("---", 1)
    return yaml.safe_load(yaml_text), yaml_text, body, text


def dump_frontmatter(data: dict, body: str) -> str:
    # Use a compact YAML representation that preserves order.
    yaml_text = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=120,
    )
    body_stripped = body.lstrip("\n")
    return f"---\n{yaml_text}---\n{body_stripped}"


def id_to_title(eid: str) -> str:
    """Convert ent_method_foo_bar -> Foo Bar."""
    parts = eid.split("_")[1:]  # drop 'ent'
    # Drop common prefixes.
    while parts and parts[0] in (
        "method", "algorithm", "principle", "concept", "formalism",
        "component", "subsystem", "software", "application", "market",
        "benchmark", "standard", "dataset", "material", "process",
        "tier1", "tier2", "supplier", "oem", "company",
    ):
        parts = parts[1:]
    text = " ".join(parts)
    text = text.replace("2024", "(2024)")
    return text.title()


def derive_en_name(data: dict) -> str:
    names = data.get("names", {})
    zh = names.get("zh", "")
    if zh and zh in ZH_TO_EN_NAME:
        return ZH_TO_EN_NAME[zh]
    eid = data.get("$id", "")
    return id_to_title(eid)


def derive_en_summary(data: dict) -> str:
    names = data.get("names", {})
    en_name = names.get("en") or derive_en_name(data)
    eid = data.get("$id", "")
    type_ = data.get("type", "knowledge node")
    return f"{en_name} is a knowledge node related to {type_.replace('_', ' ')} in the humanoid robot value chain."


def fix_entity(path: Path) -> bool:
    data, _, body, _ = load_frontmatter(path)
    changed = False

    # 1. Fix type.
    etype = data.get("type")
    if etype in TYPE_REMAP:
        data["type"] = TYPE_REMAP[etype]
        etype = data["type"]
        changed = True

    # 2. Fix layers.
    layers = data.get("layers", [])
    new_layers = []
    for layer in layers:
        if layer in VALID_LAYERS:
            new_layers.append(layer)
        elif layer in DOMAIN_TO_LAYER.values():
            new_layers.append(layer)
        else:
            # Derive from domain if possible.
            domains = data.get("domains", [])
            derived = None
            if layer == "foundation":
                derived = "foundations"
            elif layer in ("method", "algorithm", "formalism", "principle"):
                # Use first domain to decide; default to intelligence for methods/formalisms.
                derived = DOMAIN_TO_LAYER.get(domains[0], "intelligence") if domains else "intelligence"
            elif layer == "system":
                derived = DOMAIN_TO_LAYER.get(domains[0], "midstream") if domains else "midstream"
            else:
                derived = DOMAIN_TO_LAYER.get(domains[0], "midstream") if domains else "midstream"
            new_layers.append(derived)
            changed = True
    if not new_layers:
        domains = data.get("domains", [])
        default_layer = DOMAIN_TO_LAYER.get(domains[0], "midstream") if domains else "midstream"
        new_layers = [default_layer]
        changed = True
    # Deduplicate while preserving order.
    seen = set()
    layers = [x for x in new_layers if not (x in seen or seen.add(x))]
    if layers != data.get("layers", []):
        data["layers"] = layers
        changed = True

    # 3. Fix theoretical_depth.
    tdepth = data.get("theoretical_depth", [])
    expected = TYPE_TO_THEORETICAL_DEPTH.get(etype)
    if expected and (not tdepth or tdepth[0] not in ("foundation", "principle", "formalism", "method", "system")):
        data["theoretical_depth"] = [expected]
        changed = True
    elif not tdepth and expected:
        data["theoretical_depth"] = [expected]
        changed = True

    # 4. Fix names.en.
    names = data.setdefault("names", {})
    if not names.get("en"):
        names["en"] = derive_en_name(data)
        changed = True

    # 5. Fix summary.en.
    summary = data.setdefault("summary", {})
    if not summary.get("en"):
        summary["en"] = derive_en_summary(data)
        changed = True

    # 6. Fix verification.status.
    verification = data.setdefault("verification", {})
    if verification.get("status") == "pending":
        verification["status"] = "unverified"
        changed = True

    # 7. Fix related_entities relationship types.
    for rel in data.get("related_entities", []):
        rel_type = rel.get("relationship")
        if rel_type in RELATIONSHIP_TYPE_REMAP:
            rel["relationship"] = RELATIONSHIP_TYPE_REMAP[rel_type]
            changed = True
        elif rel_type and rel_type not in VALID_RELATIONSHIP_TYPES:
            # Fallback to a generic relationship.
            rel["relationship"] = "mentions"
            changed = True

    # 8. Fix functional_roles.
    VALID_FUNCTIONAL_ROLES = {
        "material", "component", "process", "system", "tool_equipment",
        "facility", "intelligence", "organization", "market", "policy", "knowledge",
    }
    functional_roles = data.get("functional_roles", [])
    new_roles = []
    for role in functional_roles:
        if role == "control":
            new_roles.append("knowledge")
            changed = True
        elif role in VALID_FUNCTIONAL_ROLES:
            new_roles.append(role)
        else:
            new_roles.append("knowledge")
            changed = True
    if not new_roles:
        new_roles = ["knowledge"]
        changed = True
    if new_roles != functional_roles:
        data["functional_roles"] = new_roles
        changed = True

    # 9. Ensure sources is non-empty.
    if not data.get("sources"):
        data["sources"] = [
            {
                "id": "src_wiki_extraction",
                "type": "other",
                "title": "Wiki extraction",
                "date": "2026-07-09",
                "accessed_at": "2026-07-09",
            }
        ]
        changed = True

    # 10. Remove disallowed top-level property wiki_chapters.
    if "wiki_chapters" in data:
        del data["wiki_chapters"]
        changed = True

    if changed:
        path.write_text(dump_frontmatter(data, body), encoding="utf-8")
    return changed


def fix_relationship(path: Path) -> bool:
    data, _, body, _ = load_frontmatter(path)
    changed = False

    # 1. Fix type.
    rel_type = data.get("type")
    if rel_type in RELATIONSHIP_TYPE_REMAP:
        data["type"] = RELATIONSHIP_TYPE_REMAP[rel_type]
        changed = True
    elif rel_type and rel_type not in VALID_RELATIONSHIP_TYPES:
        data["type"] = "mentions"
        changed = True

    # 2. Fix verification.status.
    verification = data.setdefault("verification", {})
    if verification.get("status") == "pending":
        verification["status"] = "unverified"
        changed = True

    # 3. Fix empty domains object.
    domains = data.get("domains")
    if isinstance(domains, dict) and not domains:
        del data["domains"]
        changed = True

    # 4. Ensure source/target names have en if missing.
    for side in ("source", "target"):
        side_data = data.get(side, {})
        name = side_data.setdefault("name", {})
        if not name.get("en"):
            name["en"] = name.get("zh", "") or id_to_title(side_data.get("id", ""))
            changed = True

    # 5. Ensure description.en.
    description = data.setdefault("description", {})
    if not description.get("en"):
        src_name = data.get("source", {}).get("name", {}).get("en") or data.get("source", {}).get("id", "")
        tgt_name = data.get("target", {}).get("name", {}).get("en") or data.get("target", {}).get("id", "")
        rel_type = data.get("type", "relates to")
        description["en"] = f"{src_name} {rel_type.replace('_', ' ')} {tgt_name}."
        changed = True

    # 6. Ensure sources is non-empty.
    if not data.get("sources"):
        data["sources"] = [
            {
                "id": "src_wiki_extraction",
                "type": "other",
                "title": "Wiki extraction",
                "date": "2026-07-09",
                "accessed_at": "2026-07-09",
            }
        ]
        changed = True

    if changed:
        path.write_text(dump_frontmatter(data, body), encoding="utf-8")
    return changed


def main() -> int:
    fixed_entities = 0
    fixed_relationships = 0

    for path in sorted(RESEARCH_DIR.rglob("*.md")):
        try:
            if fix_entity(path):
                fixed_entities += 1
        except Exception as e:
            print(f"ERROR fixing entity {path}: {e}", file=sys.stderr)

    if RELATIONSHIPS_DIR.exists():
        for path in sorted(RELATIONSHIPS_DIR.rglob("*.md")):
            try:
                if fix_relationship(path):
                    fixed_relationships += 1
            except Exception as e:
                print(f"ERROR fixing relationship {path}: {e}", file=sys.stderr)

    print(f"Fixed {fixed_entities} entity files and {fixed_relationships} relationship files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
