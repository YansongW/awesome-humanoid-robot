---
$id: ent_paper_curobov2_dynamics_aware_motion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots'
  zh: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots'
  ko: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots'
summary:
  en: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots is a 2026 work on manipulation
    for humanoid robots.'
  zh: cuRoboV2 是 NVIDIA 在 2026 年提出的统一运动生成框架，专为高自由度机器人（包括人形机器人）设计。其核心贡献包括：基于 B 样条的轨迹优化、GPU 原生 TSDF/ESDF 感知管线（速度提升 10 倍、内存减少
    8 倍），以及可扩展的全身计算（最高 61 倍加速），在 48-DoF 人形机器人上实现了 99.6% 的无碰撞逆运动学成功率。
  ko: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots is a 2026 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- curobov2
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.05493v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1092 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots (arXiv)'
  url: https://arxiv.org/abs/2603.05493
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
cuRoboV2 解决了现有运动生成方法碎片化的问题：快速规划器输出不可执行的轨迹，反应式控制器难以处理高保真感知，而现有求解器在高自由度系统上失效。该框架通过三项关键创新实现统一：B 样条轨迹优化确保平滑性与力矩约束；GPU 原生 TSDF/ESDF 感知管线生成覆盖完整工作空间的密集有符号距离场，相比仅提供稀疏块距离的现有方法，在操作尺度上速度提升 10 倍、内存减少 8 倍，碰撞召回率达 99%；可扩展的 GPU 原生全身计算（包括拓扑感知运动学、可微逆动力学和 map-reduce 自碰撞检测）实现最高 61 倍加速，并扩展至先前 GPU 实现失败的高自由度人形机器人。

## 核心内容
### 方法架构
cuRoboV2 是一个统一的运动生成框架，包含三个核心模块：
- **B 样条轨迹优化**：通过 B 样条参数化轨迹，显式强制平滑性并满足力矩限制，确保生成轨迹物理可执行。
- **GPU 原生 TSDF/ESDF 感知管线**：生成覆盖完整工作空间的密集有符号距离场，而非现有方法仅提供的稀疏分配块距离。在操作尺度上，该管线比现有最优方法快 10 倍，内存占用减少 8 倍，碰撞召回率高达 99%。
- **可扩展 GPU 原生全身计算**：包括拓扑感知运动学、可微逆动力学和 map-reduce 自碰撞检测，实现最高 61 倍加速，并成功扩展至 48-DoF 人形机器人（先前 GPU 实现在此场景下失败）。

### 实验设置与关键数字
- **负载测试**：在 3kg 负载下，cuRoboV2 达到 99.7% 的成功率，而基线方法仅 72–77%。
- **无碰撞逆运动学**：在 48-DoF 人形机器人上，cuRoboV2 实现 99.6% 的无碰撞逆运动学成功率，先前方法完全失败。
- **重定向约束满足**：cuRoboV2 达到 89.5%，而 PyRoki 仅 61%。
- **运动策略跟踪误差**：cuRoboV2 生成的无碰撞运动使运动策略的跟踪误差比 PyRoki 低 21%，跨种子方差比 GMR 低 12 倍。

### 代码与协作
- 代码库经过重新设计以提高可发现性，使 LLM 编码助手能够自主编写高达 73% 的新模块，包括手调优化的 CUDA 内核。
- 这表明结构良好的机器人代码能够实现高效的人机协作。

### 结论
cuRoboV2 提供了一个统一的、动力学感知的运动生成栈，可从单臂操作器扩展到完整人形机器人，代码开源在 https://github.com/NVlabs/curobo。

## Overview
Effective robot autonomy requires motion generation that is safe, feasible, and reactive. Current methods are fragmented: fast planners output physically unexecutable trajectories, reactive controllers struggle with high-fidelity perception, and existing solvers fail on high-DoF systems. We present cuRoboV2, a unified framework with three key innovations: (1) B-spline trajectory optimization that enforces smoothness and torque limits; (2) a GPU-native TSDF/ESDF perception pipeline that generates dense signed distance fields covering the full workspace, unlike existing methods that only provide distances within sparsely allocated blocks, up to 10x faster and in 8x less memory than the state-of-the-art at manipulation scale, with up to 99% collision recall; and (3) scalable GPU-native whole-body computation, namely topology-aware kinematics, differentiable inverse dynamics, and map-reduce self-collision, that achieves up to 61x speedup while also extending to high-DoF humanoids (where previous GPU implementations fail). On benchmarks, cuRoboV2 achieves 99.7% success under 3kg payload (where baselines achieve only 72--77%), 99.6% collision-free IK on a 48-DoF humanoid (where prior methods fail entirely), and 89.5% retargeting constraint satisfaction (vs. 61% for PyRoki); these collision-free motions yield locomotion policies with 21% lower tracking error than PyRoki and 12x lower cross-seed variance than GMR. A ground-up codebase redesign for discoverability enabled LLM coding assistants to author up to 73% of new modules, including hand-optimized CUDA kernels, demonstrating that well-structured robotics code can unlock productive human-LLM collaboration. Together, these advances provide a unified, dynamics-aware motion generation stack that scales from single-arm manipulators to full humanoids. Code is available at https://github.com/NVlabs/curobo.

## 参考
- http://arxiv.org/abs/2603.05493v2

## 개요
cuRoboV2는 기존 운동 생성 방법의 분절화 문제를 해결합니다: 빠른 플래너는 실행 불가능한 궤적을 출력하고, 반응형 컨트롤러는 고충실도 인식을 처리하기 어려우며, 기존 솔버는 고자유도 시스템에서 실패합니다. 이 프레임워크는 세 가지 핵심 혁신을 통해 통합을 달성합니다: B-스플라인 궤적 최적화는 매끄러움과 토크 제약을 보장합니다; GPU 네이티브 TSDF/ESDF 인식 파이프라인은 전체 작업 공간을 덮는 밀집 부호 거리 필드를 생성하며, 희소 블록 거리만 제공하는 기존 방법에 비해 조작 규모에서 속도가 10배 빠르고 메모리가 8배 적으며 충돌 재현율이 99%에 달합니다; 확장 가능한 GPU 네이티브 전신 계산(토폴로지 인식 운동학, 미분 가능 역운동학, map-reduce 자체 충돌 감지 포함)은 최대 61배 가속을 실현하고, 이전 GPU 구현이 실패한 고자유도 휴머노이드 로봇으로 확장됩니다.

## 핵심 내용
### 방법 아키텍처
cuRoboV2는 세 가지 핵심 모듈을 포함하는 통합 운동 생성 프레임워크입니다:
- **B-스플라인 궤적 최적화**: B-스플라인으로 궤적을 매개변수화하여 매끄러움을 명시적으로 강제하고 토크 제한을 충족시켜 생성된 궤적이 물리적으로 실행 가능하도록 보장합니다.
- **GPU 네이티브 TSDF/ESDF 인식 파이프라인**: 기존 방법이 제공하는 희소 할당 블록 거리 대신 전체 작업 공간을 덮는 밀집 부호 거리 필드를 생성합니다. 조작 규모에서 이 파이프라인은 기존 최적 방법보다 10배 빠르고 메모리 사용량이 8배 적으며 충돌 재현율이 최대 99%입니다.
- **확장 가능한 GPU 네이티브 전신 계산**: 토폴로지 인식 운동학, 미분 가능 역운동학, map-reduce 자체 충돌 감지를 포함하며, 최대 61배 가속을 실현하고 48-DoF 휴머노이드 로봇(이전 GPU 구현이 실패한 시나리오)으로 성공적으로 확장됩니다.

### 실험 설정 및 핵심 수치
- **부하 테스트**: 3kg 부하에서 cuRoboV2는 99.7%의 성공률을 달성하는 반면, 기준 방법은 72–77%에 불과합니다.
- **충돌 없는 역운동학**: 48-DoF 휴머노이드 로봇에서 cuRoboV2는 99.6%의 충돌 없는 역운동학 성공률을 구현하며, 이전 방법은 완전히 실패했습니다.
- **리타게팅 제약 충족**: cuRoboV2는 89.5%를 달성하는 반면, PyRoki는 61%에 불과합니다.
- **운동 정책 추적 오차**: cuRoboV2가 생성한 충돌 없는 운동은 운동 정책의 추적 오차를 PyRoki보다 21% 낮추고, 시드 간 분산은 GMR보다 12배 낮춥니다.

### 코드 및 협업
- 코드베이스는 발견 가능성을 높이기 위해 재설계되어, LLM 코딩 어시스턴트가 수동 튜닝된 CUDA 커널을 포함한 신규 모듈의 최대 73%를 자율적으로 작성할 수 있습니다.
- 이는 구조화된 로봇 코드가 효율적인 인간-기계 협업을 가능하게 함을 시사합니다.

### 결론
cuRoboV2는 단일 암 조작기에서 전체 휴머노이드 로봇으로 확장 가능한 통합적이고 역학 인식적인 운동 생성 스택을 제공하며, 코드는 https://github.com/NVlabs/curobo 에서 오픈소스로 공개되어 있습니다.
