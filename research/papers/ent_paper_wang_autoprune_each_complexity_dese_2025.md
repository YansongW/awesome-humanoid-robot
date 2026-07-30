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
  zh: AutoPrune 是由中国科学院自动化研究所、上海交通大学等机构于2025年提出的免训练、即插即用的视觉语言动作模型剪枝框架。其核心贡献在于提出复杂度自适应剪枝策略，通过互信息量化与逻辑保留曲线为不同样本和任务动态调整剪枝策略，在LLaVA-1.5-7B上实现89%视觉token剪除、76.8%
    FLOPs降低，同时保持96.7%原始精度。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23931v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
AutoPrune 针对现有视觉语言模型中固定剪枝策略无法适应输入多样性的问题，受人类视觉认知中先广泛探索后聚焦的启发，提出复杂度自适应剪枝方法。该方法通过计算视觉与文本token间的互信息，将其映射到受预算约束的逻辑保留曲线，每条曲线对应特定任务复杂度并确保满足计算约束。在标准视觉语言任务和自动驾驶视觉语言动作模型上的实验表明，AutoPrune 在LLaVA-1.5-7B上相比PDrop方法提升9.1%精度保持率，且无需额外训练即可即插即用。

## 核心内容
### 方法架构
- **复杂度量化**：通过计算视觉token与文本token之间的互信息（Mutual Information）来评估每个样本的复杂度，互信息值越高表示视觉信息与语言任务关联越紧密。
- **自适应剪枝策略**：将互信息信号投影到预算约束的逻辑保留曲线（Logistic Retention Curve）上，每条曲线由独特的形状参数定义，对应不同任务和样本的复杂度。该曲线确保剪枝过程始终满足预设的计算预算约束。
- **免训练设计**：整个框架无需额外训练或微调，可直接应用于预训练模型，实现即插即用（Plug-and-Play）。

### 实验设置
- **基础模型**：LLaVA-1.5-7B作为主要评估模型
- **任务类型**：标准视觉语言任务（如VQA、图像描述）和自动驾驶视觉语言动作模型（Vision-Language-Action Models）
- **对比方法**：与PDrop等近期剪枝方法进行对比

### 关键结果
- **剪枝效率**：在LLaVA-1.5-7B上剪除89%的视觉token，推理FLOPs降低76.8%
- **精度保持**：在所有任务上平均保持96.7%的原始精度
- **性能提升**：相比PDrop方法，精度保持率提升9.1%
- **代码开源**：https://github.com/AutoLab-SAI-SJTU/AutoPrune

### 结论
AutoPrune 通过复杂度自适应剪枝策略，有效解决了固定剪枝策略无法适应输入多样性的问题，在保持高精度的同时显著降低计算开销，为视觉语言模型的高效部署提供了新范式。

## Overview
The established redundancy in visual tokens within large vision-language models allows pruning to effectively reduce their substantial computational demands. Previous methods typically employ heuristic layer-specific pruning strategies where, although the number of tokens removed may differ across decoder layers, the overall pruning schedule is fixed and applied uniformly to all input samples and tasks, failing to align token elimination with the model's holistic reasoning trajectory. Cognitive science indicates that human visual processing often begins with broad exploration to accumulate evidence before narrowing focus as the target becomes distinct. Our experiments reveal an analogous pattern in these models. This observation suggests that neither a fixed pruning schedule nor a heuristic layer-wise strategy can optimally accommodate the diverse complexities inherent in different inputs. To overcome this limitation, we introduce Complexity-Adaptive Pruning (AutoPrune), a training-free, plug-and-play framework that tailors pruning policies to varying sample and task complexities. Specifically, AutoPrune quantifies the mutual information between visual and textual tokens, then projects this signal to a budget-constrained logistic retention curve. Each such logistic curve, defined by its unique shape, corresponds to the specific complexity of different tasks and can guarantee adherence to predefined computational constraints. We evaluate AutoPrune on standard vision-language tasks and on Vision-Language-Action models for autonomous driving. Notably, when applied to LLaVA-1.5-7B, our method prunes 89% of visual tokens and reduces inference FLOPs by 76.8% while retaining 96.7% of the original accuracy averaged over all tasks. This corresponds to a 9.1% improvement over the recent work PDrop, demonstrating the effectiveness. Code is available at https://github.com/AutoLab-SAI-SJTU/AutoPrune.

## 개요
대규모 비전-언어 모델에서 시각적 토큰의 확립된 중복성은 프루닝을 통해 상당한 계산 요구를 효과적으로 줄일 수 있게 합니다. 기존 방법들은 일반적으로 휴리스틱한 계층별 프루닝 전략을 사용하는데, 디코더 계층 간에 제거되는 토큰 수는 다를 수 있지만 전체 프루닝 일정은 고정되어 모든 입력 샘플과 작업에 균일하게 적용되어, 토큰 제거를 모델의 전체 추론 궤적과 정렬하지 못합니다. 인지 과학은 인간의 시각 처리 과정이 종종 광범위한 탐색으로 시작하여 증거를 축적한 후 목표가 뚜렷해짐에 따라 초점을 좁힌다고 나타냅니다. 우리의 실험은 이러한 모델에서 유사한 패턴을 보여줍니다. 이 관찰은 고정된 프루닝 일정이나 휴리스틱한 계층별 전략 모두 다양한 입력에 내재된 다양한 복잡성을 최적으로 수용할 수 없음을 시사합니다. 이러한 한계를 극복하기 위해, 우리는 Complexity-Adaptive Pruning (AutoPrune)을 소개합니다. 이는 훈련이 필요 없고 플러그 앤 플레이 방식의 프레임워크로, 다양한 샘플 및 작업 복잡성에 맞춰 프루닝 정책을 조정합니다. 구체적으로, AutoPrune은 시각적 토큰과 텍스트 토큰 간의 상호 정보를 정량화한 후, 이 신호를 예산이 제한된 로지스틱 유지 곡선에 투영합니다. 고유한 형태로 정의된 각 로지스틱 곡선은 다양한 작업의 특정 복잡성에 대응하며, 미리 정의된 계산 제약 조건을 준수함을 보장할 수 있습니다. 우리는 AutoPrune을 표준 비전-언어 작업과 자율 주행을 위한 비전-언어-행동 모델에서 평가합니다. 특히, LLaVA-1.5-7B에 적용했을 때, 우리의 방법은 시각적 토큰의 89%를 프루닝하고 추론 FLOPs를 76.8% 줄이면서 모든 작업 평균 원래 정확도의 96.7%를 유지합니다. 이는 최근 연구인 PDrop보다 9.1% 향상된 것으로, 효과성을 입증합니다. 코드는 https://github.com/AutoLab-SAI-SJTU/AutoPrune에서 확인할 수 있습니다.

## 핵심 내용
대규모 비전-언어 모델에서 시각적 토큰의 확립된 중복성은 프루닝을 통해 상당한 계산 요구를 효과적으로 줄일 수 있게 합니다. 기존 방법들은 일반적으로 휴리스틱한 계층별 프루닝 전략을 사용하는데, 디코더 계층 간에 제거되는 토큰 수는 다를 수 있지만 전체 프루닝 일정은 고정되어 모든 입력 샘플과 작업에 균일하게 적용되어, 토큰 제거를 모델의 전체 추론 궤적과 정렬하지 못합니다. 인지 과학은 인간의 시각 처리 과정이 종종 광범위한 탐색으로 시작하여 증거를 축적한 후 목표가 뚜렷해짐에 따라 초점을 좁힌다고 나타냅니다. 우리의 실험은 이러한 모델에서 유사한 패턴을 보여줍니다. 이 관찰은 고정된 프루닝 일정이나 휴리스틱한 계층별 전략 모두 다양한 입력에 내재된 다양한 복잡성을 최적으로 수용할 수 없음을 시사합니다. 이러한 한계를 극복하기 위해, 우리는 Complexity-Adaptive Pruning (AutoPrune)을 소개합니다. 이는 훈련이 필요 없고 플러그 앤 플레이 방식의 프레임워크로, 다양한 샘플 및 작업 복잡성에 맞춰 프루닝 정책을 조정합니다. 구체적으로, AutoPrune은 시각적 토큰과 텍스트 토큰 간의 상호 정보를 정량화한 후, 이 신호를 예산이 제한된 로지스틱 유지 곡선에 투영합니다. 고유한 형태로 정의된 각 로지스틱 곡선은 다양한 작업의 특정 복잡성에 대응하며, 미리 정의된 계산 제약 조건을 준수함을 보장할 수 있습니다. 우리는 AutoPrune을 표준 비전-언어 작업과 자율 주행을 위한 비전-언어-행동 모델에서 평가합니다. 특히, LLaVA-1.5-7B에 적용했을 때, 우리의 방법은 시각적 토큰의 89%를 프루닝하고 추론 FLOPs를 76.8% 줄이면서 모든 작업 평균 원래 정확도의 96.7%를 유지합니다. 이는 최근 연구인 PDrop보다 9.1% 향상된 것으로, 효과성을 입증합니다. 코드는 https://github.com/AutoLab-SAI-SJTU/AutoPrune에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2509.23931v2
