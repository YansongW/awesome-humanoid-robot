---
$id: ent_paper_huang_x_nav_technical_report_real_wo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot'
  zh: 'X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot'
  ko: 'X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot'
summary:
  en: 'Long-horizon navigation from indoors to outdoors remains an open problem for humanoid robots: one instruction covers
    rooms, doors and roads, and the camera moves with the gait. Worken, AGIBOT''s measure of productive robot work, depends
    on robots that reach their workplaces autonomously. We present X-Nav, to our knowledge the first system to take a bipedal
    humanoid through a language-instructed ...'
  zh: X-Nav 是首个让双足人形机器人完成从室内到室外、由语言指令驱动的长程导航任务的系统，由 AGIBOT 相关团队提出。系统覆盖从数据采集到真机部署的完整流程，其导航模型 MELIOR 仅依赖机器人自带相机的 RGB 图像，分为预测动作的
    MELIOR-A 与预测导航目标的 MELIOR-N 两个版本。在 Lingxi X2 上，X-Nav 完成了从办公楼大堂到邻近建筑商店约一百米的导航任务。
  ko: 'Long-horizon navigation from indoors to outdoors remains an open problem for humanoid robots: one instruction covers
    rooms, doors and roads, and the camera moves with the gait. Worken, AGIBOT''s measure of productive robot work, depends
    on robots that reach their workplaces autonomously. We present X-Nav, to our knowledge the first system to take a bipedal
    humanoid through a language-instructed ...'
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
- humanoid_navigation
- long_horizon_navigation
- vision_language_navigation
- sim_to_real
- indoor_to_outdoor
- agentic_workflow
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.17598);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.17598 X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot'
  url: https://arxiv.org/abs/2611.17598
  date: '2026-11-12'
  accessed_at: '2026-11-16'
---

## 概述

X-Nav 针对人形机器人室内到室外长程导航这一开放问题，提出了一套从数据到部署的完整系统。其数据引擎在开源场景、部署场地的数字孪生以及真实机器人上采集导航数据；导航模型 MELIOR 仅使用机器人内置相机的 RGB 图像，并提供预测动作与预测导航目标两种版本。智能体工作流 X-Navarch 将简短的人类指令拆解为子任务，并在机器人上以明确的目标导航与避障方式部署 MELIOR。在 Lingxi X2 上，系统完成了约一百米的室内到室外任务，LiDAR 与里程计用于目标接近和底层控制；部署阶段还利用场地数字孪生中采集的数据对 MELIOR 进行适配，提升了其在孪生环境中的闭环成功率，随后将适配后的模型部署到真实场地。此外，MELIOR 在 R2R-CE 与 RxR-CE 基准上取得了有竞争力的结果。

## 核心内容

### 问题背景
人形机器人从室内走向室外的长程导航仍是未解问题：一条指令可能覆盖房间、门和道路，且相机随步态移动。AGIBOT 提出的 Worken 以机器人能否自主到达工作地点为衡量标准，因此自主导航能力至关重要。

### 方法
- **数据引擎**：在开源场景、部署场地的数字孪生以及真实机器人上采集导航数据。
- **导航模型 MELIOR**：仅输入机器人内置相机的 RGB 图像，包含两个版本——MELIOR-A 预测动作，MELIOR-N 预测导航目标。
- **智能体工作流 X-Navarch**：将简短的人类指令转化为子任务，并在机器人上以明确的目标导航与避障方式部署 MELIOR。

### 实验设置
在 Lingxi X2 人形机器人上执行从办公楼大堂到邻近建筑商店、约一百米的任务；LiDAR 与里程计用于目标接近和底层控制。部署期间，利用在场地数字孪生中采集的数据对 MELIOR 进行适配，再将适配后的模型部署到真实场地。

### 关键结果
- 任务在 MELIOR 两个版本下均完成：机器人能够跟随目的地变更，并从大堂穿过门走到道路上；配合 X-Navarch 时还能通过路线上的静态与动态障碍。
- 在数字孪生中，数据适配提升了 MELIOR 的闭环成功率。
- MELIOR 在 R2R-CE 与 RxR-CE 基准上取得有竞争力的结果。

### 结论
X-Nav 据称是首个让双足人形机器人完成语言指令驱动的室内到室外长程任务的系统，验证了从数据采集、模型训练到真机部署的完整链路可行性。

## Overview

Long-horizon navigation from indoors to outdoors remains an open problem for humanoid robots: one instruction covers rooms, doors and roads, and the camera moves with the gait. Worken, AGIBOT's measure of productive robot work, depends on robots that reach their workplaces autonomously. We present X-Nav, to our knowledge the first system to take a bipedal humanoid through a language-instructed long-horizon mission from indoors to outdoors. X-Nav covers a pipeline from data to deployment. Its data engine collects navigation data in open-source scenes, in digital twins of deployment sites and on real robots. Its navigation model, MELIOR, takes only RGB images from the robot's built-in camera and comes in two versions: MELIOR-A predicts actions, and MELIOR-N predicts a navigation goal. Its agentic workflow, X-Navarch, turns a brief human instruction into sub-tasks and deploys MELIOR on the robot with explicit target navigation and obstacle avoidance. On the Lingxi X2, X-Nav completes a mission of about a hundred metres from an office lobby to a store in a neighbouring building; LiDAR and odometry are used for target approach and low-level control. The mission is completed with both versions of MELIOR: the robot follows a change of destination and walks through a door from the lobby to the road, and with X-Navarch it also passes static and dynamic obstacles on the route. During deployment, MELIOR is adapted with data collected in a digital twin of the site; the adaptation raises its closed-loop success rate in the twin, and the adapted model is then deployed on the robot at the real site. In addition, MELIOR achieves competitive results on the R2R-CE and RxR-CE benchmarks.

## 参考
- https://arxiv.org/abs/2611.17598
