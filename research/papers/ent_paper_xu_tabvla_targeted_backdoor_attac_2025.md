---
$id: ent_paper_xu_tabvla_targeted_backdoor_attac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models'
  zh: TabVLA
  ko: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models'
summary:
  en: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (TabVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, City University of Hong Kong.'
  zh: TabVLA 是复旦大学与香港城市大学于 2025 年提出的针对视觉-语言-动作模型（VLA）的定向后门攻击方法。其核心贡献在于实现了动作级别的细粒度后门注入，在仅污染 0.31% 训练数据的情况下，对 OpenVLA-7B 模型在
    LIBERO 基准上达到 98.67%-99.83% 的攻击成功率，同时保持 98.50%-99.17% 的正常任务保留率。
  ko: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (TabVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, City University of Hong Kong.'
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
- tabvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10932v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.10932
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TabVLA source
  url: https://doi.org/10.48550/arXiv.2510.10932
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对 VLA 模型在机器人操控中易受行为后门攻击的脆弱性，提出了一种名为 DropVLA 的动作级后门攻击方法。与以往仅实现任务级劫持或非定向攻击的工作不同，DropVLA 能够在攻击者指定的决策点强制触发特定动作原语（如打开夹爪）。该方法在流水线黑盒设置下，通过窗口一致的重标注方案实现有限数据投毒，并在物理世界中使用 7 自由度 Franka 机械臂与 pi0-fast 模型验证了攻击可行性。

## 核心内容
### 方法架构
- **攻击目标**：在 VLA 模型的动作序列中，于攻击者选定的决策点强制执行特定动作原语（如 open_gripper），同时保持模型在正常任务上的表现不受影响。
- **核心机制**：采用窗口一致的重标注方案（window-consistent relabeling scheme），在分块微调（chunked fine-tuning）过程中，对连续动作窗口内的触发点进行统一标注，确保后门触发的一致性。
- **攻击场景**：流水线黑盒设置（pipeline-black-box），攻击者仅能通过有限的数据投毒（data-poisoning）访问模型训练过程，无法控制模型架构或训练算法。

### 实验设置与关键结果
- **模型与基准**：在 OpenVLA-7B 模型上评估，使用 LIBERO 基准套件。
- **视觉触发攻击**：仅污染 0.31% 的训练片段（poisoned episodes），即可达到 98.67%-99.83% 的攻击成功率（ASR），同时正常任务保留率（clean-task retention）为 98.50%-99.17%。
- **触发效率**：在 500 Hz 控制频率下，后门触发动作可在 25 个控制步（0.05 秒）内成功执行。
- **文本触发局限性**：在低投毒预算下，纯文本触发（text-only triggers）攻击效果不稳定；将文本与视觉触发结合并未带来比纯视觉触发更一致的 ASR 提升。
- **鲁棒性与迁移性**：后门对中等程度的触发变化保持鲁棒，并能在不同评估套件间迁移（ASR 分别为 96.27% 和 99.09%），而纯文本触发在迁移场景中基本失效（ASR 仅 0.72%）。
- **物理世界验证**：在 7 自由度 Franka 机械臂上使用 pi0-fast 模型进行验证，在相机相对运动导致图像平面触发漂移（trigger drift）的情况下，仍展现出非平凡的攻击有效性。

### 结论
该研究揭示了 VLA 模型在安全关键动作粒度上可被隐蔽操控的风险，仅需极低的数据污染量且不造成可观察的正常性能下降。

## Overview
Vision-Language-Action (VLA) models map multimodal perception and language instructions to executable robot actions, making them particularly vulnerable to behavioral backdoor manipulation: a hidden trigger introduced during training can induce unintended physical actions while nominal task performance remains intact. Prior work on VLA backdoors primarily studies untargeted attacks or task-level hijacking, leaving fine-grained control over individual actions largely unexplored. In this work, we present DropVLA, an action-level backdoor attack that forces a reusable action primitive (e.g., open_gripper) to execute at attacker-chosen decision points under a realistic pipeline-black-box setting with limited data-poisoning access, using a window-consistent relabeling scheme for chunked fine-tuning. On OpenVLA-7B evaluated with LIBERO, vision-only poisoning achieves 98.67%-99.83% attack success rate (ASR) with only 0.31% poisoned episodes while preserving 98.50%-99.17% clean-task retention, and successfully triggers the targeted action within 25 control steps at 500 Hz (0.05 s). Text-only triggers are unstable at low poisoning budgets, and combining text with vision provides no consistent ASR improvement over vision-only attacks. The backdoor remains robust to moderate trigger variations and transfers across evaluation suites (96.27%, 99.09%), whereas text-only largely fails (0.72%). We further validate physical-world feasibility on a 7-DoF Franka arm with pi0-fast, demonstrating non-trivial attack efficacy under camera-relative motion that induces image-plane trigger drift. These results reveal that VLA models can be covertly steered at the granularity of safety-critical actions with minimal poisoning and without observable degradation of nominal performance.

## 개요
Vision-Language-Action (VLA) 모델은 다중 모달 인식과 언어 명령을 실행 가능한 로봇 동작으로 매핑하므로, 행동 백도어 조작에 특히 취약합니다. 즉, 훈련 중에 삽입된 숨겨진 트리거가 정상적인 작업 성능을 유지하면서 의도하지 않은 물리적 동작을 유발할 수 있습니다. VLA 백도어에 대한 기존 연구는 주로 비표적 공격 또는 작업 수준 하이재킹을 다루며, 개별 동작에 대한 세밀한 제어는 거의 탐구되지 않았습니다. 본 연구에서는 DropVLA를 제안합니다. 이는 제한된 데이터 오염 접근 권한을 가진 현실적인 파이프라인-블랙박스 설정에서, 청크 기반 미세 조정을 위한 윈도우 일관 재레이블링 방식을 사용하여 공격자가 선택한 결정 지점에서 재사용 가능한 동작 프리미티브(예: open_gripper)를 실행하도록 강제하는 동작 수준 백도어 공격입니다. LIBERO로 평가된 OpenVLA-7B에서, 시각 전용 오염은 0.31%의 오염된 에피소드만으로 98.67%-99.83%의 공격 성공률(ASR)을 달성하고, 98.50%-99.17%의 정상 작업 유지율을 보존하며, 500Hz(0.05초)에서 25개의 제어 단계 내에 목표 동작을 성공적으로 트리거합니다. 텍스트 전용 트리거는 낮은 오염 예산에서 불안정하며, 텍스트와 시각을 결합해도 시각 전용 공격에 비해 일관된 ASR 개선을 제공하지 않습니다. 백도어는 적당한 트리거 변형에 강건하며 평가 스위트 간 전이(96.27%, 99.09%)가 가능하지만, 텍스트 전용은 대부분 실패합니다(0.72%). 또한 pi0-fast를 사용한 7-DoF Franka 암에서 물리적 세계 실현 가능성을 검증하여, 이미지 평면 트리거 드리프트를 유발하는 카메라 상대 운동 하에서 상당한 공격 효능을 입증했습니다. 이러한 결과는 VLA 모델이 최소한의 오염과 정상 성능의 관찰 가능한 저하 없이 안전 중요 동작의 세분성에서 은밀하게 조종될 수 있음을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 다중 모달 인식과 언어 명령을 실행 가능한 로봇 동작으로 매핑하므로, 행동 백도어 조작에 특히 취약합니다. 즉, 훈련 중에 삽입된 숨겨진 트리거가 정상적인 작업 성능을 유지하면서 의도하지 않은 물리적 동작을 유발할 수 있습니다. VLA 백도어에 대한 기존 연구는 주로 비표적 공격 또는 작업 수준 하이재킹을 다루며, 개별 동작에 대한 세밀한 제어는 거의 탐구되지 않았습니다. 본 연구에서는 DropVLA를 제안합니다. 이는 제한된 데이터 오염 접근 권한을 가진 현실적인 파이프라인-블랙박스 설정에서, 청크 기반 미세 조정을 위한 윈도우 일관 재레이블링 방식을 사용하여 공격자가 선택한 결정 지점에서 재사용 가능한 동작 프리미티브(예: open_gripper)를 실행하도록 강제하는 동작 수준 백도어 공격입니다. LIBERO로 평가된 OpenVLA-7B에서, 시각 전용 오염은 0.31%의 오염된 에피소드만으로 98.67%-99.83%의 공격 성공률(ASR)을 달성하고, 98.50%-99.17%의 정상 작업 유지율을 보존하며, 500Hz(0.05초)에서 25개의 제어 단계 내에 목표 동작을 성공적으로 트리거합니다. 텍스트 전용 트리거는 낮은 오염 예산에서 불안정하며, 텍스트와 시각을 결합해도 시각 전용 공격에 비해 일관된 ASR 개선을 제공하지 않습니다. 백도어는 적당한 트리거 변형에 강건하며 평가 스위트 간 전이(96.27%, 99.09%)가 가능하지만, 텍스트 전용은 대부분 실패합니다(0.72%). 또한 pi0-fast를 사용한 7-DoF Franka 암에서 물리적 세계 실현 가능성을 검증하여, 이미지 평면 트리거 드리프트를 유발하는 카메라 상대 운동 하에서 상당한 공격 효능을 입증했습니다. 이러한 결과는 VLA 모델이 최소한의 오염과 정상 성능의 관찰 가능한 저하 없이 안전 중요 동작의 세분성에서 은밀하게 조종될 수 있음을 보여줍니다.

## 参考
- http://arxiv.org/abs/2510.10932v4
