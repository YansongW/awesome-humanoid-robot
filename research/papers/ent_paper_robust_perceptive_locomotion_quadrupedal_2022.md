---
$id: ent_paper_robust_perceptive_locomotion_quadrupedal_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning robust perceptive locomotion for quadrupedal robots in the wild
  zh: Learning robust perceptive locomotion for quadrupedal robots in the wild
  ko: Learning robust perceptive locomotion for quadrupedal robots in the wild
summary:
  en: 'Legged robots that can operate autonomously in remote and hazardous environments will greatly increase opportunities
    for exploration into under-explored areas. Exteroceptive perception is crucial for fast and energy-efficient locomotion:
    perceiving the terrain before making contact with it enables planning and adaptation of the gait ahead of time to maintain
    speed and stability. However,.'
  zh: 本文提出一套三阶段训练框架（教师-学生-零样本部署），让四足机器人 ANYmal-C 在野外环境中端到端融合外部感知与本体感觉，核心创新是带注意力门控的循环信念编码器。该控制器在阿尔卑斯山 2.2 km 徒步、DARPA 地下挑战赛等真实场景中实现零失败，并在台阶、障碍赛道等实验中显著超越纯本体感觉基线。
  ko: 'Legged robots that can operate autonomously in remote and hazardous environments will greatly increase opportunities
    for exploration into under-explored areas. Exteroceptive perception is crucial for fast and energy-efficient locomotion:
    perceiving the terrain before making contact with it enables planning and adaptation of the gait ahead of time to maintain
    speed and stability. However,.'
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
- robust
- perceptive
- locomotion
- quadrupedal
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P012. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: arXiv:2201.08117 Learning robust perceptive locomotion for quadrupedal robots in the wild
  url: https://arxiv.org/abs/2201.08117
  date: '2022-01-20'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套三阶段训练框架（教师-学生-零样本部署），让四足机器人 ANYmal-C 在野外环境中端到端融合外部感知与本体感觉，核心创新是带注意力门控的循环信念编码器。该控制器在阿尔卑斯山 2.2 km 徒步、DARPA 地下挑战赛等真实场景中实现零失败，并在台阶、障碍赛道等实验中显著超越纯本体感觉基线。

## 它改变了什么

这项工作的真正改变在于：它打破了“地图质量必须完美”这一隐含假设，将外部感知从“决策依据”降级为“可被质疑的观测信号”。以往方法要么完全依赖外部感知（在雪、反光、遮挡下失效），要么退回纯本体感觉（速度受限，需用脚“摸”地形）。本文通过门控机制让策略自主决定何时信任视觉、何时信任触觉，使机器人能在感知可靠时获得预测优势，在感知失效时无缝退化为触觉驱动，且这一决策过程是端到端学习得到的，而非人工设计的启发式规则。

另一个深层改变是：它将“感知-控制”耦合问题重新定义为部分可观测马尔可夫决策过程（POMDP）下的信念估计问题。通过循环编码器维护对地形和自身状态的“信念”，而非依赖单帧地图，这使得控制器能利用时间一致性来修正错误感知——例如接触后更新地形估计，并在脚离地后保持修正结果。这比单纯堆叠传感器或改进建图算法更接近生物运动控制的本质。

## 方法拆解

### 三阶段训练流程
1. **教师策略**：使用 PPO 在 RaiSim 中训练，访问特权信息（无噪声地形、摩擦系数、接触力等），在随机地形上跟随目标速度。观测包括本体感觉 `o_t^p`、外部感知 `o_t^e`（每脚周围 5 个半径的高度采样）和特权状态 `s_t^p`。
2. **学生策略**：通过行为克隆损失 `L_bc` 和重建损失 `L_re` 蒸馏教师，仅使用现场可获得的观测 `(o_t^p, n(o_t^e))`，其中 `n(·)` 为噪声模型。学生由循环信念编码器 + MLP 组成，可复用教师权重初始化。
3. **零样本部署**：直接部署到物理机器人，无微调。

### 信念编码器（核心组件）
- 输入：本体感觉 `o_t^p`、带噪外部感知特征 `l_t^e = g_e(o_t^e~)`、隐藏状态 `s_t`。
- 中间信念：`b_t' = RNN(o_t^p, l_t^e, s_t)`，使用 2 层 GRU（每层 50 单元）。
- 注意力门控：`α = σ(g_a(b_t'))`，控制外部感知信息流入量。
- 最终信念：`b_t = g_b(b_t') + l_t^e ⊙ α`，维度 120（96 外部 + 24 特权）。
- 解码器使用相同门控重建特权信息和高度采样，计算重建损失。

### 关键设计决策
- **高度图作为中间抽象**：策略接收高度采样点而非原始点云，使模型独立于具体传感器（LiDAR 或立体相机均可，无需重新训练）。
- **楼梯用盒子建模**：高度图建模的楼梯边缘非垂直，策略会利用该伪影导致 sim-to-real 迁移差。
- **噪声模型**：三种条件（名义 60%、大偏移 30%、大噪声 10%）在训练回合开始时随机选择，噪声幅度随课程因子 `c_sk` 线性增加。
- **CPG 启发的动作空间**：每条腿有相位变量 `φ_l`，策略输出相位修改量 `Δφ_l` 和残差关节目标 `Δq_i`，名义轨迹经逆运动学映射为 12 个关节目标。

### 奖励设计
总奖励 `r = 0.75(r_lv + r_av + r_lvo) + r_b + 0.003 r_fc + 0.1 r_co + 0.001 r_j + 0.08 r_jc + 0.003 r_s + 1.0·10⁻⁶ r_τ + 0.003 r_slip`，其中 `r_lv` 和 `r_av` 为分段指数速度跟随奖励，`r_co` 惩罚小腿/膝盖碰撞，`r_slip` 惩罚脚滑移。课程因子 `c_k` 单调递增收敛到 1。

## 关键创新

1. **注意力门控的信念编码器**：这是首次将可学习的门控机制引入腿足机器人感知-控制融合。门控因子 `α` 由中间信念状态计算，允许策略根据上下文动态调整对外部感知的信任度。消融实验（表 S4）显示，门控在大多数地形上降低动作差异（如 rough 地形小噪声下 0.690 vs 0.746），且在大噪声下不牺牲鲁棒性。

2. **噪声模型作为课程的一部分**：将感知噪声参数 `z` 纳入课程学习，随训练线性增加幅度。这迫使策略从“依赖完美感知”逐步过渡到“在噪声下保持鲁棒”，比固定噪声训练更高效。三种噪声条件（60%/30%/10%）模拟了正常、位姿漂移、遮挡/建图失败等真实场景。

3. **零样本 sim-to-real 迁移**：无需真实数据微调，直接部署。这得益于高度图抽象（屏蔽传感器差异）、域随机化（质量、摩擦、外力）和噪声训练（使策略对感知退化不敏感）。野外 2.2 km 徒步和 DARPA 地下挑战赛的零失败记录验证了其泛化能力。

## 实验与结果

### 野外部署
| 场景 | 关键指标 | 结果 |
|---|---|---|
| Etzel 山徒步 | 路线 2.2 km，海拔增益 120 m，最大坡度 38% | 31 分钟登顶（人类 35 分钟），78 分钟全程（规划建议 76 分钟），零失败 |
| DARPA 地下挑战赛 | 隧道/城市/洞穴三种赛道 | 四台 ANYmal 探索超 1700 m，无摔倒 |

### 受控实验（图 4）
| 实验 | 本控制器 | 纯本体感觉基线 |
|---|---|---|
| 台阶高度 | 可靠越过 30.5 cm | 20 cm 时成功率下降 |
| 障碍赛道 | 平滑通过全部障碍 | 三个障碍均卡住 |
| 平地最大速度 | 1.2 m/s | 0.6 m/s |
| 转向速度 | 3 rad/s | 0.6 rad/s（五倍差异） |

### 消融研究（表 S4/S5）
- 门控 vs 无门控：在 10 种地形上，GRU gate 在动作差异和重构误差上均优于 GRU no gate（如 grid steps 小噪声下动作差异 1.444 vs 1.674）。
- 大噪声下门控优势变小（如 rough 大噪声 0.879 vs 0.997），说明门控在大噪声下不牺牲鲁棒性。
- MLP 编码器无法重构特权信息，验证了循环结构对时间一致性建模的必要性。

### 信念状态可视化（图 5）
- 泡沫障碍：初始信任视觉，接触后迅速向下修正地形估计，脚离地后保持修正。
- 透明障碍：如履平地直到接触，接触后向上修正并改变步态。
- 传感器被遮挡：接触楼梯竖板后修正估计并成功爬楼。
- 湿滑平台：检测低摩擦后加快步伐，位姿漂移导致地图不稳定时无缝退回本体感觉。

## 边界与局限

- **狭窄悬崖/踏脚石**：高度图因遮挡信息不足，策略假设连续表面，可能导致踏空坠落（作者明确承认）。
- **高度图表示损失**：作为中间状态会遗漏原始点云中的材质和纹理信息，这些信息可能对某些地形判断有用。
- **位姿估计未联合训练**：高度图构建依赖经典位姿估计模块，未与策略端到端训练，可能成为瓶颈。
- **无法完成非常规机动**：如从狭窄洞中拔出卡住的腿或爬上高台，这些需要与正常行走显著不同的动作。
- **大噪声下门控优势减弱**：消融显示在大噪声条件下门控与无门控性能接近，说明门控主要在中低噪声下发挥作用。
- **论文未明确**：真实机器人上的定量失败率、计算延迟、训练数据量等具体数值。

## 工程启示

- **复现优先核对**：先确认 RaiSim 模拟器版本和 ANYmal-C 执行器模型参数，这是 sim-to-real 迁移的基础。其次核对噪声模型参数 `z` 的三种条件（60%/30%/10%）和课程因子更新公式 `c_{k+1} = c_k^d`（d=0.98）。
- **最容易踩坑**：楼梯地形必须用盒子建模而非高度图，否则策略会利用非垂直边缘导致迁移失败。另外，学生训练前 10 个 epoch 必须用平坦地形，20 个 epoch 后才启用自适应地形课程，否则训练不稳定。
- **门控实现细节**：注意力向量 `α` 由 `g_a(b_t')` 计算，`g_a` 和 `g_b` 均为 {64, 64} 的 MLP。滤波后的外部感知 `l_t^e ⊙ α` 需零填充到 120 维再与 `g_b(b_t')` 相加，维度不匹配是常见错误。
- **下游团队建议**：若更换传感器（如从 LiDAR 换为立体相机），无需重新训练，只需调整高度图构建管线（20 Hz 更新频率）。但需注意高度图查询位置无信息时填充随机采样值，这会影响策略行为。
- **性能预期管理**：在台阶高度超过 32 cm 时控制器会犹豫前进，这是学习到的物理极限判断，不是故障。若需更高越障能力，需调整奖励函数中 `r_co`（碰撞惩罚）权重或增加更高台阶的训练分布。

## Overview
Legged robots that can operate autonomously in remote and hazardous environments will greatly increase opportunities for exploration into under-explored areas. Exteroceptive perception is crucial for fast and energy-efficient locomotion: perceiving the terrain before making contact with it enables planning and adaptation of the gait ahead of time to maintain speed and stability. However, utilizing exteroceptive perception robustly for locomotion has remained a grand challenge in robotics. Snow, vegetation, and water visually appear as obstacles on which the robot cannot step~-- or are missing altogether due to high reflectance. Additionally, depth perception can degrade due to difficult lighting, dust, fog, reflective or transparent surfaces, sensor occlusion, and more. For this reason, the most robust and general solutions to legged locomotion to date rely solely on proprioception. This severely limits locomotion speed, because the robot has to physically feel out the terrain before adapting its gait accordingly. Here we present a robust and general solution to integrating exteroceptive and proprioceptive perception for legged locomotion. We leverage an attention-based recurrent encoder that integrates proprioceptive and exteroceptive input. The encoder is trained end-to-end and learns to seamlessly combine the different perception modalities without resorting to heuristics. The result is a legged locomotion controller with high robustness and speed. The controller was tested in a variety of challenging natural and urban environments over multiple seasons and completed an hour-long hike in the Alps in the time recommended for human hikers.

## 参考
- https://arxiv.org/abs/2201.08117

## 개요

본 논문은 3단계 훈련 프레임워크(교사-학생-제로샷 배포)를 제안하여, 사족 보행 로봇 ANYmal-C가 야외 환경에서 외부 인식과 고유 감각을 종단 간 융합하도록 한다. 핵심 혁신은 주의 게이팅이 적용된 순환 신념 인코더이다. 이 컨트롤러는 알프스 산맥 2.2km 하이킹, DARPA 지하 챌린지 등 실제 시나리오에서 제로 실패를 달성했으며, 계단, 장애물 코스 등의 실험에서 순수 고유 감각 기준선을 크게 능가했다.

## 무엇을 바꾸었는가

이 작업의 진정한 변화는 "지도 품질이 완벽해야 한다"는 암묵적 가정을 깨고, 외부 인식을 "의사 결정 근거"에서 "의심될 수 있는 관측 신호"로 격하시킨 것이다. 기존 방법은 외부 인식에 완전히 의존하거나(눈, 반사, 가림 상태에서 실패), 순수 고유 감각으로 후퇴하거나(속도 제한, 발로 지형을 "더듬어야" 함) 했다. 본 논문은 게이팅 메커니즘을 통해 정책이 언제 시각을 신뢰하고 언제 촉각을 신뢰할지 자율적으로 결정하게 하여, 로봇이 인식이 신뢰할 수 있을 때 예측 이점을 얻고, 인식이 실패할 때 촉각 구동으로 매끄럽게 퇴화하도록 한다. 이 결정 과정은 수동으로 설계된 휴리스틱 규칙이 아닌 종단 간 학습으로 얻어진다.

또 다른 심층적 변화는 "인식-제어" 결합 문제를 부분 관측 마르코프 결정 과정(POMDP) 하의 신념 추정 문제로 재정의한 것이다. 순환 인코더를 통해 단일 프레임 지도에 의존하지 않고 지형과 자신의 상태에 대한 "신념"을 유지함으로써, 컨트롤러가 시간적 일관성을 활용하여 잘못된 인식을 수정할 수 있다—예를 들어 접촉 후 지형 추정을 업데이트하고, 발이 땅에서 떨어진 후에도 수정 결과를 유지한다. 이는 단순히 센서를 쌓거나 매핑 알고리즘을 개선하는 것보다 생물학적 운동 제어의 본질에 더 가깝다.

## 방법 분해

### 3단계 훈련 절차
1. **교사 정책**: PPO를 사용하여 RaiSim에서 훈련하며, 특권 정보(무잡음 지형, 마찰 계수, 접촉력 등)에 접근하고, 무작위 지형에서 목표 속도를 추종한다. 관측에는 고유 감각 `o_t^p`, 외부 인식 `o_t^e`(각 발 주변 5개 반경의 높이 샘플링) 및 특권 상태 `s_t^p`가 포함된다.
2. **학생 정책**: 행동 복제 손실 `L_bc`와 재구성 손실 `L_re`를 통해 교사를 증류하며, 현장에서 얻을 수 있는 관측 `(o_t^p, n(o_t^e))`만 사용한다. 여기서 `n(·)`는 잡음 모델이다. 학생은 순환 신념 인코더 + MLP로 구성되며, 교사 가중치 초기화를 재사용할 수 있다.
3. **제로샷 배포**: 미세 조정 없이 물리 로봇에 직접 배포한다.

### 신념 인코더(핵심 구성 요소)
- 입력: 고유 감각 `o_t^p`, 잡음이 있는 외부 인식 특징 `l_t^e = g_e(o_t^e~)`, 은닉 상태 `s_t`.
- 중간 신념: `b_t' = RNN(o_t^p, l_t^e, s_t)`, 2층 GRU(각 층 50유닛) 사용.
- 주의 게이팅: `α = σ(g_a(b_t'))`, 외부 인식 정보의 유입량을 제어.
- 최종 신념: `b_t = g_b(b_t') + l_t^e ⊙ α`, 차원 120(96 외부 + 24 특권).
- 디코더는 동일한 게이팅을 사용하여 특권 정보와 높이 샘플링을 재구성하고 재구성 손실을 계산한다.

### 핵심 설계 결정
- **높이 맵을 중간 추상화로 사용**: 정책은 원시 포인트 클라우드가 아닌 높이 샘플링 포인트를 수신하므로, 모델이 특정 센서(LiDAR 또는 스테레오 카메라 모두 가능, 재훈련 불필요)와 독립적이다.
- **계단을 박스로 모델링**: 높이 맵으로 모델링된 계단 가장자리는 수직이 아니며, 정책이 이 아티팩트를 활용하여 sim-to-real 전이가 나빠진다.
- **잡음 모델**: 세 가지 조건(명목 60%, 큰 오프셋 30%, 큰 잡음 10%)이 훈련 에피소드 시작 시 무작위로 선택되며, 잡음 크기는 커리큘럼 인자 `c_sk`에 따라 선형적으로 증가한다.
- **CPG 영감 동작 공간**: 각 다리에는 위상 변수 `φ_l`이 있으며, 정책은 위상 수정량 `Δφ_l`과 잔차 관절 목표 `Δq_i`를 출력하고, 명목 궤적은 역기구학을 통해 12개 관절 목표로 매핑된다.

### 보상 설계
총 보상 `r = 0.75(r_lv + r_av + r_lvo) + r_b + 0.003 r_fc + 0.1 r_co + 0.001 r_j + 0.08 r_jc + 0.003 r_s + 1.0·10⁻⁶ r_τ + 0.003 r_slip`, 여기서 `r_lv`와 `r_av`는 구간 지수 속도 추종 보상, `r_co`는 종아리/무릎 충돌을 패널티, `r_slip`은 발 미끄러짐을 패널티한다. 커리큘럼 인자 `c_k`는 단조 증가하여 1로 수렴한다.

## 핵심 혁신

1. **주의 게이팅 신념 인코더**: 학습 가능한 게이팅 메커니즘을 사족 보행 로봇의 인식-제어 융합에 도입한 최초의 사례이다. 게이팅 인자 `α`는 중간 신념 상태에서 계산되며, 정책이 문맥에 따라 외부 인식에 대한 신뢰도를 동적으로 조정할 수 있게 한다. 절제 실험(표 S4)은 게이팅이 대부분의 지형에서 동작 차이를 줄이고(예: rough 지형 작은 잡음에서 0.690 vs 0.746), 큰 잡음에서도 강건성을 희생하지 않음을 보여준다.

2. **커리큘럼의 일부로서의 잡음 모델**: 인식 잡음 매개변수 `z`를 커리큘럼 학습에 포함시켜 훈련 중 선형적으로 크기를 증가시킨다. 이는 정책이 "완벽한 인식 의존"에서 "잡음 하 강건성 유지"로 점진적으로 전이하도록 강제하며, 고정 잡음 훈련보다 효율적이다. 세 가지 잡음 조건(60%/30%/10%)은 정상, 자세 드리프트, 가림/매핑 실패 등 실제 시나리오를 모사한다.

3. **제로샷 sim-to-real 전이**: 실제 데이터 미세 조정 없이 직접 배포한다. 이는 높이 맵 추상화(센서 차이 차폐), 도메인 무작위화(질량, 마찰, 외력), 잡음 훈련(인식 저하에 둔감하게) 덕분이다. 야외 2.2km 하이킹과 DARPA 지하 챌린지의 제로 실패 기록이 일반화 능력을 검증한다.

## 실험 및 결과

### 야외 배포
| 시나리오 | 핵심 지표 | 결과 |
|---|---|---|
| Etzel 산 하이킹 | 경로 2.2km, 고도 상승 120m, 최대 경사 38% | 31분 정상 도달(인간 35분), 78분 전체(계획 권장 76분), 제로 실패 |
| DARPA 지하 챌린지 | 터널/도시/동굴 세 가지 코스 | 4대의 ANYmal이 1700m 이상 탐사, 넘어짐 없음 |

### 통제 실험(그림 4)
| 실험 | 본 컨트롤러 | 순수 고유 감각 기준선 |
|---|---|---|
| 계단 높이 | 30.5cm 안정적으로 넘음 | 20cm에서 성공률 하락 |
| 장애물 코스 | 모든 장애물 매끄럽게 통과 | 세 가지 장애물 모두 걸림 |
| 평지 최대 속도 | 1.2m/s | 0.6m/s |
| 회전 속도 | 3rad/s | 0.6rad/s(5배 차이) |

### 절제 연구(표 S4/S5)
- 게이팅 vs 무게이팅: 10가지 지형에서 GRU gate가 동작 차이와 재구성 오차 모두에서 GRU no gate보다 우수(예: grid steps 작은 잡음에서 동작 차이 1.444 vs 1.674).
- 큰 잡음에서 게이팅 이점 감소(예: rough 큰 잡음 0.879 vs 0.997), 게이팅이 큰 잡음에서 강건성을 희생하지 않음을 시사.
- MLP 인코더는 특권 정보를 재구성할 수 없어, 시간적 일관성 모델링에 순환 구조의 필요성을 검증.

### 신념 상태 시각화(그림 5)
- 폼 장애물: 초기에는 시각을 신뢰, 접촉 후 지형 추정을 빠르게 하향 수정, 발이 땅에서 떨어진 후에도 수정 유지.
- 투명 장애물: 접촉까지 평지처럼 보행, 접촉 후 상향 수정 및 보행 패턴 변경.
- 센서 가림: 계단 수직판 접촉 후 추정 수정 및 계단 오르기 성공.
- 미끄러운 플랫폼: 낮은 마찰 감지 후 보폭 가속, 자세 드리프트로 지도 불안정 시 고유 감각으로 매끄럽게 복귀.

## 경계 및 한계

- **좁은 절벽/디딤돌**: 높이 맵이 가림으로 인해 정보가 부족하여, 정책이 연속 표면을 가정하므로 발을 헛디뎌 추락할 수 있다(저자가 명시적으로 인정).
- **높이 맵 표현 손실**: 중간 상태로 인해 원시 포인트 클라우드의 재질 및 텍스처 정보가 누락되며, 이는 특정 지형 판단에 유용할 수 있다.
- **자세 추정 미공동 훈련**: 높이 맵 구축은 고전적 자세 추정 모듈에 의존하며, 정책과 종단 간 훈련되지 않아 병목이 될 수 있다.
- **비정상 기동 불가**: 좁은 구멍에서 걸린 다리를 빼거나 높은 단상에 오르는 등 정상 보행과 현저히 다른 동작이 필요한 경우 수행 불가.
- **큰 잡음에서 게이팅 이점 감소**: 절제 결과 큰 잡음 조건에서 게이팅과 무게이팅 성능이 유사하여, 게이팅이 주로 중저 잡음에서 효과적임을 시사.
- **논문 미명시**: 실제 로봇에서의 정량적 실패율, 계산 지연, 훈련 데이터 양 등 구체적 수치.

## 공학적 시사점

- **재현 시 우선 확인 사항**: 먼저 RaiSim 시뮬레이터 버전과 ANYmal-C 액추에이터 모델 매개변수를 확인하라. 이는 sim-to-real 전이의 기초이다. 다음으로 잡음 모델 매개변수 `z`의 세 가지 조건(60%/30%/10%)과 커리큘럼 인자 업데이트 공식 `c_{k+1} = c_k^d`(d=0.98)를 확인하라.
- **가장 흔한 함정**: 계단 지형은 높이 맵이 아닌 박스로 모델링해야 한다. 그렇지 않으면 정책이 비수직 가장자리를 활용하여 전이 실패를 초래한다. 또한 학생 훈련 처음 10개 epoch는 평지에서만 수행하고, 20개 epoch 이후에 적응형 지형 커리큘럼을 활성화해야 한다. 그렇지 않으면 훈련이 불안정하다.
- **게이팅 구현 세부 사항**: 주의 벡터 `α`는 `g_a(b_t')`로 계산되며, `g_a`와 `g_b`는 모두 {64, 64} MLP이다. 필터링된 외부 인식 `l_t^e ⊙ α`는 120차원으로 제로 패딩한 후 `g_b(b_t')`와 더해야 한다. 차원 불일치는 흔한 오류이다.
- **하위 팀 권장 사항**: 센서를 교체할 경우(예: LiDAR에서 스테레오 카메라로), 재훈련 없이 높이 맵 구축 파이프라인(20Hz 업데이트 주파수)만 조정하면 된다. 단, 높이 맵 쿼리 위치에 정보가 없을 때 무작위 샘플링 값으로 채우는 것이 정책 동작에 영향을 미친다는 점에 유의하라.
- **성능 기대 관리**: 계단 높이가 32cm를 초과하면 컨트롤러가 전진을 주저하는데, 이는 학습된 물리적 한계 판단이지 고장이 아니다. 더 높은 장애물 극복 능력이 필요하면 보상 함수의 `r_co`(충돌 패널티) 가중치를 조정하거나 더 높은 계단의 훈련 분포를 추가하라.
