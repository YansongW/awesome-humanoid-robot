---
$id: ent_paper_lapsurgie_humanoid_robots_perf_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy'
  zh: 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy'
  ko: 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy'
summary:
  en: 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy is a 2025 work on teleoperation
    for humanoid robots.'
  zh: LapSurgie 是 2025 年提出的首个基于人形机器人的腹腔镜遥操作框架。该系统通过逆映射策略实现手动腕式腹腔镜器械的精确控制，无需额外设置即可使用现成手术工具。用户研究验证了该框架的有效性，为在腹腔镜手术中部署人形机器人提供了初步可行性证据。
  ko: 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy is a 2025 work on teleoperation
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
- lapsurgie
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.03529v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (548 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy (arXiv)'
  url: https://arxiv.org/abs/2510.03529
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
LapSurgie 旨在解决手术机器人系统在资源匮乏地区部署困难的问题。该框架利用人形机器人直接操作现有手术环境，通过逆映射策略满足远程中心运动约束，实现手持腹腔镜器械的精确控制。系统配备立体视觉控制台提供实时视觉反馈，用户研究跨平台验证了其有效性。

## 核心内容
### 背景与动机
- 机器人腹腔镜手术虽能提高微创手术效率与精度，但现有平台多局限于高资源医疗中心，加剧了农村与低资源地区的医疗不平等。
- 远程指导与全远程手术等方案尚未解决实际部署难题，而人形机器人可直接在人类设计的环境中（包括手术室）操作，无需大规模基础设施改造。

### 核心方法
- **逆映射策略**：针对手动腕式腹腔镜器械设计，自动满足远程中心运动约束，实现手到工具的精确控制。
- **兼容性**：可直接使用现成手术腹腔镜工具，无需额外设置或改装。
- **控制台**：配备立体视觉系统，提供实时视觉反馈，增强操作沉浸感。

### 实验设置与结果
- 用户研究跨多个平台进行，评估框架在不同条件下的性能。
- 结果表明，LapSurgie 能有效完成腹腔镜操作任务，初步验证了人形机器人在腹腔镜手术中的部署可行性。
- 关键数字：未在原文中提供具体数值，但强调“有效性”与“初步可行性证据”。

## Overview
Robotic laparoscopic surgery has gained increasing attention in recent years for its potential to deliver more efficient and precise minimally invasive procedures. However, adoption of surgical robotic platforms remains largely confined to high-resource medical centers, exacerbating healthcare disparities in rural and low-resource regions. To close this gap, a range of solutions has been explored, from remote mentorship to fully remote telesurgery. Yet, the practical deployment of surgical robotic systems to underserved communities remains an unsolved challenge. Humanoid systems offer a promising path toward deployability, as they can directly operate in environments designed for humans without extensive infrastructure modifications -- including operating rooms. In this work, we introduce LapSurgie, the first humanoid-robot-based laparoscopic teleoperation framework. The system leverages an inverse-mapping strategy for manual-wristed laparoscopic instruments that abides to remote center-of-motion constraints, enabling precise hand-to-tool control of off-the-shelf surgical laparoscopic tools without additional setup requirements. A control console equipped with a stereo vision system provides real-time visual feedback. Finally, a comprehensive user study across platforms demonstrates the effectiveness of the proposed framework and provides initial evidence for the feasibility of deploying humanoid robots in laparoscopic procedures.

## 参考
- http://arxiv.org/abs/2510.03529v2

## 개요
LapSurgie는 자원이 부족한 지역에서 수술 로봇 시스템의 배포가 어려운 문제를 해결하기 위해 설계되었습니다. 이 프레임워크는 휴머노이드 로봇을 활용하여 기존 수술 환경을 직접 조작하며, 역매핑 전략을 통해 원격 중심 운동 제약을 충족하고 휴대용 복강경 기구의 정밀 제어를 구현합니다. 시스템에는 실시간 시각적 피드백을 제공하는 입체 시각 콘솔이 포함되어 있으며, 사용자 연구를 통해 여러 플랫폼에서 그 효과가 검증되었습니다.

## 핵심 내용
### 배경 및 동기
- 로봇 복강경 수술은 최소 침습 수술의 효율성과 정밀도를 향상시킬 수 있지만, 기존 플랫폼은 주로 고자원 의료 센터에 국한되어 농촌 및 저자원 지역의 의료 불평등을 악화시킵니다.
- 원격 지도 및 완전 원격 수술과 같은 접근 방식은 실제 배포 문제를 아직 해결하지 못했지만, 휴머노이드 로봇은 수술실을 포함한 인간이 설계한 환경에서 직접 작동할 수 있어 대규모 인프라 개조가 필요하지 않습니다.

### 핵심 방법
- **역매핑 전략**: 수동 손목형 복강경 기구를 위해 설계되었으며, 원격 중심 운동 제약을 자동으로 충족하여 손에서 도구로의 정밀 제어를 구현합니다.
- **호환성**: 추가 설정이나 개조 없이 기성 수술용 복강경 도구를 직접 사용할 수 있습니다.
- **콘솔**: 입체 시각 시스템을 갖추어 실시간 시각적 피드백을 제공하고 조작의 몰입감을 향상시킵니다.

### 실험 설정 및 결과
- 사용자 연구는 여러 플랫폼에서 수행되어 다양한 조건에서 프레임워크의 성능을 평가했습니다.
- 결과는 LapSurgie가 복강경 조작 작업을 효과적으로 완료할 수 있음을 보여주며, 휴머노이드 로봇의 복강경 수술 배포 가능성에 대한 초기 검증을 제공합니다.
- 주요 수치: 원문에는 구체적인 값이 제공되지 않았지만, "효과성"과 "초기 타당성 증거"가 강조되었습니다.
