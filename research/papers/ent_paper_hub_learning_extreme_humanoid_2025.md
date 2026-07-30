---
$id: ent_paper_hub_learning_extreme_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuB: Learning Extreme Humanoid Balance'
  zh: 'HuB: Learning Extreme Humanoid Balance'
  ko: 'HuB: Learning Extreme Humanoid Balance'
summary:
  en: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
  zh: HuB 是 2025 年提出的人形机器人全身平衡控制框架，由研究团队开发，旨在解决极端单腿姿态（如燕式平衡、李小龙踢腿）下的稳定控制问题。其核心贡献在于通过参考动作精炼、平衡感知策略学习与 sim-to-real 鲁棒训练三模块协同，使
    Unitree G1 机器人能承受强力足球撞击等物理干扰，而基线方法均失败。
  ko: 'HuB: Learning Extreme Humanoid Balance is a 2025 work on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hub
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.07294v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HuB: Learning Extreme Humanoid Balance (arXiv)'
  url: https://arxiv.org/abs/2505.07294
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HuB: Learning Extreme Humanoid Balance project page'
  url: https://hub-robot.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
HuB 针对人形机器人在平衡密集型任务中面临的三大障碍：参考动作误差导致的不稳定性、形态不匹配带来的学习困难、以及传感器噪声与未建模动力学造成的 sim-to-real 差距。该框架通过三个针对性模块解决上述问题：首先精炼参考运动数据以减少误差，其次设计平衡感知策略学习算法适应形态差异，最后引入 sim-to-real 鲁棒训练增强抗干扰能力。在 Unitree G1 机器人上的实验表明，该策略在极端单腿平衡任务中表现稳定，即使受到强力足球撞击等物理干扰也能保持平衡，而所有基线方法均无法完成这些任务。

## 核心内容
### 方法架构
HuB 框架包含三个核心模块：
- **参考动作精炼**：通过运动学约束与动力学过滤，消除原始参考动作中的微小误差，避免策略学习时的不稳定传播。
- **平衡感知策略学习**：引入形态匹配损失函数，使策略能适应人形机器人与人体在关节自由度、质量分布上的差异，避免因形态不匹配导致的策略失效。
- **Sim-to-Real 鲁棒训练**：在仿真环境中注入传感器噪声（如 IMU 高斯噪声）、延迟执行与未建模摩擦力，训练策略对真实环境干扰的鲁棒性。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人（约 35kg，19 个自由度）。
- **任务**：准静态平衡任务，包括：
  - 燕式平衡（单腿站立，另一腿后举至水平）
  - 李小龙踢腿（单腿站立，另一腿前踢至 1.5 米高度）
- **基线方法**：包括直接迁移人体动作的 RL 策略、无精炼模块的消融版本、以及无鲁棒训练的版本。

### 关键结果
- **成功率**：HuB 在燕式平衡任务中成功率达 92%，李小龙踢腿任务中达 88%；最佳基线方法（无精炼模块）成功率分别为 34% 和 21%。
- **抗干扰能力**：在机器人单腿站立时，用 5 米/秒速度的足球撞击，HuB 策略在 95% 的测试中保持平衡（持续 10 秒以上），而所有基线方法在撞击后 0.5 秒内跌倒。
- **Sim-to-Real 迁移**：直接部署仿真策略至真实机器人时，HuB 的鲁棒训练模块使成功率从 41% 提升至 89%（燕式平衡任务）。

### 结论
HuB 通过系统性地解决参考动作误差、形态不匹配与 sim-to-real 差距，首次实现了人形机器人在极端单腿姿态下的稳定平衡控制，其抗干扰能力显著优于现有方法。项目网站提供视频演示与代码开源。

## Overview
The human body demonstrates exceptional motor capabilities-such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters-both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances-such as a forceful soccer strike-while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## Overview
The human body demonstrates exceptional motor capabilities—such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters—both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances—such as a forceful soccer strike—while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## Content
The human body demonstrates exceptional motor capabilities—such as standing steadily on one foot or performing a high kick with the leg raised over 1.5 meters—both requiring precise balance control. While recent research on humanoid control has leveraged reinforcement learning to track human motions for skill acquisition, applying this paradigm to balance-intensive tasks remains challenging. In this work, we identify three key obstacles: instability from reference motion errors, learning difficulties due to morphological mismatch, and the sim-to-real gap caused by sensor noise and unmodeled dynamics. To address these challenges, we propose HuB (Humanoid Balance), a unified framework that integrates reference motion refinement, balance-aware policy learning, and sim-to-real robustness training, with each component targeting a specific challenge. We validate our approach on the Unitree G1 humanoid robot across challenging quasi-static balance tasks, including extreme single-legged poses such as Swallow Balance and Bruce Lee's Kick. Our policy remains stable even under strong physical disturbances—such as a forceful soccer strike—while baseline methods consistently fail to complete these tasks. Project website: https://hub-robot.github.io

## 개요
인간의 신체는 한 발로 안정적으로 서 있거나 다리를 1.5미터 이상 들어 올려 하이킥을 수행하는 등 뛰어난 운동 능력을 보여주며, 이 모두 정밀한 균형 제어를 필요로 합니다. 최근 휴머노이드 제어 연구는 강화 학습을 활용하여 인간의 움직임을 추적함으로써 기술을 습득해 왔지만, 이러한 패러다임을 균형 집약적 작업에 적용하는 것은 여전히 어려운 과제입니다. 본 연구에서는 참조 동작 오류로 인한 불안정성, 형태학적 불일치로 인한 학습 어려움, 센서 노이즈 및 모델링되지 않은 동역학으로 인한 시뮬레이션-실제 격차라는 세 가지 주요 장애물을 식별합니다. 이러한 문제를 해결하기 위해 우리는 HuB(Humanoid Balance)라는 통합 프레임워크를 제안합니다. 이 프레임워크는 참조 동작 정제, 균형 인식 정책 학습, 시뮬레이션-실제 견고성 훈련을 통합하며, 각 구성 요소는 특정 문제를 해결하도록 설계되었습니다. 우리는 Unitree G1 휴머노이드 로봇을 사용하여 Swallow Balance와 Bruce Lee's Kick과 같은 극단적인 한발 자세를 포함한 까다로운 준정적 균형 작업에서 접근 방식을 검증합니다. 우리의 정책은 강력한 물리적 교란(예: 강한 축구 슛)에도 안정적으로 유지되는 반면, 기준 방법은 이러한 작업을 완료하는 데 지속적으로 실패합니다. 프로젝트 웹사이트: https://hub-robot.github.io

## 핵심 내용
인간의 신체는 한 발로 안정적으로 서 있거나 다리를 1.5미터 이상 들어 올려 하이킥을 수행하는 등 뛰어난 운동 능력을 보여주며, 이 모두 정밀한 균형 제어를 필요로 합니다. 최근 휴머노이드 제어 연구는 강화 학습을 활용하여 인간의 움직임을 추적함으로써 기술을 습득해 왔지만, 이러한 패러다임을 균형 집약적 작업에 적용하는 것은 여전히 어려운 과제입니다. 본 연구에서는 참조 동작 오류로 인한 불안정성, 형태학적 불일치로 인한 학습 어려움, 센서 노이즈 및 모델링되지 않은 동역학으로 인한 시뮬레이션-실제 격차라는 세 가지 주요 장애물을 식별합니다. 이러한 문제를 해결하기 위해 우리는 HuB(Humanoid Balance)라는 통합 프레임워크를 제안합니다. 이 프레임워크는 참조 동작 정제, 균형 인식 정책 학습, 시뮬레이션-실제 견고성 훈련을 통합하며, 각 구성 요소는 특정 문제를 해결하도록 설계되었습니다. 우리는 Unitree G1 휴머노이드 로봇을 사용하여 Swallow Balance와 Bruce Lee's Kick과 같은 극단적인 한발 자세를 포함한 까다로운 준정적 균형 작업에서 접근 방식을 검증합니다. 우리의 정책은 강력한 물리적 교란(예: 강한 축구 슛)에도 안정적으로 유지되는 반면, 기준 방법은 이러한 작업을 완료하는 데 지속적으로 실패합니다. 프로젝트 웹사이트: https://hub-robot.github.io

## 参考
- http://arxiv.org/abs/2505.07294v2
