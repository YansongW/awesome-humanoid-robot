---
$id: ent_paper_physdiff_physics_guided_human_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
  zh: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
  ko: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
summary:
  en: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
  zh: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
  ko: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- physdiff
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.02500v3.
sources:
- id: src_001
  type: paper
  title: 'PhysDiff: Physics-Guided Human Motion Diffusion Model (arXiv)'
  url: https://arxiv.org/abs/2212.02500
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'PhysDiff: Physics-Guided Human Motion Diffusion Model project page'
  url: https://nvlabs.github.io/PhysDiff/
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## 核心内容
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## 参考
- http://arxiv.org/abs/2212.02500v3

## Overview
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## Content
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## 개요
Denoising diffusion 모델은 다양하고 사실적인 인간 동작을 생성하는 데 큰 잠재력을 가지고 있습니다. 그러나 기존의 동작 diffusion 모델은 확산 과정에서 물리 법칙을 대부분 무시하며, 종종 떠다니기, 발 미끄러짐, 지면 관통과 같은 두드러진 인공물이 있는 물리적으로 타당하지 않은 동작을 생성합니다. 이는 생성된 동작의 품질에 심각한 영향을 미치고 실제 응용을 제한합니다. 이 문제를 해결하기 위해, 우리는 확산 과정에 물리적 제약을 통합한 새로운 물리 유도 동작 diffusion 모델(PhysDiff)을 제시합니다. 구체적으로, 우리는 물리 시뮬레이터에서 동작 모방을 사용하여 확산 단계의 잡음 제거된 동작을 물리적으로 타당한 동작으로 투영하는 물리 기반 동작 투영 모듈을 제안합니다. 투영된 동작은 다음 확산 단계에서 잡음 제거 확산 과정을 안내하는 데 추가로 사용됩니다. 직관적으로, 우리 모델에서 물리 사용은 동작을 반복적으로 물리적으로 타당한 공간으로 끌어당기며, 이는 단순한 후처리로는 달성할 수 없습니다. 대규모 인간 동작 데이터셋에 대한 실험은 우리의 접근 방식이 최첨단 동작 품질을 달성하고 물리적 타당성을 크게 향상시킴을 보여줍니다(모든 데이터셋에서 >78%).

## 핵심 내용
Denoising diffusion 모델은 다양하고 사실적인 인간 동작을 생성하는 데 큰 잠재력을 가지고 있습니다. 그러나 기존의 동작 diffusion 모델은 확산 과정에서 물리 법칙을 대부분 무시하며, 종종 떠다니기, 발 미끄러짐, 지면 관통과 같은 두드러진 인공물이 있는 물리적으로 타당하지 않은 동작을 생성합니다. 이는 생성된 동작의 품질에 심각한 영향을 미치고 실제 응용을 제한합니다. 이 문제를 해결하기 위해, 우리는 확산 과정에 물리적 제약을 통합한 새로운 물리 유도 동작 diffusion 모델(PhysDiff)을 제시합니다. 구체적으로, 우리는 물리 시뮬레이터에서 동작 모방을 사용하여 확산 단계의 잡음 제거된 동작을 물리적으로 타당한 동작으로 투영하는 물리 기반 동작 투영 모듈을 제안합니다. 투영된 동작은 다음 확산 단계에서 잡음 제거 확산 과정을 안내하는 데 추가로 사용됩니다. 직관적으로, 우리 모델에서 물리 사용은 동작을 반복적으로 물리적으로 타당한 공간으로 끌어당기며, 이는 단순한 후처리로는 달성할 수 없습니다. 대규모 인간 동작 데이터셋에 대한 실험은 우리의 접근 방식이 최첨단 동작 품질을 달성하고 물리적 타당성을 크게 향상시킴을 보여줍니다(모든 데이터셋에서 >78%).
