---
$id: ent_process_p10_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: IMU and joint encoder fusion
  zh: IMU 与关节编码器融合
  ko: IMU 与关节编码器融合
summary:
  en: State estimator, measured trajectory error &lt;target, standing drift controllable
  zh: '- P10.1.1.1 输入梳理与目标量化 - 整理「IMU 与关节编码器融合」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 状态估计器、实测轨迹误差 < 目标、站立漂移可控
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- process
- knowledge
tags: []
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py. English name/summary machine-translated
    from Chinese by scripts/backfill_en_translations.py.
sources:
- id: wbs_v3_report
  type: report
  title: 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）
  date: '2026-06-27'
theoretical_depth:
- method
---


## 概述
**所属阶段/工作包**：运动控制算法开发与验证（Motion Control）

## 核心内容
**方法 / 工具**：EKF/UKF/Madgwick、零速修正、关节运动学积分

**设计思考逻辑**：实时估计质心位置、速度、姿态；是平衡控制的基础

**关键约束**：传感器延迟、协方差调参、足端打滑

**完成标准 / 输出物**：状态估计器、实测轨迹误差 < 目标、站立漂移可控

**三级子任务与四级关键动作：**

- P10.1.1.1 输入梳理与目标量化
  - 整理「IMU 与关节编码器融合」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P10.1.1.2 方案/方法设计
  - 针对「IMU 与关节编码器融合」制定实施方法或候选方案，使用「EKF/UKF/Madgwick、零速修正、关节运动学积分」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P10.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「IMU 与关节编码器融合」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P10.1.1.4 验证与问题闭环
  - 对「IMU 与关节编码器融合」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P10.1.1.5 文档输出与下游交付
  - 输出「IMU 与关节编码器融合」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Motion Control Algorithm Development and Verification (Motion Control)

## Content
**Methods/Tools**: EKF/UKF/Madgwick, Zero-Velocity Update, Joint Kinematics Integration

**Design Thinking Logic**: Real-time estimation of center of mass position, velocity, and attitude; serves as the foundation for balance control

**Key Constraints**: Sensor latency, covariance tuning, foot slippage

**Completion Criteria/Deliverables**: State estimator, measured trajectory error < target, standing drift controllable

**Level-3 Subtasks and Level-4 Key Actions:**

- P10.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "IMU and Joint Encoder Fusion," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P10.1.1.2 Scheme/Method Design
  - Develop implementation methods or candidate schemes for "IMU and Joint Encoder Fusion," using "EKF/UKF/Madgwick, Zero-Velocity Update, Joint Kinematics Integration" for demonstration, and clarify the technical roadmap and resource requirements.
    - Generate at least two candidate schemes
    - Establish an evaluation matrix with quantitative scoring
    - Organize a review and freeze the scheme

- P10.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "IMU and Joint Encoder Fusion" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P10.1.1.4 Verification and Issue Closure
  - Verify the output of "IMU and Joint Encoder Fusion," check whether it meets completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P10.1.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "IMU and Joint Encoder Fusion," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 운동 제어 알고리즘 개발 및 검증 (Motion Control)

## 핵심 내용
**방법 / 도구**: EKF/UKF/Madgwick, 제로 속도 보정, 관절 운동학 적분

**설계 사고 논리**: 실시간으로 질량 중심 위치, 속도, 자세 추정; 균형 제어의 기초

**핵심 제약 조건**: 센서 지연, 공분산 파라미터 튜닝, 발끝 미끄러짐

**완료 기준 / 산출물**: 상태 추정기, 실측 궤적 오차 < 목표, 정지 시 드리프트 제어 가능

**3단계 하위 작업 및 4단계 핵심 조치:**

- P10.1.1.1 입력 정리 및 목표 정량화
  - 「IMU와 관절 엔코더 융합」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P10.1.1.2 방안/방법 설계
  - 「IMU와 관절 엔코더 융합」에 대한 실행 방법 또는 후보 방안을 수립하고, 「EKF/UKF/Madgwick, 제로 속도 보정, 관절 운동학 적분」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스를 구축하고 정량적으로 점수화
    - 검토를 조직하고 방안을 확정

- P10.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「IMU와 관절 엔코더 융합」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품을 구축하고 핵심 파라미터를 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P10.1.1.4 검증 및 문제 종결
  - 「IMU와 관절 엔코더 융합」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트를 수행하고 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P10.1.1.5 문서 출력 및 하위 전달
  - 「IMU와 관절 엔코더 융합」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
