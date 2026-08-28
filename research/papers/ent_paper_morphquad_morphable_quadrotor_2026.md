---
$id: ent_paper_morphquad_morphable_quadrotor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency'
  zh: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency'
  ko: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency'
summary:
  en: 'arXiv:2607.02764v1 Announce Type: new Abstract: Infrastructure maintenance, contact-based inspection, and emergency
    response can benefit from aerial vehicles that act as a flying human hand with extreme maneuverability, manipulation,
    and resiliency (MMR): maneuverability to fly in arbitrary orientations to reach remote and tight locations; manipulation
    to point sensors, turn valves, and press tools at arbitrary orientations; resiliency to maintain accurate motion and force
    control despite disturbances from arbitrary directions, such as wind, ground effects, and friction. Realizing MMR on aerial
    vehicles requires not only omnidirectional flight; it also requires (I) vectoring of maximum thrust in any direction,
    to maximize capacity for contact-force application and disturbance rejection, (II) global stability, to enable control
    over any orientation/position, and (III) compact, standard designs that build upon platforms such as quadrotors to inherit
    technological know-how. No current aerial vehicle simultaneously enables I--III, due to structural and control limitations
    that constrain actuation. We present MorphQuad: a morphable quadrotor that enjoys MMR. Key to our approach is a hardware
    and control co-design: on hardware, we independently articulate each of the four rotor systems via two-axis gimbals; on
    control, we introduce globally-stable control, and energy-optimal thrust allocation that permits inter-rotor thrust cancellations
    only to avoid downwash interference and gimbal lock. With fully-onboard autonomy, MorphQuad demonstrates multi-revolution
    rotation while translating or hovering, for pipe inspection and target tracking (maneuverability); valve turning, perching,
    and object pressing and pushing with human-level strengths (manipulation); and wind rejection from any direction, even
    directed to a single rotor, and push-pull recovery (resiliency).'
  zh: MorphQuad 是一种可变形四旋翼飞行器，由研究团队通过硬件与控制协同设计实现，旨在同时具备超机动性、操作能力和抗干扰韧性。其核心创新在于为每个旋翼配备双轴云台，并结合全局稳定控制与能量最优推力分配算法，使飞行器能在任意方向输出最大推力，并避免下洗干扰和万向节锁死。
  ko: 'arXiv:2607.02764v1 Announce Type: new Abstract: Infrastructure maintenance, contact-based inspection, and emergency
    response can benefit from aerial vehicles that act as a flying human hand with extreme maneuverability, manipulation,
    and resiliency (MMR): maneuverability to fly in arbitrary orientations to reach remote and tight locations; manipulation
    to point sensors, turn valves, and press tools at arbitrary orientations; resiliency to maintain accurate motion and force
    control despite disturbances from arbitrary directions, such as wind, ground effects, and friction. Realizing MMR on aerial
    vehicles requires not only omnidirectional flight; it also requires (I) vectoring of maximum thrust in any direction,
    to maximize capacity for contact-force application and disturbance rejection, (II) global stability, to enable control
    over any orientation/position, and (III) compact, standard designs that build upon platforms such as quadrotors to inherit
    technological know-how. No current aerial vehicle simultaneously enables I--III, due to structural and control limitations
    that constrain actuation. We present MorphQuad: a morphable quadrotor that enjoys MMR. Key to our approach is a hardware
    and control co-design: on hardware, we independently articulate each of the four rotor systems via two-axis gimbals; on
    control, we introduce globally-stable control, and energy-optimal thrust allocation that permits inter-rotor thrust cancellations
    only to avoid downwash interference and gimbal lock. With fully-onboard autonomy, MorphQuad demonstrates multi-revolution
    rotation while translating or hovering, for pipe inspection and target tracking (maneuverability); valve turning, perching,
    and object pressing and pushing with human-level strengths (manipulation); and wind rejection from any direction, even
    directed to a single rotor, and push-pull recovery (resiliency).'
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
- morphquad
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02764v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (601 chars, DeepSeek). [2026-08-28] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency (arXiv)'
  url: https://arxiv.org/abs/2607.02764
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述

MorphQuad 是一种基于标准四旋翼平台、通过双轴万向节独立铰接四个同轴对转旋翼系统的变倾转飞行器，由作者团队提出并实现。其核心贡献在于首次在实物平台上同时满足了全向推力矢量输出、几乎全局姿态稳定性与紧凑标准设计三个使能条件，并通过广义几何控制器、L1 自适应增强与零空间感知推力分配，在机动性、操控与抗扰三类任务中展示了超越常规四旋翼的能力。

## 它改变了什么

空中机器人领域长期存在一个三角困境：要么像固定倾转多旋翼那样推力方向受机体姿态限制，无法在任意方向输出最大推力；要么像多旋翼或“飞行器中的飞行器”那样结构复杂、体积庞大，难以继承成熟四旋翼的技术积累。MorphQuad 真正改变的是这个权衡空间——它证明了在标准四旋翼的尺寸与重量预算内，通过机械上引入双轴万向节、控制上引入全局稳定与能量最优分配，可以同时获得全向推力、几乎全局稳定性和紧凑设计，而不是在三个目标之间做取舍。

这一改变的意义在于，它将“全向飞行器”从实验室的定制原型推向了可复现、可维护的工程平台。作者没有停留在仿真或理论，而是给出了完整的硬件实现细节、控制管线与实验验证，使得后续研究者可以直接基于其设计进行复现或改进。同时，其控制架构在 PX4 混合器框架内实现，意味着现有四旋翼开发工具链可以平滑迁移，降低了采用门槛。

## 方法拆解

### 硬件架构
- 每个旋翼系统由两个同轴、反向旋转、同速电机驱动，产生同向推力，同时消除单螺旋桨的陀螺进动与反扭矩，简化动力学模型。
- 双轴万向节允许每个旋翼系统绕两个垂直轴旋转 **±1080°**（即三整圈），动力与信号线通过外伺服旋转轴中心开口走线，皮带-滑轮传动将外伺服移出旋转轴。
- 整机为 H 配置，双平行碳纤维增强 PLA 板，起飞质量 **4.56 kg**，每臂最大推力假设 **24.5 N**。

### 控制管线
1. **轨迹规划器**：以 **100 Hz** 频率发送五次多项式平滑参考状态（位置、速度、姿态、角速度）至飞控。
2. **广义几何控制器**：直接在 SE(3) 流形上定义跟踪误差，独立命令三轴推力与三轴扭矩，实现几乎处处指数稳定（初始姿态误差小于 **180°** 即可，对比常规控制器要求小于 **90°**）。
3. **L1 自适应增强**：通过预测器-自适应律实时估计未建模扰动，经一阶低通滤波器（力带宽 ω_f,v，力矩带宽 ω_f,ω）取负补偿。
4. **推力分配**：将六维期望力/力矩分解为四个三维推力向量，等效于 Moore-Penrose 伪逆解；通过零空间修正避免两个条件——(i) 任意两推力矢量不得平行于机体 x 轴或 y 轴（防下洗干扰），(ii) 单个推力矢量不得平行于机体 y 轴（防万向节锁死）。
5. **状态估计**：融合视觉惯性里程计与 IMU，扩展卡尔曼滤波器以 **800 Hz** 提供状态反馈。

### 关键设计决策
- 同轴对转双电机设计消除了陀螺进动与反扭矩，使推力分配问题简化为纯几何问题，这是控制可实现性的前提。
- 零空间修正的代价函数设计为最小化推力向量范数平方，同时引入与期望力方向接近锁死轴程度成比例的分量，保证内伺服位置远离 β_i = ±π/2。
- 推力分配在 PX4 混合器框架内实现，保持与标准多旋翼工具链兼容，降低工程集成成本。

## 关键创新

1. **机械与控制的协同设计**：双轴万向节 ±1080° 旋转范围配合同轴对转双电机，从根源上消除了单螺旋桨的陀螺效应与反扭矩，使得推力分配可以视为纯几何问题。这一设计决策是后续控制算法能够简洁实现的基础，而非简单的硬件堆叠。

2. **零空间感知的推力分配**：现有变倾转多旋翼的推力分配通常只考虑力/力矩分解，忽略旋翼间气动干扰与万向节锁死。MorphQuad 通过零空间修正显式避免共线推力矢量与锁死构型，且该修正以闭式条件赋值实现，计算开销极小，适合机载实时运行。

3. **广义几何控制器 + L1 自适应的组合**：几何控制器在 SE(3) 上提供几乎全局指数稳定（初始误差放宽至 **180°**），而 L1 自适应实时估计并补偿任意方向扰动。这一组合使得系统在强风、脉冲推力、持续拉力等未知扰动下仍能保持稳定，且无需精确的动力学模型。

## 实验与结果

实验覆盖机动性、操控与抗扰三类任务，所有任务均完全机载（无运动捕捉或外部计算）。

| 任务 | 关键指标 | 数值 |
|------|----------|------|
| 管道检查 | 位置 RMSE（所有轴） | < **6 cm** |
| 管道检查 | 俯仰 RMSE | **5.5°** |
| 手部跟踪 | 位置 RMSE | **5.5 cm** |
| 手部跟踪 | 方向 RMSE | **6.99°** |
| 阀门转动 | 最大机体扭矩 | **4.92 Nm** |
| 推物体（30 kg） | y 轴误差 | **0.8 m** |
| 风扰（30 m/s） | 位置 RMSE（主导风轴） | **8 cm** |
| 持续拉力 | 力传感器峰值负载 | **4.55 kg** |
| 持续拉力 | 估计扰动力 | **3.56 kg** |
| 持续拉力 | 两者差异 | **0.99 kg** |

结果含义：
- 机动性实验中，MorphQuad 在连续俯仰旋转 **720°** 的同时沿 **1 m** 直径圆轨迹平移，位置误差低于 **6 cm**，证明全向推力矢量输出在实际飞行中有效。
- 操控实验中，**4.92 Nm** 扭矩与 **4.55 kg** 侧向力（约等于起飞质量）表明其具备人类手腕级别的力量输出，可完成转动阀门、钉钉子、推重物等物理交互任务。
- 抗扰实验中，**30 m/s**（**108 km/h**）强风下位置误差仅 **8 cm**，脉冲推力下俯仰扰动超过 **20°** 但姿态 RMSE 仍低于 **5°**，验证了 L1 自适应对未知扰动的抑制能力。
- 持续拉力实验中，力传感器峰值 **4.55 kg** 与估计扰动力 **3.56 kg** 差异 **0.99 kg**，说明控制器对扰动的估计存在偏差，但系统仍能保持稳定。

## 边界与局限

- 所有操控任务对接触是开环的：无力和扭矩传感器，轨迹规划器不命令接触力/扭矩，无视觉伺服。这意味着精细交互（如抓取易碎物体）尚不可行。
- 阀门转动实验中，俯仰误差升高归因于前端末端执行器附加质量引起的机头下俯力矩，未在几何控制器中直接考虑（使用标称模型）。
- 栖停与钉钉子实验中，接触时出现明显振荡，归因于着陆腿柔顺性导致的撞击振动与螺旋桨靠近墙壁的湍流扰动。
- 推物体实验中，y 轴误差累积因恒定加速度前馈未更新位置设定点。
- 稳定性证明仅覆盖初始姿态误差小于 **180°** 的情况，恰好等于 **180°** 的边界情况未作说明。
- 论文未明确提及使用滑环（可替代方案以实现无限旋转），也未评估接触力和扭矩的准确性。

## 工程启示

复现或基于 MorphQuad 开发时，以下环节最值得关注：

1. **先核对万向节旋转范围与线缆走线**：±1080° 的旋转范围依赖线长松弛容纳扭转，皮带-滑轮传动将外伺服移出旋转轴。若简化此设计，旋转范围将受限，直接影响全向推力能力。

2. **推力分配中的零空间修正是关键**：直接使用伪逆解而不加零空间修正，会在某些期望力方向下导致旋翼间下洗干扰或万向节锁死。复现时应严格实现式 (19) 的条件赋值逻辑，并验证 c1、c2、c6 的计算与符号约定。

3. **L1 自适应带宽参数需根据实际扰动调谐**：力带宽 ω_f,v 与力矩带宽 ω_f,ω 的选择直接影响扰动抑制效果与稳定性。论文未给出具体数值，建议在仿真中先扫描参数范围，再迁移至实物。

4. **注意前端末端执行器对姿态控制的影响**：阀门实验中俯仰误差升高表明，附加质量产生的力矩未被控制器建模。若下游任务需要挂载不同负载，建议在几何控制器中增加负载力矩前馈，或使用在线辨识。

5. **接触任务的开环特性是最大局限**：当前所有操控任务对接触是开环的，若需精细交互，必须添加力/力矩传感与视觉伺服。建议优先考虑在末端执行器集成力传感器，并扩展轨迹规划器以命令接触力。

## 参考
- http://arxiv.org/abs/2607.02764v1

## 개요
MorphQuad는 기존 비행체가 최대 추력 벡터링, 전역 안정성, 그리고 컴팩트한 표준 설계를 동시에 구현하지 못하는 문제를 해결합니다. 하드웨어 측면에서 각 로터 시스템은 독립적인 2축 짐벌을 통해 자유롭게 편향됩니다. 제어 측면에서는 전역 안정 제어 전략과 에너지 최적 추력 분배를 사용하며, 다운워시 간섭과 짐벌 잠금을 피할 때에만 추력 상쇄를 허용합니다. 이 비행체는 완전한 온보드 자율 조건에서 다회전 비행, 밸브 조작, 단일 로터 내풍 등의 능력을 보여주며, 인간 수준의 성능을 달성합니다.

## 핵심 내용
### 방법
MorphQuad의 핵심은 하드웨어와 제어의 공동 설계입니다:
- **하드웨어**: 4개의 로터 시스템 각각에 2축 짐벌을 장착하여 독립적인 편향을 구현하고, 이를 통해 임의의 방향으로 최대 추력을 생성합니다.
- **제어**: 전역 안정 제어를 도입하여 비행체가 어떤 자세와 위치에서도 안정적으로 유지되도록 합니다. 에너지 최적 추력 분배 알고리즘은 다운워시 간섭과 짐벌 잠금을 피하기 위해 필요한 경우에만 로터 간 추력 상쇄를 허용합니다.

### 실험 설정 및 주요 수치
- **자율성**: 외부 계산이나 위치 보조 없이 완전한 온보드 자율 운영을 수행합니다.
- **기동성**: 병진 또는 호버링 상태에서 다회전 비행을 완료하며, 파이프라인 검사와 목표 추적에 사용됩니다.
- **조작 능력**: 밸브 회전, 착지, 물체 누르기 및 밀고 당기기를 구현하며, 힘은 인간 수준에 도달합니다.
- **탄력성**: 단일 로터에 대한 강풍을 포함한 임의 방향의 풍력 간섭을 견딜 수 있으며, 밀고 당기기 복구 능력을 갖추고 있습니다.

### 결론
MorphQuad는 하드웨어와 제어의 공동 설계를 통해 쿼드로터 플랫폼에서 처음으로 최대 추력 벡터링, 전역 안정성, 그리고 컴팩트한 표준 설계를 동시에 구현했습니다. 이를 통해 인프라 유지보수, 접촉식 검사, 그리고 긴급 대응을 위한 고성능 공중 조작 플랫폼을 제공합니다.
