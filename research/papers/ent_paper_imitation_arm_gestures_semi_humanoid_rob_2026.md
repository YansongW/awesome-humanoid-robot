---
$id: ent_paper_imitation_arm_gestures_semi_humanoid_rob_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Imitation of Arm Gestures by the Semi-Humanoid Robot NICO
  zh: Imitation of Arm Gestures by the Semi-Humanoid Robot NICO
  ko: Imitation of Arm Gestures by the Semi-Humanoid Robot NICO
summary:
  en: Seamless human-robot interaction (HRI) requires a number of perceptual and motor abilities from the robot, one of them
    being the imitation of human gestures. Humanoid robots have an advantage in HRI thanks to their anthropomorphic features.
    In this work, we develop a system for imitation of human arm gestures by the semi-humanoid robot NICO based on analytical
    geometry and a pretrained MediaPipe.
  zh: 本文提出一套基于单目 RGB 的解析式手臂手势模仿管线，面向无肘部 roll 关节的半人形机器人 NICO。作者利用 MediaPipe 姿态与手部关键点，通过几何公式重建肩、肘、腕共 6 自由度关节角，并线性映射至电机位置。核心贡献在于将分析几何方法适配至
    NICO 的特定运动学结构，并引入手部关键点改善前臂旋转估计，全程无需训练数据或专用深度传感器。
  ko: Seamless human-robot interaction (HRI) requires a number of perceptual and motor abilities from the robot, one of them
    being the imitation of human gestures. Humanoid robots have an advantage in HRI thanks to their anthropomorphic features.
    In this work, we develop a system for imitation of human arm gestures by the semi-humanoid robot NICO based on analytical
    geometry and a pretrained MediaPipe.
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
- imitation
- arm
- gestures
- semi
- humanoid
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
  title: arXiv:2607.18197 Imitation of Arm Gestures by the Semi-Humanoid Robot NICO
  url: https://arxiv.org/abs/2607.18197
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套基于单目 RGB 的解析式手臂手势模仿管线，面向无肘部 roll 关节的半人形机器人 NICO。作者利用 MediaPipe 姿态与手部关键点，通过几何公式重建肩、肘、腕共 6 自由度关节角，并线性映射至电机位置。核心贡献在于将分析几何方法适配至 NICO 的特定运动学结构，并引入手部关键点改善前臂旋转估计，全程无需训练数据或专用深度传感器。

## 它改变了什么

该工作的真正改变在于：将手势模仿从「依赖专用硬件或大规模学习」的二元对立中拉出，证明了一条中间路径——用单目 RGB 加解析几何，即可在受限条件下驱动一台无肘部 roll 关节的机器人完成多关节手势复现。此前分析几何方法多针对 NAO 等平台，且常回避前臂旋转与腕部屈曲这类难解自由度；本文直面这些难点，用 MediaPipe 手部关键点补充姿态关键点的不足，使管线在保持可解释性与实时性的同时，覆盖了更广的手势空间。

对 HRI 社区而言，这改变了「低成本实时模仿」的可行性边界：不再需要深度相机或 GPU 集群，一台普通 RGB 摄像头加轻量推理即可达到约 590 帧/秒的处理速度。但代价是精度天花板明显——肩部 roll 误差达 34°，前臂旋转误差 50.1°，这提示该路线更适合对精度不敏感的社会性交互场景，而非精细操作任务。

## 方法拆解

### 整体流程
RGB 帧 → MediaPipe Pose（33 关键点）与 Hands（21 关键点）→ 3D 坐标提取 → 关节角几何重建 → 线性映射至电机位置 → 执行。

### 关键点融合策略
- 优先使用手部检测器的腕部与手掌点替换姿态关键点：左手 P15、P17、P19 与右手 P16、P18、P20。
- 手部坐标以腕部为原点，需平移对齐至姿态模型腕部；无需缩放或旋转对齐，因两模型共享相机坐标系。
- 仅使用关键点 11–24（手臂区域），可扩展至全身。

### 关节角重建（左臂为例）
- **躯干偏航补偿**：通过左右肩估计肩线，绕垂直轴旋转坐标以补偿偏航；不补偿俯仰与横滚（假设直立站姿）。
- **腕部屈曲**（DoF 1）：θ_wrist-bend = π/2 + ∠A，其中 ∠A 为掌平面法向量 V_LPN = (P17 − P15) × (P19 − P15) 与上臂方向 (−V_LF) 的无符号角。
- **前臂旋转**（DoF 2）：
  - 旋转基向量 rot.base = V_LA 在垂直于 V_LF 平面上的投影（公式 3）；若手臂伸直则回退至 V_LA × V_LRS（公式 4）。
  - 手掌方向 V_PO 为掌法线在旋转平面上的投影，符号由腕部屈曲角决定（公式 6）；手掌垂直前臂时用腕点与 P17、P19 中点构造回退向量（公式 7–8）。
  - 前臂旋转角为 V_PO 绕前臂轴相对 rot.base 的带符号角。
- **肘部弯曲**（DoF 3）：θ_elbow-bend = arccos((V_LF·V_LA)/(‖V_LF‖·‖V_LA‖))，范围 (0, π]。
- **肩部 pitch**（DoF 5）：θ_shldr-pitch = atan2(√(v_x² + v_z²), v_y)，范围 [0, π]；不区分前后（由 roll 处理）。
- **肩部 roll**（DoF 4）：θ_shldr-roll = atan2(v_x, √(v_z² + v_y²)) + π/2，范围 [0, 2π)；v_z > 0 时镜像为 2π − θ（公式 12）。
- **肩部 yaw**（DoF 6）：固定中立位。

### 角度到电机映射
- 每关节解析区间 [θ_min, θ_max] 与对应电机位置通过实验标定。
- 线性映射：m = m(θ_min) + (θ − θ_min)/(θ_max − θ_min) · (m(θ_max) − m(θ_min))，取整后发送。

## 关键创新

1. **无肘部 roll 关节的运动学适配**：NICO 缺少 NAO 的肘部 roll 自由度，作者通过将前臂旋转与腕部屈曲解耦，用掌平面法向量与手部关键点重构该自由度，使解析方法能迁移至不同运动学结构。这是对「分析几何需逐平台定制」这一痛点的直接回应。

2. **手部关键点融合提升前臂旋转估计**：仅用姿态关键点时前臂旋转 MAE 为 67.1°，替换为手部关键点后降至 50.1°（改进约 25%）。这一设计决策表明：在单目 RGB 下，手部局部几何信息对解决手臂自遮挡与方向歧义具有不可替代的价值，且无需额外传感器。

3. **实时性与可解释性的兼顾**：平均处理时间 0.0017 s/帧（约 590 帧/秒），最坏情况 0.0093 s/帧（约 108 帧/秒），全程无训练阶段。这证明解析几何路线在计算效率上远超学习类方法，且每个关节角都有明确几何含义，便于调试与故障排查。

## 实验与结果

### 实验设置
- 6 名参与者（3 男 3 女，身高 158–188 cm），每人执行 11 个对称姿态 × 3 种视角（0°、30°、45°）。
- 相机：Google Pixel 9a 前置 RGB，高 125 cm，距参与者 150 cm；环境与着装全程固定。
- 评估：重建角与预定义参考角比较，循环量用最小圆角度差。

### 关键结果

| 关节 | MAE（度） | 备注 |
|------|-----------|------|
| 肩部 pitch | 约 10 | 精度最高 |
| 肘部弯曲 | 约 20 | 中等 |
| 腕部弯曲 | 约 23 | 中立位更准，极端屈曲误差大 |
| 肩部 roll | 34 | 对体态方向敏感 |
| 前臂旋转（仅姿态点） | 67.1 | 基线 |
| 前臂旋转（含手部点） | 50.1 | 改进约 25% |

- 手部关键点在 64% 情况下可用（跨所有参与者和视角平均）。
- 六名参与者 MAE 范围：含前臂旋转与腕部屈曲时 30.1°–32.1°；不含时 20.8°–23.7°。
- 视角 0°–45° 影响相对较小；左臂 MAE 通常高于右臂（逆时针转身导致左臂可见性降低）。
- 姿态本身对精度影响最大，涉及明显前臂旋转与手掌方向的姿态误差最大。
- 身高 158–188 cm 范围内未观察到与精度的明确关系。

### 结果含义
肩部 pitch 与肘部弯曲的精度（约 10°–20°）足以支撑社交性手势复现；但肩部 roll 与前臂旋转的误差（34°、50.1°）表明，涉及手臂前后摆动与手腕旋转的姿态仍不可靠。手部关键点的 25% 改进验证了融合策略的有效性，但 50.1° 的绝对误差仍说明该自由度在单目 RGB 下的本质困难。

## 边界与局限

- 前臂旋转估计是主要瓶颈：即使融合手部关键点，误差仍显著高于其他关节，且其误差会传导至腕部弯曲估计（腕部偏离中立位越远，表观腕角越依赖前臂方向）。
- 肩部 roll 精度低（34° MAE），对体态方向敏感，未做额外归一化或几何约束。
- 未补偿躯干俯仰与横滚，假设直立站姿；肩部 yaw 固定中立位，头部运动未实现。
- 自遮挡与手部方向歧义是主要误差来源，且未包含时间平滑、动态手势扩展。
- 实验在受控条件（固定环境、纯黑 T 恤、6 名参与者）下进行，泛化性未验证；论文未明确在非受控光照、复杂背景或不同体型下的表现。

## 工程启示

复现或选型时，先核对以下三点：
1. **手部关键点可用性**：64% 的可用率意味着约 1/3 帧会退化为仅姿态点估计，前臂旋转误差将从 50.1° 升至 67.1°。若下游任务对前臂旋转敏感，需考虑多帧融合或增加手部检测的触发条件。
2. **肩部 roll 的镜像逻辑**：公式 12 的镜像条件（v_z > 0）依赖躯干朝向，实验协议假设直立站姿。若实际应用中出现躯干倾斜，该自由度误差会显著放大，建议先验证躯干补偿是否必要。
3. **角度映射标定**：每个关节的解析区间与电机位置需实验标定，且电机位置取整后发送。若机器人负载或装配有差异，需重新标定，否则线性映射的端点误差会直接叠加到关节角误差上。

最易踩坑处：前臂旋转的符号约定与腕部屈曲的耦合。公式 6 中 V_PO 的符号由 cos(θ_wrist-bend) 决定，若腕部屈曲估计偏差超过 90°，符号可能翻转，导致前臂旋转误差急剧增大。建议在调试时先单独验证腕部屈曲在极端位置的精度，再联调前臂旋转。

## Overview
Seamless human-robot interaction (HRI) requires a number of perceptual and motor abilities from the robot, one of them being the imitation of human gestures. Humanoid robots have an advantage in HRI thanks to their anthropomorphic features. In this work, we develop a system for imitation of human arm gestures by the semi-humanoid robot NICO based on analytical geometry and a pretrained MediaPipe pose-estimation model. For each input RGB frame, 3D coordinates of relevant human body landmarks, including arm joints and hand keypoints, are obtained using the MediaPipe framework. Joint angles are then computed from these coordinates using derived geometric relations. Finally, the computed angles are properly mapped to NICO's motor configuration and executed in a predefined motion sequence. Preliminary experiments on several representative arm gestures with six participants of different height indicate that the proposed method can produce meaningful imitative motions from monocular RGB input only, while also highlighting limitations in more complex poses and wrist-related movements.

## 参考
- https://arxiv.org/abs/2607.18197

## 개요

본 논문은 단안 RGB 기반의 해석적 팔 제스처 모방 파이프라인을 제안하며, 팔꿈치 roll 관절이 없는 반인간형 로봇 NICO를 대상으로 한다. 저자는 MediaPipe 포즈 및 손 키포인트를 활용하여 기하학적 공식을 통해 어깨, 팔꿈치, 손목의 총 6자유도 관절각을 재구성하고, 이를 선형적으로 모터 위치에 매핑한다. 핵심 기여는 해석적 기하학 방법을 NICO의 특정 운동학 구조에 맞게 적응시키고, 손 키포인트를 도입하여 전완 회전 추정을 개선한 점이며, 훈련 데이터나 전용 깊이 센서가 전혀 필요 없다는 것이다.

## 그것이 바꾼 것

이 작업의 진정한 변화는 제스처 모방을 '전용 하드웨어 또는 대규모 학습에 의존'이라는 이분법에서 끌어내어, 단안 RGB와 해석적 기하학만으로 제한된 조건에서 팔꿈치 roll 관절이 없는 로봇이 다관절 제스처를 재현할 수 있다는 중간 경로를 증명한 것이다. 기존의 해석적 기하학 방법은 주로 NAO 같은 플랫폼을 대상으로 했으며, 전완 회전과 손목 굴곡 같은 풀기 어려운 자유도를 종종 회피했다. 본 논문은 이러한 난점을 정면으로 다루며, MediaPipe 손 키포인트로 포즈 키포인트의 부족함을 보완하여 파이프라인이 해석 가능성과 실시간성을 유지하면서도 더 넓은 제스처 공간을 커버하게 했다.

HRI 커뮤니티 관점에서 이는 '저비용 실시간 모방'의 실현 가능성 경계를 바꾼다. 더 이상 깊이 카메라나 GPU 클러스터가 필요 없으며, 일반 RGB 카메라와 경량 추론만으로 약 590프레임/초의 처리 속도를 달성한다. 그러나 정밀도 상한선이 명확히 낮아진다는 대가가 따른다. 어깨 roll 오차는 34°, 전완 회전 오차는 50.1°에 달하며, 이는 이 접근법이 정밀도에 민감하지 않은 사회적 상호작용 시나리오에는 적합하지만, 정밀 조작 작업에는 부적합함을 시사한다.

## 방법 분해

### 전체 흐름
RGB 프레임 → MediaPipe Pose(33개 키포인트) 및 Hands(21개 키포인트) → 3D 좌표 추출 → 관절각 기하학적 재구성 → 모터 위치로 선형 매핑 → 실행.

### 키포인트 융합 전략
- 손 감지기의 손목 및 손바닥 지점을 우선적으로 사용하여 포즈 키포인트를 대체한다. 왼손 P15, P17, P19와 오른손 P16, P18, P20.
- 손 좌표는 손목을 원점으로 하므로, 포즈 모델의 손목에 평행 이동으로 정렬해야 한다. 스케일링이나 회전 정렬은 필요 없다. 두 모델이 동일한 카메라 좌표계를 공유하기 때문이다.
- 키포인트 11–24(팔 영역)만 사용하며, 전신으로 확장 가능하다.

### 관절각 재구성(왼팔 기준)
- **몸통 요(yaw) 보상**: 양쪽 어깨로 어깨선을 추정하고, 수직 축을 기준으로 좌표를 회전시켜 요를 보상한다. 피치와 롤은 보상하지 않는다(직립 자세를 가정).
- **손목 굴곡**(DoF 1): θ_wrist-bend = π/2 + ∠A. 여기서 ∠A는 손바닥 평면 법선 벡터 V_LPN = (P17 − P15) × (P19 − P15)와 위팔 방향 (−V_LF) 사이의 부호 없는 각도이다.
- **전완 회전**(DoF 2):
  - 회전 기저 벡터 rot.base는 V_LF에 수직인 평면에 V_LA를 투영한 것이다(식 3). 팔이 완전히 펴지면 V_LA × V_LRS로 대체한다(식 4).
  - 손바닥 방향 V_PO는 회전 평면에 손바닥 법선을 투영한 것이며, 부호는 손목 굴곡 각도에 의해 결정된다(식 6). 손바닥이 전완에 수직일 때는 손목 지점과 P17, P19의 중점을 사용하여 대체 벡터를 구성한다(식 7–8).
  - 전완 회전 각도는 전완 축을 기준으로 V_PO가 rot.base에 대해 갖는 부호 있는 각도이다.
- **팔꿈치 굴곡**(DoF 3): θ_elbow-bend = arccos((V_LF·V_LA)/(‖V_LF‖·‖V_LA‖)), 범위 (0, π].
- **어깨 피치**(DoF 5): θ_shldr-pitch = atan2(√(v_x² + v_z²), v_y), 범위 [0, π]. 전후 구분은 하지 않는다(roll이 처리).
- **어깨 롤**(DoF 4): θ_shldr-roll = atan2(v_x, √(v_z² + v_y²)) + π/2, 범위 [0, 2π). v_z > 0일 때 2π − θ로 미러링된다(식 12).
- **어깨 요**(DoF 6): 중립 위치로 고정.

### 각도-모터 매핑
- 각 관절의 해석 구간 [θ_min, θ_max]과 해당 모터 위치는 실험적으로 캘리브레이션된다.
- 선형 매핑: m = m(θ_min) + (θ − θ_min)/(θ_max − θ_min) · (m(θ_max) − m(θ_min)), 반올림 후 전송.

## 핵심 혁신

1. **팔꿈치 roll 관절이 없는 운동학 적응**: NICO는 NAO의 팔꿈치 roll 자유도가 없다. 저자는 전완 회전과 손목 굴곡을 분리하고, 손바닥 평면 법선 벡터와 손 키포인트로 해당 자유도를 재구성하여 해석적 방법이 다른 운동학 구조로 이식될 수 있게 했다. 이는 '해석적 기하학은 플랫폼마다 맞춤화가 필요하다'는 문제점에 대한 직접적인 대응이다.

2. **손 키포인트 융합을 통한 전완 회전 추정 개선**: 포즈 키포인트만 사용할 때 전완 회전 MAE는 67.1°였으나, 손 키포인트로 대체한 후 50.1°로 감소했다(약 25% 개선). 이 설계 결정은 단안 RGB 환경에서 손의 국소 기하학 정보가 팔의 자기 가림 및 방향 모호성을 해결하는 데 대체 불가능한 가치를 지니며, 추가 센서가 필요 없음을 보여준다.

3. **실시간성과 해석 가능성의 균형**: 평균 처리 시간 0.0017초/프레임(약 590프레임/초), 최악의 경우 0.0093초/프레임(약 108프레임/초)이며, 훈련 단계가 전혀 없다. 이는 해석적 기하학 경로가 학습 기반 방법보다 계산 효율성에서 훨씬 우수하며, 각 관절각이 명확한 기하학적 의미를 가지므로 디버깅과 문제 해결이 용이함을 증명한다.

## 실험 및 결과

### 실험 설정
- 6명의 참가자(남 3명, 여 3명, 키 158–188cm), 각자 11개의 대칭 자세 × 3가지 시점(0°, 30°, 45°)을 수행.
- 카메라: Google Pixel 9a 전면 RGB, 높이 125cm, 참가자로부터 150cm 거리. 환경과 복장은 전체 실험 동안 고정.
- 평가: 재구성 각도를 사전 정의된 참조 각도와 비교하고, 순환량은 최소 원형 각도 차이를 사용.

### 주요 결과

| 관절 | MAE(도) | 비고 |
|------|-----------|------|
| 어깨 피치 | 약 10 | 정밀도 최고 |
| 팔꿈치 굴곡 | 약 20 | 중간 |
| 손목 굴곡 | 약 23 | 중립 위치에서 더 정확, 극단적 굴곡에서 오차 큼 |
| 어깨 롤 | 34 | 체형 방향에 민감 |
| 전완 회전(포즈 점만) | 67.1 | 기준선 |
| 전완 회전(손 점 포함) | 50.1 | 약 25% 개선 |

- 손 키포인트는 64%의 경우에서 사용 가능했다(모든 참가자와 시점 평균).
- 6명 참가자의 MAE 범위: 전완 회전과 손목 굴곡 포함 시 30.1°–32.1°, 제외 시 20.8°–23.7°.
- 시점 0°–45°의 영향은 상대적으로 작았다. 왼팔 MAE는 일반적으로 오른팔보다 높았다(시계 반대 방향 회전으로 왼팔 가시성 감소).
- 자세 자체가 정밀도에 가장 큰 영향을 미쳤으며, 전완 회전과 손바닥 방향이 뚜렷한 자세에서 오차가 가장 컸다.
- 키 158–188cm 범위에서는 정밀도와의 명확한 관계가 관찰되지 않았다.

### 결과 의미
어깨 피치와 팔꿈치 굴곡의 정밀도(약 10°–20°)는 사회적 제스처 재현을 지원하기에 충분하다. 그러나 어깨 롤과 전완 회전의 오차(34°, 50.1°)는 팔의 전후 흔들림과 손목 회전이 포함된 자세는 여전히 신뢰할 수 없음을 시사한다. 손 키포인트의 25% 개선은 융합 전략의 효과를 검증하지만, 50.1°의 절대 오차는 단안 RGB에서 이 자유도의 본질적 어려움을 여전히 보여준다.

## 경계 및 한계

- 전완 회전 추정이 주요 병목이다. 손 키포인트를 융합해도 오차가 다른 관절보다 현저히 높으며, 이 오차는 손목 굴곡 추정에도 전파된다(손목이 중립 위치에서 멀어질수록 겉보기 손목 각도는 전완 방향에 더 의존).
- 어깨 롤 정밀도가 낮고(34° MAE), 체형 방향에 민감하며, 추가 정규화나 기하학적 제약이 없다.
- 몸통 피치와 롤은 보상되지 않으며, 직립 자세를 가정한다. 어깨 요는 중립 위치로 고정되고, 머리 움직임은 구현되지 않았다.
- 자기 가림과 손 방향 모호성이 주요 오차 원인이며, 시간적 평활화나 동적 제스처 확장은 포함되지 않았다.
- 실험은 통제된 조건(고정 환경, 순검정 티셔츠, 6명 참가자)에서 수행되었으며, 일반화 가능성은 검증되지 않았다. 논문은 비통제 조명, 복잡한 배경 또는 다양한 체형에서의 성능을 명시하지 않았다.

## 공학적 시사점

재현 또는 모델 선택 시 다음 세 가지를 먼저 확인하라.
1. **손 키포인트 가용성**: 64%의 가용률은 약 1/3의 프레임이 포즈 점만으로 추정되며, 전완 회전 오차가 50.1°에서 67.1°로 증가함을 의미한다. 하위 작업이 전완 회전에 민감하다면, 다중 프레임 융합이나 손 감지 트리거 조건 추가를 고려해야 한다.
2. **어깨 롤의 미러링 로직**: 식 12의 미러링 조건(v_z > 0)은 몸통 방향에 의존하며, 실험 프로토콜은 직립 자세를 가정한다. 실제 적용에서 몸통 기울기가 발생하면 이 자유도의 오차가 크게 증폭되므로, 몸통 보상이 필요한지 먼저 검증하는 것이 좋다.
3. **각도 매핑 캘리브레이션**: 각 관절의 해석 구간과 모터 위치는 실험적으로 캘리브레이션해야 하며, 모터 위치는 반올림 후 전송된다. 로봇의 부하나 조립 상태가 다르면 재캘리브레이션이 필요하며, 그렇지 않으면 선형 매핑의 끝점 오차가 관절각 오차에 직접 더해진다.

가장 함정에 빠지기 쉬운 부분은 전완 회전의 부호 규약과 손목 굴곡의 결합이다. 식 6에서 V_PO의 부호는 cos(θ_wrist-bend)에 의해 결정되는데, 손목 굴곡 추정 오차가 90°를 초과하면 부호가 뒤집혀 전완 회전 오차가 급격히 증가할 수 있다. 디버깅 시 먼저 극단 위치에서 손목 굴곡의 정밀도를 단독으로 검증한 후, 전완 회전을 함께 조정하는 것을 권장한다.
