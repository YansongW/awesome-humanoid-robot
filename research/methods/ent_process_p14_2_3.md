---
$id: ent_process_p14_2_3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: CI/CD and simulation test chain
  zh: CI/CD 与仿真测试链
  ko: CI/CD 与仿真测试链
summary:
  en: CI pipeline, automatic test pass rate, coverage indicators
  zh: '- P14.2.3.1 输入梳理与目标量化 - 整理「CI/CD 与仿真测试链」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: CI 流水线、自动测试通过率、覆盖率指标
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
**方法 / 工具**：GitLab CI、Docker、SIL/HIL 自动化测试、代码覆盖率

**设计思考逻辑**：持续集成保证软件质量，减少回归问题

**关键约束**：算力、测试环境维护

**完成标准 / 输出物**：CI 流水线、自动测试通过率、覆盖率指标

**三级子任务与四级关键动作：**

- P14.2.3.1 输入梳理与目标量化
  - 整理「CI/CD 与仿真测试链」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P14.2.3.2 方案/方法设计
  - 针对「CI/CD 与仿真测试链」制定实施方法或候选方案，使用「GitLab CI、Docker、SIL/HIL 自动化测试、代码覆盖率」进行论证，明确技术路线与资源需求。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P14.2.3.3 实施/原型/样件制作
  - 根据设计方案执行「CI/CD 与仿真测试链」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P14.2.3.4 测试执行与结果分析
  - 按照验收标准执行「CI/CD 与仿真测试链」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P14.2.3.5 文档输出与下游交付
  - 输出「CI/CD 与仿真测试链」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Software Middleware and System Integration (Software & Integration)

## Content
**Method/Tool**: GitLab CI, Docker, SIL/HIL Automated Testing, Code Coverage

**Design Thinking Logic**: Continuous integration ensures software quality and reduces regression issues

**Key Constraints**: Computing power, test environment maintenance

**Completion Criteria/Deliverables**: CI pipeline, automated test pass rate, coverage metrics

**Three-Level Subtasks and Four-Level Key Actions:**

- P14.2.3.1 Input Review and Target Quantification
  - Organize the upstream inputs, reference standards, and resources required for the "CI/CD and Simulation Test Chain," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream input items and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owners, timelines, and risk register

- P14.2.3.2 Solution/Method Design
  - Develop implementation methods or candidate solutions for the "CI/CD and Simulation Test Chain," using "GitLab CI, Docker, SIL/HIL Automated Testing, Code Coverage" for justification, and clarify the technical roadmap and resource requirements.
    - Generate at least 2 candidate solutions
    - Establish an evaluation matrix and quantify scores
    - Organize a review and freeze the solution

- P14.2.3.3 Implementation/Prototype/Sample Production
  - Execute the implementation of the "CI/CD and Simulation Test Chain" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Execute simulations or prototype verification
    - Record anomalies and deviations

- P14.2.3.4 Test Execution and Result Analysis
  - Execute tests for the "CI/CD and Simulation Test Chain" according to acceptance criteria, calculate pass rate/error/deviation, conduct root cause analysis, and form an improvement list.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P14.2.3.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for the "CI/CD and Simulation Test Chain," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents according to templates and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 소프트웨어 미들웨어 및 시스템 통합 (Software & Integration)

## 핵심 내용
**방법 / 도구**: GitLab CI, Docker, SIL/HIL 자동화 테스트, 코드 커버리지

**설계 사고 논리**: 지속적 통합은 소프트웨어 품질을 보장하고 회귀 문제를 줄입니다.

**핵심 제약 조건**: 연산 능력, 테스트 환경 유지보수

**완료 기준 / 산출물**: CI 파이프라인, 자동 테스트 통과율, 커버리지 지표

**3단계 하위 작업 및 4단계 핵심 조치:**

- P14.2.3.1 입력 정리 및 목표 정량화
  - 「CI/CD 및 시뮬레이션 테스트 체인」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화된 수용 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 작성하고 버전을 확인
    - 수용 기준을 정량화된 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P14.2.3.2 방안/방법 설계
  - 「CI/CD 및 시뮬레이션 테스트 체인」에 대한 구현 방법 또는 후보 방안을 수립하고, 「GitLab CI, Docker, SIL/HIL 자동화 테스트, 코드 커버리지」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스를 구축하고 정량적 점수 부여
    - 검토를 조직하고 방안 확정

- P14.2.3.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「CI/CD 및 시뮬레이션 테스트 체인」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품을 구축하고 핵심 매개변수 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P14.2.3.4 테스트 실행 및 결과 분석
  - 수용 기준에 따라 「CI/CD 및 시뮬레이션 테스트 체인」 테스트를 실행하고, 통과율/오차/편차를 통계하며, 근본 원인 분석을 수행하고 개선 목록을 작성합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트를 실행하고 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P14.2.3.5 문서 출력 및 하위 전달
  - 「CI/CD 및 시뮬레이션 테스트 체인」 최종 보고서/도면/규격을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
