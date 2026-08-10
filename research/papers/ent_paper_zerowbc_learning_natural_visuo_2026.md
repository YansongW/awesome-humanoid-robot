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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.09170v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (745 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2603.09170v3

## 개요
ZeroWBC는 휴머노이드 로봇의 전신 상호작용 제어에서 원격 조작 데이터의 높은 비용 문제를 해결하는 것을 목표로 합니다. 이 프레임워크는 생성-추적 2단계 전략을 채택합니다: 먼저, 초기 1인칭 이미지와 언어 명령을 기반으로 미세 조정된 비전-언어 모델이 미래 인체 전신 운동 토큰을 생성하고, 이를 디코딩하여 휴머노이드 로봇으로 리타게팅합니다. 이후, 범용 상호작용 운동 추적 정책이 생성된 참조 운동 및 루트와 주요 신체 부위 궤적을 실행합니다. 상호작용 성능을 향상시키기 위해, 연구는 상호작용 지향 추적 보상을 도입하여 자연스러운 전신 운동을 유지하면서 전역 루트와 주요 신체 부위 궤적 정렬을 우선시합니다. 실험은 Unitree G1 휴머노이드 로봇에서 수행되었으며, 로봇 원격 조작 데모 없이 다양한 장면 인식 행동을 구현할 수 있음을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
ZeroWBC는 생성-추적 2단계 프레임워크를 채택합니다:
- **생성 단계**: 초기 1인칭 이미지와 언어 명령을 입력으로 받아, 미세 조정된 Vision-Language Model이 미래 인체 전신 운동 토큰을 생성합니다. 이러한 토큰은 연속 운동으로 디코딩되어 휴머노이드 로봇으로 리타게팅되며, 참조 운동 및 루트와 주요 신체 부위 궤적을 생성합니다.
- **추적 단계**: 범용 상호작용 운동 추적 정책이 생성된 참조 운동을 실행합니다. 이 정책은 강화 학습을 통해 훈련되며, 상호작용 지향 추적 보상을 도입하여 전역 루트와 주요 신체 부위 궤적 정렬을 우선시하면서 전신 운동의 자연스러움을 유지합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree G1 휴머노이드 로봇.
- **데이터 소스**: 동기화된 전신 운동 데이터와 텍스트 주석이 포함된 인간 1인칭 비디오.
- **작업 시나리오**: 정적 장면에서의 전신 상호작용 제어, 예: 파지, 조작 등.

### 주요 결과
- ZeroWBC는 로봇 원격 조작 데모 없이 다양한 장면 인식 행동을 구현할 수 있습니다.
- 상호작용 지향 추적 보상은 특히 전역 루트와 주요 신체 부위 궤적 정렬에서 상호작용 성능을 크게 향상시킵니다.
- 실험은 이 프레임워크가 인간 1인칭 데이터에서 자연스러운 휴머노이드 로봇 전신 상호작용을 학습하기 위한 확장 가능한 패러다임을 제공함을 보여줍니다.
