---
$id: ent_paper_frame_floor_aligned_representa_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video'
  zh: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video'
  ko: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video'
summary:
  en: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  zh: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  ko: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- frame
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.23094v1.
sources:
- id: src_001
  type: paper
  title: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2503.23094
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video project page'
  url: https://vcai.mpi-inf.mpg.de/projects/FRAME/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric motion capture with a head-mounted body-facing stereo camera is crucial for VR and AR applications but presents significant challenges such as heavy occlusions and limited annotated real-world data. Existing methods rely on synthetic pretraining and struggle to generate smooth and accurate predictions in real-world settings, particularly for lower limbs. Our work addresses these limitations by introducing a lightweight VR-based data collection setup with on-board, real-time 6D pose tracking. Using this setup, we collected the most extensive real-world dataset for ego-facing ego-mounted cameras to date in size and motion variability. Effectively integrating this multimodal input -- device pose and camera feeds -- is challenging due to the differing characteristics of each data source. To address this, we propose FRAME, a simple yet effective architecture that combines device pose and camera feeds for state-of-the-art body pose prediction through geometrically sound multimodal integration and can run at 300 FPS on modern hardware. Lastly, we showcase a novel training strategy to enhance the model's generalization capabilities. Our approach exploits the problem's geometric properties, yielding high-quality motion capture free from common artifacts in prior works. Qualitative and quantitative evaluations, along with extensive comparisons, demonstrate the effectiveness of our method. Data, code, and CAD designs will be available at https://vcai.mpi-inf.mpg.de/projects/FRAME/

## 核心内容
Egocentric motion capture with a head-mounted body-facing stereo camera is crucial for VR and AR applications but presents significant challenges such as heavy occlusions and limited annotated real-world data. Existing methods rely on synthetic pretraining and struggle to generate smooth and accurate predictions in real-world settings, particularly for lower limbs. Our work addresses these limitations by introducing a lightweight VR-based data collection setup with on-board, real-time 6D pose tracking. Using this setup, we collected the most extensive real-world dataset for ego-facing ego-mounted cameras to date in size and motion variability. Effectively integrating this multimodal input -- device pose and camera feeds -- is challenging due to the differing characteristics of each data source. To address this, we propose FRAME, a simple yet effective architecture that combines device pose and camera feeds for state-of-the-art body pose prediction through geometrically sound multimodal integration and can run at 300 FPS on modern hardware. Lastly, we showcase a novel training strategy to enhance the model's generalization capabilities. Our approach exploits the problem's geometric properties, yielding high-quality motion capture free from common artifacts in prior works. Qualitative and quantitative evaluations, along with extensive comparisons, demonstrate the effectiveness of our method. Data, code, and CAD designs will be available at https://vcai.mpi-inf.mpg.de/projects/FRAME/

## 参考
- http://arxiv.org/abs/2503.23094v1

## Overview
Egocentric motion capture with a head-mounted body-facing stereo camera is crucial for VR and AR applications but presents significant challenges such as heavy occlusions and limited annotated real-world data. Existing methods rely on synthetic pretraining and struggle to generate smooth and accurate predictions in real-world settings, particularly for lower limbs. Our work addresses these limitations by introducing a lightweight VR-based data collection setup with on-board, real-time 6D pose tracking. Using this setup, we collected the most extensive real-world dataset for ego-facing ego-mounted cameras to date in size and motion variability. Effectively integrating this multimodal input -- device pose and camera feeds -- is challenging due to the differing characteristics of each data source. To address this, we propose FRAME, a simple yet effective architecture that combines device pose and camera feeds for state-of-the-art body pose prediction through geometrically sound multimodal integration and can run at 300 FPS on modern hardware. Lastly, we showcase a novel training strategy to enhance the model's generalization capabilities. Our approach exploits the problem's geometric properties, yielding high-quality motion capture free from common artifacts in prior works. Qualitative and quantitative evaluations, along with extensive comparisons, demonstrate the effectiveness of our method. Data, code, and CAD designs will be available at https://vcai.mpi-inf.mpg.de/projects/FRAME/

## Content
Egocentric motion capture with a head-mounted body-facing stereo camera is crucial for VR and AR applications but presents significant challenges such as heavy occlusions and limited annotated real-world data. Existing methods rely on synthetic pretraining and struggle to generate smooth and accurate predictions in real-world settings, particularly for lower limbs. Our work addresses these limitations by introducing a lightweight VR-based data collection setup with on-board, real-time 6D pose tracking. Using this setup, we collected the most extensive real-world dataset for ego-facing ego-mounted cameras to date in size and motion variability. Effectively integrating this multimodal input -- device pose and camera feeds -- is challenging due to the differing characteristics of each data source. To address this, we propose FRAME, a simple yet effective architecture that combines device pose and camera feeds for state-of-the-art body pose prediction through geometrically sound multimodal integration and can run at 300 FPS on modern hardware. Lastly, we showcase a novel training strategy to enhance the model's generalization capabilities. Our approach exploits the problem's geometric properties, yielding high-quality motion capture free from common artifacts in prior works. Qualitative and quantitative evaluations, along with extensive comparisons, demonstrate the effectiveness of our method. Data, code, and CAD designs will be available at https://vcai.mpi-inf.mpg.de/projects/FRAME/

## 개요
헤드 마운트 바디 페이싱 스테레오 카메라를 사용한 자기 중심 모션 캡처는 VR 및 AR 애플리케이션에 필수적이지만, 심각한 폐색 및 제한된 주석 처리된 실제 데이터와 같은 상당한 과제를 제시합니다. 기존 방법은 합성 사전 학습에 의존하며, 특히 하체에서 실제 환경에서 부드럽고 정확한 예측을 생성하는 데 어려움을 겪습니다. 우리의 연구는 온보드 실시간 6D 포즈 추적 기능을 갖춘 경량 VR 기반 데이터 수집 설정을 도입하여 이러한 한계를 해결합니다. 이 설정을 사용하여, 우리는 지금까지 자기 대면 자기 장착 카메라를 위한 가장 광범위한 실제 데이터 세트를 크기와 동작 변동성 측면에서 수집했습니다. 이 다중 모달 입력(장치 포즈 및 카메라 피드)을 효과적으로 통합하는 것은 각 데이터 소스의 서로 다른 특성으로 인해 어렵습니다. 이를 해결하기 위해, 우리는 FRAME을 제안합니다. 이는 장치 포즈와 카메라 피드를 결합하여 기하학적으로 건전한 다중 모달 통합을 통해 최첨단 신체 포즈 예측을 제공하고 최신 하드웨어에서 300FPS로 실행할 수 있는 간단하면서도 효과적인 아키텍처입니다. 마지막으로, 우리는 모델의 일반화 능력을 향상시키기 위한 새로운 훈련 전략을 선보입니다. 우리의 접근 방식은 문제의 기하학적 특성을 활용하여 이전 연구의 일반적인 아티팩트가 없는 고품질 모션 캡처를 생성합니다. 정성적 및 정량적 평가와 광범위한 비교를 통해 우리 방법의 효과를 입증합니다. 데이터, 코드 및 CAD 설계는 https://vcai.mpi-inf.mpg.de/projects/FRAME/에서 제공될 예정입니다.

## 핵심 내용
헤드 마운트 바디 페이싱 스테레오 카메라를 사용한 자기 중심 모션 캡처는 VR 및 AR 애플리케이션에 필수적이지만, 심각한 폐색 및 제한된 주석 처리된 실제 데이터와 같은 상당한 과제를 제시합니다. 기존 방법은 합성 사전 학습에 의존하며, 특히 하체에서 실제 환경에서 부드럽고 정확한 예측을 생성하는 데 어려움을 겪습니다. 우리의 연구는 온보드 실시간 6D 포즈 추적 기능을 갖춘 경량 VR 기반 데이터 수집 설정을 도입하여 이러한 한계를 해결합니다. 이 설정을 사용하여, 우리는 지금까지 자기 대면 자기 장착 카메라를 위한 가장 광범위한 실제 데이터 세트를 크기와 동작 변동성 측면에서 수집했습니다. 이 다중 모달 입력(장치 포즈 및 카메라 피드)을 효과적으로 통합하는 것은 각 데이터 소스의 서로 다른 특성으로 인해 어렵습니다. 이를 해결하기 위해, 우리는 FRAME을 제안합니다. 이는 장치 포즈와 카메라 피드를 결합하여 기하학적으로 건전한 다중 모달 통합을 통해 최첨단 신체 포즈 예측을 제공하고 최신 하드웨어에서 300FPS로 실행할 수 있는 간단하면서도 효과적인 아키텍처입니다. 마지막으로, 우리는 모델의 일반화 능력을 향상시키기 위한 새로운 훈련 전략을 선보입니다. 우리의 접근 방식은 문제의 기하학적 특성을 활용하여 이전 연구의 일반적인 아티팩트가 없는 고품질 모션 캡처를 생성합니다. 정성적 및 정량적 평가와 광범위한 비교를 통해 우리 방법의 효과를 입증합니다. 데이터, 코드 및 CAD 설계는 https://vcai.mpi-inf.mpg.de/projects/FRAME/에서 제공될 예정입니다.
