---
$id: ent_paper_a_closed_form_geometric_retarg_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
  zh: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
  ko: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
summary:
  en: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation is a 2026 work on teleoperation
    for humanoid robots.
  zh: SEW-Mimic 是一种用于上半身人形机器人遥操作的闭式几何重定向求解器，由研究团队于2026年提出。其核心贡献在于将重定向问题重构为方向对齐问题，通过肩、肘、腕关键点实现闭式几何求解，推理速度达3 kHz，并具备最优性保证。
  ko: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation is a 2026 work on teleoperation
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_closed_form_geometric_retarg
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01632v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (706 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation (arXiv)
  url: https://arxiv.org/abs/2602.01632
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有将人体运动重定向到机器人姿态的方法通常优化末端执行器位置与方向，导致次优解、延迟高且限制机器人工作空间。SEW-Mimic 通过将问题简化为方向对齐，利用人体肩、肘、腕关键点计算闭式几何解，显著提升速度与精度。该方法兼容多数7自由度机械臂与人形机器人，且不依赖特定关键点输入源。实验表明其在计算时间与准确性上优于现有方法，用户研究证实其能提高遥操作任务成功率，并因数据更平滑而有利于策略学习。

## 核心内容
### 方法核心
- **问题重构**：将传统基于末端执行器位置/方向匹配的优化问题，转化为机器人上臂与前臂方向与人体对应肢体对齐的闭式几何求解。
- **关键点利用**：仅需人体肩、肘、腕（SEW）三个关键点，即可推导出机器人关节角度的解析解，无需迭代优化。
- **算法特性**：闭式解保证最优性，推理速度达3 kHz（标准商用CPU），为下游应用（如安全滤波器）预留计算资源。

### 实验设置与结果
- **性能对比**：在计算时间与重定向精度上，SEW-Mimic 显著优于现有方法（如基于逆运动学的优化方法）。
- **用户研究**：初步实验表明，使用 SEW-Mimic 的遥操作任务成功率更高，操作更自然。
- **数据质量**：收集的运动数据更平滑，有利于后续模仿学习策略的训练。
- **扩展性**：可作为即插即用模块加速全身人形机器人重定向，硬件演示验证其实用性。

### 结论
SEW-Mimic 作为双机械臂操作与人形机器人遥操作的基础组件，通过高效、精确的方向对齐重定向，解决了现有方法的延迟与工作空间限制问题，为实时遥操作与机器人学习提供了可靠支撑。

## Overview
Retargeting human motion to robot poses is a practical approach for teleoperating bimanual humanoid robot arms, but existing methods can be suboptimal and slow, often causing undesirable motion or latency. This is due to optimizing to match robot end-effector to human hand position and orientation, which can also limit the robot's workspace to that of the human. Instead, this paper reframes retargeting as an orientation alignment problem, enabling a closed-form, geometric solution algorithm with an optimality guarantee. The key idea is to align a robot arm to a human's upper and lower arm orientations, as identified from shoulder, elbow, and wrist (SEW) keypoints; hence, the method is called SEW-Mimic. The method has fast inference (3 kHz) on standard commercial CPUs, leaving computational overhead for downstream applications; an example in this paper is a safety filter to avoid bimanual self-collision. The method suits most 7-degree-of-freedom robot arms and humanoids, and is agnostic to input keypoint source. Experiments show that SEW-Mimic outperforms other retargeting methods in computation time and accuracy. A pilot user study suggests that the method improves teleoperation task success. Preliminary analysis indicates that data collected with SEW-Mimic improves policy learning due to being smoother. SEW-Mimic is also shown to be a drop-in way to accelerate full-body humanoid retargeting. Finally, hardware demonstrations illustrate SEW-Mimic's practicality. The results emphasize the utility of SEW-Mimic as a fundamental building block for bimanual robot manipulation and humanoid robot teleoperation.

## 参考
- http://arxiv.org/abs/2602.01632v1

## 개요
기존의 인간 동작을 로봇 자세로 재지정(리타게팅)하는 방법은 일반적으로 말단 실행기(end-effector)의 위치와 방향을 최적화하여 차선의 해, 높은 지연 시간, 제한된 로봇 작업 공간을 초래합니다. SEW-Mimic은 문제를 방향 정렬로 단순화하고, 인간의 어깨, 팔꿈치, 손목 키포인트를 활용하여 폐쇄형 기하 해를 계산함으로써 속도와 정확성을 크게 향상시킵니다. 이 방법은 대부분의 7자유도 로봇 팔과 휴머노이드 로봇과 호환되며, 특정 키포인트 입력 소스에 의존하지 않습니다. 실험 결과, 계산 시간과 정확성에서 기존 방법보다 우수하며, 사용자 연구를 통해 원격 조작 작업 성공률을 높이고, 더 매끄러운 데이터로 인해 정책 학습에 유리함을 확인했습니다.

## 핵심 내용
### 방법 핵심
- **문제 재구성**: 기존의 말단 실행기 위치/방향 매칭 기반 최적화 문제를, 로봇의 상완과 전완 방향을 인간의 해당 사지와 정렬하는 폐쇄형 기하 해법으로 변환합니다.
- **키포인트 활용**: 인간의 어깨, 팔꿈치, 손목(SEW) 세 개의 키포인트만으로 로봇 관절 각도의 해석적 해를 도출하며, 반복 최적화가 필요 없습니다.
- **알고리즘 특성**: 폐쇄형 해는 최적성을 보장하며, 추론 속도는 3kHz(표준 상용 CPU)로, 하위 응용 프로그램(예: 안전 필터)에 계산 리소스를 예약합니다.

### 실험 설정 및 결과
- **성능 비교**: 계산 시간과 재지정 정확성에서 SEW-Mimic은 기존 방법(예: 역기구학 기반 최적화 방법)보다 크게 우수합니다.
- **사용자 연구**: 예비 실험에서 SEW-Mimic을 사용한 원격 조작 작업의 성공률이 더 높고, 조작이 더 자연스러운 것으로 나타났습니다.
- **데이터 품질**: 수집된 동작 데이터가 더 매끄러워, 이후 모방 학습 정책 훈련에 유리합니다.
- **확장성**: 플러그 앤 플레이 모듈로 사용되어 전신 휴머노이드 로봇 재지정을 가속화할 수 있으며, 하드웨어 데모를 통해 실용성을 검증했습니다.

### 결론
SEW-Mimic은 이중 로봇 팔 조작 및 휴머노이드 로봇 원격 조작의 기본 구성 요소로서, 효율적이고 정확한 방향 정렬 재지정을 통해 기존 방법의 지연 시간과 작업 공간 제한 문제를 해결하며, 실시간 원격 조작과 로봇 학습에 신뢰할 수 있는 지원을 제공합니다.
