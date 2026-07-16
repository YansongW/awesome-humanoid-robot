---
$id: ent_paper_chiang_mobility_vla_multimodal_instru_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs'
  zh: Mobility VLA
  ko: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs'
summary:
  en: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
  zh: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
  ko: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
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
- mobility_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.07775v2.
sources:
- id: src_001
  type: paper
  title: Mobility VLA source
  url: https://proceedings.mlr.press/v270/xu25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## 核心内容
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## 参考
- http://arxiv.org/abs/2407.07775v2

## Overview
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## Content
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## 개요
내비게이션 연구의 난제 중 하나는 자연어와 이미지를 포함한 다중 모달 명령을 이해하고 유용한 내비게이션을 수행할 수 있는 지능형 에이전트를 구축하는 것입니다. 이를 위해 우리는 시연 투어를 통한 다중 모달 명령 내비게이션(MINT)이라고 부르는 광범위하게 유용한 내비게이션 작업 범주를 연구합니다. 이 작업에서는 사전에 녹화된 시연 비디오를 통해 환경 사전 정보가 제공됩니다. 최근 비전 언어 모델(VLM)의 발전은 다중 모달 입력을 인지하고 추론하는 능력을 보여주며 이 목표를 달성할 유망한 경로를 제시합니다. 그러나 VLM은 일반적으로 텍스트 출력을 예측하도록 훈련되며, 이를 내비게이션에 가장 잘 활용하는 방법은 여전히 열린 연구 질문입니다. MINT를 해결하기 위해 우리는 Mobility VLA를 제시합니다. 이는 장기 컨텍스트 VLM의 환경 이해 및 상식 추론 능력과 위상 그래프 기반의 강력한 저수준 내비게이션 정책을 결합한 계층적 비전-언어-행동(VLA) 내비게이션 정책입니다. 고수준 정책은 시연 투어 비디오와 다중 모달 사용자 명령을 입력으로 받아 투어 비디오에서 목표 프레임을 찾는 장기 컨텍스트 VLM으로 구성됩니다. 다음으로, 저수준 정책은 목표 프레임과 오프라인에서 구축된 위상 그래프를 사용하여 매 시간 단계마다 로봇 동작을 생성합니다. 우리는 836m^2의 실제 환경에서 Mobility VLA를 평가했으며, 플라스틱 통을 들고 "이걸 어디에 반납해야 하나요?"와 같은 이전에 해결되지 않은 다중 모달 명령에서 높은 종단 간 성공률을 보여줍니다. Mobility VLA를 시연하는 비디오는 여기에서 확인할 수 있습니다: https://youtu.be/-Tof__Q8_5s

## 핵심 내용
내비게이션 연구의 난제 중 하나는 자연어와 이미지를 포함한 다중 모달 명령을 이해하고 유용한 내비게이션을 수행할 수 있는 지능형 에이전트를 구축하는 것입니다. 이를 위해 우리는 시연 투어를 통한 다중 모달 명령 내비게이션(MINT)이라고 부르는 광범위하게 유용한 내비게이션 작업 범주를 연구합니다. 이 작업에서는 사전에 녹화된 시연 비디오를 통해 환경 사전 정보가 제공됩니다. 최근 비전 언어 모델(VLM)의 발전은 다중 모달 입력을 인지하고 추론하는 능력을 보여주며 이 목표를 달성할 유망한 경로를 제시합니다. 그러나 VLM은 일반적으로 텍스트 출력을 예측하도록 훈련되며, 이를 내비게이션에 가장 잘 활용하는 방법은 여전히 열린 연구 질문입니다. MINT를 해결하기 위해 우리는 Mobility VLA를 제시합니다. 이는 장기 컨텍스트 VLM의 환경 이해 및 상식 추론 능력과 위상 그래프 기반의 강력한 저수준 내비게이션 정책을 결합한 계층적 비전-언어-행동(VLA) 내비게이션 정책입니다. 고수준 정책은 시연 투어 비디오와 다중 모달 사용자 명령을 입력으로 받아 투어 비디오에서 목표 프레임을 찾는 장기 컨텍스트 VLM으로 구성됩니다. 다음으로, 저수준 정책은 목표 프레임과 오프라인에서 구축된 위상 그래프를 사용하여 매 시간 단계마다 로봇 동작을 생성합니다. 우리는 836m^2의 실제 환경에서 Mobility VLA를 평가했으며, 플라스틱 통을 들고 "이걸 어디에 반납해야 하나요?"와 같은 이전에 해결되지 않은 다중 모달 명령에서 높은 종단 간 성공률을 보여줍니다. Mobility VLA를 시연하는 비디오는 여기에서 확인할 수 있습니다: https://youtu.be/-Tof__Q8_5s
