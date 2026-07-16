---
$id: ent_paper_stagecraft_execution_aware_mit_2065
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
  zh: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
  ko: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
summary:
  en: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
  zh: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
  ko: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
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
- stagecraft
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.20659v2.
sources:
- id: src_001
  type: paper
  title: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models (arXiv)'
  url: https://arxiv.org/abs/2603.20659
  date: '2065'
  accessed_at: '2026-07-08'
---
## 概述
Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/ .

## 核心内容
Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/ .

## 参考
- http://arxiv.org/abs/2603.20659v2

## Overview
Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/ .

## Content
Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/ .

## 개요
텍스트 및 이미지 데이터에 대한 대규모 사전 학습과 다양한 로봇 시연을 통해 Vision Language Action 모델(VLA)이 새로운 작업, 객체 및 장면에 일반화될 수 있게 되었습니다. 그러나 이러한 모델은 로봇 작업 공간에서의 방해 요소 및 물리적 장애물과 같은 실행 시간 장애가 있을 때 여전히 실패하기 쉽습니다. 기존의 정책 개선 방법은 기본 VLA를 미세 조정하여 일반화를 향상시키지만, 보지 못한 방해 요소 설정에서 여전히 어려움을 겪습니다. 이 문제를 해결하기 위해, 우리는 대규모 비전-언어 모델(VLM)의 인터넷 규모 사전 학습을 활용하여 이러한 장애에 대해 추론하고 정책 실패를 완화할 수 있는지 조사합니다. 이를 위해, 우리는 VLM 기반의 문맥 내 추론을 사용하여 환경의 초기 상태를 조작함으로써 사전 학습된 VLA 정책 성능을 개선하는 훈련 없는 접근 방식인 StageCraft를 제안합니다. StageCraft는 정책 롤아웃 비디오와 성공 레이블을 입력으로 받아 VLM의 추론 능력을 활용하여 예상되는 실행 실패를 피하기 위해 초기 상태에서 어떤 객체를 조작해야 하는지 추론합니다. StageCraft는 확장 가능한 플러그 앤 플레이 모듈로, 기본 정책에 추가 제약을 도입하지 않으며 작동에 몇 가지 정책 롤아웃만 필요로 합니다. 우리는 StageCraft를 사용한 최첨단 VLA 모델의 성능을 평가하고, 다양한 방해 요소와 장애물을 포함하는 세 가지 실제 작업 도메인에서 절대 40%의 성능 향상을 보여줍니다. RLBench에서의 시뮬레이션 실험은 StageCraft가 기본 정책의 강도에 따라 개입 정도를 조정하고 더 많은 문맥 내 샘플로 성능을 향상시킴을 경험적으로 보여줍니다. StageCraft의 작동 비디오는 https://stagecraft-decorator.github.io/stagecraft/ 에서 확인할 수 있습니다.

## 핵심 내용
텍스트 및 이미지 데이터에 대한 대규모 사전 학습과 다양한 로봇 시연을 통해 Vision Language Action 모델(VLA)이 새로운 작업, 객체 및 장면에 일반화될 수 있게 되었습니다. 그러나 이러한 모델은 로봇 작업 공간에서의 방해 요소 및 물리적 장애물과 같은 실행 시간 장애가 있을 때 여전히 실패하기 쉽습니다. 기존의 정책 개선 방법은 기본 VLA를 미세 조정하여 일반화를 향상시키지만, 보지 못한 방해 요소 설정에서 여전히 어려움을 겪습니다. 이 문제를 해결하기 위해, 우리는 대규모 비전-언어 모델(VLM)의 인터넷 규모 사전 학습을 활용하여 이러한 장애에 대해 추론하고 정책 실패를 완화할 수 있는지 조사합니다. 이를 위해, 우리는 VLM 기반의 문맥 내 추론을 사용하여 환경의 초기 상태를 조작함으로써 사전 학습된 VLA 정책 성능을 개선하는 훈련 없는 접근 방식인 StageCraft를 제안합니다. StageCraft는 정책 롤아웃 비디오와 성공 레이블을 입력으로 받아 VLM의 추론 능력을 활용하여 예상되는 실행 실패를 피하기 위해 초기 상태에서 어떤 객체를 조작해야 하는지 추론합니다. StageCraft는 확장 가능한 플러그 앤 플레이 모듈로, 기본 정책에 추가 제약을 도입하지 않으며 작동에 몇 가지 정책 롤아웃만 필요로 합니다. 우리는 StageCraft를 사용한 최첨단 VLA 모델의 성능을 평가하고, 다양한 방해 요소와 장애물을 포함하는 세 가지 실제 작업 도메인에서 절대 40%의 성능 향상을 보여줍니다. RLBench에서의 시뮬레이션 실험은 StageCraft가 기본 정책의 강도에 따라 개입 정도를 조정하고 더 많은 문맥 내 샘플로 성능을 향상시킴을 경험적으로 보여줍니다. StageCraft의 작동 비디오는 https://stagecraft-decorator.github.io/stagecraft/ 에서 확인할 수 있습니다.
