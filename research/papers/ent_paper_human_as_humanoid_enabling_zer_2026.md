---
$id: ent_paper_human_as_humanoid_enabling_zer_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
  zh: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
  ko: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
summary:
  en: 'arXiv:2606.32009v1 Announce Type: new Abstract: Vision-language-action (VLA) models across robot embodiments require
    high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains
    difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric
    videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid,
    a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations
    usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label
    interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos
    to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion
    through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward
    Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human
    demonstrations from visual observations into executable observation--action supervision for the target humanoid. Experiments
    validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid
    yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and
    on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment
    without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.'
  zh: Human-as-Humanoid 是一个将人类演示转化为高自由度人形机器人可执行动作的框架，由研究团队基于 60-DoF 上体人形机器人 PrimeU 构建。其核心贡献在于通过同步 ego-exo 视频、分段逆运动学重定向和前向运动学感知监督，实现了零样本人形机器人学习，数据采集效率比遥操作提升
    4.8–7.2 倍。
  ko: 'arXiv:2606.32009v1 Announce Type: new Abstract: Vision-language-action (VLA) models across robot embodiments require
    high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains
    difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric
    videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid,
    a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations
    usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label
    interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos
    to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion
    through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward
    Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human
    demonstrations from visual observations into executable observation--action supervision for the target humanoid. Experiments
    validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid
    yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and
    on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment
    without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_as_humanoid
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.32009v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (849 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments'
  url: https://arxiv.org/abs/2606.32009
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Human-as-Humanoid 解决了高自由度人形机器人视觉-语言-动作（VLA）模型训练中数据稀缺的问题。该框架利用同步的自我中心与外中心视频，从人类演示中恢复运动，再通过分段逆运动学将人体运动重定向为 60-DoF 动作块，最后用前向运动学感知监督训练 VLA 模型，保留手腕和指尖的任务空间几何。实验在运动恢复、机器人动作空间和真实部署三个层面验证了转换链的有效性，后训练策略在多个下游任务中无需目标任务机器人演示即可泛化到真实部署。

## 核心内容
### 方法架构
- **框架核心**：Human-as-Humanoid 是一个端到端的人到人形机器人监督框架，通过联合对齐机器人本体、感知设置和动作标签接口，实现近实时的人为中心动作生成。
- **基础平台**：基于 PrimeU，一个 60-DoF 上体人形机器人，其设计已与人类对齐。
- **数据转换流程**：
  - 使用同步的 ego-exo 视频，将部署对齐的自我中心观测与外中心运动恢复配对。
  - 通过分段逆运动学（IK）将恢复的人体运动重定向为控制器对齐的 60-DoF 动作块。
  - 采用前向运动学（FK）感知监督训练 VLA 模型，以保留手腕和指尖的任务空间几何结构。

### 实验设置与关键数字
- **数据采集效率**：Human-as-Humanoid 在数据采集分析中，原始演示吞吐量比人形机器人遥操作提升 4.8–7.2 倍。
- **部署验证**：在运动恢复、机器人动作空间和真实机器人部署三个层面验证了转换链的有效性。
- **泛化能力**：在多个下游任务中，仅使用转换后的人类标签进行后训练的策略，无需目标任务机器人演示即可泛化到真实部署。

### 结论
Human-as-Humanoid 成功将大规模人类演示从视觉观测转换为可执行的观测-动作监督，用于目标人形机器人。该框架显著降低了高自由度人形机器人 VLA 训练的数据门槛，为零样本人形机器人学习提供了可行方案。

## Overview
Vision-language-action (VLA) models across robot embodiments require high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human demonstrations from visual observations into executable observation--action supervision for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.

## Overview
Vision-language-action (VLA) models across robot embodiments require high-quality observation–action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human demonstrations from visual observations into executable observation–action supervision for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid yields a 4.8–7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.

## Content
Vision-language-action (VLA) models across robot embodiments require high-quality observation–action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human demonstrations from visual observations into executable observation–action supervision for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid yields a 4.8–7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.

## 参考
- http://arxiv.org/abs/2606.32009v1

## 개요
Human-as-Humanoid는 고자유도 휴머노이드 로봇의 비전-언어-행동(VLA) 모델 훈련에서 데이터 부족 문제를 해결합니다. 이 프레임워크는 동기화된 자기중심 및 외부중심 비디오를 활용하여 인간 시연에서 동작을 복원하고, 분할 역기구학을 통해 인간 동작을 60-DoF 동작 블록으로 재지정한 후, 전방 기구학 인식 감독으로 VLA 모델을 훈련하여 손목과 손끝의 작업 공간 기하학을 보존합니다. 실험은 동작 복원, 로봇 동작 공간, 실제 배포의 세 가지 수준에서 변환 체인의 유효성을 검증했으며, 후훈련 전략은 여러 하위 작업에서 대상 작업 로봇 시연 없이도 실제 배포로 일반화됩니다.

## 핵심 내용
### 방법 아키텍처
- **프레임워크 핵심**: Human-as-Humanoid는 로봇 본체, 인식 설정, 동작 레이블 인터페이스를 공동 정렬하여 거의 실시간으로 인간 중심 동작 생성을 구현하는 종단 간 인간-휴머노이드 감독 프레임워크입니다.
- **기본 플랫폼**: 인간과 정렬되도록 설계된 60-DoF 상체 휴머노이드 로봇인 PrimeU 기반.
- **데이터 변환 흐름**:
  - 동기화된 ego-exo 비디오를 사용하여 배포 정렬된 자기중심 관측과 외부중심 동작 복원을 페어링합니다.
  - 분할 역기구학(IK)을 통해 복원된 인간 동작을 컨트롤러 정렬된 60-DoF 동작 블록으로 재지정합니다.
  - 전방 기구학(FK) 인식 감독으로 VLA 모델을 훈련하여 손목과 손끝의 작업 공간 기하학 구조를 보존합니다.

### 실험 설정 및 주요 수치
- **데이터 수집 효율성**: Human-as-Humanoid는 데이터 수집 분석에서 원시 시연 처리량이 휴머노이드 원격 조작보다 4.8–7.2배 향상되었습니다.
- **배포 검증**: 동작 복원, 로봇 동작 공간, 실제 로봇 배포의 세 가지 수준에서 변환 체인의 유효성을 검증했습니다.
- **일반화 능력**: 여러 하위 작업에서 변환된 인간 레이블만으로 후훈련된 전략은 대상 작업 로봇 시연 없이도 실제 배포로 일반화됩니다.

### 결론
Human-as-Humanoid는 대규모 인간 시연을 시각 관측에서 대상 휴머노이드 로봇용 실행 가능한 관측-행동 감독으로 성공적으로 변환합니다. 이 프레임워크는 고자유도 휴머노이드 VLA 훈련의 데이터 장벽을 크게 낮추며, 제로샷 휴머노이드 학습을 위한 실현 가능한 솔루션을 제공합니다.
