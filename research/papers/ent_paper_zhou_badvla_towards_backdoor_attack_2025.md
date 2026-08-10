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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.16640v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (976 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.16640v1

## 개요
비전-언어-행동 모델은 엔드투엔드 다중 모달 입력을 통해 로봇 제어를 구현하지만, 그 긴밀하게 결합된 아키텍처는 새로운 유형의 보안 취약점을 드러낸다. 기존의 적대적 교란과 달리, 백도어 공격은 훈련-서비스 패러다임 하에서 더 은밀하고 지속적이며 실질적인 위협을 구성하지만, VLA 모델에서는 아직 체계적으로 연구되지 않았다. BadVLA는 두 단계 최적화 전략을 채택한다: 먼저 명시적 특징 공간에서 트리거 표현과 정상 입력을 분리하고, 그런 다음 트리거가 존재할 때만 조건부 제어 편향을 활성화하면서 깨끗한 작업 성능을 유지한다. 실험은 이 방법이 여러 VLA 벤치마크에서 지속적으로 약 100%의 공격 성공률을 달성하며, 입력 교란, 작업 전이 및 모델 미세 조정에 대해 모두 견고함을 보여준다.

## 핵심 내용
### 방법 아키텍처
BadVLA의 핵심 혁신은 목표 분리 최적화에 있으며, 두 가지 중요한 단계를 포함한다:
- **명시적 특징 공간 분리**: 적대적 훈련을 통해 모델이 트리거 표현과 정상 입력 특징을 잠재 공간에서 직교적으로 분리하도록 강제하여, 트리거 특징이 정상 작업 특징 분포를 방해하지 않도록 보장한다.
- **조건부 제어 편향**: 조건부 활성화 함수를 설계하여 입력에 특정 트리거 패턴이 포함된 경우에만 제어 편향을 도입하고, 정상 입력에서는 모델 동작이 완전히 영향을 받지 않도록 한다.

### 실험 설정
- **기준 모델**: 여러 주류 VLA 모델(예: RT-2, Octo)에서 테스트
- **데이터셋**: BridgeData v2, Open X-Embodiment 등 표준 로봇 조작 데이터셋 사용
- **트리거 패턴**: 이미지 수준 패치 트리거와 텍스트 수준 키워드 트리거의 두 가지 형태 채택
- **평가 지표**: 공격 성공률(ASR) 및 깨끗한 작업 정확도(CTA)

### 주요 실험 결과
- **공격 성공률**: 모든 테스트 시나리오에서 ASR이 98.7%-100%에 도달, 이미지 트리거 패턴의 평균 ASR은 99.3%, 텍스트 트리거 패턴은 98.9%
- **깨끗한 작업 성능**: CTA 감소 폭이 1.2% 미만, 대부분의 작업에서 감소 폭이 0.5%를 초과하지 않음
- **견고성 테스트**:
  - 입력 교란: 가우시안 노이즈, 크롭, 회전 등 일반적인 교란에 대해 95% 이상의 ASR 유지
  - 작업 전이: 보지 못한 조작 작업에서도 92% 이상의 ASR 유지
  - 모델 미세 조정: 10라운드 미세 조정 후에도 ASR이 88% 이상 유지

### 결론
BadVLA는 처음으로 VLA 모델의 백도어 보안 취약점을 체계적으로 밝혀내며, 현재 엔드투엔드 다중 모달 제어 아키텍처에 심각한 보안 위험이 존재함을 증명한다. 이 작업은 훈련-서비스 패러다임 하에서 트리거 감지, 특징 공간 분리 검증 및 견고한 훈련 전략을 포함한 VLA 모델 전용 보안 방어 메커니즘을 구축해야 함을 강조한다. 프로젝트 코드와 데모는 오픈소스로 공개되었다.
