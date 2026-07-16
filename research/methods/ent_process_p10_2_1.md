---
$id: ent_process_p10_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Standing and Anti-Interference Balance Control
  zh: 站立与抗扰平衡控制
  ko: 站立与抗扰平衡控制
summary:
  en: Video of the standing anti-interference physical prototype; its recovery capability meets the specified performance
    criteria.
  zh: '- P10.2.1.1 输入梳理与目标量化 - 整理「站立与抗扰平衡控制」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 站立抗扰实物视频、恢复能力满足指标
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
**方法 / 工具**：LQR、MPC、ZMP/Capture Point、角动量控制

**设计思考逻辑**：双足站立与抗扰是核心安全功能；MPC 可统一处理约束

**关键约束**：实时求解频率 ≥ 100 Hz、关节极限

**完成标准 / 输出物**：站立抗扰实物视频、恢复能力满足指标

**三级子任务与四级关键动作：**

- P10.2.1.1 输入梳理与目标量化
  - 整理「站立与抗扰平衡控制」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P10.2.1.2 算法/控制方案设计
  - 基于「LQR、MPC、ZMP/Capture Point、角动量控制」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P10.2.1.3 算法实现与仿真验证
  - 将「站立与抗扰平衡控制」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P10.2.1.4 算法调参与性能验证
  - 对「站立与抗扰平衡控制」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P10.2.1.5 文档输出与下游交付
  - 输出「站立与抗扰平衡控制」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Motion Control Algorithm Development and Verification (Motion Control)

## Content
**Methods/Tools**: LQR, MPC, ZMP/Capture Point, Angular Momentum Control

**Design Logic**: Bipedal standing and disturbance rejection are core safety functions; MPC can handle constraints uniformly

**Key Constraints**: Real-time solving frequency ≥ 100 Hz, joint limits

**Completion Criteria/Deliverables**: Physical video of standing disturbance rejection, recovery capability meeting indicators

**Three-Level Subtasks and Four-Level Key Actions:**

- P10.2.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "standing and disturbance rejection balance control," convert completion criteria into quantifiable acceptance indicators, and clarify the Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P10.2.1.2 Algorithm/Control Scheme Design
  - Establish a mathematical model or algorithm framework based on "LQR, MPC, ZMP/Capture Point, Angular Momentum Control," form candidate schemes, evaluate stability, real-time performance, and scalability, and freeze the implementation path.
    - Develop no fewer than 2 candidate schemes
    - Establish an evaluation matrix and quantify scores
    - Organize a review and freeze the scheme

- P10.2.1.3 Algorithm Implementation and Simulation Verification
  - Implement the algorithm for "standing and disturbance rejection balance control" in a simulation environment or with offline data, verifying functional correctness, real-time performance, and robustness.
    - Build a model/prototype and record key parameters
    - Execute simulation or prototype verification
    - Record anomalies and deviations

- P10.2.1.4 Algorithm Tuning and Performance Verification
  - Perform parameter tuning and boundary testing for the "standing and disturbance rejection balance control" algorithm, verifying whether performance under typical/extreme conditions meets indicators.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P10.2.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "standing and disturbance rejection balance control," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**：운동 제어 알고리즘 개발 및 검증 (Motion Control)

## 핵심 내용
**방법 / 도구**：LQR, MPC, ZMP/Capture Point, 각운동량 제어

**설계 사고 논리**：이족 보행 및 외란 저항은 핵심 안전 기능이며, MPC는 제약 조건을 통합 처리 가능

**핵심 제약 조건**：실시간 해결 주파수 ≥ 100 Hz, 관절 한계

**완료 기준 / 산출물**：서 있는 상태에서 외란 저항을 보여주는 실제 영상, 회복 능력이 지표 충족

**3단계 하위 작업 및 4단계 핵심 조치：**

- P10.2.1.1 입력 정리 및 목표 정량화
  - 「서 있는 상태 및 외란 저항 균형 제어」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P10.2.1.2 알고리즘/제어 방식 설계
  - 「LQR, MPC, ZMP/Capture Point, 각운동량 제어」를 기반으로 수학적 모델 또는 알고리즘 프레임워크를 구축하여 후보 방안을 형성하고, 안정성, 실시간성 및 확장성을 평가하며, 구현 경로를 확정함.
    - 2개 이상의 후보 방안 형성
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P10.2.1.3 알고리즘 구현 및 시뮬레이션 검증
  - 「서 있는 상태 및 외란 저항 균형 제어」의 알고리즘을 시뮬레이션 환경 또는 오프라인 데이터에서 구현하여 기능 정확성, 실시간성 및 강건성을 검증함.
    - 모델/시제 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P10.2.1.4 알고리즘 튜닝 및 성능 검증
  - 「서 있는 상태 및 외란 저항 균형 제어」알고리즘에 대해 매개변수 최적화 및 경계 테스트를 수행하여 일반/극한 작업 조건에서의 성능이 지표를 충족하는지 검증함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P10.2.1.5 문서 출력 및 하위 전달
  - 「서 있는 상태 및 외란 저항 균형 제어」최종 보고서/도면/사양서 출력, ICD/BOM/SOP/요구 사항 추적 체인 업데이트, 하위 단계로의 공식 전달 완료.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
