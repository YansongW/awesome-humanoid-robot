---
$id: ent_paper_sapkota_harmonic_content_analysis_of_a_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Harmonic content analysis of a soft starting variable frequency motor drive based on FPGA
  zh: 基于FPGA的软启动变频电机驱动的谐波含量分析
  ko: FPGA 기반 소프트 스타팅 가변 주파수 모터 드라이브의 고조파 함량 분석
summary:
  en: This paper proposes an FPGA-based variable-frequency soft-starting drive for three-phase induction motors using Direct
    Digital Synthesis, comparing sinusoidal PWM, third-harmonic-injected PWM, and space-vector PWM for harmonic performance
    and inrush-current reduction.
  zh: 本文提出了一种基于FPGA的三相感应电机变频软启动驱动器，采用直接数字频率合成技术，比较了正弦脉宽调制、三次谐波注入脉宽调制和空间矢量脉宽调制的谐波性能与启动涌流抑制效果。
  ko: 본 논문은 직접 디지털 합성(DDS) 기술을 이용한 삼상 유도전동기용 FPGA 기반 가변 주파수 소프트 스타팅 드라이브를 제안하고, 사인파 PWM, 3차 고조파 주입 PWM, 공간벡터 PWM의 고조파 특성과
    진입 전류 감소 효과를 비교한다.
domains:
- 02_components
- 05_mass_production
layers:
- midstream
functional_roles:
- knowledge
tags:
- fpga
- motor_drive
- variable_frequency_drive
- soft_start
- pwm
- induction_motor
- actuator_electronics
- harmonic_analysis
- direct_digital_synthesis
- space_vector_pwm
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.00720v1.
sources:
- id: src_001
  type: paper
  title: Harmonic content analysis of a soft starting variable frequency motor drive based on FPGA
  url: https://arxiv.org/abs/2311.00720
  date: '2023'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
As the demands for electric vehicles, electric aircrafts, unmanned aircraft systems, and other motor-driven systems increase, high-performance motor drives employing variable frequency control with higher efficiency and reliability are becoming increasingly important parts of the ever-changing technological landscape. This study proposes a Field Programmable Gate Array (FPGA)-based variable frequency soft-starting motor drive for a three-phase induction motor. The inverter output voltage and the load currents are analyzed for the harmonic contents using MATLAB. In the experimental realization, a four-pole squirrel cage delta-connected induction motor is utilized with a switching frequency of 4 kHz. The current and voltage characteristics of the induction motor are studied under different operating conditions to study harmonic contents and the effect of changing soft-start duration. The findings demonstrate a low-cost, flexible control of the induction motor with improved harmonic performance.

## 核心内容
As the demands for electric vehicles, electric aircrafts, unmanned aircraft systems, and other motor-driven systems increase, high-performance motor drives employing variable frequency control with higher efficiency and reliability are becoming increasingly important parts of the ever-changing technological landscape. This study proposes a Field Programmable Gate Array (FPGA)-based variable frequency soft-starting motor drive for a three-phase induction motor. The inverter output voltage and the load currents are analyzed for the harmonic contents using MATLAB. In the experimental realization, a four-pole squirrel cage delta-connected induction motor is utilized with a switching frequency of 4 kHz. The current and voltage characteristics of the induction motor are studied under different operating conditions to study harmonic contents and the effect of changing soft-start duration. The findings demonstrate a low-cost, flexible control of the induction motor with improved harmonic performance.

## 参考
- http://arxiv.org/abs/2311.00720v1

## Overview
As the demands for electric vehicles, electric aircrafts, unmanned aircraft systems, and other motor-driven systems increase, high-performance motor drives employing variable frequency control with higher efficiency and reliability are becoming increasingly important parts of the ever-changing technological landscape. This study proposes a Field Programmable Gate Array (FPGA)-based variable frequency soft-starting motor drive for a three-phase induction motor. The inverter output voltage and the load currents are analyzed for the harmonic contents using MATLAB. In the experimental realization, a four-pole squirrel cage delta-connected induction motor is utilized with a switching frequency of 4 kHz. The current and voltage characteristics of the induction motor are studied under different operating conditions to study harmonic contents and the effect of changing soft-start duration. The findings demonstrate a low-cost, flexible control of the induction motor with improved harmonic performance.

## Content
As the demands for electric vehicles, electric aircrafts, unmanned aircraft systems, and other motor-driven systems increase, high-performance motor drives employing variable frequency control with higher efficiency and reliability are becoming increasingly important parts of the ever-changing technological landscape. This study proposes a Field Programmable Gate Array (FPGA)-based variable frequency soft-starting motor drive for a three-phase induction motor. The inverter output voltage and the load currents are analyzed for the harmonic contents using MATLAB. In the experimental realization, a four-pole squirrel cage delta-connected induction motor is utilized with a switching frequency of 4 kHz. The current and voltage characteristics of the induction motor are studied under different operating conditions to study harmonic contents and the effect of changing soft-start duration. The findings demonstrate a low-cost, flexible control of the induction motor with improved harmonic performance.

## 개요
전기 자동차, 전기 항공기, 무인 항공기 시스템 및 기타 모터 구동 시스템에 대한 수요가 증가함에 따라, 더 높은 효율성과 신뢰성을 갖춘 가변 주파수 제어를 사용하는 고성능 모터 드라이브는 끊임없이 변화하는 기술 환경에서 점점 더 중요한 부분이 되고 있습니다. 본 연구는 3상 유도 전동기를 위한 FPGA(Field Programmable Gate Array) 기반 가변 주파수 소프트 스타팅 모터 드라이브를 제안합니다. 인버터 출력 전압과 부하 전류는 MATLAB을 사용하여 고조파 함량을 분석합니다. 실험 구현에서는 4kHz의 스위칭 주파수로 4극 농형 델타 결선 유도 전동기를 사용합니다. 유도 전동기의 전류 및 전압 특성은 다양한 작동 조건에서 연구되어 고조파 함량과 소프트 스타트 지속 시간 변경의 영향을 분석합니다. 결과는 개선된 고조파 성능을 갖춘 저비용의 유연한 유도 전동기 제어를 보여줍니다.

## 핵심 내용
전기 자동차, 전기 항공기, 무인 항공기 시스템 및 기타 모터 구동 시스템에 대한 수요가 증가함에 따라, 더 높은 효율성과 신뢰성을 갖춘 가변 주파수 제어를 사용하는 고성능 모터 드라이브는 끊임없이 변화하는 기술 환경에서 점점 더 중요한 부분이 되고 있습니다. 본 연구는 3상 유도 전동기를 위한 FPGA(Field Programmable Gate Array) 기반 가변 주파수 소프트 스타팅 모터 드라이브를 제안합니다. 인버터 출력 전압과 부하 전류는 MATLAB을 사용하여 고조파 함량을 분석합니다. 실험 구현에서는 4kHz의 스위칭 주파수로 4극 농형 델타 결선 유도 전동기를 사용합니다. 유도 전동기의 전류 및 전압 특성은 다양한 작동 조건에서 연구되어 고조파 함량과 소프트 스타트 지속 시간 변경의 영향을 분석합니다. 결과는 개선된 고조파 성능을 갖춘 저비용의 유연한 유도 전동기 제어를 보여줍니다.
