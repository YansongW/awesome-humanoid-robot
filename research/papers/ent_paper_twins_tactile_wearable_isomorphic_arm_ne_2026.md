---
$id: ent_paper_twins_tactile_wearable_isomorphic_arm_ne_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TWINS: A Tactile Wearable Isomorphic Arm Networked System for Contact-Rich Manipulation Learning'
  zh: 'TWINS: A Tactile Wearable Isomorphic Arm Networked System for Contact-Rich Manipulation Learning'
  ko: 'TWINS: A Tactile Wearable Isomorphic Arm Networked System for Contact-Rich Manipulation Learning'
summary:
  en: Recent advances in robot learning for manipulation have increased the importance of collecting real-world demonstration
    data. However, existing robotic systems primarily focus on end-effector manipulation, making it difficult to teach and
    execute manipulation tasks involving body-surface contact with the arms and chest. This paper presents TWINS (Tactile
    Wearable Isomorphic Arm Networked System),.
  zh: TWINS 是一套由操作者穿戴的双臂装置与同构机器人组成的遥操作系统，用于采集和复现涉及身体表面接触（前臂、上臂、胸部等）的操作演示，并支持基于 Diffusion Policy 的模仿学习。系统通过共享关节配置与连杆长度实现无重定向的关节角度映射，并以
    219 个触觉单元同时记录压力与接近度，为接触丰富的操作任务提供显式观测。核心贡献在于首次将「具身操作」「形态对应」「身体表面接触」三个特性统一到单一平台，并验证了其采集数据可支撑接触相关技能的习得。
  ko: Recent advances in robot learning for manipulation have increased the importance of collecting real-world demonstration
    data. However, existing robotic systems primarily focus on end-effector manipulation, making it difficult to teach and
    execute manipulation tasks involving body-surface contact with the arms and chest. This paper presents TWINS (Tactile
    Wearable Isomorphic Arm Networked System),.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- twins
- tactile
- wearable
- isomorphic
- arm
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.01733 TWINS: A Tactile Wearable Isomorphic Arm Networked System for Contact-Rich Manip'
  url: https://arxiv.org/abs/2608.01733
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

TWINS 是一套由操作者穿戴的双臂装置与同构机器人组成的遥操作系统，用于采集和复现涉及身体表面接触（前臂、上臂、胸部等）的操作演示，并支持基于 Diffusion Policy 的模仿学习。系统通过共享关节配置与连杆长度实现无重定向的关节角度映射，并以 219 个触觉单元同时记录压力与接近度，为接触丰富的操作任务提供显式观测。核心贡献在于首次将「具身操作」「形态对应」「身体表面接触」三个特性统一到单一平台，并验证了其采集数据可支撑接触相关技能的习得。

## 它改变了什么

现有机器人学习系统几乎全部围绕末端执行器设计，身体表面接触（如用前臂托物、用胸部抵住物体）在人类操作中普遍存在，却因缺乏显式接触观测而无法被有效建模。视觉难以准确估计接触力与接触位置，而传统遥操作接口（Leader–Follower、VR、动作捕捉+触觉服）要么只传递末端位姿，要么因身体尺寸或关节配置不匹配而需要额外映射，均无法让操作者以与机器人等效的机构进行物理交互。TWINS 改变了这一局面：它不再把身体表面接触当作视觉的附属信息，而是将其作为与关节角度同等重要的状态变量纳入学习框架，从而扩展了可学习的操作技能边界——从「抓取与放置」延伸到「用身体抵住、托举、夹持」等接触密集行为。

## 方法拆解

### 系统架构
TWINS 由操作者穿戴的 Wearable Dual-Arm Device 与关节配置、外部尺寸完全一致的 Isomorphic Robot 组成。操作者手臂插入可穿戴装置的空心外壳中，通过外壳与物体交互，避免直接物理接触；肩部支撑结构固定在椅子上以承载装置重量。

### 机械设计
- 每条手臂 7 自由度：肩部 3、肘部 1、腕部 3，基于 HRP2Kai 的关节配置而非忠实复现人类上肢全部运动范围。
- 连杆长度按典型成人上肢尺寸确定；肩宽与肩高设独立手动调节机构。
- 末端执行器为基于 UMI 设计的平行两指 Fin Ray 结构夹爪。
- 每个关节配备 10 位编码器测量关节角度。
- 同构机器人采用 DYNAMIXEL 伺服电机（XM430、XM540、PH54-100-S500），高扭矩型号用于肩部等大弯矩关节，轻量型号用于腕部等远端关节；大部分外壳与连杆为 3D 打印。

### 触觉传感
- 使用 Intouch Robotics 的 e-Skin，六边形单元边长 15 mm、厚度约 5 mm，可同时测量压力与接近度。
- 传感器布局：每臂夹爪上表面 15 单元、前臂内表面 45 单元、上臂前表面 18 单元，胸部 63 单元，共 219 个单元，左右对称。
- 传感器贴片可拆卸，安装在可穿戴装置外壳上，与同构机器人布局一致；数据以 10 Hz 采集，每个身体区域的触觉信息表示为空间分布而非单点接触。

### 数据采集与执行
- 状态定义为 x(t) = {q(t), S(t)}，其中 q(t) 为关节角度，S(t) 为所有触觉单元的压力与接近度测量值。
- 演示记录为时间序列 D = {x(t)}，t=0 到 T。
- 关节角度直接映射 q_R(t) = q_W(t)，无需重定向，因为两系统共享相同关节配置与连杆长度。

### 模仿学习
- 采用 Diffusion Policy，状态历史长度 2，动作预测视界 8。
- 关节角度与触觉测量独立归一化到 [−1, 1]；触觉输入采用所有单元整体归一化，作者指出比逐单元归一化训练更稳定。
- 数据采集、训练与部署使用开源框架 RoboManipBaselines。

## 关键创新

1. **无重定向的形态对应**：通过让可穿戴装置与机器人共享完全相同的关节配置与连杆长度，TWINS 消除了传统遥操作中的人体到机器人运动映射，关节角度可直接传递。这不仅简化了数据采集流程，还保证了操作者身体表面接触的位置与机器人接触位置在空间上严格对应，这是此前系统未同时满足的关键特性。
2. **接近度与压力联合观测**：e-Skin 同时测量压力与接近度，使系统能在物理接触前观测物体距离，连续捕获从接近到分离的完整接触过程。这为模仿学习提供了比单纯接触力更丰富的时间演化信息，对涉及「先靠近再抵住」这类接触阶段转换的任务至关重要。
3. **身体表面接触作为一等状态**：将 219 个触觉单元的分布信息纳入状态空间，而非仅作为末端执行器的补充信号。这使得策略能够显式利用身体不同区域的接触事件来切换操作阶段，突破了传统方法仅依赖视觉或末端力传感的局限。

## 实验与结果

实验覆盖四个涉及身体表面接触的任务：Towel Hanging（毛巾悬挂）、Basket Holding（篮子抱持）、Ball Placing（球放置）、Adaptive Holding（自适应抱持）。每个任务采集 10 个演示，共 40 个演示，全部由单一操作者在 30 分钟内完成，无需专门训练。

| 指标 | 数值 |
|------|------|
| 关节角度跟踪平均绝对误差 | 0.94 deg（14 个手臂关节） |
| 关节角度跟踪 95 百分位误差 | 3.43 deg |
| 跟踪延迟 | 约 0.4–0.6 s |
| 触觉输入维度 | 438（219 单元 × 压力+接近度） |
| 关节角度输入维度 | 16（左右臂+夹爪） |

策略在所有任务中均能根据身体表面接触事件成功转换操作阶段。对演示中未包含的情况表现出鲁棒性：Towel Hanging 中毛巾呈现顺序反转或同时放置在双前臂时仍正确旋转对应手臂；Ball Placing 中球数量多于演示时仍能重复放置；Adaptive Holding 中物体顺序不同时仍选择正确抱持策略。涉及单臂与胸部之间抱持物体的任务偶发失败（物体掉落），附加海绵垫后大幅缓解。作者未对模仿学习算法本身进行消融评估，也未与其他基线系统做定量对比。

## 边界与局限

- 涉及单臂与胸部之间抱持物体的任务存在偶发物体掉落，海绵垫缓解但未完全解决，作者认为可能需要显式控制关节扭矩。
- 未对模仿学习算法本身进行评估，实验聚焦于验证 TWINS 采集数据能否支持接触相关操作的学习与执行。
- 未提及大规模数据采集、多操作者变体、长期稳定性测试或与其他基线系统的定量对比实验。
- 当前系统不支持移动操作（操作者在演示采集期间不可移动）；机构未纳入人类肩胛骨运动，解剖学保真度有限。
- 所有演示由单一操作者采集，未验证不同体型操作者或不同操作风格下的泛化性。

## 工程启示

复现或采用 TWINS 时，优先核对以下几点：一是关节配置与连杆长度是否严格一致，这是无重定向映射的前提，任何尺寸偏差都会破坏接触位置的对应关系；二是触觉传感器的布局与安装位置必须与机器人完全一致，且采用整体归一化而非逐单元归一化，否则训练稳定性会显著下降；三是注意跟踪延迟（约 0.4–0.6 s）对接触任务的影响，延迟可能导致接触时机偏移，必要时需在策略训练中考虑延迟补偿。最容易踩坑的地方在于抱持类任务的稳定性——若涉及单臂与胸部配合，建议预先在接触界面增加柔顺材料，并考虑显式扭矩控制而非纯位置控制。此外，数据采集时操作者需保持身体固定（肩部支撑固定在椅子上），若下游需要移动操作，需自行扩展机构与采集流程。

## Overview
Recent advances in robot learning for manipulation have increased the importance of collecting real-world demonstration data. However, existing robotic systems primarily focus on end-effector manipulation, making it difficult to teach and execute manipulation tasks involving body-surface contact with the arms and chest. This paper presents TWINS (Tactile Wearable Isomorphic Arm Networked System), a robotic system for manipulation involving body-surface contact. TWINS consists of a Wearable Dual-Arm Device, which is worn by the operator, and an Isomorphic Robot with the same joint configuration and external dimensions. Distributed tactile sensors embedded in the chest and arms enable the measurement of body-surface contact synchronized with joint motion. Using the Wearable Dual-Arm Device, we collected demonstrations for four manipulation tasks involving body-surface contact. We then trained imitation learning policies using the collected demonstrations and deployed them on the Isomorphic Robot, enabling manipulation guided by body-surface tactile observations. Experimental results demonstrate that TWINS provides a unified robotic system for demonstration, learning, and execution of manipulation involving body-surface contact. https://mmurooka.github.io/twins-project-page/

## 参考
- https://arxiv.org/abs/2608.01733

## 개요

TWINS는 작업자가 착용하는 양팔 장치와 동형 로봇으로 구성된 원격 조작 시스템으로, 신체 표면 접촉(전완, 상완, 흉부 등)을 수반하는 조작 시연을 수집하고 재현하며, Diffusion Policy 기반 모방 학습을 지원합니다. 이 시스템은 공유 관절 구성과 링크 길이를 통해 리다이렉션 없는 관절 각도 매핑을 구현하고, 219개의 촉각 유닛으로 압력과 근접도를 동시에 기록하여 접촉이 풍부한 조작 작업에 명시적 관측을 제공합니다. 핵심 기여는 '구체화된 조작', '형태 대응', '신체 표면 접촉'이라는 세 가지 특성을 단일 플랫폼에 처음으로 통합하고, 수집된 데이터가 접촉 관련 기술 습득을 지원할 수 있음을 검증한 것입니다.

## 무엇을 바꾸었는가

기존 로봇 학습 시스템은 거의 전적으로 엔드 이펙터 중심으로 설계되었으며, 신체 표면 접촉(예: 전완으로 물건을 받치기, 흉부로 물체를 고정하기)은 인간 조작에서 흔하지만 명시적 접촉 관측이 없어 효과적으로 모델링할 수 없었습니다. 시각만으로는 접촉력과 접촉 위치를 정확히 추정하기 어렵고, 기존 원격 조작 인터페이스(Leader–Follower, VR, 모션 캡처+촉각 슈트)는 엔드 이펙터 자세만 전달하거나 신체 치수나 관절 구성 불일치로 추가 매핑이 필요하여, 작업자가 로봇과 동등한 메커니즘으로 물리적 상호작용을 할 수 없었습니다. TWINS는 이러한 상황을 바꿉니다: 신체 표면 접촉을 시각의 부가 정보가 아닌 관절 각도와 동등한 상태 변수로 학습 프레임워크에 포함시켜, 학습 가능한 조작 기술의 경계를 '파지 및 배치'에서 '신체로 고정, 받치기, 집기' 등의 접촉 밀집 행동으로 확장합니다.

## 방법 분석

### 시스템 아키텍처
TWINS는 작업자가 착용하는 Wearable Dual-Arm Device와 관절 구성, 외부 치수가 완전히 동일한 Isomorphic Robot으로 구성됩니다. 작업자의 팔은 웨어러블 장치의 중공 외부 쉘에 삽입되어 쉘을 통해 물체와 상호작용하며 직접적인 물리적 접촉을 피합니다. 어깨 지지 구조는 의자에 고정되어 장치의 무게를 지탱합니다.

### 기계 설계
- 각 팔은 7자유도: 어깨 3, 팔꿈치 1, 손목 3, HRP2Kai의 관절 구성을 기반으로 하며 인간 상지의 전체 운동 범위를 충실히 재현하지는 않습니다.
- 링크 길이는 일반적인 성인 상지 치수에 따라 결정됩니다. 어깨 너비와 어깨 높이는 독립적인 수동 조절 메커니즘을 갖습니다.
- 엔드 이펙터는 UMI 기반으로 설계된 평행 2핑거 Fin Ray 구조 그리퍼입니다.
- 각 관절에는 10비트 엔코더가 장착되어 관절 각도를 측정합니다.
- 동형 로봇은 DYNAMIXEL 서보 모터(XM430, XM540, PH54-100-S500)를 사용하며, 고토크 모델은 어깨 등 큰 굽힘 모멘트 관절에, 경량 모델은 손목 등 원위 관절에 사용됩니다. 대부분의 외부 쉘과 링크는 3D 프린팅됩니다.

### 촉각 센싱
- Intouch Robotics의 e-Skin을 사용하며, 육각형 유닛 변 길이 15mm, 두께 약 5mm로 압력과 근접도를 동시에 측정할 수 있습니다.
- 센서 배치: 각 팔 그리퍼 상단 표면 15유닛, 전완 내부 표면 45유닛, 상완 전면 18유닛, 흉부 63유닛으로 총 219유닛, 좌우 대칭입니다.
- 센서 패치는 분리 가능하며 웨어러블 장치 외부 쉘에 설치되어 동형 로봇과 동일한 배치를 갖습니다. 데이터는 10Hz로 수집되며, 각 신체 영역의 촉각 정보는 단일 접촉점이 아닌 공간 분포로 표현됩니다.

### 데이터 수집 및 실행
- 상태는 x(t) = {q(t), S(t)}로 정의되며, q(t)는 관절 각도, S(t)는 모든 촉각 유닛의 압력 및 근접도 측정값입니다.
- 시연은 시간 시퀀스 D = {x(t)}, t=0에서 T까지로 기록됩니다.
- 관절 각도는 q_R(t) = q_W(t)로 직접 매핑되며, 두 시스템이 동일한 관절 구성과 링크 길이를 공유하므로 리다이렉션이 필요 없습니다.

### 모방 학습
- Diffusion Policy를 사용하며, 상태 히스토리 길이 2, 행동 예측 호라이즌 8입니다.
- 관절 각도와 촉각 측정값은 각각 [−1, 1]로 독립 정규화됩니다. 촉각 입력은 모든 유닛을 전체적으로 정규화하며, 저자는 유닛별 정규화보다 훈련이 더 안정적이라고 언급합니다.
- 데이터 수집, 훈련 및 배포는 오픈소스 프레임워크 RoboManipBaselines를 사용합니다.

## 핵심 혁신

1. **리다이렉션 없는 형태 대응**: 웨어러블 장치와 로봇이 완전히 동일한 관절 구성과 링크 길이를 공유함으로써, TWINS는 기존 원격 조작에서의 인간-로봇 운동 매핑을 제거하고 관절 각도를 직접 전달할 수 있습니다. 이는 데이터 수집 프로세스를 단순화할 뿐만 아니라 작업자의 신체 표면 접촉 위치와 로봇의 접촉 위치가 공간적으로 엄격히 대응되도록 보장하며, 이는 이전 시스템이 동시에 충족하지 못한 핵심 특성입니다.
2. **근접도와 압력의 결합 관측**: e-Skin은 압력과 근접도를 동시에 측정하여 물리적 접촉 전에 물체 거리를 관측할 수 있게 하며, 접근부터 분리까지의 완전한 접촉 과정을 연속적으로 포착합니다. 이는 단순 접촉력보다 풍부한 시간 진화 정보를 모방 학습에 제공하며, '먼저 접근한 다음 고정'과 같은 접촉 단계 전환이 포함된 작업에 중요합니다.
3. **신체 표면 접촉을 일급 상태로**: 219개 촉각 유닛의 분포 정보를 상태 공간에 포함시켜 엔드 이펙터의 보조 신호가 아닌 독립적인 상태로 취급합니다. 이를 통해 정책은 신체 여러 영역의 접촉 이벤트를 명시적으로 활용하여 조작 단계를 전환할 수 있으며, 기존 방법이 시각이나 엔드 포스 센싱에만 의존하는 한계를突破합니다.

## 실험 및 결과

실험은 신체 표면 접촉을 수반하는 네 가지 작업을 다룹니다: Towel Hanging(수건 걸기), Basket Holding(바구니 들기), Ball Placing(공 배치), Adaptive Holding(적응형 들기). 각 작업에서 10개의 시연을 수집하여 총 40개의 시연을 단일 작업자가 30분 내에 완료했으며, 특별한 훈련이 필요 없었습니다.

| 지표 | 값 |
|------|------|
| 관절 각도 추적 평균 절대 오차 | 0.94 deg(14개 팔 관절) |
| 관절 각도 추적 95 백분위 오차 | 3.43 deg |
| 추적 지연 | 약 0.4–0.6 s |
| 촉각 입력 차원 | 438(219 유닛 × 압력+근접도) |
| 관절 각도 입력 차원 | 16(좌우 팔+그리퍼) |

정책은 모든 작업에서 신체 표면 접촉 이벤트에 따라 조작 단계를 성공적으로 전환했습니다. 시연에 포함되지 않은 상황에 대한 강건성을 보였습니다: Towel Hanging에서 수건 제시 순서가 반대이거나 양쪽 전완에 동시에 놓일 때도 해당 팔을 올바르게 회전했고, Ball Placing에서 시연보다 공 수가 많을 때도 반복 배치를 수행했으며, Adaptive Holding에서 물체 순서가 다를 때도 올바른 들기 전략을 선택했습니다. 단일 팔과 흉부 사이에서 물체를 들고 있는 작업에서는 간헐적 실패(물체 낙하)가 발생했으며, 추가 스펀지 패드로 크게 완화되었습니다. 저자는 모방 학습 알고리즘 자체에 대한 절제 평가를 수행하지 않았으며, 다른 기준 시스템과의 정량적 비교도 없습니다.

## 경계 및 한계

- 단일 팔과 흉부 사이에서 물체를 들고 있는 작업에서 간헐적 물체 낙하가 발생하며, 스펀지 패드로 완화되지만 완전히 해결되지는 않았으며, 저자는 관절 토크의 명시적 제어가 필요할 수 있다고 생각합니다.
- 모방 학습 알고리즘 자체에 대한 평가는 없으며, 실험은 TWINS 수집 데이터가 접촉 관련 조작의 학습과 실행을 지원할 수 있는지 검증하는 데 초점을 맞췄습니다.
- 대규모 데이터 수집, 다중 작업자 변형, 장기 안정성 테스트 또는 다른 기준 시스템과의 정량적 비교 실험은 언급되지 않았습니다.
- 현재 시스템은 이동 조작을 지원하지 않습니다(작업자는 시연 수집 중 이동할 수 없음). 메커니즘은 인간 견갑골 운동을 포함하지 않아 해부학적 충실도가 제한적입니다.
- 모든 시연은 단일 작업자에 의해 수집되었으며, 다른 체형의 작업자나 다른 조작 스타일에서의 일반화는 검증되지 않았습니다.

## 공학적 시사점

TWINS를 재현하거나 채택할 때 다음 사항을 우선 확인해야 합니다: 첫째, 관절 구성과 링크 길이가 엄격히 일치하는지 여부—이는 리다이렉션 없는 매핑의 전제 조건이며, 치수 편차는 접촉 위치의 대응을 깨뜨립니다. 둘째, 촉각 센서의 배치와 설치 위치가 로봇과 완전히 일치해야 하며, 유닛별 정규화가 아닌 전체 정규화를 사용해야 합니다. 그렇지 않으면 훈련 안정성이 크게 저하됩니다. 셋째, 추적 지연(약 0.4–0.6 s)이 접촉 작업에 미치는 영향을 주의해야 합니다. 지연은 접촉 타이밍의 편차를 유발할 수 있으며, 필요한 경우 정책 훈련에서 지연 보상을 고려해야 합니다. 가장 함정에 빠지기 쉬운 부분은 들기 작업의 안정성입니다—단일 팔과 흉부의 협동이 포함된 경우 접촉 인터페이스에 미리 유연한 재료를 추가하고, 순수 위치 제어가 아닌 명시적 토크 제어를 고려하는 것이 좋습니다. 또한 데이터 수집 중 작업자는 신체를 고정해야 하며(어깨 지지가 의자에 고정됨), 하류에서 이동 조작이 필요하면 메커니즘과 수집 프로세스를 직접 확장해야 합니다.
