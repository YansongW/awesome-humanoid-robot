---
$id: ent_component_manufacturer_nvidia
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: NVIDIA
  zh: 英伟达
  ko: 엔비디아
summary:
  en: American semiconductor and software company supplying GPUs, edge AI compute modules,
    simulation platforms, and robot-learning tools used in humanoid development.
  zh: 美国半导体和软件公司，供应 GPU、边缘 AI 计算模块、仿真平台和机器人学习工具，用于人形机器人开发。
  ko: GPU, 엣지 AI 컴퓨팅 모듈, 시뮬레이션 플랫폼 및 로봇 학습 도구를 공급하는 미국 반도체 및
    소프트웨어 기업입니다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- upstream
- intelligence
functional_roles:
- organization
- component
- intelligence
tags:
- nvidia
- jetson
- isaac
- gpu
- edge_compute
- simulation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: high
  notes: Product specifications and software capabilities are publicly documented on official
    product pages.
sources:
- id: src_001
  type: website
  title: NVIDIA Jetson AGX Orin Series
  url: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: website
  title: NVIDIA Isaac Sim / Isaac Lab
  url: https://developer.nvidia.com/isaac
  date: '2026'
  accessed_at: '2026-06-24'
---

## Overview

NVIDIA is a leading supplier of AI compute and simulation infrastructure for robotics. Its Jetson embedded GPU modules are widely used as onboard perception and planning computers in humanoid robots, while its Isaac Sim and Isaac Lab platforms provide physics-based simulation and reinforcement-learning workflows for robot development.

## Key Offerings

- **Jetson AGX Orin**: Up to 275 TOPS AI performance at 15–60 W, with up to 64 GB LPDDR5 memory and 204.8 GB/s memory bandwidth.
- **Isaac Sim**: GPU-accelerated robotics simulator built on NVIDIA Omniverse.
- **Isaac Lab**: Unified framework for robot learning, supporting sim-to-real and imitation learning pipelines.
- **Isaac Teleop**: Human demonstration capture and teleoperation reference workflow, integrated with devices such as MANUS Metagloves.

## Relevance to Humanoid Robotics

NVIDIA's hardware and software stack is a common denominator across many humanoid development programs. Edge compute performance, simulation fidelity, and learning-tool availability directly influence which AI models and control strategies can be deployed on real hardware.
