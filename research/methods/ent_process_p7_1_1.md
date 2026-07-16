---
$id: ent_process_p7_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Selection and import of simulation platform
  zh: 仿真平台选型与导入
  ko: 仿真平台选型与导入
summary:
  en: “Simulation platform selection report”, URDF/SDF import success, basic standing simulation through
  zh: 方法 / 工具：Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet 对比
  ko: 《仿真平台选型报告》、URDF/SDF 导入成功、基础站立仿真通过
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
**方法 / 工具**：Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet 对比

**设计思考逻辑**：优先 GPU 并行、接触稳定、传感器仿真完善；不同场景可互补使用

**关键约束**：License、硬件要求、sim-to-real gap、团队熟悉度

**完成标准 / 输出物**：《仿真平台选型报告》、URDF/SDF 导入成功、基础站立仿真通过

**三级子任务与四级关键动作：**

- P7.1.1.1 输入梳理与目标量化
  - 整理「仿真平台选型与导入」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P7.1.1.2 候选方案建立与评估
  - 针对「仿真平台选型与导入」建立候选方案库，使用「Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet 对比」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P7.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「仿真平台选型与导入」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P7.1.1.4 验证与问题闭环
  - 对「仿真平台选型与导入」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P7.1.1.5 文档输出与下游交付
  - 输出「仿真平台选型与导入」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Simulation Platform Setup and Validation (Simulation)

## Content
**Method/Tool**: Comparison of Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet

**Design Logic**: Prioritize GPU parallelism, contact stability, and comprehensive sensor simulation; different scenarios can be used complementarily

**Key Constraints**: License, hardware requirements, sim-to-real gap, team familiarity

**Completion Criteria/Deliverables**: "Simulation Platform Selection Report", successful URDF/SDF import, basic standing simulation passed

**Three-level Subtasks and Four-level Key Actions:**

- P7.1.1.1 Input Review and Goal Quantification
  - Organize upstream inputs, reference standards, and resources required for "Simulation Platform Selection and Import", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P7.1.1.2 Candidate Solution Establishment and Evaluation
  - Establish a candidate solution library for "Simulation Platform Selection and Import", conduct quantitative evaluation using "Comparison of Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet", and determine the final solution after considering cost, performance, supply chain, and maintainability.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P7.1.1.3 Implementation/Prototype/Sample Production
  - Execute the implementation of "Simulation Platform Selection and Import" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Establish models/prototypes and record key parameters
    - Execute simulation or prototype validation
    - Record anomalies and deviations

- P7.1.1.4 Verification and Issue Closure
  - Verify the output of "Simulation Platform Selection and Import", check whether it meets completion criteria, record issues, and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P7.1.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawings/specifications for "Simulation Platform Selection and Import", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to template and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 시뮬레이션 플랫폼 구축 및 검증 (Simulation)

## 핵심 내용
**방법 / 도구**: Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet 비교

**설계 사고 논리**: GPU 병렬 처리, 접촉 안정성, 센서 시뮬레이션 완성도 우선; 다양한 시나리오에서 상호 보완적으로 사용 가능

**핵심 제약 조건**: 라이선스, 하드웨어 요구 사항, sim-to-real 격차, 팀 숙련도

**완료 기준 / 산출물**: 《시뮬레이션 플랫폼 선정 보고서》, URDF/SDF 가져오기 성공, 기본 기립 시뮬레이션 통과

**3단계 하위 작업 및 4단계 핵심 조치:**

- P7.1.1.1 입력 정리 및 목표 정량화
  - 「시뮬레이션 플랫폼 선정 및 가져오기」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P7.1.1.2 후보 방안 수립 및 평가
  - 「시뮬레이션 플랫폼 선정 및 가져오기」에 대한 후보 방안 라이브러리를 구축하고, 「Isaac Sim / Gazebo / MuJoCo / RaiSim / Bullet 비교」를 통해 정량적 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 결정합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P7.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「시뮬레이션 플랫폼 선정 및 가져오기」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P7.1.1.4 검증 및 문제 종결
  - 「시뮬레이션 플랫폼 선정 및 가져오기」의 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P7.1.1.5 문서 출력 및 하위 전달
  - 「시뮬레이션 플랫폼 선정 및 가져오기」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
