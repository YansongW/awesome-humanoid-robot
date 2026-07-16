---
$id: ent_paper_dextercap_an_affordable_and_au_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation'
  zh: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation'
  ko: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation'
summary:
  en: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  zh: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  ko: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation is a 2026 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dextercap
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.05844v2.
sources:
- id: src_001
  type: paper
  title: 'DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation (arXiv)'
  url: https://arxiv.org/abs/2601.05844
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Capturing fine-grained hand-object interactions is challenging due to severe self-occlusion from closely spaced fingers and the subtlety of in-hand manipulation motions. Existing optical motion capture systems rely on expensive camera setups and extensive manual post-processing, while low-cost vision-based methods often suffer from reduced accuracy and reliability under occlusion. To address these challenges, we present DexterCap, a low-cost optical capture system for dexterous in-hand manipulation. DexterCap uses dense, character-coded marker patches to achieve robust tracking under severe self-occlusion, together with an automated reconstruction pipeline that requires minimal manual effort. With DexterCap, we introduce DexterHand, a dataset of fine-grained hand-object interactions covering diverse manipulation behaviors and objects, from simple primitives to complex articulated objects such as a Rubik's Cube. We release the dataset and code to support future research on dexterous hand-object interaction. Project website: https://pku-mocca.github.io/Dextercap-Page/

## 核心内容
Capturing fine-grained hand-object interactions is challenging due to severe self-occlusion from closely spaced fingers and the subtlety of in-hand manipulation motions. Existing optical motion capture systems rely on expensive camera setups and extensive manual post-processing, while low-cost vision-based methods often suffer from reduced accuracy and reliability under occlusion. To address these challenges, we present DexterCap, a low-cost optical capture system for dexterous in-hand manipulation. DexterCap uses dense, character-coded marker patches to achieve robust tracking under severe self-occlusion, together with an automated reconstruction pipeline that requires minimal manual effort. With DexterCap, we introduce DexterHand, a dataset of fine-grained hand-object interactions covering diverse manipulation behaviors and objects, from simple primitives to complex articulated objects such as a Rubik's Cube. We release the dataset and code to support future research on dexterous hand-object interaction. Project website: https://pku-mocca.github.io/Dextercap-Page/

## 参考
- http://arxiv.org/abs/2601.05844v2

## Overview
Capturing fine-grained hand-object interactions is challenging due to severe self-occlusion from closely spaced fingers and the subtlety of in-hand manipulation motions. Existing optical motion capture systems rely on expensive camera setups and extensive manual post-processing, while low-cost vision-based methods often suffer from reduced accuracy and reliability under occlusion. To address these challenges, we present DexterCap, a low-cost optical capture system for dexterous in-hand manipulation. DexterCap uses dense, character-coded marker patches to achieve robust tracking under severe self-occlusion, together with an automated reconstruction pipeline that requires minimal manual effort. With DexterCap, we introduce DexterHand, a dataset of fine-grained hand-object interactions covering diverse manipulation behaviors and objects, from simple primitives to complex articulated objects such as a Rubik's Cube. We release the dataset and code to support future research on dexterous hand-object interaction. Project website: https://pku-mocca.github.io/Dextercap-Page/

## Content
Capturing fine-grained hand-object interactions is challenging due to severe self-occlusion from closely spaced fingers and the subtlety of in-hand manipulation motions. Existing optical motion capture systems rely on expensive camera setups and extensive manual post-processing, while low-cost vision-based methods often suffer from reduced accuracy and reliability under occlusion. To address these challenges, we present DexterCap, a low-cost optical capture system for dexterous in-hand manipulation. DexterCap uses dense, character-coded marker patches to achieve robust tracking under severe self-occlusion, together with an automated reconstruction pipeline that requires minimal manual effort. With DexterCap, we introduce DexterHand, a dataset of fine-grained hand-object interactions covering diverse manipulation behaviors and objects, from simple primitives to complex articulated objects such as a Rubik's Cube. We release the dataset and code to support future research on dexterous hand-object interaction. Project website: https://pku-mocca.github.io/Dextercap-Page/

## 개요
손가락 간의 좁은 간격으로 인한 심각한 자기 가림과 손 안에서의 조작 동작의 미묘함 때문에 세밀한 손-물체 상호작용을 포착하는 것은 어렵습니다. 기존의 광학 모션 캡처 시스템은 고가의 카메라 설정과 광범위한 수동 후처리에 의존하는 반면, 저비용 비전 기반 방법은 가림 상태에서 정확도와 신뢰성이 떨어지는 경우가 많습니다. 이러한 문제를 해결하기 위해 우리는 DexterCap, 즉 손 안에서의 정교한 조작을 위한 저비용 광학 캡처 시스템을 제시합니다. DexterCap은 밀집된 문자 코드 마커 패치를 사용하여 심각한 자기 가림 상태에서도 강건한 추적을 달성하며, 최소한의 수동 작업만 필요한 자동 재구성 파이프라인을 갖추고 있습니다. DexterCap을 통해 우리는 DexterHand 데이터셋을 소개합니다. 이 데이터셋은 단순한 기본 물체부터 루빅스 큐브와 같은 복잡한 관절 물체에 이르기까지 다양한 조작 행동과 물체를 포함하는 세밀한 손-물체 상호작용을 다룹니다. 우리는 데이터셋과 코드를 공개하여 정교한 손-물체 상호작용에 대한 향후 연구를 지원합니다. 프로젝트 웹사이트: https://pku-mocca.github.io/Dextercap-Page/

## 핵심 내용
손가락 간의 좁은 간격으로 인한 심각한 자기 가림과 손 안에서의 조작 동작의 미묘함 때문에 세밀한 손-물체 상호작용을 포착하는 것은 어렵습니다. 기존의 광학 모션 캡처 시스템은 고가의 카메라 설정과 광범위한 수동 후처리에 의존하는 반면, 저비용 비전 기반 방법은 가림 상태에서 정확도와 신뢰성이 떨어지는 경우가 많습니다. 이러한 문제를 해결하기 위해 우리는 DexterCap, 즉 손 안에서의 정교한 조작을 위한 저비용 광학 캡처 시스템을 제시합니다. DexterCap은 밀집된 문자 코드 마커 패치를 사용하여 심각한 자기 가림 상태에서도 강건한 추적을 달성하며, 최소한의 수동 작업만 필요한 자동 재구성 파이프라인을 갖추고 있습니다. DexterCap을 통해 우리는 DexterHand 데이터셋을 소개합니다. 이 데이터셋은 단순한 기본 물체부터 루빅스 큐브와 같은 복잡한 관절 물체에 이르기까지 다양한 조작 행동과 물체를 포함하는 세밀한 손-물체 상호작용을 다룹니다. 우리는 데이터셋과 코드를 공개하여 정교한 손-물체 상호작용에 대한 향후 연구를 지원합니다. 프로젝트 웹사이트: https://pku-mocca.github.io/Dextercap-Page/
