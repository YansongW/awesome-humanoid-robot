---
$id: ent_process_p3_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Overall machine quality attribute budget
  zh: 整机质量属性预算
  ko: 整机质量属性预算
summary:
  en: Quality Budget Table, CoM Scope of the Whole Machine, and Upper Limit of Master Inertia
  zh: '- P3.1.2.1 输入梳理与目标量化 - 整理「整机质量属性预算」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 《质量预算表》、整机 CoM 范围、主惯量上限
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
**方法 / 工具**：自顶向下质量分配、 bottoms-up 核算、CoM 与惯量追踪

**设计思考逻辑**：质量和惯量直接影响能耗、动态响应与稳定性；需在早期锁定

**关键约束**：总重目标、电池能量密度、结构材料

**完成标准 / 输出物**：《质量预算表》、整机 CoM 范围、主惯量上限

**三级子任务与四级关键动作：**

- P3.1.2.1 输入梳理与目标量化
  - 整理「整机质量属性预算」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P3.1.2.2 方案/方法设计
  - 针对「整机质量属性预算」制定实施方法或候选方案，使用「自顶向下质量分配、 bottoms-up 核算、CoM 与惯量追踪」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P3.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「整机质量属性预算」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P3.1.2.4 验证与问题闭环
  - 对「整机质量属性预算」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P3.1.2.5 文档输出与下游交付
  - 输出「整机质量属性预算」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: System Architecture and Electromechanical Overall Design (System / Preliminary Design)

## Content
**Method/Tool**: Top-down mass allocation, bottoms-up accounting, CoM and inertia tracking

**Design Thinking Logic**: Mass and inertia directly affect energy consumption, dynamic response, and stability; they need to be locked in early

**Key Constraints**: Total weight target, battery energy density, structural materials

**Completion Criteria/Deliverables**: "Mass Budget Table", overall CoM range, main inertia upper limit

**Three-level Subtasks and Four-level Key Actions:**

- P3.1.2.1 Input Review and Target Quantification
  - Organize the upstream inputs, reference standards, and resources required for the "Overall Machine Mass Property Budget", convert completion criteria into quantifiable acceptance indicators, and clarify the Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P3.1.2.2 Scheme/Method Design
  - Develop implementation methods or candidate schemes for the "Overall Machine Mass Property Budget", conduct demonstration using "top-down mass allocation, bottoms-up accounting, CoM and inertia tracking", and clarify the technical route and resource requirements.
    - Formulate no fewer than 2 candidate schemes
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the scheme

- P3.1.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation work of the "Overall Machine Mass Property Budget" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
    - Establish models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P3.1.2.4 Verification and Issue Closure
  - Verify the output of the "Overall Machine Mass Property Budget", check whether it meets the completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P3.1.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for the "Overall Machine Mass Property Budget", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 시스템 아키텍처 및 전기기계 종합 설계 (System / Preliminary Design)

## 핵심 내용
**방법 / 도구**: 하향식 질량 할당, 상향식 산정, CoM 및 관성 추적

**설계 사고 논리**: 질량과 관성은 에너지 소비, 동적 응답 및 안정성에 직접적인 영향을 미치며, 초기 단계에서 확정해야 함

**주요 제약 조건**: 총 중량 목표, 배터리 에너지 밀도, 구조 재료

**완료 기준 / 산출물**: 《질량 예산표》, 전체 기기 CoM 범위, 주요 관성 상한

**3단계 하위 작업 및 4단계 주요 조치:**

- P3.1.2.1 입력 정리 및 목표 정량화
  - 「전체 기기 질량 속성 예산」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P3.1.2.2 방안/방법 설계
  - 「전체 기기 질량 속성 예산」에 대한 실행 방법 또는 후보 방안을 수립하고, 「하향식 질량 할당, 상향식 산정, CoM 및 관성 추적」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 수립 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P3.1.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「전체 기기 질량 속성 예산」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 수립 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P3.1.2.4 검증 및 문제 해결
  - 「전체 기기 질량 속성 예산」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종료될 때까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P3.1.2.5 문서 출력 및 하위 전달
  - 「전체 기기 질량 속성 예산」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
