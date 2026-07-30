---
$id: ent_paper_generalizable_humanoid_manipul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies
  zh: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies
  ko: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies
summary:
  en: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies is a 2024 work on manipulation for humanoid
    robots, with open-source code available.
  zh: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies 是2024年提出的人形机器人操作系统，由研究团队构建。其核心贡献在于：通过集成全身遥操作数据采集、25自由度人形机器人平台与改进的3D
    Diffusion Policy算法，使机器人仅凭单场景数据即可在多种真实环境中自主执行操作任务，代码已开源。
  ko: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies is a 2024 work on manipulation for humanoid
    robots, with open-source code available.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalizable_humanoid_manipul
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.10803v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies (arXiv)
  url: https://arxiv.org/abs/2410.10803
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies project page
  url: https://humanoid-manipulation.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该系统针对人形机器人自主操作泛化能力不足与野外数据获取成本高的问题，提出了一套完整解决方案。系统包含三个核心模块：用于采集类人操作数据的全身遥操作装置、配备可调高度推车与3D LiDAR的25自由度人形机器人平台，以及专为处理噪声人类数据设计的改进型3D Diffusion Policy学习算法。通过超过2000次真实机器人策略部署的严格评估，验证了该系统仅使用单场景采集数据与机载计算资源，即可使全尺寸人形机器人在多样化真实场景中自主执行操作技能。

## 核心内容
### 系统架构
- **数据采集**：采用全身遥操作系统，覆盖机器人上半身所有自由度，可采集包含手臂、躯干协调动作的类人操作数据
- **硬件平台**：25自由度全尺寸人形机器人，配备高度可调推车（适应不同工作台高度）与3D LiDAR传感器（提供环境感知）
- **学习算法**：改进的3D Diffusion Policy，专门针对人类演示数据中的噪声（如抖动、不精确轨迹）进行优化

### 实验设置
- 训练数据：仅在单一场景（如固定桌面）中采集的人类演示数据
- 计算资源：完全依赖机器人机载计算单元（无外部服务器支持）
- 评估规模：超过2000次真实机器人策略部署（policy rollouts）

### 关键结果
- 单场景训练数据即可实现跨场景泛化，包括不同光照条件、物体位置偏移、背景变化等
- 机载计算条件下，策略推理延迟满足实时控制要求（具体数值未在摘要中提及）
- 开源代码与演示视频（https://humanoid-manipulation.github.io）可供复现验证

### 结论
该工作首次证明：通过改进的扩散策略与高效数据采集系统，人形机器人可突破传统操作系统的场景限制，在无需大规模多场景数据的前提下实现泛化操作能力。

## Overview
Humanoid robots capable of autonomous operation in diverse environments have long been a goal for roboticists. However, autonomous manipulation by humanoid robots has largely been restricted to one specific scene, primarily due to the difficulty of acquiring generalizable skills and the expensiveness of in-the-wild humanoid robot data. In this work, we build a real-world robotic system to address this challenging problem. Our system is mainly an integration of 1) a whole-upper-body robotic teleoperation system to acquire human-like robot data, 2) a 25-DoF humanoid robot platform with a height-adjustable cart and a 3D LiDAR sensor, and 3) an improved 3D Diffusion Policy learning algorithm for humanoid robots to learn from noisy human data. We run more than 2000 episodes of policy rollouts on the real robot for rigorous policy evaluation. Empowered by this system, we show that using only data collected in one single scene and with only onboard computing, a full-sized humanoid robot can autonomously perform skills in diverse real-world scenarios. Videos are available at https://humanoid-manipulation.github.io .

## 개요
다양한 환경에서 자율적으로 작동할 수 있는 휴머노이드 로봇은 오랫동안 로봇 공학자들의 목표였습니다. 그러나 휴머노이드 로봇의 자율 조작은 주로 일반화 가능한 기술을 습득하기 어렵고 실제 환경에서의 휴머노이드 로봇 데이터 수집 비용이 높기 때문에 특정 장면으로 크게 제한되어 왔습니다. 본 연구에서는 이러한 어려운 문제를 해결하기 위해 실제 로봇 시스템을 구축했습니다. 우리 시스템은 주로 1) 인간과 유사한 로봇 데이터를 수집하기 위한 전상반신 로봇 원격 조작 시스템, 2) 높이 조절 가능한 카트와 3D LiDAR 센서를 갖춘 25자유도 휴머노이드 로봇 플랫폼, 3) 잡음이 있는 인간 데이터로부터 학습하기 위한 휴머노이드 로봇용 개선된 3D 확산 정책 학습 알고리즘을 통합한 것입니다. 우리는 엄격한 정책 평가를 위해 실제 로봇에서 2000회 이상의 정책 롤아웃을 실행했습니다. 이 시스템을 통해 단일 장면에서 수집된 데이터와 온보드 컴퓨팅만으로도 전체 크기의 휴머노이드 로봇이 다양한 실제 시나리오에서 자율적으로 기술을 수행할 수 있음을 보여줍니다. 비디오는 https://humanoid-manipulation.github.io 에서 확인할 수 있습니다.

## 핵심 내용
다양한 환경에서 자율적으로 작동할 수 있는 휴머노이드 로봇은 오랫동안 로봇 공학자들의 목표였습니다. 그러나 휴머노이드 로봇의 자율 조작은 주로 일반화 가능한 기술을 습득하기 어렵고 실제 환경에서의 휴머노이드 로봇 데이터 수집 비용이 높기 때문에 특정 장면으로 크게 제한되어 왔습니다. 본 연구에서는 이러한 어려운 문제를 해결하기 위해 실제 로봇 시스템을 구축했습니다. 우리 시스템은 주로 1) 인간과 유사한 로봇 데이터를 수집하기 위한 전상반신 로봇 원격 조작 시스템, 2) 높이 조절 가능한 카트와 3D LiDAR 센서를 갖춘 25자유도 휴머노이드 로봇 플랫폼, 3) 잡음이 있는 인간 데이터로부터 학습하기 위한 휴머노이드 로봇용 개선된 3D 확산 정책 학습 알고리즘을 통합한 것입니다. 우리는 엄격한 정책 평가를 위해 실제 로봇에서 2000회 이상의 정책 롤아웃을 실행했습니다. 이 시스템을 통해 단일 장면에서 수집된 데이터와 온보드 컴퓨팅만으로도 전체 크기의 휴머노이드 로봇이 다양한 실제 시나리오에서 자율적으로 기술을 수행할 수 있음을 보여줍니다. 비디오는 https://humanoid-manipulation.github.io 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2410.10803v3
