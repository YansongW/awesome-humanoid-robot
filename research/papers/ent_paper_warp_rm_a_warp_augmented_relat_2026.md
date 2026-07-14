---
$id: ent_paper_warp_rm_a_warp_augmented_relat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation'
  zh: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation'
  ko: ''
summary:
  en: "arXiv:2606.28320v3 Announce Type: replace \nAbstract: Scaling imitation learning\
    \ requires large datasets, yet human teleoperation inevitably produces mixed-quality\
    \ demonstrations containing hesitations and recoveries. Prior frame-level progress\
    \ reward models supervise on absolute temporal progress proxies that suffer from\
    \ label noise, or require costly human annotations to define subtask boundaries.\
    \ We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised\
    \ algorithm for learning dense, signed relative progress magnitudes directly from\
    \ successful demonstrations. WARP generates per-frame progress targets via time-warp\
    \ augmentations of demonstrations (variable playback speeds and reversals) and\
    \ we train WARP-RM to predict the normalized elapsed time between input frames.\
    \ Aggregating these predictions across overlapping windows yields a dense frame-level\
    \ progress signal. We then introduce WARP-BC, which leverages these scalar reward\
    \ estimates to upweight high-advantage action chunks during behavior cloning,\
    \ where chunk-level advantage is obtained by aggregating per-frame rewards. We\
    \ evaluate our approach on a physical bimanual robot system performing a long-horizon\
    \ deformable object manipulation task: folding T-shirts from a random crumpled\
    \ start. To evaluate policy robustness against suboptimal data, we construct training\
    \ datasets of varying quality using episode length as a proxy for teleoperation\
    \ sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC\
    \ maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving\
    \ throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement\
    \ task in the real-world, as well as in a reproducible simulation of the task,\
    \ where gains in success, speed, and throughput hold under paired significance\
    \ tests, and we release all simulation code and evaluation artifacts. Project\
    \ page: https://uynitsuj.github.io/warp-rm/"
  zh: "arXiv:2606.28320v3 Announce Type: replace \nAbstract: Scaling imitation learning\
    \ requires large datasets, yet human teleoperation inevitably produces mixed-quality\
    \ demonstrations containing hesitations and recoveries. Prior frame-level progress\
    \ reward models supervise on absolute temporal progress proxies that suffer from\
    \ label noise, or require costly human annotations to define subtask boundaries.\
    \ We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised\
    \ algorithm for learning dense, signed relative progress magnitudes directly from\
    \ successful demonstrations. WARP generates per-frame progress targets via time-warp\
    \ augmentations of demonstrations (variable playback speeds and reversals) and\
    \ we train WARP-RM to predict the normalized elapsed time between input frames.\
    \ Aggregating these predictions across overlapping windows yields a dense frame-level\
    \ progress signal. We then introduce WARP-BC, which leverages these scalar reward\
    \ estimates to upweight high-advantage action chunks during behavior cloning,\
    \ where chunk-level advantage is obtained by aggregating per-frame rewards. We\
    \ evaluate our approach on a physical bimanual robot system performing a long-horizon\
    \ deformable object manipulation task: folding T-shirts from a random crumpled\
    \ start. To evaluate policy robustness against suboptimal data, we construct training\
    \ datasets of varying quality using episode length as a proxy for teleoperation\
    \ sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC\
    \ maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving\
    \ throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement\
    \ task in the real-world, as well as in a reproducible simulation of the task,\
    \ where gains in success, speed, and throughput hold under paired significance\
    \ tests, and we release all simulation code and evaluation artifacts. Project\
    \ page: https://uynitsuj.github.io/warp-rm/"
  ko: ''
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
- warp_rm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation
    (arXiv)'
  url: https://arxiv.org/abs/2606.28320
  date: '2026'
  accessed_at: '2026-07-14'
---

arXiv:2606.28320v3 Announce Type: replace 
Abstract: Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x. Furthermore, we evaluate a bottle-in-bin placement task in the real-world, as well as in a reproducible simulation of the task, where gains in success, speed, and throughput hold under paired significance tests, and we release all simulation code and evaluation artifacts. Project page: https://uynitsuj.github.io/warp-rm/
