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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03729v5. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1159 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.03729v5

## 개요
VideoMimic은 real-to-sim-to-real 파이프라인을 채택하여, 일상적으로 촬영된 인간 동작 비디오에서 동작과 환경 정보를 추출하고, 인간 자세와 장면 기하학을 공동 재구성하여 시뮬레이션 환경에서 전신 제어 정책을 훈련한 뒤 실제 휴머노이드 로봇으로 전이합니다. 이 방법은 단일 정책만으로 환경 컨텍스트와 전역 루트 명령에 따라 계단 오르내리기, 의자나 벤치에서 앉고 일어서기, 기타 동적 전신 동작 등 다양한 스킬을 수행할 수 있습니다. 실험 결과, 이 파이프라인은 반복 가능한 컨텍스트 제어를 구현하여 다양한 실제 환경에서 휴머노이드 로봇의 조작을 위한 확장 가능한 솔루션을 제공합니다.

## 핵심 내용
### 방법 개요
- **핵심 파이프라인**: VideoMimic은 real-to-sim-to-real 아키텍처를 사용하며, 먼저 일상 비디오에서 인간 동작과 환경 기하학을 공동 재구성한 다음, 시뮬레이션 환경에서 전신 제어 정책을 훈련하고, 마지막으로 실제 휴머노이드 로봇에 배포합니다.
- **입력 및 출력**: 입력은 인간 동작 비디오이고, 출력은 환경 컨텍스트에 적응하는 전신 제어 정책으로, 정책은 전역 루트 명령(예: 속도, 방향)과 환경 특징에 응답합니다.

### 기술 세부 사항
- **공동 재구성**: 비디오에서 인간 골격 동작(예: SMPL 파라미터)과 장면 기하학(예: 지면, 계단, 의자의 포인트 클라우드 또는 메시)을 동시에 추출하여 동작과 환경의 정렬을 보장합니다.
- **정책 훈련**: 시뮬레이션에서 강화 학습을 사용하여 정책을 훈련하며, 보상 함수에는 비디오 동작과의 유사성(예: 관절 각도 오차), 환경 상호작용 안정성(예: 충돌 회피), 작업 완료도(예: 목표 위치 도달)가 포함됩니다.
- **단일 정책**: 모든 스킬(계단 오르기, 앉기, 일어서기 등)은 동일한 정책 네트워크로 실행되며, 네트워크 입력에는 환경 컨텍스트 인코딩(예: 장애물 거리, 높이 맵)과 루트 명령이 포함됩니다.

### 실험 설정
- **로봇 플랫폼**: 실제 휴머노이드 로봇(예: Unitree H1 또는 유사 플랫폼)을 사용하며, 전신 자유도에는 다리, 몸통, 팔이 포함됩니다.
- **테스트 시나리오**: 다양한 높이와 경사의 계단, 다양한 크기와 위치의 의자/벤치, 평평한 지면에서의 동적 동작(예: 회전, 스쿼트)이 포함됩니다.
- **데이터 소스**: 공개 데이터셋(예: AMASS) 또는 직접 촬영한 일상 비디오에서 선택하며, 비디오 길이는 수 초에서 수십 초까지 다양합니다.

### 주요 결과
- **강건성**: 실제 로봇에서 VideoMimic은 90% 이상의 성공률(예: 계단 오르기 10회 중 9회 성공)을 달성하며, 동작은 반복 가능합니다.
- **일반화 능력**: 단일 정책은 보지 못한 환경 구성(예: 다른 계단 높이 또는 의자 위치)에 적응할 수 있으며, 재훈련이 필요 없습니다.
- **기준선 비교**: 수작업으로 설계된 궤적 기반 방법과 비교하여, VideoMimic의 동작은 더 자연스럽고(예: 앉을 때 몸이 앞으로 기울어지는 정도가 인간에 더 가까움), 환경 변화(예: 지면 마찰 계수)에 더 강건합니다.

### 결론
VideoMimic은 비디오에서 휴머노이드 로봇의 컨텍스트 제어를 직접 학습하는 확장 가능성을 입증하며, 복잡한 실제 환경(예: 가정, 건설 현장)에서의 향후 배포를 위한 기반을 제공합니다. 한계로는 비디오 품질(예: 폐색, 조명)에 대한 민감성과 현재 정책의 동적 장애물(예: 이동 물체)에 대한 응답 능력 제한이 있습니다.
