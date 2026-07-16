---
$id: ent_process_p3_3_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Conceptual design of functional safety
  zh: 功能安全概念设计
  ko: 功能安全概念设计
summary:
  en: Safety concept document, safety goal, functional safety architecture
  zh: '- P3.3.1.1 输入梳理与目标量化 - 整理「功能安全概念设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 安全概念文档、安全目标、功能安全架构
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
**方法 / 工具**：HARA、STPA、安全目标分解、冗余策略

**设计思考逻辑**：识别与人接触、跌倒、夹持、电气相关的危害，定义安全功能

**关键约束**：SIL/PL 等级、成本、复杂度

**完成标准 / 输出物**：安全概念文档、安全目标、功能安全架构

**三级子任务与四级关键动作：**

- P3.3.1.1 输入梳理与目标量化
  - 整理「功能安全概念设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P3.3.1.2 概念与详细设计
  - 完成「功能安全概念设计」的概念设计、详细设计与接口定义，使用「HARA、STPA、安全目标分解、冗余策略」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P3.3.1.3 实施/原型/样件制作
  - 根据设计方案执行「功能安全概念设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P3.3.1.4 验证与问题闭环
  - 对「功能安全概念设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P3.3.1.5 文档输出与下游交付
  - 输出「功能安全概念设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: System Architecture and Electromechanical Overall Design (System / Preliminary Design)

## Content
**Method/Tool**: HARA, STPA, Safety Goal Decomposition, Redundancy Strategy

**Design Logic**: Identify hazards related to human contact, falls, clamping, and electrical issues; define safety functions

**Key Constraints**: SIL/PL levels, cost, complexity

**Completion Criteria/Deliverables**: Safety concept document, safety goals, functional safety architecture

**Level-3 Subtasks and Level-4 Key Actions:**

- P3.3.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Functional Safety Concept Design"; convert completion criteria into quantifiable acceptance indicators; clarify the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owners, timelines, and risk register

- P3.3.1.2 Concept and Detailed Design
  - Complete the concept design, detailed design, and interface definition for "Functional Safety Concept Design"; verify feasibility using "HARA, STPA, Safety Goal Decomposition, Redundancy Strategy"; output drawings/algorithms/logical frameworks.
    - Develop at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize reviews and freeze the solution

- P3.3.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Functional Safety Concept Design" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype verification
    - Record anomalies and deviations

- P3.3.1.4 Verification and Issue Closure
  - Verify the outputs of "Functional Safety Concept Design"; check whether completion criteria are met; record issues and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue lists and improvement measures

- P3.3.1.5 Documentation and Downstream Delivery
  - Output the final report/drawings/specifications for "Functional Safety Concept Design"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream processes.
    - Write documents according to templates and reference raw data
    - Complete internal reviews and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 시스템 아키텍처 및 전기기계 종합 설계 (System / Preliminary Design)

## 핵심 내용
**방법 / 도구**: HARA, STPA, 안전 목표 분해, 중복 전략

**설계 사고 논리**: 사람 접촉, 낙상, 협착, 전기 관련 위험 식별 및 안전 기능 정의

**핵심 제약 조건**: SIL/PL 등급, 비용, 복잡성

**완료 기준 / 산출물**: 안전 개념 문서, 안전 목표, 기능 안전 아키텍처

**3단계 하위 작업과 4단계 핵심 조치:**

- P3.3.1.1 입력 정리 및 목표 정량화
  - 「기능 안전 개념 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 Owner, 시간 노드 및 위험 등록부 구축

- P3.3.1.2 개념 및 상세 설계
  - 「기능 안전 개념 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「HARA, STPA, 안전 목표 분해, 중복 전략」을 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력한다.
    - 2개 이상의 후보 방안 수립
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P3.3.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「기능 안전 개념 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P3.3.1.4 검증 및 문제 종결
  - 「기능 안전 개념 설계」 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P3.3.1.5 문서 출력 및 하위 전달
  - 「기능 안전 개념 설계」 최종 보고서/도면/사양서를 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
