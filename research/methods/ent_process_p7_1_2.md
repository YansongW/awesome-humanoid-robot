---
$id: ent_process_p7_1_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Sensor and actuator model configuration
  zh: 传感器与执行器模型配置
  ko: 传感器与执行器模型配置
summary:
  en: Sensor configuration files, noise/delay parameter tables, comparison with real hardware
  zh: '- P7.1.2.1 输入梳理与目标量化 - 整理「传感器与执行器模型配置」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 传感器配置文件、噪声/延迟参数表、与真实硬件对比
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
**方法 / 工具**：IMU/编码器/力觉/相机/LiDAR 噪声模型、延迟模型

**设计思考逻辑**：传感器噪声、延迟、采样率需贴近真实硬件，才能有效验证算法

**关键约束**：算力消耗、模型复杂度

**完成标准 / 输出物**：传感器配置文件、噪声/延迟参数表、与真实硬件对比

**三级子任务与四级关键动作：**

- P7.1.2.1 输入梳理与目标量化
  - 整理「传感器与执行器模型配置」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P7.1.2.2 方案/方法设计
  - 针对「传感器与执行器模型配置」制定实施方法或候选方案，使用「IMU/编码器/力觉/相机/LiDAR 噪声模型、延迟模型」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P7.1.2.3 实施/原型/样件制作
  - 根据设计方案执行「传感器与执行器模型配置」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P7.1.2.4 验证与问题闭环
  - 对「传感器与执行器模型配置」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P7.1.2.5 文档输出与下游交付
  - 输出「传感器与执行器模型配置」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Simulation Platform Construction and Validation (Simulation)

## Content
**Method/Tool**: IMU/Encoder/Force/Camera/LiDAR noise models, delay models

**Design Logic**: Sensor noise, delay, and sampling rate must closely match real hardware to effectively validate algorithms

**Key Constraints**: Computational cost, model complexity

**Completion Criteria/Deliverables**: Sensor configuration files, noise/delay parameter tables, comparison with real hardware

**Level-3 Subtasks and Level-4 Key Actions**:

- P7.1.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Sensor and Actuator Model Configuration," convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task Owner, timeline, and risk register

- P7.1.2.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Sensor and Actuator Model Configuration," using "IMU/Encoder/Force/Camera/LiDAR noise models, delay models" for demonstration, and clarify the technical roadmap and resource requirements.
    - Formulate at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and freeze the solution

- P7.1.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Sensor and Actuator Model Configuration" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype validation
    - Document anomalies and deviations

- P7.1.2.4 Validation and Issue Closure
  - Validate the output of "Sensor and Actuator Model Configuration," check whether it meets completion criteria, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P7.1.2.5 Documentation and Downstream Delivery
  - Produce the final report/drawing/specification for "Sensor and Actuator Model Configuration," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**：시뮬레이션 플랫폼 구축 및 검증 (Simulation)

## 핵심 내용
**방법 / 도구**：IMU/엔코더/힘 감지/카메라/LiDAR 노이즈 모델, 지연 모델

**설계 사고 논리**：센서 노이즈, 지연, 샘플링 속도는 실제 하드웨어에 근접해야 알고리즘을 효과적으로 검증할 수 있음

**핵심 제약 조건**：연산 소모량, 모델 복잡도

**완료 기준 / 산출물**：센서 설정 파일, 노이즈/지연 파라미터 테이블, 실제 하드웨어와의 비교

**3단계 하위 작업과 4단계 핵심 동작：**

- P7.1.2.1 입력 정리 및 목표 정량화
  - 「센서 및 액추에이터 모델 설정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 수용 지표로 변환하며, Owner와 마일스톤을 명확히 함.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 수용 기준을 정량화 가능한 KPI로 변환
    - 작업 Owner, 시간 노드 및 위험 등록부 구축

- P7.1.2.2 방안/방법 설계
  - 「센서 및 액추에이터 모델 설정」에 대한 구현 방법 또는 후보 방안을 수립하고, 「IMU/엔코더/힘 감지/카메라/LiDAR 노이즈 모델, 지연 모델」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 함.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P7.1.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「센서 및 액추에이터 모델 설정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록함.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P7.1.2.4 검증 및 문제 종결
  - 「센서 및 액추에이터 모델 설정」 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종결까지 추적함.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P7.1.2.5 문서 출력 및 하위 전달
  - 「센서 및 액추에이터 모델 설정」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료함.
    - 템플릿에 따라 문서 작성 및 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존자에게 통지
