---
$id: ent_paper_choromanski_evaluating_gemini_robotics_pol_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Evaluating Gemini Robotics Policies in a Veo World Simulator
  zh: 在 Veo 世界模拟器中评估 Gemini Robotics 策略
  ko: Veo World Simulator에서 Gemini Robotics 정책 평가
summary:
  en: This paper introduces an action-conditioned, multi-view consistent world simulator built by fine-tuning Veo2 on robotic
    data, and uses it together with generative editing to evaluate Gemini Robotics policies on ALOHA 2 bimanual tasks across
    nominal, OOD, and safety-critical settings.
  zh: 本文通过在大规模机器人数据上微调 Veo2，构建了一个动作条件化、多视角一致的世界模拟器，并结合生成式场景编辑，在 ALOHA 2 双臂任务上对 Gemini Robotics 策略在正常、分布外及安全关键场景下进行评测。
  ko: 본 논문은 대규모 로봇 데이터로 Veo2를 미세 조정하여 동작 조건부 다중 뷰 일관성 월드 시뮬레이터를 구축하고, 생성형 장면 편집과 결합하여 ALOHA 2 양팔 조작 작업에서 Gemini Robotics 정책의
    정상, OOD 및 안전 중요 설정을 평가한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- world_model
- video_generation
- simulation
- policy_evaluation
- bimanual_manipulation
- vision_language_action
- ood_generalization
- safety_red_teaming
- aloha_2
- gemini_robotics
- veo2
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10675v2.
sources:
- id: src_001
  type: paper
  title: Evaluating Gemini Robotics Policies in a Veo World Simulator
  url: https://arxiv.org/abs/2512.10675
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Generative world models hold significant potential for simulating interactions with visuomotor policies in varied environments. Frontier video models can enable generation of realistic observations and environment interactions in a scalable and general manner. However, the use of video models in robotics has been limited primarily to in-distribution evaluations, i.e., scenarios that are similar to ones used to train the policy or fine-tune the base video model. In this report, we demonstrate that video models can be used for the entire spectrum of policy evaluation use cases in robotics: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety. We introduce a generative evaluation system built upon a frontier video foundation model (Veo). The system is optimized to support robot action conditioning and multi-view consistency, while integrating generative image-editing and multi-view completion to synthesize realistic variations of real-world scenes along multiple axes of generalization. We demonstrate that the system preserves the base capabilities of the video model to enable accurate simulation of scenes that have been edited to include novel interaction objects, novel visual backgrounds, and novel distractor objects. This fidelity enables accurately predicting the relative performance of different policies in both nominal and OOD conditions, determining the relative impact of different axes of generalization on policy performance, and performing red teaming of policies to expose behaviors that violate physical or semantic safety constraints. We validate these capabilities through 1600+ real-world evaluations of eight Gemini Robotics policy checkpoints and five tasks for a bimanual manipulator.

## 核心内容
Generative world models hold significant potential for simulating interactions with visuomotor policies in varied environments. Frontier video models can enable generation of realistic observations and environment interactions in a scalable and general manner. However, the use of video models in robotics has been limited primarily to in-distribution evaluations, i.e., scenarios that are similar to ones used to train the policy or fine-tune the base video model. In this report, we demonstrate that video models can be used for the entire spectrum of policy evaluation use cases in robotics: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety. We introduce a generative evaluation system built upon a frontier video foundation model (Veo). The system is optimized to support robot action conditioning and multi-view consistency, while integrating generative image-editing and multi-view completion to synthesize realistic variations of real-world scenes along multiple axes of generalization. We demonstrate that the system preserves the base capabilities of the video model to enable accurate simulation of scenes that have been edited to include novel interaction objects, novel visual backgrounds, and novel distractor objects. This fidelity enables accurately predicting the relative performance of different policies in both nominal and OOD conditions, determining the relative impact of different axes of generalization on policy performance, and performing red teaming of policies to expose behaviors that violate physical or semantic safety constraints. We validate these capabilities through 1600+ real-world evaluations of eight Gemini Robotics policy checkpoints and five tasks for a bimanual manipulator.

## 参考
- http://arxiv.org/abs/2512.10675v2

## Overview
Generative world models hold significant potential for simulating interactions with visuomotor policies in varied environments. Frontier video models can enable generation of realistic observations and environment interactions in a scalable and general manner. However, the use of video models in robotics has been limited primarily to in-distribution evaluations, i.e., scenarios that are similar to ones used to train the policy or fine-tune the base video model. In this report, we demonstrate that video models can be used for the entire spectrum of policy evaluation use cases in robotics: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety. We introduce a generative evaluation system built upon a frontier video foundation model (Veo). The system is optimized to support robot action conditioning and multi-view consistency, while integrating generative image-editing and multi-view completion to synthesize realistic variations of real-world scenes along multiple axes of generalization. We demonstrate that the system preserves the base capabilities of the video model to enable accurate simulation of scenes that have been edited to include novel interaction objects, novel visual backgrounds, and novel distractor objects. This fidelity enables accurately predicting the relative performance of different policies in both nominal and OOD conditions, determining the relative impact of different axes of generalization on policy performance, and performing red teaming of policies to expose behaviors that violate physical or semantic safety constraints. We validate these capabilities through 1600+ real-world evaluations of eight Gemini Robotics policy checkpoints and five tasks for a bimanual manipulator.

## Content
Generative world models hold significant potential for simulating interactions with visuomotor policies in varied environments. Frontier video models can enable generation of realistic observations and environment interactions in a scalable and general manner. However, the use of video models in robotics has been limited primarily to in-distribution evaluations, i.e., scenarios that are similar to ones used to train the policy or fine-tune the base video model. In this report, we demonstrate that video models can be used for the entire spectrum of policy evaluation use cases in robotics: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety. We introduce a generative evaluation system built upon a frontier video foundation model (Veo). The system is optimized to support robot action conditioning and multi-view consistency, while integrating generative image-editing and multi-view completion to synthesize realistic variations of real-world scenes along multiple axes of generalization. We demonstrate that the system preserves the base capabilities of the video model to enable accurate simulation of scenes that have been edited to include novel interaction objects, novel visual backgrounds, and novel distractor objects. This fidelity enables accurately predicting the relative performance of different policies in both nominal and OOD conditions, determining the relative impact of different axes of generalization on policy performance, and performing red teaming of policies to expose behaviors that violate physical or semantic safety constraints. We validate these capabilities through 1600+ real-world evaluations of eight Gemini Robotics policy checkpoints and five tasks for a bimanual manipulator.

## 개요
생성적 세계 모델은 다양한 환경에서 시각-운동 정책과의 상호작용을 시뮬레이션하는 데 큰 잠재력을 지니고 있습니다. 최첨단 비디오 모델은 확장 가능하고 일반적인 방식으로 현실적인 관찰과 환경 상호작용을 생성할 수 있게 합니다. 그러나 로봇공학에서 비디오 모델의 사용은 주로 분포 내 평가, 즉 정책을 훈련하거나 기본 비디오 모델을 미세 조정하는 데 사용된 시나리오와 유사한 경우로 제한되어 왔습니다. 본 보고서에서는 비디오 모델이 로봇공학에서 정책 평가 사용 사례의 전체 스펙트럼, 즉 정상 성능 평가부터 분포 외 일반화, 물리적 및 의미적 안전성 조사에 이르기까지 사용될 수 있음을 입증합니다. 우리는 최첨단 비디오 기반 모델(Veo)을 기반으로 구축된 생성적 평가 시스템을 소개합니다. 이 시스템은 로봇 동작 조건화와 다중 뷰 일관성을 지원하도록 최적화되었으며, 생성적 이미지 편집 및 다중 뷰 완성을 통합하여 실제 장면의 현실적인 변형을 여러 일반화 축을 따라 합성합니다. 우리는 이 시스템이 비디오 모델의 기본 능력을 유지하여 새로운 상호작용 객체, 새로운 시각적 배경, 새로운 방해 객체를 포함하도록 편집된 장면을 정확하게 시뮬레이션할 수 있음을 보여줍니다. 이러한 충실도는 정상 및 분포 외 조건에서 서로 다른 정책의 상대적 성능을 정확하게 예측하고, 정책 성능에 대한 다양한 일반화 축의 상대적 영향을 결정하며, 물리적 또는 의미적 안전 제약을 위반하는 행동을 노출하기 위한 정책의 레드 팀 테스트를 수행할 수 있게 합니다. 우리는 8개의 Gemini Robotics 정책 체크포인트와 양팔 조작기를 위한 5가지 작업에 대한 1600개 이상의 실제 평가를 통해 이러한 능력을 검증합니다.

## 핵심 내용
생성적 세계 모델은 다양한 환경에서 시각-운동 정책과의 상호작용을 시뮬레이션하는 데 큰 잠재력을 지니고 있습니다. 최첨단 비디오 모델은 확장 가능하고 일반적인 방식으로 현실적인 관찰과 환경 상호작용을 생성할 수 있게 합니다. 그러나 로봇공학에서 비디오 모델의 사용은 주로 분포 내 평가, 즉 정책을 훈련하거나 기본 비디오 모델을 미세 조정하는 데 사용된 시나리오와 유사한 경우로 제한되어 왔습니다. 본 보고서에서는 비디오 모델이 로봇공학에서 정책 평가 사용 사례의 전체 스펙트럼, 즉 정상 성능 평가부터 분포 외 일반화, 물리적 및 의미적 안전성 조사에 이르기까지 사용될 수 있음을 입증합니다. 우리는 최첨단 비디오 기반 모델(Veo)을 기반으로 구축된 생성적 평가 시스템을 소개합니다. 이 시스템은 로봇 동작 조건화와 다중 뷰 일관성을 지원하도록 최적화되었으며, 생성적 이미지 편집 및 다중 뷰 완성을 통합하여 실제 장면의 현실적인 변형을 여러 일반화 축을 따라 합성합니다. 우리는 이 시스템이 비디오 모델의 기본 능력을 유지하여 새로운 상호작용 객체, 새로운 시각적 배경, 새로운 방해 객체를 포함하도록 편집된 장면을 정확하게 시뮬레이션할 수 있음을 보여줍니다. 이러한 충실도는 정상 및 분포 외 조건에서 서로 다른 정책의 상대적 성능을 정확하게 예측하고, 정책 성능에 대한 다양한 일반화 축의 상대적 영향을 결정하며, 물리적 또는 의미적 안전 제약을 위반하는 행동을 노출하기 위한 정책의 레드 팀 테스트를 수행할 수 있게 합니다. 우리는 8개의 Gemini Robotics 정책 체크포인트와 양팔 조작기를 위한 5가지 작업에 대한 1600개 이상의 실제 평가를 통해 이러한 능력을 검증합니다.
