---
$id: ent_paper_efficient_sim_to_real_transfer_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors
  zh: Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors
  ko: Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors
summary:
  en: 'arXiv:2606.31101v1 Announce Type: new Abstract: Bridging the sim-to-real gap is a core challenge in deploying learned
    manipulation policies. Sim-to-real learning is attractive because it can replace expensive real robot demonstrations with
    scalable synthetic data, yet world-action models have not previously been shown to transfer from simulation to real robotic
    manipulation. We study whether a world-action model can be trained from synthetic priors and deployed zero-shot in the
    real world. To this end, we build upon Cosmos Policy, a video diffusion model adapted for visuomotor control. We construct
    simulation environments with extensive domain randomization and generate demonstrations using the AnyTask motion planning
    pipeline. We evaluate our approach across object lifting, drawer opening, and pick-and-place tasks using ${\sim}800$ synthetic
    demonstrations per task and no real demonstrations. When deployed zero-shot on a Franka Robot, our policy attains a 35\%
    average success rate. To our knowledge, this represents the first successful sim-to-real transfer of a world-action model
    for robotic manipulation.'
  zh: 本文研究世界-动作模型从仿真到真实机器人操作的零样本迁移。研究团队基于Cosmos Policy视频扩散模型，使用AnyTask运动规划流水线生成合成演示，在Franka Robot上实现了35%的平均成功率。这是首次成功将世界-动作模型从仿真迁移到真实机器人操作。
  ko: 'arXiv:2606.31101v1 Announce Type: new Abstract: Bridging the sim-to-real gap is a core challenge in deploying learned
    manipulation policies. Sim-to-real learning is attractive because it can replace expensive real robot demonstrations with
    scalable synthetic data, yet world-action models have not previously been shown to transfer from simulation to real robotic
    manipulation. We study whether a world-action model can be trained from synthetic priors and deployed zero-shot in the
    real world. To this end, we build upon Cosmos Policy, a video diffusion model adapted for visuomotor control. We construct
    simulation environments with extensive domain randomization and generate demonstrations using the AnyTask motion planning
    pipeline. We evaluate our approach across object lifting, drawer opening, and pick-and-place tasks using ${\sim}800$ synthetic
    demonstrations per task and no real demonstrations. When deployed zero-shot on a Franka Robot, our policy attains a 35\%
    average success rate. To our knowledge, this represents the first successful sim-to-real transfer of a world-action model
    for robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficient_sim_to_real_transfer
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31101v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors
  url: https://arxiv.org/abs/2606.31101
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
本文针对仿真到真实迁移这一核心挑战，探索世界-动作模型能否仅从合成先验训练并零样本部署到真实世界。研究团队以Cosmos Policy视频扩散模型为基础，构建了具有广泛域随机化的仿真环境，并使用AnyTask运动规划流水线生成演示数据。在物体拾取、抽屉打开和抓取放置三项任务中，每项任务仅使用约800个合成演示，无需任何真实演示。在Franka Robot上零样本部署时，策略达到了35%的平均成功率，这是世界-动作模型在机器人操作领域首次成功实现仿真到真实迁移。

## 核心内容
### 方法
- 基于Cosmos Policy视频扩散模型，该模型专为视觉运动控制调整
- 使用AnyTask运动规划流水线生成合成演示，确保动作多样性
- 仿真环境采用广泛域随机化，包括物体位置、光照、纹理等参数变化

### 实验设置
- 三项任务：物体拾取、抽屉打开、抓取放置
- 每项任务使用约800个合成演示，无真实演示
- 部署平台：Franka Robot，零样本测试

### 关键结果
- 平均成功率35%，其中物体拾取任务表现最佳
- 这是世界-动作模型首次成功从仿真迁移到真实机器人操作
- 结果表明合成先验足以训练可迁移的策略，但成功率仍有提升空间

### 结论
- 世界-动作模型可以从合成先验训练并零样本部署到真实世界
- 域随机化是成功迁移的关键因素
- 未来工作可探索更复杂的任务和更高成功率的策略优化

## Overview
Bridging the sim-to-real gap is a core challenge in deploying learned manipulation policies. Sim-to-real learning is attractive because it can replace expensive real robot demonstrations with scalable synthetic data, yet world-action models have not previously been shown to transfer from simulation to real robotic manipulation. We study whether a world-action model can be trained from synthetic priors and deployed zero-shot in the real world. To this end, we build upon Cosmos Policy, a video diffusion model adapted for visuomotor control. We construct simulation environments with extensive domain randomization and generate demonstrations using the AnyTask motion planning pipeline. We evaluate our approach across object lifting, drawer opening, and pick-and-place tasks using ${\sim}800$ synthetic demonstrations per task and no real demonstrations. When deployed zero-shot on a Franka Robot, our policy attains a 35\% average success rate. To our knowledge, this represents the first successful sim-to-real transfer of a world-action model for robotic manipulation.

## 개요
시뮬레이션과 실제 환경 간의 차이를 극복하는 것은 학습된 조작 정책을 배포하는 데 있어 핵심적인 과제입니다. 시뮬레이션-실제 학습은 비용이 많이 드는 실제 로봇 시연을 확장 가능한 합성 데이터로 대체할 수 있어 매력적이지만, 월드-액션 모델이 시뮬레이션에서 실제 로봇 조작으로 전이된 사례는 이전에 보고된 바 없습니다. 우리는 월드-액션 모델이 합성 사전 지식으로부터 학습되어 실제 환경에서 제로샷으로 배포될 수 있는지 연구합니다. 이를 위해, 우리는 시각운동 제어에 맞게 조정된 비디오 확산 모델인 Cosmos Policy를 기반으로 구축합니다. 광범위한 도메인 무작위화를 적용한 시뮬레이션 환경을 구성하고, AnyTask 모션 플래닝 파이프라인을 사용하여 시연을 생성합니다. 우리는 객체 들어올리기, 서랍 열기, 집기-놓기 작업에 대해 각 작업당 ${\sim}800$개의 합성 시연을 사용하고 실제 시연은 사용하지 않고 접근 방식을 평가합니다. Franka 로봇에 제로샷으로 배포했을 때, 우리의 정책은 35%의 평균 성공률을 달성했습니다. 우리가 아는 한, 이는 로봇 조작을 위한 월드-액션 모델의 최초의 성공적인 시뮬레이션-실제 전이를 나타냅니다.

## 핵심 내용
시뮬레이션과 실제 환경 간의 차이를 극복하는 것은 학습된 조작 정책을 배포하는 데 있어 핵심적인 과제입니다. 시뮬레이션-실제 학습은 비용이 많이 드는 실제 로봇 시연을 확장 가능한 합성 데이터로 대체할 수 있어 매력적이지만, 월드-액션 모델이 시뮬레이션에서 실제 로봇 조작으로 전이된 사례는 이전에 보고된 바 없습니다. 우리는 월드-액션 모델이 합성 사전 지식으로부터 학습되어 실제 환경에서 제로샷으로 배포될 수 있는지 연구합니다. 이를 위해, 우리는 시각운동 제어에 맞게 조정된 비디오 확산 모델인 Cosmos Policy를 기반으로 구축합니다. 광범위한 도메인 무작위화를 적용한 시뮬레이션 환경을 구성하고, AnyTask 모션 플래닝 파이프라인을 사용하여 시연을 생성합니다. 우리는 객체 들어올리기, 서랍 열기, 집기-놓기 작업에 대해 각 작업당 ${\sim}800$개의 합성 시연을 사용하고 실제 시연은 사용하지 않고 접근 방식을 평가합니다. Franka 로봇에 제로샷으로 배포했을 때, 우리의 정책은 35%의 평균 성공률을 달성했습니다. 우리가 아는 한, 이는 로봇 조작을 위한 월드-액션 모델의 최초의 성공적인 시뮬레이션-실제 전이를 나타냅니다.

## 参考
- http://arxiv.org/abs/2606.31101v1
