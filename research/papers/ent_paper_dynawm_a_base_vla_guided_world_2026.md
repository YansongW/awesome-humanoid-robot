---
$id: ent_paper_dynawm_a_base_vla_guided_world_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
  zh: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
  ko: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
summary:
  en: 'arXiv:2607.02604v1 Announce Type: cross Abstract: Although vision-language-action (VLA) models have received widespread
    attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward
    or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may
    degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose
    DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA
    checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk
    produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from
    multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These
    feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object
    manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object
    manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the
    DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images.
    For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA,
    X-VLA, {\pi}0, and {\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06,
    35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%,
    while reducing success by 45.44% if action conditioning is removed.'
  zh: 'arXiv:2607.02604v1 Announce Type: cross Abstract: Although vision-language-action (VLA) models have received widespread
    attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward
    or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may
    degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose
    DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA
    checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk
    produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from
    multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These
    feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object
    manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object
    manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the
    DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images.
    For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA,
    X-VLA, {\pi}0, and {\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06,
    35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%,
    while reducing success by 45.44% if action conditioning is removed.'
  ko: 'arXiv:2607.02604v1 Announce Type: cross Abstract: Although vision-language-action (VLA) models have received widespread
    attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward
    or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may
    degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose
    DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA
    checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk
    produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from
    multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These
    feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object
    manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object
    manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the
    DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images.
    For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA,
    X-VLA, {\pi}0, and {\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06,
    35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%,
    while reducing success by 45.44% if action conditioning is removed.'
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
- dynawm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02604v1.
sources:
- id: src_001
  type: paper
  title: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.02604
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## 核心内容
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## 参考
- http://arxiv.org/abs/2607.02604v1

## Overview
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## Content
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## 개요
비전-언어-행동(VLA) 모델이 널리 주목받고 있지만, 동적 움직임 객체를 조작하는 데는 여전히 많은 과제가 남아 있습니다. 대부분의 기존 접근 방식에서는 엔드투엔드 순방향 또는 역방향 동역학 모델, 즉 월드 모델을 고성능 기본 VLA 아키텍처에 통합하는데, 이는 부적절한 파인튜닝으로 인해 사전 학습된 기본 VLA 모델의 성능을 저하시킬 수 있습니다. 본 논문에서는 다양한 파인튜닝 및 코스튜닝된 기본 VLA 체크포인트에 적응하여 움직이는 객체 조작을 수행하는 기본 VLA 기반 월드 파운데이션 모델인 DynaWM을 제안합니다. DynaWM은 Mamba-3 기반 행동 인코더를 사용하여 기본 VLA가 생성한 기본 행동 청크를 행동 조건화 표현으로 인코딩하고, V-JEPA 2.1 비전 인코더를 사용하여 다중 뷰 관찰 기록에서 특징을 추출하며, 고유수용성 상태 인코더를 사용하여 로봇 팔의 고유수용성 상태를 인코딩합니다. 이러한 특징 표현들은 공동으로 플로우 매칭 DiT를 조건화하여 움직이는 객체 조작을 위한 움직임 인식 행동 궤적을 재생성합니다. 체계적인 평가를 위해 속도 변화, 궤적 변화, 다중 객체 조작 등 여섯 가지 범주의 움직이는 객체 조작 작업을 포함하는 DynaGrasp-32 벤치마크와 32개 시나리오, 1,600개의 시연 궤적, 약 153만 개의 이미지로 구성된 DynaGrasp-1600 데이터셋을 구축했습니다. 파인튜닝된 기본 VLA 체크포인트의 경우, DynaWM은 SmolVLA, X-VLA, π0, π0.5 대비 각각 7.19%, 45.31%, 1.88%, 10.94%의 성능 향상을 달성했습니다. 코스튜닝된 기본 VLA 체크포인트의 경우, 성능이 각각 35.13%, 44.06%, 35.69%, 26.13% 향상되었습니다. 절제 실험 결과, 시각적 인코딩은 성공률을 27.50% 향상시키는 반면, 행동 조건화를 제거하면 성공률이 45.44% 감소하는 것으로 나타났습니다.

## 핵심 내용
비전-언어-행동(VLA) 모델이 널리 주목받고 있지만, 동적 움직임 객체를 조작하는 데는 여전히 많은 과제가 남아 있습니다. 대부분의 기존 접근 방식에서는 엔드투엔드 순방향 또는 역방향 동역학 모델, 즉 월드 모델을 고성능 기본 VLA 아키텍처에 통합하는데, 이는 부적절한 파인튜닝으로 인해 사전 학습된 기본 VLA 모델의 성능을 저하시킬 수 있습니다. 본 논문에서는 다양한 파인튜닝 및 코스튜닝된 기본 VLA 체크포인트에 적응하여 움직이는 객체 조작을 수행하는 기본 VLA 기반 월드 파운데이션 모델인 DynaWM을 제안합니다. DynaWM은 Mamba-3 기반 행동 인코더를 사용하여 기본 VLA가 생성한 기본 행동 청크를 행동 조건화 표현으로 인코딩하고, V-JEPA 2.1 비전 인코더를 사용하여 다중 뷰 관찰 기록에서 특징을 추출하며, 고유수용성 상태 인코더를 사용하여 로봇 팔의 고유수용성 상태를 인코딩합니다. 이러한 특징 표현들은 공동으로 플로우 매칭 DiT를 조건화하여 움직이는 객체 조작을 위한 움직임 인식 행동 궤적을 재생성합니다. 체계적인 평가를 위해 속도 변화, 궤적 변화, 다중 객체 조작 등 여섯 가지 범주의 움직이는 객체 조작 작업을 포함하는 DynaGrasp-32 벤치마크와 32개 시나리오, 1,600개의 시연 궤적, 약 153만 개의 이미지로 구성된 DynaGrasp-1600 데이터셋을 구축했습니다. 파인튜닝된 기본 VLA 체크포인트의 경우, DynaWM은 SmolVLA, X-VLA, π0, π0.5 대비 각각 7.19%, 45.31%, 1.88%, 10.94%의 성능 향상을 달성했습니다. 코스튜닝된 기본 VLA 체크포인트의 경우, 성능이 각각 35.13%, 44.06%, 35.69%, 26.13% 향상되었습니다. 절제 실험 결과, 시각적 인코딩은 성공률을 27.50% 향상시키는 반면, 행동 조건화를 제거하면 성공률이 45.44% 감소하는 것으로 나타났습니다.
