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
  en: This paper introduces an action-conditioned, multi-view consistent world simulator
    built by fine-tuning Veo2 on robotic data, and uses it together with generative
    editing to evaluate Gemini Robotics policies on ALOHA 2 bimanual tasks across
    nominal, OOD, and safety-critical settings.
  zh: 本文通过在大规模机器人数据上微调 Veo2，构建了一个动作条件化、多视角一致的世界模拟器，并结合生成式场景编辑，在 ALOHA 2 双臂任务上对 Gemini
    Robotics 策略在正常、分布外及安全关键场景下进行评测。
  ko: 본 논문은 대규모 로봇 데이터로 Veo2를 미세 조정하여 동작 조건부 다중 뷰 일관성 월드 시뮬레이터를 구축하고, 생성형 장면 편집과 결합하여
    ALOHA 2 양팔 조작 작업에서 Gemini Robotics 정책의 정상, OOD 및 안전 중요 설정을 평가한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review is required
    before marking verified.
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

## Overview

The paper presents a generative evaluation system that turns a frontier video foundation model, Veo2, into a robot-policy simulator. The model is fine-tuned on large-scale robotic data so that it can be conditioned on robot actions and produce temporally and multi-view consistent videos of policy rollouts. This simulator is combined with generative image editing (NanoBanana / Gemini 2.5 Flash Image) and multi-view completion to synthesize diverse nominal, out-of-distribution, and safety-critical scenes without requiring expensive physical setups.

The authors validate the simulator by comparing its predictions against more than 1600 real-world evaluations of eight Gemini Robotics policy checkpoints on five ALOHA 2 bimanual manipulation tasks. The reported results show strong correlation between simulated and real policy performance, with Pearson correlation around 0.88 and low rank violation metrics, suggesting that the simulator can reliably rank policies and detect failure modes.

A central claim is that the system enables predictive red teaming: it can discover physical and semantic safety violations virtually, before any unsafe real-world rollout is attempted. The work therefore positions generative video simulation as a scalable complement to, and in some cases a substitute for, traditional hardware-based policy evaluation.

## Key Contributions

- Fine-tunes Veo2 into an action-conditioned, multi-view consistent video simulator for robot policy rollouts.
- Integrates generative image editing and multi-view synthesis to create realistic variations of objects, backgrounds, and distractors.
- Reports strong correlation (Pearson ~0.88) and low rank violation (MMRV ~0.03–0.15) between simulated and real-world policy performance.
- Demonstrates predictive red teaming for physical and semantic safety without unsafe real-world rollouts.
- Validates the approach with 1600+ real-world trials across eight Gemini Robotics checkpoints and five ALOHA 2 bimanual tasks.

## Relevance to Humanoid Robotics

Humanoid robot deployment at scale depends on the ability to evaluate generalist manipulation policies reliably, cheaply, and safely. This paper directly addresses that need by replacing many physical trials with a high-fidelity generative simulator that can expose both OOD generalization gaps and safety failures before deployment. The methods are demonstrated on bimanual manipulation, which is a core capability for humanoid systems, and the use of action-conditioned world models aligns with the broader industry need for scalable virtual testing in the humanoid production pipeline.
