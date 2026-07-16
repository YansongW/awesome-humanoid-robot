# AI4Sci 工作流清单（按真实目录结构生成）

> **⚠️ 当前状态：legacy / paused**。AI4Sci 摄取工作流（`scripts/ai4sci_lib/` + `scripts/ai4sci_workstreams/` + `scripts/ai4sci_*.py`）目前处于暂停状态，日常摄取已由 `scripts/ingestion/` 统一接管（见 `docs/ingestion/README.md`）。本清单仅作为历史执行记录与后续重启时的任务索引保留。
>
> **关系挂接纪律（2026-07 修复）**：LLM 产出的 relationship / related_entities 的 `target_id` 必须逐字取自提示词中注入的候选实体清单（来自 `research/**/*.md` 中真实存在的实体，按论文 primary_domain 过滤、上限 80 个）；产出后代码侧再次校验，凡 `target_id` 不在真实实体集合中的关系一律丢弃，并在 review_notes 记录 `dropped dangling target_id: xxx`。禁止为不存在的实体编造 target_id。
>
> **维护规则**：每个叶子节点对应 `scripts/ai4sci_workstreams/` 下的一个 YAML 文件。`[x]` 表示该工作流在 `.staging/workstreams/<name>/logs/summary.json` 中已有成功产出；`[ ]` 表示未执行或无成功产出。本文件于 2026-07-16 按目录实况重新统计生成。

---

## 1. 定义 / Definition

### 1.1 `definition/algorithm_survey/control`

- [x] `definition/algorithm_survey/control/force_position_control.yaml`
- [x] `definition/algorithm_survey/control/impedance_admittance_control.yaml`
- [x] `definition/algorithm_survey/control/model_predictive_control.yaml`
- [x] `definition/algorithm_survey/control/traditional_control.yaml`
- [x] `definition/algorithm_survey/control/whole_body_control.yaml`

### 1.2 `definition/algorithm_survey/high_level_ai`

- [x] `definition/algorithm_survey/high_level_ai/vla.yaml`
- [x] `definition/algorithm_survey/high_level_ai/vlm_for_robotics.yaml`
- [x] `definition/algorithm_survey/high_level_ai/wam.yaml`
- [x] `definition/algorithm_survey/high_level_ai/world_models.yaml`

### 1.3 `definition/algorithm_survey/learning`

- [x] `definition/algorithm_survey/learning/imitation_learning.yaml`
- [x] `definition/algorithm_survey/learning/loco_manipulation.yaml`
- [x] `definition/algorithm_survey/learning/manipulation_policies.yaml`
- [x] `definition/algorithm_survey/learning/reinforcement_learning_locomotion.yaml`
- [x] `definition/algorithm_survey/learning/sim_to_real.yaml`

### 1.4 `definition/system_architecture`

- [x] `definition/system_architecture/compute_architecture.yaml`
- [x] `definition/system_architecture/power_thermal_architecture.yaml`
- [x] `definition/system_architecture/sensor_architecture.yaml`

### 1.5 `definition/use_cases`

- [x] `definition/use_cases/home_service_use_cases.yaml`
- [x] `definition/use_cases/industrial_use_cases.yaml`
- [ ] `definition/use_cases/tco_business_models.yaml`

---

## 2. 设计 / Design

### 2.1 `design/hardware/actuation`

- [x] `design/hardware/actuation/actuator_module_design.yaml`
- [x] `design/hardware/actuation/hand_actuators.yaml`
- [x] `design/hardware/actuation/linear_actuators.yaml`
- [x] `design/hardware/actuation/motor_selection.yaml`
- [x] `design/hardware/actuation/reducer_selection.yaml`
- [ ] `design/hardware/actuation/tactile_sensing_humanoid_hands.yaml`

### 2.2 `design/hardware/compute`

- [x] `design/hardware/compute/communication_buses.yaml`
- [ ] `design/hardware/compute/edge_ai_compute.yaml`
- [x] `design/hardware/compute/edge_compute.yaml`
- [x] `design/hardware/compute/real_time_controllers.yaml`

### 2.3 `design/hardware/power`

- [ ] `design/hardware/power/battery_cells.yaml`
- [x] `design/hardware/power/bms_thermal.yaml`
- [x] `design/hardware/power/charging_swapping.yaml`

### 2.4 `design/hardware/sensing`

- [x] `design/hardware/sensing/cameras_vision.yaml`
- [ ] `design/hardware/sensing/depth_3d_sensors.yaml`
- [ ] `design/hardware/sensing/encoder_technologies.yaml`
- [x] `design/hardware/sensing/force_torque_sensors.yaml`
- [x] `design/hardware/sensing/imu_inertial_sensors.yaml`
- [x] `design/hardware/sensing/imu_selection.yaml`
- [x] `design/hardware/sensing/lidar_for_humanoids.yaml`
- [x] `design/hardware/sensing/tactile_sensors.yaml`
- [x] `design/hardware/sensing/vision_sensors.yaml`

### 2.5 `design/hardware/structure`

- [x] `design/hardware/structure/cable_routing_sealing.yaml`
- [x] `design/hardware/structure/lightweighting_topology.yaml`
- [x] `design/hardware/structure/structural_materials.yaml`

### 2.6 `design/mechanical`

- [x] `design/mechanical/dfx_design.yaml`
- [ ] `design/mechanical/kinematics_dynamics.yaml`
- [ ] `design/mechanical/morphology_dof.yaml`

### 2.7 `design/software_ai`

- [x] `design/software_ai/control_stack.yaml`
- [x] `design/software_ai/learning_deployment.yaml`
- [x] `design/software_ai/perception_stack.yaml`
- [x] `design/software_ai/planning_architecture.yaml`

---

## 3. 校核规划 / Verification Planning

- [ ] `verification_planning/certification_roadmap.yaml`
- [ ] `verification_planning/hil_sil_plan.yaml`
- [ ] `verification_planning/safety_standards_mapping.yaml`
- [ ] `verification_planning/test_strategy.yaml`

---

## 4. MVP

- [ ] `mvp/looks_like_prototype.yaml`
- [ ] `mvp/subsystem_demos.yaml`
- [ ] `mvp/works_like_prototype.yaml`

---

## 5. 测试 / Testing

- [ ] `testing/balance_test_rigs.yaml`
- [ ] `testing/calibration_methods.yaml`
- [ ] `testing/environmental_testing.yaml`
- [ ] `testing/joint_test_benches.yaml`

---

## 6. EVT / 工程验证

- [x] `evt/component_qualification.yaml`
- [x] `evt/evt_functional_validation.yaml`
- [x] `evt/thermal_mechanical_electrical.yaml`

---

## 7. DVT / 设计验证

- [x] `dvt/bom_cost_dvt.yaml`
- [x] `dvt/certification_pre_testing.yaml`
- [x] `dvt/design_freeze.yaml`
- [x] `dvt/dfm_dfa_validation.yaml`

---

## 8. PVT / 生产验证

- [ ] `pvt/eol_testing.yaml`
- [ ] `pvt/golden_sample.yaml`
- [ ] `pvt/production_tooling.yaml`
- [ ] `pvt/yield_stabilization.yaml`

---

## 9. 制造工艺 / Manufacturing

### 9.1 `manufacturing/processes`

- [ ] `manufacturing/processes/actuator_assembly.yaml`
- [ ] `manufacturing/processes/precision_machining.yaml`

### 9.2 `manufacturing/testing`

- [x] `manufacturing/testing/functional_safety.yaml`
- [x] `manufacturing/testing/system_integration_test.yaml`

---

## 10. 量产与爬坡 / Mass Production & Ramp

### 10.1 `mass_production/cost_yield`

- [x] `mass_production/cost_yield/bom_cost_modeling.yaml`
- [ ] `mass_production/cost_yield/learning_curve.yaml`
- [ ] `mass_production/cost_yield/yield_optimization.yaml`

### 10.2 `mass_production/factory`

- [ ] `mass_production/factory/factory_design.yaml`
- [ ] `mass_production/factory/line_balancing.yaml`
- [ ] `mass_production/factory/mes_plm_integration.yaml`

### 10.3 `mass_production/quality_control`

- [x] `mass_production/quality_control/quality_control.yaml`

### 10.4 `mass_production/supply_chain`

- [ ] `mass_production/supply_chain/battery_materials.yaml`
- [x] `mass_production/supply_chain/companies.yaml`
- [ ] `mass_production/supply_chain/critical_minerals.yaml`
- [x] `mass_production/supply_chain/global_supply_chain_risk.yaml`
- [ ] `mass_production/supply_chain/oem_ecosystem.yaml`
- [x] `mass_production/supply_chain/rare_earth_magnets.yaml`
- [x] `mass_production/supply_chain/raw_materials.yaml`
- [ ] `mass_production/supply_chain/structural_materials.yaml`（已废弃，保留份见文件头注释）
- [ ] `mass_production/supply_chain/tier1_suppliers.yaml`
- [ ] `mass_production/supply_chain/tier2_suppliers.yaml`

---

## 11. 数据系统 / Data Systems

- [x] `data_systems/cross_embodiment_datasets.yaml`
- [x] `data_systems/data_governance.yaml`
- [x] `data_systems/fleet_telemetry.yaml`
- [x] `data_systems/motion_capture_datasets.yaml`
- [x] `data_systems/synthetic_data_generation.yaml`
- [x] `data_systems/teleoperation_data.yaml`

---

## 12. Infra / 云 / 车队

### 12.1 `infra_cloud_fleet/fleet`

- [x] `infra_cloud_fleet/fleet/ci_cd_for_robots.yaml`
- [ ] `infra_cloud_fleet/fleet/fleet_management.yaml`
- [x] `infra_cloud_fleet/fleet/ota_updates.yaml`

### 12.2 `infra_cloud_fleet/middleware`

- [x] `infra_cloud_fleet/middleware/ros2_dds_middleware.yaml`
- [x] `infra_cloud_fleet/middleware/rtos_real_time_linux.yaml`

### 12.3 `infra_cloud_fleet/simulation`

- [x] `infra_cloud_fleet/simulation/digital_twins.yaml`
- [ ] `infra_cloud_fleet/simulation/simulation_platforms.yaml`

### 12.4 `infra_cloud_fleet/software_middleware`

- [ ] `infra_cloud_fleet/software_middleware/ros2_middleware.yaml`

---

## 13. 质量与可靠性 / Quality & Reliability

- [ ] `quality_reliability/eol_reliability_screening.yaml`
- [ ] `quality_reliability/failure_analysis.yaml`
- [ ] `quality_reliability/mtbf_mttr.yaml`
- [ ] `quality_reliability/traceability_spc.yaml`

---

## 14. 安全与认证 / Safety & Certification

- [ ] `safety_certification/cybersecurity_for_humanoids.yaml`
- [ ] `safety_certification/eu_ai_act_machinery_reg.yaml`
- [ ] `safety_certification/iso_10218_15066.yaml`
- [x] `safety_certification/iso_13482.yaml`
- [ ] `safety_certification/product_liability.yaml`

---

## 15. 应用 / Applications

### 15.1 `applications/domestic`

- [x] `applications/domestic/home_assistive.yaml`

### 15.2 `applications/healthcare`

- [ ] `applications/healthcare/assistive_rehabilitation.yaml`

### 15.3 `applications/industrial`

- [ ] `applications/industrial/industrial_inspection.yaml`

### 15.4 `applications/logistics`

- [ ] `applications/logistics/warehouse.yaml`

---

## 16. 应用与市场 / Applications & Markets

- [x] `applications_markets/automotive_manufacturing.yaml`
- [x] `applications_markets/healthcare_eldercare.yaml`
- [x] `applications_markets/logistics_warehousing.yaml`
- [x] `applications_markets/market_sizing_forecasts.yaml`

---

## 17. 政策法规 / Policy & Regulation

- [x] `policy_regulation/safety_standards.yaml`

---

## 18. 政策与伦理 / Policy & Ethics

- [ ] `policy_ethics/data_privacy_humanoids.yaml`
- [ ] `policy_ethics/ethics_hri.yaml`
- [ ] `policy_ethics/labor_market_impact.yaml`
- [ ] `policy_ethics/regional_regulation.yaml`

---

## 19. 跨域关系 / Cross-Domain

- [x] `cross_domain/ai_to_hardware_requirements.yaml`
- [x] `cross_domain/cross_domain.yaml`
- [x] `cross_domain/data_to_sim_real.yaml`
- [x] `cross_domain/design_to_manufacturing_feedback.yaml`

---

## 20. 基础学科 / Foundations

### 20.1 `foundations/chemistry`

- [x] `foundations/chemistry/battery_electrochemistry.yaml`
- [x] `foundations/chemistry/electrochemistry.yaml`
- [x] `foundations/chemistry/polymer_materials.yaml`
- [ ] `foundations/chemistry/rare_earth_magnet_chemistry.yaml`
- [ ] `foundations/chemistry/surface_treatment.yaml`

### 20.2 `foundations/computer_science`

- [x] `foundations/computer_science/algorithms_data_structures.yaml`
- [x] `foundations/computer_science/distributed_systems.yaml`
- [x] `foundations/computer_science/machine_learning_theory.yaml`
- [x] `foundations/computer_science/real_time_systems.yaml`

### 20.3 `foundations/economics`

- [x] `foundations/economics/cost_analysis.yaml`
- [x] `foundations/economics/game_theory.yaml`
- [x] `foundations/economics/industrial_organization.yaml`

### 20.4 `foundations/mathematics`

- [x] `foundations/mathematics/convex_optimization.yaml`
- [x] `foundations/mathematics/differential_geometry.yaml`
- [x] `foundations/mathematics/graph_theory.yaml`
- [x] `foundations/mathematics/linear_algebra.yaml`
- [x] `foundations/mathematics/multivariable_calculus.yaml`
- [x] `foundations/mathematics/numerical_analysis.yaml`
- [x] `foundations/mathematics/optimal_control.yaml`
- [x] `foundations/mathematics/probability_statistics.yaml`
- [x] `foundations/mathematics/stochastic_calculus.yaml`

### 20.5 `foundations/or_ie`

- [x] `foundations/or_ie/inventory_management.yaml`
- [x] `foundations/or_ie/reliability_engineering.yaml`
- [x] `foundations/or_ie/scheduling_optimization.yaml`
- [x] `foundations/or_ie/statistical_process_control.yaml`

### 20.6 `foundations/physics`

- [x] `foundations/physics/contact_mechanics.yaml`
- [x] `foundations/physics/electromagnetism.yaml`
- [ ] `foundations/physics/materials_mechanics.yaml`
- [x] `foundations/physics/rigid_body_dynamics.yaml`
- [ ] `foundations/physics/thermodynamics.yaml`

---

## 21. Builder Track / 0→1 造机路线图

配合 `wiki/docs/roadmap/` 的 0→1 造人形机器人路线图（基础筑基 → 单关节 → 双足平台 → 完整人形），检索词与相关性语境面向动手造机器人的新手。

- [ ] `builder_track/open_source_humanoid_hardware.yaml`
- [ ] `builder_track/actuator_selection.yaml`
- [ ] `builder_track/biped_locomotion_control.yaml`
- [ ] `builder_track/sim_to_real_setup.yaml`

---

## 22. 精选来源 / Curated

- [x] `curated/wechat_161/contact_planning_visual_feedback_curated.yaml`
- [x] `curated/wechat_161/egocentric_video_learning_curated.yaml`
- [x] `curated/wechat_161/generative_motion_language_planning_curated.yaml`
- [x] `curated/wechat_161/hardware_perception_deployment_curated.yaml`
- [x] `curated/wechat_161/mobile_manipulation_interfaces_curated.yaml`
- [x] `curated/wechat_161/mocap_human_video_action_planning_curated.yaml`
- [x] `curated/wechat_161/teleoperation_data_collection_curated.yaml`
- [x] `curated/wechat_161/vision_driven_loco_manipulation_curated.yaml`
- [x] `curated/wechat_161/vla_world_models_curated.yaml`
- [x] `curated/wechat_161/whole_body_control_curated.yaml`

---

**统计**：共 179 个 YAML 配置（workstream 名称全部唯一），其中 117 个已有成功产出记录。
