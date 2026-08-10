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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23931v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (943 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.23931v2

## 개요
AutoPrune은 기존 비전-언어 모델에서 고정된 프루닝 전략이 입력 다양성에 적응하지 못하는 문제를 해결하기 위해, 인간의 시각 인지에서 먼저 광범위하게 탐색한 후 집중하는 방식에서 영감을 받아 복잡도 적응형 프루닝 방법을 제안합니다. 이 방법은 시각 토큰과 텍스트 토큰 간의 상호 정보를 계산하여 이를 예산 제약이 있는 로지스틱 유지 곡선에 매핑하며, 각 곡선은 특정 작업 복잡도에 대응하고 계산 제약을 충족하도록 보장합니다. 표준 비전-언어 작업과 자율주행 비전-언어-행동 모델에 대한 실험에서 AutoPrune은 LLaVA-1.5-7B에서 PDrop 방법 대비 정확도 유지율이 9.1% 향상되었으며, 추가 학습 없이 플러그 앤 플레이가 가능합니다.

## 핵심 내용
### 방법 아키텍처
- **복잡도 정량화**: 시각 토큰과 텍스트 토큰 간의 상호 정보(Mutual Information)를 계산하여 각 샘플의 복잡도를 평가합니다. 상호 정보 값이 높을수록 시각 정보와 언어 작업의 연관성이 더 밀접함을 나타냅니다.
- **적응형 프루닝 전략**: 상호 정보 신호를 예산 제약이 있는 로지스틱 유지 곡선(Logistic Retention Curve)에 투영합니다. 각 곡선은 고유한 형태 파라미터로 정의되며, 서로 다른 작업 및 샘플의 복잡도에 대응합니다. 이 곡선은 프루닝 과정이 항상 사전 설정된 계산 예산 제약을 충족하도록 보장합니다.
- **학습 불필요 설계**: 전체 프레임워크는 추가 학습이나 미세 조정이 필요 없으며, 사전 학습된 모델에 직접 적용하여 플러그 앤 플레이(Plug-and-Play)가 가능합니다.

### 실험 설정
- **기반 모델**: LLaVA-1.5-7B를 주요 평가 모델로 사용
- **작업 유형**: 표준 비전-언어 작업(예: VQA, 이미지 캡셔닝) 및 자율주행 비전-언어-행동 모델(Vision-Language-Action Models)
- **비교 방법**: PDrop 등 최근 프루닝 방법과 비교

### 주요 결과
- **프루닝 효율성**: LLaVA-1.5-7B에서 89%의 시각 토큰을 제거하고 추론 FLOPs를 76.8% 감소
- **정확도 유지**: 모든 작업에서 평균 96.7%의 원본 정확도 유지
- **성능 향상**: PDrop 방법 대비 정확도 유지율 9.1% 향상
- **코드 공개**: https://github.com/AutoLab-SAI-SJTU/AutoPrune

### 결론
AutoPrune은 복잡도 적응형 프루닝 전략을 통해 고정된 프루닝 전략이 입력 다양성에 적응하지 못하는 문제를 효과적으로 해결하며, 높은 정확도를 유지하면서 계산 비용을 크게 줄여 비전-언어 모델의 효율적인 배포를 위한 새로운 패러다임을 제시합니다.
