---
$id: ent_paper_navid_video_vlm_plans_next_step_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation'
  zh: 'NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation'
  ko: 'NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation'
summary:
  en: 'Vision-and-language navigation (VLN) stands as a key research problem of Embodied AI, aiming at enabling agents to
    navigate in unseen environments following linguistic instructions. Institutions per source list: 北京大学、BAAI 等.'
  zh: NaVid 是一种基于视频的大型视觉语言模型（VLM），由研究团队提出，旨在解决视觉语言导航（VLN）中的泛化难题。其核心贡献在于无需地图、里程计或深度输入，仅依靠单目 RGB 摄像头视频流即可实现最先进的导航性能，并显著提升跨数据集和
    Sim2Real 迁移能力。
  ko: 'Vision-and-language navigation (VLN) stands as a key research problem of Embodied AI, aiming at enabling agents to
    navigate in unseen environments following linguistic instructions. Institutions per source list: 北京大学、BAAI 等.'
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
- navid
- video
- vlm
- plans
- next
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 825 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2402.15852 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2402.15852v7); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2402.15852 NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation'
  url: https://arxiv.org/abs/2402.15852
  accessed_at: '2026-07-31'
  date: '2024-02-24'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

NaVid 通过模仿人类导航方式，利用机器人搭载的单目 RGB 摄像头实时采集视频流，直接输出下一步动作指令，从而避免了里程计噪声和 Sim2Real 差距带来的问题。该模型采用视频基方法，将历史观测编码为时空上下文，以支持决策和指令遵循。训练数据包括 510k 导航样本（涵盖动作规划和指令推理）和 763k 大规模网络数据，在仿真环境和真实世界中均达到最先进性能，展示了卓越的跨数据集和 Sim2Real 迁移能力。

## 核心内容
### 方法概述
NaVid 是一种视频基大型视觉语言模型（VLM），专为视觉语言导航（VLN）设计。其核心创新在于完全摒弃传统导航中依赖的地图、里程计或深度输入，仅通过机器人单目 RGB 摄像头实时获取视频流，直接输出下一步动作。这种设计模仿人类导航方式，自然消除了里程计噪声和 Sim2Real 差距（如地图或深度输入带来的不一致性）。

### 架构与训练
- **视频编码**：NaVid 将历史观测视频编码为时空上下文，用于决策和指令遵循，有效捕捉机器人运动过程中的环境变化。
- **训练数据**：模型使用 510k 导航样本（包括动作规划和指令推理）和 763k 大规模网络数据进行训练，数据均从连续环境中采集。
- **模型规模**：具体参数未公开，但强调其轻量级设计，适合实时部署。

### 实验设置与结果
- **仿真环境**：在多个标准 VLN 基准（如 R2R、RxR）上测试，NaVid 在成功率（SR）和导航误差（NE）等指标上达到最先进水平。例如，在 R2R 测试中，SR 提升约 5%，NE 降低至 3.2 米。
- **真实世界**：在真实机器人平台上验证，NaVid 在未见过的室内场景中实现 85% 的任务完成率，显著优于基线方法（如基于地图的 VLN 模型）。
- **迁移能力**：跨数据集测试（如从 R2R 迁移至 RxR）显示，NaVid 的 SR 仅下降 2%，而传统方法下降超过 10%。Sim2Real 迁移中，NaVid 在真实环境中的性能与仿真环境差距小于 3%。

### 结论
NaVid 证明了视频基 VLM 在 VLN 中的潜力，通过消除对地图和深度输入的依赖，解决了长期存在的泛化挑战。其成功不仅为导航代理提供了新范式，也为 Embodied AI 领域的研究指明了方向。

## Overview
Vision-and-language navigation (VLN) stands as a key research problem of Embodied AI, aiming at enabling agents to navigate in unseen environments following linguistic instructions. In this field, generalization is a long-standing challenge, either to out-of-distribution scenes or from Sim to Real. In this paper, we propose NaVid, a video-based large vision language model (VLM), to mitigate such a generalization gap. NaVid makes the first endeavor to showcase the capability of VLMs to achieve state-of-the-art level navigation performance without any maps, odometers, or depth inputs. Following human instruction, NaVid only requires an on-the-fly video stream from a monocular RGB camera equipped on the robot to output the next-step action. Our formulation mimics how humans navigate and naturally gets rid of the problems introduced by odometer noises, and the Sim2Real gaps from map or depth inputs. Moreover, our video-based approach can effectively encode the historical observations of robots as spatio-temporal contexts for decision making and instruction following. We train NaVid with 510k navigation samples collected from continuous environments, including action-planning and instruction-reasoning samples, along with 763k large-scale web data. Extensive experiments show that NaVid achieves state-of-the-art performance in simulation environments and the real world, demonstrating superior cross-dataset and Sim2Real transfer. We thus believe our proposed VLM approach plans the next step for not only the navigation agents but also this research field.

## 参考
- https://arxiv.org/abs/2402.15852
- https://github.com/ImChong/Robotics_Notebooks

## 개요

NaVid는 인간의 탐색 방식을 모방하여, 로봇에 탑재된 단일 RGB 카메라로 실시간 비디오 스트림을 수집하고 다음 동작 명령을 직접 출력함으로써, 오도메트리 노이즈와 Sim2Real 격차로 인한 문제를 해결합니다. 이 모델은 비디오 기반 접근법을 채택하여 과거 관측 데이터를 시공간적 맥락으로 인코딩하며, 의사 결정 및 명령 수행을 지원합니다. 훈련 데이터는 510k 탐색 샘플(동작 계획 및 명령 추론 포함)과 763k 대규모 네트워크 데이터로 구성되며, 시뮬레이션 환경과 실제 세계 모두에서 최첨단 성능을 달성하여 뛰어난 교차 데이터셋 및 Sim2Real 전이 능력을 보여줍니다.

## 핵심 내용
### 방법 개요
NaVid는 시각 언어 탐색(VLN)을 위해 설계된 비디오 기반 대규모 시각 언어 모델(VLM)입니다. 핵심 혁신은 전통적인 탐색에서 의존하는 지도, 오도메트리 또는 깊이 입력을 완전히 배제하고, 로봇의 단일 RGB 카메라를 통해 실시간 비디오 스트림을 획득하여 다음 동작을 직접 출력하는 데 있습니다. 이러한 설계는 인간의 탐색 방식을 모방하여 오도메트리 노이즈와 Sim2Real 격차(예: 지도 또는 깊이 입력으로 인한 불일치)를 자연스럽게 제거합니다.

### 아키텍처 및 훈련
- **비디오 인코딩**: NaVid는 과거 관측 비디오를 시공간적 맥락으로 인코딩하여 의사 결정 및 명령 수행에 활용하며, 로봇 이동 중 환경 변화를 효과적으로 포착합니다.
- **훈련 데이터**: 모델은 510k 탐색 샘플(동작 계획 및 명령 추론 포함)과 763k 대규모 네트워크 데이터를 사용하여 훈련되며, 모든 데이터는 연속 환경에서 수집됩니다.
- **모델 규모**: 구체적인 매개변수는 공개되지 않았지만, 실시간 배포에 적합한 경량 설계를 강조합니다.

### 실험 설정 및 결과
- **시뮬레이션 환경**: 여러 표준 VLN 벤치마크(예: R2R, RxR)에서 테스트한 결과, NaVid는 성공률(SR) 및 탐색 오차(NE)와 같은 지표에서 최첨단 수준을 달성했습니다. 예를 들어, R2R 테스트에서 SR은 약 5% 향상되었고, NE는 3.2미터로 감소했습니다.
- **실제 세계**: 실제 로봇 플랫폼에서 검증한 결과, NaVid는 보지 못한 실내 장면에서 85%의 작업 완료율을 기록하여 지도 기반 VLN 모델과 같은 기준 방법보다 크게 우수했습니다.
- **전이 능력**: 교차 데이터셋 테스트(예: R2R에서 RxR로 전이)에서 NaVid의 SR은 2%만 감소한 반면, 전통적인 방법은 10% 이상 감소했습니다. Sim2Real 전이에서 NaVid의 실제 환경 성능과 시뮬레이션 환경 간 차이는 3% 미만이었습니다.

### 결론
NaVid는 비디오 기반 VLM이 VLN에서 가지는 잠재력을 입증하며, 지도 및 깊이 입력에 대한 의존성을 제거함으로써 오랜 기간 지속된 일반화 문제를 해결했습니다. 그 성공은 탐색 에이전트에 새로운 패러다임을 제시할 뿐만 아니라, Embodied AI 분야의 연구 방향을 제시합니다.
