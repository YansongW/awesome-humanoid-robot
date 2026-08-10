---
$id: ent_paper_rapid_locomotion_reinforcement_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Rapid Locomotion via Reinforcement Learning
  zh: Rapid Locomotion via Reinforcement Learning
  ko: Rapid Locomotion via Reinforcement Learning
summary:
  en: Agile maneuvers such as sprinting and high-speed turning in the wild are challenging for legged robots. We present an
    end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
    This system runs and turns fast on natural terrains like grass, ice, and gravel and responds robustly to disturbances.
    Our controller is a neural network trained.
  zh: 本文由 MIT 团队提出，用端到端强化学习在 MIT Mini Cheetah 上实现了最高 3.9 m/s 的持续奔跑与 5.7 rad/s 的旋转，核心贡献是联合建模线速度与角速度指令的 Grid Adaptive 课程，以及教师-学生框架下的在线系统识别模块，使策略仅凭关节编码器与
    IMU 即可零样本部署到真实机器人。
  ko: Agile maneuvers such as sprinting and high-speed turning in the wild are challenging for legged robots. We present an
    end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
    This system runs and turns fast on natural terrains like grass, ice, and gravel and responds robustly to disturbances.
    Our controller is a neural network trained.
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
- rapid
- locomotion
- reinforcement
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P011. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过
    2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。 | WP4 trilingual backfill 2026-08-10:
    en body retranslated from zh deep-read (3008 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: arXiv:2205.02824 Rapid Locomotion via Reinforcement Learning
  url: https://arxiv.org/abs/2205.02824
  date: '2022-05-05'
  accessed_at: '2026-08-05'
---
## 概述

本文由 MIT 团队提出，用端到端强化学习在 MIT Mini Cheetah 上实现了最高 3.9 m/s 的持续奔跑与 5.7 rad/s 的旋转，核心贡献是联合建模线速度与角速度指令的 Grid Adaptive 课程，以及教师-学生框架下的在线系统识别模块，使策略仅凭关节编码器与 IMU 即可零样本部署到真实机器人。

## 它改变了什么

它改变的是“高速敏捷运动必须依赖人工设计降阶模型”这一前提。此前基于 MPC 的方法在 Mini Cheetah 上达到 3.7 m/s，但每个新地形、新速度区间都需要工程师重新调模型参数；而纯 RL 方法在指令范围扩大到高速时训练失败，因为随机探索几乎无法产生高速样本，奖励信号稀疏。作者指出，问题不在 RL 本身，而在指令采样方式——独立采样线速度和角速度会频繁生成离心力约束下不可行的组合，导致策略学到原地抖动而非奔跑。这实际上把“任务难度”从动力学问题重新定义为“指令分布设计”问题，为 RL 在敏捷控制中的可用性扫清了障碍。

## 方法拆解

### 整体架构
- 策略 πθ 输入历史观测 o_{t-H:t}（H=15）与速度指令 v_t^cmd，输出 12 维关节位置指令，由 PD 控制器（Kp=20, Kd=0.5）转为扭矩。观测仅含关节角度/速度、IMU 重力方向、上一动作，无视觉、无外部定位。

### 教师-学生训练
- 教师 πT(x_t, d_t) = π_{θb}(x_t, g_{θd}(d_t))：编码器 g_{θd} 将 12 维域参数 d_t（质量、质心、摩擦、电机强度等）压缩为 8 维潜变量 z_t，策略主体 π_{θb} 据此输出动作，用 PPO 联合优化。
- 学生 πS(x_t, x_{[t-h:t-1]}) = π_{θb}(x_t, h_{θa}(...))：用适应模块 h_{θa} 从 42×15 的历史观测估计 ẑ_t，损失 L = (ẑ_t - z_t)² 监督训练。关键设计是 h=15 足够短，使适应模块能与策略主体在 50 Hz 实时同步运行。

### Grid Adaptive 课程
- 将 v_x^cmd-ω_z^cmd 平面离散为 [0.5 m/s, 0.5 rad/s] 网格，维护联合分布。若某网格奖励低于阈值 γ，保持概率；否则将 4-连通邻域概率设为 1。初始为 [-1.0, 1.0]×[-1.0, 1.0] 均匀分布。
- 与 Box Adaptive（独立维护边际分布）的本质区别：Grid 显式建模 v_x 与 ω_z 的耦合——高速时离心力使可行域满足 ω_z ∼ 1/v_x，独立采样会等概率生成不可行组合，而联合分布能自动聚焦于可行区域。

### 域随机化
- 范围：地面摩擦 [0.05, 4.00]，恢复系数 [0.00, 1.00]，载荷质量 [-1.0, 3.0] kg，质心偏移 [-0.10, 0.10] m，电机强度 [90, 110]%。

## 关键创新

1. **Grid Adaptive 课程**：首次将指令空间视为联合分布而非独立边际。这不是工程细节，而是对“任务难度由动力学与优化算法共同决定”的显式建模——它让策略在训练中自动避开不可行的速度-角速度组合，从而发现高速奔跑行为。无课程与 Box 课程均失败，Grid 是唯一成功者。
2. **在线系统识别模块**：与文献 [23, 24] 不同，适应模块 h_{θa} 与教师同时用在线数据训练，且历史长度 h=15 足够小以实时运行。这使得学生策略在部署时无需任何微调，仅凭板载传感器即可隐式估计地形摩擦、载荷等域参数，实现零样本 sim-to-real 迁移。
3. **低增益 PD 控制器**：Kp=20, Kd=0.5 远低于常见设置，作者刻意选择低增益以促进平滑运动且不调整。这使动作空间更接近“期望位置”而非“刚性跟踪”，减少了仿真与真实的动力学失配。

## 实验与结果

### 关键结果
- 室内平地最高持续速度 **3.9 m/s**（3 个种子中最高），平均 **3.8 m/s**，超过同一机器人 MPC 的 3.7 m/s 记录。
- 户外 10 米草地冲刺平均 **3.4 m/s**（2.94 秒）。
- 最大偏航速率 **5.7 rad/s**，为模型基记录 6.28 rad/s 的 90%，且单个策略同时实现线速度与角速度（模型基需两个控制器）。
- 消融：学生策略 π_θ_ST 真实速度 3.81 ± 0.09 m/s，显著高于无系统识别的 π_θ_DR（2.49 ± 0.07 m/s），证明适应模块是 sim-to-real 的关键。

| 配置 | 仿真速度 (m/s) | 真实速度 (m/s) |
|---|---|---|
| 带系统识别 π_θ_ST | 5.46 | 3.81 ± 0.09 |
| 不带系统识别 π_θ_DR | 5.07 | 2.49 ± 0.07 |

### 课程对比
- 无课程：无法学习，机器人原地抖动。
- Box Adaptive：能控制但排除指令空间极端区域。
- Grid Adaptive：在所有误差阈值下覆盖更大命令面积（图 3），且命令面积随地形粗糙度增加而缩小（图 5，ε=0.3 处比较）。

### 鲁棒性
- 定性报告：爬砾石坡、单电机阻塞保持平衡、高速绊倒后恢复。MPC 基线在砾石坡滑下与绊倒障碍两个场景中未能恢复。

## 边界与局限

- 未在真实机器人上微调策略（零样本部署），但 sim-to-real 差距的来源（仿真参数不准确 vs 真实动力学不可捕获）未量化。
- 户外性能仅定性报告，因无法用动作捕捉记录状态，且高速摔倒对硬件不安全。
- 仅训练地面平面内的机体速度，不含跳跃、蹲伏、移动操作；不使用视觉，无法执行需要前瞻规划的任务（如上楼梯、避坑）。
- 高速步态不必然“更好”，未优化能效或磨损；仅机体速度是欠约束目标，可能存在多种同等偏好的运动。
- 教师策略无法直接部署，因域参数 d_t 无法用板载传感器测量。

## 工程启示

- **复现优先核对**：训练数据量 4 亿时间步、4000 并行环境、单块 RTX 3090 上墙钟 <3 小时（约 92 个实时天）。若资源有限，可先验证 Grid 课程在 1 亿步内是否出现高速行为，再决定是否扩量。
- **最容易踩坑**：课程阈值 γ 与网格分辨率 [0.5, 0.5] 是敏感超参。γ 过高会过早扩大指令范围导致训练不稳定，过低则策略停留在低速区域。建议从 γ=0.3 起调，并监控命令面积随训练步数的增长曲线。
- **系统识别模块的部署**：h=15 的历史长度是实时性关键，若下游平台计算资源弱于 Jetson TX2 NX，需先验证适应模块推理延迟是否满足 50 Hz 控制周期。
- **对下游团队的启示**：传感器仅需关节编码器与 IMU，适用于廉价四足机器人。但域随机化范围（摩擦 [0.05, 4.00] 等）是针对 Mini Cheetah 标定的，迁移到其他平台需重新扫描，尤其是电机强度范围 [90, 110]% 可能不适用于低扭矩执行器。

## 参考
- https://arxiv.org/abs/2205.02824

## 개요

본 논문은 MIT 팀이 제안한 것으로, 엔드투엔드 강화학습을 통해 MIT Mini Cheetah에서 최대 3.9 m/s의 지속적인 달리기와 5.7 rad/s의 회전을 구현했습니다. 핵심 기여는 선속도와 각속도 명령을 결합 모델링하는 Grid Adaptive 커리큘럼과, 교사-학생 프레임워크 하의 온라인 시스템 식별 모듈로, 정책이 관절 엔코더와 IMU만으로 실제 로봇에 제로샷 배포가 가능하게 한 것입니다.

## 무엇을 바꾸었는가

"고속 민첩 운동은 반드시 수동으로 설계된 축소 모델에 의존해야 한다"는 전제를 바꾸었습니다. 이전의 MPC 기반 방법은 Mini Cheetah에서 3.7 m/s를 달성했지만, 새로운 지형이나 속도 구간마다 엔지니어가 모델 파라미터를 재조정해야 했습니다. 반면 순수 RL 방법은 명령 범위가 고속으로 확장될 때 훈련에 실패했는데, 이는 무작위 탐색이 고속 샘플을 거의 생성할 수 없고 보상 신호가 희박하기 때문입니다. 저자들은 문제가 RL 자체가 아니라 명령 샘플링 방식에 있다고 지적합니다. 선속도와 각속도를 독립적으로 샘플링하면 원심력 제약 하에서 실행 불가능한 조합이 빈번하게 생성되어, 정책이 달리기 대신 제자리 떨림을 학습하게 됩니다. 이는 사실상 "작업 난이도"를 동역학 문제에서 "명령 분포 설계" 문제로 재정의한 것이며, RL의 민첩 제어 적용 가능성을 위한 장애물을 제거했습니다.

## 방법 분해

### 전체 아키텍처
- 정책 πθ는 과거 관측 o_{t-H:t} (H=15)과 속도 명령 v_t^cmd를 입력으로 받아 12차원 관절 위치 명령을 출력하며, PD 컨트롤러 (Kp=20, Kd=0.5)가 이를 토크로 변환합니다. 관측은 관절 각도/속도, IMU 중력 방향, 이전 행동만 포함하며, 비전이나 외부 위치 추적은 없습니다.

### 교사-학생 훈련
- 교사 πT(x_t, d_t) = π_{θb}(x_t, g_{θd}(d_t)): 인코더 g_{θd}가 12차원 도메인 파라미터 d_t (질량, 질량 중심, 마찰, 모터 강도 등)를 8차원 잠재 변수 z_t로 압축하고, 정책 본체 π_{θb}가 이를 기반으로 행동을 출력하며, PPO로 공동 최적화합니다.
- 학생 πS(x_t, x_{[t-h:t-1]}) = π_{θb}(x_t, h_{θa}(...)): 적응 모듈 h_{θa}가 42×15의 과거 관측에서 ẑ_t를 추정하며, 손실 L = (ẑ_t - z_t)²로 지도 훈련합니다. 핵심 설계는 h=15가 충분히 짧아 적응 모듈이 정책 본체와 50 Hz에서 실시간 동기 실행이 가능하다는 점입니다.

### Grid Adaptive 커리큘럼
- v_x^cmd-ω_z^cmd 평면을 [0.5 m/s, 0.5 rad/s] 그리드로 이산화하고 결합 분포를 유지합니다. 특정 그리드의 보상이 임계값 γ보다 낮으면 확률을 유지하고, 그렇지 않으면 4-연결 이웃의 확률을 1로 설정합니다. 초기값은 [-1.0, 1.0]×[-1.0, 1.0] 균등 분포입니다.
- Box Adaptive (독립적 주변 분포 유지)와의 본질적 차이: Grid는 v_x와 ω_z의 결합을 명시적으로 모델링합니다. 고속에서는 원심력으로 인해 실행 가능 영역이 ω_z ∼ 1/v_x를 만족하는데, 독립 샘플링은 실행 불가능한 조합을 등확률로 생성하는 반면, 결합 분포는 자동으로 실행 가능 영역에 집중할 수 있습니다.

### 도메인 무작위화
- 범위: 지면 마찰 [0.05, 4.00], 반발 계수 [0.00, 1.00], 하중 질량 [-1.0, 3.0] kg, 질량 중심 오프셋 [-0.10, 0.10] m, 모터 강도 [90, 110]%.

## 핵심 혁신

1. **Grid Adaptive 커리큘럼**: 명령 공간을 독립적 주변 분포가 아닌 결합 분포로 처음 취급했습니다. 이는 공학적 세부 사항이 아니라 "작업 난이도가 동역학과 최적화 알고리즘에 의해 공동 결정된다"는 점을 명시적으로 모델링한 것입니다. 이를 통해 정책이 훈련 중 실행 불가능한 속도-각속도 조합을 자동으로 회피하여 고속 달리기 행동을 발견할 수 있습니다. 커리큘럼 없음과 Box 커리큘럼은 모두 실패했으며, Grid만이 유일하게 성공했습니다.
2. **온라인 시스템 식별 모듈**: 문헌 [23, 24]과 달리 적응 모듈 h_{θa}는 교사와 동시에 온라인 데이터로 훈련되며, 히스토리 길이 h=15가 실시간 실행에 충분히 작습니다. 이를 통해 학생 정책은 배포 시 미세 조정 없이 온보드 센서만으로 지형 마찰, 하중 등 도메인 파라미터를 암시적으로 추정하여 제로샷 sim-to-real 전이를 달성합니다.
3. **낮은 이득 PD 컨트롤러**: Kp=20, Kd=0.5는 일반적인 설정보다 훨씬 낮으며, 저자들은 의도적으로 낮은 이득을 선택하여 부드러운 운동을 촉진하고 조정하지 않습니다. 이는 행동 공간을 "강성 추적"보다 "기대 위치"에 가깝게 만들어 시뮬레이션과 실제의 동역학 불일치를 줄입니다.

## 실험 및 결과

### 핵심 결과
- 실내 평지 최대 지속 속도 **3.9 m/s** (3개 시드 중 최고), 평균 **3.8 m/s**로, 동일 로봇의 MPC 기록 3.7 m/s를 초과했습니다.
- 야외 10m 잔디 질주 평균 **3.4 m/s** (2.94초).
- 최대 요(yaw)율 **5.7 rad/s**로, 모델 기반 기록 6.28 rad/s의 90%이며, 단일 정책이 선속도와 각속도를 동시에 구현합니다 (모델 기반은 두 컨트롤러 필요).
- 절제: 학생 정책 π_θ_ST의 실제 속도 3.81 ± 0.09 m/s로, 시스템 식별이 없는 π_θ_DR (2.49 ± 0.07 m/s)보다 유의미하게 높아 적응 모듈이 sim-to-real의 핵심임을 입증합니다.

| 구성 | 시뮬레이션 속도 (m/s) | 실제 속도 (m/s) |
|---|---|---|
| 시스템 식별 포함 π_θ_ST | 5.46 | 3.81 ± 0.09 |
| 시스템 식별 없음 π_θ_DR | 5.07 | 2.49 ± 0.07 |

### 커리큘럼 비교
- 커리큘럼 없음: 학습 불가, 로봇이 제자리 떨림.
- Box Adaptive: 제어 가능하지만 명령 공간의 극단 영역을 배제.
- Grid Adaptive: 모든 오류 임계값에서 더 넓은 명령 면적을 커버 (그림 3), 명령 면적은 지형 거칠기가 증가함에 따라 감소 (그림 5, ε=0.3에서 비교).

### 견고성
- 정성적 보고: 자갈 경사로 오르기, 단일 모터 차단 시 균형 유지, 고속에서 걸려 넘어진 후 회복. MPC 기준선은 자갈 경사로 미끄러짐과 걸림 장애물 두 시나리오에서 회복하지 못했습니다.

## 경계 및 한계

- 실제 로봇에서 정책을 미세 조정하지 않았지만 (제로샷 배포), sim-to-real 격차의 원인 (시뮬레이션 파라미터 부정확 vs 실제 동역학 포착 불가)은 정량화되지 않았습니다.
- 야외 성능은 모션 캡처로 상태를 기록할 수 없고 고속 낙상이 하드웨어에 안전하지 않아 정성적으로만 보고되었습니다.
- 지면 평면 내의 본체 속도만 훈련하며, 점프, 웅크리기, 이동 조작은 포함하지 않습니다. 비전을 사용하지 않으므로 계단 오르기, 구덩이 회피와 같은 전방 계획이 필요한 작업은 수행할 수 없습니다.
- 고속 보행이 반드시 "더 좋은" 것은 아니며, 에너지 효율이나 마모를 최적화하지 않았습니다. 본체 속도만으로는 과소 결정된 목표이므로 동등하게 선호되는 여러 운동이 존재할 수 있습니다.
- 교사 정책은 도메인 파라미터 d_t를 온보드 센서로 측정할 수 없으므로 직접 배포할 수 없습니다.

## 공학적 시사점

- **재현 시 우선 확인 사항**: 훈련 데이터 4억 타임스텝, 4000 병렬 환경, 단일 RTX 3090에서 벽시계 <3시간 (약 92 실시간 일). 자원이 제한적이라면 Grid 커리큘럼이 1억 스텝 내에 고속 행동을 나타내는지 먼저 검증한 후 확장 여부를 결정하세요.
- **가장 흔한 함정**: 커리큘럼 임계값 γ와 그리드 해상도 [0.5, 0.5]는 민감한 하이퍼파라미터입니다. γ가 너무 높으면 명령 범위가 조기에 확장되어 훈련이 불안정해지고, 너무 낮으면 정책이 저속 영역에 머무릅니다. γ=0.3에서 시작하여 훈련 스텝에 따른 명령 면적 증가 곡선을 모니터링하는 것을 권장합니다.
- **시스템 식별 모듈 배포**: h=15의 히스토리 길이는 실시간성의 핵심입니다. 다운스트림 플랫폼의 컴퓨팅 자원이 Jetson TX2 NX보다 약하다면 적응 모듈 추론 지연이 50 Hz 제어 주기를 충족하는지 먼저 검증해야 합니다.
- **다운스트림 팀에 대한 시사점**: 센서는 관절 엔코더와 IMU만 필요하므로 저가형 네 발 로봇에 적합합니다. 그러나 도메인 무작위화 범위 (마찰 [0.05, 4.00] 등)는 Mini Cheetah에 맞게 보정된 것이므로, 다른 플랫폼으로 전이할 때 특히 모터 강도 범위 [90, 110]%가 저토크 액추에이터에는 적합하지 않을 수 있으므로 재스캔이 필요합니다.

## Overview

This paper, proposed by the MIT team, achieves sustained running speeds of up to 3.9 m/s and rotational speeds of 5.7 rad/s on the MIT Mini Cheetah using end-to-end reinforcement learning. The core contributions are a Grid Adaptive curriculum that jointly models linear and angular velocity commands, and an online system identification module within a teacher-student framework, enabling zero-shot deployment of the policy to the real robot using only joint encoders and an IMU.

## What It Changes

It changes the premise that "high-speed agile locomotion must rely on manually designed reduced-order models." Previous MPC-based methods reached 3.7 m/s on the Mini Cheetah, but every new terrain or speed range required engineers to re-tune model parameters. Pure RL methods failed when the command range expanded to high speeds because random exploration rarely produces high-speed samples, resulting in sparse reward signals. The authors point out that the problem is not with RL itself, but with the command sampling method—independently sampling linear and angular velocities frequently generates combinations that are infeasible under centrifugal force constraints, causing the policy to learn in-place jittering rather than running. This effectively redefines "task difficulty" from a dynamics problem to a "command distribution design" problem, clearing the way for RL's applicability in agile control.

## Method Breakdown

### Overall Architecture
- The policy πθ takes as input historical observations o_{t-H:t} (H=15) and the velocity command v_t^cmd, and outputs 12-dimensional joint position commands, converted to torques by a PD controller (Kp=20, Kd=0.5). Observations include only joint angles/velocities, IMU gravity direction, and the previous action—no vision, no external localization.

### Teacher-Student Training
- Teacher πT(x_t, d_t) = π_{θb}(x_t, g_{θd}(d_t)): An encoder g_{θd} compresses 12-dimensional domain parameters d_t (mass, center of mass, friction, motor strength, etc.) into an 8-dimensional latent variable z_t. The main policy π_{θb} outputs actions based on this, optimized jointly with PPO.
- Student πS(x_t, x_{[t-h:t-1]}) = π_{θb}(x_t, h_{θa}(...)): An adaptation module h_{θa} estimates ẑ_t from 42×15 historical observations, supervised by the loss L = (ẑ_t - z_t)². The key design choice is that h=15 is short enough for the adaptation module to run synchronously with the main policy in real time at 50 Hz.

### Grid Adaptive Curriculum
- The v_x^cmd-ω_z^cmd plane is discretized into a [0.5 m/s, 0.5 rad/s] grid, maintaining a joint distribution. If a grid cell's reward falls below a threshold γ, its probability is preserved; otherwise, the probabilities of its 4-connected neighbors are set to 1. The initial distribution is uniform over [-1.0, 1.0]×[-1.0, 1.0].
- The essential difference from Box Adaptive (which maintains independent marginal distributions): Grid explicitly models the coupling between v_x and ω_z—at high speeds, centrifugal force makes the feasible region satisfy ω_z ∼ 1/v_x. Independent sampling generates infeasible combinations with equal probability, whereas the joint distribution automatically focuses on feasible regions.

### Domain Randomization
- Range: ground friction [0.05, 4.00], coefficient of restitution [0.00, 1.00], payload mass [-1.0, 3.0] kg, center of mass offset [-0.10, 0.10] m, motor strength [90, 110]%.

## Key Innovations

1. **Grid Adaptive Curriculum**: The first to treat the command space as a joint distribution rather than independent marginals. This is not an engineering detail but an explicit modeling of "task difficulty being jointly determined by dynamics and the optimization algorithm"—it allows the policy to automatically avoid infeasible velocity-angular velocity combinations during training, thereby discovering high-speed running behavior. Both no-curriculum and Box curriculum fail; Grid is the only successful one.
2. **Online System Identification Module**: Unlike references [23, 24], the adaptation module h_{θa} is trained with online data simultaneously with the teacher, and the history length h=15 is small enough for real-time operation. This allows the student policy to implicitly estimate domain parameters such as terrain friction and payload from onboard sensors alone at deployment, with no fine-tuning, achieving zero-shot sim-to-real transfer.
3. **Low-Gain PD Controller**: Kp=20, Kd=0.5 is far lower than common settings. The authors deliberately choose low gains to promote smooth motion and do not tune them. This makes the action space closer to "desired positions" rather than "rigid tracking," reducing dynamics mismatch between simulation and reality.

## Experiments and Results

### Key Results
- Highest sustained speed on indoor flat ground: **3.9 m/s** (best of 3 seeds), average **3.8 m/s**, surpassing the 3.7 m/s MPC record on the same robot.
- Outdoor 10-meter grass sprint: average **3.4 m/s** (2.94 seconds).
- Maximum yaw rate: **5.7 rad/s**, 90% of the model-based record of 6.28 rad/s, and a single policy simultaneously achieves linear and angular velocity (model-based requires two controllers).
- Ablation: The student policy π_θ_ST achieves a real-world speed of 3.81 ± 0.09 m/s, significantly higher than π_θ_DR without system identification (2.49 ± 0.07 m/s), demonstrating that the adaptation module is key to sim-to-real transfer.

| Configuration | Simulation Speed (m/s) | Real-World Speed (m/s) |
|---|---|---|
| With system ID π_θ_ST | 5.46 | 3.81 ± 0.09 |
| Without system ID π_θ_DR | 5.07 | 2.49 ± 0.07 |

### Curriculum Comparison
- No curriculum: fails to learn, robot jitters in place.
- Box Adaptive: controllable but excludes extreme regions of the command space.
- Grid Adaptive: covers a larger command area under all error thresholds (Figure 3), and the command area shrinks as terrain roughness increases (Figure 5, comparison at ε=0.3).

### Robustness
- Qualitative reports: climbing gravel slopes, maintaining balance with a single motor blocked, and recovering after high-speed trips. The MPC baseline fails to recover in both the gravel slope descent and trip-over-obstacle scenarios.

## Boundaries and Limitations

- The policy is not fine-tuned on the real robot (zero-shot deployment), but the sources of the sim-to-real gap (inaccurate simulation parameters vs. uncapturable real-world dynamics) are not quantified.
- Outdoor performance is only qualitatively reported, as state cannot be recorded with motion capture, and high-speed falls are unsafe for the hardware.
- Only body velocity in the ground plane is trained; jumping, crouching, and mobile manipulation are not included. No vision is used, so tasks requiring look-ahead planning (e.g., climbing stairs, avoiding pits) cannot be performed.
- High-speed gaits are not necessarily "better"; energy efficiency and wear are not optimized. Body velocity alone is an under-constrained objective, and multiple equally preferred motions may exist.
- The teacher policy cannot be deployed directly because the domain parameters d_t cannot be measured with onboard sensors.

## Engineering Insights

- **Priority for reproduction**: Training data volume is 400 million time steps, with 4000 parallel environments, and wall-clock time on a single RTX 3090 is <3 hours (approximately 92 real-time days). If resources are limited, first verify whether the Grid curriculum produces high-speed behavior within 100 million steps before deciding to scale up.
- **Most common pitfall**: The curriculum threshold γ and grid resolution [0.5, 0.5] are sensitive hyperparameters. If γ is too high, the command range expands prematurely, causing training instability; if too low, the policy remains in low-speed regions. It is recommended to start tuning from γ=0.3 and monitor the growth curve of command area versus training steps.
- **Deployment of the system identification module**: The history length h=15 is critical for real-time performance. If the downstream platform has weaker computational resources than the Jetson TX2 NX, first verify that the adaptation module's inference latency meets the 50 Hz control cycle.
- **Insights for downstream teams**: Sensors only require joint encoders and an IMU, making it suitable for low-cost quadruped robots. However, the domain randomization ranges (friction [0.05, 4.00], etc.) are calibrated for the Mini Cheetah; migrating to other platforms requires re-scanning, especially the motor strength range [90, 110]%, which may not apply to low-torque actuators.
