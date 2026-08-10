---
$id: ent_paper_perception_action_system_humanoid_robot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Perception-and-action system for humanoid robot task execution in construction
  zh: Perception-and-action system for humanoid robot task execution in construction
  ko: Perception-and-action system for humanoid robot task execution in construction
summary:
  en: Humanoid robots, with their human-like shape and multi-tasking capabilities, are well-aligned with human-dominated workplaces,
    like those in civil and construction engineering, where they could collaborate with human workers or autonomously perform
    physically demanding and hazardous tasks. Despite this promise, limited research has explored how to endow these robots
    with the practical.
  zh: 本文提出一套视觉感知-动作（VPA）系统，让Unitree G1人形机器人从RGB视频中学习并执行建筑工地任务。系统由Humanoid-PoseNet（3D姿态估计+人-人形运动重定向）与Humanoid-ActionNet（教师-学生强化学习控制器）组成，在8个建筑动作上达到82.45
    mm的平均MPJPE，并完成sim-to-real部署。
  ko: Humanoid robots, with their human-like shape and multi-tasking capabilities, are well-aligned with human-dominated workplaces,
    like those in civil and construction engineering, where they could collaborate with human workers or autonomously perform
    physically demanding and hazardous tasks. Despite this promise, limited research has explored how to endow these robots
    with the practical.
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
- perception
- action
- system
- humanoid
- robot
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
  title: arXiv:2608.01600 Perception-and-action system for humanoid robot task execution in construction
  url: https://arxiv.org/abs/2608.01600
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套视觉感知-动作（VPA）系统，让Unitree G1人形机器人从RGB视频中学习并执行建筑工地任务。系统由Humanoid-PoseNet（3D姿态估计+人-人形运动重定向）与Humanoid-ActionNet（教师-学生强化学习控制器）组成，在8个建筑动作上达到82.45 mm的平均MPJPE，并完成sim-to-real部署。

## 它改变了什么

建筑机器人领域长期被单任务设备（如SAM、MuLE、Spot）主导，它们无法适应工地的高度动态与多任务需求。人形机器人虽在形态上适配人类环境，但"看人类演示→变成机器人动作"这条链路存在两个被长期回避的断层：一是人类姿态因肢体比例、关节结构与驱动约束差异不能直接作为人形机器人的运动参考；二是即便得到运动学上兼容的姿态，如何将其转化为物理上可执行、保持平衡与接触一致性的全身动作，仍无系统解法。本文真正改变的，是首次把这两段断层用一个完整pipeline串起来——从单目RGB到物理机器人关节力矩，而不是像ExBody、OmniH2O等仅停留在运动模仿或日常场景。

另一个值得注意的改变在于评估范式。作者没有止步于仿真，而是强制要求策略必须通过IsaacGym→MuJoCo的sim-to-sim评估才能上真机，并在物理G1上复现全部8个动作。这种"跨模拟器验证作为部署门槛"的做法，在建筑机器人文献中罕见，直接回应了RL策略在接触丰富场景下迁移脆弱的痛点。

## 方法拆解

系统分两大模块，各自解决一段跨域映射。

### Humanoid-PoseNet：从人类视频到人形运动参考
- **3D姿态估计**：从2D RGB重建工人3D姿态，评估PoseNet、VideoPose3D、AlphaPose、3D-PoseNet四种骨干，PoseNet表现最优（58.3 mm MPJPE）。
- **人-人形重定向网络**：双编码器（Eh、Er）单解码器（Dr）结构，共享潜在空间。
  - Eh与Er均为MLP，**8**个全连接隐藏层、每层**128**单元、ReLU激活，输出d=**14**维潜在特征。
  - 训练用姿态三元组（两个人类姿态+一个人形姿态），损失含三项：
    - 三元组损失（公式2，常数c=**0.3**），用骨方向角度误差（BAE）度量姿态相似度；
    - 重建损失（公式3），确保Dr能从机器人潜在输入还原人形配置；
    - 潜在一致性损失（公式4），对齐跨域分布。
  - 总损失L_total = λ1L1 + λ2L2 + L3，λ1=**9.3**、λ2=**4.7**。

### Humanoid-ActionNet：从运动参考到物理可执行动作
- **教师-学生RL框架**：
  - 教师策略πteacher用PPO训练，输入特权观测（spo_t）、本体感觉状态（sps_t）与运动跟踪目标（smt_t），γ=**0.998**、GAE λ=**0.95**、裁剪ε=**0.2**。
  - 学生策略πstudent仅用运动跟踪目标与过去w=**10**帧本体感觉窗口，通过蒸馏损失ldistill=‖as_t−a∗_t‖²学习，结合DAgger持续蒸馏至收敛。
- **Actor网络四阶段结构**：
  1. 短历史编码器：4帧本体感觉经两层FC（128→16神经元+ELU）得到4个16维嵌入，拼接为64维后经16神经元FC融合，输出zfeat_t∈R^16；
  2. 拼接zfeat_t、sps_t、smt_t；
  3. 注入潜在变量zt：教师用特权观测经MLP（64→dz），学生用10帧窗口经历史编码器（FC投影→两个Conv1D层→展平→FC）得到；
  4. 全部特征拼接后经三层MLP（每层**256**神经元+ELU），最终FC输出23维动作均值μθ(st)。
- **PD控制器**：τt = Kp(at−qt) − Kd·q̇t，Kp=**200** N·m/rad（髋/膝）、**300**（躯干）、**40**（踝/肩/肘）；Kd=**5**（髋）、**10**（膝）、**6**（躯干）、**2**（踝/肩/肘）。
- **奖励设计**：物理感知式，含关节级跟踪（权重**5.0**）、关键点跟踪（**3.9**）、根部线速度（**6.0**）、身体旋转（**20.0**）、上半身一致性（**2.0**）、脚部空中时间整形（−**0.81**）、脚滑惩罚（−**0.002**）等。

### 数据与训练
- 5名受试者×30个动作×3次重复=**450**次试验，OptiTrack（**120** Hz）采集，RGB **30** fps，共约**150**分钟、**270000**张图像。
- RGB每30帧采样1帧得**9000**对RGB-3D样本，用于微调3D姿态估计（先在Human3.6M的**30000**样本上预训练）。
- 手动重定向：对齐T-pose、预定义关节对应、补偿尺度（人形尺度**0.01**），输出**14**关节人形表示。
- 数据划分：**80%**训练/评估（5折交叉验证）、**20%**测试。
- RL训练：PPO，学习率10⁻⁴，约**5000**次迭代收敛，训练**30000**次迭代，硬件为NVIDIA RTX PRO 6000 Blackwell Max-Q GPU。

## 关键创新

1. **首次打通"单目视频→物理人形机器人"的完整建筑任务执行链路**。此前ExBody、OmniH2O等全身控制方法面向行走、舞蹈等日常动作，本文是首个将人类施工演示转化为物理可执行人形动作的系统，且覆盖搬运、推车、举砖等接触丰富场景。

2. **跨域重定向的三元组损失设计**。用骨方向角度误差（BAE）替代传统关节位置误差，配合潜在一致性损失对齐人-人形分布，消融显示移除各损失项分别使MPJPE增加57.91 mm、37.33 mm、8.76 mm（由表内数值计算），证明三项损失各有不可替代的作用。

3. **"跨模拟器验证作为部署门槛"的工程范式**。强制要求策略通过IsaacGym→MuJoCo评估才可上真机，这一设计在建筑机器人文献中罕见，有效降低了sim-to-real的硬件风险，并保护现场人类监督员。

## 实验与结果

### 重定向精度（Humanoid-PoseNet）
- 3D姿态估计：PoseNet达**58.3** mm MPJPE，优于AlphaPose（**60.6**）、VideoPose3D（**60.3**）、3D-PoseNet（**61.0**）。
- 人形重定向（14关节平均）：**48.46** mm，各关节MPJPE在41.4（Arm）至51.8（Leg）之间。

### sim-to-sim评估（8个建筑动作）
| 动作 | MPJPE (mm) |
|---|---|
| Flagger signaling | 84.91 |
| Pushing a wheelbarrow | 82.14 |
| Over-the-shoulder carry | 87.04 |
| Carrying steel rod | 79.65 |
| Carry concrete block | 80.69 |
| Dragging a wheelbarrow | 82.46 |
| Carrying wood | 82.73 |
| Carrying pipe | 79.95 |
| **平均** | **82.45** |

### 与基线对比（14关节平均MPJPE）
| 方法 | MPJPE (mm) |
|---|---|
| ExBody | 102.75 |
| ExBody + AMP | 90.19 |
| OmniH2O | 96.35 |
| ExBody2 | 87.48 |
| **Humanoid-ActionNet** | **82.45** |

### 消融研究（重定向模块）
| 配置 | MPJPE (mm) |
|---|---|
| 排除L1 | 106.37 |
| 排除L2 | 85.79 |
| 排除L3 | 57.22 |
| 全部包含 | **48.46** |

### sim-to-real
物理G1成功复现全部8个测试动作，真实世界表现与IsaacGym-to-MuJoCo迁移趋势一致。训练指标：surrogate loss稳定在−**0.0037**，value loss降至**0.061**，学生蒸馏损失**0.0056**。

结果含义：Humanoid-ActionNet在平均MPJPE上比最强基线ExBody2低约5 mm（由表内数值82.45→87.48计算），优势主要体现在Foot（87.9 vs 108.8）与Leg（89.8 vs 84.5）等下肢关节，说明物理感知奖励对接触丰富的施工动作确有增益。

## 边界与局限

- **3D姿态估计非本文贡献**：实现细节与训练设置沿用先前工作，未做架构创新。
- **未建模工具/材料交互**：系统仅关注姿态运动模仿，不包含与施工工具或材料的物理交互建模；concrete-block试验因G1三指手不适合抓握，仅报告全身姿态执行。
- **短视界行为**：实验仅覆盖单一动作，未处理长视界、多步骤施工任务（如砌墙）。
- **sim-to-sim存在失败案例**：MuJoCo评估中出现失去平衡、扰动后不稳定恢复、跟踪崩溃三类失败，原因包括奖励函数难以捕捉接触丰富的施工动力学、模拟引擎间动力学与驱动不匹配。
- **数据规模有限**：仅5名受试者、30个动作，未使用现有施工活动数据集（如CML）。
- **跨平台适配未量化**：提及Unitree H1的适应性测试，但定量结果论文未明确。

## 工程启示

- **复现优先级**：先核对数据管线——Human3.6M的**30000**样本预训练与**9000**对自采样本微调是3D姿态估计精度的基础；手动重定向时人形尺度设为**0.01**这一细节直接影响后续所有MPJPE指标。
- **最容易踩坑处**：PD增益的设定高度依赖平台，Kp=**200**（髋/膝）、**300**（躯干）、**40**（踝/肩/肘）是针对G1调好的，换平台必须重新整定；学生策略的观测窗口w=**10**与历史编码器的Conv1D结构（kernel size 4→2、stride 2→1）是蒸馏质量的关键，改动需谨慎。
- **部署门槛建议**：作者强制IsaacGym→MuJoCo评估通过才上真机，这一流程值得直接采纳——MuJoCo中出现的失去平衡与跟踪崩溃案例，正是真实硬件上可能发生的故障预演。
- **下游团队注意**：手部配置差异不影响全身运动评估，但若任务涉及抓握（如concrete-block），需更换末端执行器或调整任务定义；负载限制为举升/搬运≤2 kg、推车总内容物≤10 kg，超出此范围需重新训练策略。

## Overview
Humanoid robots, with their human-like shape and multi-tasking capabilities, are well-aligned with human-dominated workplaces, like those in civil and construction engineering, where they could collaborate with human workers or autonomously perform physically demanding and hazardous tasks. Despite this promise, limited research has explored how to endow these robots with the practical capabilities needed to perform construction tasks. To this end, this study proposes a novel perception-and-action system that enables humanoid robots to learn and perform construction tasks from worker demonstrations. This system contains two deep networks: Humanoid-PoseNet, which extracts human postures and translates them into mechanically feasible poses for a humanoid robot; and Humanoid-ActionNet, which learns robot-executable actions based on these translated poses. Experimental results demonstrate that the humanoid robot reliably executed eight construction-related actions, achieving an average motion-tracking error of 82.45 mm MPJPE (Mean Per Joint Position Error). This work provides an early step toward deploying humanoid collaborators in construction.

## 参考
- https://arxiv.org/abs/2608.01600

## 개요

본 논문은 Unitree G1 휴머노이드 로봇이 RGB 비디오에서 건설 현장 작업을 학습하고 수행할 수 있도록 하는 시각-행동(VPA) 시스템을 제안한다. 이 시스템은 Humanoid-PoseNet(3D 자세 추정 + 인간-휴머노이드 모션 리타게팅)과 Humanoid-ActionNet(교사-학생 강화 학습 컨트롤러)으로 구성되며, 8가지 건설 작업에서 평균 82.45mm의 MPJPE를 달성하고 sim-to-real 배포를 완료한다.

## 무엇이 바뀌었는가

건설 로봇 분야는 오랫동안 단일 작업 장비(예: SAM, MuLE, Spot)가 지배해 왔으며, 이들은 건설 현장의 고도로 역동적이고 다중 작업 요구에 적응할 수 없었다. 휴머노이드 로봇은 형태적으로 인간 환경에 적합하지만, "인간 시연 보기 → 로봇 동작으로 변환"이라는 체인에는 오랫동안 회피되어 온 두 가지 단절이 존재한다. 첫째, 인간 자세는 사지 비율, 관절 구조 및 구동 제약의 차이로 인해 휴머노이드 로봇의 운동 참조로 직접 사용될 수 없다. 둘째, 운동학적으로 호환 가능한 자세를 얻더라도 이를 물리적으로 실행 가능하고 균형 및 접촉 일관성을 유지하는 전신 동작으로 변환하는 체계적인 해법은 없었다. 본 논문이 실제로 바꾼 것은 이 두 단절을 단일 파이프라인(단안 RGB에서 물리적 로봇 관절 토크까지)으로 처음으로 연결했다는 점이다. ExBody, OmniH2O 등이 단순한 모션 모방이나 일상적인 장면에 머물렀던 것과 대조적이다.

또 다른 주목할 만한 변화는 평가 패러다임에 있다. 저자들은 시뮬레이션에 그치지 않고, 정책이 실제 로봇에 적용되기 전에 반드시 IsaacGym→MuJoCo sim-to-sim 평가를 통과하도록 강제했으며, 물리적 G1에서 8가지 모든 동작을 재현했다. 이러한 "교차 시뮬레이터 검증을 배포 관문으로 삼는" 방식은 건설 로봇 문헌에서 드물며, 접촉이 풍부한 환경에서 RL 정책의 전이 취약성이라는 문제점을 직접적으로 해결한다.

## 방법 분석

시스템은 두 가지 주요 모듈로 구성되며, 각각 서로 다른 도메인 간 매핑을 해결한다.

### Humanoid-PoseNet: 인간 비디오에서 휴머노이드 운동 참조까지
- **3D 자세 추정**: 2D RGB에서 작업자의 3D 자세를 재구성하며, PoseNet, VideoPose3D, AlphaPose, 3D-PoseNet의 네 가지 백본을 평가했다. PoseNet이 가장 우수한 성능(58.3mm MPJPE)을 보였다.
- **인간-휴머노이드 리타게팅 네트워크**: 이중 인코더(Eh, Er) 단일 디코더(Dr) 구조로 공유 잠재 공간을 사용한다.
  - Eh와 Er은 모두 MLP로, **8**개의 완전 연결 은닉층, 각 층 **128**개 유닛, ReLU 활성화를 사용하며 d=**14**차원 잠재 특징을 출력한다.
  - 훈련에는 자세 삼중항(두 개의 인간 자세 + 하나의 휴머노이드 자세)을 사용하며, 손실은 세 가지 항목으로 구성된다:
    - 삼중항 손실(수식 2, 상수 c=**0.3**), 골 방향 각도 오차(BAE)로 자세 유사도 측정;
    - 재구성 손실(수식 3), Dr이 로봇 잠재 입력에서 휴머노이드 구성을 복원할 수 있도록 보장;
    - 잠재 일관성 손실(수식 4), 교차 도메인 분포 정렬.
  - 총 손실 L_total = λ1L1 + λ2L2 + L3, λ1=**9.3**, λ2=**4.7**.

### Humanoid-ActionNet: 운동 참조에서 물리적으로 실행 가능한 동작까지
- **교사-학생 RL 프레임워크**:
  - 교사 정책 πteacher는 PPO로 훈련되며, 특권 관측(spo_t), 고유수용성 상태(sps_t) 및 운동 추적 목표(smt_t)를 입력으로 사용하고, γ=**0.998**, GAE λ=**0.95**, 클리핑 ε=**0.2**를 적용한다.
  - 학생 정책 πstudent는 운동 추적 목표와 과거 w=**10**프레임의 고유수용성 상태 창만 사용하며, 증류 손실 ldistill=‖as_t−a∗_t‖²를 통해 학습하고, DAgger를 결합하여 수렴할 때까지 지속적으로 증류한다.
- **Actor 네트워크 4단계 구조**:
  1. 단기 기록 인코더: 4프레임 고유수용성 상태가 두 층의 FC(128→16 뉴런 + ELU)를 거쳐 4개의 16차원 임베딩을 얻고, 이를 연결하여 64차원으로 만든 후 16 뉴런 FC로 융합하여 zfeat_t∈R^16 출력;
  2. zfeat_t, sps_t, smt_t 연결;
  3. 잠재 변수 zt 주입: 교사는 특권 관측을 MLP(64→dz)로 처리하고, 학생은 10프레임 창을 기록 인코더(FC 프로젝션→두 개의 Conv1D 레이어→플래튼→FC)로 처리하여 획득;
  4. 모든 특징을 연결한 후 세 층의 MLP(각 층 **256** 뉴런 + ELU)를 거쳐 최종 FC가 23차원 동작 평균 μθ(st)를 출력.
- **PD 컨트롤러**: τt = Kp(at−qt) − Kd·q̇t, Kp=**200** N·m/rad(엉덩이/무릎), **300**(몸통), **40**(발목/어깨/팔꿈치); Kd=**5**(엉덩이), **10**(무릎), **6**(몸통), **2**(발목/어깨/팔꿈치).
- **보상 설계**: 물리 인지형으로, 관절 수준 추적(가중치 **5.0**), 키포인트 추적(**3.9**), 루트 선속도(**6.0**), 몸체 회전(**20.0**), 상체 일관성(**2.0**), 발 공중 시간 셰이핑(−**0.81**), 발 미끄러짐 패널티(−**0.002**) 등을 포함한다.

### 데이터 및 훈련
- 5명의 피험자 × 30개 동작 × 3회 반복 = **450**회 시험, OptiTrack(**120** Hz) 캡처, RGB **30** fps, 총 약 **150**분, **270000**장의 이미지.
- RGB에서 30프레임마다 1프레임을 샘플링하여 **9000**쌍의 RGB-3D 샘플을 얻고, 3D 자세 추정 미세 조정에 사용(먼저 Human3.6M의 **30000**개 샘플에서 사전 훈련).
- 수동 리타게팅: T-포즈 정렬, 사전 정의된 관절 대응, 스케일 보정(휴머노이드 스케일 **0.01**), **14**관절 휴머노이드 표현 출력.
- 데이터 분할: **80%** 훈련/평가(5겹 교차 검증), **20%** 테스트.
- RL 훈련: PPO, 학습률 10⁻⁴, 약 **5000**회 반복으로 수렴, **30000**회 반복 훈련, 하드웨어는 NVIDIA RTX PRO 6000 Blackwell Max-Q GPU.

## 핵심 혁신

1. **"단안 비디오→물리적 휴머노이드 로봇"의 완전한 건설 작업 실행 체인을 최초로 구축**. 이전 ExBody, OmniH2O 등의 전신 제어 방법은 걷기, 춤추기 등 일상적인 동작을 대상으로 했지만, 본 논문은 인간의 건설 시연을 물리적으로 실행 가능한 휴머노이드 동작으로 변환하는 최초의 시스템이며, 운반, 손수레 밀기, 벽돌 들기 등 접촉이 풍부한 장면을 포함한다.

2. **교차 도메인 리타게팅을 위한 삼중항 손실 설계**. 기존의 관절 위치 오차 대신 골 방향 각도 오차(BAE)를 사용하고, 잠재 일관성 손실을 결합하여 인간-휴머노이드 분포를 정렬한다. 소거 실험에서 각 손실 항목을 제거하면 MPJPE가 각각 57.91mm, 37.33mm, 8.76mm 증가하며(표 내 수치로 계산), 세 가지 손실이 각각 대체 불가능한 역할을 함을 입증한다.

3. **"교차 시뮬레이터 검증을 배포 관문으로 삼는" 엔지니어링 패러다임**. 정책이 IsaacGym→MuJoCo 평가를 통과해야만 실제 로봇에 적용할 수 있도록 강제하는 이 설계는 건설 로봇 문헌에서 드물며, sim-to-real의 하드웨어 위험을 효과적으로 줄이고 현장의 인간 감독자를 보호한다.

## 실험 및 결과

### 리타게팅 정밀도(Humanoid-PoseNet)
- 3D 자세 추정: PoseNet이 **58.3**mm MPJPE로 AlphaPose(**60.6**), VideoPose3D(**60.3**), 3D-PoseNet(**61.0**)보다 우수.
- 휴머노이드 리타게팅(14관절 평균): **48.46**mm, 각 관절 MPJPE는 41.4(Arm)에서 51.8(Leg) 사이.

### sim-to-sim 평가(8가지 건설 작업)
| 동작 | MPJPE (mm) |
|---|---|
| Flagger signaling | 84.91 |
| Pushing a wheelbarrow | 82.14 |
| Over-the-shoulder carry | 87.04 |
| Carrying steel rod | 79.65 |
| Carry concrete block | 80.69 |
| Dragging a wheelbarrow | 82.46 |
| Carrying wood | 82.73 |
| Carrying pipe | 79.95 |
| **평균** | **82.45** |

### 기준선 비교(14관절 평균 MPJPE)
| 방법 | MPJPE (mm) |
|---|---|
| ExBody | 102.75 |
| ExBody + AMP | 90.19 |
| OmniH2O | 96.35 |
| ExBody2 | 87.48 |
| **Humanoid-ActionNet** | **82.45** |

### 소거 연구(리타게팅 모듈)
| 구성 | MPJPE (mm) |
|---|---|
| L1 제외 | 106.37 |
| L2 제외 | 85.79 |
| L3 제외 | 57.22 |
| 모두 포함 | **48.46** |

## 경계 및 한계

- **3D 자세 추정은 본 논문의 기여가 아님**: 구현 세부 사항과 훈련 설정은 이전 연구를 따르며, 아키텍처 혁신은 없다.
- **도구/재료 상호작용 미모델링**: 시스템은 자세 운동 모방에만 초점을 맞추며, 건설 도구 또는 재료와의 물리적 상호작용 모델링은 포함하지 않는다. concrete-block 실험은 G1의 세 손가락 손이 파지에 적합하지 않아 전신 자세 실행만 보고한다.
- **단기 행동**: 실험은 단일 동작만 다루며, 장기적이고 다단계의 건설 작업(예: 벽 쌓기)은 처리하지 않는다.
- **sim-to-sim 실패 사례 존재**: MuJoCo 평가에서 균형 상실, 교란 후 불안정한 회복, 추적 붕괴의 세 가지 실패가 발생했으며, 원인은 접촉이 풍부한 건설 역학을 포착하기 어려운 보상 함수, 시뮬레이션 엔진 간의 역학 및 구동 불일치 등이다.
- **데이터 규모 제한**: 5명의 피험자, 30개 동작만 사용했으며, 기존 건설 활동 데이터셋(예: CML)은 사용하지 않았다.
- **교차 플랫폼 적응 미정량화**: Unitree H1 적응성 테스트를 언급했지만, 정량적 결과는 논문에 명시되지 않았다.

## 엔지니어링 시사점

- **재현 우선순위**: 먼저 데이터 파이프라인을 확인하라 — Human3.6M의 **30000**개 샘플 사전 훈련과 **9000**쌍의 자체 수집 샘플 미세 조정은 3D 자세 추정 정밀도의 기초다. 수동 리타게팅 시 휴머노이드 스케일을 **0.01**로 설정하는 세부 사항은 이후 모든 MPJPE 지표에 직접적인 영향을 미친다.
- **가장 함정에 빠지기 쉬운 부분**: PD 게인 설정은 플랫폼에 크게 의존한다. Kp=**200**(엉덩이/무릎), **300**(몸통), **40**(발목/어깨/팔꿈치)은 G1에 맞게 조정된 값이므로, 플랫폼을 바꾸면 반드시 재조정해야 한다. 학생 정책의 관측 창 w=**10**과 기록 인코더의 Conv1D 구조(kernel size 4→2, stride 2→1)는 증류 품질의 핵심이므로 변경에 주의해야 한다.
- **배포 관문 제안**: 저자들은 IsaacGym→MuJoCo 평가를 통과해야만 실제 로봇에 적용하도록 강제했으며, 이 프로세스는 직접 채택할 가치가 있다 — MuJoCo에서 발생한 균형 상실과 추적 붕괴 사례는 실제 하드웨어에서 발생할 수 있는 고장의 예고편이다.
- **하류 팀 주의사항**: 손 구성 차이는 전신 운동 평가에 영향을 미치지 않지만, 작업에 파지가 포함된 경우(예: concrete-block) 말단 실행기를 교체하거나 작업 정의를 조정해야 한다. 부하 제한은 들어올리기/운반 ≤2kg, 손수레 총 내용물 ≤10kg이며, 이 범위를 초과하면 정책을 재훈련해야 한다.
