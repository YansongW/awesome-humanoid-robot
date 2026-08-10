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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03616v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (770 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03616v1

## 개요
도시 쓰레기 양의 급증과 노동력 부족 심화로 인해 자동화된 쓰레기 분류 시스템이 필수적이 되었다. 기존 로봇 솔루션은 투명하거나 변형 가능한 물체, 또는 어수선한 물체의 3D 인식 및 조작에 종종 한계를 보인다. ROBOCYCLE은 다중 시점 RGB-D 인식, RF-DETR 기반 Transformer 인스턴스 분할, 그리고 Anygrasp SDK의 6자유도 그리핑 계획을 융합하여 불규칙하고 변형 가능한 폐기물의 문제를 효과적으로 해결한다. 이 시스템은 분할된 포인트 클라우드를 처리할 때 견고한 후보 그리핑 자세를 생성하며, 실제 환경에서 90.3%의 그리핑 성공률과 84.3%의 전체 작업 성공률을 달성했고, PET 병뚜껑을 여는 것과 같은 복잡한 협응 조작 능력을 입증했다.

## 핵심 내용
### 방법 아키텍처
- **인식 시스템**: 다중 시점 RGB-D 카메라를 사용하여 환경을 인식하고, 후속 처리를 위한 풍부한 3차원 정보를 제공한다.
- **인스턴스 분할**: Transformer 아키텍처 기반의 RF-DETR 모델을 사용하여 폐기물을 정밀하게 인스턴스 분할하며, 특히 투명하고 변형 가능한 물체에 중점을 둔다.
- **그리핑 계획**: Anygrasp SDK를 통해 6자유도 그리핑 계획을 구현하여 불규칙한 형태의 물체를 처리할 수 있다.
- **포인트 클라우드 처리**: 시스템은 분할된 포인트 클라우드를 후처리하여 다양한 폐기물 형태에 적응할 수 있는 견고한 후보 그리핑 자세를 생성한다.

### 실험 설정 및 주요 수치
- **실험 환경**: 도쿄 도시권 재활용 기준을 시뮬레이션한 실제 시나리오에서 테스트를 수행했다.
- **그리핑 성공률**: 시스템은 다양한 폐기물을 그리핑할 때 90.3%의 성공률을 달성했다.
- **전체 작업 성공률**: 완전한 재활용 작업에서 시스템은 84.3%의 전체 성공률을 구현했다.
- **복잡한 조작**: PET 병뚜껑을 여는 것과 같은 양팔 협응이 필요한 복잡한 조작을 성공적으로 시연했다.

### 결론
ROBOCYCLE은 실제 인간 환경에서의 자율 폐기물 관리를 위한 확장 가능한 솔루션을 제공하며, 현재 로봇 시스템이 투명하고 변형 가능하며 어수선한 물체를 처리할 때 겪는 인식 및 조작 문제를 효과적으로 해결한다.
