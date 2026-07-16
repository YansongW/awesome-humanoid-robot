---
$id: ent_process_p8_2_4
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Simulation-experiment closed-loop iteration
  zh: 仿真-试验闭环迭代
  ko: 仿真-试验闭环迭代
summary:
  en: Error between simulation and test is less than 15% , design iteration record
  zh: '- P8.2.4.1 输入梳理与目标量化 - 整理「仿真-试验闭环迭代」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 仿真与试验误差 < 15%、设计迭代记录
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
**方法 / 工具**：原型加载试验、应变片、位移传感器、与 FEA 对比

**设计思考逻辑**：通过试验修正仿真边界条件与材料参数，形成闭环

**关键约束**：试验夹具、加载精度

**完成标准 / 输出物**：仿真与试验误差 < 15%、设计迭代记录

**三级子任务与四级关键动作：**

- P8.2.4.1 输入梳理与目标量化
  - 整理「仿真-试验闭环迭代」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P8.2.4.2 接口与集成策略设计
  - 梳理「仿真-试验闭环迭代」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P8.2.4.3 建模/仿真与样机实现
  - 建立「仿真-试验闭环迭代」的仿真/数学模型或原型样机，使用「原型加载试验、应变片、位移传感器、与 FEA 对比」执行计算或实验，记录关键参数与边界条件。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P8.2.4.4 测试执行与结果分析
  - 按照验收标准执行「仿真-试验闭环迭代」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P8.2.4.5 文档输出与下游交付
  - 输出「仿真-试验闭环迭代」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Structural FEA

## Content
**Method/Tool**: Prototype loading test, strain gauges, displacement sensors, comparison with FEA

**Design Logic**: Correct simulation boundary conditions and material parameters through testing to form a closed loop

**Key Constraints**: Test fixtures, loading accuracy

**Completion Criteria/Deliverables**: Simulation-to-test error < 15%, design iteration records

**Level-3 Subtasks and Level-4 Key Actions:**

- P8.2.4.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for the "simulation-test closed-loop iteration", convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P8.2.4.2 Interface and Integration Strategy Design
  - Review subsystem interfaces, data flows, and timing involved in the "simulation-test closed-loop iteration", and define integration sequence, rollback strategy, and exception handling mechanism.
    - Develop at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and finalize the solution

- P8.2.4.3 Modeling/Simulation and Prototype Implementation
  - Establish a simulation/mathematical model or prototype for the "simulation-test closed-loop iteration", perform calculations or experiments using "prototype loading test, strain gauges, displacement sensors, comparison with FEA", and record key parameters and boundary conditions.
    - Build the model/prototype and record key parameters
    - Execute simulation or prototype validation
    - Record anomalies and deviations

- P8.2.4.4 Test Execution and Result Analysis
  - Execute the "simulation-test closed-loop iteration" test according to acceptance criteria, calculate pass rate/error/deviation, perform root cause analysis, and generate an improvement list.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P8.2.4.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for the "simulation-test closed-loop iteration", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documentation according to template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 구조 강도 시뮬레이션 및 반복(Structural FEA)

## 핵심 내용
**방법/도구**: 프로토타입 하중 시험, 스트레인 게이지, 변위 센서, FEA와 비교

**설계 사고 논리**: 시험을 통해 시뮬레이션 경계 조건과 재료 매개변수를 수정하여 폐루프 형성

**핵심 제약 조건**: 시험 지그, 하중 정밀도

**완료 기준/산출물**: 시뮬레이션과 시험 오차 < 15%, 설계 반복 기록

**3단계 하위 작업과 4단계 핵심 조치:**

- P8.2.4.1 입력 정리 및 목표 정량화
  - 「시뮬레이션-시험 폐루프 반복」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P8.2.4.2 인터페이스 및 통합 전략 설계
  - 「시뮬레이션-시험 폐루프 반복」에 관련된 하위 시스템 인터페이스, 데이터 흐름 및 시퀀스를 정리하고, 통합 순서, 롤백 전략 및 이상 처리 메커니즘을 수립한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P8.2.4.3 모델링/시뮬레이션 및 프로토타입 구현
  - 「시뮬레이션-시험 폐루프 반복」의 시뮬레이션/수학적 모델 또는 프로토타입을 구축하고, 「프로토타입 하중 시험, 스트레인 게이지, 변위 센서, FEA와 비교」를 사용하여 계산 또는 실험을 수행하며, 주요 매개변수와 경계 조건을 기록한다.
    - 모델/프로토타입 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P8.2.4.4 테스트 실행 및 결과 분석
  - 검수 기준에 따라 「시뮬레이션-시험 폐루프 반복」 테스트를 수행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 통해 개선 목록을 작성한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P8.2.4.5 문서 출력 및 하위 전달
  - 「시뮬레이션-시험 폐루프 반복」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
