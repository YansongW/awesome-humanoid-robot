---
$id: ent_paper_wham_reconstructing_world_grounded_human_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion'
  zh: 'WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion'
  ko: 'WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion'
summary:
  en: The estimation of 3D human motion from video has progressed rapidly but current methods still have several key limitations.
    First, most methods estimate the human in camera coordinates. Second, prior work on estimating humans in global coordinates
    often assumes a flat ground plane and produces foot sliding. Third, the most accurate methods rely on computationally
    expensive optimization pipelines,.
  zh: WHAM 是 Max Planck 智能系统研究所等团队提出的单目视频全局 3D 人体运动重建方法，以 200 fps 的推理速度在 3DPW、RICH、EMDB 上达到逐帧精度 SOTA，同时保持时间平滑性。核心贡献在于将相机角速度（来自
    SLAM 或陀螺仪）与脚-地接触概率引入递归网络，解耦相机运动与人体运动，并通过接触感知轨迹细化抑制脚滑动。
  ko: The estimation of 3D human motion from video has progressed rapidly but current methods still have several key limitations.
    First, most methods estimate the human in camera coordinates. Second, prior work on estimating humans in global coordinates
    often assumes a flat ground plane and produces foot sliding. Third, the most accurate methods rely on computationally
    expensive optimization pipelines,.
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
- wham
- reconstructing
- world
- grounded
- human
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P121. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2312.07531 WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion'
  url: https://arxiv.org/abs/2312.07531
  date: '2023-12-12'
  accessed_at: '2026-08-05'
---

## 概述

WHAM 是 Max Planck 智能系统研究所等团队提出的单目视频全局 3D 人体运动重建方法，以 200 fps 的推理速度在 3DPW、RICH、EMDB 上达到逐帧精度 SOTA，同时保持时间平滑性。核心贡献在于将相机角速度（来自 SLAM 或陀螺仪）与脚-地接触概率引入递归网络，解耦相机运动与人体运动，并通过接触感知轨迹细化抑制脚滑动。

## 它改变了什么

现有全局人体运动估计存在一个根本性矛盾：要么依赖离线优化（如 SLAHMR）获得高精度但速度极慢（处理 1000 帧需 260 分钟），要么采用前馈网络但精度反而不如单帧方法。WHAM 改变了这一格局——它证明纯前馈、可在线推理的架构也能在全局坐标系下达到超越所有优化方法的精度，且速度提升 4 个数量级。这打破了"全局精度必须付出计算代价"的行业共识。

更关键的是，它改变了"相机运动"在人体运动估计中的角色。此前方法要么假设地面平坦（导致脚滑动），要么将相机运动视为需要联合优化的未知量。WHAM 将相机角速度作为显式输入（而非隐式估计），这一设计决策使得相机运动与人体运动在特征层面解耦，从而在动态手持相机场景下实现了此前只有离线优化才能达到的全局轨迹精度（RTE 8.8 m，较 SLAHMR 的 13.8 m 降低 36%）。

## 方法拆解

### 整体架构
输入原始视频序列，输出 SMPL 参数、全局根朝向和全局平移。流程分为三条并行支路：

1. **2D 关键点支路**：ViTPose 检测 2D 关键点，输入单向 RNN 运动编码器提取运动上下文。
2. **图像特征支路**：预训练且权重固定的图像编码器（如 ViT-H/16）提取密集视觉特征。
3. **相机角速度支路**：来自 SLAM（DPVO/DROID-SLAM）或相机陀螺仪，与运动特征拼接后输入全局轨迹解码器。

### 关键设计决策
- **中间任务**：运动解码器除输出 SMPL 参数外，还预测 3D 关键点作为中间运动表示，引导运动特征同时包含隐式运动上下文和身体 3D 空间结构。
- **特征整合**：图像特征通过残差连接与运动特征融合：`ϕ̂_m(t) = ϕ_m(t) + F_I(concat(ϕ_m(t), ϕ_i(t)))`，弥补稀疏 2D 关键点缺失的密集视觉上下文（如衣服褶皱、遮挡边界）。
- **全局轨迹解码**：将相机角速度与运动特征拼接，递归预测全局根朝向和自中心速度。全局平移通过 roll-out 积分计算，避免直接回归绝对位置带来的漂移。
- **接触感知轨迹细化**：先根据脚-地接触概率 `p̂(t)=1/(1+e^(α(v(t)-v_t)/v_t))`（阈值速度 v_t=1cm/frame，系数 α=5）调整自中心速度以减少脚滑动，再通过轨迹细化网络更新根朝向和速度，最后 roll-out 得到全局平移。

### 训练策略
两阶段训练：先在 AMASS 合成数据（6.7M 帧，序列长度 L=81）上预训练运动编码器和解码器，再在真实视频数据集（3DPW、Human3.6M、MPI-INF-3DHP、InstaVariety）上微调并训练特征整合器。合成数据使用动态虚拟相机（含旋转和平移）投影 3D 关键点，并添加噪声和随机掩码（平均概率 p=0.15）增强。

## 关键创新

1. **相机角速度作为显式输入而非隐式估计**：这是全局轨迹精度的关键。此前方法要么联合优化相机参数（SLAHMR），要么假设静态相机。WHAM 将角速度作为外部信号（SLAM 或陀螺仪）直接输入，使网络无需从 RGB 中隐式推断相机运动，大幅降低学习难度。消融实验显示，去掉角速度输入后 RTE 从 8.8 m 恶化至 18.3 m（由表内数值 8.8→18.3 计算），ROE 从 40.4° 恶化至 77.1°。

2. **接触感知轨迹细化**：不同于仅用接触概率做后处理平滑，WHAM 将接触概率作为条件输入轨迹细化网络，递归更新根朝向和速度。这使得网络能主动抑制脚滑动，而非被动修正。消融实验显示，去掉该模块后 EFVE 从 19.8 mm/frame 恶化至 20.9 mm/frame。

3. **两阶段训练 + 合成数据增强**：在 AMASS 上预训练运动先验，再在真实数据上微调。合成数据使用动态虚拟相机（初始横滚角 γ_r(0)∼𝒩(0°,5°)，俯仰角 γ_p(0)∼𝒩(5°,22.5°)，变化量 Δγ_y∼𝒩(0°,45°)）模拟手持相机运动，使网络在训练阶段就见过相机运动与人体运动的耦合模式，这是泛化到真实动态场景的关键。

## 实验与结果

### 逐帧精度（3DPW 测试集）
| 方法 | PA-MPJPE (mm) | MPJPE (mm) | PVE (mm) | Accel (m/s²) |
|------|--------------|------------|----------|--------------|
| SLAHMR | 55.9 | – | – | – |
| GLAMR | 51.1 | – | – | 8.0 |
| HMR2.0 | 44.4 | 69.8 | 82.2 | 18.1 |
| WHAM (ViT) | 37.8 | 60.8 | 72.5 | 6.8 |
| WHAM-B (ViT) | 37.2 | 59.4 | 71.0 | 6.9 |

WHAM (ViT) 在 PA-MPJPE 上较 SLAHMR 降低 32%（由表内数值 55.9→37.8 计算），较 HMR2.0 降低 15%（由表内数值 44.4→37.8 计算），同时保持与时间方法相当的 Accel（6.8 vs 6.0-6.5）。

### 全局轨迹精度（EMDB 2）
| 方法 | RTE (m) | ROE (deg) | ERVE (mm/frame) |
|------|---------|-----------|-----------------|
| SLAHMR | 13.8 | 67.9 | 19.7 |
| GLAMR | 16.7 | 74.9 | 18.0 |
| WHAM (w/ DPVO) | 8.8 | 40.4 | 14.8 |
| WHAM (w/ GT gyro) | 7.1 | 26.3 | 14.8 |

WHAM 在 RTE 上较 SLAHMR 降低 36%（由表内数值 13.8→8.8 计算），ROE 降低 40%（由表内数值 67.9→40.4 计算）。使用 GT 陀螺仪时 RTE 进一步降至 7.1 m，说明角速度输入质量是全局轨迹精度的主要瓶颈。

### 消融实验（EMDB 2）
| 配置 | PA-MPJPE | RTE | ROE | ERVE |
|------|----------|-----|-----|------|
| w/o lifting | 108.9 | 18.5 | 98.3 | 29.4 |
| w/o ω | 40.7 | 18.3 | 77.1 | 14.4 |
| WHAM (Ours) | 41.9 | 8.8 | 40.4 | 14.8 |

去掉中间 3D 关键点提升任务（w/o lifting）导致 PA-MPJPE 从 41.9 恶化至 108.9，说明该中间任务对运动特征质量至关重要。去掉角速度输入（w/o ω）对逐帧精度影响不大（PA-MPJPE 40.7 vs 41.9），但 RTE 翻倍（18.3 vs 8.8），证明角速度仅影响全局轨迹。

### 运行速度
核心网络 200 fps；完整方法（含预处理）在线推理约 9 fps（batch size=1），批处理约 50 fps（batch size=64）。SLAHMR 处理 1000 帧需 260 分钟，WHAM 仅需 5 秒（由表内数值 260 分钟与 5 秒对比）。

## 边界与局限

- **非平坦地面失效**：依赖 AMASS 学习的人体运动先验，AMASS 中爬楼梯等非平坦地面数据有限，作者明确承认此类场景可能失效。
- **接触估计仅限脚部**：接触标签仅基于脚部速度生成，未扩展至手、膝等其他与场景接触的身体部位，限制了复杂交互场景的适用性。
- **角速度误差累积**：依赖 SLAM 或陀螺仪提供的角速度，误差会随时间累积导致全局轨迹漂移。消融实验显示，使用 GT 陀螺仪时 RTE 从 8.8 m 降至 7.1 m，说明当前 SLAM 输入仍有提升空间。
- **分布外运动泛化**：对骑自行车、滑板等 AMASS 未覆盖的运动模式泛化能力有限。
- **合成数据假设**：数据合成主要假设全身在视野内，随机掩码仅部分缓解遮挡问题，极端遮挡场景未充分验证。

## 工程启示

- **先核对角速度来源**：WHAM 的全局轨迹精度高度依赖角速度输入质量。复现时优先使用 GT 陀螺仪验证网络上限，再评估 SLAM（DPVO vs DROID-SLAM）的引入损失。若下游任务对全局轨迹敏感（如 AR 遮挡），建议预留陀螺仪接口。
- **图像编码器选择是精度杠杆**：从 ResNet-50（WHAM-Res）到 ViT-H/16（WHAM-ViT），PA-MPJPE 从 41.7 降至 37.8（由表内数值 41.7→37.8 计算）。若算力允许，直接上 ViT 编码器；若需实时，ResNet-50 仍优于所有先前方法。
- **最容易踩坑：中间任务不可省**：消融实验显示去掉 3D 关键点提升任务后 PA-MPJPE 恶化 160%（由表内数值 41.9→108.9 计算）。复现时务必保留该中间监督，不要为简化架构而删除。
- **训练数据顺序敏感**：先 AMASS 预训练再真实数据微调的顺序不可颠倒。若直接微调，运动先验不足会导致脚滑动和轨迹漂移。
- **批处理与在线推理速度差异大**：batch size=1 时完整流程仅 9 fps，batch size=64 时达 50 fps。若需实时在线应用，需接受约 9 fps 的帧率或优化预处理（边界框检测是关键瓶颈，batch size=1 时占 14.3 ms）。

## Overview
The estimation of 3D human motion from video has progressed rapidly but current methods still have several key limitations. First, most methods estimate the human in camera coordinates. Second, prior work on estimating humans in global coordinates often assumes a flat ground plane and produces foot sliding. Third, the most accurate methods rely on computationally expensive optimization pipelines, limiting their use to offline applications. Finally, existing video-based methods are surprisingly less accurate than single-frame methods. We address these limitations with WHAM (World-grounded Humans with Accurate Motion), which accurately and efficiently reconstructs 3D human motion in a global coordinate system from video. WHAM learns to lift 2D keypoint sequences to 3D using motion capture data and fuses this with video features, integrating motion context and visual information. WHAM exploits camera angular velocity estimated from a SLAM method together with human motion to estimate the body's global trajectory. We combine this with a contact-aware trajectory refinement method that lets WHAM capture human motion in diverse conditions, such as climbing stairs. WHAM outperforms all existing 3D human motion recovery methods across multiple in-the-wild benchmarks. Code will be available for research purposes at http://wham.is.tue.mpg.de/

## 参考
- https://arxiv.org/abs/2312.07531

## 개요

WHAM은 Max Planck 지능 시스템 연구소 등 팀이 제안한 단안 비디오 기반 전역 3D 인간 모션 재구성 방법으로, 200fps의 추론 속도로 3DPW, RICH, EMDB에서 프레임별 정확도 SOTA를 달성하면서 시간적 평활성을 유지합니다. 핵심 기여는 카메라 각속도(SLAM 또는 자이로스코프에서 획득)와 발-지면 접촉 확률을 순환 네트워크에 도입하여 카메라 모션과 인간 모션을 분리하고, 접촉 인식 궤적 세분화를 통해 발 미끄러짐을 억제하는 것입니다.

## 무엇을 바꾸었는가

기존 전역 인간 모션 추정에는 근본적인 모순이 있었습니다: 오프라인 최적화(예: SLAHMR)에 의존하면 높은 정확도를 얻을 수 있지만 속도가 매우 느리고(1000프레임 처리에 260분 소요), 피드포워드 네트워크를 사용하면 정확도가 단일 프레임 방법보다 오히려 떨어졌습니다. WHAM은 이러한 구도를 바꾸었습니다—순수 피드포워드, 온라인 추론이 가능한 아키텍처로도 전역 좌표계에서 모든 최적화 방법을 능가하는 정확도를 달성할 수 있고, 속도는 4자릿수 향상되었음을 증명했습니다. 이는 "전역 정확도는 계산 비용을 치러야 한다"는 업계의 통념을 깨뜨렸습니다.

더 중요하게는, 카메라 모션이 인간 모션 추정에서 차지하는 역할을 바꾸었습니다. 이전 방법들은 평평한 지면을 가정하거나(발 미끄러짐 유발), 카메라 모션을 공동 최적화해야 하는 미지수로 취급했습니다. WHAM은 카메라 각속도를 명시적 입력(암시적 추정이 아닌)으로 사용하는 설계 결정을 내렸고, 이를 통해 카메라 모션과 인간 모션이 특징 수준에서 분리되어 동적 핸드헬드 카메라 시나리오에서 이전에는 오프라인 최적화만이 달성할 수 있었던 전역 궤적 정확도(RTE 8.8m, SLAHMR의 13.8m 대비 36% 감소)를 구현했습니다.

## 방법 분석

### 전체 아키텍처
원본 비디오 시퀀스를 입력으로 받아 SMPL 파라미터, 전역 루트 방향, 전역 병진을 출력합니다. 프로세스는 세 개의 병렬 분기로 구성됩니다:

1. **2D 키포인트 분기**: ViTPose가 2D 키포인트를 감지하고, 단방향 RNN 모션 인코더에 입력하여 모션 컨텍스트를 추출합니다.
2. **이미지 특징 분기**: 사전 학습되고 가중치가 고정된 이미지 인코더(예: ViT-H/16)가 밀집 시각적 특징을 추출합니다.
3. **카메라 각속도 분기**: SLAM(DPVO/DROID-SLAM) 또는 카메라 자이로스코프에서 획득하며, 모션 특징과 결합된 후 전역 궤적 디코더에 입력됩니다.

### 핵심 설계 결정
- **중간 작업**: 모션 디코더는 SMPL 파라미터 외에도 3D 키포인트를 중간 모션 표현으로 예측하여, 모션 특징이 암시적 모션 컨텍스트와 신체 3D 공간 구조를 동시에 포함하도록 유도합니다.
- **특징 통합**: 이미지 특징은 잔차 연결을 통해 모션 특징과 융합됩니다: `ϕ̂_m(t) = ϕ_m(t) + F_I(concat(ϕ_m(t), ϕ_i(t)))`, 희소한 2D 키포인트가 놓치는 밀집 시각적 컨텍스트(예: 옷 주름, 폐색 경계)를 보완합니다.
- **전역 궤적 디코딩**: 카메라 각속도와 모션 특징을 결합하여 전역 루트 방향과 자체 중심 속도를 재귀적으로 예측합니다. 전역 병진은 롤아웃 적분으로 계산되어 절대 위치 직접 회귀로 인한 드리프트를 피합니다.
- **접촉 인식 궤적 세분화**: 먼저 발-지면 접촉 확률 `p̂(t)=1/(1+e^(α(v(t)-v_t)/v_t))`(임계 속도 v_t=1cm/frame, 계수 α=5)을 기반으로 자체 중심 속도를 조정하여 발 미끄러짐을 줄이고, 궤적 세분화 네트워크를 통해 루트 방향과 속도를 업데이트한 후 롤아웃으로 전역 병진을 얻습니다.

### 훈련 전략
두 단계 훈련: 먼저 AMASS 합성 데이터(670만 프레임, 시퀀스 길이 L=81)에서 모션 인코더와 디코더를 사전 훈련하고, 실제 비디오 데이터셋(3DPW, Human3.6M, MPI-INF-3DHP, InstaVariety)에서 미세 조정 및 특징 통합기를 훈련합니다. 합성 데이터는 동적 가상 카메라(회전 및 병진 포함)로 3D 키포인트를 투영하고, 노이즈와 무작위 마스킹(평균 확률 p=0.15)을 추가하여 증강합니다.

## 핵심 혁신

1. **카메라 각속도를 암시적 추정이 아닌 명시적 입력으로 사용**: 이는 전역 궤적 정확도의 핵심입니다. 이전 방법들은 카메라 파라미터를 공동 최적화하거나(SLAHMR), 정적 카메라를 가정했습니다. WHAM은 각속도를 외부 신호(SLAM 또는 자이로스코프)로 직접 입력하여 네트워크가 RGB에서 카메라 모션을 암시적으로 추론할 필요가 없게 하여 학습 난이도를 크게 낮췄습니다. 절제 실험에서 각속도 입력을 제거하면 RTE가 8.8m에서 18.3m로 악화되고(표 내 수치 8.8→18.3 계산), ROE가 40.4°에서 77.1°로 악화됩니다.

2. **접촉 인식 궤적 세분화**: 접촉 확률을 후처리 평활화에만 사용하는 것과 달리, WHAM은 접촉 확률을 궤적 세분화 네트워크의 조건 입력으로 사용하여 루트 방향과 속도를 재귀적으로 업데이트합니다. 이를 통해 네트워크가 수동적으로 수정하는 대신 능동적으로 발 미끄러짐을 억제할 수 있습니다. 절제 실험에서 이 모듈을 제거하면 EFVE가 19.8mm/frame에서 20.9mm/frame으로 악화됩니다.

3. **두 단계 훈련 + 합성 데이터 증강**: AMASS에서 모션 사전을 사전 훈련한 후 실제 데이터에서 미세 조정합니다. 합성 데이터는 동적 가상 카메라(초기 롤 각도 γ_r(0)∼𝒩(0°,5°), 피치 각도 γ_p(0)∼𝒩(5°,22.5°), 변화량 Δγ_y∼𝒩(0°,45°))로 핸드헬드 카메라 모션을 시뮬레이션하여, 네트워크가 훈련 단계에서 카메라 모션과 인간 모션의 결합 패턴을 경험하게 하며, 이는 실제 동적 장면으로의 일반화에 핵심입니다.

## 실험 및 결과

### 프레임별 정확도(3DPW 테스트 세트)
| 방법 | PA-MPJPE (mm) | MPJPE (mm) | PVE (mm) | Accel (m/s²) |
|------|--------------|------------|----------|--------------|
| SLAHMR | 55.9 | – | – | – |
| GLAMR | 51.1 | – | – | 8.0 |
| HMR2.0 | 44.4 | 69.8 | 82.2 | 18.1 |
| WHAM (ViT) | 37.8 | 60.8 | 72.5 | 6.8 |
| WHAM-B (ViT) | 37.2 | 59.4 | 71.0 | 6.9 |

WHAM (ViT)은 PA-MPJPE에서 SLAHMR 대비 32% 감소(표 내 수치 55.9→37.8 계산), HMR2.0 대비 15% 감소(표 내 수치 44.4→37.8 계산)하면서 시간적 방법과 동등한 Accel(6.8 vs 6.0-6.5)을 유지합니다.

### 전역 궤적 정확도(EMDB 2)
| 방법 | RTE (m) | ROE (deg) | ERVE (mm/frame) |
|------|---------|-----------|-----------------|
| SLAHMR | 13.8 | 67.9 | 19.7 |
| GLAMR | 16.7 | 74.9 | 18.0 |
| WHAM (w/ DPVO) | 8.8 | 40.4 | 14.8 |
| WHAM (w/ GT gyro) | 7.1 | 26.3 | 14.8 |

WHAM은 RTE에서 SLAHMR 대비 36% 감소(표 내 수치 13.8→8.8 계산), ROE 40% 감소(표 내 수치 67.9→40.4 계산)를 달성합니다. GT 자이로스코프 사용 시 RTE가 7.1m로 추가 감소하여, 각속도 입력 품질이 전역 궤적 정확도의 주요 병목임을 시사합니다.

### 절제 실험(EMDB 2)
| 구성 | PA-MPJPE | RTE | ROE | ERVE |
|------|----------|-----|-----|------|
| w/o lifting | 108.9 | 18.5 | 98.3 | 29.4 |
| w/o ω | 40.7 | 18.3 | 77.1 | 14.4 |
| WHAM (Ours) | 41.9 | 8.8 | 40.4 | 14.8 |

중간 3D 키포인트 리프팅 작업 제거(w/o lifting)는 PA-MPJPE가 41.9에서 108.9로 악화되어, 이 중간 작업이 모션 특징 품질에 매우 중요함을 보여줍니다. 각속도 입력 제거(w/o ω)는 프레임별 정확도에 큰 영향을 미치지 않지만(PA-MPJPE 40.7 vs 41.9), RTE가 두 배로 증가(18.3 vs 8.8)하여 각속도가 전역 궤적에만 영향을 미친다는 것을 증명합니다.

### 실행 속도
핵심 네트워크 200fps; 전체 방법(전처리 포함) 온라인 추론 약 9fps(batch size=1), 배치 처리 약 50fps(batch size=64). SLAHMR은 1000프레임 처리에 260분이 필요하지만, WHAM은 5초면 충분합니다(표 내 수치 260분과 5초 비교).

## 경계 및 한계

- **비평평 지면에서 실패**: AMASS에서 학습된 인간 모션 사전에 의존하며, AMASS의 계단 오르기 등 비평평 지면 데이터가 제한적이어서 저자는 이러한 장면에서 실패할 수 있음을 명시적으로 인정합니다.
- **접촉 추정이 발에만 국한**: 접촉 레이블이 발 속도에만 기반하여 생성되며, 손, 무릎 등 장면과 접촉하는 다른 신체 부위로 확장되지 않아 복잡한 상호작용 장면 적용이 제한됩니다.
- **각속도 오류 누적**: SLAM 또는 자이로스코프에서 제공하는 각속도에 의존하며, 오류가 시간에 따라 누적되어 전역 궤적 드리프트를 유발할 수 있습니다. 절제 실험에서 GT 자이로스코프 사용 시 RTE가 8.8m에서 7.1m로 감소하여 현재 SLAM 입력에 개선 여지가 있음을 보여줍니다.
- **분포 외 모션 일반화**: 자전거 타기, 스케이트보드 등 AMASS가 포함하지 않는 모션 패턴에 대한 일반화 능력이 제한적입니다.
- **합성 데이터 가정**: 데이터 합성은 주로 전신이 시야 내에 있음을 가정하며, 무작위 마스킹은 폐색 문제를 부분적으로만 완화하므로 극단적 폐색 장면은 충분히 검증되지 않았습니다.

## 엔지니어링 시사점

- **각속도 소스 먼저 확인**: WHAM의 전역 궤적 정확도는 각속도 입력 품질에 크게 의존합니다. 재현 시 GT 자이로스코프로 네트워크 상한을 먼저 검증한 후 SLAM(DPVO vs DROID-SLAM) 도입 손실을 평가하세요. 다운스트림 작업이 전역 궤적에 민감한 경우(예: AR 폐색), 자이로스코프 인터페이스를预留하는 것이 좋습니다.
- **이미지 인코더 선택이 정확도 레버**: ResNet-50(WHAM-Res)에서 ViT-H/16(WHAM-ViT)으로, PA-MPJPE가 41.7에서 37.8로 감소합니다(표 내 수치 41.7→37.8 계산). 연산 능력이 허용되면 ViT 인코더를 직접 사용하고, 실시간이 필요하면 ResNet-50도 모든 이전 방법보다 우수합니다.
- **가장 쉽게 빠지는 함정: 중간 작업 생략 불가**: 절제 실험에서 3D 키포인트 리프팅 작업 제거 시 PA-MPJPE가 160% 악화됩니다(표 내 수치 41.9→108.9 계산). 재현 시 이 중간 감독을 반드시 유지하고, 아키텍처 단순화를 위해 삭제하지 마세요.
- **훈련 데이터 순서 민감**: AMASS 사전 훈련 후 실제 데이터 미세 조정 순서는 바꿀 수 없습니다. 직접 미세 조정하면 모션 사전 부족으로 발 미끄러짐과 궤적 드리프트가 발생합니다.
- **배치 처리와 온라인 추론 속도 차이 큼**: batch size=1에서 전체 프로세스는 9fps에 불과하지만, batch size=64에서는 50fps에 도달합니다. 실시간 온라인 애플리케이션이 필요하면 약 9fps의 프레임률을 수용하거나 전처리(경계 상자 감지가 핵심 병목, batch size=1에서 14.3ms 차지)를 최적화해야 합니다.
