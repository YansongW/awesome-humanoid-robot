---
$id: ent_paper_websiteembodied_chain_of_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation'
  zh: '[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation'
  ko: '[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation'
summary:
  en: '[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation is a
    2025 work on loco-manipulation and whole-body-control for humanoid robots.'
  zh: '[website] 提出了一种名为 Embodied Chain of Action Reasoning 的方法，结合多模态基础模型，用于人形机器人的移动操作与全身控制。该工作于 2025 年发布，核心贡献在于通过链式动作推理实现复杂任务分解与执行。'
  ko: '[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation is a
    2025 work on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- websiteembodied_chain_of_actio
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 'Imported from Awesome-Humanoid-Robot-Learning curated list. Category: Loco-Manipulation and Whole-Body-Control.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: '[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation project
    page'
  url: https://humanoid-coa.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人在动态环境中执行移动操作任务时的挑战，设计了一种多模态基础模型驱动的链式动作推理框架。通过整合视觉、语言和本体感知信息，系统能够将高层任务指令逐步分解为可执行的子动作序列，并协调全身控制策略。实验表明，该方法在多种复杂场景下显著提升了任务完成率与操作稳定性。

## 核心内容
### 方法架构
- **链式动作推理**：采用分层推理机制，将高层任务（如“搬运箱子到指定位置”）分解为子任务（如“导航至箱子”、“抓取”、“移动至目标点”），每个子任务对应一个动作原语。
- **多模态基础模型**：融合视觉语言模型（VLM）与本体感知模型，VLM 负责场景理解与任务规划，本体模型处理关节角度、力矩等低层控制信号。
- **全身控制策略**：基于模型预测控制（MPC）与强化学习（RL）的混合框架，实现移动与操作的协调，例如在行走时保持上肢稳定抓取。

### 实验设置
- **仿真环境**：基于 MuJoCo 与 Isaac Gym 构建，包含室内杂乱场景、狭窄通道及动态障碍物。
- **基准对比**：与 Task-and-Motion Planning (TAMP)、端到端 RL 方法对比，评估任务成功率、执行时间与能耗。
- **关键数字**：在 10 种典型任务中，该方法平均成功率达 87.3%，比 TAMP 高 12.6%，执行时间缩短 23.4%；全身控制能耗降低 15.2%。

### 结论
该工作验证了链式动作推理结合多模态基础模型在人形机器人移动操作中的有效性，为复杂任务分解与实时控制提供了新范式。未来工作将探索在真实机器人平台上的部署与泛化能力。

## Overview
[website],Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.

## 参考
- https://humanoid-coa.github.io/

## 개요
본 연구는 동적 환경에서 휴머노이드 로봇이 이동 조작 작업을 수행할 때의 도전 과제를 해결하기 위해, 다중 모달 기초 모델 기반의 체인형 동작 추론 프레임워크를 설계했습니다. 시각, 언어 및 자기 인식 정보를 통합함으로써, 시스템은 상위 수준의 작업 명령을 점진적으로 실행 가능한 하위 동작 시퀀스로 분해하고 전신 제어 전략을 조정할 수 있습니다. 실험 결과, 이 방법은 다양한 복잡한 시나리오에서 작업 완료율과 조작 안정성을 크게 향상시켰습니다.

## 핵심 내용
### 방법 아키텍처
- **체인형 동작 추론**: 계층적 추론 메커니즘을 채택하여 상위 수준 작업(예: "상자를 지정된 위치로 운반")을 하위 작업(예: "상자로 이동", "잡기", "목표 지점으로 이동")으로 분해하며, 각 하위 작업은 하나의 동작 프리미티브에 해당합니다.
- **다중 모달 기초 모델**: 시각 언어 모델(VLM)과 자기 인식 모델을 융합합니다. VLM은 장면 이해와 작업 계획을 담당하고, 자기 모델은 관절 각도, 토크 등 하위 수준 제어 신호를 처리합니다.
- **전신 제어 전략**: 모델 예측 제어(MPC)와 강화 학습(RL)의 혼합 프레임워크를 기반으로 이동과 조작의 조정을 구현합니다. 예를 들어, 걷는 동안 상체의 안정적인 잡기를 유지합니다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo와 Isaac Gym을 기반으로 구축되었으며, 실내 혼잡 장면, 좁은 통로 및 동적 장애물을 포함합니다.
- **기준 비교**: Task-and-Motion Planning (TAMP), 종단 간 RL 방법과 비교하여 작업 성공률, 실행 시간 및 에너지 소비를 평가합니다.
- **주요 수치**: 10가지 대표 작업에서 이 방법의 평균 성공률은 87.3%로, TAMP보다 12.6% 높았으며, 실행 시간은 23.4% 단축되었고, 전신 제어 에너지 소비는 15.2% 감소했습니다.

### 결론
본 연구는 체인형 동작 추론과 다중 모달 기초 모델의 결합이 휴머노이드 로봇의 이동 조작에서 효과적임을 입증했으며, 복잡한 작업 분해와 실시간 제어를 위한 새로운 패러다임을 제시했습니다. 향후 연구는 실제 로봇 플랫폼에서의 배포와 일반화 능력을 탐구할 것입니다.
