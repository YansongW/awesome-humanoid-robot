---
$id: ent_paper_nguyen_speech2grasp_data_efficient_tr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Speech2Grasp: Data-Efficient Transfer of Text-Conditioned Grasp Detection to Speech in Humanoid Robots'
  zh: 'Speech2Grasp: Data-Efficient Transfer of Text-Conditioned Grasp Detection to Speech in Humanoid Robots'
  ko: 'Speech2Grasp: Data-Efficient Transfer of Text-Conditioned Grasp Detection to Speech in Humanoid Robots'
summary:
  en: Humanoid robots increasingly require multi-modal understanding for natural interaction with humans. Despite the prominence
    of vision-language models, they generally assume textual rather than the more natural speech inputs. In this paper, we
    investigate whether a well-established text-conditioned model can be transferred to speech in a data-efficient manner.
    Using ALBEF as a case study, we ...
  zh: 本文提出 Speech2Grasp 框架，用于将文本条件抓取检测模型高效迁移至语音输入，以 ALBEF 为案例验证了轻量级 MLP 投影器的有效性。真实人形机器人实验表明，Speech2Grasp 优于级联 ASR 流水线，并降低了推理延迟。
  ko: Humanoid robots increasingly require multi-modal understanding for natural interaction with humans. Despite the prominence
    of vision-language models, they generally assume textual rather than the more natural speech inputs. In this paper, we
    investigate whether a well-established text-conditioned model can be transferred to speech in a data-efficient manner.
    Using ALBEF as a case study, we ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_robots
- speech_conditioned_grasping
- data_efficient_transfer
- albef
- mlp_projector
- multimodal_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-04'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-04). Bibliographic metadata from arXiv API (2607.26567);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.26567 Speech2Grasp: Data-Efficient Transfer of Text-Conditioned Grasp Detection to Speech in Humanoid
    Robots'
  url: https://arxiv.org/abs/2607.26567
  date: '2026-07-29'
  accessed_at: '2026-08-04'
---

## 概述

人形机器人需要多模态理解以实现自然交互，但现有视觉-语言模型通常假设文本输入而非更自然的语音。作者以 ALBEF 为案例进行诊断分析，发现轻量级 MLP 投影器能有效适配语音，同时保持语义判别力和鲁棒性。基于此，他们提出 Speech2Grasp 框架，实现数据高效的语音条件抓取检测迁移。真实世界人形机器人实验显示，Speech2Grasp 在性能上超越级联 ASR 流水线，并减少推理延迟，为扩展既有文本条件系统到语音提供了实用范式。

## 核心内容

### 问题背景
人形机器人日益需要多模态理解以支持与人类的自然交互。尽管视觉-语言模型（如 ALBEF）在文本条件任务中表现突出，但它们通常假设文本输入，而语音是更自然的交互方式。直接训练语音条件模型需要大量标注数据，成本高昂。

### 方法
- 以 ALBEF 为案例，进行诊断分析，评估不同适配架构（如轻量级 MLP 投影器）对语音输入的迁移效果。
- 分析表明，MLP 投影器能有效将语音特征映射到文本嵌入空间，同时保留语义判别力和对噪声的鲁棒性。
- 基于此，提出 Speech2Grasp 框架，采用数据高效策略，将文本条件抓取检测模型迁移至语音输入，无需大规模重新训练。

### 实验设置
- 在真实人形机器人平台上进行抓取检测实验。
- 对比 Speech2Grasp 与级联 ASR（自动语音识别）流水线（即先语音转文本，再执行文本条件抓取检测）的性能。

### 关键结果
- Speech2Grasp 在抓取检测任务上优于级联 ASR 流水线，表明直接语音适配优于中间文本转换。
- 同时，Speech2Grasp 降低了推理延迟，提升了实时交互能力。

### 结论
研究提出一种实用范式，可将成熟的文本条件系统高效扩展至语音输入，为人形机器人多模态交互提供了低成本、高性能的解决方案。未来工作可探索更复杂的语音条件任务和更多模型架构。

## Overview

Humanoid robots increasingly require multi-modal understanding for natural interaction with humans. Despite the prominence of vision-language models, they generally assume textual rather than the more natural speech inputs. In this paper, we investigate whether a well-established text-conditioned model can be transferred to speech in a data-efficient manner. Using ALBEF as a case study, we conduct diagnostic analyses showing that a lightweight MLP-based projector effectively adapts it to speech, while preserving semantic discrimination and robustness. Motivated by these findings, we introduce Speech2Grasp, a framework for data-efficient transfer of text-conditioned grasp detection to speech. Real-world humanoid robot experiments show that Speech2Grasp outperforms cascaded ASR-based pipeline, while reducing inference latency. Our findings suggest a practical paradigm for extending established text-conditioned systems to speech.

## 参考
- https://arxiv.org/abs/2607.26567
