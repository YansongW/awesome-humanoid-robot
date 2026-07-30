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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.21970v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-Language-Action (VLA) 모델은 범용 조작 작업에서 뛰어난 성능을 보이지만, 종종 세밀한 공간 인식 능력이 부족하고 시점 변화에 대한 강건성이 제한적입니다. 이러한 한계는 주로 사전 학습된 RGB 인코더에 의존하기 때문이며, 이 인코더는 명시적인 기하학적 단서가 부족하고 의미적 정렬을 기하학적 표현보다 우선시합니다. 우리는 VLA 모델을 위한 효과적인 시각적 표현이 의미 정보와 기하학적 정보를 모두 공동으로 인코딩해야 한다고 주장합니다. 본 논문에서는 대규모 합성 스테레오 데이터에서 풍부한 기하학적 단서를 통합한 최초의 VLA 모델인 StereoVLA를 소개합니다. StereoVLA는 미세한 스테레오 시점 차이에서 기하학적 단서를 추출하여 정밀한 공간 인식을 가능하게 하는 동시에, 픽셀 관측에서 의미적 특징을 포착하여 언어 조건 조작을 지원하는 Geometric-and-Semantic (GeoSem) 비전 인코더를 사용합니다. 또한, 정밀한 공간 추론을 위한 상호작용 영역 깊이 추정(Interaction-Region Depth Estimation)과 인식 및 행동 좌표계를 암시적으로 정렬하는 카메라 파라미터 추정(Camera Parameter Estimation)이라는 두 가지 시너지 효과를 내는 공동 학습 목표를 도입합니다. 다양한 입력 모달리티를 사용하는 기준 모델과 비교하여, StereoVLA는 실제 실험에서 성공률이 33.4% 절대적으로 향상되었으며, 거의 반구에 가까운 카메라 시점에서도 강건성을 보여줍니다. 프로젝트 페이지: https://shengliangd.github.io/StereoVLA-Webpage.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 범용 조작 작업에서 뛰어난 성능을 보이지만, 종종 세밀한 공간 인식 능력이 부족하고 시점 변화에 대한 강건성이 제한적입니다. 이러한 한계는 주로 사전 학습된 RGB 인코더에 의존하기 때문이며, 이 인코더는 명시적인 기하학적 단서가 부족하고 의미적 정렬을 기하학적 표현보다 우선시합니다. 우리는 VLA 모델을 위한 효과적인 시각적 표현이 의미 정보와 기하학적 정보를 모두 공동으로 인코딩해야 한다고 주장합니다. 본 논문에서는 대규모 합성 스테레오 데이터에서 풍부한 기하학적 단서를 통합한 최초의 VLA 모델인 StereoVLA를 소개합니다. StereoVLA는 미세한 스테레오 시점 차이에서 기하학적 단서를 추출하여 정밀한 공간 인식을 가능하게 하는 동시에, 픽셀 관측에서 의미적 특징을 포착하여 언어 조건 조작을 지원하는 Geometric-and-Semantic (GeoSem) 비전 인코더를 사용합니다. 또한, 정밀한 공간 추론을 위한 상호작용 영역 깊이 추정(Interaction-Region Depth Estimation)과 인식 및 행동 좌표계를 암시적으로 정렬하는 카메라 파라미터 추정(Camera Parameter Estimation)이라는 두 가지 시너지 효과를 내는 공동 학습 목표를 도입합니다. 다양한 입력 모달리티를 사용하는 기준 모델과 비교하여, StereoVLA는 실제 실험에서 성공률이 33.4% 절대적으로 향상되었으며, 거의 반구에 가까운 카메라 시점에서도 강건성을 보여줍니다. 프로젝트 페이지: https://shengliangd.github.io/StereoVLA-Webpage.

## 参考
- http://arxiv.org/abs/2512.21970v2
