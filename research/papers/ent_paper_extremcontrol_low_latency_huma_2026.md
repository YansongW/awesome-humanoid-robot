---
$id: ent_paper_extremcontrol_low_latency_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
  zh: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
  ko: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
summary:
  en: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
  zh: ExtremControl 是 2026 年提出的一种低延迟人形机器人全身遥操作框架。它通过直接操控肢体末端 SE(3) 位姿、采用笛卡尔空间映射与速度前馈控制，将端到端延迟降至 50ms，显著超越此前 200ms 的延迟极限，并成功实现了乒乓球平衡、杂耍等快速反应任务。
  ko: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- extremcontrol
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11321v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (722 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control (arXiv)'
  url: https://arxiv.org/abs/2602.11321
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有遥操作方案依赖繁重的人到人形运动重定向与仅位置 PD 控制，导致延迟过高，无法支持需要快速反馈与反应的任务。ExtremControl 通过直接操作选定刚体（主要是肢体末端）的 SE(3) 位姿，避免了全身重定向；利用笛卡尔空间映射将人体运动直接转换为机器人连杆目标；并在底层引入速度前馈控制以增强对快速变化界面的响应能力。该系统支持光学动捕与 VR 追踪两种输入方式，在仿真与真实环境中均验证了有效性，实现了低至 50ms 的端到端延迟，远超此前 200ms 的极限。

## 核心内容
### 核心问题
- 现有方法依赖“人到人形”运动重定向与仅位置 PD 控制，导致延迟高（约 200ms），无法执行需要快速反馈与动态响应的任务（如接球、平衡）。

### 方法架构
- **直接末端控制**：直接操作选定刚体（主要是人形机器人四肢末端）的 SE(3) 位姿，避免全身运动重定向带来的计算延迟。
- **笛卡尔空间映射**：将人体运动直接映射为机器人连杆的笛卡尔空间目标，无需中间关节角度转换。
- **速度前馈控制**：在底层控制中引入速度前馈项，使机器人能对快速变化的控制指令做出即时响应。

### 系统实现
- 支持两种输入方式：光学动作捕捉与 VR 追踪。
- 端到端延迟低至 **50ms**，显著低于此前工作的 **200ms** 延迟极限。

### 实验验证
- 在仿真与真实环境中均进行了系统验证。
- 成功演示了高动态行为：乒乓球平衡、杂耍、实时回传等，证明了系统在快速反馈任务中的有效性。

### 理论贡献
- 提供了 ExtremControl 的统一理论公式，为后续低延迟遥操作研究奠定基础。

## Overview
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## 参考
- http://arxiv.org/abs/2602.11321v3

## 개요
기존 원격 조작 방식은 무거운 사람-휴머노이드 동작 재매핑과 위치 기반 PD 제어에 의존하여 지연 시간이 과도하게 발생하며, 빠른 피드백과 반응이 필요한 작업을 지원할 수 없습니다. ExtremControl은 선택된 강체(주로 사지 말단)의 SE(3) 자세를 직접 조작하여 전신 재매핑을 피하고, 데카르트 공간 매핑을 통해 인간의 동작을 로봇 링크 목표로 직접 변환하며, 하위 수준에 속도 피드포워드 제어를 도입하여 빠르게 변화하는 인터페이스에 대한 대응 능력을 강화합니다. 이 시스템은 광학 모션 캡처와 VR 트래킹 두 가지 입력 방식을 지원하며, 시뮬레이션 및 실제 환경에서 유효성을 검증하여 기존 200ms 한계를 훨씬 넘어서는 최저 50ms의 종단 간 지연 시간을 달성했습니다.

## 핵심 내용
### 핵심 문제
- 기존 방법은 '사람-휴머노이드' 동작 재매핑과 위치 기반 PD 제어에 의존하여 지연 시간이 높고(약 200ms), 빠른 피드백과 동적 반응이 필요한 작업(예: 공 받기, 균형 유지)을 수행할 수 없습니다.

### 방법 아키텍처
- **직접 말단 제어**: 선택된 강체(주로 휴머노이드 로봇 사지 말단)의 SE(3) 자세를 직접 조작하여 전신 동작 재매핑으로 인한 계산 지연을 방지합니다.
- **데카르트 공간 매핑**: 인간의 동작을 로봇 링크의 데카르트 공간 목표로 직접 변환하여 중간 관절 각도 변환을 생략합니다.
- **속도 피드포워드 제어**: 하위 수준 제어에 속도 피드포워드 항을 도입하여 로봇이 빠르게 변화하는 제어 명령에 즉각적으로 반응할 수 있게 합니다.

### 시스템 구현
- 두 가지 입력 방식 지원: 광학 모션 캡처 및 VR 트래킹.
- 종단 간 지연 시간이 최저 **50ms**로, 이전 연구의 **200ms** 지연 한계보다 현저히 낮습니다.

### 실험 검증
- 시뮬레이션 및 실제 환경 모두에서 시스템 검증을 수행했습니다.
- 높은 동적 동작을 성공적으로 시연: 탁구공 균형 유지, 저글링, 실시간 리턴 등, 빠른 피드백 작업에서 시스템의 유효성을 입증했습니다.

### 이론적 기여
- ExtremControl의 통일된 이론 공식을 제공하여 향후 저지연 원격 조작 연구의 기반을 마련했습니다.
