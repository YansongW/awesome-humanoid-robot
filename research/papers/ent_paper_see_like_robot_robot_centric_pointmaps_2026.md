---
$id: ent_paper_see_like_robot_robot_centric_pointmaps_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models'
  zh: 'See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models'
  ko: 'See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models'
summary:
  en: Vision-language-action (VLA) models predict robot actions from visual observations and language instructions. These
    actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating
    a frame mismatch between where the scene is observed and where actions are defined. The mismatch is benign under a fixed
    viewpoint, where the policy can memorize.
  zh: 本文提出机器人中心点图（robot-centric pointmaps），将RGB-D观测提升至机器人坐标系并保持H×W像素网格，以最小架构改动集成到预训练VLA中，解决相机坐标系与动作坐标系不匹配导致的跨视角泛化问题。作者在RoboCasa仿真和Franka
    Research 3真实机器人上验证，点图在固定与随机相机视角下均显著提升π0.5与SmolVLA的成功率，尤其对未见相机位姿鲁棒。
  ko: Vision-language-action (VLA) models predict robot actions from visual observations and language instructions. These
    actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating
    a frame mismatch between where the scene is observed and where actions are defined. The mismatch is benign under a fixed
    viewpoint, where the policy can memorize.
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
- see
- like
- robot
- robot
- centric
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
  title: 'arXiv:2607.11498 See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models'
  url: https://arxiv.org/abs/2607.11498
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

本文提出机器人中心点图（robot-centric pointmaps），将RGB-D观测提升至机器人坐标系并保持H×W像素网格，以最小架构改动集成到预训练VLA中，解决相机坐标系与动作坐标系不匹配导致的跨视角泛化问题。作者在RoboCasa仿真和Franka Research 3真实机器人上验证，点图在固定与随机相机视角下均显著提升π0.5与SmolVLA的成功率，尤其对未见相机位姿鲁棒。

## 它改变了什么

VLA模型的动作定义在机器人自身3D坐标系，而视觉观测来自相机坐标系，这一根本性错位在固定视角下可被策略记忆掩盖，但跨数据集聚合不同相机设置时，策略被迫学习视角无关的映射，难度陡增。现有方案各有硬伤：深度图仍绑定相机系，点云虽提供机器人中心几何却破坏预训练2D VLA所需的规则图像网格，且将密集观测降为稀疏点集。本文真正改变的是：在不牺牲预训练视觉编码器输入格式的前提下，将几何信息显式注入机器人坐标系，使VLA无需从数据中隐式学习相机标定与坐标系变换。这一改动将几何先验从“可学习的隐式知识”转为“输入的显式结构”，直接缓解了跨视角分布偏移。

## 方法拆解

### 点图构建流程
1. **相机系提升**：对每个RGB-D观测，按公式 P_c^cam(u,v) = D_c(u,v) K_c^{-1} [u,v,1]^T 将像素提升为3D点。
2. **坐标系变换**：应用相机到机器人变换 P_c^R(u,v) = R_c P_c^cam(u,v) + t_c，将点转换到机器人基座系。
3. **末端执行器居中**：P_c^EE(u,v) = P_c^R(u,v) - t_EE，以当前末端执行器位置为原点重新居中。

### 融合架构
- 使用与RGB编码器f_θ同架构的独立点图编码器g_φ（从f_θ初始化），将点图映射为与RGB token同形状的token。
- 逐元素相加融合：z_c = f_θ(I_c) + g_φ(P_c^EE) ∈ R^{N_tok×d}。

### 关键设计决策
- **预计算几何优于学习**：直接提供机器人系坐标比让策略从深度和标定中隐式学习更有效（表1中RGB+Pointmap 34.7 vs RGB+Plücker+Depth 31.6，差距3.1点）。
- **图像形式优于点云**：保留像素网格使逐元素融合成为可能（加法融合34.7 vs 拼接30.7）。
- **末端执行器居中优于基座居中**：动作是末端执行器的运动，共享原点使观察与动作空间对齐；基座系将等效交互编码为无关几何。
- **加法融合优于拼接**：加法保持空间对应关系，拼接将点图token视为独立序列。

## 关键创新

1. **坐标系对齐的显式化**：以往方法或隐式学习变换，或使用破坏网格结构的点云。点图以像素级3D坐标形式直接给出机器人系几何，既保留预训练VLA的输入格式，又消除坐标系错位，这是首个以最小架构改动实现该对齐的方案。
2. **末端执行器居中的动作空间对齐**：将观测几何以末端执行器为原点表达，使观察与动作空间共享坐标系。这一设计使等效交互（如不同位置抓取）在几何上保持一致，显著提升跨视角泛化（表3中EE居中在随机视角下仅下降0.3点，基座居中下降2.0点）。
3. **零额外token开销的融合**：通过独立编码器加逐元素相加，不增加序列长度，不引入点云专用编码器或体素化模块，对预训练VLA的架构改动极小，便于集成到任意VLA骨干。

## 实验与结果

### 受控研究（RoboCasa，π风格架构）
| 输入 | 成功率 |
|------|--------|
| RGB | 27.9 |
| RGB+Plücker | 28.7 |
| RGB+Plücker+Depth | 31.6 |
| RGB+Pointmap | 34.7 |

### 融合方式消融
| 输入 | 成功率 |
|------|--------|
| RGB+Point cloud（MLP，concat） | 24.2 |
| RGB+Point cloud（PTv3，concat） | 32.8 |
| RGB+Pointmap（concat） | 30.7 |
| RGB+Pointmap（add） | 34.7 |

### 相机随机化鲁棒性（表3）
| 输入 | Fixed | Rand. | Δ |
|------|-------|-------|---|
| RGB | 27.9 | 25.8 | -2.1 |
| RGB+Pointmap（base） | 34.7 | 32.7 | -2.0 |
| RGB+Pointmap（EE） | 36.9 | 36.6 | -0.3 |

### 模拟基准（表4，固定评估视角）
| 方法 | 平均成功率 |
|------|-----------|
| FP3 | 42.8 |
| OC-VLA | 56.3 |
| KYC | 59.1 |
| GeoVLA | 57.1 |
| PointVLA | 57.3 |
| π0.5 | 55.3 |
| π0.5+pointmap | 62.9 |
| SmolVLA | 37.2 |
| SmolVLA+pointmap | 41.4 |

### 真实机器人（Franka Research 3，表5）
| 条件 | DP3 | π0.5 | π0.5+pointmap |
|------|-----|------|---------------|
| Seen | 63.3 | 73.3 | 78.3 |
| Unseen | 48.3 | 55.0 | 66.7 |

点图在Unseen下仅下降11.6点，RGB-only下降18.3点（由表内数值 78.3→66.7 与 73.3→55.0 计算）。结果说明点图的核心价值在于跨视角泛化：在未见相机位姿下提升幅度（+11.7）远大于已见位姿（+5.0），且对随机视角几乎免疫（Δ仅-0.3）。

## 边界与局限

- 未消融点图注入方式与动作专家的关系，也未消融与预训练配方的交互。
- 点云对比仅使用单一采样预算（每相机1024点），更大预算可能缩小差距。
- 点图需要训练和测试时的标定相机内参和外参，限制于标定可用的设置。
- 相机变化结果聚焦于位置和外参变化，未覆盖相机数量或视场角变化。
- 真实机器人点图由RealSense立体深度和手眼标定构建，携带传感器噪声，与仿真精确几何不同；未在真实机器人上评估SmolVLA。

## 工程启示

复现时先核对三点：一是相机标定精度，点图质量直接依赖内外参准确性，真实场景中手眼标定误差会传导至几何表达；二是末端执行器居中逻辑，务必以当前时刻t_EE为原点而非固定原点，否则失去动作空间对齐优势；三是融合方式，加法融合依赖点图编码器与RGB编码器的token空间对齐，初始化g_φ为f_θ的权重是必要前提。最容易踩坑的是点云基线对比——不同采样预算和编码器选择会显著影响结论，本文仅用单一预算，下游对比时需自行扩展。对工程团队，点图是低侵入方案，可在现有VLA上直接替换视觉输入分支，无需改动动作头或训练配方，适合作为跨相机部署的通用增强模块。

## Overview
Vision-language-action (VLA) models predict robot actions from visual observations and language instructions. These actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating a frame mismatch between where the scene is observed and where actions are defined. The mismatch is benign under a fixed viewpoint, where the policy can memorize a single observation-to-action mapping, but grows harder as large-scale datasets aggregate demonstrations across diverse camera setups and the policy must generalize this mapping across viewpoints. We address this mismatch with robot-centric pointmaps, images whose pixels store the 3D coordinates of scene points in the robot frame. Pointmaps provide robot-frame 3D geometry while preserving the dense H x W grid expected by pretrained 2D VLAs, so they integrate into existing VLAs with minimal architectural change. On RoboCasa, pointmaps improve both pi0.5 and SmolVLA and outperform representative camera-viewpoint and 3D-aware baselines. In real-robot experiments, their advantage over an RGB-only policy widens when the camera is moved to a placement unseen during training.

## 参考
- https://arxiv.org/abs/2607.11498

## 개요

본 논문은 로봇 중심점 지도(robot-centric pointmaps)를 제안하여 RGB-D 관측을 로봇 좌표계로 승격시키고 H×W 픽셀 그리드를 유지함으로써, 최소한의 아키텍처 변경으로 사전 훈련된 VLA에 통합하여 카메라 좌표계와 동작 좌표계 간의 불일치로 인한 교차 시점 일반화 문제를 해결합니다. 저자들은 RoboCasa 시뮬레이션과 Franka Research 3 실제 로봇에서 검증했으며, 점 지도는 고정 및 무작위 카메라 시점 모두에서 π0.5와 SmolVLA의 성공률을 유의미하게 향상시켰고, 특히 보지 못한 카메라 포즈에 대해 강건함을 보였습니다.

## 무엇을 바꾸었는가

VLA 모델의 동작은 로봇 자체의 3D 좌표계에 정의되는 반면, 시각적 관측은 카메라 좌표계에서 비롯됩니다. 이러한 근본적인 불일치는 고정 시점에서는 정책 기억으로 가려질 수 있지만, 데이터셋 간에 서로 다른 카메라 설정을 통합할 때 정책은 시점과 무관한 매핑을 학습해야 하므로 난이도가 급격히 증가합니다. 기존 접근법들은 각각 명확한 한계가 있습니다: 깊이 지도는 여전히 카메라 좌표계에 묶여 있고, 점 구름은 로봇 중심 기하를 제공하지만 사전 훈련된 2D VLA에 필요한 규칙적인 이미지 그리드를 파괴하며, 밀집 관측을 희소 점 집합으로 축소합니다. 본 논문이 실제로 바꾸는 것은: 사전 훈련된 시각 인코더의 입력 형식을 희생하지 않으면서 기하 정보를 로봇 좌표계에 명시적으로 주입하여, VLA가 데이터에서 카메라 캘리브레이션과 좌표계 변환을 암시적으로 학습할 필요가 없게 만드는 것입니다. 이 변경은 기하 사전 지식을 "학습 가능한 암시적 지식"에서 "입력의 명시적 구조"로 전환하여 교차 시점 분포 이동을 직접 완화합니다.

## 방법 분해

### 점 지도 구축 과정
1. **카메라 좌표계 승격**: 각 RGB-D 관측에 대해 공식 P_c^cam(u,v) = D_c(u,v) K_c^{-1} [u,v,1]^T 을 사용하여 픽셀을 3D 점으로 승격합니다.
2. **좌표계 변환**: 카메라-로봇 변환 P_c^R(u,v) = R_c P_c^cam(u,v) + t_c 을 적용하여 점을 로봇 베이스 좌표계로 변환합니다.
3. **엔드 이펙터 중심화**: P_c^EE(u,v) = P_c^R(u,v) - t_EE 을 통해 현재 엔드 이펙터 위치를 원점으로 재중심화합니다.

### 융합 아키텍처
- RGB 인코더 f_θ와 동일한 아키텍처를 가진 독립적인 점 지도 인코더 g_φ(f_θ에서 초기화)를 사용하여 점 지도를 RGB 토큰과 동일한 형태의 토큰으로 매핑합니다.
- 요소별 덧셈 융합: z_c = f_θ(I_c) + g_φ(P_c^EE) ∈ R^{N_tok×d}.

### 핵심 설계 결정
- **사전 계산된 기하가 학습보다 우수**: 정책이 깊이와 캘리브레이션에서 암시적으로 학습하는 것보다 로봇 좌표계 좌표를 직접 제공하는 것이 더 효과적입니다(표 1에서 RGB+Pointmap 34.7 vs RGB+Plücker+Depth 31.6, 차이 3.1점).
- **이미지 형태가 점 구름보다 우수**: 픽셀 그리드를 유지하면 요소별 융합이 가능해집니다(덧셈 융합 34.7 vs 연결 30.7).
- **엔드 이펙터 중심화가 베이스 중심화보다 우수**: 동작은 엔드 이펙터의 움직임이므로, 공유 원점은 관측과 동작 공간을 정렬시킵니다; 베이스 좌표계는 동등한 상호작용을 무관한 기하로 인코딩합니다.
- **덧셈 융합이 연결보다 우수**: 덧셈은 공간적 대응 관계를 유지하고, 연결은 점 지도 토큰을 독립적인 시퀀스로 취급합니다.

## 핵심 혁신

1. **좌표계 정렬의 명시화**: 기존 방법은 변환을 암시적으로 학습하거나 그리드 구조를 파괴하는 점 구름을 사용했습니다. 점 지도는 픽셀 수준의 3D 좌표 형태로 로봇 좌표계 기하를 직접 제공하여 사전 훈련된 VLA의 입력 형식을 유지하면서 좌표계 불일치를 제거합니다. 이는 최소한의 아키텍처 변경으로 해당 정렬을 달성한 첫 번째 방법입니다.
2. **엔드 이펙터 중심화를 통한 동작 공간 정렬**: 관측 기하를 엔드 이펙터를 원점으로 표현하여 관측과 동작 공간이 좌표계를 공유하게 합니다. 이 설계는 동등한 상호작용(예: 다른 위치에서의 파지)이 기하적으로 일관되게 유지되도록 하여 교차 시점 일반화를 크게 향상시킵니다(표 3에서 EE 중심화는 무작위 시점에서 0.3점만 하락, 베이스 중심화는 2.0점 하락).
3. **추가 토큰 오버헤드가 없는 융합**: 독립 인코더와 요소별 덧셈을 통해 시퀀스 길이를 늘리지 않고, 점 구름 전용 인코더나 복셀화 모듈을 도입하지 않아 사전 훈련된 VLA에 대한 아키텍처 변경이 최소화되어 모든 VLA 백본에 쉽게 통합할 수 있습니다.

## 실험 및 결과

### 통제 연구(RoboCasa, π 스타일 아키텍처)
| 입력 | 성공률 |
|------|--------|
| RGB | 27.9 |
| RGB+Plücker | 28.7 |
| RGB+Plücker+Depth | 31.6 |
| RGB+Pointmap | 34.7 |

### 융합 방식 소거
| 입력 | 성공률 |
|------|--------|
| RGB+Point cloud(MLP, concat) | 24.2 |
| RGB+Point cloud(PTv3, concat) | 32.8 |
| RGB+Pointmap(concat) | 30.7 |
| RGB+Pointmap(add) | 34.7 |

### 카메라 무작위화 강건성(표 3)
| 입력 | Fixed | Rand. | Δ |
|------|-------|-------|---|
| RGB | 27.9 | 25.8 | -2.1 |
| RGB+Pointmap(base) | 34.7 | 32.7 | -2.0 |
| RGB+Pointmap(EE) | 36.9 | 36.6 | -0.3 |

### 시뮬레이션 벤치마크(표 4, 고정 평가 시점)
| 방법 | 평균 성공률 |
|------|-----------|
| FP3 | 42.8 |
| OC-VLA | 56.3 |
| KYC | 59.1 |
| GeoVLA | 57.1 |
| PointVLA | 57.3 |
| π0.5 | 55.3 |
| π0.5+pointmap | 62.9 |
| SmolVLA | 37.2 |
| SmolVLA+pointmap | 41.4 |

### 실제 로봇(Franka Research 3, 표 5)
| 조건 | DP3 | π0.5 | π0.5+pointmap |
|------|-----|------|---------------|
| Seen | 63.3 | 73.3 | 78.3 |
| Unseen | 48.3 | 55.0 | 66.7 |

점 지도는 Unseen에서 11.6점만 하락한 반면, RGB-only는 18.3점 하락했습니다(표 내 값 78.3→66.7 및 73.3→55.0에서 계산). 결과는 점 지도의 핵심 가치가 교차 시점 일반화에 있음을 보여줍니다: 보지 못한 카메라 포즈에서의 향상 폭(+11.7)이 이미 본 포즈(+5.0)보다 훨씬 크며, 무작위 시점에 거의 면역입니다(Δ -0.3).

## 경계 및 한계

- 점 지도 주입 방식과 동작 전문가의 관계, 사전 훈련 레시피와의 상호작용은 소거하지 않았습니다.
- 점 구름 비교는 단일 샘플링 예산(카메라당 1024점)만 사용했으며, 더 큰 예산은 격차를 줄일 수 있습니다.
- 점 지도는 훈련 및 테스트 시 캘리브레이션된 카메라 내부 및 외부 파라미터가 필요하므로, 캘리브레이션이 가능한 설정으로 제한됩니다.
- 카메라 변화 결과는 위치 및 외부 파라미터 변화에 초점을 맞추었으며, 카메라 수나 시야각 변화는 다루지 않았습니다.
- 실제 로봇 점 지도는 RealSense 스테레오 깊이와 손-눈 캘리브레이션으로 구축되어 센서 노이즈를 포함하며, 시뮬레이션의 정확한 기하와 다릅니다; 실제 로봇에서 SmolVLA는 평가하지 않았습니다.

## 공학적 시사점

재현 시 세 가지를 먼저 확인해야 합니다: 첫째, 카메라 캘리브레이션 정밀도 — 점 지도 품질은 내부/외부 파라미터 정확도에 직접 의존하며, 실제 환경에서 손-눈 캘리브레이션 오차는 기하 표현으로 전파됩니다; 둘째, 엔드 이펙터 중심화 로직 — 반드시 현재 시점의 t_EE를 원점으로 사용해야 하며 고정 원점을 사용하면 동작 공간 정렬 이점을 잃습니다; 셋째, 융합 방식 — 덧셈 융합은 점 지도 인코더와 RGB 인코더의 토큰 공간 정렬에 의존하므로, g_φ를 f_θ의 가중치로 초기화하는 것이 필수 전제 조건입니다. 가장 함정에 빠지기 쉬운 부분은 점 구름 베이스라인 비교입니다 — 서로 다른 샘플링 예산과 인코더 선택이 결론에 큰 영향을 미치며, 본 논문은 단일 예산만 사용했으므로 하류 비교 시 자체적으로 확장해야 합니다. 공학 팀에게 점 지도는 낮은 침습성 솔루션으로, 기존 VLA에서 시각 입력 분기를 직접 교체할 수 있으며 동작 헤드나 훈련 레시피를 변경할 필요가 없어, 교차 카메라 배포를 위한 범용 강화 모듈로 적합합니다.
