---
$id: ent_process_p5_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Central skeleton and limb link design
  zh: 中心骨架与四肢连杆设计
  ko: 中心骨架与四肢连杆设计
summary:
  en: 3D structural model, key section design, BOM first draft
  zh: '- P5.1.1.1 输入梳理与目标量化 - 整理「中心骨架与四肢连杆设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 3D 结构模型、关键截面设计、BOM 初稿
domains:
- 06_design_engineering
- 03_manufacturing_processes
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
**所属阶段/工作包**：本体结构工程与原型（Mechanical Structure）

## 核心内容
**方法 / 工具**：SolidWorks / NX / CATIA、拓扑优化、尺寸优化

**设计思考逻辑**：中心骨架承载躯干负载并传递至腿；四肢连杆需高刚度低重量

**关键约束**：刚度、强度、重量、装配可达性

**完成标准 / 输出物**：3D 结构模型、关键截面设计、BOM 初稿

**三级子任务与四级关键动作：**

- P5.1.1.1 输入梳理与目标量化
  - 整理「中心骨架与四肢连杆设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P5.1.1.2 概念与详细设计
  - 完成「中心骨架与四肢连杆设计」的概念设计、详细设计与接口定义，使用「SolidWorks / NX / CATIA、拓扑优化、尺寸优化」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P5.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「中心骨架与四肢连杆设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P5.1.1.4 验证与问题闭环
  - 对「中心骨架与四肢连杆设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P5.1.1.5 文档输出与下游交付
  - 输出「中心骨架与四肢连杆设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Mechanical Structure

## Content
**Methods/Tools**: SolidWorks / NX / CATIA, Topology Optimization, Size Optimization

**Design Logic**: The central skeleton bears the torso load and transmits it to the legs; limb links require high stiffness and low weight.

**Key Constraints**: Stiffness, Strength, Weight, Assembly Accessibility

**Completion Criteria/Deliverables**: 3D Structural Model, Key Cross-Section Design, BOM Draft

**Level-3 Subtasks and Level-4 Key Actions:**

- P5.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Central Skeleton and Limb Link Design," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P5.1.1.2 Conceptual and Detailed Design
  - Complete the conceptual design, detailed design, and interface definition for "Central Skeleton and Limb Link Design," verify feasibility using "SolidWorks / NX / CATIA, Topology Optimization, Size Optimization," and output drawings/algorithms/logical frameworks.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and freeze the solution

- P5.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Central Skeleton and Limb Link Design" according to the design plan, fabricate prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Document anomalies and deviations

- P5.1.1.4 Verification and Issue Closure
  - Verify the output of "Central Skeleton and Limb Link Design," check if it meets completion criteria, record issues, and track them to closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P5.1.1.5 Documentation and Downstream Delivery
  - Output the final report/drawings/specifications for "Central Skeleton and Limb Link Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents per template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 본체 구조 공학 및 프로토타입 (Mechanical Structure)

## 핵심 내용
**방법 / 도구**: SolidWorks / NX / CATIA, 위상 최적화, 치수 최적화

**설계 사고 논리**: 중심 골격이 몸통 하중을 지지하고 다리로 전달하며, 사지 링크는 높은 강성과 낮은 중량이 필요함

**핵심 제약 조건**: 강성, 강도, 중량, 조립 접근성

**완료 기준 / 산출물**: 3D 구조 모델, 주요 단면 설계, BOM 초안

**3단계 하위 작업 및 4단계 핵심 조치:**

- P5.1.1.1 입력 정리 및 목표 정량화
  - 「중심 골격 및 사지 링크 설계」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P5.1.1.2 개념 및 상세 설계
  - 「중심 골격 및 사지 링크 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「SolidWorks / NX / CATIA, 위상 최적화, 치수 최적화」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 산정
    - 검토 조직 및 방안 확정

- P5.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「중심 골격 및 사지 링크 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 공정 데이터를 기록함.
    - 모델/시제품 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P5.1.1.4 검증 및 문제 종결
  - 「중심 골격 및 사지 링크 설계」 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P5.1.1.5 문서 출력 및 하위 전달
  - 「중심 골격 및 사지 링크 설계」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
