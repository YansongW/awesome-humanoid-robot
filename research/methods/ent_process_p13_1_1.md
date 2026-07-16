---
$id: ent_process_p13_1_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Computing Platform Architecture and Selection
  zh: 计算平台架构与选型
  ko: 计算平台架构与选型
summary:
  en: Computing architecture diagram, compute power/power consumption budget for each node, security zoning
  zh: '- P13.1.1.1 输入梳理与目标量化 - 整理「计算平台架构与选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化
    KPI - 建立任务 Owner、时间节点与风险登记'
  ko: 计算架构图、各节点算力/功耗预算、安全分区
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
**方法 / 工具**：Jetson / Intel NUC / 自研载板 / FPGA / MCU 分布

**设计思考逻辑**：AI 任务用 GPU，实时控制用 MCU/FPGA，安全监控独立

**关键约束**：功耗、散热、重量、实时性、功能安全

**完成标准 / 输出物**：计算架构图、各节点算力/功耗预算、安全分区

**三级子任务与四级关键动作：**

- P13.1.1.1 输入梳理与目标量化
  - 整理「计算平台架构与选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P13.1.1.2 候选方案建立与评估
  - 针对「计算平台架构与选型」建立候选方案库，使用「Jetson / Intel NUC / 自研载板 / FPGA / MCU 分布」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P13.1.1.3 实施/原型/样件制作
  - 根据设计方案执行「计算平台架构与选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P13.1.1.4 验证与问题闭环
  - 对「计算平台架构与选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P13.1.1.5 文档输出与下游交付
  - 输出「计算平台架构与选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Electronics & Power

## Content
**Method/Tool**: Jetson / Intel NUC / Custom Carrier Board / FPGA / MCU Distribution

**Design Logic**: GPU for AI tasks, MCU/FPGA for real-time control, independent safety monitoring

**Key Constraints**: Power consumption, heat dissipation, weight, real-time performance, functional safety

**Completion Criteria/Deliverables**: Computing architecture diagram, computing power/power budget per node, safety partitioning

**Level-3 Subtasks and Level-4 Key Actions:**

- P13.1.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "Computing Platform Architecture and Selection," convert completion criteria into quantifiable acceptance indicators, and define the owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owners, timelines, and risk register

- P13.1.1.2 Candidate Solution Development and Evaluation
  - Develop a candidate solution library for "Computing Platform Architecture and Selection," conduct quantitative evaluation using "Jetson / Intel NUC / Custom Carrier Board / FPGA / MCU Distribution," and finalize the solution considering cost, performance, supply chain, and maintainability.
    - Form at least 2 candidate solutions
    - Establish an evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P13.1.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "Computing Platform Architecture and Selection" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P13.1.1.4 Verification and Issue Closure
  - Verify the output of "Computing Platform Architecture and Selection," check whether completion criteria are met, record issues, and track until closure.
    - Develop test/review plans and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P13.1.1.5 Documentation Output and Downstream Delivery
  - Output the final report/drawing/specification for "Computing Platform Architecture and Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
    - Write documents per template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependencies

## 개요
**소속 단계/작업 패키지**: 전자 전기 및 에너지 시스템 (Electronics & Power)

## 핵심 내용
**방법 / 도구**: Jetson / Intel NUC / 자체 개발 캐리어 보드 / FPGA / MCU 분포

**설계 사고 논리**: AI 작업은 GPU 사용, 실시간 제어는 MCU/FPGA 사용, 안전 모니터링은 독립적으로 수행

**핵심 제약 조건**: 전력 소모, 방열, 무게, 실시간성, 기능 안전

**완료 기준 / 산출물**: 컴퓨팅 아키텍처 다이어그램, 각 노드의 연산 능력/전력 소모 예산, 안전 분할

**3단계 하위 작업 및 4단계 핵심 동작:**

- P13.1.1.1 입력 정리 및 목표 정량화
  - 「컴퓨팅 플랫폼 아키텍처 및 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록부 구축

- P13.1.1.2 후보 방안 수립 및 평가
  - 「컴퓨팅 플랫폼 아키텍처 및 선정」에 대한 후보 방안 라이브러리를 구축하고, 「Jetson / Intel NUC / 자체 개발 캐리어 보드 / FPGA / MCU 분포」를 사용하여 정량적 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 결정합니다.
    - 2개 이상의 후보 방안 도출
    - 평가 매트릭스 구축 및 정량적 점수 산정
    - 검토를 조직하고 방안 확정

- P13.1.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「컴퓨팅 플랫폼 아키텍처 및 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 수행
    - 이상 및 편차 기록

- P13.1.1.4 검증 및 문제 해결
  - 「컴퓨팅 플랫폼 아키텍처 및 선정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 수행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P13.1.1.5 문서 출력 및 하위 전달
  - 「컴퓨팅 플랫폼 아키텍처 및 선정」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서를 작성하고 원시 데이터 인용
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통지
