---
$id: ent_process_p8_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: FEA model preparation
  zh: FEA 模型准备
  ko: FEA 模型准备
summary:
  en: High-quality FEA models, mesh quality reports, checklists of boundary conditions
  zh: '- P8.1.2.1 输入梳理与目标量化 - 整理「FEA 模型准备」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 高质量 FEA 模型、网格质量报告、边界条件清单
domains:
- 06_design_engineering
- 03_manufacturing_processes
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
**所属阶段/工作包**：结构强度仿真与迭代（Structural FEA）

## 核心内容
**方法 / 工具**：HyperMesh / ANSA / Abaqus / ANSYS、网格收敛分析

**设计思考逻辑**：简化非承力特征、合理网格划分、材料属性、接触/绑定设置

**关键约束**：网格质量、计算时间、资源

**完成标准 / 输出物**：高质量 FEA 模型、网格质量报告、边界条件清单

**三级子任务与四级关键动作：**

- P8.1.2.1 输入梳理与目标量化
  - 整理「FEA 模型准备」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P8.1.2.2 方案/方法设计
  - 针对「FEA 模型准备」制定实施方法或候选方案，使用「HyperMesh / ANSA / Abaqus / ANSYS、网格收敛分析」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P8.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「FEA 模型准备」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P8.1.2.4 验证与问题闭环
  - 对「FEA 模型准备」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P8.1.2.5 文档输出与下游交付
  - 输出「FEA 模型准备」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Structural Strength Simulation and Iteration (Structural FEA)

## Content
**Method/Tool**: HyperMesh / ANSA / Abaqus / ANSYS, Mesh Convergence Analysis

**Design Thinking Logic**: Simplify non-load-bearing features, reasonable mesh division, material properties, contact/binding settings

**Key Constraints**: Mesh quality, computation time, resources

**Completion Criteria/Deliverables**: High-quality FEA model, mesh quality report, boundary condition list

**Level-3 Subtasks and Level-4 Key Actions**:

- P8.1.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "FEA Model Preparation", convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P8.1.2.2 Scheme/Method Design
  - Develop implementation methods or candidate schemes for "FEA Model Preparation", use "HyperMesh / ANSA / Abaqus / ANSYS, Mesh Convergence Analysis" for demonstration, and clarify the technical roadmap and resource requirements.
    - Formulate at least 2 candidate schemes
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the scheme

- P8.1.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "FEA Model Preparation" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P8.1.2.4 Verification and Issue Closure
  - Verify the output of "FEA Model Preparation", check whether it meets the completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P8.1.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "FEA Model Preparation", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 구조 강도 시뮬레이션 및 반복 (Structural FEA)

## 핵심 내용
**방법 / 도구**: HyperMesh / ANSA / Abaqus / ANSYS, 메쉬 수렴 분석

**설계 사고 논리**: 비하중 특성 단순화, 적절한 메쉬 분할, 재료 속성, 접촉/구속 설정

**주요 제약 조건**: 메쉬 품질, 계산 시간, 리소스

**완료 기준 / 산출물**: 고품질 FEA 모델, 메쉬 품질 보고서, 경계 조건 목록

**3단계 하위 작업 및 4단계 주요 조치:**

- P8.1.2.1 입력 정리 및 목표 정량화
  - 「FEA 모델 준비」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P8.1.2.2 방안/방법 설계
  - 「FEA 모델 준비」에 대한 구현 방법 또는 후보 방안을 수립하고, 「HyperMesh / ANSA / Abaqus / ANSYS, 메쉬 수렴 분석」을 사용하여 검토하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P8.1.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「FEA 모델 준비」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 주요 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P8.1.2.4 검증 및 문제 종결
  - 「FEA 모델 준비」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하며 종결될 때까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P8.1.2.5 문서 출력 및 하위 전달
  - 「FEA 모델 준비」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
