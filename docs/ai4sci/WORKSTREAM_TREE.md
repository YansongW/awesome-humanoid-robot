# 工作流谱系树（长期 TODO）

> **Purpose**: 将 `docs/ai4sci/workstream_roadmap.md` 中的三维知识空间落地为可执行的 YAML 工作流清单。  
> **维护规则**: 每个叶子节点对应 `scripts/ai4sci_workstreams/` 下的一个 YAML 文件；执行完毕后把 `- [ ]` 改为 `- [x]`，并在提交信息中注明工作流名称。  
> **当前状态**: 4 个工作流已执行一轮，其余待建立或扩展。

---

## 1. 定义 / Definition

### 1.1 需求与用例
- [ ] `definition/use_cases/industrial_use_cases.yaml`
- [ ] `definition/use_cases/home_service_use_cases.yaml`
- [ ] `definition/use_cases/tco_business_models.yaml`

### 1.2 系统架构
- [ ] `definition/system_architecture/compute_architecture.yaml`
- [ ] `definition/system_architecture/sensor_architecture.yaml`
- [ ] `definition/system_architecture/power_thermal_architecture.yaml`

### 1.3 算法调研

#### 1.3.1 高层 AI
- [x] `definition/algorithm_survey/high_level_ai/vla.yaml`
- [ ] `definition/algorithm_survey/high_level_ai/vlm_for_robotics.yaml`
- [ ] `definition/algorithm_survey/high_level_ai/world_models.yaml`
- [ ] `definition/algorithm_survey/high_level_ai/wam.yaml`（Whole-Body Affordance / World Action Models）

#### 1.3.2 底层控制
- [ ] `definition/algorithm_survey/control/whole_body_control.yaml`
- [ ] `definition/algorithm_survey/control/model_predictive_control.yaml`
- [ ] `definition/algorithm_survey/control/force_position_control.yaml`
- [ ] `definition/algorithm_survey/control/impedance_admittance_control.yaml`
- [ ] `definition/algorithm_survey/control/traditional_control.yaml`（ZMP/DCM/Preview）

#### 1.3.3 学习范式
- [ ] `definition/algorithm_survey/learning/imitation_learning.yaml`
- [ ] `definition/algorithm_survey/learning/reinforcement_learning_locomotion.yaml`
- [ ] `definition/algorithm_survey/learning/sim_to_real.yaml`
- [ ] `definition/algorithm_survey/learning/manipulation_policies.yaml`
- [ ] `definition/algorithm_survey/learning/loco_manipulation.yaml`

---

## 2. 设计 / Design

### 2.1 硬件设计

#### 2.1.1 驱动 / Actuation
- [ ] `design/hardware/actuation/actuator_module_design.yaml`
- [ ] `design/hardware/actuation/motor_selection.yaml`
- [ ] `design/hardware/actuation/reducer_selection.yaml`
- [ ] `design/hardware/actuation/linear_actuators.yaml`
- [ ] `design/hardware/actuation/hand_actuators.yaml`

#### 2.1.2 感知 / Sensing
- [ ] `design/hardware/sensing/vision_sensors.yaml`
- [ ] `design/hardware/sensing/depth_3d_sensors.yaml`
- [ ] `design/hardware/sensing/lidar_for_humanoids.yaml`
- [ ] `design/hardware/sensing/imu_selection.yaml`
- [ ] `design/hardware/sensing/force_torque_sensors.yaml`
- [ ] `design/hardware/sensing/tactile_sensors.yaml`
- [ ] `design/hardware/sensing/encoder_technologies.yaml`

#### 2.1.3 电源 / Power
- [ ] `design/hardware/power/battery_cells.yaml`
- [ ] `design/hardware/power/bms_thermal.yaml`
- [ ] `design/hardware/power/charging_swapping.yaml`

#### 2.1.4 计算 / Compute
- [ ] `design/hardware/compute/edge_ai_compute.yaml`
- [ ] `design/hardware/compute/real_time_controllers.yaml`
- [ ] `design/hardware/compute/communication_buses.yaml`

#### 2.1.5 结构 / Structure
- [ ] `design/hardware/structure/structural_materials.yaml`
- [ ] `design/hardware/structure/lightweighting_topology.yaml`
- [ ] `design/hardware/structure/cable_routing_sealing.yaml`

### 2.2 软件与 AI 架构
- [ ] `design/software_ai/perception_stack.yaml`
- [ ] `design/software_ai/planning_architecture.yaml`
- [ ] `design/software_ai/control_stack.yaml`
- [ ] `design/software_ai/learning_deployment.yaml`

### 2.3 机械结构设计
- [ ] `design/mechanical/morphology_dof.yaml`
- [ ] `design/mechanical/kinematics_dynamics.yaml`
- [ ] `design/mechanical/dfx_design.yaml`

---

## 3. 校核规划 / Verification Planning

- [ ] `verification_planning/test_strategy.yaml`
- [ ] `verification_planning/safety_standards_mapping.yaml`
- [ ] `verification_planning/hil_sil_plan.yaml`
- [ ] `verification_planning/certification_roadmap.yaml`

---

## 4. MVP

- [ ] `mvp/works_like_prototype.yaml`
- [ ] `mvp/looks_like_prototype.yaml`
- [ ] `mvp/subsystem_demos.yaml`

---

## 5. 测试 / Testing

- [ ] `testing/joint_test_benches.yaml`
- [ ] `testing/balance_test_rigs.yaml`
- [ ] `testing/calibration_methods.yaml`
- [ ] `testing/environmental_testing.yaml`

---

## 6. EVT / Engineering Validation Test

- [ ] `evt/evt_functional_validation.yaml`
- [ ] `evt/component_qualification.yaml`
- [ ] `evt/thermal_mechanical_electrical.yaml`

---

## 7. DVT / Design Validation Test

- [ ] `dvt/design_freeze.yaml`
- [ ] `dvt/certification_pre_testing.yaml`
- [ ] `dvt/bom_cost_dvt.yaml`
- [ ] `dvt/dfm_dfa_validation.yaml`

---

## 8. PVT / Production Validation Test

- [ ] `pvt/production_tooling.yaml`
- [ ] `pvt/yield_stabilization.yaml`
- [ ] `pvt/eol_testing.yaml`
- [ ] `pvt/golden_sample.yaml`

---

## 9. 量产与爬坡 / Mass Production & Ramp

### 9.1 工厂与产线
- [ ] `mass_production/factory/factory_design.yaml`
- [ ] `mass_production/factory/line_balancing.yaml`
- [ ] `mass_production/factory/mes_plm_integration.yaml`

### 9.2 供应链
- [x] `mass_production/supply_chain/companies.yaml`（计划拆分为 OEM/Tier-1/Tier-2 子工作流）
- [ ] `mass_production/supply_chain/oem_ecosystem.yaml`
- [ ] `mass_production/supply_chain/tier1_suppliers.yaml`
- [ ] `mass_production/supply_chain/tier2_suppliers.yaml`
- [x] `mass_production/supply_chain/raw_materials.yaml`（计划细化为稀土/磁材、电池材料、结构材料）
- [ ] `mass_production/supply_chain/rare_earth_magnets.yaml`
- [ ] `mass_production/supply_chain/battery_materials.yaml`
- [ ] `mass_production/supply_chain/structural_materials.yaml`

### 9.3 成本与良率
- [ ] `mass_production/cost_yield/bom_cost_modeling.yaml`
- [ ] `mass_production/cost_yield/yield_optimization.yaml`
- [ ] `mass_production/cost_yield/learning_curve.yaml`

---

## 10. 数据系统 / Data Systems

- [ ] `data_systems/teleoperation_data.yaml`
- [ ] `data_systems/motion_capture_datasets.yaml`
- [ ] `data_systems/cross_embodiment_datasets.yaml`
- [ ] `data_systems/synthetic_data_generation.yaml`
- [ ] `data_systems/fleet_telemetry.yaml`
- [ ] `data_systems/data_governance.yaml`

---

## 11. Infra / 云 / 车队

- [ ] `infra_cloud_fleet/middleware/ros2_dds_middleware.yaml`
- [ ] `infra_cloud_fleet/middleware/rtos_real_time_linux.yaml`
- [ ] `infra_cloud_fleet/simulation/simulation_platforms.yaml`
- [ ] `infra_cloud_fleet/simulation/digital_twins.yaml`
- [ ] `infra_cloud_fleet/fleet/fleet_management.yaml`
- [ ] `infra_cloud_fleet/fleet/ota_updates.yaml`
- [ ] `infra_cloud_fleet/fleet/ci_cd_for_robots.yaml`

---

## 12. 质量与可靠性 / Quality & Reliability

- [ ] `quality_reliability/eol_reliability_screening.yaml`
- [ ] `quality_reliability/mtbf_mttr.yaml`
- [ ] `quality_reliability/traceability_spc.yaml`
- [ ] `quality_reliability/failure_analysis.yaml`

---

## 13. 安全与认证 / Safety & Certification

- [ ] `safety_certification/iso_13482.yaml`
- [ ] `safety_certification/iso_10218_15066.yaml`
- [ ] `safety_certification/eu_ai_act_machinery_reg.yaml`
- [ ] `safety_certification/cybersecurity_for_humanoids.yaml`
- [ ] `safety_certification/product_liability.yaml`

---

## 14. 应用与市场 / Applications & Markets

- [ ] `applications_markets/automotive_manufacturing.yaml`
- [ ] `applications_markets/logistics_warehousing.yaml`
- [ ] `applications_markets/healthcare_eldercare.yaml`
- [ ] `applications_markets/market_sizing_forecasts.yaml`

---

## 15. 政策与伦理 / Policy & Ethics

- [ ] `policy_ethics/data_privacy_humanoids.yaml`
- [ ] `policy_ethics/labor_market_impact.yaml`
- [ ] `policy_ethics/ethics_hri.yaml`
- [ ] `policy_ethics/regional_regulation.yaml`

---

## 16. 跨域关系 / Cross-Domain

- [x] `cross_domain/cross_domain_relationships.yaml`（持续提升覆盖度）
- [ ] `cross_domain/ai_to_hardware_requirements.yaml`
- [ ] `cross_domain/data_to_sim_real.yaml`
- [ ] `cross_domain/design_to_manufacturing_feedback.yaml`
