# 부록 A: 엔티티 및 관계 빠른 참조표

> 이 부록은 `scripts/build_appendices.py`를 통해 지식 그래프 데이터에서 자동 생성되었으며, KG 업데이트에 따라 갱신됩니다.

지식 그래프의 엔티티 유형, 관계 유형 및 핵심 엔티티 개요입니다.


## A.1 엔티티 유형 분포

| 유형 | 한국어 | 수량 |
|---|---|---|
| `paper` | 논문 | 1594 |
| `method` | 방법 | 210 |
| `report` | 보고서 | 86 |
| `component` | 부품 | 49 |
| `technology` | 기술 | 28 |
| `component_manufacturer` | 부품 제조사 | 19 |
| `concept` | 개념 | 17 |
| `software_platform` | 소프트웨어 플랫폼 | 16 |
| `robot_system` | 로봇 시스템 | 11 |
| `dataset` | 데이터셋 | 11 |
| `principle` | 원리 | 10 |
| `benchmark` | 평가 기준 | 9 |
| `company` | 회사 | 9 |
| `algorithm` | 알고리즘 | 9 |
| `formalism` | 형식적 방법 | 8 |
| `standard` | 표준 | 7 |
| `equation` | 방정식 | 7 |
| `foundation` | 기초 학문 | 5 |
| `material` | 재료 | 4 |
| `application_scenario` | 응용 시나리오 | 4 |
| `oem` | 완제품 제조사 | 3 |
| `tier1_supplier` | Tier 1 공급업체 | 3 |
| `operator` | 연산자 | 3 |
| `theorem` | 정리 | 2 |
| `tool_equipment` | 도구 장비 | 1 |
| `market_segment` | 시장 세분화 | 1 |
| **합계** | — | **2126** |

## A.2 관계 유형 분포

| 관계 유형 | 수량 |
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
| **합계** | **1063** |

## A.3 도메인 분포

| 도메인 | 엔티티 수 |
|---|---|
| 기초 학문 | 36 |
| 원자재 | 13 |
| 부품 | 358 |
| 제조 공정 | 83 |
| 조립·통합·테스트 | 38 |
| 양산 제조 | 81 |
| 설계 엔지니어링 | 400 |
| AI 모델 및 알고리즘 | 1595 |
| 소프트웨어 미들웨어 | 1029 |
| 데이터 및 데이터셋 | 118 |
| 평가 기준 | 84 |
| 응용 및 시장 | 312 |
| 정책·규제·윤리 | 41 |

## A.4 핵심 엔터티 Top 50 (관계 수 기준)

| 순위 | 개체 | 유형 | 관계 수 |
|---|---|---|---|
| 1 | [표준 2차 계획법(QP)](/entry/ent_qp_standard_form/) | 형식화 방법 | 43 |
| 2 | [DIAL｜종단간 VLA를 통한 잠재 세계 모델링으로 의도와 행동 분리](/entry/ent_paper_dial_decoupling_intent_and_act_2026/) | 논문 | 35 |
| 3 | [능동 공간 뇌와 일반화 가능한 행동 소뇌를 통한 휴머노이드 전신 조작](/entry/ent_paper_liang_humanoid_whole_body_manipulati_2026/) | 논문 | 31 |
| 4 | [HumanoidBench](/entry/ent_benchmark_humanoidbench/) | 평가 기준 | 24 |
| 5 | [GPT 기반 대규모 언어 모델을 활용한 가상 현실 인간-로봇 팀 협업 시뮬레이션의 가변 자율성 탐구](/entry/ent_paper_lakhnati_exploring_a_gpt_based_large_la_2023/) | 논문 | 23 |
| 6 | [로봇 비전-언어-행동: 데이터셋, 기준 및 데이터 엔진 개요](/entry/ent_paper_wang_vla_survey_2026/) | 논문 | 21 |
| 7 | [Unitree H1 휴머노이드 로봇](/entry/ent_robot_unitree_h1_humanoid_robot_2024/) | 로봇 시스템 | 21 |
| 8 | [휴머노이드 조작 ACT 모방 학습에서 능동 스테레오 카메라가 다중 센서 설정보다 우수](/entry/ent_paper_active_stereo_camera_outperfor_2026/) | 논문 | 21 |
| 9 | [다단계 강화 학습 기반 휴머노이드 전신 배드민턴 운동](/entry/ent_paper_liu_humanoid_whole_body_badminton_2026/) | 논문 | 21 |
| 10 | [자계 방향 제어(FOC)](/entry/ent_method_foc_motor_control/) | 방법 | 21 |
| 11 | [세계 행동 모델: 구현 지능의 다음 프론티어](/entry/ent_paper_wang_wam_survey_2026/) | 논문 | 20 |
| 12 | [AgiBot World Colosseo｜확장 가능하고 지능적인 구현 시스템을 위한 대규모 조작 플랫폼](/entry/ent_paper_agibot_world_colosseo_a_large_2025/) | 논문 | 20 |
| 13 | [로봇이 로봇을 훈련하다: 휴머노이드 로봇의 자동 실제 세계 정책 적응 및 학습](/entry/ent_paper_hu_robot_trains_robot_automatic_r_2025/) | 논문 | 20 |
| 14 | [RUKA: 학습을 통한 휴머노이드 손 로봇 디자인 재고](/entry/ent_paper_zorin_ruka_rethinking_the_design_of_2025/) | 논문 | 20 |
| 15 | [무향 칼만 필터 기반 휴머노이드 로봇의 관절 토크 센서 없는 토크 추정](/entry/ent_paper_sorrentino_ukf_based_sensor_fusion_for_jo_2024/) | 논문 | 20 |
| 16 | [OpenVLA: 오픈소스 비전-언어-행동 모델](/entry/ent_paper_openvla_2024/) | 논문 | 19 |
| 17 | [당신의 비전-언어-행동 모델은 이미 경로 이탈 감지를 위한 주의 헤드를 갖추고 있다](/entry/ent_paper_jeong_your_vision_language_action_mo_2026/) | 논문 | 19 |
| 18 | [LingBot-VLA｜실용적인 VLA 기반 모델](/entry/ent_paper_a_pragmatic_vla_foundation_mod_2026/) | 논문 | 18 |
| 19 | [휴머노이드 로봇을 위한 기하학 인식 예측 안전 필터: 푸아송 안전 함수에서 CBF 제약 모델 예측 제어까지](/entry/ent_paper_bena_geometry_aware_predictive_safe_2025/) | 논문 | 18 |
| 20 | [관절 토크 센서 및 힘/토크 센서 기반 다리 로봇 접촉 감지](/entry/ent_paper_grinberg_contact_sensing_via_joint_torq_2025/) | 논문 | 18 |
| 21 | [탑 그룹](/entry/ent_tier1_supplier_tuopujituan/) | Tier 1 공급업체 | 18 |
| 22 | [Tesla Optimus](/entry/ent_robot_system_tesla_optimus/) | 로봇 시스템 | 17 |
| 23 | [Open X-Embodiment 데이터셋](/entry/ent_dataset_open_x_embodiment/) | 데이터셋 | 17 |
| 24 | [ROS 기반 NimbRo-OP 휴머노이드 개방형 플랫폼 소프트웨어 프레임워크](/entry/ent_paper_allgeuer_a_ros_based_software_framework_2013/) | 논문 | 17 |
| 25 | [행성 롤러 스크류](/entry/ent_component_planetary_roller_screw/) | 부품 | 17 |
| 26 | [유한 요소 해석(FEA)](/entry/ent_method_fea_finite_element_analysis/) | 방법 | 17 |
| 27 | [RoboOmni: 전모달 컨텍스트에서의 능동 로봇 조작](/entry/ent_paper_roboomni_2025/) | 논문 | 16 |
| 28 | [LIBERO-Plus](/entry/ent_benchmark_libero_plus/) | 평가 기준 | 16 |
| 29 | [Unitree G1 휴머노이드 로봇 팔의 물리 기반 전력 소비 모델 식별](/entry/ent_paper_deniz_identification_of_a_physics_ba_2026/) | 논문 | 16 |
| 30 | [휴머노이드 로봇의 인간 수준 구동 능력](/entry/ent_paper_sunbeam_human_level_actuation_for_huma_2025/) | 논문 | 16 |
| 31 | [전문가 통찰 기반 희토류 공급 중단 비군사 전략 억제 모델링: 시뮬레이션 기반 체계적 프레임워크](/entry/ent_paper_meng_expert_insight_based_modeling_2025/) | 논문 | 16 |
| 32 | [부동 기반 동역학](/entry/ent_formalism_floating_base_dynamics/) | 형식화 방법 | 16 |
| 33 | [NVIDIA Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) | 부품 | 15 |
| 34 | [물리 정보 신경망과 무향 칼만 필터 기반 휴머노이드 로봇의 무센서 관절 토크 추정](/entry/ent_paper_sorrentino_physics_informed_neural_networ_2025/) | 논문 | 15 |
| 35 | [CAD 기반 고급 로봇 프로그래밍: 예측 불가능한 환경 대응](/entry/ent_paper_neto_high_level_robot_programming_b_2013/) | 논문 | 15 |
| 36 | [물리 기반 리튬 이온 배터리 모델의 연속 스펙트럼 개요](/entry/ent_paper_planella_a_continuum_of_physics_based_l_2022/) | 논문 | 15 |
| 37 | [영점 모멘트(ZMP)](/entry/ent_principle_zero_moment_point/) | 원리 | 15 |
| 38 | [휴머노이드 조작 인터페이스(HuMI): 로봇 시연 없는 전신 조작](/entry/ent_paper_nai_humanoid_manipulation_interfac_2026/) | 논문 | 14 |
| 39 | [π0: 범용 로봇 제어를 위한 비전-언어-행동 흐름 모델](/entry/ent_paper_pi0_2024/) | 논문 | 14 |
| 40 | [BeyondMimic｜모션 추적에서 유도 확산을 통한 다양한 휴머노이드 제어까지](/entry/ent_paper_beyondmimic_from_motion_tracki_2025/) | 논문 | 14 |
| 41 | [LIBERO](/entry/ent_benchmark_libero/) | 평가 기준 | 14 |
| 42 | [VR 기반 인간-로봇 협업 시뮬레이션에서 GPT 기반 대규모 언어 모델을 통한 가변 자율성 구현 탐구](/entry/ent_paper_lakhnati_exploring_a_gpt_based_large_la_2024/) | 논문 | 14 |
| 43 | [Drive-WM: 자율 주행을 위한 다중 시점 비전 예측 및 세계 모델 계획](/entry/ent_paper_wang_driving_into_the_future_multiv_2023/) | 논문 | 14 |
| 44 | [Gemini Robotics｜인공지능을 물리적 세계로](/entry/ent_paper_gemini_robotics_bringing_ai_in_2025/) | 논문 | 13 |
| 45 | [로봇의 현실 격차: 도전 과제, 해결책 및 모범 사례](/entry/ent_paper_aljalbout_reality_gap_2025/) | 논문 | 13 |
| 46 | [인간-로봇 협업 부하 리프팅을 위한 휴머노이드 로봇 설계 최적화](/entry/ent_paper_sartore_optimization_of_humanoid_robot_2022/) | 논문 | 13 |
| 47 | [ISO/TS 15066 제약 조건을 충족하는 에너지 탱크 기반 제어 프레임워크](/entry/ent_paper_benzi_energy_tank_based_control_fram_2023/) | 논문 | 13 |
| 48 | [정기구학](/entry/ent_method_forward_kinematics/) | 방법 | 13 |
| 49 | [역기구학](/entry/ent_method_inverse_kinematics/) | 방법 | 13 |
| 50 | [휴머노이드 로봇의 온라인 균형 동작 생성](/entry/ent_paper_ficht_online_balanced_motion_generat_2018/) | 논문 | 12 |
