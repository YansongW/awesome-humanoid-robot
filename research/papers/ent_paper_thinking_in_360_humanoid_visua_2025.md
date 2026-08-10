---
$id: ent_paper_thinking_in_360_humanoid_visua_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Thinking in 360: Humanoid Visual Search in the Wild'
  zh: 'Thinking in 360: Humanoid Visual Search in the Wild'
  ko: 'Thinking in 360: Humanoid Visual Search in the Wild'
summary:
  en: 'Thinking in 360: Humanoid Visual Search in the Wild is a 2025 work on navigation for humanoid robots.'
  zh: '《Thinking in 360: Humanoid Visual Search in the Wild》是2025年关于人形机器人导航的研究。作者提出人形视觉搜索任务，让智能体在360°全景图中主动旋转头部搜索物体或路径，并构建了H*
    Bench基准。实验显示顶级模型仅约30%成功率，而通过后训练技术将开源模型Qwen2.5-VL的成功率提升三倍以上。'
  ko: 'Thinking in 360: Humanoid Visual Search in the Wild is a 2025 work on navigation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- navigation
- thinking_in_360
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20351v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (799 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Thinking in 360: Humanoid Visual Search in the Wild (arXiv)'
  url: https://arxiv.org/abs/2511.20351
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对现有视觉搜索方法局限于静态图像、忽略物理实体与三维世界交互的不足，提出人形视觉搜索任务。作者构建了H* Bench基准，涵盖交通枢纽、大型零售空间、城市街道和公共机构等需要高级视觉空间推理能力的野外场景。实验发现顶级专有模型在物体和路径搜索中仅约30%成功率，而通过后训练技术增强开源模型Qwen2.5-VL，物体搜索成功率从14.83%提升至47.38%，路径搜索从6.44%提升至24.94%。路径搜索的较低上限揭示了其固有难度，归因于对复杂空间常识的需求。

## 核心内容
### 方法
- 提出人形视觉搜索任务：人形智能体通过主动旋转头部，在360°全景图像表示的沉浸式世界中搜索物体或路径。
- 模拟人类头部（cephalomotor）和眼部（oculomotor）的协同控制机制，实现高效视觉信息搜索。

### 基准构建
- 创建H* Bench基准，超越传统家庭场景，涵盖交通枢纽、大型零售空间、城市街道和公共机构等野外场景。
- 这些场景需要高级视觉空间推理能力，如识别方向指示牌、寻找出口、定位特定店铺等。

### 实验设置
- 评估对象包括顶级专有模型和开源模型Qwen2.5-VL。
- 采用后训练技术（post-training techniques）增强开源模型性能。

### 关键结果
- 顶级专有模型在物体搜索和路径搜索中仅约30%成功率。
- 后训练后，Qwen2.5-VL的物体搜索成功率从14.83%提升至47.38%（提升超三倍）。
- 路径搜索成功率从6.44%提升至24.94%（提升近四倍）。
- 路径搜索的较低上限（24.94%）揭示其固有难度，归因于对复杂空间常识的需求。

### 结论
- 研究展示了构建多模态大语言模型（MLLM）智能体的可行路径。
- 同时量化了将此类智能体无缝融入日常人类生活所面临的巨大挑战。

## Overview
Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

## 参考
- http://arxiv.org/abs/2511.20351v2

## 개요
본 연구는 기존의 시각 검색 방법이 정적 이미지에 국한되어 물리적 실체와 3차원 세계의 상호작용을 무시한다는 한계를 지적하며, 인간형 시각 검색 과제를 제안한다. 저자들은 교통 허브, 대형 소매 공간, 도시 거리, 공공 기관 등 고급 시각적 공간 추론 능력이 요구되는 야외 시나리오를 포괄하는 H* Bench 벤치마크를 구축했다. 실험 결과, 최고 수준의 독점 모델은 객체 및 경로 검색에서 약 30%의 성공률에 그쳤으며, 후훈련 기술을 통해 오픈소스 모델 Qwen2.5-VL을 강화한 결과 객체 검색 성공률은 14.83%에서 47.38%로, 경로 검색은 6.44%에서 24.94%로 향상되었다. 경로 검색의 낮은 상한선은 복잡한 공간 상식에 대한 요구로 인한 본질적 어려움을 드러낸다.

## 핵심 내용
### 방법
- 인간형 시각 검색 과제 제안: 인간형 에이전트가 머리를 능동적으로 회전시키며 360° 파노라마 이미지로 표현된 몰입형 세계에서 객체나 경로를 검색한다.
- 인간의 머리(cephalomotor) 및 눈(oculomotor) 협동 제어 메커니즘을 모사하여 효율적인 시각 정보 검색을 구현한다.

### 벤치마크 구축
- 전통적인 가정 환경을 넘어 교통 허브, 대형 소매 공간, 도시 거리, 공공 기관 등 야외 시나리오를 포괄하는 H* Bench 벤치마크를 생성한다.
- 이러한 시나리오는 방향 표지판 인식, 출구 찾기, 특정 매장 위치 파악 등 고급 시각적 공간 추론 능력을 요구한다.

### 실험 설정
- 평가 대상에는 최고 수준의 독점 모델과 오픈소스 모델 Qwen2.5-VL이 포함된다.
- 후훈련 기술(post-training techniques)을 적용하여 오픈소스 모델의 성능을 강화한다.

### 주요 결과
- 최고 수준의 독점 모델은 객체 검색 및 경로 검색에서 약 30%의 성공률에 그친다.
- 후훈련 후, Qwen2.5-VL의 객체 검색 성공률은 14.83%에서 47.38%로 향상된다(3배 이상 증가).
- 경로 검색 성공률은 6.44%에서 24.94%로 향상된다(약 4배 증가).
- 경로 검색의 낮은 상한선(24.94%)은 복잡한 공간 상식에 대한 요구로 인한 본질적 어려움을 드러낸다.

### 결론
- 본 연구는 다중 모달 대형 언어 모델(MLLM) 에이전트를 구축하는 실현 가능한 경로를 제시한다.
- 동시에 이러한 에이전트를 일상적인 인간 생활에 원활하게 통합하는 데 따르는 엄청난 도전 과제를 정량화한다.
