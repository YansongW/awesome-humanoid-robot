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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07998v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
우리는 능동적 관찰자로 행동하는 모바일 에이전트를 위해 특별히 설계된 새로운 양안 로봇 헤드 DIJIT를 소개합니다. DIJIT의 독특한 기능 폭은 능동 시각 연구와 인간과 유사한 눈 및 머리-목 움직임, 이들의 상호 관계, 그리고 각각이 시각 능력에 기여하는 방식을 연구할 수 있게 합니다. DIJIT는 또한 인간 시각이 시각적 작업을 해결하기 위해 눈/머리 움직임을 사용하는 방식과 현재 컴퓨터 비전 방법 간의 차이를 탐구하는 데 사용되고 있습니다. DIJIT의 설계는 9개의 기계적 자유도를 특징으로 하며, 카메라와 렌즈는 추가로 4개의 광학적 자유도를 제공합니다. 기계적 설계의 범위와 속도는 인간의 성능과 유사합니다. DIJIT는 인간 최대 단속 운동 속도의 85%에 도달합니다. 우리의 설계는 수렴 스테레오에 필요한 움직임 범위, 즉 버전스, 버전, 사이클로토션을 포함합니다. 여기서 우리는 DIJIT와 그 성능의 일부 측면을 제시합니다. 또한 카메라 방향과 모터 값 간의 직접적인 관계를 사용하는 단속적 카메라 움직임을 위한 새로운 방법을 제시합니다. 결과적인 단속적 카메라 움직임은 정확도 측면에서 인간의 움직임에 가까우며, 왼쪽 및 오른쪽 카메라에 대해 각각 1.17$^\circ$ 및 1.14$^\circ$의 평균 오차를 보입니다.

## 핵심 내용
우리는 능동적 관찰자로 행동하는 모바일 에이전트를 위해 특별히 설계된 새로운 양안 로봇 헤드 DIJIT를 소개합니다. DIJIT의 독특한 기능 폭은 능동 시각 연구와 인간과 유사한 눈 및 머리-목 움직임, 이들의 상호 관계, 그리고 각각이 시각 능력에 기여하는 방식을 연구할 수 있게 합니다. DIJIT는 또한 인간 시각이 시각적 작업을 해결하기 위해 눈/머리 움직임을 사용하는 방식과 현재 컴퓨터 비전 방법 간의 차이를 탐구하는 데 사용되고 있습니다. DIJIT의 설계는 9개의 기계적 자유도를 특징으로 하며, 카메라와 렌즈는 추가로 4개의 광학적 자유도를 제공합니다. 기계적 설계의 범위와 속도는 인간의 성능과 유사합니다. DIJIT는 인간 최대 단속 운동 속도의 85%에 도달합니다. 우리의 설계는 수렴 스테레오에 필요한 움직임 범위, 즉 버전스, 버전, 사이클로토션을 포함합니다. 여기서 우리는 DIJIT와 그 성능의 일부 측면을 제시합니다. 또한 카메라 방향과 모터 값 간의 직접적인 관계를 사용하는 단속적 카메라 움직임을 위한 새로운 방법을 제시합니다. 결과적인 단속적 카메라 움직임은 정확도 측면에서 인간의 움직임에 가까우며, 왼쪽 및 오른쪽 카메라에 대해 각각 1.17$^\circ$ 및 1.14$^\circ$의 평균 오차를 보입니다.

## 参考
- http://arxiv.org/abs/2512.07998v2
