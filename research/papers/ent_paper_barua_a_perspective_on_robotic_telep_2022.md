---
$id: ent_paper_barua_a_perspective_on_robotic_telep_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A Perspective on Robotic Telepresence and Teleoperation using Cognition: Are
    we there yet?'
  zh: 基于认知的机器人远程临场与遥操作视角：我们准备好了吗？
  ko: '인지를 활용한 로봇 원격현존 및 원격조작에 대한 관점: 우리는 아직 도달했는가?'
summary:
  en: This 2022 arXiv perspective surveys robotic telepresence and teleoperation systems,
    arguing for a hybrid cloud-edge architecture to balance heavy computation with
    real-time response, and examines cognition, social awareness, multimodal interaction,
    and the ANA Avatar XPRIZE semi-finalist humanoid nurse robot Asha.
  zh: 这篇2022年arXiv观点/综述文章调查了机器人远程临场与遥操作系统，主张采用混合云-边缘架构以平衡重计算与实时响应，并研究了认知、社交意识、多模态交互以及ANA
    Avatar XPRIZE半决赛人形护士机器人Asha。
  ko: 이 2022년 arXiv 관점/설문조사 논문은 로봇 원격현존 및 원격조작 시스템을 검토하며, 대용량 연산과 실시간 응답의 균형을 위해 하이브리드
    클라우드-엣지 아키텍처를 주장하고, 인지, 사회적 인식, 다중모드 상호작용 및 ANA Avatar XPRIZE 준결선 진출 인간형 간호 로봇
    Asha를 다룬다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- telepresence
- teleoperation
- robotic_avatar
- humanoid_avatar
- cloud_edge_computing
- real_time_communication
- social_awareness
- multimodal_cognition
- shared_autonomy
- vr_ar_interface
- ana_avatar_xprize
- asha_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv PDF; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'A Perspective on Robotic Telepresence and Teleoperation using Cognition:
    Are we there yet?'
  url: https://arxiv.org/abs/2203.02959
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
- system
---

## Overview

This 2022 arXiv paper provides a perspective-style survey of robotic telepresence and teleoperation. The authors frame telepresence as the idea of being present in a remote location virtually or through a robotic avatar, and teleoperation as operating a robot from a remote location for tasks. They argue that realizing capable avatar robots requires architectures that are robust, efficient, and real-time, and they review cloud-centric, edge-centric, and hybrid computation models, real-time communication requirements, security/privacy/reliability concerns, social awareness, cognitive capabilities, manual/automatic operation modes, and VR/AR interfaces.

Section II compares cloud-centric and edge-centric computation. Cloud-centric models handle heavy compute and storage but create excessive network overhead that hurts real-time execution, whereas edge-centric models reduce network overhead but compromise on heavy computation. The authors propose a hybrid cloud-edge centric system as the solution, with high-resource tasks offloaded to the cloud and normal computations performed at the edge. Sections III and IV then stress the importance of low-latency communication protocols (e.g., UDP-based application-layer protocols) and context-aware reliability, where important commands are sent in high-reliability mode and less critical commands can use best-effort delivery.

Section V discusses social awareness, noting that acceptance of telepresence robots depends on social behavior such as navigating among humans, joining groups, and attending to speakers. Section VI examines cognitive capabilities, emphasizing multimodal perception through vision, speech/NLP, and touch sensors, while observing that vision has advanced more than NLP and touch. Sections VII and VIII review manual versus automatic operation, shared autonomy, and the potential of VR/AR to improve remote perception. Section IX sketches use cases (remote meetings, hospital inspection, tele-education, surveillance, library guides, emotional support), Section XI describes the ANA Avatar XPRIZE and the TCS Research-led Asha humanoid nurse robot, and Table III lists commercial telepresence robots.

## Key Contributions

- Argues for a hybrid cloud-edge computation model to balance real-time responsiveness with heavy computational offload (Section II).
- Discusses the importance of real-time, low-latency communication and context-aware reliability for telepresence/teleoperation (Sections III–IV).
- Highlights the need for social awareness and multimodal cognition (vision, speech/NLP, touch) in avatar robots (Sections V–VI).
- Surveys commercial telepresence robots and reports on the ANA Avatar XPRIZE semi-finalist humanoid robot Asha (Table III and Section XI).
- Identifies limitations and future directions including VR/AR immersion and shared autonomy (Sections VII–VIII).

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robot deployment because it focuses on telepresence/teleoperation avatar robots that act as remote human surrogates. It discusses the humanoid nurse robot Asha, a semi-finalist in the ANA Avatar XPRIZE, and shows it performing grasping and handover tasks while communicating with humans using audio-visual and gesture cues. The analysis of real-time control, distributed computing, social interaction, and multimodal cognition maps closely onto the software, AI, and integration challenges facing humanoid robots deployed as remote avatars at scale.
