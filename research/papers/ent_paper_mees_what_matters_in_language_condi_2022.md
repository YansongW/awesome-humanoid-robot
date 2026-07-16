---
$id: ent_paper_mees_what_matters_in_language_condi_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data
  zh: HULC
  ko: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data
summary:
  en: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data (HULC), is a 2022 generalized
    vision-language-action model for robotic manipulation, introduced by University of Freiburg, University of Technology
    Nuremberg, and published at IEEE Robotics Autom. Lett. 2022.
  zh: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data (HULC), is a 2022 generalized
    vision-language-action model for robotic manipulation, introduced by University of Freiburg, University of Technology
    Nuremberg, and published at IEEE Robotics Autom. Lett. 2022.
  ko: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data (HULC), is a 2022 generalized
    vision-language-action model for robotic manipulation, introduced by University of Freiburg, University of Technology
    Nuremberg, and published at IEEE Robotics Autom. Lett. 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- hulc
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.06252v2.
sources:
- id: src_001
  type: website
  title: HULC source
  url: https://doi.org/10.1109/LRA.2022.3196123
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
A long-standing goal in robotics is to build robots that can perform a wide range of daily tasks from perceptions obtained with their onboard sensors and specified only via natural language. While recently substantial advances have been achieved in language-driven robotics by leveraging end-to-end learning from pixels, there is no clear and well-understood process for making various design choices due to the underlying variation in setups. In this paper, we conduct an extensive study of the most critical challenges in learning language conditioned policies from offline free-form imitation datasets. We further identify architectural and algorithmic techniques that improve performance, such as a hierarchical decomposition of the robot control learning, a multimodal transformer encoder, discrete latent plans and a self-supervised contrastive loss that aligns video and language representations. By combining the results of our investigation with our improved model components, we are able to present a novel approach that significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation CALVIN benchmark. We have open-sourced our implementation to facilitate future research in learning to perform many complex manipulation skills in a row specified with natural language. Codebase and trained models available at http://hulc.cs.uni-freiburg.de

## 核心内容
A long-standing goal in robotics is to build robots that can perform a wide range of daily tasks from perceptions obtained with their onboard sensors and specified only via natural language. While recently substantial advances have been achieved in language-driven robotics by leveraging end-to-end learning from pixels, there is no clear and well-understood process for making various design choices due to the underlying variation in setups. In this paper, we conduct an extensive study of the most critical challenges in learning language conditioned policies from offline free-form imitation datasets. We further identify architectural and algorithmic techniques that improve performance, such as a hierarchical decomposition of the robot control learning, a multimodal transformer encoder, discrete latent plans and a self-supervised contrastive loss that aligns video and language representations. By combining the results of our investigation with our improved model components, we are able to present a novel approach that significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation CALVIN benchmark. We have open-sourced our implementation to facilitate future research in learning to perform many complex manipulation skills in a row specified with natural language. Codebase and trained models available at http://hulc.cs.uni-freiburg.de

## 参考
- http://arxiv.org/abs/2204.06252v2

## Overview
A long-standing goal in robotics is to build robots that can perform a wide range of daily tasks from perceptions obtained with their onboard sensors and specified only via natural language. While recently substantial advances have been achieved in language-driven robotics by leveraging end-to-end learning from pixels, there is no clear and well-understood process for making various design choices due to the underlying variation in setups. In this paper, we conduct an extensive study of the most critical challenges in learning language conditioned policies from offline free-form imitation datasets. We further identify architectural and algorithmic techniques that improve performance, such as a hierarchical decomposition of the robot control learning, a multimodal transformer encoder, discrete latent plans and a self-supervised contrastive loss that aligns video and language representations. By combining the results of our investigation with our improved model components, we are able to present a novel approach that significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation CALVIN benchmark. We have open-sourced our implementation to facilitate future research in learning to perform many complex manipulation skills in a row specified with natural language. Codebase and trained models available at http://hulc.cs.uni-freiburg.de

## Content
A long-standing goal in robotics is to build robots that can perform a wide range of daily tasks from perceptions obtained with their onboard sensors and specified only via natural language. While recently substantial advances have been achieved in language-driven robotics by leveraging end-to-end learning from pixels, there is no clear and well-understood process for making various design choices due to the underlying variation in setups. In this paper, we conduct an extensive study of the most critical challenges in learning language conditioned policies from offline free-form imitation datasets. We further identify architectural and algorithmic techniques that improve performance, such as a hierarchical decomposition of the robot control learning, a multimodal transformer encoder, discrete latent plans and a self-supervised contrastive loss that aligns video and language representations. By combining the results of our investigation with our improved model components, we are able to present a novel approach that significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation CALVIN benchmark. We have open-sourced our implementation to facilitate future research in learning to perform many complex manipulation skills in a row specified with natural language. Codebase and trained models available at http://hulc.cs.uni-freiburg.de

## 개요
로봇 공학의 오랜 목표 중 하나는 자체 탑재 센서로 얻은 인식과 자연어로만 지정된 광범위한 일상 작업을 수행할 수 있는 로봇을 구축하는 것입니다. 최근 픽셀에서 엔드투엔드 학습을 활용하여 언어 기반 로봇 공학에서 상당한 진전이 이루어졌지만, 설정의 근본적인 차이로 인해 다양한 설계 선택을 위한 명확하고 잘 이해된 프로세스는 없습니다. 본 논문에서는 오프라인 자유 형식 모방 데이터셋에서 언어 조건화 정책을 학습하는 데 있어 가장 중요한 과제에 대한 광범위한 연구를 수행합니다. 또한 로봇 제어 학습의 계층적 분해, 다중 모달 트랜스포머 인코더, 이산 잠재 계획, 비디오와 언어 표현을 정렬하는 자기 지도 대조 손실과 같은 성능을 향상시키는 아키텍처 및 알고리즘 기법을 식별합니다. 우리의 조사 결과와 개선된 모델 구성 요소를 결합하여 도전적인 언어 조건화 장기 로봇 조작 CALVIN 벤치마크에서 최첨단 성능을 크게 능가하는 새로운 접근 방식을 제시할 수 있습니다. 자연어로 지정된 여러 복잡한 조작 기술을 연속적으로 학습하는 미래 연구를 촉진하기 위해 구현을 오픈소스로 공개했습니다. 코드베이스와 훈련된 모델은 http://hulc.cs.uni-freiburg.de에서 확인할 수 있습니다.

## 핵심 내용
로봇 공학의 오랜 목표 중 하나는 자체 탑재 센서로 얻은 인식과 자연어로만 지정된 광범위한 일상 작업을 수행할 수 있는 로봇을 구축하는 것입니다. 최근 픽셀에서 엔드투엔드 학습을 활용하여 언어 기반 로봇 공학에서 상당한 진전이 이루어졌지만, 설정의 근본적인 차이로 인해 다양한 설계 선택을 위한 명확하고 잘 이해된 프로세스는 없습니다. 본 논문에서는 오프라인 자유 형식 모방 데이터셋에서 언어 조건화 정책을 학습하는 데 있어 가장 중요한 과제에 대한 광범위한 연구를 수행합니다. 또한 로봇 제어 학습의 계층적 분해, 다중 모달 트랜스포머 인코더, 이산 잠재 계획, 비디오와 언어 표현을 정렬하는 자기 지도 대조 손실과 같은 성능을 향상시키는 아키텍처 및 알고리즘 기법을 식별합니다. 우리의 조사 결과와 개선된 모델 구성 요소를 결합하여 도전적인 언어 조건화 장기 로봇 조작 CALVIN 벤치마크에서 최첨단 성능을 크게 능가하는 새로운 접근 방식을 제시할 수 있습니다. 자연어로 지정된 여러 복잡한 조작 기술을 연속적으로 학습하는 미래 연구를 촉진하기 위해 구현을 오픈소스로 공개했습니다. 코드베이스와 훈련된 모델은 http://hulc.cs.uni-freiburg.de에서 확인할 수 있습니다.
