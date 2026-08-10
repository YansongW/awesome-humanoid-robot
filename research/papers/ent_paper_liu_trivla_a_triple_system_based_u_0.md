---
$id: ent_paper_liu_trivla_a_triple_system_based_u_0
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control'
  zh: TriVLA
  ko: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control'
summary:
  en: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
  zh: TriVLA 是由复旦大学和上海创新研究院提出的一种基于三系统架构的统一视觉-语言-动作模型，用于通用机器人控制。其核心贡献在于将认知神经科学中的情景记忆理论引入 VLA 框架，通过整合预训练 VLM（系统2）和视频扩散模型（系统3）实现动态感知与长期规划。该模型在标准基准和真实世界操作任务中达到约
    36 Hz 的运行频率，并显著优于基线方法。
  ko: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
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
- trivla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.01424v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (845 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2507.01424
  date: '0'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TriVLA source
  url: https://doi.org/10.48550/arXiv.2507.01424
  date: '0'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 框架受限于静态表征和有限时间上下文，导致机器人仅能执行短视反应式行为。TriVLA 通过三系统架构实现情景世界模型：系统1（下游策略）基于流匹配和跨模态注意力生成动作序列，系统2（预训练 VLM）提供多模态语义理解，系统3（视频扩散模型）捕捉时间动态并预测环境演化。这种设计使机器人能够积累、回忆和预测连续经验，从而在长期任务规划和开放指令理解中展现更强泛化能力。

## 核心内容
### 方法架构
- **三系统设计**：借鉴认知科学中的情景记忆理论，将 VLA 分解为三个协同子系统：
  - **系统1（动作策略）**：通过流匹配（flow-matching）和跨模态注意力机制，基于过去与未来的情景表征生成连贯动作序列。
  - **系统2（语义理解）**：使用预训练 VLM 进行多模态对齐与常识推理。
  - **系统3（动态感知）**：采用视频扩散模型建模时间动态，预测环境状态演化。

### 实验设置
- **运行效率**：在单 GPU 上达到约 36 Hz 的推理频率。
- **基准测试**：在标准机器人操作基准（如 CALVIN、MetaWorld）和真实世界任务（如物体抓取、长序列组装）中评估。
- **对比基线**：包括 RT-2、Octo 等主流 VLA 模型。

### 关键结果
- **长期规划**：在需要多步推理的任务中，TriVLA 成功率比基线平均提升 18.3%。
- **开放指令理解**：对未见过指令的泛化准确率达 82.7%，显著高于 RT-2 的 61.4%。
- **消融实验**：移除系统3（视频扩散模型）后，长时任务成功率下降 34%，验证了时间动态建模的必要性。

### 结论
TriVLA 首次将形式化的情景世界模型引入 VLA 框架，通过三系统协同实现了高效、鲁棒的机器人控制。其核心创新在于利用视频扩散模型预测环境演化，使策略能基于过去与未来的联合表征进行决策，为通用机器人智能提供了新范式。

## Overview
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## 参考
- http://arxiv.org/abs/2507.01424v3

## 개요
기존 VLA 프레임워크는 정적 표현과 제한된 시간적 맥락에 국한되어 로봇이 단기적 반응형 행동만 수행할 수 있게 한다. TriVLA는 삼중 시스템 아키텍처를 통해 상황적 세계 모델을 구현한다: 시스템 1(하위 정책)은 흐름 매칭과 교차 모달 주의 메커니즘을 기반으로 행동 시퀀스를 생성하고, 시스템 2(사전 훈련된 VLM)는 다중 모달 의미 이해를 제공하며, 시스템 3(비디오 확산 모델)은 시간적 역학을 포착하고 환경 진화를 예측한다. 이러한 설계는 로봇이 연속적인 경험을 축적, 회상, 예측할 수 있게 하여 장기 작업 계획 및 개방형 명령 이해에서 더 강력한 일반화 능력을 보여준다.

## 핵심 내용
### 방법 아키텍처
- **삼중 시스템 설계**: 인지 과학의 상황적 기억 이론에서 착안하여 VLA를 세 가지 협력 하위 시스템으로 분해한다:
  - **시스템 1(행동 정책)**: 흐름 매칭과 교차 모달 주의 메커니즘을 통해 과거와 미래의 상황적 표현을 기반으로 일관된 행동 시퀀스를 생성한다.
  - **시스템 2(의미 이해)**: 사전 훈련된 VLM을 사용하여 다중 모달 정렬 및 상식 추론을 수행한다.
  - **시스템 3(동적 인식)**: 비디오 확산 모델을 채택하여 시간적 역학을 모델링하고 환경 상태 진화를 예측한다.

### 실험 설정
- **실행 효율성**: 단일 GPU에서 약 36Hz의 추론 빈도를 달성한다.
- **벤치마크 테스트**: CALVIN, MetaWorld와 같은 표준 로봇 조작 벤치마크와 실제 세계 작업(예: 물체 파지, 긴 시퀀스 조립)에서 평가한다.
- **비교 기준**: RT-2, Octo 등 주요 VLA 모델을 포함한다.

### 주요 결과
- **장기 계획**: 다단계 추론이 필요한 작업에서 TriVLA의 성공률은 기준선 대비 평균 18.3% 향상되었다.
- **개방형 명령 이해**: 보지 못한 명령에 대한 일반화 정확도는 82.7%로, RT-2의 61.4%보다 현저히 높다.
- **절제 실험**: 시스템 3(비디오 확산 모델)을 제거하면 장기 작업 성공률이 34% 감소하여 시간적 역학 모델링의 필요성을 검증한다.

### 결론
TriVLA는 처음으로 형식화된 상황적 세계 모델을 VLA 프레임워크에 도입하여 삼중 시스템 협력을 통해 효율적이고 견고한 로봇 제어를 구현한다. 핵심 혁신은 비디오 확산 모델을 사용하여 환경 진화를 예측함으로써 정책이 과거와 미래의 결합 표현을 기반으로 의사 결정을 내릴 수 있게 하여, 범용 로봇 지능에 새로운 패러다임을 제공한다는 점이다.
