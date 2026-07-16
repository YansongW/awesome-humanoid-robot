---
$id: ent_process_p16_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Design of mould and tooling
  zh: 模具与工装设计
  ko: 模具与工装设计
summary:
  en: Tooling drawings, FAI plans, acceptance criteria
  zh: '- P16.1.2.1 输入梳理与目标量化 - 整理「模具与工装设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 模具/工装图纸、FAI 计划、验收标准
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
**方法 / 工具**：压铸模、注塑模、冲压模、夹具、治具、检具

**设计思考逻辑**：保证批量一致性与装配精度

**关键约束**：模具周期、成本、修改难度

**完成标准 / 输出物**：模具/工装图纸、FAI 计划、验收标准

**三级子任务与四级关键动作：**

- P16.1.2.1 输入梳理与目标量化
  - 整理「模具与工装设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P16.1.2.2 概念与详细设计
  - 完成「模具与工装设计」的概念设计、详细设计与接口定义，使用「压铸模、注塑模、冲压模、夹具、治具、检具」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P16.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「模具与工装设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P16.1.2.4 验证与问题闭环
  - 对「模具与工装设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P16.1.2.5 文档输出与下游交付
  - 输出「模具与工装设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Pilot & Production Ramp

## Content
**Method/Tool**: Die-casting mold, injection mold, stamping mold, fixture, jig, gauge

**Design Thinking Logic**: Ensure batch consistency and assembly precision

**Key Constraints**: Mold cycle time, cost, modification difficulty

**Completion Criteria/Deliverables**: Mold/tooling drawings, FAI plan, acceptance criteria

**Level-3 Sub-tasks and Level-4 Key Actions:**

- P16.1.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Mold and Tooling Design," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P16.1.2.2 Concept and Detailed Design
  - Complete the concept design, detailed design, and interface definition for "Mold and Tooling Design," verify feasibility using "die-casting mold, injection mold, stamping mold, fixture, jig, gauge," and output drawings/algorithms/logic frameworks.
    - Develop at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P16.1.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Mold and Tooling Design" according to the design plan, fabricate prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P16.1.2.4 Verification and Issue Closure
  - Verify the output of "Mold and Tooling Design," check whether it meets completion criteria, record issues, and track them until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P16.1.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Mold and Tooling Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 소량 시험 생산 및 양산 준비 (Pilot & Production Ramp)

## 핵심 내용
**방법 / 도구**: 다이캐스팅 금형, 사출 금형, 프레스 금형, 지그, 치공구, 검사구

**설계 사고 논리**: 배치 간 일관성과 조립 정밀도 보장

**핵심 제약 조건**: 금형 주기, 비용, 수정 난이도

**완료 기준 / 산출물**: 금형/치공구 도면, FAI 계획, 검수 기준

**3차 하위 작업과 4차 핵심 동작:**

- P16.1.2.1 입력 정리 및 목표 정량화
  - 「금형과 치공구 설계」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P16.1.2.2 개념 및 상세 설계
  - 「금형과 치공구 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「다이캐스팅 금형, 사출 금형, 프레스 금형, 지그, 치공구, 검사구」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력한다.
    - 2개 이상의 후보 방안 수립
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P16.1.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「금형과 치공구 설계」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P16.1.2.4 검증 및 문제 폐쇄
  - 「금형과 치공구 설계」의 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P16.1.2.5 문서 출력 및 하위 전달
  - 「금형과 치공구 설계」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
