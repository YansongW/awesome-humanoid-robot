---
$id: ent_process_p13_3_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: EMC/EMI design and test
  zh: EMC/EMI 设计与测试
  ko: EMC/EMI 设计与测试
summary:
  en: EMC design specification, pre-test report, corrective action record
  zh: '- P13.3.2.1 输入梳理与目标量化 - 整理「EMC/EMI 设计与测试」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: EMC 设计规范、预测试报告、整改记录
domains:
- 02_components
- 08_software_middleware
layers:
- intelligence
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
**所属阶段/工作包**：电子电气与能源系统（Electronics & Power）

## 核心内容
**方法 / 工具**：屏蔽、滤波、接地、PCB 布局、辐射/传导测试

**设计思考逻辑**：大功率电机驱动与高速计算共存，EMC 风险高

**关键约束**：CE/FCC/UL 标准、重量、成本

**完成标准 / 输出物**：EMC 设计规范、预测试报告、整改记录

**三级子任务与四级关键动作：**

- P13.3.2.1 输入梳理与目标量化
  - 整理「EMC/EMI 设计与测试」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P13.3.2.2 概念与详细设计
  - 完成「EMC/EMI 设计与测试」的概念设计、详细设计与接口定义，使用「屏蔽、滤波、接地、PCB 布局、辐射/传导测试」验证可行性，输出图纸/算法/逻辑框架。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P13.3.2.3 实施/原型/样件制作
  - 根据设计方案执行「EMC/EMI 设计与测试」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P13.3.2.4 测试执行与结果分析
  - 按照验收标准执行「EMC/EMI 设计与测试」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P13.3.2.5 文档输出与下游交付
  - 输出「EMC/EMI 设计与测试」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Electronics & Power

## Content
**Methods/Tools**: Shielding, filtering, grounding, PCB layout, radiated/conducted testing

**Design Logic**: High-power motor drives coexist with high-speed computing, posing high EMC risk

**Key Constraints**: CE/FCC/UL standards, weight, cost

**Completion Criteria/Deliverables**: EMC design specification, pre-compliance test report, rectification records

**Level-3 Subtasks and Level-4 Key Actions:**

- P13.3.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "EMC/EMI Design and Testing," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P13.3.2.2 Concept and Detailed Design
  - Complete the concept design, detailed design, and interface definition for "EMC/EMI Design and Testing," verify feasibility using "shielding, filtering, grounding, PCB layout, radiated/conducted testing," and output drawings/algorithms/logic frameworks.
    - Develop at least two candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize a review and freeze the solution

- P13.3.2.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "EMC/EMI Design and Testing" according to the design plan, fabricate prototypes or samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulations or prototype verification
    - Record anomalies and deviations

- P13.3.2.4 Test Execution and Result Analysis
  - Execute "EMC/EMI Design and Testing" tests according to acceptance criteria, calculate pass rates/errors/deviations, conduct root cause analysis, and form an improvement list.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P13.3.2.5 Documentation and Downstream Delivery
  - Output the final report/drawings/specifications for "EMC/EMI Design and Testing," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents per templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 전자 전기 및 에너지 시스템 (Electronics & Power)

## 핵심 내용
**방법/도구**: 차폐, 필터링, 접지, PCB 레이아웃, 방사/전도 테스트

**설계 사고 논리**: 고출력 모터 구동과 고속 컴퓨팅이 공존하여 EMC 위험이 높음

**핵심 제약 조건**: CE/FCC/UL 표준, 중량, 비용

**완료 기준/산출물**: EMC 설계 규격, 사전 테스트 보고서, 개선 기록

**3단계 하위 작업 및 4단계 핵심 조치:**

- P13.3.2.1 입력 정리 및 목표 정량화
  - 「EMC/EMI 설계 및 테스트」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 검수 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부를 수립

- P13.3.2.2 개념 및 상세 설계
  - 「EMC/EMI 설계 및 테스트」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「차폐, 필터링, 접지, PCB 레이아웃, 방사/전도 테스트」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
    - 최소 2개의 후보 방안을 도출
    - 평가 매트릭스를 수립하고 정량적으로 점수화
    - 검토를 조직하고 방안을 확정

- P13.3.2.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「EMC/EMI 설계 및 테스트」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품을 구축하고 핵심 매개변수를 기록
    - 시뮬레이션 또는 프로토타입 검증을 실행
    - 이상 및 편차를 기록

- P13.3.2.4 테스트 실행 및 결과 분석
  - 검수 기준에 따라 「EMC/EMI 설계 및 테스트」 테스트를 실행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성합니다.
    - 테스트/검토 계획 및 통과 기준을 수립
    - 테스트를 실행하고 원시 데이터를 기록
    - 문제 목록 및 개선 조치를 출력

- P13.3.2.5 문서 출력 및 하위 전달
  - 「EMC/EMI 설계 및 테스트」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터를 참조
    - 내부 검토 및 버전 관리를 완료
    - 게시하고 하위 의존 부서에 통지
