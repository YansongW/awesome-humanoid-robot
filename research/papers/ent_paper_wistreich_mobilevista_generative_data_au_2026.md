---
$id: ent_paper_wistreich_mobilevista_generative_data_au_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation'
  zh: 'MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation'
  ko: 'MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation'
summary:
  en: 'Mobile manipulators such as humanoid robots are increasingly deployed in dynamic, unstructured environments to perform
    dexterous manipulation tasks. However, end-to-end manipulation policies trained to imitate demonstration data collected
    from a single robot pose are brittle: even centimeter-scale deviations in robot pose at deployment can drive ego-centric
    observations and end-effector ...'
  zh: MobileVISTA 是一个面向移动操作（如人形机器人）的数据生成框架，由 Suzannah Wistreich、Stephen Tian、Isabella Huang、Vitor Campagnolo Guizilini、Sergey
    Zakharov、Katherine Liu、Jiajun Wu 提出。它通过联合增强自我中心视觉观测并对动作进行重定向，把在标准位姿下采集的演示数据转化为多样化的位姿扰动训练数据，从而提升策略对部署时位姿偏差的鲁棒性。该方法无需额外采集演示数据，也无需训练生成模型。
  ko: 'Mobile manipulators such as humanoid robots are increasingly deployed in dynamic, unstructured environments to perform
    dexterous manipulation tasks. However, end-to-end manipulation policies trained to imitate demonstration data collected
    from a single robot pose are brittle: even centimeter-scale deviations in robot pose at deployment can drive ego-centric
    observations and end-effector ...'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- mobile_manipulation
- data_augmentation
- pose_generalization
- imitation_learning
- humanoid_robots
- egocentric_vision
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.07511);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.07511 MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation'
  url: https://arxiv.org/abs/2610.07511
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

移动操作机器人（例如人形机器人）在动态非结构化环境中执行灵巧操作任务时，端到端模仿学习策略往往十分脆弱：部署时即使只有厘米级的位姿偏差，也会使自我中心观测和末端执行器轨迹偏离训练分布，导致性能急剧下降。MobileVISTA 通过同时做两件事来应对这一问题：一是对自我中心视觉观测进行增强，二是对动作进行重定向以补偿基座位姿变化，从而把标准位姿下的演示转化为位姿扰动的训练数据。与假设相机刚性安装在驱动链之外、或机器人本体大部分不在画面中的既有方法不同，MobileVISTA 面向相机既受运动学链影响、又必须观测该运动学链的自我中心平台。作者在人形与双臂形态的仿真任务以及真实 Galaxea R1 Pro 上进行了研究，发现用 MobileVISTA 增强数据训练的策略对测试时此前属于分布外的位姿具有更好的鲁棒性，且无需额外采集演示或训练生成模型；这种收益在被测人形机器人上最为显著。

## 核心内容

### 问题背景
移动操作机器人（如人形机器人）越来越多地被部署到动态、非结构化环境中执行灵巧操作任务。然而，仅用单一机器人位姿下采集的演示数据训练端到端模仿策略会带来脆弱性：部署时哪怕只有厘米级的位姿偏差，也会让自我中心观测与末端执行器轨迹落到训练分布之外，造成性能骤降。

### 方法
MobileVISTA 是一个数据生成框架，将标准位姿下采集的演示转化为多样化的位姿扰动训练数据，其核心是两项联合操作：
- 增强自我中心视觉观测；
- 对动作进行重定向，以补偿基座位姿的变化。

与先前方法不同，MobileVISTA 针对的是自我中心平台（例如人形机器人）：在这类平台上，相机既受到机器人运动学链的影响，又必须观测运动中的运动学链。而既有方法通常假设相机刚性安装在驱动链之外，或假设机器人本体大部分不在画面中。

### 实验设置
作者在覆盖人形与双臂形态的仿真任务上研究了 MobileVISTA，并在真实的 Galaxea R1 Pro 上进行了验证。

### 关键结果
- 用 MobileVISTA 增强数据训练的策略，对测试时遇到的、此前属于分布外的位姿表现出更好的鲁棒性。
- 这一效果无需额外采集演示数据，也无需训练生成模型即可获得。
- MobileVISTA 的收益在被测人形机器人上最大，原因是相机随驱动链运动，且机器人在画面中占据较大比例。

### 结论
MobileVISTA 通过联合的视觉增强与动作重定向，为自我中心移动操作平台提供了一种无需额外演示采集或生成模型的位姿泛化数据增强方案，并在人形形态上体现出最明显的优势。更多视频与附录见项目网站 https://mobilevista.github.io 。

## Overview

Mobile manipulators such as humanoid robots are increasingly deployed in dynamic, unstructured environments to perform dexterous manipulation tasks. However, end-to-end manipulation policies trained to imitate demonstration data collected from a single robot pose are brittle: even centimeter-scale deviations in robot pose at deployment can drive ego-centric observations and end-effector trajectories out of the training distribution, leading to sharp drops in performance. We introduce MobileVISTA, a data generation framework that transforms demonstrations captured at canonical poses into diverse, pose-perturbed training data by jointly (1) augmenting egocentric visual observations and (2) retargeting actions to compensate for base pose changes. Unlike prior methods, which assume a camera rigidly mounted off the actuated chain or non-trivial articulated robot geometry largely out of frame, MobileVISTA targets compatibility with egocentric platforms (e.g., humanoids) where the camera is both influenced by and must observe the robot's kinematic chain as it moves. We study MobileVISTA in simulated tasks spanning humanoid and bimanual embodiments, and on a real Galaxea R1 Pro. We find policies trained on MobileVISTA-augmented data demonstrate improved robustness to previously out-of-distribution poses encountered at test time, without additional demonstration collection or a trained generative model. Additionally, we find MobileVISTA's benefit is largest on tested humanoids, where the camera rides the actuated chain and the robot fills much of the frame. Additional videos and appendix can be found on our website: https://mobilevista.github.io

## 参考
- https://arxiv.org/abs/2610.07511
