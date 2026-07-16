---
$id: ent_paper_adapting_generalist_robot_poli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
  zh: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
  ko: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
summary:
  en: 'arXiv:2606.31958v1 Announce Type: new Abstract: Generalist robot policies learn a diverse repertoire of behaviors from
    large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning
    (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring
    the base policy''s action distribution to be close to that of a performant policy from the start. This assumption breaks
    down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently
    expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks:
    modulating language inputs elicits skills already within the policy''s repertoire, which can be composed to solve tasks
    beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize
    this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly,
    leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration
    and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world
    behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally
    new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing
    approaches for improving robot behavior in deployment.'
  zh: 'arXiv:2606.31958v1 Announce Type: new Abstract: Generalist robot policies learn a diverse repertoire of behaviors from
    large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning
    (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring
    the base policy''s action distribution to be close to that of a performant policy from the start. This assumption breaks
    down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently
    expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks:
    modulating language inputs elicits skills already within the policy''s repertoire, which can be composed to solve tasks
    beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize
    this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly,
    leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration
    and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world
    behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally
    new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing
    approaches for improving robot behavior in deployment.'
  ko: 'arXiv:2606.31958v1 Announce Type: new Abstract: Generalist robot policies learn a diverse repertoire of behaviors from
    large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning
    (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring
    the base policy''s action distribution to be close to that of a performant policy from the start. This assumption breaks
    down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently
    expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks:
    modulating language inputs elicits skills already within the policy''s repertoire, which can be composed to solve tasks
    beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize
    this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly,
    leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration
    and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world
    behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally
    new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing
    approaches for improving robot behavior in deployment.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adapting_generalist_robot_poli
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31958v1.
sources:
- id: src_001
  type: paper
  title: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
  url: https://arxiv.org/abs/2606.31958
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks: modulating language inputs elicits skills already within the policy's repertoire, which can be composed to solve tasks beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly, leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing approaches for improving robot behavior in deployment.

## 核心内容
Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks: modulating language inputs elicits skills already within the policy's repertoire, which can be composed to solve tasks beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly, leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing approaches for improving robot behavior in deployment.

## 参考
- http://arxiv.org/abs/2606.31958v1

## Overview
Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks: modulating language inputs elicits skills already within the policy's repertoire, which can be composed to solve tasks beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly, leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing approaches for improving robot behavior in deployment.

## Content
Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks: modulating language inputs elicits skills already within the policy's repertoire, which can be composed to solve tasks beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly, leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing approaches for improving robot behavior in deployment.

## 개요
제너럴리스트 로봇 정책은 대규모 사전 학습을 통해 다양한 행동 레퍼토리를 학습합니다. 원칙적으로 이는 강화 학습(RL)을 통한 하류 적응에 탁월한 사전 지식이 됩니다. 그러나 실제로 이 사전 지식을 활용하는 표준 RL 방법은 로봇 동작을 직접 최적화하며, 기본 정책의 행동 분포가 처음부터 성능이 좋은 정책의 분포와 가까워야 한다고 요구합니다. 이 가정은 사전 학습 분포를 벗어난 복잡하거나 장기적인 작업에서는 무너집니다. 우리의 핵심 통찰은 충분히 표현력이 뛰어난 제너럴리스트 정책의 경우 언어 프롬프트가 이러한 작업을 해결하기 위한 효과적인 대안 공간이라는 점입니다. 언어 입력을 조정하면 정책의 레퍼토리 내에 이미 존재하는 기술이 유발되며, 이를 조합하여 제로샷 능력을 넘어서는 작업을 해결할 수 있습니다. 우리는 의미적 행동 강화 학습(SARL)을 제안합니다. 이는 온라인 상호작용을 통해 이 프롬프트 공간을 최적화하는 방법을 학습하며, 제너럴리스트 정책을 제어 가능한 기술 사전 지식으로 취급합니다. 중요한 점은 새로운 기술을 처음부터 학습하는 대신 사전 학습된 기술을 활용함으로써 구조화되고 의미적으로 의미 있는 탐색과 매우 효율적인 온라인 개선이 가능해지며, 경험을 통해 프롬프트를 조정하는 방법을 학습함으로써 유도된 실제 세계 행동에 기반을 두어 강건한 작업 해결이 가능해진다는 것입니다. 실제 환경과 시뮬레이션 벤치마크 전반에 걸쳐 SARL이 근본적으로 새로운 능력(VLA 행동을 적응시켜 복잡하고 장기적인 작업 해결)을 열어주며, 배포 시 로봇 행동 개선을 위한 기존 접근법을 크게 능가함을 보여줍니다.

## 핵심 내용
제너럴리스트 로봇 정책은 대규모 사전 학습을 통해 다양한 행동 레퍼토리를 학습합니다. 원칙적으로 이는 강화 학습(RL)을 통한 하류 적응에 탁월한 사전 지식이 됩니다. 그러나 실제로 이 사전 지식을 활용하는 표준 RL 방법은 로봇 동작을 직접 최적화하며, 기본 정책의 행동 분포가 처음부터 성능이 좋은 정책의 분포와 가까워야 한다고 요구합니다. 이 가정은 사전 학습 분포를 벗어난 복잡하거나 장기적인 작업에서는 무너집니다. 우리의 핵심 통찰은 충분히 표현력이 뛰어난 제너럴리스트 정책의 경우 언어 프롬프트가 이러한 작업을 해결하기 위한 효과적인 대안 공간이라는 점입니다. 언어 입력을 조정하면 정책의 레퍼토리 내에 이미 존재하는 기술이 유발되며, 이를 조합하여 제로샷 능력을 넘어서는 작업을 해결할 수 있습니다. 우리는 의미적 행동 강화 학습(SARL)을 제안합니다. 이는 온라인 상호작용을 통해 이 프롬프트 공간을 최적화하는 방법을 학습하며, 제너럴리스트 정책을 제어 가능한 기술 사전 지식으로 취급합니다. 중요한 점은 새로운 기술을 처음부터 학습하는 대신 사전 학습된 기술을 활용함으로써 구조화되고 의미적으로 의미 있는 탐색과 매우 효율적인 온라인 개선이 가능해지며, 경험을 통해 프롬프트를 조정하는 방법을 학습함으로써 유도된 실제 세계 행동에 기반을 두어 강건한 작업 해결이 가능해진다는 것입니다. 실제 환경과 시뮬레이션 벤치마크 전반에 걸쳐 SARL이 근본적으로 새로운 능력(VLA 행동을 적응시켜 복잡하고 장기적인 작업 해결)을 열어주며, 배포 시 로봇 행동 개선을 위한 기존 접근법을 크게 능가함을 보여줍니다.
