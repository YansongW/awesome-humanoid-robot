---
$id: ent_paper_jia_video2act_a_dual_system_video_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling'
  zh: Video2Act
  ko: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling'
summary:
  en: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
  zh: Video2Act 是由北京大学、中山大学、武汉大学、香港科技大学及 AI2Robotics 联合提出的 2025 年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过显式整合视频扩散模型中的空间与运动感知表示，并采用异步双系统设计（慢速
    System 2 与快速 System 1），高效引导机器人动作学习。在仿真和真实世界任务中，平均成功率分别超越先前最先进方法 7.7% 和 21.7%。
  ko: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (Video2Act), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Sun Yat-sen University, Wuhan University, Hong Kong University
    of Science and Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- video2act
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03044v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1103 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.03044
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Video2Act source
  url: https://doi.org/10.48550/arXiv.2512.03044
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Video2Act 框架旨在解决现有视频扩散模型在机器人策略学习中忽略帧间连贯且物理一致的运动表示的问题。该方法从视频扩散模型中提取前景边界和帧间运动变化，同时过滤背景噪声与任务无关偏差，将这些精炼表示作为扩散 Transformer 动作头的额外条件输入，使其能推理“操作什么”和“如何移动”。为缓解推理效率低下，Video2Act 采用异步双系统设计：视频扩散模型作为慢速 System 2，扩散 Transformer 头作为快速 System 1，两者协同生成自适应动作。即使 System 2 低频更新，System 1 也能通过运动感知条件维持稳定操作。实验表明，Video2Act 在仿真和真实世界任务中均显著超越先前最先进的视觉-语言-动作方法，并展现出强大的泛化能力。

## 核心内容
### 方法架构
Video2Act 的核心创新在于显式整合视频扩散模型（VDM）中固有的空间与运动表示。具体而言：
- **表示提取**：从 VDM 中提取前景边界（空间信息）和帧间运动变化（运动信息），同时过滤背景噪声与任务无关偏差。
- **条件注入**：将精炼后的空间-运动表示作为额外条件输入到扩散 Transformer（DiT）动作头中，使其能同时推理“操作什么”（空间目标）和“如何移动”（运动模式）。
- **异步双系统设计**：
  - **System 2（慢速）**：VDM 负责低频更新，提供全局物理一致的运动表示。
  - **System 1（快速）**：DiT 动作头负责高频推理，基于 System 2 提供的运动感知条件生成实时动作。
  - 这种设计使 System 1 即使在 System 2 更新频率较低时也能保持稳定操作，显著提升推理效率。

### 实验设置与关键结果
- **仿真环境**：在多个标准机器人操作基准上测试，Video2Act 的平均成功率比先前最先进的 VLA 方法高出 **7.7%**。
- **真实世界任务**：在真实机器人平台上，平均成功率提升 **21.7%**，进一步验证了方法的实际有效性。
- **泛化能力**：实验表明，Video2Act 在未见过的物体、场景和任务配置下均表现出强大的泛化能力，这得益于其显式的运动感知建模。

### 结论
Video2Act 通过显式整合视频扩散模型中的空间与运动表示，并采用异步双系统设计，有效解决了现有方法在机器人策略学习中忽略帧间运动一致性的问题。其不仅在仿真和真实世界任务中显著超越先前方法，还展现出优异的泛化性能，为机器人操作中的物理世界建模提供了新思路。

## Overview
Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

## 参考
- http://arxiv.org/abs/2512.03044v3

## 개요
Video2Act 프레임워크는 기존 비디오 확산 모델이 로봇 정책 학습에서 프레임 간 일관성과 물리적으로 일관된 운동 표현을 무시하는 문제를 해결하는 것을 목표로 한다. 이 방법은 비디오 확산 모델에서 전경 경계와 프레임 간 운동 변화를 추출하고, 배경 노이즈와 작업 무관 편향을 필터링하여, 이러한 정제된 표현을 확산 Transformer 동작 헤드의 추가 조건 입력으로 사용하여 "무엇을 조작할지"와 "어떻게 움직일지"를 추론할 수 있게 한다. 추론 효율성 저하를 완화하기 위해 Video2Act는 비동기 이중 시스템 설계를 채택한다: 비디오 확산 모델은 느린 System 2로, 확산 Transformer 헤드는 빠른 System 1으로, 둘은 협력하여 적응형 동작을 생성한다. System 2가 저주파로 업데이트되더라도 System 1은 운동 인식 조건을 통해 안정적인 조작을 유지할 수 있다. 실험 결과, Video2Act는 시뮬레이션 및 실제 세계 작업에서 이전 최첨단 비전-언어-동작 방법을 크게 능가하며 강력한 일반화 능력을 보여준다.

## 핵심 내용
### 방법 아키텍처
Video2Act의 핵심 혁신은 비디오 확산 모델(VDM)에 내재된 공간 및 운동 표현을 명시적으로 통합하는 것이다. 구체적으로:
- **표현 추출**: VDM에서 전경 경계(공간 정보)와 프레임 간 운동 변화(운동 정보)를 추출하고, 배경 노이즈와 작업 무관 편향을 필터링한다.
- **조건 주입**: 정제된 공간-운동 표현을 확산 Transformer(DiT) 동작 헤드에 추가 조건 입력으로 제공하여, "무엇을 조작할지"(공간 목표)와 "어떻게 움직일지"(운동 패턴)를 동시에 추론할 수 있게 한다.
- **비동기 이중 시스템 설계**:
  - **System 2(느림)**: VDM은 저주파 업데이트를 담당하며 전역적으로 물리적으로 일관된 운동 표현을 제공한다.
  - **System 1(빠름)**: DiT 동작 헤드는 고주파 추론을 담당하며, System 2가 제공하는 운동 인식 조건을 기반으로 실시간 동작을 생성한다.
  - 이 설계는 System 2의 업데이트 빈도가 낮더라도 System 1이 안정적인 조작을 유지할 수 있게 하여 추론 효율성을 크게 향상시킨다.

### 실험 설정 및 주요 결과
- **시뮬레이션 환경**: 여러 표준 로봇 조작 벤치마크에서 테스트한 결과, Video2Act의 평균 성공률은 이전 최첨단 VLA 방법보다 **7.7%** 높았다.
- **실제 세계 작업**: 실제 로봇 플랫폼에서 평균 성공률이 **21.7%** 향상되어 방법의 실제 유효성을 추가로 검증했다.
- **일반화 능력**: 실험 결과, Video2Act는 보지 못한 객체, 장면 및 작업 구성에서 강력한 일반화 능력을 보여주었으며, 이는 명시적 운동 인식 모델링 덕분이다.

### 결론
Video2Act는 비디오 확산 모델의 공간 및 운동 표현을 명시적으로 통합하고 비동기 이중 시스템 설계를 채택하여, 기존 방법이 로봇 정책 학습에서 프레임 간 운동 일관성을 무시하는 문제를 효과적으로 해결한다. 시뮬레이션 및 실제 세계 작업에서 이전 방법을 크게 능가할 뿐만 아니라 우수한 일반화 성능을 보여주며, 로봇 조작에서 물리적 세계 모델링에 새로운 통찰을 제공한다.
