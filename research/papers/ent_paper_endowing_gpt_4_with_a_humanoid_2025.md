---
$id: ent_paper_endowing_gpt_4_with_a_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World'
  zh: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World'
  ko: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World'
summary:
  en: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World is a 2025
    work on manipulation for humanoid robots.'
  zh: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World is a 2025
    work on manipulation for humanoid robots.'
  ko: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World is a 2025
    work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- endowing_gpt_4_with_a_humanoid
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00041v1.
sources:
- id: src_001
  type: paper
  title: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World (arXiv)'
  url: https://arxiv.org/abs/2511.00041
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## 核心内容
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## 参考
- http://arxiv.org/abs/2511.00041v1

## Overview
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## Content
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## 개요
휴머노이드 에이전트는 개방 환경에서 유연하고 다양한 상호작용을 처리하는 데 어려움을 겪는 경우가 많습니다. 일반적인 해결책은 대규모 데이터셋을 수집하여 고성능 모델을 훈련하는 것이지만, 이 접근 방식은 비용이 엄청나게 많이 들 수 있습니다. 본 논문에서는 대안적인 해결책을 탐구합니다: 기성 비전-언어 모델(VLM, 예: GPT-4)을 활용하여 휴머노이드 에이전트를 제어함으로써, 이들의 강력한 개방형 세계 일반화 능력을 활용하여 방대한 데이터 수집의 필요성을 완화하는 것입니다. 이를 위해 우리는 \textbf{BiBo}(\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs)를 제시합니다. BiBo는 두 가지 핵심 구성 요소로 이루어져 있습니다: (1) \textbf{내장형 명령 컴파일러}는 VLM이 환경을 인식하고 상위 수준의 사용자 명령(예: {\small\itshape ``휴식 취하기''})을 제어 매개변수가 포함된 하위 수준의 기본 명령(예: {\small\itshape ``편하게 앉기, 위치: (1, 2), 방향: 90$^\circ$''})으로 정확하게 변환할 수 있게 해줍니다. (2) 확산 기반 \textbf{모션 실행기}는 이러한 명령으로부터 인간과 유사한 동작을 생성하면서 환경의 물리적 피드백에 동적으로 적응합니다. 이러한 방식으로 BiBo는 기본적인 상호작용뿐만 아니라 다양하고 복잡한 동작도 처리할 수 있습니다. 실험 결과, BiBo는 개방 환경에서 상호작용 작업 성공률 90.2%를 달성하고, 텍스트 기반 동작 실행의 정밀도를 기존 방법보다 16.3% 향상시킵니다. 코드는 공개될 예정입니다.

## 핵심 내용
휴머노이드 에이전트는 개방 환경에서 유연하고 다양한 상호작용을 처리하는 데 어려움을 겪는 경우가 많습니다. 일반적인 해결책은 대규모 데이터셋을 수집하여 고성능 모델을 훈련하는 것이지만, 이 접근 방식은 비용이 엄청나게 많이 들 수 있습니다. 본 논문에서는 대안적인 해결책을 탐구합니다: 기성 비전-언어 모델(VLM, 예: GPT-4)을 활용하여 휴머노이드 에이전트를 제어함으로써, 이들의 강력한 개방형 세계 일반화 능력을 활용하여 방대한 데이터 수집의 필요성을 완화하는 것입니다. 이를 위해 우리는 \textbf{BiBo}(\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs)를 제시합니다. BiBo는 두 가지 핵심 구성 요소로 이루어져 있습니다: (1) \textbf{내장형 명령 컴파일러}는 VLM이 환경을 인식하고 상위 수준의 사용자 명령(예: {\small\itshape ``휴식 취하기''})을 제어 매개변수가 포함된 하위 수준의 기본 명령(예: {\small\itshape ``편하게 앉기, 위치: (1, 2), 방향: 90$^\circ$''})으로 정확하게 변환할 수 있게 해줍니다. (2) 확산 기반 \textbf{모션 실행기}는 이러한 명령으로부터 인간과 유사한 동작을 생성하면서 환경의 물리적 피드백에 동적으로 적응합니다. 이러한 방식으로 BiBo는 기본적인 상호작용뿐만 아니라 다양하고 복잡한 동작도 처리할 수 있습니다. 실험 결과, BiBo는 개방 환경에서 상호작용 작업 성공률 90.2%를 달성하고, 텍스트 기반 동작 실행의 정밀도를 기존 방법보다 16.3% 향상시킵니다. 코드는 공개될 예정입니다.
