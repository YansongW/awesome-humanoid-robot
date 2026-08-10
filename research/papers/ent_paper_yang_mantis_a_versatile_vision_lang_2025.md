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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16175v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (949 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.16175v2

## 개요
Mantis는 기존 VLA 모델이 고차원 시각 상태를 직접 예측할 때 발생하는 모델 용량 분산과 훈련 비용 과다 문제를 해결하기 위해 시각 예측 분리(DVF) 프레임워크를 도입했습니다. 이 프레임워크는 메타 쿼리와 확산 Transformer 헤드를 사용하여 시각 상태 예측을 백본 네트워크에서 분리하고, 잔차 연결을 통해 현재 시각 상태를 제공함으로써 메타 쿼리가 시각 궤적을 설명하는 잠재 행동을 자동으로 포착할 수 있게 합니다. 이러한 분리 설계는 VLA 백본의 부담을 줄여 언어 감독을 통해 이해 및 추론 능력을 유지할 수 있게 합니다. 사전 훈련 단계에서 Mantis는 인간 조작 비디오, 로봇 시연 및 이미지-텍스트 쌍을 사용했으며, 미세 조정 후 LIBERO 벤치마크에서 96.7%의 성공률을 달성하여 수렴 속도가 기준 방법보다 크게 우수했습니다. 실제 세계 실험에서 Mantis는 명령 따르기, 보지 못한 명령에 대한 일반화 및 추론 능력에서 선도적인 오픈소스 VLA 모델 π₀.₅보다 우수함을 보여주었습니다.

## 핵심 내용
### 방법
- **시각 예측 분리(DVF)**: 시각 상태 예측을 VLA 백본에서 분리하고 메타 쿼리와 확산 Transformer(DiT) 헤드를 사용하여 구현합니다. 잔차 연결을 통해 현재 시각 상태를 DiT에 입력하고, 간단한 다음 상태 예측 목표를 통해 메타 쿼리가 시각 궤적을 설명하는 잠재 행동을 자동으로 포착하여 명시적 행동 학습을 강화합니다.
- **언어 감독 유지**: 분리 설계는 VLA 백본의 부담을 줄여 언어 감독을 통해 이해 및 추론 능력을 유지할 수 있게 하며, 기존 방법이 언어 감독을 무시하여 발생하는 성능 저하를 방지합니다.

### 아키텍처
- **백본 네트워크**: 시각-언어 모델 기반으로 메타 쿼리 메커니즘과 DiT 헤드를 통합합니다.
- **훈련 목표**: 다음 상태 예측과 명시적 행동 예측을 결합하고 분리를 통해 정보 병목을 줄입니다.

### 실험 설정
- **사전 훈련 데이터**: 인간 조작 비디오, 로봇 시연 및 이미지-텍스트 쌍.
- **미세 조정 벤치마크**: LIBERO 벤치마크를 사용하여 조작 성공률을 평가합니다.
- **실제 세계 평가**: π₀.₅와 비교하여 명령 따르기, 일반화 및 추론 능력을 테스트합니다.

### 주요 수치
- **LIBERO 성공률**: 미세 조정 후 96.7%에 도달하여 모든 기준 방법을 능가합니다.
- **수렴 속도**: π₀.₅와 같은 기존 VLA 모델보다 크게 높습니다.
- **실제 세계 성능**: 명령 따르기, 보지 못한 명령에 대한 일반화 및 추론 능력에서 π₀.₅보다 전반적으로 우수합니다.

### 결론
Mantis는 시각 예측 분리 프레임워크를 통해 시각 상태 예측과 언어 감독을 효과적으로 균형 잡아 로봇 조작 작업에서 높은 성공률과 강력한 일반화 능력을 달성했습니다. 코드와 가중치는 오픈소스로 공개되어 커뮤니티의 추가 연구를 지원합니다.
