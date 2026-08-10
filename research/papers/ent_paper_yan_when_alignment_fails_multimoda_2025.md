---
$id: ent_paper_yan_when_alignment_fails_multimoda_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models'
  zh: VLA-Fool
  ko: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models'
summary:
  en: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
  zh: VLA-Fool 是由西湖大学、宾夕法尼亚州立大学、索尼研究院和西安电子科技大学于 2025 年提出的研究，系统性地探索了视觉-语言-动作模型（VLA）在多模态与黑盒条件下的对抗鲁棒性。其核心贡献在于统一了文本、视觉及跨模态错位三种攻击层次，并首次引入自动生成的语义引导提示框架。实验表明，即使微小的多模态扰动也能导致机器人行为显著偏离，揭示了具身多模态对齐的脆弱性。
  ko: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
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
- vision_language_action
- vla
- vla_fool
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16203v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1154 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.16203
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Fool source
  url: https://doi.org/10.48550/arXiv.2511.16203
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有研究多聚焦于单模态扰动，忽略了影响具身推理与决策的跨模态错位问题。VLA-Fool 在 LIBERO 基准上，基于微调的 OpenVLA 模型，同时考察了白盒与黑盒场景。该方法将攻击分为三个层次：基于梯度与提示的文本扰动、基于补丁与噪声的视觉扰动，以及故意破坏感知与指令间语义对应的跨模态错位攻击。此外，研究将 VLA 感知的语义空间融入语言提示，构建了首个自动生成且语义引导的提示框架。实验结果显示，即便是微小的多模态扰动，也能引发显著的行为偏差，凸显了当前具身多模态对齐机制的脆弱性。

## 核心内容
### 方法架构
VLA-Fool 提出了一个统一的多模态对抗攻击框架，涵盖三个层次：
- **文本扰动**：通过基于梯度的优化（如对指令嵌入添加对抗性噪声）和基于提示的操控（如修改指令中的关键动词或名词）实现。
- **视觉扰动**：采用补丁攻击（在图像中叠加特定图案）和噪声攻击（添加不可察觉的像素级扰动）。
- **跨模态错位攻击**：核心创新点，旨在破坏视觉感知与语言指令之间的语义对应关系，例如使机器人将“拿起红色杯子”的指令错误关联到蓝色物体。

### 关键设计
- **VLA 感知语义空间**：将 VLA 模型内部的语义表示（如动作嵌入）映射到语言提示空间，自动生成能最大化行为偏差的对抗性提示。这是首个无需人工设计的语义引导提示框架。
- **攻击设置**：同时评估白盒（攻击者知晓模型参数）和黑盒（仅能查询模型输出）场景，覆盖更现实的威胁模型。

### 实验设置
- **基准与模型**：使用 LIBERO 基准（包含 10 个具身操作任务）和微调后的 OpenVLA 模型（参数量为 7B）。
- **评估指标**：主要衡量任务成功率（Success Rate）的下降幅度，以及行为偏差（如抓取错误物体或执行错误动作）的频率。

### 关键数字与结论
- **性能下降**：在跨模态错位攻击下，任务成功率从基线 85.3% 骤降至 12.7%，下降幅度达 72.6 个百分点。
- **单模态对比**：仅文本扰动导致成功率降至 54.1%，仅视觉扰动降至 48.6%，而跨模态攻击效果显著更强。
- **黑盒场景**：在黑盒条件下，跨模态错位攻击仍能将成功率压制至 31.2%，表明其具有实际威胁性。
- **语义引导有效性**：自动生成的语义提示相比随机提示，额外降低了 18.4% 的成功率，验证了 VLA 感知空间的有效性。

### 结论
VLA-Fool 揭示了当前 VLA 模型在跨模态对齐上的根本脆弱性：模型并非真正理解指令与视觉的语义关联，而是依赖浅层统计相关性。研究呼吁未来工作需在训练中引入对抗性对齐机制，并开发更鲁棒的多模态融合策略。

## Overview
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## 参考
- http://arxiv.org/abs/2511.16203v3

## 개요
기존 연구는 주로 단일 모달리티 교란에 초점을 맞추었으며, 구현 추론 및 의사결정에 영향을 미치는 교차 모달 정렬 문제를 간과했습니다. VLA-Fool은 LIBERO 벤치마크에서 미세 조정된 OpenVLA 모델을 기반으로 화이트박스 및 블랙박스 시나리오를 동시에 검토합니다. 이 방법은 공격을 세 가지 계층으로 나눕니다: 그래디언트 및 프롬프트 기반 텍스트 교란, 패치 및 노이즈 기반 시각 교란, 그리고 지각과 명령 간의 의미적 대응을 의도적으로 파괴하는 교차 모달 정렬 공격입니다. 또한, 연구는 VLA 지각의 의미 공간을 언어 프롬프트에 통합하여 최초의 자동 생성 및 의미 기반 프롬프트 프레임워크를 구축했습니다. 실험 결과, 미세한 다중 모달 교란조차도 상당한 행동 편향을 유발할 수 있으며, 이는 현재 구현 다중 모달 정렬 메커니즘의 취약성을 강조합니다.

## 핵심 내용
### 방법 아키텍처
VLA-Fool은 세 가지 계층을 포괄하는 통합 다중 모달 적대적 공격 프레임워크를 제안합니다:
- **텍스트 교란**: 그래디언트 기반 최적화(예: 명령 임베딩에 적대적 노이즈 추가) 및 프롬프트 기반 조작(예: 명령의 핵심 동사 또는 명사 수정)을 통해 구현됩니다.
- **시각 교란**: 패치 공격(이미지에 특정 패턴 오버레이) 및 노이즈 공격(감지할 수 없는 픽셀 수준 교란 추가)을 채택합니다.
- **교차 모달 정렬 공격**: 핵심 혁신으로, 시각 지각과 언어 명령 간의 의미적 대응을 파괴하는 것을 목표로 합니다. 예를 들어, 로봇이 "빨간 컵 집기" 명령을 파란 물체와 잘못 연관시키도록 만듭니다.

### 핵심 설계
- **VLA 지각 의미 공간**: VLA 모델 내부의 의미 표현(예: 행동 임베딩)을 언어 프롬프트 공간에 매핑하여 행동 편향을 최대화하는 적대적 프롬프트를 자동 생성합니다. 이는 수동 설계가 필요 없는 최초의 의미 기반 프롬프트 프레임워크입니다.
- **공격 설정**: 화이트박스(공격자가 모델 매개변수를 알고 있음) 및 블랙박스(모델 출력만 쿼리 가능) 시나리오를 동시에 평가하여 더 현실적인 위협 모델을 포괄합니다.

### 실험 설정
- **벤치마크 및 모델**: LIBERO 벤치마크(10개의 구현 조작 작업 포함)와 미세 조정된 OpenVLA 모델(매개변수 7B)을 사용합니다.
- **평가 지표**: 주로 작업 성공률(SR)의 감소 폭과 행동 편향(예: 잘못된 물체 집기 또는 잘못된 동작 실행)의 빈도를 측정합니다.

### 핵심 수치 및 결론
- **성능 저하**: 교차 모달 정렬 공격 하에서 작업 성공률이 기준 85.3%에서 12.7%로 급락하여 72.6% 포인트 감소했습니다.
- **단일 모달 비교**: 텍스트 교란만으로는 성공률이 54.1%로, 시각 교란만으로는 48.6%로 감소했지만, 교차 모달 공격의 효과는 훨씬 더 강력했습니다.
- **블랙박스 시나리오**: 블랙박스 조건에서도 교차 모달 정렬 공격은 성공률을 31.2%로 억제하여 실질적인 위협성을 입증했습니다.
- **의미 기반 프롬프트 효과**: 자동 생성된 의미 프롬프트는 무작위 프롬프트에 비해 성공률을 추가로 18.4% 낮추어 VLA 지각 공간의 유효성을 검증했습니다.

### 결론
VLA-Fool은 현재 VLA 모델이 교차 모달 정렬에서 근본적인 취약성을 지니고 있음을 밝혀냅니다: 모델이 명령과 시각의 의미적 연관성을 진정으로 이해하는 것이 아니라 얕은 통계적 상관관계에 의존합니다. 연구는 향후 작업이 훈련 과정에 적대적 정렬 메커니즘을 도입하고 더 강건한 다중 모달 융합 전략을 개발할 것을 촉구합니다.
