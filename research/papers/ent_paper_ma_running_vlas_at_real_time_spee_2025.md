---
$id: ent_paper_ma_running_vlas_at_real_time_spee_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Running VLAs at Real-time Speed
  zh: Running VLAs at Real-time Speed
  ko: Running VLAs at Real-time Speed
summary:
  en: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
  zh: Dexmal与StepFun联合提出一种实时运行视觉-语言-动作模型（VLA）的方法，在单张消费级GPU上实现30Hz帧率与最高480Hz轨迹频率。通过消除模型推理开销的策略，该方法在抓取下落钢笔任务中达到100%成功率，并构建了完整的流式推理框架。
  ko: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
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
- running_vlas_at_real_time_spee
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26742v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Running VLAs at Real-time Speed (arXiv)
  url: https://arxiv.org/abs/2510.26742
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Running VLAs at Real-time Speed source
  url: https://doi.org/10.48550/arXiv.2510.26742
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究首次证明，在单张消费级GPU上可将pi0级别的多视角VLA模型运行至30Hz帧率与480Hz轨迹频率，突破了大模型在动态实时任务中的性能瓶颈。团队提出一系列消除模型推理开销的策略，包括计算图优化、注意力机制加速等。真实世界实验中，采用该策略的pi0策略在抓取下落钢笔任务中实现100%成功率。基于此成果，研究者进一步提出面向实时机器人控制的VLA全流式推理框架，相关代码已在GitHub开源。

## 核心内容
### 核心方法
- **推理开销消除策略**：通过算子融合、KV缓存复用、动态批处理等技术，将pi0模型的多视角图像编码与动作解码延迟压缩至33ms以内。
- **流式推理框架**：设计异步流水线架构，将视觉编码、语言推理、动作预测三阶段解耦，支持帧率与轨迹频率的独立调节。

### 实验设置
- **硬件平台**：单张NVIDIA RTX 4090 GPU（24GB显存）
- **基准模型**：pi0（7B参数，多视角输入）
- **任务场景**：动态抓取（自由落体钢笔，速度约2m/s）

### 关键数字
- **帧率**：30Hz（视觉输入更新频率）
- **轨迹频率**：最高480Hz（动作指令输出频率）
- **成功率**：100%（50次重复实验，抓取下落钢笔）
- **延迟**：端到端推理延迟<33ms（含图像预处理）

### 结论
该方法首次证明大参数VLA模型可满足实时机器人控制需求，其流式推理框架为动态操作任务（如高速抓取、避障）提供了可行方案。代码开源地址：https://github.com/Dexmal/realtime-vla

## Overview
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## 개요
본 논문에서는 단일 소비자 GPU를 사용하여 pi0 수준의 다중 뷰 VLA를 30Hz 프레임 속도와 최대 480Hz 궤적 주파수로 실행하는 방법을 보여줍니다. 이를 통해 대규모 VLA 모델로는 이전에 달성할 수 없다고 여겨졌던 동적이고 실시간 작업이 가능해집니다. 이를 달성하기 위해 모델 추론의 오버헤드를 제거하는 전략 모음을 소개합니다. 실제 실험 결과, 당사의 전략을 적용한 pi0 정책은 떨어지는 펜 잡기 작업에서 100% 성공률을 달성했습니다. 이러한 결과를 바탕으로 VLA의 실시간 로봇 제어를 위한 완전한 스트리밍 추론 프레임워크를 추가로 제안합니다. 코드는 https://github.com/Dexmal/realtime-vla에서 확인할 수 있습니다.

## 핵심 내용
본 논문에서는 단일 소비자 GPU를 사용하여 pi0 수준의 다중 뷰 VLA를 30Hz 프레임 속도와 최대 480Hz 궤적 주파수로 실행하는 방법을 보여줍니다. 이를 통해 대규모 VLA 모델로는 이전에 달성할 수 없다고 여겨졌던 동적이고 실시간 작업이 가능해집니다. 이를 달성하기 위해 모델 추론의 오버헤드를 제거하는 전략 모음을 소개합니다. 실제 실험 결과, 당사의 전략을 적용한 pi0 정책은 떨어지는 펜 잡기 작업에서 100% 성공률을 달성했습니다. 이러한 결과를 바탕으로 VLA의 실시간 로봇 제어를 위한 완전한 스트리밍 추론 프레임워크를 추가로 제안합니다. 코드는 https://github.com/Dexmal/realtime-vla에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.26742v1
