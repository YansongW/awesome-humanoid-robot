---
$id: ent_paper_embodmocap_in_the_wild_4d_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents'
  zh: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents'
  ko: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents'
summary:
  en: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents is a 2026 work on human motion analysis and
    synthesis for humanoid robots.'
  zh: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents is a 2026 work on human motion analysis and
    synthesis for humanoid robots.'
  ko: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents is a 2026 work on human motion analysis and
    synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodmocap
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23205v2.
sources:
- id: src_001
  type: paper
  title: 'EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents (arXiv)'
  url: https://arxiv.org/abs/2602.23205
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iphone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## 核心内容
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iphone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## 参考
- http://arxiv.org/abs/2602.23205v2

## Overview
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iPhone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## Content
Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting. However, existing capture systems typically rely on costly studio setups and wearable devices, limiting the large-scale collection of scene-conditioned human motion data in the wild. To address this, we propose EmbodMocap, a portable and affordable data collection pipeline using two moving iPhones. Our key idea is to jointly calibrate dual RGB-D sequences to reconstruct both humans and scenes within a unified metric world coordinate frame. The proposed method allows metric-scale and scene-consistent capture in everyday environments without static cameras or markers, bridging human motion and scene geometry seamlessly. Compared with optical capture ground truth, we demonstrate that the dual-view setting exhibits a remarkable ability to mitigate depth ambiguity, achieving superior alignment and reconstruction performance over single iPhone or monocular models. Based on the collected data, we empower three embodied AI tasks: monocular human-scene-reconstruction, where we fine-tune on feedforward models that output metric-scale, world-space aligned humans and scenes; physics-based character animation, where we prove our data could be used to scale human-object interaction skills and scene-aware motion tracking; and robot motion control, where we train a humanoid robot via sim-to-real RL to replicate human motions depicted in videos. Experimental results validate the effectiveness of our pipeline and its contributions towards advancing embodied AI research.

## 개요
실제 세계에서의 인간 행동은 자연스럽게 풍부하고 장기적인 맥락 정보를 인코딩하며, 이는 지능형 에이전트의 인식, 이해 및 행동 훈련에 활용될 수 있습니다. 그러나 기존의 캡처 시스템은 일반적으로 고가의 스튜디오 장비와 웨어러블 기기에 의존하여, 실제 환경에서 장면 조건이 부여된 인간 동작 데이터의 대규모 수집을 제한합니다. 이를 해결하기 위해, 우리는 두 대의 이동형 아이폰을 사용하는 휴대 가능하고 저렴한 데이터 수집 파이프라인인 EmbodMocap을 제안합니다. 핵심 아이디어는 이중 RGB-D 시퀀스를 공동으로 보정하여 통합된 미터법 세계 좌표 프레임 내에서 인간과 장면을 모두 재구성하는 것입니다. 제안된 방법은 정적 카메라나 마커 없이 일상 환경에서 미터법 스케일과 장면 일관된 캡처를 가능하게 하여, 인간 동작과 장면 기하학을 원활하게 연결합니다. 광학 캡처 기준 진실과 비교하여, 이중 시점 설정이 깊이 모호성을 완화하는 놀라운 능력을 보여주며, 단일 아이폰이나 단안 모델보다 우수한 정렬 및 재구성 성능을 달성함을 입증합니다. 수집된 데이터를 기반으로, 우리는 세 가지 지능형 AI 작업을 지원합니다: 미터법 스케일과 세계 공간 정렬된 인간 및 장면을 출력하는 피드포워드 모델을 미세 조정하는 단안 인간-장면 재구성, 데이터를 사용하여 인간-객체 상호작용 기술과 장면 인식 동작 추적을 확장할 수 있음을 증명하는 물리 기반 캐릭터 애니메이션, 그리고 시뮬레이션-실제 강화 학습을 통해 휴머노이드 로봇을 훈련하여 비디오에 묘사된 인간 동작을 복제하는 로봇 동작 제어입니다. 실험 결과는 우리 파이프라인의 효과성과 지능형 AI 연구 발전에 대한 기여를 검증합니다.

## 핵심 내용
실제 세계에서의 인간 행동은 자연스럽게 풍부하고 장기적인 맥락 정보를 인코딩하며, 이는 지능형 에이전트의 인식, 이해 및 행동 훈련에 활용될 수 있습니다. 그러나 기존의 캡처 시스템은 일반적으로 고가의 스튜디오 장비와 웨어러블 기기에 의존하여, 실제 환경에서 장면 조건이 부여된 인간 동작 데이터의 대규모 수집을 제한합니다. 이를 해결하기 위해, 우리는 두 대의 이동형 아이폰을 사용하는 휴대 가능하고 저렴한 데이터 수집 파이프라인인 EmbodMocap을 제안합니다. 핵심 아이디어는 이중 RGB-D 시퀀스를 공동으로 보정하여 통합된 미터법 세계 좌표 프레임 내에서 인간과 장면을 모두 재구성하는 것입니다. 제안된 방법은 정적 카메라나 마커 없이 일상 환경에서 미터법 스케일과 장면 일관된 캡처를 가능하게 하여, 인간 동작과 장면 기하학을 원활하게 연결합니다. 광학 캡처 기준 진실과 비교하여, 이중 시점 설정이 깊이 모호성을 완화하는 놀라운 능력을 보여주며, 단일 아이폰이나 단안 모델보다 우수한 정렬 및 재구성 성능을 달성함을 입증합니다. 수집된 데이터를 기반으로, 우리는 세 가지 지능형 AI 작업을 지원합니다: 미터법 스케일과 세계 공간 정렬된 인간 및 장면을 출력하는 피드포워드 모델을 미세 조정하는 단안 인간-장면 재구성, 데이터를 사용하여 인간-객체 상호작용 기술과 장면 인식 동작 추적을 확장할 수 있음을 증명하는 물리 기반 캐릭터 애니메이션, 그리고 시뮬레이션-실제 강화 학습을 통해 휴머노이드 로봇을 훈련하여 비디오에 묘사된 인간 동작을 복제하는 로봇 동작 제어입니다. 실험 결과는 우리 파이프라인의 효과성과 지능형 AI 연구 발전에 대한 기여를 검증합니다.
