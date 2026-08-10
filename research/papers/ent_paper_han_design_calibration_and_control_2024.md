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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.20969v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (542 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2405.20969v1

## Overview
This 2024 paper addresses the need for small humanoid robots to manipulate box-shaped objects by designing a pair of low-cost, lightweight flexible force-sensing gripper pads. The gripper pads can measure normal gripping force and center of pressure in real time, and a dedicated calibration method improves the accuracy of center of pressure measurement. The research proposes a hybrid force-alignment-position control framework to regulate gripping force and ensure the gripper aligns with the object surface. A contact friction model based on Limit Surface Theory determines the minimum gripping force required to prevent slipping. The complete hardware and software system was experimentally validated on the NAO humanoid robot.

## Content
### Hardware Design
- Low-cost, lightweight flexible materials are used to fabricate the gripper pads, adapted to the grippers of small humanoid robots (e.g., NAO)
- Integrated force sensing units enable simultaneous measurement of normal gripping force and center of pressure (CoP)

### Calibration Method
- A dedicated calibration procedure is developed to enhance CoP measurement accuracy, compensating for sensor nonlinearity and installation errors

### Control Framework
- A hybrid force-alignment-position control strategy is proposed:
  - Force control: adjusts gripping force to a target value
  - Alignment control: ensures the gripper maintains parallel contact with the object surface
  - Position control: maintains the gripper's relative position
- Limit Surface Theory is introduced to model contact friction, dynamically calculating the minimum gripping force required to prevent slipping

### Experimental Validation
- Box-shaped objects are manipulated on the NAO humanoid robot to validate system effectiveness
- Experimental results demonstrate stable gripping force control, surface alignment accuracy meeting operational requirements, and successful prevention of object slippage

## 개요
이 2024년 논문은 소형 휴머노이드 로봇이 박스형 물체를 조작하는 요구를 위해 한 쌍의 저비용, 경량화된 유연한 힘 감지 그리퍼 패드를 설계했습니다. 그리퍼 패드는 실시간으로 법선 방향의 파지력과 압력 중심을 측정할 수 있으며, 전용 보정 방법을 통해 압력 중심 측정 정밀도를 향상시킵니다. 연구는 혼합 힘-정렬-위치 제어 프레임워크를 제안하여 파지력을 조절하고 그리퍼와 물체 표면의 밀착을 보장합니다. 한계 곡면 이론 기반의 접촉 마찰 모델은 미끄럼 방지에 필요한 최소 파지력을 결정할 수 있습니다. 전체 소프트웨어 및 하드웨어 시스템은 NAO 휴머노이드 로봇에서 실험 검증을 완료했습니다.

## 핵심 내용
### 하드웨어 설계
- 저비용, 경량화된 유연한 재료로 그리퍼 패드를 제작하여 소형 휴머노이드 로봇(예: NAO)의 그리퍼에 적합
- 힘 감지 유닛을 통합하여 법선 방향의 파지력과 압력 중심(CoP)을 동시에 측정

### 보정 방법
- CoP 측정 정밀도를 향상시키고 센서 비선형성 및 설치 오차를 보상하기 위한 전용 보정 절차 개발

### 제어 프레임워크
- 혼합 힘-정렬-위치 제어 전략 제안:
  - 힘 제어: 파지력을 목표 값으로 조절
  - 정렬 제어: 그리퍼와 물체 표면의 평행 접촉 보장
  - 위치 제어: 그리퍼의 상대 위치 유지
- 한계 곡면 이론(Limit Surface Theory)을 도입하여 접촉 마찰을 모델링하고, 미끄럼 방지에 필요한 최소 파지력을 동적으로 계산

### 실험 검증
- NAO 휴머노이드 로봇에서 박스형 물체를 조작하여 시스템 유효성 검증
- 실험 결과: 파지력 제어가 안정적이고, 표면 정렬 정밀도가 조작 요구를 충족하며, 물체 미끄러짐을 성공적으로 방지
