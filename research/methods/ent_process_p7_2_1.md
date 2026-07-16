---
$id: ent_process_p7_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Basic standing and walking simulation
  zh: 基础站立与行走仿真
  ko: 基础站立与行走仿真
summary:
  en: Simulation video, stable walking 10m, steering/ramp passing
  zh: '- P7.2.1.1 输入梳理与目标量化 - 整理「基础站立与行走仿真」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 仿真视频、稳定行走 10 m、转向/斜坡通过
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
**方法 / 工具**：LQR/MPC 平衡、CPG/ZMP 步态、PD 位置控制

**设计思考逻辑**：先实现稳定站立与原地踏步，再扩展到前进/转向/斜坡

**关键约束**：算力、仿真速度、模型精度

**完成标准 / 输出物**：仿真视频、稳定行走 10 m、转向/斜坡通过

**三级子任务与四级关键动作：**

- P7.2.1.1 输入梳理与目标量化
  - 整理「基础站立与行走仿真」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P7.2.1.2 方案/方法设计
  - 针对「基础站立与行走仿真」制定实施方法或候选方案，使用「LQR/MPC 平衡、CPG/ZMP 步态、PD 位置控制」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P7.2.1.3 实施/原型/样件制作
  - 根据设计方案执行「基础站立与行走仿真」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P7.2.1.4 验证与问题闭环
  - 对「基础站立与行走仿真」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P7.2.1.5 文档输出与下游交付
  - 输出「基础站立与行走仿真」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Simulation Platform Construction and Validation (Simulation)

## Content
**Method/Tool**: LQR/MPC Balance, CPG/ZMP Gait, PD Position Control

**Design Logic**: First achieve stable standing and in-place stepping, then extend to forward movement, turning, and slopes

**Key Constraints**: Computational power, simulation speed, model accuracy

**Completion Criteria/Deliverables**: Simulation video, stable walking for 10 m, turning/slope traversal

**Level-3 Subtasks and Level-4 Key Actions**:

- P7.2.1.1 Input Review and Goal Quantification
  - Organize upstream inputs, reference standards, and resources required for "Basic Standing and Walking Simulation," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P7.2.1.2 Scheme/Method Design
  - Develop implementation methods or candidate schemes for "Basic Standing and Walking Simulation," using "LQR/MPC Balance, CPG/ZMP Gait, PD Position Control" for demonstration, and clarify technical roadmap and resource requirements.
    - Form at least 2 candidate schemes
    - Establish evaluation matrix and quantify scoring
    - Organize review and freeze the scheme

- P7.2.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Basic Standing and Walking Simulation" according to the design scheme, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Execute simulation or prototype validation
    - Record anomalies and deviations

- P7.2.1.4 Validation and Issue Closure
  - Validate the output of "Basic Standing and Walking Simulation," check whether it meets completion criteria, record issues, and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P7.2.1.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for "Basic Standing and Walking Simulation," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents per template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**：시뮬레이션 플랫폼 구축 및 검증 (Simulation)

## 핵심 내용
**방법 / 도구**：LQR/MPC 균형, CPG/ZMP 보행, PD 위치 제어

**설계 사고 논리**：안정적인 기립 및 제자리 걷기를 먼저 구현한 후, 전진/회전/경사로로 확장

**핵심 제약 조건**：연산 능력, 시뮬레이션 속도, 모델 정밀도

**완료 기준 / 산출물**：시뮬레이션 영상, 안정적인 10m 보행, 회전/경사로 통과

**3단계 하위 작업 및 4단계 핵심 조치：**

- P7.2.1.1 입력 정리 및 목표 정량화
  - 「기본 기립 및 보행 시뮬레이션」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P7.2.1.2 방안/방법 설계
  - 「기본 기립 및 보행 시뮬레이션」에 대한 구현 방법 또는 후보 방안을 수립하고, 「LQR/MPC 균형, CPG/ZMP 보행, PD 위치 제어」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스를 구축하고 정량적으로 점수화
    - 검토를 조직하고 방안 확정

- P7.2.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「기본 기립 및 보행 시뮬레이션」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품을 구축하고 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P7.2.1.4 검증 및 문제 종결
  - 「기본 기립 및 보행 시뮬레이션」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트를 수행하고 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P7.2.1.5 문서 출력 및 하위 전달
  - 「기본 기립 및 보행 시뮬레이션」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
