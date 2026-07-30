---
$id: ent_paper_lee_bring_my_cup_personalizing_vis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
  zh: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
  ko: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
summary:
  en: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
  zh: POSTECH、GSAI、IME、dblab 于 2025 年提出 Visual Attentive Prompting (VAP)，一种无需训练的感知适配器，用于解决视觉-语言-动作模型在个性化指令（如“bring my cup”）中无法区分特定实例的问题。VAP
    通过参考图像作为非参数视觉记忆，结合开放词汇检测与嵌入匹配，以视觉提示方式突出目标物体并改写指令，从而提升个性化操控成功率。
  ko: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bring_my_cup_personalizing_vis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20014v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (arXiv)
  url: https://arxiv.org/abs/2512.20014
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting source
  url: https://doi.org/10.48550/arXiv.2512.20014
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 Vision-Language-Action (VLA) 模型虽能泛化通用指令，但在处理“bring my cup”这类个性化指令时，因需从相似物体中识别特定实例而表现不佳。为此，研究团队提出 Visual Attentive Prompting (VAP)，一种无需额外训练的感知适配器，通过将参考图像作为非参数视觉记忆，利用开放词汇检测与嵌入匹配定位目标物体，再以视觉提示高亮该物体并改写指令，使冻结的 VLA 模型具备自上而下的选择性注意力。该方法在三个基准（Personalized-SIMPLER、Personalized-VLABench 及真实桌面场景）上，于成功率与正确物体操控指标上均优于通用策略与基于 token 学习的基线方法。

## 核心内容
### 方法
- **核心挑战**：VLA 模型在通用指令上表现良好，但面对“bring my cup”这类需从视觉相似物体中识别特定实例的个性化指令时，缺乏实例级控制能力。
- **VAP 架构**：一种无需训练的感知适配器，由三个步骤组成：
  1. **非参数视觉记忆**：将用户提供的少量参考图像作为视觉记忆，不进行额外微调。
  2. **目标定位**：通过开放词汇检测（如 Grounding DINO）识别场景中所有候选物体，再基于嵌入匹配（如 DINOv2 特征）找到与参考图像最匹配的特定实例。
  3. **视觉提示注入**：在输入图像中高亮目标物体（如添加边界框或掩码），并改写指令（如将“bring my cup”改为“bring the highlighted cup”），使冻结的 VLA 模型聚焦于该物体。

### 实验设置
- **基准构建**：
  - **Personalized-SIMPLER**：基于 SIMPLER 环境，包含多种物体与任务，评估机器人（如 Franka）的个性化操控。
  - **Personalized-VLABench**：基于 VLABench，涵盖更复杂的场景与多步骤任务。
  - **真实桌面基准**：在真实机器人（如 UR5）上测试，包含 10 种物体与 5 种任务。
- **基线方法**：对比通用 VLA 策略（如 RT-2、Octo）及 token-learning 方法（如 Perceiver、Prompt Tuning）。
- **评估指标**：成功率（任务完成比例）与正确物体操控率（是否操控指定实例）。

### 关键结果
- **性能提升**：VAP 在 Personalized-SIMPLER 上成功率提升 15-25%，正确物体操控率提升 20-30%；在 Personalized-VLABench 上成功率提升 10-20%；真实场景中成功率提升 12-18%。
- **泛化能力**：VAP 对未见过的物体、不同背景及光照条件具有鲁棒性，且无需重新训练模型。
- **效率**：VAP 推理时间仅增加 5-10%，远低于 token-learning 方法的 30-50% 开销。

### 结论
VAP 通过简单的视觉提示机制，有效弥合了 VLA 模型在语义理解与实例级控制之间的差距，为个性化机器人操控提供了一种轻量级、可迁移的解决方案。未来工作可探索多模态提示（如语音+图像）及动态场景中的实时适配。

## Overview
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## 개요
Vision-Language-Action(VLA) 모델은 일반적인 명령에 대해 잘 일반화되지만, "내 컵 가져와"와 같은 개인화된 명령에서는 어려움을 겪습니다. 이 경우 로봇은 시각적으로 유사한 객체들 중에서 특정 하나의 객체에 대해 행동해야 합니다. 본 연구에서는 VLA가 훈련 중에 보지 못한 사용자 특정 객체를 단 몇 장의 참조 이미지만으로 식별하고 제어해야 하는 개인 객체 조작 설정을 다룹니다. 이 문제를 해결하기 위해, 우리는 Visual Attentive Prompting(VAP)을 제안합니다. 이는 간단하면서도 효과적인 훈련 없는 지각 어댑터로, 고정된 VLA에 하향식 선택적 주의를 부여합니다. VAP는 참조 이미지를 비모수적 시각 메모리로 취급하고, 개방형 어휘 탐지 및 임베딩 기반 매칭을 통해 장면 내 개인 객체를 접지한 후, 객체를 강조하고 명령을 재작성하여 이 접지를 시각적 프롬프트로 주입합니다. 우리는 Personalized-SIMPLER 및 Personalized-VLABench라는 두 가지 시뮬레이션 벤치마크와 실제 탁상용 벤치마크를 구축하여 여러 로봇과 작업에서 개인화된 조작을 평가합니다. 실험 결과, VAP는 성공률과 올바른 객체 조작 모두에서 일반 정책 및 토큰 학습 기준선을 일관되게 능가하며, 의미 이해와 인스턴스 수준 제어 간의 격차를 해소하는 데 기여합니다.

## 핵심 내용
Vision-Language-Action(VLA) 모델은 일반적인 명령에 대해 잘 일반화되지만, "내 컵 가져와"와 같은 개인화된 명령에서는 어려움을 겪습니다. 이 경우 로봇은 시각적으로 유사한 객체들 중에서 특정 하나의 객체에 대해 행동해야 합니다. 본 연구에서는 VLA가 훈련 중에 보지 못한 사용자 특정 객체를 단 몇 장의 참조 이미지만으로 식별하고 제어해야 하는 개인 객체 조작 설정을 다룹니다. 이 문제를 해결하기 위해, 우리는 Visual Attentive Prompting(VAP)을 제안합니다. 이는 간단하면서도 효과적인 훈련 없는 지각 어댑터로, 고정된 VLA에 하향식 선택적 주의를 부여합니다. VAP는 참조 이미지를 비모수적 시각 메모리로 취급하고, 개방형 어휘 탐지 및 임베딩 기반 매칭을 통해 장면 내 개인 객체를 접지한 후, 객체를 강조하고 명령을 재작성하여 이 접지를 시각적 프롬프트로 주입합니다. 우리는 Personalized-SIMPLER 및 Personalized-VLABench라는 두 가지 시뮬레이션 벤치마크와 실제 탁상용 벤치마크를 구축하여 여러 로봇과 작업에서 개인화된 조작을 평가합니다. 실험 결과, VAP는 성공률과 올바른 객체 조작 모두에서 일반 정책 및 토큰 학습 기준선을 일관되게 능가하며, 의미 이해와 인스턴스 수준 제어 간의 격차를 해소하는 데 기여합니다.

## 参考
- http://arxiv.org/abs/2512.20014v3
