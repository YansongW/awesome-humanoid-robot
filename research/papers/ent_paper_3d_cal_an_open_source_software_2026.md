---
$id: ent_paper_3d_cal_an_open_source_software_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Cal: An Open-Source Software Library for Depth Reconstruction on Vision-Based Tactile Sensors'
  zh: '3D Cal: An Open-Source Software Library for Depth Reconstruction on Vision-Based Tactile Sensors'
  ko: '3D Cal: An Open-Source Software Library for Depth Reconstruction on Vision-Based Tactile Sensors'
summary:
  en: 'arXiv:2511.03078v3 Announce Type: replace Abstract: Tactile sensing plays a key role in enabling dexterous and reliable
    robotic manipulation, but realizing this capability requires substantial calibration to convert raw sensor readings into
    physically meaningful quantities. Despite its near-universal necessity, the calibration process remains ad hoc and labor-intensive.
    Here, we introduce 3D Cal, an open-source library that transforms a low-cost 3D printer into an automated probing device
    capable of generating large volumes of labeled training data for calibrating vision-based tactile sensors. 3D Cal also
    provides an end-to-end, user-friendly pipeline for training custom convolutional networks to produce high-quality depth
    reconstructions. Using 3D Cal, we systematically explore the relationship between training data volume and spatial reconstruction
    performance on two commercially available sensors, DIGIT and GelSight Mini, and derive practical, empirically-grounded
    guidelines for calibrating these sensors. Finally, we demonstrate depth reconstruction performance on the DIGIT and GelSight
    Mini comparable to state-of-the-art methods, achieving average reconstruction errors of 156 $\mathrm{\mu m}$ and 205 $\mathrm{\mu
    m}$ on unseen objects, respectively. By automating tactile sensor calibration, 3D Cal can accelerate tactile sensing research,
    simplify sensor deployment, and facilitate the integration of tactile sensing in robotic platforms.'
  zh: 3D Cal 是一个开源软件库，能将低成本 3D 打印机改造为自动探测设备，为基于视觉的触觉传感器生成大量带标签的训练数据。该库提供了端到端的用户友好流程，用于训练自定义卷积网络以生成高质量深度重建。在 DIGIT 和 GelSight
    Mini 两款商用传感器上，3D Cal 实现了与最先进方法相当的深度重建性能，平均重建误差分别为 156 μm 和 205 μm。
  ko: 'arXiv:2511.03078v3 Announce Type: replace Abstract: Tactile sensing plays a key role in enabling dexterous and reliable
    robotic manipulation, but realizing this capability requires substantial calibration to convert raw sensor readings into
    physically meaningful quantities. Despite its near-universal necessity, the calibration process remains ad hoc and labor-intensive.
    Here, we introduce 3D Cal, an open-source library that transforms a low-cost 3D printer into an automated probing device
    capable of generating large volumes of labeled training data for calibrating vision-based tactile sensors. 3D Cal also
    provides an end-to-end, user-friendly pipeline for training custom convolutional networks to produce high-quality depth
    reconstructions. Using 3D Cal, we systematically explore the relationship between training data volume and spatial reconstruction
    performance on two commercially available sensors, DIGIT and GelSight Mini, and derive practical, empirically-grounded
    guidelines for calibrating these sensors. Finally, we demonstrate depth reconstruction performance on the DIGIT and GelSight
    Mini comparable to state-of-the-art methods, achieving average reconstruction errors of 156 $\mathrm{\mu m}$ and 205 $\mathrm{\mu
    m}$ on unseen objects, respectively. By automating tactile sensor calibration, 3D Cal can accelerate tactile sensing research,
    simplify sensor deployment, and facilitate the integration of tactile sensing in robotic platforms.'
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
- robotics
- 3d_cal
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.03078v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (762 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: '3D Cal: An Open-Source Software Library for Depth Reconstruction on Vision-Based Tactile Sensors (arXiv)'
  url: https://arxiv.org/abs/2511.03078
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
触觉传感对于实现灵巧可靠的机器人操作至关重要，但校准过程通常耗时且缺乏标准化。3D Cal 通过将低成本 3D 打印机转化为自动化探测设备，解决了这一瓶颈，能够大规模生成带标签的训练数据。该库还提供了完整的训练流程，支持用户训练自定义卷积网络进行深度重建。研究者在 DIGIT 和 GelSight Mini 两款传感器上系统探索了训练数据量与空间重建性能的关系，并推导出实用的校准指南。最终，3D Cal 在未见物体上达到了与最先进方法相当的深度重建精度。

## 核心内容
### 方法概述
3D Cal 的核心创新在于利用低成本 3D 打印机作为自动化探测平台，通过精确控制探针与传感器表面的接触，生成大量带真实深度标签的训练数据。该库提供了完整的端到端流程，包括数据采集、预处理、网络训练和深度重建。

### 实验设置
- **传感器**：使用两款商用视觉触觉传感器 DIGIT 和 GelSight Mini。
- **训练数据**：系统探索了不同训练数据量对重建性能的影响。
- **评估指标**：以平均重建误差（μm）衡量深度重建精度。

### 关键结果
- **DIGIT 传感器**：在未见物体上达到平均重建误差 156 μm。
- **GelSight Mini 传感器**：在未见物体上达到平均重建误差 205 μm。
- **性能对比**：与最先进方法相比，3D Cal 实现了可比的深度重建性能。
- **实用指南**：基于实验数据推导出训练数据量与重建性能之间的经验关系，为传感器校准提供了实用指导。

### 结论
3D Cal 通过自动化触觉传感器校准流程，显著降低了校准的复杂性和人力成本。该库不仅加速了触觉传感研究，还简化了传感器部署，促进了触觉传感在机器人平台上的集成。

## Overview
Tactile sensing plays a key role in enabling dexterous and reliable robotic manipulation, but realizing this capability requires substantial calibration to convert raw sensor readings into physically meaningful quantities. Despite its near-universal necessity, the calibration process remains ad hoc and labor-intensive. Here, we introduce 3D Cal, an open-source library that transforms a low-cost 3D printer into an automated probing device capable of generating large volumes of labeled training data for calibrating vision-based tactile sensors. 3D Cal also provides an end-to-end, user-friendly pipeline for training custom convolutional networks to produce high-quality depth reconstructions. Using 3D Cal, we systematically explore the relationship between training data volume and spatial reconstruction performance on two commercially available sensors, DIGIT and GelSight Mini, and derive practical, empirically-grounded guidelines for calibrating these sensors. Finally, we demonstrate depth reconstruction performance on the DIGIT and GelSight Mini comparable to state-of-the-art methods, achieving average reconstruction errors of 156 $\mathrm{μm}$ and 205 $\mathrm{μm}$ on unseen objects, respectively. By automating tactile sensor calibration, 3D Cal can accelerate tactile sensing research, simplify sensor deployment, and facilitate the integration of tactile sensing in robotic platforms.

## 参考
- http://arxiv.org/abs/2511.03078v3

## 개요
촉각 센싱은 정교하고 신뢰할 수 있는 로봇 조작을 구현하는 데 필수적이지만, 캘리브레이션 과정은 일반적으로 시간이 많이 소요되고 표준화가 부족합니다. 3D Cal은 저비용 3D 프린터를 자동화된 프로빙 장치로 변환하여 이러한 병목 현상을 해결하며, 대규모로 라벨이 지정된 훈련 데이터를 생성할 수 있습니다. 이 라이브러리는 또한 완전한 훈련 파이프라인을 제공하여 사용자가 깊이 재구성을 위한 맞춤형 컨볼루션 네트워크를 훈련할 수 있도록 지원합니다. 연구자들은 DIGIT 및 GelSight Mini 두 센서에서 훈련 데이터 양과 공간 재구성 성능 간의 관계를 체계적으로 탐구하고 실용적인 캘리브레이션 가이드를 도출했습니다. 최종적으로 3D Cal은 보지 못한 객체에서 최첨단 방법과 필적하는 깊이 재구성 정확도를 달성했습니다.

## 핵심 내용
### 방법 개요
3D Cal의 핵심 혁신은 저비용 3D 프린터를 자동화된 프로빙 플랫폼으로 활용하여 프로브와 센서 표면 간의 접촉을 정밀하게 제어함으로써 실제 깊이 라벨이 포함된 대규모 훈련 데이터를 생성하는 데 있습니다. 이 라이브러리는 데이터 수집, 전처리, 네트워크 훈련 및 깊이 재구성을 포함한 완전한 엔드투엔드 파이프라인을 제공합니다.

### 실험 설정
- **센서**: 두 가지 상용 비전 기반 촉각 센서인 DIGIT 및 GelSight Mini를 사용했습니다.
- **훈련 데이터**: 다양한 훈련 데이터 양이 재구성 성능에 미치는 영향을 체계적으로 탐구했습니다.
- **평가 지표**: 평균 재구성 오차(μm)로 깊이 재구성 정확도를 측정했습니다.

### 주요 결과
- **DIGIT 센서**: 보지 못한 객체에서 평균 재구성 오차 156 μm를 달성했습니다.
- **GelSight Mini 센서**: 보지 못한 객체에서 평균 재구성 오차 205 μm를 달성했습니다.
- **성능 비교**: 최첨단 방법과 비교하여 3D Cal은 필적하는 깊이 재구성 성능을 구현했습니다.
- **실용 가이드**: 실험 데이터를 기반으로 훈련 데이터 양과 재구성 성능 간의 경험적 관계를 도출하여 센서 캘리브레이션에 실용적인 지침을 제공했습니다.

### 결론
3D Cal은 촉각 센서 캘리브레이션 프로세스를 자동화하여 캘리브레이션의 복잡성과 인적 비용을 크게 줄였습니다. 이 라이브러리는 촉각 센싱 연구를 가속화할 뿐만 아니라 센서 배포를 간소화하여 로봇 플랫폼에서 촉각 센싱의 통합을 촉진합니다.
