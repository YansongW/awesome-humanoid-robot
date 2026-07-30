---
$id: ent_paper_berkeley_humanoid_a_research_p_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Berkeley Humanoid: A Research Platform for Learning-based Control'
  zh: 'Berkeley Humanoid: A Research Platform for Learning-based Control'
  ko: 'Berkeley Humanoid: A Research Platform for Learning-based Control'
summary:
  en: 'Berkeley Humanoid: A Research Platform for Learning-based Control is a 2024 work on hardware design for humanoid robots,
    with open-source code available.'
  zh: Berkeley Humanoid 是加州大学伯克利分校于 2024 年推出的低成本、轻量级人形机器人研究平台，专为基于学习的控制算法设计。其核心贡献在于通过低仿真复杂度、拟人化运动与高抗摔可靠性，实现了从仿真到现实（sim-to-real）的窄差距迁移，仅用轻量域随机化的强化学习控制器即可在户外复杂地形上完成敏捷、鲁棒的
    locomotion。
  ko: 'Berkeley Humanoid: A Research Platform for Learning-based Control is a 2024 work on hardware design for humanoid robots,
    with open-source code available.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- berkeley_humanoid
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.21781v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Berkeley Humanoid: A Research Platform for Learning-based Control (arXiv)'
  url: https://arxiv.org/abs/2407.21781
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Berkeley Humanoid: A Research Platform for Learning-based Control project page'
  url: https://berkeley-humanoid.com/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Berkeley Humanoid 是一款由伯克利团队内部自建的中型人形机器人研究平台，强调低成本、轻量化和高可靠性。该机器人专为学习算法优化，具备低仿真复杂度、拟人化运动特性，并能有效抵抗跌倒冲击。通过简单的强化学习控制器配合轻量域随机化，机器人实现了从仿真到现实的窄差距迁移，能够在户外多种地形上完成敏捷且鲁棒的 locomotion。实验展示了机器人连续行走数百米、在陡峭未铺装小径上行走、以及单腿和双腿跳跃等动态行走能力，验证了其高性能。该系统支持全向 locomotion，并能以紧凑的配置承受大幅扰动，旨在推动基于学习的人形机器人系统的可扩展仿真到现实部署。

## 核心内容
### 平台设计理念
- **低成本与轻量化**：Berkeley Humanoid 采用内部自建方式，旨在降低研究门槛，避免依赖昂贵商用平台。
- **专为学习算法设计**：机器人结构优化了仿真复杂度，使强化学习训练更高效；同时具备拟人化运动学特性，便于迁移到真实世界。
- **高抗摔可靠性**：硬件设计能承受频繁跌倒，适合在真实环境中进行探索性学习实验。

### 仿真到现实（Sim-to-Real）迁移
- **窄差距迁移**：通过轻量域随机化（light domain randomization）的强化学习控制器，机器人从仿真环境直接迁移到真实世界，无需大量手动调参。
- **户外地形适应性**：在户外环境中成功穿越多种地形，包括平坦路面、陡峭未铺装小径，并实现单腿和双腿跳跃。

### 实验性能与关键数字
- **长距离行走**：机器人连续行走数百米，验证了系统的稳定性和续航能力。
- **动态行走能力**：在陡峭未铺装小径上行走，并完成单腿和双腿跳跃动作，展示了高动态性能。
- **抗扰动能力**：支持全向 locomotion，并能以紧凑的硬件配置承受大幅外部扰动。

### 开源与资源
- 项目代码与硬件设计已开源，详情请访问 http://berkeley-humanoid.com。

## Overview
We introduce Berkeley Humanoid, a reliable and low-cost mid-scale humanoid research platform for learning-based control. Our lightweight, in-house-built robot is designed specifically for learning algorithms with low simulation complexity, anthropomorphic motion, and high reliability against falls. The robot's narrow sim-to-real gap enables agile and robust locomotion across various terrains in outdoor environments, achieved with a simple reinforcement learning controller using light domain randomization. Furthermore, we demonstrate the robot traversing for hundreds of meters, walking on a steep unpaved trail, and hopping with single and double legs as a testimony to its high performance in dynamical walking. Capable of omnidirectional locomotion and withstanding large perturbations with a compact setup, our system aims for scalable, sim-to-real deployment of learning-based humanoid systems. Please check http://berkeley-humanoid.com for more details.

## 개요
우리는 학습 기반 제어를 위한 신뢰할 수 있고 저렴한 중간 규모의 인간형 연구 플랫폼인 Berkeley Humanoid를 소개합니다. 자체 제작한 경량 로봇은 낮은 시뮬레이션 복잡성, 인간형 움직임, 낙하에 대한 높은 신뢰성을 갖춘 학습 알고리즘에 특화되어 설계되었습니다. 로봇의 좁은 시뮬레이션-실제 격차는 가벼운 도메인 무작위화를 사용하는 간단한 강화 학습 제어기를 통해 야외 환경의 다양한 지형에서 민첩하고 강건한 보행을 가능하게 합니다. 또한, 로봇이 수백 미터를 이동하고, 가파른 비포장 길을 걸으며, 한쪽 및 양쪽 다리로 점프하는 것을 시연하여 동적 보행에서의 높은 성능을 입증합니다. 전방향 이동이 가능하고 소형 설정으로 큰 외란을 견딜 수 있는 이 시스템은 학습 기반 인간형 시스템의 확장 가능한 시뮬레이션-실제 배치를 목표로 합니다. 자세한 내용은 http://berkeley-humanoid.com에서 확인하십시오.

## 핵심 내용
우리는 학습 기반 제어를 위한 신뢰할 수 있고 저렴한 중간 규모의 인간형 연구 플랫폼인 Berkeley Humanoid를 소개합니다. 자체 제작한 경량 로봇은 낮은 시뮬레이션 복잡성, 인간형 움직임, 낙하에 대한 높은 신뢰성을 갖춘 학습 알고리즘에 특화되어 설계되었습니다. 로봇의 좁은 시뮬레이션-실제 격차는 가벼운 도메인 무작위화를 사용하는 간단한 강화 학습 제어기를 통해 야외 환경의 다양한 지형에서 민첩하고 강건한 보행을 가능하게 합니다. 또한, 로봇이 수백 미터를 이동하고, 가파른 비포장 길을 걸으며, 한쪽 및 양쪽 다리로 점프하는 것을 시연하여 동적 보행에서의 높은 성능을 입증합니다. 전방향 이동이 가능하고 소형 설정으로 큰 외란을 견딜 수 있는 이 시스템은 학습 기반 인간형 시스템의 확장 가능한 시뮬레이션-실제 배치를 목표로 합니다. 자세한 내용은 http://berkeley-humanoid.com에서 확인하십시오.

## 参考
- http://arxiv.org/abs/2407.21781v1
