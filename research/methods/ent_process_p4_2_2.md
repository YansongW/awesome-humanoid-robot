---
$id: ent_process_p4_2_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Selection of reducer and transmission
  zh: 减速器与传动选型
  ko: 减速器与传动选型
summary:
  en: Reducer specification, chain drawing, stiffness/backlash budget
  zh: '- P4.2.2.1 输入梳理与目标量化 - 整理「减速器与传动选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 减速器规格、传动链图纸、刚度/背隙预算
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
**方法 / 工具**：谐波、行星、摆线、同步带、丝杠对比；背隙/刚度/寿命测试

**设计思考逻辑**：输出端力矩/位置传感器配置决定控制精度；传动链刚度影响带宽

**关键约束**：谐波柔轮疲劳、行星磨损、噪音、成本

**完成标准 / 输出物**：减速器规格、传动链图纸、刚度/背隙预算

**三级子任务与四级关键动作：**

- P4.2.2.1 输入梳理与目标量化
  - 整理「减速器与传动选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P4.2.2.2 候选方案建立与评估
  - 针对「减速器与传动选型」建立候选方案库，使用「谐波、行星、摆线、同步带、丝杠对比；背隙/刚度/寿命测试」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P4.2.2.3 实施/原型/样件制作
  - 根据设计方案执行「减速器与传动选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P4.2.2.4 验证与问题闭环
  - 对「减速器与传动选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P4.2.2.5 文档输出与下游交付
  - 输出「减速器与传动选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Joint Module and Drive System Design (Actuator & Drive)

## Content
**Methods/Tools**: Comparison of harmonic, planetary, cycloidal, synchronous belt, and lead screw; backlash/stiffness/lifetime testing

**Design Thinking Logic**: Output torque/position sensor configuration determines control accuracy; transmission chain stiffness affects bandwidth

**Key Constraints**: Harmonic flexspline fatigue, planetary wear, noise, cost

**Completion Criteria/Deliverables**: Reducer specifications, transmission chain drawings, stiffness/backlash budget

**Level-3 Subtasks and Level-4 Key Actions:**

- P4.2.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Reducer and Transmission Selection", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P4.2.2.2 Candidate Solution Establishment and Evaluation
  - Establish a candidate solution library for "Reducer and Transmission Selection", use "Comparison of harmonic, planetary, cycloidal, synchronous belt, and lead screw; backlash/stiffness/lifetime testing" for quantitative evaluation, and determine the final solution after considering cost, performance, supply chain, and maintainability.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the solution

- P4.2.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation work of "Reducer and Transmission Selection" according to the design solution, fabricate prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P4.2.2.4 Verification and Issue Closure
  - Verify the output of "Reducer and Transmission Selection", check whether it meets the completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P4.2.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Reducer and Transmission Selection", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 관절 모듈 및 구동 시스템 설계 (Actuator & Drive)

## 핵심 내용
**방법 / 도구**: 하모닉, 유성, 사이클로이드, 타이밍 벨트, 볼스크류 비교; 백래시/강성/수명 테스트

**설계 사고 논리**: 출력단 토크/위치 센서 구성이 제어 정밀도를 결정; 전동 체인 강성이 대역폭에 영향

**핵심 제약 조건**: 하모닉 플렉스플라인 피로, 유성 마모, 소음, 비용

**완료 기준 / 산출물**: 감속기 사양, 전동 체인 도면, 강성/백래시 예산

**3단계 하위 작업 및 4단계 핵심 조치:**

- P4.2.2.1 입력 정리 및 목표 정량화
  - 「감속기 및 전동 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P4.2.2.2 후보方案 수립 및 평가
  - 「감속기 및 전동 선정」에 대한 후보方案 라이브러리를 구축하고, 「하모닉, 유성, 사이클로이드, 타이밍 벨트, 볼스크류 비교; 백래시/강성/수명 테스트」를 사용하여 정량 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종方案을 결정.
    - 2개 이상의 후보方案 구성
    - 평가 매트릭스 구축 및 정량 점수화
    - 검토 조직 및方案 확정

- P4.2.2.3 구현/프로토타입/시제품 제작
  - 설계方案에 따라 「감속기 및 전동 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 공정 데이터를 기록.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P4.2.2.4 검증 및 문제 종결
  - 「감속기 및 전동 선정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하며 종결될 때까지 추적.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P4.2.2.5 문서 출력 및 하위 전달
  - 「감속기 및 전동 선정」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
