---
$id: ent_principle_current_velocity_position_loops
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Current / Velocity / Position Control Loops
  zh: 电流环/速度环/位置环
  ko: 전류·속도·위치 제어 루프
summary:
  en: The nested feedback-control hierarchy for servo drives, where an inner current loop regulates torque, a velocity loop
    regulates speed, and an outer position loop regulates joint angle.
  zh: 4.5.5 电流环、速度环、位置环的级联控制 实际关节驱动通常采用三级级联控制：最内层 电流环（力矩环），中间 速度环，最外层 位置环。每一层带宽约为下一层的 5-10 倍，以保证稳定性。
  ko: '서보 드라이브의 중첩 피드백 제어 계층: 내측 전류 루프는 토크, 속도 루프는 속도, 외측 위치 루프는 관절 각도를 제어.'
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- principle
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.5.5 电流环、速度环、位置环的级联控制 by scripts/backfill_nonpaper_entries.py. Body backfilled
    from chapter-04.md section '4.5.5 电流环、速度环、位置环的级联控制' by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
伺服驱动的级联反馈控制层级：内环电流环控制转矩，中间速度环控制转速，外环位置环控制关节角度。

## 核心内容
### 4.5.5 电流环、速度环、位置环的级联控制
实际关节驱动通常采用三级级联控制：最内层 **电流环**（力矩环），中间 **速度环**，最外层 **位置环**。每一层带宽约为下一层的 5-10 倍，以保证稳定性。

!!! note "术语解释：电流环、速度环、位置环、PI 控制器、前馈、抗饱和、带宽级联"
    - **电流环（current loop）**：以电机相电流为被控量的最快内环，直接决定输出力矩。
    - **速度环（velocity loop）**：以电机转速为被控量，输出电流指令。
    - **位置环（position loop）**：以关节角度为被控量，输出速度指令。
    - **PI 控制器（proportional-integral controller）**：由比例项和积分项组成的经典控制器，用于消除稳态误差。
    - **前馈（feedforward）**：根据期望轨迹提前计算并加入控制量，提高跟踪性能。
    - **抗饱和（anti-windup）**：防止积分器在饱和时过度累积，避免退出饱和后的大超调。
    - **带宽级联（bandwidth cascade）**：内环带宽远高于外环，确保外环指令能被内环快速跟踪。

电流环带宽通常可达 1-5 kHz；速度环 50-500 Hz；位置环 5-100 Hz，具体取决于负载惯量、刚度和采样率。

### 在人形机器人关节控制中的重要性
人形机器人关节通常需要同时实现高动态响应和精确的位置跟踪。三级级联控制通过分层带宽设计，使内环快速抑制电流扰动、中环保证速度平滑、外环实现轨迹跟踪，是多自由度人形机器人稳定运动的基础。合理整定三环参数并加入前馈与抗饱和机制，可以显著提升行走、操作和碰撞恢复能力。

## 参考
- 项目 Wiki：wiki/docs/chapters/chapter-04.md 第「4.5.5 电流环、速度环、位置环的级联控制」节
- Wiki extraction

电流环/速度环/位置环作为人形机器人产业链中的关键组成部分，其相关理论与工程实践仍在持续发展。深入理解其原理、边界条件与典型应用场景，对于将实验室样机转化为可量产产品具有重要意义。

## Overview
The cascaded feedback control hierarchy of servo drives: the inner current loop controls torque, the intermediate velocity loop controls rotational speed, and the outer position loop controls joint angle.

## Content
### 4.5.5 Cascaded Control of Current Loop, Velocity Loop, and Position Loop
Practical joint drives typically employ a three-level cascaded control structure: the innermost **current loop** (torque loop), the intermediate **velocity loop**, and the outermost **position loop**. The bandwidth of each layer is approximately 5-10 times that of the next layer to ensure stability.

!!! note "Terminology Explanation: Current Loop, Velocity Loop, Position Loop, PI Controller, Feedforward, Anti-Windup, Bandwidth Cascade"
    - **Current loop**: The fastest inner loop that controls the motor phase current, directly determining the output torque.
    - **Velocity loop**: Controls the motor speed as the controlled variable, outputting the current command.
    - **Position loop**: Controls the joint angle as the controlled variable, outputting the velocity command.
    - **PI controller (proportional-integral controller)**: A classic controller consisting of a proportional term and an integral term, used to eliminate steady-state error.
    - **Feedforward**: Pre-calculates and adds a control quantity based on the desired trajectory to improve tracking performance.
    - **Anti-windup**: Prevents the integrator from excessive accumulation during saturation, avoiding large overshoot after exiting saturation.
    - **Bandwidth cascade**: The inner loop bandwidth is significantly higher than that of the outer loop, ensuring that the outer loop commands can be quickly tracked by the inner loop.

The bandwidth of the current loop can typically reach 1-5 kHz; the velocity loop 50-500 Hz; and the position loop 5-100 Hz, depending on load inertia, stiffness, and sampling rate.

### Importance in Humanoid Robot Joint Control
Humanoid robot joints typically require both high dynamic response and precise position tracking. The three-level cascaded control, through hierarchical bandwidth design, enables the inner loop to quickly suppress current disturbances, the intermediate loop to ensure smooth velocity, and the outer loop to achieve trajectory tracking. This forms the foundation for stable motion in multi-degree-of-freedom humanoid robots. Properly tuning the parameters of the three loops and incorporating feedforward and anti-windup mechanisms can significantly enhance walking, manipulation, and collision recovery capabilities.

## 개요
서보 드라이브의 캐스케이드 피드백 제어 계층: 내부 전류 루프는 토크를 제어하고, 중간 속도 루프는 회전 속도를 제어하며, 외부 위치 루프는 관절 각도를 제어합니다.

## 핵심 내용
### 4.5.5 전류 루프, 속도 루프, 위치 루프의 캐스케이드 제어
실제 관절 구동은 일반적으로 3단계 캐스케이드 제어를 사용합니다: 최내층 **전류 루프**(토크 루프), 중간 **속도 루프**, 최외층 **위치 루프**. 각 계층의 대역폭은 안정성을 보장하기 위해 다음 계층의 약 5-10배입니다.

!!! note "용어 설명: 전류 루프, 속도 루프, 위치 루프, PI 제어기, 피드포워드, 안티와인드업, 대역폭 캐스케이드"
    - **전류 루프(current loop)**: 모터 상전류를 제어 대상으로 하는 가장 빠른 내부 루프로, 출력 토크를 직접 결정합니다.
    - **속도 루프(velocity loop)**: 모터 회전 속도를 제어 대상으로 하며, 전류 명령을 출력합니다.
    - **위치 루프(position loop)**: 관절 각도를 제어 대상으로 하며, 속도 명령을 출력합니다.
    - **PI 제어기(proportional-integral controller)**: 비례항과 적분항으로 구성된 고전적인 제어기로, 정상 상태 오차를 제거하는 데 사용됩니다.
    - **피드포워드(feedforward)**: 예상 궤적에 따라 제어량을 미리 계산하여 추가함으로써 추종 성능을 향상시킵니다.
    - **안티와인드업(anti-windup)**: 포화 상태에서 적분기가 과도하게 누적되는 것을 방지하여, 포화 해제 후 큰 오버슈트를 피합니다.
    - **대역폭 캐스케이드(bandwidth cascade)**: 내부 루프의 대역폭이 외부 루프보다 훨씬 높아, 외부 루프 명령이 내부 루프에 의해 빠르게 추종되도록 보장합니다.

전류 루프의 대역폭은 일반적으로 1-5 kHz에 도달할 수 있으며, 속도 루프는 50-500 Hz, 위치 루프는 5-100 Hz입니다. 구체적인 값은 부하 관성, 강성 및 샘플링 속도에 따라 달라집니다.

### 휴머노이드 로봇 관절 제어에서의 중요성
휴머노이드 로봇의 관절은 일반적으로 높은 동적 응답과 정밀한 위치 추종을 동시에 실현해야 합니다. 3단계 캐스케이드 제어는 계층적 대역폭 설계를 통해 내부 루프가 전류 교란을 빠르게 억제하고, 중간 루프가 속도 평활성을 보장하며, 외부 루프가 궤적 추종을 실현하도록 합니다. 이는 다자유도 휴머노이드 로봇의 안정적인 움직임의 기초입니다. 세 루프의 파라미터를 적절히 조정하고 피드포워드 및 안티와인드업 메커니즘을 추가하면 보행, 조작 및 충돌 회복 능력을 크게 향상시킬 수 있습니다.
