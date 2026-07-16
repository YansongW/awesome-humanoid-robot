---
$id: ent_process_p6_2_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Jacobian and analysis of velocity/force transmission
  zh: 雅可比与速度/力传递分析
  ko: 雅可比与速度/力传递分析
summary:
  en: Analysis of manipulability index and force transfer efficiency of typical attitude
  zh: '- P6.2.3.1 输入梳理与目标量化 - 整理「雅可比与速度/力传递分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 典型姿态可操作度指标、力传递效率分析
domains:
- 06_design_engineering
- 08_software_middleware
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
**所属阶段/工作包**：URDF 建模与运动学校核（Kinematics & URDF）

## 核心内容
**方法 / 工具**：几何雅可比、可操作度椭球、力椭球

**设计思考逻辑**：评估机器人在不同姿态下的速度/力操作能力，为控制设计提供依据

**关键约束**：数值稳定性

**完成标准 / 输出物**：典型姿态可操作度指标、力传递效率分析

**三级子任务与四级关键动作：**

- P6.2.3.1 输入梳理与目标量化
  - 整理「雅可比与速度/力传递分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P6.2.3.2 方案/方法设计
  - 针对「雅可比与速度/力传递分析」制定实施方法或候选方案，使用「几何雅可比、可操作度椭球、力椭球」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P6.2.3.3 实施/原型/样件制作
  - 根据设计方案执行「雅可比与速度/力传递分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P6.2.3.4 验证与问题闭环
  - 对「雅可比与速度/力传递分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P6.2.3.5 文档输出与下游交付
  - 输出「雅可比与速度/力传递分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: URDF Modeling and Kinematics Calibration (Kinematics & URDF)

## Content
**Method/Tool**: Geometric Jacobian, Manipulability Ellipsoid, Force Ellipsoid

**Design Thinking Logic**: Evaluate the robot's velocity/force manipulation capabilities under different postures to provide a basis for control design

**Key Constraints**: Numerical stability

**Completion Criteria/Deliverables**: Manipulability metrics for typical postures, force transmission efficiency analysis

**Three-Level Subtasks and Four-Level Key Actions**:

- P6.2.3.1 Input Review and Target Quantification
  - Organize the upstream inputs, reference standards, and resources required for "Jacobian and Velocity/Force Transmission Analysis," convert the completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm their versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P6.2.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Jacobian and Velocity/Force Transmission Analysis," using "Geometric Jacobian, Manipulability Ellipsoid, Force Ellipsoid" for demonstration, and clarify the technical roadmap and resource requirements.
    - Formulate no fewer than 2 candidate solutions
    - Establish an evaluation matrix with quantitative scoring
    - Organize a review and freeze the solution

- P6.2.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Jacobian and Velocity/Force Transmission Analysis" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype validation
    - Record anomalies and deviations

- P6.2.3.4 Verification and Issue Closure
  - Verify the output of "Jacobian and Velocity/Force Transmission Analysis," check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P6.2.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Jacobian and Velocity/Force Transmission Analysis," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: URDF 모델링 및 운동학 검증 (Kinematics & URDF)

## 핵심 내용
**방법/도구**: 기하학적 야코비, 조작도 타원체, 힘 타원체

**설계 사고 논리**: 다양한 자세에서 로봇의 속도/힘 조작 능력을 평가하여 제어 설계의 근거 제공

**핵심 제약 조건**: 수치적 안정성

**완료 기준/산출물**: 대표 자세의 조작도 지표, 힘 전달 효율 분석

**3단계 하위 작업과 4단계 핵심 동작:**

- P6.2.3.1 입력 정리 및 목표 정량화
  - 「야코비와 속도/힘 전달 분석」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P6.2.3.2 방안/방법 설계
  - 「야코비와 속도/힘 전달 분석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「기하학적 야코비, 조작도 타원체, 힘 타원체」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스를 구축하고 정량적 점수 부여
    - 검토를 조직하고 방안 확정

- P6.2.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「야코비와 속도/힘 전달 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품을 구축하고 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P6.2.3.4 검증 및 문제 종결
  - 「야코비와 속도/힘 전달 분석」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하며 종결될 때까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트를 수행하고 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P6.2.3.5 문서 출력 및 하위 전달
  - 「야코비와 속도/힘 전달 분석」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
