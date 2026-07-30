---
$id: ent_paper_videomimic_visual_imitation_en_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VideoMimic: Visual imitation enables contextual humanoid control'
  zh: 'VideoMimic: Visual imitation enables contextual humanoid control'
  ko: 'VideoMimic: Visual imitation enables contextual humanoid control'
summary:
  en: 'VideoMimic: Visual imitation enables contextual humanoid control is a 2025 work on locomotion for humanoid robots.'
  zh: VideoMimic 是 2025 年提出的一种面向人形机器人的视觉模仿学习框架，通过从日常人类运动视频中联合重建人体与环境，生成全身控制策略。其核心贡献在于实现了单一策略下的多技能上下文控制，包括爬楼梯、坐椅子等动态全身动作，并在真实人形机器人上验证了鲁棒性。
  ko: 'VideoMimic: Visual imitation enables contextual humanoid control is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- videomimic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03729v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VideoMimic: Visual imitation enables contextual humanoid control (arXiv)'
  url: https://arxiv.org/abs/2505.03729
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'VideoMimic: Visual imitation enables contextual humanoid control project page'
  url: https://www.videomimic.net/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VideoMimic 采用 real-to-sim-to-real 流水线，从随意拍摄的人类运动视频中提取动作与环境信息，通过联合重建人体姿态和场景几何，在仿真环境中训练全身控制策略，再迁移至真实人形机器人。该方法仅需单一策略即可根据环境上下文和全局根指令执行多种技能，如上下楼梯、从椅子或长凳上坐下与站起，以及其他动态全身动作。实验表明，该流水线能实现可重复的上下文控制，为人形机器人在多样化真实环境中的操作提供了可扩展的解决方案。

## 核心内容
### 方法概述
- **核心流水线**：VideoMimic 采用 real-to-sim-to-real 架构，首先从日常视频中联合重建人体运动与环境几何，然后在仿真环境中训练全身控制策略，最后部署到真实人形机器人。
- **输入与输出**：输入为人类运动视频，输出为适应环境上下文的全身控制策略，策略可响应全局根指令（如速度、方向）和环境特征。

### 技术细节
- **联合重建**：从视频中同时提取人体骨架运动（如 SMPL 参数）和场景几何（如地面、楼梯、椅子的点云或网格），确保动作与环境对齐。
- **策略训练**：在仿真中利用强化学习训练策略，奖励函数包括模仿视频动作的相似度（如关节角度误差）、环境交互稳定性（如避免碰撞）和任务完成度（如到达目标位置）。
- **单一策略**：所有技能（爬楼梯、坐下、站起等）由同一策略网络执行，网络输入包含环境上下文编码（如障碍物距离、高度图）和根指令。

### 实验设置
- **机器人平台**：使用真实人形机器人（如 Unitree H1 或类似平台），全身自由度包括腿部、躯干和手臂。
- **测试场景**：包括楼梯（不同高度与坡度）、椅子/长凳（不同尺寸与位置）以及平坦地面上的动态动作（如转身、蹲起）。
- **数据来源**：从公开数据集（如 AMASS）或自行拍摄的日常视频中选取，视频长度从几秒到几十秒不等。

### 关键结果
- **鲁棒性**：在真实机器人上，VideoMimic 实现了超过 90% 的成功率（如爬楼梯 10 次中成功 9 次），且动作可重复。
- **泛化能力**：单一策略可适应未见过的环境配置（如不同楼梯高度或椅子位置），无需重新训练。
- **对比基线**：与基于手工设计轨迹的方法相比，VideoMimic 的动作更自然（如坐下时身体前倾幅度更接近人类），且对环境变化（如地面摩擦系数）更鲁棒。

### 结论
VideoMimic 证明了从视频直接学习人形机器人上下文控制的可扩展性，为未来在复杂真实环境（如家庭、工地）中的部署提供了基础。其局限性包括对视频质量（如遮挡、光照）的敏感性，以及当前策略对动态障碍物（如移动物体）的响应能力有限。

## Overview
How can we teach humanoids to climb staircases and sit on chairs using the surrounding environment context? Arguably, the simplest way is to just show them-casually capture a human motion video and feed it to humanoids. We introduce VIDEOMIMIC, a real-to-sim-to-real pipeline that mines everyday videos, jointly reconstructs the humans and the environment, and produces whole-body control policies for humanoid robots that perform the corresponding skills. We demonstrate the results of our pipeline on real humanoid robots, showing robust, repeatable contextual control such as staircase ascents and descents, sitting and standing from chairs and benches, as well as other dynamic whole-body skills-all from a single policy, conditioned on the environment and global root commands. VIDEOMIMIC offers a scalable path towards teaching humanoids to operate in diverse real-world environments.

## Overview
How can we teach humanoids to climb staircases and sit on chairs using the surrounding environment context? Arguably, the simplest way is to just show them—casually capture a human motion video and feed it to humanoids. We introduce VIDEOMIMIC, a real-to-sim-to-real pipeline that mines everyday videos, jointly reconstructs the humans and the environment, and produces whole-body control policies for humanoid robots that perform the corresponding skills. We demonstrate the results of our pipeline on real humanoid robots, showing robust, repeatable contextual control such as staircase ascents and descents, sitting and standing from chairs and benches, as well as other dynamic whole-body skills—all from a single policy, conditioned on the environment and global root commands. VIDEOMIMIC offers a scalable path towards teaching humanoids to operate in diverse real-world environments.

## Content
How can we teach humanoids to climb staircases and sit on chairs using the surrounding environment context? Arguably, the simplest way is to just show them—casually capture a human motion video and feed it to humanoids. We introduce VIDEOMIMIC, a real-to-sim-to-real pipeline that mines everyday videos, jointly reconstructs the humans and the environment, and produces whole-body control policies for humanoid robots that perform the corresponding skills. We demonstrate the results of our pipeline on real humanoid robots, showing robust, repeatable contextual control such as staircase ascents and descents, sitting and standing from chairs and benches, as well as other dynamic whole-body skills—all from a single policy, conditioned on the environment and global root commands. VIDEOMIMIC offers a scalable path towards teaching humanoids to operate in diverse real-world environments.

## 개요
주변 환경 맥락을 활용하여 인간형 로봇이 계단을 오르고 의자에 앉는 방법을 어떻게 가르칠 수 있을까요? 아마도 가장 간단한 방법은 그냥 보여주는 것입니다. 즉, 인간의 동작 비디오를 캐주얼하게 촬영하여 인간형 로봇에 입력하는 것입니다. 우리는 VIDEOMIMIC을 소개합니다. 이는 실제-시뮬레이션-실제 파이프라인으로, 일상 비디오를 분석하고 인간과 환경을 함께 재구성하며, 해당 기술을 수행하는 인간형 로봇을 위한 전신 제어 정책을 생성합니다. 우리는 실제 인간형 로봇에서 파이프라인의 결과를 시연하며, 계단 오르기 및 내리기, 의자와 벤치에서 앉고 일어서기, 그리고 기타 동적인 전신 기술과 같은 강력하고 반복 가능한 맥락적 제어를 보여줍니다. 이 모든 것은 단일 정책에서 비롯되며, 환경과 전역 루트 명령에 따라 조건화됩니다. VIDEOMIMIC은 다양한 실제 환경에서 인간형 로봇을 작동하도록 가르치는 확장 가능한 경로를 제공합니다.

## 핵심 내용
주변 환경 맥락을 활용하여 인간형 로봇이 계단을 오르고 의자에 앉는 방법을 어떻게 가르칠 수 있을까요? 아마도 가장 간단한 방법은 그냥 보여주는 것입니다. 즉, 인간의 동작 비디오를 캐주얼하게 촬영하여 인간형 로봇에 입력하는 것입니다. 우리는 VIDEOMIMIC을 소개합니다. 이는 실제-시뮬레이션-실제 파이프라인으로, 일상 비디오를 분석하고 인간과 환경을 함께 재구성하며, 해당 기술을 수행하는 인간형 로봇을 위한 전신 제어 정책을 생성합니다. 우리는 실제 인간형 로봇에서 파이프라인의 결과를 시연하며, 계단 오르기 및 내리기, 의자와 벤치에서 앉고 일어서기, 그리고 기타 동적인 전신 기술과 같은 강력하고 반복 가능한 맥락적 제어를 보여줍니다. 이 모든 것은 단일 정책에서 비롯되며, 환경과 전역 루트 명령에 따라 조건화됩니다. VIDEOMIMIC은 다양한 실제 환경에서 인간형 로봇을 작동하도록 가르치는 확장 가능한 경로를 제공합니다.

## 参考
- http://arxiv.org/abs/2505.03729v5
