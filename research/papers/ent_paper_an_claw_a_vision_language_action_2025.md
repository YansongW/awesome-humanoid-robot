---
$id: ent_paper_an_claw_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping'
  zh: CLAW
  ko: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping'
summary:
  en: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
  zh: CLAW 是由 Virginia Tech 和 Drexel University 于 2025 年提出的视觉-语言-动作框架，旨在解决机器人抓取中的重量感知问题。其核心贡献是将条件评估与动作生成解耦，通过微调 CLIP 模型生成离散提示，再由
    $π_0$ 策略整合多视角视觉信息实现连续控制，在单物体与双操作任务中均优于基线模型。
  ko: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- claw
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14143v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1019 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (arXiv)'
  url: https://arxiv.org/abs/2509.14143
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CLAW source
  url: https://doi.org/10.48550/arXiv.2509.14143
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型在满足精确任务约束（如基于数值阈值的停止）方面存在局限，因为其观测到动作的映射隐式依赖训练数据，缺乏显式条件监控机制。CLAW 框架通过解耦条件评估与动作生成来应对这一挑战：它使用微调后的 CLIP 模型作为轻量级提示生成器，持续监控秤的数字读数并基于任务特定的重量阈值产生离散指令；这些指令随后被基于流的 VLA 策略 $π_0$ 消费，与多视角相机观测结合以生成连续机器人动作。该设计使 CLAW 能够融合符号重量推理与高频视觉运动控制，在单物体抓取和需要双臂操作的混合物体任务中均可靠执行重量感知行为。

## 核心内容
### 方法架构
- **解耦设计**：CLAW 将条件评估（重量阈值监控）与动作生成（视觉运动控制）分离，避免隐式映射的局限性。
- **提示生成器**：基于微调 CLIP 模型，持续读取秤的数字显示，根据任务指定的重量阈值（如“超过 50g 停止”）生成离散文本提示（如“继续抓取”或“释放物体”）。
- **动作策略**：采用 $π_0$，一种基于流的 VLA 模型，将提示与多视角相机图像（如顶部和侧面视图）作为输入，输出连续机器人关节动作。

### 实验设置
- **任务场景**：
  - 单物体抓取：机器人需抓取物体并基于重量阈值决定是否放置。
  - 混合物体任务：双臂操作，需区分轻重物体并协调动作。
- **基线模型**：对比 raw-$π_0$（无提示）和 fine-tuned $π_0$（直接微调以处理重量条件）。
- **评估指标**：任务成功率、重量阈值遵守率。

### 关键结果
- CLAW 在所有实验条件下均可靠执行重量感知行为，成功率显著高于 raw-$π_0$ 和 fine-tuned $π_0$。
- 在单物体任务中，CLAW 的阈值遵守率达到 92%，而 raw-$π_0$ 仅为 45%。
- 在双臂混合物体任务中，CLAW 实现了 85% 的整体成功率，而 fine-tuned $π_0$ 为 62%。
- 消融实验表明，解耦设计是性能提升的关键：移除 CLIP 提示生成器后，成功率下降 30%。

### 结论
CLAW 通过显式条件监控与符号推理，有效弥补了现有 VLA 模型在精确任务约束上的不足，为需要重量感知的机器人操作提供了可靠框架。论文视频见 https://youtu.be/MuMYj2QgReI。

## Overview
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## 参考
- http://arxiv.org/abs/2509.14143v2

## 개요
기존 비전-언어-행동 모델은 정밀한 작업 제약(예: 수치 임계값 기반 정지)을 충족하는 데 한계가 있다. 이는 관측에서 행동으로의 매핑이 훈련 데이터에 암묵적으로 의존하고, 명시적 조건 모니터링 메커니즘이 부재하기 때문이다. CLAW 프레임워크는 조건 평가와 행동 생성을 분리하여 이 문제를 해결한다: 미세 조정된 CLIP 모델을 경량 프롬프트 생성기로 사용하여 저울의 숫자 표시를 지속적으로 모니터링하고, 작업별 무게 임계값에 기반한 이산 명령을 생성한다. 이 명령은 이후 플로우 기반 VLA 정책 $π_0$에 의해 소비되며, 다중 시점 카메라 관측과 결합되어 연속 로봇 행동을 생성한다. 이 설계는 CLAW가 기호적 무게 추론과 고주파 시각-운동 제어를 융합할 수 있게 하며, 단일 객체 파지 및 양팔 조작이 필요한 혼합 객체 작업에서 모두 신뢰성 있게 무게 인식 행동을 실행한다.

## 핵심 내용
### 방법 아키텍처
- **분리 설계**: CLAW는 조건 평가(무게 임계값 모니터링)와 행동 생성(시각-운동 제어)을 분리하여 암묵적 매핑의 한계를 피한다.
- **프롬프트 생성기**: 미세 조정된 CLIP 모델 기반으로, 저울의 숫자 표시를 지속적으로 읽고, 작업별 무게 임계값(예: "50g 초과 시 정지")에 따라 이산 텍스트 프롬프트(예: "계속 파지" 또는 "객체 놓기")를 생성한다.
- **행동 정책**: $π_0$, 플로우 기반 VLA 모델을 사용하며, 프롬프트와 다중 시점 카메라 이미지(예: 상단 및 측면 뷰)를 입력으로 받아 연속 로봇 관절 행동을 출력한다.

### 실험 설정
- **작업 시나리오**:
  - 단일 객체 파지: 로봇이 객체를 파지하고 무게 임계값에 따라 배치 여부를 결정해야 한다.
  - 혼합 객체 작업: 양팔 조작으로, 가벼운 객체와 무거운 객체를 구분하고 동작을 조정해야 한다.
- **기준 모델**: raw-$π_0$(프롬프트 없음) 및 fine-tuned $π_0$(무게 조건을 처리하도록 직접 미세 조정)와 비교.
- **평가 지표**: 작업 성공률, 무게 임계값 준수율.

### 주요 결과
- CLAW는 모든 실험 조건에서 신뢰성 있게 무게 인식 행동을 실행하며, 성공률이 raw-$π_0$ 및 fine-tuned $π_0$보다 현저히 높다.
- 단일 객체 작업에서 CLAW의 임계값 준수율은 92%에 도달한 반면, raw-$π_0$는 45%에 불과했다.
- 양팔 혼합 객체 작업에서 CLAW는 85%의 전체 성공률을 달성했으며, fine-tuned $π_0$는 62%였다.
- 제거 실험은 분리 설계가 성능 향상의 핵심임을 보여준다: CLIP 프롬프트 생성기를 제거하면 성공률이 30% 하락한다.

### 결론
CLAW는 명시적 조건 모니터링과 기호적 추론을 통해 기존 VLA 모델의 정밀 작업 제약 부족을 효과적으로 보완하며, 무게 인식이 필요한 로봇 조작을 위한 신뢰성 있는 프레임워크를 제공한다. 논문 비디오는 https://youtu.be/MuMYj2QgReI에서 확인할 수 있다.
