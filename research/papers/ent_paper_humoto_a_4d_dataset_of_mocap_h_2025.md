---
$id: ent_paper_humoto_a_4d_dataset_of_mocap_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions'
  zh: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions'
  ko: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions'
summary:
  en: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions is a 2025 work on human motion analysis and synthesis for humanoid
    robots.'
  zh: HUMOTO 是一个 2025 年发布的高保真人-物交互 4D 数据集，专为运动生成、计算机视觉与机器人学设计。该数据集包含 735 段序列（共 7,875 秒，30 fps），覆盖 63 个精确建模的物体与 72 个可动部件，并通过场景驱动的
    LLM 脚本管线与动捕-相机混合录制系统，解决了遮挡与任务逻辑连贯性难题。
  ko: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions is a 2025 work on human motion analysis and synthesis for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humoto
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.10414v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions (arXiv)'
  url: https://arxiv.org/abs/2504.10414
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HUMOTO: A 4D Dataset of Mocap Human Object Interactions project page'
  url: https://jiaxin-lu.github.io/humoto/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
HUMOTO 由研究团队提出，旨在为类人机器人、动画与具身 AI 提供高质量的人-物交互运动数据。其核心创新在于利用大语言模型生成完整、有目的的任务脚本，确保动作的自然推进，同时采用动捕与相机联合录制方案有效处理交互中的遮挡问题。数据集涵盖从烹饪到户外野餐的多样化活动，经专业艺术家逐帧清理，极大减少了脚滑与物体穿透等伪影。此外，HUMOTO 提供了与其他数据集的基准对比，其全身运动与多物体同时交互的特性，为真实交互建模设立了新标准。

## 核心内容
### 数据集规模与构成
- **总时长**：7,875 秒（约 2.2 小时），以 30 fps 录制，共 735 段序列。
- **物体与部件**：包含 63 个高精度建模的物体，其中 72 个部件具有独立运动能力（如抽屉、铰链盖）。
- **活动类型**：覆盖烹饪、清洁、户外野餐等日常任务，强调任务的完整性与逻辑流程。

### 核心创新
- **场景驱动的 LLM 脚本管线**：利用大语言模型自动生成包含子目标与过渡动作的任务脚本，确保交互序列具有自然起承转合，而非随机动作拼接。
- **动捕-相机混合录制**：结合光学动捕系统与多视角相机，通过算法融合数据，有效处理手-物遮挡与物体内部遮挡问题。

### 数据质量保障
- **人工精修**：所有序列由专业动画师逐帧检查并修正，将脚滑（foot sliding）与物体穿透（object penetration）等常见伪影降至最低。
- **物理一致性**：在保持运动自然度的同时，确保手部与物体的接触点符合物理规律。

### 基准与对比
- 提供与其他公开数据集（如 GRAB、BEHAVE）的定量对比，在动作多样性、物体复杂度与任务完整性上均具优势。
- 支持全身运动生成、多物体交互预测等任务的基准测试。

### 应用价值
- **机器人学**：为类人机器人提供模仿学习的真实运动先验，尤其适用于需要精细操作与多物体协调的场景。
- **动画与具身 AI**：可作为生成式模型（如扩散模型、Transformer）的训练数据，推动虚拟角色与物理智能体的交互真实性。

项目主页：https://jiaxin-lu.github.io/humoto/

## Overview
We present Human Motions with Objects (HUMOTO), a high-fidelity dataset of human-object interactions for motion generation, computer vision, and robotics applications. Featuring 735 sequences (7,875 seconds at 30 fps), HUMOTO captures interactions with 63 precisely modeled objects and 72 articulated parts. Our innovations include a scene-driven LLM scripting pipeline creating complete, purposeful tasks with natural progression, and a mocap-and-camera recording setup to effectively handle occlusions. Spanning diverse activities from cooking to outdoor picnics, HUMOTO preserves both physical accuracy and logical task flow. Professional artists rigorously clean and verify each sequence, minimizing foot sliding and object penetrations. We also provide benchmarks compared to other datasets. HUMOTO's comprehensive full-body motion and simultaneous multi-object interactions address key data-capturing challenges and provide opportunities to advance realistic human-object interaction modeling across research domains with practical applications in animation, robotics, and embodied AI systems. Project: https://jiaxin-lu.github.io/humoto/ .

## 개요
우리는 동작 생성, 컴퓨터 비전 및 로봇공학 응용을 위한 인간-객체 상호작용의 고충실도 데이터셋인 Human Motions with Objects (HUMOTO)를 제시합니다. 735개의 시퀀스(30fps에서 7,875초)를 특징으로 하는 HUMOTO는 63개의 정밀하게 모델링된 객체와 72개의 관절 부품과의 상호작용을 포착합니다. 우리의 혁신에는 자연스러운 진행을 통해 완전하고 목적 있는 작업을 생성하는 장면 기반 LLM 스크립팅 파이프라인과 폐색을 효과적으로 처리하는 모캡 및 카메라 녹화 설정이 포함됩니다. 요리부터 야외 피크닉까지 다양한 활동을 아우르는 HUMOTO는 물리적 정확성과 논리적 작업 흐름을 모두 보존합니다. 전문 아티스트가 각 시퀀스를 엄격히 정리하고 검증하여 발 미끄러짐과 객체 관통을 최소화합니다. 또한 다른 데이터셋과 비교한 벤치마크를 제공합니다. HUMOTO의 포괄적인 전신 동작과 동시 다중 객체 상호작용은 주요 데이터 포착 과제를 해결하고 애니메이션, 로봇공학 및 체화된 AI 시스템의 실용적 응용을 통해 연구 영역 전반에서 현실적인 인간-객체 상호작용 모델링을 발전시킬 기회를 제공합니다. 프로젝트: https://jiaxin-lu.github.io/humoto/ .

## 핵심 내용
우리는 동작 생성, 컴퓨터 비전 및 로봇공학 응용을 위한 인간-객체 상호작용의 고충실도 데이터셋인 Human Motions with Objects (HUMOTO)를 제시합니다. 735개의 시퀀스(30fps에서 7,875초)를 특징으로 하는 HUMOTO는 63개의 정밀하게 모델링된 객체와 72개의 관절 부품과의 상호작용을 포착합니다. 우리의 혁신에는 자연스러운 진행을 통해 완전하고 목적 있는 작업을 생성하는 장면 기반 LLM 스크립팅 파이프라인과 폐색을 효과적으로 처리하는 모캡 및 카메라 녹화 설정이 포함됩니다. 요리부터 야외 피크닉까지 다양한 활동을 아우르는 HUMOTO는 물리적 정확성과 논리적 작업 흐름을 모두 보존합니다. 전문 아티스트가 각 시퀀스를 엄격히 정리하고 검증하여 발 미끄러짐과 객체 관통을 최소화합니다. 또한 다른 데이터셋과 비교한 벤치마크를 제공합니다. HUMOTO의 포괄적인 전신 동작과 동시 다중 객체 상호작용은 주요 데이터 포착 과제를 해결하고 애니메이션, 로봇공학 및 체화된 AI 시스템의 실용적 응용을 통해 연구 영역 전반에서 현실적인 인간-객체 상호작용 모델링을 발전시킬 기회를 제공합니다. 프로젝트: https://jiaxin-lu.github.io/humoto/ .

## 参考
- http://arxiv.org/abs/2504.10414v2
