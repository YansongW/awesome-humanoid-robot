---
$id: ent_paper_zhao_cot_vla_visual_chain_of_though_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models'
  zh: CoT-VLA
  ko: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models'
summary:
  en: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
  zh: CoT-VLA 是 NVIDIA、Stanford University、MIT 于 2025 年联合提出的 7B 规模视觉-语言-动作模型，发表于 CVPR25。其核心贡献在于将显式的视觉思维链推理引入机器人操作，通过自回归预测未来图像帧作为视觉目标，再生成短动作序列，从而提升复杂操作任务中的时序规划能力。实验表明，CoT-VLA
    在真实操作任务中比现有最优 VLA 模型提升 17%，在仿真基准中提升 6%。
  ko: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cot_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22020v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: CoT-VLA source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型虽能利用预训练模型和多样化机器人演示数据学习通用传感器运动控制，但主要依赖直接的输入-输出映射，缺乏复杂操作任务所需的中介推理步骤，导致时序规划能力不足。CoT-VLA 通过引入显式视觉思维链推理，让模型在生成动作序列前先自回归地预测未来图像帧作为视觉目标，从而将推理过程可视化。该模型在 7B 参数量级上实现了视觉与动作令牌的统一理解与生成，并在真实与仿真环境中均取得显著性能提升。

## 核心内容
### 方法
- **视觉思维链推理**：模型在生成动作序列前，先自回归地预测一系列未来图像帧（视觉目标），将推理过程显式化为可观察的中间步骤。
- **令牌统一处理**：CoT-VLA 将视觉图像与动作指令统一编码为令牌序列，实现端到端的理解与生成。

### 架构
- 基于 7B 参数量的视觉-语言-动作模型架构，融合预训练视觉语言模型与机器人演示数据。
- 采用自回归预测机制，在动作生成前先输出视觉目标帧，形成“视觉推理→动作执行”的链式结构。

### 实验设置
- **真实操作任务**：在多种机器人操作场景中测试，包括抓取、放置、组装等复杂任务。
- **仿真基准**：在标准机器人操作仿真环境中评估，涵盖多步规划与动态环境适应。

### 关键结果
- **真实操作**：CoT-VLA 比现有最优 VLA 模型性能提升 17%。
- **仿真基准**：性能提升 6%，验证了视觉思维链推理在复杂任务中的有效性。

### 结论
CoT-VLA 通过显式视觉思维链推理，有效解决了现有 VLA 模型缺乏时序规划能力的问题，在真实与仿真环境中均达到最优性能。项目网站：https://cot-vla.github.io/

## Overview
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## Overview
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input–output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## Content
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input–output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## 개요
Vision-language-action models (VLAs)는 사전 훈련된 시각-언어 모델과 다양한 로봇 시연을 활용하여 일반화 가능한 감각운동 제어를 학습하는 데 잠재력을 보여주었습니다. 이 패러다임은 로봇 및 비로봇 소스의 대규모 데이터를 효과적으로 활용하지만, 현재 VLA는 주로 직접적인 입력-출력 매핑에 초점을 맞추고 있어 복잡한 조작 작업에 중요한 중간 추론 단계가 부족합니다. 그 결과, 기존 VLA는 시간적 계획 또는 추론 능력이 결여되어 있습니다. 본 논문에서는 짧은 행동 시퀀스를 생성하여 목표를 달성하기 전에 미래 이미지 프레임을 자기회귀적으로 시각적 목표로 예측함으로써 명시적 시각적 사고 사슬(CoT) 추론을 시각-언어-행동 모델(VLA)에 통합하는 방법을 소개합니다. 우리는 시각 및 행동 토큰을 이해하고 생성할 수 있는 최첨단 7B VLA인 CoT-VLA를 제안합니다. 실험 결과, CoT-VLA는 실제 조작 작업에서 최첨단 VLA 모델보다 17%, 시뮬레이션 벤치마크에서 6% 더 뛰어난 성능을 보여주었습니다. 프로젝트 웹사이트: https://cot-vla.github.io/

## 핵심 내용
Vision-language-action models (VLAs)는 사전 훈련된 시각-언어 모델과 다양한 로봇 시연을 활용하여 일반화 가능한 감각운동 제어를 학습하는 데 잠재력을 보여주었습니다. 이 패러다임은 로봇 및 비로봇 소스의 대규모 데이터를 효과적으로 활용하지만, 현재 VLA는 주로 직접적인 입력-출력 매핑에 초점을 맞추고 있어 복잡한 조작 작업에 중요한 중간 추론 단계가 부족합니다. 그 결과, 기존 VLA는 시간적 계획 또는 추론 능력이 결여되어 있습니다. 본 논문에서는 짧은 행동 시퀀스를 생성하여 목표를 달성하기 전에 미래 이미지 프레임을 자기회귀적으로 시각적 목표로 예측함으로써 명시적 시각적 사고 사슬(CoT) 추론을 시각-언어-행동 모델(VLA)에 통합하는 방법을 소개합니다. 우리는 시각 및 행동 토큰을 이해하고 생성할 수 있는 최첨단 7B VLA인 CoT-VLA를 제안합니다. 실험 결과, CoT-VLA는 실제 조작 작업에서 최첨단 VLA 모델보다 17%, 시뮬레이션 벤치마크에서 6% 더 뛰어난 성능을 보여주었습니다. 프로젝트 웹사이트: https://cot-vla.github.io/

## 参考
- http://arxiv.org/abs/2503.22020v1
