---
$id: ent_paper_yu_forcevla_enhancing_vla_models_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation'
  zh: ForceVLA
  ko: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation'
summary:
  en: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
  zh: ForceVLA 是上海人工智能实验室、新加坡国立大学等机构联合提出的2025年大型视觉-语言-动作模型，专为解决机器人接触丰富操作中的力控难题。其核心创新在于引入力感知混合专家融合模块 FVLMoE，将实时六轴力反馈作为独立模态集成到
    VLA 系统中，在插拔等任务上成功率最高达80%，平均提升23.2%。
  ko: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- forcevla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.22159v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (724 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (arXiv)'
  url: https://arxiv.org/abs/2505.22159
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ForceVLA source
  url: https://doi.org/10.48550/arXiv.2505.22159
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型虽能利用预训练的视觉和语言表征实现通用操作，但在视觉遮挡或动态不确定的接触丰富任务中，因缺乏力控能力而表现不佳。ForceVLA 通过将外部力传感提升为第一类模态，提出力感知混合专家融合模块 FVLMoE，在动作解码阶段动态整合预训练的视觉-语言嵌入与实时六轴力反馈，实现跨模态专家路由。配合新发布的 ForceVLA-Data 数据集（包含五种接触丰富任务的同步视觉、本体感知和力-力矩信号），模型在强基线 pi_0 基础上平均任务成功率提升23.2%，插拔任务达80%。

## 核心内容
### 方法架构
- **核心问题**：VLA 模型在接触丰富操作中缺乏力控能力，尤其在视觉遮挡或动态不确定性下难以实现精细控制。
- **ForceVLA 框架**：端到端操作框架，将外部力传感作为第一类模态集成到 VLA 系统。
- **FVLMoE 模块**：力感知混合专家融合模块，在动作解码阶段动态整合预训练视觉-语言嵌入与实时六轴力反馈，通过上下文感知路由激活不同模态专家，增强对细微接触动力学的适应能力。

### 数据集
- **ForceVLA-Data**：新发布数据集，包含五种接触丰富操作任务的同步视觉、本体感知和力-力矩信号，为训练和评估提供多模态数据基础。

### 实验设置与结果
- **基线对比**：以 pi_0 为强基线，ForceVLA 在平均任务成功率上提升 23.2%。
- **关键任务表现**：在插拔任务中成功率最高达 80%，验证了力模态对灵巧操作的重要性。
- **结论**：多模态集成对物理智能机器人控制至关重要，ForceVLA 为该领域设立了新基准。代码与数据将开源。

## Overview
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 参考
- http://arxiv.org/abs/2505.22159v3

## 개요
기존 VLA 모델은 사전 학습된 시각 및 언어 표현을 활용하여 일반적인 조작을 수행할 수 있지만, 시각적 폐색이나 동적 불확실성이 있는 접촉이 많은 작업에서는 힘 제어 능력이 부족하여 성능이 저조합니다. ForceVLA는 외부 힘 센싱을 제1의 양식으로 승격시키고, 힘 인식 혼합 전문가 융합 모듈인 FVLMoE를 제안하여, 동작 디코딩 단계에서 사전 학습된 시각-언어 임베딩과 실시간 6축 힘 피드백을 동적으로 통합하여 교차 양식 전문가 라우팅을 구현합니다. 새로 공개된 ForceVLA-Data 데이터셋(다섯 가지 접촉이 많은 작업의 동기화된 시각, 고유 수용, 힘-토크 신호 포함)과 함께, 모델은 강력한 기준선 pi_0 대비 평균 작업 성공률이 23.2% 향상되었으며, 삽입-추출 작업에서는 80%에 도달했습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 문제**: VLA 모델은 접촉이 많은 조작에서 힘 제어 능력이 부족하며, 특히 시각적 폐색이나 동적 불확실성 하에서 정밀 제어를 구현하기 어렵습니다.
- **ForceVLA 프레임워크**: 외부 힘 센싱을 제1의 양식으로 VLA 시스템에 통합하는 종단 간 조작 프레임워크입니다.
- **FVLMoE 모듈**: 힘 인식 혼합 전문가 융합 모듈로, 동작 디코딩 단계에서 사전 학습된 시각-언어 임베딩과 실시간 6축 힘 피드백을 동적으로 통합하고, 컨텍스트 인식 라우팅을 통해 다양한 양식 전문가를 활성화하여 미세한 접촉 역학에 대한 적응 능력을 강화합니다.

### 데이터셋
- **ForceVLA-Data**: 새로 공개된 데이터셋으로, 다섯 가지 접촉이 많은 조작 작업의 동기화된 시각, 고유 수용, 힘-토크 신호를 포함하며, 훈련 및 평가를 위한 다중 양식 데이터 기반을 제공합니다.

### 실험 설정 및 결과
- **기준선 비교**: pi_0을 강력한 기준선으로 하여, ForceVLA는 평균 작업 성공률이 23.2% 향상되었습니다.
- **주요 작업 성능**: 삽입-추출 작업에서 성공률이 최대 80%에 도달하여, 힘 양식이 정밀 조작에 중요함을 검증했습니다.
- **결론**: 다중 양식 통합은 물리적 지능 로봇 제어에 필수적이며, ForceVLA는 이 분야에 새로운 기준을 세웠습니다. 코드와 데이터는 오픈소스로 공개될 예정입니다.
