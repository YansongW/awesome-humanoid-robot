---
$id: ent_process_p10_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: External Force/Disturbance Estimation
  zh: 外力/扰动估计
  ko: 外力/扰动估计
summary:
  en: External force estimation response &lt;100 ms, steady-state error &lt;target
  zh: '- P10.1.3.1 输入梳理与目标量化 - 整理「外力/扰动估计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 外力估计响应 < 100 ms、稳态误差 < 目标
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
**方法 / 工具**：动量观测器、广义动量、卡尔曼滤波

**设计思考逻辑**：估计外部推力/拉力，用于鲁棒平衡与跌倒预测

**关键约束**：模型误差、延迟

**完成标准 / 输出物**：外力估计响应 < 100 ms、稳态误差 < 目标

**三级子任务与四级关键动作：**

- P10.1.3.1 输入梳理与目标量化
  - 整理「外力/扰动估计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P10.1.3.2 算法/控制方案设计
  - 基于「动量观测器、广义动量、卡尔曼滤波」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P10.1.3.3 算法实现与仿真验证
  - 将「外力/扰动估计」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P10.1.3.4 算法调参与性能验证
  - 对「外力/扰动估计」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P10.1.3.5 文档输出与下游交付
  - 输出「外力/扰动估计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Motion Control Algorithm Development and Verification (Motion Control)

## Content
**Method/Tool**: Momentum Observer, Generalized Momentum, Kalman Filter

**Design Logic**: Estimate external thrust/pull forces for robust balance and fall prediction

**Key Constraints**: Model error, latency

**Completion Criteria/Deliverables**: External force estimation response < 100 ms, steady-state error < target

**Three-Level Subtasks and Four-Level Key Actions:**

- P10.1.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "external force/disturbance estimation," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P10.1.3.2 Algorithm/Control Scheme Design
  - Establish a mathematical model or algorithm framework based on "momentum observer, generalized momentum, Kalman filter," form candidate schemes, evaluate stability, real-time performance, and scalability, and freeze the implementation path.
    - Develop at least 2 candidate schemes
    - Establish an evaluation matrix and quantify scores
    - Organize a review and freeze the scheme

- P10.1.3.3 Algorithm Implementation and Simulation Verification
  - Implement the "external force/disturbance estimation" algorithm in a simulation environment or with offline data, verifying functional correctness, real-time performance, and robustness.
    - Build a model/prototype and record key parameters
    - Execute simulation or prototype verification
    - Record anomalies and deviations

- P10.1.3.4 Algorithm Tuning and Performance Verification
  - Perform parameter tuning and boundary testing on the "external force/disturbance estimation" algorithm, verifying whether performance under typical/extreme operating conditions meets the indicators.
    - Develop a test/review plan and pass criteria
    - Execute tests and record raw data
    - Output a problem list and improvement measures

- P10.1.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "external force/disturbance estimation," update the ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents according to the template and cite raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 운동 제어 알고리즘 개발 및 검증 (Motion Control)

## 핵심 내용
**방법 / 도구**: 운동량 관측기, 일반화 운동량, 칼만 필터

**설계 사고 논리**: 외부 추력/견인력 추정을 통한 강건한 균형 및 낙하 예측

**핵심 제약 조건**: 모델 오차, 지연

**완료 기준 / 산출물**: 외력 추정 응답 < 100ms, 정상 상태 오차 < 목표

**3단계 하위 작업 및 4단계 핵심 조치:**

- P10.1.3.1 입력 정리 및 목표 정량화
  - 「외력/외란 추정」에 필요한 상위 입력, 참조 기준 및 자원을 정리하고, 완료 기준을 정량화된 수용 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 수용 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P10.1.3.2 알고리즘/제어 방식 설계
  - 「운동량 관측기, 일반화 운동량, 칼만 필터」를 기반으로 수학적 모델 또는 알고리즘 프레임워크를 구축하고, 후보 방안을 도출하며, 안정성, 실시간성 및 확장성을 평가하고 구현 경로를 확정한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스를 구축하고 정량적 점수 부여
    - 검토를 조직하고 방안 확정

- P10.1.3.3 알고리즘 구현 및 시뮬레이션 검증
  - 「외력/외란 추정」 알고리즘을 시뮬레이션 환경 또는 오프라인 데이터에서 구현하고, 기능 정확성, 실시간성 및 강건성을 검증한다.
    - 모델/프로토타입을 구축하고 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P10.1.3.4 알고리즘 튜닝 및 성능 검증
  - 「외력/외란 추정」 알고리즘에 대한 매개변수 최적화 및 경계 테스트를 수행하고, 일반/극한 작업 조건에서의 성능이 지표를 충족하는지 검증한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트를 수행하고 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P10.1.3.5 문서 출력 및 하위 전달
  - 「외력/외란 추정」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
