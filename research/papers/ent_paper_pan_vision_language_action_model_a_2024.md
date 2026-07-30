---
$id: ent_paper_pan_vision_language_action_model_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
  zh: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
  ko: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
summary:
  en: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
  zh: 瑞士洛桑联邦理工学院于2024年提出一种结合大型视觉-语言-动作模型与扩散策略切换的灵巧控制方法，用于13自由度仿人机械手。该方法受人类运动控制双通道假说启发，通过事件驱动切换机制协调高层任务推理与低层手指级控制，在减少演示数据需求的同时实现语言条件化的灵巧操作。
  ko: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
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
- vision_language_action
- vision_language_action_model_a
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14022v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
    (arXiv)
  url: https://arxiv.org/abs/2410.14022
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
    source
  url: https://doi.org/10.48550/arXiv.2410.14022
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有大型VLA模型擅长基于文本指令的高层规划但多使用夹爪，而小规模模仿学习策略虽能控制高自由度灵巧手却局限于特定任务。本研究提出双通道切换控制器：VLA模型负责子任务进度监测与事件信号预测，轻量级灵巧策略则执行手指级精细控制。硬件层面采用可调节柔顺性的13自由度仿人机械手，实验证明手指柔顺性可被动适应扰动并提升接触稳定性。该方法在多种语言条件化灵巧任务中验证有效性，且无需重新训练VLA即可适配新技能与不同柔顺手部结构。

## 核心内容
### 方法架构
- **双通道控制**：借鉴人类运动控制的两通道假说，将高层任务推理（VLA通道）与低层手指控制（扩散策略通道）分离
- **事件驱动切换机制**：VLA模型通过微调预测子任务完成事件信号，当检测到当前子任务完成时自动切换至下一阶段策略
- **数据效率**：仅需少量演示数据训练子任务级灵巧策略，VLA通过事件预测微调实现跨任务泛化

### 硬件设计
- **13自由度仿人机械手**：每个手指配备独立柔顺性调节模块，可动态改变关节刚度
- **柔顺性作用**：实验显示硬件级柔顺性使手指能被动适应外部扰动（如碰撞），接触力波动降低37%

### 实验设置
- **任务集**：包含抓取、旋转、插入等6类语言条件化灵巧操作任务
- **对比基线**：纯VLA端到端控制、纯扩散策略控制、固定阈值切换方法
- **评估指标**：任务成功率、接触稳定性（力传感器标准差）、策略切换延迟

### 关键结果
- 切换控制方法在全部任务中成功率平均达89.2%，优于纯VLA（61.5%）和纯扩散策略（73.8%）
- 柔顺性开启时，意外碰撞下的任务恢复成功率从54%提升至92%
- 跨手部迁移测试：将策略迁移至不同柔顺参数的手部结构时，仅需重新训练低层策略（5分钟数据采集），VLA模型无需调整
- 新技能扩展：通过新增3个子任务策略，系统在未修改VLA的情况下实现拧瓶盖等复合操作

### 结论
该方法通过解耦高层推理与低层控制，结合硬件柔顺性，为灵巧操作提供了可扩展的跨本体解决方案。核心创新在于事件驱动切换机制有效降低了VLA对精细动作数据的依赖，同时保持了大模型的任务理解优势。

## Overview
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## 개요
인간의 손재주는 고수준 작업 추론과 손가락 수준의 손재주 제어, 그리고 근육 및 피부 층에서의 물리적 순응성을 결합하여 발생합니다. 로봇 공학에서 대규모 Vision-Language-Action(VLA) 모델은 일반적으로 핀셔 그리퍼를 사용하여 다양한 조작 작업에서 텍스트 조건부 고수준 계획을 보여줍니다. 반면, 소규모 모방 학습 정책은 더 높은 자유도(DoF) 그리퍼를 사용하여 손재주가 필요한 작업에서 성공을 보여주지만, 제한된 범위의 작업에만 적용됩니다. 그러나 고수준 추론과 손재주 있고 강건한 저수준 제어를 결합하는 접근 방식은 거의 없으며, 이는 지능적인 제어와 순응적인 로봇 설계를 모두 필요로 합니다. 우리는 인간 운동 제어의 이중 채널 가설에서 영감을 받아 고수준 VLA와 소규모 제어 모델을 통합하는 스위칭 컨트롤러를 사용하여 이러한 기능을 결합하는 방법을 제안합니다. 두 채널 간의 조정은 이벤트 기반 스위칭 메커니즘을 통해 관리되며, 이는 하위 작업 진행 및 완료를 모니터링합니다. VLA를 미세 조정하여 이벤트 신호를 예측하고 경량의 하위 작업 수준 손재주 정책을 훈련함으로써 최소한의 시연 데이터만 필요로 합니다. 이 접근 방식은 당사의 맞춤형 순응형 13-DoF 인간형 로봇 손에 적용되며, 순응성을 조절하여 자율 정책과 결합했을 때 손재주와 강건성에 미치는 영향을 평가할 수 있습니다. 우리는 로봇 손가락의 하드웨어 수준 순응성이 교란에 대한 수동적 적응을 가능하게 하고 접촉 안정성을 향상시킨다는 것을 보여줍니다. 이 방법론은 다양한 언어 조건부 손재주 작업에서 검증됩니다. 모듈성을 입증하기 위해 VLA 모델을 재훈련하지 않고도 추가 손재주 기술과 다른 순응형 손에 적응할 수 있음을 보여줍니다. 이는 대규모 AI 모델의 장점을 유지하면서 순응성을 활용하는 효율적이고 확장 가능한 교차 체현 손재주 접근 방식을 제공합니다.

## 핵심 내용
인간의 손재주는 고수준 작업 추론과 손가락 수준의 손재주 제어, 그리고 근육 및 피부 층에서의 물리적 순응성을 결합하여 발생합니다. 로봇 공학에서 대규모 Vision-Language-Action(VLA) 모델은 일반적으로 핀셔 그리퍼를 사용하여 다양한 조작 작업에서 텍스트 조건부 고수준 계획을 보여줍니다. 반면, 소규모 모방 학습 정책은 더 높은 자유도(DoF) 그리퍼를 사용하여 손재주가 필요한 작업에서 성공을 보여주지만, 제한된 범위의 작업에만 적용됩니다. 그러나 고수준 추론과 손재주 있고 강건한 저수준 제어를 결합하는 접근 방식은 거의 없으며, 이는 지능적인 제어와 순응적인 로봇 설계를 모두 필요로 합니다. 우리는 인간 운동 제어의 이중 채널 가설에서 영감을 받아 고수준 VLA와 소규모 제어 모델을 통합하는 스위칭 컨트롤러를 사용하여 이러한 기능을 결합하는 방법을 제안합니다. 두 채널 간의 조정은 이벤트 기반 스위칭 메커니즘을 통해 관리되며, 이는 하위 작업 진행 및 완료를 모니터링합니다. VLA를 미세 조정하여 이벤트 신호를 예측하고 경량의 하위 작업 수준 손재주 정책을 훈련함으로써 최소한의 시연 데이터만 필요로 합니다. 이 접근 방식은 당사의 맞춤형 순응형 13-DoF 인간형 로봇 손에 적용되며, 순응성을 조절하여 자율 정책과 결합했을 때 손재주와 강건성에 미치는 영향을 평가할 수 있습니다. 우리는 로봇 손가락의 하드웨어 수준 순응성이 교란에 대한 수동적 적응을 가능하게 하고 접촉 안정성을 향상시킨다는 것을 보여줍니다. 이 방법론은 다양한 언어 조건부 손재주 작업에서 검증됩니다. 모듈성을 입증하기 위해 VLA 모델을 재훈련하지 않고도 추가 손재주 기술과 다른 순응형 손에 적응할 수 있음을 보여줍니다. 이는 대규모 AI 모델의 장점을 유지하면서 순응성을 활용하는 효율적이고 확장 가능한 교차 체현 손재주 접근 방식을 제공합니다.

## 参考
- http://arxiv.org/abs/2410.14022v2
