---
$id: ent_paper_action_map_policy_3d_closed_loop_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Action Map Policy: Learning 3D Closed-loop Manipulation via Pixel Classification'
  zh: 'Action Map Policy: Learning 3D Closed-loop Manipulation via Pixel Classification'
  ko: 'Action Map Policy: Learning 3D Closed-loop Manipulation via Pixel Classification'
summary:
  en: The action space poses a major challenge in robot learning, since it is often high-dimensional, can span long time horizons,
    and frequently admits multi-modal optimal solutions. A good choice of action representation and loss function can help
    to address these concerns, but there are often trade offs. We propose Action Map Policy (AMP), which casts 3D closed-loop
    manipulation policy learning as a.
  zh: Action Map Policy (AMP) 将 3D 闭环操作策略学习重构为图像空间中的像素分类问题，通过预测末端执行器关键点在多视图中的投影像素位置，以单次前向传播生成整个动作块。该方法由作者团队提出，核心贡献在于用热图分类范式替代回归或扩散生成，在保留多模态分布的同时实现毫米级精度与快速推理。
  ko: The action space poses a major challenge in robot learning, since it is often high-dimensional, can span long time horizons,
    and frequently admits multi-modal optimal solutions. A good choice of action representation and loss function can help
    to address these concerns, but there are often trade offs. We propose Action Map Policy (AMP), which casts 3D closed-loop
    manipulation policy learning as a.
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
- action
- map
- policy
- 3d
- closed
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
  title: 'arXiv:2607.10706 Action Map Policy: Learning 3D Closed-loop Manipulation via Pixel Classification'
  url: https://arxiv.org/abs/2607.10706
  date: '2026-07-12'
  accessed_at: '2026-08-05'
---

## 概述

Action Map Policy (AMP) 将 3D 闭环操作策略学习重构为图像空间中的像素分类问题，通过预测末端执行器关键点在多视图中的投影像素位置，以单次前向传播生成整个动作块。该方法由作者团队提出，核心贡献在于用热图分类范式替代回归或扩散生成，在保留多模态分布的同时实现毫米级精度与快速推理。

## 它改变了什么

机器人动作学习长期受困于高维连续空间与多模态最优解的矛盾。回归方法在目标分布多峰时坍缩到均值，扩散模型虽能建模多模态但需多步去噪且难以直接约束候选动作似然。此前将分类范式从语言模型迁移到动作空间的尝试均因词表爆炸而失败——6-DoF 动作每维仅 10 个 bin 就需要 10^6 类别，随动作时间范围进一步指数增长。

AMP 真正改变的是动作表示的几何本质：不再将动作视为高维向量，而是将其嵌入观测图像平面。这一转换使分类目标从离散码本变为连续像素坐标，词表大小由图像分辨率决定而非动作维度。同时，热图天然保留空间多模态性——多个峰值对应多个可行抓取，且像素级监督直接作用于视觉特征，避免了离散 tokenization 丢失几何结构的问题。这是首次将分类范式以可扩展方式应用于高维连续动作学习。

## 方法拆解

### 动作表示：Pose2Kp 与几何逆映射
- 动作 a = (T, R, w) 映射为 m=5 个 3D 关键点 ã = (p^1, …, p^m)，基于平行夹爪几何设计
- 平移 T 为四个抓取点质心：T = 1/4(p^1 + p^2 + p^3 + p^4)
- 旋转 R 由对映轴 v_antipodal = 1/2[(p^1 − p^2) + (p^3 − p^4)] 与接近轴 v_approach = 1/2[(p^2 − p^4) + (p^1 − p^3)] 经 Gram–Schmidt 正交化构建
- 夹爪宽度 w = d_+/(d_+ + d_−)，其中 d_+ = ‖p^5 − 1/2(p^2 + p^4)‖，d_− = ‖p^5 − 1/2(p^1 + p^3)‖

### 投影与热图标签
- 通过相机矩阵 P_k 将 3D 关键点投影到 n 个侧视图的 2D 像素坐标
- 每个关键点渲染为 σ=2 的高斯软标签 h_ijk ∈ R^{H×W}，满足 ∑_{u,v} h_ijk(u,v) = 1
- 跨 l 个时间步沿通道维度堆叠形成时空体 H_jk ∈ R^{l×H×W}

### 网络架构：X-Net
- 左侧 U-Net 编码器（四个 ResBlock，16× 下采样）提取密集特征
- 特征图展平为位置编码 token，输入多视图 Transformer (MVT)：六层注意力（两个图像内、四个跨图像）
- 输出 token 重塑为空间维度，经 U-Net 解码器（四个上采样 ResBlock）生成热图
- 编码器与解码器对应层间使用跳跃连接

### 训练与推理
- 训练：完全在热图空间监督，损失为像素级交叉熵 L_CE = −∑_{i=1}^{l} ∑_{j=1}^{m} ∑_{k=1}^{n} ∑_{u,v} h_ijk(u,v) log ĥ_ijk(u,v)，不提取动作
- 推理：arg max 取最高概率像素 → 三角化重建 3D 关键点 → 几何逆映射恢复动作
- 闭环：以固定频率消费最新观测，执行前 8 个时间步后重新规划
- 等变增强：对每个视图独立施加随机旋转 [−π/6, π/6] 与平移 [−H/6, H/6]，联合变换图像与标签，满足 ψ(GO) = G ψ(O)

## 关键创新

1. **动作空间的像素化重定义**：将 6-DoF 连续动作嵌入图像平面，使分类词表大小由分辨率决定而非动作维度。224×224 分辨率下仅需约 10^10 个等效 token 即可达到 1 mm 精度，而传统离散化需要 10^6 类别仅覆盖单步 6-DoF 动作（由表内数值 (10/1.00)^3 (360/1.30)^3 计算），这是数量级的突破。

2. **几何可逆的关键点设计**：m=5 个关键点以固定相对配置排列，使平移、旋转、夹爪宽度可从关键点坐标解析恢复。该设计同时保证投影双射性——在通用相机配置下，(P, T) 在 R^3 与 Im(P) 间建立双射，确保像素预测无信息损失。

3. **多视图 Transformer 的跨图像注意力**：MVT 中跨图像注意力层显式建模不同相机视角间的对应关系，使网络能隐式学习立体匹配，替代传统手工三角化中的特征匹配步骤，提升对遮挡与视差的鲁棒性。

## 实验与结果

### 精度与鲁棒性（表 1）
| 分辨率 | 平移精度 (mm) | 旋转精度 (°) |
|--------|--------------|--------------|
| 96×96 | 2.33 ± 0.21 | 3.03 ± 0.14 |
| 128×128 | 1.75 ± 0.16 | 2.28 ± 0.11 |
| 224×224 | 1.00 ± 0.09 | 1.30 ± 0.06 |
| 512×512 | 0.44 ± 0.04 | 0.57 ± 0.03 |
| 1024×1024 | 0.22 ± 0.02 | 0.28 ± 0.01 |

精度随分辨率近似线性提升，而传统离散化所需 token 数随 n^6 多项式增长。

### 模拟任务成功率（表 2，50 次未见测试）
| 方法 | stack-three-d1 | hammer-cleanup-d1 | mug-cleanup-d1 | coffee-d2 | square-d2 | threading-d2 |
|------|---------------|-------------------|----------------|-----------|-----------|--------------|
| Diffusion Policy | 38 | 58 | 60 | 62 | 20 | 26 |
| ACT | 14 | 60 | 44 | 42 | 6 | 20 |
| OAT | 34 | 32 | 22 | 30 | 18 | 16 |
| Motion Track | 8 | 40 | 24 | 36 | 14 | 12 |
| **AMP** | **90** | **88** | **52** | **78** | **50** | **30** |

AMP 在六个任务中五个领先，平均增益 20.7% 超过第二好的 DiffPo (44.0%)。

### 真实世界实验（表 4，20 次运行）
| 方法 | 推理速度 (ms) | Coffee | Toast | Egg |
|------|--------------|--------|-------|-----|
| DiffPo (DDIM) | 93.53 | 25% | 40% | 25% |
| ACT | 7.16 | 15% | 35% | 15% |
| **AMP** | **13.80** | **80%** | **90%** | **85%** |

AMP 优于基线 50%–70%，推理速度比 DiffPo 快约 6.8 倍（由 93.53/13.80 计算）。

### 消融研究
- 软标签 σ=2 相比 one-hot (σ=0) 提升 10%
- 等变增强移除后成功率下降 12–32 个百分点
- 手内相机移除后 coffee-d2 下降 14 个百分点

## 边界与局限

- 工作空间受校准相机覆盖范围限制，观测范围外的动作无法执行
- 动作存在轻微抖动，作者建议添加几何一致性损失但未实现
- 仅验证平行夹爪，灵巧手与双臂需重新设计关键点配置
- 未使用预训练视觉编码器，未探索预训练模型的增益
- 未探索分类目标与视觉-语言模型的联合训练
- 未探索利用显式动作分布学习 Q 函数进行强化学习
- SVD 三角化步骤贡献不可忽略的开销，论文未提供优化方案

## 工程启示

复现时优先核对相机标定精度——三角化误差直接决定动作精度，建议先验证投影-三角化闭环误差在 1 mm 内。关键点几何配置是核心，修改夹爪或末端执行器时必须重新推导 Pose2Kp 与逆映射，否则轴估计会失真。

训练时注意动作块截断策略：当关键点超出图像范围时，用最后一个有效配置替换剩余关键点，这直接影响长时程任务的稳定性。等变增强是性能关键，移除后成功率下降最高 32 个百分点，务必实现联合变换而非独立增强。

推理时 arg max 取像素位置后，建议对热图做亚像素细化（如质心计算）以提升精度。若部署到新场景，先确认相机 FOV 覆盖完整工作空间，否则需增加相机数量或更换广角镜头。对于下游团队，AMP 的 13.80 ms 推理延迟适合实时控制，但需注意该数值在 RTX 3090 上测得，部署到嵌入式平台需重新评估。

## Overview
The action space poses a major challenge in robot learning, since it is often high-dimensional, can span long time horizons, and frequently admits multi-modal optimal solutions. A good choice of action representation and loss function can help to address these concerns, but there are often trade offs. We propose Action Map Policy (AMP), which casts 3D closed-loop manipulation policy learning as a classification problem in image space. While classification has been an effective formulation in generative language models, applying it to robot action learning is difficult because naively discretizing high-dimensional continuous actions explodes the token vocabulary. Our key idea is to project 3D actions onto the camera image planes and treat each pixel location as a discrete class, thus controlling dimensionality while retaining multi-modality. This method supports millimeter-level precision for high-dimensional actions without requiring a prohibitively large vocabulary, while preserving fine-grained pixel-wise visual signals. Furthermore, it can predict the entire action chunk in a single forward pass, avoiding complex noise scheduling and iterative denoising while achieving substantially faster inference than diffusion policies. Experiments on various manipulation tasks show that AMP outperforms strong baselines, achieving higher success rates, faster inference, and enhanced spatial reasoning.

## 参考
- https://arxiv.org/abs/2607.10706

## 개요

Action Map Policy (AMP)는 3D 폐루프 조작 정책 학습을 이미지 공간의 픽셀 분류 문제로 재구성하여, 엔드이펙터 키포인트의 다중 뷰 투영 픽셀 위치를 예측하고 단일 순전파로 전체 액션 블록을 생성합니다. 이 방법은 저자 팀에 의해 제안되었으며, 핵심 기여는 회귀 또는 확산 생성을 열지도 분류 패러다임으로 대체하여 다중 모드 분포를 유지하면서 밀리미터급 정밀도와 빠른 추론을 달성하는 데 있습니다.

## 무엇을 바꾸었는가

로봇 액션 학습은 오랫동안 고차원 연속 공간과 다중 모드 최적해 사이의 모순에 어려움을 겪어 왔습니다. 회귀 방법은 목표 분포가 다중 모드일 때 평균으로 붕괴되고, 확산 모델은 다중 모드를 모델링할 수 있지만 다단계 노이즈 제거가 필요하고 후보 액션의 우도를 직접 제약하기 어렵습니다. 이전에 언어 모델의 분류 패러다임을 액션 공간으로 전이하려는 시도는 어휘 폭발로 모두 실패했습니다. 6-DoF 액션의 각 차원에 10개의 bin만 있어도 10^6개의 클래스가 필요하며, 액션 시간 범위에 따라 기하급수적으로 증가합니다.

AMP가 진정으로 바꾼 것은 액션 표현의 기하학적 본질입니다. 액션을 고차원 벡터로 보지 않고 관측 이미지 평면에 임베딩합니다. 이 변환은 분류 대상을 이산 코드북에서 연속 픽셀 좌표로 바꾸며, 어휘 크기는 액션 차원이 아닌 이미지 해상도에 의해 결정됩니다. 동시에 열지도는 자연스럽게 공간적 다중 모드를 보존합니다. 여러 피크가 여러 실행 가능한 그리프에 해당하며, 픽셀 수준 감독이 시각적 특징에 직접 작용하여 이산 토큰화가 기하학적 구조를 잃는 문제를 피합니다. 이는 분류 패러다임을 확장 가능한 방식으로 고차원 연속 액션 학습에 적용한 최초의 사례입니다.

## 방법 분해

### 액션 표현: Pose2Kp 및 기하학적 역매핑
- 액션 a = (T, R, w)는 병렬 그리퍼 기하학을 기반으로 설계된 m=5개의 3D 키포인트 ã = (p^1, …, p^m)로 매핑됩니다.
- 병진 T는 네 그리프 포인트의 질량 중심: T = 1/4(p^1 + p^2 + p^3 + p^4)
- 회전 R은 대극축 v_antipodal = 1/2[(p^1 − p^2) + (p^3 − p^4)] 및 접근축 v_approach = 1/2[(p^2 − p^4) + (p^1 − p^3)]을 Gram–Schmidt 직교화를 통해 구성합니다.
- 그리퍼 폭 w = d_+/(d_+ + d_−), 여기서 d_+ = ‖p^5 − 1/2(p^2 + p^4)‖, d_− = ‖p^5 − 1/2(p^1 + p^3)‖

### 투영 및 열지도 라벨
- 카메라 행렬 P_k를 통해 3D 키포인트를 n개의 측면 뷰의 2D 픽셀 좌표로 투영합니다.
- 각 키포인트는 σ=2의 가우시안 소프트 라벨 h_ijk ∈ R^{H×W}로 렌더링되며, ∑_{u,v} h_ijk(u,v) = 1을 만족합니다.
- l개의 시간 단계에 걸쳐 채널 차원을 따라 스택하여 시공간 볼륨 H_jk ∈ R^{l×H×W}을 형성합니다.

### 네트워크 아키텍처: X-Net
- 왼쪽 U-Net 인코더(4개의 ResBlock, 16× 다운샘플링)가 밀집 특징을 추출합니다.
- 특징 맵은 위치 인코딩 토큰으로 평탄화되어 다중 뷰 Transformer(MVT)에 입력됩니다: 6개 주의 계층(2개는 이미지 내, 4개는 이미지 간).
- 출력 토큰은 공간 차원으로 재구성되고 U-Net 디코더(4개의 업샘플링 ResBlock)를 통해 열지도를 생성합니다.
- 인코더와 디코더의 해당 계층 간에는 스킵 연결이 사용됩니다.

### 훈련 및 추론
- 훈련: 완전히 열지도 공간에서 감독되며, 손실은 픽셀 수준 교차 엔트로피 L_CE = −∑_{i=1}^{l} ∑_{j=1}^{m} ∑_{k=1}^{n} ∑_{u,v} h_ijk(u,v) log ĥ_ijk(u,v)이며, 액션을 추출하지 않습니다.
- 추론: arg max로 최고 확률 픽셀을 선택 → 삼각 측량으로 3D 키포인트 재구성 → 기하학적 역매핑으로 액션 복원.
- 폐루프: 고정 주파수로 최신 관측을 소비하고, 처음 8개 시간 단계를 실행한 후 재계획합니다.
- 등변 증강: 각 뷰에 독립적으로 무작위 회전 [−π/6, π/6] 및 병진 [−H/6, H/6]을 적용하고, 이미지와 라벨을 공동 변환하여 ψ(GO) = G ψ(O)를 만족합니다.

## 핵심 혁신

1. **액션 공간의 픽셀화 재정의**: 6-DoF 연속 액션을 이미지 평면에 임베딩하여 분류 어휘 크기가 액션 차원이 아닌 해상도에 의해 결정되도록 합니다. 224×224 해상도에서 약 10^10개의 등가 토큰만으로 1 mm 정밀도에 도달할 수 있는 반면, 기존 이산화는 단일 단계 6-DoF 액션을 덮는 데 10^6개의 클래스가 필요합니다(표 내 수치 (10/1.00)^3 (360/1.30)^3으로 계산). 이는 규모의 차원에서의 돌파구입니다.

2. **기하학적으로 가역적인 키포인트 설계**: m=5개의 키포인트가 고정된 상대 구성으로 배열되어 병진, 회전, 그리퍼 폭을 키포인트 좌표에서 해석적으로 복원할 수 있습니다. 이 설계는 또한 투영의 전단사성을 보장합니다. 일반적인 카메라 구성에서 (P, T)는 R^3와 Im(P) 사이에 전단사를 설정하여 픽셀 예측이 정보 손실 없이 이루어지도록 합니다.

3. **다중 뷰 Transformer의 교차 이미지 주의**: MVT의 교차 이미지 주의 계층은 서로 다른 카메라 뷰 간의 대응 관계를 명시적으로 모델링하여 네트워크가 암시적으로 스테레오 매칭을 학습하게 하며, 기존 수동 삼각 측량의 특징 매칭 단계를 대체하여 폐색 및 시차에 대한 강건성을 향상시킵니다.

## 실험 및 결과

### 정밀도 및 강건성 (표 1)
| 해상도 | 병진 정밀도 (mm) | 회전 정밀도 (°) |
|--------|--------------|--------------|
| 96×96 | 2.33 ± 0.21 | 3.03 ± 0.14 |
| 128×128 | 1.75 ± 0.16 | 2.28 ± 0.11 |
| 224×224 | 1.00 ± 0.09 | 1.30 ± 0.06 |
| 512×512 | 0.44 ± 0.04 | 0.57 ± 0.03 |
| 1024×1024 | 0.22 ± 0.02 | 0.28 ± 0.01 |

정밀도는 해상도에 따라 거의 선형적으로 향상되는 반면, 기존 이산화에 필요한 토큰 수는 n^6 다항식으로 증가합니다.

### 시뮬레이션 작업 성공률 (표 2, 50회 미검증 테스트)
| 방법 | stack-three-d1 | hammer-cleanup-d1 | mug-cleanup-d1 | coffee-d2 | square-d2 | threading-d2 |
|------|---------------|-------------------|----------------|-----------|-----------|--------------|
| Diffusion Policy | 38 | 58 | 60 | 62 | 20 | 26 |
| ACT | 14 | 60 | 44 | 42 | 6 | 20 |
| OAT | 34 | 32 | 22 | 30 | 18 | 16 |
| Motion Track | 8 | 40 | 24 | 36 | 14 | 12 |
| **AMP** | **90** | **88** | **52** | **78** | **50** | **30** |

AMP는 6개 작업 중 5개에서 선두를 차지했으며, 두 번째로 좋은 DiffPo(44.0%)보다 평균 20.7% 더 높은 성능을 보였습니다.

### 실제 세계 실험 (표 4, 20회 실행)
| 방법 | 추론 속도 (ms) | Coffee | Toast | Egg |
|------|--------------|--------|-------|-----|
| DiffPo (DDIM) | 93.53 | 25% | 40% | 25% |
| ACT | 7.16 | 15% | 35% | 15% |
| **AMP** | **13.80** | **80%** | **90%** | **85%** |

AMP는 기준선보다 50%–70% 우수하며, 추론 속도는 DiffPo보다 약 6.8배 빠릅니다(93.53/13.80으로 계산).

### 소거 연구
- 소프트 라벨 σ=2는 one-hot(σ=0)보다 10% 향상.
- 등변 증강 제거 시 성공률이 12–32% 포인트 하락.
- 핸드 내 카메라 제거 시 coffee-d2가 14% 포인트 하락.

## 경계 및 한계

- 작업 공간은 보정된 카메라의 적용 범위로 제한되며, 관측 범위 밖의 액션은 실행할 수 없습니다.
- 액션에 약간의 떨림이 있으며, 저자는 기하학적 일관성 손실을 추가할 것을 제안하지만 구현하지 않았습니다.
- 병렬 그리퍼만 검증되었으며, 다섭 손가락 로봇 핸드와 이중 팔은 키포인트 구성을 재설계해야 합니다.
- 사전 훈련된 비전 인코더를 사용하지 않았으며, 사전 훈련 모델의 이점을 탐구하지 않았습니다.
- 분류 목표와 비전-언어 모델의 공동 훈련을 탐구하지 않았습니다.
- 명시적 액션 분포 학습을 통한 Q-함수 기반 강화 학습을 탐구하지 않았습니다.
- SVD 삼각 측량 단계는 무시할 수 없는 오버헤드를 발생시키며, 논문은 최적화 방안을 제시하지 않습니다.

## 엔지니어링 시사점

재현 시 카메라 보정 정밀도를 우선적으로 확인하십시오. 삼각 측량 오류가 액션 정밀도를 직접 결정하므로, 투영-삼각 측량 폐루프 오류가 1 mm 이내인지 먼저 검증하는 것이 좋습니다. 키포인트 기하학 구성이 핵심이며, 그리퍼나 엔드이펙터를 수정할 때는 Pose2Kp와 역매핑을 반드시 다시 유도해야 합니다. 그렇지 않으면 축 추정이 왜곡됩니다.

훈련 시 액션 블록 잘림 전략에 주의하십시오. 키포인트가 이미지 범위를 벗어나면 마지막 유효 구성을 사용하여 나머지 키포인트를 대체하며, 이는 장기 작업의 안정성에 직접적인 영향을 미칩니다. 등변 증강은 성능의 핵심이며, 제거 시 성공률이 최대 32% 포인트 하락하므로 독립 증강이 아닌 공동 변환을 반드시 구현해야 합니다.

추론 시 arg max로 픽셀 위치를 선택한 후, 열지도에 대한 서브픽셀 세분화(예: 질량 중심 계산)를 통해 정밀도를 높이는 것이 좋습니다. 새 장면에 배포할 경우 카메라 FOV가 전체 작업 공간을 덮는지 먼저 확인하고, 그렇지 않으면 카메라 수를 늘리거나 광각 렌즈로 교체해야 합니다. 다운스트림 팀의 경우 AMP의 13.80 ms 추론 지연 시간은 실시간 제어에 적합하지만, 이 수치는 RTX 3090에서 측정된 것이므로 임베디드 플랫폼에 배포할 때는 재평가가 필요합니다.
