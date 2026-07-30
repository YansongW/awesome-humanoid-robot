---
$id: ent_paper_liu_robomamba_efficient_vision_lan_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation'
  zh: RoboMamba
  ko: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation'
summary:
  en: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (RoboMamba), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial Intelligence (BAAI), and published
    at NIPS 2024.'
  zh: RoboMamba 是北京大学、AI2Robotics 与北京智源人工智能研究院（BAAI）于 NIPS 2024 提出的高效视觉-语言-动作模型。其核心贡献在于利用状态空间模型 Mamba 实现线性复杂度的推理，仅需微调 0.1%
    的参数即可获得 SE(3) 位姿预测能力，推理速度较现有 VLA 模型快 3 倍。
  ko: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (RoboMamba), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial Intelligence (BAAI), and published
    at NIPS 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robomamba
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.04339v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: RoboMamba source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有机器人 VLA 模型面临推理能力不足与计算成本高昂两大挑战。RoboMamba 通过将视觉编码器与 Mamba 集成，采用视觉-语言联合训练策略赋予模型常识推理能力。该模型仅需微调极少量参数（0.1%）即可掌握操作技能，在通用与机器人评测基准上均展现卓越推理性能，并在仿真与真实实验中实现 3 倍于现有模型的推理速度。

## 核心内容
### 方法架构
- 采用 Mamba 作为核心序列建模器，利用其线性推理复杂度特性
- 视觉编码器与 Mamba 通过联合训练实现视觉-语言嵌入对齐
- 设计轻量级策略头（policy head）实现 SE(3) 位姿预测

### 关键创新
- 高效微调策略：仅需微调 0.1% 的模型参数即可获得操作能力
- 推理速度优势：在保持推理能力的同时，实现 3 倍于现有 VLA 模型的推理速度
- 端到端架构：从视觉输入直接映射到动作输出

### 实验设置
- 通用评测基准：验证模型在视觉常识与机器人相关推理方面的能力
- 机器人操作基准：在仿真与真实环境中测试 SE(3) 位姿预测性能
- 对比基线：与现有 VLA 模型进行推理速度与操作精度对比

### 关键结果
- 在通用与机器人评测基准上均展现卓越推理能力
- 仿真与真实实验中位姿预测结果令人满意
- 推理速度达到 3 倍于现有 VLA 模型
- 微调参数仅占模型总量的 0.1%，显著降低计算成本

## Overview
A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions. Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability to tackle complex tasks, and (2) high computational costs for VLA model fine-tuning and inference. The recently proposed state space model (SSM) known as Mamba demonstrates promising capabilities in non-trivial sequence modeling with linear inference complexity. Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient fine-tuning and inference. Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and robotic-related reasoning. To further equip RoboMamba with SE(3) pose prediction abilities, we explore an efficient fine-tuning strategy with a simple policy head. We find that once RoboMamba possesses sufficient reasoning capability, it can acquire manipulation skills with minimal fine-tuning parameters (0.1\% of the model) and time. In experiments, RoboMamba demonstrates outstanding reasoning capabilities on general and robotic evaluation benchmarks. Meanwhile, our model showcases impressive pose prediction results in both simulation and real-world experiments, achieving inference speeds 3 times faster than existing VLA models. Our project web page: https://sites.google.com/view/robomamba-web

## 개요
로봇 조작의 근본적인 목표는 모델이 시각적 장면을 이해하고 행동을 실행할 수 있도록 하는 것입니다. 기존의 로봇용 Vision-Language-Action (VLA) 모델은 다양한 기본 작업을 처리할 수 있지만, 여전히 두 가지 영역에서 어려움에 직면합니다: (1) 복잡한 작업을 해결하기 위한 추론 능력 부족, (2) VLA 모델 미세 조정 및 추론의 높은 계산 비용입니다. 최근 제안된 상태 공간 모델(SSM)인 Mamba는 선형 추론 복잡도로 중요한 시퀀스 모델링에서 유망한 능력을 보여줍니다. 이에 영감을 받아, 우리는 RoboMamba를 소개합니다. 이는 Mamba를 활용하여 효율적인 미세 조정 및 추론을 유지하면서 로봇 추론 및 행동 능력을 모두 제공하는 엔드투엔드 로봇 VLA 모델입니다. 구체적으로, 먼저 비전 인코더를 Mamba와 통합하고, 공동 훈련을 통해 시각적 토큰을 언어 임베딩과 정렬하여 모델에 시각적 상식 및 로봇 관련 추론 능력을 부여합니다. RoboMamba에 SE(3) 포즈 예측 능력을 추가로 장착하기 위해, 간단한 정책 헤드를 사용한 효율적인 미세 조정 전략을 탐구합니다. RoboMamba가 충분한 추론 능력을 갖추면 최소한의 미세 조정 매개변수(모델의 0.1%)와 시간으로 조작 기술을 습득할 수 있음을 발견했습니다. 실험에서 RoboMamba는 일반 및 로봇 평가 벤치마크에서 뛰어난 추론 능력을 보여줍니다. 동시에, 우리 모델은 시뮬레이션 및 실제 실험 모두에서 인상적인 포즈 예측 결과를 보여주며, 기존 VLA 모델보다 3배 빠른 추론 속도를 달성합니다. 프로젝트 웹 페이지: https://sites.google.com/view/robomamba-web

## 핵심 내용
로봇 조작의 근본적인 목표는 모델이 시각적 장면을 이해하고 행동을 실행할 수 있도록 하는 것입니다. 기존의 로봇용 Vision-Language-Action (VLA) 모델은 다양한 기본 작업을 처리할 수 있지만, 여전히 두 가지 영역에서 어려움에 직면합니다: (1) 복잡한 작업을 해결하기 위한 추론 능력 부족, (2) VLA 모델 미세 조정 및 추론의 높은 계산 비용입니다. 최근 제안된 상태 공간 모델(SSM)인 Mamba는 선형 추론 복잡도로 중요한 시퀀스 모델링에서 유망한 능력을 보여줍니다. 이에 영감을 받아, 우리는 RoboMamba를 소개합니다. 이는 Mamba를 활용하여 효율적인 미세 조정 및 추론을 유지하면서 로봇 추론 및 행동 능력을 모두 제공하는 엔드투엔드 로봇 VLA 모델입니다. 구체적으로, 먼저 비전 인코더를 Mamba와 통합하고, 공동 훈련을 통해 시각적 토큰을 언어 임베딩과 정렬하여 모델에 시각적 상식 및 로봇 관련 추론 능력을 부여합니다. RoboMamba에 SE(3) 포즈 예측 능력을 추가로 장착하기 위해, 간단한 정책 헤드를 사용한 효율적인 미세 조정 전략을 탐구합니다. RoboMamba가 충분한 추론 능력을 갖추면 최소한의 미세 조정 매개변수(모델의 0.1%)와 시간으로 조작 기술을 습득할 수 있음을 발견했습니다. 실험에서 RoboMamba는 일반 및 로봇 평가 벤치마크에서 뛰어난 추론 능력을 보여줍니다. 동시에, 우리 모델은 시뮬레이션 및 실제 실험 모두에서 인상적인 포즈 예측 결과를 보여주며, 기존 VLA 모델보다 3배 빠른 추론 속도를 달성합니다. 프로젝트 웹 페이지: https://sites.google.com/view/robomamba-web

## 参考
- http://arxiv.org/abs/2406.04339v2
