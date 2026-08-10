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
  zh: 本文提出一种基于Veo2微调的动作条件多视角一致世界模拟器，用于评估Gemini Robotics策略在ALOHA 2双臂任务中的表现。该系统通过生成式编辑合成真实场景变体，支持标称性能、分布外泛化及安全关键场景的全面评估。实验基于1600+次真实世界评估，验证了八个策略检查点在五个任务上的有效性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10675v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (753 chars, DeepSeek).'
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
该研究构建了一个生成式评估系统，以Veo视频基础模型为核心，通过机器人数据微调实现动作条件化与多视角一致性。系统集成生成式图像编辑与多视角补全技术，可合成包含新交互物体、视觉背景及干扰物的场景变体。实验覆盖标称条件、分布外泛化及物理/语义安全约束测试，通过1600+次真实世界评估验证了八个Gemini Robotics策略检查点在ALOHA 2双臂操作任务上的表现。结果表明该系统能准确预测不同策略的相对性能，并暴露违反安全约束的行为。

## 核心内容
### 方法架构
- **基础模型**：基于Veo2视频基础模型，通过机器人数据微调实现动作条件化与多视角一致性。
- **生成式编辑**：集成图像编辑与多视角补全技术，支持沿多个泛化轴（新物体、背景、干扰物）合成真实场景变体。
- **评估框架**：覆盖标称性能、分布外泛化及安全关键场景（物理/语义约束违反检测）。

### 实验设置
- **硬件平台**：ALOHA 2双臂操作平台
- **策略**：八个Gemini Robotics策略检查点
- **任务**：五个双臂操作任务
- **评估规模**：1600+次真实世界评估

### 关键发现
- **保真度验证**：系统能准确模拟编辑后的场景（含新交互物体、视觉背景、干扰物），保持基础视频模型的生成能力。
- **性能预测**：在标称与分布外条件下，系统可准确预测不同策略的相对性能差异。
- **泛化分析**：量化不同泛化轴（物体、背景、干扰物）对策略性能的相对影响。
- **安全测试**：通过红队测试暴露违反物理或语义安全约束的行为。

### 结论
该生成式评估系统为机器人策略提供了从标称到极端条件的全谱系评估能力，显著扩展了视频模型在机器人领域的应用范围。

## Overview
Generative world models hold significant potential for simulating interactions with visuomotor policies in varied environments. Frontier video models can enable generation of realistic observations and environment interactions in a scalable and general manner. However, the use of video models in robotics has been limited primarily to in-distribution evaluations, i.e., scenarios that are similar to ones used to train the policy or fine-tune the base video model. In this report, we demonstrate that video models can be used for the entire spectrum of policy evaluation use cases in robotics: from assessing nominal performance to out-of-distribution (OOD) generalization, and probing physical and semantic safety. We introduce a generative evaluation system built upon a frontier video foundation model (Veo). The system is optimized to support robot action conditioning and multi-view consistency, while integrating generative image-editing and multi-view completion to synthesize realistic variations of real-world scenes along multiple axes of generalization. We demonstrate that the system preserves the base capabilities of the video model to enable accurate simulation of scenes that have been edited to include novel interaction objects, novel visual backgrounds, and novel distractor objects. This fidelity enables accurately predicting the relative performance of different policies in both nominal and OOD conditions, determining the relative impact of different axes of generalization on policy performance, and performing red teaming of policies to expose behaviors that violate physical or semantic safety constraints. We validate these capabilities through 1600+ real-world evaluations of eight Gemini Robotics policy checkpoints and five tasks for a bimanual manipulator.

## 参考
- http://arxiv.org/abs/2512.10675v2

## 개요
이 연구는 생성형 평가 시스템을 구축하여, Veo 비디오 기반 모델을 핵심으로 삼고 로봇 데이터 미세 조정을 통해 동작 조건화와 다중 시점 일관성을 구현했습니다. 시스템은 생성형 이미지 편집 및 다중 시점 보완 기술을 통합하여 새로운 상호작용 객체, 시각적 배경 및 방해물을 포함한 장면 변형을 합성할 수 있습니다. 실험은 명목 조건, 분포 외 일반화 및 물리적/의미적 안전 제약 테스트를 포괄하며, 1600회 이상의 실제 세계 평가를 통해 ALOHA 2 이중 팔 조작 작업에서 8개의 Gemini Robotics 정책 체크포인트 성능을 검증했습니다. 결과는 시스템이 다양한 정책의 상대적 성능을 정확히 예측하고 안전 제약을 위반하는 행동을 노출할 수 있음을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **기반 모델**: Veo2 비디오 기반 모델을 기반으로, 로봇 데이터 미세 조정을 통해 동작 조건화와 다중 시점 일관성을 구현.
- **생성형 편집**: 이미지 편집 및 다중 시점 보완 기술을 통합하여 여러 일반화 축(새로운 객체, 배경, 방해물)을 따라 실제 장면 변형을 합성 지원.
- **평가 프레임워크**: 명목 성능, 분포 외 일반화 및 안전 중요 장면(물리적/의미적 제약 위반 탐지)을 포괄.

### 실험 설정
- **하드웨어 플랫폼**: ALOHA 2 이중 팔 조작 플랫폼
- **정책**: 8개의 Gemini Robotics 정책 체크포인트
- **작업**: 5개의 이중 팔 조작 작업
- **평가 규모**: 1600회 이상의 실제 세계 평가

### 주요 발견
- **충실도 검증**: 시스템이 편집된 장면(새로운 상호작용 객체, 시각적 배경, 방해물 포함)을 정확히 시뮬레이션하며, 기반 비디오 모델의 생성 능력을 유지.
- **성능 예측**: 명목 및 분포 외 조건에서 시스템이 다양한 정책의 상대적 성능 차이를 정확히 예측.
- **일반화 분석**: 다양한 일반화 축(객체, 배경, 방해물)이 정책 성능에 미치는 상대적 영향을 정량화.
- **안전 테스트**: 레드 팀 테스트를 통해 물리적 또는 의미적 안전 제약을 위반하는 행동을 노출.

### 결론
이 생성형 평가 시스템은 로봇 정책에 명목 조건부터 극한 조건까지의 전 스펙트럼 평가 능력을 제공하며, 비디오 모델의 로봇 분야 적용 범위를 크게 확장합니다.
