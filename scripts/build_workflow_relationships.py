"""Build cross-layer workflow relationships for the humanoid robot knowledge graph.

Run: PYTHONPATH=scripts python scripts/build_workflow_relationships.py
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config, entry_builder


RESEARCH_DIR = Path(config.RESEARCH_DIR)
RELATIONSHIPS_DIR = Path(config.RELATIONSHIPS_DIR)


def load_entity_index() -> dict[str, dict[str, Any]]:
    """Map normalized titles and $ids to entity records."""
    index: dict[str, dict[str, Any]] = {}
    for path in RESEARCH_DIR.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            yaml_text, _ = rest.split("---", 1)
            data = yaml.safe_load(yaml_text) or {}
            ent_id = data.get("$id")
            if not ent_id:
                continue
            record = {"path": path, "data": data, "id": ent_id}
            index[ent_id] = record
            names = data.get("names", {})
            for lang, name in names.items():
                if name:
                    index[normalize(name)] = record
        except Exception:
            continue
    return index


def normalize(title: str) -> str:
    t = title.lower()
    t = re.sub(r"https?://\S+", "", t)
    t = re.sub(r"^(#{0,4}\s+|\d+[\.、]\s*)", "", t)
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


# Hardcoded disambiguation for titles that match multiple entities.
TITLE_TO_ID: dict[str, str] = {
    "unitree h1": "ent_robot_unitree_h1_humanoid_robot_2024",
    "tesla optimus": "ent_robot_system_tesla_optimus",
    "figure 02": "ent_robot_system_figure_02",
    "agility robotics digit": "ent_robot_agility_robotics_digit_2023",
    "diffusion policy": "ent_paper_diffusion_policy_2023",
    "action chunking with transformers": "ent_paper_action_chunking_with_transform_2023",
    "rt-1": "ent_paper_rt_1_robotics_transformer_2022",
    "rt-2": "ent_paper_rt_2_vision_language_action_mo_2023",
    "openvla": "ent_paper_openvla_2024_1",
    "nvidia gr00t n1": "ent_paper_nvidia_gr00t_n1_2025",
    "model predictive control": "ent_paper_model_predictive_control_2024",
    "zero moment point": "ent_paper_zero_moment_point_2024",
    "hover": "ent_paper_hover_versatile_humanoid_contr_2024",
    "exbody2": "ent_paper_exbody2_2024",
    "asap": "ent_paper_asap_framework_2024",
    "isaac sim": "ent_software_nvidia_isaac_sim_2024",
    "isaac lab": "ent_software_nvidia_isaac_lab_2024",
    "mujoco": "ent_software_mujoco_physics_engine_2022",
    "ros 2": "ent_software_ros_2_middleware_2024",
    "moveit": "ent_software_moveit_motion_planning_2024",
    "drake": "ent_software_drake_systems_toolbox_2024",
    "droid": "ent_dataset_droid",
    "open x-embodiment": "ent_dataset_open_x_embodiment",
    "rh20t": "ent_dataset_rh20t_manipulation_dataset_2023",
    "amass": "ent_dataset_amass_motion_dataset_2019",
    "aloha": "ent_technology_aloha_teleoperation_system_2023",
    "mobile aloha": "ent_technology_mobile_aloha_2024",
    "humanplus shadowing system": "ent_technology_humanplus_shadowing_system_2024",
    "harmonic reducer": "ent_component_harmonic_reducer_2024",
    "rotary actuator": "ent_component_rotary_actuator_2024",
    "linear actuator": "ent_component_linear_actuator_2024",
    "frameless torque motor": "ent_component_frameless_torque_motor_2024",
    "planetary roller screw": "ent_component_planetary_roller_screw_2024",
    "inertial measurement unit": "ent_component_inertial_measurement_unit_2024",
    "intel realsense": "ent_component_intel_realsense_depth_camera_2024",
    "livox mid-360": "ent_component_livox_mid_360_lidar_2024",
    "nvidia jetson agx orin": "ent_component_nvidia_jetson_agx_orin_2024",
    "nvidia jetson thor": "ent_component_nvidia_jetson_thor",
    "battery management system": "ent_component_battery_management_system",
    "power distribution system": "ent_component_power_distribution_system_2024",
    "six axis force torque sensor": "ent_component_six_axis_force_torque_sensor_2024",
    "safety mcu": "ent_component_safety_mcu_2024",
    "emergency stop system": "ent_component_emergency_stop_system_2024",
    "harmonic drive systems": "ent_company_harmonic_drive_systems_2024",
    "leaderdrive": "ent_company_leaderdrive_2024",
    "sanhua": "ent_tier1_supplier_sanhua_intelligent_controls",
    "tuopu": "ent_company_tuopu_group_2024",
    "maxon": "ent_company_maxon_group_2024",
    "kollmorgen": "ent_company_kollmorgen_corporation_2024",
    "mingzhi": "ent_company_mingzhi_appliance_2024",
    "tesla": "ent_oem_tesla",
    "design for manufacturing": "ent_paper_design_for_manufacturing_2024",
    "design for assembly": "ent_paper_design_for_assembly_2024",
    "bill of materials": "ent_paper_bill_of_materials_2024",
    "system integration test bench": "ent_equipment_system_integration_test_bench_2024",
    "hardware-in-the-loop": "ent_paper_hardware_in_the_loop_2024",
    "joint calibration procedure": "ent_paper_joint_calibration_procedure_2024",
    "model-based definition": "ent_technology_model_based_definition_2024",
    "urdf": "ent_technology_urdf_robot_description_format_2024",
    "mjcf": "ent_technology_mjcf_simulation_format_2024",
    "finite element analysis": "ent_paper_finite_element_analysis_2024",
    "thermal management system": "ent_component_thermal_management_system_2024",
    "supplier qualification": "ent_paper_supplier_qualification_2024",
    "production ramp": "ent_paper_production_ramp_2024",
    "ota software update": "ent_technology_ota_software_update_2024",
    "fleet management platform": "ent_software_fleet_management_platform_2024",
    "iso 13482": "ent_standard_iso_13482_personal_care_robot_2014",
    "servo motor": "ent_comp_servo_motor",
    "hollow cup motor": "ent_component_hollow_cup_motor_2024",
    "rv reducer": "ent_component_rv_reducer_2024",
    "joint motor": "ent_component_joint_motor_2024",
    "servo drive": "ent_component_servo_drive_2024",
    "unitree g1": "ent_robot_unitree_g1_2024",
}


def find_entity(index: dict[str, Any], *fragments: str) -> dict[str, Any] | None:
    """Find entity by title fragment, using hardcoded disambiguation first."""
    for frag in fragments:
        frag_lower = frag.lower().strip()
        hard_id = TITLE_TO_ID.get(frag_lower)
        if hard_id and hard_id in index:
            return index[hard_id]
        # direct normalized lookup
        rec = index.get(normalize(frag))
        if rec:
            return rec
        # substring search, but prefer exact word boundaries
        frag_words = frag_lower.split()
        for key, rec in index.items():
            key_lower = key.lower()
            if frag_lower in key_lower:
                return rec
            # all words present
            if all(w in key_lower for w in frag_words):
                return rec
    return None


def make_relationship_id(source_id: str, rel_type: str, target_id: str) -> str:
    base = f"rel_{source_id}_{rel_type}_{target_id}"
    return re.sub(r"[^a-z0-9_]", "_", base).lower()[:120]


def relationship_exists(rel_id: str) -> bool:
    return (RELATIONSHIPS_DIR / f"{rel_id}.md").exists()


def write_relationship(
    rel_id: str,
    rel_type: str,
    source: dict[str, Any],
    target: dict[str, Any],
    description: dict[str, str],
) -> Path:
    RELATIONSHIPS_DIR.mkdir(parents=True, exist_ok=True)
    frontmatter = {
        "$id": rel_id,
        "$schema": "../schema/v1/relationship_schema.json",
        "$version": 1,
        "type": rel_type,
        "source": {"id": source["id"], "name": source["data"].get("names", {})},
        "target": {"id": target["id"], "name": target["data"].get("names", {})},
        "domains": {
            "source": source["data"].get("domains", []),
            "target": target["data"].get("domains", []),
        },
        "description": description,
        "verification": {"status": "partially_verified", "sources": []},
        "sources": [{"type": "curated", "url": "", "description": "Workflow relationship curated from public project pages and literature."}],
    }
    path = RELATIONSHIPS_DIR / f"{rel_id}.md"
    content = f"---\n{yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)}---\n"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    print("Loading entity index...")
    index = load_entity_index()
    print(f"Indexed {len({k for k in index.keys() if k.startswith('ent_')})} entities")

    relationships: list[tuple[str, str, str, dict[str, str]]] = [
        # Data -> Method
        ("DROID", "uses_dataset", "Diffusion Policy", {"en": "DROID is used to train Diffusion Policy models.", "zh": "DROID被用于训练Diffusion Policy模型。", "ko": "DROID은 Diffusion Policy 모델 학습에 사용됩니다."}),
        ("Open X-Embodiment", "uses_dataset", "RT-2", {"en": "Open X-Embodiment data is used to train RT-2 and RT-X.", "zh": "Open X-Embodiment数据用于训练RT-2和RT-X。", "ko": "Open X-Embodiment 데이터는 RT-2 및 RT-X 학습에 사용됩니다."}),
        ("Open X-Embodiment", "uses_dataset", "Octo", {"en": "Open X-Embodiment data is used to train Octo generalist policy.", "zh": "Open X-Embodiment数据用于训练Octo通才策略。", "ko": "Open X-Embodiment 데이터는 Octo 제너럴리스트 정책 학습에 사용됩니다."}),
        ("Open X-Embodiment", "uses_dataset", "OpenVLA", {"en": "Open X-Embodiment data is used to train OpenVLA.", "zh": "Open X-Embodiment数据用于训练OpenVLA。", "ko": "Open X-Embodiment 데이터는 OpenVLA 학습에 사용됩니다."}),
        ("RH20T", "uses_dataset", "Diffusion Policy", {"en": "RH20T provides contact-rich manipulation data for policy learning.", "zh": "RH20T为策略学习提供接触丰富的操作数据。", "ko": "RH20T는 정책 학습을 위한 접촉이 풍부한 조작 데이터를 제공합니다."}),
        ("AMASS", "uses_dataset", "HumanPlus Shadowing System", {"en": "AMASS is used to pre-train HumanPlus low-level policies in simulation.", "zh": "AMASS用于在仿真中预训练HumanPlus低层策略。", "ko": "AMASS는 시뮬레이션에서 HumanPlus 저수준 정책을 사전 학습하는 데 사용됩니다."}),
        ("ALOHA", "uses_data", "Action Chunking with Transformers", {"en": "ALOHA hardware collects demonstrations used to train ACT.", "zh": "ALOHA硬件采集用于训练ACT的演示数据。", "ko": "ALOHA 하드웨어는 ACT 학습에 사용되는 시연 데이터를 수집합니다."}),
        ("Mobile ALOHA", "uses_data", "Action Chunking with Transformers", {"en": "Mobile ALOHA extends ALOHA to collect whole-body mobile manipulation data for ACT.", "zh": "Mobile ALOHA扩展ALOHA以采集用于ACT的全身移动操作数据。", "ko": "Mobile ALOHA는 ACT를 위한 전신 이동 조작 데이터를 수집하도록 ALOHA를 확장합니다."}),

        # Method -> Robot System
        ("Diffusion Policy", "implemented_on", "Unitree H1", {"en": "Diffusion Policy can be deployed on Unitree H1 for manipulation tasks.", "zh": "Diffusion Policy可部署在Unitree H1上执行操作任务。", "ko": "Diffusion Policy는 Unitree H1에 배포되어 조작 작업을 수행할 수 있습니다."}),
        ("Action Chunking with Transformers", "implemented_on", "Unitree G1", {"en": "ACT-style policies are deployed on Unitree G1 for bimanual tasks.", "zh": "ACT风格策略部署在Unitree G1上执行双臂任务。", "ko": "ACT 스타일 정책은 Unitree G1에 배포되어 양손 작업을 수행합니다."}),
        ("NVIDIA GR00T N1", "implemented_on", "Unitree H1", {"en": "GR00T N1 is trained and deployed on Unitree H1 as a reference platform.", "zh": "GR00T N1在Unitree H1参考平台上训练并部署。", "ko": "GR00T N1은 Unitree H1 참조 플랫폼에서 학습 및 배포됩니다."}),
        ("NVIDIA GR00T N1", "implemented_on", "Tesla Optimus", {"en": "GR00T N1 targets generalist humanoid control including Tesla Optimus-class hardware.", "zh": "GR00T N1面向包括Tesla Optimus级硬件在内的通用人形控制。", "ko": "GR00T N1은 Tesla Optimus급 하드웨어를 포함한 범용 휨로봇 제어를 목표로 합니다."}),
        ("Model Predictive Control", "implemented_on", "Unitree H1", {"en": "MPC is used for whole-body motion generation on Unitree H1.", "zh": "MPC用于Unitree H1的全身运动生成。", "ko": "MPC는 Unitree H1의 전신 동작 생성에 사용됩니다."}),
        ("HOVER", "implemented_on", "Unitree H1", {"en": "HOVER versatile controller is evaluated on Unitree H1.", "zh": "HOVER通用控制器在Unitree H1上评估。", "ko": "HOVER 다용도 제어기는 Unitree H1에서 평가됩니다."}),
        ("ASAP Framework", "implemented_on", "Unitree H1", {"en": "ASAP sim-to-real framework enables agile control on Unitree H1.", "zh": "ASAP Sim-to-Real框架使Unitree H1能够实现敏捷控制。", "ko": "ASAP Sim-to-Real 프레임워크는 Unitree H1에서 민첩한 제어를 가능하게 합니다."}),
        ("OpenVLA", "implemented_on", "Figure 02", {"en": "OpenVLA can be fine-tuned and deployed on Figure 02 for manipulation.", "zh": "OpenVLA可在Figure 02上微调并部署用于操作。", "ko": "OpenVLA는 Figure 02에서 미세 조정 및 배포되어 조작에 사용될 수 있습니다."}),
        ("Physical Intelligence pi0", "implemented_on", "Figure 02", {"en": "pi0 is a VLA policy candidate for Figure 02 bimanual tasks.", "zh": "pi0是Figure 02双臂任务的VLA策略候选。", "ko": "pi0는 Figure 02 양손 작업을 위한 VLA 정책 후보입니다."}),

        # Component -> Robot System
        ("Harmonic Reducer", "is_part_of", "Rotary Actuator", {"en": "Harmonic reducer is a core sub-component of rotary joint actuators.", "zh": "谐波减速器是旋转关节执行器的核心子部件。", "ko": "하모닉 감속기는 회전 관절 액추에이터의 핵심 하위 부품입니다."}),
        ("Frameless Torque Motor", "is_part_of", "Rotary Actuator", {"en": "Frameless torque motor is integrated into rotary actuators.", "zh": "无框力矩电机集成到旋转执行器中。", "ko": "프레임리스 토크 모터는 회전 액추에이터에 통합됩니다."}),
        ("Planetary Roller Screw", "is_part_of", "Linear Actuator", {"en": "Planetary roller screw converts rotary motion in linear actuators.", "zh": "行星滚柱丝杠将旋转运动转换为线性执行器的直线运动。", "ko": "행성 롤러 스크류는 선형 액추에이터에서 회전 운 동을 선형 운 동으로 변환합니다."}),
        ("Rotary Actuator", "is_part_of", "Unitree H1", {"en": "Rotary actuators drive the joints of Unitree H1.", "zh": "旋转执行器驱动Unitree H1的关节。", "ko": "회전 액추에이터는 Unitree H1의 관절을 구동합니다."}),
        ("Rotary Actuator", "is_part_of", "Tesla Optimus", {"en": "Rotary actuators are used in Tesla Optimus arm and hip joints.", "zh": "旋转执行器用于Tesla Optimus的臂部和髋部关节。", "ko": "회전 액추에이터는 Tesla Optimus의 팔과 엉덩이 관절에 사용됩니다."}),
        ("Linear Actuator", "is_part_of", "Tesla Optimus", {"en": "Linear actuators are used in Tesla Optimus lower-limb joints.", "zh": "线性执行器用于Tesla Optimus下肢关节。", "ko": "선형 액추에이터는 Tesla Optimus 하지 관절에 사용됩니다."}),
        ("Inertial Measurement Unit", "is_part_of", "Unitree H1", {"en": "IMU is mounted on Unitree H1 torso for balance estimation.", "zh": "IMU安装在Unitree H1躯干用于平衡估计。", "ko": "IMU는 Unitree H1 몸통에 장착되어 균형 추정에 사용됩니다."}),
        ("Intel RealSense Depth Camera", "is_part_of", "Unitree H1", {"en": "RealSense depth cameras provide visual perception for Unitree H1.", "zh": "RealSense深度相机为Unitree H1提供视觉感知。", "ko": "RealSense 깊이 칩차는 Unitree H1에 시각 인식을 제공합니다."}),
        ("Livox Mid-360 LiDAR", "is_part_of", "Unitree H1", {"en": "Livox LiDAR provides 360 mapping for Unitree H1 navigation.", "zh": "Livox LiDAR为Unitree H1导航提供360度建图。", "ko": "Livox LiDAR는 Unitree H1 납치를 위한 360도 매핑을 제공합니다."}),
        ("NVIDIA Jetson AGX Orin", "is_part_of", "Unitree H1", {"en": "Jetson AGX Orin serves as onboard compute for Unitree H1.", "zh": "Jetson AGX Orin作为Unitree H1的车载计算。", "ko": "Jetson AGX Orin은 Unitree H1의 온보드 컴퓨팅 역할을 합니다."}),
        ("NVIDIA Jetson Thor", "is_part_of", "Tesla Optimus", {"en": "Jetson Thor-class compute is targeted for next-generation humanoids such as Tesla Optimus.", "zh": "Jetson Thor级计算面向Tesla Optimus等下一代人形机器人。", "ko": "Jetson Thor급 컴퓨팅은 Tesla Optimus와 같은 차세대 휨로봇을 대상으로 합니다."}),
        ("Battery Management System", "is_part_of", "Tesla Optimus", {"en": "BMS manages the torso battery pack of Tesla Optimus.", "zh": "BMS管理Tesla Optimus的躯干电池包。", "ko": "BMS는 Tesla Optimus의 몸통 배터리 팩을 관리합니다."}),
        ("Power Distribution System", "is_part_of", "Tesla Optimus", {"en": "Power distribution routes battery energy to compute and actuators in Tesla Optimus.", "zh": "配电系统将电池能量分配给Tesla Optimus的计算和执行器。", "ko": "전력 분배 시스템은 Tesla Optimus의 컴퓨팅 및 액추에이터에 배터리 에너지를 분배합니다."}),
        ("Six Axis Force Torque Sensor", "is_part_of", "Tesla Optimus", {"en": "Wrist/ankle force-torque sensors enable contact control in Tesla Optimus.", "zh": "腕部/踝部力矩传感器使Tesla Optimus能够实现接触控制。", "ko": "손목/발목 힘-토크 센서는 Tesla Optimus의 접촉 제어를 가능하게 합니다."}),
        ("Safety MCU", "is_part_of", "Unitree H1", {"en": "Safety MCU monitors emergency stops and joint limits on Unitree H1.", "zh": "安全MCU监控Unitree H1的急停和关节限位。", "ko": "안전 MCU는 Unitree H1의 비상 정지 및 관절 한계를 모니터링합니다."}),
        ("Emergency Stop System", "is_part_of", "Unitree H1", {"en": "Emergency stop system is a required safety subsystem of Unitree H1.", "zh": "急停系统是Unitree H1的必备安全子系统。", "ko": "비상 정지 시스템은 Unitree H1의 필수 안전 하위 시스템입니다."}),

        # Manufacturer -> Component
        ("Harmonic Drive Systems", "manufactures", "Harmonic Reducer", {"en": "Harmonic Drive Systems manufactures harmonic reducers.", "zh": "Harmonic Drive Systems生产谐波减速器。", "ko": "Harmonic Drive Systems는 하모닉 감속기를 제조합니다."}),
        ("Nabtesco Corporation", "manufactures", "RV Reducer", {"en": "Nabtesco manufactures RV and cycloidal reducers.", "zh": "Nabtesco生产RV和摆线减速器。", "ko": "Nabtesco는 RV 및 사이클로이드 감속기를 제조합니다."}),
        ("Leaderdrive", "manufactures", "Harmonic Reducer", {"en": "Leaderdrive is a Chinese harmonic reducer manufacturer.", "zh": "绿的谐波是国产谐波减速器制造商。", "ko": "Leaderdrive는 중국 하모닉 감속기 제조업체입니다."}),
        ("Sanhua Intelligent Controls", "supplies", "Rotary Actuator", {"en": "Sanhua supplies integrated rotary actuator assemblies, reportedly for Tesla Optimus.", "zh": "三花智控供应一体化旋转执行器总成， reportedly 用于Tesla Optimus。", "ko": "Sanhua는 통합 회전 액추에이터 어셈블리를 공급하며 Tesla Optimus용으로 알려져 있습니다."}),
        ("Tuopu Group", "supplies", "Linear Actuator", {"en": "Tuopu supplies integrated linear actuator assemblies, reportedly for Tesla Optimus.", "zh": "拓普集团供应一体化线性执行器总成， reportedly 用于Tesla Optimus。", "ko": "Tuopu는 통합 선형 액추에이터 어셈블리를 공급하며 Tesla Optimus용으로 알려져 있습니다."}),
        ("CubeMars", "manufactures", "Joint Motor", {"en": "CubeMars manufactures integrated robot joint motors and actuators.", "zh": "CubeMars生产一体化机器人关节电机和执行器。", "ko": "CubeMars는 통합 로봇 관절 모터 및 액추에이터를 제조합니다."}),
        ("Maxon Group", "manufactures", "Servo Motor", {"en": "Maxon manufactures precision motors and gearheads for robot joints.", "zh": "Maxon生产用于机器人关节的精密电机和齿轮头。", "ko": "Maxon은 로봇 관절용 정밀 모터 및 기어헤드를 제조합니다."}),
        ("Kollmorgen Corporation", "manufactures", "Frameless Torque Motor", {"en": "Kollmorgen supplies frameless torque motors for robot joints.", "zh": "Kollmorgen供应用于机器人关节的无框力矩电机。", "ko": "Kollmorgen은 로봇 관절용 프레임리스 토크 모터를 공급합니다."}),
        ("Inovance Technology", "manufactures", "Servo Drive", {"en": "Inovance supplies servo drives and motors for robot joints.", "zh": "汇川技术供应用于机器人关节的伺服驱动和电机。", "ko": "Inovance는 로봇 관절용 서보 드라이브 및 모터를 공급합니다."}),
        ("Mingzhi Appliance", "manufactures", "Hollow Cup Motor", {"en": "Mingzhi manufactures hollow-cup motors for dexterous hands.", "zh": "鸣志电器生产用于灵巧手的空心杯电机。", "ko": "Mingzhi는 능숙한 손을 위한 홀컵 모터를 제조합니다."}),

        # OEM -> Supplier
        ("Tesla", "sources_from", "Sanhua Intelligent Controls", {"en": "Tesla reportedly sources rotary actuator assemblies from Sanhua for Optimus.", "zh": "据报道，Tesla从三花智控采购Optimus的旋转执行器总成。", "ko": "Tesla는 Optimus용 회전 액추에이터 어셈블리를 Sanhua에서 조달하는 것으로 알려져 있습니다."}),
        ("Tesla", "sources_from", "Tuopu Group", {"en": "Tesla reportedly sources linear actuator assemblies from Tuopu for Optimus.", "zh": "据报道，Tesla从拓普集团采购Optimus的线性执行器总成。", "ko": "Tesla는 Optimus용 선형 액추에이터 어셈블리를 Tuopu에서 조달하는 것으로 알려져 있습니다."}),

        # Missing manufacturer -> component relationships
        ("Nabtesco Corporation", "manufactures", "RV Reducer", {"en": "Nabtesco manufactures RV and cycloidal reducers for heavy-duty joints.", "zh": "Nabtesco生产用于重载关节的RV和摆线减速器。", "ko": "Nabtesco는 중하물 관절용 RV 및 사이클로이드 감속기를 제조합니다."}),
        ("CubeMars", "manufactures", "Joint Motor", {"en": "CubeMars manufactures integrated robot joint motors and actuators.", "zh": "CubeMars生产一体化机器人关节电机和执行器。", "ko": "CubeMars는 통합 로봇 관절 모터 및 액추에이터를 제조합니다."}),
        ("Inovance Technology", "manufactures", "Servo Drive", {"en": "Inovance supplies servo drives and motors for robot joints.", "zh": "汇川技术供应用于机器人关节的伺服驱动和电机。", "ko": "Inovance는 로봇 관절용 서보 드라이브 및 모터를 공급합니다."}),

        # Software Platform -> Method
        ("NVIDIA Isaac Sim", "used_by", "NVIDIA GR00T N1", {"en": "Isaac Sim is used to generate synthetic training data for GR00T N1.", "zh": "Isaac Sim用于为GR00T N1生成合成训练数据。", "ko": "Isaac Sim은 GR00T N1을 위한 합성 학습 데이터를 생성하는 데 사용됩니다."}),
        ("NVIDIA Isaac Lab", "used_by", "NVIDIA GR00T N1", {"en": "Isaac Lab is used to train GR00T N1 policies at scale.", "zh": "Isaac Lab用于大规模训练GR00T N1策略。", "ko": "Isaac Lab은 GR00T N1 정책을 대규모로 학습하는 데 사용됩니다."}),
        ("MuJoCo Physics Engine", "used_by", "Model Predictive Control", {"en": "MuJoCo is commonly used to prototype and evaluate MPC controllers.", "zh": "MuJoCo常用于原型化和评估MPC控制器。", "ko": "MuJoCo는 MPC 컨트롤러의 프로토타입 및 평가에 일반적으로 사용됩니다."}),
        ("ROS 2 Middleware", "used_by", "MoveIt Motion Planning", {"en": "MoveIt runs on top of ROS 2 for manipulation planning.", "zh": "MoveIt在ROS 2之上运行以进行运动规划。", "ko": "MoveIt은 조작 계획을 위해 ROS 2 위에서 실행됩니다."}),
        ("Drake Systems Toolbox", "used_by", "Model Predictive Control", {"en": "Drake provides optimization-based control tools for MPC development.", "zh": "Drake为MPC开发提供基于优化的控制工具。", "ko": "Drake는 MPC 개발을 위한 최적화 기반 제어 도구를 제공합니다."}),

        # Data -> Software Platform
        ("DROID", "used_with", "NVIDIA Isaac Sim", {"en": "DROID data can be replayed or augmented in Isaac Sim for policy training.", "zh": "DROID数据可在Isaac Sim中回放或增强以训练策略。", "ko": "DROID 데이터는 Isaac Sim에서 정책 학습을 위해 재생 또는 증강될 수 있습니다."}),
        ("Open X-Embodiment", "used_with", "NVIDIA Isaac Lab", {"en": "Open X-Embodiment data can be mixed with synthetic data in Isaac Lab.", "zh": "Open X-Embodiment数据可与Isaac Lab中的合成数据混合。", "ko": "Open X-Embodiment 데이터는 Isaac Lab의 합성 데이터와 혼합할 수 있습니다."}),
        ("AMASS", "used_with", "MuJoCo Physics Engine", {"en": "AMASS motions are used to seed MuJoCo simulations for humanoid tracking.", "zh": "AMASS动作用于在MuJoCo仿真中初始化人形跟踪。", "ko": "AMASS 동작은 MuJoCo 시뮬레이션에서 휨로봇 추적을 위한 시드를 만드는 데 사용됩니다."}),

        # Manufacturing / System Integration -> Robot System
        ("Design for Manufacturing", "applies_to", "Unitree H1", {"en": "DFM principles are applied to Unitree H1 mechanical parts for volume production.", "zh": "DFM原则应用于Unitree H1的机械零件以实现批量生产。", "ko": "DFM 원칙은 Unitree H1 기계 부품의 볼륨 생산을 위해 적용됩니다."}),
        ("Design for Assembly", "applies_to", "Tesla Optimus", {"en": "DFA is applied to Tesla Optimus to reduce assembly cycle time.", "zh": "DFA应用于Tesla Optimus以减少装配周期时间。", "ko": "DFA는 Tesla Optimus의 조립 사이클 타임을 줄이기 위해 적용됩니다."}),
        ("Bill of Materials", "is_part_of", "Tesla Optimus", {"en": "BOM structures all parts and subassemblies of Tesla Optimus.", "zh": "BOM结构化Tesla Optimus的所有零件和子装配件。", "ko": "BOM은 Tesla Optimus의 모든 부품 및 하위 조립품을 구조화합니다."}),
        ("System Integration Test Bench", "validates_on", "Unitree H1", {"en": "Integration test benches validate Unitree H1 joints and control loops.", "zh": "集成测试台验证Unitree H1的关节和控制回路。", "ko": "통합 테스트 벤치는 Unitree H1의 관절 및 제어 루프를 검증합니다."}),
        ("Hardware-in-the-Loop", "tested_with", "Tesla Optimus", {"en": "HIL testing is used to validate Tesla Optimus controllers before full assembly.", "zh": "HIL测试用于在完整装配前验证Tesla Optimus控制器。", "ko": "HIL 테스트는 완전한 조립 전 Tesla Optimus 컨트롤러를 검증하는 데 사용됩니다."}),
        ("Joint Calibration Procedure", "applies_to", "Unitree H1", {"en": "Joint calibration is performed on every Unitree H1 after assembly.", "zh": "每台Unitree H1装配后都进行关节标定。", "ko": "모든 Unitree H1은 조립 후 관절 보정을 수행합니다."}),
        ("Model-Based Definition", "applies_to", "Tesla Optimus", {"en": "MBD keeps Tesla Optimus CAD, kinematics, and annotations synchronized.", "zh": "MBD保持Tesla Optimus的CAD、运动学和标注同步。", "ko": "MBD는 Tesla Optimus의 CAD, 운 동학 및 주석을 동기화된 상태로 유지합니다."}),
        ("URDF Robot Description Format", "models", "Unitree H1", {"en": "URDF models Unitree H1 links, joints, and geometry for simulation.", "zh": "URDF对Unitree H1的连杆、关节和几何进行仿真建模。", "ko": "URDF는 Unitree H1의 링크, 관절 및 기하를 시뮬레이션을 위해 모델링합니다."}),
        ("MJCF Simulation Format", "models", "Unitree H1", {"en": "MJCF is used to model Unitree H1 in MuJoCo.", "zh": "MJCF用于在MuJoCo中对Unitree H1建模。", "ko": "MJCF는 MuJoCo에서 Unitree H1을 모델링하는 데 사용됩니다."}),
        ("Finite Element Analysis", "analyzes", "Unitree H1", {"en": "FEA analyzes Unitree H1 structural and thermal behavior before prototyping.", "zh": "FEA在样机前分析Unitree H1的结构和热行为。", "ko": "FEA는 프로토타입 전 Unitree H1의 구조적 및 열적 거동을 분석합니다."}),
        ("Thermal Management System", "is_part_of", "Tesla Optimus", {"en": "Thermal management keeps Tesla Optimus compute and actuators cool.", "zh": "热管理系统保持Tesla Optimus的计算和执行器冷却。", "ko": "열 관리 시스템은 Tesla Optimus의 컴퓨팅 및 액추에이터를 시원하게 유지합니다."}),
        ("ISO 13482 Personal Care Robot Safety", "is_regulated_by", "Unitree H1", {"en": "Unitree H1 must comply with ISO 13482 for service robot safety.", "zh": "Unitree H1必须符合ISO 13482服务机器人安全标准。", "ko": "Unitree H1은 서비스 로봇 안전을 위해 ISO 13482를 준수해야 합니다."}),
        ("Supplier Qualification", "applies_to", "Sanhua Intelligent Controls", {"en": "Supplier qualification is applied to Sanhua before mass-production sourcing.", "zh": "在量产采购前对三花智控进行供应商认证。", "ko": "양산 조달 전 Sanhua에 대한 공급업체 자격을 적용합니다."}),
        ("Production Ramp", "applies_to", "Tesla Optimus", {"en": "Production ramp transitions Tesla Optimus from pilot to volume builds.", "zh": "产能爬坡将Tesla Optimus从试产过渡到批量生产。", "ko": "생산 램프는 Tesla Optimus를 파일럿에서 볼륨 빌드로 전환합니다."}),
        ("OTA Software Update", "applies_to", "Unitree H1", {"en": "OTA updates deploy new policies and firmware to Unitree H1 fleets.", "zh": "OTA更新向Unitree H1机群部署新策略和固件。", "ko": "OTA 업데이트는 Unitree H1 플릿에 새로운 정책 및 펌웨어를 배포합니다."}),
        ("Fleet Management Platform", "manages", "Unitree H1", {"en": "Fleet management orchestrates deployed Unitree H1 robots.", "zh": "机群管理平台编排已部署的Unitree H1机器人。", "ko": "플릿 관리 플랫폼은 배포된 Unitree H1 로봇을 오케스트레이션합니다."}),

        # Method -> Dataset (reverse direction: method uses dataset)
        ("Diffusion Policy", "uses_dataset", "RH20T", {"en": "Diffusion Policy can be trained on RH20T contact-rich manipulation data.", "zh": "Diffusion Policy可以在RH20T接触丰富的操作数据上训练。", "ko": "Diffusion Policy는 RH20T 접촉이 풍부한 조작 데이터로 학습할 수 있습니다."}),
        ("Action Chunking with Transformers", "uses_dataset", "ALOHA", {"en": "ACT is commonly trained on demonstrations collected via ALOHA.", "zh": "ACT通常使用通过ALOHA采集的演示数据训练。", "ko": "ACT는 일반적으로 ALOHA를 통해 수집된 시연 데이터로 학습됩니다."}),

        # Method -> Component
        ("Model Predictive Control", "requires", "Inertial Measurement Unit", {"en": "MPC requires IMU feedback for state estimation.", "zh": "MPC需要IMU反馈进行状态估计。", "ko": "MPC는 상태 추정을 위해 IMU 피드백이 필요합니다."}),
        ("Action Chunking with Transformers", "requires", "ALOHA", {"en": "ACT requires a teleoperation interface such as ALOHA to collect demonstrations.", "zh": "ACT需要ALOHA等遥操作接口来采集演示。", "ko": "ACT는 시연을 수집하기 위해 ALOHA와 같은 텔레오퍼레이션 인터페이스가 필요합니다."}),
        ("NVIDIA GR00T N1", "requires", "NVIDIA Jetson Thor", {"en": "GR00T N1 requires Jetson Thor-class compute for real-time onboard inference.", "zh": "GR00T N1需要Jetson Thor级计算进行实时 onboard 推理。", "ko": "GR00T N1은 실시간 온보드 추론을 위해 Jetson Thor급 컴퓨팅이 필요합니다."}),

        # Standard -> Component
        ("ISO 13482 Personal Care Robot Safety", "is_regulated_by", "Emergency Stop System", {"en": "ISO 13482 requires emergency stop systems on personal care robots.", "zh": "ISO 13482要求个人护理机器人配备急停系统。", "ko": "ISO 13482는 개인 돌봄 로봇에 비상 정지 시스템을 요구합니다."}),
    ]

    added = 0
    skipped = 0
    failed = 0
    for source_title, rel_type, target_title, description in relationships:
        source_rec = find_entity(index, source_title)
        target_rec = find_entity(index, target_title)
        if source_rec is None or target_rec is None:
            print(f"SKIP {source_title} -> {target_title}: entity not found")
            skipped += 1
            continue
        rel_id = make_relationship_id(source_rec["id"], rel_type, target_rec["id"])
        if relationship_exists(rel_id):
            print(f"SKIP {rel_id}: already exists")
            skipped += 1
            continue
        write_relationship(rel_id, rel_type, source_rec, target_rec, description)
        print(f"ADDED {rel_id}")
        added += 1

    print(f"\nAdded {added} relationships, skipped {skipped}, failed {failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
