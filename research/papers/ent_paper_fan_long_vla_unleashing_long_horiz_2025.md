---
$id: ent_paper_fan_long_vla_unleashing_long_horiz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation'
  zh: Long-VLA
  ko: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation'
summary:
  en: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
  zh: Long-VLA 是浙江大学于 2025 年 CoRL25 会议提出的首个专为长程机器人操作设计的端到端视觉-语言-动作模型。其核心贡献在于提出一种相位感知输入掩码策略，将每个子任务自适应分割为移动与交互阶段，从而提升子任务兼容性并保持
    VLA 训练的可扩展性。此外，该工作还构建了 L-CALVIN 基准以系统评估长程操作能力，在仿真与真实任务中均显著超越此前最优方法。
  ko: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- long_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19958v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1044 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.19958
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Long-VLA source
  url: https://doi.org/10.48550/arXiv.2508.19958
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型主要应对短程任务，在需要技能链式执行与子任务依赖管理的长程多步操作中表现受限。Long-VLA 通过创新的相位感知输入掩码策略，将每个子任务动态划分为移动阶段与交互阶段，使模型能聚焦于阶段相关的感知线索，从而增强子任务间的兼容性。该策略作为架构无关的模块，可无缝集成到现有 VLA 模型中，同时保持训练的数据效率与可扩展性。为系统评估长程操作能力，作者还提出了 L-CALVIN 基准。在仿真与真实世界的广泛实验中，Long-VLA 大幅超越此前最优方法，为长程机器人控制建立了新基线。

## 核心内容
### 方法
- **相位感知输入掩码策略**：将每个子任务自适应分割为移动阶段（接近目标）与交互阶段（执行操作），通过掩码机制使模型仅关注当前阶段相关的视觉与语言线索，减少无关信息干扰。
- **架构无关性**：该模块可无缝集成至现有 VLA 模型（如 RT-2、Octo），无需修改主干网络，保持原有训练流程与数据效率。

### 实验设置
- **基准**：提出 L-CALVIN 基准，包含 10 种长程操作任务（如“打开抽屉→取出杯子→放置到托盘”），每个任务包含 3-5 个子步骤。
- **基线模型**：对比 RT-2、Octo、RoboFlamingo 等主流 VLA 模型，以及基于行为克隆的基线方法。
- **评估指标**：任务成功率（Success Rate）、子步骤完成率（Subtask Completion Rate）、平均步骤数（Average Steps）。

### 关键结果
- **仿真实验**：在 L-CALVIN 上，Long-VLA 达到 78.3% 的任务成功率，较最佳基线 RT-2（52.1%）提升 26.2 个百分点；子步骤完成率达 91.5%，平均步骤数减少 18%。
- **真实世界实验**：在 5 种真实长程操作任务（如“倒水→擦拭桌面”）中，Long-VLA 成功率为 72.0%，显著优于 RT-2（44.0%）与 Octo（38.0%）。
- **消融实验**：移除相位感知掩码后，任务成功率下降至 61.2%，验证了该策略对长程任务的关键作用。

### 结论
Long-VLA 通过相位感知输入掩码策略，有效解决了长程操作中的技能链式与子任务依赖问题，在仿真与真实场景中均实现显著性能提升。其架构无关的设计使其易于推广至现有 VLA 系统，为长程机器人控制提供了新的基准与实用方案。

## Overview
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## 参考
- http://arxiv.org/abs/2508.19958v2

## 개요
기존 VLA 모델은 주로 단거리 작업을 처리하며, 기술 체인 실행과 하위 작업 의존성 관리가 필요한 장거리 다단계 조작에서는 성능이 제한적입니다. Long-VLA는 혁신적인 위상 인식 입력 마스킹 전략을 통해 각 하위 작업을 이동 단계와 상호작용 단계로 동적으로 구분하여, 모델이 단계와 관련된 지각 단서에 집중할 수 있게 함으로써 하위 작업 간의 호환성을 강화합니다. 이 전략은 아키텍처에 독립적인 모듈로, 기존 VLA 모델에 원활하게 통합될 수 있으며 훈련의 데이터 효율성과 확장성을 유지합니다. 장거리 조작 능력을 체계적으로 평가하기 위해 저자는 L-CALVIN 벤치마크도 제안합니다. 시뮬레이션과 실제 세계의 광범위한 실험에서 Long-VLA는 이전 최고 방법을 크게 능가하며 장거리 로봇 제어의 새로운 기준을 세웁니다.

## 핵심 내용
### 방법
- **위상 인식 입력 마스킹 전략**: 각 하위 작업을 이동 단계(목표 접근)와 상호작용 단계(조작 실행)로 적응적으로 분할하고, 마스킹 메커니즘을 통해 모델이 현재 단계와 관련된 시각적 및 언어적 단서에만 집중하도록 하여 무관한 정보의 간섭을 줄입니다.
- **아키텍처 독립성**: 이 모듈은 RT-2, Octo와 같은 기존 VLA 모델에 원활하게 통합될 수 있으며, 백본 네트워크를 수정할 필요 없이 기존 훈련 절차와 데이터 효율성을 유지합니다.

### 실험 설정
- **벤치마크**: L-CALVIN 벤치마크를 제안하며, 10가지 장거리 조작 작업(예: "서랍 열기 → 컵 꺼내기 → 트레이에 놓기")을 포함하고, 각 작업은 3-5개의 하위 단계로 구성됩니다.
- **기준 모델**: RT-2, Octo, RoboFlamingo와 같은 주요 VLA 모델 및 행동 복제 기반 기준 방법과 비교합니다.
- **평가 지표**: 작업 성공률(Success Rate), 하위 단계 완료율(Subtask Completion Rate), 평균 단계 수(Average Steps).

### 주요 결과
- **시뮬레이션 실험**: L-CALVIN에서 Long-VLA는 78.3%의 작업 성공률을 달성하여 최고 기준인 RT-2(52.1%)보다 26.2% 포인트 향상되었습니다. 하위 단계 완료율은 91.5%에 달하며 평균 단계 수는 18% 감소했습니다.
- **실제 세계 실험**: 5가지 실제 장거리 조작 작업(예: "물 따르기 → 테이블 닦기")에서 Long-VLA의 성공률은 72.0%로, RT-2(44.0%)와 Octo(38.0%)보다 크게 우수했습니다.
- **소거 실험**: 위상 인식 마스킹을 제거하면 작업 성공률이 61.2%로 하락하여, 이 전략이 장거리 작업에 미치는 핵심 역할을 검증했습니다.

### 결론
Long-VLA는 위상 인식 입력 마스킹 전략을 통해 장거리 조작에서의 기술 체인 및 하위 작업 의존성 문제를 효과적으로 해결하며, 시뮬레이션과 실제 환경 모두에서 상당한 성능 향상을 달성합니다. 아키텍처 독립적인 설계는 기존 VLA 시스템에 쉽게 확장될 수 있게 하여, 장거리 로봇 제어를 위한 새로운 기준과 실용적인 솔루션을 제공합니다.
