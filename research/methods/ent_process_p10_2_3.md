---
$id: ent_process_p10_2_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Whole-body control WBC
  zh: 全身控制 WBC
  ko: 全身控制 WBC
summary:
  en: WBC controller, multi-task coordination demonstration, solution time &lt;1 ms
  zh: '- P10.2.3.1 输入梳理与目标量化 - 整理「全身控制 WBC」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: WBC 控制器、多任务协调演示、求解时间 < 1 ms
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
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
**所属阶段/工作包**：运动控制算法开发与验证（Motion Control）

## 核心内容
**方法 / 工具**：QP-based WBC、任务优先级、接触力优化、零空间投影

**设计思考逻辑**：协调下肢平衡、躯干姿态、上肢操作；满足摩擦锥约束

**关键约束**：计算实时性、任务冲突、摩擦锥

**完成标准 / 输出物**：WBC 控制器、多任务协调演示、求解时间 < 1 ms

**三级子任务与四级关键动作：**

- P10.2.3.1 输入梳理与目标量化
  - 整理「全身控制 WBC」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P10.2.3.2 算法/控制方案设计
  - 基于「QP-based WBC、任务优先级、接触力优化、零空间投影」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P10.2.3.3 算法实现与仿真验证
  - 将「全身控制 WBC」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P10.2.3.4 算法调参与性能验证
  - 对「全身控制 WBC」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P10.2.3.5 文档输出与下游交付
  - 输出「全身控制 WBC」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Motion Control Algorithm Development and Validation (Motion Control)

## Content
**Method/Tool**: QP-based WBC, Task Priority, Contact Force Optimization, Null Space Projection

**Design Logic**: Coordinate lower limb balance, torso posture, and upper limb manipulation; satisfy friction cone constraints

**Key Constraints**: Real-time computation, task conflicts, friction cone

**Completion Criteria/Deliverables**: WBC controller, multi-task coordination demonstration, solution time < 1 ms

**Level-3 Sub-tasks and Level-4 Key Actions:**

- P10.2.3.1 Input Sorting and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Whole-Body Control WBC", convert completion criteria into quantifiable acceptance indicators, and clarify Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P10.2.3.2 Algorithm/Control Scheme Design
  - Establish a mathematical model or algorithm framework based on "QP-based WBC, Task Priority, Contact Force Optimization, Null Space Projection", form candidate schemes, evaluate stability, real-time performance, and scalability, and freeze the implementation path.
    - Form at least 2 candidate schemes
    - Establish an evaluation matrix and quantify scoring
    - Organize review and freeze the scheme

- P10.2.3.3 Algorithm Implementation and Simulation Validation
  - Implement the "Whole-Body Control WBC" algorithm in a simulation environment or with offline data, verifying functional correctness, real-time performance, and robustness.
    - Establish model/prototype and record key parameters
    - Execute simulation or prototype validation
    - Record anomalies and deviations

- P10.2.3.4 Algorithm Tuning and Performance Validation
  - Perform parameter tuning and boundary testing on the "Whole-Body Control WBC" algorithm, verifying whether performance under typical/extreme operating conditions meets the indicators.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P10.2.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Whole-Body Control WBC", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documentation according to template and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 운동 제어 알고리즘 개발 및 검증 (Motion Control)

## 핵심 내용
**방법 / 도구**: QP 기반 WBC, 작업 우선순위, 접촉력 최적화, 영공간 투영

**설계 사고 논리**: 하지 균형, 상체 자세, 상지 조작 조정; 마찰 원뿔 제약 조건 충족

**핵심 제약 조건**: 계산 실시간성, 작업 충돌, 마찰 원뿔

**완료 기준 / 산출물**: WBC 제어기, 다중 작업 조정 데모, 해결 시간 < 1 ms

**3단계 하위 작업 및 4단계 핵심 동작:**

- P10.2.3.1 입력 정리 및 목표 정량화
  - 「전신 제어 WBC」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P10.2.3.2 알고리즘/제어 방식 설계
  - 「QP 기반 WBC, 작업 우선순위, 접촉력 최적화, 영공간 투영」을 기반으로 수학적 모델 또는 알고리즘 프레임워크를 구축하여 후보 방안을 형성하고, 안정성, 실시간성 및 확장성을 평가하며 구현 경로를 확정합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P10.2.3.3 알고리즘 구현 및 시뮬레이션 검증
  - 「전신 제어 WBC」의 알고리즘을 시뮬레이션 환경 또는 오프라인 데이터에서 구현하여 기능 정확성, 실시간성 및 강건성을 검증합니다.
    - 모델/프로토타입 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P10.2.3.4 알고리즘 튜닝 및 성능 검증
  - 「전신 제어 WBC」알고리즘의 매개변수 최적화 및 경계 테스트를 수행하여 일반/극한 작업 조건에서의 성능이 지표를 충족하는지 검증합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P10.2.3.5 문서 출력 및 하위 전달
  - 「전신 제어 WBC」최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하여 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
