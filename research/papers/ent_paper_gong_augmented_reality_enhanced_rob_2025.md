---
$id: ent_paper_gong_augmented_reality_enhanced_rob_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Augmented Reality-Enhanced Robot Teleoperation for Collecting User Demonstrations
  zh: 用于收集用户演示的增强现实增强型机器人遥操作系统
  ko: 사용자 시연 수집을 위한 증강 현실 기반 로봇 원격 조작
summary:
  en: Proposes an AR-based teleoperation system that lets operators control ABB industrial and collaborative robots remotely
    via an HMD and hand controllers, using real-time point-cloud rendering to collect Programming by Demonstration data without
    entering the workspace.
  zh: 提出一种基于增强现实的遥操作系统，操作者可通过头戴显示器和手柄远程控制ABB工业及协作机器人，并利用实时点云渲染在无需进入工作空间的情况下收集示教编程数据。
  ko: HMD와 컨트롤러를 이용해 ABB 산업용 및 협동 로봇을 원격으로 제어하고, 실시간 포인트 클라우드 렌더링을 통해 작업 공간에 들어가지 않고도 시연 기반 프로그래밍 데이터를 수집하는 AR 기반 원격 조작 시스템을
    제안한다.
domains:
- 08_software_middleware
- 09_data_datasets
- 03_manufacturing_processes
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- system
tags:
- augmented_reality
- teleoperation
- programming_by_demonstration
- industrial_robot
- collaborative_robot
- point_cloud
- human_robot_interface
- demonstration_collection
- machine_learning_data
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11783v1.
sources:
- id: src_001
  type: paper
  title: Augmented Reality-Enhanced Robot Teleoperation for Collecting User Demonstrations
  url: https://arxiv.org/abs/2509.11783
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Traditional industrial robot programming is often complex and time-consuming, typically requiring weeks or even months of effort from expert programmers. Although Programming by Demonstration (PbD) offers a more accessible alternative, intuitive interfaces for robot control and demonstration collection remain challenging. To address this, we propose an Augmented Reality (AR)-enhanced robot teleoperation system that integrates AR-based control with spatial point cloud rendering, enabling intuitive, contact-free demonstrations. This approach allows operators to control robots remotely without entering the workspace or using conventional tools like the teach pendant. The proposed system is generally applicable and has been demonstrated on ABB robot platforms, specifically validated with the IRB 1200 industrial robot and the GoFa 5 collaborative robot. A user study evaluates the impact of real-time environmental perception, specifically with and without point cloud rendering, on task completion accuracy, efficiency, and user confidence. Results indicate that enhanced perception significantly improves task performance by 28% and enhances user experience, as reflected by a 12% increase in the System Usability Scale (SUS) score. This work contributes to the advancement of intuitive robot teleoperation, AR interface design, environmental perception, and teleoperation safety mechanisms in industrial settings for demonstration collection. The collected demonstrations may serve as valuable training data for machine learning applications.

## 核心内容
Traditional industrial robot programming is often complex and time-consuming, typically requiring weeks or even months of effort from expert programmers. Although Programming by Demonstration (PbD) offers a more accessible alternative, intuitive interfaces for robot control and demonstration collection remain challenging. To address this, we propose an Augmented Reality (AR)-enhanced robot teleoperation system that integrates AR-based control with spatial point cloud rendering, enabling intuitive, contact-free demonstrations. This approach allows operators to control robots remotely without entering the workspace or using conventional tools like the teach pendant. The proposed system is generally applicable and has been demonstrated on ABB robot platforms, specifically validated with the IRB 1200 industrial robot and the GoFa 5 collaborative robot. A user study evaluates the impact of real-time environmental perception, specifically with and without point cloud rendering, on task completion accuracy, efficiency, and user confidence. Results indicate that enhanced perception significantly improves task performance by 28% and enhances user experience, as reflected by a 12% increase in the System Usability Scale (SUS) score. This work contributes to the advancement of intuitive robot teleoperation, AR interface design, environmental perception, and teleoperation safety mechanisms in industrial settings for demonstration collection. The collected demonstrations may serve as valuable training data for machine learning applications.

## 参考
- http://arxiv.org/abs/2509.11783v1

