---
$id: ent_paper_unitree_h1_humanoid_robot_whit_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unitree H1 Humanoid Robot Whitepaper & Specifications
  zh: Unitree H1 Humanoid Robot Whitepaper & Specifications
  ko: Unitree H1 Humanoid Robot Whitepaper & Specifications
summary:
  en: This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite
    RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body
    actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving
    average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization
    enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive
    locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate
    72 ms end-to-end latency, 3.38° joint error, and 95% gesture recogn
  zh: 本文提出基于Unitree H1人形机器人的视觉驱动人体动作模仿系统。系统通过前置OAK-Lite RGB-D相机实时捕捉上肢动作，结合级联卡尔曼与加权移动平均滤波器提升深度关键点稳定性，并采用带速度约束的温启动符号逆运动学求解器实现8自由度手臂控制。实验显示端到端延迟72毫秒、关节误差3.38°、下肢手势识别准确率95%。
  ko: Unitree H1 Humanoid Robot Whitepaper & Specifications is a paper on 硬件设计 for humanoid robotics.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- unitree_h1_humanoid_robot_whit
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Unitree H1 Humanoid Robot
    Whitepaper & Specifications. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (691 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Unitree H1 Humanoid Robot Whitepaper & Specifications
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该系统在机器人前方约1.2米处安装OAK-Lite RGB-D相机，实时捕捉人体运动并复现上肢动作。为抑制深度关键点抖动，研究者设计了级联卡尔曼与加权移动平均滤波器。手臂控制采用温启动符号逆运动学求解器，通过速度边界优化在12-18毫秒内完成8自由度稳定控制。下肢部分通过有限状态机手势识别器提供直观的移动指令，形成完整全身模仿框架。在Unitree H1机器人上的实验验证了系统流畅且响应迅速的模仿性能。

## 核心内容
### 系统架构
- **感知模块**：前置OAK-Lite RGB-D相机（安装高度约1.2米）实时捕获人体RGB-D数据
- **滤波处理**：级联卡尔曼滤波器与加权移动平均滤波器组合，有效抑制深度关键点抖动
- **运动控制**：
  - 温启动符号逆运动学求解器（warm-start symbolic IK solver）
  - 速度边界优化（velocity-bounded optimization）确保运动平滑
  - 8自由度（8-DoF）手臂控制周期12-18毫秒
- **下肢控制**：基于有限状态机（finite-state machine）的手势识别器，输出直观的移动指令

### 实验设置
- **机器人平台**：Unitree H1人形机器人
- **性能指标**：
  - 端到端延迟：72毫秒
  - 关节角度误差：3.38°
  - 手势识别准确率：95%

### 结论
该系统通过视觉感知与运动控制的协同设计，实现了人形机器人对复杂人体动作的实时模仿，验证了在延迟、精度和识别可靠性方面的综合有效性。

## Overview
This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate 72 ms end-to-end latency, 3.38° joint error, and 95% gesture recognition accuracy, validating the system’s smooth and responsive imitation performance.

## 参考
- Semantic Scholar search: Unitree H1 Humanoid Robot Whitepaper & Specifications

## 개요
이 시스템은 로봇 전방 약 1.2m 지점에 OAK-Lite RGB-D 카메라를 설치하여 실시간으로 인체 동작을 캡처하고 상지 동작을 재현합니다. 깊이 키포인트의 떨림을 억제하기 위해 연구자들은 캐스케이드 칼만 필터와 가중 이동 평균 필터를 설계했습니다. 팔 제어는 웜 스타트 기호 역운동학 솔버를 사용하며, 속도 경계 최적화를 통해 12-18밀리초 내에 8자유도 안정 제어를 완료합니다. 하지 부분은 유한 상태 머신 기반 제스처 인식기를 통해 직관적인 이동 명령을 제공하여 완전한 전신 모방 프레임워크를 구성합니다. Unitree H1 로봇에서의 실험은 시스템의 유연하고 빠른 모방 성능을 검증했습니다.

## 핵심 내용
### 시스템 아키텍처
- **인식 모듈**: 전방 OAK-Lite RGB-D 카메라(설치 높이 약 1.2m)가 실시간으로 인체 RGB-D 데이터를 캡처
- **필터링 처리**: 캐스케이드 칼만 필터와 가중 이동 평균 필터의 조합으로 깊이 키포인트 떨림을 효과적으로 억제
- **운동 제어**:
  - 웜 스타트 기호 역운동학 솔버(warm-start symbolic IK solver)
  - 속도 경계 최적화(velocity-bounded optimization)로 운동 평활성 보장
  - 8자유도(8-DoF) 팔 제어 주기 12-18밀리초
- **하지 제어**: 유한 상태 머신(finite-state machine) 기반 제스처 인식기로 직관적인 이동 명령 출력

### 실험 설정
- **로봇 플랫폼**: Unitree H1 휴머노이드 로봇
- **성능 지표**:
  - 엔드투엔드 지연 시간: 72밀리초
  - 관절 각도 오차: 3.38°
  - 제스처 인식 정확도: 95%

### 결론
이 시스템은 시각 인식과 운동 제어의 협력 설계를 통해 휴머노이드 로봇이 복잡한 인체 동작을 실시간으로 모방할 수 있게 하였으며, 지연 시간, 정밀도, 인식 신뢰성 측면에서 종합적인 효과를 검증했습니다.
