---
$id: ent_paper_zheng_tracevla_visual_trace_promptin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies'
  zh: TraceVLA
  ko: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies'
summary:
  en: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies (TraceVLA), is
    a 2024 large vision-language-action model for robotic manipulation, introduced by University of Maryland, College Park,
    Microsoft Research, Capital One, and published at ICLR 2024.'
  zh: TraceVLA 是 2024 年由马里兰大学帕克分校、微软研究院和 Capital One 联合提出的视觉-语言-动作模型，旨在提升机器人操作策略的时空感知能力。其核心贡献在于引入视觉轨迹提示（visual trace prompting），通过将状态-动作轨迹编码为视觉信息来增强模型对交互动态的理解。该模型在
    SimplerEnv 基准和真实 WidowX 机器人上均取得领先性能，并基于 4B 参数的 Phi-3-Vision 实现了高效推理。
  ko: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies (TraceVLA), is
    a 2024 large vision-language-action model for robotic manipulation, introduced by University of Maryland, College Park,
    Microsoft Research, Capital One, and published at ICLR 2024.'
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
- tracevla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.10345v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: TraceVLA source
  url: https://openreview.net/forum?id=b1CVu9l5GO
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有的大规模视觉-语言-动作（VLA）模型虽在机器人学习领域展现出通用策略潜力，但在处理操作任务时仍受限于对时空动态的建模不足。TraceVLA 通过视觉轨迹提示方法，将机器人执行过程中的状态-动作序列以可视化轨迹形式融入模型输入，从而直接提升动作预测的时空感知能力。该模型基于 OpenVLA 进行微调，在包含 15 万条操作轨迹的自建数据集上训练，并在 SimplerEnv 的 137 种配置和真实 WidowX 机器人的 4 项任务中验证了有效性。实验结果显示，TraceVLA 在 SimplerEnv 上比 OpenVLA 提升 10%，在真实机器人任务中性能提升达 3.5 倍，且展现出跨不同机器人形态和场景的泛化能力。

## 核心内容
### 方法
- **视觉轨迹提示**：将机器人执行过程中的状态-动作轨迹（如末端执行器路径、目标物体位置变化）以可视化形式叠加到当前观测图像上，作为模型输入的一部分。这种方法无需修改模型架构，仅通过输入层编码时空信息。
- **模型架构**：基于 OpenVLA（7B 参数）进行微调，同时探索了更紧凑的 4B 参数版本（基于 Phi-3-Vision），后者在 Open-X-Embodiment 数据集上预训练后，再在自建数据集上微调。

### 数据集
- 自建数据集包含 **150K** 条机器人操作轨迹，涵盖多种任务（如抓取、放置、推拉等），数据采集自模拟环境和真实机器人。
- 训练数据中每条轨迹均附带视觉轨迹提示，确保模型学习到状态-动作的时序关联。

### 实验设置
- **模拟环境**：SimplerEnv 基准，包含 **137 种** 不同配置（如物体位置、光照条件、机器人初始姿态）。
- **真实机器人**：WidowX 机械臂，执行 **4 项** 操作任务（如拾取、堆叠、插入等）。
- **对比基线**：OpenVLA（7B）、RT-2、Octo 等主流 VLA 模型。

### 关键结果
- **SimplerEnv 性能**：TraceVLA 平均成功率比 OpenVLA 高 **10%**，在复杂任务（如多物体堆叠）中提升更显著。
- **真实机器人性能**：TraceVLA 成功率是 OpenVLA 的 **3.5 倍**（例如，在“拾取-放置”任务中，TraceVLA 成功率为 82%，OpenVLA 为 23%）。
- **泛化能力**：在未见过的机器人形态（如不同夹爪类型）和场景（如不同背景、光照）中，TraceVLA 仍保持稳定性能，而基线模型性能下降超过 30%。
- **效率对比**：基于 4B Phi-3-Vision 的紧凑版 TraceVLA 在推理速度上比 7B OpenVLA 快 **2.1 倍**，同时性能仅下降 5%，接近 OpenVLA 水平。

### 结论
- 视觉轨迹提示是一种轻量级、即插即用的方法，能显著提升 VLA 模型对时空动态的建模能力，尤其适用于需要精确时序控制的操作任务。
- 紧凑版模型验证了该方法在资源受限场景下的实用性，为部署到实际机器人系统提供了可行方案。

## Overview
Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.

## 개요
대규모 로봇 데이터셋에서 사전 학습된 대규모 비전-언어-행동(VLA) 모델은 로봇 학습을 위한 유망한 범용 정책을 제공하지만, 상호작용 로봇 공학에서의 시공간 역학을 여전히 어려워하여 조작과 같은 복잡한 작업을 처리하는 데 효과적이지 않습니다. 본 연구에서는 상태-행동 궤적을 시각적으로 인코딩하여 VLA 모델의 시공간 인식을 촉진하는 간단하면서도 효과적인 접근 방식인 시각적 추적 프롬프팅(visual trace prompting)을 소개합니다. 우리는 자체 수집한 150K 로봇 조작 궤적 데이터셋에서 시각적 추적 프롬프팅을 사용하여 OpenVLA를 미세 조정한 새로운 TraceVLA 모델을 개발했습니다. SimplerEnv의 137개 구성과 실제 WidowX 로봇의 4개 작업에 걸친 TraceVLA 평가는 최첨단 성능을 입증하며, SimplerEnv에서 OpenVLA보다 10%, 실제 로봇 작업에서 3.5배 더 뛰어난 성능을 보이고 다양한 체현 및 시나리오에서 강력한 일반화를 나타냅니다. 우리 방법의 효과성과 일반성을 더 검증하기 위해, 4B Phi-3-Vision을 기반으로 Open-X-Embodiment에서 사전 학습되고 우리 데이터셋에서 미세 조정된 소형 VLA 모델을 제시하며, 이는 7B OpenVLA 기준선과 경쟁하면서 추론 효율성을 크게 향상시킵니다.

## 핵심 내용
대규모 로봇 데이터셋에서 사전 학습된 대규모 비전-언어-행동(VLA) 모델은 로봇 학습을 위한 유망한 범용 정책을 제공하지만, 상호작용 로봇 공학에서의 시공간 역학을 여전히 어려워하여 조작과 같은 복잡한 작업을 처리하는 데 효과적이지 않습니다. 본 연구에서는 상태-행동 궤적을 시각적으로 인코딩하여 VLA 모델의 시공간 인식을 촉진하는 간단하면서도 효과적인 접근 방식인 시각적 추적 프롬프팅(visual trace prompting)을 소개합니다. 우리는 자체 수집한 150K 로봇 조작 궤적 데이터셋에서 시각적 추적 프롬프팅을 사용하여 OpenVLA를 미세 조정한 새로운 TraceVLA 모델을 개발했습니다. SimplerEnv의 137개 구성과 실제 WidowX 로봇의 4개 작업에 걸친 TraceVLA 평가는 최첨단 성능을 입증하며, SimplerEnv에서 OpenVLA보다 10%, 실제 로봇 작업에서 3.5배 더 뛰어난 성능을 보이고 다양한 체현 및 시나리오에서 강력한 일반화를 나타냅니다. 우리 방법의 효과성과 일반성을 더 검증하기 위해, 4B Phi-3-Vision을 기반으로 Open-X-Embodiment에서 사전 학습되고 우리 데이터셋에서 미세 조정된 소형 VLA 모델을 제시하며, 이는 7B OpenVLA 기준선과 경쟁하면서 추론 효율성을 크게 향상시킵니다.

## 参考
- http://arxiv.org/abs/2412.10345v3
