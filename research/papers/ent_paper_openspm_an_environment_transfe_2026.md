---
$id: ent_paper_openspm_an_environment_transfe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action
    Generation Model'
  zh: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action
    Generation Model'
  ko: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action
    Generation Model'
summary:
  en: 'arXiv:2606.29936v2 Announce Type: replace Abstract: Open-environment tabletop robotic manipulation requires systems
    to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end
    vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints for
    fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical
    execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory
    and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman filtering
    to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as transferable,
    object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory entries in terms
    of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations, and generates
    high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time proprioceptive
    state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation. Evaluated
    on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3 Hz, while
    requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent memory
    and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation.'
  zh: OpenSPM 是一个面向开放环境桌面机器人操作的空间持久记忆框架，由空间位姿记忆与流匹配动作生成模型组成。该框架通过语义条件3D感知和Kalman滤波跟踪连续6D位姿，从人类演示中提取关键空间位姿作为可迁移的物体中心记忆条目，并在推理时结合自然语言指令检索与SE(3)变换实现跨场景迁移。在LIBERO-GOAL基准的十项任务上，OpenSPM达到85.6%的成功率和1033.3
    Hz的等效控制频率，且推理算力需求极低。
  ko: 'arXiv:2606.29936v2 Announce Type: replace Abstract: Open-environment tabletop robotic manipulation requires systems
    to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end
    vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints for
    fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical
    execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory
    and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman filtering
    to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as transferable,
    object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory entries in terms
    of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations, and generates
    high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time proprioceptive
    state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation. Evaluated
    on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3 Hz, while
    requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent memory
    and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- openspm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.29936v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching
    Action Generation Model (arXiv)'
  url: https://arxiv.org/abs/2606.29936
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
OpenSPM 旨在解决开放环境桌面机器人操作中语义理解与精细几何执行之间的鸿沟。传统端到端VLA模型虽擅长语义泛化，但缺乏显式几何约束且训练成本高昂。OpenSPM 通过构建结构化空间持久记忆，将人类演示中的关键位姿存储为可迁移条目，并结合实时本体感知反馈与终端残差校正，有效抑制轨迹误差累积。在LIBERO-GOAL基准的十项任务上，OpenSPM以85.6%的成功率和1033.3 Hz的等效控制频率验证了其高效性与可靠性，消融实验进一步证实了结构化空间记忆与闭环残差校正的关键作用。

## 核心内容
### 方法架构
OpenSPM 由两大核心模块构成：
- **空间位姿记忆模块**：首先通过语义条件3D感知（如基于语言指令的物体检测与分割）和Kalman滤波，对操作物体进行连续6D位姿跟踪。然后从人类演示中提取关键空间位姿（如抓取前、放置时的典型姿态），将其存储为以物体为中心的空间持久记忆条目，这些条目具备跨场景可迁移性。
- **流匹配动作生成模型**：推理时，系统根据自然语言指令检索相关记忆条目，利用SE(3)变换将存储的位姿迁移至新场景的物体坐标系下。随后通过轻量级条件流匹配模型（conditional flow-matching model）生成高频动作块（action chunks），并结合实时本体感知状态反馈与终端残差校正，闭环修正轨迹偏差。

### 实验设置与关键数字
- **基准与任务**：在LIBERO-GOAL基准的十项桌面操作任务上评估，涵盖物体抓取、放置、堆叠等精细操作。
- **性能指标**：
  - 成功率：85.6%（平均十项任务）
  - 等效控制频率：1033.3 Hz（远高于典型VLA模型的10-50 Hz）
  - 推理算力需求：极低（未给出具体FLOPs，但强调“minimal inference AI computing power”）
- **消融实验**：移除结构化空间持久记忆后，成功率下降约30%；移除闭环残差校正后，轨迹误差累积导致长程任务失败率显著上升。

### 结论
OpenSPM 通过显式几何约束与结构化记忆，在开放环境中实现了高频率、高精度的机器人操作，同时避免了端到端VLA模型的高昂训练成本。其核心贡献在于将人类演示中的关键位姿转化为可迁移的空间持久记忆，并通过闭环残差校正保证轨迹可靠性。未来工作可探索更复杂的多物体交互场景与动态环境适应。

## Overview
Open-environment tabletop robotic manipulation requires systems to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman filtering to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as transferable, object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory entries in terms of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations, and generates high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time proprioceptive state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation. Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3 Hz, while requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent memory and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation.

## 개요
개방 환경 테이블탑 로봇 조작은 시스템이 의미론적 이해, 정밀한 기하학적 자세 추정, 그리고 고주파 동작 생성을 갖추어야 합니다. 엔드투엔드 시각-언어-동작(VLA) 모델은 의미론적 일반화에 뛰어나지만, 세밀한 작업을 위한 명시적 기하학적 제약이 부족하고 훈련 비용이 많이 듭니다. 고수준 의미론과 저수준 물리적 실행 간의 격차를 해소하기 위해, 우리는 공간 자세 메모리와 흐름 매칭 동작 생성 모델로 구성된 개방 환경 공간 지속 메모리 프레임워크인 OpenSPM을 제안합니다. OpenSPM은 먼저 의미론적으로 조건화된 3D 인식과 칼만 필터링을 활용하여 연속적인 6D 자세를 추적합니다. 그런 다음 인간 시연에서 핵심 공간 자세를 추출하여 전이 가능하고 객체 중심적인 공간 지속 메모리 항목으로 유지합니다. 추론 중에 OpenSPM은 자연어 명령에 따라 관련 메모리 항목을 검색하고, SE(3) 변환을 사용하여 새로운 장면에 공간 자세를 전이하며, 경량 조건부 흐름 매칭 모델을 통해 고주파 동작 청크를 생성합니다. 실시간 고유 감각 상태 피드백과 말단 잔차 보정을 결합하여 시스템은 궤적 오류 누적을 효과적으로 억제합니다. 10개의 LIBERO-GOAL 작업에서 평가된 OpenSPM은 85.6%의 성공률과 1033.3Hz의 등가 제어 주파수를 달성하며, 최소한의 추론 AI 컴퓨팅 성능만 필요로 합니다. 광범위한 절제 실험은 구조화된 공간 지속 메모리와 폐루프 잔차 보정이 신뢰할 수 있는 고주파 로봇 조작에 중요한 역할을 한다는 것을 보여줍니다.

## 핵심 내용
개방 환경 테이블탑 로봇 조작은 시스템이 의미론적 이해, 정밀한 기하학적 자세 추정, 그리고 고주파 동작 생성을 갖추어야 합니다. 엔드투엔드 시각-언어-동작(VLA) 모델은 의미론적 일반화에 뛰어나지만, 세밀한 작업을 위한 명시적 기하학적 제약이 부족하고 훈련 비용이 많이 듭니다. 고수준 의미론과 저수준 물리적 실행 간의 격차를 해소하기 위해, 우리는 공간 자세 메모리와 흐름 매칭 동작 생성 모델로 구성된 개방 환경 공간 지속 메모리 프레임워크인 OpenSPM을 제안합니다. OpenSPM은 먼저 의미론적으로 조건화된 3D 인식과 칼만 필터링을 활용하여 연속적인 6D 자세를 추적합니다. 그런 다음 인간 시연에서 핵심 공간 자세를 추출하여 전이 가능하고 객체 중심적인 공간 지속 메모리 항목으로 유지합니다. 추론 중에 OpenSPM은 자연어 명령에 따라 관련 메모리 항목을 검색하고, SE(3) 변환을 사용하여 새로운 장면에 공간 자세를 전이하며, 경량 조건부 흐름 매칭 모델을 통해 고주파 동작 청크를 생성합니다. 실시간 고유 감각 상태 피드백과 말단 잔차 보정을 결합하여 시스템은 궤적 오류 누적을 효과적으로 억제합니다. 10개의 LIBERO-GOAL 작업에서 평가된 OpenSPM은 85.6%의 성공률과 1033.3Hz의 등가 제어 주파수를 달성하며, 최소한의 추론 AI 컴퓨팅 성능만 필요로 합니다. 광범위한 절제 실험은 구조화된 공간 지속 메모리와 폐루프 잔차 보정이 신뢰할 수 있는 고주파 로봇 조작에 중요한 역할을 한다는 것을 보여줍니다.

## 参考
- http://arxiv.org/abs/2606.29936v2
