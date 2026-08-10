---
$id: ent_paper_ze_twist2_scalable_portable_and_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
  zh: TWIST2：可扩展、便携且整体化的人形机器人数据采集系统
  ko: 'TWIST2: 확장 가능하고 휴대 가능하며 전체적인 휴머노이드 데이터 수집 시스템'
summary:
  en: TWIST2 introduces a portable, mocap-free whole-body humanoid teleoperation and data collection system using PICO4U VR
    tracking and a low-cost 2-DoF neck, together with a hierarchical visuomotor policy for autonomous full-body control.
  zh: TWIST2 是由研究团队提出的一套便携式、无需动作捕捉的全身人形机器人遥操作与数据采集系统。该系统利用 PICO4U VR 追踪和低成本 2-DoF 颈部模块实现全身控制，并配套提出分层视觉运动策略用于自主全身控制，核心贡献在于提升了数据采集的可扩展性与可复现性。
  ko: TWIST2는 PICO4U VR 추적과 저비용 2-DoF 목을 활용한 휴대 가능하고 mocap이 불필요한 전신 휴머노이드 원격 조작 및 데이터 수집 시스템을 제안하며, 자율 전신 제어를 위한 계층적 시각-운동
    정책을 함께 소개한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- teleoperation
- whole_body_control
- visuomotor_policy
- data_collection
- humanoid
- mocap_free
- diffusion_policy
- egocentric_vision
- reinforcement_learning
- retargeting
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.02832v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (800 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
  url: https://arxiv.org/abs/2511.02832
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
TWIST2 解决了人形机器人领域缺乏高效数据采集框架的问题，通过 PICO4U VR 设备实时获取全身人体运动，并设计了一个成本约 250 美元的 2-DoF 机器人颈部模块用于第一人称视觉，实现了完整的人到人形机器人的全身映射。该系统能在 15 分钟内以接近 100% 的成功率采集 100 组演示数据，并在此基础上提出了基于第一人称视觉的分层视觉运动策略，成功完成了全身灵巧操作和动态踢球等任务。整个系统完全开源，数据集也已公开。

## 核心内容
### 系统架构
TWIST2 的核心设计围绕便携性与全身控制展开：
- **遥操作模块**：采用 PICO4U VR 头显进行实时全身运动追踪，无需外部动作捕捉设备，降低了部署成本与复杂度。
- **颈部模块**：定制 2-DoF 机器人颈部（成本约 250 美元），用于承载第一人称视觉传感器，实现与人类头部运动同步的 egocentric 视角。
- **全身控制**：通过 VR 追踪数据直接映射到人形机器人全身关节，支持长时程灵巧操作与移动任务。

### 数据采集性能
- **效率**：在 15 分钟内可采集 100 组演示数据，成功率接近 100%。
- **可扩展性**：系统设计强调便携与低成本，便于大规模部署与数据积累。

### 自主控制策略
基于采集的数据，提出分层视觉运动策略：
- **底层**：基于 egocentric 视觉输入，学习全身运动映射。
- **上层**：实现全身灵巧操作（如抓取、搬运）与动态任务（如踢球）。
- **实验验证**：在真实人形机器人上成功演示了上述任务，证明了策略的有效性。

### 开源与数据
- 系统完整代码与硬件设计已开源：https://yanjieze.com/TWIST2
- 采集的数据集公开于：https://twist-data.github.io

## Overview
Large-scale data has driven breakthroughs in robotics, from language models to vision-language-action models in bimanual manipulation. However, humanoid robotics lacks equally effective data collection frameworks. Existing humanoid teleoperation systems either use decoupled control or depend on expensive motion capture setups. We introduce TWIST2, a portable, mocap-free humanoid teleoperation and data collection system that preserves full whole-body control while advancing scalability. Our system leverages PICO4U VR for obtaining real-time whole-body human motions, with a custom 2-DoF robot neck (cost around $250) for egocentric vision, enabling holistic human-to-humanoid control. We demonstrate long-horizon dexterous and mobile humanoid skills and we can collect 100 demonstrations in 15 minutes with an almost 100% success rate. Building on this pipeline, we propose a hierarchical visuomotor policy framework that autonomously controls the full humanoid body based on egocentric vision. Our visuomotor policy successfully demonstrates whole-body dexterous manipulation and dynamic kicking tasks. The entire system is fully reproducible and open-sourced at https://yanjieze.com/TWIST2 . Our collected dataset is also open-sourced at https://twist-data.github.io .

## 参考
- http://arxiv.org/abs/2511.02832v1

## 개요
TWIST2는 휴머노이드 로봇 분야에서 효율적인 데이터 수집 프레임워크가 부족한 문제를 해결하며, PICO4U VR 기기를 통해 실시간으로 전신 인체 모션을 획득하고, 약 250달러의 2-DoF 로봇 목 모듈을 설계하여 1인칭 시각을 구현함으로써 인간에서 휴머노이드 로봇으로의 완전한 전신 매핑을 달성했습니다. 이 시스템은 15분 이내에 약 100%의 성공률로 100세트의 시연 데이터를 수집할 수 있으며, 이를 기반으로 1인칭 시각 기반의 계층적 시각 운동 정책을 제안하여 전신 손재주 조작과 동적 축구 등의 작업을 성공적으로 완료했습니다. 전체 시스템은 완전히 오픈소스이며, 데이터셋도 공개되었습니다.

## 핵심 내용
### 시스템 아키텍처
TWIST2의 핵심 설계는 휴대성과 전신 제어에 중점을 둡니다:
- **원격 조작 모듈**: PICO4U VR 헤드셋을 사용하여 실시간 전신 모션 추적을 수행하며, 외부 모션 캡처 장비가 필요 없어 배포 비용과 복잡성을 낮춥니다.
- **목 모듈**: 맞춤형 2-DoF 로봇 목(약 250달러)을 설계하여 1인칭 시각 센서를 탑재하고, 인간의 머리 움직임과 동기화된 egocentric 시점을 구현합니다.
- **전신 제어**: VR 추적 데이터를 휴머노이드 로봇의 전신 관절에 직접 매핑하여 장시간 손재주 조작 및 이동 작업을 지원합니다.

### 데이터 수집 성능
- **효율성**: 15분 이내에 100세트의 시연 데이터를 수집할 수 있으며, 성공률은 약 100%입니다.
- **확장성**: 시스템 설계는 휴대성과 저비용을 강조하여 대규모 배포와 데이터 축적을 용이하게 합니다.

### 자율 제어 전략
수집된 데이터를 기반으로 계층적 시각 운동 정책을 제안합니다:
- **하위 계층**: egocentric 시각 입력을 기반으로 전신 운동 매핑을 학습합니다.
- **상위 계층**: 전신 손재주 조작(예: 잡기, 운반) 및 동적 작업(예: 축구)을 구현합니다.
- **실험 검증**: 실제 휴머노이드 로봇에서 위 작업을 성공적으로 시연하여 정책의 효과성을 입증했습니다.

### 오픈소스 및 데이터
- 시스템의 전체 코드와 하드웨어 설계가 오픈소스로 공개되었습니다: https://yanjieze.com/TWIST2
- 수집된 데이터셋은 다음에서 공개되었습니다: https://twist-data.github.io
