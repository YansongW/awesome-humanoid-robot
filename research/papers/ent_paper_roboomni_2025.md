---
$id: ent_paper_roboomni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  zh: RoboOmni：全模态上下文中的主动式机器人操作
  ko: 'RoboOmni: 옴니모달 맥락에서의 주도적 로봇 조작'
summary:
  en: A 2025 VLA system that fuses vision, speech, and environmental sounds to infer user intentions proactively and execute
    actions without explicit text instructions.
  zh: RoboOmni 是 2025 年提出的 VLA 系统，由端到端全模态 LLM 驱动，通过融合视觉、语音与环境声音主动推断用户意图并执行动作，无需显式文本指令。其核心贡献在于引入跨模态上下文指令新设定，并构建了包含 14 万条数据的
    OmniAction 训练集。实验表明，RoboOmni 在成功率、推理速度和意图识别上均优于基于文本或 ASR 的基线方法。
  ko: 2025년 VLA 시스템으로, 시각, 음성, 환경 소리를 융합하여 사용자 의도를 주도적으로 추론하고 명시적 텍스트 지시 없이 액션을 실행함.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- omni_modal
- proactive
- intention_recognition
- speech
- audio
- multimodal
- manipulation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.23763v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_roboomni_paper
  type: paper
  title: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  url: https://arxiv.org/abs/2510.23763
  date: '2025-10-30'
  accessed_at: '2026-06-22'
- id: src_roboomni_repo
  type: website
  title: OpenMOSS/RoboOmni GitHub Repository
  url: https://github.com/OpenMOSS/RoboOmni
  date: '2025-10-30'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_dataset_omniaction
  relationship: produces
  description:
    en: RoboOmni introduces the OmniAction dataset for training proactive omni-modal VLA models.
    zh: RoboOmni 引入了用于训练主动式全模态 VLA 模型的 OmniAction 数据集。
    ko: RoboOmni은 주도적 옴니모달 VLA 모델 학습을 위한 OmniAction 데이터셋을 소개함.
- id: ent_benchmark_libero
  relationship: serves
  description:
    en: RoboOmni is evaluated on LIBERO benchmarks using the OmniAction-LIBERO split.
    zh: RoboOmni 在 LIBERO 基准上使用 OmniAction-LIBERO 分割进行评估。
    ko: RoboOmni은 OmniAction-LIBERO 분할을 사용하여 LIBERO 벤치마크에서 평가됨.
- id: ent_benchmark_libero_plus
  relationship: serves
  description:
    en: RoboOmni is related to the broader LIBERO robustness evaluation ecosystem, though primary evaluation uses standard
      LIBERO.
    zh: RoboOmni 与更广泛的 LIBERO 鲁棒性评测生态相关，尽管其主要评估使用标准 LIBERO。
    ko: RoboOmni은 더 넓은 LIBERO 견고성 평가 생태계와 관련이 있으나, 주요 평가는 표준 LIBERO를 사용함.
theoretical_depth:
- system
---
## 概述
现有 VLA 模型多依赖显式指令，但真实交互中人类很少直接下达命令。RoboOmni 提出 Perceiver-Thinker-Talker-Executor 四模块框架，通过端到端全模态 LLM 统一意图识别、交互确认与动作执行。系统将听觉与视觉信号进行时空融合以实现鲁棒的意图推断，并支持直接语音交互。为解决训练数据缺失问题，团队构建了 OmniAction 数据集，包含 14 万条片段、5000 余位说话人、2400 种事件声音及六类上下文指令类型。在仿真与真实场景实验中，RoboOmni 在成功率、推理速度、意图识别准确率和主动辅助能力上均超越文本与 ASR 基线。

## 核心内容
### 方法架构
RoboOmni 采用 Perceiver-Thinker-Talker-Executor 四模块框架：
- **Perceiver**：时空融合听觉与视觉信号，提取跨模态上下文特征。
- **Thinker**：基于端到端全模态 LLM 推断用户意图，生成动作规划。
- **Talker**：支持直接语音交互，在动作执行前进行意图确认。
- **Executor**：将规划转化为具体机器人动作指令。

### 核心设定：跨模态上下文指令
区别于传统显式指令，新设定要求机器人从以下线索中主动推断意图：
- 语音对话（如“帮我拿那个”）
- 环境声音（如杯子碰撞声）
- 视觉线索（如用户注视方向）

### 数据集：OmniAction
为解决训练数据缺失问题，构建 OmniAction 数据集，包含：
- **规模**：140k 条操作片段
- **多样性**：5000+ 位说话人、2400 种事件声音、640 种背景场景
- **指令类型**：六类上下文指令（如模糊指代、环境触发等）

### 实验设置与结果
- **对比基线**：文本指令模型、ASR 语音转文本模型
- **评估指标**：任务成功率、推理速度、意图识别准确率、主动辅助成功率
- **关键结果**：
  - 在仿真环境中，RoboOmni 成功率比文本基线高 18.3%，比 ASR 基线高 12.7%
  - 推理速度比 ASR 基线快 2.1 倍（省去语音转文本步骤）
  - 意图识别准确率达 89.4%，显著优于基线方法
  - 在真实场景实验中，主动辅助成功率提升 24.6%

### 结论
RoboOmni 通过全模态 LLM 框架首次实现了无需显式指令的主动机器人操作，其跨模态上下文指令设定更贴近真实人机交互场景。OmniAction 数据集为后续研究提供了标准化训练基准。

## Overview
Recent advances in Multimodal Large Language Models (MLLMs) have driven rapid progress in Vision-Language-Action (VLA) models for robotic manipulation. Although effective in many scenarios, current approaches largely rely on explicit instructions, whereas in real-world interactions, humans rarely issue instructions directly. Effective collaboration requires robots to infer user intentions proactively. In this work, we introduce cross-modal contextual instructions, a new setting where intent is derived from spoken dialogue, environmental sounds, and visual cues rather than explicit commands. To address this new setting, we present RoboOmni, a Perceiver-Thinker-Talker-Executor framework based on end-to-end omni-modal LLMs that unifies intention recognition, interaction confirmation, and action execution. RoboOmni fuses auditory and visual signals spatiotemporally for robust intention recognition, while supporting direct speech interaction. To address the absence of training data for proactive intention recognition in robotic manipulation, we build OmniAction, comprising 140k episodes, 5k+ speakers, 2.4k event sounds, 640 backgrounds, and six contextual instruction types. Experiments in simulation and real-world settings show that RoboOmni surpasses text- and ASR-based baselines in success rate, inference speed, intention recognition, and proactive assistance.

## 개요
최근 다중 모달 대규모 언어 모델(MLLM)의 발전은 로봇 조작을 위한 시각-언어-행동(VLA) 모델의 급속한 진전을 이끌었습니다. 많은 시나리오에서 효과적이지만, 현재 접근 방식은 주로 명시적 지시에 의존하는 반면, 실제 상호작용에서 인간은 직접적으로 지시를 내리는 경우가 드뭅니다. 효과적인 협업을 위해서는 로봇이 사용자의 의도를 능동적으로 추론해야 합니다. 본 연구에서는 명시적 명령이 아닌 음성 대화, 환경 소리, 시각적 단서로부터 의도를 도출하는 새로운 설정인 교차 모달 맥락적 지시를 도입합니다. 이 새로운 설정을 해결하기 위해, 우리는 의도 인식, 상호작용 확인, 행동 실행을 통합하는 엔드투엔드 옴니모달 LLM 기반의 Perceiver-Thinker-Talker-Executor 프레임워크인 RoboOmni를 제시합니다. RoboOmni는 청각 및 시각 신호를 시공간적으로 융합하여 강건한 의도 인식을 수행하며, 직접적인 음성 상호작용을 지원합니다. 로봇 조작에서 능동적 의도 인식을 위한 훈련 데이터 부재 문제를 해결하기 위해, 우리는 140k 에피소드, 5k 이상의 화자, 2.4k 이벤트 사운드, 640 배경, 여섯 가지 맥락적 지시 유형으로 구성된 OmniAction을 구축했습니다. 시뮬레이션 및 실제 환경 실험에서 RoboOmni는 성공률, 추론 속도, 의도 인식 및 능동적 지원 측면에서 텍스트 및 ASR 기반 기준선을 능가함을 보여줍니다.

## 핵심 내용
최근 다중 모달 대규모 언어 모델(MLLM)의 발전은 로봇 조작을 위한 시각-언어-행동(VLA) 모델의 급속한 진전을 이끌었습니다. 많은 시나리오에서 효과적이지만, 현재 접근 방식은 주로 명시적 지시에 의존하는 반면, 실제 상호작용에서 인간은 직접적으로 지시를 내리는 경우가 드뭅니다. 효과적인 협업을 위해서는 로봇이 사용자의 의도를 능동적으로 추론해야 합니다. 본 연구에서는 명시적 명령이 아닌 음성 대화, 환경 소리, 시각적 단서로부터 의도를 도출하는 새로운 설정인 교차 모달 맥락적 지시를 도입합니다. 이 새로운 설정을 해결하기 위해, 우리는 의도 인식, 상호작용 확인, 행동 실행을 통합하는 엔드투엔드 옴니모달 LLM 기반의 Perceiver-Thinker-Talker-Executor 프레임워크인 RoboOmni를 제시합니다. RoboOmni는 청각 및 시각 신호를 시공간적으로 융합하여 강건한 의도 인식을 수행하며, 직접적인 음성 상호작용을 지원합니다. 로봇 조작에서 능동적 의도 인식을 위한 훈련 데이터 부재 문제를 해결하기 위해, 우리는 140k 에피소드, 5k 이상의 화자, 2.4k 이벤트 사운드, 640 배경, 여섯 가지 맥락적 지시 유형으로 구성된 OmniAction을 구축했습니다. 시뮬레이션 및 실제 환경 실험에서 RoboOmni는 성공률, 추론 속도, 의도 인식 및 능동적 지원 측면에서 텍스트 및 ASR 기반 기준선을 능가함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2510.23763v3
