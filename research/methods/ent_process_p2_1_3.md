---
$id: ent_process_p2_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Appearance handboard and scale model
  zh: 外观手板与比例模型
  ko: 外观手板与比例模型
summary:
  en: 1:1 Appearance panel, review minutes, question list
  zh: '- P2.1.3.1 输入梳理与目标量化 - 整理「外观手板与比例模型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 1:1 外观手板、评审纪要、问题清单
domains:
- 06_design_engineering
layers:
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
**所属阶段/工作包**：工业设计与外观工程（ID / A-Surface）

## 核心内容
**方法 / 工具**：SLA/SLS 3D 打印、泡沫 CNC、喷漆、覆膜

**设计思考逻辑**：1:1 物理模型验证视觉比例、装配空间、人机交互

**关键约束**：手板材料不等于量产材料、强度有限

**完成标准 / 输出物**：1:1 外观手板、评审纪要、问题清单

**三级子任务与四级关键动作：**

- P2.1.3.1 输入梳理与目标量化
  - 整理「外观手板与比例模型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P2.1.3.2 方案/方法设计
  - 针对「外观手板与比例模型」制定实施方法或候选方案，使用「SLA/SLS 3D 打印、泡沫 CNC、喷漆、覆膜」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P2.1.3.3 实施/原型/样件制作
  - 根据设计方案执行「外观手板与比例模型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P2.1.3.4 验证与问题闭环
  - 对「外观手板与比例模型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P2.1.3.5 文档输出与下游交付
  - 输出「外观手板与比例模型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Industrial Design & Appearance Engineering (ID / A-Surface)

## Content
**Methods/Tools**: SLA/SLS 3D Printing, Foam CNC, Painting, Lamination

**Design Thinking Logic**: 1:1 physical model validation of visual proportions, assembly space, and human-machine interaction

**Key Constraints**: Prototype materials differ from production materials; limited strength

**Completion Criteria/Deliverables**: 1:1 appearance prototype, review minutes, issue list

**Level-3 Subtasks and Level-4 Key Actions:**

- P2.1.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "appearance prototype and scale model"; convert completion criteria into quantifiable acceptance indicators; and define the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P2.1.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "appearance prototype and scale model"; conduct feasibility studies using "SLA/SLS 3D printing, foam CNC, painting, lamination"; and clarify the technical roadmap and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and freeze the solution

- P2.1.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "appearance prototype and scale model" according to the design solution; fabricate prototypes, samples, or complete key steps; and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype validation
    - Document anomalies and deviations

- P2.1.3.4 Verification and Issue Closure
  - Verify the output of "appearance prototype and scale model" against completion criteria; record issues and track them to closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P2.1.3.5 Documentation and Downstream Delivery
  - Output final reports/drawings/specifications for "appearance prototype and scale model"; update ICD/BOM/SOP/requirements traceability chain; and complete formal delivery to downstream stages.
    - Write documents per templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 산업 디자인 및 외관 엔지니어링 (ID / A-Surface)

## 핵심 내용
**방법/도구**: SLA/SLS 3D 프린팅, 폼 CNC, 도장, 라미네이팅

**디자인 사고 로직**: 1:1 물리적 모델을 통한 시각적 비율, 조립 공간, 인간-기계 상호작용 검증

**핵심 제약 조건**: 시제품 재료는 양산 재료와 동일하지 않으며, 강도가 제한적임

**완료 기준/산출물**: 1:1 외관 시제품, 검토 회의록, 문제 목록

**3단계 하위 작업 및 4단계 핵심 조치:**

- P2.1.3.1 입력 정리 및 목표 정량화
  - 「외관 시제품 및 축소 모델」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P2.1.3.2 방안/방법 설계
  - 「외관 시제품 및 축소 모델」에 대한 구현 방법 또는 후보 방안을 수립하고, 「SLA/SLS 3D 프린팅, 폼 CNC, 도장, 라미네이팅」을 사용하여 검토하며, 기술 경로와 자원 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 회의 조직 및 방안 확정

- P2.1.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「외관 시제품 및 축소 모델」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P2.1.3.4 검증 및 문제 종결
  - 「외관 시제품 및 축소 모델」의 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P2.1.3.5 문서 출력 및 하위 전달
  - 「외관 시제품 및 축소 모델」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서 통지
