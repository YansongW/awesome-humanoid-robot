---
$id: ent_process_p3_2_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Communication network architecture
  zh: 通信网络架构
  ko: 通信网络架构
summary:
  en: Communication topology, protocol allocation table, bandwidth/delay budget
  zh: '- P3.2.2.1 输入梳理与目标量化 - 整理「通信网络架构」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记'
  ko: 通信拓扑图、协议分配表、带宽/延迟预算
domains:
- 06_design_engineering
- 02_components
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
**所属阶段/工作包**：系统架构与机电总体设计（System / Preliminary Design）

## 核心内容
**方法 / 工具**：CAN-FD / EtherCAT / Ethernet / TSN 带宽与时延分析

**设计思考逻辑**：关节控制需要高实时性，视觉/AI 需要高带宽；必要时双总线

**关键约束**：线缆数量、EMC、成本、可扩展性

**完成标准 / 输出物**：通信拓扑图、协议分配表、带宽/延迟预算

**三级子任务与四级关键动作：**

- P3.2.2.1 输入梳理与目标量化
  - 整理「通信网络架构」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P3.2.2.2 方案/方法设计
  - 针对「通信网络架构」制定实施方法或候选方案，使用「CAN-FD / EtherCAT / Ethernet / TSN 带宽与时延分析」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P3.2.2.3 实施/原型/样件制作
  - 根据设计方案执行「通信网络架构」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P3.2.2.4 验证与问题闭环
  - 对「通信网络架构」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P3.2.2.5 文档输出与下游交付
  - 输出「通信网络架构」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: System Architecture and Electromechanical Overall Design (System / Preliminary Design)

## Content
**Method/Tool**: CAN-FD / EtherCAT / Ethernet / TSN bandwidth and latency analysis

**Design Logic**: Joint control requires high real-time performance, vision/AI requires high bandwidth; dual bus if necessary

**Key Constraints**: Cable quantity, EMC, cost, scalability

**Completion Criteria/Deliverables**: Communication topology diagram, protocol allocation table, bandwidth/latency budget

**Three-level Subtasks and Four-level Key Actions:**

- P3.2.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Communication Network Architecture," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P3.2.2.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Communication Network Architecture," use "CAN-FD / EtherCAT / Ethernet / TSN bandwidth and latency analysis" for validation, and clarify technical route and resource requirements.
    - Form at least 2 candidate solutions
    - Establish evaluation matrix and quantify scoring
    - Organize review and freeze the solution

- P3.2.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Communication Network Architecture" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P3.2.2.4 Verification and Issue Closure
  - Verify the output of "Communication Network Architecture," check if completion criteria are met, record issues, and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P3.2.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "Communication Network Architecture," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 시스템 아키텍처 및 전기기계 종합 설계 (System / Preliminary Design)

## 핵심 내용
**방법 / 도구**: CAN-FD / EtherCAT / Ethernet / TSN 대역폭 및 지연 분석

**설계 사고 논리**: 관절 제어는 높은 실시간성, 비전/AI는 높은 대역폭 필요; 필요 시 이중 버스 사용

**핵심 제약 조건**: 케이블 수량, EMC, 비용, 확장성

**완료 기준 / 산출물**: 통신 토폴로지 다이어그램, 프로토콜 할당표, 대역폭/지연 예산

**3단계 하위 작업 및 4단계 핵심 동작:**

- P3.2.2.1 입력 정리 및 목표 정량화
  - 「통신 네트워크 아키텍처」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 Owner, 시간 노드 및 위험 등록부 구축

- P3.2.2.2 방안/방법 설계
  - 「통신 네트워크 아키텍처」에 대한 구현 방법 또는 후보 방안을 수립하고, 「CAN-FD / EtherCAT / Ethernet / TSN 대역폭 및 지연 분석」을 통해 논증하며, 기술 경로와 리소스 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P3.2.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「통신 네트워크 아키텍처」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P3.2.2.4 검증 및 문제 종결
  - 「통신 네트워크 아키텍처」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P3.2.2.5 문서 출력 및 하위 전달
  - 「통신 네트워크 아키텍처」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
