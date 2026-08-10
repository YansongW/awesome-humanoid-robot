---
$id: ent_paper_rynnworld_teleop_action_conditioned_worl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation'
  zh: 'RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation'
  ko: 'RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation'
summary:
  en: Scaling robot learning requires massive, diverse trajectory data, yet collection is currently bottlenecked by physical
    teleoperation, where every demonstration binds operator time to specific hardware and workspaces. We introduce digital
    teleoperation, a paradigm that decouples data collection from physical constraints by replacing the real robot with a
    generative world model. In this framework,.
  zh: RynnWorld-Teleop 是阿里巴巴 DAMO 团队提出的数字遥操作框架，用动作条件化世界模型替代物理机器人，将操作员手部姿态流实时合成为机器人第一人称视频。核心贡献在于首次同时满足机器人中心、动作接地、实时三大要求，并通过两阶段训练与自回归蒸馏实现
    40 fps 的交互式生成，且生成数据可直接用于策略训练。
  ko: Scaling robot learning requires massive, diverse trajectory data, yet collection is currently bottlenecked by physical
    teleoperation, where every demonstration binds operator time to specific hardware and workspaces. We introduce digital
    teleoperation, a paradigm that decouples data collection from physical constraints by replacing the real robot with a
    generative world model. In this framework,.
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
- rynnworld
- teleop
- action
- conditioned
- worl
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
  title: 'arXiv:2607.06558 RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation'
  url: https://arxiv.org/abs/2607.06558
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

RynnWorld-Teleop 是阿里巴巴 DAMO 团队提出的数字遥操作框架，用动作条件化世界模型替代物理机器人，将操作员手部姿态流实时合成为机器人第一人称视频。核心贡献在于首次同时满足机器人中心、动作接地、实时三大要求，并通过两阶段训练与自回归蒸馏实现 40 fps 的交互式生成，且生成数据可直接用于策略训练。

## 它改变了什么

物理遥操作的数据吞吐量被“操作员小时数 × 硬件可用性”锁死，手动环境重置与真实物体后勤更是让长尾交互分布遥不可及。现有两条路线都不够：人-to-机器人视频翻译（Phantom、Masquerade 等）只是被动观测，底层动作从未产生，重型 DiT 主干也排除了闭环；动作条件化第一人称模型（Hand2World、CosHand 等）仍以人为中心，渲染的手还是人手，具身差距没弥合。RynnWorld-Teleop 真正改变的是把数据采集从物理世界搬到生成式世界模型里——操作员的手势流被实时消费，以单张参考图像为条件合成机器人执行视频，同时手势本身作为与具身无关的动作标签，可经重定向迁移到任意机器人。这等于把数据引擎从“硬件绑定”变成“计算绑定”，吞吐量上限从操作员小时数变成 GPU 吞吐量。

## 方法拆解

### 深度感知动作表示
动作表示为源自 21 关节手部追踪的骨架视频序列。采用深度调制渲染，每个关节和骨骼的深度编码颜色映射和直径根据相机空间深度动态缩放，解决标准 2D 投影的深度模糊性。渲染姿态视频经预训练 VAE 编码为控制潜变量 c ∈ ℝ^(C×T×H×W)，与目标视频潜变量空间和时间对齐。

### 动作条件化视频生成
基于视频扩散 Transformer（DiT），图像到视频范式。并行控制 patch 嵌入层 PatchEmbed^c 通过可学习标量门控 α 与原始视频嵌入融合：
x = PatchEmbed^z(z_t) + α·PatchEmbed^c(c̃)
其中 c̃ = (c−μ_c)/σ_c·σ_z + μ_z 为分布对齐后的控制潜变量。PatchEmbed^c 零初始化，α 初始化为 0.1，保持预训练权重生成先验。

### 渐进式跨域训练
- **阶段 1**：在大规模第一人称人类视频（EgoDex、VITRA）上预训练，学习手-物交互动力学与骨架到视觉合成映射。EgoDex 分割为 81 帧片段，VITRA 提取 25 帧片段。
- **阶段 2**：在配对遥操作数据上微调，人类手势经逆运动学（IK）映射到机器人动作，所有轨迹分割为 81 帧片段。

### 自回归蒸馏
将双向教师蒸馏为因果学生，支持帧级自回归生成：
- **因果流匹配预热**：预测速度场，建立流式生成和控制跟随能力。
- **分布匹配蒸馏（DMD）**：4 步去噪实现高保真合成，学习判别器加冻结教师提供基于分数的梯度引导，持久 KV 缓存跨连续块反向传播最小化边界伪影。

### 数据生成管线
重定向用 Vive 追踪器（胸部、手腕、上臂）6-DoF 姿态，经校准坐标变换链映射工作空间，迭代阻尼最小二乘（DLS）逆运动学求解关节配置，上臂追踪器导出零空间肩部先验正则化。每个手势产生同步 54 维机器人动作向量（双 7-DoF 手臂 + 双 20-DoF 灵巧手）。分块重锚定采用 81 帧块生成策略，第一块用真实起始帧初始化，后续每块用机器人相机实际第一人称帧作为新 I_ref 重新锚定，防止视觉漂移。

## 关键创新

1. **深度感知骨架表示**：把 2D 投影的深度模糊性通过深度调制渲染解决，让动作条件在 3D 空间上真正接地，这是此前动作条件化世界模型没做到的。
2. **分布对齐加性条件机制**：用零初始化门控的加性融合而非标准拼接，保留预训练 DiT 的潜在分布，避免破坏生成先验——这是能在大模型基础上微调而不崩的关键设计。
3. **两阶段蒸馏课程**：先因果流匹配预热弥合双向与因果处理的结构差距，再 DMD 4 步蒸馏继承教师的手-物交互先验，同时保持 40 fps 实时性。这解决了“实时”与“高保真”的矛盾。

## 实验与结果

### 定量结果（Table 4，EgoDex-Test 域）
| 方法 | PSNR | SSIM | LPIPS | FVD | FPS |
|---|---|---|---|---|---|
| RynnWorld-Teleop (SFT) | 26.78 | 0.887 | 0.119 | 550 | 2.8 |
| RynnWorld-Teleop (LoRA) | 26.08 | 0.876 | 0.151 | 585 | 2.8 |
| RynnWorld-Teleop-Causal | 22.25 | 0.830 | 0.207 | 1226 | 40.0 |
| Wan-2.2-TI2V-5B (SFT) | 20.93 | 0.806 | 0.282 | 1223 | 2.8 |
| InterDyn | 21.47 | 0.831 | 0.279 | 655 | 2.9 |
| CosHand | 18.14 | 0.785 | 0.406 | 1527 | 0.8 |
| Mask2IV | 21.50 | 0.836 | 0.219 | 1650 | 0.9 |

### 消融研究（LoRA）
| 变体 | PSNR | SSIM | LPIPS | FVD | FPS |
|---|---|---|---|---|---|
| Concatenation Fusion | 19.69 | 0.821 | 0.260 | 1191 | 2.8 |
| w/o Human Pre-training | 17.81 | 0.763 | 0.453 | 2598 | 2.8 |
| w/o DMD (Causal) | 19.25 | 0.777 | 0.244 | 1338 | 40.0 |
| w/o Causal Warm-up (Causal) | 14.26 | 0.688 | 0.408 | 2150 | 40.0 |

### 真实世界策略性能（Table 3，成功率 %）
| 配置 | Dual Picking | Block Pushing | Bimanual Lifting | Lid Placement |
|---|---|---|---|---|
| π_0.5（300 Real） | 94.29 | 100.00 | 94.29 | 42.86 |
| π_0.5（300 Real + 300 生成） | 97.14 | 97.14 | 100.00 | 62.86 |
| π_0（300 Real） | 88.57 | 94.29 | 91.43 | 34.29 |
| π_0（0 Real + 300 生成） | 68.57 | 82.86 | 77.14 | 28.57 |
| π_0（300 Real + 300 生成） | 94.29 | 100.00 | 97.14 | 54.29 |

Lid Placement 任务中，π_0.5 成功率从 42.86% 提升至 62.86%（+20%），π_0 从 34.29% 提升至 54.29%（+20%）。π_0 仅用 300 个生成片段训练，Block Pushing 达 82.86%，Bimanual Lifting 达 77.14%。延迟分析：单块 H100 上 4 步流匹配调度，480×832 分辨率下吞吐量 40.0 fps，平均每帧延迟约 25 ms，分解为骨架动作编码约 5%、因果 DiT 去噪约 72%、视觉解码约 23%。

## 边界与局限

作者未在论文片段中明确列出局限性章节。从方法细节看，深度调制渲染虽捕获 3D 空间动态，但模型偶尔难以处理细粒度液体动力学或高度可变形物体操作。跨实体差距的弥合目前需要逐平台微调，限制了在机器人集群中的可扩展性。论文未明确提及对生成视频物理精确性的定量验证（接触力、物体动力学误差）、超长时程（远超 81 帧块）稳定性评估、不同机器人硬件迁移验证，以及操作员多样性（手部形态、追踪噪声）的影响。

## 工程启示

复现时先核对三件事：一是基础模型 Wan2.2-TI2V-5B 的权重获取与 TI2V 预热微调的 2,000 步设置，这是后续所有训练的前提；二是深度感知骨架渲染的深度调制参数，这直接影响动作接地的精度；三是分块重锚定的 81 帧块策略，这是防止长时程漂移的关键，别改成更短的块。最容易踩坑的地方是分布对齐条件机制——如果改成拼接融合，FVD 会从 550 恶化到 1191（由表内数值 550→1191 计算），说明加性门控设计不是可选项而是必需项。蒸馏阶段先做因果流匹配预热再做 DMD，跳过预热 FVD 会从 1226 恶化到 2150（由表内数值 1226→2150 计算）。下游团队用生成数据训练策略时，建议先做特征分布分析（t-SNE 重叠验证），再混合真实数据训练，纯生成数据在简单任务（Block Pushing）可行，但复杂任务（Lid Placement）仍需真实数据兜底。

## Overview
Scaling robot learning requires massive, diverse trajectory data, yet collection is currently bottlenecked by physical teleoperation, where every demonstration binds operator time to specific hardware and workspaces. We introduce digital teleoperation, a paradigm that decouples data collection from physical constraints by replacing the real robot with a generative world model. In this framework, an operator's hand-pose stream drives a robot-centric generative world model to synthesize high-fidelity egocentric videos from a single reference image. The recorded pose stream serves as an embodiment-agnostic action label transferable to any target robot via standard retargeting, yielding complete state-action trajectories for imitation learning independent of physical hardware. We instantiate this paradigm in RynnWorld-Teleop, a system that integrates depth-aware skeletal conditioning, progressive human-to-robot training on a video Diffusion Transformer, and streaming autoregressive distillation. This pipeline compresses the generative process into a single-pass inference, enabling 40+ FPS, real-time interactive generation on a single H100 GPU. Policies trained exclusively on RynnWorld-Teleop-generated data achieve effective zero-shot Sim2Real transfer across dexterous and diverse bimanual tasks. Moreover, augmenting real-world datasets with our digitally teleoperated data consistently improves success rates, demonstrating that RynnWorld-Teleop serves as a high-fidelity, scalable data engine for the next generation of robotic agents.

## 参考
- https://arxiv.org/abs/2607.06558

## 개요

RynnWorld-Teleop는 알리바바 DAMO 팀이 제안한 디지털 원격 조작 프레임워크로, 물리적 로봇을 동작 조건부 월드 모델로 대체하여 작업자의 손姿态 스트림을 실시간으로 로봇 1인칭 비디오로 합성합니다. 핵심 기여는 로봇 중심, 동작 접지, 실시간이라는 세 가지 요구 사항을 최초로 동시에 충족하고, 2단계 훈련과 자기회귀 증류를 통해 40fps의 인터랙티브 생성을 달성하며, 생성된 데이터를 정책 훈련에 직접 사용할 수 있다는 점입니다.

## 무엇을 바꾸었는가

물리적 원격 조작의 데이터 처리량은 "작업자 시간 × 하드웨어 가용성"에 묶여 있으며, 수동 환경 재설정과 실제 물체 물류는 롱테일 상호작용 분포를 도달 불가능하게 만듭니다. 기존의 두 가지 접근 방식 모두 부족합니다: 인간-로봇 비디오 번역(Phantom, Masquerade 등)은 수동적 관찰에 불과하며, 기본 동작이 생성되지 않고, 무거운 DiT 백본은 폐루프를 배제합니다; 동작 조건부 1인칭 모델(Hand2World, CosHand 등)은 여전히 인간 중심이며, 렌더링된 손은 여전히 사람의 손으로, 구현 격차가 해소되지 않았습니다. RynnWorld-Teleop가 실제로 바꾼 것은 데이터 수집을 물리적 세계에서 생성적 월드 모델로 옮긴 것입니다 — 작업자의 제스처 스트림이 실시간으로 소비되어 단일 참조 이미지를 조건으로 로봇 실행 비디오를 합성하고, 동시에 제스처 자체는 구현과 무관한 동작 레이블로 작용하여 재지정을 통해 임의의 로봇으로 전이될 수 있습니다. 이는 데이터 엔진을 "하드웨어 바인딩"에서 "컴퓨팅 바인딩"으로 바꾸어, 처리량 상한을 작업자 시간에서 GPU 처리량으로 전환합니다.

## 방법 분석

### 깊이 인식 동작 표현
동작은 21개 관절 손 추적에서 파생된 골격 비디오 시퀀스로 표현됩니다. 깊이 변조 렌더링을 채택하여 각 관절과 뼈의 깊이 인코딩 색상 매핑과 직경이 카메라 공간 깊이에 따라 동적으로 스케일링되어 표준 2D 투영의 깊이 모호성을 해결합니다. 렌더링된 포즈 비디오는 사전 훈련된 VAE로 인코딩되어 제어 잠재 변수 c ∈ ℝ^(C×T×H×W)가 되며, 대상 비디오 잠재 변수 공간 및 시간과 정렬됩니다.

### 동작 조건부 비디오 생성
비디오 확산 Transformer(DiT) 기반, 이미지-투-비디오 패러다임. 병렬 제어 패치 임베딩 레이어 PatchEmbed^c는 학습 가능한 스칼라 게이팅 α를 통해 원본 비디오 임베딩과 융합됩니다:
x = PatchEmbed^z(z_t) + α·PatchEmbed^c(c̃)
여기서 c̃ = (c−μ_c)/σ_c·σ_z + μ_z는 분포 정렬된 제어 잠재 변수입니다. PatchEmbed^c는 제로 초기화되고 α는 0.1로 초기화되어 사전 훈련된 가중치의 생성 사전을 유지합니다.

### 점진적 교차 도메인 훈련
- **단계 1**: 대규모 1인칭 인간 비디오(EgoDex, VITRA)에서 사전 훈련하여 손-물체 상호작용 역학 및 골격-투-시각 합성 매핑을 학습합니다. EgoDex는 81프레임 클립으로 분할되고, VITRA는 25프레임 클립으로 추출됩니다.
- **단계 2**: 쌍을 이루는 원격 조작 데이터에서 미세 조정하며, 인간 제스처는 역운동학(IK)을 통해 로봇 동작으로 매핑되고, 모든 궤적은 81프레임 클립으로 분할됩니다.

### 자기회귀 증류
양방향 교사를 인과적 학생으로 증류하여 프레임 수준 자기회귀 생성을 지원합니다:
- **인과적 흐름 매칭 워밍업**: 속도 장을 예측하여 스트리밍 생성 및 제어 추종 능력을 확립합니다.
- **분포 매칭 증류(DMD)**: 4단계 노이즈 제거로 고충실도 합성을 구현하고, 학습된 판별기와 동결된 교사가 점수 기반 기울기 안내를 제공하며, 지속 KV 캐시가 연속 블록에 걸쳐 역전파되어 경계 아티팩트를 최소화합니다.

### 데이터 생성 파이프라인
재지정은 Vive 트래커(가슴, 손목, 상완)의 6-DoF 포즈를 사용하며, 보정된 좌표 변환 체인을 통해 작업 공간에 매핑하고, 반복 감쇠 최소 제곱(DLS) 역운동학으로 관절 구성을 해결하며, 상완 트래커에서 파생된 널 공간 어깨 사전으로 정규화합니다. 각 제스처는 동기화된 54차원 로봇 동작 벡터(이중 7-DoF 팔 + 이중 20-DoF 손)를 생성합니다. 청크 재앵커링은 81프레임 블록 생성 전략을 채택하며, 첫 번째 블록은 실제 시작 프레임으로 초기화되고, 후속 각 블록은 로봇 카메라의 실제 1인칭 프레임을 새 I_ref로 재앵커링하여 시각적 드리프트를 방지합니다.

## 핵심 혁신

1. **깊이 인식 골격 표현**: 2D 투영의 깊이 모호성을 깊이 변조 렌더링으로 해결하여 동작 조건이 3D 공간에서 실제로 접지되도록 합니다. 이는 이전 동작 조건부 월드 모델이 달성하지 못한 것입니다.
2. **분포 정렬 가산 조건 메커니즘**: 표준 연결 대신 제로 초기화 게이팅의 가산 융합을 사용하여 사전 훈련된 DiT의 잠재 분포를 보존하고 생성 사전을 파괴하지 않습니다 — 이는 대규모 모델 기반 미세 조정이 붕괴되지 않게 하는 핵심 설계입니다.
3. **2단계 증류 커리큘럼**: 먼저 인과적 흐름 매칭 워밍업으로 양방향과 인과적 처리의 구조적 격차를 메운 다음, DMD 4단계 증류로 교사의 손-물체 상호작용 사전을 계승하면서 40fps 실시간성을 유지합니다. 이는 "실시간"과 "고충실도"의 모순을 해결합니다.

## 실험 및 결과

### 정량적 결과 (Table 4, EgoDex-Test 도메인)
| 방법 | PSNR | SSIM | LPIPS | FVD | FPS |
|---|---|---|---|---|---|
| RynnWorld-Teleop (SFT) | 26.78 | 0.887 | 0.119 | 550 | 2.8 |
| RynnWorld-Teleop (LoRA) | 26.08 | 0.876 | 0.151 | 585 | 2.8 |
| RynnWorld-Teleop-Causal | 22.25 | 0.830 | 0.207 | 1226 | 40.0 |
| Wan-2.2-TI2V-5B (SFT) | 20.93 | 0.806 | 0.282 | 1223 | 2.8 |
| InterDyn | 21.47 | 0.831 | 0.279 | 655 | 2.9 |
| CosHand | 18.14 | 0.785 | 0.406 | 1527 | 0.8 |
| Mask2IV | 21.50 | 0.836 | 0.219 | 1650 | 0.9 |

### 절제 연구 (LoRA)
| 변형 | PSNR | SSIM | LPIPS | FVD | FPS |
|---|---|---|---|---|---|
| 연결 융합 | 19.69 | 0.821 | 0.260 | 1191 | 2.8 |
| 인간 사전 훈련 없음 | 17.81 | 0.763 | 0.453 | 2598 | 2.8 |
| DMD 없음 (인과적) | 19.25 | 0.777 | 0.244 | 1338 | 40.0 |
| 인과적 워밍업 없음 (인과적) | 14.26 | 0.688 | 0.408 | 2150 | 40.0 |

### 실제 세계 정책 성능 (Table 3, 성공률 %)
| 구성 | 이중 집기 | 블록 밀기 | 양손 들기 | 뚜껑 배치 |
|---|---|---|---|---|
| π_0.5 (300 실제) | 94.29 | 100.00 | 94.29 | 42.86 |
| π_0.5 (300 실제 + 300 생성) | 97.14 | 97.14 | 100.00 | 62.86 |
| π_0 (300 실제) | 88.57 | 94.29 | 91.43 | 34.29 |
| π_0 (0 실제 + 300 생성) | 68.57 | 82.86 | 77.14 | 28.57 |
| π_0 (300 실제 + 300 생성) | 94.29 | 100.00 | 97.14 | 54.29 |

뚜껑 배치 작업에서 π_0.5 성공률은 42.86%에서 62.86%(+20%)로, π_0는 34.29%에서 54.29%(+20%)로 향상되었습니다. π_0는 300개의 생성 클립만으로 훈련하여 블록 밀기 82.86%, 양손 들기 77.14%를 달성했습니다. 지연 분석: 단일 H100에서 4단계 흐름 매칭 스케줄, 480×832 해상도에서 처리량 40.0fps, 평균 프레임당 지연 약 25ms, 골격 동작 인코딩 약 5%, 인과적 DiT 노이즈 제거 약 72%, 시각 디코딩 약 23%로 분해됩니다.

## 경계 및 한계

저자는 논문 발췌문에서 한계 섹션을 명시적으로 나열하지 않았습니다. 방법 세부 사항에서 깊이 변조 렌더링이 3D 공간 역학을 포착하지만, 모델은 때때로 세밀한 유체 역학이나 고도로 변형 가능한 물체 조작을 처리하는 데 어려움을 겪습니다. 구현 간 격차 해소는 현재 플랫폼별 미세 조정이 필요하여 로봇 클러스터에서의 확장성을 제한합니다. 논문은 생성 비디오의 물리적 정확성에 대한 정량적 검증(접촉력, 물체 역학 오류), 장시간(81프레임 블록을 훨씬 초과) 안정성 평가, 다양한 로봇 하드웨어 전이 검증, 작업자 다양성(손 형태, 추적 노이즈)의 영향을 명시적으로 언급하지 않았습니다.

## 엔지니어링 시사점

재현 시 먼저 세 가지를 확인하십시오: 첫째, 기본 모델 Wan2.2-TI2V-5B의 가중치 획득과 TI2V 워밍업 미세 조정의 2,000단계 설정 — 이는 이후 모든 훈련의 전제 조건입니다; 둘째, 깊이 인식 골격 렌더링의 깊이 변조 매개변수 — 이는 동작 접지 정밀도에 직접 영향을 미칩니다; 셋째, 청크 재앵커링의 81프레임 블록 전략 — 이는 장시간 드리프트 방지의 핵심이므로 더 짧은 블록으로 변경하지 마십시오. 가장 함정에 빠지기 쉬운 곳은 분포 정렬 조건 메커니즘입니다 — 연결 융합으로 변경하면 FVD가 550에서 1191로 악화되며(표 내 수치 550→1191 계산), 이는 가산 게이팅 설계가 선택 사항이 아니라 필수 사항임을 의미합니다. 증류 단계에서는 먼저 인과적 흐름 매칭 워밍업을 수행한 다음 DMD를 수행해야 하며, 워밍업을 건너뛰면 FVD가 1226에서 2150으로 악화됩니다(표 내 수치 1226→2150 계산). 하류 팀이 생성 데이터로 정책을 훈련할 때는 먼저 특징 분포 분석(t-SNE 중첩 검증)을 수행한 다음 실제 데이터와 혼합하여 훈련하는 것이 좋습니다. 순수 생성 데이터는 단순 작업(블록 밀기)에서 가능하지만, 복잡한 작업(뚜껑 배치)은 여전히 실제 데이터가 필요합니다.
