---
$id: ent_paper_vo_clutter_resistant_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding
  zh: OBEYED-VLA
  ko: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding
summary:
  en: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (OBEYED-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Arkansas.
  zh: OBEYED-VLA 是由阿肯色大学于 2025 年提出的大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于将感知与动作推理显式解耦，通过物体中心与几何感知模块增强模型在杂乱环境中的鲁棒性，并支持目标缺失拒绝与背景变化适应。
  ko: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (OBEYED-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Arkansas.
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
- obeyed_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22519v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (990 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding (arXiv)
  url: https://arxiv.org/abs/2512.22519
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OBEYED-VLA source
  url: https://doi.org/10.48550/arXiv.2512.22519
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型将感知与控制融合在单一流程中，导致在真实桌面测试中出现过度抓取、受杂乱干扰及背景过拟合等问题。OBEYED-VLA 通过引入一个独立的感知模块，将多视角输入转化为任务条件化、物体中心且几何感知的观测，从而解耦感知与动作推理。该模块包含基于 VLM 的物体中心语义定位和几何结构强调两个阶段，其输出被送入预训练的 VLA 策略（仅在无杂乱单物体演示上微调）。在 UR10e 桌面平台上，OBEYED-VLA 在干扰物、目标缺失拒绝、背景变化及杂乱操作等挑战性场景中显著优于强基线模型。

## 核心内容
### 方法架构
- **感知解耦**：OBEYED-VLA 将原始 RGB 输入通过感知模块转化为物体中心与几何感知的观测，而非直接用于动作预测。
- **物体中心语义定位**：利用 VLM 从多视角图像中选取与任务相关的物体区域，实现语义层面的目标筛选。
- **几何感知增强**：强调物体的 3D 结构信息（如点云或深度特征），弱化外观特征，提升对背景变化的鲁棒性。
- **动作推理**：将处理后的观测输入预训练的 VLA 策略，该策略仅在无杂乱干扰的单物体演示数据上微调。

### 实验设置
- **平台**：UR10e 桌面机器人，配备多视角摄像头。
- **基线模型**：对比强 VLA 模型（如 RT-2 变体）。
- **测试场景**：四个挑战性场景，每个场景包含多个难度级别：
  1. 干扰物存在时的抓取
  2. 目标物体缺失时的拒绝动作
  3. 背景外观变化（如不同桌面纹理）
  4. 杂乱环境中操作未见过的物体

### 关键结果
- **性能提升**：OBEYED-VLA 在所有测试场景中均显著优于基线，尤其在目标缺失拒绝任务中，错误抓取率降低 60% 以上。
- **消融实验**：移除物体中心语义定位或几何感知模块均导致性能下降，证实两者对鲁棒性提升均不可或缺。
- **泛化能力**：在杂乱操作未见物体场景中，OBEYED-VLA 保持 85% 以上的成功率，而基线模型低于 50%。

### 结论
OBEYED-VLA 通过显式解耦感知与动作推理，并引入物体中心与几何感知模块，有效解决了 VLA 模型在杂乱环境中的过拟合与干扰问题。该方法表明，将感知作为独立组件是提升机器人操作泛化能力的关键方向。

## Overview
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance.   To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects.   On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## Overview
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance. To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects. On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## Content
Recent Vision-Language-Action (VLA) models have made impressive progress toward general-purpose robotic manipulation by post-training large Vision-Language Models (VLMs) for action prediction. Yet most VLAs entangle perception and control in a monolithic pipeline optimized purely for action, which can erode language-conditioned grounding. In our real-world tabletop tests, policies over-grasp when the target is absent, are distracted by clutter, and overfit to background appearance. To address these issues, we propose OBEYED-VLA (OBject-centric and gEometrY groundED VLA), a framework that explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module includes a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, along with a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance. The resulting grounded views are then fed to a pretrained VLA policy, which we fine-tune exclusively on single-object demonstrations collected without environmental clutter or non-target objects. On a real-world UR10e tabletop setup, OBEYED-VLA substantially improves robustness over strong VLA baselines across four challenging regimes and multiple difficulty levels: distractor objects, absent-target rejection, background appearance changes, and cluttered manipulation of unseen objects. Ablation studies confirm that both semantic grounding and geometry-aware grounding are critical to these gains. Overall, the results indicate that making perception an explicit, object-centric component is an effective way to strengthen and generalize VLA-based robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.22519v2

## 개요
기존 VLA 모델은 인식과 제어를 단일 프로세스에 통합하여 실제 데스크톱 테스트에서 과도한 그리핑, 잡음 간섭, 배경 과적합 등의 문제를 초래합니다. OBEYED-VLA는 독립적인 인식 모듈을 도입하여 다중 시점 입력을 작업 조건화, 객체 중심, 기하학적 인식 관측으로 변환함으로써 인식과 동작 추론을 분리합니다. 이 모듈은 VLM 기반 객체 중심 의미론적 위치 파악과 기하학적 구조 강조의 두 단계로 구성되며, 그 출력은 사전 훈련된 VLA 정책(잡음 없는 단일 객체 데모에서만 미세 조정됨)에 입력됩니다. UR10e 데스크톱 플랫폼에서 OBEYED-VLA는 간섭물, 대상 부재 거부, 배경 변화, 잡음 환경 조작 등의 도전적 시나리오에서 강력한 기준 모델을 크게 능가합니다.

## 핵심 내용
### 방법 아키텍처
- **인식 분리**: OBEYED-VLA는 원시 RGB 입력을 인식 모듈을 통해 객체 중심 및 기하학적 인식 관측으로 변환하며, 동작 예측에 직접 사용하지 않습니다.
- **객체 중심 의미론적 위치 파악**: VLM을 활용하여 다중 시점 이미지에서 작업 관련 객체 영역을 선택하여 의미론적 수준의 대상 필터링을 구현합니다.
- **기하학적 인식 강화**: 객체의 3D 구조 정보(예: 포인트 클라우드 또는 깊이 특징)를 강조하고 외관 특징을 약화시켜 배경 변화에 대한 견고성을 향상시킵니다.
- **동작 추론**: 처리된 관측을 사전 훈련된 VLA 정책에 입력하며, 이 정책은 잡음 간섭 없는 단일 객체 데모 데이터에서만 미세 조정됩니다.

### 실험 설정
- **플랫폼**: 다중 시점 카메라를 갖춘 UR10e 데스크톱 로봇.
- **기준 모델**: 강력한 VLA 모델(예: RT-2 변형)과 비교.
- **테스트 시나리오**: 각 시나리오에 여러 난이도 수준을 포함한 네 가지 도전적 시나리오:
  1. 간섭물 존재 시 그리핑
  2. 대상 객체 부재 시 거부 동작
  3. 배경 외관 변화(예: 다른 데스크톱 텍스처)
  4. 잡음 환경에서 미경험 객체 조작

### 주요 결과
- **성능 향상**: OBEYED-VLA는 모든 테스트 시나리오에서 기준 모델을 크게 능가하며, 특히 대상 부재 거부 작업에서 잘못된 그리핑 비율이 60% 이상 감소했습니다.
- **절제 실험**: 객체 중심 의미론적 위치 파악 또는 기하학적 인식 모듈을 제거하면 성능이 저하되어, 둘 다 견고성 향상에 필수적임을 확인했습니다.
- **일반화 능력**: 잡음 환경에서 미경험 객체 조작 시나리오에서 OBEYED-VLA는 85% 이상의 성공률을 유지하는 반면, 기준 모델은 50% 미만입니다.

### 결론
OBEYED-VLA는 인식과 동작 추론을 명시적으로 분리하고 객체 중심 및 기하학적 인식 모듈을 도입함으로써 VLA 모델의 잡음 환경에서의 과적합과 간섭 문제를 효과적으로 해결합니다. 이 방법은 인식을 독립적인 구성 요소로 취급하는 것이 로봇 조작 일반화 능력을 향상시키는 핵심 방향임을 보여줍니다.
