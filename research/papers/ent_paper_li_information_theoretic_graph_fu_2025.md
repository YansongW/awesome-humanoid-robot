---
$id: ent_paper_li_information_theoretic_graph_fu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control
  zh: GF-VLA
  ko: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control
summary:
  en: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control (GF-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Alabama at Birmingham.
  zh: GF-VLA 是一个由阿拉巴马大学伯明翰分校于2025年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过信息论图融合技术，从人类演示中提取任务相关线索并生成场景图，结合语言条件Transformer生成层次化行为树，实现双机械臂的任务级推理与执行。实验在四种双机械臂组装任务中达到94%抓取成功率和90%整体任务成功率。
  ko: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control (GF-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Alabama at Birmingham.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gf_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.05342v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1016 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control
    (arXiv)
  url: https://arxiv.org/abs/2508.05342
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GF-VLA source
  url: https://doi.org/10.48550/arXiv.2508.05342
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
GF-VLA 框架旨在解决从人类视频中教授机器人灵巧技能时，因依赖低级轨迹模仿而难以泛化到不同物体类型、空间布局和机械臂配置的问题。该框架首先利用基于Shannon信息论的线索提取，识别与任务最相关的手和物体，并将其编码为时间有序的场景图，捕捉手-物体和物体-物体交互。随后，这些场景图与语言条件Transformer融合，生成层次化行为树和可解释的笛卡尔运动命令。此外，为提升双机械臂执行效率，GF-VLA引入跨手选择策略，无需显式几何推理即可推断最优夹爪分配。实验在四种结构化双机械臂组装任务（包括符号形状构建和空间泛化）中验证了其有效性。

## 核心内容
### 方法
- **信息论线索提取**：GF-VLA 首先从RGB和深度人类演示中提取基于Shannon信息论的线索，识别与任务最相关的手和物体，减少冗余信息。
- **场景图编码**：将提取的线索编码为时间有序的场景图，明确表示手-物体和物体-物体交互，为后续推理提供结构化输入。
- **语言条件Transformer**：场景图与语言条件Transformer融合，生成层次化行为树（Behavior Trees）和可解释的笛卡尔运动命令，支持任务级推理。
- **跨手选择策略**：针对双机械臂场景，引入跨手选择策略，无需显式几何推理即可推断最优夹爪分配，提升执行效率。

### 实验设置
- **任务**：在四种结构化双机械臂组装任务上评估，包括符号形状构建（如堆叠、字母构建）和空间泛化（如几何重配置）。
- **评估指标**：图准确率、子任务分割准确率、抓取成功率、放置准确率、整体任务成功率。

### 关键数字
- **图准确率**：超过95%，表明信息论场景表示能准确捕捉任务相关交互。
- **子任务分割**：93%准确率，支持LLM规划器生成可靠且可读的任务策略。
- **执行性能**：
  - 抓取成功率：94%
  - 放置准确率：89%
  - 整体任务成功率：90%（涵盖堆叠、字母构建和几何重配置场景）
- **泛化能力**：在多样空间和语义变化下表现出强鲁棒性。

### 结论
GF-VLA 通过信息论图融合和语言条件Transformer，有效解决了从人类视频学习双机械臂灵巧技能的泛化问题。其场景表示和跨手选择策略显著提升了任务推理和执行效率，在结构化组装任务中达到高成功率，展示了在复杂机器人操作中的潜力。

## Overview
Teaching robots dexterous skills from human videos remains challenging due to the reliance on low-level trajectory imitation, which fails to generalize across object types, spatial layouts, and manipulator configurations. We propose Graph-Fused Vision-Language-Action (GF-VLA), a framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB and Depth human demonstrations. GF-VLA first extracts Shannon-information-based cues to identify hands and objects with the highest task relevance, then encodes these cues into temporally ordered scene graphs that capture both hand-object and object-object interactions. These graphs are fused with a language-conditioned transformer that generates hierarchical behavior trees and interpretable Cartesian motion commands. To improve execution efficiency in bimanual settings, we further introduce a cross-hand selection policy that infers optimal gripper assignment without explicit geometric reasoning. We evaluate GF-VLA on four structured dual-arm block assembly tasks involving symbolic shape construction and spatial generalization. Experimental results show that the information-theoretic scene representation achieves over 95 percent graph accuracy and 93 percent subtask segmentation, supporting the LLM planner in generating reliable and human-readable task policies. When executed by the dual-arm robot, these policies yield 94 percent grasp success, 89 percent placement accuracy, and 90 percent overall task success across stacking, letter-building, and geometric reconfiguration scenarios, demonstrating strong generalization and robustness across diverse spatial and semantic variations.

## 参考
- http://arxiv.org/abs/2508.05342v2

## 개요
GF-VLA 프레임워크는 인간 비디오에서 로봇의 손재주 기술을 가르칠 때, 저수준 궤적 모방에 의존하여 다양한 객체 유형, 공간 배치 및 로봇 팔 구성으로 일반화하기 어려운 문제를 해결하는 것을 목표로 합니다. 이 프레임워크는 먼저 Shannon 정보 이론 기반의 단서 추출을 활용하여 작업과 가장 관련된 손과 객체를 식별하고, 이를 시간 순서화된 장면 그래프로 인코딩하여 손-객체 및 객체-객체 상호작용을 포착합니다. 이후 이러한 장면 그래프는 언어 조건 Transformer와 융합되어 계층적 행동 트리와 해석 가능한 데카르트 운동 명령을 생성합니다. 또한, 이중 로봇 팔 실행 효율성을 향상시키기 위해 GF-VLA는 명시적 기하 추론 없이 최적의 그리퍼 할당을 추론할 수 있는 교차 손 선택 전략을 도입합니다. 실험은 네 가지 구조화된 이중 로봇 팔 조립 작업(기호 모양 구축 및 공간 일반화 포함)에서 그 효과를 검증합니다.

## 핵심 내용
### 방법
- **정보 이론 단서 추출**: GF-VLA는 먼저 RGB 및 깊이 인간 시연에서 Shannon 정보 이론 기반의 단서를 추출하여 작업과 가장 관련된 손과 객체를 식별하고 중복 정보를 줄입니다.
- **장면 그래프 인코딩**: 추출된 단서를 시간 순서화된 장면 그래프로 인코딩하여 손-객체 및 객체-객체 상호작용을 명시적으로 표현하고, 후속 추론을 위한 구조화된 입력을 제공합니다.
- **언어 조건 Transformer**: 장면 그래프는 언어 조건 Transformer와 융합되어 계층적 행동 트리(Behavior Trees)와 해석 가능한 데카르트 운동 명령을 생성하여 작업 수준 추론을 지원합니다.
- **교차 손 선택 전략**: 이중 로봇 팔 시나리오를 위해 교차 손 선택 전략을 도입하여 명시적 기하 추론 없이 최적의 그리퍼 할당을 추론하고 실행 효율성을 향상시킵니다.

### 실험 설정
- **작업**: 네 가지 구조화된 이중 로봇 팔 조립 작업에서 평가되며, 기호 모양 구축(예: 쌓기, 문자 구축) 및 공간 일반화(예: 기하 재구성)를 포함합니다.
- **평가 지표**: 그래프 정확도, 하위 작업 분할 정확도, 그리핑 성공률, 배치 정확도, 전체 작업 성공률.

### 주요 수치
- **그래프 정확도**: 95% 이상으로, 정보 이론 장면 표현이 작업 관련 상호작용을 정확히 포착함을 나타냅니다.
- **하위 작업 분할**: 93% 정확도로, LLM 플래너가 신뢰할 수 있고 읽기 쉬운 작업 전략을 생성하도록 지원합니다.
- **실행 성능**:
  - 그리핑 성공률: 94%
  - 배치 정확도: 89%
  - 전체 작업 성공률: 90%(쌓기, 문자 구축 및 기하 재구성 시나리오 포함)
- **일반화 능력**: 다양한 공간 및 의미 변화에서 강한 견고성을 보여줍니다.

### 결론
GF-VLA는 정보 이론 그래프 융합과 언어 조건 Transformer를 통해 인간 비디오에서 이중 로봇 팔 손재주 기술을 학습할 때의 일반화 문제를 효과적으로 해결합니다. 그 장면 표현과 교차 손 선택 전략은 작업 추론 및 실행 효율성을 크게 향상시키며, 구조화된 조립 작업에서 높은 성공률을 달성하여 복잡한 로봇 조작에서의 잠재력을 보여줍니다.
