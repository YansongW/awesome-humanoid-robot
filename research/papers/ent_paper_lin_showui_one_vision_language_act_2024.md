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
  zh: ShowUI 是微软于 2024 年提出、发表于 CVPR25 的视觉-语言-动作模型，专为 GUI 视觉智能体设计。其核心贡献包括 UI 引导的视觉令牌选择、交错式视觉-语言-动作流以及小规模高质量指令数据集，在零样本截图定位上达到
    75.1% 的准确率，并减少 33% 冗余视觉令牌。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.17465v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (749 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: ShowUI source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
ShowUI 旨在解决现有 GUI 智能体依赖文本元信息（如 HTML）而缺乏视觉感知能力的问题。该模型通过 UI 引导的视觉令牌选择，将截图构建为 UI 连接图，自适应识别冗余关系并优化自注意力中的令牌选择，从而降低计算成本。同时，交错式视觉-语言-动作流统一了 GUI 任务中的多种需求，有效管理导航中的视觉-动作历史或配对多轮查询-动作序列。此外，通过精心数据整理和重采样策略，模型仅用 256K 数据训练，在零样本截图定位上达到 75.1% 准确率，并实现 1.4 倍速度提升。

## 核心内容
### 方法
- **UI 引导的视觉令牌选择**：将截图建模为 UI 连接图，通过图结构自适应识别冗余视觉令牌，并在自注意力块中作为选择标准，减少 33% 的冗余令牌。
- **交错式视觉-语言-动作流**：灵活统一 GUI 任务中的视觉、语言和动作需求，支持导航中视觉-动作历史的管理，或每张截图的多轮查询-动作序列配对，提升训练效率。
- **小规模高质量指令数据集**：通过数据整理和重采样策略解决数据类型不平衡问题，仅用 256K 数据训练。

### 实验设置与结果
- **模型规模**：轻量级 2B 参数模型。
- **零样本截图定位**：在未见过的截图任务上达到 75.1% 准确率。
- **效率提升**：UI 引导的令牌选择在训练中减少 33% 冗余视觉令牌，并实现 1.4 倍速度提升。
- **导航实验**：在 Web 环境 Mind2Web、移动环境 AITW 和在线环境 MiniWob 上验证了模型的有效性。

### 结论
ShowUI 通过视觉感知和高效令牌选择，显著提升了 GUI 视觉智能体的性能，在多个基准上展示了其潜力。模型代码已开源。

## Overview
Building Graphical User Interface (GUI) assistants holds significant promise for enhancing human workflow productivity. While most agents are language-based, relying on closed-source API with text-rich meta-information (e.g., HTML or accessibility tree), they show limitations in perceiving UI visuals as humans do, highlighting the need for GUI visual agents. In this work, we develop a vision-language-action model in digital world, namely ShowUI, which features the following innovations: (i) UI-Guided Visual Token Selection to reduce computational costs by formulating screenshots as an UI connected graph, adaptively identifying their redundant relationship and serve as the criteria for token selection during self-attention blocks; (ii) Interleaved Vision-Language-Action Streaming that flexibly unifies diverse needs within GUI tasks, enabling effective management of visual-action history in navigation or pairing multi-turn query-action sequences per screenshot to enhance training efficiency; (iii) Small-scale High-quality GUI Instruction-following Datasets by careful data curation and employing a resampling strategy to address significant data type imbalances. With above components, ShowUI, a lightweight 2B model using 256K data, achieves a strong 75.1% accuracy in zero-shot screenshot grounding. Its UI-guided token selection further reduces 33% of redundant visual tokens during training and speeds up the performance by 1.4x. Navigation experiments across web Mind2Web, mobile AITW, and online MiniWob environments further underscore the effectiveness and potential of our model in advancing GUI visual agents. The models are available at https://github.com/showlab/ShowUI.

## 参考
- http://arxiv.org/abs/2411.17465v1

## 개요
ShowUI는 기존 GUI 에이전트가 HTML과 같은 텍스트 메타정보에 의존하여 시각적 인식 능력이 부족한 문제를 해결하는 것을 목표로 합니다. 이 모델은 UI 기반 시각 토큰 선택을 통해 스크린샷을 UI 연결 그래프로 구축하고, 적응적으로 중복 관계를 식별하며 자기 주의(self-attention)에서 토큰 선택을 최적화하여 계산 비용을 줄입니다. 동시에, 인터리브된 시각-언어-행동 흐름은 GUI 작업의 다양한 요구를 통합하여 내비게이션 중 시각-행동 기록 또는 다중 턴 쿼리-행동 시퀀스 쌍을 효과적으로 관리합니다. 또한, 정교한 데이터 정리 및 재샘플링 전략을 통해 모델은 256K 데이터만으로 훈련하여 제로샷 스크린샷 위치 파악에서 75.1% 정확도를 달성하고 1.4배 속도 향상을 실현합니다.

## 핵심 내용
### 방법
- **UI 기반 시각 토큰 선택**: 스크린샷을 UI 연결 그래프로 모델링하고, 그래프 구조를 통해 중복 시각 토큰을 적응적으로 식별하며, 자기 주의 블록에서 선택 기준으로 사용하여 33%의 중복 토큰을 줄입니다.
- **인터리브된 시각-언어-행동 흐름**: GUI 작업의 시각, 언어, 행동 요구를 유연하게 통합하여 내비게이션 중 시각-행동 기록 관리 또는 각 스크린샷의 다중 턴 쿼리-행동 시퀀스 쌍을 지원하여 훈련 효율성을 향상시킵니다.
- **소규모 고품질 명령 데이터셋**: 데이터 정리 및 재샘플링 전략을 통해 데이터 유형 불균형 문제를 해결하고 256K 데이터만으로 훈련합니다.

### 실험 설정 및 결과
- **모델 규모**: 경량 2B 파라미터 모델.
- **제로샷 스크린샷 위치 파악**: 보지 못한 스크린샷 작업에서 75.1% 정확도 달성.
- **효율성 향상**: UI 기반 토큰 선택이 훈련 중 33%의 중복 시각 토큰을 줄이고 1.4배 속도 향상을 실현.
- **내비게이션 실험**: 웹 환경 Mind2Web, 모바일 환경 AITW 및 온라인 환경 MiniWob에서 모델의 유효성을 검증.

### 결론
ShowUI는 시각적 인식과 효율적인 토큰 선택을 통해 GUI 시각 에이전트의 성능을 크게 향상시키며, 여러 벤치마크에서 잠재력을 입증합니다. 모델 코드는 오픈소스로 공개되었습니다.
