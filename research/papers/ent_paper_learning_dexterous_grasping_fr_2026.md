---
$id: ent_paper_learning_dexterous_grasping_fr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  zh: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  ko: Learning Dexterous Grasping from Sparse Taxonomy Guidance
summary:
  en: 'arXiv:2604.04138v2 Announce Type: replace Abstract: Dexterous manipulation requires planning a grasp configuration
    suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp
    plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement
    learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur.
    To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT
    first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command,
    a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our
    result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship,
    GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover,
    real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy
    selection based on object geometry and task intent.'
  zh: GRIT是一个两阶段框架，通过稀疏分类学指导学习灵巧操控。它首先从场景和任务上下文中预测基于分类学的抓取规范，然后由策略生成连续手指运动以完成任务。该方法在实验中达到87.9%的整体成功率，并展现出对新颖物体的良好泛化能力和用户可控性。
  ko: 'arXiv:2604.04138v2 Announce Type: replace Abstract: Dexterous manipulation requires planning a grasp configuration
    suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp
    plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement
    learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur.
    To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT
    first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command,
    a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our
    result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship,
    GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover,
    real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy
    selection based on object geometry and task intent.'
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
- learning_dexterous_grasping_fr
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04138v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (643 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  url: https://arxiv.org/abs/2604.04138
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
GRIT框架解决了灵巧操控中密集位姿或接触目标指定不切实际，以及端到端强化学习缺乏可控性的问题。它采用两阶段设计：第一阶段从场景和任务上下文预测基于分类学的抓取规范，第二阶段基于该稀疏指令生成连续手指运动。实验表明，特定抓取分类学对特定物体几何形状更有效，GRIT利用这一关系在基线方法上提升了泛化能力，整体成功率达到87.9%。真实世界实验还验证了其可控性，允许用户通过高层分类学选择调整抓取策略。

## 核心内容
### 方法
GRIT框架包含两个阶段：
- **第一阶段**：从场景和任务上下文中预测基于分类学的抓取规范（taxonomy-based grasp specification）。该规范是稀疏的，避免了为每个物体和任务指定密集位姿或接触目标。
- **第二阶段**：基于第一阶段输出的稀疏指令，策略生成连续手指运动，在完成任务的同时保持预期的抓取结构。

### 实验设置
- 在仿真环境和真实世界中进行实验。
- 基线方法包括端到端强化学习等。

### 关键结果
- GRIT整体成功率达到87.9%。
- 特定抓取分类学对特定物体几何形状更有效，GRIT利用这一关系提升了对新颖物体的泛化能力。
- 真实世界实验验证了可控性：用户可通过高层分类学选择，基于物体几何形状和任务意图调整抓取策略。

### 结论
GRIT通过稀疏分类学指导，实现了灵巧操控的高成功率和可控性，同时避免了密集标注的负担。其泛化能力和用户干预能力使其适用于实际应用场景。

## Overview
Dexterous manipulation requires planning a grasp configuration suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur. To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command, a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship, GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover, real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy selection based on object geometry and task intent.

## 参考
- http://arxiv.org/abs/2604.04138v2

## 개요
GRIT 프레임워크는 정밀 조작에서 밀집된 자세 또는 접촉 목표 지정이 비현실적인 문제와 엔드투엔드 강화 학습의 제어 가능성 부족 문제를 해결합니다. 이는 두 단계 설계를 채택합니다: 첫 번째 단계는 장면 및 작업 맥락에서 분류학 기반 파지 사양을 예측하고, 두 번째 단계는 해당 희소 명령을 기반으로 연속적인 손가락 움직임을 생성합니다. 실험 결과, 특정 파지 분류학이 특정 물체 기하학적 형태에 더 효과적이며, GRIT는 이 관계를 활용하여 기준 방법 대비 일반화 능력을 향상시켜 전체 성공률 87.9%를 달성했습니다. 실제 세계 실험은 또한 사용자가 고수준 분류학 선택을 통해 파지 전략을 조정할 수 있는 제어 가능성을 검증했습니다.

## 핵심 내용
### 방법
GRIT 프레임워크는 두 단계로 구성됩니다:
- **첫 번째 단계**: 장면 및 작업 맥락에서 분류학 기반 파지 사양을 예측합니다. 이 사양은 희소하며, 각 물체와 작업에 대해 밀집된 자세 또는 접촉 목표를 지정하는 것을 피합니다.
- **두 번째 단계**: 첫 번째 단계에서 출력된 희소 명령을 기반으로 정책이 연속적인 손가락 움직임을 생성하여, 예상된 파지 구조를 유지하면서 작업을 완료합니다.

### 실험 설정
- 시뮬레이션 환경과 실제 세계에서 실험을 수행합니다.
- 기준 방법에는 엔드투엔드 강화 학습 등이 포함됩니다.

### 주요 결과
- GRIT의 전체 성공률은 87.9%입니다.
- 특정 파지 분류학이 특정 물체 기하학적 형태에 더 효과적이며, GRIT는 이 관계를 활용하여 새로운 물체에 대한 일반화 능력을 향상시킵니다.
- 실제 세계 실험은 제어 가능성을 검증했습니다: 사용자는 고수준 분류학 선택을 통해 물체 기하학적 형태와 작업 의도에 기반하여 파지 전략을 조정할 수 있습니다.

### 결론
GRIT는 희소 분류학 지침을 통해 정밀 조작의 높은 성공률과 제어 가능성을 달성하면서 밀집 주석의 부담을 피합니다. 그 일반화 능력과 사용자 개입 가능성은 실제 응용 시나리오에 적합하게 만듭니다.
