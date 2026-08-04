---
$id: ent_paper_closing_loop_humanoid_vla_persistent_3d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation'
  zh: 'Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation'
  ko: 'Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation'
summary:
  en: 'Vision-language-action policies are a promising foundation for general robot control, but long-horizon humanoid loco-manipulation
    requires the robot to treat task objects as persistent physical entities across movement, contact, occlusion, and recovery.
    We study this problem as object-state divergence: the object state used to condition a whole-body action can differ from
    the state used to decide.'
  zh: 本文提出 Persistent Object Tokenization (POT)，一种为人形机器人 loco-manipulation 设计的闭环状态表示方法，通过将任务物体绑定到角色索引的持久 3D 对象令牌，并插入 DiT 动作头自注意力序列，使
    VLA 策略在长时程移动操作中持续可寻址且可验证。作者在 Unitree G1 上完成 8 个真实世界任务族共 80 次试验，POT-VLA 总成功率 71/80，显著优于直接基线 39/80，并在一组外部参考任务上以 44/50 超过
    Being-0 的 37/50。
  ko: 'Vision-language-action policies are a promising foundation for general robot control, but long-horizon humanoid loco-manipulation
    requires the robot to treat task objects as persistent physical entities across movement, contact, occlusion, and recovery.
    We study this problem as object-state divergence: the object state used to condition a whole-body action can differ from
    the state used to decide.'
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
- closing
- loop
- humanoid
- vla
- persistent
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
  title: 'arXiv:2607.18016 Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loc'
  url: https://arxiv.org/abs/2607.18016
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Persistent Object Tokenization (POT)，一种为人形机器人 loco-manipulation 设计的闭环状态表示方法，通过将任务物体绑定到角色索引的持久 3D 对象令牌，并插入 DiT 动作头自注意力序列，使 VLA 策略在长时程移动操作中持续可寻址且可验证。作者在 Unitree G1 上完成 8 个真实世界任务族共 80 次试验，POT-VLA 总成功率 71/80，显著优于直接基线 39/80，并在一组外部参考任务上以 44/50 超过 Being-0 的 37/50。

## 它改变了什么

它真正改变的不是“感知更准”或“控制更强”，而是把 VLA 策略从“开环执行器”变成了“闭环决策器”。此前，VLA 的典型用法是：给定当前观测，输出一段动作块，然后靠外部监控器或语言级状态检查来判断任务进度。问题在于，用于生成动作的对象状态（如抓取点、目标位置）与用于验证任务是否达成的状态（如谓词、几何关系）往往来自不同表征，一旦出现小的接地误差或抓取偏移，动作头还在按旧状态执行，而验证器已经判定失败或提前切换子任务——这就是作者点名的 object-state divergence。POT 的贡献在于把“动作条件”和“验证条件”统一到同一份持久 3D 对象记忆上，让策略在每次动作块后都能刷新同一组对象令牌，再决定继续、重试还是重规划。这不是加一个模块，而是改变了 VLA 的闭环结构：从“感知→动作”的单向流水线，变成“感知→动作→验证→再感知”的循环。

## 方法拆解

### 类型化子任务作为输入
POT 不依赖特定规划器，而是接受 VLM 规划器或人工任务文件给出的类型化子任务计划 Π = ⟨task_id, I, {τ_i}⟩。每个子任务 τ_i 指定角色、接地查询、成功谓词、失败处理器、块时域、超时和重试预算，但不指定低级运动——运动完全由动作专家生成。

### 角色索引对象记忆
每个子任务维护 M_t^{τ_i} = {m_t^e | e ∈ E_i}，每条记录 m_t^e 存储实体角色、短语、图像框、3D 质心和范围、置信度、可见性和关系特征。在线或缓存的 SAM3 掩码提供角色/查询掩码，有效深度像素通过相机内参和相机到基座变换反投影，经校准工作空间过滤后在机器人基座坐标系中汇总。

### 持久令牌模式
默认 K=8 槽位、F=33 特征每槽。有效槽位携带角色 ID（TARGET、DESTINATION、SUPPORT、HANDOVER_PARTNER），未使用槽位为 PADDING 并被掩码。槽位特征包括可见性、置信度、归一化 2D 框坐标、3D 质心、3D 范围、可选方向字段和关系。持久性机制的关键设计：任务实体绑定到角色槽位，每个动作块后刷新度量证据；若物体被遮挡或低置信度，槽位仍存在但可见性/置信度字段标记为不确定，允许验证器请求重新观测而非视为已确认。

### 动作头插入
POT-VLA 将对象令牌插入 DiT 动作头自注意力序列，而非视觉-语言骨干。序列布局为 S_t = [Z_t^state, Z_t^obj, Z_t^action]，填充槽位被掩码，视觉-语言骨干特征保持为编码器隐藏状态用于交叉注意力。对象令牌投影器 f_θ^obj 为 LayerNorm → Linear → GELU → Dropout → Linear，每个投影槽位与学习的角色嵌入和上下文嵌入结合，使动作头能区分任务角色语义与通用对象特征内容。

### 训练与闭环执行
训练目标与基础动作专家相同（动作块预测），不添加辅助对象记忆或谓词损失。对象令牌微调期间，演示与部署时相同的角色感知 RGB-D 模式生成的对象令牌侧车配对。闭环执行时，每次只执行一个验证过的短时域块（chunk horizon H），在 t^+ = t+H 时刷新感知并重新生成 Z_{t^+}^obj。谓词验证 p = ⟨κ, α, op, ν, n⟩，阈值和稳定窗口由类型化子任务和机器人校准指定。监督器返回 {in_progress, done, blocked, failed, uncertain}，恢复选择为 {continue, retry, reobserve, reground, replan}。

## 关键创新

1. **统一动作条件与验证条件的对象表征**：这是最核心的创新。POT 让用于生成动作的对象状态和用于判断任务达成的谓词状态来自同一份持久 3D 记忆，从机制上消除 object-state divergence。此前方法要么用视觉特征做动作、用语言状态做验证，要么用两套独立感知管线，POT 是第一个把两者绑定到同一角色槽位的方案。

2. **角色槽位的持久性与不确定性显式建模**：物体被遮挡或低置信度时，槽位不消失，而是标记为不确定并触发重新观测。这比“检测不到就当作不存在”或“检测不到就重试”都更鲁棒，因为它给验证器提供了明确的“我不知道”信号，而不是错误的“已确认”或“已失败”。

3. **对象令牌插入动作头而非骨干**：这是一个工程上巧妙的设计决策。插入 DiT 动作头自注意力序列意味着视觉-语言骨干完全不动，基础动作专家训练路径不变，对象令牌微调只影响动作头分支。这大幅降低了适配成本，且允许在禁用对象令牌时无缝回退到基础动作专家。

## 实验与结果

### 主结果（表1 Panel A，10次试验/任务）

| 任务 | Direct | POT-VLA |
|---|---|---|
| Cart transport/place | 3/10 | 8/10 |
| Chip box to basket | 9/10 | 10/10 |
| Two balls to basket | 5/10 | 9/10 |
| Stack three cups | 1/10 | 8/10 |
| Garments to basket | 3/10 | 9/10 |
| Drawer/tray place-close | 4/10 | 8/10 |
| Tabletop sorting | 5/10 | 9/10 |
| Close-range handover | 9/10 | 10/10 |
| **总计** | **39/80** | **71/80** |

### 外部参考（表1 Panel B，Being-0 对齐服务任务）

| 任务 | Being-0 | POT-VLA |
|---|---|---|
| Fetch-bottle | 9/10 | 9/10 |
| Deliver-basket | 8/10 | 8/10 |
| Grasp-bottle | 8/10 | 10/10 |
| Place-basket | 6/10 | 9/10 |
| Place-coffee | 6/10 | 8/10 |
| **总计** | **37/50** | **44/50** |

### 消融（表2 Panel A，4任务×10次）

| 变体 | 成功率 |
|---|---|
| Direct baseline | 15/40 |
| Verifier only | 22/40 |
| POT tokens only | 31/40 |
| POT-VLA | 34/40 |

### 泛化（表2 Panel B，10次/设置）

| 设置 | Direct | POT-VLA |
|---|---|---|
| Novel object instances | 6/10 | 9/10 |
| Shifted poses/layouts | 5/10 | 9/10 |
| Distractor objects | 8/10 | 9/10 |
| Mid-execution perturbations | 4/10 | 8/10 |

消融结果的关键含义：仅加验证器（22/40）比直接基线（15/40）提升有限，仅加 POT 令牌（31/40）提升显著，两者结合（34/40）接近最优——说明验证器需要持久对象状态才能发挥价值，而 POT 令牌单独也能改善动作质量。泛化测试中 mid-execution perturbations 从 4/10 提升到 8/10，直接验证了闭环恢复的价值。

## 边界与局限

POT-VLA 仍受限于对象记录质量、SAM3/RGB-D 可靠性、相机校准和动作专家具身覆盖范围。作者明确未在仿真中训练或评估，未使用显式物理引擎或学习动力学模型，未在除 Unitree G1 外的平台实验。对于 Being-0 参考，作者明确说明这不是本地复现，而是使用其论文报告的重叠服务任务成功计数——这意味着跨系统比较存在协议差异风险。论文未提及训练数据量、推理频率（Hz）等关键工程参数，也未讨论对象令牌在极端遮挡或快速运动下的失效边界。

## 工程启示

复现时先核对三件事：一是 SAM3 掩码质量与深度反投影的相机标定精度，这是对象令牌度量证据的源头，标定误差会直接污染 3D 质心和范围；二是动作专家（GR00T-N1.7）的检查点与对象令牌微调的配对方式——演示时必须使用与部署相同的角色感知 RGB-D 模式生成侧车，否则微调分布不匹配；三是谓词阈值和稳定窗口的校准，这些由类型化子任务和机器人校准指定，不是学习出来的，设置不当会导致验证器频繁返回 uncertain 或误报 done。最容易踩坑的地方是对象令牌插入动作头后的序列布局：S_t = [Z_t^state, Z_t^obj, Z_t^action]，填充槽位必须正确掩码，否则动作头会学到对 PADDING 槽位的虚假依赖。另一个隐蔽问题是恢复选择逻辑：reobserve 和 reground 的触发条件依赖置信度阈值，阈值过严会导致频繁重观测拖慢执行，过松则回到 object-state divergence 的老问题。建议先在小任务集（如 two balls to basket）上校准验证器阈值，再扩展到堆叠和铰接交互任务。

## Overview
Vision-language-action policies are a promising foundation for general robot control, but long-horizon humanoid loco-manipulation requires the robot to treat task objects as persistent physical entities across movement, contact, occlusion, and recovery. We study this problem as object-state divergence: the object state used to condition a whole-body action can differ from the state used to decide whether the action achieved the intended physical relation. We propose \emph{Persistent Object Tokenization} (POT), which maintains role-indexed 3D object records from RGB-D observations and converts them into object tokens for a whole-body action expert. Instantiated as \emph{POT-VLA}, the same object records condition action generation and support geometric predicate checks, yielding a closed-loop execution system in which object state is both actionable and verifiable. On a Unitree G1, POT-VLA improves a matched direct GR00T-N1.7 baseline from 39/80 to 71/80 successes over eight real-world task families. In an external Being-0-aligned reference, POT-VLA achieves 44/50 successes on aligned service tasks, compared with the 37/50 success reported by the Being-0 paper. The largest gains occur on tasks requiring maintained 3D relations, suggesting that persistent object-centered state is a useful abstraction for verifiable humanoid VLA execution.

## 参考
- https://arxiv.org/abs/2607.18016

## 개요

본 논문은 Persistent Object Tokenization (POT)을 제안한다. 이는 휴머노이드 로봇의 loco-manipulation을 위해 설계된 폐루프 상태 표현 방법으로, 작업 객체를 역할 인덱스 기반의 지속적 3D 객체 토큰에 바인딩하고 DiT 액션 헤드 자기주의 시퀀스에 삽입하여, VLA 정책이 장시간 이동 조작 중에도 객체를 지속적으로 주소 지정 가능하고 검증 가능하게 만든다. 저자는 Unitree G1에서 8개의 실제 세계 작업 패밀리, 총 80회의 시험을 수행했으며, POT-VLA의 총 성공률은 71/80으로 직접 베이스라인 39/80을 크게 능가했고, 외부 참조 작업 세트에서는 44/50으로 Being-0의 37/50을 초과했다.

## 그것이 바꾸는 것

진정으로 바뀌는 것은 "인식이 더 정확해진다"거나 "제어가 더 강해진다"는 것이 아니라, VLA 정책을 "개루프 실행기"에서 "폐루프 의사결정기"로 바꾸는 것이다. 이전에는 VLA의 일반적인 사용법은 다음과 같았다: 현재 관측이 주어지면 일련의 액션 블록을 출력하고, 외부 모니터나 언어 수준 상태 점검에 의존하여 작업 진행 상황을 판단했다. 문제는 액션 생성에 사용되는 객체 상태(예: 파지 지점, 목표 위치)와 작업 달성 여부를 검증하는 상태(예: 술어, 기하학적 관계)가 종종 서로 다른 표현에서 비롯된다는 점이다. 작은 접지 오류나 파지 오프셋이 발생하면 액션 헤드는 여전히 이전 상태에 따라 실행하는 반면, 검증기는 이미 실패를 판정하거나 하위 작업을 조기에 전환한다—이것이 저자가 지적하는 object-state divergence이다. POT의 기여는 "액션 조건"과 "검증 조건"을 동일한 지속적 3D 객체 메모리에 통합하여, 정책이 각 액션 블록 후에 동일한 객체 토큰 세트를 새로 고치고 계속, 재시도, 또는 재계획을 결정할 수 있게 하는 것이다. 이는 모듈을 추가하는 것이 아니라 VLA의 폐루프 구조를 바꾸는 것이다: "인식→액션"의 단방향 파이프라인에서 "인식→액션→검증→재인식"의 순환으로.

## 방법 분해

### 유형화된 하위 작업을 입력으로
POT는 특정 플래너에 의존하지 않고, VLM 플래너 또는 수동 작업 파일에서 제공하는 유형화된 하위 작업 계획 Π = ⟨task_id, I, {τ_i}⟩을 수용한다. 각 하위 작업 τ_i는 역할, 접지 쿼리, 성공 술어, 실패 처리기, 블록 시간 영역, 타임아웃 및 재시도 예산을 지정하지만, 저수준 운동은 지정하지 않는다—운동은 전적으로 액션 전문가에 의해 생성된다.

### 역할 인덱스 객체 메모리
각 하위 작업은 M_t^{τ_i} = {m_t^e | e ∈ E_i}을 유지하며, 각 레코드 m_t^e는 엔터티 역할, 구문, 이미지 박스, 3D 질량 중심 및 범위, 신뢰도, 가시성 및 관계 특징을 저장한다. 온라인 또는 캐시된 SAM3 마스크는 역할/쿼리 마스크를 제공하고, 유효한 깊이 픽셀은 카메라 내부 파라미터와 카메라-베이스 변환을 통해 역투영되며, 보정된 작업 공간에서 필터링된 후 로봇 베이스 좌표계에서 집계된다.

### 지속적 토큰 패턴
기본 K=8 슬롯, F=33 특징/슬롯. 유효 슬롯은 역할 ID(TARGET, DESTINATION, SUPPORT, HANDOVER_PARTNER)를 전달하고, 사용되지 않은 슬롯은 PADDING이며 마스킹된다. 슬롯 특징에는 가시성, 신뢰도, 정규화된 2D 박스 좌표, 3D 질량 중심, 3D 범위, 선택적 방향 필드 및 관계가 포함된다. 지속성 메커니즘의 핵심 설계: 작업 엔터티는 역할 슬롯에 바인딩되고, 각 액션 블록 후에 측정 증거가 새로 고쳐진다. 객체가 가려지거나 신뢰도가 낮으면 슬롯은 여전히 존재하지만 가시성/신뢰도 필드는 불확실로 표시되어, 검증기가 확인된 것으로 간주하지 않고 재관측을 요청할 수 있다.

### 액션 헤드 삽입
POT-VLA는 객체 토큰을 시각-언어 백본이 아닌 DiT 액션 헤드 자기주의 시퀀스에 삽입한다. 시퀀스 레이아웃은 S_t = [Z_t^state, Z_t^obj, Z_t^action]이며, 패딩 슬롯은 마스킹되고, 시각-언어 백본 특징은 교차 주의를 위한 인코더 은닉 상태로 유지된다. 객체 토큰 프로젝터 f_θ^obj는 LayerNorm → Linear → GELU → Dropout → Linear이며, 각 투영 슬롯은 학습된 역할 임베딩 및 컨텍스트 임베딩과 결합되어 액션 헤드가 작업 역할 의미론과 일반 객체 특징 콘텐츠를 구별할 수 있게 한다.

### 훈련 및 폐루프 실행
훈련 목표는 기본 액션 전문가와 동일하며(액션 블록 예측), 보조 객체 메모리 또는 술어 손실을 추가하지 않는다. 객체 토큰 미세 조정 중에는 데모와 동일한 역할 인식 RGB-D 패턴으로 생성된 객체 토큰 사이드카 페어링이 사용된다. 폐루프 실행 시, 검증된 짧은 시간 영역 블록(chunk horizon H)만 실행되고, t^+ = t+H에서 인식을 새로 고치고 Z_{t^+}^obj를 재생성한다. 술어 검증 p = ⟨κ, α, op, ν, n⟩, 임계값 및 안정 창은 유형화된 하위 작업 및 로봇 보정에 의해 지정된다. 감독자는 {in_progress, done, blocked, failed, uncertain}을 반환하고, 복구 선택은 {continue, retry, reobserve, reground, replan}이다.

## 핵심 혁신

1. **액션 조건과 검증 조건을 통합하는 객체 표현**: 이것이 가장 핵심적인 혁신이다. POT는 액션 생성에 사용되는 객체 상태와 작업 달성 판단에 사용되는 술어 상태가 동일한 지속적 3D 메모리에서 비롯되도록 하여, 메커니즘적으로 object-state divergence를 제거한다. 이전 방법은 액션에 시각적 특징을, 검증에 언어 상태를 사용하거나 두 개의 독립적인 인식 파이프라인을 사용했지만, POT는 둘을 동일한 역할 슬롯에 바인딩하는 최초의 방법이다.

2. **역할 슬롯의 지속성과 불확실성의 명시적 모델링**: 객체가 가려지거나 신뢰도가 낮을 때 슬롯은 사라지지 않고 불확실로 표시되어 재관측을 트리거한다. 이는 "감지되지 않으면 존재하지 않는 것으로 간주"하거나 "감지되지 않으면 재시도"하는 것보다 더 견고하다. 검증기에 명확한 "모름" 신호를 제공하여 잘못된 "확인" 또는 "실패"를 방지하기 때문이다.

3. **백본이 아닌 액션 헤드에 객체 토큰 삽입**: 이는 공학적으로 영리한 설계 결정이다. DiT 액션 헤드 자기주의 시퀀스에 삽입하면 시각-언어 백본이 완전히 변경되지 않고, 기본 액션 전문가 훈련 경로도 변경되지 않으며, 객체 토큰 미세 조정은 액션 헤드 분기에만 영향을 미친다. 이는 적응 비용을 크게 줄이고, 객체 토큰을 비활성화할 때 기본 액션 전문가로의 원활한 폴백을 허용한다.

## 실험 및 결과

### 주요 결과 (표1 패널 A, 10회 시험/작업)

| 작업 | Direct | POT-VLA |
|---|---|---|
| 카트 운반/배치 | 3/10 | 8/10 |
| 칩 박스를 바구니로 | 9/10 | 10/10 |
| 공 두 개를 바구니로 | 5/10 | 9/10 |
| 컵 세 개 쌓기 | 1/10 | 8/10 |
| 의류를 바구니로 | 3/10 | 9/10 |
| 서랍/트레이 배치-닫기 | 4/10 | 8/10 |
| 테이블 위 분류 | 5/10 | 9/10 |
| 근거리 핸드오버 | 9/10 | 10/10 |
| **총계** | **39/80** | **71/80** |

### 외부 참조 (표1 패널 B, Being-0 정렬 서비스 작업)

| 작업 | Being-0 | POT-VLA |
|---|---|---|
| 병 가져오기 | 9/10 | 9/10 |
| 바구니 전달 | 8/10 | 8/10 |
| 병 파지 | 8/10 | 10/10 |
| 바구니 배치 | 6/10 | 9/10 |
| 커피 배치 | 6/10 | 8/10 |
| **총계** | **37/50** | **44/50** |

### 소거 (표2 패널 A, 4작업×10회)

| 변형 | 성공률 |
|---|---|
| 직접 베이스라인 | 15/40 |
| 검증기만 | 22/40 |
| POT 토큰만 | 31/40 |
| POT-VLA | 34/40 |

### 일반화 (표2 패널 B, 10회/설정)

| 설정 | Direct | POT-VLA |
|---|---|---|
| 새로운 객체 인스턴스 | 6/10 | 9/10 |
| 이동된 포즈/레이아웃 | 5/10 | 9/10 |
| 방해 객체 | 8/10 | 9/10 |
| 실행 중 교란 | 4/10 | 8/10 |

소거 결과의 핵심 의미: 검증기만 추가(22/40)는 직접 베이스라인(15/40)보다 제한적으로 향상되고, POT 토큰만 추가(31/40)는 상당한 향상을 보이며, 둘을 결합(34/40)하면 최적에 가깝다—검증기는 지속적 객체 상태가 있어야 가치를 발휘하고, POT 토큰만으로도 액션 품질을 개선할 수 있음을 시사한다. 일반화 테스트에서 실행 중 교란은 4/10에서 8/10으로 향상되어 폐루프 복구의 가치를 직접 검증한다.

## 경계 및 한계

POT-VLA는 여전히 객체 레코드 품질, SAM3/RGB-D 신뢰성, 카메라 보정 및 액션 전문가의 신체 범위에 의해 제한된다. 저자는 시뮬레이션에서 훈련하거나 평가하지 않았고, 명시적 물리 엔진이나 학습된 역학 모델을 사용하지 않았으며, Unitree G1 이외의 플랫폼에서 실험하지 않았다고 명시했다. Being-0 참조에 대해 저자는 이것이 로컬 재현이 아니라 그들의 논문에서 보고된 중복 서비스 작업 성공 횟수를 사용한 것임을 명확히 밝혔다—즉, 교차 시스템 비교에는 프로토콜 차이 위험이 있다. 논문은 훈련 데이터 양, 추론 빈도(Hz)와 같은 핵심 엔지니어링 파라미터를 언급하지 않았으며, 극단적인 가림이나 빠른 움직임에서 객체 토큰의 실패 경계도 논의하지 않았다.

## 엔지니어링 시사점

재현 시 먼저 세 가지를 확인해야 한다: 첫째, SAM3 마스크 품질과 깊이 역투영의 카메라 보정 정밀도—이것이 객체 토큰 측정 증거의 원천이며, 보정 오류는 3D 질량 중심과 범위를 직접 오염시킨다. 둘째, 액션 전문가(GR00T-N1.7)의 체크포인트와 객체 토큰 미세 조정의 페어링 방식—데모에서 배포와 동일한 역할 인식 RGB-D 패턴으로 사이드카를 생성해야 하며, 그렇지 않으면 미세 조정 분포가 불일치한다. 셋째, 술어 임계값과 안정 창의 보정—이는 유형화된 하위 작업 및 로봇 보정에 의해 지정되며 학습되지 않으므로, 잘못 설정하면 검증기가 빈번하게 uncertain을 반환하거나 done을 오보한다. 가장 함정에 빠지기 쉬운 곳은 객체 토큰을 액션 헤드에 삽입한 후의 시퀀스 레이아웃이다: S_t = [Z_t^state, Z_t^obj, Z_t^action], 패딩 슬롯은 올바르게 마스킹되어야 하며, 그렇지 않으면 액션 헤드가 PADDING 슬롯에 대한 거짓 의존성을 학습하게 된다. 또 다른 은밀한 문제는 복구 선택 논리이다: reobserve와 reground의 트리거 조건은 신뢰도 임계값에 의존하며, 임계값이 너무 엄격하면 빈번한 재관측으로 실행이 느려지고, 너무 느슨하면 object-state divergence의 기존 문제로 돌아간다. 작은 작업 세트(예: two balls to basket)에서 검증기 임계값을 먼저 보정한 다음, 쌓기 및 관절 상호작용 작업으로 확장하는 것을 권장한다.
