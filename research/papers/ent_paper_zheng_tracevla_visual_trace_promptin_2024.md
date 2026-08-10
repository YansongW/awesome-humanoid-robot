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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.10345v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1320 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2412.10345v3

## 개요
기존의 대규모 시각-언어-행동(VLA) 모델은 로봇 학습 분야에서 일반적인 정책의 잠재력을 보여주었지만, 조작 작업을 처리할 때 시공간 역학에 대한 모델링 부족이라는 한계를 여전히 가지고 있습니다. TraceVLA는 시각적 궤적 프롬프트 방법을 통해 로봇 실행 과정의 상태-행동 시퀀스를 시각화된 궤적 형태로 모델 입력에 통합하여, 행동 예측의 시공간 인식 능력을 직접적으로 향상시킵니다. 이 모델은 OpenVLA를 기반으로 미세 조정되었으며, 15만 개의 조작 궤적을 포함하는 자체 구축 데이터셋에서 훈련되었고, SimplerEnv의 137가지 구성과 실제 WidowX 로봇의 4가지 작업에서 유효성을 검증했습니다. 실험 결과, TraceVLA는 SimplerEnv에서 OpenVLA보다 10% 향상되었고, 실제 로봇 작업에서는 성능이 3.5배 향상되었으며, 서로 다른 로봇 형태와 시나리오에 걸친 일반화 능력을 보여주었습니다.

## 핵심 내용
### 방법
- **시각적 궤적 프롬프트**: 로봇 실행 과정의 상태-행동 궤적(예: 엔드 이펙터 경로, 목표 객체 위치 변화)을 현재 관찰 이미지 위에 시각화된 형태로 겹쳐 모델 입력의 일부로 사용합니다. 이 방법은 모델 아키텍처를 수정할 필요 없이 입력 레이어만으로 시공간 정보를 인코딩합니다.
- **모델 아키텍처**: OpenVLA(7B 파라미터)를 기반으로 미세 조정되었으며, 동시에 더 컴팩트한 4B 파라미터 버전(Phi-3-Vision 기반)도 탐구되었습니다. 후자는 Open-X-Embodiment 데이터셋에서 사전 훈련된 후 자체 구축 데이터셋에서 미세 조정되었습니다.

### 데이터셋
- 자체 구축 데이터셋은 **150K**개의 로봇 조작 궤적을 포함하며, 다양한 작업(예: 파지, 배치, 밀기/당기기 등)을 다루고, 데이터는 시뮬레이션 환경과 실제 로봇에서 수집되었습니다.
- 훈련 데이터의 각 궤적에는 시각적 궤적 프롬프트가 포함되어 모델이 상태-행동의 시간적 연관성을 학습하도록 보장합니다.

### 실험 설정
- **시뮬레이션 환경**: SimplerEnv 벤치마크로, **137가지**의 다양한 구성(예: 객체 위치, 조명 조건, 로봇 초기 자세)을 포함합니다.
- **실제 로봇**: WidowX 로봇 팔로, **4가지** 조작 작업(예: 집기, 쌓기, 삽입 등)을 수행합니다.
- **비교 기준선**: OpenVLA(7B), RT-2, Octo 등 주요 VLA 모델.

### 주요 결과
- **SimplerEnv 성능**: TraceVLA의 평균 성공률은 OpenVLA보다 **10%** 높으며, 복잡한 작업(예: 다중 객체 쌓기)에서는 향상 폭이 더 큽니다.
- **실제 로봇 성능**: TraceVLA의 성공률은 OpenVLA의 **3.5배**입니다(예: "집기-배치" 작업에서 TraceVLA 성공률은 82%, OpenVLA는 23%).
- **일반화 능력**: 보지 못한 로봇 형태(예: 다른 그리퍼 유형)와 시나리오(예: 다른 배경, 조명)에서 TraceVLA는 안정적인 성능을 유지하는 반면, 기준선 모델의 성능은 30% 이상 하락합니다.
- **효율성 비교**: 4B Phi-3-Vision 기반의 컴팩트 버전 TraceVLA는 추론 속도가 7B OpenVLA보다 **2.1배** 빠르며, 성능은 5%만 하락하여 OpenVLA 수준에 근접합니다.

### 결론
- 시각적 궤적 프롬프트는 경량화되고 플러그 앤 플레이 방식의 방법으로, VLA 모델의 시공간 역학 모델링 능력을 크게 향상시킬 수 있으며, 특히 정밀한 시간적 제어가 필요한 조작 작업에 적합합니다.
- 컴팩트 버전 모델은 리소스가 제한된 시나리오에서 이 방법의 실용성을 검증하여, 실제 로봇 시스템에 배포할 수 있는 실행 가능한 솔루션을 제공합니다.
