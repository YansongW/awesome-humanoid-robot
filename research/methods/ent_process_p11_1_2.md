---
$id: ent_process_p11_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Drive and Transmission Solutions
  zh: 驱动与传动方案
  ko: 驱动与传动方案
summary:
  en: Drive System Decision Report, Powertrain Drawings
  zh: '- P11.1.2.1 输入梳理与目标量化 - 整理「驱动与传动方案」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 驱动方案决策报告、传动链图纸
domains:
- 02_components
- 06_design_engineering
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
**所属阶段/工作包**：灵巧手选型/设计与集成（Dexterous Hand）

## 核心内容
**方法 / 工具**：腱绳传动、微型电机直驱、连杆传动、液压/气动对比

**设计思考逻辑**：腱绳体积小但复杂；直驱易维护但体积大；欠驱动降低成本

**关键约束**：可靠性、可维护性、回差、力控精度

**完成标准 / 输出物**：驱动方案决策报告、传动链图纸

**三级子任务与四级关键动作：**

- P11.1.2.1 输入梳理与目标量化
  - 整理「驱动与传动方案」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P11.1.2.2 方案/方法设计
  - 针对「驱动与传动方案」制定实施方法或候选方案，使用「腱绳传动、微型电机直驱、连杆传动、液压/气动对比」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P11.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「驱动与传动方案」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P11.1.2.4 验证与问题闭环
  - 对「驱动与传动方案」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P11.1.2.5 文档输出与下游交付
  - 输出「驱动与传动方案」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Dexterous Hand Selection/Design and Integration (Dexterous Hand)

## Content
**Methods/Tools**: Tendon-driven, micro-motor direct drive, linkage transmission, hydraulic/pneumatic comparison

**Design Logic**: Tendon-driven is compact but complex; direct drive is easy to maintain but bulky; underactuation reduces cost

**Key Constraints**: Reliability, maintainability, backlash, force control accuracy

**Completion Criteria/Deliverables**: Drive scheme decision report, transmission chain drawings

**Level 3 Sub-tasks and Level 4 Key Actions:**

- P11.1.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for the "Drive and Transmission Scheme," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P11.1.2.2 Scheme/Method Design
  - Develop implementation methods or candidate schemes for the "Drive and Transmission Scheme," conduct argumentation using "Tendon-driven, micro-motor direct drive, linkage transmission, hydraulic/pneumatic comparison," and clarify the technical route and resource requirements.
    - Generate at least 2 candidate schemes
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize a review and freeze the scheme

- P11.1.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of the "Drive and Transmission Scheme" according to the design, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P11.1.2.4 Verification and Issue Closure
  - Verify the output of the "Drive and Transmission Scheme," check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P11.1.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for the "Drive and Transmission Scheme," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 다기능 손 선정/설계 및 통합 (Dexterous Hand)

## 핵심 내용
**방법 / 도구**: 텐더 구동, 초소형 모터 직접 구동, 링크 구동, 유압/공압 비교

**설계 사고 논리**: 텐더는 부피가 작지만 복잡함; 직접 구동은 유지보수가 쉽지만 부피가 큼; 언더액추에이션은 비용 절감

**핵심 제약 조건**: 신뢰성, 유지보수성, 백래시, 힘 제어 정밀도

**완료 기준 / 산출물**: 구동 방식 결정 보고서, 동력 전달 체인 도면

**3단계 하위 작업과 4단계 핵심 동작:**

- P11.1.2.1 입력 정리 및 목표 정량화
  - 「구동 및 전달 방식」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 수립

- P11.1.2.2 방식/방법 설계
  - 「구동 및 전달 방식」에 대한 구현 방법 또는 후보 방안을 수립하고, 「텐더 구동, 초소형 모터 직접 구동, 링크 구동, 유압/공압 비교」를 통해 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P11.1.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「구동 및 전달 방식」의 구현 작업을 수행하고, 프로토타입 또는 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P11.1.2.4 검증 및 문제 해결
  - 「구동 및 전달 방식」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P11.1.2.5 문서 출력 및 하위 전달
  - 「구동 및 전달 방식」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
