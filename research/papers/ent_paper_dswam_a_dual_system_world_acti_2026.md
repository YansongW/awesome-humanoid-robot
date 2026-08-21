---
$id: ent_paper_dswam_a_dual_system_world_acti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
  zh: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
  ko: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
summary:
  en: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
  zh: DSWAM 是一个双系统世界动作基础模型，由研究者提出用于精细机器人操作。其核心贡献在于结合了 System 1 的 WAM 执行器与可选的 System 2 视觉语言子任务规划器，以弥补现有 WAM 在粗指令分解上的不足。该模型在
    DeMaVLA 真实变形操作设置下，通过匹配的机器人平台、预训练数据、后训练数据和评估标准，实现了与 VLA 策略的公平对比。
  ko: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
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
- robotics
- dswam
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04927v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (737 chars, DeepSeek). [2026-08-21] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04927
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述

DSWAM 提出一种双系统世界动作基础模型，用于细粒度机器人操作。其核心是 DynaRetarget 框架，将逆运动学重定向与新型采样轨迹优化（SBTO）结合，通过增量扩展优化时域生成动态可行的轨迹，并支持零样本迁移到真实机器人。作者在 285 个 OmniRetarget 运动上验证，SBTO 成功率达 74.6%，显著优于 SPIDER 的 37.9%。

## 它改变了什么

现有 loco-manipulation 轨迹生成方法存在根本性缺陷：基于运动学优化的重定向产生物理不一致伪影（缺失接触、穿透），而短时域模型预测控制（如 SPIDER）具有固有短视性，无法保证长时域一致性。深度 RL 虽鲁棒但探索困难，需要大量奖励塑形。作者真正改变的是将轨迹优化从“固定时域单射”范式转向“增量时域扩展”范式，使长时域问题通过短时域子问题逐步求解，从而在保持计算可行性的同时获得全局一致性。

这一转变的关键在于认识到全时域单射优化会因变量数增长和局部极小值而失败，而短时域优化虽高效但短视。通过增量扩展时域，SBTO 在每次迭代中只优化当前活动节点，避免了对末端变量的过早更新，使前端变量有足够机会逃离局部极小。这解决了长时域行为生成中“探索-利用”的根本矛盾。

## 方法拆解

### 整体流程
人类-物体演示 → IK 重定向（运动学可行但不完美）→ SBTO 动态精炼 → RL 跟踪策略训练（带域随机化）→ 零样本迁移

### 最优控制问题
最小化成本 J，满足动力学 x_{t+1}=f_dyn(x_t, u_t)，状态 x_t=(q_t, v_t)，控制 u_t。采用单射方式，用 MuJoCo 模拟器作为黑盒滚动动力学。

### SBTO 核心算法
- **采样优化**：使用 CEM，采样插值节点 k ∈ R^{K·n_u} 而非完整控制序列，节点时间等距分布（τ_0=0, τ_{K-1}=T-1），间隔 0.25 s
- **FHTO（固定时域）**：迭代采样 N=1024 个节点、插值、滚动、评估成本、更新分布参数（精英集比例 ρ_e=0.03，保留精英比例 ρ_k=0.04，均值动量 α_μ=0.95，协方差动量 α_Σ=0.2，初始标准差 σ_0=0.25）
- **增量扩展**：外循环从 k=1 到 K-1 增加优化变量数，内循环精炼当前活动变量；每次增量只部分滚动到 τ_k
- **收敛条件**：协方差矩阵 Σ 最大对角值低于阈值 σ_min 时进行增量

### 关键设计决策
- 增量优化避免全时域单射优化因变量数和局部极小值失败
- σ_min 需适中：太小使分布缩成点分布，阻止前端变量逃离局部极小；太大致增量过早，等同于从头求解全时域问题
- 适用于成本函数稠密的问题，短时域窗口能提供有意义的解估计

### 成本函数
惩罚状态位置 q 和速度 v 偏差，加任务空间项（躯干、脚、手位姿），接触项惩罚非期望碰撞。关键权重：物体位置 40.0、物体方向 4.0、躯干位置 30.0、脚位置 10.0、手位置 5.0、机器人-物体碰撞 2.0、自碰撞 1.0。

## 关键创新

1. **增量时域扩展机制**：这是首次将时域增量扩展与采样优化结合，使长时域问题通过短时域子问题逐步求解。不同于 SBMPC 的固定短时域，SBTO 通过外循环增加优化变量数，最终求解原始长时域问题，同时避免全时域单射优化的失败模式。

2. **部分滚动策略**：每次增量只滚动到当前最后优化节点 τ_k，而非从头滚动全轨迹。这显著降低计算成本，同时保持对前端变量的持续优化。案例分析显示，即使经过 10 次时域增量（有效时域约 3.4 s），前端节点仍被优化。

3. **协方差收敛驱动的自适应增量**：通过监控协方差矩阵最大对角值决定增量时机，使优化过程自适应问题难度。σ_min 的适中设置平衡了探索与利用，这是传统固定时域方法无法实现的。

## 实验与结果

### 实验设置
- 任务：OmniRetarget 数据集中 285 个短于 9 s 的运动，包含 G1 人形机器人与箱子交互（pick-and-place、踢、推/拖）
- 基线：SPIDER（SBMPC）、SBTO_pos（SBTO 变体，仅用配置项，省略速度项）
- 成功标准：物体轨迹平均位置误差 E_pos < 10 cm 且平均旋转误差 E_rot < 25°

### 关键结果

| 算法 | Success (%) ↑ | Smoothness ↓ | Compute η_eff ↓ |
|------|---------------|--------------|-----------------|
| SBTO | 74.6 | 1.7 | 405529 — 3.3 |
| SBTO_pos | 62.1 | 2.7 | 444924 — 3.6 |
| SPIDER | 37.9 | 3.4 | 123496 — 1.0 |

### 结果分析
- SBTO 成功率比 SPIDER 高 36.7 个百分点（由表内数值 74.6→37.9 计算），平滑度提升 50%（由表内数值 1.7→3.4 计算）
- 计算成本约为 SPIDER 的三倍，但成功率和轨迹质量显著提升
- 实际精炼时间约 1 分钟每 1 秒精炼运动，在 112 核 Intel(R) Xeon(R) Platinum 8480+ CPU 上
- 案例分析（运动 sub_10_largebox_045，时长 4.6 s）显示物体位置误差在约 200 次迭代中持续下降

## 边界与局限

- 计算成本约为 SPIDER 的三倍，因为每次迭代需从初始状态滚动，后期增量需大量模拟步
- 失败案例发生在参考质量差时，特别是手-物体接触突变或物体方向突然翻转
- SBTO 适用于成本函数稠密的问题，未明确扩展到其他类型问题
- 未提及对更复杂物体交互（如多物体、非刚体）或更长时域（>9 s）的验证
- 未提及对真实机器人所有任务的详细成功率或失败分析（仅提及零样本迁移成功）

## 工程启示

复现时先核对三个关键点：一是 σ_min 的设置，这是增量时机的核心，太小会导致分布过早收缩，太大致增量过早；二是成本函数中速度项的权重（关节速度 0.01、物体线速度 0.2），SBTO_pos 省略速度项后成功率下降 12.5 个百分点（由表内数值 74.6→62.1 计算），说明速度项对动态可行性至关重要；三是 CEM 超参数中的协方差动量 α_Σ=0.2 和均值动量 α_μ=0.95，这些控制分布更新的平滑度，直接影响收敛稳定性。

最容易踩坑的地方是 MuJoCo 的 rollout 函数并行化——作者在 112 核 CPU 上实现，若单机核数不足，计算时间会显著增加。另外，节点间时间间隔固定为 0.25 s，若参考运动速度变化剧烈，可能需要自适应调整。对于下游团队，建议先用短时域（<3 s）运动验证 SBTO 的增量机制是否正常工作，再扩展到长时域任务。

## 参考
- http://arxiv.org/abs/2607.04927v1

## 개요
DSWAM은 이중 시스템 아키텍처를 통해 기존 World Action Models(WAMs)이 복잡한 다단계 가정용 작업에서 언어 수준의 계획 인터페이스가 부족한 문제를 해결합니다. System 1은 기본 제어 경로로 작동하며, 세계 인식에 기반한 동작 생성을 수행합니다. System 2는 작업 분해가 필요할 때만 활성화되어, 단기 시각적 이력과 전역 작업 프롬프트에서 실행 가능한 하위 작업을 예측합니다. 실제 배포 효율성을 높이기 위해 모델은 TensorRT 가속, 비동기 실행 및 실시간 청크(RTC) 기술을 통합하여 정책 쿼리가 로봇 제어를 차단하지 않도록 보장합니다. DeMaVLA 실제 변형 조작 설정에서 DSWAM은 VLA 정책과 동일한 플랫폼, 데이터 및 평가 기준에서 공정하게 비교되었습니다.

## 핵심 내용
### 방법
DSWAM은 이중 시스템 아키텍처를 채택합니다:
- **System 1 (WAM 실행기)**: 기본 제어 경로로 작동하며, 세계 인식에 기반한 동작 생성을 수행합니다. 훈련 시 동작 예측과 비디오 공동 훈련을 결합하고, 추론 시 명시적 미래 비디오 생성 없이 동작 청크를 직접 예측합니다.
- **System 2 (시각 언어 하위 작업 계획기)**: 작업 분해가 유익할 때만 활성화되어, 단기 시각적 이력과 전역 작업 프롬프트에서 실행 가능한 하위 작업을 예측합니다.

### 아키텍처 및 실험 설정
- **실행 경로 최적화**: TensorRT 가속, 비동기 실행 및 실시간 청크(RTC)를 통합하여 정책 쿼리가 로봇 제어를 차단하지 않도록 보장합니다.
- **공정 비교 설정**: DeMaVLA 실제 변형 조작 설정에서 로봇 플랫폼, 사전 훈련 데이터, 후속 훈련 데이터 및 평가 기준을 일치시켜 VLA 정책과 비교합니다.

### 주요 수치 및 결론
- DSWAM은 이중 시스템 설계를 통해 복잡한 다단계 가정용 작업에서 거친 명령을 세분화된 하위 작업으로 분해합니다.
- 실험은 실제 로봇 플랫폼에서 수행되었으며, WAM 실행기와 VLA 정책 간의 동일 조건에서의 성능 차이를 검증했습니다.
- 최적화된 실행 경로는 모델이 실제 로봇에서 실용성과 실시간성을 갖추도록 합니다.
