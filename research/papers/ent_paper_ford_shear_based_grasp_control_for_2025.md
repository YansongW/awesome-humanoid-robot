---
$id: ent_paper_ford_shear_based_grasp_control_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shear-based Grasp Control for Multi-fingered Underactuated Tactile Robotic Hands
  zh: 基于剪切力的多指欠驱动触觉机器人手抓取控制
  ko: 다지점 저작동 촉각 로봇 손을 위한 전단력 기반 파지 제어
summary:
  en: Proposes a shear-based grasp controller for the Pisa/IIT SoftHand using five fingertip microTac optical tactile sensors;
    contact pose and shear/normal force are predicted via supervised deep learning with transfer learning, enabling real-time
    multi-finger grasp adjustments during delicate-object manipulation.
  zh: 本文提出一种基于剪切力的抓取控制器，用于Pisa/IIT SoftHand多指欠驱动灵巧手。该控制器利用五个指尖microTac光学触觉传感器，通过监督深度学习与迁移学习预测接触位姿及剪切/法向力，实现对易碎物体操作过程中的实时多指抓取调整。
  ko: Pisa/IIT SoftHand의 다섯 손끝에 장착된 microTac 광학 촉각 센서를 이용한 전단력 기반 파지 제어기를 제안하며, 지도 학습과 전이 학습으로 접촉 자세 및 전단/법선력을 예측하여 섬세한 물체
    조작 중 실시간 다지점 파지 조정을 가능하게 한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- tactile_sensing
- grasp_control
- underactuated_hand
- soft_robotics
- optical_tactile_sensor
- shear_force
- deep_learning
- transfer_learning
- multi_fingered_hand
- pisa_iit_softhand
- microtac
- dexterous_manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.17501v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (630 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Shear-based Grasp Control for Multi-fingered Underactuated Tactile Robotic Hands
  url: https://arxiv.org/abs/2503.17501
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该研究为Pisa/IIT SoftHand设计了基于剪切力的抓取控制方案，在全部五个指尖安装微型仿生触觉传感器microTac。这些传感器可提取精确的接触几何与力信息，通过并行处理流水线异步采集触觉图像并预测接触位姿与力。研究采用监督深度学习结合迁移学习技术，在所有传感器上建立一致的位姿与力预测模型。最终开发的抓取控制框架能同时利用所有指尖传感器的接触力反馈，使手部在外部扰动下安全处理易碎物体。

## 核心内容
### 方法架构
- 采用Pisa/IIT SoftHand欠驱动仿人灵巧手，配备五个指尖microTac光学触觉传感器（TacTip微型版本）
- 构建并行处理流水线：异步采集多传感器触觉图像，同步预测接触位姿与剪切/法向力
- 通过监督深度学习+迁移学习实现跨传感器模型一致性，减少数据标注成本

### 实验设置
- 实验1：柔性杯抓取保持——在物体重量变化时避免压碎
- 实验2：倾倒任务——杯子质心动态变化场景下的抓取调整
- 实验3：触觉引导的主从任务——人类引导被持物体运动

### 关键结果
- 控制器能实时响应外部扰动，在重量变化时自动调节抓取力
- 倾倒任务中成功应对动态质心偏移，保持稳定抓取
- 主从任务展示出类似人类的灵巧操作能力，通过触觉反射控制实现欠驱动手的快速响应

### 结论
该剪切力控制方案使欠驱动灵巧手具备类似人类的操作灵巧性，通过触觉传感的快速反射控制，在易碎物体操作中展现出鲁棒性。

## Overview
This paper presents a shear-based control scheme for grasping and manipulating delicate objects with a Pisa/IIT anthropomorphic SoftHand equipped with soft biomimetic tactile sensors on all five fingertips. These `microTac' tactile sensors are miniature versions of the TacTip vision-based tactile sensor, and can extract precise contact geometry and force information at each fingertip for use as feedback into a controller to modulate the grasp while a held object is manipulated. Using a parallel processing pipeline, we asynchronously capture tactile images and predict contact pose and force from multiple tactile sensors. Consistent pose and force models across all sensors are developed using supervised deep learning with transfer learning techniques. We then develop a grasp control framework that uses contact force feedback from all fingertip sensors simultaneously, allowing the hand to safely handle delicate objects even under external disturbances. This control framework is applied to several grasp-manipulation experiments: first, retaining a flexible cup in a grasp without crushing it under changes in object weight; second, a pouring task where the center of mass of the cup changes dynamically; and third, a tactile-driven leader-follower task where a human guides a held object. These manipulation tasks demonstrate more human-like dexterity with underactuated robotic hands by using fast reflexive control from tactile sensing.

## 参考
- http://arxiv.org/abs/2503.17501v1

## 개요
이 연구는 Pisa/IIT SoftHand를 위해 전단력 기반 파지 제어 방식을 설계했으며, 다섯 손가락 끝 모두에 소형 생체모방 촉각 센서 microTac을 장착했다. 이 센서들은 정밀한 접촉 형상과 힘 정보를 추출하며, 병렬 처리 파이프라인을 통해 촉각 이미지를 비동기적으로 수집하고 접촉 자세와 힘을 예측한다. 연구는 지도 딥러닝과 전이 학습 기술을 결합하여 모든 센서에서 일관된 자세 및 힘 예측 모델을 구축했다. 최종적으로 개발된 파지 제어 프레임워크는 모든 손가락 끝 센서의 접촉 힘 피드백을 동시에 활용하여, 외부 교란 하에서도 손이 취약한 물체를 안전하게 다룰 수 있게 한다.

## 핵심 내용
### 방법 아키텍처
- Pisa/IIT SoftHand의 부족구동 인간형 다섯 손가락 손을 채택하고, 다섯 손가락 끝에 microTac 광학 촉각 센서(TacTip 소형 버전)를 장착
- 병렬 처리 파이프라인 구축: 다중 센서 촉각 이미지를 비동기적으로 수집하고, 접촉 자세와 전단/수직 힘을 동기적으로 예측
- 지도 딥러닝 + 전이 학습을 통해 센서 간 모델 일관성을 확보하고 데이터 라벨링 비용 절감

### 실험 설정
- 실험 1: 유연한 컵 파지 유지 — 물체 무게 변화 시 압착을 방지
- 실험 2: 따르기 작업 — 컵의 질량 중심이 동적으로 변화하는 상황에서의 파지 조정
- 실험 3: 촉각 유도 마스터-슬레이브 작업 — 인간이 잡힌 물체의 움직임을 유도

### 주요 결과
- 컨트롤러가 외부 교란에 실시간으로 반응하며, 무게 변화 시 파지력을 자동으로 조절
- 따르기 작업에서 동적 질량 중심 이동에 성공적으로 대응하며 안정적인 파지를 유지
- 마스터-슬레이브 작업에서 인간과 유사한 손재주 조작 능력을 보여주며, 촉각 반사 제어를 통해 부족구동 손의 빠른 응답을 구현

### 결론
이 전단력 제어 방식은 부족구동 손에 인간과 유사한 조작 손재주를 부여하며, 촉각 센싱의 빠른 반사 제어를 통해 취약한 물체 조작에서 견고성을 입증한다.
