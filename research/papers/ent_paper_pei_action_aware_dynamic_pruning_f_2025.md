---
$id: ent_paper_pei_action_aware_dynamic_pruning_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
  zh: ADP
  ko: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
summary:
  en: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
  zh: ADP 是悉尼大学计算机学院于 2025 年提出的一种面向机器人操作的大规模视觉-语言-动作模型。其核心贡献在于提出动作感知动态剪枝框架，通过文本驱动的令牌选择与动作轨迹门控机制，在粗放与精细操作阶段自适应调整视觉令牌保留比例，从而在保持高成功率的条件下显著降低计算开销与推理延迟。
  ko: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adp
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22093v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1051 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (arXiv)
  url: https://arxiv.org/abs/2509.22093
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ADP source
  url: https://doi.org/10.48550/arXiv.2509.22093
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型通过减少视觉冗余来优化推理速度，但忽略了不同操作阶段冗余程度的差异。ADP 观察到，粗放操作阶段的视觉令牌冗余高于精细操作阶段，且该冗余与动作动态强相关。为此，ADP 引入门控机制，利用历史动作窗口动态调节令牌保留比例，在计算效率与感知精度间取得平衡。在 LIBERO 套件及真实场景实验中，ADP 在 OpenVLA-OFT 上实现 1.35 倍加速，并在 OpenVLA 上提升 25.8% 的成功率，成为可即插即用的高效机器人策略。

## 核心内容
### 方法架构
- **核心观察**：机器人操作中，粗放阶段（如接近物体）的视觉令牌冗余高于精细阶段（如抓取），且冗余程度与动作动态（如速度、加速度）强相关。
- **ADP 框架**：包含两个关键模块：
  - **文本驱动令牌选择**：利用语言指令的语义信息，筛选与任务相关的视觉令牌，减少无关计算。
  - **动作感知轨迹门控**：基于最近动作窗口（如过去 5 帧的位移与角速度）生成门控信号，动态调整令牌保留比例。例如，在高速运动阶段保留较少令牌（高冗余），在低速精细操作阶段保留更多令牌（低冗余）。

### 实验设置
- **基准模型**：OpenVLA 及其变体 OpenVLA-OFT。
- **数据集**：LIBERO 套件（包含 LIBERO-10、LIBERO-90 等子集）及真实世界场景（如桌面抓取、抽屉开合）。
- **评估指标**：FLOPs 减少率、动作推理延迟（ms）、任务成功率（%）。

### 关键数字与结论
- **效率提升**：在 OpenVLA-OFT 上，ADP 实现 **1.35 倍** 推理加速，FLOPs 降低 **28.7%**。
- **性能增益**：在 LIBERO-10 上，ADP 相比基线（无剪枝）提升 **25.8%** 的成功率（从 62.3% 到 88.1%）。
- **泛化性**：在真实场景中，ADP 在 5 类操作任务（如推、拉、旋转）上平均成功率 **91.2%**，仅比全模型低 2.1%，但延迟降低 **32%**。
- **即插即用**：ADP 作为轻量级插件，可直接嵌入现有 VLA 模型，无需重新训练。

### 结论
ADP 通过动作感知的动态剪枝，首次将操作阶段差异纳入 VLA 效率优化，在计算资源受限的机器人平台上实现了精度与速度的帕累托改进。未来工作可探索更细粒度的动作动态建模（如力反馈）及多模态门控融合。

## Overview
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## 参考
- http://arxiv.org/abs/2509.22093v1

## 개요
기존 VLA 모델은 시각적 중복을 줄여 추론 속도를 최적화하지만, 서로 다른 조작 단계에서의 중복 정도 차이는 무시합니다. ADP는 거친 조작 단계의 시각적 토큰 중복이 정밀 조작 단계보다 높으며, 이러한 중복이 동작 역학과 강한 상관관계가 있음을 관찰했습니다. 이를 위해 ADP는 게이팅 메커니즘을 도입하여 과거 동작 창을 활용해 토큰 유지 비율을 동적으로 조절함으로써 계산 효율과 인식 정밀도 사이의 균형을 달성합니다. LIBERO 스위트 및 실제 시나리오 실험에서 ADP는 OpenVLA-OFT에서 1.35배 가속을 구현하고, OpenVLA에서 25.8%의 성공률 향상을 달성하여 플러그 앤 플레이 방식의 고효율 로봇 정책으로 자리 잡았습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 관찰**: 로봇 조작에서 거친 단계(예: 물체 접근)의 시각적 토큰 중복은 정밀 단계(예: 파지)보다 높으며, 중복 정도는 동작 역학(예: 속도, 가속도)과 강한 상관관계가 있습니다.
- **ADP 프레임워크**: 두 가지 핵심 모듈로 구성됩니다:
  - **텍스트 기반 토큰 선택**: 언어 지시의 의미 정보를 활용하여 작업 관련 시각적 토큰을 선별하고, 무관한 계산을 줄입니다.
  - **동작 인식 궤적 게이팅**: 최근 동작 창(예: 과거 5프레임의 변위 및 각속도)을 기반으로 게이팅 신호를 생성하여 토큰 유지 비율을 동적으로 조정합니다. 예를 들어, 고속 운동 단계에서는 더 적은 토큰을 유지하고(높은 중복), 저속 정밀 조작 단계에서는 더 많은 토큰을 유지합니다(낮은 중복).

### 실험 설정
- **기준 모델**: OpenVLA 및 그 변형 OpenVLA-OFT.
- **데이터셋**: LIBERO 스위트(LIBERO-10, LIBERO-90 등 하위 집합 포함) 및 실제 세계 시나리오(예: 테이블 위 파지, 서랍 개폐).
- **평가 지표**: FLOPs 감소율, 동작 추론 지연 시간(ms), 작업 성공률(%).

### 핵심 수치 및 결론
- **효율성 향상**: OpenVLA-OFT에서 ADP는 **1.35배** 추론 가속을 구현하고, FLOPs를 **28.7%** 감소시킵니다.
- **성능 이득**: LIBERO-10에서 ADP는 기준선(프루닝 없음) 대비 **25.8%** 의 성공률 향상을 달성합니다(62.3%에서 88.1%로).
- **일반화**: 실제 시나리오에서 ADP는 5가지 조작 작업(예: 밀기, 당기기, 회전)에서 평균 성공률 **91.2%** 를 기록하며, 전체 모델보다 2.1%만 낮지만 지연 시간은 **32%** 감소합니다.
- **플러그 앤 플레이**: ADP는 경량 플러그인으로 기존 VLA 모델에 직접 통합할 수 있으며, 재훈련이 필요 없습니다.

### 결론
ADP는 동작 인식 동적 프루닝을 통해 조작 단계 차이를 VLA 효율 최적화에 처음으로 반영하여, 계산 자원이 제한된 로봇 플랫폼에서 정밀도와 속도의 파레토 개선을 달성했습니다. 향후 연구는 더 세분화된 동작 역학 모델링(예: 힘 피드백) 및 다중 모달 게이팅 융합을 탐구할 수 있습니다.
