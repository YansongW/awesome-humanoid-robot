---
$id: ent_paper_osmo_open_source_tactile_glove_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer'
  zh: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer'
  ko: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer'
summary:
  en: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer is a 2025 work on hardware design for humanoid robots.'
  zh: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer is a 2025 work on hardware design for humanoid robots.'
  ko: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer is a 2025 work on hardware design for humanoid robots.'
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
- hardware_design
- humanoid
- osmo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08920v1.
sources:
- id: src_001
  type: paper
  title: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer (arXiv)'
  url: https://arxiv.org/abs/2512.08920
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## 核心内容
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## 参考
- http://arxiv.org/abs/2512.08920v1

## Overview
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## Content
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## 개요
인간의 비디오 시연은 로봇 정책 학습을 위한 풍부한 훈련 데이터를 제공하지만, 비디오만으로는 조작 기술 습득에 중요한 접촉 신호를 포착할 수 없습니다. 우리는 인간-로봇 기술 전이를 위해 설계된 오픈소스 웨어러블 촉각 장갑인 OSMO를 소개합니다. 이 장갑은 손가락 끝과 손바닥에 12개의 3축 촉각 센서를 갖추고 있으며, 실제 환경 데이터 수집을 위한 최첨단 손 추적 방법과 호환되도록 설계되었습니다. 우리는 OSMO로 수집된 인간 시연 데이터만으로 훈련된 로봇 정책이 실제 로봇 데이터 없이도 어려운 접촉 기반 조작 작업을 실행할 수 있음을 입증했습니다. 인간과 로봇 모두에 동일한 장갑을 장착함으로써 OSMO는 시각적 및 촉각적 구현 격차를 최소화하고, 이미지 인페인팅이나 다른 비전 기반 힘 추론 없이도 연속적인 전단력 및 수직력 피드백 전이를 가능하게 합니다. 지속적인 접촉 압력이 필요한 실제 닦기 작업에서, 우리의 촉각 인식 정책은 72%의 성공률을 달성하여 접촉 관련 실패 모드를 제거함으로써 비전 전용 기준선을 능가했습니다. 우리는 커뮤니티 채택을 지원하기 위해 완전한 하드웨어 설계, 펌웨어 및 조립 지침을 공개합니다.

## 핵심 내용
인간의 비디오 시연은 로봇 정책 학습을 위한 풍부한 훈련 데이터를 제공하지만, 비디오만으로는 조작 기술 습득에 중요한 접촉 신호를 포착할 수 없습니다. 우리는 인간-로봇 기술 전이를 위해 설계된 오픈소스 웨어러블 촉각 장갑인 OSMO를 소개합니다. 이 장갑은 손가락 끝과 손바닥에 12개의 3축 촉각 센서를 갖추고 있으며, 실제 환경 데이터 수집을 위한 최첨단 손 추적 방법과 호환되도록 설계되었습니다. 우리는 OSMO로 수집된 인간 시연 데이터만으로 훈련된 로봇 정책이 실제 로봇 데이터 없이도 어려운 접촉 기반 조작 작업을 실행할 수 있음을 입증했습니다. 인간과 로봇 모두에 동일한 장갑을 장착함으로써 OSMO는 시각적 및 촉각적 구현 격차를 최소화하고, 이미지 인페인팅이나 다른 비전 기반 힘 추론 없이도 연속적인 전단력 및 수직력 피드백 전이를 가능하게 합니다. 지속적인 접촉 압력이 필요한 실제 닦기 작업에서, 우리의 촉각 인식 정책은 72%의 성공률을 달성하여 접촉 관련 실패 모드를 제거함으로써 비전 전용 기준선을 능가했습니다. 우리는 커뮤니티 채택을 지원하기 위해 완전한 하드웨어 설계, 펌웨어 및 조립 지침을 공개합니다.
