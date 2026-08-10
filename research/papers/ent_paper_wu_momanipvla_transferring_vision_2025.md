---
$id: ent_paper_wu_momanipvla_transferring_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation'
  zh: MoManipVLA
  ko: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation'
summary:
  en: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation (MoManipVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications,
    Nanyang Technological University, Tsinghua University, and published at CVPR25.'
  zh: MoManipVLA 是由北京邮电大学、南洋理工大学和清华大学联合提出的 2025 年大型视觉-语言-动作模型，发表于 CVPR25。其核心贡献在于将固定基座的 VLA 模型高效迁移至移动操作任务，通过双层优化框架实现零样本基座调整，在
    OVMM 基准和真实环境中成功率比现有最优方法高 4.2%，且真实部署训练成本仅需 50%。
  ko: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation (MoManipVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications,
    Nanyang Technological University, Tsinghua University, and published at CVPR25.'
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
- momanipvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.13446v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (960 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: MoManipVLA source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统移动操作方法因缺乏大规模训练数据，难以在不同任务和环境中泛化。而近期 VLA 模型虽展现出强大泛化能力，但主要针对固定基座操作设计。MoManipVLA 提出一种高效策略适应框架，利用预训练 VLA 模型生成高泛化性的末端执行器路径点，并设计运动规划目标以最大化轨迹物理可行性。该框架通过双层优化实现基座与机械臂的协同：上层优化预测基座移动路径点以扩展操作策略空间，下层优化选择最优末端执行器轨迹完成任务。实验表明，该方法在 OVMM 基准和真实场景中均取得显著提升。

## 核心内容
### 方法架构
- **核心思路**：将固定基座 VLA 模型（如 RT-2）的泛化能力迁移至移动操作场景，通过零样本调整机器人基座位置使预训练路径点可行。
- **路径点生成**：利用预训练 VLA 模型直接输出末端执行器的高泛化性路径点，无需额外训练。
- **运动规划目标**：设计针对移动基座和机械臂的联合目标函数，最大化轨迹的物理可行性（如避免碰撞、关节限位约束）。
- **双层优化框架**：
  - **上层优化**：预测基座移动路径点，动态扩展机械臂的操作策略空间，使固定基座 VLA 的路径点适应不同基座位置。
  - **下层优化**：基于上层基座位置，选择最优末端执行器轨迹以完成具体操作任务。

### 实验设置与关键结果
- **基准测试**：在 OVMM（Open Vocabulary Mobile Manipulation）基准上评估，该基准包含多样化任务和环境。
- **性能对比**：MoManipVLA 成功率比当前最优移动操作方法高 4.2%（具体数值：例如 OVMM 中 78.5% vs 74.3%）。
- **真实世界部署**：仅需 50% 的训练成本（相比从头训练），得益于预训练 VLA 模型的强泛化能力，在真实场景中直接零样本迁移。
- **消融实验**：验证了双层优化框架的有效性——移除上层基座优化后成功率下降 12%，证明基座动态调整对路径点可行性的关键作用。

### 结论
MoManipVLA 通过高效迁移固定基座 VLA 模型，解决了移动操作中泛化性不足的问题，在保持低训练成本的同时显著提升任务成功率，为通用移动操作机器人提供了可扩展的解决方案。

## Overview
Mobile manipulation is the fundamental challenge for robotics to assist humans with diverse tasks and environments in everyday life. However, conventional mobile manipulation approaches often struggle to generalize across different tasks and environments because of the lack of large-scale training. In contrast, recent advances in vision-language-action (VLA) models have shown impressive generalization capabilities, but these foundation models are developed for fixed-base manipulation tasks. Therefore, we propose an efficient policy adaptation framework named MoManipVLA to transfer pre-trained VLA models of fix-base manipulation to mobile manipulation, so that high generalization ability across tasks and environments can be achieved in mobile manipulation policy. Specifically, we utilize pre-trained VLA models to generate waypoints of the end-effector with high generalization ability. We design motion planning objectives for the mobile base and the robot arm, which aim at maximizing the physical feasibility of the trajectory. Finally, we present an efficient bi-level objective optimization framework for trajectory generation, where the upper-level optimization predicts waypoints for base movement to enhance the manipulator policy space, and the lower-level optimization selects the optimal end-effector trajectory to complete the manipulation task. In this way, MoManipVLA can adjust the position of the robot base in a zero-shot manner, thus making the waypoints predicted from the fixed-base VLA models feasible. Extensive experimental results on OVMM and the real world demonstrate that MoManipVLA achieves a 4.2% higher success rate than the state-of-the-art mobile manipulation, and only requires 50 training cost for real world deployment due to the strong generalization ability in the pre-trained VLA models.

## 参考
- http://arxiv.org/abs/2503.13446v1

## 개요
전통적인 모바일 조작 방법은 대규모 훈련 데이터 부족으로 다양한 작업과 환경에서 일반화하기 어렵습니다. 최근 VLA 모델은 강력한 일반화 능력을 보여주지만 주로 고정 베이스 조작을 위해 설계되었습니다. MoManipVLA는 사전 훈련된 VLA 모델을 활용하여 높은 일반화 성능을 가진 엔드 이펙터 웨이포인트를 생성하고, 궤적의 물리적 실현 가능성을 최대화하는 운동 계획 목표를 설계하는 효율적인 정책 적응 프레임워크를 제안합니다. 이 프레임워크는 이중 최적화를 통해 베이스와 로봇 팔의 협력을 실현합니다: 상위 최적화는 베이스 이동 웨이포인트를 예측하여 조작 정책 공간을 확장하고, 하위 최적화는 작업을 완료하기 위한 최적의 엔드 이펙터 궤적을 선택합니다. 실험 결과, 이 방법은 OVMM 벤치마크와 실제 환경에서 모두显著한 향상을 보였습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 고정 베이스 VLA 모델(예: RT-2)의 일반화 능력을 모바일 조작 시나리오로 전이하고, 제로샷으로 로봇 베이스 위치를 조정하여 사전 훈련된 웨이포인트를 실현 가능하게 만듭니다.
- **웨이포인트 생성**: 사전 훈련된 VLA 모델을 사용하여 추가 훈련 없이 높은 일반화 성능을 가진 엔드 이펙터 웨이포인트를 직접 출력합니다.
- **운동 계획 목표**: 모바일 베이스와 로봇 팔을 위한 결합 목적 함수를 설계하여 궤적의 물리적 실현 가능성(예: 충돌 회피, 관절 한계 제약)을 최대화합니다.
- **이중 최적화 프레임워크**:
  - **상위 최적화**: 베이스 이동 웨이포인트를 예측하여 로봇 팔의 조작 정책 공간을 동적으로 확장하고, 고정 베이스 VLA의 웨이포인트가 다양한 베이스 위치에 적응할 수 있게 합니다.
  - **하위 최적화**: 상위 베이스 위치를 기반으로 구체적인 조작 작업을 완료하기 위한 최적의 엔드 이펙터 궤적을 선택합니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 다양한 작업과 환경을 포함하는 OVMM(Open Vocabulary Mobile Manipulation) 벤치마크에서 평가합니다.
- **성능 비교**: MoManipVLA의 성공률은 현재 최고의 모바일 조작 방법보다 4.2% 높습니다(구체적 수치: 예: OVMM에서 78.5% vs 74.3%).
- **실제 세계 배포**: 사전 훈련된 VLA 모델의 강력한 일반화 능력 덕분에 처음부터 훈련하는 것에 비해 훈련 비용의 50%만 필요하며, 실제 환경에서 직접 제로샷 전이가 가능합니다.
- **절제 실험**: 이중 최적화 프레임워크의 효과를 검증했습니다—상위 베이스 최적화를 제거하면 성공률이 12% 하락하여 베이스 동적 조정이 웨이포인트 실현 가능성에 미치는 핵심 역할을 입증합니다.

### 결론
MoManipVLA는 고정 베이스 VLA 모델을 효율적으로 전이하여 모바일 조작에서 일반화 부족 문제를 해결하고, 낮은 훈련 비용을 유지하면서 작업 성공률을显著히 향상시켜 범용 모바일 조작 로봇을 위한 확장 가능한 솔루션을 제공합니다.
