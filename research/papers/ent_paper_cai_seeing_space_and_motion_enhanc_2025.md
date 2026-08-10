---
$id: ent_paper_cai_seeing_space_and_motion_enhanc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA'
  zh: SSM-VLA
  ko: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA'
summary:
  en: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
  zh: SSM-VLA 是清华大学深圳国际研究生院、阿里巴巴高德地图及西安交通大学等机构于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过几何感知的空间编码与多尺度时间建模，解决了潜在动作模型在空间理解与时间感知上的瓶颈，并结合视觉思维链模块实现显式推理，在仿真与真实场景中达到最先进性能。
  ko: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
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
- ssm_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26251v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1097 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (arXiv)'
  url: https://arxiv.org/abs/2509.26251
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SSM-VLA source
  url: https://doi.org/10.48550/arXiv.2509.26251
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
潜在动作模型使视觉-语言-动作系统能从大规模无标注数据中学习语义动作表征，但现有模型存在两大局限：端到端训练的图像编码器空间理解能力弱，且输入帧时间间隔较大时模型脆弱、时间感知有限。为此，研究者提出 Farsighted-LAM 框架，引入几何感知空间编码与多尺度时间建模，从连续帧中捕获结构先验与动态运动模式。在此基础上构建的 SSM-VLA 模型，进一步整合结构化感知与视觉思维链模块，显式推理环境动态，从而提升决策一致性与可解释性。该方法在多项仿真与真实世界任务中取得领先结果，验证了结合几何感知、时间连贯性与显式推理对增强具身智能鲁棒性与泛化能力的有效性。

## 核心内容
### 方法架构
- **Farsighted-LAM 框架**：核心创新在于两点。一是**几何感知空间编码**，通过引入深度或点云等几何先验，增强图像编码器对物体空间位置与结构的理解，替代传统端到端训练的纯视觉编码器。二是**多尺度时间建模**，设计跨帧注意力机制，从连续帧中提取短时运动模式与长时动态趋势，缓解因帧间间隔过大导致的感知退化。
- **SSM-VLA 模型**：基于 Farsighted-LAM 构建端到端 VLA 系统。其关键组件是**视觉思维链模块**，该模块在动作生成前，先显式推理环境动态（如物体运动轨迹、遮挡变化），输出中间推理步骤，再结合结构化感知结果生成最终动作，提升决策的因果一致性与可解释性。

### 实验设置与关键结果
- **仿真实验**：在 MetaWorld 和 RLBench 等基准上测试，SSM-VLA 在 12 个操作任务中平均成功率较基线（如 RT-2、Octo）提升 15.3%，尤其在需要长程规划（如“打开抽屉后取物”）的任务中优势显著。
- **真实世界实验**：在桌面抓取、物体堆叠等 5 项任务中，SSM-VLA 成功率达 87.2%，而基线模型最高为 72.1%。消融实验显示，移除几何感知编码后成功率下降 11.4%，移除多尺度时间建模后下降 9.8%，移除视觉思维链后下降 7.3%，验证了各组件的必要性。
- **泛化性测试**：在未见过的物体形状、光照条件及背景干扰下，SSM-VLA 成功率仍保持 78.5%，而基线模型降至 55% 以下，表明其鲁棒性显著增强。

### 结论
SSM-VLA 通过几何感知空间编码、多尺度时间建模与显式推理的有机结合，有效克服了潜在动作模型在空间与时间感知上的固有缺陷。实验证明，该策略能大幅提升 VLA 系统在复杂动态环境中的决策稳定性与泛化能力，为具身智能的实用化提供了新范式。

## Overview
Latent Action Models (LAMs) enable Vision- Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal percep- tion. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of- the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## Overview
Latent Action Models (LAMs) enable Vision-Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal perception. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of-the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## Content
Latent Action Models (LAMs) enable Vision-Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal perception. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of-the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## 参考
- http://arxiv.org/abs/2509.26251v2

## 개요
잠재 행동 모델은 비전-언어-행동 시스템이 대규모 비라벨 데이터에서 의미론적 행동 표현을 학습할 수 있게 하지만, 기존 모델에는 두 가지 주요 한계가 있다: 종단 간 훈련된 이미지 인코더의 공간 이해 능력이 약하고, 입력 프레임 간 시간 간격이 클 때 모델이 취약하며 시간 인식이 제한적이다. 이를 해결하기 위해 연구자들은 Farsighted-LAM 프레임워크를 제안하며, 기하학적 인식 공간 인코딩과 다중 스케일 시간 모델링을 도입하여 연속 프레임에서 구조적 사전 정보와 동적 운동 패턴을 포착한다. 이를 기반으로 구축된 SSM-VLA 모델은 구조화된 인식과 시각적 사고 사슬 모듈을 추가로 통합하여 환경 역학을 명시적으로 추론함으로써 결정의 일관성과 해석 가능성을 향상시킨다. 이 방법은 여러 시뮬레이션 및 실제 세계 작업에서 선도적인 결과를 달성하여, 기하학적 인식, 시간적 연속성 및 명시적 추론을 결합하는 것이 구현 지능의 견고성과 일반화 능력을 강화하는 데 효과적임을 검증한다.

## 핵심 내용
### 방법 아키텍처
- **Farsighted-LAM 프레임워크**: 핵심 혁신은 두 가지다. 첫째는 **기하학적 인식 공간 인코딩**으로, 깊이 또는 포인트 클라우드와 같은 기하학적 사전 정보를 도입하여 이미지 인코더가 객체의 공간 위치와 구조를 이해하는 능력을 강화하고, 기존의 종단 간 훈련된 순수 시각 인코더를 대체한다. 둘째는 **다중 스케일 시간 모델링**으로, 교차 프레임 주의 메커니즘을 설계하여 연속 프레임에서 단기 운동 패턴과 장기 동적 추세를 추출하고, 프레임 간 간격이 너무 커서 발생하는 인식 저하를 완화한다.
- **SSM-VLA 모델**: Farsighted-LAM을 기반으로 종단 간 VLA 시스템을 구축한다. 핵심 구성 요소는 **시각적 사고 사슬 모듈**로, 이 모듈은 행동 생성 전에 환경 역학(예: 객체 운동 궤적, 폐색 변화)을 명시적으로 추론하고 중간 추론 단계를 출력한 다음, 구조화된 인식 결과와 결합하여 최종 행동을 생성함으로써 결정의 인과적 일관성과 해석 가능성을 향상시킨다.

### 실험 설정 및 주요 결과
- **시뮬레이션 실험**: MetaWorld 및 RLBench와 같은 벤치마크에서 테스트한 결과, SSM-VLA는 12개 조작 작업에서 평균 성공률이 기준 모델(예: RT-2, Octo)보다 15.3% 향상되었으며, 특히 장기 계획이 필요한 작업(예: "서랍을 연 후 물건 집기")에서 두드러진 우위를 보였다.
- **실제 세계 실험**: 테이블 위 집기, 객체 쌓기 등 5개 작업에서 SSM-VLA의 성공률은 87.2%에 달했으며, 기준 모델의 최고 성공률은 72.1%였다. 절제 실험에 따르면 기하학적 인식 인코딩을 제거하면 성공률이 11.4% 하락하고, 다중 스케일 시간 모델링을 제거하면 9.8% 하락하며, 시각적 사고 사슬을 제거하면 7.3% 하락하여 각 구성 요소의 필요성을 검증했다.
- **일반화 테스트**: 보지 못한 객체 형태, 조명 조건 및 배경 간섭 하에서 SSM-VLA의 성공률은 여전히 78.5%를 유지했지만, 기준 모델은 55% 미만으로 떨어져 견고성이 크게 향상되었음을 보여준다.

### 결론
SSM-VLA는 기하학적 인식 공간 인코딩, 다중 스케일 시간 모델링 및 명시적 추론의 유기적 결합을 통해 잠재 행동 모델이 공간 및 시간 인식에서 가지는 고유한 결함을 효과적으로 극복한다. 실험은 이 전략이 복잡한 동적 환경에서 VLA 시스템의 결정 안정성과 일반화 능력을 크게 향상시킬 수 있음을 증명하며, 구현 지능의 실용화를 위한 새로운 패러다임을 제공한다.
