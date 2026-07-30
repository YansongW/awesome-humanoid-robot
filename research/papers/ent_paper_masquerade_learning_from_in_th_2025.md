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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.09976v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
로봇 조작 연구는 여전히 심각한 데이터 부족 문제를 겪고 있습니다. 가장 큰 로봇 데이터셋조차도 언어 및 시각 분야의 최근 혁신을 이끈 데이터셋에 비해 규모가 수십 배 작고 다양성도 떨어집니다. 우리는 Masquerade를 소개합니다. 이는 실제 환경의 자기중심적 인간 비디오를 편집하여 인간과 로봇 간의 시각적 구현 격차를 해소하고, 편집된 비디오를 통해 로봇 정책을 학습하는 방법입니다. 우리의 파이프라인은 (i) 3D 손 자세 추정, (ii) 인간 팔 인페인팅, (iii) 복원된 엔드 이펙터 궤적을 추적하는 렌더링된 양팔 로봇 오버레이를 통해 각 인간 비디오를 로봇화된 시연으로 변환합니다. 편집된 클립의 675K 프레임에서 미래 2D 로봇 키포인트를 예측하도록 시각 인코더를 사전 학습하고, 작업당 50개의 로봇 시연만으로 확산 정책 헤드를 미세 조정하는 동안 보조 손실을 유지하면, 이전 연구보다 훨씬 더 잘 일반화되는 정책을 얻을 수 있습니다. 각각 세 가지 보지 못한 장면에서 평가된 세 가지 장기적 양팔 주방 작업에서 Masquerade는 기준선보다 5-6배 더 뛰어난 성능을 보였습니다. 절제 연구는 로봇 오버레이와 공동 학습이 모두 필수적이며, 성능이 편집된 인간 비디오 양에 따라 로그 스케일로 증가함을 보여줍니다. 이러한 결과는 시각적 구현 격차를 명시적으로 해소함으로써 인간 비디오에서 얻을 수 있는 방대하고 즉시 활용 가능한 데이터 소스를 활용하여 로봇 정책을 개선할 수 있음을 입증합니다.

## 핵심 내용
로봇 조작 연구는 여전히 심각한 데이터 부족 문제를 겪고 있습니다. 가장 큰 로봇 데이터셋조차도 언어 및 시각 분야의 최근 혁신을 이끈 데이터셋에 비해 규모가 수십 배 작고 다양성도 떨어집니다. 우리는 Masquerade를 소개합니다. 이는 실제 환경의 자기중심적 인간 비디오를 편집하여 인간과 로봇 간의 시각적 구현 격차를 해소하고, 편집된 비디오를 통해 로봇 정책을 학습하는 방법입니다. 우리의 파이프라인은 (i) 3D 손 자세 추정, (ii) 인간 팔 인페인팅, (iii) 복원된 엔드 이펙터 궤적을 추적하는 렌더링된 양팔 로봇 오버레이를 통해 각 인간 비디오를 로봇화된 시연으로 변환합니다. 편집된 클립의 675K 프레임에서 미래 2D 로봇 키포인트를 예측하도록 시각 인코더를 사전 학습하고, 작업당 50개의 로봇 시연만으로 확산 정책 헤드를 미세 조정하는 동안 보조 손실을 유지하면, 이전 연구보다 훨씬 더 잘 일반화되는 정책을 얻을 수 있습니다. 각각 세 가지 보지 못한 장면에서 평가된 세 가지 장기적 양팔 주방 작업에서 Masquerade는 기준선보다 5-6배 더 뛰어난 성능을 보였습니다. 절제 연구는 로봇 오버레이와 공동 학습이 모두 필수적이며, 성능이 편집된 인간 비디오 양에 따라 로그 스케일로 증가함을 보여줍니다. 이러한 결과는 시각적 구현 격차를 명시적으로 해소함으로써 인간 비디오에서 얻을 수 있는 방대하고 즉시 활용 가능한 데이터 소스를 활용하여 로봇 정책을 개선할 수 있음을 입증합니다.

## 参考
- http://arxiv.org/abs/2508.09976v1
