---
$id: ent_paper_toddlerbot_open_source_ml_comp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'
  zh: ToddlerBot｜用于移动操作的开源ML兼容人形平台
  ko: 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'
summary:
  en: Learning-based robotics research driven by data demands a new approach to robot hardware design-one that serves as both
    a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a
    low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot
    enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration
    and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from
    simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection
    for learning motor skills from human demonstrations. Utilizing its data c
  zh: ToddlerBot 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、分层技能/专家策略转成可训练、可复用的地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: ToddlerBot 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、分层技能/专家策略转成可训练、可复用的地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- deployment
- hardware_platform
- real_world
- sensor_suite
- toddlerbot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: ToddlerBot: Open-Source
    ML-Compatible Humanoid Platform for Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: ToddlerBot project page
  url: https://toddlerbot.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Learning-based robotics research driven by data demands a new approach to robot hardware design-one that serves as both a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection for learning motor skills from human demonstrations. Utilizing its data collection ability and anthropomorphic design, ToddlerBot is an ideal platform to perform whole-body loco-manipulation. Additionally, ToddlerBot's compact size (0.56m, 3.4kg) ensures safe operation in real-world environments. Reproducibility is achieved with an entirely 3D-printed, open-source design and commercially available components, keeping the total cost under 6,000 USD. Comprehensive documentation allows assembly and maintenance with basic technical expertise, as validated by a successful independent replication of the system. We demonstrate ToddlerBot's capabilities through arm span, payload, endurance tests, loco-manipulation tasks, and a collaborative long-horizon scenario where two robots tidy a toy session together. By advancing ML-compatibility, capability, and reproducibility, ToddlerBot provides a robust platform for scalable learning and dynamic policy execution in robotics research.

## 核心内容
Learning-based robotics research driven by data demands a new approach to robot hardware design-one that serves as both a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection for learning motor skills from human demonstrations. Utilizing its data collection ability and anthropomorphic design, ToddlerBot is an ideal platform to perform whole-body loco-manipulation. Additionally, ToddlerBot's compact size (0.56m, 3.4kg) ensures safe operation in real-world environments. Reproducibility is achieved with an entirely 3D-printed, open-source design and commercially available components, keeping the total cost under 6,000 USD. Comprehensive documentation allows assembly and maintenance with basic technical expertise, as validated by a successful independent replication of the system. We demonstrate ToddlerBot's capabilities through arm span, payload, endurance tests, loco-manipulation tasks, and a collaborative long-horizon scenario where two robots tidy a toy session together. By advancing ML-compatibility, capability, and reproducibility, ToddlerBot provides a robust platform for scalable learning and dynamic policy execution in robotics research.

## 参考
- Semantic Scholar search: ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation

