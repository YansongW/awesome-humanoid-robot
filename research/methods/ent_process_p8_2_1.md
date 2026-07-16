---
$id: ent_process_p8_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Static and dynamic stress and deformation analysis
  zh: 静动态应力与变形分析
  ko: 静动态应力与变形分析
summary:
  en: 'FEA stress report: stress, deformation, safety factor'
  zh: '- P8.2.1.1 输入梳理与目标量化 - 整理「静动态应力与变形分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 《FEA 应力报告》：应力、变形、安全系数
domains:
- 06_design_engineering
- 03_manufacturing_processes
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
**所属阶段/工作包**：结构强度仿真与迭代（Structural FEA）

## 核心内容
**方法 / 工具**：线弹性/弹塑性分析、von Mises、变形云图

**设计思考逻辑**：校核关键件应力是否低于材料屈服/疲劳极限，变形是否影响运动

**关键约束**：局部应力集中、焊缝/螺接模拟

**完成标准 / 输出物**：《FEA 应力报告》：应力、变形、安全系数

**三级子任务与四级关键动作：**

- P8.2.1.1 输入梳理与目标量化
  - 整理「静动态应力与变形分析」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P8.2.1.2 方案/方法设计
  - 针对「静动态应力与变形分析」制定实施方法或候选方案，使用「线弹性/弹塑性分析、von Mises、变形云图」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P8.2.1.3 实施/原型/样件制作
  - 根据设计方案执行「静动态应力与变形分析」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P8.2.1.4 验证与问题闭环
  - 对「静动态应力与变形分析」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P8.2.1.5 文档输出与下游交付
  - 输出「静动态应力与变形分析」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Structural FEA

## Content
**Method/Tool**: Linear elastic/elastoplastic analysis, von Mises, deformation contour

**Design Thinking Logic**: Verify whether key component stresses are below material yield/fatigue limits, and whether deformation affects motion

**Key Constraints**: Local stress concentration, weld/bolt simulation

**Completion Criteria/Deliverable**: "FEA Stress Report": stress, deformation, safety factor

**Level-3 Subtasks and Level-4 Key Actions**:

- P8.2.1.1 Input Review and Target Quantification
  - Compile upstream inputs, reference standards, and resources required for "static and dynamic stress and deformation analysis", convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P8.2.1.2 Approach/Method Design
  - Develop implementation methods or candidate approaches for "static and dynamic stress and deformation analysis", using "linear elastic/elastoplastic analysis, von Mises, deformation contour" for demonstration, and clarify technical route and resource requirements.
    - Formulate no fewer than 2 candidate approaches
    - Establish evaluation matrix and quantify scoring
    - Organize review and freeze the approach

- P8.2.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "static and dynamic stress and deformation analysis" according to the design approach, produce prototypes, samples, or complete key steps, and record process data.
    - Build model/prototype and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P8.2.1.4 Verification and Issue Closure
  - Verify the output of "static and dynamic stress and deformation analysis", check whether it meets completion criteria, record issues, and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P8.2.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "static and dynamic stress and deformation analysis", update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documentation per template and cite raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 구조 강도 시뮬레이션 및 반복 (Structural FEA)

## 핵심 내용
**방법 / 도구**: 선형 탄성/탄소성 해석, von Mises, 변형 분포도

**설계 사고 논리**: 주요 부품의 응력이 재료 항복/피로 한계 이하인지 확인, 변형이 운동에 영향을 미치는지 검토

**주요 제약 조건**: 국부 응력 집중, 용접/볼트 체결 시뮬레이션

**완료 기준 / 산출물**: 《FEA 응력 보고서》: 응력, 변형, 안전 계수

**3단계 하위 작업과 4단계 주요 조치:**

- P8.2.1.1 입력 정리 및 목표 정량화
  - 「정적/동적 응력 및 변형 해석」에 필요한 상위 입력, 참조 표준 및 자원을 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 한다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P8.2.1.2 방안/방법 설계
  - 「정적/동적 응력 및 변형 해석」에 대한 구현 방법 또는 후보 방안을 수립하고, 「선형 탄성/탄소성 해석, von Mises, 변형 분포도」를 사용하여 논증하며, 기술 경로와 자원 요구 사항을 명확히 한다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P8.2.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「정적/동적 응력 및 변형 해석」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 주요 단계를 완료하며, 과정 데이터를 기록한다.
    - 모델/시제품 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P8.2.1.4 검증 및 문제 종결
  - 「정적/동적 응력 및 변형 해석」의 출력을 검증하고, 완료 기준 충족 여부를 확인하며, 문제를 기록하고 종결될 때까지 추적한다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P8.2.1.5 문서 출력 및 하위 전달
  - 「정적/동적 응력 및 변형 해석」의 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료한다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
