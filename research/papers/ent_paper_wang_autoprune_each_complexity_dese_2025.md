---
$id: ent_paper_wang_autoprune_each_complexity_dese_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoPrune: Each Complexity Deserves a Pruning Policy'
  zh: AutoPrune
  ko: 'AutoPrune: Each Complexity Deserves a Pruning Policy'
summary:
  en: 'AutoPrune: Each Complexity Deserves a Pruning Policy (AutoPrune), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), CASIA,
    School of Artificial Intelligence, University of Chinese Academy of Sciences, AutoLab, Shanghai Jiao Tong University,
    Anyverse Intelligence, Beijing Key Laboratory of Super Intelligent Security of Multi-Modal Information, School of Information
    Science and Technology, ShanghaiTech University, KargoBot.'
  zh: 'AutoPrune: Each Complexity Deserves a Pruning Policy (AutoPrune), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), CASIA,
    School of Artificial Intelligence, University of Chinese Academy of Sciences, AutoLab, Shanghai Jiao Tong University,
    Anyverse Intelligence, Beijing Key Laboratory of Super Intelligent Security of Multi-Modal Information, School of Information
    Science and Technology, ShanghaiTech University, KargoBot.'
  ko: 'AutoPrune: Each Complexity Deserves a Pruning Policy (AutoPrune), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by State Key Laboratory of Multimodal Artificial Intelligence Systems (MAIS), CASIA,
    School of Artificial Intelligence, University of Chinese Academy of Sciences, AutoLab, Shanghai Jiao Tong University,
    Anyverse Intelligence, Beijing Key Laboratory of Super Intelligent Security of Multi-Modal Information, School of Information
    Science and Technology, ShanghaiTech University, KargoBot.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autoprune
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23931v2.
sources:
- id: src_001
  type: paper
  title: 'AutoPrune: Each Complexity Deserves a Pruning Policy (arXiv)'
  url: https://arxiv.org/abs/2509.23931
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AutoPrune source
  url: https://doi.org/10.48550/arXiv.2509.23931
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The established redundancy in visual tokens within large vision-language models allows pruning to effectively reduce their substantial computational demands. Previous methods typically employ heuristic layer-specific pruning strategies where, although the number of tokens removed may differ across decoder layers, the overall pruning schedule is fixed and applied uniformly to all input samples and tasks, failing to align token elimination with the model's holistic reasoning trajectory. Cognitive science indicates that human visual processing often begins with broad exploration to accumulate evidence before narrowing focus as the target becomes distinct. Our experiments reveal an analogous pattern in these models. This observation suggests that neither a fixed pruning schedule nor a heuristic layer-wise strategy can optimally accommodate the diverse complexities inherent in different inputs. To overcome this limitation, we introduce Complexity-Adaptive Pruning (AutoPrune), a training-free, plug-and-play framework that tailors pruning policies to varying sample and task complexities. Specifically, AutoPrune quantifies the mutual information between visual and textual tokens, then projects this signal to a budget-constrained logistic retention curve. Each such logistic curve, defined by its unique shape, corresponds to the specific complexity of different tasks and can guarantee adherence to predefined computational constraints. We evaluate AutoPrune on standard vision-language tasks and on Vision-Language-Action models for autonomous driving. Notably, when applied to LLaVA-1.5-7B, our method prunes 89% of visual tokens and reduces inference FLOPs by 76.8% while retaining 96.7% of the original accuracy averaged over all tasks. This corresponds to a 9.1% improvement over the recent work PDrop, demonstrating the effectiveness. Code is available at https://github.com/AutoLab-SAI-SJTU/AutoPrune.

## 核心内容
The established redundancy in visual tokens within large vision-language models allows pruning to effectively reduce their substantial computational demands. Previous methods typically employ heuristic layer-specific pruning strategies where, although the number of tokens removed may differ across decoder layers, the overall pruning schedule is fixed and applied uniformly to all input samples and tasks, failing to align token elimination with the model's holistic reasoning trajectory. Cognitive science indicates that human visual processing often begins with broad exploration to accumulate evidence before narrowing focus as the target becomes distinct. Our experiments reveal an analogous pattern in these models. This observation suggests that neither a fixed pruning schedule nor a heuristic layer-wise strategy can optimally accommodate the diverse complexities inherent in different inputs. To overcome this limitation, we introduce Complexity-Adaptive Pruning (AutoPrune), a training-free, plug-and-play framework that tailors pruning policies to varying sample and task complexities. Specifically, AutoPrune quantifies the mutual information between visual and textual tokens, then projects this signal to a budget-constrained logistic retention curve. Each such logistic curve, defined by its unique shape, corresponds to the specific complexity of different tasks and can guarantee adherence to predefined computational constraints. We evaluate AutoPrune on standard vision-language tasks and on Vision-Language-Action models for autonomous driving. Notably, when applied to LLaVA-1.5-7B, our method prunes 89% of visual tokens and reduces inference FLOPs by 76.8% while retaining 96.7% of the original accuracy averaged over all tasks. This corresponds to a 9.1% improvement over the recent work PDrop, demonstrating the effectiveness. Code is available at https://github.com/AutoLab-SAI-SJTU/AutoPrune.

## 参考
- http://arxiv.org/abs/2509.23931v2

