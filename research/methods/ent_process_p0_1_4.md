---
$id: ent_process_p0_1_4
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Life Cycle Cost Model v0
  zh: 全生命周期成本模型 v0
  ko: 全生命周期成本模型 v0
summary:
  en: Whole-machine BOM target, subsystem cost cap, break-even production volume
  zh: '- P0.1.4.1 输入梳理与目标量化 - 整理「全生命周期成本模型 v0」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 整机 BOM 目标、子系统成本上限、盈亏平衡产量
domains:
- 11_applications_markets
- 12_policy_regulation_ethics
layers:
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
**所属阶段/工作包**：项目立项与商业基线

## 核心内容
**方法 / 工具**：BOM 目标分解、TCO 模型、盈亏平衡批量计算

**设计思考逻辑**：成本目标必须早于设计冻结；用于指导自研/外购与材料选择

**关键约束**：目标售价、毛利率、供应链最小订单量

**完成标准 / 输出物**：整机 BOM 目标、子系统成本上限、盈亏平衡产量

**三级子任务与四级关键动作：**

- P0.1.4.1 输入梳理与目标量化
  - 整理「全生命周期成本模型 v0」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P0.1.4.2 方案/方法设计
  - 针对「全生命周期成本模型 v0」制定实施方法或候选方案，使用「BOM 目标分解、TCO 模型、盈亏平衡批量计算」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P0.1.4.3 实施/原型/样件制作
  - 根据设计方案执行「全生命周期成本模型 v0」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P0.1.4.4 验证与问题闭环
  - 对「全生命周期成本模型 v0」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P0.1.4.5 文档输出与下游交付
  - 输出「全生命周期成本模型 v0」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Project Initiation and Commercial Baseline

## Content
**Methods/Tools**: BOM Target Decomposition, TCO Model, Break-Even Volume Calculation

**Design Thinking Logic**: Cost targets must be set before design freeze; used to guide make-or-buy decisions and material selection

**Key Constraints**: Target selling price, gross margin, minimum order quantity from supply chain

**Completion Criteria/Deliverables**: Overall BOM target, subsystem cost ceiling, break-even production volume

**Level-3 Subtasks and Level-4 Key Actions:**

- P0.1.4.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for the "Lifecycle Cost Model v0"; convert completion criteria into quantifiable acceptance indicators, and assign owners and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owners, timelines, and risk register

- P0.1.4.2 Approach/Method Design
  - Develop implementation methods or candidate approaches for the "Lifecycle Cost Model v0"; use "BOM Target Decomposition, TCO Model, Break-Even Volume Calculation" for validation, and define technical roadmap and resource requirements.
    - Generate at least 2 candidate approaches
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the approach

- P0.1.4.3 Implementation/Prototype/Sample Production
  - Execute the implementation of the "Lifecycle Cost Model v0" according to the design plan; produce prototypes, samples, or complete key steps, and record process data.
    - Build model/prototype and record key parameters
    - Perform simulation or prototype validation
    - Document anomalies and deviations

- P0.1.4.4 Verification and Issue Closure
  - Verify the output of the "Lifecycle Cost Model v0"; check whether completion criteria are met, record issues, and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement actions

- P0.1.4.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for the "Lifecycle Cost Model v0"; update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream phases.
    - Write documentation per template and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 프로젝트 수립 및 사업 기준선

## 핵심 내용
**방법/도구**: BOM 목표 분해, TCO 모델, 손익분기점 배치 계산

**설계 사고 논리**: 비용 목표는 설계 동결보다 먼저 설정되어야 함; 자체 개발/외주 및 재료 선택을 지침하는 데 사용됨

**핵심 제약 조건**: 목표 판매 가격, 총이익률, 공급망 최소 주문량

**완료 기준/산출물**: 전체 기기 BOM 목표, 하위 시스템 비용 상한, 손익분기점 생산량

**3단계 하위 작업 및 4단계 핵심 조치:**

- P0.1.4.1 입력 정리 및 목표 정량화
  - 「전 생애 주기 비용 모델 v0」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P0.1.4.2 방안/방법 설계
  - 「전 생애 주기 비용 모델 v0」에 대한 구현 방법 또는 후보 방안을 수립하고, 「BOM 목표 분해, TCO 모델, 손익분기점 배치 계산」을 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 동결

- P0.1.4.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「전 생애 주기 비용 모델 v0」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P0.1.4.4 검증 및 문제 종결
  - 「전 생애 주기 비용 모델 v0」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P0.1.4.5 문서 출력 및 하위 전달
  - 「전 생애 주기 비용 모델 v0」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
