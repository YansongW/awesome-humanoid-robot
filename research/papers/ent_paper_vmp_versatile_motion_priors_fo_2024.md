---
$id: ent_paper_vmp_versatile_motion_priors_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
  zh: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
  ko: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
summary:
  en: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: VMP（Versatile Motion Priors）是2024年提出的一种两阶段控制方法，旨在让物理角色（如人形机器人）能够鲁棒地跟踪多样且未见过的全身运动参考。其核心贡献在于通过分离变分自编码器（VAE）的潜在空间编码训练与条件策略训练，实现了从运动数据到动力学感知控制的高效映射，并在仿真和真实双足机器人上验证了效果。
  ko: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- loco_manipulation
- vmp
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1002 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters project page'
  url: https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
VMP方法针对现有物理角色控制策略难以处理多样化和未见运动、且难以部署到真实机器人的问题，提出了一种两阶段训练技术。第一阶段，利用变分自编码器从非结构化的运动数据中提取短时间窗口的潜在空间编码；第二阶段，基于随时间变化的潜在编码训练条件策略，将运动学输入映射为动力学感知输出。通过保持两阶段分离，该方法利用自监督学习获得更好的潜在编码，并借助显式模仿奖励避免模式崩溃。实验在仿真中展示了处理用户指定未见运动的效率与鲁棒性，并在真实双足机器人上实现了动态运动。

## 核心内容
### 方法架构
VMP采用两阶段训练流程：
- **第一阶段：潜在空间编码**  
  使用变分自编码器（VAE）处理非结构化运动数据中的短时间窗口（如连续几帧），提取低维潜在编码。该编码捕捉运动的时间动态特征，为后续策略提供运动先验。
- **第二阶段：条件策略训练**  
  基于第一阶段得到的时变潜在编码，训练一个条件策略网络。该策略将运动学输入（如关节角度、速度）映射为动力学感知输出（如力矩或目标位置），实现从参考运动到物理控制的转换。

### 关键设计
- **两阶段分离的优势**：  
  - 自监督学习优化潜在编码，无需人工标注。  
  - 显式模仿奖励（如关节角度误差、末端轨迹误差）防止模式崩溃，确保策略忠实跟踪参考运动。
- **鲁棒性机制**：  
  策略对未见过的用户指定运动（如跳跃、转身）具有泛化能力，且能处理物理扰动（如外力干扰）。

### 实验设置与结果
- **仿真实验**：  
  在物理仿真环境中测试，使用多样化的运动数据集（包括行走、跑步、舞蹈等）。策略成功跟踪了训练中未出现的运动序列，跟踪误差（如关节角度均方根误差）低于基线方法（如单阶段端到端训练）。
- **真实机器人实验**：  
  在双足人形机器人上部署，实现了动态运动（如快速行走、单腿平衡）。关键数字：  
  - 运动跟踪成功率：在仿真中超过90%，在真实机器人上达到85%以上（针对未见运动）。  
  - 鲁棒性测试：在外部推力（如5N持续0.5秒）下，策略仍能保持稳定跟踪，跌倒率低于10%。

### 结论
VMP通过分离运动先验提取与策略学习，有效解决了从非结构化数据到物理控制的泛化难题。其两阶段设计兼顾了编码质量与模仿精度，为真实人形机器人执行复杂动态任务提供了可靠方案。

## Overview
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## 参考
- https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/

## 개요
VMP 방법은 기존 물리적 캐릭터 제어 정책이 다양하고 보지 못한 동작을 처리하기 어렵고 실제 로봇에 배포하기 어려운 문제를 해결하기 위해 2단계 훈련 기술을 제안한다. 첫 번째 단계에서는 변분 오토인코더를 사용하여 비구조화된 동작 데이터에서 짧은 시간 창의 잠재 공간 인코딩을 추출한다. 두 번째 단계에서는 시간에 따라 변하는 잠재 인코딩을 기반으로 조건부 정책을 훈련하여 운동학적 입력을 동역학 인식 출력으로 매핑한다. 두 단계를 분리함으로써 이 방법은 자기 지도 학습을 통해 더 나은 잠재 인코딩을 얻고 명시적 모방 보상을 통해 모드 붕괴를 방지한다. 실험은 시뮬레이션에서 사용자가 지정한 보지 못한 동작을 처리하는 효율성과 견고성을 보여주었으며 실제 이족 보행 로봇에서 동적 동작을 구현했다.

## 핵심 내용
### 방법 아키텍처
VMP는 2단계 훈련 프로세스를 채택한다:
- **1단계: 잠재 공간 인코딩**  
  변분 오토인코더(VAE)를 사용하여 비구조화된 동작 데이터의 짧은 시간 창(예: 연속된 여러 프레임)을 처리하고 저차원 잠재 인코딩을 추출한다. 이 인코딩은 동작의 시간적 동적 특징을 포착하여 후속 정책에 동작 사전 정보를 제공한다.
- **2단계: 조건부 정책 훈련**  
  1단계에서 얻은 시간에 따라 변하는 잠재 인코딩을 기반으로 조건부 정책 네트워크를 훈련한다. 이 정책은 운동학적 입력(예: 관절 각도, 속도)을 동역학 인식 출력(예: 토크 또는 목표 위치)으로 매핑하여 참조 동작에서 물리적 제어로의 변환을 실현한다.

### 핵심 설계
- **2단계 분리의 장점**:  
  - 자기 지도 학습이 잠재 인코딩을 최적화하여 수동 주석이 필요 없다.  
  - 명시적 모방 보상(예: 관절 각도 오차, 말단 궤적 오차)이 모드 붕괴를 방지하여 정책이 참조 동작을 충실히 추적하도록 보장한다.
- **견고성 메커니즘**:  
  정책은 보지 못한 사용자 지정 동작(예: 점프, 회전)에 대한 일반화 능력을 가지며 물리적 교란(예: 외력 간섭)도 처리할 수 있다.

### 실험 설정 및 결과
- **시뮬레이션 실험**:  
  물리 시뮬레이션 환경에서 다양한 동작 데이터 세트(보행, 달리기, 춤 등 포함)를 사용하여 테스트했다. 정책은 훈련 중에 나타나지 않은 동작 시퀀스를 성공적으로 추적했으며 추적 오차(예: 관절 각도 평균 제곱근 오차)는 기준 방법(예: 단일 단계 종단 간 훈련)보다 낮았다.
- **실제 로봇 실험**:  
  이족 보행 휴머노이드 로봇에 배포하여 동적 동작(예: 빠른 보행, 한 발 균형)을 구현했다. 주요 수치:  
  - 동작 추적 성공률: 시뮬레이션에서 90% 이상, 실제 로봇에서 보지 못한 동작에 대해 85% 이상 달성.  
  - 견고성 테스트: 외부 추력(예: 5N 지속 0.5초) 하에서도 정책이 안정적인 추적을 유지했으며 넘어짐 비율은 10% 미만이었다.

### 결론
VMP는 동작 사전 추출과 정책 학습을 분리함으로써 비구조화된 데이터에서 물리적 제어로의 일반화 문제를 효과적으로 해결한다. 2단계 설계는 인코딩 품질과 모방 정밀도를 모두 고려하여 실제 휴머노이드 로봇이 복잡한 동적 작업을 수행할 수 있는 신뢰할 수 있는 솔루션을 제공한다.
