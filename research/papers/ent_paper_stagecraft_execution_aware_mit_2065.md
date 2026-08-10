---
$id: ent_paper_stagecraft_execution_aware_mit_2065
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
  zh: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
  ko: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
summary:
  en: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
  zh: StageCraft 是一种无需训练的即插即用模块，通过利用大型视觉语言模型（VLM）的上下文推理能力，在机器人执行任务前调整环境初始状态，从而缓解视觉语言动作模型（VLA）因干扰物或物理障碍导致的执行失败。该方法在三个真实世界任务域中实现了绝对性能提升40%，并在RLBench仿真实验中验证了其干预程度可随底层策略强度自适应调整。
  ko: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
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
- robotics
- stagecraft
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.20659v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1072 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models (arXiv)'
  url: https://arxiv.org/abs/2603.20659
  date: '2065'
  accessed_at: '2026-07-08'
---
## 概述
现有VLA模型虽经大规模预训练能泛化至新任务，但在执行阶段仍易受工作空间内干扰物或物理障碍的影响。StageCraft通过输入策略执行视频与成功标签，借助VLM的推理能力识别初始状态中需调整的物体，从而避免预期失败。该方法不依赖额外训练，仅需少量策略执行样本即可工作，且不改变底层策略的约束条件。实验表明，StageCraft在真实场景中显著提升了多种先进VLA模型的鲁棒性，并在仿真中展示了随上下文样本增加而性能持续改善的特性。

## 核心内容
### 方法概述
StageCraft 的核心思想是利用互联网规模预训练的VLM（如GPT-4V）进行上下文推理，在机器人执行任务前对环境初始状态进行“装饰性”调整。具体流程如下：
- **输入**：策略执行视频（policy rollout videos）与对应的成功/失败标签。
- **推理**：VLM分析视频中失败原因（如干扰物位置不当或障碍物阻挡），推断初始状态中哪些物体需要被移动、移除或重新排列。
- **干预**：基于VLM的推理结果，通过机械臂或外部系统调整初始状态，再重新执行策略。

### 架构特点
- **无需训练**：StageCraft 不修改底层VLA策略的权重，仅作为外部模块介入。
- **即插即用**：可无缝集成至任何VLA模型（如RT-2、Octo等），不引入额外约束。
- **样本高效**：仅需少量（通常3-5次）策略执行视频即可触发有效干预。

### 实验设置与关键结果
- **真实世界任务**：在三个任务域（桌面操作、抓取放置、障碍物避让）中，引入多种干扰物（如随机物体、动态障碍）和物理阻塞。StageCraft 使VLA策略的绝对成功率提升40%（例如从50%提升至90%）。
- **仿真实验（RLBench）**：验证了干预程度与底层策略强度的关系——当策略本身较弱时，StageCraft 会进行更频繁的初始状态调整；随着上下文样本（in-context samples）数量增加（从1个增至5个），性能持续提升，表明VLM的推理能力随示例丰富而增强。
- **消融实验**：对比直接微调VLA策略的方法，StageCraft 在未见过的干扰物设置下表现更优，且无需收集额外训练数据。

### 结论
StageCraft 通过VLM的上下文推理，以零训练成本显著提升了VLA模型在复杂动态环境中的鲁棒性。其模块化设计使其易于扩展至更多任务，且干预程度可自适应调整。未来工作可探索更高效的VLM推理策略或结合多模态反馈。

## Overview
Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/ .

## 参考
- http://arxiv.org/abs/2603.20659v2

## 개요
기존 VLA 모델은 대규모 사전 학습을 통해 새로운 작업에 일반화할 수 있지만, 실행 단계에서 작업 공간 내 방해물이나 물리적 장애물의 영향을 여전히 받기 쉽습니다. StageCraft는 정책 실행 비디오와 성공 레이블을 입력으로 사용하고, VLM의 추론 능력을 활용하여 초기 상태에서 조정이 필요한 객체를 식별함으로써 예상되는 실패를 방지합니다. 이 방법은 추가 훈련에 의존하지 않으며, 소량의 정책 실행 샘플만으로 작동하고, 기본 정책의 제약 조건을 변경하지 않습니다. 실험 결과, StageCraft는 실제 환경에서 여러 최신 VLA 모델의 견고성을 크게 향상시켰으며, 시뮬레이션에서도 컨텍스트 샘플이 증가함에 따라 성능이 지속적으로 개선되는 특성을 보여주었습니다.

## 핵심 내용
### 방법 개요
StageCraft의 핵심 아이디어는 인터넷 규모로 사전 학습된 VLM(예: GPT-4V)을 활용한 컨텍스트 추론을 통해, 로봇이 작업을 실행하기 전에 환경의 초기 상태를 "장식적으로" 조정하는 것입니다. 구체적인 절차는 다음과 같습니다:
- **입력**: 정책 실행 비디오(policy rollout videos)와 해당 성공/실패 레이블.
- **추론**: VLM이 비디오에서 실패 원인(예: 방해물의 부적절한 위치 또는 장애물 차단)을 분석하고, 초기 상태에서 이동, 제거 또는 재배열이 필요한 객체를 추론합니다.
- **개입**: VLM의 추론 결과를 기반으로 로봇 팔 또는 외부 시스템을 통해 초기 상태를 조정한 후, 정책을 다시 실행합니다.

### 아키텍처 특징
- **훈련 불필요**: StageCraft는 기본 VLA 정책의 가중치를 수정하지 않으며, 외부 모듈로만 개입합니다.
- **플러그 앤 플레이**: RT-2, Octo 등 모든 VLA 모델에 원활하게 통합될 수 있으며, 추가 제약을 도입하지 않습니다.
- **샘플 효율성**: 소량(일반적으로 3-5회)의 정책 실행 비디오만으로 효과적인 개입을 유도할 수 있습니다.

### 실험 설정 및 주요 결과
- **실제 세계 작업**: 세 가지 작업 영역(테이블 조작, 집기-배치, 장애물 회피)에서 다양한 방해물(예: 무작위 객체, 동적 장애물)과 물리적 차단을 도입했습니다. StageCraft는 VLA 정책의 절대 성공률을 40% 향상시켰습니다(예: 50%에서 90%로).
- **시뮬레이션 실험(RLBench)**: 개입 정도와 기본 정책 강도 간의 관계를 검증했습니다——정책 자체가 약할 때 StageCraft는 더 빈번하게 초기 상태를 조정합니다. 컨텍스트 샘플(in-context samples) 수가 증가함에 따라(1개에서 5개로), 성능이 지속적으로 향상되어 VLM의 추론 능력이 예제가 풍부해질수록 강화됨을 보여줍니다.
- **절제 실험**: VLA 정책을 직접 미세 조정하는 방법과 비교했을 때, StageCraft는 보지 못한 방해물 설정에서 더 우수한 성능을 보였으며, 추가 훈련 데이터 수집이 필요하지 않습니다.

### 결론
StageCraft는 VLM의 컨텍스트 추론을 통해 훈련 비용 없이 VLA 모델의 복잡한 동적 환경에서의 견고성을 크게 향상시킵니다. 모듈식 설계로 더 많은 작업으로 쉽게 확장할 수 있으며, 개입 정도는 적응적으로 조정될 수 있습니다. 향후 연구에서는 더 효율적인 VLM 추론 전략이나 다중 모달 피드백 통합을 탐구할 수 있습니다.
