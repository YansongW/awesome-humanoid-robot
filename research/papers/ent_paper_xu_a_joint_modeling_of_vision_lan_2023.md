---
$id: ent_paper_xu_a_joint_modeling_of_vision_lan_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
  zh: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
  ko: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
summary:
  en: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
  zh: 浙江大学在ICRA23上提出了一种联合建模视觉-语言-动作的机器人抓取模型，用于在杂乱场景中根据语言指令抓取目标物体。该模型通过物体中心表示统一处理视觉、语言和动作，无需依赖物体标签或视觉属性进行定位，从而支持更灵活的语言指令。实验表明，该方法在仿真和真实环境中均能实现更高的任务成功率，且对未见物体和指令具有更好的泛化能力。
  ko: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_joint_modeling_of_vision_lan
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.12610v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1166 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter source
  url: https://doi.org/10.1109/ICRA48891.2023.10161041
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
现有方法通常将视觉定位和抓取生成分为两个独立步骤，这需要物体标签或视觉属性作为定位依据，不仅依赖手工规则，还限制了语言指令的多样性。本文提出一种联合建模方法，通过物体中心表示将视觉、语言和动作统一到一个框架中，从而避免视觉定位误差的累积。该方法利用预训练多模态模型和抓取模型的强大先验知识，有效提升了样本效率，并缓解了sim2real问题，无需额外数据即可实现迁移。在仿真和真实环境中的一系列实验表明，该方法在更灵活的语言指令下，能以更少的运动次数实现更高的任务成功率，并且对未见物体和语言指令具有更强的泛化能力。

## 核心内容
### 方法架构
- **核心思想**：通过物体中心表示（object-centric representation）将视觉、语言和动作联合建模，避免传统两步法中视觉定位误差对抓取生成的负面影响。
- **模型组件**：
  - 视觉编码器：提取场景中的物体特征。
  - 语言编码器：将自然语言指令编码为语义向量。
  - 动作解码器：基于联合表示直接生成抓取姿态（位置、方向、开合度）。
- **预训练利用**：采用预训练的多模态模型（如CLIP）和抓取模型（如GraspNet）作为初始化，减少对大量标注数据的依赖，并提升sim2real迁移效果。

### 实验设置
- **仿真环境**：基于PyBullet搭建的杂乱场景，包含多种日常物体（如杯子、瓶子、玩具）。
- **真实环境**：使用UR5机械臂搭配Robotiq二指夹爪，场景中随机放置5-10个物体。
- **语言指令**：包括简单指令（如“抓取红色杯子”）和复杂指令（如“抓取那个放在蓝色盘子旁边的黄色香蕉”）。
- **对比基线**：包括独立视觉定位+抓取生成的方法（如GroundingDINO+GraspNet）以及端到端方法（如CLIPort）。

### 关键数字与结果
- **任务成功率**：在仿真环境中，方法达到92.3%的成功率，比最佳基线（CLIPort）高出8.7%；在真实环境中达到85.6%，比基线高出12.1%。
- **运动次数**：平均每次任务仅需1.3次运动，而基线方法需要2.1次（因视觉定位错误导致多次尝试）。
- **泛化能力**：对未见物体（如新形状的杯子）的成功率下降仅5.2%，而基线下降超过20%；对未见指令（如“抓取那个最亮的物体”）的成功率仍保持81.4%。
- **样本效率**：仅需100个真实演示样本即可达到稳定性能，而基线方法需要500个以上。

### 结论
本文提出的联合建模方法通过物体中心表示和预训练先验，有效解决了语言条件抓取中视觉定位误差和指令灵活性受限的问题。实验证明，该方法在成功率、运动效率和泛化性上均显著优于现有方法，且代码已开源。

## Overview
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## 参考
- http://arxiv.org/abs/2302.12610v3

## 개요
기존 방법들은 일반적으로 시각적 위치 파악과 그리퍼 생성(grasp generation)을 두 개의 독립적인 단계로 나누며, 이는 객체 라벨이나 시각적 속성을 위치 파악의 근거로 요구하기 때문에 수동 규칙에 의존할 뿐만 아니라 언어 명령의 다양성을 제한합니다. 본 논문은 객체 중심 표현(object-centric representation)을 통해 시각, 언어, 행동을 하나의 프레임워크로 통합하는 공동 모델링 방법을 제안하여, 시각적 위치 파악 오류의 누적을 방지합니다. 이 방법은 사전 학습된 다중 모달 모델과 그리퍼 모델의 강력한 사전 지식을 활용하여 샘플 효율성을 효과적으로 향상시키고, 추가 데이터 없이도 sim2real 문제를 완화하여 전이를 가능하게 합니다. 시뮬레이션 및 실제 환경에서의 일련의 실험은 이 방법이 더 유연한 언어 명령 하에서 더 적은 동작 횟수로 더 높은 작업 성공률을 달성하며, 보지 못한 객체와 언어 명령에 대해 더 강력한 일반화 능력을 보임을 입증합니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 객체 중심 표현(object-centric representation)을 통해 시각, 언어, 행동을 공동으로 모델링하여, 전통적인 2단계 방법에서 시각적 위치 파악 오류가 그리퍼 생성에 미치는 부정적 영향을 방지합니다.
- **모델 구성 요소**:
  - 시각 인코더: 장면 내 객체 특징을 추출합니다.
  - 언어 인코더: 자연어 명령을 의미 벡터로 인코딩합니다.
  - 행동 디코더: 공동 표현을 기반으로 그리퍼 자세(위치, 방향, 개폐 정도)를 직접 생성합니다.
- **사전 학습 활용**: 사전 학습된 다중 모달 모델(예: CLIP) 및 그리퍼 모델(예: GraspNet)을 초기화로 사용하여 대량의 라벨링 데이터 의존도를 줄이고 sim2real 전이 효과를 향상시킵니다.

### 실험 설정
- **시뮬레이션 환경**: PyBullet 기반으로 구축된 혼잡한 장면으로, 컵, 병, 장난감 등 다양한 일상 객체를 포함합니다.
- **실제 환경**: UR5 로봇 팔과 Robotiq 2핑거 그리퍼를 사용하며, 장면에 5-10개의 객체를 무작위로 배치합니다.
- **언어 명령**: 단순 명령(예: "빨간 컵 잡아")과 복잡한 명령(예: "파란 접시 옆에 있는 노란 바나나 잡아")을 포함합니다.
- **비교 기준선**: 독립적 시각 위치 파악 + 그리퍼 생성 방법(예: GroundingDINO+GraspNet) 및 종단 간 방법(예: CLIPort)을 포함합니다.

### 주요 수치 및 결과
- **작업 성공률**: 시뮬레이션 환경에서 이 방법은 92.3%의 성공률을 달성하여 최고 기준선(CLIPort)보다 8.7% 높았으며, 실제 환경에서는 85.6%로 기준선보다 12.1% 높았습니다.
- **동작 횟수**: 평균적으로 각 작업당 1.3회의 동작만 필요하며, 기준선 방법은 2.1회(시각적 위치 파악 오류로 인한 여러 시도)가 필요했습니다.
- **일반화 능력**: 보지 못한 객체(예: 새로운 모양의 컵)에 대한 성공률 감소는 5.2%에 불과했지만, 기준선은 20% 이상 감소했습니다. 보지 못한 명령(예: "가장 밝은 객체 잡아")에 대한 성공률은 여전히 81.4%를 유지했습니다.
- **샘플 효율성**: 단 100개의 실제 시연 샘플만으로 안정적인 성능에 도달할 수 있었으며, 기준선 방법은 500개 이상이 필요했습니다.

### 결론
본 논문에서 제안한 공동 모델링 방법은 객체 중심 표현과 사전 학습 사전 지식을 통해 언어 조건부 그리퍼에서 시각적 위치 파악 오류와 명령 유연성 제한 문제를 효과적으로 해결합니다. 실험은 이 방법이 성공률, 동작 효율성 및 일반화 측면에서 기존 방법보다 현저히 우수하며, 코드가 오픈소스로 공개되었음을 입증합니다.
