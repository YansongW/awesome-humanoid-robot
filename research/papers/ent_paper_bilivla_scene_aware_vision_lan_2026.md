---
$id: ent_paper_bilivla_scene_aware_vision_lan_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  zh: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  ko: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
summary:
  en: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
  zh: BiliVLA 是一个场景感知的视觉-语言-动作（VLA）框架，由研究团队提出，用于自主胆道内窥镜导航。其核心贡献在于将内窥镜导航建模为指令条件化的视觉运动学习问题，并通过结合语义定位、场景感知监督与两阶段训练范式（SFT + GRPO），在真实体模实验中实现了91.96%的动作精度和84.85%的整体成功率。
  ko: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- bilivla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.23531v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (776 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic
    Navigation (arXiv)'
  url: https://arxiv.org/abs/2606.23531
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
BiliVLA 针对 ERCP 手术中单目视野狭窄、镜面反射、组织接触等挑战，将胆道内窥镜导航转化为基于语言指令的视觉运动学习任务。该框架能同时预测目标类别、定位边界框和连续内窥镜的离散三自由度运动指令。通过引入场景感知监督提升语义一致性，并利用安全感知恢复监督在管壁接触时诱导保守后退行为。其两阶段训练策略结合了增强定位的监督微调（SFT）与 Group Relative Policy Optimization（GRPO），显著提升了闭环导航中的动作可靠性和决策一致性。

## 核心内容
### 方法架构
BiliVLA 将胆道内窥镜导航形式化为指令条件化的视觉运动学习问题。输入为内窥镜观测图像和阶段特定的语言指令，输出联合预测目标类别、定位边界框以及连续内窥镜的离散三自由度（3-DoF）运动指令。

### 关键组件
- **场景感知监督**：增强语义目标的一致性，使模型能更好地理解内窥镜视野中的解剖结构。
- **安全感知恢复监督**：在管腔壁接触时诱导保守后退行为，避免组织损伤。
- **两阶段训练范式**：
  1. **增强定位的监督微调（SFT）**：通过定位信息强化视觉与动作的映射。
  2. **Group Relative Policy Optimization（GRPO）**：基于奖励引导的策略优化，提升闭环导航中的动作可靠性和决策一致性。

### 实验设置与结果
在真实体模实验中，BiliVLA 在三个 ERCP 子任务上取得了最佳整体性能：
- **总 mIoU**：0.9625
- **整体动作精度**：91.96%
- **整体成功率（SR）**：84.85%

### 结论
结果表明，整合语义定位、场景感知学习和奖励引导优化能够强化感知-动作对齐，从而实现更鲁棒的自主胆道内窥镜导航。

## Overview
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## 参考
- http://arxiv.org/abs/2606.23531v3

## 개요
BiliVLA는 ERCP 수술 중 단일 시야의 협소함, 거울 반사, 조직 접촉 등의 도전 과제를 해결하기 위해 담도 내시경 내비게이션을 언어 기반의 시각 운동 학습 작업으로 변환합니다. 이 프레임워크는 목표 클래스 예측, 경계 상자 위치 파악, 연속 내시경의 이산 3자유도 운동 명령을 동시에 예측할 수 있습니다. 장면 인식 감독을 도입하여 의미적 일관성을 강화하고, 안전 인식 복구 감독을 활용하여 관벽 접촉 시 보수적인 후퇴 행동을 유도합니다. 두 단계 훈련 전략은 위치 파악 강화를 위한 지도 미세 조정(SFT)과 Group Relative Policy Optimization(GRPO)을 결합하여 폐쇄 루프 내비게이션에서 동작 신뢰성과 결정 일관성을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
BiliVLA는 담도 내시경 내비게이션을 명령 조건부 시각 운동 학습 문제로 공식화합니다. 입력은 내시경 관찰 이미지와 단계별 언어 명령이며, 출력은 목표 클래스, 경계 상자 위치, 연속 내시경의 이산 3자유도(3-DoF) 운동 명령을 공동으로 예측합니다.

### 주요 구성 요소
- **장면 인식 감독**: 의미적 목표의 일관성을 강화하여 모델이 내시경 시야 내 해부학적 구조를 더 잘 이해할 수 있게 합니다.
- **안전 인식 복구 감독**: 관강벽 접촉 시 보수적인 후퇴 행동을 유도하여 조직 손상을 방지합니다.
- **두 단계 훈련 패러다임**:
  1. **위치 파악 강화를 위한 지도 미세 조정(SFT)**: 위치 정보를 통해 시각-동작 매핑을 강화합니다.
  2. **Group Relative Policy Optimization(GRPO)**: 보상 기반 정책 최적화를 통해 폐쇄 루프 내비게이션에서 동작 신뢰성과 결정 일관성을 향상시킵니다.

### 실험 설정 및 결과
실제 팬텀 실험에서 BiliVLA는 세 가지 ERCP 하위 작업에서 최고의 전체 성능을 달성했습니다:
- **총 mIoU**: 0.9625
- **전체 동작 정확도**: 91.96%
- **전체 성공률(SR)**: 84.85%

### 결론
결과는 의미적 위치 파악, 장면 인식 학습, 보상 기반 최적화를 통합하면 인식-동작 정렬이 강화되어 더 견고한 자율 담도 내시경 내비게이션이 가능함을 보여줍니다.
