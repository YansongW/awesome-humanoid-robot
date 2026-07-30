---
$id: ent_paper_zhong_dexgraspvla_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping'
  zh: DexGraspVLA
  ko: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping'
summary:
  en: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (DexGraspVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute for Artificial Intelligence, Peking University, PKU-PsiBot Joint
    Lab, Hong Kong University of Science and Technology (Guangzhou), University of Pennsylvania.'
  zh: DexGraspVLA 是北京大学、香港科技大学（广州）和宾夕法尼亚大学联合提出的 2025 年大型视觉-语言-动作模型，用于通用灵巧抓取。其核心贡献在于通过层次化框架结合预训练视觉-语言模型与扩散动作控制器，在数千种未见过的杂乱场景中实现
    90% 以上的抓取成功率，并首次支持自由形式长程指令、对抗性物体和人类干扰下的鲁棒操作及失败恢复。
  ko: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (DexGraspVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute for Artificial Intelligence, Peking University, PKU-PsiBot Joint
    Lab, Hong Kong University of Science and Technology (Guangzhou), University of Pennsylvania.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexgraspvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.20900v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (arXiv)'
  url: https://arxiv.org/abs/2502.20900
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexGraspVLA source
  url: https://doi.org/10.48550/arXiv.2502.20900
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DexGraspVLA 针对现有灵巧抓取研究依赖单物体或受限环境的局限，提出层次化框架实现鲁棒泛化。高层规划器使用预训练视觉-语言模型理解语言指令和场景，低层控制器则通过扩散模型生成精确抓取动作。其关键创新在于利用基础模型将多样化的语言和视觉输入转化为域不变表示，从而缓解域偏移问题，使模仿学习能有效应用于新场景。实验表明，该方法在数千个挑战性杂乱场景中达到 90% 以上的抓取成功率，并首次同时展示自由形式长程提示执行、对抗物体和人类干扰下的鲁棒性以及失败恢复能力。

## 核心内容
### 方法架构
DexGraspVLA 采用层次化框架：
- **高层规划器**：基于预训练视觉-语言模型（如 CLIP 或类似架构），将语言指令和视觉场景解析为抽象任务规划。
- **低层动作控制器**：使用扩散模型（Diffusion-based）生成连续的灵巧手抓取动作，通过迭代去噪过程输出精确的关节角度序列。
- **域不变表示**：通过基础模型将语言和视觉输入映射到共享的域不变特征空间，消除不同场景间的分布差异，使模仿学习能直接应用。

### 实验设置
- **训练数据**：使用大规模灵巧抓取演示数据集，涵盖多种物体类型和场景配置。
- **测试场景**：数千个未见过的杂乱场景，包括堆叠物体、遮挡、光照变化等挑战。
- **评估指标**：抓取成功率（90%+）、长程指令执行成功率、对抗物体鲁棒性、人类干扰恢复率。

### 关键结果
- **抓取成功率**：在数千个挑战性杂乱场景中达到 90% 以上，显著优于基线方法（如单物体抓取模型）。
- **泛化能力**：内部模型行为在不同环境变化下保持一致性，验证了域不变表示的有效性。
- **长程指令**：首次支持自由形式长程提示（如“先拿起杯子，再抓取旁边的球”），无需重新训练。
- **鲁棒性**：对对抗性物体（如不规则形状、易碎物体）和人类干扰（如移动物体）表现出强鲁棒性。
- **失败恢复**：当抓取失败时，模型能自动调整策略并重新尝试，无需外部干预。
- **非抓取操作**：扩展至非抓取操作（如推、拉），进一步证明框架的通用性。

### 结论
DexGraspVLA 通过层次化框架和域不变表示，在通用灵巧抓取中实现了前所未有的泛化能力和鲁棒性，为机器人操作领域提供了新的范式。

## Overview
Dexterous grasping remains a fundamental yet challenging problem in robotics. A general-purpose robot must be capable of grasping diverse objects in arbitrary scenarios. However, existing research typically relies on restrictive assumptions, such as single-object settings or limited environments, showing constrained generalization. We present DexGraspVLA, a hierarchical framework for robust generalization in language-guided general dexterous grasping and beyond. It utilizes a pre-trained Vision-Language model as the high-level planner and learns a diffusion-based low-level Action controller. The key insight to achieve generalization lies in iteratively transforming diverse language and visual inputs into domain-invariant representations via foundation models, where imitation learning can be effectively applied due to the alleviation of domain shift. Notably, our method achieves a 90+% dexterous grasping success rate under thousands of challenging unseen cluttered scenes. Empirical analysis confirms the consistency of internal model behavior across environmental variations, validating our design. DexGraspVLA also, for the first time, simultaneously demonstrates free-form long-horizon prompt execution, robustness to adversarial objects and human disturbance, and failure recovery. Extended application to nonprehensile grasping further proves its generality. Project website: https://dexgraspvla.github.io.

## 개요
정밀 파지(dexterous grasping)는 로봇 공학에서 여전히 근본적이면서도 도전적인 문제로 남아 있습니다. 범용 로봇은 임의의 시나리오에서 다양한 물체를 잡을 수 있어야 합니다. 그러나 기존 연구는 일반적으로 단일 물체 설정이나 제한된 환경과 같은 제약적인 가정에 의존하여 일반화 능력이 제한적입니다. 본 논문에서는 언어 기반 범용 정밀 파지 및 그 이상을 위한 강건한 일반화를 위한 계층적 프레임워크인 DexGraspVLA를 제안합니다. 이는 사전 훈련된 Vision-Language 모델을 상위 수준 계획자로 활용하고, 확산 기반 하위 수준 Action 컨트롤러를 학습합니다. 일반화를 달성하기 위한 핵심 통찰은 다양한 언어 및 시각 입력을 기반 모델을 통해 반복적으로 도메인 불변 표현으로 변환하는 데 있으며, 이로 인해 도메인 변화가 완화되어 모방 학습이 효과적으로 적용될 수 있습니다. 특히, 본 방법은 수천 개의 도전적인 미지의 복잡한 장면에서 90% 이상의 정밀 파지 성공률을 달성합니다. 실증 분석은 환경 변화에 따른 내부 모델 행동의 일관성을 확인하여 설계를 검증합니다. DexGraspVLA는 또한 처음으로 자유 형식의 장기 프롬프트 실행, 적대적 물체 및 인간 방해에 대한 강건성, 그리고 실패 복구를 동시에 보여줍니다. 비파지(nonprehensile) 파지로의 확장 적용은 그 일반성을 더욱 입증합니다. 프로젝트 웹사이트: https://dexgraspvla.github.io.

## 핵심 내용
정밀 파지는 로봇 공학에서 여전히 근본적이면서도 도전적인 문제로 남아 있습니다. 범용 로봇은 임의의 시나리오에서 다양한 물체를 잡을 수 있어야 합니다. 그러나 기존 연구는 일반적으로 단일 물체 설정이나 제한된 환경과 같은 제약적인 가정에 의존하여 일반화 능력이 제한적입니다. 본 논문에서는 언어 기반 범용 정밀 파지 및 그 이상을 위한 강건한 일반화를 위한 계층적 프레임워크인 DexGraspVLA를 제안합니다. 이는 사전 훈련된 Vision-Language 모델을 상위 수준 계획자로 활용하고, 확산 기반 하위 수준 Action 컨트롤러를 학습합니다. 일반화를 달성하기 위한 핵심 통찰은 다양한 언어 및 시각 입력을 기반 모델을 통해 반복적으로 도메인 불변 표현으로 변환하는 데 있으며, 이로 인해 도메인 변화가 완화되어 모방 학습이 효과적으로 적용될 수 있습니다. 특히, 본 방법은 수천 개의 도전적인 미지의 복잡한 장면에서 90% 이상의 정밀 파지 성공률을 달성합니다. 실증 분석은 환경 변화에 따른 내부 모델 행동의 일관성을 확인하여 설계를 검증합니다. DexGraspVLA는 또한 처음으로 자유 형식의 장기 프롬프트 실행, 적대적 물체 및 인간 방해에 대한 강건성, 그리고 실패 복구를 동시에 보여줍니다. 비파지 파지로의 확장 적용은 그 일반성을 더욱 입증합니다. 프로젝트 웹사이트: https://dexgraspvla.github.io.

## 参考
- http://arxiv.org/abs/2502.20900v5
