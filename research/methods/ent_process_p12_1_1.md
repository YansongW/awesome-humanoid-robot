---
$id: ent_process_p12_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Sensor Selection and Calibration
  zh: 传感器选型与标定
  ko: 传感器选型与标定
summary:
  en: Perception module architecture, calibration results, and accuracy metrics
  zh: '- P12.1.1.1 输入梳理与目标量化 - 整理「传感器选型与标定」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 感知模块架构、标定结果、精度指标
domains:
- 07_ai_models_algorithms
layers:
- intelligence
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
**所属阶段/工作包**：VLA / WAM / AI 算法集成（AI & Perception）

## 核心内容
**方法 / 工具**：RGB-D 相机、LiDAR、IMU、麦克风阵列、触觉阵列

**设计思考逻辑**：提供语义理解、深度估计、SLAM、人体/物体检测

**关键约束**：算力、延迟、光照鲁棒性、成本

**完成标准 / 输出物**：感知模块架构、标定结果、精度指标

**三级子任务与四级关键动作：**

- P12.1.1.1 输入梳理与目标量化
  - 整理「传感器选型与标定」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P12.1.1.2 候选方案建立与评估
  - 针对「传感器选型与标定」建立候选方案库，使用「RGB-D 相机、LiDAR、IMU、麦克风阵列、触觉阵列」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P12.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「传感器选型与标定」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P12.1.1.4 验证与问题闭环
  - 对「传感器选型与标定」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P12.1.1.5 文档输出与下游交付
  - 输出「传感器选型与标定」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: VLA / WAM / AI Algorithm Integration (AI & Perception)

## Content
**Methods/Tools**: RGB-D camera, LiDAR, IMU, microphone array, tactile array

**Design Logic**: Provide semantic understanding, depth estimation, SLAM, human/object detection

**Key Constraints**: Computing power, latency, lighting robustness, cost

**Completion Criteria/Deliverables**: Perception module architecture, calibration results, accuracy metrics

**Level-3 Subtasks and Level-4 Key Actions:**

- P12.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Sensor Selection and Calibration," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P12.1.1.2 Candidate Solution Development and Evaluation
  - Develop a candidate solution library for "Sensor Selection and Calibration," conduct quantitative evaluation using "RGB-D camera, LiDAR, IMU, microphone array, tactile array," and finalize the solution after considering cost, performance, supply chain, and maintainability.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P12.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Sensor Selection and Calibration" according to the design plan, fabricate prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype validation
    - Record anomalies and deviations

- P12.1.1.4 Verification and Issue Closure
  - Verify the output of "Sensor Selection and Calibration," check whether it meets the completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P12.1.1.5 Documentation and Downstream Delivery
  - Output the final report/drawing/specification for "Sensor Selection and Calibration," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: VLA / WAM / AI 알고리즘 통합 (AI & Perception)

## 핵심 내용
**방법 / 도구**: RGB-D 카메라, LiDAR, IMU, 마이크 어레이, 촉각 어레이

**설계 사고 논리**: 의미 이해, 깊이 추정, SLAM, 인체/물체 감지 제공

**핵심 제약 조건**: 연산 능력, 지연 시간, 조명 강건성, 비용

**완료 기준 / 산출물**: 인식 모듈 아키텍처, 캘리브레이션 결과, 정밀도 지표

**3단계 하위 작업 및 4단계 핵심 동작:**

- P12.1.1.1 입력 정리 및 목표 정량화
  - 「센서 선정 및 캘리브레이션」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P12.1.1.2 후보方案 수립 및 평가
  - 「센서 선정 및 캘리브레이션」을 위한 후보方案 라이브러리를 구축하고, 「RGB-D 카메라, LiDAR, IMU, 마이크 어레이, 촉각 어레이」를 사용하여 정량 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종方案을 결정합니다.
    - 2개 이상의 후보方案 구성
    - 평가 매트릭스 구축 및 정량 점수화
    - 검토 조직 및方案 확정

- P12.1.1.3 구현/프로토타입/시제품 제작
  - 설계方案에 따라 「센서 선정 및 캘리브레이션」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P12.1.1.4 검증 및 문제 종결
  - 「센서 선정 및 캘리브레이션」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P12.1.1.5 문서 출력 및 하위 전달
  - 「센서 선정 및 캘리브레이션」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 참조
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존자에게 통지
