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
  zh: OSMO 是一款 2025 年发布的开源可穿戴触觉手套，由研究团队设计用于人形机器人的技能迁移。其核心贡献在于通过 12 个三轴触觉传感器实现人手与机器人之间的触觉信号直接传递，使仅基于人类演示训练的机器人策略在接触密集型任务中达到
    72% 的成功率，无需任何真实机器人数据。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08920v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer (arXiv)'
  url: https://arxiv.org/abs/2512.08920
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
OSMO 手套在指尖和手掌处集成了 12 个三轴触觉传感器，兼容主流手部追踪方法以支持野外数据采集。该设计通过让人类和机器人佩戴相同手套，最小化视觉与触觉的具身差距，直接传递连续剪切力和法向力反馈，避免了图像修复或基于视觉的力推断。在需要持续接触压力的真实擦拭任务中，基于触觉的策略消除了接触相关故障模式，性能显著优于纯视觉基线。

## 核心内容
### 方法
- **硬件设计**：手套配备 12 个三轴触觉传感器，分布于指尖和手掌区域，支持高分辨率接触力采集。
- **数据采集**：兼容 SOTA 手部追踪方法，可在野外环境中收集人类演示数据，无需受控实验室条件。
- **技能迁移**：人类和机器人佩戴相同手套，直接传递连续剪切力和法向力反馈，消除视觉与触觉的具身差距，避免图像修复或视觉力推断。

### 实验设置
- **任务**：真实世界擦拭任务，要求持续接触压力。
- **训练数据**：仅使用 OSMO 收集的人类演示数据，无任何真实机器人数据。
- **基线**：纯视觉策略（无触觉反馈）。

### 关键结果
- **成功率**：触觉感知策略达到 72% 成功率，显著高于纯视觉基线。
- **故障模式**：触觉策略消除了接触相关故障，如压力不足或滑脱。

### 结论
OSMO 通过开源硬件设计，证明了触觉反馈在接触密集型机器人任务中的关键作用，为社区提供了完整的硬件设计、固件和组装指南。

## Overview
Human video demonstrations provide abundant training data for learning robot policies, but video alone cannot capture the rich contact signals critical for mastering manipulation. We introduce OSMO, an open-source wearable tactile glove designed for human-to-robot skill transfer. The glove features 12 three-axis tactile sensors across the fingertips and palm and is designed to be compatible with state-of-the-art hand-tracking methods for in-the-wild data collection. We demonstrate that a robot policy trained exclusively on human demonstrations collected with OSMO, without any real robot data, is capable of executing a challenging contact-rich manipulation task. By equipping both the human and the robot with the same glove, OSMO minimizes the visual and tactile embodiment gap, enabling the transfer of continuous shear and normal force feedback while avoiding the need for image inpainting or other vision-based force inference. On a real-world wiping task requiring sustained contact pressure, our tactile-aware policy achieves a 72% success rate, outperforming vision-only baselines by eliminating contact-related failure modes. We release complete hardware designs, firmware, and assembly instructions to support community adoption.

## 개요
인간의 비디오 시연은 로봇 정책 학습을 위한 풍부한 훈련 데이터를 제공하지만, 비디오만으로는 조작 기술 습득에 중요한 접촉 신호를 포착할 수 없습니다. 우리는 인간-로봇 기술 전이를 위해 설계된 오픈소스 웨어러블 촉각 장갑인 OSMO를 소개합니다. 이 장갑은 손가락 끝과 손바닥에 12개의 3축 촉각 센서를 갖추고 있으며, 실제 환경 데이터 수집을 위한 최첨단 손 추적 방법과 호환되도록 설계되었습니다. 우리는 OSMO로 수집된 인간 시연 데이터만으로 훈련된 로봇 정책이 실제 로봇 데이터 없이도 어려운 접촉 기반 조작 작업을 실행할 수 있음을 입증했습니다. 인간과 로봇 모두에 동일한 장갑을 장착함으로써 OSMO는 시각적 및 촉각적 구현 격차를 최소화하고, 이미지 인페인팅이나 다른 비전 기반 힘 추론 없이도 연속적인 전단력 및 수직력 피드백 전이를 가능하게 합니다. 지속적인 접촉 압력이 필요한 실제 닦기 작업에서, 우리의 촉각 인식 정책은 72%의 성공률을 달성하여 접촉 관련 실패 모드를 제거함으로써 비전 전용 기준선을 능가했습니다. 우리는 커뮤니티 채택을 지원하기 위해 완전한 하드웨어 설계, 펌웨어 및 조립 지침을 공개합니다.

## 핵심 내용
인간의 비디오 시연은 로봇 정책 학습을 위한 풍부한 훈련 데이터를 제공하지만, 비디오만으로는 조작 기술 습득에 중요한 접촉 신호를 포착할 수 없습니다. 우리는 인간-로봇 기술 전이를 위해 설계된 오픈소스 웨어러블 촉각 장갑인 OSMO를 소개합니다. 이 장갑은 손가락 끝과 손바닥에 12개의 3축 촉각 센서를 갖추고 있으며, 실제 환경 데이터 수집을 위한 최첨단 손 추적 방법과 호환되도록 설계되었습니다. 우리는 OSMO로 수집된 인간 시연 데이터만으로 훈련된 로봇 정책이 실제 로봇 데이터 없이도 어려운 접촉 기반 조작 작업을 실행할 수 있음을 입증했습니다. 인간과 로봇 모두에 동일한 장갑을 장착함으로써 OSMO는 시각적 및 촉각적 구현 격차를 최소화하고, 이미지 인페인팅이나 다른 비전 기반 힘 추론 없이도 연속적인 전단력 및 수직력 피드백 전이를 가능하게 합니다. 지속적인 접촉 압력이 필요한 실제 닦기 작업에서, 우리의 촉각 인식 정책은 72%의 성공률을 달성하여 접촉 관련 실패 모드를 제거함으로써 비전 전용 기준선을 능가했습니다. 우리는 커뮤니티 채택을 지원하기 위해 완전한 하드웨어 설계, 펌웨어 및 조립 지침을 공개합니다.

## 参考
- http://arxiv.org/abs/2512.08920v1
