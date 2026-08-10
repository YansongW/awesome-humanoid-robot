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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.07294v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1043 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.07294v2

## 개요
HuB는 휴머노이드 로봇이 균형 집약적 작업에서 직면하는 세 가지 장애물, 즉 참조 동작 오류로 인한 불안정성, 형태 불일치로 인한 학습 어려움, 센서 노이즈 및 미모델링 동역학으로 인한 sim-to-real 격차를 해결합니다. 이 프레임워크는 세 가지 맞춤형 모듈을 통해 문제를 해결합니다: 먼저 참조 운동 데이터를 정제하여 오류를 줄이고, 다음으로 형태 차이에 적응하는 균형 인식 정책 학습 알고리즘을 설계하며, 마지막으로 sim-to-real 강건 훈련을 도입하여 외란 저항 능력을 강화합니다. Unitree G1 로봇에서의 실험은 이 정책이 극단적인 한쪽 다리 균형 작업에서 안정적으로 동작하며, 강력한 축구공 충격과 같은 물리적 외란에도 균형을 유지할 수 있음을 보여줍니다. 반면 모든 기준선 방법은 이러한 작업을 완료하지 못했습니다.

## 핵심 내용
### 방법 아키텍처
HuB 프레임워크는 세 가지 핵심 모듈을 포함합니다:
- **참조 동작 정제**: 운동학적 제약과 동역학 필터링을 통해 원본 참조 동작의 미세 오류를 제거하여 정책 학습 시 불안정한 전파를 방지합니다.
- **균형 인식 정책 학습**: 형태 정합 손실 함수를 도입하여 정책이 휴머노이드 로봇과 인간 간의 관절 자유도, 질량 분포 차이에 적응하도록 하여 형태 불일치로 인한 정책 실패를 방지합니다.
- **Sim-to-Real 강건 훈련**: 시뮬레이션 환경에 센서 노이즈(예: IMU 가우시안 노이즈), 지연 실행 및 미모델링 마찰력을 주입하여 실제 환경 외란에 대한 정책의 강건성을 훈련합니다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇(약 35kg, 19자유도).
- **작업**: 준정적 균형 작업, 포함:
  - 제비 균형(한쪽 다리로 서서 다른 다리를 뒤로 수평으로 들어 올림)
  - 이소룡 발차기(한쪽 다리로 서서 다른 다리를 앞으로 1.5미터 높이까지 차기)
- **기준선 방법**: 인간 동작을 직접 전이하는 RL 정책, 정제 모듈이 없는 절제 버전, 강건 훈련이 없는 버전을 포함합니다.

### 주요 결과
- **성공률**: HuB는 제비 균형 작업에서 92%, 이소룡 발차기 작업에서 88%의 성공률을 달성했습니다. 최고 기준선 방법(정제 모듈 없음)은 각각 34%와 21%의 성공률을 보였습니다.
- **외란 저항 능력**: 로봇이 한쪽 다리로 서 있을 때 5m/s 속도의 축구공 충격을 가한 경우, HuB 정책은 95%의 테스트에서 균형을 유지했습니다(10초 이상). 반면 모든 기준선 방법은 충격 후 0.5초 이내에 넘어졌습니다.
- **Sim-to-Real 전이**: 시뮬레이션 정책을 실제 로봇에 직접 배포할 때, HuB의 강건 훈련 모듈은 성공률을 41%에서 89%로 향상시켰습니다(제비 균형 작업).

### 결론
HuB는 참조 동작 오류, 형태 불일치 및 sim-to-real 격차를 체계적으로 해결함으로써 휴머노이드 로봇이 극단적인 한쪽 다리 자세에서 안정적인 균형 제어를 최초로 구현했으며, 외란 저항 능력이 기존 방법보다 현저히 우수합니다. 프로젝트 웹사이트에서 비디오 데모와 코드 오픈소스를 제공합니다.
