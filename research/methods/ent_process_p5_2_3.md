---
$id: ent_process_p5_2_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Process evaluation for mass production
  zh: 面向量产工艺评估
  ko: 面向量产工艺评估
summary:
  en: Mass production process roadmap, key parts of the process selection
  zh: '- P5.2.3.1 输入梳理与目标量化 - 整理「面向量产工艺评估」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 量产工艺路线图、关键件工艺选择
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
**方法 / 工具**：压铸、注塑、钣金、CNC、复材成型工艺对比

**设计思考逻辑**：原型验证后需将 3D 打印件转换为可量产工艺

**关键约束**：模具成本、最小订单量、良率、周期

**完成标准 / 输出物**：量产工艺路线图、关键件工艺选择

**三级子任务与四级关键动作：**

- P5.2.3.1 输入梳理与目标量化
  - 整理「面向量产工艺评估」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P5.2.3.2 方案/方法设计
  - 针对「面向量产工艺评估」制定实施方法或候选方案，使用「压铸、注塑、钣金、CNC、复材成型工艺对比」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P5.2.3.3 实施/原型/样件制作
  - 根据设计方案执行「面向量产工艺评估」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P5.2.3.4 验证与问题闭环
  - 对「面向量产工艺评估」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P5.2.3.5 文档输出与下游交付
  - 输出「面向量产工艺评估」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Mechanical Structure

## Content
**Method/Tool**: Comparison of die casting, injection molding, sheet metal, CNC, and composite forming processes

**Design Thinking Logic**: After prototype validation, 3D printed parts need to be converted into mass-producible processes

**Key Constraints**: Mold cost, minimum order quantity, yield rate, cycle time

**Completion Criteria/Deliverables**: Mass production process roadmap, process selection for key parts

**Level-3 Subtasks and Level-4 Key Actions:**

- P5.2.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "mass production process evaluation," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P5.2.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "mass production process evaluation," using "comparison of die casting, injection molding, sheet metal, CNC, and composite forming processes" for justification, and clarify the technical route and resource requirements.
    - Generate no fewer than 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the solution

- P5.2.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "mass production process evaluation" according to the design solution, fabricate prototypes or samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype validation
    - Record anomalies and deviations

- P5.2.3.4 Verification and Issue Closure
  - Verify the output of "mass production process evaluation," check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P5.2.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "mass production process evaluation," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 본체 구조 엔지니어링 및 프로토타입(Mechanical Structure)

## 핵심 내용
**방법 / 도구**: 다이캐스팅, 사출 성형, 판금, CNC, 복합재 성형 공정 비교

**설계 사고 논리**: 프로토타입 검증 후 3D 프린팅 부품을 양산 가능 공정으로 전환 필요

**핵심 제약 조건**: 금형 비용, 최소 주문량, 수율, 사이클 타임

**완료 기준 / 산출물**: 양산 공정 로드맵, 핵심 부품 공정 선정

**3단계 하위 작업 및 4단계 핵심 액션:**

- P5.2.3.1 입력 정리 및 목표 정량화
  - 「양산 지향 공정 평가」에 필요한 상위 입력, 참조 기준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P5.2.3.2 방안/방법 설계
  - 「양산 지향 공정 평가」를 위한 실행 방법 또는 후보 방안을 수립하고, 「다이캐스팅, 사출 성형, 판금, CNC, 복합재 성형 공정 비교」를 통해 논증하며, 기술 경로와 리소스 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P5.2.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「양산 지향 공정 평가」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P5.2.3.4 검증 및 문제 종결
  - 「양산 지향 공정 평가」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P5.2.3.5 문서 출력 및 하위 전달
  - 「양산 지향 공정 평가」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서 통지
