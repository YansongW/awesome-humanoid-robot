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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.10414v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (947 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.10414v2

## 개요
HUMOTO는 연구팀이 제안한 것으로, 휴머노이드 로봇, 애니메이션 및 구현 AI를 위한 고품질 인간-물체 상호작용 모션 데이터를 제공하는 것을 목표로 합니다. 핵심 혁신은 대규모 언어 모델을 활용하여 완전하고 목적 있는 작업 스크립트를 생성함으로써 동작의 자연스러운 진행을 보장하고, 동시에 모션 캡처와 카메라를 결합한 녹화 방식을 채택하여 상호작용 중 발생하는 폐색 문제를 효과적으로 처리한다는 점입니다. 데이터셋은 요리부터 야외 피크닉까지 다양한 활동을 포괄하며, 전문 아티스트의 프레임별 정리를 통해 발 미끄러짐과 물체 관통과 같은 아티팩트를 크게 줄였습니다. 또한 HUMOTO는 다른 데이터셋과의 벤치마크 비교를 제공하며, 전신 모션과 다중 물체 동시 상호작용 특성을 통해 실제 상호작용 모델링의 새로운 기준을 세웠습니다.

## 핵심 내용
### 데이터셋 규모와 구성
- **총 길이**: 7,875초(약 2.2시간), 30fps로 녹화, 총 735개 시퀀스.
- **물체와 부품**: 고정밀 모델링된 63개의 물체 포함, 그중 72개 부품은 독립적인 운동 능력 보유(예: 서랍, 힌지 뚜껑).
- **활동 유형**: 요리, 청소, 야외 피크닉 등 일상 작업을 포괄하며, 작업의 완전성과 논리적 흐름을 강조.

### 핵심 혁신
- **장면 기반 LLM 스크립트 파이프라인**: 대규모 언어 모델을 활용하여 하위 목표와 전환 동작을 포함한 작업 스크립트를 자동 생성, 상호작용 시퀀스가 무작위 동작 조합이 아닌 자연스러운 시작-전개-전환-종결을 갖도록 보장.
- **모션 캡처-카메라 혼합 녹화**: 광학 모션 캡처 시스템과 다중 시점 카메라를 결합하고, 알고리즘을 통해 데이터를 융합하여 손-물체 폐색 및 물체 내부 폐색 문제를 효과적으로 처리.

### 데이터 품질 보장
- **수동 정밀 수정**: 모든 시퀀스는 전문 애니메이터가 프레임별로 검사하고 수정하여 발 미끄러짐(foot sliding)과 물체 관통(object penetration)과 같은 일반적인 아티팩트를 최소화.
- **물리적 일관성**: 동작의 자연스러움을 유지하면서 손과 물체의 접촉점이 물리 법칙을 따르도록 보장.

### 벤치마크 및 비교
- GRAB, BEHAVE와 같은 다른 공개 데이터셋과의 정량적 비교를 제공하며, 동작 다양성, 물체 복잡성 및 작업 완전성에서 모두 우위를 보임.
- 전신 모션 생성, 다중 물체 상호작용 예측 등의 작업을 위한 벤치마크 테스트 지원.

### 응용 가치
- **로봇공학**: 휴머노이드 로봇에 모방 학습을 위한 실제 모션 사전을 제공하며, 특히 정밀 조작과 다중 물체 조정이 필요한 시나리오에 적합.
- **애니메이션 및 구현 AI**: 확산 모델, 트랜스포머와 같은 생성 모델의 학습 데이터로 활용되어 가상 캐릭터와 물리적 지능체의 상호작용 사실성을 향상.

프로젝트 홈페이지: https://jiaxin-lu.github.io/humoto/
