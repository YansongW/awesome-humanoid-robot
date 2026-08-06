---
$id: ent_paper_real2sim2real_vision_language_action_man_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline'
  zh: 'Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline'
  ko: 'Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline'
summary:
  en: Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real
    world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big
    thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI
    ... this is where AI enters the real.
  zh: 本文是 AMD 团队在 Physical AI 挑战赛中的技术报告，展示了一套完全基于 AMD 开放硬件（MI/Radeon/Ryzen）与 ROCm 软件栈的 Real2Sim2Real 全流程，覆盖 VLA 操控策略的仿真生成、训练、部署与
    RL 训练。核心贡献在于证明 VLA 操控研究无需绑定 CUDA 生态，并提出了 3DGS 重建真实背景 + Genesis 物理仿真的混合数据管线。
  ko: Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real
    world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big
    thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI
    ... this is where AI enters the real.
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
- real2sim2real
- vision
- language
- action
- man
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.22997 Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipelin'
  url: https://arxiv.org/abs/2607.22997
  date: '2026-07-25'
  accessed_at: '2026-08-05'
---

## 概述

本文是 AMD 团队在 Physical AI 挑战赛中的技术报告，展示了一套完全基于 AMD 开放硬件（MI/Radeon/Ryzen）与 ROCm 软件栈的 Real2Sim2Real 全流程，覆盖 VLA 操控策略的仿真生成、训练、部署与 RL 训练。核心贡献在于证明 VLA 操控研究无需绑定 CUDA 生态，并提出了 3DGS 重建真实背景 + Genesis 物理仿真的混合数据管线。

## 它改变了什么

它改变的是 VLA 操控研究对单一厂商封闭生态的路径依赖。过去，从仿真生成（通常依赖 CUDA 加速的物理引擎）到 VLA 训练（PyTorch/CUDA）再到边缘部署（TensorRT），每个环节都隐含 NVIDIA 硬件假设，这抬高了具身智能研究的迭代门槛。作者用四个 Demo 证明，AMD 的 ROCm + HIP 栈（已上游到 PyTorch 和 JAX）可以端到端覆盖这一流程，且无需 CUDA 转换层。

更关键的是，它改变了 sim-to-real 数据生成的思路。传统做法要么纯仿真（视觉差距大），要么纯真实数据（成本高、规模小）。作者提出的 Real2Sim 混合表示——用 3DGS 重建真实静态场景、用程序化方式注入动态交互物体——在保留真实视觉保真度的同时，获得了仿真独有的无限 rollout 能力。这为视觉多样化的操控任务提供了一条可扩展的数据路径。

## 方法拆解

### 总体架构：三层开放栈
开放硅片（MI/Radeon/Ryzen）→ ROCm + HIP 软件栈（上游到 PyTorch/JAX）→ 开源社区（LeRobot、Hugging Face、ModelScope）。所有管线原生运行于 ROCm，无 CUDA 转换层。

### Demo 1：Sim-to-Real 操控闭环
1. Genesis 物理仿真器生成示范 → 2. 转换为 LeRobot 数据集格式 → 3. AMD 平台上训练 SmolVLA-450M → 4. 仿真验证 → 5. 部署到真实 Franka 机械臂。合成数据生成在目标抓取任务分布上达到 100% 成功率。

### Demo 3：Real2Sim 合成数据管线（核心方法）
四阶段流程：
1. **3DGS 重建**：Radeon GPU + ROCm 对真实环境高保真重建，生成可实时渲染的高斯场景表示
2. **场景注入**：高斯点云作为静态背景加载到 Genesis，引入 Franka 机械臂 + 带物理属性（质量、摩擦、碰撞几何）的交互物体
3. **自动标注**：Genesis 生成末端执行器轨迹、多视角 RGB、深度图、分割掩码、关节状态、离散/连续动作，导出为 LeRobot 格式，可关联语言标注
4. **随机化控制**：物体布局、材质/纹理、光照、相机视角、机器人初始姿态、任务目标

关键设计决策：混合表示兼顾真实场景视觉保真度（避免"仿真外观"扩大 sim-to-real 差距）与仿真无限 rollout 能力。该管线同时作为 AMD 统一计算能力的压力测试——3DGS 重建、物理仿真、transformer 训练在同一块 Radeon PRO GPU 上完成。

### Demo 4：Unilab RL 训练
对 Unitree Go2（四足）和 G1（人形）进行并行批量仿真训练，任务包括全身跟踪（WBT）、行走、摇杆指令、动态翻转，使用 FastSAC、FlashSAC、PPO 混合算法匹配任务特性。

## 关键创新

1. **Real2Sim 混合表示**：3DGS 重建真实静态背景 + 程序化动态物体，这是首次将神经渲染与物理仿真结合用于 VLA 数据生成。它解决了纯仿真视觉差距大、纯真实数据成本高的两难，且开源为 vk-gsplat-plugin（Vulkan 实时 3DGS 渲染器）。

2. **全流程 ROCm 覆盖**：从 3DGS 重建、物理仿真到 VLA 训练、RL 训练，全部在 AMD 硬件 + ROCm 上完成，无需切换到 CUDA 专用栈。这打破了具身智能研究对单一厂商的锁定，为硬件多样化提供了实证。

3. **任务分离诊断**：Demo 2 将运动能力与语义接地分离，可诊断失败模式——抓取良好但选错物体表明语言-视觉融合缺陷，反之亦然。这种诊断思路对 VLA 策略调试有方法论价值。

## 实验与结果

Demo 1 关键指标：SmolVLA-450M 微调在 4,000 训练步下约 7–11 分钟收敛，峰值 VRAM 低于 2.4GB；从合成数据生成到真实部署完整循环 1 小时内完成；纯仿真训练策略直接迁移到真实 Franka，无需真实微调。

Demo 4 RL 训练吞吐量（steps/second，越高越好）：

| 设备 | FastSAC (G1 WBT) | FastSAC (G1 Walk) | FlashSAC (Go2 Joy.) | PPO (G1 Flip) |
|---|---|---|---|---|
| RTX 4090 (baseline) | 58.8 | 18.3 | 6.0 | 109.0 |
| RTX 4090 + AMD 9950X3D | 18.5 | 3.0 | 1.1 | 16.4 |
| AMD 8060S + AI MAX 395 | 33.6 | 9.4 | 4.2 | 19.6 |
| Apple M5 Max | 75.0 | 18.8 | 4.5 | 16.8 |

关键观察：RTX 4090 在 PPO/G1 Flip 领先（109.0 steps/s），但在 FlashSAC/Go2 Joy 上最慢（6.0 steps/s）；"RTX 4090 + AMD 9950X3D"配置全面低于纯 RTX 4090，表明 RL 训练部分受 CPU/主机限制；集成 AMD Ryzen AI MAX 395（8060S iGPU + 统一内存）在部分任务优于独立 GPU + AMD CPU 配置。作者明确强调跨硬件基准必须按算法逐个解读，吞吐量高度依赖任务而非纯硬件。

## 边界与局限

作者未在真实机器人上部署 Demo 3 的 Real2Sim 管线结果，仅描述管线本身。Demo 2 和 Demo 3 未提供定量成功率或误差指标。Demo 1 中用于播种的程序化随机化"相对简单"，仅足以弥合基本拾放任务的 sim-to-real 差距。Demo 4 的跨硬件基准受 CPU/主机限制影响，不能简单归因于 GPU 算力。论文未明确 Real2Sim 管线在视觉更复杂场景下的泛化能力，也未对比与纯仿真或纯真实数据管线的定量差异。

## 工程启示

复现时先核对硬件匹配：Demo 1 在 RDNA4（Radeon AI PRO R9700）和 RDNA3.5（Radeon PRO W7900）上原生运行 ROCm + PyTorch，无 CUDA 转换层；Radeon Cloud Platform 可免费复现全部四个管线，Real2Sim 笔记本在 R9700 或 W7900 节点上约 30 分钟完成端到端流程。最容易踩坑的是 Demo 4 的 RL 吞吐量基准——它受 CPU/主机限制显著，RTX 4090 + AMD CPU 组合反而低于纯 RTX 4090，因此对比硬件时应固定主机配置，且按算法逐个解读而非聚合。Demo 3 的 3DGS 重建依赖 Vulkan 插件（vk-gsplat-plugin），需确认 ROCm 版本与 PyTorch 上游兼容性。SmolVLA-450M 训练占用低于 2.4GB VRAM，意味着消费级显卡即可复现，但合成数据生成质量取决于 3DGS 重建保真度，建议先验证重建场景的视觉质量再投入大规模数据生成。

## Overview
Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI ... this is where AI enters the real world,' CES 2026). This paper presents an end-to-end, fully AMD-accelerated technology stack for embodied manipulation, spanning data-center training silicon, Radeon PRO simulation/rendering GPUs, and Ryzen AI edge compute, unified by the open ROCm software stack. We demonstrate that training and deploying VLA-based manipulation policies does not require a CUDA-locked ecosystem. Four progressive demonstrations are presented: (1) a Sim-to-Real manipulation pipeline trained with SmolVLA and deployed on a physical Franka arm; (2) a semantic, language-grounded object-selection task (`one-of-three'); (3) a Real2Sim synthetic-data generation pipeline that fuses 3D Gaussian Splatting (3DGS) reconstructions of real scenes with the Genesis physics engine; and (4) large-scale reinforcement learning for quadruped and humanoid locomotion benchmarked across multiple hardware platforms. All pipelines run natively on ROCm + PyTorch on RDNA4 (Radeon AI PRO R9700) and RDNA3.5 (Radeon PRO W7900) hardware and are reproducible on the free Radeon Cloud Platform.

## 参考
- https://arxiv.org/abs/2607.22997

## 개요

본 문서는 AMD 팀이 Physical AI 챌린지에서 제출한 기술 보고서로, 완전히 AMD 개방형 하드웨어(MI/Radeon/Ryzen)와 ROCm 소프트웨어 스택에 기반한 Real2Sim2Real 전체 프로세스를 보여준다. VLA 조작 정책의 시뮬레이션 생성, 훈련, 배포 및 RL 훈련을 포괄한다. 핵심 기여는 VLA 조작 연구가 CUDA 생태계에 얽매일 필요가 없음을 입증하고, 3DGS 재구성 기반 실제 배경 + Genesis 물리 시뮬레이션의 하이브리드 데이터 파이프라인을 제안한 것이다.

## 무엇을 바꾸는가

이는 VLA 조작 연구가 단일 공급업체 폐쇄 생태계에 대한 경로 의존성을 바꾼다. 과거에는 시뮬레이션 생성(일반적으로 CUDA 가속 물리 엔진에 의존)부터 VLA 훈련(PyTorch/CUDA), 엣지 배포(TensorRT)까지 모든 단계가 NVIDIA 하드웨어 가정을 내포하여, 임베디드 지능 연구의 반복 비용을 높였다. 저자들은 네 가지 데모를 통해 AMD의 ROCm + HIP 스택(이미 PyTorch 및 JAX에 업스트림됨)이 CUDA 변환 계층 없이 이 프로세스를 종단 간 포괄할 수 있음을 입증한다.

더 중요하게는, sim-to-real 데이터 생성 방식을 바꾼다. 기존 방식은 순수 시뮬레이션(시각적 격차 큼) 또는 순수 실제 데이터(비용 높음, 규모 작음) 중 하나였다. 저자들이 제안한 Real2Sim 하이브리드 표현——3DGS로 실제 정적 장면을 재구성하고, 절차적 방식으로 동적 상호작용 객체를 주입——은 실제 시각적 충실도를 유지하면서 시뮬레이션만의 무한 rollout 능력을 확보한다. 이는 시각적 다양성이 있는 조작 작업에 확장 가능한 데이터 경로를 제공한다.

## 방법 분석

### 전체 아키텍처: 3계층 개방형 스택
개방형 실리콘(MI/Radeon/Ryzen) → ROCm + HIP 소프트웨어 스택(PyTorch/JAX에 업스트림) → 오픈소스 커뮤니티(LeRobot, Hugging Face, ModelScope). 모든 파이프라인은 CUDA 변환 계층 없이 ROCm에서 기본 실행된다.

### 데모 1: Sim-to-Real 조작 폐쇄 루프
1. Genesis 물리 시뮬레이터가 시연 생성 → 2. LeRobot 데이터셋 형식으로 변환 → 3. AMD 플랫폼에서 SmolVLA-450M 훈련 → 4. 시뮬레이션 검증 → 5. 실제 Franka 로봇 팔에 배포. 합성 데이터 생성은 목표 파지 작업 분포에서 100% 성공률을 달성한다.

### 데모 3: Real2Sim 합성 데이터 파이프라인(핵심 방법)
4단계 프로세스:
1. **3DGS 재구성**: Radeon GPU + ROCm으로 실제 환경을 고충실도로 재구성, 실시간 렌더링 가능한 가우시안 장면 표현 생성
2. **장면 주입**: 가우시안 포인트 클라우드를 정적 배경으로 Genesis에 로드, Franka 로봇 팔 + 물리 속성(질량, 마찰, 충돌 기하)을 가진 상호작용 객체 도입
3. **자동 주석**: Genesis가 엔드 이펙터 궤적, 다중 시점 RGB, 깊이 맵, 분할 마스크, 관절 상태, 이산/연속 동작을 생성하고 LeRobot 형식으로 내보내며, 언어 주석과 연결 가능
4. **무작위화 제어**: 객체 레이아웃, 재질/텍스처, 조명, 카메라 시점, 로봇 초기 자세, 작업 목표

핵심 설계 결정: 하이브리드 표현은 실제 장면의 시각적 충실도("시뮬레이션 외관"이 sim-to-real 격차를 확대하는 것을 방지)와 시뮬레이션의 무한 rollout 능력을 동시에 확보한다. 이 파이프라인은 AMD 통합 컴퓨팅 능력의 스트레스 테스트이기도 하다——3DGS 재구성, 물리 시뮬레이션, transformer 훈련이 동일한 Radeon PRO GPU에서 수행된다.

### 데모 4: Unilab RL 훈련
Unitree Go2(4족) 및 G1(휴머노이드)에 대해 병렬 배치 시뮬레이션 훈련을 수행하며, 전신 추적(WBT), 보행, 조이스틱 명령, 동적 뒤집기 작업을 포함하고, FastSAC, FlashSAC, PPO 혼합 알고리즘으로 작업 특성에 맞춘다.

## 핵심 혁신

1. **Real2Sim 하이브리드 표현**: 3DGS로 실제 정적 배경 재구성 + 절차적 동적 객체. 신경 렌더링과 물리 시뮬레이션을 VLA 데이터 생성에 결합한 최초의 사례다. 순수 시뮬레이션의 시각적 격차와 순수 실제 데이터의 높은 비용이라는 딜레마를 해결하며, vk-gsplat-plugin(Vulkan 실시간 3DGS 렌더러)으로 오픈소스화되었다.

2. **전체 프로세스 ROCm 커버리지**: 3DGS 재구성, 물리 시뮬레이션부터 VLA 훈련, RL 훈련까지 모두 AMD 하드웨어 + ROCm에서 수행되며, CUDA 전용 스택으로 전환할 필요가 없다. 이는 임베디드 지능 연구의 단일 공급업체 잠금을 깨고 하드웨어 다양성에 대한 실증을 제공한다.

3. **작업 분리 진단**: 데모 2는 운동 능력과 의미적 접지를 분리하여 실패 모드를 진단할 수 있다——파지는 잘 되지만 객체 선택이 틀리면 언어-시각 융합 결함을 나타내고, 그 반대도 마찬가지다. 이러한 진단 접근법은 VLA 정책 디버깅에 방법론적 가치가 있다.

## 실험 및 결과

데모 1 핵심 지표: SmolVLA-450M 미세 조정은 4,000 훈련 스텝에서 약 7–11분 내 수렴, 최대 VRAM 2.4GB 미만; 합성 데이터 생성부터 실제 배포까지 전체 루프 1시간 내 완료; 순수 시뮬레이션 훈련 정책이 실제 미세 조정 없이 실제 Franka에 직접 전이.

데모 4 RL 훈련 처리량(steps/second, 높을수록 좋음):

| 장치 | FastSAC (G1 WBT) | FastSAC (G1 Walk) | FlashSAC (Go2 Joy.) | PPO (G1 Flip) |
|---|---|---|---|---|
| RTX 4090 (baseline) | 58.8 | 18.3 | 6.0 | 109.0 |
| RTX 4090 + AMD 9950X3D | 18.5 | 3.0 | 1.1 | 16.4 |
| AMD 8060S + AI MAX 395 | 33.6 | 9.4 | 4.2 | 19.6 |
| Apple M5 Max | 75.0 | 18.8 | 4.5 | 16.8 |

핵심 관찰: RTX 4090은 PPO/G1 Flip에서 선두(109.0 steps/s)지만, FlashSAC/Go2 Joy에서는 가장 느림(6.0 steps/s); "RTX 4090 + AMD 9950X3D" 구성은 순수 RTX 4090보다 전반적으로 낮아 RL 훈련이 CPU/호스트 제약을 받음을 시사; 통합 AMD Ryzen AI MAX 395(8060S iGPU + 통합 메모리)는 일부 작업에서 개별 GPU + AMD CPU 구성보다 우수. 저자들은 크로스 하드웨어 벤치마크를 알고리즘별로 개별 해석해야 하며, 처리량은 순수 하드웨어가 아닌 작업에 크게 의존한다고 명시적으로 강조한다.

## 경계 및 한계

저자들은 데모 3의 Real2Sim 파이프라인 결과를 실제 로봇에 배포하지 않았으며, 파이프라인 자체만 설명한다. 데모 2와 데모 3은 정량적 성공률 또는 오류 지표를 제공하지 않는다. 데모 1에서 시딩에 사용된 절차적 무작위화는 "상대적으로 단순"하여 기본 픽앤플레이스 작업의 sim-to-real 격차를 메우기에 충분하다. 데모 4의 크로스 하드웨어 벤치마크는 CPU/호스트 제약의 영향을 받아 GPU 연산 능력으로 단순 귀인할 수 없다. 논문은 Real2Sim 파이프라인의 시각적으로 더 복잡한 장면에서의 일반화 능력을 명확히 하지 않았으며, 순수 시뮬레이션 또는 순수 실제 데이터 파이프라인과의 정량적 차이도 비교하지 않았다.

## 엔지니어링 시사점

재현 시 먼저 하드웨어 호환성을 확인하라: 데모 1은 RDNA4(Radeon AI PRO R9700) 및 RDNA3.5(Radeon PRO W7900)에서 CUDA 변환 계층 없이 ROCm + PyTorch를 기본 실행한다; Radeon Cloud Platform에서 네 가지 파이프라인을 모두 무료로 재현할 수 있으며, Real2Sim 노트북은 R9700 또는 W7900 노드에서 약 30분 내 종단 간 프로세스를 완료한다. 가장 함정이 많은 부분은 데모 4의 RL 처리량 벤치마크——CPU/호스트 제약이 크며, RTX 4090 + AMD CPU 조합이 순수 RTX 4090보다 오히려 낮으므로, 하드웨어 비교 시 호스트 구성을 고정하고 알고리즘별로 개별 해석해야 한다. 데모 3의 3DGS 재구성은 Vulkan 플러그인(vk-gsplat-plugin)에 의존하므로, ROCm 버전과 PyTorch 업스트림 호환성을 확인해야 한다. SmolVLA-450M 훈련은 2.4GB 미만 VRAM을 사용하므로 소비자용 GPU로도 재현 가능하지만, 합성 데이터 생성 품질은 3DGS 재구성 충실도에 달려 있으므로, 대규모 데이터 생성 전에 재구성 장면의 시각적 품질을 먼저 검증할 것을 권장한다.
