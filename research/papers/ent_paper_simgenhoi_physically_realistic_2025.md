---
$id: ent_paper_simgenhoi_physically_realistic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL'
  zh: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL'
  ko: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL'
summary:
  en: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL is a 2025 work
    on physics-based character animation for humanoid robots.'
  zh: SimGenHOI 是 2025 年提出的统一框架，结合生成式建模与强化学习，用于生成物理真实的人形机器人-物体交互。其核心贡献在于通过 Diffusion Transformers 预测关键动作，并利用接触感知全身控制策略修正穿透、滑动等伪影，同时引入互微调策略提升运动真实性与跟踪鲁棒性。
  ko: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL is a 2025 work
    on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- simgenhoi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14120v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL (arXiv)'
  url: https://arxiv.org/abs/2508.14120
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有基于扩散模型的交互生成方法常出现不合理的接触、穿透及不自然的全身动作，难以在物理环境中执行。SimGenHOI 通过 Diffusion Transformers 生成关键动作序列，并插值为平滑轨迹，支持长时程交互。随后，基于强化学习的接触感知全身控制策略跟踪生成运动，同时修正物理伪影。此外，生成模型与控制策略通过互微调相互优化，显著提升了运动真实性与跟踪成功率。

## 核心内容
### 方法架构
SimGenHOI 包含两个核心模块：
- **HOI 生成模型**：基于 Diffusion Transformers (DiT)，以文本提示、物体几何、稀疏物体路径点及初始人形姿态为条件，预测一组关键动作。这些关键动作捕捉交互动态，并通过插值生成平滑运动轨迹，支持长时程生成。
- **接触感知全身控制策略**：通过强化学习训练，跟踪生成运动的同时修正穿透、足部滑动等伪影。策略设计为接触感知，确保物理合理性。

### 互微调策略
生成模型与控制策略通过迭代互微调相互优化：生成模型根据控制策略的跟踪反馈调整动作分布，控制策略则利用生成模型提供的多样化运动数据提升鲁棒性。这一循环使运动真实性与跟踪性能同步提升。

### 实验设置与关键结果
- **基准与数据集**：在仿真环境中测试，涵盖多种物体交互任务（如推、拉、抓取）。
- **关键数字**：SimGenHOI 在仿真中实现显著更高的跟踪成功率，并支持长时程操作任务。与现有扩散模型相比，其生成的交互动作在接触合理性、穿透率及全身自然度上均表现更优。
- **结论**：实验证明 SimGenHOI 能生成真实、多样且物理合理的人形-物体交互，为机器人操作任务提供可靠基础。代码将在论文接收后于项目页面发布。

## Overview
Generating physically realistic humanoid-object interactions (HOI) is a fundamental challenge in robotics. Existing HOI generation approaches, such as diffusion-based models, often suffer from artifacts such as implausible contacts, penetrations, and unrealistic whole-body actions, which hinder successful execution in physical environments. To address these challenges, we introduce SimGenHOI, a unified framework that combines the strengths of generative modeling and reinforcement learning to produce controllable and physically plausible HOI. Our HOI generative model, based on Diffusion Transformers (DiT), predicts a set of key actions conditioned on text prompts, object geometry, sparse object waypoints, and the initial humanoid pose. These key actions capture essential interaction dynamics and are interpolated into smooth motion trajectories, naturally supporting long-horizon generation. To ensure physical realism, we design a contact-aware whole-body control policy trained with reinforcement learning, which tracks the generated motions while correcting artifacts such as penetration and foot sliding. Furthermore, we introduce a mutual fine-tuning strategy, where the generative model and the control policy iteratively refine each other, improving both motion realism and tracking robustness. Extensive experiments demonstrate that SimGenHOI generates realistic, diverse, and physically plausible humanoid-object interactions, achieving significantly higher tracking success rates in simulation and enabling long-horizon manipulation tasks. Code will be released upon acceptance on our project page: https://xingxingzuo.github.io/simgen_hoi.

## 개요
물리적으로 현실적인 인간형-객체 상호작용(HOI)을 생성하는 것은 로봇공학의 근본적인 과제입니다. 확산 기반 모델과 같은 기존 HOI 생성 접근 방식은 종종 비현실적인 접촉, 관통, 비현실적인 전신 동작과 같은 인공물로 인해 물리적 환경에서의 성공적인 실행을 저해합니다. 이러한 문제를 해결하기 위해, 우리는 생성 모델링과 강화 학습의 장점을 결합하여 제어 가능하고 물리적으로 타당한 HOI를 생성하는 통합 프레임워크인 SimGenHOI를 소개합니다. Diffusion Transformers(DiT)를 기반으로 하는 HOI 생성 모델은 텍스트 프롬프트, 객체 형상, 희소 객체 웨이포인트, 초기 인간형 자세에 따라 일련의 핵심 동작을 예측합니다. 이러한 핵심 동작은 필수적인 상호작용 역학을 포착하며 부드러운 모션 궤적으로 보간되어 장기간 생성을 자연스럽게 지원합니다. 물리적 현실성을 보장하기 위해, 우리는 강화 학습으로 훈련된 접촉 인식 전신 제어 정책을 설계하여 생성된 동작을 추적하면서 관통 및 발 미끄러짐과 같은 인공물을 교정합니다. 또한, 생성 모델과 제어 정책이 상호 반복적으로 정제되어 동작 현실성과 추적 견고성을 모두 향상시키는 상호 미세 조정 전략을 도입합니다. 광범위한 실험을 통해 SimGenHOI가 현실적이고 다양하며 물리적으로 타당한 인간형-객체 상호작용을 생성하여 시뮬레이션에서 현저히 높은 추적 성공률을 달성하고 장기간 조작 작업을 가능하게 함을 입증합니다. 코드는 수락 시 프로젝트 페이지(https://xingxingzuo.github.io/simgen_hoi)에서 공개될 예정입니다.

## 핵심 내용
물리적으로 현실적인 인간형-객체 상호작용(HOI)을 생성하는 것은 로봇공학의 근본적인 과제입니다. 확산 기반 모델과 같은 기존 HOI 생성 접근 방식은 종종 비현실적인 접촉, 관통, 비현실적인 전신 동작과 같은 인공물로 인해 물리적 환경에서의 성공적인 실행을 저해합니다. 이러한 문제를 해결하기 위해, 우리는 생성 모델링과 강화 학습의 장점을 결합하여 제어 가능하고 물리적으로 타당한 HOI를 생성하는 통합 프레임워크인 SimGenHOI를 소개합니다. Diffusion Transformers(DiT)를 기반으로 하는 HOI 생성 모델은 텍스트 프롬프트, 객체 형상, 희소 객체 웨이포인트, 초기 인간형 자세에 따라 일련의 핵심 동작을 예측합니다. 이러한 핵심 동작은 필수적인 상호작용 역학을 포착하며 부드러운 모션 궤적으로 보간되어 장기간 생성을 자연스럽게 지원합니다. 물리적 현실성을 보장하기 위해, 우리는 강화 학습으로 훈련된 접촉 인식 전신 제어 정책을 설계하여 생성된 동작을 추적하면서 관통 및 발 미끄러짐과 같은 인공물을 교정합니다. 또한, 생성 모델과 제어 정책이 상호 반복적으로 정제되어 동작 현실성과 추적 견고성을 모두 향상시키는 상호 미세 조정 전략을 도입합니다. 광범위한 실험을 통해 SimGenHOI가 현실적이고 다양하며 물리적으로 타당한 인간형-객체 상호작용을 생성하여 시뮬레이션에서 현저히 높은 추적 성공률을 달성하고 장기간 조작 작업을 가능하게 함을 입증합니다. 코드는 수락 시 프로젝트 페이지(https://xingxingzuo.github.io/simgen_hoi)에서 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2508.14120v1
