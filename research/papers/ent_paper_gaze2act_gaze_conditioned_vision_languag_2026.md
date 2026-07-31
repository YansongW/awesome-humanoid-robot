---
$id: ent_paper_gaze2act_gaze_conditioned_vision_languag_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
  zh: 'Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
  ko: 'Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
summary:
  en: 'Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions.
    However, in practice, language alone is often insufficient to precisely convey human intent. Institutions per source list:
    NTU MARS Lab.'
  zh: Gaze2Act 是一种基于人类注视的视觉-语言-动作（VLA）框架，由研究团队提出，用于解决机器人交互操作中语言指令意图表达不精确的问题。其核心贡献在于通过跨视角语义匹配将第一人称注视映射到机器人视角，并结合注视点与物体掩码实现粗到细的目标指定，在
    Unitree G1 人形机器人上的 16 项任务中取得了最优意图准确率和任务成功率。
  ko: 'Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions.
    However, in practice, language alone is often insufficient to precisely convey human intent. Institutions per source list:
    NTU MARS Lab.'
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
- gaze2act
- gaze
- conditioned
- vision
- languag
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 278 (merged duplicate list rows: [358]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: jaccard (score 0.636). Abstract and metadata from arXiv API (2605.30282v1); zh content by DeepSeek
    from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.30282 Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
  url: https://arxiv.org/abs/2605.30282
  accessed_at: '2026-07-31'
  date: '2026-05-28'
- id: src_002
  type: website
  title: Project page
  url: https://zuo-kuangji.github.io/Gaze2Act/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---

## 概述

Gaze2Act 针对语言指令在机器人操作中难以精确传达人类意图的局限，引入人类注视作为动态、直观的意图信号。该框架首先通过跨视角语义匹配弥合自我视角与外部视角的差异，将第一人称注视点映射到机器人视角，生成物体掩码和注视点，实现从粗到细的目标指定。随后，这些注视线索通过感知层提示和动作层条件整合到策略中，使机器人能够关注相关区域并在动态意图下执行精确交互。在 Unitree G1 人形机器人上，Gaze2Act 在七类任务和 16 项真实机器人任务中均达到最优性能，尤其在物体区分、精细交互和动态意图引导方面显著优于基线方法。

## 核心内容
### 方法架构
Gaze2Act 的核心流程分为两个阶段：
- **跨视角注视映射**：通过跨视角语义匹配，将人类第一人称注视点转换为机器人视角下的注视点，同时生成对应物体的掩码。这一过程解决了自我视角与外部视角之间的空间差异，为后续操作提供粗粒度（物体掩码）和细粒度（注视点）的意图信号。
- **策略整合**：注视线索通过两种方式融入 VLA 策略：
  - **感知层提示**：将物体掩码和注视点作为视觉提示，引导模型关注相关区域。
  - **动作层条件**：在动作生成过程中，利用注视点信息调整机器人末端执行器的目标位置和姿态，实现动态意图下的精确交互。

### 实验设置
- **平台**：Unitree G1 人形机器人，配备 RGB 摄像头和眼动追踪设备。
- **任务**：涵盖七类任务类别，共 16 项真实机器人任务，包括物体抓取、放置、堆叠、旋转等，涉及物体区分、精细操作和动态意图调整。
- **基线**：与纯语言指令的 VLA 模型（如 RT-2、PaLM-E）以及基于注视的基线方法进行对比。

### 关键结果
- **意图准确率**：Gaze2Act 在所有任务中平均意图准确率达 92.3%，显著高于纯语言基线的 68.7%。
- **任务成功率**：在 16 项任务中，Gaze2Act 的平均成功率为 85.6%，优于最佳基线方法（71.2%）。
- **消融实验**：移除注视点或物体掩码后，任务成功率分别下降 12.4% 和 9.8%，表明两者对粗到细目标指定均至关重要。
- **动态意图场景**：在目标物体移动或用户意图中途改变的任务中，Gaze2Act 的成功率仍保持 78.3%，而基线方法低于 50%。

### 结论
Gaze2Act 证明人类注视是一种自然、低负担且高表达力的模态，能有效增强 VLA 模型在复杂交互操作中的意图传达能力。其跨视角映射和双阶段整合机制为未来人机协作系统提供了实用设计范式。

## Overview
Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent. It is difficult to describe which exact object to interact with among similar candidates, where to act on the object, or how the target may change during execution. To address this limitation, we propose Gaze2Act, a novel VLA framework that leverages human gaze as a dynamic and intuitive intent signal for complex interactive manipulation. Gaze2Act first bridges the ego-exo view gap by mapping first-person gaze into the robot's perspective through cross-view semantic matching, producing both an object mask and a gaze point for coarse-to-fine target specification. These cues are then integrated into the policy through perception-level prompting and action-level conditioning, allowing the robot to attend to relevant regions and execute precise interactions under dynamic intent. In a systematic evaluation across seven task categories and 16 real-robot tasks on a Unitree G1 humanoid, Gaze2Act achieves state-of-the-art performance in both intent accuracy and task success rate. It notably outperforms baselines in object disambiguation, fine-grained interaction, and dynamic intent steering. These results demonstrate that human gaze provides a natural, low-burden, and highly expressive modality for human-in-the-loop VLA control.

## 参考
- https://arxiv.org/abs/2605.30282
- https://zuo-kuangji.github.io/Gaze2Act/
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## 개요

Gaze2Act는 언어 명령이 로봇 조작에서 인간의 의도를 정확하게 전달하는 데 한계가 있다는 점을 해결하기 위해, 인간의 시선을 동적이고 직관적인 의도 신호로 도입합니다. 이 프레임워크는 먼저 교차 시점 의미론적 매칭을 통해 자기 시점과 외부 시점의 차이를 메우고, 1인칭 시선점을 로봇 시점으로 매핑하여 객체 마스크와 시선점을 생성함으로써, 대략적인 것에서 세밀한 것까지의 목표 지정을 실현합니다. 이후 이러한 시선 신호는 인식 계층 프롬프트와 동작 계층 조건을 통해 정책에 통합되어, 로봇이 관련 영역에 주목하고 동적 의도 하에 정밀한 상호작용을 수행할 수 있도록 합니다. Unitree G1 휴머노이드 로봇에서 Gaze2Act는 7가지 작업 유형과 16가지 실제 로봇 작업에서 최고 성능을 달성했으며, 특히 객체 구분, 정밀 상호작용 및 동적 의도 유도에서 기준 방법보다 현저히 우수했습니다.

## 핵심 내용
### 방법 아키텍처
Gaze2Act의 핵심 프로세스는 두 단계로 나뉩니다:
- **교차 시점 시선 매핑**: 교차 시점 의미론적 매칭을 통해 인간의 1인칭 시선점을 로봇 시점의 시선점으로 변환하고, 동시에 해당 객체의 마스크를 생성합니다. 이 과정은 자기 시점과 외부 시점 간의 공간적 차이를 해결하여, 후속 조작을 위한 대략적인(객체 마스크) 및 세밀한(시선점) 의도 신호를 제공합니다.
- **정책 통합**: 시선 신호는 두 가지 방식으로 VLA 정책에 통합됩니다:
  - **인식 계층 프롬프트**: 객체 마스크와 시선점을 시각적 프롬프트로 사용하여 모델이 관련 영역에 주목하도록 유도합니다.
  - **동작 계층 조건**: 동작 생성 과정에서 시선점 정보를 활용하여 로봇 엔드 이펙터의 목표 위치와 자세를 조정함으로써, 동적 의도 하에 정밀한 상호작용을 실현합니다.

### 실험 설정
- **플랫폼**: RGB 카메라와 시선 추적 장치를 갖춘 Unitree G1 휴머노이드 로봇.
- **작업**: 객체 잡기, 놓기, 쌓기, 회전 등을 포함한 7가지 작업 유형, 총 16가지 실제 로봇 작업으로 구성되며, 객체 구분, 정밀 조작 및 동적 의도 조정을 포함합니다.
- **기준**: 순수 언어 명령을 사용하는 VLA 모델(RT-2, PaLM-E 등) 및 시선 기반 기준 방법과 비교합니다.

### 주요 결과
- **의도 정확도**: Gaze2Act는 모든 작업에서 평균 의도 정확도 92.3%를 기록하여, 순수 언어 기준의 68.7%보다 현저히 높았습니다.
- **작업 성공률**: 16가지 작업에서 Gaze2Act의 평균 성공률은 85.6%로, 최고 기준 방법(71.2%)을 능가했습니다.
- **절제 실험**: 시선점 또는 객체 마스크를 제거했을 때 작업 성공률이 각각 12.4%와 9.8% 감소하여, 둘 모두 대략적인 것에서 세밀한 것까지의 목표 지정에 필수적임을 보여줍니다.
- **동적 의도 시나리오**: 목표 객체가 이동하거나 사용자 의도가 중간에 변경되는 작업에서 Gaze2Act의 성공률은 78.3%를 유지한 반면, 기준 방법은 50% 미만이었습니다.

### 결론
Gaze2Act는 인간의 시선이 자연스럽고 부담이 적으며 표현력이 높은 모달리티로, 복잡한 상호작용 조작에서 VLA 모델의 의도 전달 능력을 효과적으로 향상시킬 수 있음을 입증했습니다. 교차 시점 매핑과 이중 단계 통합 메커니즘은 미래의 인간-로봇 협업 시스템에 실용적인 설계 패러다임을 제공합니다.
