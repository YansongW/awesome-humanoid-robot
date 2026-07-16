---
$id: ent_paper_humanoidvlm_vision_language_gu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
  zh: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
  ko: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
summary:
  en: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  zh: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  ko: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
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
- humanoidvlm
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.14874v1.
sources:
- id: src_001
  type: paper
  title: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation (arXiv)'
  url: https://arxiv.org/abs/2601.14874
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## 核心内容
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## 参考
- http://arxiv.org/abs/2601.14874v1

## Overview
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## Content
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## 개요
휴머노이드 로봇은 다양한 물체와 작업에 맞춰 접촉 행동을 적응시켜야 하지만, 대부분의 제어기는 고정되고 수동으로 조정된 임피던스 게인과 그리퍼 설정에 의존합니다. 본 논문에서는 Unitree G1 휴머노이드가 1인칭 RGB 이미지에서 직접 작업에 적합한 직교 임피던스 매개변수와 그리퍼 구성을 선택할 수 있도록 하는 비전-언어 기반 검색 프레임워크인 HumanoidVLM을 소개합니다. 이 시스템은 의미론적 작업 추론을 위한 비전-언어 모델과 FAISS 기반의 검색 증강 생성(RAG) 모듈을 결합하여, 두 개의 맞춤형 데이터베이스에서 실험적으로 검증된 강성-감쇠 쌍과 물체별 파지 각도를 검색하고, 이를 작업 공간 임피던스 제어기를 통해 순응적 조작을 실행합니다. 우리는 HumanoidVLM을 14가지 시각적 시나리오에서 평가하여 93%의 검색 정확도를 달성했습니다. 실제 실험에서는 안정적인 상호작용 동역학을 보여주었으며, z축 추적 오차는 일반적으로 1-3.5cm 이내이고 가상 힘은 작업 의존적 임피던스 설정과 일관되었습니다. 이러한 결과는 의미론적 인식과 검색 기반 제어를 연결하는 것이 적응형 휴머노이드 조작을 위한 해석 가능한 경로로서 실현 가능함을 입증합니다.

## 핵심 내용
휴머노이드 로봇은 다양한 물체와 작업에 맞춰 접촉 행동을 적응시켜야 하지만, 대부분의 제어기는 고정되고 수동으로 조정된 임피던스 게인과 그리퍼 설정에 의존합니다. 본 논문에서는 Unitree G1 휴머노이드가 1인칭 RGB 이미지에서 직접 작업에 적합한 직교 임피던스 매개변수와 그리퍼 구성을 선택할 수 있도록 하는 비전-언어 기반 검색 프레임워크인 HumanoidVLM을 소개합니다. 이 시스템은 의미론적 작업 추론을 위한 비전-언어 모델과 FAISS 기반의 검색 증강 생성(RAG) 모듈을 결합하여, 두 개의 맞춤형 데이터베이스에서 실험적으로 검증된 강성-감쇠 쌍과 물체별 파지 각도를 검색하고, 이를 작업 공간 임피던스 제어기를 통해 순응적 조작을 실행합니다. 우리는 HumanoidVLM을 14가지 시각적 시나리오에서 평가하여 93%의 검색 정확도를 달성했습니다. 실제 실험에서는 안정적인 상호작용 동역학을 보여주었으며, z축 추적 오차는 일반적으로 1-3.5cm 이내이고 가상 힘은 작업 의존적 임피던스 설정과 일관되었습니다. 이러한 결과는 의미론적 인식과 검색 기반 제어를 연결하는 것이 적응형 휴머노이드 조작을 위한 해석 가능한 경로로서 실현 가능함을 입증합니다.
