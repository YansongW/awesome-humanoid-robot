---
$id: ent_process_p6_1_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Model of collision and self-interference
  zh: 碰撞与自干涉模型
  ko: 碰撞与自干涉模型
summary:
  en: There is no self-collision false alarm and no environment penetration in key postures
  zh: '- P6.1.3.1 输入梳理与目标量化 - 整理「碰撞与自干涉模型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 典型动作无自碰撞误报、关键姿态无环境穿透
domains:
- 06_design_engineering
- 08_software_middleware
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
**所属阶段/工作包**：URDF 建模与运动学校核（Kinematics & URDF）

## 核心内容
**方法 / 工具**：凸包/简化网格、FCL/PyBullet、碰撞矩阵

**设计思考逻辑**：运动过程中肢体与环境、肢体与肢体不得发生碰撞；碰撞体过紧会误报，过松会漏报

**关键约束**：计算开销、精度、维护性

**完成标准 / 输出物**：典型动作无自碰撞误报、关键姿态无环境穿透

**三级子任务与四级关键动作：**

- P6.1.3.1 输入梳理与目标量化
  - 整理「碰撞与自干涉模型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P6.1.3.2 方案/方法设计
  - 针对「碰撞与自干涉模型」制定实施方法或候选方案，使用「凸包/简化网格、FCL/PyBullet、碰撞矩阵」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P6.1.3.3 实施/原型/样件制作
  - 根据设计方案执行「碰撞与自干涉模型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P6.1.3.4 验证与问题闭环
  - 对「碰撞与自干涉模型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P6.1.3.5 文档输出与下游交付
  - 输出「碰撞与自干涉模型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: URDF Modeling and Kinematics Verification (Kinematics & URDF)

## Content
**Method/Tool**: Convex Hull/Simplified Mesh, FCL/PyBullet, Collision Matrix

**Design Rationale**: During motion, limbs must not collide with the environment or with each other; overly tight collision bodies cause false positives, while overly loose ones cause missed detections.

**Key Constraints**: Computational cost, accuracy, maintainability

**Completion Criteria/Deliverables**: No false self-collision alarms in typical motions, no environmental penetration in key poses

**Level-3 Subtasks and Level-4 Key Actions:**

- P6.1.3.1 Input Review and Target Quantification
  - Organize the upstream inputs, reference standards, and resources required for the "Collision and Self-Interference Model," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm their versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P6.1.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for the "Collision and Self-Interference Model," using "Convex Hull/Simplified Mesh, FCL/PyBullet, Collision Matrix" for justification, and clarify the technical approach and resource requirements.
    - Formulate no fewer than 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and freeze the solution

- P6.1.3.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of the "Collision and Self-Interference Model" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build the model/prototype and record key parameters
    - Perform simulation or prototype verification
    - Document anomalies and deviations

- P6.1.3.4 Verification and Issue Closure
  - Verify the output of the "Collision and Self-Interference Model," check whether it meets the completion criteria, record issues, and track them until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P6.1.3.5 Documentation Output and Downstream Delivery
  - Produce the final report/drawings/specifications for the "Collision and Self-Interference Model," update the ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Publish and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: URDF 모델링 및 운동학 검증 (Kinematics & URDF)

## 핵심 내용
**방법/도구**: 볼록 껍질/단순화 메쉬, FCL/PyBullet, 충돌 매트릭스

**설계 사고 논리**: 운동 과정에서 사지와 환경, 사지와 사지 간 충돌이 발생하지 않아야 함; 충돌체가 너무 조밀하면 오탐지가 발생하고, 너무 느슨하면 누락이 발생함

**핵심 제약 조건**: 계산 비용, 정밀도, 유지보수성

**완료 기준/산출물**: 일반 동작에서 자체 충돌 오탐지 없음, 주요 자세에서 환경 관통 없음

**3단계 하위 작업 및 4단계 핵심 동작:**

- P6.1.3.1 입력 정리 및 목표 정량화
  - 「충돌 및 자체 간섭 모델」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P6.1.3.2 방안/방법 설계
  - 「충돌 및 자체 간섭 모델」에 대한 구현 방법 또는 후보 방안을 수립하고, 「볼록 껍질/단순화 메쉬, FCL/PyBullet, 충돌 매트릭스」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 수립 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P6.1.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「충돌 및 자체 간섭 모델」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P6.1.3.4 검증 및 문제 종결
  - 「충돌 및 자체 간섭 모델」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P6.1.3.5 문서 출력 및 하위 전달
  - 「충돌 및 자체 간섭 모델」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서 통지
