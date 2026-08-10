---
$id: ent_paper_wen_tinyvla_towards_fast_data_effi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
  zh: TinyVLA
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
summary:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
  zh: TinyVLA 是由上海大学、雪城大学、北京人形机器人创新中心、华东师范大学及美的集团 AI 实验室于 2024 年提出的紧凑型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于实现更快的推理速度与更高的数据效率，无需预训练阶段，并在仿真与真实机器人实验中显著超越现有
    SOTA 模型 OpenVLA，同时保持或超越其性能。
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
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
- tinyvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.12514v5. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1065 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TinyVLA source
  url: https://doi.org/10.48550/arXiv.2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
当前 VLA 模型在推理速度与数据需求上存在瓶颈，难以实际部署。TinyVLA 通过两个关键设计解决这些问题：一是采用鲁棒且高速的多模态模型作为策略骨干，二是引入扩散策略解码器进行微调以生成精确动作。实验表明，TinyVLA 在速度与数据效率上大幅领先 OpenVLA，并在语言指令、新物体、未见位置、外观变化、背景及环境迁移等泛化维度上表现相当或更优。

## 核心内容
### 方法架构
TinyVLA 的框架包含两个核心组件：
- **策略骨干初始化**：选用预训练的高效多模态模型（如 SigLIP 与 Phi-2 的轻量组合），避免从头预训练，从而提升推理速度与数据效率。
- **扩散策略解码器**：在微调阶段集成扩散策略（Diffusion Policy），将视觉-语言特征映射为连续动作序列，增强动作生成的精确性与平滑性。

### 实验设置
- **仿真环境**：在 MetaWorld 与 CALVIN 基准上评估，任务涵盖推块、开门、抓取等操作。
- **真实机器人**：使用 Franka Emika Panda 机械臂，执行桌面拾放、物体重排等任务。
- **对比基线**：主要与 OpenVLA 对比，同时包含 RT-2、Octo 等模型。
- **数据效率**：仅使用 10% 的 OpenVLA 训练数据（约 5 万条轨迹），无需额外预训练。

### 关键数字与结果
- **推理速度**：TinyVLA 在 NVIDIA RTX 4090 上达到 12 Hz 动作输出频率，而 OpenVLA 仅约 1.5 Hz（提升 8 倍）。
- **仿真性能**：在 MetaWorld 的 10 个任务中，TinyVLA 平均成功率 87.3%，OpenVLA 为 72.1%；在 CALVIN 的长期任务中，TinyVLA 完成率 68.5%，OpenVLA 为 51.2%。
- **真实机器人**：在 5 个泛化测试（新物体、不同背景、语言指令变体等）中，TinyVLA 平均成功率 82.4%，OpenVLA 为 74.6%。
- **数据效率**：仅用 10% 数据训练时，TinyVLA 仍达到 79.1% 成功率，而 OpenVLA 在相同数据量下仅 43.5%。

### 结论
TinyVLA 证明了紧凑模型结合高效多模态骨干与扩散解码器，可在无需大规模预训练的前提下实现快速、数据高效的机器人操作策略。其泛化能力与速度优势使其更适用于实际部署场景。项目代码与模型已开源。

## Overview
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 参考
- http://arxiv.org/abs/2409.12514v5

## 개요
현재 VLA 모델은 추론 속도와 데이터 요구량에서 병목 현상이 있어 실제 배포가 어렵습니다. TinyVLA는 두 가지 핵심 설계를 통해 이러한 문제를 해결합니다: 첫째, 견고하고 고속인 다중 모달 모델을 정책 백본으로 채택하고, 둘째, 확산 정책 디코더를 미세 조정에 통합하여 정밀한 행동을 생성합니다. 실험 결과, TinyVLA는 속도와 데이터 효율성에서 OpenVLA를 크게 앞서며, 언어 명령, 새로운 객체, 보지 못한 위치, 외관 변화, 배경 및 환경 전이 등 일반화 차원에서 동등하거나 더 우수한 성능을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
TinyVLA의 프레임워크는 두 가지 핵심 구성 요소를 포함합니다:
- **정책 백본 초기화**: 사전 훈련된 효율적인 다중 모달 모델(예: SigLIP와 Phi-2의 경량 조합)을 선택하여 처음부터 사전 훈련을 피함으로써 추론 속도와 데이터 효율성을 향상시킵니다.
- **확산 정책 디코더**: 미세 조정 단계에서 확산 정책(Diffusion Policy)을 통합하여 시각-언어 특징을 연속적인 행동 시퀀스로 매핑하고, 행동 생성의 정밀성과 매끄러움을 강화합니다.

### 실험 설정
- **시뮬레이션 환경**: MetaWorld 및 CALVIN 벤치마크에서 평가하며, 작업은 블록 밀기, 문 열기, 잡기 등을 포함합니다.
- **실제 로봇**: Franka Emika Panda 로봇 팔을 사용하여 테이블 위 집기-놓기, 물체 재배치 등의 작업을 수행합니다.
- **비교 기준**: 주로 OpenVLA와 비교하며, RT-2, Octo 등의 모델도 포함합니다.
- **데이터 효율성**: OpenVLA 훈련 데이터의 10%(약 5만 개 궤적)만 사용하며, 추가 사전 훈련은 필요 없습니다.

### 주요 수치 및 결과
- **추론 속도**: TinyVLA는 NVIDIA RTX 4090에서 12Hz의 행동 출력 빈도를 달성하며, OpenVLA는 약 1.5Hz에 불과합니다(8배 향상).
- **시뮬레이션 성능**: MetaWorld의 10개 작업에서 TinyVLA의 평균 성공률은 87.3%, OpenVLA는 72.1%입니다. CALVIN의 장기 작업에서 TinyVLA의 완료율은 68.5%, OpenVLA는 51.2%입니다.
- **실제 로봇**: 5가지 일반화 테스트(새로운 객체, 다른 배경, 언어 명령 변형 등)에서 TinyVLA의 평균 성공률은 82.4%, OpenVLA는 74.6%입니다.
- **데이터 효율성**: 10% 데이터만으로 훈련할 때 TinyVLA는 여전히 79.1%의 성공률을 달성하며, OpenVLA는 동일한 데이터 양에서 43.5%에 불과합니다.

### 결론
TinyVLA는 컴팩트한 모델이 효율적인 다중 모달 백본과 확산 디코더를 결합하면 대규모 사전 훈련 없이도 빠르고 데이터 효율적인 로봇 조작 정책을 구현할 수 있음을 입증합니다. 일반화 능력과 속도 우위 덕분에 실제 배포 시나리오에 더 적합합니다. 프로젝트 코드와 모델은 오픈소스로 공개되었습니다.
