---
$id: ent_process_p16_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Supplier selection and audit
  zh: 供应商选择与审核
  ko: 供应商选择与审核
summary:
  en: Supplier list, Sample Test Report, qualified supplier list
  zh: '- P16.2.1.1 输入梳理与目标量化 - 整理「供应商选择与审核」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 供应商清单、样品测试报告、合格供方名录
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
**方法 / 工具**：供应商审核、样品承认、IQC、第二供应商开发

**设计思考逻辑**：关键部件（电机、减速器、电池、计算板）需多家备份

**关键约束**：交付周期、质量一致性、价格

**完成标准 / 输出物**：供应商清单、样品测试报告、合格供方名录

**三级子任务与四级关键动作：**

- P16.2.1.1 输入梳理与目标量化
  - 整理「供应商选择与审核」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P16.2.1.2 候选方案建立与评估
  - 针对「供应商选择与审核」建立候选方案库，使用「供应商审核、样品承认、IQC、第二供应商开发」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P16.2.1.3 实施/原型/样件制作
  - 根据设计方案执行「供应商选择与审核」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P16.2.1.4 验证与问题闭环
  - 对「供应商选择与审核」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P16.2.1.5 文档输出与下游交付
  - 输出「供应商选择与审核」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Pilot & Production Ramp

## Content
**Methods/Tools**: Supplier audit, sample approval, IQC, second supplier development

**Design Thinking Logic**: Critical components (motors, reducers, batteries, computing boards) require multiple backups

**Key Constraints**: Lead time, quality consistency, price

**Completion Criteria/Deliverables**: Supplier list, sample test report, approved supplier list

**Level-3 Sub-tasks and Level-4 Key Actions:**

- P16.2.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Supplier Selection and Audit," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P16.2.1.2 Candidate Solution Establishment and Evaluation
  - Establish a candidate solution library for "Supplier Selection and Audit," conduct quantitative evaluation using "Supplier audit, sample approval, IQC, second supplier development," and determine the final solution after considering cost, performance, supply chain, and maintainability.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P16.2.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Supplier Selection and Audit" based on the design plan, fabricate prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P16.2.1.4 Verification and Issue Closure
  - Verify the output of "Supplier Selection and Audit," check whether completion criteria are met, record issues, and track them to closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P16.2.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "Supplier Selection and Audit," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 소량 시험 생산 및 양산 준비 (Pilot & Production Ramp)

## 핵심 내용
**방법 / 도구**: 공급업체 심사, 샘플 승인, IQC, 2차 공급업체 개발

**설계 사고 논리**: 핵심 부품(모터, 감속기, 배터리, 컴퓨팅 보드)은 다중 업체 백업 필요

**핵심 제약 조건**: 납기, 품질 일관성, 가격

**완료 기준 / 산출물**: 공급업체 목록, 샘플 테스트 보고서, 적격 공급업체 명부

**3단계 하위 작업 및 4단계 핵심 조치:**

- P16.2.1.1 입력 정리 및 목표 정량화
  - 「공급업체 선정 및 심사」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P16.2.1.2 후보 방안 수립 및 평가
  - 「공급업체 선정 및 심사」에 대한 후보 방안 라이브러리를 구축하고, 「공급업체 심사, 샘플 승인, IQC, 2차 공급업체 개발」을 사용하여 정량적 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 결정합니다.
    - 2개 이상의 후보 방안 확보
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토를 조직하고 방안 확정

- P16.2.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「공급업체 선정 및 심사」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P16.2.1.4 검증 및 문제 종결
  - 「공급업체 선정 및 심사」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종결될 때까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P16.2.1.5 문서 출력 및 하위 전달
  - 「공급업체 선정 및 심사」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
