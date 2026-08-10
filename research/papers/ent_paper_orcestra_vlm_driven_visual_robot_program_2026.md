---
$id: ent_paper_orcestra_vlm_driven_visual_robot_program_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
  zh: 'ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
  ko: 'ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
summary:
  en: ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided
    control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save
    robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin
    plans. Both interaction modes.
  zh: ORCESTRA 是一个由 Skoltech 智能空间机器人实验室与 MWS 研发中心开发的 Unity 6 独立应用，在 Quest 3 MR 头显上提供共置数字孪生环境，将无代码路点示教与 VLM 引导任务规范统一为可验证的机器人编程流程。其核心贡献在于将
    VLM 输出严格限定为待接地和验证的“提案”，通过共享验证层与确认门控，在物理执行前拦截错误目标与不可达姿态，并以机器人相对剧集格式实现跨实施例的编程复用。
  ko: ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided
    control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save
    robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin
    plans. Both interaction modes.
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
- orcestra
- vlm
- driven
- visual
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
  title: 'arXiv:2608.00775 ORCESTRA: VLM-driven Visual Robot programming in Mixed Reality'
  url: https://arxiv.org/abs/2608.00775
  date: '2026-08-01'
  accessed_at: '2026-08-05'
---

## 概述

ORCESTRA 是一个由 Skoltech 智能空间机器人实验室与 MWS 研发中心开发的 Unity 6 独立应用，在 Quest 3 MR 头显上提供共置数字孪生环境，将无代码路点示教与 VLM 引导任务规范统一为可验证的机器人编程流程。其核心贡献在于将 VLM 输出严格限定为待接地和验证的“提案”，通过共享验证层与确认门控，在物理执行前拦截错误目标与不可达姿态，并以机器人相对剧集格式实现跨实施例的编程复用。

## 它改变了什么

机器人编程长期面临“直接操作硬件成本高、迭代慢”的困境，而现有 VR 数字孪生系统又普遍与物理工作空间割裂，操作者只能在纯虚拟场景中观察，无法建立对真实环境的空间信任。ORCESTRA 真正改变的是将“语言引导”从不可靠的端到端生成，转变为“VLM 提案 + 客户端度量接地 + 人工确认”的闭环：它不再让 VLM 直接输出机器人命令，而是让模型返回图像空间参考与结构化计划，由客户端负责射线投射、碰撞检测和 IK 预解等确定性验证。这一设计把不确定性从执行层前移到验证层，使得语言编程在物理硬件上变得可审计、可取消、可重试。

另一个重要变化是它统一了两种编程范式——手动示教与语言规范——在同一个共置 MR 工作空间中。操作者既可以用控制器射线创建路点，也可以口头描述任务让 VLM 生成计划，两种模态最终都汇入相同的机器人相对剧集格式与验证管线。这打破了“示教器编程”与“自然语言编程”之间的工具壁垒，让同一套数字孪生基础设施同时服务熟练工程师与高层级任务描述者。

## 方法拆解

### 系统架构与运行模式
ORCESTRA 采用客户端—网关架构：Quest 3 客户端维护共置数字孪生、交互逻辑、场景接地、预览、验证与执行；轻量 FastAPI 网关连接 VLM（Qwen3-VL 经 vLLM/SGLang 服务，OpenAI 兼容端点）。支持桌面、沉浸式 VR、MR 透传三种模式，模式管理器切换相机、指针与透传配置，世界空间 UI 面板保持有效。

### 机器人放置与低层控制
操作者从目录选择机器人，ORCESTRA 生成半透明幽灵跟随控制器射线，MR 模式下落在检测到的水平表面上（否则为虚拟地板），确认前有位置与偏航微调面板。6-DOF 机械臂使用关节空间控制器与循环坐标下降（CCD）逆运动学求解器，支持关节/TCP 点动与关节驱动目标轨迹回放；回放时离线 IK 预解采样路径点生成关节轨迹，无需逐帧 IK。AgileX Scout V2 使用带物理车轮接触的差速驱动 go-to-goal 控制器。

### 无代码示教与剧集格式
操作者用控制器射线创建路点：机械臂用拇指杆推拉 3D 标记指定 TCP 目标，超出可达工作空间的目标被拒绝；移动基座以地板为示教平面指定路线点序列。ORCESTRA 拟合平滑样条并执行离线 CCD IK 预解。剧集以机器人相对格式存储（公式 1）：
E = (r, e, T₀, q₀, {pᵢ}ᵢ₌₁ᴺ, ρ)
其中 r 为机器人标识符，e 为实施例类型，T₀ 为记录时基座姿态，q₀ 为起始配置，{pᵢ} 为基座坐标系中的路点，ρ 为回放速率。路点位于基座坐标系，剧集随孪生体重定位而移动。

### VLM 引导规范与接地
VLM 作为高层级任务解释器，返回类型化 JSON（公式 2）：ℛ = (I, {gⱼ}ⱼ₌₁ᴹ, P_AI, D)，含解析意图 I、视觉接地 gⱼ（标签、置信度 κⱼ、图像空间参考）、中间计划 P_AI（种类、目标机器人、路点、允许接触标志 α）及诊断 D。客户端从活动相机投射射线（公式 3）：
R_u(t) = o + t·d(u)，取与 MR 场景第一个有效交点 x* = R_u(t*)，t* = min{t | R_u(t) ∈ 𝒞}；若无碰撞体交点且 R_u(t_Π) ∈ Π，则取回退地板平面交点。

### 共享验证层与确认门控
验证公式（公式 4）：valid(P_AI) = placed(r) ∧ kind(k,e) ∧ grounded_τ({gⱼ}) ∧ finite({wⱼ}) ∧ feasible_e(P_AI) ∧ ¬α。要求：机器人已实例化、计划种类匹配实施例、视觉参考置信度高于 τ、路点坐标有限、计划可实现（机械臂为可达性加 IK 预解，移动基座为带障碍检查的路线有效性）。仅有效计划被预览，操作者确认后执行才开始——这是 ORCESTRA 的核心安全设计。

## 关键创新

1. **VLM 作为提案者而非控制器**：将大语言模型的输出严格限定为“待验证的假设”，所有度量接地、碰撞检测与 IK 可行性检查都在客户端确定性完成。这一分层避免了 VLM 幻觉直接传导至物理执行，是语言编程安全性的关键架构决策。

2. **机器人相对剧集格式**：路点存储于基座坐标系而非世界坐标系，使剧集可随孪生体重定位而移动，同一段示教可在不同放置位置复用。这为跨实施例、跨场景的编程迁移提供了统一数据载体。

3. **共置 MR 验证层**：在物理工作空间内叠加数字孪生，操作者可以在真实环境中观察虚拟机器人执行轨迹，确认门控让每一次语言引导的编程都经过人工预览。这种“物理共置 + 虚拟验证”的组合，比纯 VR 或纯仿真更贴近实际部署条件。

## 实验与结果

实验在 Quest 3 上作为完整集成 MR 原型评估，VLM 网关运行在工作站 GPU 上，目标不是与示教器编程比较，而是验证系统在异构实施例和两种模态下端到端工作。无代码示教在 UR3、KUKA KR 600 FORTEC 和 AgileX Scout V2 上测试通过。语言引导接地用户验证：5 名参与者，每人从 4 个递增复杂度类别中各对一个对象发出一次重定位命令，共 20 次试验。

| 对象类别 | 成功率 |
|---------|--------|
| 简单几何（立方体、球） | 5/5 |
| 日常（水瓶） | 5/5 |
| 非常规（手工具） | 4/5 |
| 大型/大体积（箱子） | 1/5 |

所有失败均在预览阶段被捕获，验证了确认门控安全层的有效性。大型对象成功率显著下降，因其尺寸和几何使单一、视觉合理的抓取点更难定义和接近。

## 边界与局限

原型没有夹爪，研究隔离了 VLM 侧理解而非物理抓取执行，因此抓取点合理性仅停留在视觉层面。大型、大体积对象是当前最大短板，单点接地无法处理需要双臂或多接触的操作。论文未与示教器编程进行对比评估，也未涉及物理控制器导出与真实硬件执行。透传深度和场景网格尚未替代水平面回退，基于约束的规划与多指夹爪闭环均列为未来工作。论文未明确系统在真实物理机器人上的端到端延迟与可靠性数据。

## 工程启示

复现时先核对三点：一是 VLM 端点是否严格遵循 OpenAI 兼容协议，Qwen3-VL 经 vLLM/SGLang 部署时的 JSON 输出格式必须与公式 2 完全匹配，否则客户端解析会失败；二是 CCD IK 预解的采样密度与回放速率 ρ 的配合，离线预解虽免去逐帧 IK，但路径点过疏会导致轨迹抖动，过密则增加加载时间；三是 MR 场景碰撞体 𝒞 的构建质量——射线投射的接地精度直接取决于物理对象与 MR 平面的碰撞体是否完整，这是最容易踩坑的地方。

对下游团队，建议优先扩展大型对象的接地策略，单点射线投射在箱子类目标上成功率仅 1/5，可考虑多点采样或体积包围盒替代单点参考。确认门控是安全底线，不要为了流畅体验跳过验证层。机器人相对剧集格式值得借鉴，但要注意 q₀ 的起始配置记录——若机器人加载时未正确回到 q₀，回放会从错误姿态开始。最后，若需部署到真实硬件，务必先完成物理控制器导出接口的闭环测试，当前原型尚未覆盖这一环节。

## Overview
ORCESTRA is a mixed-reality system for programming robot digital twins through no-code waypoint teaching and language-guided control. In a passthrough mixed-reality workspace, users place robot twins on real surfaces, teach trajectories, save robot-relative episodes, or issue spoken/typed commands that a vision-language model converts into structured digital-twin plans. Both interaction modes share a backend for metric grounding, embodiment-aware validation, preview, confirmation, and digital-twin execution. The system supports heterogeneous robot embodiments, including fixed-base manipulators, a mobile base, and a humanoid robot, demonstrating MR validation as a safety layer for language-guided robot programming before physical deployment.

## 参考
- https://arxiv.org/abs/2608.00775

## 개요

ORCESTRA는 Skoltech 지능형 우주 로봇 연구실과 MWS 연구개발 센터가 개발한 Unity 6 독립 실행형 애플리케이션으로, Quest 3 MR 헤드셋에서 공동 배치된 디지털 트윈 환경을 제공하며, 코드 없는 웨이포인트 시연과 VLM 기반 작업 사양을 검증 가능한 로봇 프로그래밍 워크플로우로 통합합니다. 핵심 기여는 VLM 출력을 접지 및 검증 대상인 "제안"으로 엄격히 제한하고, 공유 검증 계층과 확인 게이트를 통해 물리적 실행 전에 잘못된 대상과 도달 불가능한 자세를 차단하며, 로봇 상대 에피소드 형식으로 교차 구현 프로그래밍 재사용을 실현한다는 점입니다.

## 무엇을 바꾸는가

로봇 프로그래밍은 오랫동안 "하드웨어 직접 조작의 높은 비용과 느린 반복"이라는 어려움에 직면해 왔으며, 기존 VR 디지털 트윈 시스템은 일반적으로 물리적 작업 공간과 단절되어 있어 작업자는 순수 가상 시나리오에서만 관찰할 수 있고 실제 환경에 대한 공간적 신뢰를 구축할 수 없었습니다. ORCESTRA가 진정으로 바꾸는 것은 "언어 유도"를 신뢰할 수 없는 종단 간 생성에서 "VLM 제안 + 클라이언트 측정 접지 + 인간 확인"의 폐쇄 루프로 전환하는 것입니다. 더 이상 VLM이 로봇 명령을 직접 출력하지 않고, 모델이 이미지 공간 참조와 구조화된 계획을 반환하며, 클라이언트가 레이 캐스팅, 충돌 감지, IK 사전 해석 등의 결정적 검증을 담당합니다. 이 설계는 불확실성을 실행 계층에서 검증 계층으로 전진시켜, 언어 프로그래밍이 물리적 하드웨어에서 감사 가능하고 취소 가능하며 재시도 가능하게 만듭니다.

또 다른 중요한 변화는 수동 시연과 언어 사양이라는 두 가지 프로그래밍 패러다임을 동일한 공동 배치 MR 작업 공간에서 통합한다는 점입니다. 작업자는 컨트롤러 레이로 웨이포인트를 생성하거나 음성으로 작업을 설명하여 VLM이 계획을 생성하도록 할 수 있으며, 두 가지 모달리티는 궁극적으로 동일한 로봇 상대 에피소드 형식과 검증 파이프라인으로 수렴합니다. 이는 "시연기 프로그래밍"과 "자연어 프로그래밍" 사이의 도구 장벽을 허물어, 동일한 디지털 트윈 인프라가 숙련된 엔지니어와 고수준 작업 설명자 모두에게 서비스를 제공할 수 있게 합니다.

## 방법 분해

### 시스템 아키텍처 및 실행 모드
ORCESTRA는 클라이언트-게이트웨이 아키텍처를 채택합니다. Quest 3 클라이언트는 공동 배치 디지털 트윈, 상호작용 로직, 장면 접지, 미리보기, 검증 및 실행을 유지하며, 경량 FastAPI 게이트웨이는 VLM(Qwen3-VL이 vLLM/SGLang을 통해 서비스되고 OpenAI 호환 엔드포인트 사용)을 연결합니다. 데스크톱, 몰입형 VR, MR 투시의 세 가지 모드를 지원하며, 모드 관리자가 카메라, 포인터 및 투시 구성을 전환하고 월드 공간 UI 패널은 유효하게 유지됩니다.

### 로봇 배치 및 저수준 제어
작업자는 카탈로그에서 로봇을 선택하며, ORCESTRA는 반투명 고스트가 컨트롤러 레이를 따라가도록 생성하고, MR 모드에서는 감지된 수평 표면(그렇지 않으면 가상 바닥)에 배치하며, 확인 전에 위치 및 요 미세 조정 패널이 제공됩니다. 6-DOF 매니퓰레이터는 관절 공간 컨트롤러와 순환 좌표 하강(CCD) 역운동학 솔버를 사용하며, 관절/TCP 조그 및 관절 구동 목표 궤적 재생을 지원합니다. 재생 시 오프라인 IK 사전 해석이 경로점을 샘플링하여 관절 궤적을 생성하므로 프레임별 IK가 필요 없습니다. AgileX Scout V2는 물리적 바퀴 접촉이 있는 차동 구동 go-to-goal 컨트롤러를 사용합니다.

### 코드 없는 시연 및 에피소드 형식
작업자는 컨트롤러 레이로 웨이포인트를 생성합니다. 매니퓰레이터는 썸스틱으로 3D 마커를 밀고 당겨 TCP 대상을 지정하며, 도달 가능한 작업 공간을 벗어난 대상은 거부됩니다. 이동 베이스는 바닥을 시연 평면으로 사용하여 경로점 시퀀스를 지정합니다. ORCESTRA는 부드러운 스플라인을 피팅하고 오프라인 CCD IK 사전 해석을 수행합니다. 에피소드는 로봇 상대 형식(수식 1)으로 저장됩니다.
E = (r, e, T₀, q₀, {pᵢ}ᵢ₌₁ᴺ, ρ)
여기서 r은 로봇 식별자, e는 구현 유형, T₀는 기록 시 베이스 자세, q₀는 시작 구성, {pᵢ}는 베이스 좌표계의 웨이포인트, ρ는 재생 속도입니다. 웨이포인트는 베이스 좌표계에 있으며, 에피소드는 트윈의 재배치에 따라 이동합니다.

### VLM 기반 사양 및 접지
VLM은 고수준 작업 해석기로 작동하며, 타입이 지정된 JSON(수식 2)을 반환합니다. ℛ = (I, {gⱼ}ⱼ₌₁ᴹ, P_AI, D)는 해석된 의도 I, 시각적 접지 gⱼ(레이블, 신뢰도 κⱼ, 이미지 공간 참조), 중간 계획 P_AI(종류, 대상 로봇, 웨이포인트, 접촉 허용 플래그 α) 및 진단 D를 포함합니다. 클라이언트는 활성 카메라에서 레이를 투사합니다(수식 3).
R_u(t) = o + t·d(u), MR 장면과의 첫 번째 유효 교차점 x* = R_u(t*), t* = min{t | R_u(t) ∈ 𝒞}을 취하며, 충돌체 교차점이 없고 R_u(t_Π) ∈ Π이면 폴백 바닥 평면 교차점을 취합니다.

### 공유 검증 계층 및 확인 게이트
검증 수식(수식 4): valid(P_AI) = placed(r) ∧ kind(k,e) ∧ grounded_τ({gⱼ}) ∧ finite({wⱼ}) ∧ feasible_e(P_AI) ∧ ¬α. 요구 사항: 로봇이 인스턴스화되고, 계획 종류가 구현과 일치하며, 시각적 참조 신뢰도가 τ보다 높고, 웨이포인트 좌표가 유한하며, 계획이 실현 가능해야 합니다(매니퓰레이터는 도달 가능성 및 IK 사전 해석, 이동 베이스는 장애물 검사가 포함된 경로 유효성). 유효한 계획만 미리보기되며, 작업자 확인 후에만 실행이 시작됩니다. 이것이 ORCESTRA의 핵심 안전 설계입니다.

## 핵심 혁신

1. **VLM을 제어기가 아닌 제안자로 사용**: 대규모 언어 모델의 출력을 "검증 대상 가설"로 엄격히 제한하며, 모든 측정 접지, 충돌 감지 및 IK 실현 가능성 검사는 클라이언트에서 결정적으로 완료됩니다. 이 계층화는 VLM 환각이 물리적 실행으로 직접 전달되는 것을 방지하며, 언어 프로그래밍 안전성의 핵심 아키텍처 결정입니다.

2. **로봇 상대 에피소드 형식**: 웨이포인트가 월드 좌표계가 아닌 베이스 좌표계에 저장되어 에피소드가 트윈의 재배치에 따라 이동할 수 있으며, 동일한 시연이 다른 배치 위치에서 재사용될 수 있습니다. 이는 교차 구현, 교차 장면 프로그래밍 전이를 위한 통합 데이터 매체를 제공합니다.

3. **공동 배치 MR 검증 계층**: 물리적 작업 공간에 디지털 트윈을 오버레이하여 작업자가 실제 환경에서 가상 로봇의 실행 궤적을 관찰할 수 있으며, 확인 게이트는 모든 언어 유도 프로그래밍이 인간 미리보기를 거치도록 보장합니다. 이 "물리적 공동 배치 + 가상 검증"의 조합은 순수 VR이나 순수 시뮬레이션보다 실제 배포 조건에 더 가깝습니다.

## 실험 및 결과

실험은 Quest 3에서 완전히 통합된 MR 프로토타입으로 평가되었으며, VLM 게이트웨이는 워크스테이션 GPU에서 실행되었습니다. 목표는 시연기 프로그래밍과의 비교가 아니라 이기종 구현과 두 가지 모달리티에서 시스템이 종단 간 작동함을 검증하는 것이었습니다. 코드 없는 시연은 UR3, KUKA KR 600 FORTEC 및 AgileX Scout V2에서 테스트되었습니다. 언어 유도 접지 사용자 검증: 5명의 참가자가 각각 4개의 증가하는 복잡성 범주에서 각각 하나의 객체에 대해 재배치 명령을 한 번씩 내려 총 20회의 시행이 이루어졌습니다.

| 객체 범주 | 성공률 |
|---------|--------|
| 단순 기하(큐브, 구) | 5/5 |
| 일상(물병) | 5/5 |
| 비정형(수공구) | 4/5 |
| 대형/대용량(상자) | 1/5 |

모든 실패는 미리보기 단계에서 포착되어 확인 게이트 안전 계층의 유효성을 검증했습니다. 대형 객체의 성공률은 크기와 기하학으로 인해 단일하고 시각적으로 타당한 파지점을 정의하고 접근하기 어렵기 때문에 현저히 감소했습니다.

## 경계 및 한계

프로토타입에는 그리퍼가 없으며, 연구는 물리적 파지 실행이 아닌 VLM 측 이해를 격리했으므로 파지점 타당성은 시각적 수준에만 머물렀습니다. 대형, 대용량 객체는 현재 가장 큰 약점이며, 단일 점 접지는 양팔 또는 다중 접촉이 필요한 조작을 처리할 수 없습니다. 논문은 시연기 프로그래밍과의 비교 평가를 수행하지 않았으며, 물리적 컨트롤러 내보내기 및 실제 하드웨어 실행도 다루지 않았습니다. 투시 깊이와 장면 메시는 아직 수평면 폴백을 대체하지 못했으며, 제약 기반 계획과 다중 핑거 그리퍼 폐쇄 루프는 모두 향후 작업으로 나열되었습니다. 논문은 실제 물리적 로봇에서의 종단 간 지연 및 신뢰성 데이터를 명시하지 않았습니다.

## 공학적 시사점

재현 시 세 가지를 먼저 확인하십시오. 첫째, VLM 엔드포인트가 OpenAI 호환 프로토콜을 엄격히 따르는지, Qwen3-VL이 vLLM/SGLang으로 배포될 때 JSON 출력 형식이 수식 2와 완전히 일치해야 하며, 그렇지 않으면 클라이언트 파싱이 실패합니다. 둘째, CCD IK 사전 해석의 샘플링 밀도와 재생 속도 ρ의 조화로, 오프라인 사전 해석은 프레임별 IK를 피하지만 경로점이 너무 드물면 궤적이 떨리고 너무 조밀하면 로딩 시간이 증가합니다. 셋째, MR 장면 충돌체 𝒞의 구축 품질입니다. 레이 캐스팅의 접지 정확도는 물리적 객체와 MR 평면의 충돌체가 완전한지에 직접적으로 달려 있으며, 이것이 가장 함정에 빠지기 쉬운 지점입니다.

하류 팀에게는 대형 객체의 접지 전략을 우선 확장할 것을 권장합니다. 단일 점 레이 투사는 상자류 대상에서 성공률이 1/5에 불과하므로, 다중 점 샘플링이나 볼륨 경계 상자로 단일 점 참조를 대체할 수 있습니다. 확인 게이트는 안전의 최소 기준이므로 원활한 경험을 위해 검증 계층을 건너뛰지 마십시오. 로봇 상대 에피소드 형식은 차용할 가치가 있지만, q₀의 시작 구성 기록에 주의하십시오. 로봇이 로드 시 q₀로 올바르게 복귀하지 않으면 재생이 잘못된 자세에서 시작됩니다. 마지막으로 실제 하드웨어에 배포해야 한다면 물리적 컨트롤러 내보내기 인터페이스의 폐쇄 루프 테스트를 먼저 완료해야 하며, 현재 프로토타입은 이 단계를 다루지 않습니다.
