---
$id: ent_paper_antagonistic_bowden_cable_actu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained
    Humanoids'
  zh: 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained
    Humanoids'
  ko: 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained
    Humanoids'
summary:
  en: 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained
    Humanoids is a 2025 work on hardware design for humanoid robots.'
  zh: 本文提出一种轻量级仿人机器人手，采用Bowden线缆驱动与拮抗式线缆传动相结合的设计，将驱动模块移至躯干以减轻末端质量。该手部末端质量仅236克，指尖力超过18N，可抓取超过自身重量百倍的负载，在负载受限的人形机器人上实现了灵巧操作能力。
  ko: 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained
    Humanoids is a 2025 work on hardware design for humanoid robots.'
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
- antagonistic_bowden_cable_actu
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24657v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained
    Humanoids (arXiv)'
  url: https://arxiv.org/abs/2512.24657
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人对手部高抓取力、快速驱动、多自由度与轻量化结构的矛盾需求，本文提出一种Bowden线缆驱动的轻量仿人手。通过将滚动接触关节优化与拮抗式线缆传动结合，实现单电机控制单关节且线缆长度偏差可忽略。驱动模块移至躯干的设计大幅降低末端质量，同时保持仿人尺寸与灵巧性，且拮抗式传动无需电机同步。实验表明，末端质量236克的手部可执行灵巧任务，指尖力超18N，负载能力超自重百倍，并通过Cutkosky分类抓取与轨迹一致性验证了鲁棒性。

## 核心内容
### 方法
- **拮抗式Bowden线缆驱动**：采用双线缆拮抗配置，每关节由单个电机通过Bowden线缆驱动，线缆长度偏差极小，无需电机同步。
- **滚动接触关节优化**：关节设计结合滚动接触结构，减少摩擦与磨损，提升传动效率与精度。
- **驱动模块后置**：将电机与传动系统移至躯干，仅保留线缆与末端执行器，手部末端质量降至236克（不含远程驱动器和Bowden护套）。

### 实验设置
- **硬件平台**：仿人手尺寸符合人类比例，总自由度未明确列出，但支持多指灵巧操作。
- **性能测试**：测量指尖力、负载能力、抓取稳定性与轨迹一致性。
- **鲁棒性验证**：采用Cutkosky分类法评估抓取类型覆盖，并在驱动-手部变换受扰动时测试轨迹重复性。

### 关键数字
- **末端质量**：236克（不含远程组件）。
- **指尖力**：超过18N。
- **负载能力**：可抓取超过自身质量100倍的物体。
- **驱动方式**：单电机控制单关节，拮抗式线缆传动。

### 结论
该设计通过拮抗式Bowden线缆驱动与滚动接触关节优化，在保持轻量化与仿人尺寸的同时，实现了高抓取力与灵巧操作能力，适用于负载受限的人形机器人。实验验证了其在高负载与扰动条件下的鲁棒性，为下一代灵巧手硬件提供了可行方案。

## Overview
Humanoid robots toward human-level dexterity require robotic hands capable of simultaneously providing high grasping force, rapid actuation speeds, multiple degrees of freedom, and lightweight structures within human-like size constraints. Meeting these conflicting requirements remains challenging, as satisfying this combination typically necessitates heavier actuators and bulkier transmission systems, significantly restricting the payload capacity of robot arms. In this letter, we present a lightweight anthropomorphic hand actuated by Bowden cables, which uniquely combines rolling-contact joint optimization with antagonistic cable actuation, enabling single-motor-per-joint control with negligible cable-length deviation. By relocating the actuator module to the torso, the design substantially reduces distal mass while maintaining anthropomorphic scale and dexterity. Additionally, this antagonistic cable actuation eliminates the need for synchronization between motors. Using the proposed methods, the hand assembly with a distal mass of 236g (excluding remote actuators and Bowden sheaths) demonstrated reliable execution of dexterous tasks, exceeding 18N fingertip force and lifting payloads over one hundred times its own mass. Furthermore, robustness was validated through Cutkosky taxonomy grasps and trajectory consistency under perturbed actuator-hand transformations.

## 개요
인간 수준의 손재주를 목표로 하는 휴머노이드 로봇은 인간과 유사한 크기 제약 내에서 높은 파지력, 빠른 구동 속도, 다중 자유도, 경량 구조를 동시에 제공할 수 있는 로봇 손을 필요로 합니다. 이러한 상충되는 요구 사항을 충족하는 것은 여전히 어려운 과제이며, 이러한 조합을 만족시키기 위해서는 일반적으로 더 무거운 액추에이터와 부피가 큰 전달 시스템이 필요하여 로봇 팔의 페이로드 용량이 크게 제한됩니다. 본 논문에서는 Bowden 케이블로 구동되는 경량 인체공학적 손을 제시하며, 이는 롤링 접촉 관절 최적화와 대항 케이블 구동을 독특하게 결합하여 무시할 수 있는 케이블 길이 편차로 관절당 단일 모터 제어를 가능하게 합니다. 액추에이터 모듈을 몸통으로 재배치함으로써, 이 설계는 인체공학적 규모와 손재주를 유지하면서 원위 질량을 크게 줄입니다. 또한, 이 대항 케이블 구동은 모터 간 동기화의 필요성을 제거합니다. 제안된 방법을 사용하여, 원위 질량이 236g(원격 액추에이터 및 Bowden 시스 제외)인 손 어셈블리는 18N 이상의 손끝 힘과 자체 질량의 100배가 넘는 페이로드를 들어 올리며 손재주가 필요한 작업을 안정적으로 수행함을 입증했습니다. 또한, Cutkosky 분류법 파지 및 교란된 액추에이터-손 변환 하에서의 궤적 일관성을 통해 견고성이 검증되었습니다.

## 핵심 내용
인간 수준의 손재주를 목표로 하는 휴머노이드 로봇은 인간과 유사한 크기 제약 내에서 높은 파지력, 빠른 구동 속도, 다중 자유도, 경량 구조를 동시에 제공할 수 있는 로봇 손을 필요로 합니다. 이러한 상충되는 요구 사항을 충족하는 것은 여전히 어려운 과제이며, 이러한 조합을 만족시키기 위해서는 일반적으로 더 무거운 액추에이터와 부피가 큰 전달 시스템이 필요하여 로봇 팔의 페이로드 용량이 크게 제한됩니다. 본 논문에서는 Bowden 케이블로 구동되는 경량 인체공학적 손을 제시하며, 이는 롤링 접촉 관절 최적화와 대항 케이블 구동을 독특하게 결합하여 무시할 수 있는 케이블 길이 편차로 관절당 단일 모터 제어를 가능하게 합니다. 액추에이터 모듈을 몸통으로 재배치함으로써, 이 설계는 인체공학적 규모와 손재주를 유지하면서 원위 질량을 크게 줄입니다. 또한, 이 대항 케이블 구동은 모터 간 동기화의 필요성을 제거합니다. 제안된 방법을 사용하여, 원위 질량이 236g(원격 액추에이터 및 Bowden 시스 제외)인 손 어셈블리는 18N 이상의 손끝 힘과 자체 질량의 100배가 넘는 페이로드를 들어 올리며 손재주가 필요한 작업을 안정적으로 수행함을 입증했습니다. 또한, Cutkosky 분류법 파지 및 교란된 액추에이터-손 변환 하에서의 궤적 일관성을 통해 견고성이 검증되었습니다.

## 参考
- http://arxiv.org/abs/2512.24657v1
