---
$id: ent_process_p5_2_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Design for Additive Manufacturing (DfAM)
  zh: 面向增材制造的设计（DfAM）
  ko: 面向增材制造的设计（DfAM）
summary:
  en: DfAM checklist, 3D print drawings, print parameters
  zh: '- P5.2.2.1 输入梳理与目标量化 - 整理「面向增材制造的设计（DfAM）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: DfAM 检查清单、3D 打印件图纸、打印参数
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
**所属阶段/工作包**：本体结构工程与原型（Mechanical Structure）

## 核心内容
**方法 / 工具**：SLS/MJF/SLA 设计规范、支撑优化、晶格结构

**设计思考逻辑**：原型阶段大量结构件采用 3D 打印，需针对打印工艺优化

**关键约束**：打印材料强度、层间结合、尺寸精度、表面质量

**完成标准 / 输出物**：DfAM 检查清单、3D 打印件图纸、打印参数

**三级子任务与四级关键动作：**

- P5.2.2.1 输入梳理与目标量化
  - 整理「面向增材制造的设计（DfAM）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P5.2.2.2 概念与详细设计
  - 完成「面向增材制造的设计（DfAM）」的概念设计、详细设计与接口定义，使用「SLS/MJF/SLA 设计规范、支撑优化、晶格结构」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P5.2.2.3 实施/原型/样件制作
  - 根据设计方案执行「面向增材制造的设计（DfAM）」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P5.2.2.4 验证与问题闭环
  - 对「面向增材制造的设计（DfAM）」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P5.2.2.5 文档输出与下游交付
  - 输出「面向增材制造的设计（DfAM）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Mechanical Structure

## Content
**Methods/Tools**: SLS/MJF/SLA Design Guidelines, Support Optimization, Lattice Structures

**Design Thinking Logic**: In the prototype phase, a large number of structural parts are manufactured via 3D printing, requiring optimization for the printing process.

**Key Constraints**: Print material strength, interlayer bonding, dimensional accuracy, surface quality

**Completion Criteria/Deliverables**: DfAM checklist, 3D printed part drawings, print parameters

**Level-3 Subtasks and Level-4 Key Actions:**

- P5.2.2.1 Input Review and Target Quantification
  - Organize the upstream inputs, reference standards, and resources required for Design for Additive Manufacturing (DfAM); convert completion criteria into quantifiable acceptance indicators; and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owners, timelines, and risk registers

- P5.2.2.2 Conceptual and Detailed Design
  - Complete the conceptual design, detailed design, and interface definition for Design for Additive Manufacturing (DfAM); verify feasibility using SLS/MJF/SLA design guidelines, support optimization, and lattice structures; and output drawings/algorithms/logic frameworks.
    - Generate at least two candidate solutions
    - Establish an evaluation matrix with quantitative scoring
    - Organize a review and freeze the solution

- P5.2.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of Design for Additive Manufacturing (DfAM) according to the design plan; produce prototypes, samples, or complete key steps; and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype verification
    - Document anomalies and deviations

- P5.2.2.4 Verification and Issue Closure
  - Verify the output of Design for Additive Manufacturing (DfAM); check whether completion criteria are met; record issues and track them to closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue lists and improvement actions

- P5.2.2.5 Documentation and Downstream Delivery
  - Output the final report/drawings/specifications for Design for Additive Manufacturing (DfAM); update the ICD/BOM/SOP/requirements traceability chain; and complete formal delivery to downstream stages.
    - Write documents according to templates and cite raw data
    - Complete internal reviews and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 본체 구조 공학 및 프로토타입(Mechanical Structure)

## 핵심 내용
**방법/도구**: SLS/MJF/SLA 설계 규범, 서포트 최적화, 격자 구조

**설계 사고 논리**: 프로토타입 단계에서 많은 구조 부품이 3D 프린팅을 사용하므로, 프린팅 공정에 맞춰 최적화해야 함

**핵심 제약 조건**: 프린팅 재료 강도, 층간 결합, 치수 정밀도, 표면 품질

**완료 기준/산출물**: DfAM 체크리스트, 3D 프린팅 부품 도면, 프린팅 파라미터

**3단계 하위 작업 및 4단계 핵심 동작:**

- P5.2.2.1 입력 정리 및 목표 정량화
  - 「적층 제조를 위한 설계(DfAM)」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 Owner, 시간 노드 및 위험 등록부 구축

- P5.2.2.2 개념 및 상세 설계
  - 「적층 제조를 위한 설계(DfAM)」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「SLS/MJF/SLA 설계 규범, 서포트 최적화, 격자 구조」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P5.2.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「적층 제조를 위한 설계(DfAM)」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 공정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P5.2.2.4 검증 및 문제 종결
  - 「적층 제조를 위한 설계(DfAM)」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P5.2.2.5 문서 출력 및 하위 전달
  - 「적층 제조를 위한 설계(DfAM)」의 최종 보고서/도면/규범을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
