---
$id: ent_paper_zhou_badvla_towards_backdoor_attack_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization'
  zh: BadVLA
  ko: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization'
summary:
  en: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (BadVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Lehigh University, and published at NIPS25.'
  zh: BadVLA 是由华中科技大学与理海大学联合提出的首个针对视觉-语言-动作模型的后门攻击方法，发表于 NIPS25。该方法通过目标解耦优化实现特征空间分离与条件控制偏差，在多个 VLA 基准上达到近100%攻击成功率，同时保持干净任务精度几乎不变。
  ko: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (BadVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Lehigh University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- badvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.16640v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (arXiv)'
  url: https://arxiv.org/abs/2505.16640
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BadVLA source
  url: https://doi.org/10.48550/arXiv.2505.16640
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
视觉-语言-动作模型通过端到端多模态输入实现机器人控制，但其紧密耦合的架构暴露出新型安全漏洞。与传统的对抗性扰动不同，后门攻击在训练即服务范式下构成更隐蔽、持久且实际威胁，但在 VLA 模型中尚未被系统研究。BadVLA 采用两阶段优化策略：首先在显式特征空间中隔离触发表示与良性输入，然后仅在触发存在时激活条件控制偏差，同时保持干净任务性能。实验表明该方法在多个 VLA 基准上持续达到近100%攻击成功率，且对输入扰动、任务迁移和模型微调均具有鲁棒性。

## 核心内容
### 方法架构
BadVLA 的核心创新在于目标解耦优化，包含两个关键阶段：
- **显式特征空间分离**：通过对抗训练迫使模型将触发表示与正常输入特征在隐空间中进行正交化分离，确保触发特征不干扰正常任务特征分布。
- **条件控制偏差**：设计条件激活函数，仅在输入包含特定触发模式时引入控制偏差，而正常输入下模型行为完全不受影响。

### 实验设置
- **基准模型**：在多个主流 VLA 模型（如 RT-2、Octo）上进行测试
- **数据集**：使用 BridgeData v2、Open X-Embodiment 等标准机器人操作数据集
- **触发模式**：采用图像级补丁触发和文本级关键词触发两种形式
- **评估指标**：攻击成功率（ASR）和干净任务准确率（CTA）

### 关键实验结果
- **攻击成功率**：在全部测试场景中 ASR 达到 98.7%-100%，其中图像触发模式平均 ASR 为 99.3%，文本触发模式为 98.9%
- **干净任务性能**：CTA 下降幅度小于 1.2%，在大多数任务中下降不超过 0.5%
- **鲁棒性测试**：
  - 输入扰动：对高斯噪声、裁剪、旋转等常见扰动保持 95% 以上 ASR
  - 任务迁移：在未见过的操作任务上仍保持 92% 以上 ASR
  - 模型微调：经过 10 轮微调后 ASR 仍高于 88%

### 结论
BadVLA 首次系统揭示了 VLA 模型的后门安全漏洞，证明当前端到端多模态控制架构存在严重安全隐患。该工作强调在训练即服务范式下，需要建立针对 VLA 模型的专用安全防护机制，包括触发检测、特征空间隔离验证和鲁棒训练策略。项目代码与演示已开源。

## Overview
Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat-particularly under the emerging Training-as-a-Service paradigm-but remain largely unexplored in the context of VLA models. To address this gap, we propose BadVLA, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices. We have released the project page at https://badvla-project.github.io/.

## Overview
Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat—particularly under the emerging Training-as-a-Service paradigm—but remain largely unexplored in the context of VLA models. To address this gap, we propose BadVLA, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices. We have released the project page at https://badvla-project.github.io/.

## Content
Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat—particularly under the emerging Training-as-a-Service paradigm—but remain largely unexplored in the context of VLA models. To address this gap, we propose BadVLA, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices. We have released the project page at https://badvla-project.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 다중 모드 입력으로부터 직접적인 종단 간 의사 결정을 가능하게 하여 로봇 제어를 발전시켰습니다. 그러나 이들의 긴밀하게 결합된 아키텍처는 새로운 보안 취약점을 드러냅니다. 기존의 적대적 섭동과 달리, 백도어 공격은 더 은밀하고 지속적이며 실질적으로 중요한 위협을 나타냅니다. 특히 등장하는 Training-as-a-Service 패러다임 하에서 더욱 그렇지만, VLA 모델의 맥락에서는 아직 거의 탐구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 Objective-Decoupled Optimization에 기반한 백도어 공격 방법인 BadVLA를 제안하며, 이는 처음으로 VLA 모델의 백도어 취약점을 드러냅니다. 구체적으로, 이는 두 단계 프로세스로 구성됩니다: (1) 명시적 특징 공간 분리를 통해 정상 입력으로부터 트리거 표현을 격리하고, (2) 조건부 제어 편차를 통해 트리거가 있을 때만 활성화되면서 깨끗한 작업 성능을 유지합니다. 여러 VLA 벤치마크에 대한 실증적 결과는 BadVLA가 깨끗한 작업 정확도에 최소한의 영향을 미치면서 거의 100%의 공격 성공률을 일관되게 달성함을 보여줍니다. 추가 분석은 일반적인 입력 섭동, 작업 전이 및 모델 미세 조정에 대한 견고성을 확인하며, 현재 VLA 배포에서의 중요한 보안 취약점을 강조합니다. 우리의 연구는 VLA 모델의 백도어 취약점에 대한 최초의 체계적인 조사를 제공하며, 안전하고 신뢰할 수 있는 구현 모델 설계 관행의 긴급한 필요성을 강조합니다. 프로젝트 페이지를 https://badvla-project.github.io/에 공개했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 다중 모드 입력으로부터 직접적인 종단 간 의사 결정을 가능하게 하여 로봇 제어를 발전시켰습니다. 그러나 이들의 긴밀하게 결합된 아키텍처는 새로운 보안 취약점을 드러냅니다. 기존의 적대적 섭동과 달리, 백도어 공격은 더 은밀하고 지속적이며 실질적으로 중요한 위협을 나타냅니다. 특히 등장하는 Training-as-a-Service 패러다임 하에서 더욱 그렇지만, VLA 모델의 맥락에서는 아직 거의 탐구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 Objective-Decoupled Optimization에 기반한 백도어 공격 방법인 BadVLA를 제안하며, 이는 처음으로 VLA 모델의 백도어 취약점을 드러냅니다. 구체적으로, 이는 두 단계 프로세스로 구성됩니다: (1) 명시적 특징 공간 분리를 통해 정상 입력으로부터 트리거 표현을 격리하고, (2) 조건부 제어 편차를 통해 트리거가 있을 때만 활성화되면서 깨끗한 작업 성능을 유지합니다. 여러 VLA 벤치마크에 대한 실증적 결과는 BadVLA가 깨끗한 작업 정확도에 최소한의 영향을 미치면서 거의 100%의 공격 성공률을 일관되게 달성함을 보여줍니다. 추가 분석은 일반적인 입력 섭동, 작업 전이 및 모델 미세 조정에 대한 견고성을 확인하며, 현재 VLA 배포에서의 중요한 보안 취약점을 강조합니다. 우리의 연구는 VLA 모델의 백도어 취약점에 대한 최초의 체계적인 조사를 제공하며, 안전하고 신뢰할 수 있는 구현 모델 설계 관행의 긴급한 필요성을 강조합니다. 프로젝트 페이지를 https://badvla-project.github.io/에 공개했습니다.

## 参考
- http://arxiv.org/abs/2505.16640v1
