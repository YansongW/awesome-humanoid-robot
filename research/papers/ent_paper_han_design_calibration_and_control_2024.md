---
$id: ent_paper_han_design_calibration_and_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design, Calibration, and Control of Compliant Force-sensing Gripping Pads for Humanoid Robots
  zh: 面向人形机器人的柔顺力传感夹持垫设计、标定与控制
  ko: 휴머노이드 로봇을 위한 순응형 힘 감지 그리핑 패드의 설계, 보정 및 제어
summary:
  en: This 2024 paper presents low-cost, lightweight compliant gripping pads that measure normal gripping force and center
    of pressure, together with a calibration procedure and a hybrid force-alignment-position controller using limit-surface
    theory for slippage avoidance, demonstrated on a NAO humanoid robot manipulating box-like objects.
  zh: 本文提出了一种低成本、轻量化的柔性力传感夹持垫，用于人形机器人操作箱状物体。该夹持垫可测量法向夹持力和压力中心，并开发了校准方法提升测量精度。研究结合极限曲面理论设计了混合力-对齐-位置控制器，在NAO人形机器人上验证了防滑效果。
  ko: 이 2024년 논문은 저렴하고 가벼운 순응형 힘 감지 그리핑 패드를 제안하며, 법선 방향 그리핑 힘과 압력 중심을 측정하고 비선형 보정 절차와 극한 표면 이론을 활용한 미끄러짐 방지 하이브리드 힘-정렬-위치
    제어기를 개발하여 NAO 휴머노이드 로봇의 상자형 물체 조작에서 입증하였다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- force_sensing
- gripping_pad
- end_effector
- nao
- dual_arm_manipulation
- compliant_mechanism
- load_cell
- center_of_pressure
- limit_surface
- slippage_avoidance
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.20969v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Design, Calibration, and Control of Compliant Force-sensing Gripping Pads for Humanoid Robots
  url: https://arxiv.org/abs/2405.20969
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该2024年论文针对小型人形机器人操作箱状物体的需求，设计了一对低成本、轻量化的柔性力传感夹持垫。夹持垫能够实时测量法向夹持力与压力中心，并通过专用校准方法提高压力中心测量精度。研究提出混合力-对齐-位置控制框架，用于调节夹持力并确保夹持器与物体表面贴合。基于极限曲面理论的接触摩擦模型可确定防滑所需的最小夹持力。整套软硬件系统在NAO人形机器人上完成实验验证。

## 核心内容
### 硬件设计
- 采用低成本、轻量化柔性材料制作夹持垫，适配小型人形机器人（如NAO）的夹持器
- 集成力传感单元，可同时测量法向夹持力与压力中心（CoP）

### 校准方法
- 开发专用校准流程以提升CoP测量精度，补偿传感器非线性与安装误差

### 控制框架
- 提出混合力-对齐-位置控制策略：
  - 力控制：调节夹持力至目标值
  - 对齐控制：确保夹持器与物体表面平行接触
  - 位置控制：维持夹持器相对位置
- 引入极限曲面理论（Limit Surface Theory）建模接触摩擦，动态计算防滑所需的最小夹持力

### 实验验证
- 在NAO人形机器人上操作箱状物体，验证系统有效性
- 实验结果表明：夹持力控制稳定，表面对齐精度满足操作需求，成功避免物体滑落

## Overview
This paper introduces a pair of low-cost, light-weight and compliant force-sensing gripping pads used for manipulating box-like objects with smaller-sized humanoid robots. These pads measure normal gripping forces and center of pressure (CoP). A calibration method is developed to improve the CoP measurement accuracy. A hybrid force-alignment-position control framework is proposed to regulate the gripping forces and to ensure the surface alignment between the grippers and the object. Limit surface theory is incorporated as a contact friction modeling approach to determine the magnitude of gripping forces for slippage avoidance. The integrated hardware and software system is demonstrated with a NAO humanoid robot. Experiments show the effectiveness of the overall approach.

## 개요
본 논문은 소형 휴머노이드 로봇을 이용해 상자 형태의 물체를 조작하기 위한 저비용, 경량 및 유연한 힘 감지 그리핑 패드 한 쌍을 소개합니다. 이 패드는 수직 그리핑 힘과 압력 중심(CoP)을 측정합니다. CoP 측정 정확도를 향상시키기 위한 캘리브레이션 방법이 개발되었습니다. 그리핑 힘을 조절하고 그리퍼와 물체 간의 표면 정렬을 보장하기 위해 하이브리드 힘-정렬-위치 제어 프레임워크가 제안됩니다. 미끄러짐 방지를 위한 그리핑 힘의 크기를 결정하기 위해 접촉 마찰 모델링 접근법으로 한계 표면 이론이 통합되었습니다. 통합된 하드웨어 및 소프트웨어 시스템은 NAO 휴머노이드 로봇으로 시연됩니다. 실험을 통해 전체 접근법의 효과가 입증되었습니다.

## 핵심 내용
본 논문은 소형 휴머노이드 로봇을 이용해 상자 형태의 물체를 조작하기 위한 저비용, 경량 및 유연한 힘 감지 그리핑 패드 한 쌍을 소개합니다. 이 패드는 수직 그리핑 힘과 압력 중심(CoP)을 측정합니다. CoP 측정 정확도를 향상시키기 위한 캘리브레이션 방법이 개발되었습니다. 그리핑 힘을 조절하고 그리퍼와 물체 간의 표면 정렬을 보장하기 위해 하이브리드 힘-정렬-위치 제어 프레임워크가 제안됩니다. 미끄러짐 방지를 위한 그리핑 힘의 크기를 결정하기 위해 접촉 마찰 모델링 접근법으로 한계 표면 이론이 통합되었습니다. 통합된 하드웨어 및 소프트웨어 시스템은 NAO 휴머노이드 로봇으로 시연됩니다. 실험을 통해 전체 접근법의 효과가 입증되었습니다.

## 参考
- http://arxiv.org/abs/2405.20969v1
