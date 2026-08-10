---
$id: ent_paper_correll_materials_that_make_robots_sma_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Materials that make robots smart
  zh: 使机器人智能化的材料
  ko: 로봇을 스마트하게 만드는 재료
summary:
  en: This paper argues that embodied artificial intelligence is also a materials problem, defines "robotic materials" as
    composites that tightly integrate structure, sensing, actuation, computation, and communication, surveys existing prototypes,
    and identifies interdisciplinary challenges in manufacturing, networking, materials science, and control.
  zh: 本文提出具身人工智能不仅是计算问题，更是材料问题。作者定义了“机器人材料”为紧密集成结构、传感、驱动、计算与通信的复合材料，并调查了现有原型。核心贡献在于识别了制造、网络、材料科学与控制领域的跨学科挑战。
  ko: 본 논문은 구체화된 인공지능 역시 재료 문제이며, 구조, 센싱, 구동, 계산, 통신을 긴밀히 통합한 복합 재료인 “로봇 재료”를 정의하고, 기존 프로토타입을 조사하며 제조, 네트워킹, 재료 과학 및 제어 분야의
    학제간 과제를 제시한다.
domains:
- 02_components
- 01_raw_materials
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- robotic_materials
- smart_materials
- tactile_sensing_skin
- morphological_computation
- humanoid_skin
- multi_material_manufacturing
- wireless_sensor_networks
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1711.00537v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (554 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Materials that make robots smart
  url: https://arxiv.org/abs/1711.00537
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- principle
- method
---
## 概述
论文主张具身人工智能需要从材料层面重新思考，强调材料与结构特性在控制回路中的主动作用。通过将传感器、驱动器、计算和通信深度整合，机器人材料能抽象化功能，使智能机器人构建更直接、更鲁棒。文章综述了从操作任务到自动驾驶等应用中的现有原型，并指出机器人社区需与无线传感器网络研究者、聚合物科学家等合作解决的关键挑战。

## 核心内容
### 核心论点
- 具身智能不仅是计算问题，更是材料问题：材料可通过紧密集成传感、驱动、计算与通信在控制中发挥主动作用。
- 功能抽象化：机器人材料应使构建更简单、更鲁棒，例如：
  - 骨骼：测量负载
  - 肌肉：驱动运动
  - 皮肤：提供触觉信息（压力、纹理、损伤位置）
  - 眼睛：提取高层信息
  - 大脑材料：可扩展计算

### 现有原型与应用
- 综述了“机器人材料”领域的最新技术水平
- 潜在应用：从机械臂操作到自动驾驶

### 开放挑战
- 制造工艺：如何实现异构组件的集成
- 网络通信：无线传感器网络与材料内通信的协同
- 材料科学：聚合物等新型材料的开发
- 控制理论：材料主动参与下的控制算法设计

### 合作需求
- 机器人社区需与以下领域专家协作：
  - 无线传感器网络研究者
  - 聚合物科学家
  - 其他相关学科

## Overview
We posit that embodied artificial intelligence is not only a computational, but also a materials problem. While the importance of material and structural properties in the control loop are well understood, materials can take an active role during control by tight integration of sensors, actuators, computation and communication. We envision such materials to abstract functionality, therefore making the construction of intelligent robots more straightforward and robust. For example, robots could be made of bones that measure load, muscles that move, skin that provides the robot with information about the kind and location of tactile sensations ranging from pressure, to texture and damage, eyes that extract high-level information, and brain material that provides computation in a scalable manner. Such materials will not resemble any existing engineered materials, but rather the heterogeneous components out of which their natural counterparts are made. We describe the state-of-the-art in so-called "robotic materials", their opportunities for revolutionizing applications ranging from manipulation to autonomous driving, and open challenges the robotics community needs to address in collaboration with allies, such as wireless sensor network researchers and polymer scientists.

## 参考
- http://arxiv.org/abs/1711.00537v2

## 개요
이 논문은 구현 지능(Embodied AI)이 재료 수준에서의 재고가 필요하다고 주장하며, 재료와 구조적 특성이 제어 루프에서 능동적인 역할을 수행해야 한다고 강조한다. 센서, 액추에이터, 계산 및 통신을 깊이 통합함으로써 로봇 재료는 기능을 추상화할 수 있으며, 지능형 로봇 구축을 더 직접적이고 견고하게 만든다. 이 글은 조작 작업부터 자율주행까지의 응용 분야에서 기존 프로토타입을 검토하고, 로봇 공학 커뮤니티가 무선 센서 네트워크 연구자, 폴리머 과학자 등과 협력하여 해결해야 할 핵심 과제를 지적한다.

## 핵심 내용
### 핵심 논점
- 구현 지능은 단순한 계산 문제가 아니라 재료 문제이다: 재료는 센싱, 구동, 계산 및 통신을 긴밀하게 통합함으로써 제어에서 능동적인 역할을 할 수 있다.
- 기능 추상화: 로봇 재료는 구축을 더 단순하고 견고하게 만들어야 한다. 예를 들어:
  - 뼈: 하중 측정
  - 근육: 운동 구동
  - 피부: 촉각 정보 제공(압력, 질감, 손상 위치)
  - 눈: 고수준 정보 추출
  - 뇌 재료: 확장 가능한 계산

### 기존 프로토타입 및 응용
- "로봇 재료" 분야의 최신 기술 수준 검토
- 잠재적 응용: 기계 팔 조작부터 자율주행까지

### 공개 과제
- 제조 공정: 이종 구성 요소의 통합을 어떻게 구현할 것인가
- 네트워크 통신: 무선 센서 네트워크와 재료 내 통신의 협력
- 재료 과학: 폴리머 등 새로운 재료 개발
- 제어 이론: 재료가 능동적으로 참여하는 상황에서의 제어 알고리즘 설계

### 협력 필요성
- 로봇 공학 커뮤니티는 다음 분야의 전문가와 협력해야 한다:
  - 무선 센서 네트워크 연구자
  - 폴리머 과학자
  - 기타 관련 학문 분야
