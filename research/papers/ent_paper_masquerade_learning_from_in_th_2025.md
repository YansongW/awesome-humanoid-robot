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
  zh: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing is a 2025 work on manipulation for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.09976v1.
sources:
- id: src_001
  type: paper
  title: 'Masquerade: Learning from In-the-wild Human Videos using Data-Editing (arXiv)'
  url: https://arxiv.org/abs/2508.09976
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot manipulation research still suffers from significant data scarcity: even the largest robot datasets are orders of magnitude smaller and less diverse than those that fueled recent breakthroughs in language and vision. We introduce Masquerade, a method that edits in-the-wild egocentric human videos to bridge the visual embodiment gap between humans and robots and then learns a robot policy with these edited videos. Our pipeline turns each human video into robotized demonstrations by (i) estimating 3-D hand poses, (ii) inpainting the human arms, and (iii) overlaying a rendered bimanual robot that tracks the recovered end-effector trajectories. Pre-training a visual encoder to predict future 2-D robot keypoints on 675K frames of these edited clips, and continuing that auxiliary loss while fine-tuning a diffusion policy head on only 50 robot demonstrations per task, yields policies that generalize significantly better than prior work. On three long-horizon, bimanual kitchen tasks evaluated in three unseen scenes each, Masquerade outperforms baselines by 5-6x. Ablations show that both the robot overlay and co-training are indispensable, and performance scales logarithmically with the amount of edited human video. These results demonstrate that explicitly closing the visual embodiment gap unlocks a vast, readily available source of data from human videos that can be used to improve robot policies.

## 核心内容
Robot manipulation research still suffers from significant data scarcity: even the largest robot datasets are orders of magnitude smaller and less diverse than those that fueled recent breakthroughs in language and vision. We introduce Masquerade, a method that edits in-the-wild egocentric human videos to bridge the visual embodiment gap between humans and robots and then learns a robot policy with these edited videos. Our pipeline turns each human video into robotized demonstrations by (i) estimating 3-D hand poses, (ii) inpainting the human arms, and (iii) overlaying a rendered bimanual robot that tracks the recovered end-effector trajectories. Pre-training a visual encoder to predict future 2-D robot keypoints on 675K frames of these edited clips, and continuing that auxiliary loss while fine-tuning a diffusion policy head on only 50 robot demonstrations per task, yields policies that generalize significantly better than prior work. On three long-horizon, bimanual kitchen tasks evaluated in three unseen scenes each, Masquerade outperforms baselines by 5-6x. Ablations show that both the robot overlay and co-training are indispensable, and performance scales logarithmically with the amount of edited human video. These results demonstrate that explicitly closing the visual embodiment gap unlocks a vast, readily available source of data from human videos that can be used to improve robot policies.

## 参考
- http://arxiv.org/abs/2508.09976v1

## Overview
Robot manipulation research still suffers from significant data scarcity: even the largest robot datasets are orders of magnitude smaller and less diverse than those that fueled recent breakthroughs in language and vision. We introduce Masquerade, a method that edits in-the-wild egocentric human videos to bridge the visual embodiment gap between humans and robots and then learns a robot policy with these edited videos. Our pipeline turns each human video into robotized demonstrations by (i) estimating 3-D hand poses, (ii) inpainting the human arms, and (iii) overlaying a rendered bimanual robot that tracks the recovered end-effector trajectories. Pre-training a visual encoder to predict future 2-D robot keypoints on 675K frames of these edited clips, and continuing that auxiliary loss while fine-tuning a diffusion policy head on only 50 robot demonstrations per task, yields policies that generalize significantly better than prior work. On three long-horizon, bimanual kitchen tasks evaluated in three unseen scenes each, Masquerade outperforms baselines by 5-6x. Ablations show that both the robot overlay and co-training are indispensable, and performance scales logarithmically with the amount of edited human video. These results demonstrate that explicitly closing the visual embodiment gap unlocks a vast, readily available source of data from human videos that can be used to improve robot policies.

## Content
Robot manipulation research still suffers from significant data scarcity: even the largest robot datasets are orders of magnitude smaller and less diverse than those that fueled recent breakthroughs in language and vision. We introduce Masquerade, a method that edits in-the-wild egocentric human videos to bridge the visual embodiment gap between humans and robots and then learns a robot policy with these edited videos. Our pipeline turns each human video into robotized demonstrations by (i) estimating 3-D hand poses, (ii) inpainting the human arms, and (iii) overlaying a rendered bimanual robot that tracks the recovered end-effector trajectories. Pre-training a visual encoder to predict future 2-D robot keypoints on 675K frames of these edited clips, and continuing that auxiliary loss while fine-tuning a diffusion policy head on only 50 robot demonstrations per task, yields policies that generalize significantly better than prior work. On three long-horizon, bimanual kitchen tasks evaluated in three unseen scenes each, Masquerade outperforms baselines by 5-6x. Ablations show that both the robot overlay and co-training are indispensable, and performance scales logarithmically with the amount of edited human video. These results demonstrate that explicitly closing the visual embodiment gap unlocks a vast, readily available source of data from human videos that can be used to improve robot policies.

## 개요
로봇 조작 연구는 여전히 심각한 데이터 부족 문제를 겪고 있습니다. 가장 큰 로봇 데이터셋조차도 언어 및 시각 분야의 최근 혁신을 이끈 데이터셋에 비해 규모가 수십 배 작고 다양성도 떨어집니다. 우리는 Masquerade를 소개합니다. 이는 실제 환경의 자기중심적 인간 비디오를 편집하여 인간과 로봇 간의 시각적 구현 격차를 해소하고, 편집된 비디오를 통해 로봇 정책을 학습하는 방법입니다. 우리의 파이프라인은 (i) 3D 손 자세 추정, (ii) 인간 팔 인페인팅, (iii) 복원된 엔드 이펙터 궤적을 추적하는 렌더링된 양팔 로봇 오버레이를 통해 각 인간 비디오를 로봇화된 시연으로 변환합니다. 편집된 클립의 675K 프레임에서 미래 2D 로봇 키포인트를 예측하도록 시각 인코더를 사전 학습하고, 작업당 50개의 로봇 시연만으로 확산 정책 헤드를 미세 조정하는 동안 보조 손실을 유지하면, 이전 연구보다 훨씬 더 잘 일반화되는 정책을 얻을 수 있습니다. 각각 세 가지 보지 못한 장면에서 평가된 세 가지 장기적 양팔 주방 작업에서 Masquerade는 기준선보다 5-6배 더 뛰어난 성능을 보였습니다. 절제 연구는 로봇 오버레이와 공동 학습이 모두 필수적이며, 성능이 편집된 인간 비디오 양에 따라 로그 스케일로 증가함을 보여줍니다. 이러한 결과는 시각적 구현 격차를 명시적으로 해소함으로써 인간 비디오에서 얻을 수 있는 방대하고 즉시 활용 가능한 데이터 소스를 활용하여 로봇 정책을 개선할 수 있음을 입증합니다.

## 핵심 내용
로봇 조작 연구는 여전히 심각한 데이터 부족 문제를 겪고 있습니다. 가장 큰 로봇 데이터셋조차도 언어 및 시각 분야의 최근 혁신을 이끈 데이터셋에 비해 규모가 수십 배 작고 다양성도 떨어집니다. 우리는 Masquerade를 소개합니다. 이는 실제 환경의 자기중심적 인간 비디오를 편집하여 인간과 로봇 간의 시각적 구현 격차를 해소하고, 편집된 비디오를 통해 로봇 정책을 학습하는 방법입니다. 우리의 파이프라인은 (i) 3D 손 자세 추정, (ii) 인간 팔 인페인팅, (iii) 복원된 엔드 이펙터 궤적을 추적하는 렌더링된 양팔 로봇 오버레이를 통해 각 인간 비디오를 로봇화된 시연으로 변환합니다. 편집된 클립의 675K 프레임에서 미래 2D 로봇 키포인트를 예측하도록 시각 인코더를 사전 학습하고, 작업당 50개의 로봇 시연만으로 확산 정책 헤드를 미세 조정하는 동안 보조 손실을 유지하면, 이전 연구보다 훨씬 더 잘 일반화되는 정책을 얻을 수 있습니다. 각각 세 가지 보지 못한 장면에서 평가된 세 가지 장기적 양팔 주방 작업에서 Masquerade는 기준선보다 5-6배 더 뛰어난 성능을 보였습니다. 절제 연구는 로봇 오버레이와 공동 학습이 모두 필수적이며, 성능이 편집된 인간 비디오 양에 따라 로그 스케일로 증가함을 보여줍니다. 이러한 결과는 시각적 구현 격차를 명시적으로 해소함으로써 인간 비디오에서 얻을 수 있는 방대하고 즉시 활용 가능한 데이터 소스를 활용하여 로봇 정책을 개선할 수 있음을 입증합니다.
