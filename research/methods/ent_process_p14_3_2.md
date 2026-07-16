---
$id: ent_process_p14_3_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Hardware/software in the loop testing (HIL/SIL)
  zh: 软硬件在环测试（HIL/SIL）
  ko: 软硬件在环测试（HIL/SIL）
summary:
  en: HIL/SIL test reports, 100% coverage of key use cases
  zh: '- P14.3.2.1 输入梳理与目标量化 - 整理「软硬件在环测试（HIL/SIL）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: HIL/SIL 测试报告、关键用例 100% 覆盖
domains:
- 08_software_middleware
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
**所属阶段/工作包**：软件中间件与系统集成（Software & Integration）

## 核心内容
**方法 / 工具**：仿真模型 + 真实控制器、自动化测试用例

**设计思考逻辑**：在实物前验证控制器与软件逻辑

**关键约束**：模型保真度、测试覆盖率

**完成标准 / 输出物**：HIL/SIL 测试报告、关键用例 100% 覆盖

**三级子任务与四级关键动作：**

- P14.3.2.1 输入梳理与目标量化
  - 整理「软硬件在环测试（HIL/SIL）」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P14.3.2.2 方案/方法设计
  - 针对「软硬件在环测试（HIL/SIL）」制定实施方法或候选方案，使用「仿真模型 + 真实控制器、自动化测试用例」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P14.3.2.3 建模/仿真与样机实现
  - 建立「软硬件在环测试（HIL/SIL）」的仿真/数学模型或原型样机，使用「仿真模型 + 真实控制器、自动化测试用例」执行计算或实验，记录关键参数与边界条件。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P14.3.2.4 测试执行与结果分析
  - 按照验收标准执行「软硬件在环测试（HIL/SIL）」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P14.3.2.5 文档输出与下游交付
  - 输出「软硬件在环测试（HIL/SIL）」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Software Middleware and System Integration (Software & Integration)

## Content
**Method/Tool**: Simulation model + real controller, automated test cases

**Design Thinking Logic**: Verify controller and software logic before physical hardware

**Key Constraints**: Model fidelity, test coverage

**Completion Criteria/Deliverables**: HIL/SIL test report, 100% coverage of key use cases

**Level-3 Subtasks and Level-4 Key Actions:**

- P14.3.2.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Hardware-in-the-Loop/Software-in-the-Loop (HIL/SIL)" testing, convert completion criteria into quantifiable acceptance indicators, and define the Owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P14.3.2.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for "Hardware-in-the-Loop/Software-in-the-Loop (HIL/SIL)" testing, use "simulation model + real controller, automated test cases" for demonstration, and clarify the technical roadmap and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and perform quantitative scoring
    - Organize review and freeze the solution

- P14.3.2.3 Modeling/Simulation and Prototype Implementation
  - Build simulation/mathematical models or prototypes for "Hardware-in-the-Loop/Software-in-the-Loop (HIL/SIL)" testing, use "simulation model + real controller, automated test cases" to perform calculations or experiments, and record key parameters and boundary conditions.
    - Establish models/prototypes and record key parameters
    - Execute simulations or prototype verification
    - Record anomalies and deviations

- P14.3.2.4 Test Execution and Result Analysis
  - Execute "Hardware-in-the-Loop/Software-in-the-Loop (HIL/SIL)" tests according to acceptance criteria, calculate pass rate/error/deviation, perform root cause analysis, and generate an improvement list.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P14.3.2.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "Hardware-in-the-Loop/Software-in-the-Loop (HIL/SIL)" testing, update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream processes.
    - Write documents according to template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 소프트웨어 미들웨어 및 시스템 통합 (Software & Integration)

## 핵심 내용
**방법 / 도구**: 시뮬레이션 모델 + 실제 컨트롤러, 자동화된 테스트 케이스

**설계 사고 논리**: 실물 전에 컨트롤러와 소프트웨어 로직 검증

**핵심 제약 조건**: 모델 충실도, 테스트 커버리지

**완료 기준 / 산출물**: HIL/SIL 테스트 보고서, 핵심 사용 사례 100% 커버리지

**3단계 하위 작업 및 4단계 핵심 조치:**

- P14.3.2.1 입력 정리 및 목표 정량화
  - 「하드웨어/소프트웨어 인더루프 테스트(HIL/SIL)」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 수용 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 수용 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P14.3.2.2 방안/방법 설계
  - 「하드웨어/소프트웨어 인더루프 테스트(HIL/SIL)」에 대한 구현 방법 또는 후보 방안을 수립하고, 「시뮬레이션 모델 + 실제 컨트롤러, 자동화된 테스트 케이스」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 부여
    - 검토 조직 및 방안 확정

- P14.3.2.3 모델링/시뮬레이션 및 프로토타입 구현
  - 「하드웨어/소프트웨어 인더루프 테스트(HIL/SIL)」의 시뮬레이션/수학적 모델 또는 프로토타입을 구축하고, 「시뮬레이션 모델 + 실제 컨트롤러, 자동화된 테스트 케이스」를 사용하여 계산 또는 실험을 수행하며, 주요 매개변수와 경계 조건을 기록합니다.
    - 모델/프로토타입 구축 및 주요 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P14.3.2.4 테스트 실행 및 결과 분석
  - 수용 기준에 따라 「하드웨어/소프트웨어 인더루프 테스트(HIL/SIL)」 테스트를 실행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P14.3.2.5 문서 출력 및 하위 전달
  - 「하드웨어/소프트웨어 인더루프 테스트(HIL/SIL)」 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구 사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 참조
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
