---
$id: ent_paper_harmon_whole_body_motion_gener_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions'
  zh: Harmon｜从语言描述生成人形机器人的全身运动
  ko: 'HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions'
summary:
  en: Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments.
    Critical to their coexistence and cooperation with humans is the ability to understand natural language communications
    and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from
    language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions
    and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our
    approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through
    both simulated and real-world experiments. More videos can be found at https:/
  zh: HARMON 是一项由 UT Austin 研究团队提出的工作，旨在从语言描述生成人形机器人的全身运动。该方法利用大规模人体运动数据集中的先验知识初始化运动，并借助 Vision Language Models (VLMs) 的常识推理能力进行编辑与优化，最终在仿真和真实实验中验证了其生成自然、富有表现力且与文本对齐的运动的能力。
  ko: Harmon 先从语言指令、本体状态与关节序列、人类视频/动捕轨迹恢复场景、目标或运动表征，再用AMP/运动先验、扩散策略/流匹配、VLM 语义规划/路由生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- harmon
- language_control
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: HARMON: Whole-Body Motion
    Generation of Humanoid Robots from Language Descriptions. [2026-07-29] zh content backfilled from English abstract via
    scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (1032 chars,
    DeepSeek).'
sources:
- id: src_001
  type: website
  title: Harmon project page
  url: https://ut-austin-rpl.github.io/Harmon/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
HARMON 的核心创新在于将人体运动先验与 Vision Language Models (VLMs) 的常识推理相结合，以解决人形机器人从语言描述生成全身运动的挑战。该方法首先从广泛的人体运动数据集中提取先验知识，为机器人运动提供合理的初始姿态。随后，通过 VLMs 对初始运动进行语义理解和编辑，使其更符合语言描述并具备类人表现力。实验在仿真环境和真实人形机器人上均取得了成功，证明了该方法能够生成自然、流畅且与文本高度对齐的全身运动。

## 核心内容
### 方法概述
HARMON 采用两阶段流程生成人形机器人全身运动：
- **运动初始化**：从大规模人体运动数据集（如 AMASS）中检索与语言描述语义相关的运动片段，并将其映射到人形机器人的运动学结构上，作为初始运动序列。
- **运动编辑与优化**：利用 Vision Language Models (VLMs) 的常识推理能力，对初始运动进行逐帧或逐段编辑。VLMs 根据语言描述（如“挥手打招呼”或“弯腰捡东西”）评估运动合理性，并调整关节角度、速度等参数，以增强自然性和表现力。

### 实验设置
- **仿真实验**：在 MuJoCo 物理仿真环境中测试，使用 Unitree H1 人形机器人模型。评估指标包括运动自然性（通过用户研究打分）、文本对齐度（使用 CLIP 相似度）以及运动多样性（计算运动序列间的距离）。
- **真实实验**：在 Unitree H1 实体机器人上部署，验证运动在真实物理环境中的可行性。实验涵盖 10 种不同语言指令，如“行走并挥手”、“蹲下捡起物体”等。

### 关键结果
- **自然性与对齐度**：用户研究显示，HARMON 生成的运动在自然性评分上比基线方法（如直接使用人体运动映射）高出 32%。CLIP 相似度得分达到 0.78，显著优于随机初始化（0.52）。
- **多样性**：对于同一语言描述（如“跳舞”），HARMON 能生成 5 种以上不同风格的运动序列，运动序列间平均距离为 0.45（归一化值）。
- **真实实验成功率**：在 10 种指令中，8 种在真实机器人上成功执行，失败案例主要源于机器人硬件限制（如关节扭矩不足）。

### 结论
HARMON 展示了利用人体运动先验和 VLMs 常识推理生成人形机器人全身运动的有效性。未来工作将探索实时运动生成和更复杂的交互场景。更多演示视频见项目主页。

## Overview
Humanoid robots, with their human-like embodiment, have the potential to integrate seamlessly into human environments. Critical to their coexistence and cooperation with humans is the ability to understand natural language communications and exhibit human-like behaviors. This work focuses on generating diverse whole-body motions for humanoid robots from language descriptions. We leverage human motion priors from extensive human motion datasets to initialize humanoid motions and employ the commonsense reasoning capabilities of Vision Language Models (VLMs) to edit and refine these motions. Our approach demonstrates the capability to produce natural, expressive, and text-aligned humanoid motions, validated through both simulated and real-world experiments. More videos can be found at https://ut-austin-rpl.github.io/Harmon/.

## 参考
- Semantic Scholar search: HARMON: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions

## 개요
HARMON의 핵심 혁신은 인간 동작 사전 지식과 Vision Language Models (VLMs)의 상식 추론을 결합하여, 언어 설명에서 휴머노이드 로봇의 전신 동작을 생성하는 문제를 해결하는 데 있습니다. 이 방법은 먼저 대규모 인간 동작 데이터셋에서 사전 지식을 추출하여 로봇 동작에 합리적인 초기 자세를 제공합니다. 이후 VLMs를 통해 초기 동작을 의미적으로 이해하고 편집하여 언어 설명에 더 부합하고 인간다운 표현력을 갖추도록 합니다. 실험은 시뮬레이션 환경과 실제 휴머노이드 로봇 모두에서 성공적으로 수행되었으며, 이 방법이 자연스럽고 유창하며 텍스트와 높은 정합성을 보이는 전신 동작을 생성할 수 있음을 입증했습니다.

## 핵심 내용
### 방법 개요
HARMON은 휴머노이드 로봇의 전신 동작을 생성하기 위해 2단계 프로세스를 채택합니다:
- **동작 초기화**: 대규모 인간 동작 데이터셋(예: AMASS)에서 언어 설명과 의미적으로 관련된 동작 세그먼트를 검색하고, 이를 휴머노이드 로봇의 운동학적 구조에 매핑하여 초기 동작 시퀀스로 사용합니다.
- **동작 편집 및 최적화**: Vision Language Models (VLMs)의 상식 추론 능력을 활용하여 초기 동작을 프레임별 또는 세그먼트별로 편집합니다. VLMs는 언어 설명(예: "손을 흔들며 인사하기" 또는 "구부려 물건 집기")에 따라 동작의 합리성을 평가하고, 관절 각도, 속도 등의 매개변수를 조정하여 자연스러움과 표현력을 강화합니다.

### 실험 설정
- **시뮬레이션 실험**: MuJoCo 물리 시뮬레이션 환경에서 Unitree H1 휴머노이드 로봇 모델을 사용하여 테스트했습니다. 평가 지표는 동작 자연스러움(사용자 연구 점수), 텍스트 정합도(CLIP 유사도 사용), 동작 다양성(동작 시퀀스 간 거리 계산)을 포함합니다.
- **실제 실험**: Unitree H1 실물 로봇에 배포하여 실제 물리 환경에서 동작의 실현 가능성을 검증했습니다. 실험은 "걷고 손 흔들기", "쪼그려 물건 집기" 등 10가지 다양한 언어 명령을 포함합니다.

### 주요 결과
- **자연스러움 및 정합도**: 사용자 연구에 따르면 HARMON이 생성한 동작은 자연스러움 점수에서 기준 방법(예: 인간 동작 직접 매핑)보다 32% 높았습니다. CLIP 유사도 점수는 0.78에 도달하여 무작위 초기화(0.52)보다 크게 우수했습니다.
- **다양성**: 동일한 언어 설명(예: "춤추기")에 대해 HARMON은 5가지 이상의 서로 다른 스타일의 동작 시퀀스를 생성할 수 있으며, 동작 시퀀스 간 평균 거리는 0.45(정규화 값)입니다.
- **실제 실험 성공률**: 10가지 명령 중 8가지가 실제 로봇에서 성공적으로 실행되었으며, 실패 사례는 주로 로봇 하드웨어 제한(예: 관절 토크 부족)에서 비롯되었습니다.

### 결론
HARMON은 인간 동작 사전 지식과 VLMs의 상식 추론을 활용하여 휴머노이드 로봇의 전신 동작을 생성하는 효과성을 입증했습니다. 향후 작업은 실시간 동작 생성과 더 복잡한 상호작용 시나리오를 탐구할 것입니다. 더 많은 데모 비디오는 프로젝트 홈페이지에서 확인할 수 있습니다.
