---
$id: ent_paper_actfovea_runtime_safeguarding_vla_polici_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency'
  zh: 'ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency'
  ko: 'ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency'
summary:
  en: Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime
    disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce
    ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying
    the underlying VLA policy..
  zh: ActFovea 是一个面向视觉-语言-动作（VLA）策略的即插即用运行时防护框架，由研究团队提出，核心贡献在于通过动作条件化注视、时空一致性监控与确定性路由，在不重训练底层策略的前提下统一处理动作漂移、视觉延迟、局部覆盖与观测重放四类扰动。其核心原则是视觉观测、本体感受转变与候选动作应共同描述机器人与环境的连贯物理演化。
  ko: Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime
    disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce
    ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying
    the underlying VLA policy..
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
- actfovea
- runtime
- safeguarding
- vla
- polici
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.29169 ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action'
  url: https://arxiv.org/abs/2607.29169
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---

## 概述

ActFovea 是一个面向视觉-语言-动作（VLA）策略的即插即用运行时防护框架，由研究团队提出，核心贡献在于通过动作条件化注视、时空一致性监控与确定性路由，在不重训练底层策略的前提下统一处理动作漂移、视觉延迟、局部覆盖与观测重放四类扰动。其核心原则是视觉观测、本体感受转变与候选动作应共同描述机器人与环境的连贯物理演化。

## 它改变了什么

现有 VLA 安全防护的痛点在于“头痛医头”：控制屏障层只针对动力学约束，观测干预只处理单一扰动族，且大多施加预定保守约束而非根据证据动态决策。ActFovea 真正改变的是将运行时防护从“检测-拒绝”范式升级为“检测-分诊-恢复”范式——它不再问“这个观测是否被破坏”，而是问“这个破坏是否仍存在合理的物理恢复路径”。这一转变使系统能够在动作漂移时保持 90.1% 的成功率（由表内 83.1%→90.1% 计算），而在视觉覆盖时获得 41.0 个百分点的绝对增益，同时避免均匀保守响应抑制有效行为。

另一个关键改变是它把“时间”维度纳入视觉-动作一致性检查。现有方法要么完全忽略时间戳健康性，要么仅做简单的“过旧则保持”（Timestamp-Only Hold 在延迟场景下成功率降至 0.0%）。ActFovea 通过多视角滞后估计、缺失局部运动检测与全局重放相似性，将时间错位从“二元判定”变为“可恢复性分级”，从而在视觉延迟下维持 86.0% 的成功率，而基线仅 76.2%。

## 方法拆解

### 动作条件化注视（Action-Conditioned Foveation）
利用机器人运动学与近期动作构建保留掩码：
- 投影接触中心圆盘 M_{c,t}^v（半径 r_c）与投影折线走廊 M_{Γ,t}^v（半径 r_Γ）取并集后膨胀（半径 r_m），得到 M_t^v = Dilate(M_{c,t}^v ∨ M_{Γ,t}^v, r_m)
- 图像滤波：Ĩ_t^v = (1 − α B̄_t^v) ⊙ I_t^v + α B̄_t^v ⊙ E(I_t^v)，其中 E 为背景归一化、高斯平滑与颜色-灰度混合，α 为有界编辑强度
- 设计理由：保留接触相关区域与预测运动走廊，抑制任务无关视觉内容，避免扰动注入点被“注视”放大

### 一致性监控与风险聚合
- 几何一致性：观测中心与投影接触中心距离
- 动态一致性：预测与观测图像位移的方向和幅度
- 时间证据：时间戳健康、缺失局部运动、滞后估计、全局重放相似性
- 加权风险：R_t = clip(β r̄_t + (1−β) r_t + p_t^cam + p_t^lag + p_t^cal, 0, 1)，β 与组件权重为固定实现常数，低置信度估计收缩至 0.5

### 确定性路由器与恢复路径
- 根据证据推断扰动类型：直接滞后→时间延迟；动态/本体感受不一致→动作漂移；强陈旧/重放证据且闩锁激活→不可恢复冻结
- 可恢复扰动构建候选观测库：原始观测、注视观测、时间稳定化候选（有限视觉滞后）、空间恢复算子（局部覆盖）
- 空间恢复：X̂_t^v = clip((P_t^v − α̂_t^v Q̂_t^v)/(1 − α̂_t^v), 0, 255)，基于最后干净参考与当前图像的中值稠密光流对齐；仅当所有检测视图均重建且最弱视图质量通过准入阈值时才接受修复

### 动作验证与执行仲裁
- 验证分数 V_k = clip(w^T u_k + b_k, 0, 1)，w 为固定非负权重，b_k 为威胁条件奖励；排除最终夹爪维度，测量首动作方向、端点方向、运动幅度、平滑度、视界和块漂移
- 两阶段仲裁：监控器产生 λ_t^mon 和 h_t^mon，验证器产生 λ_t^ver 和 h_t^ver；最终动作 â_{t,i}^mot = λ_t^mon λ_t^ver a_{t,i}^{⋆,mot}（i < h_t），h_t = min(h_t^mon, h_t^ver)
- 安全失败：观测持续陈旧或重放时禁用恢复并调用有界运动抑制；保持闩锁在强重放证据或可配置陈旧连续后激活，在足够新鲜证据后释放

## 关键创新

1. **动作条件化注视作为统一预处理**：不同于现有方法对整幅图像做鲁棒化或直接丢弃，ActFovea 利用机器人运动学预测“哪些像素区域与当前动作物理相关”，从而在保留任务关键信息的同时抑制扰动注入点。这是首次将动作意图显式编码进视觉防护的预处理阶段，且不依赖分割标注或对象状态。

2. **可恢复性分诊而非二元拒绝**：路由器根据证据强度区分“可恢复扰动”（动作漂移、视觉延迟、局部覆盖）与“不可恢复状态”（冻结重放），并分别触发恢复候选库或安全失败。这一设计避免了“所有异常都尝试恢复”导致失控延长（无 Hold/Safe-Fail 时控制器在检测后继续 259.2 个动作），也避免了“所有异常都保守抑制”导致有效行为被阻断。

3. **时空一致性作为统一检测信号**：将几何一致性（空间）、动态一致性（时间-空间耦合）与时间证据（纯时间）融合为加权风险，使系统能区分“观测被局部覆盖但时间健康”与“观测被重放但空间看似合理”等细微差异。这在表 4 中体现为 w/o Threat Typing 在视觉覆盖下增益降至 −7.6，而完整模型达 +41.0。

## 实验与结果

实验在 LIBERO 基准上使用冻结 π_0 检查点，四个十任务套件各 2,000 个片段，覆盖四类扰动。

| 场景 | 指标 | Base VLA | ActFovea | 增益 |
|------|------|----------|----------|------|
| Action Drift | Disturbed SR | 83.1% | 90.1% | +7.0 |
| Visual Delay | Disturbed SR | 76.2% | 86.0% | +9.8 |
| Visual Overlay | Disturbed SR | 49.3% | 90.3% | +41.0 |
| Frozen Replay | Timely Safe Failure | 0.00% | 100.00% | — |

表 2 对比训练无关运行时方法：ActFovea 在视觉覆盖下 90.3% 远超 Action Clip/Smoothing 的 30.9% 与 Fixed Short Horizon 的 32.4%；在视觉延迟下 86.0% 远超 Timestamp-Only Hold 的 0.0%。表 3 显示完整执行器在冻结重放下实现 100% 及时安全失败，检测后仅执行 2.0 个有界动作步骤，累积运动范数 0.326，无动作界违规；而无 Hold/Safe-Fail 时控制器继续 259.2 个动作，累积运动 241.98（由表内数值计算，检测后动作数减少 99.23%，累积运动减少 99.87%）。

表 4 消融显示：w/o Recovery Bank 在视觉覆盖下增益降至 −33.3，w/o Candidate Expansion 降至 −31.7，w/o Action Verification 在动作漂移下增益为 −1.2，证明恢复候选库、候选扩展与动作验证均不可或缺。

## 边界与局限

- 正式碰撞避免保证不在机制范围内，安全失败仅表示保守运动抑制，不提供物理安全性证明。
- 扰动在接口之后引入（即已进入策略内部或执行器层）的情况不在威胁模型内。
- 未进行重训练或参数优化，底层 VLA 策略保持冻结；所有选择规则在推理时固定，不添加训练目标。
- 未提供奖励信号、模拟器对象状态、分割标注或扰动类型先验；投影不可用时依赖恒速笛卡尔外推或先前跟踪中心加图像平面方向推断，极端运动下可能失效。
- 论文未明确硬件平台细节与推理延迟开销。

## 工程启示

复现时先核对三处：一是动作条件化注视的掩码构建——投影不可用时的外推策略直接影响覆盖场景下的恢复质量，建议优先验证恒速外推在快速旋转下的稳定性；二是风险聚合中 β 与组件权重的固定常数——论文未给出具体值，需自行标定，低置信度收缩至 0.5 的行为对延迟场景影响显著；三是空间恢复的准入阈值——仅当所有检测视图均重建且最弱视图质量通过阈值时才接受修复，阈值过严会退化为 w/o Recovery Bank（视觉覆盖增益 −33.3），过松则引入错误修复。

最容易踩坑的是 Timestamp-Only Hold 的“假安全”：它在冻结重放查询中 96.55% 时间保持，但从未转换为终端安全失败，导致任务卡死而非及时失败。ActFovea 的保持闩锁必须在强重放证据或可配置陈旧连续后激活，并在足够新鲜证据后释放——实现时需确保闩锁释放条件与重放检测解耦，否则会复现 0.0% 及时安全失败的失败模式。下游团队集成时，建议先以视觉覆盖场景验证恢复候选库的准入逻辑，再逐步开放动作验证的权重向量。

## Overview
Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying the underlying VLA policy. ActFovea uses robot kinematics, proprioceptive states, and recent actions to construct action-conditioned foveated regions that retain contact-relevant areas and predicted motion corridors while suppressing task-irrelevant visual content. It detects runtime risks by evaluating whether visual motion and observation freshness remain consistent with geometric, proprioceptive, and action transitions. For recoverable disturbances, ActFovea constructs disturbance-specific candidate observations and accepts a recovery only after verifying the resulting action chunk. When stale or replayed observations make reliable recovery impossible, it invokes a bounded safe-failure procedure. In closed-loop evaluations of $π_0$ across multiple LIBERO suites, ActFovea increases success under localized visual overlays from 49.3\% to 90.3\%, closing 93.7\% of the gap to clean performance. It further improves success under action drift and visual delay by 7.0 and 9.8 percentage points, respectively, while preserving clean-task performance. Under frozen-observation replay, ActFovea triggers timely safe failure in all trials, with no unprotected failures. These results demonstrate that spatiotemporal visual-action consistency provides an effective basis for runtime safeguarding of VLA policies.

## 参考
- https://arxiv.org/abs/2607.29169

## 개요

ActFovea는 비전-언어-행동(VLA) 정책을 위한 플러그 앤 플레이 런타임 보호 프레임워크로, 연구팀에 의해 제안되었습니다. 핵심 기여는 행동 조건화 주시(액션 컨디셔닝 포비에이션), 시공간 일관성 모니터링, 결정적 라우팅을 통해 기본 정책을 재훈련하지 않으면서 행동 드리프트, 시각적 지연, 국소적 덮개, 관측 재생의 네 가지 교란을 통합적으로 처리하는 데 있습니다. 핵심 원칙은 시각적 관측, 고유수용감각 변화, 후보 행동이 로봇과 환경의 일관된 물리적 진화를 함께 설명해야 한다는 것입니다.

## 무엇을 바꾸는가

기존 VLA 안전 보호의痛点은 "머리 아프면 머리 약" 식입니다: 제어 장벽 계층은 동역학 제약만 다루고, 관측 개입은 단일 교란 계열만 처리하며, 대부분 사전에 결정된 보수적 제약을 적용할 뿐 증거에 기반한 동적 의사결정을 하지 않습니다. ActFovea가 진정으로 바꾸는 것은 런타임 보호를 "탐지-거부" 패러다임에서 "탐지-분류-복구" 패러다임으로 업그레이드한다는 점입니다—더 이상 "이 관측이 손상되었는가"를 묻지 않고 "이 손상에 여전히 합리적인 물리적 복구 경로가 존재하는가"를 묻습니다. 이러한 전환을 통해 시스템은 행동 드리프트 시 90.1%의 성공률을 유지하고(표 내 83.1%→90.1% 계산), 시각적 덮개 시 41.0퍼센트 포인트의 절대적 이득을 얻으며, 균일한 보수적 대응이 유효 행동을 억제하는 것을 피합니다.

또 다른 핵심 변화는 "시간" 차원을 시각-행동 일관성 검사에 통합한 것입니다. 기존 방법은 타임스탬프 건강성을 완전히 무시하거나 단순히 "너무 오래되면 유지"만 수행합니다(Timestamp-Only Hold는 지연 시나리오에서 성공률이 0.0%로 하락). ActFovea는 다중 시점 지연 추정, 누락된 국소 운동 감지, 전역 재생 유사성을 통해 시간적 불일치를 "이진 판정"에서 "복구 가능성 등급화"로 전환하여, 시각적 지연 하에서 86.0%의 성공률을 유지하는 반면 기준선은 76.2%에 불과합니다.

## 방법 분해

### 행동 조건화 주시(Action-Conditioned Foveation)
로봇 운동학과 최근 행동을 활용하여 보존 마스크를 구축합니다:
- 접촉 중심 원판 M_{c,t}^v(반경 r_c)와 투영 폴리라인 회랑 M_{Γ,t}^v(반경 r_Γ)의 합집합을 팽창(반경 r_m)하여 M_t^v = Dilate(M_{c,t}^v ∨ M_{Γ,t}^v, r_m)을 얻습니다.
- 이미지 필터링: Ĩ_t^v = (1 − α B̄_t^v) ⊙ I_t^v + α B̄_t^v ⊙ E(I_t^v), 여기서 E는 배경 정규화, 가우시안 평활화, 색-그레이 혼합이며, α는 유계 편집 강도입니다.
- 설계 근거: 접촉 관련 영역과 예측 운동 회랑을 보존하고, 작업 무관 시각 콘텐츠를 억제하여 교란 주입 지점이 "주시"에 의해 증폭되는 것을 방지합니다.

### 일관성 모니터링 및 위험 집계
- 기하 일관성: 관측 중심과 투영 접촉 중심 간 거리
- 동역학 일관성: 예측 및 관측 이미지 변위의 방향과 크기
- 시간 증거: 타임스탬프 건강성, 누락된 국소 운동, 지연 추정, 전역 재생 유사성
- 가중 위험: R_t = clip(β r̄_t + (1−β) r_t + p_t^cam + p_t^lag + p_t^cal, 0, 1), β와 구성 요소 가중치는 고정 구현 상수이며, 낮은 신뢰도 추정은 0.5로 수축됩니다.

### 결정적 라우터 및 복구 경로
- 증거에 따라 교란 유형 추론: 직접 지연→시간 지연; 동역학/고유수용감각 불일치→행동 드리프트; 강한 오래됨/재생 증거 및 래치 활성화→복구 불가 동결
- 복구 가능 교란에 대한 후보 관측 라이브러리 구축: 원본 관측, 주시 관측, 시간 안정화 후보(유한 시각적 지연), 공간 복구 연산자(국소 덮개)
- 공간 복구: X̂_t^v = clip((P_t^v − α̂_t^v Q̂_t^v)/(1 − α̂_t^v), 0, 255), 마지막 깨끗한 참조와 현재 이미지의 중간 밀집 광류 정렬 기반; 모든 감지 뷰가 재구성되고 가장 약한 뷰 품질이 허용 임계값을 통과할 때만 복구를 수락합니다.

### 행동 검증 및 실행 중재
- 검증 점수 V_k = clip(w^T u_k + b_k, 0, 1), w는 고정 비음수 가중치, b_k는 위협 조건 보상; 최종 그리퍼 차원을 제외하고 첫 행동 방향, 끝점 방향, 운동 크기, 평활도, 시야, 블록 드리프트를 측정합니다.
- 2단계 중재: 모니터가 λ_t^mon 및 h_t^mon을 생성하고, 검증기가 λ_t^ver 및 h_t^ver을 생성; 최종 행동 â_{t,i}^mot = λ_t^mon λ_t^ver a_{t,i}^{⋆,mot}(i < h_t), h_t = min(h_t^mon, h_t^ver)
- 안전 실패: 관측이 지속적으로 오래되었거나 재생될 때 복구를 비활성화하고 유계 운동 억제를 호출; 강한 재생 증거 또는 구성 가능한 오래됨 연속 후에 유지 래치가 활성화되고, 충분히 새로운 증거 후에 해제됩니다.

## 핵심 혁신

1. **행동 조건화 주시를 통합 전처리로 사용**: 기존 방법이 전체 이미지를 강건화하거나 직접 폐기하는 것과 달리, ActFovea는 로봇 운동학을 활용하여 "어떤 픽셀 영역이 현재 행동과 물리적으로 관련되는지"를 예측함으로써 작업 핵심 정보를 보존하면서 교란 주입 지점을 억제합니다. 이는 행동 의도를 시각적 보호의 전처리 단계에 명시적으로 인코딩한 최초의 사례이며, 분할 주석이나 객체 상태에 의존하지 않습니다.

2. **이진 거부가 아닌 복구 가능성 분류**: 라우터는 증거 강도에 따라 "복구 가능 교란"(행동 드리프트, 시각적 지연, 국소 덮개)과 "복구 불가 상태"(동결 재생)를 구분하고, 각각 복구 후보 라이브러리 또는 안전 실패를 트리거합니다. 이 설계는 "모든 이상에 복구 시도"로 인한 통제 상실 연장(무 Hold/Safe-Fail 시 컨트롤러가 탐지 후 259.2개 행동 지속)과 "모든 이상에 보수적 억제"로 인한 유효 행동 차단을 모두 피합니다.

3. **시공간 일관성을 통합 탐지 신호로 사용**: 기하 일관성(공간), 동역학 일관성(시간-공간 결합), 시간 증거(순수 시간)를 가중 위험으로 융합하여, 시스템이 "국소적으로 덮였지만 시간적으로 건강한 관측"과 "재생되었지만 공간적으로 그럴듯해 보이는 관측" 같은 미세한 차이를 구분할 수 있습니다. 이는 표 4에서 w/o Threat Typing이 시각적 덮개 하에서 이득이 −7.6으로 하락하는 반면, 완전 모델은 +41.0에 도달하는 것으로 나타납니다.

## 실험 및 결과

실험은 LIBERO 벤치마크에서 동결된 π_0 체크포인트를 사용하여, 네 개의 10-작업 스위트 각각 2,000개 에피소드로 네 가지 교란 유형을 다룹니다.

| 시나리오 | 지표 | Base VLA | ActFovea | 이득 |
|------|------|----------|----------|------|
| Action Drift | Disturbed SR | 83.1% | 90.1% | +7.0 |
| Visual Delay | Disturbed SR | 76.2% | 86.0% | +9.8 |
| Visual Overlay | Disturbed SR | 49.3% | 90.3% | +41.0 |
| Frozen Replay | Timely Safe Failure | 0.00% | 100.00% | — |

표 2는 훈련 무관 런타임 방법과의 비교: ActFovea는 시각적 덮개에서 90.3%로 Action Clip/Smoothing의 30.9% 및 Fixed Short Horizon의 32.4%를 크게 능가; 시각적 지연에서 86.0%로 Timestamp-Only Hold의 0.0%를 크게 능가. 표 3은 완전 실행기가 동결 재생 하에서 100% 적시 안전 실패를 달성하고, 탐지 후 2.0개의 유계 행동 단계만 실행하며, 누적 운동 노름 0.326, 행동 경계 위반 없음; 반면 무 Hold/Safe-Fail 시 컨트롤러는 259.2개 행동을 지속하고 누적 운동 241.98(표 내 수치 계산, 탐지 후 행동 수 99.23% 감소, 누적 운동 99.87% 감소).

표 4 소거 실험: w/o Recovery Bank는 시각적 덮개에서 이득이 −33.3으로 하락, w/o Candidate Expansion은 −31.7로 하락, w/o Action Verification은 행동 드리프트에서 이득이 −1.2로 하락하여, 복구 후보 라이브러리, 후보 확장, 행동 검증이 모두 필수적임을 증명합니다.

## 경계 및 한계

- 공식적 충돌 회피 보장은 메커니즘 범위에 없으며, 안전 실패는 보수적 운동 억제만 의미하고 물리적 안전성 증명을 제공하지 않습니다.
- 인터페이스 이후에 교란이 도입되는 경우(즉, 정책 내부 또는 실행기 계층에 이미 진입)는 위협 모델에 포함되지 않습니다.
- 재훈련이나 매개변수 최적화가 수행되지 않았으며, 기본 VLA 정책은 동결 상태를 유지; 모든 선택 규칙은 추론 시 고정되고 훈련 목표가 추가되지 않습니다.
- 보상 신호, 시뮬레이터 객체 상태, 분할 주석 또는 교란 유형 사전 정보가 제공되지 않음; 투영을 사용할 수 없을 때 등속 데카르트 외삽 또는 이전 추적 중심 및 이미지 평면 방향 추론에 의존하며, 극단적 운동에서 실패할 수 있습니다.
- 논문은 하드웨어 플랫폼 세부 사항과 추론 지연 오버헤드를 명시하지 않았습니다.

## 공학적 시사점

재현 시 세 가지를 먼저 확인하십시오: 첫째, 행동 조건화 주시의 마스크 구축—투영을 사용할 수 없을 때의 외삽 전략이 덮개 시나리오의 복구 품질에 직접 영향을 미치므로, 빠른 회전에서 등속 외삽의 안정성을 우선 검증할 것을 권장합니다; 둘째, 위험 집계에서 β와 구성 요소 가중치의 고정 상수—논문은 구체적인 값을 제공하지 않으므로 자체 보정이 필요하며, 낮은 신뢰도가 0.5로 수축되는 동작은 지연 시나리오에 큰 영향을 미칩니다; 셋째, 공간 복구의 허용 임계값—모든 감지 뷰가 재구성되고 가장 약한 뷰 품질이 임계값을 통과할 때만 복구를 수락하며, 임계값이 너무 엄격하면 w/o Recovery Bank로 퇴화하고(시각적 덮개 이득 −33.3), 너무 느슨하면 잘못된 복구가 도입됩니다.

가장 쉽게 함정에 빠지는 것은 Timestamp-Only Hold의 "가짜 안전"입니다: 동결 재생 쿼리에서 96.55% 시간 동안 유지되지만, 종료 안전 실패로 전환되지 않아 작업이 적시 실패가 아닌 교착 상태가 됩니다. ActFovea의 유지 래치는 강한 재생 증거 또는 구성 가능한 오래됨 연속 후에 활성화되고, 충분히 새로운 증거 후에 해제되어야 합니다—구현 시 래치 해제 조건이 재생 탐지와 분리되도록 보장해야 하며, 그렇지 않으면 0.0% 적시 안전 실패의 실패 모드가 재현됩니다. 하위 팀 통합 시, 먼저 시각적 덮개 시나리오로 복구 후보 라이브러리의 허용 로직을 검증한 다음, 행동 검증의 가중치 벡터를 점진적으로 개방할 것을 권장합니다.
