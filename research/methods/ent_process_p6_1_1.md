---
$id: ent_process_p6_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: URDF/SDF file generation
  zh: URDF/SDF 文件生成
  ko: URDF/SDF 文件生成
summary:
  en: It loads correctly in RViz/Gazebo/Isaac Sim with no parsing errors
  zh: 方法 / 工具：ROS URDF、Xacro、SolidWorks/NX → URDF 插件、惯性参数校核
  ko: 可在 RViz/Gazebo/Isaac Sim 中正确加载、无解析错误
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
**方法 / 工具**：ROS URDF、Xacro、SolidWorks/NX → URDF 插件、惯性参数校核

**设计思考逻辑**：连杆、关节、惯性、碰撞体、视觉模型需与 CAD 完全一致；质量属性来自 P3.1.2/P3.1.3

**关键约束**：坐标系一致性、单位统一、碰撞体不能太密

**完成标准 / 输出物**：可在 RViz/Gazebo/Isaac Sim 中正确加载、无解析错误

**三级子任务与四级关键动作：**

- P6.1.1.1 输入梳理与目标量化
  - 整理「URDF/SDF 文件生成」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P6.1.1.2 方案/方法设计
  - 针对「URDF/SDF 文件生成」制定实施方法或候选方案，使用「ROS URDF、Xacro、SolidWorks/NX → URDF 插件、惯性参数校核」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P6.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「URDF/SDF 文件生成」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P6.1.1.4 验证与问题闭环
  - 对「URDF/SDF 文件生成」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P6.1.1.5 文档输出与下游交付
  - 输出「URDF/SDF 文件生成」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: URDF Modeling and Kinematics Verification (Kinematics & URDF)

## Content
**Method/Tool**: ROS URDF, Xacro, SolidWorks/NX → URDF Plugin, Inertia Parameter Verification

**Design Logic**: Links, joints, inertia, collision bodies, and visual models must be fully consistent with CAD; mass properties are derived from P3.1.2/P3.1.3

**Key Constraints**: Coordinate system consistency, unit uniformity, collision bodies must not be too dense

**Completion Criteria/Deliverables**: Correctly loadable in RViz/Gazebo/Isaac Sim without parsing errors

**Three-Level Subtasks and Four-Level Key Actions**:

- P6.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "URDF/SDF File Generation", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, time nodes, and risk register

- P6.1.1.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "URDF/SDF File Generation", evaluate using "ROS URDF, Xacro, SolidWorks/NX → URDF Plugin, Inertia Parameter Verification", and clarify technical roadmap and resource requirements.
    - Formulate no fewer than 2 candidate solutions
    - Establish an evaluation matrix and quantify scoring
    - Organize review and freeze the solution

- P6.1.1.3 Implementation/Prototype/Sample Production
  - Execute the implementation of "URDF/SDF File Generation" according to the design solution, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P6.1.1.4 Verification and Issue Closure
  - Verify the output of "URDF/SDF File Generation", check whether it meets completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P6.1.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "URDF/SDF File Generation", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documentation according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: URDF 모델링 및 운동학 검증 (Kinematics & URDF)

## 핵심 내용
**방법 / 도구**: ROS URDF, Xacro, SolidWorks/NX → URDF 플러그인, 관성 매개변수 검증

**설계 사고 논리**: 링크, 조인트, 관성, 충돌체, 시각 모델은 CAD와 완전히 일치해야 함; 질량 속성은 P3.1.2/P3.1.3에서 가져옴

**핵심 제약 조건**: 좌표계 일관성, 단위 통일, 충돌체가 너무 조밀하지 않아야 함

**완료 기준 / 산출물**: RViz/Gazebo/Isaac Sim에서 정상적으로 로드 가능, 구문 오류 없음

**3단계 하위 작업 및 4단계 핵심 동작:**

- P6.1.1.1 입력 정리 및 목표 정량화
  - 「URDF/SDF 파일 생성」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P6.1.1.2 방안/방법 설계
  - 「URDF/SDF 파일 생성」에 대한 구현 방법 또는 후보 방안을 수립하고, 「ROS URDF, Xacro, SolidWorks/NX → URDF 플러그인, 관성 매개변수 검증」을 통해 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수화
    - 검토 조직 및 방안 확정

- P6.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「URDF/SDF 파일 생성」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P6.1.1.4 검증 및 문제 종결
  - 「URDF/SDF 파일 생성」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결될 때까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P6.1.1.5 문서 출력 및 하위 전달
  - 「URDF/SDF 파일 생성」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
