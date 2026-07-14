---
$id: ent_paper_liang_pixelvla_advancing_pixel_level_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model'
  zh: PixelVLA
  ko: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model'
summary:
  en: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (PixelVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Automation Science and Engineering, South China University of
    Technology, Shenyang Institute of Automation, Chinese Academy of Sciences, Mohamed bin Zayed University of Artificial
    Intelligence, Australian National University.'
  zh: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (PixelVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Automation Science and Engineering, South China University of
    Technology, Shenyang Institute of Automation, Chinese Academy of Sciences, Mohamed bin Zayed University of Artificial
    Intelligence, Australian National University.'
  ko: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (PixelVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Automation Science and Engineering, South China University of
    Technology, Shenyang Institute of Automation, Chinese Academy of Sciences, Mohamed bin Zayed University of Artificial
    Intelligence, Australian National University.'
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
- pixelvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01571v2.
sources:
- id: src_001
  type: paper
  title: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2511.01571
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PixelVLA source
  url: https://doi.org/10.48550/arXiv.2511.01571
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual promptaware encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-28.7% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments.

## 核心内容
Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual promptaware encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-28.7% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments.

## 参考
- http://arxiv.org/abs/2511.01571v2

