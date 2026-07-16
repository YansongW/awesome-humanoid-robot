---
$id: ent_process_p7_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Calibration of contact and friction parameters
  zh: 接触与摩擦参数标定
  ko: 接触与摩擦参数标定
summary:
  en: Contact parameter table, calibration video/data, single leg standing stability
  zh: '- P7.1.3.1 输入梳理与目标量化 - 整理「接触与摩擦参数标定」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 《接触参数表》、标定视频/数据、单腿站立稳定
domains:
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
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
**所属阶段/工作包**：仿真平台搭建与验证（Simulation）

## 核心内容
**方法 / 工具**：摩擦系数辨识、接触刚度/阻尼调参、单腿站立实验对比

**设计思考逻辑**：通过简单实验调参，使仿真与真实物理响应一致

**关键约束**：仿真稳定性 vs 真实性

**完成标准 / 输出物**：《接触参数表》、标定视频/数据、单腿站立稳定

**三级子任务与四级关键动作：**

- P7.1.3.1 输入梳理与目标量化
  - 整理「接触与摩擦参数标定」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P7.1.3.2 方案/方法设计
  - 针对「接触与摩擦参数标定」制定实施方法或候选方案，使用「摩擦系数辨识、接触刚度/阻尼调参、单腿站立实验对比」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P7.1.3.3 实施/原型/样件制作
  - 根据设计方案执行「接触与摩擦参数标定」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P7.1.3.4 验证与问题闭环
  - 对「接触与摩擦参数标定」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P7.1.3.5 文档输出与下游交付
  - 输出「接触与摩擦参数标定」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Simulation Platform Construction and Validation (Simulation)

## Content
**Method/Tool**: Friction coefficient identification, contact stiffness/damping parameter tuning, single-leg standing experimental comparison

**Design Logic**: Achieve consistency between simulation and real physical response through simple experimental parameter tuning

**Key Constraints**: Simulation stability vs. realism

**Completion Criteria/Deliverables**: "Contact Parameter Table", calibration video/data, single-leg standing stability

**Three-Level Subtasks and Four-Level Key Actions:**

- P7.1.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Contact and Friction Parameter Calibration", convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P7.1.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Contact and Friction Parameter Calibration", conduct demonstration using "friction coefficient identification, contact stiffness/damping parameter tuning, single-leg standing experimental comparison", and clarify the technical roadmap and resource requirements.
    - Formulate no fewer than 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and finalize the solution

- P7.1.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Contact and Friction Parameter Calibration" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Establish model/prototype and record key parameters
    - Execute simulation or prototype validation
    - Record anomalies and deviations

- P7.1.3.4 Verification and Issue Closure
  - Verify the output of "Contact and Friction Parameter Calibration", check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P7.1.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "Contact and Friction Parameter Calibration", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to template and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**：시뮬레이션 플랫폼 구축 및 검증 (Simulation)

## 핵심 내용
**방법 / 도구**：마찰 계수 식별, 접촉 강성/댐핑 파라미터 조정, 단일 다리 서기 실험 비교

**설계 사고 논리**：간단한 실험을 통한 파라미터 조정으로 시뮬레이션과 실제 물리적 응답 일치

**핵심 제약 조건**：시뮬레이션 안정성 vs 현실성

**완료 기준 / 산출물**：《접촉 파라미터 테이블》, 교정 영상/데이터, 단일 다리 서기 안정성

**3단계 하위 작업 및 4단계 핵심 조치：**

- P7.1.3.1 입력 정리 및 목표 정량화
  - 「접촉 및 마찰 파라미터 교정」에 필요한 상위 입력, 참조 기준 및 자원을 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P7.1.3.2 방안/방법 설계
  - 「접촉 및 마찰 파라미터 교정」에 대한 구현 방법 또는 후보 방안을 수립하고, 「마찰 계수 식별, 접촉 강성/댐핑 파라미터 조정, 단일 다리 서기 실험 비교」를 통해 논증하며, 기술 경로와 자원 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P7.1.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「접촉 및 마찰 파라미터 교정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P7.1.3.4 검증 및 문제 종결
  - 「접촉 및 마찰 파라미터 교정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P7.1.3.5 문서 출력 및 하위 전달
  - 「접촉 및 마찰 파라미터 교정」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서 통지
