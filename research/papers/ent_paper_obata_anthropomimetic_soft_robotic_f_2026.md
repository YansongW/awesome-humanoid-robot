---
$id: ent_paper_obata_anthropomimetic_soft_robotic_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness
    Modulability
  zh: Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness
    Modulability
  ko: Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness
    Modulability
summary:
  en: 'The human wrist exhibits adaptive stiffness modulability: joint stiffness anisotropy can be actively regulated through
    muscle co-contraction. This functionality is essential for stable manipulation, yet the underlying morphological factors
    remain unclear. To identify these factors, we developed an anatomically accurate anthropomimetic soft robotic forearm
    comprising eight independently movable ...'
  zh: 该研究由 Yoshinobu Obata、Yinlai Jiang、Hiroshi Yokoi 与 Shunta Togo 完成，构建了一个解剖学精确的拟人软体机器人前臂，包含八块独立可动的腕骨、韧带连接、22 条驱动肌肉以及柔性指尖。通过对比正常腕骨、近排腕骨融合与几何椭球骨架三种配置下的腕关节刚度，研究发现腕骨形态是实现类人自适应刚度调节的主导因素，为仿人机器人手腕设计提供了原则。
  ko: 'The human wrist exhibits adaptive stiffness modulability: joint stiffness anisotropy can be actively regulated through
    muscle co-contraction. This functionality is essential for stable manipulation, yet the underlying morphological factors
    remain unclear. To identify these factors, we developed an anatomically accurate anthropomimetic soft robotic forearm
    comprising eight independently movable ...'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- soft_robotics
- wrist_stiffness
- carpal_bones
- anthropomimetic_design
- humanoid_robot_wrist
- stiffness_modulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.29176);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.29176 Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like
    Adaptive Stiffness Modulability
  url: https://arxiv.org/abs/2609.29176
  date: '2026-09-24'
  accessed_at: '2026-09-28'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/TogoLab/anthropomimetic-forearm-carpal-stiffness
  accessed_at: '2026-09-28'
---

## 概述

人类手腕具备自适应刚度调节能力，其关节刚度各向异性可通过肌肉共收缩主动调控，但背后的形态学因素尚不明确。为识别这些因素，作者开发了一个解剖学精确的拟人软体机器人前臂，由八块独立可动的腕骨经韧带互连，配备 22 条驱动肌肉与柔性指尖。研究在三种骨骼配置（解剖学正常腕骨、近排腕骨融合、几何椭球骨架）下，测量了四种肌肉激活模式对应的腕关节刚度。结果显示，正常配置下刚度椭圆在手指肌肉激活时沿掷镖运动（DTM）方向呈现低刚度，而腕部与手指肌肉同时激活时该方向转为高刚度，与已报道的人体测量结果一致。近排腕骨融合消除了手指肌肉激活时的低 DTM 方向刚度，几何椭球骨架则在所有条件下均表现出较差的刚度椭圆重定向能力。

## 核心内容

### 问题背景
人类手腕的关节刚度具有各向异性，并可通过肌肉共收缩主动调节，这种自适应刚度调节能力对稳定操作至关重要。然而，哪些形态学因素决定了这一功能此前并不清楚。

### 方法
- 构建解剖学精确的拟人软体机器人前臂，包含八块独立可动的腕骨，由韧带相互连接，配备 22 条驱动肌肉与柔性指尖。
- 在三种骨骼配置下测量腕关节刚度：解剖学正常腕骨、近排腕骨融合、几何椭球骨架。
- 每种配置下测试四种肌肉激活模式。

### 关键结果
- 正常配置中，手指肌肉激活时刚度椭圆沿掷镖运动（DTM）方向呈现低刚度；腕部与手指肌肉同时激活时，同一方向转为高刚度。该结果与已报道的人体测量一致，表明精确的解剖学复现可重现类人的刚度调节能力。
- 近排腕骨融合后，手指肌肉激活下的低 DTM 方向刚度消失。
- 几何椭球骨架在所有条件下均表现出较差的刚度椭圆重定向能力。
- 腕骨运动分析显示，在近排腕骨处，腕部肌肉与手指肌肉之间存在显著的对向耦合模式，腕中关节处也呈现一致但未达显著水平的趋势，为上述刚度调节提供了力学解释。

### 结论
腕骨形态在人类手腕刚度调节中起主导作用，相关发现可为仿人机器人手腕的设计提供原则。

## Overview

The human wrist exhibits adaptive stiffness modulability: joint stiffness anisotropy can be actively regulated through muscle co-contraction. This functionality is essential for stable manipulation, yet the underlying morphological factors remain unclear. To identify these factors, we developed an anatomically accurate anthropomimetic soft robotic forearm comprising eight independently movable carpal bones interconnected by ligaments, 22 actuated muscles, and compliant fingertips. We measured wrist joint stiffness under four muscle activation patterns across three skeletal configurations: anatomically normal carpal bones, a fused proximal carpal row, and a geometric ellipsoidal skeleton. The stiffness ellipse exhibited low stiffness along the dart-throwing motion (DTM) direction when finger muscles were activated, but high stiffness along the same direction when wrist and finger muscles were activated simultaneously. These results agree with previously reported human measurements, demonstrating that precise anatomical replication reproduces human-like stiffness modulability. Fusing the proximal carpal row eliminated the low DTM-direction stiffness under finger muscle activation, while the geometric ellipsoidal skeleton showed poor stiffness ellipse reorientation across all conditions. Carpal bone motion analysis revealed significantly opposing coupling patterns between wrist and finger muscles at the proximal carpal row, accompanied by a consistent but non-significant trend at the midcarpal joint, providing a mechanical explanation for this modulation. These findings demonstrate that carpal bone morphology plays a dominant role in human wrist stiffness modulation and provide design principles for humanoid robot wrists.

## 参考
- https://arxiv.org/abs/2609.29176
- https://github.com/TogoLab/anthropomimetic-forearm-carpal-stiffness
