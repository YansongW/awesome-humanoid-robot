---
$id: ent_paper_safehumanoid_vlm_rag_driven_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
  zh: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
  ko: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
summary:
  en: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
  zh: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
  ko: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- safehumanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23300v1.
sources:
- id: src_001
  type: paper
  title: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2511.23300
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## 核心内容
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## 参考
- http://arxiv.org/abs/2511.23300v1

## Overview
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## Content
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## 개요
안전하고 신뢰할 수 있는 인간-로봇 상호작용(HRI)을 위해서는 로봇이 작업을 완료할 뿐만 아니라 장면 맥락과 인간과의 근접성에 따라 임피던스와 속도를 조절할 수 있어야 합니다. 본 논문에서는 인간형 로봇의 임피던스 및 속도 파라미터를 스케줄링하기 위해 Vision Language Models(VLM)과 Retrieval-Augmented Generation(RAG)을 연결하는 1인칭 시점 비전 파이프라인인 SafeHumanoid를 제안합니다. 1인칭 시점 프레임은 구조화된 VLM 프롬프트로 처리되고, 임베딩되어 검증된 시나리오 큐레이션 데이터베이스와 매칭된 후, 역기구학을 통해 관절 수준의 임피던스 명령으로 매핑됩니다. 우리는 인간의 존재 유무에 따른 테이블 위 조작 작업(닦기, 물체 전달, 액체 따르기 등)에서 시스템을 평가했습니다. 결과는 파이프라인이 맥락을 인식하는 방식으로 강성, 감쇠 및 속도 프로파일을 조정하여 안전성을 향상시키면서 작업 성공을 유지함을 보여줍니다. 현재 추론 지연 시간(최대 1.4초)이 고도로 동적인 환경에서의 응답성을 제한하지만, SafeHumanoid는 임피던스 제어의 의미론적 기반이 더 안전하고 표준을 준수하는 인간형 협업을 위한 실행 가능한 경로임을 입증합니다.

## 핵심 내용
안전하고 신뢰할 수 있는 인간-로봇 상호작용(HRI)을 위해서는 로봇이 작업을 완료할 뿐만 아니라 장면 맥락과 인간과의 근접성에 따라 임피던스와 속도를 조절할 수 있어야 합니다. 본 논문에서는 인간형 로봇의 임피던스 및 속도 파라미터를 스케줄링하기 위해 Vision Language Models(VLM)과 Retrieval-Augmented Generation(RAG)을 연결하는 1인칭 시점 비전 파이프라인인 SafeHumanoid를 제안합니다. 1인칭 시점 프레임은 구조화된 VLM 프롬프트로 처리되고, 임베딩되어 검증된 시나리오 큐레이션 데이터베이스와 매칭된 후, 역기구학을 통해 관절 수준의 임피던스 명령으로 매핑됩니다. 우리는 인간의 존재 유무에 따른 테이블 위 조작 작업(닦기, 물체 전달, 액체 따르기 등)에서 시스템을 평가했습니다. 결과는 파이프라인이 맥락을 인식하는 방식으로 강성, 감쇠 및 속도 프로파일을 조정하여 안전성을 향상시키면서 작업 성공을 유지함을 보여줍니다. 현재 추론 지연 시간(최대 1.4초)이 고도로 동적인 환경에서의 응답성을 제한하지만, SafeHumanoid는 임피던스 제어의 의미론적 기반이 더 안전하고 표준을 준수하는 인간형 협업을 위한 실행 가능한 경로임을 입증합니다.
