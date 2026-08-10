---
$id: ent_paper_zheng_leveraging_os_level_primitives_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Leveraging OS-Level Primitives for Robotic Action Management
  zh: AMS
  ko: Leveraging OS-Level Primitives for Robotic Action Management
summary:
  en: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
  zh: AMS 是由上海交通大学与南方科技大学于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于将操作系统级原语（如异常、上下文切换和记录-回放）引入机器人动作管理，显著提升了任务成功率和执行效率。
  ko: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ams
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.10259v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (856 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Leveraging OS-Level Primitives for Robotic Action Management (arXiv)
  url: https://arxiv.org/abs/2508.10259
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AMS source
  url: https://doi.org/10.48550/arXiv.2508.10259
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对端到端模仿学习框架（如 VLA）因训练数据不足导致的泛化能力弱和动作效率低的问题，AMS 创新性地将机器人动作切片与操作系统线程时间片进行类比，从系统层面提出解决方案。该系统通过引入动作异常（action exception）实现即时中断以防止错误传播，利用动作上下文（action context）消除 VLA 模型中的冗余计算以加速执行，并借助动作回放（action replay）支持重复或相似任务而无需重新训练。在仿真环境和真实机器人平台上的实验表明，AMS 可将任务成功率提升 7 至 24 倍，并将端到端执行时间缩短 29% 至 74%。

## 核心内容
### 方法
- **动作异常（Action Exception）**：允许在检测到错误时立即中断当前机器人动作，防止错误连锁传播，类似操作系统中的异常处理机制。
- **动作上下文（Action Context）**：通过保存和复用 VLA 模型中间计算结果，避免重复计算，从而加速动作执行，类比操作系统的上下文切换。
- **动作回放（Action Replay）**：记录成功动作序列，在遇到相似任务时直接回放，无需重新训练模型，类似操作系统的记录-回放功能。

### 实验设置
- 在仿真环境（如 Robosuite）和真实机器人平台（如 Franka Emika Panda 机械臂）上评估。
- 对比基线为未集成 AMS 的现有机器人系统。

### 关键结果
- **任务成功率**：AMS 将成功率提升 7 倍至 24 倍，具体取决于任务复杂度。
- **执行时间**：端到端执行时间节省 29% 至 74%，尤其在重复性任务中效果显著。
- **泛化能力**：在未见过的物体位置和光照条件下，AMS 仍保持较高成功率，而基线模型性能大幅下降。

### 结论
AMS 通过将操作系统级原语融入机器人动作管理，有效解决了 VLA 模型因数据不足导致的泛化与效率瓶颈，为机器人系统设计提供了新的系统级优化思路。

## Overview
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level.   In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## Overview
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level. In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## Content
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level. In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## 参考
- http://arxiv.org/abs/2508.10259v1

## 개요
엔드투엔드 모방 학습 프레임워크(예: VLA)가 훈련 데이터 부족으로 인해 발생하는 일반화 능력 저하와 동작 효율성 문제를 해결하기 위해, AMS는 로봇 동작 슬라이스를 운영 체제 스레드 시간 슬라이스와 혁신적으로 유사하게 대응시켜 시스템 수준에서 해결 방안을 제시합니다. 이 시스템은 동작 예외(action exception)를 도입하여 즉각적인 중단을 통해 오류 전파를 방지하고, 동작 컨텍스트(action context)를 활용하여 VLA 모델의 중복 계산을 제거함으로써 실행을 가속화하며, 동작 재생(action replay)을 통해 재훈련 없이 반복적이거나 유사한 작업을 지원합니다. 시뮬레이션 환경과 실제 로봇 플랫폼에서의 실험 결과, AMS는 작업 성공률을 7배에서 24배까지 향상시키고 엔드투엔드 실행 시간을 29%에서 74%까지 단축할 수 있음을 보여줍니다.

## 핵심 내용
### 방법
- **동작 예외(Action Exception)**: 오류 감지 시 현재 로봇 동작을 즉시 중단하여 오류의 연쇄 전파를 방지하며, 운영 체제의 예외 처리 메커니즘과 유사합니다.
- **동작 컨텍스트(Action Context)**: VLA 모델의 중간 계산 결과를 저장하고 재사용하여 중복 계산을 피함으로써 동작 실행을 가속화하며, 운영 체제의 컨텍스트 스위칭과 유사합니다.
- **동작 재생(Action Replay)**: 성공적인 동작 시퀀스를 기록하고, 유사한 작업이 발생할 때 모델을 재훈련하지 않고 직접 재생하며, 운영 체제의 기록-재생 기능과 유사합니다.

### 실험 설정
- 시뮬레이션 환경(예: Robosuite)과 실제 로봇 플랫폼(예: Franka Emika Panda 로봇 팔)에서 평가되었습니다.
- 비교 기준은 AMS가 통합되지 않은 기존 로봇 시스템입니다.

### 주요 결과
- **작업 성공률**: AMS는 작업 복잡도에 따라 성공률을 7배에서 24배까지 향상시킵니다.
- **실행 시간**: 엔드투엔드 실행 시간이 29%에서 74%까지 절약되며, 특히 반복적인 작업에서 효과가 두드러집니다.
- **일반화 능력**: 보지 못한 객체 위치와 조명 조건에서도 AMS는 높은 성공률을 유지하는 반면, 기준 모델의 성능은 크게 저하됩니다.

### 결론
AMS는 운영 체제 수준의 프리미티브를 로봇 동작 관리에 통합함으로써 VLA 모델의 데이터 부족으로 인한 일반화 및 효율성 병목을 효과적으로 해결하며, 로봇 시스템 설계에 새로운 시스템 수준의 최적화 방향을 제시합니다.
