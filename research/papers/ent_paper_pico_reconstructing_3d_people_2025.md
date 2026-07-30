---
$id: ent_paper_pico_reconstructing_3d_people_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PICO: Reconstructing 3D People In Contact with Objects'
  zh: 'PICO: Reconstructing 3D People In Contact with Objects'
  ko: 'PICO: Reconstructing 3D People In Contact with Objects'
summary:
  en: 'PICO: Reconstructing 3D People In Contact with Objects is a 2025 work on human motion analysis and synthesis for humanoid
    robots.'
  zh: PICO 是 2025 年提出的一项从单张彩色图像重建 3D 人体-物体交互（HOI）的工作。其核心贡献包括构建了 PICO-db 数据集，该数据集为自然图像提供了人体与物体网格上的密集 3D 接触对应关系；并提出了 PICO-fit
    优化方法，利用这些接触信息恢复交互中的 3D 人体与物体网格。该方法能泛化到多种未见过的物体类别，推动了 HOI 理解在自然场景中的规模化应用。
  ko: 'PICO: Reconstructing 3D People In Contact with Objects is a 2025 work on human motion analysis and synthesis for humanoid
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
- motion_analysis
- motion_synthesis
- pico
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.17695v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PICO: Reconstructing 3D People In Contact with Objects (arXiv)'
  url: https://arxiv.org/abs/2504.17695
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对单张彩色图像中 3D 人体-物体交互重建面临的深度模糊、遮挡及物体形状外观多变等挑战，PICO 提出了两项关键策略。首先，它基于 DAMON 数据集构建了 PICO-db，通过视觉基础模型检索 3D 物体网格，并利用一种仅需每块接触区域两次点击的新方法，将人体接触标签投影到物体上，从而建立人体与物体间的密集接触对应。其次，PICO 提出了 PICO-fit 方法，该方法在优化过程中利用 PICO-db 中的接触信息，迭代拟合 SMPL-X 人体模型和检索到的 3D 物体网格，使其与图像证据对齐。实验表明，PICO-fit 能有效处理现有方法无法应对的多种物体类别，这对于实现自然场景下的 HOI 理解至关重要。

## 核心内容
### 方法架构
PICO 的核心方法分为两个主要部分：
- **数据集构建 (PICO-db)**：利用 DAMON 数据集中与接触信息配对的自然图像。DAMON 仅在标准 3D 人体上标注了接触，而 PICO 需要同时获得人体和物体上的接触标签。为此，PICO 首先通过视觉基础模型从数据库中检索合适的 3D 物体网格。然后，采用一种新颖的方法，将 DAMON 的人体接触区域投影到该物体网格上，整个过程每块接触区域仅需两次人工点击，从而以最小的人力投入建立了丰富的接触对应关系。
- **优化拟合方法 (PICO-fit)**：这是一种新颖的“渲染-比较”拟合方法。它首先为 SMPL-X 人体模型推断接触信息，然后从 PICO-db 中检索与该物体最匹配的 3D 网格及其接触信息。最后，通过优化过程，利用这些接触信息迭代地拟合 3D 人体和物体网格，使其与图像证据对齐。

### 实验设置与关键数字
- **数据集**：PICO-db 基于 DAMON 数据集构建，提供了自然图像与人体、物体网格上密集 3D 接触的配对。
- **方法特点**：PICO-fit 能够处理多种物体类别，这是现有方法无法做到的。其独特之处在于利用接触信息作为桥梁，将人体与物体的 3D 重建过程紧密耦合。
- **可用性**：数据和代码已开源，地址为 https://pico.is.tue.mpg.de。

### 结论
PICO 通过构建包含密集接触对应关系的数据集和利用该数据集进行优化的拟合方法，有效解决了单张图像中 3D 人体-物体交互重建的泛化难题。该方法在多种未见过的物体类别上表现出色，为 HOI 理解在自然场景中的规模化应用提供了关键支撑。

## Overview
Recovering 3D Human-Object Interaction (HOI) from single color images is challenging due to depth ambiguities, occlusions, and the huge variation in object shape and appearance. Thus, past work requires controlled settings such as known object shapes and contacts, and tackles only limited object classes. Instead, we need methods that generalize to natural images and novel object classes. We tackle this in two main ways: (1) We collect PICO-db, a new dataset of natural images uniquely paired with dense 3D contact on both body and object meshes. To this end, we use images from the recent DAMON dataset that are paired with contacts, but these contacts are only annotated on a canonical 3D body. In contrast, we seek contact labels on both the body and the object. To infer these given an image, we retrieve an appropriate 3D object mesh from a database by leveraging vision foundation models. Then, we project DAMON's body contact patches onto the object via a novel method needing only 2 clicks per patch. This minimal human input establishes rich contact correspondences between bodies and objects. (2) We exploit our new dataset of contact correspondences in a novel render-and-compare fitting method, called PICO-fit, to recover 3D body and object meshes in interaction. PICO-fit infers contact for the SMPL-X body, retrieves a likely 3D object mesh and contact from PICO-db for that object, and uses the contact to iteratively fit the 3D body and object meshes to image evidence via optimization. Uniquely, PICO-fit works well for many object categories that no existing method can tackle. This is crucial to enable HOI understanding to scale in the wild. Our data and code are available at https://pico.is.tue.mpg.de.

## 개요
단일 컬러 이미지에서 3D 인간-객체 상호작용(HOI)을 복원하는 것은 깊이 모호성, 폐색, 그리고 객체 형태와 외관의 큰 변동성으로 인해 어렵습니다. 따라서 기존 연구는 알려진 객체 형태와 접촉과 같은 통제된 환경을 필요로 하며, 제한된 객체 클래스만 다룹니다. 대신, 우리는 자연 이미지와 새로운 객체 클래스에 일반화되는 방법이 필요합니다. 우리는 이를 두 가지 주요 방식으로 해결합니다: (1) 우리는 신체와 객체 메시 모두에 밀집된 3D 접촉이 고유하게 쌍을 이루는 자연 이미지의 새로운 데이터셋인 PICO-db를 수집합니다. 이를 위해, 우리는 최근 DAMON 데이터셋의 이미지를 사용하며, 이 이미지들은 접촉과 쌍을 이루지만, 이러한 접촉은 표준 3D 신체에만 주석이 달려 있습니다. 반대로, 우리는 신체와 객체 모두에 접촉 레이블을 원합니다. 이미지가 주어졌을 때 이를 추론하기 위해, 우리는 비전 기반 모델을 활용하여 데이터베이스에서 적절한 3D 객체 메시를 검색합니다. 그런 다음, 패치당 2번의 클릭만 필요한 새로운 방법을 통해 DAMON의 신체 접촉 패치를 객체에 투영합니다. 이 최소한의 인간 입력은 신체와 객체 간의 풍부한 접촉 대응 관계를 설정합니다. (2) 우리는 새로운 접촉 대응 데이터셋을 활용하여 PICO-fit이라는 새로운 렌더-앤-컴파어 피팅 방법을 통해 상호작용 중인 3D 신체와 객체 메시를 복원합니다. PICO-fit은 SMPL-X 신체에 대한 접촉을 추론하고, PICO-db에서 해당 객체에 대한 가능한 3D 객체 메시와 접촉을 검색한 후, 최적화를 통해 이미지 증거에 맞게 3D 신체와 객체 메시를 반복적으로 피팅합니다. 독특하게도, PICO-fit은 기존 방법이 다룰 수 없는 많은 객체 카테고리에서 잘 작동합니다. 이는 야생에서 HOI 이해를 확장하는 데 중요합니다. 우리의 데이터와 코드는 https://pico.is.tue.mpg.de에서 확인할 수 있습니다.

## 핵심 내용
단일 컬러 이미지에서 3D 인간-객체 상호작용(HOI)을 복원하는 것은 깊이 모호성, 폐색, 그리고 객체 형태와 외관의 큰 변동성으로 인해 어렵습니다. 따라서 기존 연구는 알려진 객체 형태와 접촉과 같은 통제된 환경을 필요로 하며, 제한된 객체 클래스만 다룹니다. 대신, 우리는 자연 이미지와 새로운 객체 클래스에 일반화되는 방법이 필요합니다. 우리는 이를 두 가지 주요 방식으로 해결합니다: (1) 우리는 신체와 객체 메시 모두에 밀집된 3D 접촉이 고유하게 쌍을 이루는 자연 이미지의 새로운 데이터셋인 PICO-db를 수집합니다. 이를 위해, 우리는 최근 DAMON 데이터셋의 이미지를 사용하며, 이 이미지들은 접촉과 쌍을 이루지만, 이러한 접촉은 표준 3D 신체에만 주석이 달려 있습니다. 반대로, 우리는 신체와 객체 모두에 접촉 레이블을 원합니다. 이미지가 주어졌을 때 이를 추론하기 위해, 우리는 비전 기반 모델을 활용하여 데이터베이스에서 적절한 3D 객체 메시를 검색합니다. 그런 다음, 패치당 2번의 클릭만 필요한 새로운 방법을 통해 DAMON의 신체 접촉 패치를 객체에 투영합니다. 이 최소한의 인간 입력은 신체와 객체 간의 풍부한 접촉 대응 관계를 설정합니다. (2) 우리는 새로운 접촉 대응 데이터셋을 활용하여 PICO-fit이라는 새로운 렌더-앤-컴파어 피팅 방법을 통해 상호작용 중인 3D 신체와 객체 메시를 복원합니다. PICO-fit은 SMPL-X 신체에 대한 접촉을 추론하고, PICO-db에서 해당 객체에 대한 가능한 3D 객체 메시와 접촉을 검색한 후, 최적화를 통해 이미지 증거에 맞게 3D 신체와 객체 메시를 반복적으로 피팅합니다. 독특하게도, PICO-fit은 기존 방법이 다룰 수 없는 많은 객체 카테고리에서 잘 작동합니다. 이는 야생에서 HOI 이해를 확장하는 데 중요합니다. 우리의 데이터와 코드는 https://pico.is.tue.mpg.de에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2504.17695v1
