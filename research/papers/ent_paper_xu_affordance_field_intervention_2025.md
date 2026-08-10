---
$id: ent_paper_xu_affordance_field_intervention_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation'
  zh: AFI
  ko: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation'
summary:
  en: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (AFI), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The University of Sydney, John Hopcropt Center for
    Computer Science, Shanghai Jiao Tong University.'
  zh: Affordance Field Intervention (AFI) 是由悉尼大学、约翰霍普克罗夫特计算机科学中心及上海交通大学于2025年提出的轻量级混合框架，旨在解决视觉-语言-动作模型在机器人操作中因分布偏移而陷入“记忆陷阱”的问题。其核心贡献在于利用3D空间可供性场作为即插即用模块，通过检测记忆陷阱、重定位机器人及生成可供性引导路径点，显著提升VLA模型在未知环境中的鲁棒性，在真实机器人平台和LIBERO-Pro基准上分别实现平均23.5%和20.2%的性能提升。
  ko: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (AFI), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The University of Sydney, John Hopcropt Center for
    Computer Science, Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- afi
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07472v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (895 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.07472
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AFI source
  url: https://doi.org/10.48550/arXiv.2512.07472
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) 模型在机器人操作中表现优异，但面对测试场景变化时容易复现记忆轨迹而非适应新环境，这种失败模式被称为“记忆陷阱”。该问题源于端到端设计缺乏显式3D空间推理，无法可靠识别陌生环境中的可操作区域。为此，AFI引入3D Spatial Affordance Fields (SAFs) 作为几何表征，通过本体感觉检测记忆陷阱、将机器人重定位至高可供性区域，并生成可供性驱动的路径点来锚定VLA动作。实验表明，该方法在真实机器人平台和LIBERO-Pro基准上均能有效增强VLA模型对分布偏移的鲁棒性。

## 核心内容
### 方法架构
AFI 是一个轻量级混合框架，将 SAFs 作为按需插件集成到 VLA 模型中，具体流程包括：
- **记忆陷阱检测**：通过本体感觉（如关节位置、力反馈）监控机器人行为，当检测到动作与当前场景不匹配时触发干预。
- **重定位与路径点生成**：将机器人重新定位到最近的高可供性区域，并基于 SAF 生成一系列路径点，这些路径点作为 VLA 生成动作的锚点，确保动作与物理可行性对齐。
- **轨迹评分**：使用基于 SAF 的评分器选择累积可供性最高的轨迹，避免 VLA 陷入记忆轨迹。

### 实验设置与关键数字
- **VLA 骨干网络**：测试了 $π_{0}$ 和 $π_{0.5}$ 两种模型。
- **真实机器人平台**：在分布外场景下，AFI 使平均性能提升 **23.5%**。
- **LIBERO-Pro 基准**：在分布偏移条件下，平均性能提升 **20.2%**。
- **对比基线**：与未使用 AFI 的原始 VLA 模型相比，AFI 在多种任务（如抓取、放置、堆叠）中均表现出更稳定的适应性。

### 结论
AFI 通过引入 3D 空间可供性场作为显式几何线索，有效弥补了 VLA 模型在空间推理上的不足，使其在分布偏移场景下避免复现记忆轨迹。该方法无需修改 VLA 骨干网络，即可作为通用插件提升鲁棒性，为机器人操作中的端到端模型提供了轻量级解决方案。

## Overview
Vision-Language-Action (VLA) models have shown great performance in robotic manipulation by mapping visual observations and language instructions directly to actions. However, they remain brittle under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is a failure mode we refer to as the "Memory Trap". This limitation stems from the end-to-end design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments. To compensate for this missing spatial understanding, 3D Spatial Affordance Fields (SAFs) can provide a geometric representation that highlights where interactions are physically feasible, offering explicit cues about regions the robot should approach or avoid. We therefore introduce Affordance Field Intervention (AFI), a lightweight hybrid framework that uses SAFs as an on-demand plug-in to guide VLA behavior. Our system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions. A SAF-based scorer then selects trajectories with the highest cumulative affordance. Extensive experiments demonstrate that our method achieves an average improvement of 23.5% across different VLA backbones ($π_{0}$ and $π_{0.5}$) under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts.

## 参考
- http://arxiv.org/abs/2512.07472v1

## 개요
Vision-Language-Action (VLA) 모델은 로봇 조작에서 뛰어난 성능을 보이지만, 테스트 환경이 변화할 때 새로운 환경에 적응하기보다 기억된 궤적을 재현하는 경향이 있으며, 이러한 실패 모드는 "기억 함정"이라고 불립니다. 이 문제는 엔드투엔드 설계가 명시적 3D 공간 추론을 결여하여 낯선 환경에서 조작 가능한 영역을 안정적으로 식별하지 못하는 데서 비롯됩니다. 이를 해결하기 위해 AFI는 3D Spatial Affordance Fields (SAFs)를 기하학적 표현으로 도입하여, 고유 감각을 통해 기억 함정을 감지하고, 로봇을 높은 어포던스 영역으로 재배치하며, 어포던스 기반 경유점을 생성하여 VLA 동작을 고정합니다. 실험 결과, 이 방법은 실제 로봇 플랫폼과 LIBERO-Pro 벤치마크에서 VLA 모델의 분포 이동에 대한 강건성을 효과적으로 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
AFI는 SAFs를 주문형 플러그인으로 VLA 모델에 통합하는 경량 하이브리드 프레임워크로, 구체적인 절차는 다음과 같습니다:
- **기억 함정 감지**: 고유 감각(예: 관절 위치, 힘 피드백)을 통해 로봇의 행동을 모니터링하고, 동작이 현재 장면과 일치하지 않을 때 개입을 트리거합니다.
- **재배치 및 경유점 생성**: 로봇을 가장 가까운 높은 어포던스 영역으로 재배치하고, SAF 기반으로 일련의 경유점을 생성합니다. 이 경유점들은 VLA가 생성하는 동작의 앵커 역할을 하여 동작이 물리적 실현 가능성과 정렬되도록 보장합니다.
- **궤적 점수화**: SAF 기반 점수기를 사용하여 누적 어포던스가 가장 높은 궤적을 선택하여 VLA가 기억 궤적에 빠지는 것을 방지합니다.

### 실험 설정 및 주요 수치
- **VLA 백본 네트워크**: $π_{0}$ 및 $π_{0.5}$ 두 모델을 테스트했습니다.
- **실제 로봇 플랫폼**: 분포 외 시나리오에서 AFI는 평균 성능을 **23.5%** 향상시켰습니다.
- **LIBERO-Pro 벤치마크**: 분포 이동 조건에서 평균 성능을 **20.2%** 향상시켰습니다.
- **비교 기준선**: AFI를 사용하지 않은 원래 VLA 모델과 비교하여, AFI는 다양한 작업(예: 잡기, 놓기, 쌓기)에서 더 안정적인 적응성을 보였습니다.

### 결론
AFI는 3D 공간 어포던스 필드를 명시적 기하학적 단서로 도입하여 VLA 모델의 공간 추론 부족을 효과적으로 보완하며, 분포 이동 시나리오에서 기억 궤적을 재현하는 것을 방지합니다. 이 방법은 VLA 백본 네트워크를 수정할 필요 없이 범용 플러그인으로 강건성을 향상시킬 수 있어, 로봇 조작의 엔드투엔드 모델에 경량 솔루션을 제공합니다.
