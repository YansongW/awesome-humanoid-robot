---
$id: ent_paper_multi_view_unified_camera_fields_geometr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multi-View Unified Camera Fields: Geometry-Shaped Action-Facing Representations for RGB-Only Multi-Camera VLA Policies'
  zh: 'Multi-View Unified Camera Fields: Geometry-Shaped Action-Facing Representations for RGB-Only Multi-Camera VLA Policies'
  ko: 'Multi-View Unified Camera Fields: Geometry-Shaped Action-Facing Representations for RGB-Only Multi-Camera VLA Policies'
summary:
  en: Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation, yet complex contact-rich
    tasks often benefit from multi-camera observations that jointly capture the end effector, objects, and targets under occlusion.
    Existing multi-camera VLAs usually concatenate view tokens, leaving action representations weak in metric depth and inconsistent
    across cameras. We.
  zh: MVUCF 是一个仅训练时的框架，在动作模块消费的 token 格子上联合注入度量深度与跨视角对应两种几何属性，使纯 RGB 输入的 VLA 策略获得可用的 3D 结构感知。该方法由 NVIDIA 团队基于 GR00T-N1.6 实现，通过两阶段训练（几何注入
    + 动作训练）在不增加任何部署时传感器或推理 FLOPs 的前提下，显著提升多相机操作任务的成功率与鲁棒性。
  ko: Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation, yet complex contact-rich
    tasks often benefit from multi-camera observations that jointly capture the end effector, objects, and targets under occlusion.
    Existing multi-camera VLAs usually concatenate view tokens, leaving action representations weak in metric depth and inconsistent
    across cameras. We.
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
- multi
- view
- unified
- camera
- fields
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.01826 Multi-View Unified Camera Fields: Geometry-Shaped Action-Facing Representations '
  url: https://arxiv.org/abs/2608.01826
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

MVUCF 是一个仅训练时的框架，在动作模块消费的 token 格子上联合注入度量深度与跨视角对应两种几何属性，使纯 RGB 输入的 VLA 策略获得可用的 3D 结构感知。该方法由 NVIDIA 团队基于 GR00T-N1.6 实现，通过两阶段训练（几何注入 + 动作训练）在不增加任何部署时传感器或推理 FLOPs 的前提下，显著提升多相机操作任务的成功率与鲁棒性。

## 它改变了什么

现有 VLA 模型在处理接触丰富的多相机操作时，面临一个根本性的表征缺陷：骨干网络从 2D 语义预训练的 VLM 初始化，其隐藏状态无法可靠恢复度量深度（原生 MAE 4.3 cm）和跨视角对应（Hit@1 仅 0.4%，接近随机 0.3%）。此前工作如 Spatial Forcing 和 Selfi 分别解决跨视角一致性与度量 3D 接地，但两者机制差异过大无法模块化组合。MVUCF 真正改变的是：它证明了无需改变部署接口（仍为纯 RGB），仅通过训练时的几何监督注入，就能让 VLM 骨干的隐藏状态同时具备线性可读的度量深度与跨视角物理点对应能力。这打破了“几何感知必须依赖额外传感器或推理时模块”的隐含假设，将几何能力从辅助分支转移到了动作模块直接消费的主干表征中。

## 方法拆解

### 两阶段训练流程
1. **几何注入阶段**：仅更新 VLM 层 8–15 和两个辅助头（深度头、跨视角头），视觉编码器与层 0–7 冻结。更新范围跨数据集固定，不基于下游基准选择。
2. **动作训练阶段**：移除辅助头、深度观测和相机校准，冻结几何塑形后的骨干，使用 RGB-only 输入训练原生动作模块。

### 坐标查询深度目标（Coordinate-Query Depth Objective）
- 在 9×9 token 网格上定义 144×144 连续查询晶格（密集查询因子 P=16）。
- 每视图抽取 3072 个查询：50% 均匀采样，50% 偏向近表面与深度边缘的重要性采样。
- 查询表示拼接 1024 维特征、局部 x/y 差异和子单元相位 φ(q)=q-⌊q⌋，形成 3074 维输入，无绝对位置编码。
- 深度头：LN(2048)→Linear(1024)→GELU→Conv 3×3(1024)→GELU 的 GridTrunk 后，双线性特征查找，MLP 3074→1024→1024→1 + Softplus 预测度量深度。
- 损失：L_depth = 0.5·L_silog + 1.25·L_inv + 1.0·L_grad + 0.1·L_seam + 0.05·L_unc，有效深度范围 [0.05, 5.0] m。

### 预处理感知对应目标（Preprocessing-Aware Correspondence Objective）
- 正样本由原始帧几何重投影定义，非视觉相似性。组合变换 T_img→grid = T_unshuffle(2) ∘ T_patch(14) ∘ T_smart ∘ T_resize2 ∘ T_crop ∘ T_resize1 ∘ T_letterbox 避免坐标标签误差。
- 有效性检查：目标在图像边界内、深度在 [0.05, 5.0] m、z-buffer 一致性 |Z_j - z_j*(u_j^raw)| < 0.10 m。
- 共享投影器极简：h_ω(f) = normalize₂(W·LN₂₀₄₈(f))，W ∈ R^{128×2048}，无隐藏层。
- 全局匹配 logits ℓ_mn = 10(e_m^s)ᵀ e_n^t；软标签 y_mn ∝ exp(-‖c_n - q_j*‖²/(2σ²))，σ=0.75。
- 损失：L_cv = L_softCE + 0.1·L_hnce + 0.1·L_margin，γ=0.2，外层权重 40k 步从 1.0 退火至 0.1。

### 关键设计决策
- 深度建立视图内度量位置，对应建立跨视图物理点身份，两者互补且直接更新动作模块消费的上层隐藏状态。
- 监督抽取点选在第 15 层（而非第 12 层），因其保留更强同点判别力且是动作模块直接消费的最终隐藏空间网格。
- 空间软化正样本吸收子 token 投影误差；空间环负样本防止邻近 patch 坍缩为等效匹配。

## 关键创新

1. **统一框架同时恢复跨视角一致性与度量 3D 结构**：此前方法分别解决两者但无法组合，MVUCF 通过在同一 token 格子上联合注入两个互补属性，形成跨相机的共享动作面向潜在场，而非两个断开的辅助表示。
2. **预处理感知的坐标映射**：显式建模完整图像预处理链（unshuffle、patch、resize、crop、letterbox）的组合变换，避免直接缩放原始像素到 token 坐标的标签误差，这是工程上极易被忽视但影响几何监督精度的关键细节。
3. **查询模式深度监督**：不监督每训练步的密集全图预测，而是通过 3072 个查询点（含重要性采样偏向近表面与边缘）在连续网格位置监督度量深度，配合梯度项阻止恒定深度坍缩，在训练效率与几何精度间取得平衡。

## 实验与结果

### LIBERO 标准基准（表 1）
| 指标 | Base (GR00T-N1.6) | Ours | Δ |
|---|---|---|---|
| Spatial | 99.3 ± 1.2 | 100.0 ± 0.0 | +0.7 |
| Object | 99.2 ± 0.8 | 99.2 ± 0.3 | 0.0 |
| Goal | 98.4 ± 1.2 | 99.5 ± 0.5 | +1.1 |
| Long | 92.9 ± 1.0 | 97.0 ± 1.5 | +4.1 |
| Average | 97.4 ± 0.3 | 98.9 ± 0.4 | +1.5 |

### LIBERO-Plus 鲁棒性（表 2）
| 扰动类型 | Base | Ours | Δ |
|---|---|---|---|
| Camera | 20.9 | 24.1 | +3.2 |
| Robot | 40.2 | 54.1 | +13.9 |
| Language | 35.0 | 72.9 | +37.9 |
| Light | 65.4 | 95.1 | +29.7 |
| Background | 76.3 | 91.8 | +15.5 |
| Noise | 27.8 | 61.3 | +33.5 |
| Layout | 51.3 | 74.9 | +23.6 |
| Total | 42.8 | 65.2 | +22.4 |

### RoboTwin 六任务（表 3）
| 任务族 | Base | Ours | Δ |
|---|---|---|---|
| Touch | 92.0→99.5 (Alarm), 85.5→100.0 (Bell) | — | +11.0 |
| Move/Place | 6.5→40.5 (Pill), 0.0→27.0 (Phone) | — | +30.5 |
| Contact | 43.0→93.5 (Stapler), 4.5→11.0 (Switch) | — | +28.5 |
| Overall | 38.6% (35.9–41.4%) | 61.9% (59.1–64.6%) | +23.3 |

### 消融（表 4，LIBERO-10）
| 配置 | 成功率 |
|---|---|
| Native Base | 92.88 ± 1.01 |
| Depth only | 94.00 ± 1.00（Δ +1.12） |
| Cross-view only | 94.21 ± 2.40（Δ +1.33） |
| Full | 97.00 ± 1.50（Δ +4.12） |

### 表示诊断
- 深度 MAE：原生 4.3 cm → 几何注入后 0.78 cm（单帧每视图）；全评估均值从 4.9 降至 0.44 cm，2 cm 内预测从 44% 升至 97%。
- 跨视角检索 Hit@1：原生 0.4%（随机 0.3%）→ 几何注入后 64%。

### 真实机器人（Agibot Expedition A2）
- Ours：49/60 成功（81.7%；70.1–89.4%）；Base：40/60（66.7%；54.1–77.3%）。两任务均改善：17/30→21/30 和 23/30→28/30。

## 边界与局限

- MVUCF 假设训练时校准准确；对损坏或噪声校准标签的鲁棒性未测试。
- 几何注入隐式地将训练时相机参数纳入学习到的几何表示，限制了在相机视点和视场扰动下的改进。
- 真实机器人实验中置信区间重叠（81.7% vs 66.7%），仅提供试点规模物理可行性证据。
- 未进行基于验证或下游成功率的检查点选择，使用预声明 horizon 的最终检查点。
- 透明、反射和无纹理区域可产生缺失或有偏深度，由有效性掩码排除但未单独评估。
- 两轮 RoboTwin 评估不足以支持轮间方差的稳定估计，报告聚合二项不确定性而非重训练变异性。

## 工程启示

- **复现优先核对**：几何注入与动作训练必须使用同一批官方开源演示轨迹（LIBERO 每套件 100 episodes，RoboTwin 每任务 50 条 clean50 划分），否则对比无效。训练超参（LR 10⁻⁴、WD 10⁻⁵、预热 0.05、batch 128）需严格匹配官方 GR00T-N1.6 微调默认值。
- **最容易踩坑处**：预处理感知坐标映射 T_img→grid 必须完整实现 unshuffle、patch、resize、crop、letterbox 的组合变换，直接缩放原始像素到 token 坐标会引入标签误差。深度补全管线必须使用最近邻采样（非双线性），避免对象边界度量深度被人工平滑。
- **可见性阈值 0.10 m 是经验操作点**：更紧会因深度量化丢弃有效对，更松会在遮挡边界引入模糊投影。该值应在目标构建阶段固定，不基于下游成功率选择。
- **层选择不可随意**：监督抽取点选第 15 层（动作模块直接消费的最终隐藏空间网格），放在第 12 层会降低 token 级分离。更新范围（层 8–15）跨数据集固定，不按基准调参。
- **部署验证**：确认推理图保持纯 RGB-only，无额外传感器、模块或推理 FLOPs；相机校准仅用于离线目标构建，部署策略不消费相机矩阵。

## Overview
Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation, yet complex contact-rich tasks often benefit from multi-camera observations that jointly capture the end effector, objects, and targets under occlusion. Existing multi-camera VLAs usually concatenate view tokens, leaving action representations weak in metric depth and inconsistent across cameras. We introduce Multi-View Unified Camera Fields (MVUCF), a training-only framework that forms a shared action-facing latent field across views. A coordinate-query depth objective makes metric depth recoverable, while a preprocessing-aware correspondence objective aligns tokens observing the same physical point from different cameras. Both directly shape the hidden states consumed by the action module. After geometry injection, depth, camera calibration, and auxiliary heads are removed, so deployment uses the original RGB-only graph with no extra inference FLOPs. Held-out probes confirm stronger depth recovery and cross-view matching. Under matched GR00T-N1.6 settings, MVUCF reaches 98.9% on LIBERO, improves LIBERO-Plus by 22.4 points, and raises success by 23.3 points across six RoboTwin tasks spanning three action families: touch, move-and-place, and contact interaction. Real-world humanoid experiments further provide evidence of its practical effectiveness under RGB-only deployment.

## 参考
- https://arxiv.org/abs/2608.01826

## 개요

MVUCF는 학습 시에만 적용되는 프레임워크로, 액션 모듈이 소비하는 토큰 그리드에 측정적 깊이(metric depth)와 교차 뷰 대응(cross-view correspondence)이라는 두 가지 기하 속성을 공동으로 주입하여, 순수 RGB 입력만 사용하는 VLA 정책에 실용적인 3D 구조 인지 능력을 부여합니다. 이 방법은 NVIDIA 팀이 GR00T-N1.6을 기반으로 구현했으며, 2단계 학습(기하 주입 + 액션 학습)을 통해 배포 시 추가 센서나 추론 FLOPs 증가 없이 다중 카메라 조작 작업의 성공률과 강건성을 크게 향상시킵니다.

## 무엇을 바꾸었는가

기존 VLA 모델은 접촉이 많은 다중 카메라 조작 작업에서 근본적인 표현 결함에 직면합니다: 백본 네트워크가 2D 의미론적 사전 학습된 VLM에서 초기화되므로, 그 은닉 상태는 측정적 깊이(원래 MAE 4.3 cm)와 교차 뷰 대응(Hit@1 0.4%로, 무작위 0.3%에 근접)을 신뢰할 수 있게 복원하지 못합니다. 이전 연구인 Spatial Forcing과 Selfi는 각각 교차 뷰 일관성과 측정적 3D 접지를 해결했지만, 두 메커니즘의 차이가 너무 커서 모듈식으로 결합할 수 없었습니다. MVUCF가 실제로 바꾼 것은: 배포 인터페이스(여전히 순수 RGB)를 변경하지 않고도, 학습 시 기하 감독 주입만으로 VLM 백본의 은닉 상태가 선형적으로 읽을 수 있는 측정적 깊이와 교차 뷰 물리적 점 대응을 동시에 갖출 수 있음을 증명했다는 점입니다. 이는 "기하 인식은 반드시 추가 센서나 추론 시 모듈에 의존해야 한다"는 암묵적 가정을 깨고, 기하 능력을 보조 분기에서 액션 모듈이 직접 소비하는 백본 표현으로 이동시켰습니다.

## 방법 분석

### 2단계 학습 프로세스
1. **기하 주입 단계**: VLM 레이어 8–15와 두 개의 보조 헤드(깊이 헤드, 교차 뷰 헤드)만 업데이트하고, 비전 인코더와 레이어 0–7은 동결합니다. 업데이트 범위는 데이터셋 전반에 걸쳐 고정되며, 하위 벤치마크에 기반하여 선택되지 않습니다.
2. **액션 학습 단계**: 보조 헤드, 깊이 관측, 카메라 보정을 제거하고, 기하적으로 형성된 백본을 동결한 채 RGB-only 입력으로 원래 액션 모듈을 학습합니다.

### 좌표 쿼리 깊이 목표(Coordinate-Query Depth Objective)
- 9×9 토큰 그리드 위에 144×144 연속 쿼리 격자(밀집 쿼리 팩터 P=16)를 정의합니다.
- 각 뷰에서 3072개 쿼리를 추출: 50% 균일 샘플링, 50%는 표면 근처와 깊이 경계에 편향된 중요도 샘플링.
- 쿼리 표현은 1024차원 특징, 로컬 x/y 차이, 서브유닛 위상 φ(q)=q-⌊q⌋를 연결하여 3074차원 입력을 형성하며, 절대 위치 인코딩은 없습니다.
- 깊이 헤드: LN(2048)→Linear(1024)→GELU→Conv 3×3(1024)→GELU의 GridTrunk 후, 쌍선형 특징 조회, MLP 3074→1024→1024→1 + Softplus로 측정적 깊이를 예측합니다.
- 손실: L_depth = 0.5·L_silog + 1.25·L_inv + 1.0·L_grad + 0.1·L_seam + 0.05·L_unc, 유효 깊이 범위는 [0.05, 5.0] m.

### 전처리 인지 대응 목표(Preprocessing-Aware Correspondence Objective)
- 양성 샘플은 원본 프레임의 기하 재투영으로 정의되며, 시각적 유사성이 아닙니다. 결합 변환 T_img→grid = T_unshuffle(2) ∘ T_patch(14) ∘ T_smart ∘ T_resize2 ∘ T_crop ∘ T_resize1 ∘ T_letterbox를 통해 좌표 라벨 오류를 방지합니다.
- 유효성 검사: 목표가 이미지 경계 내에 있고, 깊이가 [0.05, 5.0] m이며, z-buffer 일관성 |Z_j - z_j*(u_j^raw)| < 0.10 m를 만족해야 합니다.
- 공유 프로젝터는 극도로 단순합니다: h_ω(f) = normalize₂(W·LN₂₀₄₈(f)), W ∈ R^{128×2048}, 은닉 레이어 없음.
- 전역 매칭 로짓 ℓ_mn = 10(e_m^s)ᵀ e_n^t; 소프트 라벨 y_mn ∝ exp(-‖c_n - q_j*‖²/(2σ²)), σ=0.75.
- 손실: L_cv = L_softCE + 0.1·L_hnce + 0.1·L_margin, γ=0.2, 외부 가중치는 40k 스텝 동안 1.0에서 0.1로 감소.

### 핵심 설계 결정
- 깊이는 뷰 내 측정적 위치를 설정하고, 대응은 교차 뷰 물리적 점 정체성을 설정하며, 둘은 상호 보완적이고 액션 모듈이 소비하는 상위 은닉 상태를 직접 업데이트합니다.
- 감독 추출 지점은 (12번째 레이어가 아닌) 15번째 레이어에서 선택되는데, 이는 더 강한 동일 점 판별력을 유지하고 액션 모듈이 직접 소비하는 최종 은닉 공간 그리드이기 때문입니다.
- 공간적 소프트 양성 샘플은 서브토큰 투영 오류를 흡수하고, 공간적 링 음성 샘플은 인접 패치가 동등한 매칭으로 붕괴되는 것을 방지합니다.

## 핵심 혁신

1. **교차 뷰 일관성과 측정적 3D 구조를 동시에 복원하는 통합 프레임워크**: 이전 방법은 각각을 개별적으로 해결했지만 결합할 수 없었던 반면, MVUCF는 동일한 토큰 그리드에 두 상보적 속성을 공동으로 주입하여, 두 개의 분리된 보조 표현이 아닌 교차 카메라 공유 액션 지향 잠재 필드를 형성합니다.
2. **전처리 인지 좌표 매핑**: 전체 이미지 전처리 체인(unshuffle, patch, resize, crop, letterbox)의 결합 변환을 명시적으로 모델링하여, 원본 픽셀을 토큰 좌표로 직접 스케일링할 때 발생하는 라벨 오류를 방지합니다. 이는 공학적으로 쉽게 간과되지만 기하 감독 정밀도에 영향을 미치는 핵심 세부 사항입니다.
3. **쿼리 패턴 깊이 감독**: 매 학습 스텝의 밀집 전체 이미지 예측을 감독하는 대신, 3072개 쿼리 지점(표면 근처와 경계에 편향된 중요도 샘플링 포함)을 통해 연속 그리드 위치에서 측정적 깊이를 감독하고, 기울기 항으로 일정 깊이 붕괴를 방지하여 학습 효율과 기하 정밀도 사이의 균형을 달성합니다.

## 실험 및 결과

### LIBERO 표준 벤치마크 (표 1)
| 지표 | Base (GR00T-N1.6) | Ours | Δ |
|---|---|---|---|
| Spatial | 99.3 ± 1.2 | 100.0 ± 0.0 | +0.7 |
| Object | 99.2 ± 0.8 | 99.2 ± 0.3 | 0.0 |
| Goal | 98.4 ± 1.2 | 99.5 ± 0.5 | +1.1 |
| Long | 92.9 ± 1.0 | 97.0 ± 1.5 | +4.1 |
| Average | 97.4 ± 0.3 | 98.9 ± 0.4 | +1.5 |

### LIBERO-Plus 강건성 (표 2)
| 교란 유형 | Base | Ours | Δ |
|---|---|---|---|
| Camera | 20.9 | 24.1 | +3.2 |
| Robot | 40.2 | 54.1 | +13.9 |
| Language | 35.0 | 72.9 | +37.9 |
| Light | 65.4 | 95.1 | +29.7 |
| Background | 76.3 | 91.8 | +15.5 |
| Noise | 27.8 | 61.3 | +33.5 |
| Layout | 51.3 | 74.9 | +23.6 |
| Total | 42.8 | 65.2 | +22.4 |

### RoboTwin 6개 작업 (표 3)
| 작업군 | Base | Ours | Δ |
|---|---|---|---|
| Touch | 92.0→99.5 (Alarm), 85.5→100.0 (Bell) | — | +11.0 |
| Move/Place | 6.5→40.5 (Pill), 0.0→27.0 (Phone) | — | +30.5 |
| Contact | 43.0→93.5 (Stapler), 4.5→11.0 (Switch) | — | +28.5 |
| Overall | 38.6% (35.9–41.4%) | 61.9% (59.1–64.6%) | +23.3 |

### 절제 연구 (표 4, LIBERO-10)
| 구성 | 성공률 |
|---|---|
| Native Base | 92.88 ± 1.01 |
| Depth only | 94.00 ± 1.00 (Δ +1.12) |
| Cross-view only | 94.21 ± 2.40 (Δ +1.33) |
| Full | 97.00 ± 1.50 (Δ +4.12) |

### 표현 진단
- 깊이 MAE: 원래 4.3 cm → 기하 주입 후 0.78 cm(단일 프레임, 뷰당); 전체 평가 평균은 4.9에서 0.44 cm로 감소, 2 cm 내 예측은 44%에서 97%로 증가.
- 교차 뷰 검색 Hit@1: 원래 0.4%(무작위 0.3%) → 기하 주입 후 64%.

### 실제 로봇 (Agibot Expedition A2)
- Ours: 49/60 성공 (81.7%; 70.1–89.4%); Base: 40/60 (66.7%; 54.1–77.3%). 두 작업 모두 개선: 17/30→21/30 및 23/30→28/30.

## 경계 및 한계

- MVUCF는 학습 시 보정이 정확하다고 가정합니다; 손상되거나 노이즈가 있는 보정 라벨에 대한 강건성은 테스트되지 않았습니다.
- 기하 주입은 학습 시 카메라 파라미터를 학습된 기하 표현에 암묵적으로 포함시켜, 카메라 시점 및 시야각 교란 하에서의 개선을 제한합니다.
- 실제 로봇 실험에서 신뢰 구간이 겹치며(81.7% vs 66.7%), 파일럿 규모의 물리적 실현 가능성 증거만 제공합니다.
- 검증 또는 하위 성공률 기반 체크포인트 선택은 수행되지 않았으며, 사전 선언된 horizon의 최종 체크포인트가 사용되었습니다.
- 투명, 반사, 무질감 영역은 누락되거나 편향된 깊이를 생성할 수 있으며, 유효성 마스크로 제외되지만 별도로 평가되지는 않았습니다.
- 두 차례의 RoboTwin 평가는 라운드 간 분산의 안정적 추정을 지원하기에 충분하지 않으며, 보고된 것은 재학습 변동성이 아닌 집계된 이항 불확실성입니다.

## 공학적 시사점

- **재현 시 우선 확인 사항**: 기하 주입과 액션 학습은 동일한 공식 오픈소스 데모 궤적(LIBERO 각 스위트 100 에피소드, RoboTwin 각 작업 50개 clean50 분할)을 사용해야 하며, 그렇지 않으면 비교가 무효합니다. 학습 하이퍼파라미터(LR 10⁻⁴, WD 10⁻⁵, 워밍업 0.05, batch 128)는 공식 GR00T-N1.6 미세조정 기본값과 엄격히 일치해야 합니다.
- **가장 함정에 빠지기 쉬운 부분**: 전처리 인지 좌표 매핑 T_img→grid는 unshuffle, patch, resize, crop, letterbox의 결합 변환을 완전히 구현해야 하며, 원본 픽셀을 토큰 좌표로 직접 스케일링하면 라벨 오류가 발생합니다. 깊이 완성 파이프라인은 최근접 이웃 샘플링(쌍선형 아님)을 사용해야 하며, 객체 경계의 측정적 깊이가 인위적으로 평활화되는 것을 방지해야 합니다.
- **가시성 임계값 0.10 m는 경험적 운영 지점입니다**: 더 엄격하면 깊이 양자화로 유효 쌍이 버려지고, 더 느슨하면 폐색 경계에서 모호한 투영이 발생합니다. 이 값은 목표 구축 단계에서 고정되어야 하며, 하위 성공률에 기반하여 선택되지 않아야 합니다.
- **레이어 선택은 임의로 할 수 없습니다**: 감독 추출 지점은 15번째 레이어(액션 모듈이 직접 소비하는 최종 은닉 공간 그리드)에서 선택되며, 12번째 레이어에 두면 토큰 수준 분리가 저하됩니다. 업데이트 범위(레이어 8–15)는 데이터셋 전반에 걸쳐 고정되며, 벤치마크별로 조정되지 않습니다.
- **배포 검증**: 추론 그래프가 순수 RGB-only로 유지되고, 추가 센서, 모듈 또는 추론 FLOPs가 없음을 확인하십시오; 카메라 보정은 오프라인 목표 구축에만 사용되며, 배포 정책은 카메라 행렬을 소비하지 않습니다.
