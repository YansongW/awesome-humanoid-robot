---
$id: ent_paper_egohtr_egocentric_4d_demonstrations_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal'
  zh: 'EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal'
  ko: 'EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal'
summary:
  en: Deploying humanoid robots in unstructured terrain remains an open problem. While classic reinforcement learning struggles
    with the sheer complexity of real-world interactions, more promising methods leveraging human priors remain limited to
    models lacking contextual awareness. The restricted motion synthesis is a direct consequence of existing dataset pipelines
    failing to capture human-scene.
  zh: EgoHTR 是一个面向非结构化地形中人类穿越行为的自我中心 4D 演示数据集与采集管线，由研究团队结合商用传感器（Aria 眼镜、Rokoko 动捕服、Leica 扫描仪）构建。其核心贡献在于提供场景对齐的高保真人-地形交互数据，并验证了该数据在感知运动策略训练中的直接价值。
  ko: Deploying humanoid robots in unstructured terrain remains an open problem. While classic reinforcement learning struggles
    with the sheer complexity of real-world interactions, more promising methods leveraging human priors remain limited to
    models lacking contextual awareness. The restricted motion synthesis is a direct consequence of existing dataset pipelines
    failing to capture human-scene.
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
- egohtr
- egocentric
- 4d
- demonstrations
- huma
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
  title: 'arXiv:2607.13472 EgoHTR: Egocentric 4D Demonstrations of Human Terrain Traversal'
  url: https://arxiv.org/abs/2607.13472
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

EgoHTR 是一个面向非结构化地形中人类穿越行为的自我中心 4D 演示数据集与采集管线，由研究团队结合商用传感器（Aria 眼镜、Rokoko 动捕服、Leica 扫描仪）构建。其核心贡献在于提供场景对齐的高保真人-地形交互数据，并验证了该数据在感知运动策略训练中的直接价值。

## 它改变了什么

现有 4D 人-场景数据集存在根本性的模态割裂：要么像 AMASS、LaFAN1 那样只有高保真运动学却无环境上下文，要么像 PROX、RICH 那样有场景但空间受限。SLOPER4D 虽尝试野外采集，却因传感器配置缺失（无自我中心视觉或场景几何不完整）导致重建精度有限。这造成一个尴尬局面——下游机器人感知运动研究既需要精确的落脚点几何，又需要与全局轨迹对齐的身体运动，而现有数据无法同时满足。

EgoHTR 真正改变的是数据采集的“可行性边界”。它证明无需定制硬件或精密同步设备，仅用商用现成传感器组合，就能在 25 m² 至 1000 m² 的野外场景中产出局部精度（MPJPE 73.2 mm）优于最强基线 SLOPER4D（78.01 mm）的数据。这降低了高保真人-场景数据集的准入门槛，使“采集即服务”成为可能。

## 方法拆解

### 硬件配置与数据流
- **主体 Aria 眼镜**：1408×1408 RGB @ 30 fps，闭环 SLAM 轨迹 @ 1000 fps，半稠密点云
- **Rokoko Pro II 动捕服**：22 个主要关节 BVH @ 30 fps，原始 IMU @ 100 Hz，序列开始时 I-pose 重校准
- **Leica BLK2GO 扫描仪**：稠密彩色网格 + 6-DoF 轨迹，提供全局几何锚点
- **可选**：第二副观察者 Aria 眼镜（同步数据）、GoPro Hero 10 固定相机、Qualisys 光学动捕（毫米级真值）

### 人体-场景重建三阶段
1. **身体参数化**：SMPL-X 模型，仅估计姿态 θ∈ℝ165 和全局平移 t∈ℝ3；形状 β、表情 ψ 固定为身份姿态。重定向分两步：先逐关节旋转偏移补偿骨骼轴错位，再通过 IK 最小化 SMPL-X 肢体关节与 MoCap 关节的 3D 位置差异（损失仅限肢体子集 L，因源/目标骨架结构差异）。
2. **时间对齐**：利用序列开始的拍手声，在 48 kHz 音频流与 100 Hz IMU 信号中检测近同时峰值。省略 PPS 硬连线电缆换取野外移动性，对齐误差 < 60 ms（经验评估），序列限长 5 min 约束时钟漂移。
3. **空间对齐**：两阶段。第一阶段将身体运动学锚定到 Aria 闭环轨迹，假设眼镜相对头部无位移，建模为静态偏移 r_{C_AH}，完全依赖 SLAM 消除全局 IMU 漂移。第二阶段先用 VGGT 估计扫描仪初始图像与 Aria 图像相对变换做粗对齐，再用 ICP 将半稠密 Aria 点云配准到稠密扫描。

### 感知运动训练
- PPO 在 Isaac Lab 训练，Unitree G1 人形机器人，29 自由度关节位置目标
- Actor 观测本体感觉、参考关节指令、偏航对齐地形高度扫描；Critic 额外接收特权身体状态和踝关节接触力
- 引入时间足部接触奖励；回合初始化限制在无穿插帧，锚点或末端执行器漂移时终止

## 关键创新

1. **拍手声同步替代硬连线**：这是最实用的工程创新。放弃 PPS 电缆虽引入 < 60 ms 对齐误差，但换来了野外采集的移动自由度。对 30 fps 数据而言，60 ms 误差不足两帧，对下游运动训练影响可忽略，却大幅简化了采集流程。
2. **SLAM 锚定消除 IMU 漂移**：将身体运动学完全锚定到 Aria 闭环轨迹，而非依赖动捕服自身积分。这一设计决策使全局轨迹精度（RTE 0.09%）比肩专用动捕系统，同时保持野外可部署性。
3. **跨模态验证闭环**：同时提供 Qualisys 光学真值子集（0.7 hours）和感知运动训练验证，形成“采集→重建→训练→部署”的完整证据链。这在同类数据集中罕见，直接证明了数据质量足以支撑真实机器人策略学习。

## 实验与结果

### 局部姿态精度对比（表 2）
| 方法 | MPJPE (mm) | PA-MPJPE (mm) |
|---|---|---|
| PROX '19 | 167.1 | 72.0 |
| HPS '21 | 93.1 | — |
| RICH '22 | 161.8 | 63.7 |
| SLOPER4D '23 | 78.01 | 55.4 |
| **EgoHTR (local)** | **73.2** | **54.3** |

EgoHTR 相比 SLOPER4D，MPJPE 降低 6.2%（由 78.01→73.2 计算），PA-MPJPE 降低 2.0%（由 55.4→54.3 计算）。全局指标 W-MPJPE 151.3 mm、WA-MPJPE 66.7 mm、RTE 0.09%。

### 足部接触奖励消融（表 3，5 种子均值±标准差）
| 地形 | 指标 | π0（无奖励） | π1（有奖励） |
|---|---|---|---|
| Flat | 最大 SR (%) | 99.0±0.1 | 99.0±0.1 |
| Flat | 收敛步数 (×10⁸) | 0.90±0.01 | 0.84±0.01 |
| Box up | 最大 SR (%) | 89.0±0.1 | 90.0±0.2 |
| Box up | 收敛步数 (×10⁸) | 1.23±0.07 | 1.08±0.02 |
| Beam | 最大 SR (%) | 96.0±0.1 | 96.0±0.1 |
| Beam | 收敛步数 (×10⁸) | 0.82±0.02 | 0.75±0.02 |
| S.Stones | 最大 SR (%) | 67.0±1.0 | 72.0±1.0 |
| S.Stones | 收敛步数 (×10⁸) | 7.14±0.65 | 5.72±0.21 |

足部接触奖励在 S.Stones（最复杂地形）上提升最显著（SR 67.0→72.0，收敛加速 1.42×10⁸ 步），说明该奖励对不规则落脚点地形尤为关键。

### 网格恢复方法基准（表 4）
| 方法 | SR (%) | MPJPE | PA-M. | Jitter | W-M. | WA-M. | RTE | CD | Prec |
|---|---|---|---|---|---|---|---|---|---|
| JOSH | 57.18 | 101.5 | 66.5 | 2.02 | 321.3 | 138.2 | 2.26 | 0.71 | 73.11 |
| Human3R | 80.53 | 148.4 | 64.7 | 12.97 | 693.5 | 305.9 | 5.55 | 1.71 | 24.11 |
| EgoAllo | 100 | 161.1 | 111.5 | 0.14 | 392.7 | 167.1 | 0.14 | — | — |

EgoAllo 成功率最高但精度最差，JOSH 精度最优但成功率低，Human3R 抖动严重（Jitter 12.97）。EgoHTR 的参考重建（73.2 MPJPE）优于所有网格恢复方法。

### MoCap 真值验证（表 D.3）
EgoAllo 在 EgoHTR 与 MoCap GT 上 MPJPE 差异 3.6 mm（161.8 vs 158.2），JOSH 差异 1.4 mm（89.4 vs 75.3）。参考重建在 MoCap GT 上 MPJPE 70.3、PA-MPJPE 56.4，与 EgoHTR 结果（73.2、54.3）接近，验证管线精度。

### 参考运动精度消融
训练容忍噪声至约 σ = 0.05 m，误差超 0.1 m 时训练崩溃。单目方法在粗糙地形上全局估计误差通常超 0.1 m，说明 EgoHTR 的精度（局部 MPJPE 73.2 mm）恰好处于可训练区间边缘。

## 边界与局限

- **规模不足**：1.37 hours 数据量（0.15M 帧）远小于 NymeriaPlus（300 hours）等大规模数据集，多样性受限，可能影响泛化。
- **静态环境假设**：管线限于无铰接物体的静态场景，无法处理动态障碍或可变形地形。
- **手部未建模**：Aria 眼镜支持手部追踪但未纳入身体模型，手部参数固定为身份姿态，限制人-物交互类任务。
- **无联合优化**：未进行采集后的人-场景联合优化，重建精度存在进一步提升空间。
- **硬件物理约束**：在无特征环境或高加速度机动中，SLAM 或 IMU 可能失效，管线性能下降。
- **未做之事**：未将端到端模型微调用于绕过后处理优化；未将数据集扩展至运动合成（均留作未来工作）。

## 工程启示

- **复现优先级**：先核对时间对齐模块。拍手声同步依赖 48 kHz 音频与 100 Hz IMU 的峰值检测，若采集环境背景噪声大，建议增加人工校验步骤。序列限长 5 min 是硬约束，超时需分段采集。
- **最易踩坑点**：空间对齐的 ICP 细化对初始粗对齐敏感。VGGT 估计的初始变换若偏差过大，ICP 易陷入局部最优。建议在特征丰富场景中采集，并保留扫描仪初始图像作为几何锚点。
- **下游训练适配**：参考运动精度需控制在 σ ≤ 0.05 m 内，否则策略训练崩溃。EgoHTR 的局部 MPJPE 73.2 mm 已接近此阈值，若用于训练建议先做平滑预处理。足部接触奖励在复杂地形（如 S.Stones）上增益显著，应作为默认配置。
- **硬件选型**：若预算有限，可省略第二副 Aria 眼镜和固定相机，仅保留主体三件套即可完成核心采集。Qualisys 真值子集仅 0.7 hours，主要用于验证而非训练，可按需采集。

## Overview
Deploying humanoid robots in unstructured terrain remains an open problem. While classic reinforcement learning struggles with the sheer complexity of real-world interactions, more promising methods leveraging human priors remain limited to models lacking contextual awareness. The restricted motion synthesis is a direct consequence of existing dataset pipelines failing to capture human-scene sequences in challenging environments. To bridge this gap between humanoid learning and scene reconstruction, we introduce the Egocentric Human-Terrain Reconstruction (EgoHTR) dataset. We develop and open-source a reconstruction pipeline capturing 55 scene-aligned 4D human motion sequences in diverse, complex environments using a multi-sensor setup of egocentric wearables and a portable 3D scanner. The resulting dataset comprises over 150k frames, which we evaluate against motion-capture ground truth, demonstrating state-of-the-art accuracy and establishing a rigorous benchmark for human motion analysis and synthesis. Further, we leverage this data to train perceptive locomotion policies, demonstrating hardware deployment on a Unitree G1 for reconstructed reference motions. Our pipeline enables community-driven dataset extensions and factors the problem to help researchers build foundational, context-aware robots that reliably traverse uneven terrain.

## 参考
- https://arxiv.org/abs/2607.13472

## 개요

EgoHTR은 비정형 지형에서의 인간 이동 행동을 위한 자기중심적 4D 데모 데이터셋 및 수집 파이프라인으로, 연구팀이 상용 센서(Aria 글래스, Rokoko 모션캡처 슈트, Leica 스캐너)를 결합하여 구축했습니다. 핵심 기여는 장면 정렬된 고충실도 인간-지형 상호작용 데이터를 제공하고, 해당 데이터가 지각-운동 전략 훈련에서 직접적인 가치가 있음을 검증한 것입니다.

## 무엇을 바꾸었는가

기존 4D 인간-장면 데이터셋은 근본적인 양식 분리가 존재합니다. AMASS, LaFAN1처럼 고충실도 운동학만 있고 환경 맥락이 없거나, PROX, RICH처럼 장면은 있지만 공간이 제한적입니다. SLOPER4D는 야외 수집을 시도했지만, 센서 구성 누락(자기중심적 시각 없음 또는 장면 기하학 불완전)으로 인해 재구성 정밀도가 제한적입니다. 이로 인해 하위 로봇 지각-운동 연구가 정확한 착지점 기하학과 전역 궤적에 정렬된 신체 운동을 동시에 필요로 하지만, 기존 데이터로는 이를 충족할 수 없는 어색한 상황이 발생합니다.

EgoHTR이 실제로 바꾼 것은 데이터 수집의 '실현 가능성 경계'입니다. 맞춤형 하드웨어나 정밀 동기화 장비 없이 상용 기성 센서 조합만으로 25 m²에서 1000 m²의 야외 장면에서 최강 베이스라인 SLOPER4D(78.01 mm)보다 우수한 국소 정밀도(MPJPE 73.2 mm)의 데이터를 생산할 수 있음을 증명했습니다. 이는 고충실도 인간-장면 데이터셋의 진입 장벽을 낮추어 '수집 서비스화'를 가능하게 합니다.

## 방법 분석

### 하드웨어 구성 및 데이터 흐름
- **본체 Aria 글래스**: 1408×1408 RGB @ 30 fps, 폐루프 SLAM 궤적 @ 1000 fps, 반조밀 점군
- **Rokoko Pro II 모션캡처 슈트**: 22개 주요 관절 BVH @ 30 fps, 원시 IMU @ 100 Hz, 시퀀스 시작 시 I-포즈 재보정
- **Leica BLK2GO 스캐너**: 조밀 컬러 메시 + 6-DoF 궤적, 전역 기하학 앵커 제공
- **선택 사항**: 두 번째 관찰자 Aria 글래스(동기화 데이터), GoPro Hero 10 고정 카메라, Qualisys 광학 모션캡처(밀리미터급 진실값)

### 인간-장면 재구성 3단계
1. **신체 파라미터화**: SMPL-X 모델, 자세 θ∈ℝ165 및 전역 병진 t∈ℝ3만 추정; 형태 β, 표정 ψ는 신원 자세로 고정. 리타게팅은 두 단계로 진행: 먼저 관절별 회전 오프셋으로 골격 축 정렬 오류를 보상한 후, IK를 통해 SMPL-X 사지 관절과 MoCap 관절의 3D 위치 차이를 최소화(손실은 소스/타깃 골격 구조 차이로 인해 사지 부분집합 L로 제한).
2. **시간 정렬**: 시퀀스 시작 시 박수 소리를 활용하여 48 kHz 오디오 스트림과 100 Hz IMU 신호에서 거의 동시에 발생하는 피크를 감지. PPS 하드와이어 케이블을 생략하여 야외 이동성을 확보했으며, 정렬 오류 < 60 ms(경험적 평가), 시퀀스 길이 5분 제한으로 클록 드리프트를 구속.
3. **공간 정렬**: 2단계로 구성. 1단계는 신체 운동학을 Aria 폐루프 궤적에 앵커링하며, 글래스가 머리 기준 변위가 없다고 가정하고 정적 오프셋 r_{C_AH}로 모델링하여 전역 IMU 드리프트를 완전히 SLAM에 의존. 2단계는 먼저 VGGT로 스캐너 초기 이미지와 Aria 이미지의 상대 변환을 추정하여 대략적 정렬을 수행한 후, ICP로 반조밀 Aria 점군을 조밀 스캔에 정합.

### 지각-운동 훈련
- PPO를 Isaac Lab에서 훈련, Unitree G1 휴머노이드 로봇, 29 자유도 관절 위치 목표
- Actor는 고유수용감각, 참조 관절 명령, 요각 정렬 지형 높이 스캔을 관측; Critic은 특권 신체 상태 및 발목 접촉력을 추가로 수신
- 시간적 발 접촉 보상 도입; 에피소드 초기화는 비관통 프레임으로 제한, 앵커 또는 말단 효과기 드리프트 시 종료

## 핵심 혁신

1. **박수 소리 동기화로 하드와이어 대체**: 가장 실용적인 엔지니어링 혁신. PPS 케이블을 포기하면서 < 60 ms 정렬 오류가 발생했지만, 야외 수집의 이동 자유도를 얻었습니다. 30 fps 데이터 기준 60 ms 오류는 2프레임 미만으로 하위 운동 훈련에 미치는 영향은 무시할 수 있지만, 수집 프로세스는 크게 단순화되었습니다.
2. **SLAM 앵커링으로 IMU 드리프트 제거**: 신체 운동학을 모션캡처 슈트 자체 적분이 아닌 Aria 폐루프 궤적에 완전히 앵커링. 이 설계 결정으로 전역 궤적 정밀도(RTE 0.09%)가 전용 모션캡처 시스템에 필적하면서도 야외 배치 가능성을 유지합니다.
3. **교차 양식 검증 폐루프**: Qualisys 광학 진실값 부분집합(0.7시간)과 지각-운동 훈련 검증을 동시에 제공하여 '수집→재구성→훈련→배치'의 완전한 증거 체인을 형성. 이는 유사 데이터셋에서 드물며, 데이터 품질이 실제 로봇 정책 학습을 지원할 수 있음을 직접 증명합니다.

## 실험 및 결과

### 국소 자세 정밀도 비교(표 2)
| 방법 | MPJPE (mm) | PA-MPJPE (mm) |
|---|---|---|
| PROX '19 | 167.1 | 72.0 |
| HPS '21 | 93.1 | — |
| RICH '22 | 161.8 | 63.7 |
| SLOPER4D '23 | 78.01 | 55.4 |
| **EgoHTR (local)** | **73.2** | **54.3** |

EgoHTR은 SLOPER4D 대비 MPJPE 6.2% 감소(78.01→73.2 계산), PA-MPJPE 2.0% 감소(55.4→54.3 계산). 전역 지표 W-MPJPE 151.3 mm, WA-MPJPE 66.7 mm, RTE 0.09%.

### 발 접촉 보상 소거(표 3, 5개 시드 평균±표준편차)
| 지형 | 지표 | π0(보상 없음) | π1(보상 있음) |
|---|---|---|---|
| Flat | 최대 SR (%) | 99.0±0.1 | 99.0±0.1 |
| Flat | 수렴 스텝 (×10⁸) | 0.90±0.01 | 0.84±0.01 |
| Box up | 최대 SR (%) | 89.0±0.1 | 90.0±0.2 |
| Box up | 수렴 스텝 (×10⁸) | 1.23±0.07 | 1.08±0.02 |
| Beam | 최대 SR (%) | 96.0±0.1 | 96.0±0.1 |
| Beam | 수렴 스텝 (×10⁸) | 0.82±0.02 | 0.75±0.02 |
| S.Stones | 최대 SR (%) | 67.0±1.0 | 72.0±1.0 |
| S.Stones | 수렴 스텝 (×10⁸) | 7.14±0.65 | 5.72±0.21 |

발 접촉 보상은 S.Stones(가장 복잡한 지형)에서 가장 큰 향상을 보였으며(SR 67.0→72.0, 수렴 가속 1.42×10⁸ 스텝), 불규칙한 착지점 지형에서 특히 중요함을 시사합니다.

### 메시 복원 방법 벤치마크(표 4)
| 방법 | SR (%) | MPJPE | PA-M. | Jitter | W-M. | WA-M. | RTE | CD | Prec |
|---|---|---|---|---|---|---|---|---|---|
| JOSH | 57.18 | 101.5 | 66.5 | 2.02 | 321.3 | 138.2 | 2.26 | 0.71 | 73.11 |
| Human3R | 80.53 | 148.4 | 64.7 | 12.97 | 693.5 | 305.9 | 5.55 | 1.71 | 24.11 |
| EgoAllo | 100 | 161.1 | 111.5 | 0.14 | 392.7 | 167.1 | 0.14 | — | — |

EgoAllo는 성공률이 가장 높지만 정밀도가 가장 낮고, JOSH는 정밀도가 가장 우수하지만 성공률이 낮으며, Human3R은 지터가 심합니다(Jitter 12.97). EgoHTR의 참조 재구성(73.2 MPJPE)은 모든 메시 복원 방법보다 우수합니다.

### MoCap 진실값 검증(표 D.3)
EgoAllo는 EgoHTR과 MoCap GT에서 MPJPE 차이 3.6 mm(161.8 vs 158.2), JOSH는 차이 1.4 mm(89.4 vs 75.3). 참조 재구성은 MoCap GT에서 MPJPE 70.3, PA-MPJPE 56.4로 EgoHTR 결과(73.2, 54.3)와 유사하여 파이프라인 정밀도를 검증합니다.

### 참조 운동 정밀도 소거
훈련은 약 σ = 0.05 m까지의 노이즈를 허용하며, 오류가 0.1 m를 초과하면 훈련이 붕괴됩니다. 단안 방법은 거친 지형에서 전역 추정 오류가 일반적으로 0.1 m를 초과하므로, EgoHTR의 정밀도(국소 MPJPE 73.2 mm)가 훈련 가능한 구간의 경계에 정확히 위치함을 시사합니다.

## 경계 및 한계

- **규모 부족**: 1.37시간 데이터량(0.15M 프레임)은 NymeriaPlus(300시간) 등 대규모 데이터셋보다 훨씬 작아 다양성이 제한적이며, 일반화에 영향을 줄 수 있습니다.
- **정적 환경 가정**: 파이프라인은 관절 물체가 없는 정적 장면으로 제한되며, 동적 장애물이나 변형 가능한 지형을 처리할 수 없습니다.
- **손 모델링 없음**: Aria 글래스는 손 추적을 지원하지만 신체 모델에 포함되지 않았으며, 손 파라미터는 신원 자세로 고정되어 인간-물체 상호작용 작업을 제한합니다.
- **결합 최적화 없음**: 수집 후 인간-장면 결합 최적화를 수행하지 않아 재구성 정밀도에 추가 개선 여지가 있습니다.
- **하드웨어 물리적 제약**: 특징 없는 환경이나 고가속 기동에서 SLAM 또는 IMU가 실패할 수 있어 파이프라인 성능이 저하됩니다.
- **수행하지 않은 작업**: 후처리 최적화를 우회하기 위한 엔드투엔드 모델 미세 조정 미수행; 데이터셋을 운동 합성으로 확장하지 않음(모두 향후 작업으로 남김).

## 엔지니어링 시사점

- **재현 우선순위**: 시간 정렬 모듈을 먼저 확인하세요. 박수 소리 동기화는 48 kHz 오디오와 100 Hz IMU의 피크 감지에 의존하므로, 수집 환경의 배경 소음이 크면 수동 검증 단계를 추가하는 것이 좋습니다. 시퀀스 길이 5분 제한은 하드 제약이므로, 초과 시 분할 수집이 필요합니다.
- **가장 쉽게 실수하는 지점**: 공간 정렬의 ICP 세부 조정은 초기 대략적 정렬에 민감합니다. VGGT로 추정한 초기 변환이 너무 크게 벗어나면 ICP가 국소 최적해에 빠지기 쉽습니다. 특징이 풍부한 장면에서 수집하고, 스캐너 초기 이미지를 기하학 앵커로 유지하는 것이 좋습니다.
- **하위 훈련 적응**: 참조 운동 정밀도를 σ ≤ 0.05 m 이내로 제어해야 하며, 그렇지 않으면 정책 훈련이 붕괴됩니다. EgoHTR의 국소 MPJPE 73.2 mm는 이미 이 임계값에 근접하므로, 훈련에 사용할 경우 평활화 전처리를 먼저 수행하는 것이 좋습니다. 발 접촉 보상은 복잡한 지형(예: S.Stones)에서 뚜렷한 이득이 있으므로 기본 구성으로 채택해야 합니다.
- **하드웨어 선택**: 예산이 제한된 경우 두 번째 Aria 글래스와 고정 카메라를 생략하고 본체 3종 세트만으로 핵심 수집을 완료할 수 있습니다. Qualisys 진실값 부분집합은 0.7시간에 불과하며 주로 검증용이므로 필요에 따라 수집하세요.
