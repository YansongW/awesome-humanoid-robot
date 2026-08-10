---
$id: ent_paper_embodiedgen_v2_agentic_simulation_ready_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI'
  zh: 'EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI'
  ko: 'EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI'
summary:
  en: We present EmbodiedGen V2, a generative 3D world engine for building executable policy-ready environments for embodied
    intelligence. Sim-ready 3D asset generation has advanced rapidly, yet assembling such assets into policy-ready task environments
    remains largely manual, limiting scalable closed-loop learning. EmbodiedGen V2 addresses this gap through a unified sim-ready
    representation that.
  zh: EmbodiedGen V2 是地平线机器人与 WuwenAI 联合提出的具身智能仿真就绪 3D 世界引擎，将资产生成、物理属性恢复、可操作标注、任务驱动布局与有状态编辑统一为闭环管线。核心贡献在于以 URDF 为统一中间表示，打通从单图/文本到多模拟器可执行任务环境的全链路，并通过生成-验证-重试机制将人工介入降至最低。
  ko: We present EmbodiedGen V2, a generative 3D world engine for building executable policy-ready environments for embodied
    intelligence. Sim-ready 3D asset generation has advanced rapidly, yet assembling such assets into policy-ready task environments
    remains largely manual, limiting scalable closed-loop learning. EmbodiedGen V2 addresses this gap through a unified sim-ready
    representation that.
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
- embodiedgen
- v2
- agentic
- simulation
- ready
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P117. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.07459 EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI'
  url: https://arxiv.org/abs/2607.07459
  date: '2026-07-08'
  accessed_at: '2026-08-05'
---

## 概述

EmbodiedGen V2 是地平线机器人与 WuwenAI 联合提出的具身智能仿真就绪 3D 世界引擎，将资产生成、物理属性恢复、可操作标注、任务驱动布局与有状态编辑统一为闭环管线。核心贡献在于以 URDF 为统一中间表示，打通从单图/文本到多模拟器可执行任务环境的全链路，并通过生成-验证-重试机制将人工介入降至最低。

## 它改变了什么

生成式 3D 模型此前解决的是"看起来对"，而具身策略学习要求"用起来对"——物体必须有碰撞体、质量、摩擦系数和可抓取部位，布局必须满足机器人可达性与任务语义，资产必须能在不同模拟器间无痛迁移。EmbodiedGen V2 真正改变的是将模拟兼容性从生成后的附加导出步骤，前置为贯穿候选筛选、3D 生成、物理恢复全过程的硬约束，使"仿真就绪"成为生成器的内生属性而非事后补救。

相比 V1 的全景反投影单网格背景，V2 暴露了真实房间拓扑、可穿越开口和独立可寻址家具实体，这直接解锁了长时程导航与移动操作场景。更关键的是，它把"世界生成"从一次性提示-输出范式，升级为带持久状态（Scene Graph + 资产 + 位姿 + 编辑历史）的可交互编辑循环，让 LLM 智能体能够对已生成世界做有界、可审计的局部修改，而非每次推倒重来。

## 方法拆解

### 统一 sim-ready 表示（两层级）
- **对象层级**：捆绑纹理化视觉几何、碰撞几何（CoACD 凸分解）、物理参数（VLM 推断尺度/质量/摩擦）与可操作标注（部件分割 + 语义 + 验证过的抓取）。
- **场景层级**：类型化 Scene Graph 指定实体、任务角色（ROBOT/BACKGROUND/CONTEXT/MANIPULATED_OBJS/DISTRACTOR_OBJS）及空间关系（ON/INSIDE/FLOOR/IN），落地为物理稳定的 6-DoF 位姿。

### 资产生成五阶段
1. **输入准备**：文本经 SD3.5/Kolors 生成候选图；图像经 Rembg/SAM/RMBG 分割前景。
2. **3D 生成**：TRELLIS/SAM3D/Hunyuan3D 同时产出 3D 高斯与网格。
3. **几何精修**：拓扑修复 + 简化，多视角反投影将高斯外观烘焙为显式纹理。
4. **物理恢复**：VLM 从多视角渲染推断真实尺度、质量与摩擦系数。
5. **打包导出**：统一中间表示 URDF，自动转换 XML（MuJoCo/Genesis）与 USD（Isaac Sim）。

### 分层质量门控
- 输入阶段：VLM 验证分割语义与几何完整性。
- 3D 阶段：多视角渲染评估，拒绝截断/重复主体，失败自动换随机种子重试。
- 末端：美学评分模型过滤低质量样本，结果以结构化标签写入资产文件。

### 任务驱动世界生成（三阶段）
1. **Scene Graph 生成**：LLM 将任务分解为五类语义角色，组织为浅层有根图（单父结构减少放置歧义）。
2. **资产生成**：在线生成或离线数据库检索。
3. **BFS 空间放置**：父先子后，按足迹排序兄弟节点；支撑谓词 + IoU 碰撞项约束；被操作物体限制在机器人前向可达区；SAPIEN 重力沉降解决残余穿透。

### 大规模场景生成（三阶段）
- 输出三元组 S = (R, F, C)：房间拓扑图（带门/窗连接）、逐房间可寻址家具集、全局一致坐标系。
- 任务条件化路由：VLM 输出房间范围与复杂度 ℓ ∈ {Minimalist, Simple, Medium, Detail}。
- 分层求解：骨架级家具 → 中尺度物体 → 桌面杂乱，程序化生成器面向模拟重塑（抑制纯装饰几何）。
- 模拟器无关规范化：逐实例分解 + 批量 CoACD + 质心对齐世界原点。

### Vibe Coding 有状态编辑
- 三组件：LLM 智能体（意图解析/技能选择）、自描述技能套件（暴露输入/输出/失败模式）、运行时 Harness（技能注册表/共享世界状态/编辑日志）。
- 世界状态 S_t = (G_t, A_t, P_t, H_t)，每次更新保持几何物理可行性并记录审计轨迹。
- 空间计算技能将场景暴露为 2D 平面图，复用碰撞-IoU 项解析 ON/BESIDE/IN 关系。

## 关键创新

1. **生成-验证-重试闭环**：将质量检查嵌入每个生成阶段而非末端一次性过滤，使每个有效资产平均仅需 1.35 次生成尝试。这不是简单的质量控制，而是将"失败-诊断-重试"作为一等公民设计进管线，大幅降低端到端成本。

2. **URDF 作为统一中间表示**：利用 URDF 原生支持视觉/碰撞网格、惯性参数与元数据的结构化打包，将对象生成与模拟器适配彻底解耦。同一资产在六个模拟器（Genesis、Isaac Gym、Isaac Sim、MuJoCo、PyBullet、SAPIEN3）中无需手动适配即可加载执行，这是工程上最实用的创新。

3. **有状态 Vibe Coding 编辑**：区别于 Chat-Edit-3D 的 2D 机制或每次重新生成，V2 将离线放置求解器变为在线技能核心，每次编辑提交有界增量 ΔS 到 (G, A, P, H)，保持跨模拟器一致性。这让 LLM 智能体首次能对 sim-ready 世界做可审计的局部手术而非整体移植。

## 实验与结果

| 指标 | 完整管线 | 无质量检查器 | 无网格修复 | 无凸分解 |
|---|---|---|---|---|
| 人类接受率 | 96.5% | 91.0% | 95.5% | 94.5% |
| 碰撞成功率 | 98.6% | 98.1% | 98.3% | 96.5% |
| 时间（分钟） | 2.6 ± 0.4 | 2.2 ± 0.4 | 21.3 ± 22.8 | 2.3 ± 0.3 |
| 视觉网格（MB） | 1.43 ± 0.63 | 1.44 ± 0.63 | 51.63 ± 25.87 | 1.45 ± 0.64 |
| 碰撞网格（MB） | 0.29 ± 0.21 | 0.30 ± 0.22 | 0.31 ± 0.26 | 1.45 ± 0.64 |

| 可供性管线 | 分割通过率 | 语义有效性 | 抓取覆盖率 | 可供性通过率 | 时间（秒） |
|---|---|---|---|---|---|
| 基线 | 47.0% | 98.9% | 66.7% | 31.0% | 109 ± 45 |
| +后处理 | 56.5% | 97.3% | 74.6% | 41.0% | 105 ± 41 |
| +后处理+VLM合并 | 69.5% | 99.3% | 72.5% | 50.0% | 94 ± 30 |

| 下游验证 | 指标 | 数值 |
|---|---|---|
| 在线 RL（EmbodiedGen 场景） | 仿真成功率 | 9.7% → 79.8% |
| 场景缩放 N=1→50 | OOD 成功率 | 53.2% → 77.9% |
| 手工场景训练→EmbodiedGen 测试 | 成功率 | 96.7% → 36.0% |
| 真实机器人迁移（240 次试验） | 任务成功率 | 21.7% → 75.0% |
| 真实机器人迁移 | 动力学失败率 | 66.7% → 18.3% |

关键发现：网格修复移除后运行时间暴增约 8 倍（由表内 2.6→21.3 计算），视觉网格从 1.43 MB 增至 51.63 MB，证明原始生成输出的拓扑缺陷是管线瓶颈。凸分解移除后碰撞网格从 0.29 MB 增至 1.45 MB（由表内数值计算），碰撞成功率下降 2.1 个百分点（由表内 98.6%→96.5% 计算），作者指出此类接触错误会在长时程操作中累积。手工场景训练在 EmbodiedGen 场景上仅 36.0% 成功率，反向验证了生成场景的分布多样性。

## 边界与局限

- 任务驱动世界生成将输出限制为刚体，未集成可变形体（尽管资产生成管线已展示服装软体模拟能力）。
- 大规模场景生成中 LLM 仅做离散语义决策，几何可行性完全依赖约束求解器，作者明确这是对 LLM 布局工作的补充而非替代。
- 任务世界采用"绿幕式分解"：背景 + 最小任务相关资产集，而非联合生成每个世界细节，这是有意的抽象。
- 论文未明确讨论失败案例分析、极端场景鲁棒性，或与真实世界物理保真度的定量对比。
- 最终环境接受率 83.3%，剩余失败源于对象尺度不匹配、局部几何缺陷或初始放置不完美，通常需重采样或轻微手动调整。

## 工程启示

- **先核对网格修复**：这是管线最大时间黑洞（移除后 21.3 ± 22.8 分钟/资产），复现时优先验证拓扑修复与简化步骤的鲁棒性，否则下游 UV 展开、纹理烘焙和凸分解都会被拖垮。
- **质量检查器不可省**：移除后人类接受率下降 5.5 个百分点（由表内 96.5%→91.0% 计算），但每资产仅节省 0.4 分钟，性价比极低。它针对的是感知缺陷而非几何属性，是保证资产语义完整性的关键防线。
- **凸分解是碰撞成功率的底线**：虽然绝对下降仅 2.1 个百分点（由表内 98.6%→96.5% 计算），但作者明确指出此类接触错误会在长时程操作中累积。对抓取、堆叠等接触密集任务，务必保留 CoACD 步骤。
- **URDF 中间表示是跨模拟器迁移的捷径**：若你的团队需要同时支持 MuJoCo 与 Isaac Sim，直接采用 URDF 作为统一格式可省去大量格式转换适配工作。
- **最容易踩坑的是空间放置**：83.3% 的接受率意味着约 1/6 的世界需要重采样或手动修正，主要问题集中在对象尺度不匹配与初始放置不完美。建议在下游训练前先跑一轮 SAPIEN 重力沉降验证，并保留重试机制。
- **场景分布缩放收益显著**：从 N=1 到 N=50 个生成场景，OOD 成功率提升 24.7 个百分点（由表内 53.2%→77.9% 计算），ID-OOD 差距从 41.1 个百分点缩至 2.6 个百分点。若你的策略在分布外表现差，优先扩展生成场景数量而非手工调参。

## Overview
We present EmbodiedGen V2, a generative 3D world engine for building executable policy-ready environments for embodied intelligence. Sim-ready 3D asset generation has advanced rapidly, yet assembling such assets into policy-ready task environments remains largely manual, limiting scalable closed-loop learning. EmbodiedGen V2 addresses this gap through a unified sim-ready representation that connects cross-simulator assets, interaction affordances, task-driven worlds, large-scale multi-room scenes, and stateful Vibe Coding into a generative, editable, and reusable simulation pipeline. The generated environments support manipulation, navigation, mobile manipulation, cross-simulator deployment, and embodied policy training. In evaluation, the asset pipeline achieves 96.5% human acceptance and 98.6% collision success, and 83.3% of task-driven worlds are directly usable for downstream simulation without manual modification. Online reinforcement learning with generated environments further improves simulation success from 9.7% to 79.8%, and transfers to real robots with task success increasing from 21.7% to 75.0%. These results establish EmbodiedGen V2 as scalable simulation infrastructure for training, evaluating, and deploying embodied policies.

## 参考
- https://arxiv.org/abs/2607.07459

## 개요

EmbodiedGen V2는 Horizon Robotics와 WuwenAI가 공동으로 제안한 임베디드 인텔리전스 시뮬레이션 준비 완료 3D 월드 엔진으로, 자산 생성, 물리 속성 복원, 조작 가능 주석, 작업 기반 레이아웃, 상태 저장 편집을 하나의 폐쇄 루프 파이프라인으로 통합합니다. 핵심 기여는 URDF를 통합 중간 표현으로 사용하여 단일 이미지/텍스트에서 다중 시뮬레이터 실행 가능 작업 환경까지의 전체 체인을 연결하고, 생성-검증-재시도 메커니즘을 통해 수동 개입을 최소화하는 것입니다.

## 무엇을 바꾸었는가

생성형 3D 모델은 이전에 "보기에는 맞는" 문제를 해결했지만, 임베디드 정책 학습은 "사용하기에 맞는" 것을 요구합니다—물체는 충돌체, 질량, 마찰 계수, 파지 가능 부위를 가져야 하며, 레이아웃은 로봇의 도달 가능성과 작업 의미론을 충족해야 하고, 자산은 서로 다른 시뮬레이터 간에 매끄럽게 이식되어야 합니다. EmbodiedGen V2가 실제로 바꾼 것은 시뮬레이션 호환성을 생성 후 추가 내보내기 단계에서 후보 선별, 3D 생성, 물리 복원 전 과정을 관통하는 하드 제약 조건으로 전치시켜 "시뮬레이션 준비 완료"를 사후 보완이 아닌 생성기의 내재적 속성으로 만든 것입니다.

V1의 파노라마 역투영 단일 메시 배경과 비교하여 V2는 실제 방 토폴로지, 통과 가능한 개구부, 독립적으로 주소 지정 가능한 가구 엔티티를 노출하여 장시간 내비게이션과 이동 조작 시나리오를 직접적으로 해금합니다. 더 중요하게는 "세계 생성"을 일회성 프롬프트-출력 패러다임에서 영구 상태(Scene Graph + 자산 + 자세 + 편집 기록)를 가진 상호작용 가능한 편집 루프로 업그레이드하여 LLM 에이전트가 생성된 세계에 대해 매번 처음부터 다시 시작하는 대신 경계가 있고 감사 가능한 국소 수정을 수행할 수 있게 합니다.

## 방법 분해

### 통합 sim-ready 표현(두 계층)
- **객체 계층**: 텍스처링된 시각적 지오메트리, 충돌 지오메트리(CoACD 볼록 분해), 물리 파라미터(VLM이 스케일/질량/마찰 추론) 및 조작 가능 주석(부품 분할 + 의미론 + 검증된 파지)을 번들로 제공.
- **장면 계층**: 타입화된 Scene Graph가 엔티티, 작업 역할(ROBOT/BACKGROUND/CONTEXT/MANIPULATED_OBJS/DISTRACTOR_OBJS) 및 공간 관계(ON/INSIDE/FLOOR/IN)를 지정하고, 물리적으로 안정적인 6-DoF 자세로 구현.

### 자산 생성 5단계
1. **입력 준비**: 텍스트는 SD3.5/Kolors로 후보 이미지 생성; 이미지는 Rembg/SAM/RMBG로 전경 분할.
2. **3D 생성**: TRELLIS/SAM3D/Hunyuan3D가 3D 가우시안과 메시를 동시에 생성.
3. **지오메트리 정제**: 토폴로지 복구 + 단순화, 다중 뷰 역투영으로 가우시안 외관을 명시적 텍스처로 베이킹.
4. **물리 복원**: VLM이 다중 뷰 렌더링에서 실제 스케일, 질량, 마찰 계수 추론.
5. **패키징 내보내기**: 통합 중간 표현 URDF, 자동 XML(MuJoCo/Genesis) 및 USD(Isaac Sim) 변환.

### 계층적 품질 게이팅
- 입력 단계: VLM이 분할 의미론과 지오메트리 완전성 검증.
- 3D 단계: 다중 뷰 렌더링 평가, 절단/중복 본체 거부, 실패 시 자동으로 무작위 시드 재시도.
- 최종 단계: 미적 평가 모델이 저품질 샘플 필터링, 결과는 구조화된 라벨로 자산 파일에 기록.

### 작업 기반 세계 생성(3단계)
1. **Scene Graph 생성**: LLM이 작업을 5가지 의미론적 역할로 분해, 얕은 루트 그래프로 구성(단일 부모 구조로 배치 모호성 감소).
2. **자산 생성**: 온라인 생성 또는 오프라인 데이터베이스 검색.
3. **BFS 공간 배치**: 부모 우선 자식 순서, 형제 노드는 풋프린트 기준 정렬; 지지 술어 + IoU 충돌 항으로 제약; 조작 대상 물체는 로봇 전방 도달 영역으로 제한; SAPIEN 중력 침강으로 잔여 관통 해결.

### 대규모 장면 생성(3단계)
- 출력 삼중항 S = (R, F, C): 방 토폴로지 그래프(문/창 연결 포함), 방별 주소 지정 가능 가구 집합, 전역 일관 좌표계.
- 작업 조건부 라우팅: VLM이 방 범위와 복잡도 ℓ ∈ {Minimalist, Simple, Medium, Detail} 출력.
- 계층적 해결: 골격 수준 가구 → 중간 규모 물체 → 테이블 잡동사니, 프로그램 생성기는 시뮬레이션에 맞게 재구성(순수 장식 지오메트리 억제).
- 시뮬레이터 무관 정규화: 인스턴스별 분해 + 배치 CoACD + 질량 중심을 세계 원점에 정렬.

### Vibe Coding 상태 저장 편집
- 세 가지 구성 요소: LLM 에이전트(의도 해석/스킬 선택), 자기 설명적 스킬 스위트(입력/출력/실패 모드 노출), 런타임 Harness(스킬 레지스트리/공유 세계 상태/편집 로그).
- 세계 상태 S_t = (G_t, A_t, P_t, H_t), 각 업데이트는 지오메트리 물리적 타당성을 유지하고 감사 궤적 기록.
- 공간 계산 스킬은 장면을 2D 평면도로 노출, 충돌-IoU 항을 재사용하여 ON/BESIDE/IN 관계 해석.

## 핵심 혁신

1. **생성-검증-재시도 폐쇄 루프**: 품질 검사를 최종 일회성 필터링이 아닌 각 생성 단계에 내장하여, 각 유효 자산은 평균 1.35회의 생성 시도만 필요. 이는 단순한 품질 관리가 아니라 "실패-진단-재시도"를 일급 시민으로 파이프라인에 설계하여 엔드투엔드 비용을 크게 절감.

2. **URDF를 통합 중간 표현으로**: URDF가 시각적/충돌 메시, 관성 파라미터, 메타데이터의 구조화된 패키징을 기본 지원하는 것을 활용하여 객체 생성과 시뮬레이터 적응을 완전히 분리. 동일 자산이 6개 시뮬레이터(Genesis, Isaac Gym, Isaac Sim, MuJoCo, PyBullet, SAPIEN3)에서 수동 적응 없이 로드 및 실행 가능—이는 엔지니어링 측면에서 가장 실용적인 혁신.

3. **상태 저장 Vibe Coding 편집**: Chat-Edit-3D의 2D 메커니즘이나 매번 재생성과 달리, V2는 오프라인 배치 솔버를 온라인 스킬 코어로 전환하고, 각 편집은 경계가 있는 증분 ΔS를 (G, A, P, H)에 커밋하여 크로스 시뮬레이터 일관성 유지. 이를 통해 LLM 에이전트가 처음으로 sim-ready 세계에 대해 감사 가능한 국소 수술을 수행할 수 있게 됨(전체 이식이 아닌).

## 실험 및 결과

| 지표 | 전체 파이프라인 | 품질 검사기 없음 | 메시 복구 없음 | 볼록 분해 없음 |
|---|---|---|---|---|
| 인간 수용률 | 96.5% | 91.0% | 95.5% | 94.5% |
| 충돌 성공률 | 98.6% | 98.1% | 98.3% | 96.5% |
| 시간(분) | 2.6 ± 0.4 | 2.2 ± 0.4 | 21.3 ± 22.8 | 2.3 ± 0.3 |
| 시각 메시(MB) | 1.43 ± 0.63 | 1.44 ± 0.63 | 51.63 ± 25.87 | 1.45 ± 0.64 |
| 충돌 메시(MB) | 0.29 ± 0.21 | 0.30 ± 0.22 | 0.31 ± 0.26 | 1.45 ± 0.64 |

| 가용성 파이프라인 | 분할 통과율 | 의미론적 유효성 | 파지 커버리지 | 가용성 통과율 | 시간(초) |
|---|---|---|---|---|---|
| 베이스라인 | 47.0% | 98.9% | 66.7% | 31.0% | 109 ± 45 |
| +후처리 | 56.5% | 97.3% | 74.6% | 41.0% | 105 ± 41 |
| +후처리+VLM 병합 | 69.5% | 99.3% | 72.5% | 50.0% | 94 ± 30 |

| 다운스트림 검증 | 지표 | 값 |
|---|---|---|
| 온라인 RL(EmbodiedGen 장면) | 시뮬레이션 성공률 | 9.7% → 79.8% |
| 장면 스케일링 N=1→50 | OOD 성공률 | 53.2% → 77.9% |
| 수동 장면 훈련→EmbodiedGen 테스트 | 성공률 | 96.7% → 36.0% |
| 실제 로봇 이전(240회 실험) | 작업 성공률 | 21.7% → 75.0% |
| 실제 로봇 이전 | 역학 실패율 | 66.7% → 18.3% |

핵심 발견: 메시 복구 제거 시 실행 시간이 약 8배 폭증(표 내 2.6→21.3 계산), 시각 메시가 1.43 MB에서 51.63 MB로 증가—원시 생성 출력의 토폴로지 결함이 파이프라인 병목임을 증명. 볼록 분해 제거 시 충돌 메시가 0.29 MB에서 1.45 MB로 증가(표 내 값 계산), 충돌 성공률 2.1%p 하락(표 내 98.6%→96.5% 계산), 저자는 이러한 접촉 오류가 장시간 조작에서 누적된다고 지적. 수동 장면 훈련은 EmbodiedGen 장면에서 36.0% 성공률에 그쳐, 생성 장면의 분포 다양성을 역으로 검증.

## 경계 및 한계

- 작업 기반 세계 생성은 출력을 강체로 제한, 변형체 미통합(자산 생성 파이프라인이 의류 소프트 바디 시뮬레이션 능력을 이미 보여줬음에도).
- 대규모 장면 생성에서 LLM은 이산 의미론적 결정만 수행, 지오메트리 타당성은 전적으로 제약 솔버에 의존—저자는 이를 LLM 레이아웃 작업에 대한 보완이지 대체가 아니라고 명시.
- 작업 세계는 "그린 스크린식 분해": 배경 + 최소 작업 관련 자산 집합, 각 세계 세부 사항의 공동 생성이 아닌 의도적 추상화.
- 논문은 실패 사례 분석, 극단적 장면 견고성, 또는 실제 세계 물리 충실도와의 정량적 비교를 명시적으로 다루지 않음.
- 최종 환경 수용률 83.3%, 잔여 실패는 객체 스케일 불일치, 국소 지오메트리 결함 또는 초기 배치 불완전성에서 비롯되며, 일반적으로 재샘플링 또는 경미한 수동 조정 필요.

## 엔지니어링 시사점

- **메시 복구를 먼저 확인**: 이는 파이프라인의 최대 시간 병목(제거 시 21.3 ± 22.8분/자산), 재현 시 토폴로지 복구 및 단순화 단계의 견고성을 우선 검증해야 함—그렇지 않으면 다운스트림 UV 언랩, 텍스처 베이킹, 볼록 분해가 모두 지연됨.
- **품질 검사기는 생략 불가**: 제거 시 인간 수용률 5.5%p 하락(표 내 96.5%→91.0% 계산), 그러나 자산당 0.4분만 절약—비용 효율이 극히 낮음. 이는 지각적 결함이 아닌 지오메트리 속성을 대상으로 하며, 자산 의미론적 완전성을 보장하는 핵심 방어선.
- **볼록 분해는 충돌 성공률의 최소 기준**: 절대 하락은 2.1%p에 불과하지만(표 내 98.6%→96.5% 계산), 저자는 이러한 접촉 오류가 장시간 조작에서 누적된다고 명시. 파지, 적재 등 접촉 집약적 작업에서는 CoACD 단계를 반드시 유지.
- **URDF 중간 표현은 크로스 시뮬레이터 이전의 지름길**: 팀이 MuJoCo와 Isaac Sim을 동시에 지원해야 한다면, URDF를 통합 형식으로 직접 채택하여 많은 형식 변환 적응 작업을 절약 가능.
- **가장 함정에 빠지기 쉬운 것은 공간 배치**: 83.3% 수용률은 약 1/6의 세계가 재샘플링 또는 수동 수정을 필요로 함을 의미, 주요 문제는 객체 스케일 불일치와 초기 배치 불완전성에 집중. 다운스트림 훈련 전에 SAPIEN 중력 침강 검증을 먼저 실행하고 재시도 메커니즘을 유지할 것을 권장.
- **장면 분포 스케일링 이점이 상당**: N=1에서 N=50 생성 장면으로, OOD 성공률 24.7%p 향상(표 내 53.2%→77.9% 계산), ID-OOD 격차가 41.1%p에서 2.6%p로 축소. 정책이 분포 외 성능이 나쁘다면 수동 튜닝보다 생성 장면 수를 우선 확장.
