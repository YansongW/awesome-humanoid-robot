---
$id: ent_paper_compositional_motion_generation_demonstr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Compositional Motion Generation from Demonstration with Object-Centric Neural Fields
  zh: Compositional Motion Generation from Demonstration with Object-Centric Neural Fields
  ko: Compositional Motion Generation from Demonstration with Object-Centric Neural Fields
summary:
  en: Compositionality, by organizing complex behavior as combinations of simpler elements, enables robot learning that is
    scalable and data efficient. Leveraging this principle, we propose a generative learning-from-demonstration framework
    that enables compositional modeling of robotic behavior by connecting perception and motion through shared object-level
    representations. We render scenes from.
  zh: 本文提出一个生成式学习框架，通过物体中心的神经场（object-centric neural fields）将感知与运动生成统一建模，实现从少量演示中学习组合性机器人行为。作者设计了空间混合专家（spatial MoE）与时间混合专家（temporal
    MoE）分别处理场景表示与轨迹生成，并引入潜在重标记（latent relabeling）机制扩充有效训练数据。核心贡献在于以物体级潜在变量为纽带，在保持数据效率（低至10-30个演示）的同时实现系统化泛化，在仿真与真实机器人任务上显著优于现有基线。
  ko: Compositionality, by organizing complex behavior as combinations of simpler elements, enables robot learning that is
    scalable and data efficient. Leveraging this principle, we propose a generative learning-from-demonstration framework
    that enables compositional modeling of robotic behavior by connecting perception and motion through shared object-level
    representations. We render scenes from.
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
- compositional
- motion
- generation
- demonstr
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
  title: arXiv:2607.07129 Compositional Motion Generation from Demonstration with Object-Centric Neural Fi
  url: https://arxiv.org/abs/2607.07129
  date: '2026-07-08'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一个生成式学习框架，通过物体中心的神经场（object-centric neural fields）将感知与运动生成统一建模，实现从少量演示中学习组合性机器人行为。作者设计了空间混合专家（spatial MoE）与时间混合专家（temporal MoE）分别处理场景表示与轨迹生成，并引入潜在重标记（latent relabeling）机制扩充有效训练数据。核心贡献在于以物体级潜在变量为纽带，在保持数据效率（低至10-30个演示）的同时实现系统化泛化，在仿真与真实机器人任务上显著优于现有基线。

## 它改变了什么

现有LfD方法要么将运动视为整体序列，要么依赖手工设计的运动基元（MPs）与低维特征，前者忽略了行为的组合结构，后者受限于特征工程的可扩展性。从图像直接学习特征的方法（如CNMP）虽免去手工设计，却需要大规模数据集，牺牲了MPs的数据效率优势。神经场方法（如tekden2023neural）在场景级别操作，随物体数量增加扩展性急剧恶化；无监督场景分解方法（Slot Attention、GIRAFFE）同样依赖大规模图像数据，并非为机器人学习设计。

本文真正改变的是将“物体中心表示”确立为连接感知与运动的中间层，使组合性不再依赖人工指定的基元连接或经由点，而是从数据中自动涌现。通过将场景分解为物体特定神经场，每个物体的潜在向量同时驱动感知重建与运动条件化，这一设计使得少量演示即可覆盖物体属性（颜色、形状、位置）的连续变化空间，并在推理时通过潜在插值实现系统化泛化。相比手工特征，物体中心表示无需任务特定的特征工程；相比端到端图像条件化，它提供了可解释的潜在结构，显著降低了对数据量的需求。

## 方法拆解

### 空间混合专家（场景建模）
- 图像建模为物体特定神经场与背景的组合：\(\hat{I}(x|\{z_i\}) = \sum_{i=1}^{N} M_i(x_i) F_i(x_i) + M_{bg} F_{bg}(x)\)，其中 \(x_i = x - \Delta_i(x|z_i)\)
- \(F_i\) 预测物体外观，\(\Delta_i\) 为条件于潜在向量 \(z_i\) 的形变场，\(M_i\) 通过空间softmax计算：\(M_i(x_i) = \frac{\exp(l_i(x_i))}{\exp(l_{bg}) + \sum_{j=1}^{N} \exp(l_j(x_j))}\)
- 所有场均为坐标MLP（神经场），背景logit \(l_{bg}\) 为常数

### 三阶段训练
1. **背景建模**：仅用非掩码像素训练 \(F_{bg}\)，提供比中值图像更一致的背景估计
2. **物体中心训练**：每个物体模型 \(F_i\) 在物体中心采样框架内训练，对其他物体像素从背景模型采样，防止串扰；采用位置感知的缩放课程学习
3. **联合组合训练**：用完整组合模型联合优化所有场

- 对形变网络 \(\Delta_i\) 施加Lipschitz正则化，保证潜在空间平滑性

### 潜在重标记
- 每个物体关联潜在向量 \(z_i^{(k)} \in \mathbb{R}^{d_z}\)，通过插值角集 \(C^i\) 的凸组合捕获物体变化
- 潜在搜索算法：采样角集凸组合 → 梯度下降细化 → 保留满足 \(E_{i,l}^{(k)} < \lambda E_{\min}\) 的候选（最多 \(L\) 个）
- 角集迭代扩展：初始化两个最大距离嵌入，测试剩余实例可重建性，不可则扩展
- 效果：训练集从 \(K\) 扩充至 \(K \times L\)

### 时间混合专家（运动生成）
- 假设顺序组合性：不同轨迹段依赖不同 \(\hat{z}_i\) 子集
- 条件信号：\(c(t) = \sum_{i=1}^{N} w_i(t) c_i(\hat{z}_i)\)，权重 \(w_i(t) = \frac{\exp(s_i(t))}{\sum_{j=1}^{N} \exp(s_j(t))}\)
- 轨迹建模为高斯分布：\(q(t) \sim \mathcal{N}(\mu(t), \mathrm{diag}(\sigma^2(t)))\)，最小化负对数似然
- 潜在dropout作为热身正则化；概率公式使不相关潜在变量被方差吸收
- 四元数轨迹转为轴角形式，在初始四元数切空间中表达

### FiLM条件化
- \(h_i(z_i) = \{\gamma_i^{(\ell)}, \beta_i^{(\ell)}\}_{\ell=1}^{L}\)，聚合条件信号：\(\gamma^{(\ell)}(t) = \sum_{i=1}^{N} w_i(t) \gamma_i^{(\ell)}\)
- 相比超网络参数更少、稳定性更好

### 推理
- 测试时应用相同潜在搜索，物体按大小降序处理（较大物体提供更可靠重建线索）

## 关键创新

1. **物体中心神经场作为组合性中间层**：将场景分解为物体特定神经场，每个物体的潜在向量同时驱动感知与运动，使组合性从数据中自动涌现而非人工指定。这是首次将物体中心表示用于数据高效的LfD，相比场景级神经场（tekden2023neural）显著提升扩展性。

2. **潜在重标记机制**：通过插值角集凸组合并搜索最优潜在表示，将训练集从 \(K\) 扩充至 \(K \times L\)，在不增加演示采集成本的情况下提升数据效率。这一机制使模型能从少至10-30张图像中学习连续物体变化，是数据效率的关键来源。

3. **双MoE架构（空间+时间）**：空间MoE处理感知分解，时间MoE处理运动组合，两者通过物体潜在向量耦合。时间MoE的概率轨迹公式允许不相关潜在变量被方差吸收，避免均值偏置；FiLM条件化相比超网络更稳定高效。

## 实验与结果

### 仿真任务（低数据制度，仅评估提出方法）
| 任务 | CNN-CNMP (Low) | DP (Low) | CNN-Film (Low) | Ours w/o gating (Low) | Ours (Low) |
|------|---------------|----------|----------------|----------------------|------------|
| Wall Avoidance | 2.72±0.08 / 0.67±0.04 | 2.31±0.04 / 0.79±0.02 | 1.41±0.19 / 0.89±0.02 | 0.71±0.04 / 0.99±0.00 | **0.51±0.03 / 0.99±0.00** |
| Incline | 4.35±0.27 / 0.11±0.03 | 3.60±0.08 / 0.25±0.01 | 3.01±0.55 / 0.40±0.13 | 0.89±0.03 / 0.99±0.01 | **0.71±0.02 / 1.00±0.00** |
| Cup Stacking | 10.85±1.39 / 0.02±0.01 | 11.13±1.29 / 0.02±0.02 | 8.74±1.83 / 0.03±0.01 | 1.10±0.03 / 0.86±0.05 | **0.65±0.04 / 0.99±0.00** |
| Cube Stacking | 14.22±0.59 / 0.00±0.00 | 11.55±0.19 / 0.00±0.00 | 9.26±0.74 / 0.00±0.00 | 1.33±0.05 / 0.85±0.06 | **0.72±0.05 / 0.97±0.02** |

（MED/Accuracy，MED越低越好，Accuracy越高越好）

### 关键结果
- 在低数据制度下，Ours在所有任务上MED均低于0.72，成功率≥0.97，而CNN-CNMP和DP在Cup/Cube任务上成功率接近0
- Ours在低数据下的表现甚至优于多数基线在高数据下的结果（如CNN-CNMP High在Cube上MED=6.07，成功率0.00）
- 消融：去除gating后Cube任务MED从0.72升至1.33，成功率从0.97降至0.85，证明时间门控的重要性
- 鲁棒性：30个演示中最多3个含不完整掩码时性能不变；时间扭曲使MED升至2.03，成功率降至约0.90

### 真实机器人实验
- 任务1（拾取放碗）：30个演示，25/25测试成功；20个演示时5个额外试验中3个成功；添加视觉干扰物体后5/5成功
- 任务2（类别级泛化）：15个测试用例，14/15成功，唯一失败为未见棒球（表面更硬，抓取精度要求更高）
- 任务3（多物体语言条件化）：15/15成功；每任务5次试验×3次执行全部成功
- 任务4（抽屉放箱子）：4个占据场训练，10个新颖配置全部成功；关键位姿误差：抽屉把手0.32 cm，箱子抓取0.35 cm

## 边界与局限

- 泛化被自然限制在演示潜在支持内的变化，外推超出此区域不保证
- 视觉上相似的干扰物体（如相同颜色）可能导致歧义或性能下降
- 超过3个（共30个）演示含不完整掩码时，场景模型无法可靠分解物体
- 方法仍依赖跨演示的粗略相位对齐（夹爪状态转换）
- NFMP基线因网格训练扩展性为 \(3^n\) 仅在Wall Avoidance上评估
- 最终任务中少于4个示例时场景表示模型无法捕捉抽屉关节运动
- 未评估语言理解本身的错误（假设提示能产生正确分割掩码）
- 未涉及大规模跨任务学习或VLA风格预训练

## 工程启示

复现时优先核对**潜在搜索算法的超参数**（角集初始化、候选保留阈值 \(\lambda\)、最大候选数 \(L\)），这些直接决定数据扩充效果与泛化边界。最容易踩坑的是**掩码质量**：超过10%演示含不完整掩码会导致场景分解失败，实践中建议用矩形标注并人工检查。训练顺序必须严格遵循三阶段（背景→物体中心→联合），跳过背景建模会导致物体场捕获背景区域。

对下游团队：若任务涉及**类别级泛化**（如不同杯子、球），需确保训练演示覆盖物体属性的连续变化（颜色、形状、位置），潜在插值才能有效。真实系统部署时，**夹爪状态转换的时间对齐**是运动生成的前提，建议在数据采集阶段记录开/关信号。推理时按物体大小降序处理可提升重建稳定性。若需更高精度（如1 cm级抓取），可考虑将场景表示扩展至ESDF（如最终任务所示），但需注意最少4个示例的限制。硬件方面，RGB推理约1.4秒/物体，3D约0.8秒/物体，实时性要求高的场景需优化或并行化。

## Overview
Compositionality, by organizing complex behavior as combinations of simpler elements, enables robot learning that is scalable and data efficient. Leveraging this principle, we propose a generative learning-from-demonstration framework that enables compositional modeling of robotic behavior by connecting perception and motion through shared object-level representations. We render scenes from object-centric neural representations that integrate canonical neural fields with latent-conditioned deformations, capturing positional and geometric variations in a smooth, consistent, and interpretable way. For motion generation, a temporal mixture-of-experts (MoE) employs a gating mechanism to combine object-conditioned movement primitives over time, producing complete trajectories. This spatial-temporal compositionality maintains the data efficiency of movement primitives while grounding motion in visual structure, enabling systematic generalization across diverse scene configurations. In simulation, long-horizon manipulation tasks are successfully completed using the proposed model, which requires significantly less training data than other image-based baselines. Real-world experiments further demonstrate the method's robustness to noise, its ability to generalize at the category level through language-based segmentation models, and its capacity to operate directly on 3D scene representations.

## 参考
- https://arxiv.org/abs/2607.07129

## 개요

본 논문은 객체 중심 신경장(object-centric neural fields)을 통해 인지와 운동 생성을 통합 모델링하는 생성적 학습 프레임워크를 제안하여, 소수의 시연으로부터 조합적 로봇 행동을 학습한다. 저자는 공간 혼합 전문가(spatial MoE)와 시간 혼합 전문가(temporal MoE)를 각각 장면 표현과 궤적 생성에 설계하고, 잠재 재레이블링(latent relabeling) 메커니즘을 도입하여 유효 훈련 데이터를 확장한다. 핵심 기여는 객체 수준 잠재 변수를 연결고리로 삼아 데이터 효율성(10~30개 시연)을 유지하면서도 체계적 일반화를 달성하며, 시뮬레이션 및 실제 로봇 작업에서 기존 베이스라인을 크게 능가한다는 점이다.

## 무엇을 바꾸었는가

기존 LfD 방법은 운동을 전체 시퀀스로 취급하거나 수작업으로 설계된 운동 프리미티브(MPs)와 저차원 특징에 의존한다. 전자는 행동의 조합 구조를 무시하고, 후자는 특징 엔지니어링의 확장성에 제한을 받는다. 이미지에서 직접 특징을 학습하는 방법(예: CNMP)은 수작업 설계를 피하지만 대규모 데이터셋이 필요하여 MPs의 데이터 효율성 이점을 희생한다. 신경장 방법(예: tekden2023neural)은 장면 수준에서 작동하며 객체 수가 증가함에 따라 확장성이 급격히 악화된다. 비지도 장면 분해 방법(Slot Attention, GIRAFFE) 역시 대규모 이미지 데이터에 의존하며 로봇 학습을 위해 설계되지 않았다.

본 논문이 실제로 바꾼 것은 '객체 중심 표현'을 인지와 운동을 연결하는 중간 계층으로 확립하여, 조합성이 수작업으로 지정된 프리미티브 연결이나 경유점에 의존하지 않고 데이터에서 자동으로 출현하도록 한 것이다. 장면을 객체별 신경장으로 분해하고 각 객체의 잠재 벡터가 인지 재구성과 운동 조건화를 동시에 구동함으로써, 소수의 시연으로 객체 속성(색상, 모양, 위치)의 연속적 변화 공간을 커버하고 추론 시 잠재 보간을 통해 체계적 일반화를 달성한다. 수작업 특징에 비해 객체 중심 표현은 작업별 특징 엔지니어링이 필요 없고, 엔드투엔드 이미지 조건화에 비해 해석 가능한 잠재 구조를 제공하여 데이터 요구량을 크게 줄인다.

## 방법 분해

### 공간 혼합 전문가(장면 모델링)
- 이미지는 객체별 신경장과 배경의 조합으로 모델링: \(\hat{I}(x|\{z_i\}) = \sum_{i=1}^{N} M_i(x_i) F_i(x_i) + M_{bg} F_{bg}(x)\), 여기서 \(x_i = x - \Delta_i(x|z_i)\)
- \(F_i\)는 객체 외관을 예측하고, \(\Delta_i\)는 잠재 벡터 \(z_i\)에 조건화된 변형장이며, \(M_i\)는 공간 소프트맥스로 계산: \(M_i(x_i) = \frac{\exp(l_i(x_i))}{\exp(l_{bg}) + \sum_{j=1}^{N} \exp(l_j(x_j))}\)
- 모든 장은 좌표 MLP(신경장)이며, 배경 로짓 \(l_{bg}\)는 상수

### 3단계 훈련
1. **배경 모델링**: 비마스크 픽셀만으로 \(F_{bg}\)를 훈련하여 중앙값 이미지보다 일관된 배경 추정 제공
2. **객체 중심 훈련**: 각 객체 모델 \(F_i\)를 객체 중심 샘플링 프레임워크에서 훈련하고, 다른 객체 픽셀은 배경 모델에서 샘플링하여 간섭 방지; 위치 인지 스케일링 커리큘럼 학습 적용
3. **결합 조합 훈련**: 전체 조합 모델로 모든 장을 공동 최적화

- 변형 네트워크 \(\Delta_i\)에 Lipschitz 정규화를 적용하여 잠재 공간 평활성 보장

### 잠재 재레이블링
- 각 객체는 잠재 벡터 \(z_i^{(k)} \in \mathbb{R}^{d_z}\)와 연관되며, 각도 집합 \(C^i\)의 볼록 조합을 보간하여 객체 변화 포착
- 잠재 탐색 알고리즘: 각도 집합 볼록 조합 샘플링 → 경사 하강법 정제 → \(E_{i,l}^{(k)} < \lambda E_{\min}\)을 만족하는 후보 유지(최대 \(L\)개)
- 각도 집합 반복 확장: 두 개의 최대 거리 임베딩으로 초기화, 나머지 인스턴스의 재구성 가능성을 테스트하고 불가능하면 확장
- 효과: 훈련 세트가 \(K\)에서 \(K \times L\)로 확장

### 시간 혼합 전문가(운동 생성)
- 순차적 조합성 가정: 서로 다른 궤적 구간이 서로 다른 \(\hat{z}_i\) 부분집합에 의존
- 조건 신호: \(c(t) = \sum_{i=1}^{N} w_i(t) c_i(\hat{z}_i)\), 가중치 \(w_i(t) = \frac{\exp(s_i(t))}{\sum_{j=1}^{N} \exp(s_j(t))}\)
- 궤적을 가우시안 분포로 모델링: \(q(t) \sim \mathcal{N}(\mu(t), \mathrm{diag}(\sigma^2(t)))\), 음의 로그 우도 최소화
- 잠재 드롭아웃을 워밍업 정규화로 사용; 확률적 공식으로 무관한 잠재 변수가 분산에 흡수됨
- 쿼터니언 궤적을 축각(axis-angle) 형태로 변환하여 초기 쿼터니언 탄젠트 공간에서 표현

### FiLM 조건화
- \(h_i(z_i) = \{\gamma_i^{(\ell)}, \beta_i^{(\ell)}\}_{\ell=1}^{L}\), 조건 신호 집계: \(\gamma^{(\ell)}(t) = \sum_{i=1}^{N} w_i(t) \gamma_i^{(\ell)}\)
- 하이퍼네트워크보다 파라미터가 적고 안정성이 우수

### 추론
- 테스트 시 동일한 잠재 탐색을 적용하고, 객체를 크기 내림차순으로 처리(큰 객체가 더 신뢰할 수 있는 재구성 단서 제공)

## 핵심 혁신

1. **객체 중심 신경장을 조합성의 중간 계층으로**: 장면을 객체별 신경장으로 분해하고 각 객체의 잠재 벡터가 인지와 운동을 동시에 구동하여, 조합성이 수작업 지정 없이 데이터에서 자동으로 출현한다. 객체 중심 표현을 데이터 효율적 LfD에 처음 적용한 사례로, 장면 수준 신경장(tekden2023neural)보다 확장성이 크게 향상되었다.

2. **잠재 재레이블링 메커니즘**: 각도 집합 볼록 조합을 보간하고 최적 잠재 표현을 탐색하여 훈련 세트를 \(K\)에서 \(K \times L\)로 확장하며, 시연 수집 비용 증가 없이 데이터 효율성을 높인다. 이 메커니즘은 10~30개 이미지에서 연속적 객체 변화를 학습할 수 있게 하며, 데이터 효율성의 핵심 원천이다.

3. **이중 MoE 아키텍처(공간+시간)**: 공간 MoE는 인지 분해를, 시간 MoE는 운동 조합을 담당하며, 둘은 객체 잠재 벡터로 결합된다. 시간 MoE의 확률적 궤적 공식은 무관한 잠재 변수가 분산에 흡수되도록 하여 평균 편향을 방지하고, FiLM 조건화는 하이퍼네트워크보다 안정적이고 효율적이다.

## 실험 및 결과

### 시뮬레이션 작업(저데이터 체제, 제안 방법만 평가)
| 작업 | CNN-CNMP (Low) | DP (Low) | CNN-Film (Low) | Ours w/o gating (Low) | Ours (Low) |
|------|---------------|----------|----------------|----------------------|------------|
| Wall Avoidance | 2.72±0.08 / 0.67±0.04 | 2.31±0.04 / 0.79±0.02 | 1.41±0.19 / 0.89±0.02 | 0.71±0.04 / 0.99±0.00 | **0.51±0.03 / 0.99±0.00** |
| Incline | 4.35±0.27 / 0.11±0.03 | 3.60±0.08 / 0.25±0.01 | 3.01±0.55 / 0.40±0.13 | 0.89±0.03 / 0.99±0.01 | **0.71±0.02 / 1.00±0.00** |
| Cup Stacking | 10.85±1.39 / 0.02±0.01 | 11.13±1.29 / 0.02±0.02 | 8.74±1.83 / 0.03±0.01 | 1.10±0.03 / 0.86±0.05 | **0.65±0.04 / 0.99±0.00** |
| Cube Stacking | 14.22±0.59 / 0.00±0.00 | 11.55±0.19 / 0.00±0.00 | 9.26±0.74 / 0.00±0.00 | 1.33±0.05 / 0.85±0.06 | **0.72±0.05 / 0.97±0.02** |

(MED/Accuracy, MED는 낮을수록, Accuracy는 높을수록 좋음)

### 핵심 결과
- 저데이터 체제에서 Ours는 모든 작업에서 MED가 0.72 미만, 성공률 ≥0.97을 달성한 반면, CNN-CNMP와 DP는 Cup/Cube 작업에서 성공률이 0에 가까움
- Ours의 저데이터 성능은 대부분 베이스라인의 고데이터 결과보다 우수(예: CNN-CNMP High의 Cube MED=6.07, 성공률 0.00)
- 절제: gating 제거 시 Cube 작업 MED가 0.72에서 1.33으로 상승, 성공률이 0.97에서 0.85로 하락하여 시간 게이팅의 중요성 입증
- 강건성: 30개 시연 중 최대 3개가 불완전 마스크를 포함해도 성능 불변; 시간 왜곡 시 MED가 2.03으로 상승, 성공률 약 0.90으로 하락

### 실제 로봇 실험
- 작업 1(집어서 그릇에 넣기): 30개 시연, 25/25 테스트 성공; 20개 시연 시 추가 5개 시도 중 3개 성공; 시각적 방해 객체 추가 후 5/5 성공
- 작업 2(클래스 수준 일반화): 15개 테스트 케이스 중 14/15 성공, 유일한 실패는 보지 못한 야구공(표면이 더 단단하여 파지 정밀도 요구가 높음)
- 작업 3(다중 객체 언어 조건화): 15/15 성공; 작업당 5회 시도 × 3회 실행 모두 성공
- 작업 4(서랍에 상자 넣기): 4개 점유장으로 훈련, 10개 새로운 구성 모두 성공; 핵심 자세 오차: 서랍 손잡이 0.32 cm, 상자 파지 0.35 cm

## 경계 및 한계

- 일반화는 자연스럽게 시연의 잠재 지원 범위 내 변화로 제한되며, 이 영역을 벗어난 외삽은 보장되지 않음
- 시각적으로 유사한 방해 객체(예: 동일 색상)는 모호성 또는 성능 저하를 유발할 수 있음
- 30개 시연 중 3개 이상이 불완전 마스크를 포함하면 장면 모델이 객체를 안정적으로 분해할 수 없음
- 방법은 여전히 시연 간 대략적인 위상 정렬(그리퍼 상태 전환)에 의존
- NFMP 베이스라인은 그리드 훈련 확장성이 \(3^n\)이므로 Wall Avoidance에서만 평가
- 최종 작업에서 4개 미만의 예시일 때 장면 표현 모델이 서랍 관절 운동을 포착할 수 없음
- 언어 이해 자체의 오류는 평가하지 않음(프롬프트가 올바른 분할 마스크를 생성한다고 가정)
- 대규모 교차 작업 학습 또는 VLA 스타일 사전 훈련은 다루지 않음

## 공학적 시사점

재현 시 **잠재 탐색 알고리즘의 하이퍼파라미터**(각도 집합 초기화, 후보 유지 임계값 \(\lambda\), 최대 후보 수 \(L\))를 우선적으로 확인해야 한다. 이들은 데이터 확장 효과와 일반화 경계를 직접 결정한다. 가장 쉽게 실패하는 지점은 **마스크 품질**이다: 시연의 10% 이상이 불완전 마스크를 포함하면 장면 분해가 실패하므로, 실제로는 사각형 주석과 수동 검사를 권장한다. 훈련 순서는 반드시 3단계(배경→객체 중심→결합)를 엄격히 따라야 하며, 배경 모델링을 건너뛰면 객체 장이 배경 영역을 포착하게 된다.

하류 팀에게: 작업이 **클래스 수준 일반화**(예: 다양한 컵, 공)를 포함한다면, 훈련 시연이 객체 속성(색상, 모양, 위치)의 연속적 변화를 커버하도록 보장해야 잠재 보간이 효과적이다. 실제 시스템 배포 시 **그리퍼 상태 전환의 시간 정렬**은 운동 생성의 전제 조건이므로, 데이터 수집 단계에서 개폐 신호를 기록하는 것이 좋다. 추론 시 객체를 크기 내림차순으로 처리하면 재구성 안정성이 향상된다. 더 높은 정밀도(예: 1 cm 수준 파지)가 필요하다면 장면 표현을 ESDF로 확장(최종 작업 참조)할 수 있지만, 최소 4개 예시 제한에 주의해야 한다. 하드웨어 측면에서 RGB 추론은 객체당 약 1.4초, 3D는 객체당 약 0.8초이므로, 실시간 요구가 높은 환경에서는 최적화 또는 병렬화가 필요하다.
