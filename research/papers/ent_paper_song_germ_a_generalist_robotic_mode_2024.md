---
$id: ent_paper_song_germ_a_generalist_robotic_mode_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot'
  zh: GeRM
  ko: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot'
summary:
  en: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
  zh: GeRM 是西湖大学 MiLAB 团队在 IROS 2024 上提出的大型视觉-语言-动作模型，专为四足机器人多任务操作设计。其核心贡献在于利用离线强化学习优化数据利用策略，并引入 Mixture-of-Experts 结构提升推理速度与模型容量，同时发布了自动采集的
    QUARD-Auto 数据集。
  ko: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- germ
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.13358v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (922 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: GeRM source
  url: https://doi.org/10.1109/IROS58592.2024.10801816
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
GeRM 通过离线强化学习从演示数据和次优数据中学习，突破了仅依赖人类演示的限制。模型采用基于 transformer 的 VLA 网络处理多模态输入并输出动作，借助 Mixture-of-Experts 结构在保持高模型容量的同时实现更快推理，解决了强化学习参数受限的问题。实验表明，GeRM 在所有任务上均优于其他方法，并展现出涌现新技能的能力。此外，团队贡献了自动采集的 QUARD-Auto 数据集，以降低机器人数据收集成本并推动多任务学习发展。

## 核心内容
### 方法
- **数据利用策略**：采用离线强化学习，从演示数据和次优数据中学习，优化数据利用效率，避免仅依赖高质量人类演示的局限性。
- **网络架构**：基于 transformer 的 VLA（Vision-Language-Action）网络，处理多模态输入（视觉、语言）并直接输出动作指令。
- **Mixture-of-Experts 结构**：引入 MoE 机制，在保持高模型容量的同时实现更快推理速度，解决强化学习参数受限问题，提升多任务学习性能并控制计算成本。

### 实验设置
- **任务**：在四足机器人多任务操作场景中进行评估，涵盖多种复杂操作任务。
- **对比方法**：与现有多任务学习方法进行对比，GeRM 在所有任务上均取得最优性能。
- **数据集**：贡献 QUARD-Auto 数据集，通过自动采集方式生成，支持训练并推动四足机器人多任务学习研究。

### 关键结果
- **性能**：GeRM 在所有测试任务上超越其他方法，验证了其在训练和推理过程中的高效性。
- **涌现能力**：模型展现出学习新技能（emergent skills）的潜力，表明其泛化能力。
- **效率**：MoE 结构在提升模型容量的同时，未显著增加推理时间，实现了性能与计算成本的平衡。

### 结论
GeRM 提出了一种降低机器人数据收集成本的新范式，通过离线强化学习与 MoE 架构的结合，为多任务四足机器人学习提供了高效解决方案。项目详情与演示视频见：https://songwxuan.github.io/GeRM/ 。

## Overview
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## 参考
- http://arxiv.org/abs/2403.13358v2

## 개요
GeRM은 오프라인 강화 학습을 통해 시연 데이터와 준최적 데이터로부터 학습하여 인간 시연에만 의존하는 한계를 극복합니다. 모델은 transformer 기반 VLA 네트워크를 사용하여 다중 모달 입력을 처리하고 동작을 출력하며, Mixture-of-Experts 구조를 도입하여 높은 모델 용량을 유지하면서도 더 빠른 추론을 가능하게 하여 강화 학습의 매개변수 제한 문제를 해결합니다. 실험 결과, GeRM은 모든 작업에서 다른 방법보다 우수하며 새로운 기술을 창발하는 능력을 보여줍니다. 또한, 팀은 자동 수집된 QUARD-Auto 데이터셋을 기여하여 로봇 데이터 수집 비용을 줄이고 다중 작업 학습 발전을 촉진합니다.

## 핵심 내용
### 방법
- **데이터 활용 전략**: 오프라인 강화 학습을 사용하여 시연 데이터와 준최적 데이터로부터 학습하며, 데이터 활용 효율을 최적화하여 고품질 인간 시연에만 의존하는 한계를 피합니다.
- **네트워크 아키텍처**: transformer 기반 VLA(Vision-Language-Action) 네트워크로, 다중 모달 입력(시각, 언어)을 처리하고 동작 명령을 직접 출력합니다.
- **Mixture-of-Experts 구조**: MoE 메커니즘을 도입하여 높은 모델 용량을 유지하면서도 더 빠른 추론 속도를 구현하며, 강화 학습의 매개변수 제한 문제를 해결하고 다중 작업 학습 성능을 향상시키면서 계산 비용을 제어합니다.

### 실험 설정
- **작업**: 사족 로봇 다중 작업 조작 시나리오에서 평가하며, 다양한 복잡한 조작 작업을 포함합니다.
- **비교 방법**: 기존 다중 작업 학습 방법과 비교하여 GeRM은 모든 작업에서 최적의 성능을 달성합니다.
- **데이터셋**: QUARD-Auto 데이터셋을 기여하며, 자동 수집 방식을 통해 생성되어 훈련을 지원하고 사족 로봇 다중 작업 학습 연구를 촉진합니다.

### 주요 결과
- **성능**: GeRM은 모든 테스트 작업에서 다른 방법을 능가하며, 훈련 및 추론 과정에서의 효율성을 검증합니다.
- **창발 능력**: 모델은 새로운 기술(emergent skills)을 학습할 잠재력을 보여주며, 일반화 능력을 입증합니다.
- **효율성**: MoE 구조는 모델 용량을 향상시키면서도 추론 시간을 크게 증가시키지 않아 성능과 계산 비용 간의 균형을 달성합니다.

### 결론
GeRM은 로봇 데이터 수집 비용을 줄이는 새로운 패러다임을 제안하며, 오프라인 강화 학습과 MoE 아키텍처의 결합을 통해 다중 작업 사족 로봇 학습을 위한 효율적인 솔루션을 제공합니다. 프로젝트 세부 정보 및 데모 비디오는 다음에서 확인할 수 있습니다: https://songwxuan.github.io/GeRM/ .
