---
$id: ent_paper_language_guided_grasping_under_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Language-Guided Grasping under Partial Observation for Mobile Manipulation in Field Inspection and Maintenance
  zh: Language-Guided Grasping under Partial Observation for Mobile Manipulation in Field Inspection and Maintenance
  ko: Language-Guided Grasping under Partial Observation for Mobile Manipulation in Field Inspection and Maintenance
summary:
  en: 'arXiv:2603.07866v3 Announce Type: replace Abstract: Offshore inspection and maintenance have increasingly been using
    legged robots for routine sensing, yet many useful interventions still require physical interaction with tools, containers,
    and task-relevant objects. Employing robots for these tasks can reduce operators'' exposure in confined, elevated, or
    potentially explosive areas. This paper presents a language-guided grasping pipeline for a legged mobile manipulator operating
    under partial observation. An operator defines the target, the system grounds it in RGB with open-vocabulary detection
    and promptable segmentation, extracts an object-centric RGB-D point cloud, improves sparse geometry through depth compensation
    and point-cloud completion, and selects a 6-DoF grasp using collision, clearance, reachability, and approach constraints.
    The system is implemented on a quadruped robot with an arm and evaluated in two cluttered tabletop scenes motivated by
    small-object retrieval during inspection and maintenance. Across paired trials, the proposed pipeline achieved 9/10 successful
    grasps, compared with 3/10 for a view-dependent deployment baseline. In this controlled setting, object-centric completion
    and execution-aware selection reduced approach collisions and improved the reliability of language-guided grasping for
    supervised field manipulation.'
  zh: 本文提出一种面向部分观测条件下腿式移动机械臂的语言引导抓取流水线。该系统由操作员指定目标，通过开放词汇检测与可提示分割在RGB图像中定位物体，提取物体中心RGB-D点云，并利用深度补偿与点云补全改善稀疏几何结构，最终结合碰撞、间隙、可达性与接近约束选择6自由度抓取姿态。在海上巡检维护场景的桌面实验中，该流水线在10次尝试中成功抓取9次，而基线方法仅成功3次。
  ko: 'arXiv:2603.07866v3 Announce Type: replace Abstract: Offshore inspection and maintenance have increasingly been using
    legged robots for routine sensing, yet many useful interventions still require physical interaction with tools, containers,
    and task-relevant objects. Employing robots for these tasks can reduce operators'' exposure in confined, elevated, or
    potentially explosive areas. This paper presents a language-guided grasping pipeline for a legged mobile manipulator operating
    under partial observation. An operator defines the target, the system grounds it in RGB with open-vocabulary detection
    and promptable segmentation, extracts an object-centric RGB-D point cloud, improves sparse geometry through depth compensation
    and point-cloud completion, and selects a 6-DoF grasp using collision, clearance, reachability, and approach constraints.
    The system is implemented on a quadruped robot with an arm and evaluated in two cluttered tabletop scenes motivated by
    small-object retrieval during inspection and maintenance. Across paired trials, the proposed pipeline achieved 9/10 successful
    grasps, compared with 3/10 for a view-dependent deployment baseline. In this controlled setting, object-centric completion
    and execution-aware selection reduced approach collisions and improved the reliability of language-guided grasping for
    supervised field manipulation.'
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
- language_guided_grasping_under
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.07866v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1031 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Language-Guided Grasping under Partial Observation for Mobile Manipulation in Field Inspection and Maintenance (arXiv)
  url: https://arxiv.org/abs/2603.07866
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该研究针对海上巡检维护中腿式机器人仅能执行常规感知任务、缺乏物理交互能力的痛点，提出一套语言引导的抓取流水线。系统在部分观测条件下运行，操作员通过自然语言定义目标物体，系统依次执行开放词汇检测、可提示分割、物体中心点云提取、深度补偿与点云补全，最后基于碰撞、间隙、可达性与接近约束选择6自由度抓取姿态。在四足机器人平台上，该方法在两类桌面场景中取得90%的抓取成功率，显著优于依赖视角的基线方法（30%），验证了物体中心点云补全与执行感知选择策略的有效性。

## 核心内容
### 方法架构
- **语言引导目标定位**：操作员通过自然语言描述目标物体，系统利用开放词汇检测（open-vocabulary detection）与可提示分割（promptable segmentation）在RGB图像中定位并分割目标。
- **点云提取与补全**：从分割区域提取物体中心RGB-D点云，针对稀疏几何结构实施深度补偿（depth compensation）与点云补全（point-cloud completion），以应对部分观测下的数据缺失。
- **抓取选择**：基于碰撞（collision）、间隙（clearance）、可达性（reachability）与接近约束（approach constraints）选择6自由度抓取姿态，确保执行安全性与成功率。

### 实验设置
- **平台**：四足机器人（quadruped robot）搭载机械臂，在两类桌面场景中测试，模拟巡检维护中的小物体取回任务。
- **基线**：对比一种依赖视角的部署基线（view-dependent deployment baseline）。
- **评估指标**：配对试验（paired trials）中的抓取成功率。

### 关键结果
- **成功率**：提出流水线在10次尝试中成功抓取9次（90%），基线方法仅成功3次（30%）。
- **碰撞减少**：物体中心点云补全（object-centric completion）与执行感知选择（execution-aware selection）显著降低了接近阶段的碰撞次数，提升了语言引导抓取在受控现场操作中的可靠性。

### 结论
该研究证明，在部分观测条件下，通过物体中心点云补全与执行感知约束选择，可显著提升语言引导抓取在腿式移动机械臂上的表现，为海上巡检维护中的物理交互任务提供了可行方案。

## Overview
Offshore inspection and maintenance have increasingly been using legged robots for routine sensing, yet many useful interventions still require physical interaction with tools, containers, and task-relevant objects. Employing robots for these tasks can reduce operators' exposure in confined, elevated, or potentially explosive areas. This paper presents a language-guided grasping pipeline for a legged mobile manipulator operating under partial observation. An operator defines the target, the system grounds it in RGB with open-vocabulary detection and promptable segmentation, extracts an object-centric RGB-D point cloud, improves sparse geometry through depth compensation and point-cloud completion, and selects a 6-DoF grasp using collision, clearance, reachability, and approach constraints. The system is implemented on a quadruped robot with an arm and evaluated in two cluttered tabletop scenes motivated by small-object retrieval during inspection and maintenance. Across paired trials, the proposed pipeline achieved 9/10 successful grasps, compared with 3/10 for a view-dependent deployment baseline. In this controlled setting, object-centric completion and execution-aware selection reduced approach collisions and improved the reliability of language-guided grasping for supervised field manipulation.

## 参考
- http://arxiv.org/abs/2603.07866v3

## 개요
본 연구는 해상 순찰 및 유지보수 과정에서 보행형 로봇이 일반적인 인식 작업만 수행할 수 있고 물리적 상호작용 능력이 부족하다는 문제점을 해결하기 위해, 언어 기반 그리핑 파이프라인을 제안한다. 시스템은 부분 관측 조건에서 작동하며, 운영자가 자연어로 대상 물체를 정의하면 시스템은 개방형 어휘 탐지, 프롬프트 가능한 분할, 객체 중심 포인트 클라우드 추출, 깊이 보정 및 포인트 클라우드 완성을 순차적으로 수행한 후, 충돌, 간격, 도달 가능성 및 접근 제약 조건을 기반으로 6자유도 그리핑 자세를 선택한다. 사족 보행 로봇 플랫폼에서 이 방법은 두 가지 테이블형 시나리오에서 90%의 그리핑 성공률을 달성하여, 시점 의존형 기준 방법(30%)보다 크게 우수함을 입증했으며, 객체 중심 포인트 클라우드 완성과 실행 인식 선택 전략의 효과를 검증했다.

## 핵심 내용
### 방법 아키텍처
- **언어 기반 목표 위치 파악**: 운영자가 자연어로 대상 물체를 설명하면, 시스템은 개방형 어휘 탐지(open-vocabulary detection)와 프롬프트 가능한 분할(promptable segmentation)을 사용하여 RGB 이미지에서 대상을 위치 파악하고 분할한다.
- **포인트 클라우드 추출 및 완성**: 분할 영역에서 객체 중심 RGB-D 포인트 클라우드를 추출하고, 희소한 기하 구조에 대해 깊이 보정(depth compensation)과 포인트 클라우드 완성(point-cloud completion)을 수행하여 부분 관측에서의 데이터 누락 문제를 해결한다.
- **그리핑 선택**: 충돌(collision), 간격(clearance), 도달 가능성(reachability) 및 접근 제약 조건(approach constraints)을 기반으로 6자유도 그리핑 자세를 선택하여 실행 안전성과 성공률을 보장한다.

### 실험 설정
- **플랫폼**: 사족 보행 로봇(quadruped robot)에 로봇 팔을 장착하고, 두 가지 테이블형 시나리오에서 테스트하여 순찰 및 유지보수 중 소형 물체 회수 작업을 모사한다.
- **기준 방법**: 시점 의존형 배포 기준 방법(view-dependent deployment baseline)과 비교한다.
- **평가 지표**: 짝지어진 시험(paired trials)에서의 그리핑 성공률.

### 핵심 결과
- **성공률**: 제안된 파이프라인은 10회 시도 중 9회 성공(90%)했으며, 기준 방법은 3회만 성공(30%)했다.
- **충돌 감소**: 객체 중심 포인트 클라우드 완성(object-centric completion)과 실행 인식 선택(execution-aware selection)이 접근 단계에서의 충돌 횟수를 크게 줄여, 통제된 현장 작업에서 언어 기반 그리핑의 신뢰성을 향상시켰다.

### 결론
본 연구는 부분 관측 조건에서 객체 중심 포인트 클라우드 완성과 실행 인식 제약 선택을 통해 보행형 이동 로봇 팔의 언어 기반 그리핑 성능을 크게 향상시킬 수 있음을 입증했으며, 해상 순찰 및 유지보수에서의 물리적 상호작용 작업에 실현 가능한 솔루션을 제공한다.
