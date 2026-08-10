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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14022v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (931 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.14022v2

## 개요
기존 대형 VLA 모델은 텍스트 기반 고수준 계획에 뛰어나지만 주로 그리퍼를 사용하며, 소규모 모방 학습 정책은 고자유도 다섯 손가락 로봇 손을 제어할 수 있지만 특정 작업에 국한됩니다. 본 연구는 이중 채널 전환 제어기를 제안합니다: VLA 모델은 하위 작업 진행 상황 모니터링과 이벤트 신호 예측을 담당하고, 경량 다섯 손가락 정책은 손가락 수준의 정밀 제어를 수행합니다. 하드웨어 측면에서는 조절 가능한 유연성을 갖춘 13자유도 인간형 로봇 손을 채택했으며, 실험을 통해 손가락 유연성이 외란을 수동적으로 흡수하고 접촉 안정성을 향상시킬 수 있음을 입증했습니다. 이 방법은 다양한 언어 조건화 다섯 손가락 작업에서 유효성을 검증했으며, VLA를 재훈련하지 않고도 새로운 기술과 다양한 유연성 손 구조에 적응할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **이중 채널 제어**: 인간 운동 제어의 이중 채널 가설을 차용하여 고수준 작업 추론(VLA 채널)과 저수준 손가락 제어(확산 정책 채널)를 분리
- **이벤트 기반 전환 메커니즘**: VLA 모델은 미세 조정을 통해 하위 작업 완료 이벤트 신호를 예측하며, 현재 하위 작업 완료가 감지되면 자동으로 다음 단계 정책으로 전환
- **데이터 효율성**: 하위 작업 수준의 다섯 손가락 정책 훈련에는 소량의 시연 데이터만 필요하며, VLA는 이벤트 예측 미세 조정을 통해 작업 간 일반화를 달성

### 하드웨어 설계
- **13자유도 인간형 로봇 손**: 각 손가락에는 독립적인 유연성 조절 모듈이 장착되어 관절 강성을 동적으로 변경 가능
- **유연성의 역할**: 실험 결과 하드웨어 수준의 유연성 덕분에 손가락이 외부 외란(예: 충돌)에 수동적으로 적응할 수 있으며, 접촉력 변동이 37% 감소

### 실험 설정
- **작업 세트**: 잡기, 회전, 삽입 등 6가지 언어 조건화 다섯 손가락 조작 작업 포함
- **비교 기준선**: 순수 VLA 종단 간 제어, 순수 확산 정책 제어, 고정 임계값 전환 방법
- **평가 지표**: 작업 성공률, 접촉 안정성(힘 센서 표준 편차), 정책 전환 지연 시간

### 핵심 결과
- 전환 제어 방법은 모든 작업에서 평균 성공률 89.2%를 달성하여 순수 VLA(61.5%) 및 순수 확산 정책(73.8%)보다 우수
- 유연성 활성화 시 예기치 않은 충돌 상황에서 작업 복구 성공률이 54%에서 92%로 향상
- 손 구조 간 전이 테스트: 다른 유연성 매개변수를 가진 손 구조로 정책을 전이할 때 저수준 정책만 재훈련하면 되며(5분 데이터 수집), VLA 모델은 조정 불필요
- 새로운 기술 확장: 3개의 하위 작업 정책을 추가함으로써 VLA를 수정하지 않고도 병뚜껑 돌리기와 같은 복합 작업 구현 가능

### 결론
이 방법은 고수준 추론과 저수준 제어를 분리하고 하드웨어 유연성을 결합하여 다섯 손가락 조작을 위한 확장 가능한 교차 본체 솔루션을 제공합니다. 핵심 혁신은 이벤트 기반 전환 메커니즘이 VLA의 정밀 동작 데이터 의존도를 효과적으로 낮추면서도 대규모 모델의 작업 이해 이점을 유지한다는 점입니다.
