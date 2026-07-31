---
$id: ent_paper_aspire_agentic_skill_programming_through
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASPIRE: Agentic Skill Programming through Iterative Robot Exploration'
  zh: 'ASPIRE: Agentic Skill Programming through Iterative Robot Exploration'
  ko: 'ASPIRE: Agentic Skill Programming through Iterative Robot Exploration'
summary:
  en: 'ASPIRE: Agentic /Skills Discovery for Robotics Overview Method Task Gallery Skill Library Benchmarks Limitations Conclusion
    Team BibTeX Paper Scroll Auto Discover /skills for Robots Scroll Paper Code (coming soon) Method: How ASPIRE Works ASPIRE
    is a self-improving continual learning system for robo Institutions per source list: NVIDIA GEAR Lab、UMich、UIUC、UC Berkeley、CMU.'
  zh: ASPIRE 是一个面向机器人的自我改进持续学习系统，由研究团队提出。其核心贡献在于通过闭环执行引擎、持续扩展的技能库和进化搜索程序，自主编写并优化代码形式的控制策略，将验证后的修复经验提炼为可复用的技能，从而显著提升任务成功率。
  ko: 'ASPIRE: Agentic /Skills Discovery for Robotics Overview Method Task Gallery Skill Library Benchmarks Limitations Conclusion
    Team BibTeX Paper Scroll Auto Discover /skills for Robots Scroll Paper Code (coming soon) Method: How ASPIRE Works ASPIRE
    is a self-improving continual learning system for robo Institutions per source list: NVIDIA GEAR Lab、UMich、UIUC、UC Berkeley、CMU.'
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
- aspire
- agentic
- skill
- programming
- through
- project_page_sourced
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: Full ingest from Yuanxq lab paper list row 309 (.staging/ingest_yuanxq). Tier B->page. Content compiled by DeepSeek
    from the fetched project page (https://research.nvidia.com/labs/gear/aspire/). Institutions as given in the source list,
    not verified.
sources:
- id: src_001
  type: website
  title: Project page
  url: https://research.nvidia.com/labs/gear/aspire/
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

ASPIRE 系统包含三个关键组件：闭环机器人执行引擎会记录每次感知、规划、抓取和控制调用的多模态轨迹，使系统能够定位故障并验证修复；持续扩展的技能库将验证后的修复提炼为模块化、可迁移的机器人知识，供未来任务检索；进化搜索程序则通过生成多样化的任务序列和控制程序，在迭代调试与并行优化中探索超越单条轨迹的自我改进。在 LIBERO-PRO、Robosuite 和 BEHAVIOR-1K 等基准测试中，ASPIRE 显著提升了任务成功率，例如将双臂交接任务的成功率从 20% 基线提升至 92%。

## 核心内容
### 方法：ASPIRE 的工作原理
ASPIRE 是一个自我改进的持续学习系统，它通过执行反馈来编写和优化代码形式的机器人控制程序。系统会检查执行轨迹、诊断故障、修复程序、验证修正后的行为，并将可复用的技能保存到技能库中。ASPIRE 在一个开放式学习循环中运行，包含三个核心组件：
- **闭环机器人执行引擎**：每次感知、规划、抓取和控制调用时，引擎都会记录观察结果、输入、输出以及可能的视觉证据。这些丰富的多模态轨迹允许系统选择性地检查关键原始日志，逐步定位故障，并通过重新执行来验证修复。
- **持续扩展的技能库**：ASPIRE 维护一个不断增长的技能库，将验证后的修复提炼为模块化、可迁移的机器人知识，可作为未来任务的上下文指导进行检索。
- **程序进化搜索**：ASPIRE 采用进化搜索程序，生成多样化的任务序列和控制程序，通过迭代调试和并行优化，探索超越单条轨迹的自我改进。

### 基准测试结果
所有基准测试中，每个任务实例都使用环境种子固定，包括物体姿态、干扰物以及初始机器人/物体状态。ASPIRE 使用不相交的调试种子和评估种子：ASPIRE 在一个小的调试集上学习，然后在更大的保留评估种子上报告成功率，每个 LIBERO-Pro/Robosuite 任务生成一个程序；而 CaP-Agent0 则通过测试时推理和重试，为每个种子重新生成一个单独的程序。对于 BEHAVIOR-1K 评估，ASPIRE 使用增量块执行，从当前多模态轨迹生成下一个代码块。
- **LIBERO-PRO**：ASPIRE 编写的控制程序能够泛化到不同的物体类型、物体位置和任务细节。
- **Robosuite**：ASPIRE 处理接触密集的桌面操作任务。最值得注意的是，通过迭代调试，ASPIRE 将双臂交接任务的成功率从 20% 的基线提升到了 92%。
- **BEHAVIOR-1K**：对于长时域移动操作，导航和任务完成情况分开报告。

### 技能库的零样本迁移与规模扩展
- **LIBERO-Long**：在 LIBERO-90 上学习到的技能可以迁移到保留的长时域任务中。随着技能库的增长，编码代理在 LIBERO-Long 上实现了更高的成功率。
- **真实机器人跨实体技能迁移**：对于每个任务，我们比较了有和没有从 ASPIRE 技能库中检索对应仿真发现技能时的真实机器人调试情况。令牌计数测量到第一个成功的真实机器人程序为止。成功率报告的是实现首次成功的代码在保留评估试验中的表现。当配备 ASPIRE 技能时，编码代理用更少的令牌就达到了首次成功，并且生成的代码实现了更高的成功率。输出令牌（M）、总令牌（M）、保留成功率（%）。

### 局限性
- 尚未成为完全自主的真实世界学习者。真实世界部署仍需稳健的成功检测、安全重置、安全监控和校准。
- 依赖于固定的前沿 LLM。ASPIRE 依赖一个前沿模型（Claude Opus 4.6）；尚未验证较小或较弱的 LLM 能否维持调试循环。
- 受限于预定义的原始 API。固定的感知、规划和控制原语集合保证了调试的安全性，但限制了可表达的行为。
- 不完整的长期记忆管理。技能库目前优先考虑验证过的可复用修复，但未完全解决长期记忆管理问题。随着技能库增长，某些条目可能变得过时、过于具体、冗余或对新任务产生误导。
- 计算密集的搜索循环。调试和进化搜索循环每个任务需要大量 LLM 调用和 rollout，因此扩展需要更便宜的推理或更高效的搜索。

### 结论
我们提出了 ASPIRE，一个自我改进的持续学习机器人系统，它能够自主编写和优化机器人控制程序，同时将经验积累到可复用的技能库中。ASPIRE 在一个开放式学习循环中运行，包含三个组件：一个暴露细粒度多模态轨迹的闭环机器人执行引擎，一个将验证修复提炼为可迁移知识的持续扩展技能库，以及一个探索多样化任务序列和控制程序的进化搜索程序。在多个基准测试中，ASPIRE 取得了显著成果。

## 参考
- https://research.nvidia.com/labs/gear/aspire/
- https://github.com/ImChong/Robotics_Notebooks

## Overview

The ASPIRE system comprises three key components: a closed-loop robot execution engine that records multimodal trajectories for each perception, planning, grasping, and control call, enabling the system to localize failures and verify fixes; a continuously expanding skill library that distills verified repairs into modular, transferable robot knowledge for retrieval in future tasks; and an evolutionary search program that generates diverse task sequences and control programs, exploring self-improvement beyond single trajectories through iterative debugging and parallel optimization. On benchmarks such as LIBERO-PRO, Robosuite, and BEHAVIOR-1K, ASPIRE significantly improves task success rates, for example, boosting the success rate of a bimanual handover task from a 20% baseline to 92%.

## Content
### Method: How ASPIRE Works
ASPIRE is a self-improving continual learning system that writes and optimizes robot control programs in code form through execution feedback. The system examines execution trajectories, diagnoses failures, repairs programs, verifies corrected behaviors, and saves reusable skills into a skill library. ASPIRE operates in an open-ended learning loop with three core components:
- **Closed-Loop Robot Execution Engine**: For each perception, planning, grasping, and control call, the engine records observations, inputs, outputs, and possible visual evidence. These rich multimodal trajectories allow the system to selectively inspect key primitive logs, progressively localize failures, and verify fixes through re-execution.
- **Continuously Expanding Skill Library**: ASPIRE maintains a growing skill library that distills verified repairs into modular, transferable robot knowledge, which can be retrieved as contextual guidance for future tasks.
- **Program Evolution Search**: ASPIRE employs an evolutionary search program that generates diverse task sequences and control programs, exploring self-improvement beyond single trajectories through iterative debugging and parallel optimization.

### Benchmark Results
Across all benchmarks, each task instance is fixed using environment seeds, including object poses, distractors, and initial robot/object states. ASPIRE uses disjoint debugging and evaluation seeds: ASPIRE learns on a small debugging set and then reports success rates on a larger held-out evaluation set, generating one program per LIBERO-Pro/Robosuite task; whereas CaP-Agent0 regenerates a separate program for each seed through test-time inference and retries. For BEHAVIOR-1K evaluation, ASPIRE uses incremental block execution, generating the next code block from the current multimodal trajectory.
- **LIBERO-PRO**: Control programs written by ASPIRE generalize to different object types, object positions, and task details.
- **Robosuite**: ASPIRE handles contact-rich tabletop manipulation tasks. Most notably, through iterative debugging, ASPIRE improves the success rate of a bimanual handover task from a 20% baseline to 92%.
- **BEHAVIOR-1K**: For long-horizon mobile manipulation, navigation and task completion are reported separately.

### Zero-Shot Transfer and Scaling of the Skill Library
- **LIBERO-Long**: Skills learned on LIBERO-90 transfer to held-out long-horizon tasks. As the skill library grows, the coding agent achieves higher success rates on LIBERO-Long.
- **Real Robot Cross-Embodiment Skill Transfer**: For each task, we compare real robot debugging with and without retrieving corresponding simulation-discovered skills from the ASPIRE skill library. Token count is measured up to the first successful real robot program. Success rate reports the performance of the code achieving first success on held-out evaluation trials. When equipped with ASPIRE skills, the coding agent reaches first success with fewer tokens, and the generated code achieves higher success rates. Output tokens (M), total tokens (M), held-out success rate (%).

### Limitations
- Not yet a fully autonomous real-world learner. Real-world deployment still requires robust success detection, safe resetting, safety monitoring, and calibration.
- Relies on a fixed frontier LLM. ASPIRE depends on a frontier model (Claude Opus 4.6); it has not been verified whether smaller or weaker LLMs can sustain the debugging loop.
- Constrained by predefined primitive APIs. The fixed set of perception, planning, and control primitives ensures safe debugging but limits expressible behaviors.
- Incomplete long-term memory management. The skill library currently prioritizes verified reusable fixes but does not fully address long-term memory management. As the skill library grows, some entries may become outdated, overly specific, redundant, or misleading for new tasks.
- Computationally intensive search loop. The debugging and evolutionary search loops require many LLM calls and rollouts per task, so scaling requires cheaper inference or more efficient search.

### Conclusion
We propose ASPIRE, a self-improving continual learning robot system that autonomously writes and optimizes robot control programs while accumulating experience into a reusable skill library. ASPIRE operates in an open-ended learning loop with three components: a closed-loop robot execution engine that exposes fine-grained multimodal trajectories, a continuously expanding skill library that distills verified repairs into transferable knowledge, and an evolutionary search program that explores diverse task sequences and control programs. On multiple benchmarks, ASPIRE achieves significant results.

## 개요

ASPIRE 시스템은 세 가지 핵심 구성 요소로 이루어져 있습니다: 폐쇄 루프 로봇 실행 엔진은 매번 인식, 계획, 파지 및 제어 호출 시 멀티모달 궤적을 기록하여 시스템이 장애를 식별하고 수정을 검증할 수 있게 합니다; 지속적으로 확장되는 스킬 라이브러리는 검증된 수정 사항을 모듈화되고 이전 가능한 로봇 지식으로 정제하여 향후 작업에서 검색할 수 있도록 합니다; 진화 검색 프로그램은 다양한 작업 시퀀스와 제어 프로그램을 생성하여 반복적 디버깅과 병렬 최적화를 통해 단일 궤적을 넘어선 자기 개선을 탐색합니다. LIBERO-PRO, Robosuite 및 BEHAVIOR-1K와 같은 벤치마크에서 ASPIRE는 작업 성공률을 크게 향상시켰으며, 예를 들어 양팔 인계 작업의 성공률을 20% 기준선에서 92%로 끌어올렸습니다.

## 핵심 내용
### 방법: ASPIRE의 작동 원리
ASPIRE는 실행 피드백을 통해 코드 형태의 로봇 제어 프로그램을 작성하고 최적화하는 자기 개선형 지속 학습 시스템입니다. 시스템은 실행 궤적을 검사하고, 장애를 진단하며, 프로그램을 수정하고, 수정된 동작을 검증한 후, 재사용 가능한 스킬을 스킬 라이브러리에 저장합니다. ASPIRE는 개방형 학습 루프에서 작동하며, 세 가지 핵심 구성 요소로 이루어져 있습니다:
- **폐쇄 루프 로봇 실행 엔진**: 매번 인식, 계획, 파지 및 제어 호출 시 엔진은 관찰 결과, 입력, 출력 및 가능한 시각적 증거를 기록합니다. 이러한 풍부한 멀티모달 궤적은 시스템이 선택적으로 주요 원시 로그를 검사하고, 단계적으로 장애를 식별하며, 재실행을 통해 수정을 검증할 수 있게 합니다.
- **지속적으로 확장되는 스킬 라이브러리**: ASPIRE는 계속 성장하는 스킬 라이브러리를 유지하며, 검증된 수정 사항을 모듈화되고 이전 가능한 로봇 지식으로 정제하여 향후 작업의 맥락 지침으로 검색할 수 있도록 합니다.
- **프로그램 진화 검색**: ASPIRE는 진화 검색 프로그램을 채택하여 다양한 작업 시퀀스와 제어 프로그램을 생성하고, 반복적 디버깅과 병렬 최적화를 통해 단일 궤적을 넘어선 자기 개선을 탐색합니다.

### 벤치마크 결과
모든 벤치마크에서 각 작업 인스턴스는 환경 시드를 사용하여 고정되며, 여기에는 물체 자세, 방해물 및 초기 로봇/물체 상태가 포함됩니다. ASPIRE는 분리된 디버깅 시드와 평가 시드를 사용합니다: ASPIRE는 작은 디버깅 세트에서 학습한 후 더 큰 보류 평가 시드에서 성공률을 보고하며, 각 LIBERO-Pro/Robosuite 작업에 대해 하나의 프로그램을 생성합니다; 반면 CaP-Agent0는 테스트 시간 추론과 재시도를 통해 각 시드에 대해 별도의 프로그램을 다시 생성합니다. BEHAVIOR-1K 평가의 경우, ASPIRE는 증분 블록 실행을 사용하여 현재 멀티모달 궤적에서 다음 코드 블록을 생성합니다.
- **LIBERO-PRO**: ASPIRE가 작성한 제어 프로그램은 다양한 물체 유형, 물체 위치 및 작업 세부 사항에 일반화될 수 있습니다.
- **Robosuite**: ASPIRE는 접촉이 많은 데스크탑 조작 작업을 처리합니다. 가장 주목할 만한 점은 반복적 디버깅을 통해 ASPIRE가 양팔 인계 작업의 성공률을 20% 기준선에서 92%로 향상시켰다는 것입니다.
- **BEHAVIOR-1K**: 장시간 이동 조작의 경우, 탐색과 작업 완료가 별도로 보고됩니다.

### 스킬 라이브러리의 제로샷 전이 및 규모 확장
- **LIBERO-Long**: LIBERO-90에서 학습된 스킬은 보류된 장시간 작업으로 전이될 수 있습니다. 스킬 라이브러리가 성장함에 따라 코딩 에이전트는 LIBERO-Long에서 더 높은 성공률을 달성합니다.
- **실제 로봇 간 스킬 전이**: 각 작업에 대해, ASPIRE 스킬 라이브러리에서 해당 시뮬레이션 발견 스킬을 검색한 경우와 그렇지 않은 경우의 실제 로봇 디버깅을 비교합니다. 토큰 수는 첫 번째 성공적인 실제 로봇 프로그램까지 측정됩니다. 성공률은 첫 번째 성공을 달성한 코드가 보류 평가 시험에서 보인 성과를 보고합니다. ASPIRE 스킬을 갖추었을 때, 코딩 에이전트는 더 적은 토큰으로 첫 번째 성공에 도달했으며, 생성된 코드는 더 높은 성공률을 달성했습니다. 출력 토큰(M), 총 토큰(M), 보류 성공률(%).

### 한계점
- 아직 완전 자율적인 실제 세계 학습자가 아님. 실제 세계 배포는 여전히 견고한 성공 감지, 안전 리셋, 안전 모니터링 및 보정이 필요함.
- 고정된 최첨단 LLM에 의존함. ASPIRE는 최첨단 모델(Claude Opus 4.6)에 의존하며, 더 작거나 약한 LLM이 디버깅 루프를 유지할 수 있는지는 아직 검증되지 않음.
- 미리 정의된 원시 API에 제한됨. 고정된 인식, 계획 및 제어 기본 요소 집합은 디버깅의 안전성을 보장하지만, 표현 가능한 동작을 제한함.
- 불완전한 장기 기억 관리. 스킬 라이브러리는 현재 검증된 재사용 가능한 수정 사항을 우선시하지만, 장기 기억 관리 문제를 완전히 해결하지는 못함. 스킬 라이브러리가 성장함에 따라 일부 항목은 구식이 되거나, 너무 구체적이거나, 중복되거나, 새로운 작업에 오해를 줄 수 있음.
- 계산 집약적인 검색 루프. 디버깅 및 진화 검색 루프는 각 작업에 대해 많은 LLM 호출과 롤아웃이 필요하므로, 확장을 위해서는 더 저렴한 추론 또는 더 효율적인 검색이 필요함.

### 결론
우리는 ASPIRE를 제안합니다. 이는 자율적으로 로봇 제어 프로그램을 작성하고 최적화하면서 경험을 재사용 가능한 스킬 라이브러리에 축적하는 자기 개선형 지속 학습 로봇 시스템입니다. ASPIRE는 개방형 학습 루프에서 작동하며, 세 가지 구성 요소로 이루어져 있습니다: 세분화된 멀티모달 궤적을 노출하는 폐쇄 루프 로봇 실행 엔진, 검증된 수정 사항을 이전 가능한 지식으로 정제하는 지속적으로 확장되는 스킬 라이브러리, 그리고 다양한 작업 시퀀스와 제어 프로그램을 탐색하는 진화 검색 프로그램입니다. 여러 벤치마크에서 ASPIRE는 주목할 만한 결과를 달성했습니다.
