---
$id: ent_paper_densereward_dense_reward_failure_synthes_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation'
  zh: 'DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation'
  ko: 'DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation'
summary:
  en: 'Reinforcement learning holds great promise for improving robot policies beyond the limits of imitation learning. However,
    its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and
    informative feedback. Two key challenges remain: acquiring diverse failure data at scale and obtaining fine-grained reward
    signals beyond sparse.'
  zh: DenseReward 提出了一套完整的密集视觉-语言奖励模型训练方案，核心贡献在于通过自动数据生成流水线与目标扰动合成多样化失败轨迹，构建了包含 26579 个操作片段、7560942 个帧级样本的密集奖励数据集，并基于 Qwen3-VL-4B-Instruct
    微调出能输出细粒度任务进度（保留三位小数）的奖励模型。该工作解决了强化学习在机器人操作中缺乏可靠密集奖励信号的核心瓶颈，在密集奖励预测精度、MPC 引导质量以及真实世界策略学习成功率上均显著超越现有基线。
  ko: 'Reinforcement learning holds great promise for improving robot policies beyond the limits of imitation learning. However,
    its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and
    informative feedback. Two key challenges remain: acquiring diverse failure data at scale and obtaining fine-grained reward
    signals beyond sparse.'
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
- densereward
- dense
- reward
- failure
- synthes
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
  title: 'arXiv:2607.13033 DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulatio'
  url: https://arxiv.org/abs/2607.13033
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

DenseReward 提出了一套完整的密集视觉-语言奖励模型训练方案，核心贡献在于通过自动数据生成流水线与目标扰动合成多样化失败轨迹，构建了包含 26579 个操作片段、7560942 个帧级样本的密集奖励数据集，并基于 Qwen3-VL-4B-Instruct 微调出能输出细粒度任务进度（保留三位小数）的奖励模型。该工作解决了强化学习在机器人操作中缺乏可靠密集奖励信号的核心瓶颈，在密集奖励预测精度、MPC 引导质量以及真实世界策略学习成功率上均显著超越现有基线。

## 它改变了什么

这个工作真正改变的是奖励模型训练数据的获取范式。此前领域内要么依赖人工标注（成本极高且难以规模化），要么通过截断成功轨迹或构建偏好对来伪造失败样本——但这些伪失败无法反映真实机器人执行中的物理失败模式，比如碰撞后的动力学响应、抓取偏移导致的物体滑落、运输中的意外掉落等。DenseReward 通过目标扰动主动合成六种明确界定的失败类型，并配合自动有效性检查过滤掉扰动未生效的样本，使得奖励模型第一次能在包含真实失败分布的数据上学习。

另一个关键改变在于奖励信号的粒度。现有方法大多输出稀疏的轨迹级二元标签，策略无法获知中间动作的优劣。DenseReward 将操作分解为 Reach、Grasp、Lift、Move、Place 五个规范相位，为每个时间步赋予 [0,1] 区间的密集奖励值，且保留三位小数以捕捉细微进度差异——这让策略优化能从"最终成败"细化到"每一步推进了多少"，对长时程操作任务尤其重要。

## 方法拆解

### 数据生成流水线
- 场景随机初始化，目标物体与容器随机放置于桌面
- GraspNet 从多视角 RGB-D 预测最多 N=50 个抓取候选
- CuRobo 进行碰撞感知运动规划，筛选可行候选并端到端规划六个固定运动段（对应五个操作相位）
- 相位边界自动检测：Grasp 始于夹爪接触物体，Lift 始于物体离开桌面，Place 始于末端执行器进入目标邻近半径 d_place，全程无需人工标注

### 失败合成与扰动设计
六种轨迹类型对应不同扰动策略：
- Success：无扰动，奖励单调上升
- Collision：禁用碰撞避免，迫使机器人撞击物体或桌面，奖励呈山形曲线
- Miss：偏移抓取目标位姿，夹爪在空中闭合，奖励上升后衰减
- Fall：Move 阶段施加随机旋转扰动，物体运输中掉落，奖励呈山形曲线
- Smooth：每步注入小高斯关节噪声，产生抖动次优轨迹
- Recover：先碰撞后重新规划并完成任务，奖励先降后升

### 有效性检查
在阶段边界应用自动检查，拒绝物理不一致的轨迹（如扰动抓取仍意外抓住物体、掉落轨迹中物体未保持高度阈值等），确保失败标签的可靠性。

### 奖励模型
- 基于 Qwen3-VL-4B-Instruct，LoRA rank 16，训练 10 epoch，8 张 H100，batch size 32
- 输入任务指令、当前观测与历史帧，输出单个三位小数的浮点值（0.000 到 1.000）
- 奖励规则：0.000 表示无进度或失败，1.000 表示完全完成，随阶段推进递增，不可逆失败时下降

### 下游应用
- MPC 评估：每步采样 28 个候选动作（27 个空间方向 + 1 个夹爪开关），d=0.05 m，滚动后用奖励模型评分选最优
- RL 微调：PPO 算法，动作块长度 C=5，组合奖励 r_t = α·r_t^sim + β·r_t^model，α=1.0，β=C/T_max
- 真实世界：DSRL 适配冻结的 π_0 策略，奖励整合 r_t = -1 + r_t^model

## 关键创新

第一，失败合成机制是全新的。不同于 RoboReward 截断成功片段或 Robometer 构建偏好对，DenseReward 通过物理扰动主动制造六种明确界定的失败模式，并配套自动有效性检查确保扰动确实产生了预期失败。这使得奖励模型能学习到真实执行中出现的物理失败特征，而非仅从成功轨迹中推断。

第二，相位感知的密集奖励标注是自动完成的。通过 GraspNet 与 CuRobo 的规划信息自动检测相位边界，无需人工标注，将密集奖励的获取成本从"人工逐帧标注"降为"自动流水线生成"，这是规模化扩展的关键。

第三，三位小数的奖励精度设计看似微小实则重要。它迫使模型学习任务进度的细粒度差异（如更接近目标物体或从失败状态恢复的程度），而非仅输出粗糙的进度等级，这直接提升了奖励信号对策略优化的指导价值。

## 实验与结果

### 密集奖励预测精度（MAE，越低越好）
| 模型 | Overall | DROID | Isaac Sim | RoboSuite | LIBERO |
|---|---|---|---|---|---|
| DenseReward (Ours) | 0.081 | 0.259 | 0.081 | 0.051 | 0.044 |
| Qwen3-VL-4B-Instruct | 0.289 | 0.532 | 0.285 | 0.195 | 0.478 |
| Qwen3-VL-8B-Instruct | 0.293 | 0.538 | 0.305 | 0.180 | 0.502 |
| Molmo2-4B | 0.282 | 0.506 | 0.282 | 0.187 | 0.478 |
| Molmo2-8B | 0.335 | 0.480 | 0.307 | 0.303 | 0.455 |
| RoboReward-4B | 0.275 | 0.534 | 0.269 | 0.179 | 0.470 |
| RoboReward-8B | 0.230 | 0.484 | 0.185 | 0.172 | 0.431 |
| Robometer | 0.366 | 0.521 | 0.328 | 0.345 | 0.468 |

DenseReward 在 Overall 上比最强基线 RoboReward-8B 降低约 65% 误差（由表内数值 0.230→0.081 计算），在 LIBERO 上优势最明显（0.044 vs 0.431）。

### MPC 引导质量（物体与夹爪最小距离，越低越好）
| 模型 | Can | Cup | Lemon | Avg. |
|---|---|---|---|---|
| DenseReward (Ours) | 0.219 | 0.181 | 0.288 | 0.229 |
| RoboReward-4B | 0.199 | 0.307 | 0.295 | 0.267 |
| RoboReward-8B | 0.314 | 0.270 | 0.317 | 0.300 |
| VLAC-2B | 0.316 | 0.346 | 0.380 | 0.347 |
| VLAC-8B | 0.351 | 0.360 | 0.363 | 0.358 |

DenseReward 在 Avg. 上比最强基线 RoboReward-4B 降低约 14%（由表内数值 0.267→0.229 计算），定性结果显示其产生更一致的朝向目标引导。

### 消融与真实世界
- 移除所有失败轨迹后 MAE 从 0.0809 升至 0.1312，验证失败数据有效性
- 历史帧数消融：0 帧 0.096、1 帧 0.088、2 帧 0.081、3 帧 0.086，默认 2 帧最优
- 真实世界：stack the cups 成功率从 40% 提升到 80%，put ball in basket 从 30% 提升到 70%（各评估 10 次试验）

## 边界与局限

MPC 实验未包含旋转动作，因为会大幅增加候选动作数量与计算成本，这意味着奖励模型在需要姿态调整的任务上的引导能力未被验证。有效性过滤步骤依赖人工设计的检查规则，对于未覆盖的失败模式（如工具使用中的复杂失效）可能失效。论文未明确说明 DenseReward 在超出 60 个训练物体类别时的泛化边界，也未涉及人类偏好对齐。真实世界实验仅两个任务且各 10 次试验，统计显著性有限。

## 工程启示

复现时最先核对的是数据生成流水线的有效性检查逻辑——这是整个方法可靠性的基石，扰动本身不总能保证预期失败（如扰动抓取仍可能意外抓住物体），过滤不严会导致误标记数据污染训练。其次确认相位边界检测的触发条件（Grasp 接触、Lift 离桌、Place 进入 d_place 半径），这些阈值直接影响奖励曲线的形状。

最容易踩坑的地方是 MPC 评估中的候选动作空间设计：仅 28 个候选（27 方向 + 1 夹爪）且不含旋转，虽然控制了计算成本，但会限制奖励模型在高自由度任务上的表现评估。下游团队若需复现真实世界结果，注意 DSRL 的冻结 π_0 策略与动作幅度 1.5 的配置，以及奖励整合公式 r_t = -1 + r_t^model 中偏移量对探索行为的影响。训练预算方面，stack the cups 需 20k 步（约 20 个 rollout），put ball in basket 需 10k 步（约 10 个 rollout），硬件为 Franka Research 3 + Robotiq 2F-85 + ZED 相机组合。

## Overview
Reinforcement learning holds great promise for improving robot policies beyond the limits of imitation learning. However, its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and informative feedback. Two key challenges remain: acquiring diverse failure data at scale and obtaining fine-grained reward signals beyond sparse trajectory-level success labels. Collecting failure trajectories typically requires laborious human effort, while pseudo-failures constructed by relabeling successful demonstrations fail to capture the diverse physical failure modes that arise during robot execution. Meanwhile, existing reward models often predict sparse binary or trajectory-level rewards, which provide limited guidance for efficient policy optimization. We introduce DenseReward, a dense robotic reward model that addresses both challenges. To train DenseReward, we develop an automated failure data generation pipeline that synthesizes physically realistic failure trajectories in simulation without human labeling, covering diverse failure modes such as collisions, missed grasps, object drops, and recovery behaviors. DenseReward predicts dense frame-level reward scores from visual observations and language instructions, enabling fine-grained estimation of task progress throughout an episode. Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation. We further demonstrate that DenseReward provides effective reward guidance for downstream model predictive control and reinforcement learning. We release the dataset, trained reward models, and evaluation suite to support the development of failure-aware dense reward modeling for robot learning.

## 参考
- https://arxiv.org/abs/2607.13033

## 개요

DenseReward는 완전한 밀집 비전-언어 보상 모델 훈련 방안을 제시하며, 핵심 기여는 자동 데이터 생성 파이프라인과 목표 교란을 통한 다양한 실패 궤적 합성에 있습니다. 이를 통해 26,579개의 조작 세그먼트와 7,560,942개의 프레임 수준 샘플로 구성된 밀집 보상 데이터셋을 구축하고, Qwen3-VL-4B-Instruct를 기반으로 미세 조정하여 세밀한 작업 진행도(소수점 세 자리 유지)를 출력하는 보상 모델을 개발했습니다. 이 연구는 강화 학습이 로봇 조작에서 신뢰할 수 있는 밀집 보상 신호가 부족하다는 핵심 병목을 해결하며, 밀집 보상 예측 정확도, MPC 유도 품질, 실제 세계 정책 학습 성공률에서 기존 기준선을 크게 능가합니다.

## 무엇을 바꾸었는가

이 연구가 진정으로 바꾼 것은 보상 모델 훈련 데이터 획득 패러다임입니다. 기존에는 수동 주석(비용이 매우 높고 확장이 어려움)에 의존하거나, 성공 궤적을 잘라내거나 선호 쌍을 구성하여 가짜 실패 샘플을 만들었습니다. 그러나 이러한 가짜 실패는 충돌 후 동역학적 반응, 그리핑 오프셋으로 인한 물체 미끄러짐, 운반 중 예상치 못한 낙하 등 실제 로봇 실행에서 발생하는 물리적 실패 패턴을 반영하지 못합니다. DenseReward는 목표 교란을 통해 여섯 가지 명확히 정의된 실패 유형을 능동적으로 합성하고, 자동 유효성 검사를 통해 교란이 효과를 발휘하지 못한 샘플을 걸러냄으로써, 보상 모델이 처음으로 실제 실패 분포를 포함한 데이터에서 학습할 수 있게 했습니다.

또 다른 핵심 변화는 보상 신호의 세분화입니다. 기존 방법은 대부분 희소한 궤적 수준의 이진 레이블을 출력하여 정책이 중간 동작의 우수성을 알 수 없었습니다. DenseReward는 조작을 Reach, Grasp, Lift, Move, Place의 다섯 가지 표준 단계로 분해하고, 각 시간 단계에 [0,1] 구간의 밀집 보상 값을 부여하며, 소수점 세 자리를 유지하여 미세한 진행 차이를 포착합니다. 이는 정책 최적화가 "최종 성공 여부"에서 "각 단계가 얼마나 진행되었는지"로 세분화될 수 있게 하며, 장기 조작 작업에서 특히 중요합니다.

## 방법 분해

### 데이터 생성 파이프라인
- 장면을 무작위로 초기화하고, 목표 물체와 용기를 테이블 위에 무작위로 배치
- GraspNet이 다중 시점 RGB-D에서 최대 N=50개의 그리핑 후보를 예측
- CuRobo가 충돌 인식 운동 계획을 수행하여 실행 가능한 후보를 선별하고, 다섯 가지 조작 단계에 해당하는 여섯 개의 고정 운동 세그먼트를 종단 간 계획
- 단계 경계 자동 감지: Grasp는 그리퍼가 물체에 접촉할 때 시작, Lift는 물체가 테이블을 떠날 때 시작, Place는 엔드 이펙터가 목표 인접 반경 d_place에 진입할 때 시작하며, 수동 주석이 전혀 필요 없음

### 실패 합성 및 교란 설계
여섯 가지 궤적 유형은 서로 다른 교란 전략에 해당:
- Success: 교란 없음, 보상이 단조 증가
- Collision: 충돌 회피를 비활성화하여 로봇이 물체나 테이블에 부딪히도록 강제, 보상이 산 모양 곡선을 그림
- Miss: 그리핑 목표 자세를 오프셋하여 그리퍼가 공중에서 닫히고, 보상이 상승 후 감소
- Fall: Move 단계에서 무작위 회전 교란을 주입하여 물체가 운반 중 떨어지고, 보상이 산 모양 곡선을 그림
- Smooth: 각 단계에 작은 가우시안 관절 노이즈를 주입하여 떨리는 차선 궤적 생성
- Recover: 먼저 충돌한 후 재계획하여 작업을 완료하고, 보상이 먼저 감소 후 증가

### 유효성 검사
단계 경계에서 자동 검사를 적용하여 물리적으로 일관되지 않은 궤적(예: 교란된 그리핑이 여전히 물체를 잡는 경우, 낙하 궤적에서 물체가 높이 임계값을 유지하지 못하는 경우 등)을 거부하여 실패 레이블의 신뢰성을 보장합니다.

### 보상 모델
- Qwen3-VL-4B-Instruct 기반, LoRA rank 16, 10 epoch 훈련, 8대 H100, batch size 32
- 입력은 작업 지시, 현재 관측 및 과거 프레임이며, 출력은 소수점 세 자리의 단일 부동 소수점 값(0.000 ~ 1.000)
- 보상 규칙: 0.000은 진행 없음 또는 실패, 1.000은 완전 완료, 단계 진행에 따라 증가, 되돌릴 수 없는 실패 시 감소

### 하위 응용
- MPC 평가: 각 단계에서 28개의 후보 동작(27개 공간 방향 + 1개 그리퍼 개폐)을 샘플링, d=0.05 m, 롤아웃 후 보상 모델로 점수를 매겨 최적 선택
- RL 미세 조정: PPO 알고리즘, 동작 블록 길이 C=5, 결합 보상 r_t = α·r_t^sim + β·r_t^model, α=1.0, β=C/T_max
- 실제 세계: DSRL이 동결된 π_0 정책에 적응, 보상 통합 r_t = -1 + r_t^model

## 핵심 혁신

첫째, 실패 합성 메커니즘은 완전히 새로운 것입니다. RoboReward가 성공 세그먼트를 잘라내거나 Robometer가 선호 쌍을 구성하는 것과 달리, DenseReward는 물리적 교란을 통해 여섯 가지 명확히 정의된 실패 모드를 능동적으로 생성하고, 자동 유효성 검사를 통해 교란이 실제로 의도된 실패를 발생시켰는지 확인합니다. 이를 통해 보상 모델이 성공 궤적에서만 추론하는 것이 아니라 실제 실행에서 나타나는 물리적 실패 특징을 학습할 수 있습니다.

둘째, 단계 인식 밀집 보상 주석이 자동으로 수행됩니다. GraspNet과 CuRobo의 계획 정보를 통해 단계 경계를 자동 감지하여 수동 주석이 필요 없으며, 밀집 보상 획득 비용을 "프레임별 수동 주석"에서 "자동 파이프라인 생성"으로 낮추는 것이 확장의 핵심입니다.

셋째, 소수점 세 자리의 보상 정밀도 설계는 사소해 보이지만 중요합니다. 이는 모델이 작업 진행의 세밀한 차이(예: 목표 물체에 더 가까워지거나 실패 상태에서 회복되는 정도)를 학습하도록 강제하며, 거친 진행 등급만 출력하는 것보다 보상 신호의 정책 최적화 지도 가치를 직접적으로 향상시킵니다.

## 실험 및 결과

### 밀집 보상 예측 정확도 (MAE, 낮을수록 좋음)
| 모델 | Overall | DROID | Isaac Sim | RoboSuite | LIBERO |
|---|---|---|---|---|---|
| DenseReward (Ours) | 0.081 | 0.259 | 0.081 | 0.051 | 0.044 |
| Qwen3-VL-4B-Instruct | 0.289 | 0.532 | 0.285 | 0.195 | 0.478 |
| Qwen3-VL-8B-Instruct | 0.293 | 0.538 | 0.305 | 0.180 | 0.502 |
| Molmo2-4B | 0.282 | 0.506 | 0.282 | 0.187 | 0.478 |
| Molmo2-8B | 0.335 | 0.480 | 0.307 | 0.303 | 0.455 |
| RoboReward-4B | 0.275 | 0.534 | 0.269 | 0.179 | 0.470 |
| RoboReward-8B | 0.230 | 0.484 | 0.185 | 0.172 | 0.431 |
| Robometer | 0.366 | 0.521 | 0.328 | 0.345 | 0.468 |

DenseReward는 Overall에서 가장 강한 기준선인 RoboReward-8B보다 약 65% 오류를 줄였으며(표 값 0.230→0.081로 계산), LIBERO에서 가장 큰 우위를 보입니다(0.044 vs 0.431).

### MPC 유도 품질 (물체와 그리퍼의 최소 거리, 낮을수록 좋음)
| 모델 | Can | Cup | Lemon | Avg. |
|---|---|---|---|---|
| DenseReward (Ours) | 0.219 | 0.181 | 0.288 | 0.229 |
| RoboReward-4B | 0.199 | 0.307 | 0.295 | 0.267 |
| RoboReward-8B | 0.314 | 0.270 | 0.317 | 0.300 |
| VLAC-2B | 0.316 | 0.346 | 0.380 | 0.347 |
| VLAC-8B | 0.351 | 0.360 | 0.363 | 0.358 |

DenseReward는 Avg.에서 가장 강한 기준선인 RoboReward-4B보다 약 14% 낮추었으며(표 값 0.267→0.229로 계산), 정성적 결과는 목표를 향한 더 일관된 유도를 보여줍니다.

### 소거 및 실제 세계
- 모든 실패 궤적을 제거하면 MAE가 0.0809에서 0.1312로 상승하여 실패 데이터의 유효성을 검증
- 과거 프레임 수 소거: 0프레임 0.096, 1프레임 0.088, 2프레임 0.081, 3프레임 0.086, 기본 2프레임이 최적
- 실제 세계: stack the cups 성공률이 40%에서 80%로, put ball in basket이 30%에서 70%로 향상(각 10회 시험 평가)

## 경계 및 한계

MPC 실험에는 회전 동작이 포함되지 않았는데, 이는 후보 동작 수와 계산 비용을 크게 증가시키기 때문입니다. 이는 자세 조정이 필요한 작업에서 보상 모델의 유도 능력이 검증되지 않았음을 의미합니다. 유효성 필터링 단계는 수동으로 설계된 검사 규칙에 의존하므로, 다루지 않는 실패 모드(예: 도구 사용 중 복잡한 고장)에서는 작동하지 않을 수 있습니다. 논문은 60개 훈련 물체 범주를 넘어서는 DenseReward의 일반화 경계를 명확히 밝히지 않았으며, 인간 선호 정렬도 다루지 않았습니다. 실제 세계 실험은 두 가지 작업에 각각 10회 시험뿐이므로 통계적 유의성이 제한적입니다.

## 공학적 시사점

재현 시 가장 먼저 확인해야 할 것은 데이터 생성 파이프라인의 유효성 검사 로직입니다. 이는 전체 방법의 신뢰성의 기초이며, 교란 자체가 항상 의도된 실패를 보장하지 않기 때문입니다(예: 교란된 그리핑이 여전히 물체를 잡을 수 있음). 필터링이 엄격하지 않으면 잘못 레이블된 데이터가 훈련을 오염시킬 수 있습니다. 다음으로 단계 경계 감지의 트리거 조건(Grasp 접촉, Lift 테이블 이탈, Place d_place 반경 진입)을 확인해야 하며, 이러한 임계값은 보상 곡선의 형태에 직접적인 영향을 미칩니다.

가장 함정에 빠지기 쉬운 부분은 MPC 평가의 후보 동작 공간 설계입니다: 28개 후보(27 방향 + 1 그리퍼)뿐이고 회전이 포함되지 않아 계산 비용을 통제하지만, 고자유도 작업에서 보상 모델의 성능 평가를 제한합니다. 하류 팀이 실제 세계 결과를 재현하려면 DSRL의 동결된 π_0 정책과 동작 크기 1.5 설정, 그리고 보상 통합 공식 r_t = -1 + r_t^model에서 오프셋이 탐색 행동에 미치는 영향을 주의해야 합니다. 훈련 예산 측면에서 stack the cups는 20k 스텝(약 20회 롤아웃), put ball in basket은 10k 스텝(약 10회 롤아웃)이 필요하며, 하드웨어는 Franka Research 3 + Robotiq 2F-85 + ZED 카메라 조합입니다.
