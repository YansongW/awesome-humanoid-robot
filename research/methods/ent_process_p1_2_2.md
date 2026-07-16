---
$id: ent_process_p1_2_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Whole machine architecture and function allocation
  zh: 整机架构与功能分配
  ko: 整机架构与功能分配
summary:
  en: System architecture diagram, function allocation table, ICD draft
  zh: '- P1.2.2.1 输入梳理与目标量化 - 整理「整机架构与功能分配」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 系统架构图、功能分配表、ICD 草案
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
**方法 / 工具**：功能分解、N² 图、接口控制文档（ICD）草案

**设计思考逻辑**：明确运动、操作、感知、计算、能源、热管理、结构子系统的边界

**关键约束**：实时性、功耗、线缆数量、可维护性

**完成标准 / 输出物**：系统架构图、功能分配表、ICD 草案

**三级子任务与四级关键动作：**

- P1.2.2.1 输入梳理与目标量化
  - 整理「整机架构与功能分配」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P1.2.2.2 方案/方法设计
  - 针对「整机架构与功能分配」制定实施方法或候选方案，使用「功能分解、N² 图、接口控制文档（ICD）草案」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P1.2.2.3 实施/原型/样件制作
  - 根据设计方案执行「整机架构与功能分配」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P1.2.2.4 验证与问题闭环
  - 对「整机架构与功能分配」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P1.2.2.5 文档输出与下游交付
  - 输出「整机架构与功能分配」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Requirements Definition and System Concept (Concept / Pre-A)

## Content
**Methods/Tools**: Functional decomposition, N² diagram, Interface Control Document (ICD) draft

**Design Logic**: Define the boundaries of subsystems: motion, operation, perception, computation, energy, thermal management, and structure

**Key Constraints**: Real-time performance, power consumption, cable count, maintainability

**Completion Criteria/Deliverables**: System architecture diagram, function allocation table, ICD draft

**Level-3 Sub-tasks and Level-4 Key Actions:**

- P1.2.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Overall Architecture and Function Allocation"; convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P1.2.2.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Overall Architecture and Function Allocation"; use "functional decomposition, N² diagram, Interface Control Document (ICD) draft" for demonstration, and clarify technical roadmap and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the solution

- P1.2.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Overall Architecture and Function Allocation" according to the design solution; produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P1.2.2.4 Verification and Issue Closure
  - Verify the outputs of "Overall Architecture and Function Allocation"; check whether completion criteria are met, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P1.2.2.5 Documentation and Downstream Delivery
  - Output the final report/drawings/specifications for "Overall Architecture and Function Allocation"; update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 요구사항 정의 및 시스템 방안 (Concept / Pre-A)

## 핵심 내용
**방법 / 도구**: 기능 분해, N² 다이어그램, 인터페이스 제어 문서(ICD) 초안

**설계 사고 논리**: 운동, 조작, 인지, 연산, 에너지, 열 관리, 구조 서브시스템의 경계 명확화

**핵심 제약 조건**: 실시간성, 전력 소모, 케이블 수량, 유지보수성

**완료 기준 / 산출물**: 시스템 아키텍처 다이어그램, 기능 할당표, ICD 초안

**3단계 하위 작업 및 4단계 핵심 동작:**

- P1.2.2.1 입력 정리 및 목표 정량화
  - 「전체 아키텍처와 기능 할당」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 검증 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검증 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P1.2.2.2 방안/방법 설계
  - 「전체 아키텍처와 기능 할당」에 대한 구현 방법 또는 후보 방안을 수립하고, 「기능 분해, N² 다이어그램, 인터페이스 제어 문서(ICD) 초안」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P1.2.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「전체 아키텍처와 기능 할당」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P1.2.2.4 검증 및 문제 폐쇄
  - 「전체 아키텍처와 기능 할당」의 산출물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 산출

- P1.2.2.5 문서 출력 및 하위 전달
  - 「전체 아키텍처와 기능 할당」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
