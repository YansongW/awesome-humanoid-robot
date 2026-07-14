---
$id: ent_paper_scalemogen_autoregressive_next_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
  zh: 用下一尺度自回归把文本生成的人体动作做成由粗到细
  ko: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
summary:
  en: We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional
    autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine
    process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing
    granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural
    integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly
    preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale
    up the tokenizer vocabulary to preserve motion details and stabilize optim
  zh: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation is a paper on 人体动作 for humanoid robotics.
    用下一尺度自回归把文本生成的人体动作做成由粗到细.'
  ko: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation is a paper on 人体动作 for humanoid robotics.
    用下一尺度自回归把文本生成的人体动作做成由粗到细.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_motion
- humanoid
- motion_synthesis
- scalemogen
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: ScaleMoGen: Autoregressive
    Next-Scale Prediction for Human Motion Generation.'
sources:
- id: src_001
  type: website
  title: 'ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## 核心内容
We present ScaleMoGen, a scale-wise autoregressive framework for text-driven human motion generation. Unlike conventional autoregressive approaches that rely on standard next-token prediction, ScaleMoGen frames motion generation as a coarse-to-fine process. We quantize 3D motions into compositional discrete tokens across multiple skeletal-emporal scales of increasing granularity, learning to generate motion by autoregressively predicting next-scale token maps. To maintain structural integrity, our motion tokenizers and quantizers are explicitly designed so that discrete tokens at every scale strictly preserve the skeletal hierarchy. Additionally, we employ bitwise quantization and prediction, which efficiently scale up the tokenizer vocabulary to preserve motion details and stabilize optimization. Extensive experiments demonstrate that ScaleMoGen achieves state-of-the-art performance, establishing an FID of 0.030 (vs. 0.045 for MoMask) on HumanML3D and a CLIP Score of 0.693 (vs. 0.685 for MoMask++) on the SnapMoGen dataset. Furthermore, we demonstrate that our skeletal-temporal multi-scale representation naturally facilitates training-free, text-guided motion editing.

## 参考
- Semantic Scholar search: ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation

