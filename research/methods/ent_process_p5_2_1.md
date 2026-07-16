---
$id: ent_process_p5_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Structural material selection
  zh: 结构材料选型
  ko: 结构材料选型
summary:
  en: 'Material Selection Table: Materials, Processes, and Reasons for Each Component'
  zh: '- P5.2.1.1 输入梳理与目标量化 - 整理「结构材料选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记'
  ko: 《材料选型表》：各部件材料、工艺、原因
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
**方法 / 工具**：铝合金 7075/6061、碳纤维、钛合金、工程塑料对比

**设计思考逻辑**：高载荷连杆用铝合金/CNC，外壳/支架用 SLS/MJF 3D 打印或注塑

**关键约束**：强度、刚度、密度、成本、批量制造可行性

**完成标准 / 输出物**：《材料选型表》：各部件材料、工艺、原因

**三级子任务与四级关键动作：**

- P5.2.1.1 输入梳理与目标量化
  - 整理「结构材料选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P5.2.1.2 候选方案建立与评估
  - 针对「结构材料选型」建立候选方案库，使用「铝合金 7075/6061、碳纤维、钛合金、工程塑料对比」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P5.2.1.3 实施/原型/样件制作
  - 根据设计方案执行「结构材料选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P5.2.1.4 验证与问题闭环
  - 对「结构材料选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P5.2.1.5 文档输出与下游交付
  - 输出「结构材料选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Mechanical Structure

## Content
**Method/Tool**: Comparison of aluminum alloys 7075/6061, carbon fiber, titanium alloy, and engineering plastics

**Design Logic**: Use aluminum alloy/CNC for high-load connecting rods; use SLS/MJF 3D printing or injection molding for housings/brackets

**Key Constraints**: Strength, stiffness, density, cost, manufacturability for mass production

**Completion Criteria/Deliverables**: "Material Selection Table": material, process, and rationale for each component

**Level-3 Subtasks and Level-4 Key Actions:**

- P5.2.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Structural Material Selection"; convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P5.2.1.2 Candidate Solution Development and Evaluation
  - Build a candidate solution library for "Structural Material Selection"; conduct quantitative evaluation using "Comparison of aluminum alloys 7075/6061, carbon fiber, titanium alloy, and engineering plastics"; determine the final solution after considering cost, performance, supply chain, and maintainability.
    - Develop no fewer than 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P5.2.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Structural Material Selection" according to the design plan; fabricate prototypes, samples, or complete key steps; record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Document anomalies and deviations

- P5.2.1.4 Verification and Issue Closure
  - Verify the output of "Structural Material Selection"; check whether completion criteria are met; record issues and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P5.2.1.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for "Structural Material Selection"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream processes.
    - Write documents according to template and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 본체 구조 엔지니어링 및 프로토타입 (Mechanical Structure)

## 핵심 내용
**방법 / 도구**: 알루미늄 합금 7075/6061, 탄소 섬유, 티타늄 합금, 엔지니어링 플라스틱 비교

**설계 사고 논리**: 고하중 커넥팅 로드는 알루미늄 합금/CNC 사용, 외부 케이싱/브래킷은 SLS/MJF 3D 프린팅 또는 사출 성형 사용

**핵심 제약 조건**: 강도, 강성, 밀도, 비용, 양산 가능성

**완료 기준 / 산출물**: 《재료 선정표》: 각 부품의 재료, 공정, 이유

**3단계 하위 작업 및 4단계 핵심 조치:**

- P5.2.1.1 입력 정리 및 목표 정량화
  - 「구조 재료 선정」에 필요한 상위 입력, 참조 기준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P5.2.1.2 후보 방안 수립 및 평가
  - 「구조 재료 선정」에 대한 후보 방안 라이브러리를 구축하고, 「알루미늄 합금 7075/6061, 탄소 섬유, 티타늄 합금, 엔지니어링 플라스틱 비교」를 사용하여 정량 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 결정합니다.
    - 2개 이상의 후보 방안 형성
    - 평가 매트릭스 구축 및 정량 점수 부여
    - 검토 조직 및 방안 확정

- P5.2.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「구조 재료 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P5.2.1.4 검증 및 문제 종결
  - 「구조 재료 선정」 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P5.2.1.5 문서 출력 및 하위 전달
  - 「구조 재료 선정」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
