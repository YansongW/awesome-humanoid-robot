---
$id: ent_process_p4_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Specification of joint performance requirements
  zh: 关节性能需求精化
  ko: 关节性能需求精化
summary:
  en: Final torque/Speed/bandwidth requirements for each joint V 2
  zh: '- P4.1.1.1 输入梳理与目标量化 - 整理「关节性能需求精化」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 各关节最终扭矩/速度/带宽需求表 v2
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
**所属阶段/工作包**：关节模组与驱动系统设计（Actuator & Drive）

## 核心内容
**方法 / 工具**：P3.1.3 输出 + 安全系数、热裕量、带宽需求

**设计思考逻辑**：峰值扭矩 = 动力学峰值 × 1.5–2.0 安全系数；连续扭矩按持续行走工况

**关键约束**：电机热时间常数、散热能力、反向驱动透明度

**完成标准 / 输出物**：各关节最终扭矩/速度/带宽需求表 v2

**三级子任务与四级关键动作：**

- P4.1.1.1 输入梳理与目标量化
  - 整理「关节性能需求精化」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P4.1.1.2 方案/方法设计
  - 针对「关节性能需求精化」制定实施方法或候选方案，使用「P3.1.3 输出 + 安全系数、热裕量、带宽需求」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P4.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「关节性能需求精化」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P4.1.1.4 验证与问题闭环
  - 对「关节性能需求精化」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P4.1.1.5 文档输出与下游交付
  - 输出「关节性能需求精化」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Joint Module and Drive System Design (Actuator & Drive)

## Content
**Method/Tool**: P3.1.3 Output + Safety Factor, Thermal Margin, Bandwidth Requirement

**Design Logic**: Peak Torque = Dynamic Peak × 1.5–2.0 Safety Factor; Continuous Torque Based on Sustained Walking Conditions

**Key Constraints**: Motor Thermal Time Constant, Heat Dissipation Capacity, Backdrive Transparency

**Completion Criteria/Deliverables**: Final Torque/Speed/Bandwidth Requirement Table v2 for Each Joint

**Level-3 Subtasks and Level-4 Key Actions:**

- P4.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Joint Performance Requirement Refinement," translate completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P4.1.1.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Joint Performance Requirement Refinement," using "P3.1.3 Output + Safety Factor, Thermal Margin, Bandwidth Requirement" for justification, and clarify technical approach and resource needs.
    - Generate at least 2 candidate solutions
    - Establish evaluation matrix and quantify scoring
    - Organize review and freeze the solution

- P4.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Joint Performance Requirement Refinement" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype verification
    - Document anomalies and deviations

- P4.1.1.4 Verification and Issue Closure
  - Verify the output of "Joint Performance Requirement Refinement," check whether completion criteria are met, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P4.1.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "Joint Performance Requirement Refinement," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents per template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**：관절 모듈 및 구동 시스템 설계 (Actuator & Drive)

## 핵심 내용
**방법 / 도구**：P3.1.3 출력 + 안전 계수, 열 여유, 대역폭 요구사항

**설계 사고 논리**：최대 토크 = 동역학 최대값 × 1.5–2.0 안전 계수；연속 토크는 지속 보행 조건 기준

**핵심 제약 조건**：모터 열 시정수, 방열 능력, 역구동 투명성

**완료 기준 / 산출물**：각 관절 최종 토크/속도/대역폭 요구사항 표 v2

**3단계 하위 작업 및 4단계 핵심 조치：**

- P4.1.1.1 입력 정리 및 목표 정량화
  - 「관절 성능 요구사항 정밀화」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P4.1.1.2 방안/방법 설계
  - 「관절 성능 요구사항 정밀화」에 대한 실행 방법 또는 후보 방안을 수립하고, 「P3.1.3 출력 + 안전 계수, 열 여유, 대역폭 요구사항」을 사용하여 논증하며, 기술 경로와 자원 요구사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 수립 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P4.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「관절 성능 요구사항 정밀화」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P4.1.1.4 검증 및 문제 종결
  - 「관절 성능 요구사항 정밀화」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P4.1.1.5 문서 출력 및 하위 전달
  - 「관절 성능 요구사항 정밀화」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
