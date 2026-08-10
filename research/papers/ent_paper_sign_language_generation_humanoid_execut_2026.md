---
$id: ent_paper_sign_language_generation_humanoid_execut_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Sign Language Generation to Humanoid Execution: Vision-Language Guided Retargeting with Collision Mitigation'
  zh: 'From Sign Language Generation to Humanoid Execution: Vision-Language Guided Retargeting with Collision Mitigation'
  ko: 'From Sign Language Generation to Humanoid Execution: Vision-Language Guided Retargeting with Collision Mitigation'
summary:
  en: Recent sign language generation (SLG) systems increasingly output dense 3D body representations, which better preserve
    full-body kinematics and geometry for downstream embodiment on humanoid robots. However, these generated motions frequently
    exhibit self-intersections such as hand-hand and hand-torso penetration. While such artifacts may be tolerated in offline
    rendering, they become critical in.
  zh: 本文提出一套从手语生成（SLG）到人形机器人执行的离线重定向流程，核心是两阶段设计：先在SMPL-X域用VolumetricSMPL-X做碰撞缓解，再用IK骨干重定向并辅以GPT-5.2驱动的VLM引导细化循环。作者用CSL-Daily数据集验证了碰撞缓解的有效性，并指出VLM细化目前仅有定性证据。
  ko: Recent sign language generation (SLG) systems increasingly output dense 3D body representations, which better preserve
    full-body kinematics and geometry for downstream embodiment on humanoid robots. However, these generated motions frequently
    exhibit self-intersections such as hand-hand and hand-torso penetration. While such artifacts may be tolerated in offline
    rendering, they become critical in.
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
- sign
- language
- generation
- humanoid
- execut
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
  title: 'arXiv:2607.17769 From Sign Language Generation to Humanoid Execution: Vision-Language Guided Reta'
  url: https://arxiv.org/abs/2607.17769
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套从手语生成（SLG）到人形机器人执行的离线重定向流程，核心是两阶段设计：先在SMPL-X域用VolumetricSMPL-X做碰撞缓解，再用IK骨干重定向并辅以GPT-5.2驱动的VLM引导细化循环。作者用CSL-Daily数据集验证了碰撞缓解的有效性，并指出VLM细化目前仅有定性证据。

## 它改变了什么

手语生成领域长期忽视一个事实：生成的SMPL-X运动序列在离线渲染中看似可用，但一旦交给人形机器人执行，自交（手-手、手-躯干穿透）会直接导致IK无解、碰撞和轨迹不稳定。这不是简单的“重定向问题”——上游SLG的学习目标从未显式强制物理合理性，即使最强的重定向骨干也会继承并放大这些伪影。作者真正改变的是将“生成-执行”视为一个端到端物理可行性问题，而非在重定向阶段打补丁。

更关键的是，作者否定了预计算无碰撞手语字典的路线。手语是能产的，句子语境通过空间引用、协同发音和语法空间使用改变符号实现，字典绑定特定形态意味着每个机器人形态都要重写。同时，现有VLM引导运动细化方法依赖运动描述文本监督，而标准SL数据集只有口语语句配对手语视频，没有显式动作描述。作者因此提出依赖视觉反馈而非文本监督的VLM引导公式，这是对SLG到机器人执行研究空白的直接填补。

## 方法拆解

### 整体流程
输入为SMPL-X轴角姿态序列 x(0) ∈ ℝ^(T×132)，输出人形机器人关节轨迹 q_(1:T)，需同时满足机器人运动学/几何约束和保留手语交际意图。两阶段分离是有意设计：碰撞缓解处理SLG继承的系统性物理失效，VLM细化针对形态差异和IK近似引入的残余误差。

### 阶段一：SMPL-X域碰撞缓解
- 使用VolumetricSMPL-X提供可微分SDF查询，自碰撞损失：
  ℒ_col(x) = (1/T) Σ_t Σ_{v∈V_t} max(0, −f(v; x_t))²
  其中f(·; x_t)为姿态帧t下的SDF，V_t为表面采样点，负距离对应穿透，损失随穿透深度二次增长。
- 测试时后处理：Adam优化，学习率 1 × 10⁻²，500步，默认优化手部姿态参数。
- 掩码更新：x_eff = x^(0) + M ⊙ (x − x^(0))，M ∈ {0,1}^(T×132) 防止全局漂移。
- 总目标：min_x λ_col ℒ_col(x_eff) + λ_close ‖x_eff − x^(0)‖₂² + λ_smooth ‖Δ²x_eff‖₂²，其中Δ²x_t = x_(t+1) − 2x_t + x_(t−1)，默认λ_col = 50，λ_close = 1 × 10⁻⁴，λ_smooth = 1 × 10⁻⁴。

### 阶段二：形状对齐与IK重定向
- 形状优化：用T-pose对应关系将SMPL-X模板对齐到机器人运动学结构，优化β最小化 ℒ_shape(β) = Σ_k w_k ‖J^smplx_k(β) − J^rob_k‖₂² + λ_β‖β‖₂²，w_k可强调手语相关上肢关节。
- 逐帧IK：给定对齐后手腕位置和方向目标，求解满足关节限制的机器人关节轨迹，并额外执行机器人几何碰撞检查。

### 阶段三：VLM引导细化循环
- 每轮渲染原始SMPL-X参考视频和IK重定向机器人视频，交给GPT-5.2比较并提出修正。
- 控制原语设计：直接编辑关节角无效，改为末端执行器任务空间原语，如move_left_up（左腕+y方向+10 cm）、left_yaw_in（左腕偏航向内+20°）等，输出为JSON类结构化动作列表。
- 迭代过程：应用任务空间偏移→重新IK→渲染新视频→VLM再评估，重复直至确认对齐或达最大轮数（所有实验执行两次细化迭代）。

## 关键创新

1. **视觉反馈替代文本监督的VLM引导**：现有VLM运动细化方法假设可访问运动描述文本，而标准SL数据集只有口语语句配对手语视频。作者直接让VLM比较两段渲染视频并提出任务空间原语，绕开了文本监督的稀缺瓶颈，这是对SLG到机器人执行场景的适配性创新。

2. **任务空间控制原语作为VLM与IK之间的接口**：直接让VLM编辑关节角在感知上不可行，作者定义在手腕任务空间的小型原语集（位置10 cm、偏航20°），使VLM能提出可解释调整而IK求解器保持可行性。这个设计决策将VLM的高层语义判断与底层运动学约束解耦，是工程上务实且可扩展的架构选择。

3. **碰撞缓解与VLM细化的两阶段分离**：碰撞缓解解决SLG继承的系统性物理失效模式（手-手、手-躯干穿透），VLM细化针对形态差异和IK近似引入的残余语义/几何差异。分离使每个模块的优化目标清晰，且碰撞缓解作为轻量级后处理可独立复用。

## 实验与结果

### 数据集与配置
- CSL-Daily：18K训练、1K验证、2K测试，使用[33]发布的预处理SMPL-X运动特征（6D旋转和10个形状参数）。
- 碰撞缓解：Adam优化，学习率 1 × 10⁻²，500步，默认优化手部姿态参数。
- VLM：GPT-5.2，固定批评提示，所有实验执行两次细化迭代。

### 表I：碰撞缓解结果（较低更好）
| 指标 | Before | After |
|---|---|---|
| 碰撞能量（均值） | 3.52 | 0.94 |
| 碰撞能量（中位数） | 0.82 | 0.71 |
| 改进序列（%） | — | 88.9% |
| 碰撞减少（中位数） | — | 21.66% |
| 碰撞减少（均值） | — | 31.93% |
| Pose MSE vs. 原始（中位数） | — | 6.80 × 10⁻⁴ |
| Δ Accel MSE（中位数） | — | +5.71 × 10⁻³ |
| 每序列运行时间（均值） | — | 521.7 s |

### 表II：正则化项消融
| 配置 | N | Succ. (%) | Red. (%) | Pose MSE | Δ Accel MSE | Time (s) |
|---|---|---|---|---|---|---|
| Collision only | 8 | 62.5 | 18.98 | 6.05 × 10⁻⁴ | +4.47 × 10⁻³ | 324.7 |
| + Closeness | 9 | 88.9 | 21.66 | 6.80 × 10⁻⁴ | +5.71 × 10⁻³ | 521.7 |
| + Closeness + Smoothness | 10 | 60.0 | 24.40 | 5.08 × 10⁻⁴ | +2.59 × 10⁻³ | 362.2 |

### 结果含义
碰撞缓解显著降低均值碰撞能量（3.52→0.94，由表内数值计算），但中位数改善有限（0.82→0.71），说明主要收益集中在高碰撞序列。消融显示+Closeness提升成功率至88.9%但增加运行时间，+Smoothness降低Pose MSE和Δ Accel MSE但牺牲成功率至60.0%，表明平滑正则化可能过度抑制手部运动。VLM细化仅有定性证据，论文未明确量化其相对IK-only基线的收益。

## 边界与局限

- VLM引导细化的证据目前是定性的，限于代表性序列，未进行定量评估（如末端执行器轨迹误差或手腕方向误差）。
- 碰撞缓解运行时间高（表I，均值521.7 s/序列），不适合在线处理；全流程设计为离线预处理，交互时机器人执行预计算轨迹。
- 未在物理人形平台上验证，结论基于仿真渲染。
- 未进行控制原语词汇粒度和步长的系统敏感性研究；步长权衡收敛速度与过冲，较粗步长可能围绕目标振荡，较细步长需更多VLM查询。
- 控制原语覆盖范围有限：表达编辑空间之外的失效模式（如躯干倾斜或时序错误）完全无法修正。
- 未实现在线细化（如通过学习批评者近似），论文未明确。

## 工程启示

复现时先核对碰撞缓解的掩码设计：默认只优化手部姿态参数，M ∈ {0,1}^(T×132) 的构造直接影响全局漂移抑制效果，建议先验证掩码是否覆盖所有需要修正的关节维度。运行时间521.7 s/序列是主要瓶颈，若需批量处理，优先考虑减少Adam步数或改用L-BFGS类二阶优化器。

VLM细化环节最容易踩坑的是控制原语步长选择：位置10 cm、偏航20°在仿真中可能合适，但不同机器人形态的连杆长度差异会放大或缩小实际效果。建议先做一次步长敏感性测试，确认VLM提出的偏移在IK重解后不会导致关节限位冲突。另外，GPT-5.2的批评提示词质量直接影响细化效果，固定提示模板在不同序列上的泛化性需要人工抽检。

对下游团队，最实用的建议是：碰撞缓解模块可独立复用为任何SLG输出的后处理，不必绑定本流程的IK和VLM部分。若你的机器人形态与SMPL-X差异较大，形状优化中的关节权重w_k需要针对手语相关上肢关节重新标定，否则IK目标可能失真。最后，VLM细化的定性证据意味着在正式部署前，务必用你自己的序列集做一次人工评估，确认细化不会引入新的语义偏差。

## Overview
Recent sign language generation (SLG) systems increasingly output dense 3D body representations, which better preserve full-body kinematics and geometry for downstream embodiment on humanoid robots. However, these generated motions frequently exhibit self-intersections such as hand-hand and hand-torso penetration. While such artifacts may be tolerated in offline rendering, they become critical in humanoid execution as they lead to infeasible inverse-kinematics (IK) solutions, collisions, and unstable retargeted trajectories. We present a system-level framework that bridges SLG outputs to humanoid joint-space execution via two components. First, we introduce a volumetric SMPL-X collision-mitigation module that projects generated signing motions toward physically plausible configurations while minimally deviating from the original trajectory. Second, we propose a vision-language-guided retargeting algorithm built on an IK backbone: a VLM serves as a visual critic over rendered humanoid motion, identifies embodiment-specific failure modes, and triggers targeted task-space corrections. Our results highlight collision handling and perception-guided refinement as key missing components for reliable humanoid signing.

## 参考
- https://arxiv.org/abs/2607.17769

## 개요

본 논문은 수어 생성(SLG)에서 휴머노이드 로봇 실행까지의 오프라인 리타겟팅 파이프라인을 제안하며, 핵심은 2단계 설계입니다: 먼저 SMPL-X 도메인에서 VolumetricSMPL-X를 사용한 충돌 완화를 수행하고, 이후 IK 백본 리타겟팅과 GPT-5.2 기반 VLM 유도 세분화 루프를 결합합니다. 저자들은 CSL-Daily 데이터셋으로 충돌 완화의 효과를 검증했으며, VLM 세분화는 현재 정성적 증거만 있다고 지적합니다.

## 무엇을 바꾸었는가

수어 생성 분야는 오랫동안 한 가지 사실을 간과해 왔습니다: 생성된 SMPL-X 모션 시퀀스는 오프라인 렌더링에서 사용 가능해 보이지만, 휴머노이드 로봇에 전달되면 자기 충돌(손-손, 손-몸통 관통)이 IK 무해, 충돌, 궤적 불안정을 직접 초래합니다. 이는 단순한 "리타겟팅 문제"가 아닙니다—상류 SLG의 학습 목표는 물리적 타당성을 명시적으로 강제한 적이 없으며, 가장 강력한 리타겟팅 백본조차 이러한 인공물을 계승하고 증폭시킵니다. 저자들이 진정으로 바꾼 것은 "생성-실행"을 엔드투엔드 물리적 실현 가능성 문제로 간주한 것이지, 리타겟팅 단계에서 패치를 적용한 것이 아닙니다.

더 중요하게, 저자들은 사전 계산된 무충돌 수어 사전 접근법을 부정합니다. 수어는 생산적이며, 문장 맥락은 공간 참조, 조음 협응, 문법적 공간 사용을 통해 기호 구현을 변경합니다. 사전이 특정 형태에 묶이면 모든 로봇 형태마다 재작성해야 합니다. 동시에, 기존 VLM 유도 모션 세분화 방법은 모션 설명 텍스트 감독에 의존하지만, 표준 SL 데이터셋은 구어 문장과 수어 비디오만 짝지어 제공할 뿐 명시적 동작 설명이 없습니다. 따라서 저자들은 텍스트 감독이 아닌 시각적 피드백에 의존하는 VLM 유도 공식을 제안하며, 이는 SLG에서 로봇 실행까지의 연구 공백을 직접 메우는 것입니다.

## 방법 분해

### 전체 흐름
입력은 SMPL-X 축각 자세 시퀀스 x(0) ∈ ℝ^(T×132)이고, 출력은 휴머노이드 로봇 관절 궤적 q_(1:T)로, 로봇 운동학/기하학적 제약과 수어 의사소통 의도 보존을 동시에 충족해야 합니다. 2단계 분리는 의도된 설계입니다: 충돌 완화는 SLG가 계승한 체계적 물리적 실패를 처리하고, VLM 세분화는 형태 차이와 IK 근사로 도입된 잔여 오류를 대상으로 합니다.

### 1단계: SMPL-X 도메인 충돌 완화
- VolumetricSMPL-X를 사용한 미분 가능한 SDF 쿼리, 자기 충돌 손실:
  ℒ_col(x) = (1/T) Σ_t Σ_{v∈V_t} max(0, −f(v; x_t))²
  여기서 f(·; x_t)는 자세 프레임 t에서의 SDF, V_t는 표면 샘플 포인트, 음의 거리는 관통에 해당하며 손실은 관통 깊이에 따라 2차적으로 증가합니다.
- 테스트 시 후처리: Adam 최적화, 학습률 1 × 10⁻², 500스텝, 기본적으로 손 자세 매개변수 최적화.
- 마스크 업데이트: x_eff = x^(0) + M ⊙ (x − x^(0)), M ∈ {0,1}^(T×132)로 전역 드리프트 방지.
- 총 목표: min_x λ_col ℒ_col(x_eff) + λ_close ‖x_eff − x^(0)‖₂² + λ_smooth ‖Δ²x_eff‖₂², 여기서 Δ²x_t = x_(t+1) − 2x_t + x_(t−1), 기본 λ_col = 50, λ_close = 1 × 10⁻⁴, λ_smooth = 1 × 10⁻⁴.

### 2단계: 형태 정렬 및 IK 리타겟팅
- 형태 최적화: T-포즈 대응 관계로 SMPL-X 템플릿을 로봇 운동학 구조에 정렬하고, β를 최적화하여 ℒ_shape(β) = Σ_k w_k ‖J^smplx_k(β) − J^rob_k‖₂² + λ_β‖β‖₂² 최소화, w_k로 수어 관련 상지 관절 강조 가능.
- 프레임별 IK: 정렬된 손목 위치와 방향 목표가 주어지면 관절 제한을 충족하는 로봇 관절 궤적을 풀고, 추가로 로봇 기하학적 충돌 검사를 수행.

### 3단계: VLM 유도 세분화 루프
- 각 라운드에서 원본 SMPL-X 참조 비디오와 IK 리타겟팅 로봇 비디오를 렌더링하여 GPT-5.2에 비교 및 수정 제안 요청.
- 제어 프리미티브 설계: 관절 각도 직접 편집은 비효율적이므로, 엔드 이펙터 작업 공간 프리미티브로 대체—예: move_left_up(왼쪽 손목 +y 방향 +10 cm), left_yaw_in(왼쪽 손목 요 안쪽 +20°) 등—출력은 JSON 유사 구조화 동작 목록.
- 반복 과정: 작업 공간 오프셋 적용 → IK 재해석 → 새 비디오 렌더링 → VLM 재평가, 정렬 확인 또는 최대 라운드 도달까지 반복(모든 실험에서 두 번의 세분화 반복 수행).

## 핵심 혁신

1. **텍스트 감독 대신 시각적 피드백을 사용하는 VLM 유도**: 기존 VLM 모션 세분화 방법은 모션 설명 텍스트 접근성을 가정하지만, 표준 SL 데이터셋은 구어 문장과 수어 비디오만 짝지어 제공합니다. 저자들은 VLM이 두 렌더링 비디오를 직접 비교하고 작업 공간 프리미티브를 제안하도록 하여 텍스트 감독의 희소성 병목을 우회했으며, 이는 SLG에서 로봇 실행 시나리오에 대한 적응형 혁신입니다.

2. **VLM과 IK 사이의 인터페이스로서 작업 공간 제어 프리미티브**: VLM이 관절 각도를 직접 편집하는 것은 지각적으로 불가능하므로, 저자들은 손목 작업 공간의 소형 프리미티브 집합(위치 10 cm, 요 20°)을 정의하여 VLM이 해석 가능한 조정을 제안하면서 IK 솔버의 실현 가능성을 유지합니다. 이 설계 결정은 VLM의 고수준 의미 판단과 저수준 운동학 제약을 분리하며, 공학적으로 실용적이고 확장 가능한 아키텍처 선택입니다.

3. **충돌 완화와 VLM 세분화의 2단계 분리**: 충돌 완화는 SLG가 계승한 체계적 물리적 실패 모드(손-손, 손-몸통 관통)를 해결하고, VLM 세분화는 형태 차이와 IK 근사로 도입된 잔여 의미/기하학적 차이를 대상으로 합니다. 분리를 통해 각 모듈의 최적화 목표가 명확해지고, 충돌 완화는 경량 후처리로 독립적으로 재사용 가능합니다.

## 실험 및 결과

### 데이터셋 및 설정
- CSL-Daily: 18K 훈련, 1K 검증, 2K 테스트, [33]에서 공개한 전처리된 SMPL-X 모션 특징(6D 회전 및 10개 형태 매개변수) 사용.
- 충돌 완화: Adam 최적화, 학습률 1 × 10⁻², 500스텝, 기본적으로 손 자세 매개변수 최적화.
- VLM: GPT-5.2, 고정 비평 프롬프트, 모든 실험에서 두 번의 세분화 반복 수행.

### 표 I: 충돌 완화 결과(낮을수록 좋음)
| 지표 | Before | After |
|---|---|---|
| 충돌 에너지(평균) | 3.52 | 0.94 |
| 충돌 에너지(중앙값) | 0.82 | 0.71 |
| 개선 시퀀스(%) | — | 88.9% |
| 충돌 감소(중앙값) | — | 21.66% |
| 충돌 감소(평균) | — | 31.93% |
| Pose MSE vs. 원본(중앙값) | — | 6.80 × 10⁻⁴ |
| Δ Accel MSE(중앙값) | — | +5.71 × 10⁻³ |
| 시퀀스당 실행 시간(평균) | — | 521.7 s |

### 표 II: 정규화 항 소거 실험
| 설정 | N | Succ. (%) | Red. (%) | Pose MSE | Δ Accel MSE | Time (s) |
|---|---|---|---|---|---|---|
| Collision only | 8 | 62.5 | 18.98 | 6.05 × 10⁻⁴ | +4.47 × 10⁻³ | 324.7 |
| + Closeness | 9 | 88.9 | 21.66 | 6.80 × 10⁻⁴ | +5.71 × 10⁻³ | 521.7 |
| + Closeness + Smoothness | 10 | 60.0 | 24.40 | 5.08 × 10⁻⁴ | +2.59 × 10⁻³ | 362.2 |

### 결과 의미
충돌 완화는 평균 충돌 에너지를 크게 감소시키지만(3.52→0.94, 표 내 수치로 계산), 중앙값 개선은 제한적(0.82→0.71)으로, 주요 이점이 고충돌 시퀀스에 집중되어 있음을 시사합니다. 소거 실험은 +Closeness가 성공률을 88.9%로 높이지만 실행 시간을 증가시키고, +Smoothness는 Pose MSE와 Δ Accel MSE를 낮추지만 성공률을 60.0%로 희생시켜, 평활화 정규화가 손 움직임을 과도하게 억제할 수 있음을 보여줍니다. VLM 세분화는 정성적 증거만 있으며, 논문은 IK 단독 기준선 대비 이점을 명시적으로 정량화하지 않았습니다.

## 경계 및 한계

- VLM 유도 세분화의 증거는 현재 정성적이며 대표 시퀀스에 국한되어 있고, 정량적 평가(엔드 이펙터 궤적 오류 또는 손목 방향 오류)는 수행되지 않았습니다.
- 충돌 완화 실행 시간이 높아(표 I, 평균 521.7 s/시퀀스) 온라인 처리에 부적합하며, 전체 흐름은 오프라인 전처리로 설계되어 상호작용 시 로봇은 사전 계산된 궤적을 실행합니다.
- 물리적 휴머노이드 플랫폼에서 검증되지 않았으며, 결론은 시뮬레이션 렌더링에 기반합니다.
- 제어 프리미티브 어휘 세분성과 스텝 크기에 대한 체계적 민감도 연구가 수행되지 않았습니다; 스텝 크기는 수렴 속도와 오버슈트를 절충하며, 더 거친 스텝은 목표 주변에서 진동할 수 있고 더 미세한 스텝은 더 많은 VLM 쿼리가 필요합니다.
- 제어 프리미티브 범위가 제한적입니다: 표현 편집 공간 밖의 실패 모드(예: 몸통 기울기 또는 타이밍 오류)는 전혀 수정할 수 없습니다.
- 온라인 세분화(예: 학습된 비평가 근사)는 구현되지 않았으며, 논문에서 명시하지 않았습니다.

## 공학적 시사점

재현 시 먼저 충돌 완화의 마스크 설계를 확인하세요: 기본적으로 손 자세 매개변수만 최적화하며, M ∈ {0,1}^(T×132)의 구성은 전역 드리프트 억제 효과에 직접 영향을 미치므로, 마스크가 수정해야 할 모든 관절 차원을 포함하는지 먼저 검증하는 것이 좋습니다. 실행 시간 521.7 s/시퀀스가 주요 병목이므로, 배치 처리가 필요하면 Adam 스텝 수를 줄이거나 L-BFGS 계열 2차 최적화기로 전환하는 것을 우선 고려하세요.

VLM 세분화 단계에서 가장 쉽게 함정에 빠지는 부분은 제어 프리미티브 스텝 크기 선택입니다: 위치 10 cm, 요 20°는 시뮬레이션에서 적합할 수 있지만, 로봇 형태별 링크 길이 차이가 실제 효과를 증폭하거나 축소할 수 있습니다. 먼저 스텝 크기 민감도 테스트를 수행하여 VLM이 제안한 오프셋이 IK 재해석 후 관절 한계 충돌을 유발하지 않는지 확인하는 것이 좋습니다. 또한 GPT-5.2의 비평 프롬프트 품질은 세분화 효과에 직접 영향을 미치며, 고정 프롬프트 템플릿의 다양한 시퀀스에 대한 일반화는 수동 샘플링 검사가 필요합니다.

하류 팀에게 가장 실용적인 조언은: 충돌 완화 모듈은 본 흐름의 IK 및 VLM 부분에 얽매이지 않고 모든 SLG 출력의 후처리로 독립적으로 재사용할 수 있다는 점입니다. 로봇 형태가 SMPL-X와 크게 다르면, 형태 최적화의 관절 가중치 w_k를 수어 관련 상지 관절에 맞게 재보정해야 하며, 그렇지 않으면 IK 목표가 왜곡될 수 있습니다. 마지막으로, VLM 세분화의 정성적 증거는 공식 배포 전에 자체 시퀀스 집합으로 수동 평가를 반드시 수행하여 세분화가 새로운 의미 편향을 도입하지 않는지 확인해야 함을 의미합니다.
