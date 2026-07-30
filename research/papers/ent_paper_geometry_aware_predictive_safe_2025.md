---
$id: ent_paper_geometry_aware_predictive_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometry-Aware Predictive Safety Filters on Humanoids
  zh: Geometry-Aware Predictive Safety Filters on Humanoids
  ko: Geometry-Aware Predictive Safety Filters on Humanoids
summary:
  en: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
  zh: Geometry-Aware Predictive Safety Filters on Humanoids 是2025年关于人形机器人自主导航的工作，由研究团队提出。核心贡献在于将基于Poisson safety functions的控制障碍函数（CBF）约束集成到非线性模型预测控制（MPC）中，实现几何感知的实时安全轨迹生成，并在人形与四足机器人上验证了有效性。
  ko: Geometry-Aware Predictive Safety Filters on Humanoids is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- geometry_aware_predictive_safe
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11129v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Geometry-Aware Predictive Safety Filters on Humanoids (arXiv)
  url: https://arxiv.org/abs/2508.11129
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对非结构化动态环境中机器人导航的挑战，特别是腿式机器人可操作非对称几何体带来的安全约束问题。方法通过Poisson safety functions从感知数据数值合成CBF约束，并将静态Dirichlet问题扩展为参数化移动边界值问题以处理时变域。同时，利用Minkowski集合运算将域提升至考虑机器人几何的构型空间。最终在人形和四足机器人上实现实时预测安全滤波器，在多种安全关键场景中验证了Poisson safety functions的通用性与CBF约束MPC控制器的优势。

## 核心内容
### 方法架构
- **核心框架**：提出基于非线性模型预测控制（MPC）的预测安全滤波器，用于在线轨迹生成。
- **安全约束**：采用控制障碍函数（CBF）实现几何感知安全约束，关键创新在于使用Poisson safety functions从感知数据数值合成CBF约束。
- **时变域处理**：将Poisson方程的静态Dirichlet问题重新表述为参数化移动边界值问题，使理论框架能适应环境域的时变变化。
- **几何建模**：通过Minkowski集合运算将环境域提升至构型空间，显式考虑机器人可操作非对称几何体。

### 实验设置
- **机器人平台**：在人形机器人（humanoid）和四足机器人（quadruped）上部署实时预测安全滤波器。
- **测试场景**：涵盖多种安全关键场景（如动态障碍物避让、非结构化地形导航）。

### 关键结果
- **性能验证**：实验证明Poisson safety functions在几何感知安全约束中的通用性，CBF约束MPC控制器在实时轨迹生成中显著提升安全性。
- **数值优势**：方法无需预定义安全区域，直接从感知数据在线合成约束，降低了对环境先验知识的依赖。

### 结论
该工作为腿式机器人自主导航提供了几何感知的安全保障框架，通过Poisson safety functions与CBF-MPC的结合，实现了对非对称几何体与时变环境的鲁棒处理。未来可扩展至更复杂的动态交互场景。

## Overview
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 개요
구조화되지 않고 동적으로 변화하는 환경에서의 자율 주행은 현대 로봇 공학자들에게 많은 도전 과제를 제시하는 복잡한 작업입니다. 특히, 보행 로봇은 일반적으로 조작 가능한 비대칭 형상을 가지며, 이는 안전이 중요한 궤적 계획 중에 고려되어야 합니다. 본 연구는 제어 장벽 함수(CBF)를 기반으로 형상을 인식하는 안전 제약 조건을 갖춘 온라인 궤적 생성을 위한 비선형 모델 예측 제어(MPC) 알고리즘인 예측 안전 필터를 제안합니다. 중요한 점은, 우리의 방법이 푸아송 안전 함수를 활용하여 인식 데이터로부터 직접 CBF 제약 조건을 수치적으로 합성한다는 것입니다. 우리는 푸아송 방정식에 대한 정적 디리클레 문제를 매개변수화된 이동 경계값 문제로 재구성하여 도메인의 시간적 변화를 통합하도록 푸아송 안전 함수의 이론적 프레임워크를 확장합니다. 또한, 민코프스키 집합 연산을 사용하여 로봇 형상을 고려한 구성 공간으로 도메인을 확장합니다. 마지막으로, 다양한 안전이 중요한 시나리오에서 인간형 및 사족 로봇에 실시간 예측 안전 필터를 구현합니다. 결과는 푸아송 안전 함수의 다용성과 CBF 제약 조건이 적용된 모델 예측 안전 중요 제어기의 이점을 강조합니다.

## 핵심 내용
구조화되지 않고 동적으로 변화하는 환경에서의 자율 주행은 현대 로봇 공학자들에게 많은 도전 과제를 제시하는 복잡한 작업입니다. 특히, 보행 로봇은 일반적으로 조작 가능한 비대칭 형상을 가지며, 이는 안전이 중요한 궤적 계획 중에 고려되어야 합니다. 본 연구는 제어 장벽 함수(CBF)를 기반으로 형상을 인식하는 안전 제약 조건을 갖춘 온라인 궤적 생성을 위한 비선형 모델 예측 제어(MPC) 알고리즘인 예측 안전 필터를 제안합니다. 중요한 점은, 우리의 방법이 푸아송 안전 함수를 활용하여 인식 데이터로부터 직접 CBF 제약 조건을 수치적으로 합성한다는 것입니다. 우리는 푸아송 방정식에 대한 정적 디리클레 문제를 매개변수화된 이동 경계값 문제로 재구성하여 도메인의 시간적 변화를 통합하도록 푸아송 안전 함수의 이론적 프레임워크를 확장합니다. 또한, 민코프스키 집합 연산을 사용하여 로봇 형상을 고려한 구성 공간으로 도메인을 확장합니다. 마지막으로, 다양한 안전이 중요한 시나리오에서 인간형 및 사족 로봇에 실시간 예측 안전 필터를 구현합니다. 결과는 푸아송 안전 함수의 다용성과 CBF 제약 조건이 적용된 모델 예측 안전 중요 제어기의 이점을 강조합니다.

## 参考
- http://arxiv.org/abs/2508.11129v1
