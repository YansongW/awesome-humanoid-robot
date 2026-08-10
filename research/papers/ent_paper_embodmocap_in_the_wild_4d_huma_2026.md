---
$id: ent_paper_embodmocap_in_the_wild_4d_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents'
  zh: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents'
  ko: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents'
summary:
  en: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents is a 2026 work on human motion analysis and
    synthesis for humanoid robots.'
  zh: EmbodMocap 是 2026 年提出的一种便携式、低成本的人体运动数据采集方案，由研究团队使用两台移动 iPhone 实现。其核心贡献在于通过联合标定双 RGB-D 序列，在统一的度量世界坐标系中同时重建人体与场景，无需固定相机或穿戴设备，从而支持大规模野外场景下的具身智能研究。
  ko: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents is a 2026 work on human motion analysis and
    synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodmocap
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23205v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (723 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents (arXiv)'
  url: https://arxiv.org/abs/2602.23205
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有的人体运动捕捉系统通常依赖昂贵的演播室设备和可穿戴装置，限制了在真实世界中大规模采集场景关联的人体运动数据。EmbodMocap 提出使用两台移动 iPhone 进行数据采集，通过联合标定双 RGB-D 序列，在统一的度量世界坐标系中同时重建人体与场景。该方法无需静态相机或标记点，即可在日常环境中实现度量尺度和场景一致的运动捕捉。实验表明，双视角设置能有效缓解深度模糊问题，在配准和重建性能上优于单 iPhone 或单目模型。基于采集的数据，该方法赋能了三个具身 AI 任务：单目人体-场景重建、基于物理的角色动画以及机器人运动控制。

## 核心内容
### 方法概述
EmbodMocap 的核心思想是使用两台移动 iPhone 进行双 RGB-D 序列的联合标定，从而在统一的度量世界坐标系中重建人体与场景。该方法无需固定相机或穿戴设备，即可在自然环境中实现度量尺度和场景一致的运动捕捉。

### 实验设置与关键结果
- **深度模糊缓解**：与光学捕捉真值对比，双视角设置显著缓解了深度模糊问题，在配准和重建性能上优于单 iPhone 或单目模型。
- **任务一：单目人体-场景重建**：基于采集数据微调前馈模型，输出度量尺度、世界空间对齐的人体与场景。
- **任务二：基于物理的角色动画**：数据可用于扩展人-物交互技能和场景感知运动跟踪。
- **任务三：机器人运动控制**：通过 sim-to-real 强化学习训练人形机器人，使其能够复现视频中的人体运动。

### 结论
实验验证了 EmbodMocap 管线的有效性，表明其能够为具身 AI 研究提供大规模、场景关联的人体运动数据，推动相关领域的发展。

## Overview
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iphone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## Overview
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iPhone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## Content
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iPhone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## 参考
- http://arxiv.org/abs/2602.23205v2

## 개요
기존의 인간 동작 캡처 시스템은 일반적으로 고가의 스튜디오 장비와 웨어러블 장치에 의존하여, 실제 세계에서 대규모로 장면과 연관된 인간 동작 데이터를 수집하는 데 제약이 있었습니다. EmbodMocap은 두 대의 이동형 iPhone을 사용하여 데이터를 수집하고, 이중 RGB-D 시퀀스를 공동 보정하여 통일된 미터법 세계 좌표계에서 인간과 장면을 동시에 재구성하는 방법을 제안합니다. 이 방법은 고정 카메라나 마커 없이도 일상 환경에서 미터법 스케일과 장면 일관성을 갖춘 동작 캡처를 가능하게 합니다. 실험 결과, 이중 시점 설정이 깊이 모호성 문제를 효과적으로 완화하여 단일 iPhone 또는 단안 모델보다 정합 및 재구성 성능이 우수함을 보여줍니다. 수집된 데이터를 기반으로, 이 방법은 단안 인간-장면 재구성, 물리 기반 캐릭터 애니메이션, 로봇 동작 제어라는 세 가지 구현 AI 작업을 지원합니다.

## 핵심 내용
### 방법 개요
EmbodMocap의 핵심 아이디어는 두 대의 이동형 iPhone을 사용하여 이중 RGB-D 시퀀스를 공동 보정함으로써, 통일된 미터법 세계 좌표계에서 인간과 장면을 재구성하는 것입니다. 이 방법은 고정 카메라나 웨어러블 장치 없이도 자연 환경에서 미터법 스케일과 장면 일관성을 갖춘 동작 캡처를 가능하게 합니다.

### 실험 설정 및 주요 결과
- **깊이 모호성 완화**: 광학 캡처 진실값과 비교하여, 이중 시점 설정이 깊이 모호성 문제를 크게 완화하여 단일 iPhone 또는 단안 모델보다 정합 및 재구성 성능이 우수함을 보여줍니다.
- **작업 1: 단안 인간-장면 재구성**: 수집된 데이터를 기반으로 피드포워드 모델을 미세 조정하여, 미터법 스케일과 세계 공간 정렬된 인간과 장면을 출력합니다.
- **작업 2: 물리 기반 캐릭터 애니메이션**: 데이터는 인간-객체 상호작용 기술 확장 및 장면 인식 동작 추적에 사용될 수 있습니다.
- **작업 3: 로봇 동작 제어**: sim-to-real 강화 학습을 통해 휴머노이드 로봇을 훈련하여 비디오 속 인간 동작을 재현할 수 있게 합니다.

### 결론
실험은 EmbodMocap 파이프라인의 효율성을 검증하여, 구현 AI 연구를 위한 대규모의 장면 연관 인간 동작 데이터를 제공할 수 있음을 보여주며, 관련 분야의 발전을 촉진합니다.
