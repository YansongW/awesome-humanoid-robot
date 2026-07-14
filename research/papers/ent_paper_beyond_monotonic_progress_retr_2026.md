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
  en: "arXiv:2606.24633v2 Announce Type: replace \nAbstract: Human demonstrations for robot imitation learning often contain\
    \ mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts.\
    \ While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution\
    \ deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often\
    \ rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors\
    \ and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning),\
    \ a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry\
    \ events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining\
    \ global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The\
    \ learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence\
    \ of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks\
    \ show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning\
    \ from imperfect demonstrations."
  zh: "arXiv:2606.24633v2 Announce Type: replace \nAbstract: Human demonstrations for robot imitation learning often contain\
    \ mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts.\
    \ While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution\
    \ deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often\
    \ rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors\
    \ and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning),\
    \ a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry\
    \ events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining\
    \ global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The\
    \ learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence\
    \ of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks\
    \ show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning\
    \ from imperfect demonstrations."
  ko: "arXiv:2606.24633v2 Announce Type: replace \nAbstract: Human demonstrations for robot imitation learning often contain\
    \ mistakes and corrective behaviors, such as imprecise grasps, object misalignment, unstable contact, and repeated attempts.\
    \ While these segments are commonly treated as noisy or suboptimal data, they provide valuable evidence about when execution\
    \ deviates from a desirable path and how task feasibility can be restored. However, existing reward and value models often\
    \ rely on monotonic progress assumptions, which capture coarse task advancement but may overlook local execution errors\
    \ and corrective behaviors in imperfect demonstrations. In this work, we propose ReTVL (ReTry-Supervised Value Learning),\
    \ a framework for learning mistake-sensitive value functions from mixed-quality robot demonstrations by leveraging retry\
    \ events as sparse supervision. ReTVL captures the local degradation-and-recovery structure around mistakes by combining\
    \ global progress calibration with local pairwise preference learning induced by sparsely annotated retry keypoints. The\
    \ learned value model is then used to reweight demonstration chunks for downstream behavior cloning, reducing the influence\
    \ of harmful execution errors while preserving useful corrective behaviors. Experiments on real-robot manipulation tasks\
    \ show that ReTVL produces more fine-grained value estimates than progress-based baselines and improves imitation learning\
    \ from imperfect demonstrations."
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

