---
$id: ent_paper_masquerade_learning_from_in_th_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing'
  zh: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing'
  ko: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing'
summary:
  en: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing is a 2025 work on manipulation for humanoid robots.'
  zh: Masquerade 是 2025 年提出的一种利用自然场景人体视频编辑来训练人形机器人策略的方法。该方法通过将人类视频转化为机器人演示，弥合了人类与机器人之间的视觉具身差距，在仅使用少量机器人演示的情况下显著提升了策略的泛化能力。
  ko: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing is a 2025 work on manipulation for humanoid robots.'
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
- manipulation
- masquerade
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.09976v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (857 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing (arXiv)'
  url: https://arxiv.org/abs/2508.09976
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
机器人操作研究长期受限于数据稀缺问题，现有机器人数据集在规模和多样性上远不及语言和视觉领域。Masquerade 提出了一种数据编辑流水线，将自然场景中的第一人称人类视频转化为机器人演示：首先估计 3D 手部姿态，然后修复人类手臂区域，最后叠加渲染的双臂机器人模型以跟踪恢复的末端执行器轨迹。通过预训练视觉编码器预测未来 2D 机器人关键点（使用 675K 帧编辑视频），并在微调扩散策略头时保持该辅助损失（每任务仅需 50 个机器人演示），所得策略在三个未见场景的长时程双臂厨房任务中比基线方法提升 5-6 倍。

## 核心内容
### 方法架构
Masquerade 的核心流水线包含三个步骤：
- **3D 手部姿态估计**：从自然场景第一人称视频中恢复手部关键点轨迹。
- **手臂修复**：使用图像修复技术移除人类手臂区域，生成干净的背景。
- **机器人叠加**：根据手部轨迹渲染双臂机器人模型，覆盖在修复后的视频帧上，形成“机器人化”演示。

### 训练设置
- **预训练阶段**：在 675K 帧编辑视频上训练视觉编码器，任务为预测未来 2D 机器人关键点位置。
- **微调阶段**：在每任务仅 50 个真实机器人演示上微调扩散策略头，同时保留辅助关键点预测损失。
- **任务与场景**：三个长时程双臂厨房任务（如切菜、摆盘），每个任务在三个未见场景中评估。

### 关键结果
- **性能提升**：Masquerade 在三个任务上的成功率比基线方法（如直接使用人类视频或仅用机器人数据）高 5-6 倍。
- **消融实验**：
  - 机器人叠加层不可或缺：移除叠加层后性能下降 70%。
  - 联合训练（预训练+微调）比单独微调提升 3 倍。
  - 性能随编辑视频数量呈对数增长：从 100K 帧增至 675K 帧时，成功率提升约 2 倍。
- **结论**：通过显式弥合视觉具身差距，Masquerade 成功解锁了海量自然场景人类视频作为机器人策略训练数据源。

## Overview
Robot manipulation research still suffers from significant data scarcity: even the largest robot datasets are orders of magnitude smaller and less diverse than those that fueled recent breakthroughs in language and vision. We introduce Masquerade, a method that edits in-the-wild egocentric human videos to bridge the visual embodiment gap between humans and robots and then learns a robot policy with these edited videos. Our pipeline turns each human video into robotized demonstrations by (i) estimating 3-D hand poses, (ii) inpainting the human arms, and (iii) overlaying a rendered bimanual robot that tracks the recovered end-effector trajectories. Pre-training a visual encoder to predict future 2-D robot keypoints on 675K frames of these edited clips, and continuing that auxiliary loss while fine-tuning a diffusion policy head on only 50 robot demonstrations per task, yields policies that generalize significantly better than prior work. On three long-horizon, bimanual kitchen tasks evaluated in three unseen scenes each, Masquerade outperforms baselines by 5-6x. Ablations show that both the robot overlay and co-training are indispensable, and performance scales logarithmically with the amount of edited human video. These results demonstrate that explicitly closing the visual embodiment gap unlocks a vast, readily available source of data from human videos that can be used to improve robot policies.

## 参考
- http://arxiv.org/abs/2508.09976v1

## 개요
로봇 조작 연구는 오랫동안 데이터 부족 문제에 제약을 받아 왔으며, 기존 로봇 데이터셋은 규모와 다양성 면에서 언어 및 시각 분야에 크게 미치지 못한다. Masquerade는 자연 장면의 1인칭 인간 비디오를 로봇 시연으로 변환하는 데이터 편집 파이프라인을 제안한다: 먼저 3D 손姿态를 추정하고, 인간 팔 영역을 복원한 다음, 복구된 엔드 이펙터 궤적을 추적하도록 렌더링된 이중 팔 로봇 모델을 오버레이한다. 사전 훈련된 시각 인코더로 미래 2D 로봇 키포인트를 예측하고(675K 프레임 편집 비디오 사용), 미세 조정 확산 정책 헤드에서 이 보조 손실을 유지함으로써(작업당 50개의 로봇 시연만 필요), 얻어진 정책은 세 가지 미지의 장면에서의 장기 이중 팔 주방 작업에서 기준 방법보다 5-6배 향상된 성능을 보인다.

## 핵심 내용
### 방법 아키텍처
Masquerade의 핵심 파이프라인은 세 단계로 구성된다:
- **3D 손姿态 추정**: 자연 장면의 1인칭 비디오에서 손 키포인트 궤적을 복구한다.
- **팔 복원**: 이미지 인페인팅 기술을 사용하여 인간 팔 영역을 제거하고 깨끗한 배경을 생성한다.
- **로봇 오버레이**: 손 궤적에 따라 이중 팔 로봇 모델을 렌더링하여 복원된 비디오 프레임 위에 덮어 "로봇화된" 시연을 형성한다.

### 훈련 설정
- **사전 훈련 단계**: 675K 프레임 편집 비디오에서 시각 인코더를 훈련하며, 작업은 미래 2D 로봇 키포인트 위치를 예측하는 것이다.
- **미세 조정 단계**: 작업당 50개의 실제 로봇 시연만으로 확산 정책 헤드를 미세 조정하면서 보조 키포인트 예측 손실을 유지한다.
- **작업 및 장면**: 세 가지 장기 이중 팔 주방 작업(예: 채소 썰기, 플레이팅)이며, 각 작업은 세 가지 미지의 장면에서 평가된다.

### 주요 결과
- **성능 향상**: Masquerade는 세 가지 작업에서 기준 방법(예: 인간 비디오 직접 사용 또는 로봇 데이터만 사용)보다 성공률이 5-6배 높다.
- **절제 실험**:
  - 로봇 오버레이 레이어는 필수적이다: 오버레이를 제거하면 성능이 70% 하락한다.
  - 공동 훈련(사전 훈련+미세 조정)은 단독 미세 조정보다 3배 향상된다.
  - 성능은 편집 비디오 수에 따라 로그적으로 증가한다: 100K 프레임에서 675K 프레임으로 증가할 때 성공률이 약 2배 향상된다.
- **결론**: 시각적 구현 격차를 명시적으로 해소함으로써, Masquerade는 대규모 자연 장면 인간 비디오를 로봇 정책 훈련 데이터 소스로 성공적으로 활용할 수 있게 한다.
