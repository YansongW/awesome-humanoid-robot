---
$id: ent_paper_li_mimicdreamer_aligning_human_an_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training'
  zh: MimicDreamer
  ko: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training'
summary:
  en: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
  zh: MimicDreamer 是由 GigaAI、CASIA、NJUST 和清华大学于 2025 年提出的视觉-语言-动作模型框架，旨在将低成本的人类演示视频转化为可扩展的机器人训练数据。其核心贡献在于通过视觉对齐、视角稳定和动作对齐三大模块，弥合人类与机器人演示之间的领域差异，使
    VLA 模型在仅使用合成数据训练后即可实现真实机器人的少样本执行，并将平均成功率提升 14.7%。
  ko: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
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
- mimicdreamer
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22199v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (896 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (arXiv)'
  url: https://arxiv.org/abs/2509.22199
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MimicDreamer source
  url: https://doi.org/10.48550/arXiv.2509.22199
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MimicDreamer 通过三个关键模块解决人类视频与机器人执行视频之间的领域差异：H2R Aligner 利用视频扩散模型将人类操作动作迁移至机器人场景，生成高保真机器人演示视频；EgoStabilizer 通过单应性变换稳定第一人称视角，并修复扭曲导致的遮挡与畸变；动作对齐模块将人类手部轨迹映射至机器人坐标系，结合约束逆运动学求解器生成低抖动、可执行的关节指令。实验表明，仅使用合成视频训练的 VLA 模型在真实机器人上展现出少样本执行能力，且相较于纯真实数据训练，在六项典型操作任务中平均成功率提升 14.7%。

## 核心内容
### 方法架构
MimicDreamer 包含三个核心对齐模块：
- **H2R Aligner（视觉对齐）**：基于视频扩散模型，从人类操作视频中提取运动信息，生成与机器人形态匹配的高保真演示视频，消除人类手部与机械臂之间的视觉差异。
- **EgoStabilizer（视角稳定）**：通过单应性变换将第一人称视频标准化，修复因视角变化产生的遮挡与畸变，确保视频帧的时空一致性。
- **动作对齐**：将人类手部轨迹映射至机器人坐标系，采用约束逆运动学求解器生成低抖动、高精度的关节指令，同时保持末端执行器的位姿追踪准确性。

### 实验设置与关键结果
- **训练数据**：仅使用 MimicDreamer 合成的人类到机器人视频训练 VLA 模型，未依赖真实机器人数据。
- **任务与性能**：在六项代表性操作任务（如抓取、放置、装配等）中，合成数据训练的模型实现真实机器人少样本执行。与纯真实数据训练的基线相比，平均成功率提升 14.7%。
- **可扩展性验证**：增加人类演示数据规模后，模型性能持续提升，表明该方法具备数据扩展潜力，可有效降低机器人数据采集成本。

### 结论
MimicDreamer 通过联合对齐视觉、视角与动作，将低成本人类演示转化为机器人可用的训练信号，显著缓解了 VLA 模型训练中的数据稀缺问题。其合成数据在真实场景中的有效性验证了跨域迁移的可行性，为大规模机器人策略学习提供了新路径。

## Overview
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## 参考
- http://arxiv.org/abs/2509.22199v2

## 개요
MimicDreamer는 인간 비디오와 로봇 실행 비디오 간의 도메인 차이를 해결하기 위해 세 가지 핵심 모듈을 사용합니다: H2R Aligner는 비디오 확산 모델을 활용하여 인간 조작 동작을 로봇 환경으로 전이하고, 고충실도 로봇 시연 비디오를 생성합니다; EgoStabilizer는 호모그래피 변환을 통해 1인칭 시점을 안정화하고, 왜곡으로 인한 폐색 및 변형을 복구합니다; 동작 정렬 모듈은 인간 손 궤적을 로봇 좌표계에 매핑하고, 제약 조건이 있는 역운동학 솔버를 결합하여 저지터링(low-jitter) 및 실행 가능한 관절 명령을 생성합니다. 실험 결과, 합성 비디오만으로 훈련된 VLA 모델은 실제 로봇에서 few-shot 실행 능력을 보여주었으며, 순수 실제 데이터 훈련과 비교하여 여섯 가지 대표적인 조작 작업에서 평균 성공률이 14.7% 향상되었습니다.

## 핵심 내용
### 방법 아키텍처
MimicDreamer는 세 가지 핵심 정렬 모듈을 포함합니다:
- **H2R Aligner(시각 정렬)**: 비디오 확산 모델을 기반으로 인간 조작 비디오에서 운동 정보를 추출하고, 로봇 형태와 일치하는 고충실도 시연 비디오를 생성하여 인간 손과 로봇 팔 사이의 시각적 차이를 제거합니다.
- **EgoStabilizer(시점 안정화)**: 호모그래피 변환을 통해 1인칭 비디오를 표준화하고, 시점 변화로 인한 폐색 및 변형을 복구하여 비디오 프레임의 시공간 일관성을 보장합니다.
- **동작 정렬**: 인간 손 궤적을 로봇 좌표계에 매핑하고, 제약 조건이 있는 역운동학 솔버를 사용하여 저지터링 및 고정밀 관절 명령을 생성하면서 엔드 이펙터의 자세 추적 정확도를 유지합니다.

### 실험 설정 및 주요 결과
- **훈련 데이터**: MimicDreamer가 합성한 인간-로봇 비디오만으로 VLA 모델을 훈련했으며, 실제 로봇 데이터에 의존하지 않았습니다.
- **작업 및 성능**: 여섯 가지 대표적인 조작 작업(예: 파지, 배치, 조립 등)에서 합성 데이터로 훈련된 모델은 실제 로봇에서 few-shot 실행을 구현했습니다. 순수 실제 데이터 훈련 기준선과 비교하여 평균 성공률이 14.7% 향상되었습니다.
- **확장성 검증**: 인간 시연 데이터 규모를 증가시킨 후 모델 성능이 지속적으로 향상되어, 이 방법이 데이터 확장 잠재력을 가지며 로봇 데이터 수집 비용을 효과적으로 절감할 수 있음을 보여줍니다.

### 결론
MimicDreamer는 시각, 시점, 동작을 공동으로 정렬하여 저비용 인간 시연을 로봇이 사용 가능한 훈련 신호로 변환하고, VLA 모델 훈련에서의 데이터 희소성 문제를 크게 완화합니다. 합성 데이터가 실제 환경에서 유효함을 검증함으로써 교차 도메인 전이의 가능성을 입증했으며, 대규모 로봇 정책 학습을 위한 새로운 경로를 제공합니다.
