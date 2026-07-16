# 附录 A 实体与关系速查表

> 本附录由 `scripts/build_appendices.py` 从知识图谱数据自动生成，随 KG 更新而更新。

知识图谱的实体类型、关系类型与核心实体一览。


## A.1 实体类型分布

| 类型 | 中文 | 数量 |
|---|---|---|
| `paper` | 论文 | 1594 |
| `method` | 方法 | 210 |
| `report` | 报告 | 86 |
| `component` | 零部件 | 49 |
| `technology` | 技术 | 28 |
| `component_manufacturer` | 零部件制造商 | 19 |
| `concept` | 概念 | 17 |
| `software_platform` | 软件平台 | 16 |
| `robot_system` | 机器人系统 | 11 |
| `dataset` | 数据集 | 11 |
| `principle` | 原理 | 10 |
| `benchmark` | 评测基准 | 9 |
| `company` | 公司 | 9 |
| `algorithm` | 算法 | 9 |
| `formalism` | 形式化方法 | 8 |
| `standard` | 标准 | 7 |
| `equation` | 方程 | 7 |
| `foundation` | 基础学科 | 5 |
| `material` | 材料 | 4 |
| `application_scenario` | 应用场景 | 4 |
| `oem` | 整机厂商 | 3 |
| `tier1_supplier` | Tier 1 供应商 | 3 |
| `operator` | 算子 | 3 |
| `theorem` | 定理 | 2 |
| `tool_equipment` | 工具设备 | 1 |
| `market_segment` | 市场细分 | 1 |
| **合计** | — | **2126** |

## A.2 关系类型分布

| 关系类型 | 数量 |
|---|---|
| `cites` | 562 |
| `mentions` | 100 |
| `is_based_on` | 64 |
| `uses` | 60 |
| `requires` | 42 |
| `evaluates_on` | 38 |
| `evaluates` | 28 |
| `is_part_of` | 18 |
| `produces` | 18 |
| `implemented_on` | 12 |
| `integrates` | 12 |
| `enables` | 11 |
| `has_prerequisite` | 9 |
| `manufacturer_of` | 8 |
| `supplies` | 8 |
| `sources_from` | 8 |
| `applies_to` | 8 |
| `uses_dataset` | 7 |
| `combines_with` | 7 |
| `formalizes` | 6 |
| `is_regulated_by` | 4 |
| `constrains` | 4 |
| `models` | 4 |
| `derived_from` | 3 |
| `includes` | 3 |
| `verified_by` | 3 |
| `solves` | 2 |
| `is_alternative_to` | 2 |
| `uses_data` | 2 |
| `serves` | 2 |
| `validates_on` | 1 |
| `uses_technology` | 1 |
| `analyzes` | 1 |
| `uses_product_of` | 1 |
| `tested_with` | 1 |
| `addresses` | 1 |
| `is_version_of` | 1 |
| `instantiates` | 1 |
| **合计** | **1063** |

## A.3 领域（Domain）分布

| 领域 | 实体数 |
|---|---|
| 基础学科 | 36 |
| 原材料 | 13 |
| 零部件 | 358 |
| 制造工艺 | 83 |
| 组装集成测试 | 38 |
| 量产制造 | 81 |
| 设计工程 | 400 |
| AI 模型与算法 | 1595 |
| 软件中间件 | 1029 |
| 数据与数据集 | 118 |
| 评测基准 | 84 |
| 应用与市场 | 312 |
| 政策法规伦理 | 41 |

## A.4 核心实体 Top 50（按关系数）

| 排名 | 实体 | 类型 | 关系数 |
|---|---|---|---|
| 1 | [标准二次规划（QP）](/entry/ent_qp_standard_form/) | 形式化方法 | 43 |
| 2 | [DIAL｜通过端到端VLA的潜在世界建模解耦意图和行动](/entry/ent_paper_dial_decoupling_intent_and_act_2026/) | 论文 | 35 |
| 3 | [通过主动空间脑和可泛化动作小脑实现人形全身操作](/entry/ent_paper_liang_humanoid_whole_body_manipulati_2026/) | 论文 | 31 |
| 4 | [HumanoidBench](/entry/ent_benchmark_humanoidbench/) | 评测基准 | 24 |
| 5 | [探索基于GPT的大语言模型在虚拟现实人机团队协作仿真中的可变自主性](/entry/ent_paper_lakhnati_exploring_a_gpt_based_large_la_2023/) | 论文 | 23 |
| 6 | [机器人视觉-语言-动作：数据集、基准与数据引擎综述](/entry/ent_paper_wang_vla_survey_2026/) | 论文 | 21 |
| 7 | [宇树 H1 人形机器人](/entry/ent_robot_unitree_h1_humanoid_robot_2024/) | 机器人系统 | 21 |
| 8 | [在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置](/entry/ent_paper_active_stereo_camera_outperfor_2026/) | 论文 | 21 |
| 9 | [基于多阶段强化学习的人形全身羽毛球运动](/entry/ent_paper_liu_humanoid_whole_body_badminton_2026/) | 论文 | 21 |
| 10 | [磁场定向控制（FOC）](/entry/ent_method_foc_motor_control/) | 方法 | 21 |
| 11 | [世界动作模型：具身智能的下一个前沿](/entry/ent_paper_wang_wam_survey_2026/) | 论文 | 20 |
| 12 | [AgiBot World Colosseo｜用于可扩展和智能具身系统的大规模操作平台](/entry/ent_paper_agibot_world_colosseo_a_large_2025/) | 论文 | 20 |
| 13 | [机器人训练机器人：人形机器人的自动现实世界策略适应与学习](/entry/ent_paper_hu_robot_trains_robot_automatic_r_2025/) | 论文 | 20 |
| 14 | [RUKA：以学习重新思考人形手机器人设计](/entry/ent_paper_zorin_ruka_rethinking_the_design_of_2025/) | 论文 | 20 |
| 15 | [基于无迹卡尔曼滤波的仿人机器人无关节力矩传感器力矩估计](/entry/ent_paper_sorrentino_ukf_based_sensor_fusion_for_jo_2024/) | 论文 | 20 |
| 16 | [OpenVLA：一个开源的视觉-语言-动作模型](/entry/ent_paper_openvla_2024/) | 论文 | 19 |
| 17 | [你的视觉-语言-动作模型已具备路径偏离检测的注意力头](/entry/ent_paper_jeong_your_vision_language_action_mo_2026/) | 论文 | 19 |
| 18 | [LingBot-VLA｜务实的VLA基础模型](/entry/ent_paper_a_pragmatic_vla_foundation_mod_2026/) | 论文 | 18 |
| 19 | [面向人形机器人的几何感知预测安全滤波器：从泊松安全函数到 CBF 约束模型预测控制](/entry/ent_paper_bena_geometry_aware_predictive_safe_2025/) | 论文 | 18 |
| 20 | [基于关节力矩传感器和力/力矩传感器的腿式机器人接触感知](/entry/ent_paper_grinberg_contact_sensing_via_joint_torq_2025/) | 论文 | 18 |
| 21 | [拓普集团](/entry/ent_tier1_supplier_tuopujituan/) | Tier 1 供应商 | 18 |
| 22 | [Tesla Optimus](/entry/ent_robot_system_tesla_optimus/) | 机器人系统 | 17 |
| 23 | [Open X-Embodiment 数据集](/entry/ent_dataset_open_x_embodiment/) | 数据集 | 17 |
| 24 | [基于ROS的NimbRo-OP人形开放平台软件框架](/entry/ent_paper_allgeuer_a_ros_based_software_framework_2013/) | 论文 | 17 |
| 25 | [行星滚柱丝杠](/entry/ent_component_planetary_roller_screw/) | 零部件 | 17 |
| 26 | [有限元分析（FEA）](/entry/ent_method_fea_finite_element_analysis/) | 方法 | 17 |
| 27 | [RoboOmni：全模态上下文中的主动式机器人操作](/entry/ent_paper_roboomni_2025/) | 论文 | 16 |
| 28 | [LIBERO-Plus](/entry/ent_benchmark_libero_plus/) | 评测基准 | 16 |
| 29 | [Unitree G1人形机器人手臂基于物理的电力消耗模型辨识](/entry/ent_paper_deniz_identification_of_a_physics_ba_2026/) | 论文 | 16 |
| 30 | [人形机器人的类人驱动能力](/entry/ent_paper_sunbeam_human_level_actuation_for_huma_2025/) | 论文 | 16 |
| 31 | [基于专家洞见的稀土供应中断非动能战略威慑建模：一种仿真驱动的系统化框架](/entry/ent_paper_meng_expert_insight_based_modeling_2025/) | 论文 | 16 |
| 32 | [浮动基动力学](/entry/ent_formalism_floating_base_dynamics/) | 形式化方法 | 16 |
| 33 | [NVIDIA Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) | 零部件 | 15 |
| 34 | [基于物理信息神经网络与无迹卡尔曼滤波的人形机器人无传感器关节力矩估计](/entry/ent_paper_sorrentino_physics_informed_neural_networ_2025/) | 论文 | 15 |
| 35 | [基于CAD的高级机器人编程：应对不可预测环境](/entry/ent_paper_neto_high_level_robot_programming_b_2013/) | 论文 | 15 |
| 36 | [基于物理的锂离子电池模型连续谱综述](/entry/ent_paper_planella_a_continuum_of_physics_based_l_2022/) | 论文 | 15 |
| 37 | [零力矩点（ZMP）](/entry/ent_principle_zero_moment_point/) | 原理 | 15 |
| 38 | [人形机器人操作接口（HuMI）：无需机器人演示的全身操作](/entry/ent_paper_nai_humanoid_manipulation_interfac_2026/) | 论文 | 14 |
| 39 | [π0：用于通用机器人控制的视觉-语言-动作流模型](/entry/ent_paper_pi0_2024/) | 论文 | 14 |
| 40 | [BeyondMimic｜从运动跟踪到通过引导扩散的多样化人形控制](/entry/ent_paper_beyondmimic_from_motion_tracki_2025/) | 论文 | 14 |
| 41 | [LIBERO](/entry/ent_benchmark_libero/) | 评测基准 | 14 |
| 42 | [在基于VR的人机协作模拟中探索基于GPT的大型语言模型实现可变自主性](/entry/ent_paper_lakhnati_exploring_a_gpt_based_large_la_2024/) | 论文 | 14 |
| 43 | [Drive-WM：面向自动驾驶的多视角视觉预测与世界模型规划](/entry/ent_paper_wang_driving_into_the_future_multiv_2023/) | 论文 | 14 |
| 44 | [Gemini Robotics｜将人工智能带入物理世界](/entry/ent_paper_gemini_robotics_bringing_ai_in_2025/) | 论文 | 13 |
| 45 | [机器人中的现实鸿沟：挑战、解决方案与最佳实践](/entry/ent_paper_aljalbout_reality_gap_2025/) | 论文 | 13 |
| 46 | [面向人机工效协作负载提升的人形机器人设计优化](/entry/ent_paper_sartore_optimization_of_humanoid_robot_2022/) | 论文 | 13 |
| 47 | [满足 ISO/TS 15066 约束的能量罐控制框架](/entry/ent_paper_benzi_energy_tank_based_control_fram_2023/) | 论文 | 13 |
| 48 | [正运动学](/entry/ent_method_forward_kinematics/) | 方法 | 13 |
| 49 | [逆运动学](/entry/ent_method_inverse_kinematics/) | 方法 | 13 |
| 50 | [人形机器人在线平衡运动生成](/entry/ent_paper_ficht_online_balanced_motion_generat_2018/) | 论文 | 12 |
