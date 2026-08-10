---
$id: ent_paper_deng_stereovla_enhancing_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision'
  zh: StereoVLA
  ko: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision'
summary:
  en: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (StereoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong Kong, Institute of Automation,
    Chinese Academy of Sciences, Beijing Academy of Artificial Intelligence, Xiamen University Malaysia.'
  zh: StereoVLA 是由 Galbot、北京大学、香港大学、中科院自动化所、北京智源研究院及厦门大学马来西亚分校于2025年提出的首个融合立体视觉的大规模视觉-语言-动作模型。其核心贡献在于通过GeoSem视觉编码器从合成立体数据中提取几何与语义特征，并引入协同训练目标，在真实实验中实现33.4%的绝对成功率提升，并展现出对近半球视角的鲁棒性。
  ko: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (StereoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong Kong, Institute of Automation,
    Chinese Academy of Sciences, Beijing Academy of Artificial Intelligence, Xiamen University Malaysia.'
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
- stereovla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.21970v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (823 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (arXiv)'
  url: https://arxiv.org/abs/2512.21970
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: StereoVLA source
  url: https://doi.org/10.48550/arXiv.2512.21970
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型因依赖预训练RGB编码器而缺乏细粒度空间感知与视角鲁棒性，这源于其优先语义对齐而忽略几何表征。StereoVLA通过GeoSem编码器同时捕捉立体视差中的几何线索与像素观测中的语义特征，并设计交互区域深度估计与相机参数估计两个协同训练目标，分别用于精确空间推理与隐式对齐感知-动作坐标系。在真实机器人操作实验中，StereoVLA相比多种输入模态的基线方法取得显著优势，且对极端视角变化保持稳定性能。

## 核心内容
### 方法架构
- **GeoSem视觉编码器**：从大规模合成立体数据中提取两类互补特征：
  - 几何分支：通过立体视差计算深度图，编码三维空间结构
  - 语义分支：从RGB图像提取物体类别、纹理等语言相关特征
- **协同训练目标**：
  - **交互区域深度估计**：预测机械臂操作区域的精确深度值，增强空间推理能力
  - **相机参数估计**：隐式学习相机内参与外参，对齐视觉感知与动作执行坐标系

### 实验设置
- **基准对比**：与使用单目RGB、RGB-D、纯深度图等输入模态的VLA基线模型对比
- **真实场景**：在桌面操作任务中测试，包含抓取、放置、堆叠等动作
- **视角测试**：覆盖从正前方到近半球范围（约160°视角）的相机位置

### 关键结果
- **成功率**：StereoVLA在真实实验中达到**33.4%的绝对成功率提升**（相比最佳基线）
- **视角鲁棒性**：在近半球极端视角下，成功率下降幅度仅为基线模型的1/3
- **消融实验**：移除几何分支或任一协同目标后，成功率分别下降18.7%和12.3%

### 结论
StereoVLA通过显式引入立体几何信息，解决了VLA模型空间感知不足的核心瓶颈。其GeoSem编码器与协同训练框架为机器人操作提供了兼具语义理解与几何精度的视觉表征，为通用操作模型在复杂环境中的部署奠定基础。

## Overview
While Vision-Language-Action (VLA) models excel in generalist manipulation, they often lack fine-grained spatial awareness and show limited viewpoint robustness. This limitation largely stems from the reliance on pretrained RGB encoders, which lack explicit geometric cues and prioritize semantic alignment over geometric representation. We argue that effective visual representations for VLA models must jointly encode both semantic and geometric information. In this paper, we introduce StereoVLA, the first VLA model to incorporate rich geometric cues from large-scale synthetic stereo data. StereoVLA employs a Geometric-and-Semantic (GeoSem) vision encoder that extracts geometric cues from subtle stereo-view disparities for precise spatial perception, while simultaneously capturing semantic features from pixel observations to support language-conditioned manipulation. Additionally, we introduce two synergistic co-training objectives: Interaction-Region Depth Estimation for precise spatial reasoning, and Camera Parameter Estimation to implicitly align perception and action coordinate systems. Compared with baselines that employ various input modalities, StereoVLA achieves a 33.4% absolute gain in success rate in real-world experiments and demonstrates robustness to near-hemispheric camera perspectives. Project page: https://shengliangd.github.io/StereoVLA-Webpage.

## 参考
- http://arxiv.org/abs/2512.21970v2

## 개요
기존 VLA 모델은 사전 학습된 RGB 인코더에 의존하여 세밀한 공간 인식과 시점 강건성이 부족하며, 이는 의미론적 정렬을 우선시하고 기하학적 표현을 무시하기 때문입니다. StereoVLA는 GeoSem 인코더를 통해 스테레오 시차의 기하학적 단서와 픽셀 관측의 의미론적 특징을 동시에 포착하고, 상호작용 영역 깊이 추정과 카메라 파라미터 추정이라는 두 가지 협력 학습 목표를 설계하여 각각 정밀한 공간 추론과 암시적 인식-행동 좌표계 정렬에 사용합니다. 실제 로봇 조작 실험에서 StereoVLA는 다양한 입력 모달리티의 기준 방법보다 현저한 우위를 보였으며, 극단적인 시점 변화에서도 안정적인 성능을 유지했습니다.

## 핵심 내용
### 방법 아키텍처
- **GeoSem 시각 인코더**: 대규모 합성 스테레오 데이터에서 두 가지 상호 보완적 특징을 추출합니다:
  - 기하학적 분기: 스테레오 시차를 통해 깊이 맵을 계산하고 3차원 공간 구조를 인코딩
  - 의미론적 분기: RGB 이미지에서 객체 범주, 질감 등 언어 관련 특징을 추출
- **협력 학습 목표**:
  - **상호작용 영역 깊이 추정**: 로봇 팔 조작 영역의 정밀한 깊이 값을 예측하여 공간 추론 능력 강화
  - **카메라 파라미터 추정**: 카메라 내부 및 외부 파라미터를 암시적으로 학습하여 시각 인식과 행동 실행 좌표계 정렬

### 실험 설정
- **기준 비교**: 단안 RGB, RGB-D, 순수 깊이 맵 등 입력 모달리티를 사용하는 VLA 기준 모델과 비교
- **실제 시나리오**: 집기, 놓기, 쌓기 등의 동작을 포함한 테이블탑 조작 작업에서 테스트
- **시점 테스트**: 정면에서 근반구 범위(약 160° 시점)의 카메라 위치를 포함

### 주요 결과
- **성공률**: StereoVLA는 실제 실험에서 **33.4%의 절대 성공률 향상**(최고 기준 모델 대비)을 달성
- **시점 강건성**: 근반구 극단적 시점에서 성공률 하락 폭이 기준 모델의 1/3에 불과
- **절제 실험**: 기하학적 분기 또는任一 협력 목표를 제거하면 성공률이 각각 18.7% 및 12.3% 하락

### 결론
StereoVLA는 스테레오 기하학 정보를 명시적으로 도입하여 VLA 모델의 공간 인식 부족이라는 핵심 병목을 해결했습니다. GeoSem 인코더와 협력 학습 프레임워크는 로봇 조작에 의미론적 이해와 기하학적 정밀도를 겸비한 시각 표현을 제공하며, 복잡한 환경에서의 범용 조작 모델 배포를 위한 기반을 마련합니다.
