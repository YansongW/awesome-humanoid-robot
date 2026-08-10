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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03693v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1143 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03693v1

## 개요
실세계의 로봇은 다양한 센서 구성, 보조 센서의 예기치 않은 고장, 서로 다른 본체 설계에서 특정 센서의 부재 등의 도전에 직면합니다. 기존 VLA 정책은 공유된 고밀도 계산을 통해 동작 생성을 고정된 센서 세트와 결합하여, 센서가 없을 때 취약한 성능을 보이고 다양한 작업과 장기 행동의 전문화가 어렵습니다. CoRE-VLA는 센서 가용성 게이팅을 통해 모달리티 전용 전문가를 제어하여 센서 부재 시 우아한 성능 저하를 실현합니다. 동시에 작업 의도를 활용하여 동작 측 표현을 작업 관련 전문가로 라우팅하여 교차 작업 및 장기 하위 목표의 전문화 능력을 향상시킵니다. 실험은 LIBERO, RoboCasa GR1 Tabletop 및 실제 이중 팔 조작 시나리오에서 수행되었으며, CoRE-VLA는 장기 및 다중 작업 벤치마크에서 강력한 결과를 얻었고, 고밀도 동작 생성 절제 모델 및 강력한 사전 훈련 VLA 기준선(미지의 장면에 대한 제로샷 일반화 포함)보다 우수합니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 동작 생성을 전통적인 고밀도 계산이 아닌 문맥 조건부 희소 계산으로 간주합니다.
- **조건부 전문가 라우팅**:
  - **센서 가용성 게이팅**: 현재 사용 가능한 센서 모달리티(예: 깊이 카메라 온라인 여부)에 따라 해당 모달리티 전용 전문가(modality-specialized experts)를 활성화합니다. 누락된 센서에 해당하는 전문가는 자동으로 비활성화되며 재훈련이 필요 없습니다.
  - **작업 의도 라우팅**: 작업 지시(task intent)를 활용하여 동작 측 표현을 작업 관련 전문가로 라우팅하여 다양한 작업 및 장기 하위 목표의 전문화 능력을 강화합니다.
- **보조 모달리티**: 프레임워크는 여러 보조 센서를 지원하며, 실험에서는 깊이(depth)를 대표적인 보조 모달리티로 검증합니다.

### 실험 설정
- **벤치마크 및 시나리오**:
  - LIBERO(장기 조작 벤치마크)
  - RoboCasa GR1 Tabletop(테이블탑 조작)
  - 실제 세계 이중 팔 조작
- **비교 기준선**:
  - 고밀도 동작 생성 절제 모델(dense-action-generator ablation)
  - 강력한 사전 훈련 VLA 기준선
- **평가 지표**: 작업 성공률, 제로샷 일반화 능력, 모달리티 견고성.

### 주요 결과
- **성능 우위**: CoRE-VLA는 모든 벤치마크에서 강력한 결과를 얻었으며, 특히 장기 및 다중 작업 시나리오에서 기준선보다 크게 우수합니다.
- **제로샷 일반화**: 미지의 장면에서 CoRE-VLA는 여전히 높은 성공률을 유지하며 비교 방법보다 우수합니다.
- **모달리티 분석**:
  - 깊이 센서가 사용 가능할 때 CoRE-VLA는 깊이 정보를 효과적으로 활용하여 성능을 향상시킵니다.
  - 배포 중 깊이 센서를 사용할 수 없을 때 모델 성능 저하 폭이 매우 작아 재훈련이나 조정 없이 견고성을 보여줍니다.

### 결론
CoRE-VLA는 조건부 전문가 라우팅 메커니즘을 통해 기존 VLA 모델의 고정 센서 세트 의존 문제를 해결하고, 센서 부재 시 우아한 성능 저하와 작업 전문화를 실현합니다. 실험은 장기, 다중 작업 및 실제 시나리오에서의 효과를 입증하여 확장 가능하고 견고한 로봇 조작 정책의 새로운 패러다임을 제공합니다.
