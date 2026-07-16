---
$id: ent_paper_lin_showui_one_vision_language_act_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent'
  zh: ShowUI
  ko: 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent'
summary:
  en: 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent (ShowUI), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by Microsoft, and published at CVPR25.'
  zh: 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent (ShowUI), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by Microsoft, and published at CVPR25.'
  ko: 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent (ShowUI), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by Microsoft, and published at CVPR25.'
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
- robotic_manipulation
- showui
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.17465v1.
sources:
- id: src_001
  type: website
  title: ShowUI source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Building Graphical User Interface (GUI) assistants holds significant promise for enhancing human workflow productivity. While most agents are language-based, relying on closed-source API with text-rich meta-information (e.g., HTML or accessibility tree), they show limitations in perceiving UI visuals as humans do, highlighting the need for GUI visual agents. In this work, we develop a vision-language-action model in digital world, namely ShowUI, which features the following innovations: (i) UI-Guided Visual Token Selection to reduce computational costs by formulating screenshots as an UI connected graph, adaptively identifying their redundant relationship and serve as the criteria for token selection during self-attention blocks; (ii) Interleaved Vision-Language-Action Streaming that flexibly unifies diverse needs within GUI tasks, enabling effective management of visual-action history in navigation or pairing multi-turn query-action sequences per screenshot to enhance training efficiency; (iii) Small-scale High-quality GUI Instruction-following Datasets by careful data curation and employing a resampling strategy to address significant data type imbalances. With above components, ShowUI, a lightweight 2B model using 256K data, achieves a strong 75.1% accuracy in zero-shot screenshot grounding. Its UI-guided token selection further reduces 33% of redundant visual tokens during training and speeds up the performance by 1.4x. Navigation experiments across web Mind2Web, mobile AITW, and online MiniWob environments further underscore the effectiveness and potential of our model in advancing GUI visual agents. The models are available at https://github.com/showlab/ShowUI.

## 核心内容
Building Graphical User Interface (GUI) assistants holds significant promise for enhancing human workflow productivity. While most agents are language-based, relying on closed-source API with text-rich meta-information (e.g., HTML or accessibility tree), they show limitations in perceiving UI visuals as humans do, highlighting the need for GUI visual agents. In this work, we develop a vision-language-action model in digital world, namely ShowUI, which features the following innovations: (i) UI-Guided Visual Token Selection to reduce computational costs by formulating screenshots as an UI connected graph, adaptively identifying their redundant relationship and serve as the criteria for token selection during self-attention blocks; (ii) Interleaved Vision-Language-Action Streaming that flexibly unifies diverse needs within GUI tasks, enabling effective management of visual-action history in navigation or pairing multi-turn query-action sequences per screenshot to enhance training efficiency; (iii) Small-scale High-quality GUI Instruction-following Datasets by careful data curation and employing a resampling strategy to address significant data type imbalances. With above components, ShowUI, a lightweight 2B model using 256K data, achieves a strong 75.1% accuracy in zero-shot screenshot grounding. Its UI-guided token selection further reduces 33% of redundant visual tokens during training and speeds up the performance by 1.4x. Navigation experiments across web Mind2Web, mobile AITW, and online MiniWob environments further underscore the effectiveness and potential of our model in advancing GUI visual agents. The models are available at https://github.com/showlab/ShowUI.

## 参考
- http://arxiv.org/abs/2411.17465v1

## Overview
Building Graphical User Interface (GUI) assistants holds significant promise for enhancing human workflow productivity. While most agents are language-based, relying on closed-source API with text-rich meta-information (e.g., HTML or accessibility tree), they show limitations in perceiving UI visuals as humans do, highlighting the need for GUI visual agents. In this work, we develop a vision-language-action model in digital world, namely ShowUI, which features the following innovations: (i) UI-Guided Visual Token Selection to reduce computational costs by formulating screenshots as an UI connected graph, adaptively identifying their redundant relationship and serve as the criteria for token selection during self-attention blocks; (ii) Interleaved Vision-Language-Action Streaming that flexibly unifies diverse needs within GUI tasks, enabling effective management of visual-action history in navigation or pairing multi-turn query-action sequences per screenshot to enhance training efficiency; (iii) Small-scale High-quality GUI Instruction-following Datasets by careful data curation and employing a resampling strategy to address significant data type imbalances. With above components, ShowUI, a lightweight 2B model using 256K data, achieves a strong 75.1% accuracy in zero-shot screenshot grounding. Its UI-guided token selection further reduces 33% of redundant visual tokens during training and speeds up the performance by 1.4x. Navigation experiments across web Mind2Web, mobile AITW, and online MiniWob environments further underscore the effectiveness and potential of our model in advancing GUI visual agents. The models are available at https://github.com/showlab/ShowUI.

## Content
Building Graphical User Interface (GUI) assistants holds significant promise for enhancing human workflow productivity. While most agents are language-based, relying on closed-source API with text-rich meta-information (e.g., HTML or accessibility tree), they show limitations in perceiving UI visuals as humans do, highlighting the need for GUI visual agents. In this work, we develop a vision-language-action model in digital world, namely ShowUI, which features the following innovations: (i) UI-Guided Visual Token Selection to reduce computational costs by formulating screenshots as an UI connected graph, adaptively identifying their redundant relationship and serve as the criteria for token selection during self-attention blocks; (ii) Interleaved Vision-Language-Action Streaming that flexibly unifies diverse needs within GUI tasks, enabling effective management of visual-action history in navigation or pairing multi-turn query-action sequences per screenshot to enhance training efficiency; (iii) Small-scale High-quality GUI Instruction-following Datasets by careful data curation and employing a resampling strategy to address significant data type imbalances. With above components, ShowUI, a lightweight 2B model using 256K data, achieves a strong 75.1% accuracy in zero-shot screenshot grounding. Its UI-guided token selection further reduces 33% of redundant visual tokens during training and speeds up the performance by 1.4x. Navigation experiments across web Mind2Web, mobile AITW, and online MiniWob environments further underscore the effectiveness and potential of our model in advancing GUI visual agents. The models are available at https://github.com/showlab/ShowUI.

## 개요
GUI(Graphical User Interface) 어시스턴트를 구축하는 것은 인간의 작업 흐름 생산성을 향상시키는 데 큰 가능성을 지니고 있습니다. 대부분의 에이전트는 언어 기반으로, 폐쇄형 API와 텍스트가 풍부한 메타 정보(예: HTML 또는 접근성 트리)에 의존하지만, 인간처럼 UI 시각적 요소를 인식하는 데 한계가 있어 GUI 시각적 에이전트의 필요성이 부각됩니다. 본 연구에서는 디지털 세계에서의 비전-언어-행동 모델인 ShowUI를 개발했으며, 이는 다음과 같은 혁신을 특징으로 합니다: (i) UI 기반 시각적 토큰 선택: 스크린샷을 UI 연결 그래프로 구성하여 중복 관계를 적응적으로 식별하고, 자기 주의 블록에서 토큰 선택 기준으로 활용함으로써 계산 비용을 절감합니다; (ii) 인터리브드 비전-언어-행동 스트리밍: GUI 작업 내 다양한 요구를 유연하게 통합하여, 탐색에서 시각-행동 기록을 효과적으로 관리하거나 스크린샷당 다중 턴 쿼리-행동 시퀀스를 쌍으로 연결하여 훈련 효율성을 향상시킵니다; (iii) 소규모 고품질 GUI 명령어 수행 데이터셋: 신중한 데이터 큐레이션과 데이터 유형 불균형을 해결하기 위한 재샘플링 전략을 통해 구축됩니다. 이러한 구성 요소를 바탕으로, 256K 데이터를 사용한 경량 2B 모델인 ShowUI는 제로샷 스크린샷 그라운딩에서 75.1%의 높은 정확도를 달성합니다. UI 기반 토큰 선택은 훈련 중 중복 시각적 토큰을 33% 추가로 줄이고 성능을 1.4배 향상시킵니다. 웹 Mind2Web, 모바일 AITW, 온라인 MiniWob 환경에서의 탐색 실험은 GUI 시각적 에이전트 발전에 있어 우리 모델의 효과성과 잠재력을 더욱 강조합니다. 모델은 https://github.com/showlab/ShowUI에서 확인할 수 있습니다.

## 핵심 내용
GUI(Graphical User Interface) 어시스턴트를 구축하는 것은 인간의 작업 흐름 생산성을 향상시키는 데 큰 가능성을 지니고 있습니다. 대부분의 에이전트는 언어 기반으로, 폐쇄형 API와 텍스트가 풍부한 메타 정보(예: HTML 또는 접근성 트리)에 의존하지만, 인간처럼 UI 시각적 요소를 인식하는 데 한계가 있어 GUI 시각적 에이전트의 필요성이 부각됩니다. 본 연구에서는 디지털 세계에서의 비전-언어-행동 모델인 ShowUI를 개발했으며, 이는 다음과 같은 혁신을 특징으로 합니다: (i) UI 기반 시각적 토큰 선택: 스크린샷을 UI 연결 그래프로 구성하여 중복 관계를 적응적으로 식별하고, 자기 주의 블록에서 토큰 선택 기준으로 활용함으로써 계산 비용을 절감합니다; (ii) 인터리브드 비전-언어-행동 스트리밍: GUI 작업 내 다양한 요구를 유연하게 통합하여, 탐색에서 시각-행동 기록을 효과적으로 관리하거나 스크린샷당 다중 턴 쿼리-행동 시퀀스를 쌍으로 연결하여 훈련 효율성을 향상시킵니다; (iii) 소규모 고품질 GUI 명령어 수행 데이터셋: 신중한 데이터 큐레이션과 데이터 유형 불균형을 해결하기 위한 재샘플링 전략을 통해 구축됩니다. 이러한 구성 요소를 바탕으로, 256K 데이터를 사용한 경량 2B 모델인 ShowUI는 제로샷 스크린샷 그라운딩에서 75.1%의 높은 정확도를 달성합니다. UI 기반 토큰 선택은 훈련 중 중복 시각적 토큰을 33% 추가로 줄이고 성능을 1.4배 향상시킵니다. 웹 Mind2Web, 모바일 AITW, 온라인 MiniWob 환경에서의 탐색 실험은 GUI 시각적 에이전트 발전에 있어 우리 모델의 효과성과 잠재력을 더욱 강조합니다. 모델은 https://github.com/showlab/ShowUI에서 확인할 수 있습니다.
