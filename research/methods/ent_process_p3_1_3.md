---
$id: ent_process_p3_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Preliminary analysis of kinematics and dynamics
  zh: 运动学与动力学初步分析
  ko: 运动学与动力学初步分析
summary:
  en: Joint requirements specifications v1, peak/continuous torque meter, critical action reaction force
  zh: '- P3.1.3.1 输入梳理与目标量化 - 整理「运动学与动力学初步分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 关节需求规格 v1、峰值/连续扭矩表、关键动作反力
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
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
**所属阶段/工作包**：系统架构与机电总体设计（System / Preliminary Design）

## 核心内容
**方法 / 工具**：解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真

**设计思考逻辑**：估算站立、蹲起、行走、抓取时各关节峰值扭矩和速度

**关键约束**：载荷假设保守性、接触模型简化

**完成标准 / 输出物**：关节需求规格 v1、峰值/连续扭矩表、关键动作反力

**三级子任务与四级关键动作：**

- P3.1.3.1 输入梳理与目标量化
  - 整理「运动学与动力学初步分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P3.1.3.2 方案/方法设计
  - 针对「运动学与动力学初步分析」制定实施方法或候选方案，使用「解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P3.1.3.3 建模/仿真与样机实现
  - 建立「运动学与动力学初步分析」的仿真/数学模型或原型样机，使用「解析法、Matlab/Python、Pinocchio/RBDL、典型动作仿真」执行计算或实验，记录关键参数与边界条件。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P3.1.3.4 仿真结果校核与优化
  - 校核「运动学与动力学初步分析」仿真结果与理论/试验数据的一致性，识别薄弱点并迭代优化。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P3.1.3.5 文档输出与下游交付
  - 输出「运动学与动力学初步分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: System Architecture and Electromechanical Overall Design (System / Preliminary Design)

## Content
**Method/Tool**: Analytical method, Matlab/Python, Pinocchio/RBDL, typical motion simulation

**Design Thinking Logic**: Estimate peak torque and speed of each joint during standing, squatting, walking, and grasping

**Key Constraints**: Conservatism of load assumptions, simplification of contact models

**Completion Criteria/Deliverables**: Joint requirement specification v1, peak/continuous torque table, reaction forces for key actions

**Three-level Subtasks and Four-level Key Actions:**

- P3.1.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Preliminary Kinematics and Dynamics Analysis," convert completion criteria into quantifiable acceptance indicators, and clarify the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P3.1.3.2 Scheme/Method Design
  - Develop implementation methods or candidate schemes for "Preliminary Kinematics and Dynamics Analysis," using "analytical method, Matlab/Python, Pinocchio/RBDL, typical motion simulation" for demonstration, and clarify the technical roadmap and resource requirements.
    - Formulate no fewer than 2 candidate schemes
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the scheme

- P3.1.3.3 Modeling/Simulation and Prototype Implementation
  - Establish simulation/mathematical models or prototype prototypes for "Preliminary Kinematics and Dynamics Analysis," using "analytical method, Matlab/Python, Pinocchio/RBDL, typical motion simulation" to perform calculations or experiments, and record key parameters and boundary conditions.
    - Build models/prototypes and record key parameters
    - Execute simulations or prototype verification
    - Record anomalies and deviations

- P3.1.3.4 Simulation Result Verification and Optimization
  - Verify the consistency of simulation results from "Preliminary Kinematics and Dynamics Analysis" with theoretical/experimental data, identify weak points, and perform iterative optimization.
    - Build models/prototypes and record key parameters
    - Execute simulations or prototype verification
    - Record anomalies and deviations

- P3.1.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Preliminary Kinematics and Dynamics Analysis," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and cite original data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 시스템 아키텍처 및 기전 종합 설계 (System / Preliminary Design)

## 핵심 내용
**방법 / 도구**: 해석법, Matlab/Python, Pinocchio/RBDL, 대표 동작 시뮬레이션

**설계 사고 논리**: 서기, 쪼그려 앉기, 보행, 파지 시 각 관절의 피크 토크와 속도 추정

**주요 제약 조건**: 하중 가정의 보수성, 접촉 모델 단순화

**완료 기준 / 산출물**: 관절 요구 사양 v1, 피크/연속 토크 표, 주요 동작 반력

**3단계 하위 작업과 4단계 주요 동작:**

- P3.1.3.1 입력 정리 및 목표 정량화
  - 「운동학 및 동역학 예비 분석」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P3.1.3.2 방안/방법 설계
  - 「운동학 및 동역학 예비 분석」을 위한 실행 방법 또는 후보 방안을 수립하고, 「해석법, Matlab/Python, Pinocchio/RBDL, 대표 동작 시뮬레이션」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P3.1.3.3 모델링/시뮬레이션 및 시제 구현
  - 「운동학 및 동역학 예비 분석」을 위한 시뮬레이션/수학적 모델 또는 프로토타입 시제를 구축하고, 「해석법, Matlab/Python, Pinocchio/RBDL, 대표 동작 시뮬레이션」을 사용하여 계산 또는 실험을 수행하며, 주요 매개변수와 경계 조건을 기록한다.
    - 모델/시제 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P3.1.3.4 시뮬레이션 결과 검증 및 최적화
  - 「운동학 및 동역학 예비 분석」 시뮬레이션 결과와 이론/실험 데이터의 일관성을 검증하고, 취약점을 식별하여 반복 최적화를 수행한다.
    - 모델/시제 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P3.1.3.5 문서 출력 및 하위 전달
  - 「운동학 및 동역학 예비 분석」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서 통지
