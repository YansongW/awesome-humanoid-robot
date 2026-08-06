---
$id: ent_paper_v_jepa_2_self_supervised_video_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning'
  zh: 'V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning'
  ko: 'V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning'
summary:
  en: A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper
    explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot
    trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train
    an action-free.
  zh: V-JEPA 2 是 Meta FAIR 与 Mila 联合提出的自监督视频世界模型，通过两阶段训练（互联网规模视频预训练 + 少量交互数据后训练）实现视频理解、未来预测与机器人规划。核心贡献在于证明基于表示空间的视频预测（而非像素生成）能以
    62 小时无标签机器人视频实现跨实验室零样本操作，并在多个视频理解基准上刷新 SOTA。
  ko: A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper
    explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot
    trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train
    an action-free.
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
- v
- jepa
- '2'
- self
- supervised
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P067. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2506.09985 V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Plan'
  url: https://arxiv.org/abs/2506.09985
  date: '2025-06-11'
  accessed_at: '2026-08-05'
---

## 概述

V-JEPA 2 是 Meta FAIR 与 Mila 联合提出的自监督视频世界模型，通过两阶段训练（互联网规模视频预训练 + 少量交互数据后训练）实现视频理解、未来预测与机器人规划。核心贡献在于证明基于表示空间的视频预测（而非像素生成）能以 62 小时无标签机器人视频实现跨实验室零样本操作，并在多个视频理解基准上刷新 SOTA。

## 它改变了什么

这篇工作真正改变的是“世界模型必须依赖生成式视频预测”这一隐含假设。此前基于视频生成的动作条件模型（如 Cosmos）在机器人控制中表现有限，主要因为像素级预测的计算成本与保真度压力挤占了规划能力。V-JEPA 2 将预测目标从像素空间转移到学习到的表示空间，用 L1 特征匹配替代像素重建，使规划在 16 秒内完成而 Cosmos 需要 4 分钟——这不是工程优化，而是范式选择：世界模型的价值在于捕捉任务相关的抽象状态变化，而非视觉细节。

另一个被挑战的假设是“语言监督是视觉编码器性能关键”。V-JEPA 2 在无任何语言监督的预训练下，于视频问答任务（如 MVP 44.5、TemporalBench 36.7）上超越 InternVL-2.5、Qwen2.5VL 等有语言监督的模型，说明自监督视频预训练能学到与语言对齐互补的时序与物理常识。这为多模态模型提供了新的视觉骨干选项，尤其在数据稀缺的机器人领域。

## 方法拆解

### 两阶段训练流程
- **阶段一（V-JEPA 2 预训练）**：在 VideoMix22M（2200 万视频）上优化掩码去噪目标：
  `minimize_{θ,φ,Δ_y} ||P_φ(Δ_y, E_θ(x)) - sg(E_θ̄(y))||_1`
  其中 `sg` 为停止梯度，`θ̄` 为 EMA 教师权重，损失仅作用于掩码 patch。架构为 ViT 编码器 + ViT 预测器，关键设计是 **3D-RoPE**（将特征维度分为时间/高度/宽度三段分别施加 1D 旋转），替代绝对位置编码以稳定 1B 模型训练。
- **阶段二（V-JEPA 2-AC 后训练）**：冻结编码器，训练 300M 参数动作条件预测器（24 层、16 头、隐藏维度 1024）。输入为 4 秒视频（16 帧、256×256、4fps）、7 维末端执行器状态及 7 维动作序列。损失为教师强制（T=15）与两步展开（T=2）之和，采用块因果注意力使当前 patch 可关注历史动作与状态。

### 规划推理（MPC）
- 目标函数：`E(â_{1:T}; z_k, s_k, z_g) = ||P(â_{1:T}; s_k, z_k) - z_g||_1`
- 使用交叉熵方法（CEM）优化：采样 800 个动作轨迹，经 10 次迭代细化，每次保留 top-10 更新高斯分布均值方差
- 动作约束在 L1-Ball 半径 0.075 内（对应约 13 cm 位移）
- 拾取-放置任务通过多目标切换实现：先优化 4 步针对抓取子目标，再 10 步针对放置子目标，最后 4 步针对最终目标

### 关键扩展要素
1. 数据从 200 万增至 2200 万视频（+1.0 点）
2. 模型从 300M 扩至 1B 参数（+1.5 点）
3. 训练迭代从 90K 增至 252K（+0.8 点）
4. 渐进式分辨率训练：cooldown 阶段将时长从 16 增至 64 帧、分辨率从 256 增至 384（累计 +4.0 点，GPU 时间减少 8.4×）

## 关键创新

1. **表示空间预测替代像素生成**：这是最本质的创新。V-JEPA 2-AC 在特征空间做自回归预测，避免了像素重建的计算开销与视觉细节干扰，使规划速度比 Cosmos 快 15 倍（16 秒 vs 4 分钟/动作），同时保持对物体恒常性、重力等物理规律的表征能力（可视化实验显示夹爪张开时杯子位置不变）。

2. **无语言监督的视觉编码器在 VidQA 上超越有语言监督模型**：V-JEPA 2 在冻结编码器设置下，于 MVP（44.5）、TemporalBench（36.7）、TOMATO（40.3）等时序理解基准上显著优于 DINOv2、SigLIP2、Perception Encoder，证明自监督视频预训练能学到与语言对齐互补的时序常识，挑战了“语言监督是视觉编码器性能关键”的主流观点。

3. **零样本机器人操作**：仅用 62 小时无标签 Droid 视频（无奖励、无任务元数据）后训练，在两个未见过的实验室 Franka 机械臂上实现 100% 到达、65% 抓杯、80% 拾取-放置成功率，远超行为克隆基线 Octo（15% 抓杯、15% 拾取-放置）。这证明世界模型加 MPC 可以替代大规模模仿学习，为机器人数据稀缺问题提供新路径。

## 实验与结果

### 机器人操作（表 2、表 3）
| 方法 | 实验室 | Reach | Grasp Cup | Grasp Box | Pick-&-Place Cup | Pick-&-Place Box |
|------|--------|-------|-----------|-----------|-------------------|-------------------|
| Octo | Avg | 100% | 15% | 0% | 15% | 10% |
| V-JEPA 2-AC | Avg | 100% | 65% | 25% | 80% | 65% |
| Cosmos | Lab 2 | 80% | 0% | 20% | 0% | 0% |

V-JEPA 2-AC 在抓取与拾取-放置任务上显著优于 Octo（行为克隆）与 Cosmos（视频生成）。规划速度：V-JEPA 2-AC 每动作 16 秒（800 样本），Cosmos 需 4 分钟（80 样本），完整拾取-放置轨迹 Cosmos 需超 1 小时。

### 视频理解（表 4、表 5）
| 方法 | 参数 | SSv2 | K400 | EK100 Action |
|------|------|------|------|--------------|
| InternVideo2-6B | 6B | 67.7 | 88.8 | – |
| V-JEPA 2 ViT-g 384 | 1B | 77.3 | 87.3 | 39.7 |

V-JEPA 2 在 SSv2 上以 1B 参数超越 6B 的 InternVideo2（77.3 vs 67.7）。EK100 动作预期 recall-at-5 达 39.7，相对 PlausiVL（27.6）提升 44%（由表内数值 39.7→27.6 计算）。

### 视频问答（表 6、表 7、表 8）
| 方法 | 平均 | PerceptionTest | MVP | TempCompass | TemporalBench | TOMATO |
|------|------|----------------|-----|-------------|---------------|--------|
| V-JEPA 2 ViT-g 512（冻结） | 52.3 | 72.0 | 31.1 | 69.2 | 33.3 | 37.0 |
| V-JEPA 2 ViT-g 384 Llama 3.1 8B | 59.5 | 84.0 | 44.5 | 76.9 | 36.7 | 40.3 |
| PLM 8B | 56.7 | 82.7 | 39.7 | 72.7 | 28.3 | 33.2 |

端到端训练下，V-JEPA 2 在 6 个基准平均分上超越 PerceptionLM 8B（59.5 vs 56.7），尤其在 TemporalBench 提升 8.4 点（由表内数值 36.7→28.3 计算）。

### 消融（扩展分析）
- 数据 2M→22M：+1.0 点；模型 300M→1B：+1.5 点；训练 90K→252K：+0.8 点
- 分辨率 256→384 且时长 16→64 帧：累计 +4.0 点至 88.2%
- 渐进式分辨率训练：GPU 时间减少 8.4×
- 数据整理（Curated-YT1B）：+1.4 点平均改进

## 边界与局限

- **相机位置敏感性**：V-JEPA 2-AC 未做显式标定，需隐式从单目 RGB 推断动作坐标轴；当机器人基座不在视野中时问题定义不明确，实践中需手动尝试不同相机位置（约 35°-85° 范围）
- **长时程规划受限**：自回归预测存在误差累积，表示空间精度随 rollout 长度下降；扩展到 128/256 帧未见进一步改进，长时程任务需引入子目标
- **任务指定方式单一**：仅支持图像目标，不支持语言目标；作者承认未来需与语言模型对齐
- **EK100 未完全解决**：存在动词/名词预测错误的失败案例，仅关注 1 秒预期时间，更长时程精度下降；限于厨房环境与封闭词汇表
- **基线比较非严格公平**：不同编码器在不同数据上预训练（如 DINOv2 在 LVD-142M），只能做系统级比较

## 工程启示

- **复现优先级**：先核对 3D-RoPE 实现（将特征维度三等分分别旋转）与 EMA 教师权重（0.99925），这是稳定 1B 模型训练的关键；其次确认渐进式训练调度（warmup 12K + constant 228K + cooldown 12K），cooldown 阶段同时增加时长与分辨率是收益最大来源
- **机器人部署最容易踩坑**：相机位置对动作坐标轴推断影响极大，务必先扫描机器人底座周围 35°-85° 的相机位姿；训练时仅用左外参相机视图（同时使用左右视图会降低性能）；动作约束半径 0.075 对应约 13 cm 位移，需根据实际机械臂工作空间调整
- **规划参数选择**：CEM 用 800 样本、10 次迭代、top-10 更新即可；规划视界 1 对贪婪任务足够，但非贪婪任务（如无图像子目标的拾取-放置）必须引入多目标切换机制
- **下游团队适配**：V-JEPA 2 编码器可直接替换现有 MLLM 的视觉骨干，冻结设置下已优于 DINOv2/SigLIP2；但注意其预训练分辨率为 256/384，直接上 512 需验证显存与性能权衡
- **数据整理不可跳过**：Curated-YT1B 相比未整理数据平均提升 1.4 点，且未整理数据在 epoch 600 后性能开始下降——长训练必须配合数据整理

## Overview
A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on Something-Something v2) and state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100) surpassing previous task-specific models. Additionally, after aligning V-JEPA 2 with a large language model, we demonstrate state-of-the-art performance on multiple video question-answering tasks at the 8 billion parameter scale (e.g., 84.0 on PerceptionTest, 76.9 on TempCompass). Finally, we show how self-supervised learning can be applied to robotic planning tasks by post-training a latent action-conditioned world model, V-JEPA 2-AC, using less than 62 hours of unlabeled robot videos from the Droid dataset. We deploy V-JEPA 2-AC zero-shot on Franka arms in two different labs and enable picking and placing of objects using planning with image goals. Notably, this is achieved without collecting any data from the robots in these environments, and without any task-specific training or reward. This work demonstrates how self-supervised learning from web-scale data and a small amount of robot interaction data can yield a world model capable of planning in the physical world.

## 参考
- https://arxiv.org/abs/2506.09985

## 개요

V-JEPA 2는 Meta FAIR와 Mila가 공동으로 제안한 자기 지도 비디오 세계 모델로, 2단계 훈련(인터넷 규모 비디오 사전 훈련 + 소량의 상호작용 데이터 후훈련)을 통해 비디오 이해, 미래 예측 및 로봇 계획을 구현합니다. 핵심 기여는 표현 공간 기반 비디오 예측(픽셀 생성이 아닌)이 62시간의 레이블 없는 로봇 비디오만으로도 교차 실험실 제로샷 조작을 가능하게 하고, 여러 비디오 이해 벤치마크에서 SOTA를 경신한다는 것을 입증한 것입니다.

## 그것이 바꾼 것

이 작업이 진정으로 바꾼 것은 "세계 모델은 반드시 생성적 비디오 예측에 의존해야 한다"는 암묵적 가정입니다. 이전의 비디오 생성 기반 행동 조건 모델(예: Cosmos)은 로봇 제어에서 제한적인 성능을 보였는데, 주로 픽셀 수준 예측의 계산 비용과 충실도 압박이 계획 능력을 잠식했기 때문입니다. V-JEPA 2는 예측 대상을 픽셀 공간에서 학습된 표현 공간으로 전환하고, L1 특징 매칭으로 픽셀 재구성을 대체하여 계획을 16초 내에 완료하는 반면 Cosmos는 4분이 필요합니다——이는 엔지니어링 최적화가 아니라 패러다임 선택입니다: 세계 모델의 가치는 작업 관련 추상 상태 변화를 포착하는 데 있으며, 시각적 세부 사항이 아닙니다.

또 다른 도전받은 가정은 "언어 감독이 시각 인코더 성능의 핵심"이라는 것입니다. V-JEPA 2는 언어 감독 없이 사전 훈련된 상태에서 비디오 질문 응답 작업(예: MVP 44.5, TemporalBench 36.7)에서 InternVL-2.5, Qwen2.5VL 등 언어 감독이 있는 모델을 능가하며, 자기 지도 비디오 사전 훈련이 언어 정렬과 상호 보완적인 시간적 및 물리적 상식을 학습할 수 있음을 보여줍니다. 이는 데이터가 부족한 로봇 분야에서 특히 다중 모달 모델에 새로운 시각적 백본 옵션을 제공합니다.

## 방법 분해

### 2단계 훈련 프로세스
- **1단계(V-JEPA 2 사전 훈련)**: VideoMix22M(2200만 비디오)에서 마스크된 노이즈 제거 목표 최적화:
  `minimize_{θ,φ,Δ_y} ||P_φ(Δ_y, E_θ(x)) - sg(E_θ̄(y))||_1`
  여기서 `sg`는 정지 그래디언트, `θ̄`는 EMA 교사 가중치, 손실은 마스크된 패치에만 적용됩니다. 아키텍처는 ViT 인코더 + ViT 예측기이며, 핵심 설계는 **3D-RoPE**(특징 차원을 시간/높이/너비 3개 세그먼트로 나누어 각각 1D 회전 적용)로, 절대 위치 인코딩을 대체하여 1B 모델 훈련을 안정화합니다.
- **2단계(V-JEPA 2-AC 후훈련)**: 인코더를 동결하고 300M 파라미터 행동 조건 예측기(24층, 16헤드, 은닉 차원 1024)를 훈련합니다. 입력은 4초 비디오(16프레임, 256×256, 4fps), 7차원 엔드 이펙터 상태 및 7차원 행동 시퀀스입니다. 손실은 교사 강제(T=15)와 2단계 전개(T=2)의 합이며, 블록 인과 어텐션을 사용하여 현재 패치가 과거 행동과 상태를 참조할 수 있게 합니다.

### 계획 추론(MPC)
- 목표 함수: `E(â_{1:T}; z_k, s_k, z_g) = ||P(â_{1:T}; s_k, z_k) - z_g||_1`
- 교차 엔트로피 방법(CEM)으로 최적화: 800개 행동 궤적 샘플링, 10회 반복 정제, 각 반복에서 top-10을 유지하여 가우시안 분포 평균/분산 업데이트
- 행동은 L1-Ball 반경 0.075 내로 제약(약 13cm 변위에 해당)
- 집기-놓기 작업은 다중 목표 전환으로 구현: 먼저 4단계로 집기 하위 목표 최적화, 그 다음 10단계로 놓기 하위 목표, 마지막 4단계로 최종 목표

### 핵심 확장 요소
1. 데이터 200만 → 2200만 비디오(+1.0점)
2. 모델 300M → 1B 파라미터(+1.5점)
3. 훈련 반복 90K → 252K(+0.8점)
4. 점진적 해상도 훈련: cooldown 단계에서 지속 시간 16 → 64프레임, 해상도 256 → 384(누적 +4.0점, GPU 시간 8.4× 감소)

## 핵심 혁신

1. **표현 공간 예측이 픽셀 생성을 대체**: 이것이 가장 본질적인 혁신입니다. V-JEPA 2-AC는 특징 공간에서 자기 회귀 예측을 수행하여 픽셀 재구성의 계산 오버헤드와 시각적 세부 사항 간섭을 피하고, 계획 속도를 Cosmos보다 15배 빠르게(16초 vs 4분/행동) 하면서도 객체 항상성, 중력 등 물리 법칙의 표현 능력을 유지합니다(시각화 실험에서 집게가 열려도 컵 위치가 변하지 않음을 보여줌).

2. **언어 감독 없는 시각 인코더가 VidQA에서 언어 감독 모델을 능가**: V-JEPA 2는 동결 인코더 설정에서 MVP(44.5), TemporalBench(36.7), TOMATO(40.3) 등 시간적 이해 벤치마크에서 DINOv2, SigLIP2, Perception Encoder를 크게 능가하며, 자기 지도 비디오 사전 훈련이 언어 정렬과 상호 보완적인 시간적 상식을 학습할 수 있음을 입증하고, "언어 감독이 시각 인코더 성능의 핵심"이라는 주류 관점에 도전합니다.

3. **제로샷 로봇 조작**: 62시간의 레이블 없는 Droid 비디오(보상 없음, 작업 메타데이터 없음)만으로 후훈련하여, 두 개의 본 적 없는 실험실 Franka 로봇 팔에서 100% 도달, 65% 컵 집기, 80% 집기-놓기 성공률을 달성하며, 행동 클로닝 베이스라인 Octo(15% 컵 집기, 15% 집기-놓기)를 크게 능가합니다. 이는 세계 모델 + MPC가 대규모 모방 학습을 대체할 수 있음을 증명하며, 로봇 데이터 부족 문제에 새로운 경로를 제공합니다.

## 실험 및 결과

### 로봇 조작(표 2, 표 3)
| 방법 | 실험실 | Reach | Grasp Cup | Grasp Box | Pick-&-Place Cup | Pick-&-Place Box |
|------|--------|-------|-----------|-----------|-------------------|-------------------|
| Octo | Avg | 100% | 15% | 0% | 15% | 10% |
| V-JEPA 2-AC | Avg | 100% | 65% | 25% | 80% | 65% |
| Cosmos | Lab 2 | 80% | 0% | 20% | 0% | 0% |

V-JEPA 2-AC는 집기 및 집기-놓기 작업에서 Octo(행동 클로닝)와 Cosmos(비디오 생성)를 크게 능가합니다. 계획 속도: V-JEPA 2-AC는 행동당 16초(800샘플), Cosmos는 4분(80샘플)이 필요하며, 전체 집기-놓기 궤적은 Cosmos가 1시간 이상 필요합니다.

### 비디오 이해(표 4, 표 5)
| 방법 | 파라미터 | SSv2 | K400 | EK100 Action |
|------|------|------|------|--------------|
| InternVideo2-6B | 6B | 67.7 | 88.8 | – |
| V-JEPA 2 ViT-g 384 | 1B | 77.3 | 87.3 | 39.7 |

V-JEPA 2는 SSv2에서 1B 파라미터로 6B의 InternVideo2를 능가합니다(77.3 vs 67.7). EK100 행동 예측 recall-at-5는 39.7로, PlausiVL(27.6) 대비 44% 향상(표 내 수치 39.7→27.6으로 계산).

### 비디오 질문 응답(표 6, 표 7, 표 8)
| 방법 | 평균 | PerceptionTest | MVP | TempCompass | TemporalBench | TOMATO |
|------|------|----------------|-----|-------------|---------------|--------|
| V-JEPA 2 ViT-g 512(동결) | 52.3 | 72.0 | 31.1 | 69.2 | 33.3 | 37.0 |
| V-JEPA 2 ViT-g 384 Llama 3.1 8B | 59.5 | 84.0 | 44.5 | 76.9 | 36.7 | 40.3 |
| PLM 8B | 56.7 | 82.7 | 39.7 | 72.7 | 28.3 | 33.2 |

엔드투엔드 훈련에서 V-JEPA 2는 6개 벤치마크 평균 점수에서 PerceptionLM 8B를 능가하며(59.5 vs 56.7), 특히 TemporalBench에서 8.4점 향상(표 내 수치 36.7→28.3으로 계산).

### 소거 연구(확장 분석)
- 데이터 2M→22M: +1.0점; 모델 300M→1B: +1.5점; 훈련 90K→252K: +0.8점
- 해상도 256→384 및 지속 시간 16→64프레임: 누적 +4.0점으로 88.2% 도달
- 점진적 해상도 훈련: GPU 시간 8.4× 감소
- 데이터 정리(Curated-YT1B): 평균 +1.4점 개선

## 경계 및 한계

- **카메라 위치 민감성**: V-JEPA 2-AC는 명시적 캘리브레이션을 수행하지 않으며, 단안 RGB에서 행동 좌표축을 암시적으로 추론해야 합니다. 로봇 베이스가 시야에 없으면 문제 정의가 불명확하며, 실제로는 다양한 카메라 위치(약 35°-85° 범위)를 수동으로 시도해야 합니다.
- **장기 계획 제한**: 자기 회귀 예측은 오류 누적이 존재하며, 표현 공간 정확도는 rollout 길이에 따라 감소합니다. 128/256프레임으로 확장해도 추가 개선이 없었으며, 장기 작업에는 하위 목표 도입이 필요합니다.
- **작업 지정 방식 단일**: 이미지 목표만 지원하고 언어 목표는 지원하지 않습니다. 저자는 향후 언어 모델과의 정렬이 필요함을 인정합니다.
- **EK100 완전 해결 안 됨**: 동사/명사 예측 오류의 실패 사례가 존재하며, 1초 예측 시간에만 초점을 맞추고 더 긴 시간에서는 정확도가 감소합니다. 주방 환경과 폐쇄 어휘로 제한됩니다.
- **베이스라인 비교가 엄격히 공정하지 않음**: 서로 다른 인코더가 서로 다른 데이터에서 사전 훈련되었으며(예: DINOv2는 LVD-142M), 시스템 수준 비교만 가능합니다.

## 엔지니어링 시사점

- **재현 우선순위**: 먼저 3D-RoPE 구현(특징 차원을 3등분하여 각각 회전)과 EMA 교사 가중치(0.99925)를 확인하세요. 이는 1B 모델 훈련 안정화의 핵심입니다. 다음으로 점진적 훈련 스케줄(warmup 12K + constant 228K + cooldown 12K)을 확인하고, cooldown 단계에서 지속 시간과 해상도를 동시에 증가시키는 것이 수익이 가장 큰 원천입니다.
- **로봇 배포에서 가장 쉽게 함정에 빠지는 부분**: 카메라 위치가 행동 좌표축 추론에 큰 영향을 미치므로, 반드시 로봇 베이스 주변 35°-85°의 카메라 포즈를 먼저 스캔하세요. 훈련 시 왼쪽 외부 파라미터 카메라 뷰만 사용(좌우 뷰를 동시에 사용하면 성능 저하). 행동 제약 반경 0.075는 약 13cm 변위에 해당하며, 실제 로봇 팔 작업 공간에 따라 조정해야 합니다.
- **계획 파라미터 선택**: CEM은 800샘플, 10회 반복, top-10 업데이트로 충분합니다. 계획 지평 1은 탐욕적 작업에 충분하지만, 비탐욕적 작업(예: 이미지 하위 목표가 없는 집기-놓기)에는 반드시 다중 목표 전환 메커니즘을 도입해야 합니다.
- **하류 팀 적응**: V-JEPA 2 인코더는 기존 MLLM의 시각적 백본을 직접 대체할 수 있으며, 동결 설정에서 이미 DINOv2/SigLIP2보다 우수합니다. 단, 사전 훈련 해상도가 256/384이므로 512로 직접 올리려면 메모리와 성능 트레이드오프를 검증해야 합니다.
- **데이터 정리는 건너뛸 수 없음**: Curated-YT1B는 정리되지 않은 데이터보다 평균 1.4점 향상되며, 정리되지 않은 데이터는 epoch 600 이후 성능이 하락하기 시작합니다——긴 훈련에는 반드시 데이터 정리가 필요합니다.
