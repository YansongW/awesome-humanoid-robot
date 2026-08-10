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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24657v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (799 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.24657v1

## 개요
인간형 로봇의 손에 대한 높은 파지력, 빠른 구동, 다자유도, 경량 구조라는 상충되는 요구를 해결하기 위해, 본 논문은 Bowden 케이블 구동 방식의 경량 인간형 손을 제안한다. 구름 접촉 관절 최적화와 길항식 케이블 전동을 결합하여, 단일 모터가 단일 관절을 제어하면서 케이블 길이 편차를 무시할 수 있도록 구현했다. 구동 모듈을 몸통으로 이동시킨 설계는 말단 질량을 크게 줄이면서도 인간형 크기와 기민성을 유지하며, 길항식 전동은 모터 동기화를 필요로 하지 않는다. 실험 결과, 말단 질량 236g의 손으로 기민한 작업을 수행할 수 있고, 손끝 힘은 18N을 초과하며, 부하 능력은 자체 중량의 100배를 초과한다. 또한 Cutkosky 분류 파지와 궤적 일관성을 통해 강건성을 검증했다.

## 핵심 내용
### 방법
- **길항식 Bowden 케이블 구동**: 이중 케이블 길항 구성을 채택하여, 각 관절은 단일 모터가 Bowden 케이블을 통해 구동하며, 케이블 길이 편차가 매우 작아 모터 동기화가 필요 없다.
- **구름 접촉 관절 최적화**: 관절 설계에 구름 접촉 구조를 결합하여 마찰과 마모를 줄이고, 전동 효율과 정밀도를 향상시킨다.
- **구동 모듈 후방 배치**: 모터와 전동 시스템을 몸통으로 이동시키고, 케이블과 말단 실행기만 남겨 손 말단 질량을 236g(원격 구동기 및 Bowden 외장 제외)으로 줄인다.

### 실험 설정
- **하드웨어 플랫폼**: 인간형 손 크기는 인간 비율에 부합하며, 총 자유도는 명시되지 않았지만 다지 기민한 조작을 지원한다.
- **성능 테스트**: 손끝 힘, 부하 능력, 파지 안정성 및 궤적 일관성을 측정한다.
- **강건성 검증**: Cutkosky 분류법을 사용하여 파지 유형 범위를 평가하고, 구동-손 변환에 교란이 있을 때 궤적 반복성을 테스트한다.

### 주요 수치
- **말단 질량**: 236g(원격 구성 요소 제외).
- **손끝 힘**: 18N 초과.
- **부하 능력**: 자체 질량의 100배를 초과하는 물체를 파지할 수 있음.
- **구동 방식**: 단일 모터가 단일 관절을 제어하며, 길항식 케이블 전동을 사용.

### 결론
본 설계는 길항식 Bowden 케이블 구동과 구름 접촉 관절 최적화를 통해 경량화와 인간형 크기를 유지하면서도 높은 파지력과 기민한 조작 능력을 구현하여, 부하 제한이 있는 인간형 로봇에 적합하다. 실험은 고부하 및 교란 조건에서의 강건성을 검증했으며, 차세대 기민한 손 하드웨어에 실현 가능한 솔루션을 제공한다.
