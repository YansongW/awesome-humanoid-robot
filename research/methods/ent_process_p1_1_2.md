---
$id: ent_process_p1_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: System Requirements Specification (SyRS)
  zh: 系统需求规格书（SyRS）
  ko: 系统需求规格书（SyRS）
summary:
  en: SyRS baseline release, requirements traceability, and acceptance condition quantification
  zh: '- P1.1.2.1 输入梳理与目标量化 - 整理「系统需求规格书（SyRS）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: SyRS 基线发布、需求可追溯、验收条件量化
domains:
- 06_design_engineering
- 12_policy_regulation_ethics
layers:
- midstream
- validation_markets
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
**所属阶段/工作包**：需求定义与系统方案（Concept / Pre-A）

## 核心内容
**方法 / 工具**：SysML 用例图、需求树、SMART 原则

**设计思考逻辑**：将商业语言转化为工程语言：尺寸、重量、DOF、速度、负载、续航、安全等级

**关键约束**：指标耦合、测试可行性、成本驱动

**完成标准 / 输出物**：SyRS 基线发布、需求可追溯、验收条件量化

**三级子任务与四级关键动作：**

- P1.1.2.1 输入梳理与目标量化
  - 整理「系统需求规格书（SyRS）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P1.1.2.2 方案/方法设计
  - 针对「系统需求规格书（SyRS）」制定实施方法或候选方案，使用「SysML 用例图、需求树、SMART 原则」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P1.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「系统需求规格书（SyRS）」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P1.1.2.4 验证与问题闭环
  - 对「系统需求规格书（SyRS）」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P1.1.2.5 文档输出与下游交付
  - 输出「系统需求规格书（SyRS）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Requirements Definition and System Solution (Concept / Pre-A)

## Content
**Method/Tool**: SysML Use Case Diagram, Requirements Tree, SMART Principle

**Design Thinking Logic**: Translate business language into engineering language: dimensions, weight, DOF, speed, payload, endurance, safety level

**Key Constraints**: Indicator coupling, test feasibility, cost-driven

**Completion Criteria/Deliverables**: SyRS baseline release, requirements traceability, quantified acceptance criteria

**Level-3 Subtasks and Level-4 Key Actions:**

- P1.1.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for the "System Requirements Specification (SyRS)", convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P1.1.2.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for the "System Requirements Specification (SyRS)", conduct argumentation using "SysML Use Case Diagram, Requirements Tree, SMART Principle", and clarify technical routes and resource requirements.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and quantify scores
    - Organize review and freeze the solution

- P1.1.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation work of the "System Requirements Specification (SyRS)" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P1.1.2.4 Verification and Issue Closure
  - Verify the output of the "System Requirements Specification (SyRS)", check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P1.1.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification of the "System Requirements Specification (SyRS)", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 요구사항 정의 및 시스템 방안 (Concept / Pre-A)

## 핵심 내용
**방법 / 도구**: SysML 유스케이스 다이어그램, 요구사항 트리, SMART 원칙

**설계 사고 논리**: 비즈니스 언어를 엔지니어링 언어로 변환: 크기, 무게, DOF, 속도, 부하, 배터리 수명, 안전 등급

**핵심 제약 조건**: 지표 간 결합, 테스트 가능성, 비용 주도

**완료 기준 / 산출물**: SyRS 기준선 릴리스, 요구사항 추적 가능, 인수 조건 정량화

**3단계 하위 작업 및 4단계 핵심 조치:**

- P1.1.2.1 입력 정리 및 목표 정량화
  - 「시스템 요구사항 명세서(SyRS)」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 인수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 인수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P1.1.2.2 방안/방법 설계
  - 「시스템 요구사항 명세서(SyRS)」에 대한 구현 방법 또는 후보 방안을 수립하고, 「SysML 유스케이스 다이어그램, 요구사항 트리, SMART 원칙」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P1.1.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「시스템 요구사항 명세서(SyRS)」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P1.1.2.4 검증 및 문제 종결
  - 「시스템 요구사항 명세서(SyRS)」 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P1.1.2.5 문서 출력 및 하위 전달
  - 「시스템 요구사항 명세서(SyRS)」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 릴리스 및 하위 의존 부서에 통지
