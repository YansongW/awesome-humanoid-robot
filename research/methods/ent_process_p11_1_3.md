---
$id: ent_process_p11_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Integration of tactile and force sensors
  zh: 触觉与力觉传感器集成
  ko: 触觉与力觉传感器集成
summary:
  en: Sensor deployment scheme, signal processing chain, and calibration method
  zh: '- P11.1.3.1 输入梳理与目标量化 - 整理「触觉与力觉传感器集成」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 传感器布置方案、信号处理链、标定方法
domains:
- 02_components
- 06_design_engineering
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
**所属阶段/工作包**：灵巧手选型/设计与集成（Dexterous Hand）

## 核心内容
**方法 / 工具**：阵列触觉、指尖六维力、关节力矩、滑移检测

**设计思考逻辑**：精细操作依赖触觉反馈；力控保障安全

**关键约束**：布线、信号处理、成本、空间

**完成标准 / 输出物**：传感器布置方案、信号处理链、标定方法

**三级子任务与四级关键动作：**

- P11.1.3.1 输入梳理与目标量化
  - 整理「触觉与力觉传感器集成」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P11.1.3.2 接口与集成策略设计
  - 梳理「触觉与力觉传感器集成」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P11.1.3.3 实施/原型/样件制作
  - 根据设计方案执行「触觉与力觉传感器集成」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P11.1.3.4 验证与问题闭环
  - 对「触觉与力觉传感器集成」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P11.1.3.5 文档输出与下游交付
  - 输出「触觉与力觉传感器集成」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Dexterous Hand Selection/Design and Integration

## Content
**Methods/Tools**: Array tactile sensing, fingertip six-axis force, joint torque, slip detection

**Design Logic**: Fine manipulation relies on tactile feedback; force control ensures safety

**Key Constraints**: Wiring, signal processing, cost, space

**Completion Criteria/Deliverables**: Sensor layout scheme, signal processing chain, calibration method

**Level-3 Subtasks and Level-4 Key Actions:**

- P11.1.3.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Tactile and Force Sensor Integration," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P11.1.3.2 Interface and Integration Strategy Design
  - Review subsystem interfaces, data flow, and timing involved in "Tactile and Force Sensor Integration," and define integration sequence, rollback strategy, and exception handling mechanisms.
    - Develop at least 2 candidate solutions
    - Establish an evaluation matrix with quantitative scoring
    - Organize review and freeze the solution

- P11.1.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Tactile and Force Sensor Integration" according to the design plan, fabricate prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype validation
    - Record anomalies and deviations

- P11.1.3.4 Verification and Issue Closure
  - Verify the output of "Tactile and Force Sensor Integration," check compliance with completion criteria, record issues, and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P11.1.3.5 Documentation Output and Downstream Delivery
  - Produce final reports/drawings/specifications for "Tactile and Force Sensor Integration," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents per template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 다기능 손 선정/설계 및 통합 (Dexterous Hand)

## 핵심 내용
**방법/도구**: 배열 촉각, 손끝 6축 힘, 관절 토크, 미끄러짐 감지

**설계 사고 논리**: 정밀 조작은 촉각 피드백에 의존; 힘 제어는 안전 보장

**주요 제약 조건**: 배선, 신호 처리, 비용, 공간

**완료 기준/산출물**: 센서 배치 계획, 신호 처리 체인, 교정 방법

**3단계 하위 작업 및 4단계 주요 동작:**

- P11.1.3.1 입력 정리 및 목표 정량화
  - 「촉각 및 힘 센서 통합」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P11.1.3.2 인터페이스 및 통합 전략 설계
  - 「촉각 및 힘 센서 통합」과 관련된 하위 시스템 인터페이스, 데이터 흐름 및 타이밍을 정리하고, 통합 순서, 복귀 전략 및 이상 처리 메커니즘을 수립한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P11.1.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「촉각 및 힘 센서 통합」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 주요 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P11.1.3.4 검증 및 문제 해결
  - 「촉각 및 힘 센서 통합」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료 시까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P11.1.3.5 문서 출력 및 하위 전달
  - 「촉각 및 힘 센서 통합」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
