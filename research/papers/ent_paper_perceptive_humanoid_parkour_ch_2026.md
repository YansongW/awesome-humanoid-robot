---
$id: ent_paper_perceptive_humanoid_parkour_ch_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching'
  zh: 跑酷的难点不是单技能，而是长程组合
  ko: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching'
summary:
  en: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: Perceptive Humanoid Parkour (PHP) 是一个模块化框架，由研究团队提出，旨在让 Unitree G1 人形机器人通过视觉感知自主完成长时域跑酷任务。其核心贡献在于利用运动匹配技术组合动态人类技能，并训练强化学习策略实现闭环适应，使机器人能攀爬高达1.25米（96%机器人身高）的障碍物。
  ko: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15827v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (729 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching (arXiv)'
  url: https://arxiv.org/abs/2602.15827
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 跑酷的难点不是单技能，而是长程组合 project page
  url: https://php-parkour.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
该框架首先通过特征空间中的最近邻搜索进行运动匹配，将重定向后的原子人类技能组合成长期运动轨迹，实现复杂技能链的灵活编排与平滑过渡。随后，针对这些组合动作训练运动跟踪强化学习专家策略，并通过 DAgger 与 RL 结合的方法将其蒸馏为单一深度感知多技能学生策略。最终，机器人仅依靠机载深度传感器和离散二维速度指令，即可自主决策跨越、攀爬、跳跃或滚落不同几何形状与高度的障碍物。

## 核心内容
### 方法架构
- **运动匹配层**：将人类运动捕捉数据重定向至机器人运动学，通过特征空间最近邻搜索动态组合原子技能（如跨步、攀爬、跳跃），生成连续且流畅的长时域运动轨迹。
- **策略训练**：为每个组合动作训练独立的运动跟踪 RL 专家策略，再通过 DAgger 与 RL 联合蒸馏方法，将其整合为单一深度感知多技能学生策略，降低部署复杂度。
- **感知决策**：学生策略仅依赖机载深度相机与离散 2D 速度指令，实时感知障碍物几何特征，自主选择并执行相应动作（如跨越、攀爬、滚落）。

### 实验设置与关键结果
- **硬件平台**：Unitree G1 人形机器人，搭载机载深度传感器。
- **障碍物测试**：
  - 静态障碍：成功攀爬高达 1.25m（占机器人身高 96%）的垂直障碍物。
  - 动态场景：在长时域多障碍物穿越中，实时适应障碍物位置扰动（如突然移动的箱子）。
- **技能多样性**：实现跨越、攀爬、跳跃、滚落四种动态动作的闭环组合，无需预编程切换逻辑。

### 结论
PHP 框架通过运动匹配与感知驱动的策略蒸馏，首次在人形机器人上实现了类人动态跑酷能力，验证了模块化技能组合在复杂地形中的鲁棒性与适应性。

## Overview
While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

## 参考
- http://arxiv.org/abs/2602.15827v2

## 개요
이 프레임워크는 먼저 특징 공간에서의 최근접 이웃 탐색을 통한 동작 매칭으로, 리타게팅된 원자적 인간 스킬을 조합하여 장기 운동 궤적을 생성하며, 복잡한 스킬 체인의 유연한 편성과 부드러운 전환을 구현합니다. 이후 이러한 조합 동작에 대해 운동 추적 강화 학습 전문가 정책을 훈련하고, DAgger와 RL을 결합한 방법으로 이를 단일의 깊이 인식 다중 스킬 학생 정책으로 증류합니다. 최종적으로 로봇은 온보드 깊이 센서와 이산 2D 속도 명령만으로 자율적으로 다양한 기하학적 형태와 높이의 장애물을 넘고, 기어오르고, 점프하거나 구르는 결정을 내릴 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **동작 매칭 계층**: 인간 모션 캡처 데이터를 로봇 운동학으로 리타게팅하고, 특징 공간에서의 최근접 이웃 탐색을 통해 원자적 스킬(예: 보폭, 기어오르기, 점프)을 동적으로 조합하여 연속적이고 부드러운 장기 운동 궤적을 생성합니다.
- **정책 훈련**: 각 조합 동작에 대해 독립적인 운동 추적 RL 전문가 정책을 훈련한 후, DAgger와 RL의 결합 증류 방법을 통해 이를 단일의 깊이 인식 다중 스킬 학생 정책으로 통합하여 배포 복잡성을 낮춥니다.
- **인식 및 의사 결정**: 학생 정책은 온보드 깊이 카메라와 이산 2D 속도 명령에만 의존하여 장애물의 기하학적 특징을 실시간으로 인식하고, 자율적으로 해당 동작(예: 넘기, 기어오르기, 구르기)을 선택 및 실행합니다.

### 실험 설정 및 주요 결과
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇, 온보드 깊이 센서 탑재.
- **장애물 테스트**:
  - 정적 장애물: 로봇 키의 96%에 해당하는 1.25m 높이의 수직 장애물을 성공적으로 기어오름.
  - 동적 시나리오: 장기 다중 장애물 통과에서 장애물 위치 변동(예: 갑작스럽게 이동하는 상자)에 실시간 적응.
- **스킬 다양성**: 넘기, 기어오르기, 점프, 구르기의 네 가지 동적 동작의 폐루프 조합을 구현하며, 사전 프로그래밍된 전환 로직 없이 동작.

### 결론
PHP 프레임워크는 동작 매칭과 인식 기반 정책 증류를 통해 휴머노이드 로봇에서 처음으로 인간형 동적 파쿠르 능력을 구현했으며, 모듈식 스킬 조합의 복잡한 지형에서의 견고성과 적응성을 검증했습니다.
