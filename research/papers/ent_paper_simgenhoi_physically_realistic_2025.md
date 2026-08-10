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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14120v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (747 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2508.14120v1

## 개요
기존 확산 모델 기반 상호작용 생성 방법은 종종 비합리적인 접촉, 관통 및 부자연스러운 전신 동작을 초래하여 물리적 환경에서 실행하기 어렵습니다. SimGenHOI는 Diffusion Transformers를 통해 핵심 동작 시퀀스를 생성하고 이를 보간하여 부드러운 궤적으로 변환함으로써 장시간 상호작용을 지원합니다. 이후 강화 학습 기반의 접촉 인식 전신 제어 정책이 생성된 동작을 추적하면서 물리적 인공물을 수정합니다. 또한 생성 모델과 제어 정책은 상호 미세 조정을 통해 서로 최적화되어 동작의 사실성과 추적 성공률을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
SimGenHOI는 두 가지 핵심 모듈로 구성됩니다:
- **HOI 생성 모델**: Diffusion Transformers (DiT) 기반으로, 텍스트 프롬프트, 객체 기하학, 희소 객체 웨이포인트 및 초기 인간형 자세를 조건으로 하여 일련의 핵심 동작을 예측합니다. 이러한 핵심 동작은 상호작용 역학을 포착하며, 보간을 통해 부드러운 운동 궤적을 생성하여 장시간 생성을 지원합니다.
- **접촉 인식 전신 제어 정책**: 강화 학습을 통해 훈련되며, 생성된 동작을 추적하면서 관통, 발 미끄러짐 등의 인공물을 수정합니다. 정책은 접촉 인식으로 설계되어 물리적 합리성을 보장합니다.

### 상호 미세 조정 전략
생성 모델과 제어 정책은 반복적인 상호 미세 조정을 통해 서로 최적화됩니다: 생성 모델은 제어 정책의 추적 피드백에 따라 동작 분포를 조정하고, 제어 정책은 생성 모델이 제공하는 다양한 동작 데이터를 활용하여 견고성을 향상시킵니다. 이 순환 과정은 동작 사실성과 추적 성능이 동시에 향상되도록 합니다.

### 실험 설정 및 주요 결과
- **벤치마크 및 데이터셋**: 시뮬레이션 환경에서 테스트되며, 다양한 객체 상호작용 작업(예: 밀기, 당기기, 잡기)을 포함합니다.
- **주요 수치**: SimGenHOI는 시뮬레이션에서 현저히 높은 추적 성공률을 달성하고 장시간 조작 작업을 지원합니다. 기존 확산 모델과 비교하여 생성된 상호작용 동작은 접촉 합리성, 관통률 및 전신 자연스러움에서 모두 더 우수한 성능을 보입니다.
- **결론**: 실험은 SimGenHOI가 사실적이고 다양하며 물리적으로 합리적인 인간형-객체 상호작용을 생성할 수 있음을 증명하며, 로봇 조작 작업에 신뢰할 수 있는 기반을 제공합니다. 코드는 논문 수락 후 프로젝트 페이지에서 공개될 예정입니다.
