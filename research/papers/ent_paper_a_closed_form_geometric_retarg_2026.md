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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01632v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
인간의 동작을 로봇 자세로 재타겟팅하는 것은 양팔 휴머노이드 로봇 팔을 원격 조작하는 실용적인 접근 방식이지만, 기존 방법은 종종 차선책이거나 느려 바람직하지 않은 움직임이나 지연을 초래할 수 있습니다. 이는 로봇의 엔드 이펙터를 인간 손의 위치와 방향에 맞추기 위해 최적화하기 때문이며, 이는 로봇의 작업 공간을 인간의 작업 공간으로 제한할 수도 있습니다. 대신, 본 논문은 재타겟팅을 방향 정렬 문제로 재정의하여 최적성이 보장된 폐쇄형 기하학적 해법 알고리즘을 가능하게 합니다. 핵심 아이디어는 어깨, 팔꿈치, 손목(SEW) 키포인트에서 식별된 인간의 상완 및 하완 방향에 로봇 팔을 정렬하는 것이며, 따라서 이 방법을 SEW-Mimic이라고 명명했습니다. 이 방법은 표준 상용 CPU에서 빠른 추론(3kHz)을 제공하여 다운스트림 애플리케이션을 위한 계산 오버헤드를 남깁니다. 본 논문의 예시로는 양팔 자체 충돌을 방지하기 위한 안전 필터가 있습니다. 이 방법은 대부분의 7자유도 로봇 팔과 휴머노이드에 적합하며, 입력 키포인트 소스에 구애받지 않습니다. 실험 결과 SEW-Mimic이 계산 시간과 정확도에서 다른 재타겟팅 방법보다 우수함을 보여줍니다. 파일럿 사용자 연구는 이 방법이 원격 조작 작업 성공률을 향상시킨다는 것을 시사합니다. 예비 분석에 따르면 SEW-Mimic으로 수집된 데이터가 더 부드러워 정책 학습을 개선합니다. 또한 SEW-Mimic은 전신 휴머노이드 재타겟팅을 가속화하는 드롭인 방식으로도 입증되었습니다. 마지막으로, 하드웨어 데모를 통해 SEW-Mimic의 실용성을 보여줍니다. 결과는 양팔 로봇 조작 및 휴머노이드 로봇 원격 조작을 위한 기본 구성 요소로서 SEW-Mimic의 유용성을 강조합니다.

## 핵심 내용
인간의 동작을 로봇 자세로 재타겟팅하는 것은 양팔 휴머노이드 로봇 팔을 원격 조작하는 실용적인 접근 방식이지만, 기존 방법은 종종 차선책이거나 느려 바람직하지 않은 움직임이나 지연을 초래할 수 있습니다. 이는 로봇의 엔드 이펙터를 인간 손의 위치와 방향에 맞추기 위해 최적화하기 때문이며, 이는 로봇의 작업 공간을 인간의 작업 공간으로 제한할 수도 있습니다. 대신, 본 논문은 재타겟팅을 방향 정렬 문제로 재정의하여 최적성이 보장된 폐쇄형 기하학적 해법 알고리즘을 가능하게 합니다. 핵심 아이디어는 어깨, 팔꿈치, 손목(SEW) 키포인트에서 식별된 인간의 상완 및 하완 방향에 로봇 팔을 정렬하는 것이며, 따라서 이 방법을 SEW-Mimic이라고 명명했습니다. 이 방법은 표준 상용 CPU에서 빠른 추론(3kHz)을 제공하여 다운스트림 애플리케이션을 위한 계산 오버헤드를 남깁니다. 본 논문의 예시로는 양팔 자체 충돌을 방지하기 위한 안전 필터가 있습니다. 이 방법은 대부분의 7자유도 로봇 팔과 휴머노이드에 적합하며, 입력 키포인트 소스에 구애받지 않습니다. 실험 결과 SEW-Mimic이 계산 시간과 정확도에서 다른 재타겟팅 방법보다 우수함을 보여줍니다. 파일럿 사용자 연구는 이 방법이 원격 조작 작업 성공률을 향상시킨다는 것을 시사합니다. 예비 분석에 따르면 SEW-Mimic으로 수집된 데이터가 더 부드러워 정책 학습을 개선합니다. 또한 SEW-Mimic은 전신 휴머노이드 재타겟팅을 가속화하는 드롭인 방식으로도 입증되었습니다. 마지막으로, 하드웨어 데모를 통해 SEW-Mimic의 실용성을 보여줍니다. 결과는 양팔 로봇 조작 및 휴머노이드 로봇 원격 조작을 위한 기본 구성 요소로서 SEW-Mimic의 유용성을 강조합니다.

## 参考
- http://arxiv.org/abs/2602.01632v1
