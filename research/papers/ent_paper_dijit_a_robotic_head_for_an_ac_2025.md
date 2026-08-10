---
$id: ent_paper_dijit_a_robotic_head_for_an_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DIJIT: A Robotic Head for an Active Observer'
  zh: 'DIJIT: A Robotic Head for an Active Observer'
  ko: 'DIJIT: A Robotic Head for an Active Observer'
summary:
  en: 'DIJIT: A Robotic Head for an Active Observer is a 2025 work on hardware design for humanoid robots.'
  zh: DIJIT 是一款专为主动观察型移动代理设计的双目机器人头部，由研究团队于2025年提出。其核心贡献在于实现了9个机械自由度和4个光学自由度，运动性能达到人类水平的85%，并提出了基于相机朝向与电机值直接映射的新型扫视运动方法，左右相机平均误差分别为1.17°和1.14°。
  ko: 'DIJIT: A Robotic Head for an Active Observer is a 2025 work on hardware design for humanoid robots.'
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
- dijit
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07998v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (796 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DIJIT: A Robotic Head for an Active Observer (arXiv)'
  url: https://arxiv.org/abs/2512.07998
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DIJIT 是一款面向主动视觉研究的仿人双目机器人头部硬件，旨在模拟人类眼-头协调运动及其对视力的贡献。该设计包含9个机械自由度和4个光学自由度，运动范围与速度接近人类水平，尤其扫视速度达到人类峰值的85%。DIJIT 支持汇聚立体视觉所需的辐辏、版本和扭转运动，并引入了一种通过相机朝向与电机值直接映射实现扫视运动的新方法，其精度接近人类，左右相机平均误差分别为1.17°和1.14°。

## 核心内容
### 设计目标与功能
DIJIT 专为移动代理设计，使其作为主动观察者进行视觉研究。其核心目标包括：
- 支持主动视觉研究，探索人类眼-头运动模式及其相互关系。
- 对比人类视觉通过眼/头运动解决视觉任务的方式与当前计算机视觉方法的差异。

### 机械与光学架构
- **机械自由度**：共9个，涵盖颈部、眼球等关节，运动范围与速度对标人类性能。
- **光学自由度**：额外4个，由相机与镜头系统提供，增强视觉调节能力。
- **运动能力**：扫视速度达到人类峰值的85%；支持汇聚立体视觉所需的辐辏、版本和扭转运动。

### 扫视运动方法创新
提出一种基于相机朝向与电机值直接映射的扫视控制方法，无需复杂中间计算：
- **精度表现**：左相机平均误差1.17°，右相机平均误差1.14°，接近人类扫视精度。
- **实现机制**：通过建立相机姿态与电机位置的直接关系，简化控制流程，提升响应速度。

### 实验设置与性能验证
- 实验环境未明确指定，但通过对比人类扫视运动数据评估精度。
- 关键数字：机械自由度9、光学自由度4、扫视速度达人类峰值85%、左右相机误差分别为1.17°和1.14°。

### 结论
DIJIT 在仿人运动范围、速度及扫视精度上均达到较高水平，为主动视觉研究提供了硬件基础，尤其适用于眼-头协调机制与计算机视觉方法的对比分析。

## Overview
We present DIJIT, a novel binocular robotic head expressly designed for mobile agents that behave as active observers. DIJIT's unique breadth of functionality enables active vision research and the study of human-like eye and head-neck motions, their interrelationships, and how each contributes to visual ability. DIJIT is also being used to explore the differences between how human vision employs eye/head movements to solve visual tasks and current computer vision methods. DIJIT's design features nine mechanical degrees of freedom, while the cameras and lenses provide an additional four optical degrees of freedom. The ranges and speeds of the mechanical design are comparable to human performance. DIJIT attains 85\% of the peak human saccade speed. Our design includes the ranges of motion required for convergent stereo, namely, vergence, version, and cyclotorsion. Here, we present DIJIT and some aspects of its performance. We also present a novel method for saccadic camera movements, using a direct relationship between camera orientation and motor values. The resulting saccadic camera movements are close to human movements in terms of their accuracy, with 1.17$^\circ$ and 1.14$^\circ$ mean error for the left and right cameras, respectively.

## 参考
- http://arxiv.org/abs/2512.07998v2

## 개요
DIJIT은 능동 시각 연구를 위한 인간형 양안 로봇 헤드 하드웨어로, 인간의 눈-머리 협응 운동과 시력에 대한 기여를 모방하는 것을 목표로 합니다. 이 설계는 9개의 기계적 자유도와 4개의 광학적 자유도를 포함하며, 운동 범위와 속도는 인간 수준에 근접하고, 특히 단속 운동 속도는 인간 최대치의 85%에 도달합니다. DIJIT은 양안 입체 시각에 필요한 수렴, 버전 및 회선 운동을 지원하며, 카메라 방향과 모터 값의 직접 매핑을 통해 단속 운동을 구현하는 새로운 방법을 도입하여 정밀도가 인간에 근접하며, 좌우 카메라 평균 오차는 각각 1.17° 및 1.14°입니다.

## 핵심 내용
### 설계 목표 및 기능
DIJIT은 이동 에이전트를 위해 설계되어 능동적 관찰자로서 시각 연구를 수행할 수 있게 합니다. 핵심 목표는 다음과 같습니다:
- 능동 시각 연구를 지원하여 인간의 눈-머리 운동 패턴과 상호 관계를 탐구합니다.
- 인간이 눈/머리 운동을 통해 시각 작업을 해결하는 방식과 현재 컴퓨터 비전 방법의 차이를 비교합니다.

### 기계 및 광학 아키텍처
- **기계적 자유도**: 총 9개로, 목, 안구 등의 관절을 포함하며, 운동 범위와 속도는 인간 성능에 맞춰져 있습니다.
- **광학적 자유도**: 추가 4개로, 카메라와 렌즈 시스템에 의해 제공되어 시각 조절 능력을 강화합니다.
- **운동 능력**: 단속 운동 속도는 인간 최대치의 85%에 도달하며, 양안 입체 시각에 필요한 수렴, 버전 및 회선 운동을 지원합니다.

### 단속 운동 방법 혁신
카메라 방향과 모터 값의 직접 매핑에 기반한 단속 운동 제어 방법을 제안하며, 복잡한 중간 계산이 필요 없습니다:
- **정밀도 성능**: 왼쪽 카메라 평균 오차 1.17°, 오른쪽 카메라 평균 오차 1.14°로 인간의 단속 운동 정밀도에 근접합니다.
- **구현 메커니즘**: 카메라 자세와 모터 위치의 직접 관계를 설정하여 제어 흐름을 단순화하고 응답 속도를 향상시킵니다.

### 실험 설정 및 성능 검증
- 실험 환경은 명시되지 않았지만, 인간의 단속 운동 데이터와 비교하여 정밀도를 평가합니다.
- 주요 수치: 기계적 자유도 9, 광학적 자유도 4, 단속 운동 속도는 인간 최대치의 85%, 좌우 카메라 오차는 각각 1.17° 및 1.14°입니다.

### 결론
DIJIT은 인간형 운동 범위, 속도 및 단속 운동 정밀도에서 높은 수준을 달성하여 능동 시각 연구를 위한 하드웨어 기반을 제공하며, 특히 눈-머리 협응 메커니즘과 컴퓨터 비전 방법의 비교 분석에 적합합니다.
