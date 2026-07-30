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
  zh: BiBo 是一项2025年的研究，旨在利用现成的视觉语言模型（如GPT-4）控制人形机器人，无需大规模数据收集。其核心贡献在于通过“具身指令编译器”将高层用户指令转化为低层控制参数，并借助扩散模型“运动执行器”生成类人运动，在开放环境中实现90.2%的任务成功率。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00041v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World (arXiv)'
  url: https://arxiv.org/abs/2511.00041
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究提出BiBo框架，解决人形机器人在开放环境中灵活交互的难题。它利用GPT-4等现成视觉语言模型的强泛化能力，避免昂贵的数据收集。BiBo包含两个关键模块：具身指令编译器将用户指令（如“休息一下”）精确转换为控制参数（如“随意坐下，位置：(1, 2)，朝向：90°”）；扩散模型运动执行器则根据这些参数生成类人运动，并动态适应环境物理反馈。实验表明，BiBo在开放环境中的交互任务成功率达90.2%，文本引导运动执行精度比先前方法提升16.3%。

## 核心内容
### 方法概述
BiBo 框架由两个核心组件构成：
- **具身指令编译器**：负责将高层用户指令（如“have a rest”）转换为低层原始命令及控制参数（如“sit casually, location: (1, 2), facing: 90°”）。该模块使视觉语言模型能够感知环境并精确理解任务。
- **扩散模型运动执行器**：基于扩散模型生成类人运动，从原始命令中生成自然动作，并动态适应环境物理反馈，确保运动在开放环境中的鲁棒性。

### 实验设置与结果
- **任务成功率**：在开放环境中，BiBo 的交互任务成功率达到 **90.2%**，显著优于基线方法。
- **运动执行精度**：在文本引导运动执行任务中，BiBo 的精度比先前方法提升 **16.3%**，验证了其在高精度控制上的优势。
- **泛化能力**：BiBo 无需大规模数据集训练，仅依赖现成视觉语言模型的开放世界泛化能力，即可处理多样化和复杂的运动。

### 结论
BiBo 通过结合现成视觉语言模型与扩散模型，为人形机器人提供了一种低成本、高泛化能力的控制方案。代码将公开发布，以促进相关研究。

## Overview
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## 개요
휴머노이드 에이전트는 개방 환경에서 유연하고 다양한 상호작용을 처리하는 데 어려움을 겪는 경우가 많습니다. 일반적인 해결책은 대규모 데이터셋을 수집하여 고성능 모델을 훈련하는 것이지만, 이 접근 방식은 비용이 엄청나게 많이 들 수 있습니다. 본 논문에서는 대안적인 해결책을 탐구합니다: 기성 비전-언어 모델(VLM, 예: GPT-4)을 활용하여 휴머노이드 에이전트를 제어함으로써, 이들의 강력한 개방형 세계 일반화 능력을 활용하여 방대한 데이터 수집의 필요성을 완화하는 것입니다. 이를 위해 우리는 \textbf{BiBo}(\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs)를 제시합니다. BiBo는 두 가지 핵심 구성 요소로 이루어져 있습니다: (1) \textbf{내장형 명령 컴파일러}는 VLM이 환경을 인식하고 상위 수준의 사용자 명령(예: {\small\itshape ``휴식 취하기''})을 제어 매개변수가 포함된 하위 수준의 기본 명령(예: {\small\itshape ``편하게 앉기, 위치: (1, 2), 방향: 90$^\circ$''})으로 정확하게 변환할 수 있게 해줍니다. (2) 확산 기반 \textbf{모션 실행기}는 이러한 명령으로부터 인간과 유사한 동작을 생성하면서 환경의 물리적 피드백에 동적으로 적응합니다. 이러한 방식으로 BiBo는 기본적인 상호작용뿐만 아니라 다양하고 복잡한 동작도 처리할 수 있습니다. 실험 결과, BiBo는 개방 환경에서 상호작용 작업 성공률 90.2%를 달성하고, 텍스트 기반 동작 실행의 정밀도를 기존 방법보다 16.3% 향상시킵니다. 코드는 공개될 예정입니다.

## 핵심 내용
휴머노이드 에이전트는 개방 환경에서 유연하고 다양한 상호작용을 처리하는 데 어려움을 겪는 경우가 많습니다. 일반적인 해결책은 대규모 데이터셋을 수집하여 고성능 모델을 훈련하는 것이지만, 이 접근 방식은 비용이 엄청나게 많이 들 수 있습니다. 본 논문에서는 대안적인 해결책을 탐구합니다: 기성 비전-언어 모델(VLM, 예: GPT-4)을 활용하여 휴머노이드 에이전트를 제어함으로써, 이들의 강력한 개방형 세계 일반화 능력을 활용하여 방대한 데이터 수집의 필요성을 완화하는 것입니다. 이를 위해 우리는 \textbf{BiBo}(\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs)를 제시합니다. BiBo는 두 가지 핵심 구성 요소로 이루어져 있습니다: (1) \textbf{내장형 명령 컴파일러}는 VLM이 환경을 인식하고 상위 수준의 사용자 명령(예: {\small\itshape ``휴식 취하기''})을 제어 매개변수가 포함된 하위 수준의 기본 명령(예: {\small\itshape ``편하게 앉기, 위치: (1, 2), 방향: 90$^\circ$''})으로 정확하게 변환할 수 있게 해줍니다. (2) 확산 기반 \textbf{모션 실행기}는 이러한 명령으로부터 인간과 유사한 동작을 생성하면서 환경의 물리적 피드백에 동적으로 적응합니다. 이러한 방식으로 BiBo는 기본적인 상호작용뿐만 아니라 다양하고 복잡한 동작도 처리할 수 있습니다. 실험 결과, BiBo는 개방 환경에서 상호작용 작업 성공률 90.2%를 달성하고, 텍스트 기반 동작 실행의 정밀도를 기존 방법보다 16.3% 향상시킵니다. 코드는 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2511.00041v1
