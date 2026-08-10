---
$id: ent_paper_learning_humanoid_end_effector_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
  zh: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
  ko: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
summary:
  en: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: HERO 是一种用于人形机器人开放词汇视觉移动操作的新型模块化系统，由 2026 年的研究工作提出。其核心创新在于通过结合经典机器人与机器学习，实现高精度末端执行器跟踪，将跟踪误差降至 2.44cm，比此前最强方法提升 5.5 倍。该系统在办公室、咖啡店等真实环境中成功抓取多种日常物体，展示了强大的泛化能力。
  ko: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
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
- learning_humanoid_end_effector
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.16705v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (666 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2602.16705
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人在开放场景中操作任意物体的挑战，提出了一种模块化架构。它利用大型视觉模型进行场景理解，并通过模拟训练实现精确的末端执行器控制，避免了端到端学习的扩展难题。核心技术 HERO 结合了逆运动学、学习型前向模型和目标调整与重规划，显著降低了跟踪误差。系统在高度从 43cm 到 92cm 的表面上成功抓取杯子、苹果、玩具等物体，验证了其在实际环境中的有效性。

## 核心内容
### 方法概述
- **模块化设计**：将视觉场景理解与末端执行器控制分离，分别利用大型视觉模型和模拟训练的优势。
- **HERO 策略**：核心是残差感知的末端执行器跟踪策略，包含三个关键组件：
  - **逆运动学**：将残差末端执行器目标转换为参考轨迹。
  - **学习型前向模型**：提供准确的机器人正运动学估计。
  - **目标调整与重规划**：动态修正执行过程中的偏差。

### 实验设置与结果
- **跟踪精度**：HERO 将末端执行器跟踪误差降低至 2.44cm，相比此前最强方法性能提升 5.5 倍。
- **真实环境测试**：系统在办公室、咖啡店等多样化场景中运行，成功抓取杯子、苹果、玩具等日常物体。
- **表面高度范围**：操作表面高度从 43cm 到 92cm，覆盖常见家具高度。
- **验证方式**：通过系统的模块化测试和端到端测试，证明了设计有效性。

### 结论
该工作通过模块化方法解决了人形机器人开放词汇视觉移动操作中的扩展性问题，为训练人形机器人交互日常物体开辟了新途径。

## Overview
Visual loco-manipulation of arbitrary in-the-wild objects requires accurate end-effector (EE) control and a generalizable understanding of the scene from visual inputs (eg, RGB-D images). Existing imitation and sim2real methods jointly learn both these aspects via monolithic end-to-end learning and are thus hard to scale. In this work, we bring to bear the best tools for each of these problems -- large vision models for generalizable scene understanding and simulated training for accurate EE control -- leading to an overall modular loco-manipulation system that exhibits strong generalization. Our core technical innovation is HERO, an accurate residual-aware EE tracking policy made possible by combining classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, and c) goal adjustment and replanning. Together, these innovations reduce the end-effector tracking error to 2.44cm, outperforming the strongest prior method by 5.5x. Our overall system operates in diverse real-world environments, from offices to coffee shops, where the robot reliably grasps various everyday objects (eg, mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests demonstrate the effectiveness of our proposed design. We believe our advances open up new ways of training humanoids to interact with daily objects.

## Overview
Visual loco-manipulation of arbitrary in-the-wild objects requires accurate end-effector (EE) control and a generalizable understanding of the scene from visual inputs (e.g., RGB-D images). Existing imitation and sim2real methods jointly learn both these aspects via monolithic end-to-end learning and are thus hard to scale. In this work, we bring to bear the best tools for each of these problems — large vision models for generalizable scene understanding and simulated training for accurate EE control — leading to an overall modular loco-manipulation system that exhibits strong generalization. Our core technical innovation is HERO, an accurate residual-aware EE tracking policy made possible by combining classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, and c) goal adjustment and replanning. Together, these innovations reduce the end-effector tracking error to 2.44cm, outperforming the strongest prior method by 5.5x. Our overall system operates in diverse real-world environments, from offices to coffee shops, where the robot reliably grasps various everyday objects (e.g., mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests demonstrate the effectiveness of our proposed design. We believe our advances open up new ways of training humanoids to interact with daily objects.

## Content
Visual loco-manipulation of arbitrary in-the-wild objects requires accurate end-effector (EE) control and a generalizable understanding of the scene from visual inputs (e.g., RGB-D images). Existing imitation and sim2real methods jointly learn both these aspects via monolithic end-to-end learning and are thus hard to scale. In this work, we bring to bear the best tools for each of these problems — large vision models for generalizable scene understanding and simulated training for accurate EE control — leading to an overall modular loco-manipulation system that exhibits strong generalization. Our core technical innovation is HERO, an accurate residual-aware EE tracking policy made possible by combining classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, and c) goal adjustment and replanning. Together, these innovations reduce the end-effector tracking error to 2.44cm, outperforming the strongest prior method by 5.5x. Our overall system operates in diverse real-world environments, from offices to coffee shops, where the robot reliably grasps various everyday objects (e.g., mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests demonstrate the effectiveness of our proposed design. We believe our advances open up new ways of training humanoids to interact with daily objects.

## 参考
- http://arxiv.org/abs/2602.16705v3

## 개요
이 연구는 휴머노이드 로봇이 개방된 환경에서 임의의 물체를 조작하는 과제를 해결하기 위해 모듈식 아키텍처를 제안합니다. 이는 대규모 비전 모델을 활용한 장면 이해와 시뮬레이션 훈련을 통한 정밀한 엔드이펙터 제어를 결합하여, 엔드투엔드 학습의 확장 문제를 피합니다. 핵심 기술인 HERO는 역기구학, 학습 기반 순방향 모델, 목표 조정 및 재계획을 결합하여 추적 오류를 크게 줄입니다. 시스템은 높이 43cm에서 92cm 사이의 표면에서 컵, 사과, 장난감 등의 물체를 성공적으로 집어 올려 실제 환경에서의 효과를 입증했습니다.

## 핵심 내용
### 방법 개요
- **모듈식 설계**: 시각적 장면 이해와 엔드이펙터 제어를 분리하여, 각각 대규모 비전 모델과 시뮬레이션 훈련의 장점을 활용합니다.
- **HERO 전략**: 핵심은 잔차 인식 엔드이펙터 추적 전략으로, 세 가지 주요 구성 요소를 포함합니다:
  - **역기구학**: 잔차 엔드이펙터 목표를 참조 궤적으로 변환합니다.
  - **학습 기반 순방향 모델**: 정확한 로봇 순방향 운동학 추정을 제공합니다.
  - **목표 조정 및 재계획**: 실행 중 발생하는 편차를 동적으로 수정합니다.

### 실험 설정 및 결과
- **추적 정밀도**: HERO는 엔드이펙터 추적 오류를 2.44cm로 줄여, 이전 최강 방법 대비 성능을 5.5배 향상시켰습니다.
- **실제 환경 테스트**: 시스템은 사무실, 카페 등 다양한 환경에서 작동하며 컵, 사과, 장난감 등의 일상 물체를 성공적으로 집어 올렸습니다.
- **표면 높이 범위**: 조작 표면 높이는 43cm에서 92cm로, 일반적인 가구 높이를 포괄합니다.
- **검증 방식**: 시스템의 모듈식 테스트와 엔드투엔드 테스트를 통해 설계의 효과성을 입증했습니다.

### 결론
이 연구는 모듈식 접근 방식을 통해 휴머노이드 로봇의 개방 어휘 시각 이동 조작에서의 확장 문제를 해결하며, 휴머노이드 로봇이 일상 물체와 상호작용하도록 훈련하는 새로운 경로를 제시합니다.
