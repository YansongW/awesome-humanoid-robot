---
$id: ent_paper_ttt_parkour_rapid_test_time_tr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour'
  zh: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour'
  ko: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour'
summary:
  en: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: TTT-Parkour 是 2026 年提出的一种面向人形机器人的快速测试时训练框架，旨在解决未知复杂地形上的动态跑酷难题。其核心贡献在于通过真实到仿真再到真实的闭环流程，结合高效几何重建与两阶段端到端学习，使机器人在不到 10 分钟内掌握楔形、窄梁等极端障碍的穿越能力，并实现零样本仿真到现实的迁移。
  ko: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- ttt_parkour
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02331v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (701 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour (arXiv)'
  url: https://arxiv.org/abs/2602.02331
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
尽管通用运动策略在广泛地形分布上展现出一定能力，但在面对任意且极具挑战性的环境时仍显不足。为此，TTT-Parkour 提出了一种真实到仿真再到真实的框架，利用快速测试时训练显著提升机器人穿越极端困难几何地形的能力。该方法采用两阶段端到端学习范式：首先在多样化的程序化生成地形上预训练策略，随后在从真实场景捕获重建的高保真网格上进行快速微调。具体而言，研究团队开发了一种基于 RGB-D 输入的前馈式高效高保真几何重建流水线，确保测试时训练的速度与质量。实验表明，该框架使人形机器人能够掌握楔形、木桩、箱子、梯形和窄梁等复杂障碍，且整个捕获、重建与测试时训练流程在多数测试地形上耗时不足 10 分钟。

## 核心内容
### 方法架构
- **两阶段端到端学习**：第一阶段在程序化生成的地形上预训练策略，第二阶段利用真实场景重建的高保真网格进行快速微调。
- **高效几何重建流水线**：基于 RGB-D 输入的前馈式设计，兼顾速度与保真度，确保测试时训练的实时性。

### 实验设置
- **测试地形**：包括楔形、木桩、箱子、梯形和窄梁等极端复杂障碍。
- **时间效率**：整个流程（捕获、重建、测试时训练）在多数地形上耗时少于 10 分钟。
- **迁移能力**：经过测试时训练的策略展现出鲁棒的零样本仿真到现实迁移能力。

### 关键结论
- TTT-Parkour 显著增强了人形机器人在未见复杂地形上的动态跑酷能力。
- 快速测试时训练是克服通用策略在极端环境下性能瓶颈的有效手段。
- 高保真几何重建与两阶段学习范式的结合，为真实世界部署提供了高效且可靠的解决方案。

## Overview
Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries. We adopt a two-stage end-to-end learning paradigm: a policy is first pre-trained on diverse procedurally generated terrains, followed by rapid fine-tuning on high-fidelity meshes reconstructed from real-world captures. Specifically, we develop a feed-forward, efficient, and high-fidelity geometry reconstruction pipeline using RGB-D inputs, ensuring both speed and quality during test-time training. We demonstrate that TTT-Parkour empowers humanoid robots to master complex obstacles, including wedges, stakes, boxes, trapezoids, and narrow beams. The whole pipeline of capturing, reconstructing, and test-time training requires less than 10 minutes on most tested terrains. Extensive experiments show that the policy after test-time training exhibits robust zero-shot sim-to-real transfer capability.

## 参考
- http://arxiv.org/abs/2602.02331v1

## 개요
일반적인 운동 정책이 광범위한 지형 분포에서 일정 수준의 능력을 보여주지만, 임의적이고 매우 도전적인 환경에서는 여전히 부족함을 드러낸다. 이를 해결하기 위해 TTT-Parkour는 실제-시뮬레이션-실제 프레임워크를 제안하며, 빠른 테스트 타임 트레이닝을 활용하여 로봇이 극도로 어려운 기하학적 지형을 통과하는 능력을 크게 향상시킨다. 이 방법은 두 단계의 엔드투엔드 학습 패러다임을 채택한다: 먼저 다양한 절차적 생성 지형에서 정책을 사전 훈련하고, 이후 실제 장면에서 캡처 및 재구성된 고충실도 메시에서 빠른 미세 조정을 수행한다. 구체적으로, 연구팀은 RGB-D 입력 기반의 피드포워드 방식의 효율적이고 고충실도 기하학 재구성 파이프라인을 개발하여 테스트 타임 트레이닝의 속도와 품질을 보장한다. 실험 결과, 이 프레임워크는 인간형 로봇이 쐐기형, 나무 말뚝, 상자, 사다리꼴, 좁은 빔과 같은 복잡한 장애물을 마스터할 수 있게 하며, 캡처, 재구성, 테스트 타임 트레이닝 전체 프로세스는 대부분의 테스트 지형에서 10분 미만이 소요된다.

## 핵심 내용
### 방법 아키텍처
- **두 단계 엔드투엔드 학습**: 첫 번째 단계는 절차적 생성 지형에서 정책을 사전 훈련하고, 두 번째 단계는 실제 장면에서 재구성된 고충실도 메시를 활용한 빠른 미세 조정을 수행한다.
- **효율적인 기하학 재구성 파이프라인**: RGB-D 입력 기반의 피드포워드 설계로 속도와 충실도를 균형 있게 유지하며, 테스트 타임 트레이닝의 실시간성을 보장한다.

### 실험 설정
- **테스트 지형**: 쐐기형, 나무 말뚝, 상자, 사다리꼴, 좁은 빔과 같은 극도로 복잡한 장애물을 포함한다.
- **시간 효율성**: 전체 프로세스(캡처, 재구성, 테스트 타임 트레이닝)는 대부분의 지형에서 10분 미만이 소요된다.
- **전이 능력**: 테스트 타임 트레이닝을 거친 정책은 강력한 제로샷 시뮬레이션-실제 전이 능력을 보여준다.

### 주요 결론
- TTT-Parkour는 인간형 로봇의 보지 못한 복잡한 지형에서의 동적 파쿠르 능력을 크게 향상시킨다.
- 빠른 테스트 타임 트레이닝은 일반 정책의 극한 환경에서의 성능 병목을 극복하는 효과적인 수단이다.
- 고충실도 기하학 재구성과 두 단계 학습 패러다임의 결합은 실제 세계 배포를 위한 효율적이고 신뢰할 수 있는 솔루션을 제공한다.
