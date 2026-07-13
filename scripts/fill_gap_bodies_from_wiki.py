#!/usr/bin/env python3
"""
Fill gap entity bodies with relevant sections from the project Wiki.

The Wiki chapters are in Chinese, so extracted bodies are Chinese-only for now.
The website loader already filters body sections by language, so English/Korean
pages will still show only the English/Korean summary while Chinese pages get
the richer Wiki-derived content.

Usage:
    python scripts/fill_gap_bodies_from_wiki.py
"""

import re
import sys
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).parent.parent
MAPPING_PATH = ROOT / "data" / "wiki-chapter-mapping.yaml"
WIKI_DIR = ROOT / "wiki" / "docs" / "chapters"

# Extra search keywords (Chinese) for entities whose chapter name differs
# from the heading text.  The first keyword is tried first.
EXTRA_KEYWORDS = {
    "ent_concept_demo_to_product_gap": ["演示", "产品指标", "鸿沟", "产品型机器人"],
    "ent_concept_seven_transitions": ["七个跃迁", "从 0 到 1", "七阶跃迁"],
    "ent_material_rare_earth_supply": ["稀土", "钕", "镝", "铽"],
    "ent_material_sic_gan_power_devices": ["SiC", "GaN", "碳化硅", "氮化镓", "宽禁带"],
    "ent_component_rv_reducer": ["摆线减速器", "RV 减速器", "RV减速器", "摆线"],
    "ent_component_planetary_roller_screw": ["滚柱丝杠", "行星滚柱", "滚珠丝杠"],
    "ent_principle_current_velocity_position_loops": ["电流环", "速度环", "位置环", "级联控制"],
    "ent_metric_torque_density": ["扭矩密度", "转矩密度", "功率密度"],
    "ent_component_rgbd_camera": ["RGB-D", "深度相机", "深度感知"],
    "ent_component_lidar_livox_mid360": ["激光雷达", "LiDAR", "固态激光雷达"],
    "ent_component_safety_mcu": ["安全 MCU", "功能安全", "安全微控制器"],
    "ent_method_thermal_simulation": ["热仿真", "热分析", "热网络"],
    "ent_tier1_supplier_sanhuazhikong": ["三花"],
    "ent_tier1_supplier_tuopujituan": ["拓普"],
    "ent_principle_zero_moment_point": ["零力矩点", "ZMP"],
    "ent_principle_center_of_mass": ["质心", "COM", "质心动量"],
    "ent_method_forward_kinematics": ["正运动学", "DH 参数", "Denavit-Hartenberg"],
    "ent_method_inverse_kinematics": ["逆运动学", "Jacobian", "雅可比"],
    "ent_formalism_floating_base_dynamics": ["浮动基", "浮动基动力学"],
    "ent_method_fea_finite_element_analysis": ["有限元", "FEA", "有限元分析"],
    "ent_subsystem_leg_mechanism": ["腿部机构", "腿设计", "下肢"],
    "ent_subsystem_ankle_compliance": ["脚踝", "踝", "柔顺", "足"],
    "ent_process_cnc_machining": ["CNC", "机加工", "数控加工"],
    "ent_method_design_for_manufacturing": ["可制造性设计", "DFM"],
    "ent_method_design_for_assembly": ["可装配性设计", "DFA"],
    "ent_method_hardware_in_the_loop": ["硬件在环", "HIL"],
    "ent_method_calibration_joint_camera_imu": ["联合标定", "标定", "相机标定"],
    "ent_standard_iec_61508": ["IEC 61508", "功能安全"],
    "ent_standard_iso_13849": ["ISO 13849", "控制系统安全"],
    "ent_standard_ul_fcc_ce": ["UL", "FCC", "CE", "准入认证"],
    "ent_method_bom_cost_engineering": ["BOM", "物料清单", "成本"],
    "ent_method_value_analysis_value_engineering": ["价值工程", "VA/VE", "价值分析"],
    "ent_method_fmea": ["失效模式", "FMEA", "失效模式与影响分析"],
    "ent_method_pid_control": ["PID", "PI 控制", "比例积分微分"],
    "ent_method_impedance_control": ["阻抗控制", "导纳控制"],
    "ent_method_admittance_control": ["导纳控制", "阻抗控制"],
    "ent_method_force_position_hybrid_control": ["力位混合", "力/位置", "力位"],
    "ent_method_model_predictive_control": ["模型预测控制", "MPC"],
    "ent_method_whole_body_control": ["全身控制", "WBC", "Whole-Body"],
    "ent_formalism_euler_lagrange_equations": ["欧拉-拉格朗日", "Euler-Lagrange", "拉格朗日"],
    "ent_method_gait_planning": ["步态规划", "步态"],
    "ent_principle_capture_point": ["捕获点", "Capture Point"],
    "ent_method_direct_collocation": ["直接配点", "配点法", "collocation"],
    "ent_method_shooting_method": ["打靶法", "Shooting"],
    "ent_algorithm_ppo": ["PPO", "近端策略优化"],
    "ent_algorithm_sac": ["SAC", "软演员-评论家"],
    "ent_method_sim_to_real": ["Sim-to-Real", "仿真到真实", "域随机化"],
    "ent_principle_force_closure": ["力闭合", "力闭合条件"],
    "ent_principle_form_closure": ["形闭合", "形闭合条件"],
    "ent_software_ompl": ["OMPL", "运动规划库"],
    "ent_method_dexterous_manipulation": ["灵巧操作", "灵巧手", "多指操作"],
    "ent_method_bilateral_teleoperation": ["双边遥操作", "遥操作", "主从"],
    "ent_concept_human_robot_collaboration_safety": ["人机协作", "协作安全", "HRC"],
    "ent_method_behavior_cloning": ["行为克隆", "Behavior Cloning"],
    "ent_method_diffusion_policy": ["扩散策略", "Diffusion Policy"],
    "ent_method_action_chunking_transformer": ["ACT", "Action Chunking", "动作分块"],
    "ent_method_domain_randomization": ["域随机化", "Domain Randomization"],
    "ent_method_domain_adaptation": ["域适应", "Domain Adaptation"],
    "ent_method_system_identification": ["系统辨识", "System Identification"],
    "ent_method_openvla": ["OpenVLA"],
    "ent_method_gr00t_n1": ["GR00T", "GR00T N1"],
    "ent_method_pi0": ["π0", "Pi Zero", "pi0"],
    "ent_dataset_open_x_embodiment": ["Open X-Embodiment", "X-Embodiment"],
    "ent_concept_world_model": ["世界模型", "World Model"],
    "ent_method_task_planning": ["任务规划", "Task Planning"],
    "ent_method_neuro_symbolic_reasoning": ["神经符号", "符号-神经", "Neuro-Symbolic"],
    "ent_dataset_humanplus_shadowing": ["HumanPlus", "Shadowing"],
    "ent_method_fleet_data_flywheel": ["数据飞轮", "车队数据", "fleet data"],
    "ent_software_rt_preempt_linux": ["RT-PREEMPT", "实时 Linux"],
    "ent_software_qnx": ["QNX"],
    "ent_software_pinocchio": ["Pinocchio"],
    "ent_software_gazebo": ["Gazebo"],
    "ent_concept_digital_twin": ["数字孪生", "Digital Twin"],
    "ent_concept_perception_stack": ["感知栈", "感知系统"],
    "ent_concept_decision_stack": ["决策栈", "决策系统"],
    "ent_concept_actuation_stack": ["执行栈", "执行系统"],
    "ent_benchmark_maniskill": ["ManiSkill"],
    "ent_benchmark_isaac_gym": ["Isaac Gym"],
    "ent_application_industrial_manufacturing": ["工业制造", "工厂"],
    "ent_application_logistics_warehouse": ["物流", "仓储", "仓库"],
    "ent_application_healthcare": ["医疗", "健康", "康养"],
    "ent_application_home_service": ["家庭服务", "家用", "服务机器人"],
    "ent_market_humanoid_global_forecast": ["市场", "预测", "规模"],
    "ent_concept_robot_as_a_service": ["RaaS", "Robot-as-a-Service", "即服务"],
    "ent_concept_product_liability": ["产品责任", "责任"],
    "ent_concept_privacy_biometrics": ["隐私", "生物识别", "人脸", "声纹"],
    "ent_concept_embodied_general_intelligence": ["具身通用智能", "具身智能", "通用智能"],
    "ent_concept_data_flywheel": ["数据飞轮", "飞轮"],
}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    _, rest = text.split("---", 1)
    yaml_text, body = rest.split("---", 1)
    return yaml_text, body


def parse_chapter(path: Path) -> list[tuple[int, str, str]]:
    """Return list of (level, heading, content) sections."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    sections: list[tuple[int, str, str]] = []
    current_level = 0
    current_heading = ""
    current_lines: list[str] = []

    def flush():
        if current_heading:
            sections.append((current_level, current_heading, "\n".join(current_lines).strip()))

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            current_level = len(m.group(1))
            current_heading = m.group(2)
            current_lines = []
        else:
            current_lines.append(line)
    flush()
    return sections


def score_section(section: tuple[int, str, str], keywords: list[str]) -> int:
    level, heading, content = section
    heading_norm = heading.lower()
    content_norm = content.lower()
    score = 0
    # Prefer deeper (more specific) sections.
    score += level * 10
    for kw in keywords:
        kw_lower = kw.lower()
        if kw_lower in heading_norm:
            # Heading match is strong; earlier keywords get a bonus.
            score += 1000 + (len(keywords) - keywords.index(kw)) * 10
        if kw_lower in content_norm:
            score += 50 + content_norm.count(kw_lower) * 5
    return score


def extract_section_for_entity(chapter_path: Path, keywords: list[str]) -> Optional[tuple[int, str, str]]:
    sections = parse_chapter(chapter_path)
    # Drop the top-level chapter title; it rarely contains useful entity-specific text.
    sections = [s for s in sections if s[0] > 1]
    if not sections:
        return None
    best = max(sections, key=lambda s: score_section(s, keywords))
    best_score = score_section(best, keywords)
    # Require a heading match or strong repeated content matches to avoid
    # grabbing a generic section that happens to mention the keyword once.
    level, heading, content = best
    heading_norm = heading.lower()
    content_norm = content.lower()
    has_heading_match = any(kw.lower() in heading_norm for kw in keywords)
    content_hits = sum(content_norm.count(kw.lower()) for kw in keywords)
    if not has_heading_match and content_hits < 3:
        return None
    if best_score < 80:
        return None
    return best


def process_entity(eid: str, chapter: int, name_zh: str) -> bool:
    path = next((p for p in (ROOT / "research").rglob(f"{eid}.md")), None)
    if path is None:
        print(f"  SKIP: {eid} not found", file=sys.stderr)
        return False

    chapter_path = WIKI_DIR / f"chapter-{chapter:02d}.md"
    if not chapter_path.exists():
        print(f"  SKIP: {eid} chapter {chapter} not found", file=sys.stderr)
        return False

    keywords = [name_zh] + EXTRA_KEYWORDS.get(eid, [])
    section = extract_section_for_entity(chapter_path, keywords)
    if section is None:
        print(f"  NO MATCH: {eid} ({name_zh})", file=sys.stderr)
        return False

    level, heading, content = section
    # Avoid using the chapter summary/abstract or the "本章小结" / "知识图谱锚点".
    if heading in ("摘要", "本章小结", "本章知识图谱锚点", "参考文献与数据来源"):
        print(f"  SKIP META: {eid} matched {heading}", file=sys.stderr)
        return False

    # Build body from the extracted section.  Keep the original heading level
    # so nested structure is preserved.
    body_lines = [f"{'#' * min(level, 6)} {heading}", "", content]
    new_body = "\n".join(body_lines)

    text = path.read_text(encoding="utf-8")
    yaml_text, old_body = split_frontmatter(text)
    fm = yaml.safe_load(yaml_text)

    # Do not overwrite rich existing bodies (e.g. PID); only fill empty or
    # previously-cleared placeholder bodies.
    stripped_old = old_body.strip()
    if stripped_old and not any(
        stripped_old.startswith(prefix) for prefix in ("# ", "## 摘要", "## Abstract", "## 요약")
    ):
        print(f"  KEEP RICH: {eid}", file=sys.stderr)
        return False

    fm["verification"] = fm.get("verification", {})
    fm["verification"]["notes"] = (
        "Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; "
        "pending human review and translation to en/ko."
    )

    new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
    new_text = f"---\n{new_yaml}---\n{new_body}\n"
    path.write_text(new_text, encoding="utf-8")
    print(f"  OK: {eid} <- {heading}")
    return True


def main() -> int:
    with MAPPING_PATH.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    ok = 0
    skipped = 0
    for ch in data["chapters"]:
        for g in ch.get("gaps", []):
            if process_entity(g["id"], ch["number"], g["name"]):
                ok += 1
            else:
                skipped += 1

    print(f"\nFilled {ok} entity bodies, skipped/no-match {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
