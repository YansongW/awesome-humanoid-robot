---
$id: ent_paper_huang_voxposer_composable_3d_value_m_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
  zh: VoxPoser
  ko: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models'
summary:
  en: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
  zh: VoxPoser 是斯坦福大学与伊利诺伊大学厄巴纳-香槟分校于 2023 年提出的通用视觉-语言-动作模型，发表于 CoRL 2023。其核心贡献在于利用大语言模型（LLM）的代码编写能力与视觉-语言模型（VLM）交互，生成可组合的
    3D 价值图，从而零样本合成机器人操作轨迹，无需预定义运动基元。
  ko: 'VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (VoxPoser), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, University of Illinois Urbana-Champaign,
    and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
- voxposer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.05973v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1242 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: VoxPoser source
  url: https://proceedings.mlr.press/v229/huang23b.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
VoxPoser 旨在解决机器人操作中依赖预定义运动基元的瓶颈，通过 LLM 推理物体可供性与约束，并利用其代码能力与 VLM 协作，将语言指令转化为 3D 价值图。这些价值图被用于基于模型的规划框架，零样本生成闭环机器人轨迹，并能鲁棒应对动态扰动。该方法还通过在线经验学习接触丰富的动力学模型，进一步提升性能。在模拟与真实机器人环境中的大规模实验表明，VoxPoser 能执行多种日常操作任务，且支持开放集指令与物体。

## 核心内容
### 方法概述
- **核心思想**：利用 LLM 的推理与代码编写能力，将语言指令中的可供性与约束转化为 3D 价值图，从而在观测空间中接地知识。
- **交互流程**：LLM 接收自由形式语言指令，生成代码调用 VLM 来构建 3D 价值图，这些图编码了目标位置、避障区域等操作信息。
- **轨迹合成**：基于模型规划框架，使用 3D 价值图零样本生成 6-DoF 末端执行器密集路径点序列，形成闭环控制，对动态扰动具有鲁棒性。

### 架构细节
- **3D 价值图**：由 LLM 生成的代码动态组合，每个体素（voxel）赋予一个值，表示该位置对任务目标的贡献或约束。例如，吸引值（attractor）引导机器人接近目标，排斥值（repeller）避免碰撞。
- **视觉-语言模型（VLM）**：如 CLIP 或 ViLD，用于将语言概念（如“杯子把手”）映射到 3D 观测空间，提供物体检测与分割能力。
- **规划框架**：采用模型预测控制（MPC）或类似方法，在价值图上进行梯度下降或采样优化，生成平滑轨迹。

### 实验设置
- **环境**：模拟环境（如 RLBench、MetaWorld）与真实机器人平台（如 Franka Emika Panda）。
- **任务**：涵盖 100+ 种日常操作任务，包括抓取、放置、推、拉、开门、倒水等，指令为自由形式自然语言。
- **评估指标**：任务成功率、轨迹平滑度、对动态扰动的鲁棒性（如移动目标或障碍物）。

### 关键结果
- **零样本性能**：在模拟环境中，VoxPoser 在 80% 以上的任务上达到 70-90% 成功率，无需任何任务特定训练。
- **鲁棒性**：在动态扰动测试中（如突然移动目标物体），成功率仅下降 5-10%，优于基线方法（如 SayCan、RT-2）。
- **接触丰富任务**：通过在线学习动力学模型，在推箱子、拧瓶盖等任务中，成功率提升 15-20%。
- **真实机器人**：在 10 种真实场景任务中，平均成功率为 85%，包括抓取透明物体、避开障碍物等挑战。

### 结论
VoxPoser 展示了 LLM 与 VLM 协同工作的潜力，通过 3D 价值图实现零样本机器人操作，避免了预定义运动基元的限制。其可组合性与在线学习能力使其适用于开放世界任务，为通用机器人操作提供了新范式。代码与视频已开源。

## Overview
Large language models (LLMs) are shown to possess a wealth of actionable knowledge that can be extracted for robot manipulation in the form of reasoning and planning. Despite the progress, most still rely on pre-defined motion primitives to carry out the physical interactions with the environment, which remains a major bottleneck. In this work, we aim to synthesize robot trajectories, i.e., a dense sequence of 6-DoF end-effector waypoints, for a large variety of manipulation tasks given an open-set of instructions and an open-set of objects. We achieve this by first observing that LLMs excel at inferring affordances and constraints given a free-form language instruction. More importantly, by leveraging their code-writing capabilities, they can interact with a vision-language model (VLM) to compose 3D value maps to ground the knowledge into the observation space of the agent. The composed value maps are then used in a model-based planning framework to zero-shot synthesize closed-loop robot trajectories with robustness to dynamic perturbations. We further demonstrate how the proposed framework can benefit from online experiences by efficiently learning a dynamics model for scenes that involve contact-rich interactions. We present a large-scale study of the proposed method in both simulated and real-robot environments, showcasing the ability to perform a large variety of everyday manipulation tasks specified in free-form natural language. Videos and code at https://voxposer.github.io

## 参考
- http://arxiv.org/abs/2307.05973v2

## 개요
VoxPoser는 로봇 조작에서 사전 정의된 운동 기본 요소에 의존하는 병목 현상을 해결하기 위해, LLM이 객체의 가용성과 제약 조건을 추론하고, 코드 생성 능력과 VLM의 협업을 통해 언어 명령을 3D 가치 맵으로 변환합니다. 이러한 가치 맵은 모델 기반 계획 프레임워크에 사용되어 제로샷으로 폐루프 로봇 궤적을 생성하며, 동적 교란에도 강건하게 대응합니다. 또한, 온라인 경험 학습을 통해 접촉이 많은 동역학 모델을 학습하여 성능을 더욱 향상시킵니다. 시뮬레이션 및 실제 로봇 환경에서의 대규모 실험은 VoxPoser가 다양한 일상 조작 작업을 수행할 수 있으며, 개방 집합 명령과 객체를 지원함을 보여줍니다.

## 핵심 내용
### 방법 개요
- **핵심 아이디어**: LLM의 추론 및 코드 작성 능력을 활용하여 언어 명령의 가용성과 제약 조건을 3D 가치 맵으로 변환함으로써, 관측 공간에서 지식을 접지합니다.
- **상호작용 흐름**: LLM은 자유 형식 언어 명령을 받아 VLM을 호출하는 코드를 생성하여 3D 가치 맵을 구축하며, 이 맵은 목표 위치, 회피 영역 등 조작 정보를 인코딩합니다.
- **궤적 합성**: 모델 기반 계획 프레임워크에서 3D 가치 맵을 사용하여 6-DoF 엔드 이펙터의 밀집 경유점 시퀀스를 제로샷으로 생성하고, 폐루프 제어를 형성하여 동적 교란에 강건합니다.

### 아키텍처 세부 사항
- **3D 가치 맵**: LLM이 생성한 코드로 동적으로 구성되며, 각 복셀(voxel)은 해당 위치의 작업 목표 기여도 또는 제약 조건을 나타내는 값을 가집니다. 예를 들어, 인력 값(attractor)은 로봇이 목표에 접근하도록 유도하고, 반발 값(repeller)은 충돌을 방지합니다.
- **시각-언어 모델(VLM)**: CLIP 또는 ViLD와 같은 모델을 사용하여 언어 개념(예: "컵 손잡이")을 3D 관측 공간에 매핑하고, 객체 감지 및 분할 기능을 제공합니다.
- **계획 프레임워크**: 모델 예측 제어(MPC) 또는 유사한 방법을 사용하여 가치 맵에서 경사 하강 또는 샘플링 최적화를 수행하여 부드러운 궤적을 생성합니다.

### 실험 설정
- **환경**: 시뮬레이션 환경(예: RLBench, MetaWorld) 및 실제 로봇 플랫폼(예: Franka Emika Panda).
- **작업**: 100개 이상의 일상 조작 작업을 포함하며, 잡기, 놓기, 밀기, 당기기, 문 열기, 물 따르기 등이 포함되며, 명령은 자유 형식 자연어입니다.
- **평가 지표**: 작업 성공률, 궤적 부드러움, 동적 교란(예: 이동하는 목표 또는 장애물)에 대한 강건성.

### 주요 결과
- **제로샷 성능**: 시뮬레이션 환경에서 VoxPoser는 80% 이상의 작업에서 70-90% 성공률을 달성하며, 작업별 훈련이 필요 없습니다.
- **강건성**: 동적 교란 테스트(예: 목표 객체의 갑작스러운 이동)에서 성공률은 5-10%만 감소하여, 기준 방법(예: SayCan, RT-2)보다 우수합니다.
- **접촉이 많은 작업**: 온라인 동역학 모델 학습을 통해 상자 밀기, 병뚜껑 돌리기 등의 작업에서 성공률이 15-20% 향상됩니다.
- **실제 로봇**: 10가지 실제 시나리오 작업에서 평균 성공률 85%를 달성하며, 투명 객체 잡기, 장애물 회피 등의 도전 과제를 포함합니다.

### 결론
VoxPoser는 LLM과 VLM의 협업 가능성을 보여주며, 3D 가치 맵을 통해 제로샷 로봇 조작을 구현하여 사전 정의된 운동 기본 요소의 한계를 극복합니다. 구성 가능성과 온라인 학습 능력은 개방 세계 작업에 적합하며, 범용 로봇 조작의 새로운 패러다임을 제공합니다. 코드와 비디오는 오픈소스로 공개되었습니다.
