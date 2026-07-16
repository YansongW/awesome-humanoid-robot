---
$id: ent_process_p10_3_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: System Identification and Parameter Calibration
  zh: 系统辨识与参数校准
  ko: 系统辨识与参数校准
summary:
  en: Identification report, simulation–hardware frequency response comparison
  zh: '- P10.3.1.1 输入梳理与目标量化 - 整理「系统辨识与参数校准」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 辨识报告、仿真-实物频率响应对比
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
**方法 / 工具**：最小二乘、最大似然、频域辨识、摩擦/惯量辨识

**设计思考逻辑**：仿真参数与实际存在差异，需通过辨识缩小 gap

**关键约束**：激励信号安全性、参数可辨识性

**完成标准 / 输出物**：辨识报告、仿真-实物频率响应对比

**三级子任务与四级关键动作：**

- P10.3.1.1 输入梳理与目标量化
  - 整理「系统辨识与参数校准」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P10.3.1.2 方案/方法设计
  - 针对「系统辨识与参数校准」制定实施方法或候选方案，使用「最小二乘、最大似然、频域辨识、摩擦/惯量辨识」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P10.3.1.3 实施/原型/样件制作
  - 根据设计方案执行「系统辨识与参数校准」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P10.3.1.4 验证与问题闭环
  - 对「系统辨识与参数校准」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P10.3.1.5 文档输出与下游交付
  - 输出「系统辨识与参数校准」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Motion Control Algorithm Development and Validation (Motion Control)

## Content
**Methods/Tools**: Least Squares, Maximum Likelihood, Frequency Domain Identification, Friction/Inertia Identification

**Design Thinking Logic**: Simulation parameters differ from actual ones, requiring identification to narrow the gap

**Key Constraints**: Safety of excitation signals, parameter identifiability

**Completion Criteria/Deliverables**: Identification report, comparison of simulation and actual frequency responses

**Level-3 Subtasks and Level-4 Key Actions**:

- P10.3.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "System Identification and Parameter Calibration," convert completion criteria into quantifiable acceptance indicators, and clarify the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P10.3.1.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "System Identification and Parameter Calibration," using "Least Squares, Maximum Likelihood, Frequency Domain Identification, Friction/Inertia Identification" for demonstration, and clarify the technical roadmap and resource requirements.
    - Formulate at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P10.3.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "System Identification and Parameter Calibration" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype validation
    - Record anomalies and deviations

- P10.3.1.4 Validation and Issue Closure
  - Validate the output of "System Identification and Parameter Calibration," check whether completion criteria are met, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P10.3.1.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for "System Identification and Parameter Calibration," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**：운동 제어 알고리즘 개발 및 검증 (Motion Control)

## 핵심 내용
**방법 / 도구**：최소제곱법, 최대우도법, 주파수 영역 식별, 마찰/관성 식별

**설계 사고 논리**：시뮬레이션 파라미터와 실제 간 차이가 존재하므로, 식별을 통해 격차를 줄여야 함

**핵심 제약 조건**：여기 신호 안전성, 파라미터 식별 가능성

**완료 기준 / 산출물**：식별 보고서, 시뮬레이션-실물 주파수 응답 비교

**3단계 하위 작업 및 4단계 핵심 동작：**

- P10.3.1.1 입력 정리 및 목표 정량화
  - 「시스템 식별 및 파라미터 보정」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 Owner, 시간 노드 및 위험 등록 수립

- P10.3.1.2 방안/방법 설계
  - 「시스템 식별 및 파라미터 보정」에 대한 실행 방법 또는 후보 방안을 수립하고, 「최소제곱법, 최대우도법, 주파수 영역 식별, 마찰/관성 식별」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 수립 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P10.3.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「시스템 식별 및 파라미터 보정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P10.3.1.4 검증 및 문제 해결
  - 「시스템 식별 및 파라미터 보정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P10.3.1.5 문서 출력 및 하위 전달
  - 「시스템 식별 및 파라미터 보정」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 완료 및 버전 관리
    - 게시 및 하위 의존 부서에 통보
