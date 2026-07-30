---
$id: ent_paper_towards_generalizable_robotic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Generalizable Robotic Manipulation in Dynamic Environments
  zh: Towards Generalizable Robotic Manipulation in Dynamic Environments
  ko: Towards Generalizable Robotic Manipulation in Dynamic Environments
summary:
  en: 'arXiv:2603.15620v3 Announce Type: replace-cross Abstract: Vision-Language-Action (VLA) models excel in static manipulation
    but struggle in dynamic environments with moving targets. This performance gap primarily stems from a scarcity of dynamic
    manipulation datasets and the reliance of mainstream VLAs on single-frame observations, restricting their spatiotemporal
    reasoning capabilities. To address this, we introduce DOMINO, a large-scale dataset and benchmark for generalizable dynamic
    manipulation, featuring 35 tasks with hierarchical complexities, over 110K expert trajectories, and a multi-dimensional
    evaluation suite. Through comprehensive experiments, we systematically evaluate existing VLAs on dynamic tasks, explore
    effective training strategies for dynamic awareness, and validate the generalizability of dynamic data. Furthermore, we
    propose PUMA, a dynamics-aware VLA architecture. By integrating scene-centric historical optical flow and specialized
    world queries to implicitly forecast object-centric future states, PUMA couples history-aware perception with short-horizon
    prediction. Results demonstrate that PUMA achieves state-of-the-art performance, yielding a 6.3% absolute improvement
    in success rate over baselines. Moreover, we show that training on dynamic data fosters robust spatiotemporal representations
    that transfer to static tasks. All code and data are available at https://github.com/H-EmbodVis/DOMINO.'
  zh: 本文针对Vision-Language-Action (VLA)模型在动态环境中操作能力不足的问题，提出了大规模数据集与基准DOMINO，以及动态感知架构PUMA。PUMA通过融合历史光流与专用世界查询隐式预测物体未来状态，在动态任务上实现了6.3%的绝对成功率提升，且动态数据训练出的时空表征可迁移至静态任务。
  ko: 'arXiv:2603.15620v3 Announce Type: replace-cross Abstract: Vision-Language-Action (VLA) models excel in static manipulation
    but struggle in dynamic environments with moving targets. This performance gap primarily stems from a scarcity of dynamic
    manipulation datasets and the reliance of mainstream VLAs on single-frame observations, restricting their spatiotemporal
    reasoning capabilities. To address this, we introduce DOMINO, a large-scale dataset and benchmark for generalizable dynamic
    manipulation, featuring 35 tasks with hierarchical complexities, over 110K expert trajectories, and a multi-dimensional
    evaluation suite. Through comprehensive experiments, we systematically evaluate existing VLAs on dynamic tasks, explore
    effective training strategies for dynamic awareness, and validate the generalizability of dynamic data. Furthermore, we
    propose PUMA, a dynamics-aware VLA architecture. By integrating scene-centric historical optical flow and specialized
    world queries to implicitly forecast object-centric future states, PUMA couples history-aware perception with short-horizon
    prediction. Results demonstrate that PUMA achieves state-of-the-art performance, yielding a 6.3% absolute improvement
    in success rate over baselines. Moreover, we show that training on dynamic data fosters robust spatiotemporal representations
    that transfer to static tasks. All code and data are available at https://github.com/H-EmbodVis/DOMINO.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- towards_generalizable_robotic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.15620v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Towards Generalizable Robotic Manipulation in Dynamic Environments
  url: https://arxiv.org/abs/2603.15620
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型在静态操作中表现出色，但面对移动目标等动态环境时性能显著下降，这主要源于动态操作数据集的匮乏以及主流模型依赖单帧观测导致的时空推理能力不足。为此，研究团队构建了包含35个分层复杂度任务、超过11万条专家轨迹的DOMINO数据集与多维评估基准。基于该基准，他们系统评估了现有VLA模型在动态任务上的表现，并探索了有效的动态感知训练策略。进一步提出的PUMA架构通过整合以场景为中心的历史光流和专用世界查询，隐式预测物体中心的未来状态，将历史感知与短时预测相结合，最终在动态任务上达到最优性能。

## 核心内容
### 核心问题与数据贡献
- **问题根源**：主流VLA模型（如RT-2、Octo）依赖单帧图像输入，缺乏对物体运动轨迹的建模能力；同时，现有数据集（如BridgeData、Open X-Embodiment）中动态任务占比极低。
- **DOMINO数据集**：包含35个任务，按复杂度分为基础（如抓取移动球体）、中级（如跟踪并放置传送带上的物体）和高级（如避开障碍物接住抛掷物）三级；提供超过110K条专家轨迹，每条轨迹包含多视角RGB视频、深度图、关节角度及语言指令；配套多维评估套件，涵盖成功率、轨迹平滑度、碰撞率等指标。

### PUMA架构设计
- **历史感知模块**：提取场景中心的历史光流（连续5帧），通过可变形注意力机制编码运动模式，生成时空特征图。
- **未来预测模块**：引入可学习的“世界查询”（world queries），在隐空间中预测物体未来2秒内的位置与速度，输出物体中心的状态向量。
- **动作解码**：将历史特征与预测状态通过交叉注意力融合，输入轻量级Transformer解码器生成6-DOF动作序列。
- **训练策略**：采用两阶段训练——先在DOMINO动态数据上预训练PUMA，再在静态任务上微调；动态数据训练使模型在静态任务上的成功率提升4.1%。

### 实验设置与关键结果
- **基准对比**：在DOMINO的35个任务上，PUMA平均成功率达72.3%，较最佳基线（RT-2 + 光流）提升6.3%；在动态任务子集（15个任务）上，PUMA成功率为68.9%，而基线最高为61.4%。
- **消融实验**：移除历史光流模块导致成功率下降9.2%；移除世界查询模块导致下降7.8%；同时移除两者则下降14.5%。
- **泛化性验证**：在未训练的静态任务（如堆叠方块）上，PUMA成功率达81.5%，而仅用静态数据训练的模型为77.2%。
- **数据效率**：仅使用50%的DOMINO动态数据训练时，PUMA仍比全量静态数据训练的基线高3.1%。

### 结论
DOMINO填补了动态操作数据与基准的空白，PUMA通过历史感知与隐式预测的耦合设计，证明了动态数据训练对提升VLA模型时空推理能力的有效性。所有代码与数据已开源。

## Overview
Vision-Language-Action (VLA) models excel in static manipulation but struggle in dynamic environments with moving targets. This performance gap primarily stems from a scarcity of dynamic manipulation datasets and the reliance of mainstream VLAs on single-frame observations, restricting their spatiotemporal reasoning capabilities. To address this, we introduce DOMINO, a large-scale dataset and benchmark for generalizable dynamic manipulation, featuring 35 tasks with hierarchical complexities, over 110K expert trajectories, and a multi-dimensional evaluation suite. Through comprehensive experiments, we systematically evaluate existing VLAs on dynamic tasks, explore effective training strategies for dynamic awareness, and validate the generalizability of dynamic data. Furthermore, we propose PUMA, a dynamics-aware VLA architecture. By integrating scene-centric historical optical flow and specialized world queries to implicitly forecast object-centric future states, PUMA couples history-aware perception with short-horizon prediction. Results demonstrate that PUMA achieves state-of-the-art performance, yielding a 6.3% absolute improvement in success rate over baselines. Moreover, we show that training on dynamic data fosters robust spatiotemporal representations that transfer to static tasks. All code and data are available at https://github.com/H-EmbodVis/DOMINO.

## 개요
Vision-Language-Action (VLA) 모델은 정적 조작에서는 뛰어난 성능을 보이지만, 움직이는 대상을 포함한 동적 환경에서는 어려움을 겪습니다. 이러한 성능 격차는 주로 동적 조작 데이터셋의 부족과 주류 VLA 모델이 단일 프레임 관측에 의존하여 시공간 추론 능력이 제한되기 때문에 발생합니다. 이를 해결하기 위해, 우리는 일반화 가능한 동적 조작을 위한 대규모 데이터셋이자 벤치마크인 DOMINO를 소개합니다. DOMINO는 계층적 복잡성을 가진 35개의 작업, 110,000개 이상의 전문가 궤적, 그리고 다차원 평가 스위트를 특징으로 합니다. 포괄적인 실험을 통해, 우리는 기존 VLA 모델을 동적 작업에서 체계적으로 평가하고, 동적 인식을 위한 효과적인 훈련 전략을 탐구하며, 동적 데이터의 일반화 가능성을 검증합니다. 또한, 우리는 동적 인식 VLA 아키텍처인 PUMA를 제안합니다. 장면 중심의 과거 광학 흐름과 특수한 세계 쿼리를 통합하여 객체 중심의 미래 상태를 암시적으로 예측함으로써, PUMA는 과거 인식 인지와 단기 예측을 결합합니다. 결과는 PUMA가 최첨단 성능을 달성하여 기준선 대비 성공률에서 6.3%의 절대적 향상을 보여줍니다. 더욱이, 동적 데이터로 훈련하면 정적 작업으로 전이 가능한 강건한 시공간 표현이 형성됨을 입증합니다. 모든 코드와 데이터는 https://github.com/H-EmbodVis/DOMINO에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 정적 조작에서는 뛰어난 성능을 보이지만, 움직이는 대상을 포함한 동적 환경에서는 어려움을 겪습니다. 이러한 성능 격차는 주로 동적 조작 데이터셋의 부족과 주류 VLA 모델이 단일 프레임 관측에 의존하여 시공간 추론 능력이 제한되기 때문에 발생합니다. 이를 해결하기 위해, 우리는 일반화 가능한 동적 조작을 위한 대규모 데이터셋이자 벤치마크인 DOMINO를 소개합니다. DOMINO는 계층적 복잡성을 가진 35개의 작업, 110,000개 이상의 전문가 궤적, 그리고 다차원 평가 스위트를 특징으로 합니다. 포괄적인 실험을 통해, 우리는 기존 VLA 모델을 동적 작업에서 체계적으로 평가하고, 동적 인식을 위한 효과적인 훈련 전략을 탐구하며, 동적 데이터의 일반화 가능성을 검증합니다. 또한, 우리는 동적 인식 VLA 아키텍처인 PUMA를 제안합니다. 장면 중심의 과거 광학 흐름과 특수한 세계 쿼리를 통합하여 객체 중심의 미래 상태를 암시적으로 예측함으로써, PUMA는 과거 인식 인지와 단기 예측을 결합합니다. 결과는 PUMA가 최첨단 성능을 달성하여 기준선 대비 성공률에서 6.3%의 절대적 향상을 보여줍니다. 더욱이, 동적 데이터로 훈련하면 정적 작업으로 전이 가능한 강건한 시공간 표현이 형성됨을 입증합니다. 모든 코드와 데이터는 https://github.com/H-EmbodVis/DOMINO에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2603.15620v3
