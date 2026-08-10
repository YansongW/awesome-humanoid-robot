---
$id: ent_paper_hifi_umi_deployable_manipulation_policie_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone'
  zh: 'HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone'
  ko: 'HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone'
summary:
  en: Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable.
    Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice
    uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising
    the fidelity of robot-free UMI.
  zh: HiFi-UMI 提出一套硬件与软件协同设计的高保真无机器人数据采集系统，并验证“零机器人后训练”假设：仅用高保真 UMI 数据微调，即可在三个骨干网络（StarVLA-QwenPI、OpenPI-π₀.₅、LingBot-VA）上获得与真实遥操作后训练相当的真实机器人部署成功率。核心贡献在于将保真度（轨迹精度、夹爪相对位姿、同步、视场角）作为设计原则，而非依赖真实机器人锚点数据。
  ko: Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable.
    Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice
    uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising
    the fidelity of robot-free UMI.
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
- hifi
- umi
- deployable
- manipulation
- policie
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
  title: 'arXiv:2607.25895 HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data '
  url: https://arxiv.org/abs/2607.25895
  date: '2026-07-28'
  accessed_at: '2026-08-05'
---

## 概述

HiFi-UMI 提出一套硬件与软件协同设计的高保真无机器人数据采集系统，并验证“零机器人后训练”假设：仅用高保真 UMI 数据微调，即可在三个骨干网络（StarVLA-QwenPI、OpenPI-π₀.₅、LingBot-VA）上获得与真实遥操作后训练相当的真实机器人部署成功率。核心贡献在于将保真度（轨迹精度、夹爪相对位姿、同步、视场角）作为设计原则，而非依赖真实机器人锚点数据。

## 它改变了什么

过去行业默认 UMI 这类无机器人数据只能做预训练，后训练必须掺入少量真实遥操作“锚点”才能部署。作者质疑的不是数据量，而是保真度——如果无机器人数据在轨迹精度、时间同步、夹爪重建上做到与遥操作同等水平，锚点是否根本不需要。这个问题的价值在于：遥操作采集的墙钟成本是 UMI 的数倍，且受限于单一物理环境；若高保真 UMI 能独立支撑后训练，数据生产范式将从“稀缺但精准”转向“海量且精准”。

它真正改变的是数据采集的“精度-规模”权衡曲线。此前手持设备在长时程漂移、夹爪相对位姿重建误差、软同步抖动、单目盲区四个维度上妥协，导致下游策略必须依赖真实机器人数据纠偏。HiFi-UMI 把每个妥协点都换成原生测量或硬件级方案，使无机器人数据首次具备与域内遥操作同等的“动作对齐”质量。

## 方法拆解

### 数据生产系统（四轴保真度设计）
- **轨迹精度**：头戴式离线立体惯性 SLAM（ORB-SLAM3）+ AprilTag 标记定位。头部相机估计全局轨迹，每只手通过刚性连接的标记立方体在头部坐标系中定位，组合得到全局一致双手轨迹。设计理由：头戴视角比腕部视角更稳定，腕部在操作中常被自遮挡和快速运动破坏。
- **夹爪相对位姿**：两个标记立方体在同一头部相机帧中观测，相对位姿被原生测量，继承单夹爪精度，而非事后从跨相机共视重建。
- **同步**：所有传感器由单一 GPIO 外部触发，微秒级（< 40 μs）时间对齐，取代软件或无线方案。
- **视场角**：每只手两个非平行鱼眼相机，约 200° 覆盖；完整设备六相机。

### 离线 SLAM 策略
刻意放弃全局回环闭合，改为动态滑动窗口局部一致性约束，将长时程漂移限制在厘米级、保持毫米级局部精度。SLAM 随机失败时自动重算异常轨迹。

### 数据处理流水线（六阶段）
采集与上传 → 轨迹重建与自动清理 → 仿真重定向（全身运动控制回放，丢弃动力学不可行轨迹）→ AI 辅助标注（多视角联合推理，低置信度路由人工）→ 人工验证（采样检查+结构化 QC 元数据）→ 分析与导出（任务属性平衡组装训练集）。

### 动作表示
- 机器人中心末端执行器坐标系，预测相对位姿增量 + 绝对夹爪开度。
- 块内每个未来位姿相对同一当前观测锚点：ΔT = (T_t0^j)^(-1) T_(t0+δ_h)^(m)，不递归依赖前一个动作目标。
- 每臂 3+6+1=10 通道，双手 20 通道；平移在锚点坐标系表达，旋转用 Rotation6D。

### 骨干网络适配
- **StarVLA-QwenPI**：Qwen3-VL-4B + π 风格条件流匹配 DiT 头，36 层交叉注意力 + 奇数块后自注意力残差，8 步欧拉推理。
- **OpenPI-π₀.₅**：PaliGemma 视觉流 + Gemma 连续动作专家，本体感觉离散化序列化，10 步欧拉。
- **LingBot-VA**：因果 WAM，先预测未来视频潜变量再逆动力学解码动作，块因果掩码。

## 关键创新

1. **零机器人后训练假设的直接验证**：在三个骨干上，仅用 HiFi-UMI 后训练与域内遥操作后训练的成功率差异在 ±3.1 个百分点内且方向不一致，首次系统证明无机器人数据可独立支撑部署级策略微调。
2. **保真度作为设计原则而非消融变量**：作者明确不做受控退化隔离，而是把轨迹精度、原生相对位姿、硬件同步、宽视场角四个轴一次性做到位。这种“整体验证”策略在工程上更务实——先证明可行，再分解贡献。
3. **数据生产管线的规模化验证**：20,000+ 小时数据、96% 累积通过率（两个串联门各约 98%）、3 mm 局部精度，证明高保真采集不是实验室演示，而是可扩展的工业级数据引擎。

## 实验与结果

### 零机器人后训练对比（每任务 40 次 rollout）
| 骨干 | UMI 后训练 | 遥操作后训练 | 差异 |
|---|---|---|---|
| StarVLA-QwenPI | 51.3% | 53.8% | -2.5 个百分点 |
| OpenPI-π₀.₅ | 77.5% | 74.4% | +3.1 个百分点 |
| LingBot-VA | 56.9% | 57.5% | -0.6 个百分点 |
关键点：遥操作数据在评估场景中采集，UMI 数据不在——此不对称性有利于基线，但 UMI 仍能持平。
### 数据缩放（Remote Insertion，OpenPI-π₀.₅）
| 演示数 | 成功率 |
|---|---|
| 400 | 37.5% |
| 800 | 65.0% |
| 3,200 | 85.0% |
| 6,400 | 82.5% |
约 3,200 episodes 后饱和，6,400 无增益。
### 预训练效果（StarVLA-QwenPI，4,000 小时）
- 留出动作误差一个 pass 内下降 61%，幂律 α=0.268，R²=0.993。
- 十个未见任务 OOD 误差平均降低 41%。
- 四任务基准成功率提升 18.1 个百分点；800 个任务 episodes 即超过随机初始化基线在 3,200 episodes 的表现。
### WAM 诊断（LingBot-VA，ground-truth-video 条件）
| 条件 | XYZ RMSE (mm) | SO(3) 误差 (°) |
|---|---|---|
| UMI → Real | 24.33 | 0.65 |
| UMI → UMI | 21.13 | 0.88 |
| 遥操作 → Real | 21.64 | 0.46 |
| 随机 → Real | 117.57 | 126.47 |
UMI → Real 相对随机参考降低平移误差 79.3%、旋转误差 99.5%，跨域差异仅 3.20 mm 平移。
（本节另有 1 句含无法从全文文本核实的数字，已按纪律移除；论文未明确或以图/表图片形式给出。）

## 边界与局限

- **保真度未分解**：作者明确未做受控退化消融，无法归因各保真度轴的边际贡献。
- **场景不对称性未消除**：遥操作数据在评估场景采集，UMI 数据不在，作者承认这是对 UMI 的保守测试，但未做对称设计。
- **初始化轴仅测一个骨干**：UMI 预训练 + UMI 后训练仅在 StarVLA-QwenPI 上实例化，OpenPI-π₀.₅ 和 LingBot-VA 未参与。
- **任务级统计分辨率低**：每任务 40 次 rollout，一次成功改变 2.5 个百分点，任务级差异视为描述性。
- **数据效率非样本匹配**：UMI 后训练用 3,200 条轨迹 vs 遥操作 300 条，约 10 倍差距，未做等样本对比。
- **失败案例分析缺失**：论文未报告系统性失败模式分类。

## 工程启示

- **复现优先核对同步与相对位姿**：GPIO 硬件触发（< 40 μs）和原生夹爪相对位姿测量是 HiFi-UMI 与先前系统最本质的差异。若复现时退化为软件同步或跨相机重建，成功率差距可能重新出现。
- **数据过滤是隐形成本**：96% 累积通过率来自两个串联门（轨迹重建约 98%、全身控制回放约 98%）。下游团队应预留约 4% 的原始数据损耗，并确保过滤在训练/验证分割前完成，防止近重复窗口跨分割泄漏。
- **动作表示锚点设计需严格遵循**：块内所有未来位姿相对同一当前观测锚点（ΔT = (T_t0^j)^(-1) T_(t0+δ_h)^(m)），不要递归依赖前一个动作目标——这是跨骨干迁移时最容易踩坑的地方。
- **夹爪通道需单独处理**：UMI 保留操作者手部手势角度，真实遥操作无抓取时默认全开，物理语义未校准。主分析排除夹爪通道，下游若需使用应单独校准。
- **预训练收益在数据量 4 倍差距下仍显著**：800 个任务 episodes 超过随机初始化基线在 3,200 episodes 的表现，说明大规模 UMI 预训练是数据效率杠杆，但仅在 StarVLA-QwenPI 上验证，迁移到其他骨干需谨慎。

## Overview
Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable. Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising the fidelity of robot-free UMI data, rather than shrinking the real-robot fraction, can remove that anchor. We present HiFi-UMI, a portable UMI data-production system co-designed for trajectory accuracy, inter-gripper relative pose, synchronization, and field of view: head-mounted offline stereo-inertial SLAM, native rather than reconstructed relative pose, a shared microsecond GPIO trigger, and two wide-angle cameras per hand covering ~200 degrees. It reaches 3 mm workspace-local end-effector accuracy without external tracking infrastructure. Using this corpus, we demonstrate zero-robot post-training: a policy post-trained solely on HiFi-UMI demonstrations deploys directly on a real robot and matches in-domain teleoperation across three backbones spanning the vision-language-action and world-action-model families, with success-rate differences of -2.5, +3.1, and -0.6 percentage points on StarVLA-QwenPI, OpenPI-pi_0.5, and LingBot-VA; the strongest policy reaches 85% on a precision insertion task, even though the teleoperation baseline is collected in the evaluation scene and no HiFi-UMI trajectory is. Pre-training on 4,000 hours from the same corpus lowers action error on ten unseen tasks by 41% and, on StarVLA-QwenPI, raises real-robot success by a further 18.1 percentage points. We open-source HiFi-UMI-2K, 2,000 hours of microsecond-synchronized, ultra-wide-FoV demonstrations, each automatically reconstructed and validated through simulation replay, as a large-scale, high-fidelity resource for the robot-learning community.

## 参考
- https://arxiv.org/abs/2607.25895

## 개요

HiFi-UMI는 하드웨어와 소프트웨어의 협력 설계를 통한 고충실도 로봇-프리 데이터 수집 시스템을 제안하며, "제로 로봇 후훈련" 가설을 검증한다: 고충실도 UMI 데이터만으로 미세 조정하여 세 가지 백본 네트워크(StarVLA-QwenPI, OpenPI-π₀.₅, LingBot-VA)에서 실제 원격 조작 후훈련과 동등한 실제 로봇 배포 성공률을 달성할 수 있다. 핵심 기여는 충실도(궤적 정밀도, 그리퍼 상대 자세, 동기화, 시야각)를 설계 원칙으로 삼고, 실제 로봇 앵커 데이터에 의존하지 않는 것이다.

## 무엇을 바꾸는가

과거 업계는 UMI와 같은 로봇-프리 데이터는 사전 훈련에만 사용할 수 있고, 후훈련에는 소량의 실제 원격 조작 "앵커"를 혼합해야 배포가 가능하다고 기본 전제로 삼았다. 저자가 의문을 제기하는 것은 데이터 양이 아니라 충실도다—로봇-프리 데이터가 궤적 정밀도, 시간 동기화, 그리퍼 재구성에서 원격 조작과 동등한 수준을 달성한다면, 앵커가 정말 필요 없는가? 이 질문의 가치는: 원격 조작 수집의 벽시계 비용은 UMI의 수 배이며, 단일 물리 환경에 제한된다. 고충실도 UMI가 독립적으로 후훈련을 지원할 수 있다면, 데이터 생산 패러다임은 "희소하지만 정밀"에서 "대규모이면서 정밀"로 전환된다.

진정으로 바꾸는 것은 데이터 수집의 "정밀도-규모" 트레이드오프 곡선이다. 기존 핸드헬드 장치는 장시간 드리프트, 그리퍼 상대 자세 재구성 오차, 소프트 동기화 지터, 단안 사각지대의 네 가지 차원에서 타협하여, 하위 정책이 실제 로봇 데이터에 의존하여 오류를 보정해야 했다. HiFi-UMI는 각 타협 지점을 네이티브 측정 또는 하드웨어 수준 솔루션으로 대체하여, 로봇-프리 데이터가 처음으로 도메인 내 원격 조작과 동등한 "동작 정렬" 품질을 갖추게 한다.

## 방법 분해

### 데이터 생산 시스템(4축 충실도 설계)
- **궤적 정밀도**: 헤드마운트 오프라인 스테레오 관성 SLAM(ORB-SLAM3) + AprilTag 마커 위치 추정. 헤드 카메라가 전역 궤적을 추정하고, 각 손은 강체 연결된 마커 큐브를 통해 헤드 좌표계에서 위치가 결정되어, 전역적으로 일관된 양손 궤적을 얻는다. 설계 근거: 헤드마운트 시점은 손목 시점보다 안정적이며, 손목은 조작 중 자주 자기 가림과 빠른 움직임으로 손상된다.
- **그리퍼 상대 자세**: 두 마커 큐브가 동일한 헤드 카메라 프레임에서 관측되어, 상대 자세가 네이티브로 측정되며 단일 그리퍼 정밀도를 상속한다. 사후에 교차 카메라 공동 시야에서 재구성하지 않는다.
- **동기화**: 모든 센서는 단일 GPIO 외부 트리거로 마이크로초(< 40 μs) 시간 정렬을 달성하며, 소프트웨어 또는 무선 방식을 대체한다.
- **시야각**: 각 손에 두 개의 비평행 어안 카메라로 약 200° 커버리지; 전체 장치는 6개 카메라.

### 오프라인 SLAM 전략
의도적으로 전역 루프 폐쇄를 포기하고, 동적 슬라이딩 윈도우 로컬 일관성 제약으로 대체하여 장시간 드리프트를 센티미터 수준으로 제한하고 밀리미터 수준의 로컬 정밀도를 유지한다. SLAM이 무작위로 실패하면 이상 궤적을 자동으로 재계산한다.

### 데이터 처리 파이프라인(6단계)
수집 및 업로드 → 궤적 재구성 및 자동 정리 → 시뮬레이션 리타게팅(전신 운동 제어 재생, 동역학적으로 불가능한 궤적 폐기) → AI 보조 주석(다중 시점 공동 추론, 낮은 신뢰도는 수동 라우팅) → 수동 검증(샘플링 검사 + 구조화 QC 메타데이터) → 분석 및 내보내기(작업 속성 균형 훈련 세트 조립).

### 동작 표현
- 로봇 중심 엔드 이펙터 좌표계, 상대 자세 증분 + 절대 그리퍼 개방도 예측.
- 블록 내 각 미래 자세는 동일한 현재 관측 앵커를 기준으로: ΔT = (T_t0^j)^(-1) T_(t0+δ_h)^(m), 이전 동작 목표에 재귀적으로 의존하지 않는다.
- 각 팔 3+6+1=10채널, 양손 20채널; 병진은 앵커 좌표계로 표현, 회전은 Rotation6D 사용.

### 백본 네트워크 적응
- **StarVLA-QwenPI**: Qwen3-VL-4B + π 스타일 조건부 흐름 매칭 DiT 헤드, 36층 교차 어텐션 + 홀수 블록 후 자기 어텐션 잔차, 8단계 오일러 추론.
- **OpenPI-π₀.₅**: PaliGemma 비전 스트림 + Gemma 연속 동작 전문가, 고유 감각 이산화 직렬화, 10단계 오일러.
- **LingBot-VA**: 인과 WAM, 먼저 미래 비디오 잠재 변수를 예측한 후 역동역학 디코더로 동작을 해독, 블록 인과 마스크.

## 핵심 혁신

1. **제로 로봇 후훈련 가설의 직접 검증**: 세 가지 백본에서 HiFi-UMI 후훈련만으로 도메인 내 원격 조작 후훈련과의 성공률 차이가 ±3.1% 포인트 이내이며 방향이 일관되지 않아, 로봇-프리 데이터가 독립적으로 배포 수준 정책 미세 조정을 지원할 수 있음을 처음으로 체계적으로 증명했다.
2. **충실도를 소거 변수가 아닌 설계 원칙으로**: 저자는 의도적으로 통제된 열화 분리를 수행하지 않고, 궤적 정밀도, 네이티브 상대 자세, 하드웨어 동기화, 넓은 시야각의 네 축을 한 번에 완성했다. 이러한 "전체 검증" 전략은 공학적으로 더 실용적이다—먼저 가능성을 증명하고, 그 다음 기여를 분해한다.
3. **데이터 생산 파이프라인의 대규모 검증**: 20,000+ 시간 데이터, 96% 누적 통과율(두 직렬 게이트 각각 약 98%), 3mm 로컬 정밀도는 고충실도 수집이 실험실 시연이 아니라 확장 가능한 산업급 데이터 엔진임을 증명한다.

## 실험 및 결과

### 제로 로봇 후훈련 비교(작업당 40회 롤아웃)
| 백본 | UMI 후훈련 | 원격 조작 후훈련 | 차이 |
|---|---|---|---|
| StarVLA-QwenPI | 51.3% | 53.8% | -2.5% 포인트 |
| OpenPI-π₀.₅ | 77.5% | 74.4% | +3.1% 포인트 |
| LingBot-VA | 56.9% | 57.5% | -0.6% 포인트 |
핵심: 원격 조작 데이터는 평가 시나리오에서 수집되고, UMI 데이터는 그렇지 않다—이 비대칭성은 기준선에 유리하지만 UMI는 여전히 동등한 성능을 보인다.
### 데이터 스케일링(Remote Insertion, OpenPI-π₀.₅)
| 데모 수 | 성공률 |
|---|---|
| 400 | 37.5% |
| 800 | 65.0% |
| 3,200 | 85.0% |
| 6,400 | 82.5% |
약 3,200 에피소드 후 포화, 6,400에서 이득 없음.
### 사전 훈련 효과(StarVLA-QwenPI, 4,000시간)
- 홀드아웃 동작 오차가 한 패스 내 61% 감소, 멱법칙 α=0.268, R²=0.993.
- 10개의 미지 작업 OOD 오차 평균 41% 감소.
- 4개 작업 기준 성공률 18.1% 포인트 향상; 800개 작업 에피소드로 무작위 초기화 기준선의 3,200 에피소드 성능을 초과.
### WAM 진단(LingBot-VA, ground-truth-video 조건)
| 조건 | XYZ RMSE (mm) | SO(3) 오차 (°) |
|---|---|---|
| UMI → Real | 24.33 | 0.65 |
| UMI → UMI | 21.13 | 0.88 |
| 원격 조작 → Real | 21.64 | 0.46 |
| 무작위 → Real | 117.57 | 126.47 |
UMI → Real은 무작위 기준 대비 병진 오차 79.3%, 회전 오차 99.5% 감소, 교차 도메인 차이는 병진 3.20mm에 불과.
(이 섹션에는 전체 텍스트에서 확인할 수 없는 숫자가 포함된 문장이 1개 있어 규율에 따라 제거됨; 논문에 명시되지 않았거나 그림/표 이미지로 제공됨.)

## 경계 및 한계

- **충실도 미분해**: 저자는 의도적으로 통제된 열화 소거를 수행하지 않아, 각 충실도 축의 한계 기여를 귀인할 수 없다.
- **시나리오 비대칭성 미해소**: 원격 조작 데이터는 평가 시나리오에서 수집되고, UMI 데이터는 그렇지 않다. 저자는 이를 UMI에 대한 보수적 테스트로 인정하지만, 대칭 설계는 수행하지 않았다.
- **초기화 축은 하나의 백본만 테스트**: UMI 사전 훈련 + UMI 후훈련은 StarVLA-QwenPI에서만 구현되었고, OpenPI-π₀.₅와 LingBot-VA는 참여하지 않았다.
- **작업 수준 통계 해상도 낮음**: 작업당 40회 롤아웃, 한 번의 성공이 2.5% 포인트를 바꾸므로 작업 수준 차이는 기술적(descriptive)으로 간주.
- **데이터 효율성은 샘플 매칭 아님**: UMI 후훈련은 3,200개 궤적 vs 원격 조작 300개, 약 10배 차이, 동일 샘플 비교는 수행되지 않음.
- **실패 사례 분석 부재**: 논문은 체계적 실패 모드 분류를 보고하지 않았다.

## 공학적 시사점

- **재현 시 동기화와 상대 자세를 우선 확인**: GPIO 하드웨어 트리거(< 40 μs)와 네이티브 그리퍼 상대 자세 측정은 HiFi-UMI와 이전 시스템의 가장 본질적인 차이다. 재현 시 소프트웨어 동기화나 교차 카메라 재구성으로 퇴화하면 성공률 차이가 다시 나타날 수 있다.
- **데이터 필터링은 숨은 비용**: 96% 누적 통과율은 두 직렬 게이트(궤적 재구성 약 98%, 전신 제어 재생 약 98%)에서 비롯된다. 하위 팀은 약 4%의 원시 데이터 손실을 예비하고, 필터링이 훈련/검증 분할 전에 완료되어 근접 중복 창이 분할을 넘어 누출되지 않도록 해야 한다.
- **동작 표현 앵커 설계를 엄격히 준수**: 블록 내 모든 미래 자세는 동일한 현재 관측 앵커를 기준으로(ΔT = (T_t0^j)^(-1) T_(t0+δ_h)^(m)), 이전 동작 목표에 재귀적으로 의존하지 말 것—이는 백본 간 전이에서 가장 실수하기 쉬운 지점이다.
- **그리퍼 채널은 별도 처리 필요**: UMI는 조작자의 손 제스처 각도를 유지하지만, 실제 원격 조작은 파지가 없을 때 기본적으로 완전 개방이며 물리적 의미가 보정되지 않았다. 주 분석은 그리퍼 채널을 제외하며, 하위에서 사용하려면 별도 보정이 필요하다.
- **사전 훈련 이득은 데이터량 4배 차이에서도 유의미**: 800개 작업 에피소드로 무작위 초기화 기준선의 3,200 에피소드 성능을 초과하여, 대규모 UMI 사전 훈련이 데이터 효율성 레버임을 시사하지만, StarVLA-QwenPI에서만 검증되었으므로 다른 백본으로의 전이는 주의가 필요하다.
