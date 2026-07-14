---
$id: ent_paper_unveiling_the_impact_of_data_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots
  zh: 揭示数据和模型扩展对人形机器人高级控制的影响
  ko: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots
summary:
  en: Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion
    data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to
    the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video,
    extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this,
    we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours
    of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset
    can be further expanded via the same pipeline. Building on this data resource
  zh: 这篇工作先从人类视频/动捕轨迹恢复场景、目标或运动表征，再用扩散策略/流匹配生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: 这篇工作先从人类视频/动捕轨迹恢复场景、目标或运动表征，再用扩散策略/流匹配生成全身轨迹/动作序列。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- language_control
- motion_generation
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Unveiling the Impact of
    Data and Model Scaling on High-Level Control for Humanoid Robots.'
sources:
- id: src_001
  type: website
  title: 揭示数据和模型扩展对人形机器人高级控制的影响 project page
  url: https://vfishc.github.io/schur/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

## 核心内容
Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

## 参考
- Semantic Scholar search: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots

