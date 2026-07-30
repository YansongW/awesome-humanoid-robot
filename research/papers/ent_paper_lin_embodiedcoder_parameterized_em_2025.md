---
$id: ent_paper_lin_embodiedcoder_parameterized_em_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model'
  zh: EmbodiedCoder
  ko: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model'
summary:
  en: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
  zh: EmbodiedCoder 是由中国科学院大学、中国科学院自动化研究所、北京航空航天大学及香港中文大学等机构于2025年提出的一种无需训练的开源框架，用于开放世界移动机器人操作。其核心贡献在于利用现代编码模型直接生成可执行的机器人轨迹，通过代码将高层指令与物体几何参数化及操作轨迹合成相结合，无需额外数据收集或微调。
  ko: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodiedcoder
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.06207v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (arXiv)'
  url: https://arxiv.org/abs/2510.06207
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EmbodiedCoder source
  url: https://doi.org/10.48550/arXiv.2510.06207
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EmbodiedCoder 是一种基于编码模型的训练无关框架，旨在解决移动机器人在开放世界中执行自然语言指令时的可扩展性与可解释性问题。与依赖大量标注数据或预定义原语的端到端视觉-语言-动作模型不同，EmbodiedCoder 通过将高层指令转化为代码，直接生成可执行的机器人轨迹，从而灵活地参数化物体几何并合成操作轨迹。该方法在真实移动机器人上的实验表明，其在多种长期任务中表现稳健，并能有效泛化到新物体和新环境，为连接高层推理与低层控制提供了一种透明且通用的途径。

## 核心内容
### 方法概述
EmbodiedCoder 的核心思想是利用现代编码模型（如大型语言模型）将自然语言指令转化为可执行的机器人控制代码，从而绕过传统方法中需要大量标注数据和预定义原语的限制。该框架无需训练，直接通过代码生成轨迹，实现了对物体几何的灵活参数化。

### 架构与流程
- **输入**：自然语言指令（如“将杯子放到桌子上”）。
- **处理**：编码模型将指令解析为结构化代码，其中包含物体几何参数（如位置、尺寸）和操作轨迹（如抓取、移动、放置）。
- **输出**：可执行的机器人轨迹代码，直接驱动移动机械臂完成操作。

### 实验设置
- **平台**：真实移动机器人（配备机械臂和传感器）。
- **任务**：多种长期操作任务，包括物体搬运、堆叠和重新排列。
- **评估指标**：任务成功率、泛化能力（对新物体和新环境）。

### 关键结果
- **性能**：在多种长期任务中，EmbodiedCoder 实现了稳健的性能，成功率显著高于基线方法（如基于预定义原语的模块化系统）。
- **泛化性**：对未见过的物体和环境表现出良好的泛化能力，无需额外数据收集或微调。
- **可解释性**：通过代码生成轨迹，提供了透明且可解释的决策过程，便于调试和验证。

### 结论
EmbodiedCoder 通过编码模型将高层推理与低层控制桥接，提供了一种无需训练、可解释且泛化性强的移动机器人操作框架。其代码生成范式为机器人智能从固定原语向通用能力演进提供了新思路。项目页面：https://embodiedcoder.github.io/EmbodiedCoder/

## Overview
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability.In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning.This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments.Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## Overview
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability. In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning. This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments. Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## Content
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability. In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning. This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments. Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## 개요
최근 로봇 제어 방법의 발전은 엔드투엔드 비전-언어-행동 프레임워크부터 사전 정의된 프리미티브를 갖춘 모듈식 시스템에 이르기까지, 로봇이 자연어 명령을 따르는 능력을 향상시켰습니다. 그럼에도 불구하고 많은 접근 방식은 대규모 주석 데이터셋에 의존하고 해석 가능성이 제한적이어서 다양한 환경으로 확장하는 데 여전히 어려움을 겪고 있습니다. 본 연구에서는 코딩 모델을 활용하여 실행 가능한 로봇 궤적을 직접 생성하는 훈련 없는 프레임워크인 EmbodiedCoder를 소개합니다. 고수준 명령을 코드에 기반함으로써 EmbodiedCoder는 추가 데이터 수집이나 미세 조정 없이 유연한 객체 형상 매개변수화와 조작 궤적 합성을 가능하게 합니다. 이 코딩 기반 패러다임은 인식과 조작을 연결하는 투명하고 일반화 가능한 방법을 제공합니다. 실제 모바일 로봇 실험에서 EmbodiedCoder는 다양한 장기 작업에서 강력한 성능을 달성하고 새로운 객체와 환경에 효과적으로 일반화됨을 보여줍니다. 우리의 결과는 고수준 추론과 저수준 제어를 연결하는 해석 가능한 접근 방식을 입증하며, 고정된 프리미티브를 넘어 다재다능한 로봇 지능으로 나아갑니다. 프로젝트 페이지: https://embodiedcoder.github.io/EmbodiedCoder/

## 핵심 내용
최근 로봇 제어 방법의 발전은 엔드투엔드 비전-언어-행동 프레임워크부터 사전 정의된 프리미티브를 갖춘 모듈식 시스템에 이르기까지, 로봇이 자연어 명령을 따르는 능력을 향상시켰습니다. 그럼에도 불구하고 많은 접근 방식은 대규모 주석 데이터셋에 의존하고 해석 가능성이 제한적이어서 다양한 환경으로 확장하는 데 여전히 어려움을 겪고 있습니다. 본 연구에서는 코딩 모델을 활용하여 실행 가능한 로봇 궤적을 직접 생성하는 훈련 없는 프레임워크인 EmbodiedCoder를 소개합니다. 고수준 명령을 코드에 기반함으로써 EmbodiedCoder는 추가 데이터 수집이나 미세 조정 없이 유연한 객체 형상 매개변수화와 조작 궤적 합성을 가능하게 합니다. 이 코딩 기반 패러다임은 인식과 조작을 연결하는 투명하고 일반화 가능한 방법을 제공합니다. 실제 모바일 로봇 실험에서 EmbodiedCoder는 다양한 장기 작업에서 강력한 성능을 달성하고 새로운 객체와 환경에 효과적으로 일반화됨을 보여줍니다. 우리의 결과는 고수준 추론과 저수준 제어를 연결하는 해석 가능한 접근 방식을 입증하며, 고정된 프리미티브를 넘어 다재다능한 로봇 지능으로 나아갑니다. 프로젝트 페이지: https://embodiedcoder.github.io/EmbodiedCoder/

## 参考
- http://arxiv.org/abs/2510.06207v2
