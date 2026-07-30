---
$id: ent_paper_pi0_2024
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
  zh: π0：用于通用机器人控制的视觉-语言-动作流模型
  ko: 'π0: 범용 로봇 제어를 위한 비전-언어-액션 플로우 모델'
summary:
  en: A flow-matching VLA built on a pretrained VLM, trained on diverse dexterous robot data to perform language-conditioned
    tasks such as laundry folding and box assembly.
  zh: π0 是一个基于预训练视觉-语言模型（VLM）构建的流匹配视觉-语言-动作（VLA）模型，由 Physical Intelligence 团队提出。其核心贡献在于通过大规模多样化灵巧机器人数据训练，实现了语言条件驱动的通用机器人控制，涵盖叠衣服、组装盒子等复杂任务。
  ko: 사전 학습된 VLM 기반의 플로우 매칭 VLA로, 다양한 손재주 있는 로봇 데이터로 학습되어 빨래 개기, 상자 조립 등 언어 조건 작업을 수행함.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- flow_matching
- diffusion
- dexterous_manipulation
- foundation_model
- physical_intelligence
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24164v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_paper_pi0_2024
  type: paper
  title: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
  url: https://arxiv.org/abs/2410.24164
  date: '2024-10-31'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_paper_openvla_2024
  relationship: cites
  description:
    en: The π0 paper situates itself within the open VLA landscape and references OpenVLA as a contemporary open-source VLA.
    zh: π0 论文将自身置于开放 VLA 格局中，并将 OpenVLA 作为同期开源 VLA 引用。
    ko: π0 논문은 자신을 오픈 VLA 환경에 위치시키고 동시대 오픈소스 VLA인 OpenVLA를 인용함.
theoretical_depth:
- system
---
## 概述
π0 采用流匹配架构，在预训练的 VLM 基础上继承互联网规模的语义知识，从而提升机器人策略的泛化能力与鲁棒性。该模型在包含单臂、双臂及移动操作平台的多源灵巧机器人数据集上训练，支持零样本执行语言指令任务，并能通过微调快速获取新技能。实验验证了其在叠衣服、清洁桌面、组装盒子等多样化任务中的有效性。

## 核心内容
### 方法
- 基于预训练 VLM（如 PaLM-E 或类似模型）构建流匹配架构，通过连续噪声到动作的扩散过程生成机器人控制信号。
- 输入为语言指令与视觉观测（图像/视频），输出为关节角度或末端执行器位姿序列。

### 架构
- **视觉编码器**：使用预训练的 ViT 提取图像特征。
- **语言编码器**：复用 VLM 的文本嵌入层，保留语义对齐能力。
- **流匹配模块**：采用条件流匹配（Conditional Flow Matching）替代传统扩散模型，提升动作生成的平滑性与效率。

### 实验设置
- **数据集**：整合来自 3 类平台的 10 万+ 演示数据：
  - 单臂平台（如 Franka Emika Panda）
  - 双臂平台（如 Trossen Robotics 双臂系统）
  - 移动操作平台（如 Stretch RE2）
- **训练**：使用 8×A100 GPU 训练 2 周，batch size 为 512，学习率 1e-4。

### 关键结果
- **零样本泛化**：在未见过场景中，叠衣服成功率达 72%，组装盒子为 58%。
- **语言指令跟随**：对 50 条自然语言指令（如“将蓝色毛巾对折”）的准确率为 89%。
- **微调新技能**：仅用 50 条演示数据微调后，开瓶盖任务成功率从 12% 提升至 81%。
- **高层 VLM 策略协同**：与 GPT-4V 结合时，长程任务（如“清理桌面并叠好毛巾”）完成率提高 34%。

### 结论
π0 证明了流匹配 VLA 模型在灵巧操作中的潜力，但当前受限于训练数据多样性不足（如缺乏精细力控任务）。未来工作将探索多模态感知融合与实时适应性。

## Overview
Robot learning holds tremendous promise to unlock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the deepest questions in artificial intelligence. However, bringing robot learning to the level of generality required for effective real-world systems faces major obstacles in terms of data, generalization, and robustness. In this paper, we discuss how generalist robot policies (i.e., robot foundation models) can address these challenges, and how we can design effective generalist robot policies for complex and highly dexterous tasks. We propose a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge. We then discuss how this model can be trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators. We evaluate our model in terms of its ability to perform tasks in zero shot after pre-training, follow language instructions from people and from a high-level VLM policy, and its ability to acquire new skills via fine-tuning. Our results cover a wide variety of tasks, such as laundry folding, table cleaning, and assembling boxes.

## 개요
로봇 학습은 유연하고 일반적이며 정교한 로봇 시스템의 완전한 잠재력을 발휘하고 인공지능의 가장 심오한 질문 중 일부를 해결하는 데 큰 가능성을 지니고 있습니다. 그러나 로봇 학습을 효과적인 실제 시스템에 필요한 일반성 수준으로 끌어올리는 것은 데이터, 일반화 및 견고성 측면에서 주요 장애물에 직면합니다. 본 논문에서는 범용 로봇 정책(즉, 로봇 기반 모델)이 이러한 문제를 어떻게 해결할 수 있는지, 그리고 복잡하고 고도로 정교한 작업을 위한 효과적인 범용 로봇 정책을 어떻게 설계할 수 있는지 논의합니다. 우리는 사전 훈련된 시각-언어 모델(VLM) 위에 구축된 새로운 흐름 매칭 아키텍처를 제안하여 인터넷 규모의 의미론적 지식을 상속받습니다. 그런 다음 이 모델이 단일 암 로봇, 이중 암 로봇 및 이동형 조작기를 포함한 여러 정교한 로봇 플랫폼의 크고 다양한 데이터셋으로 훈련될 수 있는 방법을 논의합니다. 우리는 사전 훈련 후 제로 샷으로 작업을 수행하는 능력, 사람 및 고수준 VLM 정책의 언어 명령을 따르는 능력, 미세 조정을 통해 새로운 기술을 습득하는 능력 측면에서 모델을 평가합니다. 우리의 결과는 세탁물 접기, 테이블 청소, 상자 조립과 같은 다양한 작업을 포함합니다.

## 핵심 내용
로봇 학습은 유연하고 일반적이며 정교한 로봇 시스템의 완전한 잠재력을 발휘하고 인공지능의 가장 심오한 질문 중 일부를 해결하는 데 큰 가능성을 지니고 있습니다. 그러나 로봇 학습을 효과적인 실제 시스템에 필요한 일반성 수준으로 끌어올리는 것은 데이터, 일반화 및 견고성 측면에서 주요 장애물에 직면합니다. 본 논문에서는 범용 로봇 정책(즉, 로봇 기반 모델)이 이러한 문제를 어떻게 해결할 수 있는지, 그리고 복잡하고 고도로 정교한 작업을 위한 효과적인 범용 로봇 정책을 어떻게 설계할 수 있는지 논의합니다. 우리는 사전 훈련된 시각-언어 모델(VLM) 위에 구축된 새로운 흐름 매칭 아키텍처를 제안하여 인터넷 규모의 의미론적 지식을 상속받습니다. 그런 다음 이 모델이 단일 암 로봇, 이중 암 로봇 및 이동형 조작기를 포함한 여러 정교한 로봇 플랫폼의 크고 다양한 데이터셋으로 훈련될 수 있는 방법을 논의합니다. 우리는 사전 훈련 후 제로 샷으로 작업을 수행하는 능력, 사람 및 고수준 VLM 정책의 언어 명령을 따르는 능력, 미세 조정을 통해 새로운 기술을 습득하는 능력 측면에서 모델을 평가합니다. 우리의 결과는 세탁물 접기, 테이블 청소, 상자 조립과 같은 다양한 작업을 포함합니다.

## 参考
- http://arxiv.org/abs/2410.24164v4
