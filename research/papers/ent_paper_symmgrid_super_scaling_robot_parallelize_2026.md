---
$id: ent_paper_symmgrid_super_scaling_robot_parallelize_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception'
  zh: 'SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception'
  ko: 'SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception'
summary:
  en: Deep reinforcement policy learning directly in physical robots (on-robot learning) remains bottlenecked by slow wall-clock
    training times. We present SymmGrid, a trajectory level augmentation framework inspired by parallelized symmetries that
    super-scales group transformations to significantly accelerate on-robot learning in both egocentric and exocentric visual
    setups. We model a Markov Decision.
  zh: SymmGrid 是一个面向真实机器人上深度强化学习（on-robot RL）的轨迹级数据增强框架，通过并行化平移对称性（branched symmetries）超缩放数据生成，并针对自我中心（egocentric）与外部中心（exocentric）视觉分别采用指针复用与单应性（homography）扭曲策略。作者在
    Franka 机器人上验证了插销、线缆布线与物体搬运三类任务，相比 SOTA 基线 SERL 实现了 1.37–2.17 倍的墙钟训练收敛加速与 1.09–1.27 倍的评估成功率提升。
  ko: Deep reinforcement policy learning directly in physical robots (on-robot learning) remains bottlenecked by slow wall-clock
    training times. We present SymmGrid, a trajectory level augmentation framework inspired by parallelized symmetries that
    super-scales group transformations to significantly accelerate on-robot learning in both egocentric and exocentric visual
    setups. We model a Markov Decision.
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
- symmgrid
- super
- scaling
- robot
- parallelize
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.26985 SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egoce'
  url: https://arxiv.org/abs/2607.26985
  date: '2026-07-29'
  accessed_at: '2026-08-05'
---

## 概述

SymmGrid 是一个面向真实机器人上深度强化学习（on-robot RL）的轨迹级数据增强框架，通过并行化平移对称性（branched symmetries）超缩放数据生成，并针对自我中心（egocentric）与外部中心（exocentric）视觉分别采用指针复用与单应性（homography）扭曲策略。作者在 Franka 机器人上验证了插销、线缆布线与物体搬运三类任务，相比 SOTA 基线 SERL 实现了 1.37–2.17 倍的墙钟训练收敛加速与 1.09–1.27 倍的评估成功率提升。

## 它改变了什么

现有 on-robot 学习方法（如 SERL）的墙钟训练时间约为 20–180 分钟，且通常需要约 20 个演示启动，这种速度不足以支撑野外快速部署。作者认为瓶颈不仅在于样本效率，更在于每个物理交互产生的数据量太少——每次真实转移只能为回放缓冲区贡献一条经验，而深度 RL 恰恰需要海量数据。SymmGrid 真正改变的是“数据生成”的粒度：它不再依赖算法在样本效率上的微调，而是通过数学上可容许的对称变换，将每一次物理转移在逻辑上“复制”为数百条等价经验，从而在相同墙钟时间内大幅提高回放缓冲区的周转率与多样性。这一思路将加速问题从“如何更省地学”转向“如何更便宜地造数据”，且不改变底层 RL 算法（仍为 SAC 类离策略方法），因此具有即插即用的工程价值。

## 方法拆解

### 对称树与网格生成
- 将 MDP 建模为对称树 𝒢=(V,E)，深度 h，顶点 v_k 描述姿态 x∈ℝⁿ，通过仿射变换 T_k(x)=Ax+t_k 生成，其中 A∈O(n) 为正交群成员，t∈ℝⁿ 为平移。
- 采用恒定分支策略 b_const(0)，产生 K×K 网格几何结构（K∈ℤ），例如 K=27 时共 729 个顶点（含原始轨迹），所有变换并行计算。
- 对称算子 σ(·):T_k(·)=I(·)+t_k，仅作用于状态的位置分量与动作（动作变换平凡：σ_{t_k}(a)=a），即 σ_{t_k}(τ)=(σ_{t_k}(s), a)。

### 对称工作空间（SymWS）
- 定义方形 SymWS，始终以末端执行器位置为中心，宽度可调（如 0.3 m 或 0.175 m）。
- 分支定位由 t_{k_x,k_y} 控制：t_{k_x,k_y}=SymWS_(0,0)+(2*b_{i,j}-1)*SymWS/(2*b_{c_h})（公式 1），其中 SymWS_(0,0)=s_(x,y,·)-SymWS_width/2。

### 视觉处理：自我中心 vs 外部中心
- 自我中心：视觉场景在对称分支下不变，使用基于指针的系统避免复制相同图像，仅修改原始状态图像 K² 次。
- 外部中心：全局固定相机无法随分支移动，需在采样时通过单应性扭曲图像。单应性 H(Δ)=MT(Δ)M⁻¹（公式 2），利用校准矩阵 M 将平面齐次坐标映射到图像像素坐标（公式 3），用 OpenCV 的 findHomography() 计算。采用反向映射（backward mapping）避免空洞，边缘像素复制为填充策略。
- 回放缓冲区附加索引，指示该转换经历的变换，采样时用索引提取对应变换并就地计算。

### 网络与训练
- 预训练 ResNet-10 视觉骨干，连接本体感觉信息，通过 2 层 MLP 处理策略和 Q 网络。
- 策略输出 6D 或 7D 末端执行器增量姿态，角度更新限制在 ±0.01 rad（滚转/俯仰）与 ±π/6（偏航），仅允许绕 z 轴旋转。
- 使用 RLPD 算法，20 个演示启动（对象重定位 30 个），回放缓冲区 360 万条目（3.6），采样 50% 来自先验与在线数据。

## 关键创新

1. **轨迹级并行化对称性**：不同于常见的图像级增强（如随机裁剪、颜色抖动），SymmGrid 在轨迹层面施加全局仿射变换，且变换是 MDP 的不变映射（保持奖励不变）。这使得增强数据不仅改变观测外观，还对应着物理上可执行的状态-动作对，从而让策略在局部利用全局学习的动力学。
2. **双视觉模态的统一处理**：自我中心场景下平移对称性天然成立，采用指针复用避免图像复制；外部中心场景下通过预计算单应性矩阵（H_b(Δ)=MT_b(Δ)M⁻¹）在采样时实时扭曲图像。这一设计使得框架能同时覆盖腕装相机与全局固定相机，且计算开销可控（仅修改原始图像 K² 次）。
3. **计算与内存效率**：利用恒定分支中反向映射可预先计算的特性，避免每次调用 findHomography() 的重复计算；回放缓冲区仅存储索引而非复制图像，显著降低内存占用。这使得 729 个对称分支的并行生成在单张 RTX 4070 上即可完成。

## 实验与结果

实验在真实 Franka FR3 机器人上进行，基线为 SERL（RLPD 算法，阻抗控制器 1K Hz）。评估指标为 50 个样本的平均成功率（训练）与 50 次任务尝试的成功率（评估），并采用 nAUC（归一化曲线下面积）衡量整体效率。

| 任务 | 指标 | SERL | SymmGrid | 变化 |
|------|------|------|----------|------|
| Peg insertion | 训练收敛时间 | 26 min | 18.5 min | 1.41× 加速（减少 28.8%） |
| Peg insertion | 90% 成功率时间 | 20.13 min | 15.9 min | 26.6% 加速 |
| Peg insertion | nAUC（3500 步） | 0.499 | 0.607 | 1.22× 增加 |
| Cable routing | 训练收敛（98%） | 25 min 内未达（最大 74.8%） | 22.8 min | 论文未明确 |
| Cable routing | 90% 成功率时间 | 20.13 min | 15.9 min | 21% 时间减少 |
| Cable routing | nAUC（6000 步） | 0.58 | 0.63 | 9.0% 增加 |
| Object relocation | 训练收敛（92%） | 130.0 min | 94.6 min | 37.4% 加速 |
| Object relocation | 10k 步评估成功率 | 74.7%（前向）/ 79.3%（后向） | 99.3% / 95.3% | 增益 33.0% / 20.2% |
| Object relocation | nAUC | 0.1911 | 0.494 | 2.59× 比率 |

关键结果解读：Peg insertion 中 SymmGrid 在 20.13 分钟达到 96.4% 成功率（SERL 在 22.7 分钟，1.28× 加速）；Cable routing 中 SymmGrid 在 11.0 分钟达到 SERL 23.9 分钟才实现的 78.9% 成功率（117.3% 加速）；Object relocation 中 SymmGrid 在 5851 步达到 SERL 10000 步的 60% 成功率（70% 改进）。值得注意的是，硬件对比中 SymmGrid 使用 RTX 4070（29.1 TFLOP FP32），而 SERL 原始结果使用 RTX 4090（82.6 TFLOP），计算能力相差 2.84 倍，带宽相差 2 倍（504 vs 1008 GB/s），SymmGrid 在更弱硬件上仍取得加速，进一步凸显方法效率。

## 边界与局限

- 仅使用纯平移变换，未涉及旋转或其他仿射变换；对于需要旋转对称性的任务（如拧螺丝），框架需扩展。
- 外部中心场景中，全局变换会同时作用于代理与对象，背景场景与多深度（桌面、托盘、物体、机器人）引入视差、插值与边界伪影；增大网格会降低未变形观测比例，使缓冲区分布偏离真实观测。
- Object relocation 的最佳配置（3 分支、0.175 m 工作空间）与另两个任务（27 分支、0.3 m）不同，表明外中心场景下对称性增益有限，参数需逐任务调优。
- Cable-routing 评估结果存在较大散布，作者承认可能需要更多种子或进一步分析。
- 未实现光随机化（RLPD 不实现），对光照变化敏感，需一致照明才能成功训练。
- 仅处理 RGB 图像与本体感觉，未涉及点云等更复杂表示。
- 论文未明确提及仿真训练或迁移学习、人形机器人实验及多任务泛化。

## 工程启示

- **复现优先核对**：先确认对称工作空间（SymWS）宽度与分支数 K 的匹配关系——公式 1 中 t_{k_x,k_y} 的边界条件直接决定网格覆盖范围，若 SymWS 超出机器人实际工作空间，增强数据将对应不可达状态，导致策略学习失效。
- **外中心场景最易踩坑**：单应性校准必须使用与学习系统相同参考坐标系（末端执行器框架），且校准点需跨越整个工作空间（如 20 个非共线点，RMSE 1.387 px）。若校准误差超过 3 px（内点最大误差 2.240 px），扭曲图像将引入系统性偏差，建议先单独验证单应性精度再启动训练。
- **回放缓冲区比例监控**：增大 K 会降低未变形观测比例，导致视觉编码器利用伪影而非几何信息。建议在训练中监控缓冲区中原始观测占比，若低于 50% 需减小 K 或增大缓冲区容量（3.6 百万条目为参考）。
- **硬件需求低于预期**：SymmGrid 在 RTX 4070（12 GB VRAM）上即可运行，但需注意反向映射的预计算与 remap() 的就地调用——若在采样时重复调用 findHomography() 会显著拖慢训练，务必预先计算 H_b(Δ) 并缓存。
- **下游团队选型建议**：对于自我中心视觉任务（腕装相机），SymmGrid 可直接套用 27 分支与 0.3 m 工作空间；对于外部中心视觉任务，建议从 3 分支与 0.175 m 起步，并优先验证单应性伪影对策略的影响。

## Overview
Deep reinforcement policy learning directly in physical robots (on-robot learning) remains bottlenecked by slow wall-clock training times. We present SymmGrid, a trajectory level augmentation framework inspired by parallelized symmetries that super-scales group transformations to significantly accelerate on-robot learning in both egocentric and exocentric visual setups. We model a Markov Decision Process (MDP) under a symmetry tree, in which state-action pairs have admissible parallelized invariant transformations that yield a geometric grid structure. The state is modelled with ego- or exocentric images and proprioception information. The latter require special treatment, in the form of homographies, to warp visual scenes in line with their corresponding spatial transformations. These parallelized transformations produce a large set of unique symmetric equivalences that populate the replay buffer with diverse and consistent experiences that speed up learning and improve performance. We present extensive training and evaluations performed directly on real robot manipulation contact tasks including peg-insertions, cable routing, and object relocations. Relative to SOTA, SymmGrid achieved wall-clock training convergence speed-ups of 1.37-2.17x, evaluation success rate improvements of 1.09x-1.27x, fastest training convergence times of 16.6, 10.9, and 79.3 minutes respectively. For trajectory wide assessments, we used normalized area under the curve (nAUC) ratios. SymmGrid achieved improvements of up to 2.59x. These results confirm that simple branch symmetries can have an outsized result due to super-scaling and bring us closer to sub-10 minute on-robot learning training in manipulation tasks suitable for arms and humanoids. The project page is available at symmgrid-robot.github.io

## 参考
- https://arxiv.org/abs/2607.26985

## 개요

SymmGrid는 실제 로봇에서의 심층 강화 학습(on-robot RL)을 위한 궤적 수준 데이터 증강 프레임워크로, 병렬화된 평행 이동 대칭성(branched symmetries)을 통해 데이터 생성을 초대규모로 확장하며, 자기중심(egocentric) 및 외부중심(exocentric) 비전에 대해 각각 포인터 재사용과 호모그래피(homography) 왜곡 전략을 적용한다. 저자들은 Franka 로봇에서 핀 삽입, 케이블 배선, 물체 운반 세 가지 작업을 검증했으며, SOTA 베이스라인인 SERL 대비 벽시계 기준 훈련 수렴 속도를 1.37–2.17배, 평가 성공률을 1.09–1.27배 향상시켰다.

## 무엇을 바꾸었는가

기존 on-robot 학습 방법(예: SERL)의 벽시계 훈련 시간은 약 20–180분이며, 일반적으로 약 20개의 데모로 시작해야 한다. 이러한 속도로는 야외에서의 빠른 배포를 지원하기 어렵다. 저자들은 병목이 샘플 효율성뿐만 아니라 각 물리적 상호작용에서 생성되는 데이터 양이 너무 적다는 점에 있다고 본다—실제 전이 한 번이 리플레이 버퍼에 기여하는 경험은 단 하나뿐이며, 심층 RL은 바로 방대한 데이터를 필요로 한다. SymmGrid가 실제로 바꾸는 것은 "데이터 생성"의 세분화 수준이다. 더 이상 알고리즘의 샘플 효율성 미세 조정에 의존하지 않고, 수학적으로 허용 가능한 대칭 변환을 통해 각 물리적 전이를 논리적으로 수백 개의 동등한 경험으로 "복제"하여, 동일한 벽시계 시간 내에 리플레이 버퍼의 회전율과 다양성을 크게 향상시킨다. 이 접근 방식은 가속 문제를 "더 절약하며 학습하는 방법"에서 "더 저렴하게 데이터를 만드는 방법"으로 전환하며, 기본 RL 알고리즘(여전히 SAC 계열의 off-policy 방법)을 변경하지 않으므로 플러그 앤 플레이 방식의 엔지니어링 가치를 지닌다.

## 방법 분해

### 대칭 트리 및 그리드 생성
- MDP를 대칭 트리 𝒢=(V,E)로 모델링하며, 깊이 h, 정점 v_k는 자세 x∈ℝⁿ을 설명하고, 아핀 변환 T_k(x)=Ax+t_k를 통해 생성된다. 여기서 A∈O(n)은 직교군의 원소이고, t∈ℝⁿ은 평행 이동이다.
- 일정 분기 전략 b_const(0)을 사용하여 K×K 그리드 기하 구조(K∈ℤ)를 생성한다. 예를 들어 K=27일 때 총 729개의 정점(원본 궤적 포함)이 생성되며, 모든 변환은 병렬로 계산된다.
- 대칭 연산자 σ(·):T_k(·)=I(·)+t_k는 상태의 위치 성분과 행동에만 작용한다(행동 변환은 자명함: σ_{t_k}(a)=a), 즉 σ_{t_k}(τ)=(σ_{t_k}(s), a).

### 대칭 작업 공간(SymWS)
- 정사각형 SymWS를 정의하며, 항상 엔드 이펙터 위치를 중심으로 하고, 폭은 조정 가능하다(예: 0.3 m 또는 0.175 m).
- 분기 위치는 t_{k_x,k_y}에 의해 제어된다: t_{k_x,k_y}=SymWS_(0,0)+(2*b_{i,j}-1)*SymWS/(2*b_{c_h}) (수식 1), 여기서 SymWS_(0,0)=s_(x,y,·)-SymWS_width/2.

### 비전 처리: 자기중심 vs 외부중심
- 자기중심: 비전 장면은 대칭 분기 아래에서 불변이므로, 포인터 기반 시스템을 사용하여 동일한 이미지 복사를 피하고 원본 상태 이미지만 K²번 수정한다.
- 외부중심: 전역 고정 카메라는 분기에 따라 이동할 수 없으므로, 샘플링 시 호모그래피로 이미지를 왜곡해야 한다. 호모그래피 H(Δ)=MT(Δ)M⁻¹ (수식 2)는 캘리브레이션 행렬 M을 이용해 평면 동차 좌표를 이미지 픽셀 좌표로 매핑하며(수식 3), OpenCV의 findHomography()로 계산한다. 역방향 매핑(backward mapping)을 사용하여 빈 구멍을 피하고, 가장자리 픽셀 복사를 채움 전략으로 사용한다.
- 리플레이 버퍼에는 해당 전이가 겪은 변환을 나타내는 인덱스가 추가되며, 샘플링 시 인덱스로 해당 변환을 추출하여 제자리에서 계산한다.

### 네트워크 및 훈련
- 사전 훈련된 ResNet-10 비전 백본을 사용하고, 고유수용감각 정보를 연결하여 2층 MLP로 정책과 Q 네트워크를 처리한다.
- 정책은 6D 또는 7D 엔드 이펙터 증분 자세를 출력하며, 각도 업데이트는 ±0.01 rad(롤/피치) 및 ±π/6(요)로 제한되고, z축 회전만 허용된다.
- RLPD 알고리즘을 사용하며, 20개의 데모로 시작(객체 재배치는 30개), 리플레이 버퍼는 360만 개 항목(3.6), 샘플링은 사전 및 온라인 데이터에서 50%씩 수행된다.

## 핵심 혁신

1. **궤적 수준 병렬화 대칭성**: 일반적인 이미지 수준 증강(예: 무작위 크롭, 색상 지터)과 달리, SymmGrid는 궤적 수준에서 전역 아핀 변환을 적용하며, 이 변환은 MDP의 불변 매핑(보상을 유지)이다. 이를 통해 증강 데이터는 관측 외관만 바꿀 뿐만 아니라 물리적으로 실행 가능한 상태-행동 쌍에 대응하므로, 정책이 로컬에서 전역 학습된 역학을 활용할 수 있다.
2. **이중 비전 모달리티의 통합 처리**: 자기중심 장면에서는 평행 이동 대칭성이 자연스럽게 성립하므로 포인터 재사용으로 이미지 복사를 피하고, 외부중심 장면에서는 사전 계산된 호모그래피 행렬(H_b(Δ)=MT_b(Δ)M⁻¹)을 통해 샘플링 시 실시간으로 이미지를 왜곡한다. 이 설계는 손목 장착 카메라와 전역 고정 카메라를 모두 포괄할 수 있으며, 계산 오버헤드가 제어 가능하다(원본 이미지만 K²번 수정).
3. **계산 및 메모리 효율성**: 일정 분기에서 역방향 매핑을 사전 계산할 수 있는 특성을 활용하여 findHomography() 호출의 반복 계산을 피하고, 리플레이 버퍼는 이미지를 복사하지 않고 인덱스만 저장하므로 메모리 사용량이 크게 줄어든다. 이를 통해 729개 대칭 분기의 병렬 생성이 단일 RTX 4070에서 완료될 수 있다.

## 실험 및 결과

실험은 실제 Franka FR3 로봇에서 수행되었으며, 베이스라인은 SERL(RLPD 알고리즘, 임피던스 컨트롤러 1K Hz)이다. 평가 지표는 50개 샘플의 평균 성공률(훈련)과 50회 작업 시도의 성공률(평가)이며, nAUC(정규화 곡선 아래 면적)로 전체 효율성을 측정한다.

| 작업 | 지표 | SERL | SymmGrid | 변화 |
|------|------|------|----------|------|
| 핀 삽입 | 훈련 수렴 시간 | 26분 | 18.5분 | 1.41× 가속(28.8% 감소) |
| 핀 삽입 | 90% 성공률 도달 시간 | 20.13분 | 15.9분 | 26.6% 가속 |
| 핀 삽입 | nAUC(3500步) | 0.499 | 0.607 | 1.22× 증가 |
| 케이블 배선 | 훈련 수렴(98%) | 25분 내 미달(최대 74.8%) | 22.8분 | 논문에서 명시 안 함 |
| 케이블 배선 | 90% 성공률 도달 시간 | 20.13분 | 15.9분 | 21% 시간 감소 |
| 케이블 배선 | nAUC(6000步) | 0.58 | 0.63 | 9.0% 증가 |
| 객체 재배치 | 훈련 수렴(92%) | 130.0분 | 94.6분 | 37.4% 가속 |
| 객체 재배치 | 10k步 평가 성공률 | 74.7%(전방)/79.3%(후방) | 99.3%/95.3% | 이득 33.0%/20.2% |
| 객체 재배치 | nAUC | 0.1911 | 0.494 | 2.59× 비율 |

주요 결과 해석: 핀 삽입에서 SymmGrid는 20.13분에 96.4% 성공률을 달성(SERL은 22.7분, 1.28× 가속); 케이블 배선에서 SymmGrid는 11.0분에 SERL이 23.9분에 달성한 78.9% 성공률을 달성(117.3% 가속); 객체 재배치에서 SymmGrid는 5851步에 SERL이 10000步에 달성한 60% 성공률을 달성(70% 개선). 주목할 점은 하드웨어 비교에서 SymmGrid는 RTX 4070(29.1 TFLOP FP32)을 사용한 반면, SERL 원본 결과는 RTX 4090(82.6 TFLOP)을 사용하여 계산 능력이 2.84배, 대역폭이 2배(504 vs 1008 GB/s) 차이가 났음에도, SymmGrid는 더 약한 하드웨어에서도 가속을 달성하여 방법의 효율성을 더욱 부각시킨다.

## 경계 및 한계

- 순수 평행 이동 변환만 사용하며, 회전이나 기타 아핀 변환은 포함하지 않는다. 회전 대칭성이 필요한 작업(예: 나사 조이기)에서는 프레임워크 확장이 필요하다.
- 외부중심 장면에서 전역 변환은 에이전트와 객체 모두에 작용하며, 배경 장면과 다중 깊이(테이블, 트레이, 객체, 로봇)가 시차, 보간, 경계 아티팩트를 유발한다. 그리드를 늘리면 비변형 관측 비율이 감소하여 버퍼 분포가 실제 관측에서 벗어난다.
- 객체 재배치의 최적 구성(3분기, 0.175m 작업 공간)은 다른 두 작업(27분기, 0.3m)과 달라, 외부중심 장면에서 대칭성 이득이 제한적이며 매개변수를 작업별로 튜닝해야 함을 시사한다.
- 케이블 배선 평가 결과는 큰 산포를 보이며, 저자들은 더 많은 시드나 추가 분석이 필요할 수 있음을 인정한다.
- 광 무작위화(RLPD는 구현하지 않음)가 없어 조명 변화에 민감하며, 일관된 조명이 있어야 훈련이 성공할 수 있다.
- RGB 이미지와 고유수용감각만 처리하며, 포인트 클라우드 등 더 복잡한 표현은 다루지 않는다.
- 논문은 시뮬레이션 훈련이나 전이 학습, 휴머노이드 로봇 실험, 다중 작업 일반화를 명시적으로 언급하지 않는다.

## 엔지니어링 시사점

- **재현 시 우선 확인 사항**: 대칭 작업 공간(SymWS) 폭과 분기 수 K의 일치 관계를 먼저 확인하라—수식 1에서 t_{k_x,k_y}의 경계 조건이 그리드 커버리지를 직접 결정하며, SymWS가 로봇의 실제 작업 공간을 초과하면 증강 데이터가 도달 불가능한 상태에 대응하여 정책 학습이 실패할 수 있다.
- **외부중심 장면에서 가장 함정이 많음**: 호모그래피 캘리브레이션은 학습 시스템과 동일한 참조 좌표계(엔드 이펙터 프레임)를 사용해야 하며, 캘리브레이션 포인트는 전체 작업 공간을 아우르도록 해야 한다(예: 20개의 비공선점, RMSE 1.387 px). 캘리브레이션 오차가 3 px(내점 최대 오차 2.240 px)를 초과하면 왜곡 이미지가 체계적 편향을 도입하므로, 훈련 시작 전에 호모그래피 정밀도를 별도로 검증하는 것이 좋다.
- **리플레이 버퍼 비율 모니터링**: K를 늘리면 비변형 관측 비율이 감소하여 비전 인코더가 기하 정보 대신 아티팩트를 활용하게 된다. 훈련 중 버퍼 내 원본 관측 비율을 모니터링하고, 50% 미만이면 K를 줄이거나 버퍼 용량을 늘리는 것이 좋다(360만 항목이 참고 기준).
- **하드웨어 요구 사항은 예상보다 낮음**: SymmGrid는 RTX 4070(12GB VRAM)에서 실행 가능하지만, 역방향 매핑의 사전 계산과 remap()의 제자리 호출에 주의해야 한다—샘플링 시 findHomography()를 반복 호출하면 훈련이 크게 느려지므로, H_b(Δ)를 미리 계산하고 캐시해야 한다.
- **하위 팀 선택 가이드**: 자기중심 비전 작업(손목 장착 카메라)의 경우 SymmGrid를 27분기와 0.3m 작업 공간으로 바로 적용할 수 있다. 외부중심 비전 작업의 경우 3분기와 0.175m에서 시작하고, 호모그래피 아티팩트가 정책에 미치는 영향을 우선 검증하는 것이 좋다.
