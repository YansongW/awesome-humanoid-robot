---
$id: ent_process_p9_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: List of heat sources and power consumption
  zh: 热源与功耗清单
  ko: 热源与功耗清单
summary:
  en: '“Heat source list”: the components of power consumption, heat power, accounted for'
  zh: '- P9.1.1.1 输入梳理与目标量化 - 整理「热源与功耗清单」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 《热源清单》：各部件功耗、发热功率、占比
domains:
- 06_design_engineering
layers:
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
**所属阶段/工作包**：热管理仿真与迭代（Thermal Management）

## 核心内容
**方法 / 工具**：电机损耗（铜损+铁损）、驱动器损耗、计算平台功耗、传感器功耗统计

**设计思考逻辑**：按连续运行工况统计总发热功率，识别主要热源

**关键约束**：工作制、环境温度、 duty cycle

**完成标准 / 输出物**：《热源清单》：各部件功耗、发热功率、占比

**三级子任务与四级关键动作：**

- P9.1.1.1 输入梳理与目标量化
  - 整理「热源与功耗清单」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P9.1.1.2 方案/方法设计
  - 针对「热源与功耗清单」制定实施方法或候选方案，使用「电机损耗（铜损+铁损）、驱动器损耗、计算平台功耗、传感器功耗统计」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P9.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「热源与功耗清单」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P9.1.1.4 验证与问题闭环
  - 对「热源与功耗清单」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P9.1.1.5 文档输出与下游交付
  - 输出「热源与功耗清单」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Thermal Management Simulation and Iteration (Thermal Management)

## Content
**Method/Tool**: Motor losses (copper loss + iron loss), drive losses, computing platform power consumption, sensor power consumption statistics

**Design Thinking Logic**: Calculate total heat generation power under continuous operating conditions, identify main heat sources

**Key Constraints**: Duty cycle, ambient temperature, duty cycle

**Completion Criteria/Deliverable**: "Heat Source Inventory": power consumption, heat generation power, and proportion of each component

**Three-Level Subtasks and Four-Level Key Actions:**

- P9.1.1.1 Input Review and Target Quantification
  - Organize the upstream inputs, reference standards, and resources required for the "Heat Source and Power Consumption Inventory", convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P9.1.1.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for the "Heat Source and Power Consumption Inventory", use "motor losses (copper loss + iron loss), drive losses, computing platform power consumption, sensor power consumption statistics" for demonstration, and clarify the technical route and resource requirements.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize a review and freeze the solution

- P9.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation work of the "Heat Source and Power Consumption Inventory" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P9.1.1.4 Verification and Issue Closure
  - Verify the output of the "Heat Source and Power Consumption Inventory", check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P9.1.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification of the "Heat Source and Power Consumption Inventory", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to the template and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 열 관리 시뮬레이션 및 반복(Thermal Management)

## 핵심 내용
**방법/도구**: 모터 손실(동손+철손), 드라이버 손실, 계산 플랫폼 전력 소비, 센서 전력 소비 통계

**설계 사고 논리**: 연속 운전 조건에 따라 총 발열 전력을 통계하고 주요 열원 식별

**주요 제약 조건**: 작업 제도, 환경 온도, duty cycle

**완료 기준/산출물**: 《열원 목록》: 각 부품의 전력 소비, 발열 전력, 비율

**3단계 하위 작업 및 4단계 주요 조치:**

- P9.1.1.1 입력 정리 및 목표 정량화
  - 「열원 및 전력 소비 목록」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P9.1.1.2 방안/방법 설계
  - 「열원 및 전력 소비 목록」에 대한 구현 방법 또는 후보 방안을 수립하고, 「모터 손실(동손+철손), 드라이버 손실, 계산 플랫폼 전력 소비, 센서 전력 소비 통계」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P9.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「열원 및 전력 소비 목록」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록.
    - 모델/시제품 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P9.1.1.4 검증 및 문제 종결
  - 「열원 및 전력 소비 목록」 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P9.1.1.5 문서 출력 및 하위 전달
  - 「열원 및 전력 소비 목록」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
