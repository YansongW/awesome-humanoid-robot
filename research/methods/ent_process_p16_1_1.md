---
$id: ent_process_p16_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: DFM/DFA review
  zh: DFM/DFA 评审
  ko: DFM/DFA 评审
summary:
  en: DFM/DFA reports, engineering change lists, cost impact assessments
  zh: '- P16.1.1.1 输入梳理与目标量化 - 整理「DFM/DFA 评审」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: DFM/DFA 报告、工程变更清单、成本影响评估
domains:
- 05_mass_production
- 11_applications_markets
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
**所属阶段/工作包**：小批量试产与量产准备（Pilot & Production Ramp）

## 核心内容
**方法 / 工具**：设计可制造性/可装配性分析、装配工时估算

**设计思考逻辑**：将 3D 打印/CNC 原型转化为压铸、注塑、钣金等量产工艺

**关键约束**：模具成本、良率、节拍

**完成标准 / 输出物**：DFM/DFA 报告、工程变更清单、成本影响评估

**三级子任务与四级关键动作：**

- P16.1.1.1 输入梳理与目标量化
  - 整理「DFM/DFA 评审」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P16.1.1.2 方案/方法设计
  - 针对「DFM/DFA 评审」制定实施方法或候选方案，使用「设计可制造性/可装配性分析、装配工时估算」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P16.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「DFM/DFA 评审」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P16.1.1.4 测试执行与结果分析
  - 按照验收标准执行「DFM/DFA 评审」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P16.1.1.5 文档输出与下游交付
  - 输出「DFM/DFA 评审」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Pilot & Production Ramp

## Content
**Method/Tool**: Design for Manufacturing/Assembly Analysis, Assembly Time Estimation

**Design Thinking Logic**: Convert 3D printing/CNC prototypes into mass production processes such as die casting, injection molding, and sheet metal forming

**Key Constraints**: Mold cost, yield rate, cycle time

**Completion Criteria/Deliverables**: DFM/DFA report, engineering change list, cost impact assessment

**Level-3 Subtasks and Level-4 Key Actions:**

- P16.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for the "DFM/DFA Review," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P16.1.1.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for the "DFM/DFA Review," demonstrate using "Design for Manufacturing/Assembly Analysis, Assembly Time Estimation," and clarify the technical approach and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and freeze the solution

- P16.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of the "DFM/DFA Review" based on the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype verification
    - Document anomalies and deviations

- P16.1.1.4 Test Execution and Result Analysis
  - Conduct "DFM/DFA Review" tests according to acceptance criteria, calculate pass rate/error/deviation, perform root cause analysis, and generate an improvement list.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P16.1.1.5 Documentation Output and Downstream Delivery
  - Produce the final report/drawing/specification for the "DFM/DFA Review," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents following templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 소량 시험 생산 및 양산 준비 (Pilot & Production Ramp)

## 핵심 내용
**방법/도구**: 설계 제조 가능성/조립 가능성 분석, 조립 공수 추정

**설계 사고 논리**: 3D 프린팅/CNC 프로토타입을 다이캐스팅, 사출 성형, 판금 등 양산 공정으로 전환

**핵심 제약 조건**: 금형 비용, 수율, 택트 타임

**완료 기준/산출물**: DFM/DFA 보고서, 엔지니어링 변경 목록, 비용 영향 평가

**3단계 하위 작업 및 4단계 핵심 조치:**

- P16.1.1.1 입력 정리 및 목표 정량화
  - 「DFM/DFA 검토」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 수용 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 수용 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P16.1.1.2 방안/방법 설계
  - 「DFM/DFA 검토」에 대한 실행 방법 또는 후보 방안을 수립하고, 「설계 제조 가능성/조립 가능성 분석, 조립 공수 추정」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P16.1.1.3 실행/프로토타입/시제품 제작
  - 설계 방안에 따라 「DFM/DFA 검토」의 실행 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P16.1.1.4 테스트 실행 및 결과 분석
  - 수용 기준에 따라 「DFM/DFA 검토」 테스트를 실행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P16.1.1.5 문서 출력 및 하위 전달
  - 「DFM/DFA 검토」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서 통지
