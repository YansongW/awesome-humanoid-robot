---
$id: ent_process_p16_3_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Cost Accounting and cost reduction
  zh: 成本核算与降本
  ko: 成本核算与降本
summary:
  en: Small-batch cost analysis report, cost reduction project list
  zh: '- P16.3.2.1 输入梳理与目标量化 - 整理「成本核算与降本」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 小批量成本分析报告、降本项目清单
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
**方法 / 工具**：实际 BOM、制造成本、良率影响、VA/VE

**设计思考逻辑**：小批量数据修正早期成本模型，为量产定价提供依据

**关键约束**：规模经济、供应商议价能力

**完成标准 / 输出物**：小批量成本分析报告、降本项目清单

**三级子任务与四级关键动作：**

- P16.3.2.1 输入梳理与目标量化
  - 整理「成本核算与降本」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P16.3.2.2 方案/方法设计
  - 针对「成本核算与降本」制定实施方法或候选方案，使用「实际 BOM、制造成本、良率影响、VA/VE」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P16.3.2.3 实施/原型/样件制作
  - 根据设计方案执行「成本核算与降本」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P16.3.2.4 验证与问题闭环
  - 对「成本核算与降本」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P16.3.2.5 文档输出与下游交付
  - 输出「成本核算与降本」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Pilot & Production Ramp

## Content
**Method/Tool**: Actual BOM, Manufacturing Cost, Yield Impact, VA/VE

**Design Thinking Logic**: Correct early cost models with pilot data to provide basis for production pricing

**Key Constraints**: Economies of scale, supplier bargaining power

**Completion Criteria/Deliverables**: Pilot cost analysis report, cost reduction project list

**Level-3 Sub-tasks and Level-4 Key Actions:**

- P16.3.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "cost accounting and cost reduction," convert completion criteria into quantifiable acceptance indicators, and define owners and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owners, timelines, and risk register

- P16.3.2.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "cost accounting and cost reduction," demonstrate using "actual BOM, manufacturing cost, yield impact, VA/VE," and clarify technical roadmap and resource requirements.
    - Formulate no fewer than 2 candidate solutions
    - Establish an evaluation matrix with quantitative scoring
    - Organize review and freeze the solution

- P16.3.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "cost accounting and cost reduction" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P16.3.2.4 Verification and Issue Closure
  - Verify the output of "cost accounting and cost reduction," check whether it meets completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P16.3.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "cost accounting and cost reduction," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents per template and cite raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 소량 시험 생산 및 양산 준비 (Pilot & Production Ramp)

## 핵심 내용
**방법/도구**: 실제 BOM, 제조 비용, 수율 영향, VA/VE

**설계 사고 논리**: 소량 데이터로 초기 비용 모델을 수정하여 양산 가격 책정의 근거 제공

**핵심 제약 조건**: 규모의 경제, 공급업체 협상력

**완료 기준/산출물**: 소량 비용 분석 보고서, 원가 절감 프로젝트 목록

**3단계 하위 작업 및 4단계 핵심 조치:**

- P16.3.2.1 입력 정리 및 목표 정량화
  - 「원가 계산 및 원가 절감」에 필요한 상위 입력, 참조 기준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 전환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화 가능한 KPI로 전환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P16.3.2.2 방안/방법 설계
  - 「원가 계산 및 원가 절감」에 대한 실행 방법 또는 후보 방안을 수립하고, 「실제 BOM, 제조 비용, 수율 영향, VA/VE」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P16.3.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「원가 계산 및 원가 절감」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P16.3.2.4 검증 및 문제 종결
  - 「원가 계산 및 원가 절감」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P16.3.2.5 문서 출력 및 하위 전달
  - 「원가 계산 및 원가 절감」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
