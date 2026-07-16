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
  zh: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots is a 2026 work on manipulation
    for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.05493v2.
sources:
- id: src_001
  type: paper
  title: 'cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots (arXiv)'
  url: https://arxiv.org/abs/2603.05493
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Effective robot autonomy requires motion generation that is safe, feasible, and reactive. Current methods are fragmented: fast planners output physically unexecutable trajectories, reactive controllers struggle with high-fidelity perception, and existing solvers fail on high-DoF systems. We present cuRoboV2, a unified framework with three key innovations: (1) B-spline trajectory optimization that enforces smoothness and torque limits; (2) a GPU-native TSDF/ESDF perception pipeline that generates dense signed distance fields covering the full workspace, unlike existing methods that only provide distances within sparsely allocated blocks, up to 10x faster and in 8x less memory than the state-of-the-art at manipulation scale, with up to 99% collision recall; and (3) scalable GPU-native whole-body computation, namely topology-aware kinematics, differentiable inverse dynamics, and map-reduce self-collision, that achieves up to 61x speedup while also extending to high-DoF humanoids (where previous GPU implementations fail). On benchmarks, cuRoboV2 achieves 99.7% success under 3kg payload (where baselines achieve only 72--77%), 99.6% collision-free IK on a 48-DoF humanoid (where prior methods fail entirely), and 89.5% retargeting constraint satisfaction (vs. 61% for PyRoki); these collision-free motions yield locomotion policies with 21% lower tracking error than PyRoki and 12x lower cross-seed variance than GMR. A ground-up codebase redesign for discoverability enabled LLM coding assistants to author up to 73% of new modules, including hand-optimized CUDA kernels, demonstrating that well-structured robotics code can unlock productive human-LLM collaboration. Together, these advances provide a unified, dynamics-aware motion generation stack that scales from single-arm manipulators to full humanoids. Code is available at https://github.com/NVlabs/curobo.

## 核心内容
Effective robot autonomy requires motion generation that is safe, feasible, and reactive. Current methods are fragmented: fast planners output physically unexecutable trajectories, reactive controllers struggle with high-fidelity perception, and existing solvers fail on high-DoF systems. We present cuRoboV2, a unified framework with three key innovations: (1) B-spline trajectory optimization that enforces smoothness and torque limits; (2) a GPU-native TSDF/ESDF perception pipeline that generates dense signed distance fields covering the full workspace, unlike existing methods that only provide distances within sparsely allocated blocks, up to 10x faster and in 8x less memory than the state-of-the-art at manipulation scale, with up to 99% collision recall; and (3) scalable GPU-native whole-body computation, namely topology-aware kinematics, differentiable inverse dynamics, and map-reduce self-collision, that achieves up to 61x speedup while also extending to high-DoF humanoids (where previous GPU implementations fail). On benchmarks, cuRoboV2 achieves 99.7% success under 3kg payload (where baselines achieve only 72--77%), 99.6% collision-free IK on a 48-DoF humanoid (where prior methods fail entirely), and 89.5% retargeting constraint satisfaction (vs. 61% for PyRoki); these collision-free motions yield locomotion policies with 21% lower tracking error than PyRoki and 12x lower cross-seed variance than GMR. A ground-up codebase redesign for discoverability enabled LLM coding assistants to author up to 73% of new modules, including hand-optimized CUDA kernels, demonstrating that well-structured robotics code can unlock productive human-LLM collaboration. Together, these advances provide a unified, dynamics-aware motion generation stack that scales from single-arm manipulators to full humanoids. Code is available at https://github.com/NVlabs/curobo.

## 参考
- http://arxiv.org/abs/2603.05493v2

## Overview
Effective robot autonomy requires motion generation that is safe, feasible, and reactive. Current methods are fragmented: fast planners output physically unexecutable trajectories, reactive controllers struggle with high-fidelity perception, and existing solvers fail on high-DoF systems. We present cuRoboV2, a unified framework with three key innovations: (1) B-spline trajectory optimization that enforces smoothness and torque limits; (2) a GPU-native TSDF/ESDF perception pipeline that generates dense signed distance fields covering the full workspace, unlike existing methods that only provide distances within sparsely allocated blocks, up to 10x faster and in 8x less memory than the state-of-the-art at manipulation scale, with up to 99% collision recall; and (3) scalable GPU-native whole-body computation, namely topology-aware kinematics, differentiable inverse dynamics, and map-reduce self-collision, that achieves up to 61x speedup while also extending to high-DoF humanoids (where previous GPU implementations fail). On benchmarks, cuRoboV2 achieves 99.7% success under 3kg payload (where baselines achieve only 72--77%), 99.6% collision-free IK on a 48-DoF humanoid (where prior methods fail entirely), and 89.5% retargeting constraint satisfaction (vs. 61% for PyRoki); these collision-free motions yield locomotion policies with 21% lower tracking error than PyRoki and 12x lower cross-seed variance than GMR. A ground-up codebase redesign for discoverability enabled LLM coding assistants to author up to 73% of new modules, including hand-optimized CUDA kernels, demonstrating that well-structured robotics code can unlock productive human-LLM collaboration. Together, these advances provide a unified, dynamics-aware motion generation stack that scales from single-arm manipulators to full humanoids. Code is available at https://github.com/NVlabs/curobo.

## Content
Effective robot autonomy requires motion generation that is safe, feasible, and reactive. Current methods are fragmented: fast planners output physically unexecutable trajectories, reactive controllers struggle with high-fidelity perception, and existing solvers fail on high-DoF systems. We present cuRoboV2, a unified framework with three key innovations: (1) B-spline trajectory optimization that enforces smoothness and torque limits; (2) a GPU-native TSDF/ESDF perception pipeline that generates dense signed distance fields covering the full workspace, unlike existing methods that only provide distances within sparsely allocated blocks, up to 10x faster and in 8x less memory than the state-of-the-art at manipulation scale, with up to 99% collision recall; and (3) scalable GPU-native whole-body computation, namely topology-aware kinematics, differentiable inverse dynamics, and map-reduce self-collision, that achieves up to 61x speedup while also extending to high-DoF humanoids (where previous GPU implementations fail). On benchmarks, cuRoboV2 achieves 99.7% success under 3kg payload (where baselines achieve only 72--77%), 99.6% collision-free IK on a 48-DoF humanoid (where prior methods fail entirely), and 89.5% retargeting constraint satisfaction (vs. 61% for PyRoki); these collision-free motions yield locomotion policies with 21% lower tracking error than PyRoki and 12x lower cross-seed variance than GMR. A ground-up codebase redesign for discoverability enabled LLM coding assistants to author up to 73% of new modules, including hand-optimized CUDA kernels, demonstrating that well-structured robotics code can unlock productive human-LLM collaboration. Together, these advances provide a unified, dynamics-aware motion generation stack that scales from single-arm manipulators to full humanoids. Code is available at https://github.com/NVlabs/curobo.

## 개요
효과적인 로봇 자율성은 안전하고 실행 가능하며 반응적인 모션 생성을 필요로 합니다. 현재 방법들은 분산되어 있습니다: 빠른 플래너는 물리적으로 실행 불가능한 궤적을 출력하고, 반응형 제어기는 고충실도 인식에 어려움을 겪으며, 기존 솔버는 고자유도(high-DoF) 시스템에서 실패합니다. 우리는 세 가지 핵심 혁신을 갖춘 통합 프레임워크인 cuRoboV2를 제시합니다: (1) 평활성과 토크 제한을 강제하는 B-스플라인 궤적 최적화; (2) 희소 할당 블록 내에서만 거리를 제공하는 기존 방법과 달리 전체 작업 공간을 포괄하는 조밀한 부호 거리 필드를 생성하는 GPU 네이티브 TSDF/ESDF 인식 파이프라인으로, 조작 규모에서 최첨단 기술보다 최대 10배 빠르고 8배 적은 메모리를 사용하며 최대 99%의 충돌 재현율을 달성; (3) 확장 가능한 GPU 네이티브 전신 계산, 즉 토폴로지 인식 운동학, 미분 가능 역동역학, 맵-리듀스 자체 충돌로, 최대 61배 속도 향상을 달성하면서 이전 GPU 구현이 실패하는 고자유도 휴머노이드로 확장됩니다. 벤치마크에서 cuRoboV2는 3kg 페이로드 하에서 99.7%의 성공률(기준 방법은 72~77%만 달성), 48-DoF 휴머노이드에서 99.6%의 충돌 없는 역운동학(IK)(이전 방법은 완전히 실패), 89.5%의 리타겟팅 제약 조건 충족(PyRoki의 61% 대비)을 달성합니다; 이러한 충돌 없는 모션은 PyRoki보다 21% 낮은 추적 오차와 GMR보다 12배 낮은 교차 시드 분산을 가진 보행 정책을 생성합니다. 발견 가능성을 위한 근본적인 코드베이스 재설계로 LLM 코딩 어시스턴트가 수동 최적화된 CUDA 커널을 포함한 새 모듈의 최대 73%를 작성할 수 있게 되어, 잘 구조화된 로봇공학 코드가 생산적인 인간-LLM 협업을 가능하게 함을 입증했습니다. 이러한 발전은 단일 암 매니퓰레이터에서 전체 휴머노이드까지 확장되는 통합된 동역학 인식 모션 생성 스택을 제공합니다. 코드는 https://github.com/NVlabs/curobo에서 확인할 수 있습니다.

## 핵심 내용
효과적인 로봇 자율성은 안전하고 실행 가능하며 반응적인 모션 생성을 필요로 합니다. 현재 방법들은 분산되어 있습니다: 빠른 플래너는 물리적으로 실행 불가능한 궤적을 출력하고, 반응형 제어기는 고충실도 인식에 어려움을 겪으며, 기존 솔버는 고자유도(high-DoF) 시스템에서 실패합니다. 우리는 세 가지 핵심 혁신을 갖춘 통합 프레임워크인 cuRoboV2를 제시합니다: (1) 평활성과 토크 제한을 강제하는 B-스플라인 궤적 최적화; (2) 희소 할당 블록 내에서만 거리를 제공하는 기존 방법과 달리 전체 작업 공간을 포괄하는 조밀한 부호 거리 필드를 생성하는 GPU 네이티브 TSDF/ESDF 인식 파이프라인으로, 조작 규모에서 최첨단 기술보다 최대 10배 빠르고 8배 적은 메모리를 사용하며 최대 99%의 충돌 재현율을 달성; (3) 확장 가능한 GPU 네이티브 전신 계산, 즉 토폴로지 인식 운동학, 미분 가능 역동역학, 맵-리듀스 자체 충돌로, 최대 61배 속도 향상을 달성하면서 이전 GPU 구현이 실패하는 고자유도 휴머노이드로 확장됩니다. 벤치마크에서 cuRoboV2는 3kg 페이로드 하에서 99.7%의 성공률(기준 방법은 72~77%만 달성), 48-DoF 휴머노이드에서 99.6%의 충돌 없는 역운동학(IK)(이전 방법은 완전히 실패), 89.5%의 리타겟팅 제약 조건 충족(PyRoki의 61% 대비)을 달성합니다; 이러한 충돌 없는 모션은 PyRoki보다 21% 낮은 추적 오차와 GMR보다 12배 낮은 교차 시드 분산을 가진 보행 정책을 생성합니다. 발견 가능성을 위한 근본적인 코드베이스 재설계로 LLM 코딩 어시스턴트가 수동 최적화된 CUDA 커널을 포함한 새 모듈의 최대 73%를 작성할 수 있게 되어, 잘 구조화된 로봇공학 코드가 생산적인 인간-LLM 협업을 가능하게 함을 입증했습니다. 이러한 발전은 단일 암 매니퓰레이터에서 전체 휴머노이드까지 확장되는 통합된 동역학 인식 모션 생성 스택을 제공합니다. 코드는 https://github.com/NVlabs/curobo에서 확인할 수 있습니다.
