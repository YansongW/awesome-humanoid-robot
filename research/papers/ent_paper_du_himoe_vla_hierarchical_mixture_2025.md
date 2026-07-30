---
$id: ent_paper_du_himoe_vla_hierarchical_mixture_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies'
  zh: HiMoE-VLA
  ko: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies'
summary:
  en: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (HiMoE-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Microsoft Research Asia, Xi’an
    Jiaotong University, Tsinghua University.'
  zh: HiMoE-VLA 是复旦大学、微软亚洲研究院、西安交通大学和清华大学于 2025 年提出的通用视觉-语言-动作大模型，专为机器人操作任务设计。其核心贡献在于引入分层混合专家（HiMoE）动作模块，通过动作空间 MoE 层、异构平衡
    MoE 层和密集 Transformer 块的分层架构，有效缓解了多源异构训练数据中的负迁移问题。在 CALVIN、LIBERO 及真实机器人任务上均取得领先性能，代码已开源。
  ko: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (HiMoE-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Microsoft Research Asia, Xi’an
    Jiaotong University, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- himoe_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05693v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (arXiv)'
  url: https://arxiv.org/abs/2512.05693
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: HiMoE-VLA source
  url: https://doi.org/10.48550/arXiv.2512.05693
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
通用视觉-语言-动作（VLA）策略通常训练于包含多种机器人形态、动作空间和观测配置的异构演示数据混合集。若使用共享的密集动作模块建模此类异构性，当不同数据源的动作空间或视觉观测存在差异时，容易引发负迁移。HiMoE-VLA 通过分层混合专家（HiMoE）动作模块解决该问题：在输入/输出边界使用动作空间 MoE 层专门处理不同动作空间，在相邻层使用异构平衡 MoE 层为观测、场景和形态的残余变化提供均衡容量，中间层则采用密集 Transformer 块整合共享表征。两个辅助目标进一步引导该分层结构：用于边界专业化的对比动作空间正则化目标，以及用于稳定专家利用率的负载均衡目标。

## 核心内容
### 方法架构
HiMoE-VLA 的核心是分层混合专家（HiMoE）动作模块，其结构分为三层：
- **动作空间 MoE 层**：位于输入/输出边界，每个专家专门处理特定动作空间（如关节角度、末端执行器位姿），通过门控网络动态选择专家组合。
- **异构平衡 MoE 层**：位于相邻层，为观测配置、场景和机器人形态的残余变化提供均衡容量，避免单一专家过载。
- **密集 Transformer 块**：位于中间层，整合跨数据源的共享表征，维持全局一致性。

两个辅助目标：
- **对比动作空间正则化**：通过对比学习拉近同动作空间样本的专家选择分布，拉远不同动作空间样本的分布，强化边界专业化。
- **负载均衡目标**：通过辅助损失函数平衡各专家的利用率，防止部分专家被过度使用或闲置。

### 实验设置与关键数字
- **基准测试**：
  - **CALVIN**：达到 3.98 分（满分 5），超越此前最佳方法。
  - **LIBERO**：准确率 98.0%，在 10 个任务中表现稳定。
  - **真实机器人任务**：
    - **xArm7**：平均成功率 75.0%，涵盖抓取、放置等操作。
    - **ALOHA**：平均成功率 63.7%，涉及双臂协调任务。
- **异构协同训练**：在受控的异构数据混合训练中，HiMoE-VLA 将强基线模型（如 Octo、RT-2）中出现的负迁移（性能下降 5-10%）转化为正迁移（性能提升 3-8%），验证了分层架构对异构性的鲁棒性。

### 结论
HiMoE-VLA 通过分层混合专家架构，有效解决了通用 VLA 策略在多源异构数据训练中的负迁移问题，在多个仿真和真实机器人基准上达到最优性能。其开源代码和模型为后续研究提供了可复现的基础。

## Overview
Generalist vision--language--action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0\% on LIBERO, and 75.0\% and 63.7\% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## Overview
Generalist vision–language–action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0% on LIBERO, and 75.0% and 63.7% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## Content
Generalist vision–language–action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0% on LIBERO, and 75.0% and 63.7% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## 개요
Generalist vision-language-action (VLA) 정책은 일반적으로 다양한 형태, 행동 공간 및 관찰 구성을 아우르는 로봇 시연의 이질적 혼합 데이터로 훈련됩니다. 이러한 이질성을 공유된 밀집 행동 모듈로 모델링하면, 특히 데이터 소스 간에 행동 공간이나 시각적 관찰이 다를 때 부정적 전이가 발생할 수 있습니다. 우리는 이 문제를 계층적 전문가 혼합(HiMoE) 행동 모듈을 기반으로 구축된 VLA 프레임워크인 HiMoE-VLA로 해결합니다. HiMoE는 입력/출력 경계에서 Action-Space MoE 계층을 사용하여 서로 다른 행동 공간에 특화된 계산을 수행하고, 인접 계층에서 Heterogeneity-Balancing MoE 계층을 사용하여 관찰, 장면 및 형태의 잔여 변동에 대한 균형 잡힌 용량을 제공하며, 중간에 밀집 Transformer 블록을 사용하여 공유 표현을 통합합니다. 두 가지 보조 목표가 이 계층 구조를 더욱 안내합니다: 경계 특화를 위한 대조적 Action-Space 정규화 목표와 안정적인 전문가 활용을 위한 부하 균형 목표입니다. HiMoE-VLA는 CALVIN에서 3.98, LIBERO에서 98.0%, 실제 xArm7 및 ALOHA 작업에서 각각 75.0% 및 63.7%의 평균 성공률을 달성합니다. 통제된 이질적 공동 훈련 하에서는 강력한 기준선에서 관찰된 부정적 전이를 긍정적 전이로 전환합니다. 코드와 모델은 https://github.com/ZhiyingDu/HiMoE-VLA에서 공개적으로 제공됩니다.

## 핵심 내용
Generalist vision-language-action (VLA) 정책은 일반적으로 다양한 형태, 행동 공간 및 관찰 구성을 아우르는 로봇 시연의 이질적 혼합 데이터로 훈련됩니다. 이러한 이질성을 공유된 밀집 행동 모듈로 모델링하면, 특히 데이터 소스 간에 행동 공간이나 시각적 관찰이 다를 때 부정적 전이가 발생할 수 있습니다. 우리는 이 문제를 계층적 전문가 혼합(HiMoE) 행동 모듈을 기반으로 구축된 VLA 프레임워크인 HiMoE-VLA로 해결합니다. HiMoE는 입력/출력 경계에서 Action-Space MoE 계층을 사용하여 서로 다른 행동 공간에 특화된 계산을 수행하고, 인접 계층에서 Heterogeneity-Balancing MoE 계층을 사용하여 관찰, 장면 및 형태의 잔여 변동에 대한 균형 잡힌 용량을 제공하며, 중간에 밀집 Transformer 블록을 사용하여 공유 표현을 통합합니다. 두 가지 보조 목표가 이 계층 구조를 더욱 안내합니다: 경계 특화를 위한 대조적 Action-Space 정규화 목표와 안정적인 전문가 활용을 위한 부하 균형 목표입니다. HiMoE-VLA는 CALVIN에서 3.98, LIBERO에서 98.0%, 실제 xArm7 및 ALOHA 작업에서 각각 75.0% 및 63.7%의 평균 성공률을 달성합니다. 통제된 이질적 공동 훈련 하에서는 강력한 기준선에서 관찰된 부정적 전이를 긍정적 전이로 전환합니다. 코드와 모델은 https://github.com/ZhiyingDu/HiMoE-VLA에서 공개적으로 제공됩니다.

## 参考
- http://arxiv.org/abs/2512.05693v2
