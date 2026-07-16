---
$id: ent_process_p4_2_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Motor type selection
  zh: 电机选型
  ko: 电机选型
summary:
  en: Motor specification, type selection comparison table, heat check
  zh: '- P4.2.1.1 输入梳理与目标量化 - 整理「电机选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。 - 列出所有上游输入清单并确认版本 - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记'
  ko: 电机规格书、选型对比表、热校核
domains:
- 02_components
- 06_design_engineering
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
**所属阶段/工作包**：关节模组与驱动系统设计（Actuator & Drive）

## 核心内容
**方法 / 工具**：转矩密度、热阻、编码器分辨率、峰值电流、效率图对比

**设计思考逻辑**：优先高转矩密度无框/集成电机；校核绕组温升与退磁

**关键约束**：驱动器母线电压、电流能力、供货周期

**完成标准 / 输出物**：电机规格书、选型对比表、热校核

**三级子任务与四级关键动作：**

- P4.2.1.1 输入梳理与目标量化
  - 整理「电机选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
    - 列出所有上游输入清单并确认版本
    - 将验收标准转化为可量化 KPI
    - 建立任务 Owner、时间节点与风险登记

- P4.2.1.2 候选方案建立与评估
  - 针对「电机选型」建立候选方案库，使用「转矩密度、热阻、编码器分辨率、峰值电流、效率图对比」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
    - 形成不少于 2 个候选方案
    - 建立评估矩阵并量化打分
    - 组织评审并冻结方案

- P4.2.1.3 实施/原型/样件制作
  - 根据设计方案执行「电机选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
    - 建立模型/样机并记录关键参数
    - 执行仿真或原型验证
    - 记录异常与偏差

- P4.2.1.4 验证与问题闭环
  - 对「电机选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
    - 制定测试/评审计划与通过准则
    - 执行测试并记录原始数据
    - 输出问题清单与改进措施

- P4.2.1.5 文档输出与下游交付
  - 输出「电机选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
    - 按模板编写文档并引用原始数据
    - 完成内部评审与版本控制
    - 发布并通知下游依赖方

## 参考
- 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）

## Overview
**Phase/Work Package**: Joint Module and Drive System Design (Actuator & Drive)

## Content
**Method/Tool**: Torque density, thermal resistance, encoder resolution, peak current, efficiency map comparison

**Design Logic**: Prioritize high torque density frameless/integrated motors; verify winding temperature rise and demagnetization

**Key Constraints**: Drive bus voltage, current capability, supply lead time

**Completion Criteria/Deliverables**: Motor specification sheet, selection comparison table, thermal verification

**Level-3 Subtasks and Level-4 Key Actions:**

- P4.2.1.1 Input Review and Target Quantification
  - Organize upstream inputs, reference standards, and resources required for "motor selection"; convert completion criteria into quantifiable acceptance indicators; define owner and milestones.
    - List all upstream inputs and confirm versions
    - Convert acceptance criteria into quantifiable KPIs
    - Establish task owner, timeline, and risk register

- P4.2.1.2 Candidate Solution Development and Evaluation
  - Develop a candidate solution library for "motor selection"; perform quantitative evaluation using "torque density, thermal resistance, encoder resolution, peak current, efficiency map comparison"; finalize solution considering cost, performance, supply chain, and maintainability.
    - Form at least 2 candidate solutions
    - Establish evaluation matrix and assign quantitative scores
    - Organize review and freeze the solution

- P4.2.1.3 Implementation/Prototype/Sample Fabrication
  - Execute the implementation of "motor selection" according to the design solution; fabricate prototypes, samples, or complete key steps; record process data.
    - Build models/prototypes and record key parameters
    - Perform simulation or prototype verification
    - Record anomalies and deviations

- P4.2.1.4 Verification and Issue Closure
  - Verify the output of "motor selection"; check if completion criteria are met; record issues and track until closure.
    - Develop test/review plan and pass criteria
    - Execute tests and record raw data
    - Output issue list and improvement measures

- P4.2.1.5 Documentation and Downstream Delivery
  - Output final report/drawing/specification for "motor selection"; update ICD/BOM/SOP/requirements traceability chain; complete formal delivery to downstream stages.
    - Write documents per template and reference raw data
    - Complete internal review and version control
    - Release and notify downstream dependents

## 개요
**소속 단계/작업 패키지**: 관절 모듈 및 구동 시스템 설계 (Actuator & Drive)

## 핵심 내용
**방법 / 도구**: 토크 밀도, 열 저항, 엔코더 분해능, 피크 전류, 효율 그래프 비교

**설계 사고 논리**: 높은 토크 밀도의 프레임리스/일체형 모터 우선; 권선 온도 상승 및 감자 확인

**핵심 제약 조건**: 드라이버 모선 전압, 전류 용량, 공급 기간

**완료 기준 / 산출물**: 모터 사양서, 선정 비교표, 열 확인

**3단계 하위 작업 및 4단계 핵심 조치:**

- P4.2.1.1 입력 정리 및 목표 정량화
  - 「모터 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, 담당자와 마일스톤을 명확히 합니다.
    - 모든 상위 입력 목록을 나열하고 버전 확인
    - 검수 기준을 정량화 가능한 KPI로 변환
    - 작업 담당자, 시간 노드 및 위험 등록 수립

- P4.2.1.2 후보 방안 수립 및 평가
  - 「모터 선정」을 위한 후보 방안 라이브러리를 구축하고, 「토크 밀도, 열 저항, 엔코더 분해능, 피크 전류, 효율 그래프 비교」를 사용하여 정량 평가하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 방안을 결정합니다.
    - 2개 이상의 후보 방안 구성
    - 평가 매트릭스 구축 및 정량 점수화
    - 검토 조직 및 방안 확정

- P4.2.1.3 구현/프로토타입/시제품 제작
  - 설계 방안에 따라 「모터 선정」의 구현 작업을 수행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
    - 모델/시제품 구축 및 핵심 파라미터 기록
    - 시뮬레이션 또는 프로토타입 검증 실행
    - 이상 및 편차 기록

- P4.2.1.4 검증 및 문제 종결
  - 「모터 선정」 출력물을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하며 종결될 때까지 추적합니다.
    - 테스트/검토 계획 및 통과 기준 수립
    - 테스트 실행 및 원시 데이터 기록
    - 문제 목록 및 개선 조치 출력

- P4.2.1.5 문서 출력 및 하위 전달
  - 「모터 선정」 최종 보고서/도면/사양서를 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
    - 템플릿에 따라 문서 작성 및 원시 데이터 참조
    - 내부 검토 및 버전 관리 완료
    - 게시 및 하위 의존 부서에 통보
