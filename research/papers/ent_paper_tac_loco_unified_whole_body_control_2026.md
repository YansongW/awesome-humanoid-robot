---
$id: ent_paper_tac_loco_unified_whole_body_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation'
  zh: 'TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation'
  ko: 'TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation'
summary:
  en: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction
    with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation,
    its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback commonly grasp
    firmly rather than.
  zh: TAC-LOCO 是首个将触觉阵列观测引入四足机器人全身动态移动操作（loco-manipulation）的统一强化学习框架，由学术团队基于 Unitree Go2 + Interbotix WidowX 250 平台实现。其核心贡献在于将
    768 维触觉信号编码为 32 维潜表征，与本体感觉联合驱动单一策略同时控制腿、臂与夹爪，在仿真与零样本硬件实验中实现 90% 动态操作成功率，并将平均抓取力降低 47%。
  ko: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction
    with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation,
    its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback commonly grasp
    firmly rather than.
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
- tac
- loco
- unified
- whole
- body
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.10132 TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manip'
  url: https://arxiv.org/abs/2607.10132
  date: '2026-07-11'
  accessed_at: '2026-08-05'
---

## 概述

TAC-LOCO 是首个将触觉阵列观测引入四足机器人全身动态移动操作（loco-manipulation）的统一强化学习框架，由学术团队基于 Unitree Go2 + Interbotix WidowX 250 平台实现。其核心贡献在于将 768 维触觉信号编码为 32 维潜表征，与本体感觉联合驱动单一策略同时控制腿、臂与夹爪，在仿真与零样本硬件实验中实现 90% 动态操作成功率，并将平均抓取力降低 47%。

## 它改变了什么

现有腿式移动操作方法存在一个根本性盲区：它们要么依赖视觉或本体感觉隐式估计外部力，要么手动预设夹爪状态，导致对物体滑移反应迟缓，在未知时变外力下难以维持稳定抓取。TAC-LOCO 改变了这一范式——它不再将触觉视为可选的辅助信号，而是将其作为与本体感觉同等重要的核心观测模态，直接编码进策略的潜空间。这意味着抓取不再是一个开环预设的动作，而是一个由触觉反馈实时调节的闭环控制量。

更关键的是，这项工作打破了"移动"与"操作"在策略架构上的割裂。以往方法通常将 locomotion 和 manipulation 视为两个独立模块或简单拼接，而 TAC-LOCO 通过共享骨干网络加分离动作头、配合优势混合机制，让腿部运动与手臂抓取在训练中动态耦合。这改变了"先站稳再抓取"的时序假设，使机器人能够在行走过程中同时调整步态与抓取力，真正实现全身协同的动态操作。

## 方法拆解

### 触觉信号仿真与编码
- 每个 FlexiTac 传感器为 12×32 taxel 网格，taxel 间距 2 mm，接触面积 25×66 mm²
- 法向力采用 Kelvin–Voigt 模型：`f_{n,i} = -(k_n * d_i + k_d * ḋ_i)`，其中 `k_n = 1.0`，`k_d = 3×10⁻³`
- 两指触觉观测展平拼接为 768 维向量，经共享 MLP（128 隐层，ELU 激活）编码为 32 维潜变量
- 编码器参数与 actor–critic 网络在 PPO 训练中联合优化

### 策略架构
- 单一 MLP 策略，共享骨干 `[256]`，分支为 locomotion 头 `[256, 128]` 和 manipulation 头 `[256, 128]`
- 观测拼接：63 维本体感觉 + 5 维用户命令 + 32 维触觉潜变量 + 96 维历史编码
- 训练时使用特权信息（物体相对位置/速度、内部接触力等），部署时仅用本体感觉 + 触觉

### 优势混合训练
目标函数：
`J(θ_π) = (1/|D|) Σ_{(s_t,a_t)∈D} [log π(a_t^arm|s_t)(A^manip + β A^loco) + log π(a_t^leg|s_t)(β A^manip + A^loco)]`
- β 从 0 线性增至 1，跨越 9000 步，实现从独立优化到联合优化的平滑过渡

### 奖励设计
- 操作奖励：抓取保持（权重 5.0）、滑落惩罚（-0.3）、力调节（-0.005）、EE 位置指数（1.5）/L1（1.0）
- 运动奖励：基座线速度（1.5）、偏航率（1.5）、垂直速度惩罚（-2.5）、脚部离地时间（0.4）、基座高度（-5.0）等

### 仿真到真实迁移
- 触觉信号归一化：`F̃_ij = F_ij/F_max`（当 F_max ≥ τ_F），否则 `F̃_ij = F_ij/F_ref`，裁剪至 [0,1]
- 域随机化：弹性体柔顺接触刚度 `[5, 100]`，碰撞偏移穿透允许量 `[1, 3] mm`
- 触觉仿真频率 100 Hz，匹配真实硬件采样率

## 关键创新

1. **触觉作为全身控制的一等公民**：以往触觉传感仅用于固定基座机械臂操作，TAC-LOCO 首次将其引入四足动态移动操作，且不是简单拼接原始信号，而是通过联合训练的编码器提取紧凑潜表征，使策略能在线推断抓取状态并实时调节夹爪宽度。

2. **优势混合机制**：受 Deep WBC 启发但做了关键改进——β 从 0 线性增至 1，让 locomotion 和 manipulation 动作头先独立优化再逐渐耦合。这避免了早期训练中两个任务互相干扰，同时保证最终策略是统一的全身控制器，而非两个独立策略的简单叠加。

3. **触觉域随机化策略**：不校准逐 taxel 力-响应曲线，而是对弹性体刚度和碰撞偏移做随机化，配合归一化触觉信号，实现了零样本 sim-to-real 迁移。这一设计决策绕开了触觉传感器标定的老大难问题，使硬件部署成为可能。

## 实验与结果

### 仿真实验（8000 随机化 rollout）
| 配置 | 成功率/保留率 |
|---|---|
| 无触觉基线（仅本体感觉） | 46.4% 完成轨迹 |
| TAC-LOCO（触觉信息） | 99.9% 时间保持物体 |

### 消融实验（Tab. 2）
| 配置 | 平均抓取力 (N) | 夹爪宽度 (mm) |
|---|---|---|
| TAC-LOCO 完整奖励 | 13.11 | 24.65 |
| 无力调节奖励 | 24.76 | 22.20 |
| 无保留/滑移奖励 | 25.74 | 21.62 |

完整奖励设计仅用 53% 的平均抓取力即保持相当的物体保留性能，验证了力调节奖励的有效性。

### 硬件实验（Tab. 3, 4）
| 任务/配置 | 成功率 |
|---|---|
| 大末端执行器运动 | 1.0 |
| 动态操作 | 0.9 |
| Deep WBC [4] 基线 | 0.5 |
| TAC-LOCO | 0.9 |

硬件扰动鲁棒性测试中，手动施加最大 5.6 N 随机扰动力，机器人仍成功完成任务。摘要提及抓取力减少 47%，物体掉落率低于 1%。

## 边界与局限

论文未明确讨论整体局限，但可从方法细节推断边界。首先，任务定义排除了物体搜索、导航、抓取选择与到达-抓取，仅处理"已抓取物体后的控制"，这显著缩小了问题范围。其次，仿真器无法完美复现真实夹爪与触觉阵列的变形，归一化触觉读数虽能推断接触状态相对变化，但无法强制执行精确的绝对抓取力阈值——这意味着策略对极端抓取力场景可能不鲁棒。第三，硬件使用伺服控制臂，其执行器动力学难以精确辨识，部署结果可能未完全反映方法潜力；作者预期可反驱动力控臂能实现更强动态性能。最后，硬件实验中夹爪宽度调整比仿真更大，可能源于指尖柔顺性和材料属性差异，说明 sim-to-real 在触觉模态上仍有未建模偏差。

## 工程启示

复现 TAC-LOCO 时，最优先核对的是触觉仿真参数：Kelvin–Voigt 模型的 `k_n = 1.0` 与 `k_d = 3×10⁻³` 必须严格遵循 TacSL 设置，同时 PhysX 的碰撞偏移和弹性体柔顺接触刚度直接影响 taxel 穿透深度，这两个参数是触觉信号质量的关键。域随机化范围（刚度 `[5, 100]`、穿透 `[1, 3] mm`）不可随意缩小，否则 sim-to-real 迁移会失败。

最容易踩坑的地方是优势混合的 β 调度——9000 步的线性增长看似简单，但若过早增大 β，locomotion 和 manipulation 会互相干扰导致训练不稳定；若过晚，则两个动作头可能收敛到局部最优而无法有效耦合。建议严格按论文设置，并监控两个优势函数的量级差异。

另一个工程陷阱是触觉归一化：必须在每个仿真帧独立归一化，且 `τ_F` 阈值的选择直接影响信号分辨率。硬件部署时，确认触觉传感器采样率确实为 100 Hz，否则策略输入频率不匹配会导致性能骤降。最后，由于真实手臂伺服扭矩和带宽有限，建议先复现论文的"轨迹子集"策略，而非直接部署完整轨迹，以保障硬件安全。

## Overview
Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation, its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback commonly grasp firmly rather than regulate the grasp according to the interaction. We propose TAC-LOCO, a tactile-augmented unified reinforcement learning framework that encodes tactile array observations from compliant grippers into a compact latent representation and joins it with proprioception for unified control of the legs, arm, and gripper. With effective grasp stability reward design, the policy learns to simultaneously track body velocity and end-effector trajectories, moderate grasp force, and prevent object slip under both gradual load changes and sudden release events. We deploy the policy zero-shot on a Unitree Go2 with an Interbotix WidowX 250 arm and tactile gripper, demonstrating dynamic tactile-informed loco-manipulation under varying external interactions, achieving a 47% reduction in grasping force and an object drop rate of less than 1%.

## 参考
- https://arxiv.org/abs/2607.10132

## 개요

TAC-LOCO는 촉각 어레이 관측을 사족 로봇의 전신 동적 이동 조작(loco-manipulation)에 도입한 최초의 통합 강화 학습 프레임워크로, 학술 팀이 Unitree Go2 + Interbotix WidowX 250 플랫폼을 기반으로 구현했습니다. 핵심 기여는 768차원 촉각 신호를 32차원 잠재 표현으로 인코딩하고, 고유수용감각과 결합하여 단일 정책이 다리, 팔, 그리퍼를 동시에 제어하도록 하는 것입니다. 시뮬레이션 및 제로샷 하드웨어 실험에서 90%의 동적 조작 성공률을 달성하고 평균 파지력을 47% 감소시켰습니다.

## 무엇을 바꾸었는가

기존 보행형 이동 조작 방법에는 근본적인 사각지대가 있습니다: 외력을 시각 또는 고유수용감각으로 암시적으로 추정하거나, 그리퍼 상태를 수동으로 사전 설정하여 물체 미끄러짐에 대한 반응이 느리고, 알 수 없는 시변 외력 하에서 안정적인 파지를 유지하기 어렵습니다. TAC-LOCO는 이 패러다임을 바꿉니다——촉각을 선택적 보조 신호가 아닌 고유수용감각과 동등하게 중요한 핵심 관측 양식으로 취급하여 정책의 잠재 공간에 직접 인코딩합니다. 이는 파지가 더 이상 개루프 사전 설정 동작이 아니라 촉각 피드백에 의해 실시간으로 조정되는 폐루프 제어량임을 의미합니다.

더 중요하게, 이 작업은 정책 아키텍처에서 "이동"과 "조작"의 분리를 깨뜨렸습니다. 기존 방법은 일반적으로 locomotion과 manipulation을 독립 모듈 또는 단순 연결로 취급했지만, TAC-LOCO는 공유 백본 네트워크와 분리된 액션 헤드, 그리고 어드밴티지 혼합 메커니즘을 통해 다리 운동과 팔 파지가 훈련 중 동적으로 결합되도록 합니다. 이는 "먼저 안정화한 다음 파지"라는 시간적 가정을 바꾸어 로봇이 보행 중에 보폭과 파지력을 동시에 조정할 수 있게 하여 진정한 전신 협조 동적 조작을 실현합니다.

## 방법 분해

### 촉각 신호 시뮬레이션 및 인코딩
- 각 FlexiTac 센서는 12×32 taxel 그리드, taxel 간격 2 mm, 접촉 면적 25×66 mm²
- 법선력은 Kelvin–Voigt 모델 사용: `f_{n,i} = -(k_n * d_i + k_d * ḋ_i)`, 여기서 `k_n = 1.0`, `k_d = 3×10⁻³`
- 두 손가락 촉각 관측을 펼쳐 연결하여 768차원 벡터로 만들고, 공유 MLP(128 은닉층, ELU 활성화)를 통해 32차원 잠재 변수로 인코딩
- 인코더 파라미터는 actor–critic 네트워크와 함께 PPO 훈련에서 공동 최적화

### 정책 아키텍처
- 단일 MLP 정책, 공유 백본 `[256]`, locomotion 헤드 `[256, 128]`와 manipulation 헤드 `[256, 128]`로 분기
- 관측 연결: 63차원 고유수용감각 + 5차원 사용자 명령 + 32차원 촉각 잠재 변수 + 96차원 히스토리 인코딩
- 훈련 시 특권 정보(물체 상대 위치/속도, 내부 접촉력 등) 사용, 배포 시 고유수용감각 + 촉각만 사용

### 어드밴티지 혼합 훈련
목적 함수:
`J(θ_π) = (1/|D|) Σ_{(s_t,a_t)∈D} [log π(a_t^arm|s_t)(A^manip + β A^loco) + log π(a_t^leg|s_t)(β A^manip + A^loco)]`
- β는 0에서 1로 선형 증가하며 9000스텝에 걸쳐 독립 최적화에서 공동 최적화로의 부드러운 전환 구현

### 보상 설계
- 조작 보상: 파지 유지(가중치 5.0), 미끄러짐 패널티(-0.3), 힘 조절(-0.005), EE 위치 지수(1.5)/L1(1.0)
- 운동 보상: 베이스 선속도(1.5), 요 레이트(1.5), 수직 속도 패널티(-2.5), 발 이탈 시간(0.4), 베이스 높이(-5.0) 등

### 시뮬레이션에서 실제로의 전이
- 촉각 신호 정규화: `F̃_ij = F_ij/F_max` (F_max ≥ τ_F일 때), 그렇지 않으면 `F̃_ij = F_ij/F_ref`, [0,1]로 클리핑
- 도메인 무작위화: 탄성체 컴플라이언트 접촉 강성 `[5, 100]`, 충돌 오프셋 침투 허용량 `[1, 3] mm`
- 촉각 시뮬레이션 주파수 100 Hz, 실제 하드웨어 샘플링 레이트와 일치

## 핵심 혁신

1. **촉각을 전신 제어의 일급 시민으로**: 기존 촉각 센싱은 고정 베이스 로봇 팔 조작에만 사용되었지만, TAC-LOCO는 이를 사족 동적 이동 조작에 처음 도입했으며, 단순히 원시 신호를 연결하는 것이 아니라 공동 훈련된 인코더로 컴팩트한 잠재 표현을 추출하여 정책이 온라인으로 파지 상태를 추론하고 실시간으로 그리퍼 폭을 조정할 수 있게 합니다.

2. **어드밴티지 혼합 메커니즘**: Deep WBC에서 영감을 받았지만 핵심 개선이 있습니다——β가 0에서 1로 선형 증가하여 locomotion과 manipulation 액션 헤드가 먼저 독립적으로 최적화된 후 점진적으로 결합됩니다. 이는 초기 훈련에서 두 작업이 서로 간섭하는 것을 방지하면서, 최종 정책이 두 독립 정책의 단순 중첩이 아닌 통합된 전신 컨트롤러임을 보장합니다.

3. **촉각 도메인 무작위화 전략**: taxel별 힘-응답 곡선을 보정하지 않고 탄성체 강성과 충돌 오프셋을 무작위화하고 정규화된 촉각 신호와 결합하여 제로샷 sim-to-real 전이를 구현했습니다. 이 설계 결정은 촉각 센서 보정의 오래된 문제를 우회하여 하드웨어 배포를 가능하게 합니다.

## 실험 및 결과

### 시뮬레이션 실험(8000 무작위화 rollout)
| 구성 | 성공률/유지율 |
|---|---|
| 무촉각 베이스라인(고유수용감각만) | 46.4% 궤적 완료 |
| TAC-LOCO(촉각 정보) | 99.9% 시간 물체 유지 |

### 소거 실험(Tab. 2)
| 구성 | 평균 파지력 (N) | 그리퍼 폭 (mm) |
|---|---|---|
| TAC-LOCO 전체 보상 | 13.11 | 24.65 |
| 힘 조절 보상 없음 | 24.76 | 22.20 |
| 유지/미끄러짐 보상 없음 | 25.74 | 21.62 |

전체 보상 설계는 평균 파지력의 53%만으로 동등한 물체 유지 성능을 유지하여 힘 조절 보상의 효과를 검증했습니다.

### 하드웨어 실험(Tab. 3, 4)
| 작업/구성 | 성공률 |
|---|---|
| 큰 엔드 이펙터 운동 | 1.0 |
| 동적 조작 | 0.9 |
| Deep WBC [4] 베이스라인 | 0.5 |
| TAC-LOCO | 0.9 |

하드웨어 교란 강건성 테스트에서 최대 5.6 N의 무작위 교란력을 수동으로 가했음에도 로봇이 성공적으로 작업을 완료했습니다. 요약에서 파지력 47% 감소, 물체 낙하율 1% 미만을 언급했습니다.

## 경계 및 한계

논문은 전체적인 한계를 명시적으로 논의하지 않았지만, 방법 세부 사항에서 경계를 추론할 수 있습니다. 첫째, 작업 정의는 물체 탐색, 내비게이션, 파지 선택 및 도달-파지를 제외하고 "이미 파지된 물체의 제어"만 처리하므로 문제 범위가 크게 축소됩니다. 둘째, 시뮬레이터는 실제 그리퍼와 촉각 어레이의 변형을 완벽하게 재현할 수 없으며, 정규화된 촉각 판독값은 접촉 상태의 상대적 변화를 추론할 수 있지만 정확한 절대 파지력 임계값을 강제할 수 없습니다——이는 정책이 극단적인 파지력 시나리오에 강건하지 않을 수 있음을 의미합니다. 셋째, 하드웨어는 서보 제어 암을 사용하며, 그 액추에이터 동역학은 정확히 식별하기 어려워 배포 결과가 방법의 잠재력을 완전히 반영하지 못할 수 있습니다; 저자는 역구동 가능한 힘 제어 암이 더 강력한 동적 성능을 구현할 수 있을 것으로 기대합니다. 마지막으로, 하드웨어 실험에서 그리퍼 폭 조정이 시뮬레이션보다 더 큰데, 이는 손끝 컴플라이언스와 재료 특성 차이에서 비롯될 수 있으며, 촉각 양식에서 sim-to-real에 여전히 모델링되지 않은 편향이 있음을 시사합니다.

## 공학적 시사점

TAC-LOCO를 재현할 때 가장 우선적으로 확인해야 할 것은 촉각 시뮬레이션 파라미터입니다: Kelvin–Voigt 모델의 `k_n = 1.0`과 `k_d = 3×10⁻³`은 TacSL 설정을 엄격히 따라야 하며, PhysX의 충돌 오프셋과 탄성체 컴플라이언트 접촉 강성은 taxel 침투 깊이에 직접 영향을 미치므로 이 두 파라미터가 촉각 신호 품질의 핵심입니다. 도메인 무작위화 범위(강성 `[5, 100]`, 침투 `[1, 3] mm`)를 임의로 줄이면 sim-to-real 전이가 실패할 수 있습니다.

가장 함정에 빠지기 쉬운 부분은 어드밴티지 혼합의 β 스케줄입니다——9000스텝의 선형 증가는 단순해 보이지만, β를 너무 일찍 증가시키면 locomotion과 manipulation이 서로 간섭하여 훈련이 불안정해질 수 있고, 너무 늦으면 두 액션 헤드가 로컬 최적에 수렴하여 효과적으로 결합되지 못할 수 있습니다. 논문 설정을 엄격히 따르고 두 어드밴티지 함수의 크기 차이를 모니터링하는 것이 좋습니다.

또 다른 공학적 함정은 촉각 정규화입니다: 각 시뮬레이션 프레임에서 독립적으로 정규화해야 하며, `τ_F` 임계값 선택이 신호 해상도에 직접 영향을 미칩니다. 하드웨어 배포 시 촉각 센서 샘플링 레이트가 실제로 100 Hz인지 확인해야 합니다. 그렇지 않으면 정책 입력 주파수 불일치로 성능이 급격히 저하됩니다. 마지막으로, 실제 암의 서보 토크와 대역폭이 제한적이므로 전체 궤적을 직접 배포하기보다 논문의 "궤적 부분집합" 전략을 먼저 재현하여 하드웨어 안전을 보장하는 것이 좋습니다.
