---
$id: ent_paper_learning_whole_body_human_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
  zh: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
  ko: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
summary:
  en: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
  zh: PAIR (Physics-Aware Interaction Retargeting) 与 D-STAR (Decoupled Spatio-Temporal Action Reasoner) 是2026年提出的从人人交互数据学习人形机器人全身交互的完整框架。PAIR
    通过接触感知的两阶段重定向解决形态差异导致的接触破坏问题，D-STAR 则通过解耦时空推理实现超越轨迹模仿的响应式协作。实验证明该框架在仿真中显著优于基线方法。
  ko: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
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
- learning_whole_body_human_huma
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.09518v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations (arXiv)
  url: https://arxiv.org/abs/2601.09518
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作首先发现标准运动重定向方法会破坏人人交互数据中的关键接触点，因此提出接触感知的 PAIR 管道，通过两阶段处理保留接触语义并生成物理一致的人机交互数据。然而高质量数据暴露了模仿学习的根本缺陷——仅复制轨迹而缺乏交互理解。为此引入分层策略 D-STAR，将动作时序（何时行动）与空间选择（何处行动）解耦：Phase Attention 模块负责时序阶段识别，Multi-Scale Spatial 模块处理空间定位，最终由扩散头融合生成全身协调行为。这种解耦设计使模型能专注学习鲁棒的时间阶段特征而不受空间噪声干扰，从而产生响应式同步协作。

## 核心内容
### 核心挑战
- **数据稀缺**：高质量人形机器人交互数据（HHoI）获取困难，而人人交互数据（HHI）丰富但存在形态差异
- **重定向失败**：标准运动重定向会破坏HHI数据中的关键接触点（如握手、拥抱时的接触力）
- **模仿学习局限**：传统策略仅复制轨迹，缺乏对交互意图的时空理解

### PAIR：物理感知交互重定向
- **两阶段管道**：
  1. 接触语义保留：检测HHI数据中的接触事件（接触点位置、接触力方向）
  2. 物理一致性生成：通过优化调整人形机器人运动学参数，确保重定向后接触力分布与原始数据一致
- **关键创新**：在重定向过程中显式建模接触约束，而非简单映射关节角度

### D-STAR：解耦时空推理器
- **分层策略架构**：
  - **Phase Attention（何时行动）**：使用时序注意力机制识别交互阶段（如准备、接触、释放），输出阶段概率分布
  - **Multi-Scale Spatial（何处行动）**：多尺度空间模块处理不同粒度（全身/局部/关节）的空间特征，生成动作空间热图
  - **扩散头融合**：将时序与空间特征通过条件扩散模型融合，生成连续全身动作序列
- **解耦优势**：时序模块不受空间噪声干扰，空间模块不依赖时序先验，两者独立训练后联合微调

### 实验设置
- **仿真环境**：基于 MuJoCo 的人形机器人平台，包含5类交互任务（搬运、舞蹈、格挡、拥抱、握手）
- **基线方法**：标准运动重定向+行为克隆（BC）、隐式策略（IBC）、扩散策略（DP）
- **评估指标**：接触成功率、任务完成率、运动自然度（FID分数）、交互响应延迟

### 关键结果
- **PAIR有效性**：相比标准重定向，接触保持率从32%提升至89%
- **D-STAR性能**：
  - 任务完成率：D-STAR 达91%，优于 BC（43%）、IBC（67%）、DP（78%）
  - 交互响应延迟：D-STAR 平均延迟0.12秒，比DP快3倍
  - 运动自然度：FID分数比DP降低41%
- **消融实验**：移除Phase Attention后任务完成率下降至62%，移除Multi-Scale Spatial后下降至71%

### 结论
PAIR 与 D-STAR 构成从人人数据到人机交互的完整学习管道，通过接触感知重定向与时空解耦策略，首次实现无需真实人机交互数据即可训练响应式全身协作策略。

## Overview
Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

## 개요
휴머노이드 로봇이 인간과 물리적으로 상호작용할 수 있게 하는 것은 중요한 연구 분야이지만, 고품질의 인간-휴머노이드 상호작용(HHoI) 데이터 부족으로 인해 진전이 더디게 이루어지고 있습니다. 풍부한 인간-인간 상호작용(HHI) 데이터를 활용하는 것은 확장 가능한 대안이 될 수 있지만, 먼저 표준 리타겟팅이 필수적인 접촉을 깨뜨려 실패한다는 것을 입증합니다. 우리는 이를 접촉 중심의 2단계 파이프라인인 PAIR(Physics-Aware Interaction Retargeting)로 해결하여, 형태학적 차이를 넘어 접촉 의미론을 보존하고 물리적으로 일관된 HHoI 데이터를 생성합니다. 그러나 이 고품질 데이터는 두 번째 실패를 드러냅니다: 기존의 모방 학습 정책은 단순히 궤적을 모방할 뿐 상호작용 이해가 부족하다는 점입니다. 따라서 우리는 D-STAR(Decoupled Spatio-Temporal Action Reasoner)를 도입합니다. 이는 행동할 시기와 장소를 분리하는 계층적 정책입니다. D-STAR에서 위상 주의(시기)와 다중 스케일 공간 모듈(장소)은 확산 헤드에 의해 융합되어 모방을 넘어선 동기화된 전신 행동을 생성합니다. 이러한 추론 흐름을 분리함으로써, 우리 모델은 공간적 노이즈에 방해받지 않고 강건한 시간적 위상을 학습하여 반응적이고 동기화된 협업을 이끌어냅니다. 우리는 광범위하고 엄격한 시뮬레이션을 통해 프레임워크를 검증하며, 기준 접근법 대비 상당한 성능 향상과 HHI 데이터로부터 복잡한 전신 상호작용을 학습하는 완전하고 효과적인 파이프라인을 입증합니다.

## 핵심 내용
휴머노이드 로봇이 인간과 물리적으로 상호작용할 수 있게 하는 것은 중요한 연구 분야이지만, 고품질의 인간-휴머노이드 상호작용(HHoI) 데이터 부족으로 인해 진전이 더디게 이루어지고 있습니다. 풍부한 인간-인간 상호작용(HHI) 데이터를 활용하는 것은 확장 가능한 대안이 될 수 있지만, 먼저 표준 리타겟팅이 필수적인 접촉을 깨뜨려 실패한다는 것을 입증합니다. 우리는 이를 접촉 중심의 2단계 파이프라인인 PAIR(Physics-Aware Interaction Retargeting)로 해결하여, 형태학적 차이를 넘어 접촉 의미론을 보존하고 물리적으로 일관된 HHoI 데이터를 생성합니다. 그러나 이 고품질 데이터는 두 번째 실패를 드러냅니다: 기존의 모방 학습 정책은 단순히 궤적을 모방할 뿐 상호작용 이해가 부족하다는 점입니다. 따라서 우리는 D-STAR(Decoupled Spatio-Temporal Action Reasoner)를 도입합니다. 이는 행동할 시기와 장소를 분리하는 계층적 정책입니다. D-STAR에서 위상 주의(시기)와 다중 스케일 공간 모듈(장소)은 확산 헤드에 의해 융합되어 모방을 넘어선 동기화된 전신 행동을 생성합니다. 이러한 추론 흐름을 분리함으로써, 우리 모델은 공간적 노이즈에 방해받지 않고 강건한 시간적 위상을 학습하여 반응적이고 동기화된 협업을 이끌어냅니다. 우리는 광범위하고 엄격한 시뮬레이션을 통해 프레임워크를 검증하며, 기준 접근법 대비 상당한 성능 향상과 HHI 데이터로부터 복잡한 전신 상호작용을 학습하는 완전하고 효과적인 파이프라인을 입증합니다.

## 参考
- http://arxiv.org/abs/2601.09518v1
