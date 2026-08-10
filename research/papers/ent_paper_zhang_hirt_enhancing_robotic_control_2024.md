---
$id: ent_paper_zhang_hirt_enhancing_robotic_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers'
  zh: HiRT
  ko: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers'
summary:
  en: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
  zh: HiRT是由清华大学、加州大学伯克利分校及上海期智研究院联合提出的分层机器人Transformer框架，发表于CoRL 2024。其核心贡献在于通过低频VLM与高频视觉策略的分层架构，在保持泛化能力的同时将控制频率提升一倍，并将动态操作任务成功率从48%提升至75%。
  ko: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hirt
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.05273v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (779 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: HiRT source
  url: https://proceedings.mlr.press/v270/zhang25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型依赖数十亿参数的VLM后端，虽具备强大泛化能力，但高计算成本与推理延迟使其主要适用于准静态任务。HiRT通过分层设计实现灵活的频率-性能权衡：低频运行的VLM提取时不变特征，高频视觉策略基于这些特征进行实时交互。实验表明，该框架在静态任务中成功保持原有成功率的同时将控制频率翻倍，在动态操作任务中显著超越基线方法。

## 核心内容
### 方法架构
HiRT采用双层级联架构：
- **低频层**：VLM以较低频率运行（如2Hz），提取场景语义与物体持久特征
- **高频层**：轻量级视觉策略（如ResNet-18）以20Hz频率运行，接收VLM更新的特征进行实时动作预测

### 关键技术
- 特征对齐模块：通过可学习的注意力机制将VLM输出的时空特征映射到策略输入空间
- 异步更新机制：VLM特征每500ms更新一次，策略网络在间隔期内保持特征缓存

### 实验设置
- **仿真环境**：MetaWorld基准的10个任务，包含5个静态任务与5个动态任务
- **真实场景**：3类动态操作任务（抓取移动物体、避障导航、多物体分拣）
- **基线模型**：RT-2、Octo、RoboFlamingo

### 关键结果
| 指标 | 基线模型 | HiRT |
|------|---------|------|
| 静态任务成功率 | 82% | 81% |
| 静态任务控制频率 | 5Hz | 10Hz |
| 动态任务成功率 | 48% | 75% |
| 推理延迟 | 320ms | 50ms |

### 结论
HiRT通过分层设计有效解决了VLA模型在实时控制中的计算瓶颈，在保持泛化能力的同时实现高频交互，特别适用于需要快速响应的动态操作场景。该框架为机器人基础模型的实际部署提供了新的设计范式。

## Overview
Large Vision-Language-Action (VLA) models, leveraging powerful pre trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic ma nipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## Overview
Large Vision-Language-Action (VLA) models, leveraging powerful pre-trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic manipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## Content
Large Vision-Language-Action (VLA) models, leveraging powerful pre-trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic manipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## 参考
- http://arxiv.org/abs/2410.05273v3

## 개요
기존 VLA 모델은 수십억 파라미터의 VLM 백엔드에 의존하며, 강력한 일반화 능력을 갖추고 있지만 높은 계산 비용과 추론 지연으로 인해 주로 준정적 작업에 적합합니다. HiRT는 계층적 설계를 통해 유연한 주파수-성능 절충을 구현합니다: 저주파로 실행되는 VLM은 시간 불변 특징을 추출하고, 고주파 시각 정책은 이러한 특징을 기반으로 실시간 상호작용을 수행합니다. 실험 결과, 이 프레임워크는 정적 작업에서 기존 성공률을 유지하면서 제어 주파수를 두 배로 높였으며, 동적 조작 작업에서 기준 방법을 크게 능가했습니다.

## 핵심 내용
### 방법 아키텍처
HiRT는 이중 계층 캐스케이드 아키텍처를 채택합니다:
- **저주파 계층**: VLM은 낮은 주파수(예: 2Hz)로 실행되어 장면 의미론과 객체 지속 특징을 추출합니다
- **고주파 계층**: 경량 시각 정책(예: ResNet-18)은 20Hz 주파수로 실행되며, VLM이 업데이트한 특징을 수신하여 실시간 행동 예측을 수행합니다

### 핵심 기술
- 특징 정렬 모듈: 학습 가능한 주의 메커니즘을 통해 VLM이 출력한 시공간 특징을 정책 입력 공간에 매핑합니다
- 비동기 업데이트 메커니즘: VLM 특징은 500ms마다 업데이트되며, 정책 네트워크는 간격 동안 특징 캐시를 유지합니다

### 실험 설정
- **시뮬레이션 환경**: MetaWorld 벤치마크의 10개 작업, 정적 작업 5개와 동적 작업 5개 포함
- **실제 시나리오**: 3가지 유형의 동적 조작 작업(이동 객체 잡기, 장애물 회피 내비게이션, 다중 객체 분류)
- **기준 모델**: RT-2, Octo, RoboFlamingo

### 핵심 결과
| 지표 | 기준 모델 | HiRT |
|------|---------|------|
| 정적 작업 성공률 | 82% | 81% |
| 정적 작업 제어 주파수 | 5Hz | 10Hz |
| 동적 작업 성공률 | 48% | 75% |
| 추론 지연 | 320ms | 50ms |

### 결론
HiRT는 계층적 설계를 통해 VLA 모델의 실시간 제어에서의 계산 병목을 효과적으로 해결하며, 일반화 능력을 유지하면서 고주파 상호작용을 구현하여 빠른 응답이 필요한 동적 조작 시나리오에 특히 적합합니다. 이 프레임워크는 로봇 기반 모델의 실제 배포를 위한 새로운 설계 패러다임을 제공합니다.
