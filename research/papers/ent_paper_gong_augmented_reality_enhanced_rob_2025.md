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
  zh: 本文提出了一种基于增强现实（AR）的机器人遥操作系统，允许操作员通过头戴式显示器和手部控制器远程控制ABB工业与协作机器人。该系统利用实时点云渲染收集编程示教数据，无需进入工作空间，在用户研究中将任务性能提升28%，系统可用性量表（SUS）得分提高12%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11783v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (661 chars, DeepSeek).'
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
传统工业机器人编程通常需要专家程序员花费数周甚至数月时间，而编程示教（PbD）虽提供更易用的替代方案，但直观的控制与示教收集接口仍具挑战。为此，研究者开发了AR增强遥操作系统，将AR控制与空间点云渲染结合，实现无接触式远程示教。该系统已在ABB IRB 1200工业机器人和GoFa 5协作机器人上验证，并通过用户研究对比了有无点云渲染对任务精度、效率和用户信心的影响。结果表明，增强感知使任务性能提升28%，系统可用性量表（SUS）得分提高12%，为工业场景下的直观遥操作、AR界面设计及安全机制提供了新方案。

## 核心内容
### 方法架构
- 系统集成AR头戴式显示器（HMD）与手部控制器，操作员通过实时点云渲染感知机器人工作空间，无需物理接触或传统示教器。
- 采用编程示教（PbD）范式，收集的示教数据可直接用于机器学习模型训练。

### 实验设置
- 在ABB IRB 1200工业机器人和GoFa 5协作机器人平台上验证系统通用性。
- 用户研究对比两种条件：启用实时点云渲染（增强感知）与禁用点云渲染（基础感知）。

### 关键结果
- 增强感知使任务完成准确率提升28%，用户信心显著增强。
- 系统可用性量表（SUS）得分提高12%，反映用户体验优化。
- 操作效率提升，示教数据收集过程更安全（无需进入工作空间）。

### 结论
- 该系统为工业场景下的直观遥操作、AR界面设计、环境感知与安全机制提供了有效方案。
- 收集的示教数据可作为高质量训练样本，支持机器人学习应用。

## Overview
Traditional industrial robot programming is often complex and time-consuming, typically requiring weeks or even months of effort from expert programmers. Although Programming by Demonstration (PbD) offers a more accessible alternative, intuitive interfaces for robot control and demonstration collection remain challenging. To address this, we propose an Augmented Reality (AR)-enhanced robot teleoperation system that integrates AR-based control with spatial point cloud rendering, enabling intuitive, contact-free demonstrations. This approach allows operators to control robots remotely without entering the workspace or using conventional tools like the teach pendant. The proposed system is generally applicable and has been demonstrated on ABB robot platforms, specifically validated with the IRB 1200 industrial robot and the GoFa 5 collaborative robot. A user study evaluates the impact of real-time environmental perception, specifically with and without point cloud rendering, on task completion accuracy, efficiency, and user confidence. Results indicate that enhanced perception significantly improves task performance by 28% and enhances user experience, as reflected by a 12% increase in the System Usability Scale (SUS) score. This work contributes to the advancement of intuitive robot teleoperation, AR interface design, environmental perception, and teleoperation safety mechanisms in industrial settings for demonstration collection. The collected demonstrations may serve as valuable training data for machine learning applications.

## 参考
- http://arxiv.org/abs/2509.11783v1

## 개요
전통적인 산업용 로봇 프로그래밍은 일반적으로 전문 프로그래머가 수 주에서 수 개월이 소요되지만, 프로그래밍 시범(PbD)은 더 사용하기 쉬운 대안을 제공하지만 직관적인 제어와 시범 수집 인터페이스는 여전히 도전 과제입니다. 이를 위해 연구자들은 AR 제어와 공간 포인트 클라우드 렌더링을 결합한 AR 증강 원격 조작 시스템을 개발하여 비접촉식 원격 시범을 구현했습니다. 이 시스템은 ABB IRB 1200 산업용 로봇과 GoFa 5 협동 로봇에서 검증되었으며, 사용자 연구를 통해 포인트 클라우드 렌더링 유무가 작업 정확도, 효율성 및 사용자 자신감에 미치는 영향을 비교했습니다. 결과는 증강 인식이 작업 성능을 28% 향상시키고, 시스템 사용성 척도(SUS) 점수를 12% 높여 산업 현장에서의 직관적인 원격 조작, AR 인터페이스 설계 및 안전 메커니즘에 새로운 솔루션을 제공함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- 시스템은 AR 헤드 마운트 디스플레이(HMD)와 손 제어기를 통합하여, 작업자가 실시간 포인트 클라우드 렌더링을 통해 로봇 작업 공간을 인식하며 물리적 접촉이나 전통적인 티칭 펜던트 없이 작업할 수 있습니다.
- 프로그래밍 시범(PbD) 패러다임을 채택하여 수집된 시범 데이터는 머신러닝 모델 훈련에 직접 사용될 수 있습니다.

### 실험 설정
- ABB IRB 1200 산업용 로봇과 GoFa 5 협동 로봇 플랫폼에서 시스템의 범용성을 검증했습니다.
- 사용자 연구는 두 가지 조건을 비교했습니다: 실시간 포인트 클라우드 렌더링 활성화(증강 인식)와 포인트 클라우드 렌더링 비활성화(기본 인식).

### 주요 결과
- 증강 인식은 작업 완료 정확도를 28% 향상시키고 사용자 자신감을 크게 강화했습니다.
- 시스템 사용성 척도(SUS) 점수가 12% 상승하여 사용자 경험 최적화를 반영했습니다.
- 작업 효율성이 향상되었고, 시범 데이터 수집 과정이 더 안전해졌습니다(작업 공간에 들어갈 필요 없음).

### 결론
- 이 시스템은 산업 현장에서의 직관적인 원격 조작, AR 인터페이스 설계, 환경 인식 및 안전 메커니즘에 효과적인 솔루션을 제공합니다.
- 수집된 시범 데이터는 고품질 훈련 샘플로 활용되어 로봇 학습 응용을 지원할 수 있습니다.
