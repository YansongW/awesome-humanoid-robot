---
$id: ent_process_p1_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Mapping of regulations, standards and safety requirements
  zh: 法规、标准与安全需求映射
  ko: 法规、标准与安全需求映射
summary:
  en: Regulatory requirements matrix, compliance roadmap, security objective level (SIL/PL)
  zh: 方法 / 工具：ISO 10218-1/2、ISO/TS 15066、IEC 61508、IEC 62368、CE/FCC/UL 差距分析
  ko: 法规需求矩阵、合规路线图、安全目标等级（SIL/PL）
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
**方法 / 工具**：ISO 10218-1/2、ISO/TS 15066、IEC 61508、IEC 62368、CE/FCC/UL 差距分析

**设计思考逻辑**：安全需求必须在设计早期成为硬约束，而非后期补票

**关键约束**：地区差异、认证周期、测试费用

**完成标准 / 输出物**：法规需求矩阵、合规路线图、安全目标等级（SIL/PL）

**三级子任务与四级关键动作：**

- P1.1.3.1 输入梳理与目标量化
  - 整理「法规、标准与安全需求映射」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P1.1.3.2 方案/方法设计
  - 针对「法规、标准与安全需求映射」制定实施方法或候选方案，使用「ISO 10218-1/2、ISO/TS 15066、IEC 61508、IEC 62368、CE/FCC/UL 差距分析」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P1.1.3.3 实施/原型/样件制作
  - 根据设计方案执行「法规、标准与安全需求映射」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P1.1.3.4 验证与问题闭环
  - 对「法规、标准与安全需求映射」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P1.1.3.5 文档输出与下游交付
  - 输出「法规、标准与安全需求映射」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Requirements Definition and System Solution (Concept / Pre-A)

## Content
**Methods/Tools**: ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL Gap Analysis

**Design Thinking Logic**: Safety requirements must become hard constraints early in the design phase, rather than being retrofitted later.

**Key Constraints**: Regional differences, certification cycles, testing costs

**Completion Criteria/Deliverables**: Regulatory requirements matrix, compliance roadmap, safety integrity level (SIL/PL)

**Three-Level Sub-Tasks and Four-Level Key Actions:**

- P1.1.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Mapping of Regulations, Standards, and Safety Requirements," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P1.1.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Mapping of Regulations, Standards, and Safety Requirements," conduct feasibility analysis using "ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL Gap Analysis," and clarify the technical roadmap and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the solution

- P1.1.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Mapping of Regulations, Standards, and Safety Requirements" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype verification
    - Document anomalies and deviations

- P1.1.3.4 Verification and Issue Closure
  - Verify the outputs of "Mapping of Regulations, Standards, and Safety Requirements," check whether completion criteria are met, document issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P1.1.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Mapping of Regulations, Standards, and Safety Requirements," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 요구사항 정의 및 시스템 방안 (Concept / Pre-A)

## 핵심 내용
**방법 / 도구**: ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL 차이 분석

**설계 사고 논리**: 안전 요구사항은 설계 초기에 하드 제약 조건이 되어야 하며, 후반에 추가하는 방식이 아님

**핵심 제약 조건**: 지역별 차이, 인증 주기, 테스트 비용

**완료 기준 / 산출물**: 규제 요구사항 매트릭스, 규정 준수 로드맵, 안전 목표 등급 (SIL/PL)

**3단계 하위 작업 및 4단계 핵심 조치:**

- P1.1.3.1 입력 정리 및 목표 정량화
  - 「규제, 표준 및 안전 요구사항 매핑」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P1.1.3.2 방안/방법 설계
  - 「규제, 표준 및 안전 요구사항 매핑」에 대한 구현 방법 또는 후보 방안을 수립하고, 「ISO 10218-1/2, ISO/TS 15066, IEC 61508, IEC 62368, CE/FCC/UL 차이 분석」을 사용하여 논증하며, 기술 경로와 리소스 요구사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P1.1.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「규제, 표준 및 안전 요구사항 매핑」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P1.1.3.4 검증 및 문제 종결
  - 「규제, 표준 및 안전 요구사항 매핑」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하며 종결될 때까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P1.1.3.5 문서 출력 및 하위 전달
  - 「규제, 표준 및 안전 요구사항 매핑」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
