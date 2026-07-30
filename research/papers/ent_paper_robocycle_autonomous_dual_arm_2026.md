---
$id: ent_paper_robocycle_autonomous_dual_arm_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications'
  zh: 'ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications'
  ko: 'ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications'
summary:
  en: 'arXiv:2607.03616v1 Announce Type: new Abstract: As urban waste volumes escalate and labor shortages intensify, automated
    waste sorting systems are becoming a necessity. However, current robotic solutions often struggle with the 3D perception
    and manipulation of transparent, deformable, or cluttered objects. This work introduces ROBOCYCLE, an autonomous dual-arm
    robotic recycling platform designed to meet the recycling standards of the Tokyo metropolitan area. Our approach integrates
    multi-view RGB-D perception, transformer-based instance segmentation using RF-DETR, and 6-DoF grasp planning via the Anygrasp
    SDK. By processing segmentated point clouds, the system generates robust candidate poses for irregular and deformable
    waste. The system achieved a 90.3% grasp success rate and 84.3% overall task success rate, effectively performing complex
    coordinated tasks such as unscrewing PET bottle caps. The proposed platform offers a scalable solution for autonomous
    waste management in real-world human environments.'
  zh: ROBOCYCLE 是一个面向东京都市圈回收标准的自主双臂机器人回收平台。它整合了多视角 RGB-D 感知、基于 RF-DETR 的 Transformer 实例分割以及 Anygrasp SDK 的 6 自由度抓取规划，实现了 90.3%
    的抓取成功率和 84.3% 的整体任务成功率，并能完成拧开 PET 瓶盖等复杂协调操作。
  ko: 'arXiv:2607.03616v1 Announce Type: new Abstract: As urban waste volumes escalate and labor shortages intensify, automated
    waste sorting systems are becoming a necessity. However, current robotic solutions often struggle with the 3D perception
    and manipulation of transparent, deformable, or cluttered objects. This work introduces ROBOCYCLE, an autonomous dual-arm
    robotic recycling platform designed to meet the recycling standards of the Tokyo metropolitan area. Our approach integrates
    multi-view RGB-D perception, transformer-based instance segmentation using RF-DETR, and 6-DoF grasp planning via the Anygrasp
    SDK. By processing segmentated point clouds, the system generates robust candidate poses for irregular and deformable
    waste. The system achieved a 90.3% grasp success rate and 84.3% overall task success rate, effectively performing complex
    coordinated tasks such as unscrewing PET bottle caps. The proposed platform offers a scalable solution for autonomous
    waste management in real-world human environments.'
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
- robotics
- robocycle
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03616v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications (arXiv)'
  url: https://arxiv.org/abs/2607.03616
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
随着城市垃圾量激增和劳动力短缺加剧，自动化垃圾分类系统变得不可或缺。现有机器人方案在处理透明、可变形或杂乱物体的 3D 感知与操作时往往力不从心。ROBOCYCLE 通过融合多视角 RGB-D 感知、基于 RF-DETR 的 Transformer 实例分割以及 Anygrasp SDK 的 6 自由度抓取规划，有效应对了不规则和可变形废弃物的挑战。该系统在处理分割后的点云时能生成稳健的候选抓取姿态，最终在真实环境中取得了 90.3% 的抓取成功率和 84.3% 的整体任务成功率，并展示了拧开 PET 瓶盖等复杂协调操作能力。

## 核心内容
### 方法架构
- **感知系统**：采用多视角 RGB-D 相机进行环境感知，为后续处理提供丰富的三维信息。
- **实例分割**：使用基于 Transformer 架构的 RF-DETR 模型，对废弃物进行精确的实例分割，尤其针对透明和可变形物体。
- **抓取规划**：通过 Anygrasp SDK 实现 6 自由度抓取规划，能够处理不规则形状的物体。
- **点云处理**：系统对分割后的点云进行后处理，生成稳健的候选抓取姿态，以适应各种废弃物形态。

### 实验设置与关键数字
- **实验环境**：在模拟东京都市圈回收标准的真实场景中进行测试。
- **抓取成功率**：系统在抓取各类废弃物时达到了 90.3% 的成功率。
- **整体任务成功率**：在完整的回收任务中，系统实现了 84.3% 的整体成功率。
- **复杂操作**：成功演示了拧开 PET 瓶盖等需要双臂协调的复杂操作。

### 结论
ROBOCYCLE 为真实人类环境中的自主废弃物管理提供了一个可扩展的解决方案，有效解决了当前机器人系统在处理透明、可变形和杂乱物体时的感知与操作难题。

## Overview
As urban waste volumes escalate and labor shortages intensify, automated waste sorting systems are becoming a necessity. However, current robotic solutions often struggle with the 3D perception and manipulation of transparent, deformable, or cluttered objects. This work introduces ROBOCYCLE, an autonomous dual-arm robotic recycling platform designed to meet the recycling standards of the Tokyo metropolitan area. Our approach integrates multi-view RGB-D perception, transformer-based instance segmentation using RF-DETR, and 6-DoF grasp planning via the Anygrasp SDK. By processing segmentated point clouds, the system generates robust candidate poses for irregular and deformable waste. The system achieved a 90.3% grasp success rate and 84.3% overall task success rate, effectively performing complex coordinated tasks such as unscrewing PET bottle caps. The proposed platform offers a scalable solution for autonomous waste management in real-world human environments.

## Overview
As urban waste volumes escalate and labor shortages intensify, automated waste sorting systems are becoming a necessity. However, current robotic solutions often struggle with the 3D perception and manipulation of transparent, deformable, or cluttered objects. This work introduces ROBOCYCLE, an autonomous dual-arm robotic recycling platform designed to meet the recycling standards of the Tokyo metropolitan area. Our approach integrates multi-view RGB-D perception, transformer-based instance segmentation using RF-DETR, and 6-DoF grasp planning via the Anygrasp SDK. By processing segmented point clouds, the system generates robust candidate poses for irregular and deformable waste. The system achieved a 90.3% grasp success rate and 84.3% overall task success rate, effectively performing complex coordinated tasks such as unscrewing PET bottle caps. The proposed platform offers a scalable solution for autonomous waste management in real-world human environments.

## Content
As urban waste volumes escalate and labor shortages intensify, automated waste sorting systems are becoming a necessity. However, current robotic solutions often struggle with the 3D perception and manipulation of transparent, deformable, or cluttered objects. This work introduces ROBOCYCLE, an autonomous dual-arm robotic recycling platform designed to meet the recycling standards of the Tokyo metropolitan area. Our approach integrates multi-view RGB-D perception, transformer-based instance segmentation using RF-DETR, and 6-DoF grasp planning via the Anygrasp SDK. By processing segmented point clouds, the system generates robust candidate poses for irregular and deformable waste. The system achieved a 90.3% grasp success rate and 84.3% overall task success rate, effectively performing complex coordinated tasks such as unscrewing PET bottle caps. The proposed platform offers a scalable solution for autonomous waste management in real-world human environments.

## 개요
도시 폐기물 양이 증가하고 노동력 부족이 심화됨에 따라 자동화된 폐기물 분류 시스템이 필수적으로 자리 잡고 있습니다. 그러나 현재의 로봇 솔루션은 투명하거나 변형 가능하거나 복잡하게 쌓인 물체의 3D 인식 및 조작에 어려움을 겪는 경우가 많습니다. 본 연구는 도쿄 도심 지역의 재활용 기준을 충족하도록 설계된 자율 이중 암 로봇 재활용 플랫폼인 ROBOCYCLE을 소개합니다. 우리의 접근 방식은 다중 시점 RGB-D 인식, RF-DETR을 사용한 트랜스포머 기반 인스턴스 분할, Anygrasp SDK를 통한 6자유도 파지 계획을 통합합니다. 분할된 포인트 클라우드를 처리함으로써 시스템은 불규칙하고 변형 가능한 폐기물에 대해 강건한 후보 자세를 생성합니다. 시스템은 90.3%의 파지 성공률과 84.3%의 전체 작업 성공률을 달성했으며, PET 병뚜껑을 푸는 것과 같은 복잡한 협력 작업을 효과적으로 수행했습니다. 제안된 플랫폼은 실제 인간 환경에서 자율 폐기물 관리를 위한 확장 가능한 솔루션을 제공합니다.

## 핵심 내용
도시 폐기물 양이 증가하고 노동력 부족이 심화됨에 따라 자동화된 폐기물 분류 시스템이 필수적으로 자리 잡고 있습니다. 그러나 현재의 로봇 솔루션은 투명하거나 변형 가능하거나 복잡하게 쌓인 물체의 3D 인식 및 조작에 어려움을 겪는 경우가 많습니다. 본 연구는 도쿄 도심 지역의 재활용 기준을 충족하도록 설계된 자율 이중 암 로봇 재활용 플랫폼인 ROBOCYCLE을 소개합니다. 우리의 접근 방식은 다중 시점 RGB-D 인식, RF-DETR을 사용한 트랜스포머 기반 인스턴스 분할, Anygrasp SDK를 통한 6자유도 파지 계획을 통합합니다. 분할된 포인트 클라우드를 처리함으로써 시스템은 불규칙하고 변형 가능한 폐기물에 대해 강건한 후보 자세를 생성합니다. 시스템은 90.3%의 파지 성공률과 84.3%의 전체 작업 성공률을 달성했으며, PET 병뚜껑을 푸는 것과 같은 복잡한 협력 작업을 효과적으로 수행했습니다. 제안된 플랫폼은 실제 인간 환경에서 자율 폐기물 관리를 위한 확장 가능한 솔루션을 제공합니다.

## 参考
- http://arxiv.org/abs/2607.03616v1
