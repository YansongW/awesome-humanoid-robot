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
  zh: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02331v1.
sources:
- id: src_001
  type: paper
  title: 'TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour (arXiv)'
  url: https://arxiv.org/abs/2602.02331
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries. We adopt a two-stage end-to-end learning paradigm: a policy is first pre-trained on diverse procedurally generated terrains, followed by rapid fine-tuning on high-fidelity meshes reconstructed from real-world captures. Specifically, we develop a feed-forward, efficient, and high-fidelity geometry reconstruction pipeline using RGB-D inputs, ensuring both speed and quality during test-time training. We demonstrate that TTT-Parkour empowers humanoid robots to master complex obstacles, including wedges, stakes, boxes, trapezoids, and narrow beams. The whole pipeline of capturing, reconstructing, and test-time training requires less than 10 minutes on most tested terrains. Extensive experiments show that the policy after test-time training exhibits robust zero-shot sim-to-real transfer capability.

## 核心内容
Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries. We adopt a two-stage end-to-end learning paradigm: a policy is first pre-trained on diverse procedurally generated terrains, followed by rapid fine-tuning on high-fidelity meshes reconstructed from real-world captures. Specifically, we develop a feed-forward, efficient, and high-fidelity geometry reconstruction pipeline using RGB-D inputs, ensuring both speed and quality during test-time training. We demonstrate that TTT-Parkour empowers humanoid robots to master complex obstacles, including wedges, stakes, boxes, trapezoids, and narrow beams. The whole pipeline of capturing, reconstructing, and test-time training requires less than 10 minutes on most tested terrains. Extensive experiments show that the policy after test-time training exhibits robust zero-shot sim-to-real transfer capability.

## 参考
- http://arxiv.org/abs/2602.02331v1

## Overview
Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries. We adopt a two-stage end-to-end learning paradigm: a policy is first pre-trained on diverse procedurally generated terrains, followed by rapid fine-tuning on high-fidelity meshes reconstructed from real-world captures. Specifically, we develop a feed-forward, efficient, and high-fidelity geometry reconstruction pipeline using RGB-D inputs, ensuring both speed and quality during test-time training. We demonstrate that TTT-Parkour empowers humanoid robots to master complex obstacles, including wedges, stakes, boxes, trapezoids, and narrow beams. The whole pipeline of capturing, reconstructing, and test-time training requires less than 10 minutes on most tested terrains. Extensive experiments show that the policy after test-time training exhibits robust zero-shot sim-to-real transfer capability.

## Content
Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries. We adopt a two-stage end-to-end learning paradigm: a policy is first pre-trained on diverse procedurally generated terrains, followed by rapid fine-tuning on high-fidelity meshes reconstructed from real-world captures. Specifically, we develop a feed-forward, efficient, and high-fidelity geometry reconstruction pipeline using RGB-D inputs, ensuring both speed and quality during test-time training. We demonstrate that TTT-Parkour empowers humanoid robots to master complex obstacles, including wedges, stakes, boxes, trapezoids, and narrow beams. The whole pipeline of capturing, reconstructing, and test-time training requires less than 10 minutes on most tested terrains. Extensive experiments show that the policy after test-time training exhibits robust zero-shot sim-to-real transfer capability.

## 개요
보지 못한 복잡한 지형에서 고도로 역동적인 인간형 파쿠르를 구현하는 것은 로봇 공학에서 여전히 과제로 남아 있습니다. 일반적인 보행 정책은 광범위한 지형 분포에서 능력을 보여주지만, 임의적이고 매우 도전적인 환경에서는 종종 어려움을 겪습니다. 이러한 한계를 극복하기 위해, 우리는 새로운 지형에서 빠른 테스트 시간 훈련(TTT)을 활용하는 실물-시뮬레이션-실물 프레임워크를 제안하여, 극도로 어려운 형상을 통과하는 로봇의 능력을 크게 향상시킵니다. 우리는 두 단계의 종단 간 학습 패러다임을 채택합니다: 먼저 다양한 절차적으로 생성된 지형에서 정책을 사전 훈련한 후, 실제 환경 캡처에서 재구성된 고충실도 메시에서 빠른 미세 조정을 수행합니다. 구체적으로, RGB-D 입력을 사용하여 피드포워드, 효율적이며 고충실도 형상 재구성 파이프라인을 개발하여 테스트 시간 훈련 중 속도와 품질을 모두 보장합니다. 우리는 TTT-Parkour가 인간형 로봇이 쐐기, 말뚝, 상자, 사다리꼴 및 좁은 빔을 포함한 복잡한 장애물을 마스터할 수 있게 함을 입증합니다. 캡처, 재구성 및 테스트 시간 훈련의 전체 파이프라인은 대부분의 테스트된 지형에서 10분 미만이 소요됩니다. 광범위한 실험을 통해 테스트 시간 훈련 후의 정책이 강력한 제로샷 시뮬레이션-실물 전이 능력을 보여줍니다.

## 핵심 내용
보지 못한 복잡한 지형에서 고도로 역동적인 인간형 파쿠르를 구현하는 것은 로봇 공학에서 여전히 과제로 남아 있습니다. 일반적인 보행 정책은 광범위한 지형 분포에서 능력을 보여주지만, 임의적이고 매우 도전적인 환경에서는 종종 어려움을 겪습니다. 이러한 한계를 극복하기 위해, 우리는 새로운 지형에서 빠른 테스트 시간 훈련(TTT)을 활용하는 실물-시뮬레이션-실물 프레임워크를 제안하여, 극도로 어려운 형상을 통과하는 로봇의 능력을 크게 향상시킵니다. 우리는 두 단계의 종단 간 학습 패러다임을 채택합니다: 먼저 다양한 절차적으로 생성된 지형에서 정책을 사전 훈련한 후, 실제 환경 캡처에서 재구성된 고충실도 메시에서 빠른 미세 조정을 수행합니다. 구체적으로, RGB-D 입력을 사용하여 피드포워드, 효율적이며 고충실도 형상 재구성 파이프라인을 개발하여 테스트 시간 훈련 중 속도와 품질을 모두 보장합니다. 우리는 TTT-Parkour가 인간형 로봇이 쐐기, 말뚝, 상자, 사다리꼴 및 좁은 빔을 포함한 복잡한 장애물을 마스터할 수 있게 함을 입증합니다. 캡처, 재구성 및 테스트 시간 훈련의 전체 파이프라인은 대부분의 테스트된 지형에서 10분 미만이 소요됩니다. 광범위한 실험을 통해 테스트 시간 훈련 후의 정책이 강력한 제로샷 시뮬레이션-실물 전이 능력을 보여줍니다.
