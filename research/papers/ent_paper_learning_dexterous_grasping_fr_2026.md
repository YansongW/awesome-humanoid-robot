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
  zh: 'arXiv:2604.04138v2 Announce Type: replace Abstract: Dexterous manipulation requires planning a grasp configuration
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04138v2.
sources:
- id: src_001
  type: paper
  title: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  url: https://arxiv.org/abs/2604.04138
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Dexterous manipulation requires planning a grasp configuration suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur. To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command, a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship, GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover, real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy selection based on object geometry and task intent.

## 核心内容
Dexterous manipulation requires planning a grasp configuration suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur. To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command, a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship, GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover, real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy selection based on object geometry and task intent.

## 参考
- http://arxiv.org/abs/2604.04138v2

## Overview
Dexterous manipulation requires planning a grasp configuration suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur. To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command, a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship, GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover, real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy selection based on object geometry and task intent.

## Content
Dexterous manipulation requires planning a grasp configuration suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur. To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command, a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship, GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover, real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy selection based on object geometry and task intent.

## 개요
정밀한 조작은 객체와 작업에 적합한 파지 구성을 계획한 후, 이를 조정된 다지 제어를 통해 실행해야 합니다. 그러나 모든 객체와 작업에 대해 조밀한 자세나 접촉 목표를 가진 파지 계획을 지정하는 것은 비현실적입니다. 한편, 작업 보상만으로 종단간 강화 학습을 수행하면 제어 가능성이 부족하여 실패 발생 시 사용자가 개입하기 어렵습니다. 이를 위해 우리는 희소 분류 체계 지침을 통해 정밀한 제어를 학습하는 2단계 프레임워크인 GRIT을 제시합니다. GRIT은 먼저 장면 및 작업 맥락에서 분류 체계 기반의 파지 사양을 예측합니다. 이 희소 명령에 따라 정책은 의도된 파지 구조를 유지하면서 작업을 완료하는 연속적인 손가락 움직임을 생성합니다. 우리의 결과는 특정 객체 형상에 대해 특정 파지 분류 체계가 더 효과적임을 보여줍니다. 이 관계를 활용함으로써 GRIT은 기준 모델 대비 새로운 객체에 대한 일반화를 개선하고 전체 성공률 87.9%를 달성합니다. 또한 실제 환경 실험을 통해 객체 형상과 작업 의도에 기반한 고수준 분류 체계 선택을 통해 파지 전략을 조정할 수 있는 제어 가능성을 입증합니다.

## 핵심 내용
정밀한 조작은 객체와 작업에 적합한 파지 구성을 계획한 후, 이를 조정된 다지 제어를 통해 실행해야 합니다. 그러나 모든 객체와 작업에 대해 조밀한 자세나 접촉 목표를 가진 파지 계획을 지정하는 것은 비현실적입니다. 한편, 작업 보상만으로 종단간 강화 학습을 수행하면 제어 가능성이 부족하여 실패 발생 시 사용자가 개입하기 어렵습니다. 이를 위해 우리는 희소 분류 체계 지침을 통해 정밀한 제어를 학습하는 2단계 프레임워크인 GRIT을 제시합니다. GRIT은 먼저 장면 및 작업 맥락에서 분류 체계 기반의 파지 사양을 예측합니다. 이 희소 명령에 따라 정책은 의도된 파지 구조를 유지하면서 작업을 완료하는 연속적인 손가락 움직임을 생성합니다. 우리의 결과는 특정 객체 형상에 대해 특정 파지 분류 체계가 더 효과적임을 보여줍니다. 이 관계를 활용함으로써 GRIT은 기준 모델 대비 새로운 객체에 대한 일반화를 개선하고 전체 성공률 87.9%를 달성합니다. 또한 실제 환경 실험을 통해 객체 형상과 작업 의도에 기반한 고수준 분류 체계 선택을 통해 파지 전략을 조정할 수 있는 제어 가능성을 입증합니다.
