---
$id: ent_paper_vitacworld_scaling_visuo_tactile_world_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation'
  zh: 'ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation'
  ko: 'ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation'
summary:
  en: Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile
    sensing essential for robust control. However, scaling visuo-tactile robot learning remains difficult because real tactile
    interaction data are expensive to collect, hardware-dependent, and limited in task and scene diversity. We present ViTacWorld,
    an action-conditioned.
  zh: ViTacWorld 是一个动作条件视觉-触觉世界模型，由上海科技大学等机构提出，旨在为接触丰富操作生成合成视觉-触觉-动作轨迹。其核心贡献在于将世界建模能力从纯视觉扩展到视觉-触觉联合，并通过生成“梦境数据”增强下游触觉策略，同时可作为策略评估器使用。
  ko: Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile
    sensing essential for robust control. However, scaling visuo-tactile robot learning remains difficult because real tactile
    interaction data are expensive to collect, hardware-dependent, and limited in task and scene diversity. We present ViTacWorld,
    an action-conditioned.
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
- vitacworld
- scaling
- visuo
- tactile
- world
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
  title: 'arXiv:2607.22530 ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulati'
  url: https://arxiv.org/abs/2607.22530
  date: '2026-07-24'
  accessed_at: '2026-08-05'
---

## 概述

ViTacWorld 是一个动作条件视觉-触觉世界模型，由上海科技大学等机构提出，旨在为接触丰富操作生成合成视觉-触觉-动作轨迹。其核心贡献在于将世界建模能力从纯视觉扩展到视觉-触觉联合，并通过生成“梦境数据”增强下游触觉策略，同时可作为策略评估器使用。

## 它改变了什么

接触丰富操作（如插拔、剥离）中，触觉反馈是成功的关键，但真实触觉数据采集昂贵且受硬件寿命限制，模拟数据又存在 sim-to-real 差距。现有动作条件世界模型仅处理视觉流，无法合成触觉观测，因此不能作为下游触觉策略的数据生成器。ViTacWorld 真正改变了这一局面：它将触觉提升为与视觉同等地位的一等观测流，使世界模型能够生成时间对齐的视觉-触觉-动作轨迹，从而为触觉策略提供可扩展的训练数据来源。这一转变意味着触觉策略训练不再完全依赖昂贵的真实演示，而是可以通过世界模型合成数据来扩充。

## 方法拆解

### 整体框架
给定 H 步动作序列，预测未来视觉和触觉观测：ô_{t+1:t+H} = f_θ(o_t, u_{t:t+H-1}, m)，其中 m ∈ {0,1}^{|V|} 是视图存在掩码，V = {main, wrist, tactile}。

### 架构设计
- 扩展预训练动作条件视频世界模型，保留骨干和动作条件路径
- 各视图分别由 VAE 编码为潜在 token，组装为统一序列
- 引入流身份嵌入 e^v，投影到 AdaLN 调制路径
- 流感知自注意力：Z̃_b^v = SelfAttn_v(AdaLN(Z_{b-1}^v; c_b + P(e^v)))，P 为零初始化投影
- 跨视图注意力：Z_b^v = CrossViewAttn_v(Z̃_b^v, {Z̃_b^{v'}}_{v'≠v})，避免 token 不受控混合

### 训练目标
L_wm = E_{z_0,σ}[‖D_θ(z_σ, σ, o_t, u_{t:t+H-1}, m) − z_0‖²₂]，损失仅应用于未来帧和有效流。

### 两阶段训练
1. **预训练**：OmniViTac 公共数据（超过 21K 轨迹）加任务对齐模拟数据（超过 5K 轨迹），13 帧窗口，15 Hz 采样，32 块 H20 GPU，全局批量 256，30K 步，学习率 3 × 10⁻⁵
2. **微调**：真实演示加策略 rollout，全局批量 128，学习率 1 × 10⁻⁵，7K 步

### 模拟数据生成
在 Isaac Sim 中通过 Xense 触觉渲染管线合成触觉，3D 高斯扫描重建场景，EasyHeC 校准外参。

## 关键创新

1. **触觉作为一等观测流**：触觉不再作为辅助信号，而是与视觉流同等参与世界模型生成，保持时间对齐。这是首个将触觉纳入动作条件世界模型生成框架的工作。
2. **流感知自注意力与跨视图注意力分离**：避免相机和触觉 token 在普通自注意力中不受控混合，同时允许触觉流与视觉流交换接触信息。这一设计决策对多模态世界模型架构具有普适意义。
3. **梦境数据增强闭环**：世界模型生成的成功 rollout 与专家演示合并训练下游策略，再用增强策略生成更多 rollout 进行第二轮增强，形成数据飞轮。这为接触丰富操作的数据稀缺问题提供了可扩展的解决方案。

## 实验与结果

### 真实机器人成功率（表 1，每任务 10 次试验）

| 训练数据 | 策略 | Charger | Cucumber | U-Block | Cuboid | Avg |
|---|---|---|---|---|---|---|
| Expert only | ACT + tactile | 0 | 0 | 30 | 30 | 15.0 |
| Expert only | π_0.5 | 10 | 30 | 60 | 40 | 35.0 |
| Expert only | π_0.5 + tactile | 20 | 40 | 70 | 40 | 42.5 |
| Expert + ViTacWorld | ACT + tactile | 10 | 20 | 40 | 40 | 27.5 |
| Expert + ViTacWorld | π_0.5 | 30 | 60 | 60 | 40 | 47.5 |
| Expert + ViTacWorld | π_0.5 + tactile | 40 | 80 | 80 | 70 | 67.5 |

### 世界模型预测质量（表 2，held-out 验证）

| 视图 | 指标 | w/o pretraining | w/o task-aligned sim | Full |
|---|---|---|---|---|
| Main | PSNR | 22.718 | 23.128 | 24.258 |
| Main | SSIM | 0.7859 | 0.8011 | 0.8286 |
| Main | LPIPS | 0.0781 | 0.0687 | 0.0513 |
| Wrist | PSNR | 21.080 | 21.434 | 21.925 |
| Wrist | SSIM | 0.6649 | 0.6869 | 0.6962 |
| Wrist | LPIPS | 0.1084 | 0.0901 | 0.0725 |
| Tactile | PSNR | 34.967 | 35.127 | 35.225 |
| Tactile | SSIM | 0.9204 | 0.9296 | 0.9318 |
| Tactile | LPIPS | 0.0211 | 0.0179 | 0.0157 |

### 策略评估器（表 3）
真实成功率平均 67.5%，ViTacWorld 预测成功率平均 57.5%，差距 10.0 个百分点。表 4 显示 U-Block 任务 90.0% 初始条件一致性，无假阳性。

### 第二轮增强（表 5）
π_0.5 + tactile 策略平均成功率从 67.5% 提升至 80.0%，ACT + tactile 从 27.5% 提升至 42.5%。

触觉流 PSNR 增益不明显，因为非接触帧像素相似度已很高；LPIPS 改善表明预训练提升接触模式感知一致性。

## 边界与局限

- 成功梦境数据筛选仍部分依赖人工检查，未实现全自动过滤
- 未讨论模拟数据具体规模、训练计算成本、推理延迟
- 未与其他世界模型方法定量对比
- 第二轮增强在已饱和任务上收益有限
- 未进行更多轮次增强实验，未在更多任务或传感器类型上验证评估器性能
- 预测成功率略低于真实执行，表现为保守，对数据选择有利但可能低估策略能力

## 工程启示

复现时先核对预训练数据管线：OmniViTac 与模拟数据采样比约 2:1，13 帧窗口、15 Hz 采样是关键配置。最容易踩坑的是视图存在掩码 m 的处理——不完整轨迹参与预训练时，缺失流必须正确掩蔽，否则会破坏训练。微调阶段学习率从 3 × 10⁻⁵ 降至 1 × 10⁻⁵，全局批量从 256 降至 128，直接照搬可能不稳定。下游策略训练中 π_0.5 用批量 128、30K 步，ACT 用批量 16、10K 步，两者差异大，需分别调参。梦境数据筛选时注意 ViTacWorld 预测偏保守，假阳性少但可能漏掉有效轨迹，人工检查环节在早期可接受，规模化时需引入自动过滤。

## Overview
Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile sensing essential for robust control. However, scaling visuo-tactile robot learning remains difficult because real tactile interaction data are expensive to collect, hardware-dependent, and limited in task and scene diversity. We present ViTacWorld, an action-conditioned visuo-tactile world model for scalable contact-rich robot manipulation. ViTacWorld leverages public real tactile datasets and a constructed simulation environment to scale visuo-tactile-action data, exploiting the fact that tactile signals are directly grounded in physical contact and can exhibit a smaller simulation-to-real gap than purely visual observations. The model is first pretrained with large-scale real and simulated visuo-tactile trajectories, and then finetuned with real-world policy rollouts to better match downstream manipulation behaviors. Given robot actions, ViTacWorld predicts temporally aligned visual observations and tactile feedback, enabling visuo-tactile-action rollout generation. To the best of our knowledge, ViTacWorld is the first framework that uses a world model for robot visuo-tactile-action trajectory generation and policy evaluation. It serves two roles: synthesizing rollouts to improve downstream tactile policies, and evaluating policies by predicting action-conditioned visuo-tactile outcomes under controlled action sequences. Experiments on contact-rich manipulation tasks show that ViTacWorld generates physically meaningful rollouts, improves policy performance through scalable data augmentation, and enables action-conditioned policy evaluation. Project page: https://vitacworld.github.io/

## 参考
- https://arxiv.org/abs/2607.22530

## 개요

ViTacWorld는 상하이과학기술대학 등 기관이 제안한 행동 조건부 시각-촉각 세계 모델로, 접촉이 풍부한 조작을 위한 합성 시각-촉각-행동 궤적을 생성하는 것을 목표로 합니다. 핵심 기여는 세계 모델링 능력을 순수 시각에서 시각-촉각 결합으로 확장하고, "꿈 데이터" 생성을 통해 하류 촉각 정책을 강화하며, 정책 평가기로도 사용할 수 있다는 점입니다.

## 무엇을 바꾸었나

접촉이 풍부한 조작(예: 삽입, 박리)에서 촉각 피드백은 성공의 핵심이지만, 실제 촉각 데이터 수집은 비용이 높고 하드웨어 수명에 제한되며, 시뮬레이션 데이터는 sim-to-real 격차가 존재합니다. 기존 행동 조건부 세계 모델은 시각 스트림만 처리하여 촉각 관측을 합성할 수 없으므로 하류 촉각 정책의 데이터 생성기로 사용할 수 없습니다. ViTacWorld는 이러한 상황을 실질적으로 바꿉니다: 촉각을 시각과 동등한 지위의 일등 관측 스트림으로 승격시켜, 세계 모델이 시간적으로 정렬된 시각-촉각-행동 궤적을 생성할 수 있게 하여 촉각 정책에 확장 가능한 훈련 데이터 소스를 제공합니다. 이러한 전환은 촉각 정책 훈련이 더 이상 값비싼 실제 시연에 완전히 의존하지 않고, 세계 모델 합성 데이터로 확장할 수 있음을 의미합니다.

## 방법 분해

### 전체 프레임워크
H 단계 행동 시퀀스가 주어지면 미래 시각 및 촉각 관측을 예측합니다: ô_{t+1:t+H} = f_θ(o_t, u_{t:t+H-1}, m), 여기서 m ∈ {0,1}^{|V|}는 뷰 존재 마스크이고, V = {main, wrist, tactile}입니다.

### 아키텍처 설계
- 사전 훈련된 행동 조건부 비디오 세계 모델을 확장하고 백본과 행동 조건 경로를 유지
- 각 뷰는 VAE로 잠재 토큰으로 인코딩되어 통합 시퀀스로 조립
- 흐름 정체성 임베딩 e^v를 도입하고 AdaLN 변조 경로에 투영
- 흐름 인식 자기 주의: Z̃_b^v = SelfAttn_v(AdaLN(Z_{b-1}^v; c_b + P(e^v))), P는 제로 초기화 투영
- 교차 뷰 주의: Z_b^v = CrossViewAttn_v(Z̃_b^v, {Z̃_b^{v'}}_{v'≠v}), 토큰의 통제되지 않은 혼합 방지

### 훈련 목표
L_wm = E_{z_0,σ}[‖D_θ(z_σ, σ, o_t, u_{t:t+H-1}, m) − z_0‖²₂], 손실은 미래 프레임과 유효 스트림에만 적용됩니다.

### 2단계 훈련
1. **사전 훈련**: OmniViTac 공개 데이터(21K 이상 궤적)와 작업 정렬 시뮬레이션 데이터(5K 이상 궤적), 13프레임 창, 15Hz 샘플링, 32개 H20 GPU, 전역 배치 256, 30K 스텝, 학습률 3 × 10⁻⁵
2. **미세 조정**: 실제 시연과 정책 롤아웃, 전역 배치 128, 학습률 1 × 10⁻⁵, 7K 스텝

### 시뮬레이션 데이터 생성
Isaac Sim에서 Xense 촉각 렌더링 파이프라인을 통해 촉각을 합성하고, 3D 가우시안 스캔으로 장면을 재구성하며, EasyHeC로 외부 파라미터를 보정합니다.

## 핵심 혁신

1. **촉각을 일등 관측 스트림으로**: 촉각은 더 이상 보조 신호가 아니라 시각 스트림과 동등하게 세계 모델 생성에 참여하며 시간 정렬을 유지합니다. 이는 촉각을 행동 조건부 세계 모델 생성 프레임워크에 통합한 최초의 작업입니다.
2. **흐름 인식 자기 주의와 교차 뷰 주의 분리**: 카메라와 촉각 토큰이 일반 자기 주의에서 통제되지 않게 혼합되는 것을 방지하면서, 촉각 스트림과 시각 스트림이 접촉 정보를 교환할 수 있게 합니다. 이 설계 결정은 다중 모달 세계 모델 아키텍처에 일반적으로 의미가 있습니다.
3. **꿈 데이터 증강 폐쇄 루프**: 세계 모델이 생성한 성공 롤아웃과 전문가 시연을 병합하여 하류 정책을 훈련하고, 강화된 정책으로 더 많은 롤아웃을 생성하여 2차 증강을 수행하는 데이터 플라이휠을 형성합니다. 이는 접촉이 풍부한 조작의 데이터 부족 문제에 확장 가능한 해결책을 제공합니다.

## 실험 및 결과

### 실제 로봇 성공률(표 1, 작업당 10회 시도)

| 훈련 데이터 | 정책 | Charger | Cucumber | U-Block | Cuboid | 평균 |
|---|---|---|---|---|---|---|
| Expert only | ACT + tactile | 0 | 0 | 30 | 30 | 15.0 |
| Expert only | π_0.5 | 10 | 30 | 60 | 40 | 35.0 |
| Expert only | π_0.5 + tactile | 20 | 40 | 70 | 40 | 42.5 |
| Expert + ViTacWorld | ACT + tactile | 10 | 20 | 40 | 40 | 27.5 |
| Expert + ViTacWorld | π_0.5 | 30 | 60 | 60 | 40 | 47.5 |
| Expert + ViTacWorld | π_0.5 + tactile | 40 | 80 | 80 | 70 | 67.5 |

### 세계 모델 예측 품질(표 2, held-out 검증)

| 뷰 | 지표 | w/o pretraining | w/o task-aligned sim | Full |
|---|---|---|---|---|
| Main | PSNR | 22.718 | 23.128 | 24.258 |
| Main | SSIM | 0.7859 | 0.8011 | 0.8286 |
| Main | LPIPS | 0.0781 | 0.0687 | 0.0513 |
| Wrist | PSNR | 21.080 | 21.434 | 21.925 |
| Wrist | SSIM | 0.6649 | 0.6869 | 0.6962 |
| Wrist | LPIPS | 0.1084 | 0.0901 | 0.0725 |
| Tactile | PSNR | 34.967 | 35.127 | 35.225 |
| Tactile | SSIM | 0.9204 | 0.9296 | 0.9318 |
| Tactile | LPIPS | 0.0211 | 0.0179 | 0.0157 |

### 정책 평가기(표 3)
실제 성공률 평균 67.5%, ViTacWorld 예측 성공률 평균 57.5%, 차이 10.0% 포인트. 표 4는 U-Block 작업에서 90.0% 초기 조건 일관성, 거짓 양성 없음을 보여줍니다.

### 2차 증강(표 5)
π_0.5 + tactile 정책 평균 성공률이 67.5%에서 80.0%로, ACT + tactile이 27.5%에서 42.5%로 향상되었습니다.

촉각 스트림의 PSNR 이득은 뚜렷하지 않은데, 비접촉 프레임의 픽셀 유사도가 이미 높기 때문입니다. LPIPS 개선은 사전 훈련이 접촉 패턴 인식 일관성을 향상시킴을 시사합니다.

## 경계 및 한계

- 성공 꿈 데이터 선별은 여전히 부분적으로 수동 검사에 의존하며 완전 자동 필터링이 구현되지 않음
- 시뮬레이션 데이터의 구체적 규모, 훈련 계산 비용, 추론 지연 시간이 논의되지 않음
- 다른 세계 모델 방법과의 정량적 비교가 없음
- 2차 증강은 이미 포화된 작업에서 이득이 제한적
- 더 많은 라운드 증강 실험이 수행되지 않았고, 더 많은 작업이나 센서 유형에서 평가기 성능이 검증되지 않음
- 예측 성공률이 실제 실행보다 약간 낮아 보수적으로 나타나며, 데이터 선택에 유리하지만 정책 능력을 과소평가할 수 있음

## 엔지니어링 시사점

재현 시 먼저 사전 훈련 데이터 파이프라인을 확인하세요: OmniViTac와 시뮬레이션 데이터 샘플링 비율은 약 2:1이며, 13프레임 창, 15Hz 샘플링이 핵심 구성입니다. 가장 함정에 빠지기 쉬운 부분은 뷰 존재 마스크 m의 처리입니다 — 불완전한 궤적이 사전 훈련에 참여할 때 누락된 스트림을 올바르게 마스킹해야 하며, 그렇지 않으면 훈련이 손상됩니다. 미세 조정 단계에서 학습률은 3 × 10⁻⁵에서 1 × 10⁻⁵로, 전역 배치는 256에서 128로 감소하므로 그대로 적용하면 불안정할 수 있습니다. 하류 정책 훈련에서 π_0.5는 배치 128, 30K 스텝을 사용하고, ACT는 배치 16, 10K 스텝을 사용하므로 차이가 크므로 각각 파라미터를 조정해야 합니다. 꿈 데이터 선별 시 ViTacWorld 예측이 보수적이어서 거짓 양성이 적지만 유효 궤적을 놓칠 수 있으므로, 수동 검사 단계는 초기에 허용 가능하지만 규모 확장 시 자동 필터링 도입이 필요합니다.
