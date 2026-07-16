---
$id: ent_process_p2_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Human body scale and reachable domain analysis
  zh: 人体尺度与可达域分析
  ko: 人体尺度与可达域分析
summary:
  en: Reachable area reporting, critical operational posture, interference checks
  zh: '- P2.2.1.1 输入梳理与目标量化 - 整理「人体尺度与可达域分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 可达域报告、关键操作姿态、干涉检查
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
**所属阶段/工作包**：工业设计与外观工程（ID / A-Surface）

## 核心内容
**方法 / 工具**：人体测量数据库、CATIA / Jack / RAMSIS、可达域云图

**设计思考逻辑**：验证机器人能完成目标场景所需的操作高度、视野与避障

**关键约束**：关节运动范围未定、需预留裕量

**完成标准 / 输出物**：可达域报告、关键操作姿态、干涉检查

**三级子任务与四级关键动作：**

- P2.2.1.1 输入梳理与目标量化
  - 整理「人体尺度与可达域分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P2.2.1.2 方案/方法设计
  - 针对「人体尺度与可达域分析」制定实施方法或候选方案，使用「人体测量数据库、CATIA / Jack / RAMSIS、可达域云图」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P2.2.1.3 实施/原型/样件制作
  - 根据设计方案执行「人体尺度与可达域分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P2.2.1.4 验证与问题闭环
  - 对「人体尺度与可达域分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P2.2.1.5 文档输出与下游交付
  - 输出「人体尺度与可达域分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Industrial Design and Exterior Engineering (ID / A-Surface)

## Content
**Methods/Tools**: Anthropometric database, CATIA / Jack / RAMSIS, reachability envelope cloud map

**Design Logic**: Verify that the robot can achieve the required operating height, field of view, and obstacle avoidance for the target scenario

**Key Constraints**: Joint range of motion not yet determined, margin must be reserved

**Completion Criteria/Deliverables**: Reachability report, key operating postures, interference check

**Level-3 Subtasks and Level-4 Key Actions:**

- P2.2.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Human Scale and Reachability Analysis," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P2.2.1.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Human Scale and Reachability Analysis," using "anthropometric database, CATIA / Jack / RAMSIS, reachability envelope cloud map" for validation, and clarify the technical approach and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix with quantitative scoring
    - Organize a review and freeze the solution

- P2.2.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Human Scale and Reachability Analysis" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype validation
    - Document anomalies and deviations

- P2.2.1.4 Verification and Issue Closure
  - Verify the output of "Human Scale and Reachability Analysis," check whether completion criteria are met, record issues, and track them to closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P2.2.1.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for "Human Scale and Reachability Analysis," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 산업 디자인 및 외관 엔지니어링 (ID / A-Surface)

## 핵심 내용
**방법/도구**: 인체 측정 데이터베이스, CATIA / Jack / RAMSIS, 도달 영역 클라우드 맵

**설계 사고 논리**: 로봇이 목표 시나리오에 필요한 작업 높이, 시야 및 장애물 회피를 수행할 수 있는지 검증

**핵심 제약 조건**: 관절 운동 범위 미확정, 여유분 확보 필요

**완료 기준/산출물**: 도달 영역 보고서, 핵심 작업 자세, 간섭 검사

**3단계 하위 작업 및 4단계 핵심 동작:**

- P2.2.1.1 입력 정리 및 목표 정량화
  - 「인체 치수 및 도달 영역 분석」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 Owner, 시간 노드 및 위험 등록부 구축

- P2.2.1.2 방안/방법 설계
  - 「인체 치수 및 도달 영역 분석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「인체 측정 데이터베이스, CATIA / Jack / RAMSIS, 도달 영역 클라우드 맵」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P2.2.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「인체 치수 및 도달 영역 분석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P2.2.1.4 검증 및 문제 종결
  - 「인체 치수 및 도달 영역 분석」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하며 종결될 때까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P2.2.1.5 문서 출력 및 하위 전달
  - 「인체 치수 및 도달 영역 분석」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
