---
$id: ent_paper_li_robonurse_vla_robotic_scrub_nu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboNurse-VLA: Robotic Scrub Nurse System based on Vision-Language-Action Model'
  zh: RoboNurse-VLA
  ko: 'RoboNurse-VLA: Robotic Scrub Nurse System based on Vision-Language-Action Model'
summary:
  en: 'RoboNurse-VLA: Robotic Scrub Nurse System based on Vision-Language-Action Model (RoboNurse-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Multi-Scale Medical Robotics Centre, Ltd., The Chinese University of Hong
    Kong, Department of Surgery, The Chinese University of Hong Kong, Humanoids and Human-Centered Mechatronics (HHCM), Istituto
    Italiano di Tecnologia, and published at IROS 2024.'
  zh: 'RoboNurse-VLA: Robotic Scrub Nurse System based on Vision-Language-Action Model (RoboNurse-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Multi-Scale Medical Robotics Centre, Ltd., The Chinese University of Hong
    Kong, Department of Surgery, The Chinese University of Hong Kong, Humanoids and Human-Centered Mechatronics (HHCM), Istituto
    Italiano di Tecnologia, and published at IROS 2024.'
  ko: 'RoboNurse-VLA: Robotic Scrub Nurse System based on Vision-Language-Action Model (RoboNurse-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Multi-Scale Medical Robotics Centre, Ltd., The Chinese University of Hong
    Kong, Department of Surgery, The Chinese University of Hong Kong, Humanoids and Human-Centered Mechatronics (HHCM), Istituto
    Italiano di Tecnologia, and published at IROS 2024.'
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
- robonurse_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.19590v1.
sources:
- id: src_001
  type: website
  title: RoboNurse-VLA source
  url: https://doi.org/10.1109/IROS60139.2025.11246030
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In modern healthcare, the demand for autonomous robotic assistants has grown significantly, particularly in the operating room, where surgical tasks require precision and reliability. Robotic scrub nurses have emerged as a promising solution to improve efficiency and reduce human error during surgery. However, challenges remain in terms of accurately grasping and handing over surgical instruments, especially when dealing with complex or difficult objects in dynamic environments. In this work, we introduce a novel robotic scrub nurse system, RoboNurse-VLA, built on a Vision-Language-Action (VLA) model by integrating the Segment Anything Model 2 (SAM 2) and the Llama 2 language model.   The proposed RoboNurse-VLA system enables highly precise grasping and handover of surgical instruments in real-time based on voice commands from the surgeon. Leveraging state-of-the-art vision and language models, the system can address key challenges for object detection, pose optimization, and the handling of complex and difficult-to-grasp instruments. Through extensive evaluations, RoboNurse-VLA demonstrates superior performance compared to existing models, achieving high success rates in surgical instrument handovers, even with unseen tools and challenging items. This work presents a significant step forward in autonomous surgical assistance, showcasing the potential of integrating VLA models for real-world medical applications. More details can be found at https://robonurse-vla.github.io.

## 核心内容
In modern healthcare, the demand for autonomous robotic assistants has grown significantly, particularly in the operating room, where surgical tasks require precision and reliability. Robotic scrub nurses have emerged as a promising solution to improve efficiency and reduce human error during surgery. However, challenges remain in terms of accurately grasping and handing over surgical instruments, especially when dealing with complex or difficult objects in dynamic environments. In this work, we introduce a novel robotic scrub nurse system, RoboNurse-VLA, built on a Vision-Language-Action (VLA) model by integrating the Segment Anything Model 2 (SAM 2) and the Llama 2 language model.   The proposed RoboNurse-VLA system enables highly precise grasping and handover of surgical instruments in real-time based on voice commands from the surgeon. Leveraging state-of-the-art vision and language models, the system can address key challenges for object detection, pose optimization, and the handling of complex and difficult-to-grasp instruments. Through extensive evaluations, RoboNurse-VLA demonstrates superior performance compared to existing models, achieving high success rates in surgical instrument handovers, even with unseen tools and challenging items. This work presents a significant step forward in autonomous surgical assistance, showcasing the potential of integrating VLA models for real-world medical applications. More details can be found at https://robonurse-vla.github.io.

## 参考
- http://arxiv.org/abs/2409.19590v1

## Overview
In modern healthcare, the demand for autonomous robotic assistants has grown significantly, particularly in the operating room, where surgical tasks require precision and reliability. Robotic scrub nurses have emerged as a promising solution to improve efficiency and reduce human error during surgery. However, challenges remain in terms of accurately grasping and handing over surgical instruments, especially when dealing with complex or difficult objects in dynamic environments. In this work, we introduce a novel robotic scrub nurse system, RoboNurse-VLA, built on a Vision-Language-Action (VLA) model by integrating the Segment Anything Model 2 (SAM 2) and the Llama 2 language model. The proposed RoboNurse-VLA system enables highly precise grasping and handover of surgical instruments in real-time based on voice commands from the surgeon. Leveraging state-of-the-art vision and language models, the system can address key challenges for object detection, pose optimization, and the handling of complex and difficult-to-grasp instruments. Through extensive evaluations, RoboNurse-VLA demonstrates superior performance compared to existing models, achieving high success rates in surgical instrument handovers, even with unseen tools and challenging items. This work presents a significant step forward in autonomous surgical assistance, showcasing the potential of integrating VLA models for real-world medical applications. More details can be found at https://robonurse-vla.github.io.

## Content
In modern healthcare, the demand for autonomous robotic assistants has grown significantly, particularly in the operating room, where surgical tasks require precision and reliability. Robotic scrub nurses have emerged as a promising solution to improve efficiency and reduce human error during surgery. However, challenges remain in terms of accurately grasping and handing over surgical instruments, especially when dealing with complex or difficult objects in dynamic environments. In this work, we introduce a novel robotic scrub nurse system, RoboNurse-VLA, built on a Vision-Language-Action (VLA) model by integrating the Segment Anything Model 2 (SAM 2) and the Llama 2 language model. The proposed RoboNurse-VLA system enables highly precise grasping and handover of surgical instruments in real-time based on voice commands from the surgeon. Leveraging state-of-the-art vision and language models, the system can address key challenges for object detection, pose optimization, and the handling of complex and difficult-to-grasp instruments. Through extensive evaluations, RoboNurse-VLA demonstrates superior performance compared to existing models, achieving high success rates in surgical instrument handovers, even with unseen tools and challenging items. This work presents a significant step forward in autonomous surgical assistance, showcasing the potential of integrating VLA models for real-world medical applications. More details can be found at https://robonurse-vla.github.io.

## 개요
현대 의료 환경에서 자율 로봇 보조 시스템에 대한 수요가 크게 증가하고 있으며, 특히 수술실에서는 정밀성과 신뢰성이 요구되는 수술 작업이 이루어집니다. 로봇 수술 간호사는 수술 중 효율성을 높이고 인간의 오류를 줄이기 위한 유망한 해결책으로 부상하고 있습니다. 그러나 동적 환경에서 복잡하거나 까다로운 물체를 다룰 때, 특히 수술 도구를 정확하게 잡고 전달하는 데 있어 여전히 과제가 남아 있습니다. 본 연구에서는 Segment Anything Model 2 (SAM 2)와 Llama 2 언어 모델을 통합한 Vision-Language-Action (VLA) 모델을 기반으로 구축된 새로운 로봇 수술 간호사 시스템인 RoboNurse-VLA를 소개합니다. 제안된 RoboNurse-VLA 시스템은 외과의사의 음성 명령에 따라 실시간으로 수술 도구를 매우 정밀하게 잡고 전달할 수 있습니다. 최첨단 비전 및 언어 모델을 활용하여 이 시스템은 객체 감지, 자세 최적화, 복잡하고 잡기 어려운 도구 처리와 같은 주요 과제를 해결할 수 있습니다. 광범위한 평가를 통해 RoboNurse-VLA는 기존 모델보다 우수한 성능을 보여주며, 보지 못한 도구와 까다로운 물건에서도 높은 성공률로 수술 도구 전달을 달성합니다. 이 연구는 자율 수술 보조 분야에서 중요한 진전을 나타내며, 실제 의료 응용 분야에 VLA 모델을 통합할 가능성을 보여줍니다. 자세한 내용은 https://robonurse-vla.github.io에서 확인할 수 있습니다.

## 핵심 내용
현대 의료 환경에서 자율 로봇 보조 시스템에 대한 수요가 크게 증가하고 있으며, 특히 수술실에서는 정밀성과 신뢰성이 요구되는 수술 작업이 이루어집니다. 로봇 수술 간호사는 수술 중 효율성을 높이고 인간의 오류를 줄이기 위한 유망한 해결책으로 부상하고 있습니다. 그러나 동적 환경에서 복잡하거나 까다로운 물체를 다룰 때, 특히 수술 도구를 정확하게 잡고 전달하는 데 있어 여전히 과제가 남아 있습니다. 본 연구에서는 Segment Anything Model 2 (SAM 2)와 Llama 2 언어 모델을 통합한 Vision-Language-Action (VLA) 모델을 기반으로 구축된 새로운 로봇 수술 간호사 시스템인 RoboNurse-VLA를 소개합니다. 제안된 RoboNurse-VLA 시스템은 외과의사의 음성 명령에 따라 실시간으로 수술 도구를 매우 정밀하게 잡고 전달할 수 있습니다. 최첨단 비전 및 언어 모델을 활용하여 이 시스템은 객체 감지, 자세 최적화, 복잡하고 잡기 어려운 도구 처리와 같은 주요 과제를 해결할 수 있습니다. 광범위한 평가를 통해 RoboNurse-VLA는 기존 모델보다 우수한 성능을 보여주며, 보지 못한 도구와 까다로운 물건에서도 높은 성공률로 수술 도구 전달을 달성합니다. 이 연구는 자율 수술 보조 분야에서 중요한 진전을 나타내며, 실제 의료 응용 분야에 VLA 모델을 통합할 가능성을 보여줍니다. 자세한 내용은 https://robonurse-vla.github.io에서 확인할 수 있습니다.
