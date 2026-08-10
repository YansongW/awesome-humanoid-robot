---
$id: ent_paper_ding_toward_certified_functional_sa_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study'
  zh: 'Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study'
  ko: 'Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study'
summary:
  en: 'Industrial humanoid robots are constrained less by locomotion or manipulation capability than by the immaturity of
    functional safety certification for legged platforms. The root difficulty is that the safe state of a legged robot is
    an actively-controlled state, which violates the fail-passive assumption underlying ISO~13849-1 / EN~60204-1: removing
    power from a walking biped causes an ...'
  zh: 本文由 Caiwu Ding、Tao Cui、Lingyun Wang 和 Chengtao Wen 撰写，针对工业人形机器人的功能安全认证难题，提出“失效-被动间隙”概念，并通过外部安全链和西门子安全 PLC 参考设计进行可行性研究。研究在
    Unitree G1 EDU 机器人上验证了主动安全状态分析，但明确不声称实现端到端认证的 PL e / SIL 3。
  ko: 'Industrial humanoid robots are constrained less by locomotion or manipulation capability than by the immaturity of
    functional safety certification for legged platforms. The root difficulty is that the safe state of a legged robot is
    an actively-controlled state, which violates the fail-passive assumption underlying ISO~13849-1 / EN~60204-1: removing
    power from a walking biped causes an ...'
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
- functional_safety
- fail_passive_gap
- industrial_humanoid
- safety_certification
- active_safe_state
- profisafe
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-10'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-10). Bibliographic metadata from arXiv API (2608.02809);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.02809 Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility
    Study'
  url: https://arxiv.org/abs/2608.02809
  date: '2026-08-03'
  accessed_at: '2026-08-10'
---

## 概述

工业人形机器人的主要瓶颈并非运动或操作能力，而是腿式平台功能安全认证的不成熟。核心困难在于腿式机器人的安全状态是主动控制状态，违反 ISO 13849-1 / EN 60204-1 中“失效-被动”假设——断电会导致双足机器人失控摔倒，因此传统断电本身即构成危险。作者将此称为“失效-被动间隙”，并使用认证的外部安全链（光幕、急停、安全输入、安全 PLC、无线 PROFIsafe）精确定位该间隙，将不可认证元素缩小到机器人侧反应链。通过西门子 S7-1500 安全急停参考，他们证明可认证的反应子系统是基于接触器的断电（停止类别 0），而这正是平衡人形机器人无法具备的元素。研究在 Unitree G1 EDU 的拾放单元中验证了方法，并贡献了主动安全状态的人形机器人特定分析。

## 核心内容

### 问题背景
工业人形机器人在功能安全认证方面面临根本性挑战。传统工业机械依赖“失效-被动”原则，即断电后设备进入安全状态。然而，双足机器人断电后会失控摔倒，使得经典的去能化本身成为危险源。这一矛盾被定义为“失效-被动间隙”，是腿式平台安全认证不成熟的核心原因。

### 方法
作者使用认证的外部安全链作为定位工具，包括光幕、紧急停止、失效安全输入、失效安全 PLC 和无线 PROFIsafe。由于外部链是封闭的，且可通过既有方法（PFHD、DC、CCF、PL/SILCL）量化，残余的不可认证元素被精确定位到机器人侧反应链。通过西门子失效安全 S7-1500 紧急停止参考，他们展示了可认证的反应子系统是基于接触器的断电（停止类别 0），而这正是平衡人形机器人无法具备的元素。

### 实验设置
研究在 Unitree G1 EDU 拾放单元中进行，工作空间为 3m x 1.5m 的半封闭区域。作者贡献了人形机器人特定的主动安全状态分析，包括摔倒作为危险、单支撑停止边界、平衡策略残余风险以及 ISO 13855 分离距离。他们还提供了带来源标记的时序预算。

### 关键结果
将工业软件定义自动化（SDA）控制器托管在机器人上，与平衡策略共置，可将机器人侧 PROFINET/PROFIsafe 接收移至标准化的 IEC 61131-3 接口。然而，由于 G1 的机载计算不是安全评级硬件，该端点并非认证的安全运行时，这强化而非解决了失效-被动间隙，并将其定位到 SDA 与平衡策略之间的接口。

### 结论
作者明确不声称实现端到端认证的 PL e / SIL 3。研究验证了外部安全链的可行性，但确认机器人侧反应链仍是认证的关键障碍，需要进一步开发主动安全状态的标准和硬件。

## Overview

Industrial humanoid robots are constrained less by locomotion or manipulation capability than by the immaturity of functional safety certification for legged platforms. The root difficulty is that the safe state of a legged robot is an actively-controlled state, which violates the fail-passive assumption underlying ISO~13849-1 / EN~60204-1: removing power from a walking biped causes an uncontrolled fall, so classical de-energization is itself a hazard. We term this the fail-passive gap and use a certified external safety chain (light curtain, emergency stop, fail-safe input, fail-safe PLC, and wireless PROFIsafe) as an instrument to locate it precisely: because the external chain is closed and quantifiable with established methods (PFHD, DC, CCF, PL/SILCL), the residual uncertifiable element is pinpointed to the robot-side reaction chain. Using a Siemens fail-safe S7-1500 emergency-stop reference, we show its certifiable Reaction subsystem is contactor-based power removal (Stop Category~0)---exactly the element a balancing humanoid cannot have. We deliberately do not claim end-to-end certified PL~e / SIL~3. We validate the approach on a Unitree G1 EDU pick-and-place cell in a 3m x 1.5m semi-enclosed workspace, and contribute a humanoid-specific analysis of the active safe state (fall-as-hazard, single-support stop bounds, balancing-policy residual risk, ISO~13855 separation) and a provenance-labeled timing budget. Hosting an industrial software-defined automation (SDA) controller on the robot, co-located with the balancing policy, moves robot-side PROFINET/PROFIsafe reception onto a standardized IEC~61131-3 interface; because the G1's onboard compute is not safety-rated hardware, this endpoint is not a certified safety runtime, which reinforces rather than resolves the fail-passive gap and localizes it to the SDA-to-balancing-policy interface.

## 参考
- https://arxiv.org/abs/2608.02809
