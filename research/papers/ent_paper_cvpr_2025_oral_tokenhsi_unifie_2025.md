---
$id: ent_paper_cvpr_2025_oral_tokenhsi_unifie_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
  zh: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
  ko: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
summary:
  en: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
  zh: TokenHSI 是 CVPR 2025 Oral 论文，提出一种基于 Transformer 的统一策略，用于合成多样且物理合理的人-场景交互（HSI）。其核心创新在于将人形机器人本体感觉建模为共享令牌，并通过掩码机制与不同任务令牌组合，实现多技能统一与灵活适应。该方法在多种
    HSI 任务中显著提升了通用性、适应性和可扩展性。
  ko: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- cvpr_2025_oral_tokenhsi
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.19901v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (897 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization (arXiv)'
  url: https://arxiv.org/abs/2503.19901
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization project
    page'
  url: https://liangpan99.github.io/TokenHSI/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前 HSI 合成方法主要针对单一交互任务开发独立控制器，难以应对需要多技能整合的复杂任务（如携带物体坐下）。TokenHSI 通过统一 Transformer 策略解决此问题，将人形机器人本体感觉作为共享令牌，与不同任务令牌通过掩码机制结合，实现跨技能知识共享与多任务训练。该策略支持可变长度输入，可灵活适应新场景，并通过训练额外任务分词器修改交互目标几何形状或协调多技能处理复杂任务。

## 核心内容
### 方法架构
- **统一策略设计**：基于 Transformer 架构，将人形机器人本体感觉（如关节角度、速度）编码为共享令牌，与不同交互任务（如坐、搬物）对应的任务令牌通过掩码机制组合。掩码机制允许策略在推理时动态选择相关任务令牌，实现多技能统一。
- **可变长度输入**：策略支持输入不同数量的任务令牌，从而灵活适应新场景（如不同几何形状的椅子）或组合多个技能（如先搬物后坐下）。

### 实验设置
- **任务范围**：涵盖多种 HSI 任务，包括坐、搬物、推拉物体等，以及需要多技能整合的复合任务（如携带物体坐下）。
- **对比基线**：与专门为单一任务训练的独立控制器（如基于强化学习的控制器）进行比较，评估通用性、适应性和可扩展性。

### 关键结果
- **多技能统一**：TokenHSI 在单一策略中成功整合多种交互技能，无需为每个任务单独训练控制器，显著提升训练效率。
- **适应性**：通过训练额外任务分词器，策略可适应不同几何形状的交互目标（如不同高度或宽度的椅子），无需重新训练整个策略。
- **复合任务**：在需要多技能协调的复合任务（如携带物体坐下）中，TokenHSI 优于独立控制器组合，实现更自然、物理合理的交互。
- **定量指标**：在成功率、物理合理性（如接触力、关节力矩）和多样性（如不同交互轨迹）上均优于基线方法。

### 结论
TokenHSI 通过任务令牌化与统一 Transformer 策略，有效解决了 HSI 合成中多技能整合与灵活适应的问题，为物理角色动画和具身 AI 提供了可扩展的解决方案。

## Overview
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## 参考
- http://arxiv.org/abs/2503.19901v2

## 개요
현재 HSI 합성 방법은 주로 단일 상호작용 작업을 위해 독립 컨트롤러를 개발하며, 다중 기술 통합이 필요한 복잡한 작업(예: 물체를 들고 앉기)을 처리하기 어렵습니다. TokenHSI는 통합 Transformer 정책을 통해 이 문제를 해결하며, 휴머노이드 로봇의 고유 감각을 공유 토큰으로 사용하고, 다양한 작업 토큰과 마스크 메커니즘을 통해 결합하여 교차 기술 지식 공유와 다중 작업 훈련을 구현합니다. 이 정책은 가변 길이 입력을 지원하여 새로운 시나리오에 유연하게 적응할 수 있으며, 추가 작업 토크나이저를 훈련하여 상호작용 목표의 기하학적 형태를 수정하거나 다중 기술을 조정하여 복잡한 작업을 처리할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **통합 정책 설계**: Transformer 아키텍처를 기반으로 휴머노이드 로봇의 고유 감각(예: 관절 각도, 속도)을 공유 토큰으로 인코딩하고, 다양한 상호작용 작업(예: 앉기, 물건 옮기기)에 해당하는 작업 토큰과 마스크 메커니즘을 통해 결합합니다. 마스크 메커니즘은 정책이 추론 시 관련 작업 토큰을 동적으로 선택할 수 있게 하여 다중 기술 통합을 구현합니다.
- **가변 길이 입력**: 정책은 다양한 수의 작업 토큰 입력을 지원하여 새로운 시나리오(예: 다른 기하학적 형태의 의자)에 유연하게 적응하거나 여러 기술을 결합할 수 있습니다(예: 먼저 물건을 옮긴 후 앉기).

### 실험 설정
- **작업 범위**: 앉기, 물건 옮기기, 물체 밀고 당기기 등 다양한 HSI 작업과 다중 기술 통합이 필요한 복합 작업(예: 물체를 들고 앉기)을 포함합니다.
- **비교 기준선**: 단일 작업 훈련을 위해 특별히 설계된 독립 컨트롤러(예: 강화 학습 기반 컨트롤러)와 비교하여 일반성, 적응성 및 확장성을 평가합니다.

### 주요 결과
- **다중 기술 통합**: TokenHSI는 단일 정책에서 여러 상호작용 기술을 성공적으로 통합하며, 각 작업에 대해 별도로 컨트롤러를 훈련할 필요 없이 훈련 효율성을 크게 향상시킵니다.
- **적응성**: 추가 작업 토크나이저를 훈련함으로써 정책은 다른 기하학적 형태의 상호작용 목표(예: 다른 높이 또는 너비의 의자)에 적응할 수 있으며, 전체 정책을 재훈련할 필요가 없습니다.
- **복합 작업**: 다중 기술 조정이 필요한 복합 작업(예: 물체를 들고 앉기)에서 TokenHSI는 독립 컨트롤러 조합보다 우수하여 더 자연스럽고 물리적으로 합리적인 상호작용을 구현합니다.
- **정량적 지표**: 성공률, 물리적 합리성(예: 접촉력, 관절 토크) 및 다양성(예: 다양한 상호작용 궤적)에서 기준선 방법보다 우수합니다.

### 결론
TokenHSI는 작업 토큰화와 통합 Transformer 정책을 통해 HSI 합성에서 다중 기술 통합과 유연한 적응 문제를 효과적으로 해결하며, 물리적 캐릭터 애니메이션과 구현 AI를 위한 확장 가능한 솔루션을 제공합니다.
