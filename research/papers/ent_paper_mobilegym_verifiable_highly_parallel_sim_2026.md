---
$id: ent_paper_mobilegym_verifiable_highly_parallel_sim_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research'
  zh: 'MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research'
  ko: 'MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research'
summary:
  en: 'We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting
    interaction fidelity without replicating proprietary backends. Institutions per source list: 中科院自动化所、北大、港中文等.'
  zh: MobileGym 是一个基于浏览器的轻量级移动 GUI 智能体仿真平台，由研究团队提出，支持确定性状态判据与低成本并行在线强化学习。其核心贡献在于通过结构化 JSON 状态实现可验证结果信号，并能在单台服务器上托管数百个并行实例，每个实例仅需约
    400 MB 内存和约 3 秒冷启动时间。配套的 MobileGym-Bench 包含 416 个参数化任务模板，覆盖 28 个应用，在 Sim-to-Real 实验中，GRPO 在 Qwen3-VL-4B-Instruct 上提升了
    12.8 个百分点，真实设备执行保留了 95.1% 的仿真训练增益。
  ko: 'We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting
    interaction fidelity without replicating proprietary backends. Institutions per source list: 中科院自动化所、北大、港中文等.'
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
- mobilegym
- verifiable
- highly
- parallel
- sim
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 713 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2605.26114 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.26114v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.26114 MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research'
  url: https://arxiv.org/abs/2605.26114
  accessed_at: '2026-07-31'
  date: '2026-05-25'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/Purewhiter/mobilegym
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://mobilegym.github.io
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: Project page (fetched)
  url: https://raw.githubusercontent.com/Purewhiter/mobilegym/HEAD/README.md
  accessed_at: '2026-07-31'
- id: src_005
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

MobileGym 是一个面向移动 GUI 智能体研究的高效仿真平台，运行于浏览器中，无需复制专有后端即可实现高交互保真度。它通过结构化 JSON 状态捕获、配置、分叉和比较环境，实现了确定性状态判据，避免了传统自由文本匹配的失败问题。平台采用分层状态模型和声明式任务定义框架，支持大规模任务创建，单台服务器可运行数百个并行实例，内存占用约 400 MB，冷启动时间约 3 秒。配套的 MobileGym-Bench 提供了 416 个参数化任务模板，包括 256 个测试和 160 个训练模板，覆盖 28 个应用，并配有确定性判据和结构化 AnswerSheet 协议。在 Sim-to-Real 案例研究中，GRPO 在 Qwen3-VL-4B-Instruct 上于 256 任务测试集获得 12.8 个百分点的提升，在 59 任务真实设备子集上保留了 95.1% 的仿真训练增益。

## 核心内容
### 方法
MobileGym 采用浏览器托管架构，通过结构化 JSON 状态模型实现环境全状态捕获、配置、分叉和比较。其分层状态模型支持状态可编程性，而声明式任务定义框架使得大规模任务创建变得实用。平台使用单一程序化判据机制，同时提供确定性评估结果和密集的强化学习奖励信号。

### 架构
- **环境架构**：基于浏览器的轻量级设计，无需复制专有后端，支持高交互保真度。
- **并行能力**：单台服务器可托管数百个并行实例，每个实例内存占用约 400 MB，冷启动时间约 3 秒。
- **状态管理**：通过结构化 JSON 实现环境状态的确定性捕获、配置、分叉和比较。

### 实验设置
- **基准测试**：MobileGym-Bench 包含 416 个参数化任务模板，其中 256 个测试模板和 160 个训练模板，覆盖 28 个应用。
- **判据机制**：使用确定性判据和结构化 AnswerSheet 协议，避免自由文本匹配失败。
- **Sim-to-Real 实验**：在 Qwen3-VL-4B-Instruct 模型上应用 GRPO 算法进行训练。

### 关键数字
- **内存占用**：每个并行实例约 400 MB。
- **冷启动时间**：约 3 秒。
- **任务模板**：416 个参数化任务模板（256 测试 + 160 训练），覆盖 28 个应用。
- **Sim-to-Real 结果**：GRPO 在 Qwen3-VL-4B-Instruct 上于 256 任务测试集获得 +12.8 个百分点提升；在 59 任务真实设备子集上，真实设备执行保留了 95.1% 的仿真训练增益。

### 结论
MobileGym 通过可验证结果信号和低成本并行在线强化学习，显著提升了移动 GUI 智能体研究的效率。其 Sim-to-Real 案例研究证明了仿真训练的有效性，真实设备执行保留了大部分训练增益，为移动 GUI 智能体研究提供了实用平台。

## Overview
We present MobileGym, a browser-hosted, lightweight, fully controllable environment for everyday mobile use, targeting interaction fidelity without replicating proprietary backends. It enables two capabilities previously out of reach for everyday apps: verifiable outcome signals through deterministic state-based judging over structured JSON state, and scalable online RL through low-cost parallel rollouts. The full environment state is captured, configured, forked, and compared as structured JSON, and a single server can host hundreds of parallel instances, with about 400 MB memory per instance and about 3 s cold start. A layered state model and a declarative task-definition framework keep state programmability and task creation practical at scale, and a single programmatic judging mechanism delivers both deterministic evaluation verdicts and dense RL rewards. The accompanying MobileGym-Bench provides 416 parameterized task templates, including 256 test and 160 train templates, over 28 apps, with deterministic judges and a structured AnswerSheet protocol that avoids free-text matching failures. In a Sim-to-Real case study, GRPO on Qwen3-VL-4B-Instruct gains +12.8 percentage points on the 256-task test set, and on a 59-task real-device signal subset, real-device execution retains 95.1% of the simulation-side training gain. Project page: https://mobilegym.github.io.

## 参考
- https://arxiv.org/abs/2605.26114
- https://github.com/Purewhiter/mobilegym
- https://mobilegym.github.io
- https://raw.githubusercontent.com/Purewhiter/mobilegym/HEAD/README.md
- https://github.com/ImChong/Robotics_Notebooks

## 개요

MobileGym은 모바일 GUI 에이전트 연구를 위한 효율적인 시뮬레이션 플랫폼으로, 브라우저에서 실행되며 독점 백엔드를 복제할 필요 없이 높은 상호작용 충실도를 제공합니다. 구조화된 JSON 상태 캡처, 구성, 포크 및 환경 비교를 통해 결정론적 상태 판정 기준을 구현하여 기존 자유 텍스트 매칭의 실패 문제를 방지합니다. 플랫폼은 계층적 상태 모델과 선언적 작업 정의 프레임워크를 채택하여 대규모 작업 생성을 지원하며, 단일 서버에서 수백 개의 병렬 인스턴스를 실행할 수 있고 메모리 사용량은 약 400MB, 콜드 스타트 시간은 약 3초입니다. 함께 제공되는 MobileGym-Bench는 416개의 매개변수화된 작업 템플릿(256개의 테스트 및 160개의 훈련 템플릿 포함)을 제공하며, 28개의 앱을 포괄하고 결정론적 판정 기준 및 구조화된 AnswerSheet 프로토콜을 갖추고 있습니다. Sim-to-Real 사례 연구에서 GRPO는 Qwen3-VL-4B-Instruct에서 256개 작업 테스트 세트에서 12.8% 포인트 향상을 달성했으며, 59개 작업 실제 기기 하위 집합에서 시뮬레이션 훈련 이득의 95.1%를 유지했습니다.

## 핵심 내용
### 방법
MobileGym은 브라우저 호스팅 아키텍처를 채택하여 구조화된 JSON 상태 모델을 통해 환경의 전체 상태 캡처, 구성, 포크 및 비교를 구현합니다. 계층적 상태 모델은 상태 프로그래밍 가능성을 지원하며, 선언적 작업 정의 프레임워크는 대규모 작업 생성을 실용적으로 만듭니다. 플랫폼은 단일 프로그래밍 방식 판정 기준 메커니즘을 사용하여 결정론적 평가 결과와 밀집된 강화 학습 보상 신호를 동시에 제공합니다.

### 아키텍처
- **환경 아키텍처**: 브라우저 기반의 경량 설계로 독점 백엔드를 복제할 필요 없이 높은 상호작용 충실도를 지원합니다.
- **병렬 능력**: 단일 서버에서 수백 개의 병렬 인스턴스를 호스팅할 수 있으며, 각 인스턴스의 메모리 사용량은 약 400MB, 콜드 스타트 시간은 약 3초입니다.
- **상태 관리**: 구조화된 JSON을 통해 환경 상태의 결정론적 캡처, 구성, 포크 및 비교를 구현합니다.

### 실험 설정
- **벤치마크**: MobileGym-Bench는 416개의 매개변수화된 작업 템플릿(256개의 테스트 템플릿 및 160개의 훈련 템플릿 포함)을 포함하며, 28개의 앱을 포괄합니다.
- **판정 기준 메커니즘**: 결정론적 판정 기준과 구조화된 AnswerSheet 프로토콜을 사용하여 자유 텍스트 매칭 실패를 방지합니다.
- **Sim-to-Real 실험**: Qwen3-VL-4B-Instruct 모델에 GRPO 알고리즘을 적용하여 훈련을 수행합니다.

### 주요 수치
- **메모리 사용량**: 각 병렬 인스턴스당 약 400MB.
- **콜드 스타트 시간**: 약 3초.
- **작업 템플릿**: 416개의 매개변수화된 작업 템플릿(256개 테스트 + 160개 훈련), 28개 앱 포괄.
- **Sim-to-Real 결과**: GRPO는 Qwen3-VL-4B-Instruct에서 256개 작업 테스트 세트에서 +12.8% 포인트 향상 달성; 59개 작업 실제 기기 하위 집합에서 실제 기기 실행이 시뮬레이션 훈련 이득의 95.1%를 유지.

### 결론
MobileGym은 검증 가능한 결과 신호와 저비용 병렬 온라인 강화 학습을 통해 모바일 GUI 에이전트 연구의 효율성을 크게 향상시킵니다. Sim-to-Real 사례 연구는 시뮬레이션 훈련의 효과성을 입증하며, 실제 기기 실행이 대부분의 훈련 이득을 유지하여 모바일 GUI 에이전트 연구에 실용적인 플랫폼을 제공합니다.
