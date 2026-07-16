---
$id: ent_paper_beyond_monotonic_progress_retr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation'
  zh: 'Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation'
  ko: 'Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation'
summary:
  en: 'arXiv:2606.24633v2 Announce Type: replace Abstract: Human demonstrations for robot imitation learning often contain
    mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts.
    While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution
    deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often
    rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors
    and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning),
    a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry
    events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining
    global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The
    learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence
    of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks
    show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning
    from imperfect demonstrations.'
  zh: 'arXiv:2606.24633v2 Announce Type: replace Abstract: Human demonstrations for robot imitation learning often contain
    mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts.
    While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution
    deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often
    rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors
    and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning),
    a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry
    events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining
    global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The
    learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence
    of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks
    show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning
    from imperfect demonstrations.'
  ko: 'arXiv:2606.24633v2 Announce Type: replace Abstract: Human demonstrations for robot imitation learning often contain
    mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts.
    While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution
    deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often
    rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors
    and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning),
    a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry
    events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining
    global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The
    learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence
    of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks
    show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning
    from imperfect demonstrations.'
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
- beyond_monotonic_progress
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.24633v2.
sources:
- id: src_001
  type: paper
  title: 'Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation (arXiv)'
  url: https://arxiv.org/abs/2606.24633
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Human demonstrations for robot imitation learning often contain mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts. While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning), a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning from imperfect demonstrations.

## 核心内容
Human demonstrations for robot imitation learning often contain mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts. While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning), a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning from imperfect demonstrations.

## 参考
- http://arxiv.org/abs/2606.24633v2

## Overview
Human demonstrations for robot imitation learning often contain mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts. While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning), a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning from imperfect demonstrations.

## Content
Human demonstrations for robot imitation learning often contain mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts. While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning), a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning from imperfect demonstrations.

## 개요
로봇 모방 학습을 위한 인간 시연 데이터에는 종종 부정확한 그립, 객체 정렬 오류, 불안정한 접촉, 반복 시도와 같은 실수와 교정 행동이 포함됩니다. 이러한 구간은 일반적으로 잡음이 있거나 최적이 아닌 데이터로 간주되지만, 실행이 바람직한 경로에서 벗어나는 시점과 작업 실행 가능성을 어떻게 복원할 수 있는지에 대한 귀중한 증거를 제공합니다. 그러나 기존의 보상 및 가치 모델은 종종 단조로운 진행 가정에 의존하여 대략적인 작업 진행 상황을 포착하지만, 불완전한 시연에서 국소적 실행 오류와 교정 행동을 간과할 수 있습니다. 본 연구에서는 재시도 이벤트를 희소 감독 신호로 활용하여 혼합 품질의 로봇 시연으로부터 실수에 민감한 가치 함수를 학습하는 프레임워크인 ReTVL(ReTry-Supervised Value Learning)을 제안합니다. ReTVL은 희소하게 주석이 달린 재시도 키포인트에 의해 유도된 전역 진행 보정과 국소 쌍별 선호도 학습을 결합하여 실수 주변의 국소적 성능 저하 및 복구 구조를 포착합니다. 학습된 가치 모델은 이후 하위 행동 복제를 위해 시연 청크의 가중치를 재조정하여 유용한 교정 행동은 유지하면서 유해한 실행 오류의 영향을 줄입니다. 실제 로봇 조작 작업에 대한 실험 결과, ReTVL이 진행 기반 기준선보다 더 세분화된 가치 추정치를 생성하고 불완전한 시연으로부터의 모방 학습을 개선함을 보여줍니다.

## 핵심 내용
로봇 모방 학습을 위한 인간 시연 데이터에는 종종 부정확한 그립, 객체 정렬 오류, 불안정한 접촉, 반복 시도와 같은 실수와 교정 행동이 포함됩니다. 이러한 구간은 일반적으로 잡음이 있거나 최적이 아닌 데이터로 간주되지만, 실행이 바람직한 경로에서 벗어나는 시점과 작업 실행 가능성을 어떻게 복원할 수 있는지에 대한 귀중한 증거를 제공합니다. 그러나 기존의 보상 및 가치 모델은 종종 단조로운 진행 가정에 의존하여 대략적인 작업 진행 상황을 포착하지만, 불완전한 시연에서 국소적 실행 오류와 교정 행동을 간과할 수 있습니다. 본 연구에서는 재시도 이벤트를 희소 감독 신호로 활용하여 혼합 품질의 로봇 시연으로부터 실수에 민감한 가치 함수를 학습하는 프레임워크인 ReTVL(ReTry-Supervised Value Learning)을 제안합니다. ReTVL은 희소하게 주석이 달린 재시도 키포인트에 의해 유도된 전역 진행 보정과 국소 쌍별 선호도 학습을 결합하여 실수 주변의 국소적 성능 저하 및 복구 구조를 포착합니다. 학습된 가치 모델은 이후 하위 행동 복제를 위해 시연 청크의 가중치를 재조정하여 유용한 교정 행동은 유지하면서 유해한 실행 오류의 영향을 줄입니다. 실제 로봇 조작 작업에 대한 실험 결과, ReTVL이 진행 기반 기준선보다 더 세분화된 가치 추정치를 생성하고 불완전한 시연으로부터의 모방 학습을 개선함을 보여줍니다.
