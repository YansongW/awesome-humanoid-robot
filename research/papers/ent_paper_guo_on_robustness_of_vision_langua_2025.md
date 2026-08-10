---
$id: ent_paper_guo_on_robustness_of_vision_langua_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
  zh: RobustVLA
  ko: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
summary:
  en: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
  zh: RobustVLA 是由香港中文大学、清华大学、北大-普赛特实验室、北京航空航天大学和北京大学联合提出的2025年大型视觉-语言-动作模型，旨在提升机器人操作任务中对多模态扰动的鲁棒性。其核心贡献在于首次系统评估了主流VLA模型在17种扰动下的表现，并提出了针对输入和输出鲁棒性的优化方法，在LIBERO基准上实现了12.6%的绝对性能提升。
  ko: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
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
- robotic_manipulation
- robustvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.00037v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (980 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (arXiv)
  url: https://arxiv.org/abs/2510.00037
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RobustVLA source
  url: https://doi.org/10.48550/arXiv.2510.00037
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型主要针对视觉扰动进行优化，忽略了动作、指令、环境和观测等多模态扰动的影响。RobustVLA通过评估发现动作模态最为脆弱，且现有视觉鲁棒方法无法推广到其他模态。为此，该模型采用离线鲁棒优化对抗最坏情况的动作噪声，并通过保持任务语义的一致性动作来增强输入鲁棒性。此外，RobustVLA将多扰动鲁棒性建模为多臂老虎机问题，利用上置信界算法自动识别最具破坏性的噪声。实验表明，在LIBERO基准上，RobustVLA在pi0和OpenVLA骨干网络上分别实现12.6%和10.4%的绝对增益，推理速度比现有方法快50.6倍，并在真实FR5机器人上以25个演示样本超越pi0达65.6%的成功率。

## 核心内容
### 方法架构
RobustVLA 针对VLA模型的输入和输出两个层面设计鲁棒性增强策略：
- **输出鲁棒性**：通过离线鲁棒优化，对抗最坏情况的动作噪声，该噪声最大化流匹配目标中的不匹配度。这相当于同时实现对抗训练、标签平滑和异常值惩罚。
- **输入鲁棒性**：强制模型在保留任务语义的输入变化下产生一致的动作输出，从而增强对指令、环境和观测扰动的抵抗能力。
- **多扰动处理**：将鲁棒性优化形式化为多臂老虎机问题，采用上置信界算法自动识别当前最有害的噪声类型，实现自适应防御。

### 实验设置与关键数字
- **基准测试**：在LIBERO基准上评估17种扰动，覆盖动作、指令、环境和观测四个模态。
- **性能提升**：
  - 在pi0骨干网络上实现12.6%的绝对增益，在OpenVLA骨干网络上实现10.4%的绝对增益。
  - 推理速度比现有视觉鲁棒方法BYOVLA快50.6倍（BYOVLA需依赖外部大语言模型）。
  - 在混合扰动场景下仍保持10.4%的增益。
- **真实机器人实验**：在FR5机器人上，面对四种多模态扰动：
  - 仅用25个演示样本时，RobustVLA成功率比pi0高65.6%。
  - 即使使用充足演示数据，仍比pi0高30%的成功率。

### 结论
RobustVLA通过联合优化输入和输出鲁棒性，并引入自适应多扰动识别机制，显著提升了VLA模型在真实世界部署中的可靠性。其高效推理和低数据依赖特性为机器人操作任务提供了实用解决方案。代码和演示视频已开源。

## Overview
In Vision-Language-Actionf(VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## Overview
In Vision-Language-Action (VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## Content
In Vision-Language-Action (VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## 参考
- http://arxiv.org/abs/2510.00037v4

## 개요
기존 VLA 모델은 주로 시각적 교란에 최적화되어 있으며, 행동, 명령, 환경, 관측 등 다중 모달 교란의 영향을 무시합니다. RobustVLA는 평가를 통해 행동 모달이 가장 취약하며, 기존의 시각적 강건성 방법이 다른 모달로 일반화될 수 없음을 발견했습니다. 이를 위해 해당 모델은 오프라인 강건 최적화를 통해 최악의 행동 노이즈에 대응하고, 작업 의미를 유지하는 일관된 행동을 통해 입력 강건성을 강화합니다. 또한 RobustVLA는 다중 교란 강건성을 다중 팔 밴딧 문제로 모델링하고, 상위 신뢰 경계 알고리즘을 활용해 가장 파괴적인 노이즈를 자동으로 식별합니다. 실험 결과, LIBERO 벤치마크에서 RobustVLA는 pi0 및 OpenVLA 백본 네트워크에서 각각 12.6% 및 10.4%의 절대적 향상을 달성했으며, 추론 속도는 기존 방법보다 50.6배 빠르고, 실제 FR5 로봇에서 25개의 데모 샘플로 pi0를 65.6%의 성공률로 능가했습니다.

## 핵심 내용
### 방법 아키텍처
RobustVLA는 VLA 모델의 입력 및 출력 두 계층에 대해 강건성 강화 전략을 설계합니다:
- **출력 강건성**: 오프라인 강건 최적화를 통해 최악의 행동 노이즈에 대응하며, 이 노이즈는 흐름 매칭 목표에서 불일치도를 최대화합니다. 이는 적대적 훈련, 라벨 평활화, 이상치 페널티를 동시에 구현하는 것과 같습니다.
- **입력 강건성**: 작업 의미를 유지하는 입력 변화 하에서 모델이 일관된 행동 출력을 생성하도록 강제하여, 명령, 환경, 관측 교란에 대한 저항력을 강화합니다.
- **다중 교란 처리**: 강건성 최적화를 다중 팔 밴딧 문제로 형식화하고, 상위 신뢰 경계 알고리즘을 사용해 현재 가장 유해한 노이즈 유형을 자동으로 식별하여 적응형 방어를 구현합니다.

### 실험 설정 및 주요 수치
- **벤치마크 테스트**: LIBERO 벤치마크에서 17가지 교란을 평가하며, 행동, 명령, 환경, 관측 네 가지 모달을 포괄합니다.
- **성능 향상**:
  - pi0 백본 네트워크에서 12.6%의 절대적 향상, OpenVLA 백본 네트워크에서 10.4%의 절대적 향상 달성.
  - 추론 속도는 기존 시각적 강건성 방법 BYOVLA보다 50.6배 빠름 (BYOVLA는 외부 대형 언어 모델에 의존).
  - 혼합 교란 시나리오에서도 10.4%의 향상을 유지.
- **실제 로봇 실험**: FR5 로봇에서 네 가지 다중 모달 교란에 직면:
  - 25개의 데모 샘플만 사용했을 때, RobustVLA의 성공률은 pi0보다 65.6% 높음.
  - 충분한 데모 데이터를 사용해도 pi0보다 30% 높은 성공률을 유지.

### 결론
RobustVLA는 입력 및 출력 강건성을 공동 최적화하고 적응형 다중 교란 식별 메커니즘을 도입하여, VLA 모델의 실제 세계 배포에서의 신뢰성을 크게 향상시켰습니다. 효율적인 추론과 낮은 데이터 의존성 특성은 로봇 조작 작업에 실용적인 솔루션을 제공합니다. 코드와 데모 비디오는 오픈소스로 공개되었습니다.
