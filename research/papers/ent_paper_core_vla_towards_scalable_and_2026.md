---
$id: ent_paper_core_vla_towards_scalable_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts'
  zh: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts'
  ko: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts'
summary:
  en: 'arXiv:2607.03693v1 Announce Type: new Abstract: Vision-language-action (VLA) models have advanced generalist robotic
    manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous
    sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often
    lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining
    reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However,
    existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle
    when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We
    propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse
    computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors
    without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization
    across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors,
    we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on
    LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon
    and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline,
    including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary
    depth when available while remaining robust when depth is unavailable during deployment.'
  zh: CoRE-VLA 是一种面向机器人操作的可扩展且鲁棒的视觉-语言-动作（VLA）框架，由研究团队提出。其核心贡献在于将动作生成建模为基于上下文条件的稀疏计算，通过条件专家路由机制，使模型在传感器缺失时无需重新训练即可优雅降级，并在多任务与长时域基准上超越现有方法。
  ko: 'arXiv:2607.03693v1 Announce Type: new Abstract: Vision-language-action (VLA) models have advanced generalist robotic
    manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous
    sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often
    lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining
    reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However,
    existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle
    when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We
    propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse
    computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors
    without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization
    across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors,
    we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on
    LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon
    and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline,
    including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary
    depth when available while remaining robust when depth is unavailable during deployment.'
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
- core_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03693v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts (arXiv)'
  url: https://arxiv.org/abs/2607.03693
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现实世界中的机器人面临传感器配置多样、辅助传感器可能意外失效、不同本体设计上缺少某些传感器等挑战。现有 VLA 策略通过共享密集计算将动作生成与固定传感器集耦合，导致传感器缺失时表现脆弱，且难以针对多样任务和长时域行为进行专门化。CoRE-VLA 通过传感器可用性门控模态专用专家，实现缺失传感器下的优雅降级；同时利用任务意图将动作侧表示路由至任务相关专家，提升跨任务与长时域子目标的专门化能力。实验在 LIBERO、RoboCasa GR1 Tabletop 及真实双臂操作场景中验证，CoRE-VLA 在长时域和多任务基准上取得强结果，并优于密集动作生成消融模型及强预训练 VLA 基线，包括对未见场景的零样本泛化。

## 核心内容
### 方法架构
- **核心思想**：将动作生成视为上下文条件稀疏计算，而非传统密集计算。
- **条件专家路由**：
  - **传感器可用性门控**：根据当前可用的传感器模态（如深度相机是否在线），激活对应的模态专用专家（modality-specialized experts）。缺失传感器对应的专家被自动关闭，无需重新训练。
  - **任务意图路由**：利用任务指令（task intent）将动作侧表示路由至任务相关专家，增强对多样任务和长时域子目标的专门化能力。
- **辅助模态**：框架设计支持多种辅助传感器，实验中以深度（depth）作为代表性辅助模态进行验证。

### 实验设置
- **基准与场景**：
  - LIBERO（长时域操作基准）
  - RoboCasa GR1 Tabletop（桌面操作）
  - 真实世界双臂操作
- **对比基线**：
  - 密集动作生成消融模型（dense-action-generator ablation）
  - 强预训练 VLA 基线
- **评估指标**：任务成功率、零样本泛化能力、模态鲁棒性。

### 关键结果
- **性能优势**：CoRE-VLA 在所有基准上均取得强结果，尤其在长时域和多任务场景中显著优于基线。
- **零样本泛化**：在未见场景中，CoRE-VLA 仍能保持较高成功率，优于对比方法。
- **模态分析**：
  - 当深度传感器可用时，CoRE-VLA 能有效利用深度信息提升性能。
  - 当深度传感器在部署中不可用时，模型性能下降幅度极小，展现出鲁棒性，无需重新训练或调整。

### 结论
CoRE-VLA 通过条件专家路由机制，解决了现有 VLA 模型对固定传感器集的依赖问题，实现了传感器缺失下的优雅降级与任务专门化。实验证明其在长时域、多任务及真实场景中的有效性，为可扩展、鲁棒的机器人操作策略提供了新范式。

## Overview
Vision-language-action (VLA) models have advanced generalist robotic manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However, existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors, we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline, including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary depth when available while remaining robust when depth is unavailable during deployment.

## 개요
Vision-language-action (VLA) 모델은 범용 로봇 조작 기술을 발전시켰지만, 실제 환경 배포에서는 근본적인 과제가 드러납니다. 로봇은 다양하고 이질적인 센서 구성을 갖추고 있으며, 작동 중 보조 센서가 예기치 않게 고장날 수 있고, 서로 다른 로봇 형체는 설계상 특정 센서가 없는 경우가 많습니다. 따라서 보조 지각 입력이 가능할 때는 이를 활용하고, 우발적이든 설계상이든 센서가 없을 때도 신뢰성을 유지할 수 있는 통합 정책이 실제 배포에 필수적입니다. 그러나 기존 VLA 정책은 공유된 밀집 계산을 통해 고정된 센서 세트에 동작 생성을 결합하여, 센서가 없을 때 취약해지고 다양한 작업과 장기 행동에 특화되는 능력을 제한합니다. 우리는 동작 생성을 컨텍스트 조건부 희소 계산으로 공식화하는 확장 가능하고 강건한 VLA 프레임워크인 CoRE-VLA를 제안합니다. 센서 가용성은 모달리티별 전문가를 게이팅하여 재학습 없이 센서 부재 시 우아한 성능 저하를 가능하게 합니다. 작업 의도는 동작 측 표현을 작업 관련 전문가로 더 라우팅하여 다양한 작업과 장기 하위 목표에 대한 특화를 개선합니다. 프레임워크는 다양한 보조 센서를 수용하도록 설계되었지만, 실험에서는 대표적이고 실질적으로 중요한 보조 모달리티로서 깊이에 초점을 맞춥니다. LIBERO, RoboCasa GR1 Tabletop 및 실제 세계 이중 팔 조작 실험에서 CoRE-VLA는 장기 및 다중 작업 벤치마크에서 강력한 결과를 달성하고, 밀집 동작 생성기 절제 및 강력한 사전 학습 VLA 기준선을 능가하며, 보지 못한 시나리오에 대한 제로샷 일반화에서도 우수함을 보여줍니다. 모달리티 분석은 CoRE-VLA가 깊이를 사용할 수 있을 때 보조 깊이를 활용하면서도 배포 중 깊이가 없을 때 강건함을 유지함을 보여줍니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 범용 로봇 조작 기술을 발전시켰지만, 실제 환경 배포에서는 근본적인 과제가 드러납니다. 로봇은 다양하고 이질적인 센서 구성을 갖추고 있으며, 작동 중 보조 센서가 예기치 않게 고장날 수 있고, 서로 다른 로봇 형체는 설계상 특정 센서가 없는 경우가 많습니다. 따라서 보조 지각 입력이 가능할 때는 이를 활용하고, 우발적이든 설계상이든 센서가 없을 때도 신뢰성을 유지할 수 있는 통합 정책이 실제 배포에 필수적입니다. 그러나 기존 VLA 정책은 공유된 밀집 계산을 통해 고정된 센서 세트에 동작 생성을 결합하여, 센서가 없을 때 취약해지고 다양한 작업과 장기 행동에 특화되는 능력을 제한합니다. 우리는 동작 생성을 컨텍스트 조건부 희소 계산으로 공식화하는 확장 가능하고 강건한 VLA 프레임워크인 CoRE-VLA를 제안합니다. 센서 가용성은 모달리티별 전문가를 게이팅하여 재학습 없이 센서 부재 시 우아한 성능 저하를 가능하게 합니다. 작업 의도는 동작 측 표현을 작업 관련 전문가로 더 라우팅하여 다양한 작업과 장기 하위 목표에 대한 특화를 개선합니다. 프레임워크는 다양한 보조 센서를 수용하도록 설계되었지만, 실험에서는 대표적이고 실질적으로 중요한 보조 모달리티로서 깊이에 초점을 맞춥니다. LIBERO, RoboCasa GR1 Tabletop 및 실제 세계 이중 팔 조작 실험에서 CoRE-VLA는 장기 및 다중 작업 벤치마크에서 강력한 결과를 달성하고, 밀집 동작 생성기 절제 및 강력한 사전 학습 VLA 기준선을 능가하며, 보지 못한 시나리오에 대한 제로샷 일반화에서도 우수함을 보여줍니다. 모달리티 분석은 CoRE-VLA가 깊이를 사용할 수 있을 때 보조 깊이를 활용하면서도 배포 중 깊이가 없을 때 강건함을 유지함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.03693v1
