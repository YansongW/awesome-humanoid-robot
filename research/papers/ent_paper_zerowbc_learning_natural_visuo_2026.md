---
$id: ent_paper_zerowbc_learning_natural_visuo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video'
  zh: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video'
  ko: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video'
summary:
  en: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: ZeroWBC 是一个无需遥操作的人形机器人全身交互控制框架，由研究团队于 2026 年提出。其核心贡献在于直接从人类第一人称视频中学习自然的视觉运动控制，通过生成-跟踪两阶段方法实现静态场景下的全身交互，并在 Unitree G1
    人形机器人上验证了多样化的场景感知行为。
  ko: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- loco_manipulation
- whole_body_control
- zerowbc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.09170v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2603.09170
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video project page'
  url: https://zerowbc.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
ZeroWBC 旨在解决人形机器人全身交互控制中遥操作数据成本高昂的问题。该框架采用生成-跟踪两阶段策略：首先，基于初始第一人称图像和语言指令，微调后的视觉语言模型生成未来人体全身运动令牌，解码后重定向至人形机器人；随后，一个通用交互运动跟踪策略执行生成的参考运动及根部和关键身体部位轨迹。为提升交互性能，研究引入了面向交互的跟踪奖励，在保持自然全身运动的同时优先对齐全局根部和关键身体部位轨迹。实验在 Unitree G1 人形机器人上进行，展示了无需机器人遥操作演示即可实现多样化场景感知行为的能力。

## 核心内容
### 方法架构
ZeroWBC 采用生成-跟踪两阶段框架：
- **生成阶段**：输入初始第一人称图像和语言指令，通过微调的 Vision-Language Model 生成未来人体全身运动令牌。这些令牌被解码为连续运动，并重定向至人形机器人，生成参考运动及根部和关键身体部位轨迹。
- **跟踪阶段**：一个通用交互运动跟踪策略执行生成的参考运动。该策略通过强化学习训练，引入面向交互的跟踪奖励，优先对齐全局根部和关键身体部位轨迹，同时保持全身运动的自然性。

### 实验设置
- **机器人平台**：Unitree G1 人形机器人。
- **数据来源**：人类第一人称视频，配合同步的全身运动数据和文本标注。
- **任务场景**：静态场景下的全身交互控制，如抓取、操作等。

### 关键结果
- ZeroWBC 无需机器人遥操作演示即可实现多样化的场景感知行为。
- 面向交互的跟踪奖励显著提升了交互性能，尤其在全局根部和关键身体部位轨迹对齐方面。
- 实验表明，该框架为从人类第一人称数据学习自然人形机器人全身交互提供了一种可扩展的范式。

## Overview
Achieving versatile and natural whole-body humanoid interaction control remains challenging due to the high cost of whole-body teleoperation data. We present ZeroWBC, a teleoperation-free framework that learns humanoid whole-body interaction from human egocentric videos paired with synchronized whole-body motion and text annotations. ZeroWBC adopts a generation-then-tracking formulation to tackle the static scene whole-body interaction control problem. Given an initial egocentric image and a language instruction, a fine-tuned Vision-Language Model generates future human whole-body motion tokens, which are decoded into continuous motions and retargeted to the humanoid. The resulting reference motions, together with root and key body-part trajectories, are then executed by a general interactive motion tracking policy. To improve interaction performance, we introduce an interaction-oriented tracking reward that prioritizes global root and key body-part trajectory alignment while preserving natural whole-body motion. Experiments on the Unitree G1 humanoid robot show that ZeroWBC enables diverse scene-aware behaviors without robot teleoperation demonstrations. These results suggest a scalable paradigm for learning natural humanoid whole-body interaction from human egocentric data.

## 개요
다재다능하고 자연스러운 전신 휴머노이드 상호작용 제어는 전신 원격 조작 데이터의 높은 비용으로 인해 여전히 어려운 과제입니다. 우리는 인간의 자기중심적 영상과 동기화된 전신 움직임 및 텍스트 주석을 활용하여 휴머노이드 전신 상호작용을 학습하는 원격 조작 없는 프레임워크인 ZeroWBC를 제시합니다. ZeroWBC는 생성 후 추적(generation-then-tracking) 방식을 채택하여 정적 장면 전신 상호작용 제어 문제를 해결합니다. 초기 자기중심적 이미지와 언어 명령이 주어지면, 미세 조정된 Vision-Language Model이 미래의 인간 전신 움직임 토큰을 생성하고, 이를 연속적인 움직임으로 디코딩하여 휴머노이드에 리타겟팅합니다. 결과적으로 생성된 참조 움직임과 루트 및 주요 신체 부위 궤적은 일반적인 상호작용 움직임 추적 정책에 의해 실행됩니다. 상호작용 성능을 향상시키기 위해, 자연스러운 전신 움직임을 유지하면서 전역 루트 및 주요 신체 부위 궤적 정렬을 우선시하는 상호작용 지향 추적 보상을 도입합니다. Unitree G1 휴머노이드 로봇 실험 결과, ZeroWBC는 로봇 원격 조작 시연 없이도 다양한 장면 인식 행동을 가능하게 함을 보여줍니다. 이러한 결과는 인간의 자기중심적 데이터로부터 자연스러운 휴머노이드 전신 상호작용을 학습하기 위한 확장 가능한 패러다임을 시사합니다.

## 핵심 내용
다재다능하고 자연스러운 전신 휴머노이드 상호작용 제어는 전신 원격 조작 데이터의 높은 비용으로 인해 여전히 어려운 과제입니다. 우리는 인간의 자기중심적 영상과 동기화된 전신 움직임 및 텍스트 주석을 활용하여 휴머노이드 전신 상호작용을 학습하는 원격 조작 없는 프레임워크인 ZeroWBC를 제시합니다. ZeroWBC는 생성 후 추적(generation-then-tracking) 방식을 채택하여 정적 장면 전신 상호작용 제어 문제를 해결합니다. 초기 자기중심적 이미지와 언어 명령이 주어지면, 미세 조정된 Vision-Language Model이 미래의 인간 전신 움직임 토큰을 생성하고, 이를 연속적인 움직임으로 디코딩하여 휴머노이드에 리타겟팅합니다. 결과적으로 생성된 참조 움직임과 루트 및 주요 신체 부위 궤적은 일반적인 상호작용 움직임 추적 정책에 의해 실행됩니다. 상호작용 성능을 향상시키기 위해, 자연스러운 전신 움직임을 유지하면서 전역 루트 및 주요 신체 부위 궤적 정렬을 우선시하는 상호작용 지향 추적 보상을 도입합니다. Unitree G1 휴머노이드 로봇 실험 결과, ZeroWBC는 로봇 원격 조작 시연 없이도 다양한 장면 인식 행동을 가능하게 함을 보여줍니다. 이러한 결과는 인간의 자기중심적 데이터로부터 자연스러운 휴머노이드 전신 상호작용을 학습하기 위한 확장 가능한 패러다임을 시사합니다.

## 参考
- http://arxiv.org/abs/2603.09170v3
