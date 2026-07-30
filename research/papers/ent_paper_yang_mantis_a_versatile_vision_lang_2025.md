---
$id: ent_paper_yang_mantis_a_versatile_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight'
  zh: Mantis
  ko: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight'
summary:
  en: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (Mantis), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, SII, Nanjing University of Posts and Telecommunications,
    Fudan University, Bosch.'
  zh: Mantis 是上海交通大学、SII、南京邮电大学、复旦大学和 Bosch 于 2025 年提出的视觉-语言-动作模型，专为机器人操作设计。其核心贡献是解耦视觉预见（DVF）机制，通过元查询和扩散 Transformer 头分离视觉状态预测，在
    LIBERO 基准上微调后达到 96.7% 的成功率，并在真实世界评估中超越 π₀.₅ 等模型。
  ko: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (Mantis), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, SII, Nanjing University of Posts and Telecommunications,
    Fudan University, Bosch.'
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
- mantis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16175v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (arXiv)'
  url: https://arxiv.org/abs/2511.16175
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Mantis source
  url: https://doi.org/10.48550/arXiv.2511.16175
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Mantis 通过解耦视觉预见（DVF）框架解决了现有 VLA 模型在直接预测高维视觉状态时导致的模型容量分散和训练成本过高问题。该框架利用元查询和扩散 Transformer 头将视觉状态预测从主干网络中分离，并通过残差连接提供当前视觉状态，使元查询能自动捕捉描述视觉轨迹的潜在动作。这种解耦设计减轻了 VLA 主干的负担，使其能通过语言监督保持理解和推理能力。在预训练阶段，Mantis 使用了人类操作视频、机器人演示和图像-文本对，微调后在 LIBERO 基准上达到 96.7% 的成功率，收敛速度显著优于基线方法。真实世界实验表明，Mantis 在指令跟随、泛化到未见指令和推理能力方面均优于领先的开源 VLA 模型 π₀.₅。

## 核心内容
### 方法
- **解耦视觉预见（DVF）**：将视觉状态预测从 VLA 主干中解耦，使用元查询和扩散 Transformer（DiT）头实现。通过残差连接将当前视觉状态输入 DiT，简单的下一状态预测目标使元查询自动捕捉描述视觉轨迹的潜在动作，从而增强显式动作学习。
- **语言监督保持**：解耦设计减少了 VLA 主干的负担，使其能通过语言监督维持理解和推理能力，避免现有方法因忽视语言监督导致的性能下降。

### 架构
- **主干网络**：基于视觉-语言模型，集成元查询机制和 DiT 头。
- **训练目标**：结合下一状态预测和显式动作预测，通过解耦减少信息瓶颈。

### 实验设置
- **预训练数据**：人类操作视频、机器人演示和图像-文本对。
- **微调基准**：LIBERO 基准，用于评估操作成功率。
- **真实世界评估**：与 π₀.₅ 对比，测试指令跟随、泛化和推理能力。

### 关键数字
- **LIBERO 成功率**：微调后达到 96.7%，超越所有基线方法。
- **收敛速度**：显著高于现有 VLA 模型，如 π₀.₅。
- **真实世界性能**：在指令跟随、泛化到未见指令和推理能力上全面优于 π₀.₅。

### 结论
Mantis 通过解耦视觉预见框架有效平衡了视觉状态预测和语言监督，在机器人操作任务中实现了高成功率和强泛化能力。代码和权重已开源，支持社区进一步研究。

## Overview
Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

## 개요
최근 Vision-Language-Action(VLA) 모델의 발전은 시각 신호가 희소한 행동 감독을 효과적으로 보완할 수 있음을 보여줍니다. 그러나 VLA가 고차원 시각 상태를 직접 예측하도록 하면 모델 용량이 분산되고 막대한 훈련 비용이 발생하는 반면, 시각 상태를 더 간결한 감독 신호로 압축하면 필연적으로 정보 병목 현상이 발생합니다. 또한 기존 방법들은 언어 감독을 간과하여 이해 및 추론 능력이 부족한 경우가 많습니다. 본 논문에서는 이러한 문제를 해결하기 위해 분리된 시각 예측(Disentangled Visual Foresight, DVF)을 특징으로 하는 새로운 프레임워크인 Mantis를 소개합니다. 구체적으로 Mantis는 메타 쿼리와 확산 트랜스포머(DiT) 헤드를 결합하여 시각 예측을 백본에서 분리합니다. 잔차 연결을 통해 DiT에 현재 시각 상태를 제공함으로써, 간단한 다음 상태 예측 목표를 통해 메타 쿼리가 시각 궤적을 설명하는 잠재 행동을 자동으로 포착하여 명시적 행동 학습을 촉진합니다. 이러한 분리는 VLA 백본의 부담을 줄여 언어 감독을 통해 이해 및 추론 능력을 유지할 수 있게 합니다. 실험적으로 인간 조작 비디오, 로봇 시연, 이미지-텍스트 쌍으로 사전 훈련된 Mantis는 미세 조정 후 LIBERO 벤치마크에서 96.7%의 성공률을 달성하며 강력한 기준 모델을 능가하고 높은 수렴 속도를 보여줍니다. 실제 환경 평가에서 Mantis는 선도적인 오픈소스 VLA 모델인 $π_{0.5}$를 능가하며, 특히 명령 수행 능력, 보지 못한 명령에 대한 일반화, 추론 능력에서 우수함을 입증했습니다. 코드와 가중치는 오픈소스 커뮤니티를 지원하기 위해 공개되었습니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델의 발전은 시각 신호가 희소한 행동 감독을 효과적으로 보완할 수 있음을 보여줍니다. 그러나 VLA가 고차원 시각 상태를 직접 예측하도록 하면 모델 용량이 분산되고 막대한 훈련 비용이 발생하는 반면, 시각 상태를 더 간결한 감독 신호로 압축하면 필연적으로 정보 병목 현상이 발생합니다. 또한 기존 방법들은 언어 감독을 간과하여 이해 및 추론 능력이 부족한 경우가 많습니다. 본 논문에서는 이러한 문제를 해결하기 위해 분리된 시각 예측(Disentangled Visual Foresight, DVF)을 특징으로 하는 새로운 프레임워크인 Mantis를 소개합니다. 구체적으로 Mantis는 메타 쿼리와 확산 트랜스포머(DiT) 헤드를 결합하여 시각 예측을 백본에서 분리합니다. 잔차 연결을 통해 DiT에 현재 시각 상태를 제공함으로써, 간단한 다음 상태 예측 목표를 통해 메타 쿼리가 시각 궤적을 설명하는 잠재 행동을 자동으로 포착하여 명시적 행동 학습을 촉진합니다. 이러한 분리는 VLA 백본의 부담을 줄여 언어 감독을 통해 이해 및 추론 능력을 유지할 수 있게 합니다. 실험적으로 인간 조작 비디오, 로봇 시연, 이미지-텍스트 쌍으로 사전 훈련된 Mantis는 미세 조정 후 LIBERO 벤치마크에서 96.7%의 성공률을 달성하며 강력한 기준 모델을 능가하고 높은 수렴 속도를 보여줍니다. 실제 환경 평가에서 Mantis는 선도적인 오픈소스 VLA 모델인 $π_{0.5}$를 능가하며, 특히 명령 수행 능력, 보지 못한 명령에 대한 일반화, 추론 능력에서 우수함을 입증했습니다. 코드와 가중치는 오픈소스 커뮤니티를 지원하기 위해 공개되었습니다.

## 参考
- http://arxiv.org/abs/2511.16175v2
