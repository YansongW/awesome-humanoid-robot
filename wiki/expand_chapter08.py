#!/usr/bin/env python3
"""
Expansion script for Chapter 8 of the Awesome Humanoid Robot Wiki.
Adds subsections on foot/hand/torso design, deepens whole-body control,
and fills foundational gaps (statics/duality, trajectory generation,
closed chains, parameter identification, motion planning, force/impedance
control) while preserving existing content.
"""
import re
from pathlib import Path

ROOT = Path("/Users/yansong/Desktop/awesome-humanoid-robot/wiki")
CHAPTER = ROOT / "docs/chapters/chapter-08.md"

# ---------------------------------------------------------------------------
# New content blocks
# ---------------------------------------------------------------------------

SECTION_8_2_7 = r'''
### 8.2.7 下肢与足部设计原理

人形机器人的下肢是把整机质量传递到地面的最终环节，也是决定行走、奔跑、跳跃与抗扰能力的核心。**下肢运动链（leg kinematic chain）**通常由髋（hip）、膝（knee）、踝（ankle）三段组成，其自由度配置深受人类解剖结构与工程可实现性的双重影响[2][3]。

!!! note "术语解释：下肢运动链、髋、膝、踝、自由度配置"
    - **下肢运动链（leg kinematic chain）**：由髋、膝、踝及其连杆串联而成的运动链。
    - **髋（hip）**：连接躯干与大腿的关节，通常提供 3 个旋转自由度。
    - **膝（knee）**：大腿与小腿之间的关节，主要提供俯仰自由度。
    - **踝（ankle）**：小腿与脚之间的关节，通常提供滚转与俯仰 2 个自由度。
    - **自由度配置（DOF configuration）**：各关节自由度数目与排列方式的选择。

#### 腿部运动链：髋 3-DOF + 膝 1-DOF + 踝 2-DOF

典型人形机器人单腿采用 **6-DOF 配置**：

- **髋部 3-DOF**：roll（侧摆）、pitch（屈伸）、yaw（转向）三轴正交，使腿能在三维空间中摆动与支撑。
- **膝部 1-DOF**：单俯仰轴，主要完成小腿相对于大腿的屈伸，提供步态中最大的垂直位移。
- **踝部 2-DOF**：roll + pitch，调整脚掌姿态以适应不平地面、斜坡与侧向平衡。

这种 3-1-2 布局并非唯一选择。某些简化平台使用 3-1-0（无踝关节）或 2-1-2 配置以降低成本，但会牺牲姿态调节能力与地形适应性。增加髋部偏航轴虽然提高了转向灵活性，却使髋关节结构更复杂、质量更大。设计者需在运动能力、质量、惯量、控制复杂度之间权衡[3][82]。

!!! note "术语解释：侧摆、屈伸、转向、地形适应性、运动惯量"
    - **侧摆（abduction/adduction）**：绕身体前后轴的摆动，对应 roll。
    - **屈伸（flexion/extension）**：绕身体左右轴的摆动，对应 pitch。
    - **转向（rotation）**：绕身体垂直轴的转动，对应 yaw。
    - **地形适应性（terrain adaptability）**：机器人适应不同地面形状与材质的能力。
    - **运动惯量（inertia）**：肢体运动时表现出的转动惯量，影响动态响应。

髋部三轴的排列顺序会显著影响运动学与动力学特性。常见顺序包括 R-P-Y（roll-pitch-yaw）与 Y-P-R（yaw-pitch-roll）：

- **R-P-Y**：俯仰轴靠近躯干中心，有利于步行时前后摆动，减小躯干晃动。
- **Y-P-R**：偏航轴在上下两端，便于转向与侧摆解耦，适合需要快速转向的场景。

```mermaid
flowchart TD
    subgraph 髋["髋 3-DOF"]
    H1["髋 roll"] --> H2["髋 pitch"]
    H2 --> H3["髋 yaw"]
    end
    H3 --> K["膝 1-DOF<br/>pitch"]
    K --> A["踝 2-DOF<br/>roll + pitch"]
    A --> F["足部"]
```

#### 足部设计：平足 vs 仿人足

**足部（foot）**是人形机器人与地面的唯一接触界面，其几何、质量与柔顺性直接影响稳定性、能量效率与传感能力。足部设计可分为两大类：

1. **平足（flat foot）**： soles 为一块刚性或半刚性平板，接触面积大、稳定性高、易于集成力/力矩传感器。大多数工程人形机器人采用此类设计。
2. **仿人足（human-like foot）**：带有足弓、脚跟与脚趾关节，质量分布更接近人体，可模拟人类的滚动着地（rocker motion）与蹬离（push-off），但结构复杂、控制困难。

!!! note "术语解释：平足、仿人足、足弓、滚动着地、蹬离"
    - **平足（flat foot）**：足底近似平面的足部设计。
    - **仿人足（human-like foot）**：模仿人类足部结构的足部设计。
    - **足弓（foot arch）**：足底中部的拱形结构，具有缓冲与储能作用。
    - **滚动着地（rocker motion）**：行走时足跟先着地，重心逐渐前移经过脚掌的运动模式。
    - **蹬离（push-off）**：脚趾离地前脚掌向下后方蹬地以推进身体向前的动作。

足部关键设计参数包括：

- **接触贴片（contact patch）**：足底与地面实际接触的区域。较大的贴片提高稳定性，但降低对地形的顺应性。
- **压力中心（Center of Pressure, CoP）**：地面反作用力在足底的作用点。行走中 CoP 从脚跟滚向脚尖，与 ZMP 密切相关。
- **踝关节力矩（ankle torque）**：单腿支撑期全身重量绕踝关节产生力矩，通常要求踝关节具有极高扭矩密度。
- **力/力矩传感器集成**：六轴力/力矩传感器常安装在踝部或足底，用于测量 GRF、CoP 与接触力矩。

!!! note "术语解释：接触贴片、压力中心（CoP）、踝关节力矩、六轴力/力矩传感器"
    - **接触贴片（contact patch）**：足部与地面接触的实际区域。
    - **压力中心（Center of Pressure, CoP）**：地面反作用力在接触面上的等效作用点。
    - **踝关节力矩（ankle torque）**：绕踝关节的力矩，由地面反作用力与重力产生。
    - **六轴力/力矩传感器（6-axis F/T sensor）**：同时测量三个力分量与三个力矩分量的传感器。

对于单腿支撑阶段，踝关节俯仰力矩可近似为：

$$
\tau_{\text{ankle,pitch}} \approx m g \, d_{\text{CoM-ankle}}
$$

其中 \(m\) 为整机质量，\(g\) 为重力加速度，\(d_{\text{CoM-ankle}}\) 为质心到踝关节的水平距离。以 60 kg 机器人、质心偏移 0.05 m 为例，踝关节俯仰力矩约为 \(60 \times 9.81 \times 0.05 \approx 29.4\ \text{N·m}\)；若考虑动态摆动与斜坡，峰值力矩可能翻倍。

```mermaid
flowchart TD
    subgraph 足接触模型["足-地接触模型"]
    A["足底"]
    B["地面反作用力 GRF"]
    C["压力中心 CoP"]
    D["摩擦锥约束"]
    end
    A -->|"接触区域"| C
    B -->|"等效作用点"| C
    C -->|"必须在支撑多边形内"| E["动态稳定判据"]
    B -->|"切向/法向比"| D
```

#### 柔顺性与冲击吸收

双足行走每一步都伴随脚触地冲击。若冲击力直接传递到关节减速器与电机，将加速磨损、激发结构振动并增加能耗。因此，足部与小腿通常设计有**柔顺元件（compliant element）**吸收冲击：

- **弹性垫片/橡胶垫**：安装在足底或踝关节输出端，提供可控的法向柔度。
- **弹簧-阻尼机构**：在踝部或小腿引入线性弹簧与阻尼器，储存并耗散触地能量。
- **粘弹性材料**：如 TPU、硅胶等，可在宽频范围内提供阻尼。

!!! note "术语解释：柔顺元件、弹性垫片、弹簧-阻尼机构、粘弹性材料"
    - **柔顺元件（compliant element）**：在外力作用下产生弹性变形的结构或材料。
    - **弹性垫片（elastomer pad）**：由橡胶或类似材料制成的缓冲垫。
    - **弹簧-阻尼机构（spring-damper mechanism）**：由弹簧与阻尼器组合而成的振动吸收装置。
    - **粘弹性材料（viscoelastic material）**：同时具有弹性与粘性响应的材料。

柔顺性设计需要权衡：过柔会降低姿态控制带宽与定位精度，过刚则无法有效吸收冲击。常用设计指标为**等效刚度** \(k_{\text{eq}}\) 与**等效阻尼** \(c_{\text{eq}}\)，满足：

$$
m \ddot{z} + c_{\text{eq}} \dot{z} + k_{\text{eq}} z = F_{\text{GRF}}
$$

其中 \(z\) 为足部或踝部垂直位移。触地冲击的峰值力与等效刚度成正比， designers 常通过实验或仿真优化 \(k_{\text{eq}}\) 与 \(c_{\text{eq}}\)。

#### 运动范围与人类步态需求

人类正常步态的关节运动范围（Range of Motion, ROM）为足部与腿部设计提供了重要参考：

| 关节 | 典型人类 ROM（步行） | 人形机器人设计目标 |
|---|---|---|
| 髋屈伸 | \(-30° \sim +30°\) | \(\pm 45°\) 以上 |
| 髋侧摆 | \(\pm 10°\) | \(\pm 20°\) 以上 |
| 髋旋转 | \(\pm 10°\) | \(\pm 30°\) 以上 |
| 膝屈伸 | \(0° \sim +60°\) | \(0° \sim +90°\) 以上 |
| 踝背屈/跖屈 | \(-10° \sim +20°\) | \(-20° \sim +30°\) 以上 |
| 踝内外翻 | \(\pm 5°\) | \(\pm 15°\) 以上 |

!!! note "术语解释：运动范围（ROM）、髋屈伸、髋侧摆、踝背屈/跖屈、踝内外翻"
    - **运动范围（Range of Motion, ROM）**：关节可活动的角度范围。
    - **髋屈伸（hip flexion/extension）**：大腿绕髋部前后摆动。
    - **髋侧摆（hip abduction/adduction）**：大腿绕髋部左右摆动。
    - **踝背屈/跖屈（ankle dorsiflexion/plantarflexion）**：脚背向上/脚尖向下的运动。
    - **踝内外翻（ankle inversion/eversion）**：脚掌绕前后轴向内/向外倾斜。

机器人关节 ROM 通常大于人类步行所需，以保留上下楼梯、跨越障碍、下蹲等动作余量。但过大的 ROM 会牺牲结构刚度与紧凑性，因此需在关节限位处设置软限位与硬限位双重保护。

```mermaid
flowchart TD
    A["人类步态 ROM 数据"] --> B["确定机器人关节 ROM 目标"]
    B --> C["结构/驱动设计"]
    C --> D["运动仿真验证"]
    D --> E{"满足任务?"}
    E -->|"否"| F["增加 ROM 或改变构型"]
    F --> C
    E -->|"是"| G["设置软硬限位"]
```
'''

SECTION_8_2_8 = r'''
### 8.2.8 上肢与手部设计原理

人形机器人的上肢负责与环境交互、操作物体与保持平衡。**手臂运动链（arm kinematic chain）**与**手部（hand）**的设计必须在负载能力、工作空间、灵巧度、重量与成本之间取得平衡[1][2][3]。

!!! note "术语解释：上肢、手臂运动链、手部、工作空间、灵巧度"
    - **上肢（upper limb）**：包括肩、臂、肘、腕、手的机器人肢体。
    - **手臂运动链（arm kinematic chain）**：由肩、肘、腕及其连杆组成的多自由度串联链。
    - **手部（hand）**：手臂末端用于抓取与操作的执行器。
    - **工作空间（workspace）**：手臂末端可到达的所有位姿集合。
    - **灵巧度（dexterity）**：手部完成精细操作的能力。

#### 手臂运动链：肩 3-DOF、肘 1-2 DOF、腕 2-3 DOF

典型人形机器人单臂采用 **7-DOF** 配置，模仿人类手臂的运动冗余：

- **肩部 3-DOF**：roll-pitch-yaw 三轴正交，决定手臂根部姿态。
- **肘部 1-DOF**：单俯仰轴，完成前臂屈伸。
- **腕部 3-DOF**：roll-pitch-yaw，精细调整末端姿态。

这种 3-1-3 布局使手臂在末端 6-DOF 位姿任务外具有 1 维冗余，可在零空间内优化姿态、避障或远离奇异。若任务对姿态要求不高，腕部可减为 2-DOF（roll + pitch 或 pitch + yaw），降低成本与质量。

!!! note "术语解释：肩部、肘部、腕部、末端位姿、运动冗余"
    - **肩部（shoulder）**：连接躯干与上臂的关节群。
    - **肘部（elbow）**：上臂与前臂之间的关节。
    - **腕部（wrist）**：前臂与手之间的关节群。
    - **末端位姿（end-effector pose）**：手臂末端在操作空间中的位置与姿态。
    - **运动冗余（kinematic redundancy）**：关节 DOF 多于任务空间维度的情形。

手臂设计的关键指标包括：

- **工作空间**：由肩、肘、腕长度与关节 ROM 共同决定。人形机器人手臂通常需要覆盖从地面到头顶、从前胸到身后一定范围。
- **负载能力（payload）**：手臂末端可承受的最大质量。工业场景要求 5 kg 以上，服务场景可能只需 1-2 kg。
- **灵巧度**：常用可操作性椭球、条件数等指标衡量，与 Jacobian 矩阵的奇异值分布相关。
- **自重与惯量**：手臂越轻，对躯干平衡与动态响应越有利。

```mermaid
flowchart LR
    subgraph 肩["肩 3-DOF"]
    S1["roll"] --> S2["pitch"]
    S2 --> S3["yaw"]
    end
    S3 --> E["肘 1-DOF<br/>pitch"]
    E --> W["腕 3-DOF<br/>roll-pitch-yaw"]
    W --> H["手"]
```

#### 手部设计：灵巧手 vs 平行夹爪

人形机器人手部可分为两大类型：

1. **平行夹爪（parallel-jaw gripper）**：仅两个手指做开合运动，结构简单、可靠、成本低，适合规则物体抓取，但无法完成复杂操作。
2. **灵巧手（dexterous hand）**：具有多手指、多关节，可模仿人类手部运动，完成抓、捏、握、拧等多种操作，但结构复杂、控制困难、成本高。

!!! note "术语解释：平行夹爪、灵巧手、多指操作、抓取"
    - **平行夹爪（parallel-jaw gripper）**：仅有两个平行手指的夹持器。
    - **灵巧手（dexterous hand）**：具有多手指和多关节、可完成复杂操作的手。
    - **多指操作（multi-finger manipulation）**：利用多个手指协同控制物体的运动。
    - **抓取（grasping）**：用手部固定或移动物体的行为。

灵巧手的驱动方式主要有两种：

- **直接驱动（direct-drive）**：每个关节由独立电机驱动，控制精度高、响应快，但电机数量多、体积大、质量大。
- **腱驱动（tendon-driven）**：电机置于前臂或手掌，通过腱索与滑轮传递力到手指关节，可减小手指尺寸与惯量，但存在摩擦、回差与腱磨损问题。

!!! note "术语解释：直接驱动、腱驱动、腱索、回差、手指惯量"
    - **直接驱动（direct-drive）**：电机直接安装在关节处的驱动方式。
    - **腱驱动（tendon-driven）**：通过柔性腱索传递力与运动的驱动方式。
    - **腱索（tendon）**：传递拉力的柔性缆线。
    - **回差（backlash）**：传动系统中由于间隙导致的输入输出滞后。
    - **手指惯量（finger inertia）**：手指运动时的转动惯量。

#### 拇指对掌与抓取分类

人类手部最重要的特征之一是**拇指对掌（thumb opposition）**：拇指可与其余四指相对运动，形成钳形抓取。机器人灵巧手通常至少包括拇指、食指、中指，部分设计还包含无名指与小指。

根据 Napier 经典分类，抓取可分为两大类：

1. **力量型抓取（power grasp）**：手指包裹物体，手掌提供主要支撑，用于高稳定性、大力矩的抓取，如握锤子、提箱子。
2 **精确型抓取（precision grasp）**：仅用指尖捏住物体，用于精细操作，如捏钥匙、拾取螺丝。

此外，还有**钩握（hook grasp）**、**侧捏（lateral pinch）**、**球形握（spherical grasp）**、**圆柱握（cylindrical grasp）**等变体[1]。

!!! note "术语解释：拇指对掌、力量型抓取、精确型抓取、钩握、侧捏"
    - **拇指对掌（thumb opposition）**：拇指能够与其他手指相对运动的能力。
    - **力量型抓取（power grasp）**：利用手掌与手指大面积包裹物体的稳定抓取。
    - **精确型抓取（precision grasp）**：仅用指尖控制物体的小力抓取。
    - **钩握（hook grasp）**：手指弯曲成钩状悬挂物体的抓取方式。
    - **侧捏（lateral pinch）**：拇指指腹与食指侧缘夹持物体的动作。

```mermaid
flowchart TD
    A["抓取分类"] --> B["力量型抓取"]
    A --> C["精确型抓取"]
    A --> D["钩握"]
    A --> E["侧捏"]
    B --> F["手掌支撑 + 手指包裹"]
    C --> G["指尖捏持"]
    D --> H["手指成钩悬挂"]
    E --> I["拇指与食指侧缘夹持"]
```

#### 手指自由度分配与欠驱动

一只人手约有 21 个自由度（4 指各 4 DOF + 拇指 5 DOF），但机器人灵巧手受限于体积与驱动器数量，常采用**欠驱动（underactuated）**设计：

- **完全驱动（fully actuated）**：每个关节独立驱动，控制灵活但复杂。
- **欠驱动（underactuated）**：驱动器数量少于关节 DOF，通过机械耦合（如腱索、连杆、差动机构）使手指在接触物体时自动包络。

!!! note "术语解释：手指自由度、完全驱动、欠驱动、机械耦合、自适应包络"
    - **手指自由度（finger DOF）**：手指独立运动参数的数目。
    - **完全驱动（fully actuated）**：每个自由度都有独立执行器。
    - **欠驱动（underactuated）**：执行器数量少于自由度数量。
    - **机械耦合（mechanical coupling）**：通过机构使多个关节运动相关联。
    - **自适应包络（adaptive enveloping）**：手指在接触物体时自动贴合其外形的特性。

典型欠驱动手指采用 "1 个电机驱动 2-3 个关节" 的配置：电机通过腱索牵引近端指骨，近端指骨再带动中端与远端指骨。当近端指骨先接触物体时，后续运动自动转移到远端指骨，实现自适应包络。这种设计显著降低驱动器数量，提高对未知形状物体的适应性。

手指 DOF 常见分配：

| 手指 | 关节 | 典型 DOF | 说明 |
|---|---|---|---|
| 食指/中指/无名指/小指 | 掌指关节（MCP） | 2 | 屈伸 + 侧摆 |
| | 近端指间关节（PIP） | 1 | 屈伸 |
| | 远端指间关节（DIP） | 1 | 屈伸 |
| 拇指 | 腕掌关节（CMC） | 2-3 | 屈伸 + 侧摆 + 对掌 |
| | 掌指关节（MCP） | 1 | 屈伸 |
| | 指间关节（IP） | 1 | 屈伸 |

!!! note "术语解释：掌指关节（MCP）、近端指间关节（PIP）、远端指间关节（DIP）、腕掌关节（CMC）"
    - **掌指关节（Metacarpophalangeal joint, MCP）**：手掌与近端指骨之间的关节。
    - **近端指间关节（Proximal Interphalangeal joint, PIP）**：近端与中间指骨之间的关节。
    - **远端指间关节（Distal Interphalangeal joint, DIP）**：中间与远端指骨之间的关节。
    - **腕掌关节（Carpometacarpal joint, CMC）**：腕骨与掌骨之间的关节，拇指处活动度最大。

```mermaid
flowchart TD
    subgraph 手指DOF["手指 DOF 布局示例"]
    A["拇指 CMC 2-3 DOF"] --> B["拇指 MCP 1 DOF"]
    B --> C["拇指 IP 1 DOF"]
    D["食指 MCP 2 DOF"] --> E["食指 PIP 1 DOF"]
    E --> F["食指 DIP 1 DOF"]
    end
    A -->|"对掌运动"| G["拇指-食指捏合"]
```

#### 软指尖与触觉传感集成

手指末端与物体的接触特性决定抓取稳定性。**软指尖（soft fingertip）**通过弹性材料（硅胶、橡胶、凝胶）增加接触面积、提高摩擦、吸收冲击，并允许轻微的形状自适应。软 fingertip 的接触力分布可用 Hertz 接触或有限变形模型描述。

!!! note "术语解释：软指尖、接触面积、摩擦系数、Hertz 接触"
    - **软指尖（soft fingertip）**：由柔性材料制成的手指末端。
    - **接触面积（contact area）**：指尖与物体实际接触的面积。
    - **摩擦系数（friction coefficient）**：接触面切向力与法向力之比的上限。
    - **Hertz 接触（Hertzian contact）**：描述弹性体在法向力下接触变形的经典理论。

触觉传感器的集成使手能够感知：

- **法向力分布**：判断抓握是否过紧或过松。
- **切向力/滑移**：检测物体是否即将滑动，触发防滑策略。
- **物体形状与材质**：通过压力分布模式识别接触物体。
- **温度/振动**：扩展感知维度。

常见触觉传感技术包括：电阻式阵列、电容式阵列、光学触觉传感器（基于视觉的 GelSight 类）、压电薄膜等。

!!! note "术语解释：触觉传感器、法向力、切向力、滑移检测、触觉阵列"
    - **触觉传感器（tactile sensor）**：测量接触力、压力或形变的传感器。
    - **法向力（normal force）**：垂直于接触面的力分量。
    - **切向力（tangential force）**：平行于接触面的力分量。
    - **滑移检测（slip detection）**：识别物体与手指间相对滑动的过程。
    - **触觉阵列（tactile array）**：由多个触觉 sensing 单元组成的矩阵。

```mermaid
flowchart LR
    A["软指尖"] --> B["弹性材料"]
    A --> C["触觉传感阵列"]
    B --> D["增大摩擦/顺应外形"]
    C --> E["力/滑移/形状感知"]
    D --> F["稳定抓取"]
    E --> G["闭环抓取控制"]
```
'''

SECTION_8_2_9 = r'''
### 8.2.9 躯干、头颈与质量分布

躯干是人形机器人各肢体、电源、计算与感测设备的集成平台，其设计直接影响整机质量分布、惯量特性、运动协调与人机交互能力[3][82]。

!!! note "术语解释：躯干、头颈、质量分布、惯量特性、人机交互"
    - **躯干（torso）**：连接头、手臂、腿的核心身体部分。
    - **头颈（head-neck）**：头部与颈部组件，承载主要环境传感器。
    - **质量分布（mass distribution）**：质量在机器人各部位的分配。
    - **惯量特性（inertial properties）**：整机及各部位的转动惯量。
    - **人机交互（human-robot interaction, HRI）**：人与机器人之间的信息与动作交流。

#### 腰部/脊柱：1-3 DOF 主动关节

人类脊柱由多节椎骨组成，具有相当大的活动范围。人形机器人通常用简化的**主动腰（actuated waist）**或**主动脊柱（actuated spine）**实现躯干运动：

- **1-DOF 腰**：仅俯仰轴，允许躯干前倾/后仰，结构简单。
- **2-DOF 腰**：俯仰 + 偏航，增加转向与弯腰能力。
- **3-DOF 腰**：俯仰 + 偏航 + 滚转，提供完整三维姿态调节。

!!! note "术语解释：主动腰、主动脊柱、俯仰、偏航、滚转"
    - **主动腰（actuated waist）**：具有主动驱动自由度的腰部关节。
    - **主动脊柱（actuated spine）**：具有多个主动关节的脊柱机构。
    - **俯仰（pitch）**：绕身体左右轴的旋转。
    - **偏航（yaw）**：绕身体垂直轴的旋转。
    - **滚转（roll）**：绕身体前后轴的旋转。

主动腰部在以下任务中至关重要：

1. **扩大工作空间**：弯腰可使手臂够到更低位置，侧摆可扩大横向 reach。
2. **平衡调节**：在单腿支撑或受到扰动时，躯干姿态调整可补偿角动量。
3. **步态协调**：行走时躯干的反向旋转可抵消下肢摆动产生的角动量，提高能量效率。
4. **人机交互**：点头、转身等躯干-头部协调动作使机器人显得更自然。

```mermaid
flowchart TD
    A["主动腰 1-3 DOF"] --> B["扩大工作空间"]
    A --> C["平衡/角动量调节"]
    A --> D["步态协调"]
    A --> E["自然交互"]
    B --> F["手臂可达范围提升"]
    C --> G["抗扰动能力提升"]
    D --> H["行走能耗降低"]
    E --> I["人机交互更自然"]
```

#### 颈部 2-DOF：俯仰与偏航

人形机器人头部通常通过 **2-DOF 颈部（neck）**实现俯仰（点头）与偏航（摇头）运动，部分设计增加滚转以模拟头部倾斜。颈部的设计目标包括：

- **传感器指向**：使相机、LiDAR 等传感器对准感兴趣区域。
- **视野扩展**：在不移动躯干的情况下扩大感知范围。
- **交互表达**：头部姿态是人类非语言交流的重要部分。

!!! note "术语解释：颈部自由度、传感器指向、视野、非语言交流"
    - **颈部自由度（neck DOF）**：颈部关节的独立运动参数数目。
    - **传感器指向（sensor pointing）**：将传感器对准目标方向的能力。
    - **视野（field of view, FOV）**：传感器可感知的空间范围。
    - **非语言交流（non-verbal communication）**：通过姿态、表情、眼神传递信息。

颈部运动范围通常设计为：俯仰 \(\pm 30°\) 至 \(\pm 45°\)，偏航 \(\pm 60°\) 至 \(\pm 90°\)。由于头部质量较小但运动频繁，颈部驱动器需要高响应速度、低摩擦与良好的位置控制精度。

#### 头部传感器桅杆：相机、LiDAR、IMU 布局

头部通常被称为**传感器桅杆（sensor mast）**，因为人形机器人的头部是安装相机、LiDAR、IMU、麦克风等感知设备的最佳位置。其设计考虑包括：

- **高度**：与人类眼睛接近的高度有利于社交交互与场景理解。
- **视野重叠**：双目相机之间保持适当基线（通常 50-80 mm）以获得深度信息。
- **LiDAR 安装**：通常置于头顶以获得 360° 水平扫描视野，避免手臂遮挡。
- **IMU 放置**：尽量靠近整机质心或刚性安装于躯干，减少振动干扰。

!!! note "术语解释：传感器桅杆、双目基线、LiDAR、IMU、视野遮挡"
    - **传感器桅杆（sensor mast）**：集中安装头部传感器的结构。
    - **双目基线（stereo baseline）**：左右相机光心之间的距离。
    - **LiDAR（Light Detection and Ranging）**：激光雷达，用于测距与建图。
    - **IMU（Inertial Measurement Unit）**：惯性测量单元，测量角速度与加速度。
    - **视野遮挡（occlusion）**：障碍物阻挡传感器视野的现象。

```mermaid
flowchart TD
    subgraph 头部传感器布局["头部传感器布局"]
    A["双目相机<br/>前向/下倾"]
    B["LiDAR<br/>头顶 360°"]
    C["IMU<br/>头/躯干刚性安装"]
    D["麦克风阵列<br/>耳部/前额"]
    end
    A --> E["视觉感知"]
    B --> F["3D 建图"]
    C --> G["状态估计"]
    D --> H["语音交互"]
```

#### 质量分布：降低质心

人形机器人的**质量分布（mass distribution）**对动态稳定性、响应速度与能耗影响巨大。核心原则是：

- **把重的部件放低、放靠近质心**：电池、主计算机、大功率驱动器等尽量布置在髋部/骨盆区域，以降低整机质心高度。
- **减小四肢惯量**：手臂与腿部连杆应尽量轻量化，以降低摆动惯量与动态响应时间。
- **头部轻量化**：头部传感器多但运动频繁，应尽量减小其质量与惯量。

!!! note "术语解释：质心高度、四肢惯量、摆动惯量、骨盆区域"
    - **质心高度（CoM height）**：整机质心到地面的垂直距离。
    - **四肢惯量（limb inertia）**：手臂与腿部的转动惯量。
    - **摆动惯量（swing inertia）**：摆动腿或手臂时的等效惯量。
    - **骨盆区域（pelvic region）**：髋部与躯干下部，靠近人体质心。

质心高度 \(h_{\text{CoM}}\) 直接影响线性倒立摆的自然频率：

$$
\omega_0 = \sqrt{\frac{g}{h_{\text{CoM}}}}
$$

质心越低，\(\omega_0\) 越小，质心运动越慢，控制器越容易稳定；但过低会限制步幅与运动敏捷性。典型人形机器人质心高度约为身高的 40%-55%，即 0.6-0.9 m 之间。

```mermaid
flowchart TD
    A["质量分布目标"] --> B["重部件放低"]
    A --> C["四肢轻量化"]
    A --> D["头部轻量化"]
    B --> E["低质心"]
    C --> F["低摆动惯量"]
    D --> G["低颈部负载"]
    E --> H["提高稳定性"]
    F --> I["提高动态响应"]
    G --> J["提高头部控制带宽"]
```
'''

print("Content blocks loaded.")


SECTION_STATICS_DUALITY = r'''
### 8.3.13 静力学与力对偶

运动学研究位置与速度的映射，而**静力学（statics）**研究力与力矩在机构中的传递。对于机器人，末端接触力与关节力矩之间的关系由 **Jacobian 转置** 给出，这是机器人学中最基本也最深刻的对偶关系之一[2][3][5]。

!!! note "术语解释：静力学、Jacobian 转置、力对偶、关节力矩、末端接触力"
    - **静力学（statics）**：研究系统在平衡状态下力与力矩传递的学科。
    - **Jacobian 转置（Jacobian transpose）**：Jacobian 矩阵的转置，建立末端力与关节力矩的关系。
    - **力对偶（force duality）**：速度与力之间通过 Jacobian 及其转置相互映射的对偶关系。
    - **关节力矩（joint torque）**：执行器在关节处提供的力或力矩。
    - **末端接触力（end-effector contact force）**：末端执行器与外界接触时受到的力。

设机器人末端施加广义力（力与力矩）\(\mathbf{F} \in \mathbb{R}^m\)，关节需提供广义力矩 \(\boldsymbol{\tau} \in \mathbb{R}^n\)。在静态平衡下，关节力矩与末端力满足：

$$
\boldsymbol{\tau} = \mathbf{J}^T(\mathbf{q}) \, \mathbf{F}
$$

其中 \(\mathbf{J}\) 为 \(m \times n\) 的末端雅可比矩阵。该式表明：末端力被 "投影" 到关节空间，每个关节所需力矩等于末端力与对应 Jacobian 列向量的点积。

!!! note "术语解释：广义力、广义力矩、静态平衡、投影"
    - **广义力（generalized force）**：与广义坐标对应的力或力矩。
    - **广义力矩（generalized torque）**：与关节坐标对应的力矩。
    - **静态平衡（static equilibrium）**：系统加速度为零、合外力为零的状态。
    - **投影（projection）**：把一个向量映射到另一个子空间的操作。

对于非冗余机械臂（\(n = m\) 且 \(\mathbf{J}\) 可逆），末端力可由关节力矩反解：

$$
\mathbf{F} = \mathbf{J}^{-T}(\mathbf{q}) \, \boldsymbol{\tau}
$$

其中 \(\mathbf{J}^{-T} = (\mathbf{J}^T)^{-1}\)。该式说明：若 Jacobian 在某些方向上奇异（\(\mathbf{J}\) 降秩），则相应方向上的末端力无法由有限关节力矩产生——这正是**速度奇异与力奇异的对偶性**。

!!! note "术语解释：非冗余机械臂、Jacobian 可逆、力奇异、对偶性"
    - **非冗余机械臂（non-redundant manipulator）**：自由度等于任务空间维度的机械臂。
    - **Jacobian 可逆（invertible Jacobian）**：Jacobian 矩阵满秩且可求逆。
    - **力奇异（force singularity）**：某些方向末端力无法由关节力矩实现的状态。
    - **对偶性（duality）**：速度空间与力空间之间的相互映射关系。

#### 速度椭球与力椭球

Jacobian 把关节速度映射到末端操作空间速度：

$$
\dot{\mathbf{x}} = \mathbf{J} \dot{\mathbf{q}}
$$

若约束关节速度满足 \(\|\dot{\mathbf{q}}\| \leq 1\)，则末端可达速度集合构成一个**速度椭球（velocity ellipsoid）**。该椭球的主轴方向与长度由 \(\mathbf{J}\mathbf{J}^T\) 的特征向量与特征值平方根决定。

!!! note "术语解释：速度椭球、特征向量、特征值、操作空间速度"
    - **速度椭球（velocity ellipsoid）**：单位关节速度映射到操作空间形成的椭球。
    - **特征向量（eigenvector）**：矩阵变换中方向保持不变的向量。
    - **特征值（eigenvalue）**：特征向量被拉伸的倍数。
    - **操作空间速度（task-space velocity）**：末端在操作空间中的速度。

类似地，若约束关节力矩满足 \(\|\boldsymbol{\tau}\| \leq 1\)，末端可达广义力集合构成**力椭球（force ellipsoid）**。力椭球由 \((\mathbf{J}\mathbf{J}^T)^{-1}\) 的特征值决定：

- 速度椭球长轴方向对应力椭球短轴方向。
- 速度椭球短轴方向对应力椭球长轴方向。

这就是机器人学中著名的 **速度-力对偶（velocity-force duality）**：在机构便于快速运动的方向上，它难以产生大力；在便于产生大力的方向上，它难以快速运动[2][5]。

!!! note "术语解释：力椭球、速度-力对偶、运动方向、力方向"
    - **力椭球（force ellipsoid）**：单位关节力矩映射到操作空间形成的椭球。
    - **速度-力对偶（velocity-force duality）**：速度能力与力能力在机构中相互制约的关系。
    - **运动方向（velocity direction）**：机构容易实现快速运动的方向。
    - **力方向（force direction）**：机构容易实现大力输出的方向。

```mermaid
flowchart TD
    A["单位关节速度球 ||q_dot|| <= 1"] -->|"J"| B["速度椭球"]
    C["单位关节力矩球 ||tau|| <= 1"] -->|"J^{-T}"| D["力椭球"]
    B --> E["长轴 = 高速方向"]
    D --> F["短轴 = 小力方向"]
    E --> G["速度-力对偶"]
    F --> G
```

#### 可操作性椭球与可操作性度量

**可操作性（manipulability）**椭球是速度椭球的缩放形式，其体积为可操作性度量的几何体现。Yoshikawa 提出的可操作性度量定义为：

$$
w(\mathbf{q}) = \sqrt{\det(\mathbf{J}\mathbf{J}^T)}
$$

当 \(w = 0\) 时，机器人处于奇异位形；\(w\) 越大，机器人在各方向上运动与传力的综合性能越好。对于冗余机器人，可使用简化 Jacobian 或加权形式：

$$
w(\mathbf{q}) = \sqrt{\det(\mathbf{J}\mathbf{W}^{-1}\mathbf{J}^T)}
$$

其中 \(\mathbf{W}\) 为正定加权矩阵，可反映不同关节的能力差异。

!!! note "术语解释：可操作性椭球、可操作性度量、Yoshikawa 度量、奇异位形"
    - **可操作性椭球（manipulability ellipsoid）**：描述机构运动传递能力的椭球。
    - **可操作性度量（manipulability measure）**：量化机器人远离奇异程度的标量。
    - **Yoshikawa 度量（Yoshikawa's measure）**：基于 Jacobian 奇异值乘积的可操作性指标。
    - **奇异位形（singular configuration）**：Jacobian 降秩的位形。

```mermaid
flowchart LR
    A["奇异值分解 J = U S V^T"] --> B["奇异值 sigma_i"]
    B --> C["速度椭球半轴 = sigma_i"]
    B --> D["力椭球半轴 = 1/sigma_i"]
    C --> E["可操作性 w = product sigma_i"]
```

#### 力对偶在人形机器人中的意义

在人形机器人中，速度-力对偶无处不在：

1. **手臂操作**：抓持重物时，手臂需伸展到力椭球长轴方向；快速拾取轻物时，可利用速度椭球长轴方向。
2. **腿部支撑**：单腿支撑期，质心投影到地面的点应尽量落在足底力椭球有利方向，以减小踝关节力矩。
3. **全身控制**：QP 控制器在优化关节力矩时，实际上是在力椭球约束下分配任务力。

理解这种对偶性，有助于设计者从机构层面优化 Jacobian 结构，使机器人既能在关键任务方向上产生足够力，又能在需要时快速运动。

!!! note "术语解释：力椭球约束、任务力、Jacobian 结构、机构优化"
    - **力椭球约束（force ellipsoid constraint）**：由机构 Jacobian 决定的力输出能力边界。
    - **任务力（task force）**：完成任务所需的末端力或力矩。
    - **Jacobian 结构（Jacobian structure）**：Jacobian 矩阵的元素分布与奇异值特性。
    - **机构优化（mechanism optimization）**：通过改变连杆长度、关节布局改善性能。
'''

SECTION_CLOSED_CHAINS = r'''
### 8.3.14 闭链机构与并联机构

前述运动学主要讨论**开链机构（open-chain mechanism）**：连杆通过关节串联，末端自由运动。然而，人形机器人在双脚站立、双手抓持物体、攀爬等场景中， limbs 与地面或物体形成**闭链机构（closed-chain mechanism）**。理解闭链约束对建模与控制至关重要[2][3][10]。

!!! note "术语解释：开链机构、闭链机构、闭环约束、并联机构"
    - **开链机构（open-chain mechanism）**：连杆首尾不相连的串联机构。
    - **闭链机构（closed-chain mechanism）**：连杆形成闭合回路的机构。
    - **闭环约束（loop-closure constraint）**：闭合回路中各连杆位姿必须满足的约束。
    - **并联机构（parallel mechanism）**：由动平台、定平台和多条运动支链组成的闭链机构。

#### Grübler 自由度公式与闭链

对于闭链机构，Grübler-Kutzbach 公式需要修正。设有 \(n\) 个连杆、\(j\) 个关节，机构中共有 \(L\) 个独立闭环，则空间机构自由度为：

$$
M = 6(n - 1) - \sum_{i=1}^{j}(6 - f_i) + 6L
$$

或者更常用的等价形式：

$$
M = \sum_{i=1}^{j} f_i - 6L
$$

其中 \(L = j - n + 1\) 为独立闭环数。每增加一个闭环，就增加 6 个闭环约束方程，因此总 DOF 减少 6。

!!! note "术语解释：独立闭环、闭环约束方程、Grübler 修正公式"
    - **独立闭环（independent loop）**：不能由其他闭环组合得到的闭合回路。
    - **闭环约束方程（loop-closure equation）**：描述闭环几何约束的方程。
    - **Grübler 修正公式（modified Grübler formula）**：考虑闭环约束后的自由度计算公式。

人形机器人双足站立时，两条腿与躯干、地面形成多个闭环。若每条腿视为 6-DOF 链，双腿站立时共有 12 个关节自由度，但双脚固定于地面引入 12 个闭环约束（每脚 6-DOF 位姿固定），因此系统整体自由度退化为躯干 6-DOF（浮动基）加上可能的上肢自由度。这些闭环约束必须在运动学与动力学求解中显式处理。

!!! note "术语解释：双脚站立、闭环约束退化、浮动基自由度"
    - **双脚站立（double support）**：两只脚同时接触地面的状态。
    - **闭环约束退化（constraint degeneration）**：闭环约束使系统可用自由度减少。
    - **浮动基自由度（floating-base DOF）**：未受约束时基座的 6 个运动自由度。

```mermaid
flowchart TD
    A["开链腿 6+6 DOF"] --> B["双脚触地"]
    B --> C["每脚 6-DOF 位姿约束"]
    C --> D["12 闭环约束"]
    D --> E["系统退化为浮动基 + 上肢"]
```

#### 并联机构：Stewart 平台、Delta、3-RRR

**并联机构（parallel mechanism）**是闭链机构的重要子类，具有高刚度、高精度、高承载能力的特点。典型代表包括：

1. **Stewart 平台**：由上下平台和 6 条可伸缩支腿组成，具有 6-DOF，广泛用于飞行模拟器、机床、力反馈设备。
2. **Delta 机构**：由三个平行四边形支链驱动动平台，具有 3 个平移自由度，常用于高速拾取机器人。
3. **3-RRR 机构**：三条 RRR 支链连接动平台与定平台，具有平面 3-DOF，常用于精密定位。

!!! note "术语解释：Stewart 平台、Delta 机构、3-RRR 机构、动平台、定平台"
    - **Stewart 平台（Stewart platform）**：由 6 条伸缩支腿驱动的 6-DOF 并联机构。
    - **Delta 机构（Delta mechanism）**：具有 3 个平移自由度的并联机器人。
    - **3-RRR 机构（3-RRR mechanism）**：三条 RRR 支链组成的平面并联机构。
    - **动平台（moving platform）**：并联机构中可运动的平台。
    - **定平台（fixed platform）**：并联机构中固定的平台。

并联机构的正运动学通常比逆运动学困难：给定支链长度求动平台位姿可能有多个解；而逆运动学（由位姿求支链长度）通常更直接。这与串联机构形成鲜明对比。

!!! note "术语解释：并联正运动学、并联逆运动学、多解性"
    - **并联正运动学（parallel forward kinematics）**：由支链变量求动平台位姿。
    - **并联逆运动学（parallel inverse kinematics）**：由动平台位姿求支链变量。
    - **多解性（multi-solution）**：同一输入对应多个可能输出的特性。

```mermaid
flowchart TD
    subgraph Stewart["Stewart 平台"]
    A["上平台"] --> B["6 条伸缩支腿"]
    B --> C["下平台"]
    end
    subgraph Delta["Delta 机构"]
    D["动平台"] --> E["3 条平行四边形支链"]
    E --> F["定平台"]
    end
    subgraph 3RRR["3-RRR 机构"]
    G["动平台"] --> H["3 条 RRR 支链"]
    H --> I["定平台"]
    end
```

#### 人形机器人中的并联元素

虽然人形机器人主体多为串联链，但许多局部机构采用并联思想：

- **踝关节并联驱动**：某些设计用两个线性执行器以并联方式驱动踝关节 roll/pitch，提高扭矩密度与刚度。
- **躯干并联脊柱**：多条弹性执行器并联驱动脊柱，模拟人体脊柱的柔韧性与承载能力。
- **手部并联机构**：手指基座或手掌内部可能采用微型并联机构提高刚度。

!!! note "术语解释：并联驱动、线性执行器、并联脊柱、微型并联机构"
    - **并联驱动（parallel actuation）**：多个执行器以并联方式驱动同一输出。
    - **线性执行器（linear actuator）**：输出直线运动的执行器。
    - **并联脊柱（parallel spine）**：由并联机构实现的脊柱。
    - **微型并联机构（micro parallel mechanism）**：小尺寸的并联机构。

闭链约束在数学上表示为：

$$
\boldsymbol{\Phi}(\mathbf{q}) = \mathbf{0}
$$

其中 \(\boldsymbol{\Phi}\) 为闭环约束方程。对时间求导得到速度级约束：

$$
\mathbf{J}_{\Phi}(\mathbf{q}) \dot{\mathbf{q}} = \mathbf{0}
$$

其中 \(\mathbf{J}_{\Phi} = \partial \boldsymbol{\Phi}/\partial \mathbf{q}\) 为约束雅可比。再求导得到加速度级约束：

$$
\mathbf{J}_{\Phi} \ddot{\mathbf{q}} + \dot{\mathbf{J}}_{\Phi} \dot{\mathbf{q}} = \mathbf{0}
$$

这些约束必须与人形机器人浮动基动力学联立求解，是全身 QP 控制中的核心等式约束来源[3][4]。

!!! note "术语解释：闭环约束方程、约束雅可比、速度级约束、加速度级约束"
    - **闭环约束方程（loop-closure equation）**：描述闭链几何约束的方程。
    - **约束雅可比（constraint Jacobian）**：约束方程对广义坐标的偏导数矩阵。
    - **速度级约束（velocity-level constraint）**：对关节速度的线性约束。
    - **加速度级约束（acceleration-level constraint）**：对关节加速度的约束。

```mermaid
flowchart TD
    A["闭链几何约束 Phi(q)=0"] --> B["速度级约束 J_Phi q_dot=0"]
    B --> C["加速度级约束 J_Phi q_ddot + J_dot q_dot=0"]
    C --> D["与浮动基动力学联立"]
    D --> E["求解关节加速度与接触力"]
```
'''

SECTION_TRAJECTORY_GENERATION = r'''
### 8.3.15 轨迹生成基础

运动学解决了 "到达哪里"，而**轨迹生成（trajectory generation）**解决 "如何到达"——在关节空间或操作空间中生成满足连续性、光滑性与动力学约束的时间序列[2][3][6]。

!!! note "术语解释：轨迹生成、关节空间、操作空间、连续性、光滑性"
    - **轨迹生成（trajectory generation）**：生成机器人随时间变化的位置、速度、加速度序列的过程。
    - **关节空间（joint space）**：以关节变量为坐标的空间。
    - **操作空间（task space）**：以末端位姿为坐标的空间。
    - **连续性（continuity）**：位置、速度、加速度等随时间连续变化无跳变。
    - **光滑性（smoothness）**：轨迹具有连续的高阶导数，减少冲击与振动。

#### 关节空间插值：多项式轨迹

最简单的轨迹是在两个关节位形 \(\mathbf{q}_0\) 与 \(\mathbf{q}_f\) 之间插值。若要求起点与终点速度为零，可使用**三次多项式（cubic polynomial）**：

$$
q(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3, \quad t \in [0, T]
$$

边界条件：

$$
q(0) = q_0, \quad q(T) = q_f, \quad \dot{q}(0) = 0, \quad \dot{q}(T) = 0
$$

解得系数：

$$
a_0 = q_0, \quad a_1 = 0, \quad a_2 = \frac{3}{T^2}(q_f - q_0), \quad a_3 = -\frac{2}{T^3}(q_f - q_0)
$$

三次多项式保证位置与速度连续，但加速度在起点与终点可能不连续，产生有限冲击。

!!! note "术语解释：三次多项式、边界条件、插值、冲击"
    - **三次多项式（cubic polynomial）**：最高次为 3 的多项式函数。
    - **边界条件（boundary condition）**：轨迹在起点与终点需满足的位置、速度、加速度约束。
    - **插值（interpolation）**：在两个或多个已知点之间构造连续函数。
    - **冲击（jerk）**：加速度对时间的导数，不连续冲击会激发振动。

若要求加速度也为零或连续，可使用**五次多项式（quintic polynomial）**：

$$
q(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3 + a_4 t^4 + a_5 t^5
$$

边界条件增加加速度约束：

$$
\ddot{q}(0) = \ddot{q}_0, \quad \ddot{q}(T) = \ddot{q}_f
$$

五次多项式保证位置、速度、加速度均连续，适合高动态人形机器人关节运动。

!!! note "术语解释：五次多项式、加速度连续、高动态运动"
    - **五次多项式（quintic polynomial）**：最高次为 5 的多项式函数。
    - **加速度连续（acceleration continuity）**：加速度在轨迹连接处无跳变。
    - **高动态运动（highly dynamic motion）**：具有大加速度与高速度的运动。

```mermaid
flowchart TD
    A["起点 q0, v0, a0"] --> B["选择多项式阶次"]
    B --> C["三次：位置/速度连续"]
    B --> D["五次：位置/速度/加速度连续"]
    C --> E["求解多项式系数"]
    D --> E
    E --> F["生成 q(t), v(t), a(t)"]
```

#### 笛卡尔直线轨迹与姿态插值

在操作空间中，常需要末端沿直线运动。设起点位姿 \(\mathbf{x}_0 = (\mathbf{p}_0, \mathbf{R}_0)\)，终点位姿 \(\mathbf{x}_f = (\mathbf{p}_f, \mathbf{R}_f)\)。位置部分可直接线性插值：

$$
\mathbf{p}(t) = \mathbf{p}_0 + s(t)(\mathbf{p}_f - \mathbf{p}_0)
$$

其中 \(s(t) \in [0,1]\) 为归一化时间参数。姿态部分不宜用欧拉角直接插值，而应使用**四元数球面线性插值（Slerp）**或**对偶四元数 ScLERP**，以避免万向节锁与姿态路径不自然（参见 8.3.8 节）。

!!! note "术语解释：笛卡尔直线轨迹、位姿插值、四元数 Slerp、姿态路径"
    - **笛卡尔直线轨迹（Cartesian straight-line path）**：末端在笛卡尔空间中沿直线运动的路径。
    - **位姿插值（pose interpolation）**：在两个位姿之间生成连续过渡。
    - **四元数 Slerp（quaternion Slerp）**：四元数间的球面线性插值。
    - **姿态路径（orientation path）**：姿态随时间变化的几何轨迹。

```mermaid
flowchart LR
    A["起点位姿"] --> B{"插值空间"}
    B -->|"位置"| C["直线插值 p(t)"]
    B -->|"姿态"| D["Slerp/ScLERP"]
    C --> E["组合位姿 x(t)"]
    D --> E
    E --> F["逆运动学映射到关节空间"]
```

#### 混合与 S-curve 速度剖面

多段轨迹连接时需要**混合（blending）**以避免在 via point 处完全停顿。混合通过在三段轨迹交点附近用圆弧或多项式过渡，使速度保持连续。

!!! note "术语解释：混合（blending）、via point、过渡曲线、速度连续"
    - **混合（blending）**：在多段轨迹连接处进行平滑过渡。
    - **via point（途经点）**：轨迹经过的中间点。
    - **过渡曲线（transition curve）**：连接两段轨迹的平滑曲线。
    - **速度连续（velocity continuity）**：连接处速度无跳变。

**S-curve 速度剖面（S-curve velocity profile）**在梯形速度剖面基础上增加加减速斜坡，使加速度连续，从而减小机械冲击。其速度曲线呈 "S" 形，分为七段：加加速、匀加速、减加速、匀速、加减速、匀减速、减减速。

!!! note "术语解释：S-curve 速度剖面、加加速、匀加速、减加速、机械冲击"
    - **S-curve 速度剖面（S-curve velocity profile）**：加速度连续变化的速度规划曲线。
    - **加加速（jerk acceleration phase）**：加速度从零增加到最大值的阶段。
    - **匀加速（constant acceleration phase）**：加速度保持最大的阶段。
    - **减加速（deceleration of acceleration）**：加速度从最大值减到零的阶段。
    - **机械冲击（mechanical shock）**：加速度突变引起的结构振动与磨损。

```mermaid
xychart-beta
    title "S-curve 速度剖面示意"
    x-axis "时间 t"
    y-axis "速度 v"
    line [0, 0.02, 0.08, 0.18, 0.32, 0.5, 0.68, 0.82, 0.92, 0.98, 1.0, 1.0, 1.0, 0.98, 0.92, 0.82, 0.68, 0.5, 0.32, 0.18, 0.08, 0.02, 0]
```

#### 时间最优路径参数化（TOPP）概念

对于给定的几何路径 \(\mathbf{q}(s)\)，其中 \(s \in [0,1]\) 为路径参数，时间最优路径参数化（Time-Optimal Path Parameterization, TOPP）寻找最短的遍历时间 \(T\)，同时满足关节速度、加速度与力矩约束[3][6]。

!!! note "术语解释：时间最优路径参数化（TOPP）、路径参数、遍历时间、约束"
    - **时间最优路径参数化（TOPP）**：在满足约束下最小化路径遍历时间的方法。
    - **路径参数（path parameter）**：描述沿几何路径位置的参数 \(s\)。
    - **遍历时间（traversal time）**：沿路径运动所需的总时间。
    - **约束（constraint）**：速度、加速度、力矩等限制条件。

TOPP 的核心是把动力学约束转化为关于 \(\dot{s}\) 与 \(\ddot{s}\) 的约束，并在状态空间 \((s, \dot{s})\) 中寻找最快路径。虽然 TOPP 在人形机器人全身运动中计算复杂，但其思想——**先规划几何路径，再优化时间参数**——是运动规划与控制分治策略的重要体现。

!!! note "术语解释：状态空间、分治策略、动力学约束转化"
    - **状态空间（state space）**：系统状态变量构成的空间。
    - **分治策略（divide-and-conquer strategy）**：把复杂问题分解为子问题分别求解。
    - **动力学约束转化（dynamic constraint transformation）**：把关节空间约束转化为路径参数空间约束。

```mermaid
flowchart TD
    A["几何路径 q(s)"] --> B["速度/加速度/力矩约束"]
    B --> C["转化为 (s, s_dot) 约束"]
    C --> D["求解最优 s(t)"]
    D --> E["最短时间轨迹 q(t)"]
```

#### Python 算例：三次与五次多项式轨迹生成

以下代码生成并绘制一条关节轨迹的三次与五次多项式插值，比较其速度、加速度连续性。

```python
import numpy as np
import matplotlib.pyplot as plt

def cubic_poly(q0, qf, T, t):
    """三次多项式插值，起点终点速度为零。"""
    a0 = q0
    a1 = 0.0
    a2 = 3.0 * (qf - q0) / T**2
    a3 = -2.0 * (qf - q0) / T**3
    return a0 + a1*t + a2*t**2 + a3*t**3

def quintic_poly(q0, qf, T, t):
    """五次多项式插值，起点终点速度/加速度均为零。"""
    a0 = q0
    a1 = 0.0
    a2 = 0.0
    a3 = 10.0 * (qf - q0) / T**3
    a4 = -15.0 * (qf - q0) / T**4
    a5 = 6.0 * (qf - q0) / T**5
    return a0 + a1*t + a2*t**2 + a3*t**3 + a4*t**4 + a5*t**5

T = 2.0
q0, qf = 0.0, 1.0
t = np.linspace(0, T, 200)

q_cubic = cubic_poly(q0, qf, T, t)
q_quintic = quintic_poly(q0, qf, T, t)

# 数值微分求速度与加速度
dt = t[1] - t[0]
v_cubic = np.gradient(q_cubic, dt)
a_cubic = np.gradient(v_cubic, dt)
v_quintic = np.gradient(q_quintic, dt)
a_quintic = np.gradient(v_quintic, dt)

fig, ax = plt.subplots(3, 1, figsize=(8, 7), sharex=True)
ax[0].plot(t, q_cubic, label='三次')
ax[0].plot(t, q_quintic, label='五次')
ax[0].set_ylabel('位置')
ax[0].legend()
ax[0].grid(True)
ax[1].plot(t, v_cubic, label='三次')
ax[1].plot(t, v_quintic, label='五次')
ax[1].set_ylabel('速度')
ax[1].legend()
ax[1].grid(True)
ax[2].plot(t, a_cubic, label='三次')
ax[2].plot(t, a_quintic, label='五次')
ax[2].set_ylabel('加速度')
ax[2].set_xlabel('时间 (s)')
ax[2].legend()
ax[2].grid(True)
plt.suptitle('三次与五次多项式轨迹对比')
plt.tight_layout()
plt.savefig('trajectory_poly.png', dpi=150)
plt.show()
```

!!! note "术语解释：数值微分、位置曲线、速度曲线、加速度曲线"
    - **数值微分（numerical differentiation）**：用离散数据近似计算导数。
    - **位置曲线（position profile）**：位置随时间变化的曲线。
    - **速度曲线（velocity profile）**：速度随时间变化的曲线。
    - **加速度曲线（acceleration profile）**：加速度随时间变化的曲线。
'''

print("Statics/duality, closed chains, and trajectory sections loaded.")


SECTION_PARAMETER_ID = r'''
### 8.3.16 机器人参数辨识

精确的动力学模型是高性能控制的基础，但 CAD 名义质量、惯量、质心位置与实际机器人往往存在偏差。原因在于材料密度不均、加工余量、电缆质量、紧固件公差以及装配差异。**机器人参数辨识（robot parameter identification）**通过测量数据估计真实动力学参数，是提高模型精度的重要手段[3][4][6]。

!!! note "术语解释：机器人参数辨识、动力学参数、名义参数、辨识精度"
    - **机器人参数辨识（robot parameter identification）**：从实验数据估计机器人动力学参数的过程。
    - **动力学参数（dynamic parameters）**：质量、质心位置、惯性张量等描述动力学特性的参数。
    - **名义参数（nominal parameters）**：由 CAD 或设计文档给出的理论参数。
    - **辨识精度（identification accuracy）**：估计参数与真实参数的接近程度。

#### 动力学参数与最小参数集

对于每个连杆 \(i\)，其动力学参数包括：

- 质量 \(m_i\)
- 质心位置 \(\mathbf{r}_{c,i} = (x_{c,i}, y_{c,i}, z_{c,i})\)
- 惯性张量 \(\mathbf{I}_i\)（6 个独立参数：\(I_{xx}, I_{yy}, I_{zz}, I_{xy}, I_{xz}, I_{yz}\)）

共 10 个参数。对于 \(n\) 连杆机器人，名义上有 \(10n\) 个参数，但其中许多参数对关节力矩没有独立影响，或可通过线性组合合并。能够由力矩数据唯一辨识的参数集合称为**最小参数集（base parameter set / minimal parameter set）**。

!!! note "术语解释：惯性张量、质心位置、最小参数集、线性组合"
    - **惯性张量（inertia tensor）**：描述刚体惯性特性的 3×3 矩阵。
    - **质心位置（center of mass position）**：刚体质量加权平均位置。
    - **最小参数集（base parameter set）**：可由观测数据唯一辨识的最小动力学参数集合。
    - **线性组合（linear combination）**：多个参数以系数相加减形成的新参数。

最小参数集的大小取决于机器人构型。例如，对于平面 2-DOF RR 机械臂，每个连杆最多 3 个参数（质量、质心距离、绕轴转动惯量）可辨识；对于 7-DOF 手臂，最小参数集通常远小于 70。确定最小参数集需要对回归矩阵进行秩分析或 QR/SVD 分解。

#### 最小二乘辨识

机器人标准动力学方程可写为：

$$
\boldsymbol{\tau} = \mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q})
$$

可以证明，上式对动力学参数是线性的：

$$
\boldsymbol{\tau} = \mathbf{Y}(\mathbf{q}, \dot{\mathbf{q}}, \ddot{\mathbf{q}}) \, \boldsymbol{\pi}
$$

其中 \(\mathbf{Y}\) 为 \(n \times p\) 的**回归矩阵（regressor matrix）**，\(\boldsymbol{\pi} \in \mathbb{R}^p\) 为待辨识的最小参数向量。通过在多个时刻 \(t_1, t_2, \ldots, t_N\) 测量 \(\mathbf{q}, \dot{\mathbf{q}}, \ddot{\mathbf{q}}, \boldsymbol{\tau}\)，可堆叠成超定方程组：

$$
\begin{bmatrix}
\boldsymbol{\tau}(t_1) \\
\boldsymbol{\tau}(t_2) \\
\vdots \\
\boldsymbol{\tau}(t_N)
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{Y}(t_1) \\
\mathbf{Y}(t_2) \\
\vdots \\
\mathbf{Y}(t_N)
\end{bmatrix}
\boldsymbol{\pi}
$$

用最小二乘法求解：

$$
\hat{\boldsymbol{\pi}} = \left( \boldsymbol{\mathcal{Y}}^T \boldsymbol{\mathcal{Y}} \right)^{-1} \boldsymbol{\mathcal{Y}}^T \boldsymbol{\mathcal{T}}
$$

!!! note "术语解释：回归矩阵、超定方程组、最小二乘解、观测数据"
    - **回归矩阵（regressor matrix）**：力矩对参数的线性系数矩阵。
    - **超定方程组（overdetermined system）**：方程数多于未知数的系统。
    - **最小二乘解（least-squares solution）**：最小化残差平方和的解。
    - **观测数据（observation data）**：实验中测得的输入输出数据。

```mermaid
flowchart TD
    A["设计激励轨迹 q(t)"] --> B["测量 q, q_dot, q_ddot, tau"]
    B --> C["构建回归矩阵 Y"]
    C --> D["堆叠超定方程"]
    D --> E["最小二乘求解 pi"]
    E --> F["验证与物理一致性检查"]
```

#### 激励轨迹设计

辨识精度高度依赖**激励轨迹（excitation trajectory）**的选择。若轨迹使回归矩阵 \(\boldsymbol{\mathcal{Y}}\) 接近秩亏，则参数辨识对噪声极其敏感。常用优化指标为最小化回归矩阵条件数：

$$
\min_{\mathbf{q}(t)} \, \kappa(\boldsymbol{\mathcal{Y}})
$$

其中 \(\kappa(\cdot)\) 为矩阵条件数。工程上常采用有限傅里叶级数（Fourier series）参数化周期性轨迹，再用优化方法寻找最优幅值与相位。

!!! note "术语解释：激励轨迹、条件数、有限傅里叶级数、周期性轨迹"
    - **激励轨迹（excitation trajectory）**：用于激发动力学参数的特定运动。
    - **条件数（condition number）**：矩阵最大奇异值与最小奇异值之比。
    - **有限傅里叶级数（finite Fourier series）**：用有限项正弦/余弦函数表示的周期轨迹。
    - **周期性轨迹（periodic trajectory）**：重复循环的运动轨迹。

#### 物理一致性约束

最小二乘辨识可能得到物理上不可行的参数，例如负质量或非正定的惯性张量。因此需要施加**物理一致性约束（physical consistency constraints）**：

$$
m_i > 0, \quad \mathbf{I}_i \succ 0
$$

即每个连杆质量必须为正，惯性张量必须正定。更精细的约束还包括三角不等式：

$$
I_{xx} + I_{yy} \geq I_{zz}, \quad I_{yy} + I_{zz} \geq I_{xx}, \quad I_{zz} + I_{xx} \geq I_{yy}
$$

以及主转动惯量为正。这些约束使参数辨识从线性最小二乘变为带约束优化问题，可用半定规划（SDP）或投影梯度法求解。

!!! note "术语解释：物理一致性、正定惯性张量、半定规划、投影梯度法"
    - **物理一致性（physical consistency）**：辨识参数符合物理定律（如质量为正、惯量正定）。
    - **正定惯性张量（positive-definite inertia tensor）**：所有特征值为正的惯性张量。
    - **半定规划（Semidefinite Programming, SDP）**：处理半正定约束的凸优化方法。
    - **投影梯度法（projected gradient method）**：将迭代解投影到可行域的优化方法。

```mermaid
flowchart TD
    A["最小二乘估计 pi_hat"] --> B{"物理一致?"}
    B -->|"否"| C["施加 m_i>0, I_i>0 约束"]
    C --> D["带约束优化"]
    D --> E["物理一致参数 pi*"]
    B -->|"是"| E
```

#### 在人形机器人中的应用

人形机器人参数辨识比固定基机械臂更复杂，原因包括：

1. **浮动基**：基座 6-DOF 无编码器，需通过 IMU、运动捕捉或视觉估计。
2. **接触不确定性**：脚-地接触力未知且时变，难以直接测量。
3. **闭链约束**：双脚站立时存在闭环约束，辨识模型需同时考虑。
4. **上肢与躯干耦合**：全身运动使参数耦合更强。

常用方法包括：利用单腿/单臂独立运动辨识局部参数，再整机协调运动辨识耦合参数；结合 IMU 与力传感器数据进行浮动基辨识；使用机器学习辅助的残差补偿模型。精确辨识后的动力学模型可显著改善模型预测控制（MPC）与全身控制的跟踪性能。

!!! note "术语解释：浮动基辨识、接触不确定性、残差补偿、模型预测控制"
    - **浮动基辨识（floating-base identification）**：辨识含浮动基机器人动力学参数。
    - **接触不确定性（contact uncertainty）**：接触力大小、方向与作用点的不确定性。
    - **残差补偿（residual compensation）**：用数据驱动模型补偿动力学残差。
    - **模型预测控制（Model Predictive Control, MPC）**：基于模型在未来时域内优化控制输入。
'''

SECTION_MOTION_PLANNING = r'''
### 8.3.17 运动规划基础

运动规划（motion planning）研究如何在**构型空间（configuration space, C-space）**中为机器人找到一条从起点到终点的可行路径，同时避开障碍物并满足运动学与动力学约束[3][6][65]。

!!! note "术语解释：运动规划、构型空间、障碍物、可行路径、约束"
    - **运动规划（motion planning）**：寻找满足约束的无碰撞路径的过程。
    - **构型空间（configuration space, C-space）**：以机器人全部独立关节变量为坐标的空间。
    - **障碍物（obstacle）**：机器人不能与之碰撞的环境物体。
    - **可行路径（feasible path）**：满足所有约束的路径。
    - **约束（constraint）**：运动学、动力学、几何等限制条件。

#### 构型空间与障碍物

机器人位形由关节向量 \(\mathbf{q}\) 表示，所有可能位形构成 C-space。C-space 中的障碍物区域 \(C_{\text{obs}}\) 由环境障碍物映射得到：

$$
C_{\text{obs}} = \{ \mathbf{q} \in C \mid \text{机器人}(\mathbf{q}) \cap \text{障碍物} \neq \emptyset \}
$$

自由空间为 \(C_{\text{free}} = C \setminus C_{\text{obs}}\)。运动规划的本质就是在 \(C_{\text{free}}\) 中寻找连续路径。

!!! note "术语解释：C-space 障碍物、自由空间、连续路径、碰撞检测"
    - **C-space 障碍物（C-space obstacle）**：构型空间中被障碍物占据的区域。
    - **自由空间（free space）**：构型空间中不与障碍物相交的区域。
    - **连续路径（continuous path）**：参数连续的位形序列。
    - **碰撞检测（collision detection）**：判断机器人是否与障碍物相交的计算。

对于高维 C-space（人形机器人可达 30-60 维），显式构造 \(C_{\text{obs}}\) 不可行，因此需要**隐式采样**方法。

#### 采样法规划：RRT 与 PRM

**快速探索随机树（Rapidly-exploring Random Tree, RRT）**是单查询（single-query）采样规划器：从起点出发，不断在 C-space 中随机采样，并将新样本连接到树上最近的节点，直到到达目标附近。RRT 适合高维空间且不需要预建图，常用于人形机器人全身运动规划。

!!! note "术语解释：RRT、随机树、单查询规划器、最近节点"
    - **RRT（Rapidly-exploring Random Tree）**：从起点生长随机树的运动规划算法。
    - **随机树（random tree）**：通过随机采样逐步构建的树形数据结构。
    - **单查询规划器（single-query planner）**：为单次起点-终点对规划路径的算法。
    - **最近节点（nearest node）**：树中距离新样本最近的节点。

RRT 基本步骤：

1. 初始化树 \(T\) 包含起点 \(\mathbf{q}_{\text{start}}\)。
2. 随机采样 \(\mathbf{q}_{\text{rand}}\)。
3. 找到 \(T\) 中离 \(\mathbf{q}_{\text{rand}}\) 最近的节点 \(\mathbf{q}_{\text{near}}\)。
4. 从 \(\mathbf{q}_{\text{near}}\) 向 \(\mathbf{q}_{\text{rand}}\) 扩展固定步长得到 \(\mathbf{q}_{\text{new}}\)。
5. 若 \(\mathbf{q}_{\text{new}}\) 无碰撞，则加入 \(T\)。
6. 若 \(\mathbf{q}_{\text{new}}\) 到达目标附近，返回路径。

!!! note "术语解释：随机采样、扩展步长、无碰撞检查、目标附近"
    - **随机采样（random sampling）**：按概率分布生成随机位形。
    - **扩展步长（extension step）**：从最近节点向随机样本移动的距离。
    - **无碰撞检查（collision-free check）**：验证路径段不与障碍物相交。
    - **目标附近（goal region）**：围绕目标点的小区域，到达即认为成功。

**概率路线图（Probabilistic Roadmap, PRM）**是多查询（multi-query）规划器：先通过大量随机采样在 \(C_{\text{free}}\) 中构建 roadmap（图），然后对任意起点-终点对，只需把起点/终点连接到 roadmap 再用图搜索（如 A*、Dijkstra）即可。PRM 适合同一环境中多次规划。

!!! note "术语解释：PRM、概率路线图、多查询规划器、图搜索"
    - **PRM（Probabilistic Roadmap）**：先构建路线图再查询路径的规划算法。
    - **概率路线图（probabilistic roadmap）**：C-free 中采样节点与无碰撞边构成的图。
    - **多查询规划器（multi-query planner）**：可重复用于多个起点-终点对的规划算法。
    - **图搜索（graph search）**：在图中寻找最短或最优路径的算法。

```mermaid
flowchart TD
    subgraph RRT["RRT 算法"]
    A["起点"] --> B["随机采样"]
    B --> C["找最近节点"]
    C --> D["扩展新节点"]
    D --> E{"无碰撞?"}
    E -->|"是"| F["加入树"]
    E -->|"否"| B
    F --> G{"到达目标?"}
    G -->|"否"| B
    G -->|"是"| H["返回路径"]
    end
```

#### 搜索法规划：A* 与栅格

在低维 C-space 或离散化栅格上，**A* 算法**通过启发函数 \(h(\mathbf{q})\) 引导搜索，高效找到最优路径。A* 维护每个节点的估计总代价：

$$
f(\mathbf{q}) = g(\mathbf{q}) + h(\mathbf{q})
$$

其中 \(g(\mathbf{q})\) 为从起点到 \(\mathbf{q}\) 的实际代价，\(h(\mathbf{q})\) 为从 \(\mathbf{q}\) 到目标的启发估计。若 \(h\) 满足可采纳性（admissible，即从不高估真实代价），A* 保证最优。

!!! note "术语解释：A* 算法、启发函数、可采纳性、最优路径"
    - **A* 算法（A-star algorithm）**：使用启发函数引导的图搜索算法。
    - **启发函数（heuristic function）**：估计从当前节点到目标代价的函数。
    - **可采纳性（admissibility）**：启发函数不高估真实代价的性质。
    - **最优路径（optimal path）**：代价最小的可行路径。

对于人形机器人，栅格 A* 常用于：

- 足部落脚点规划（二维或三维栅格）。
- 上肢在简化任务空间中的避障路径。
- 作为高层规划器指导低层全身控制器。

!!! note "术语解释：落脚点规划、任务空间、高层规划器、低层控制器"
    - **落脚点规划（footstep planning）**：确定行走时脚应落在哪里。
    - **任务空间（task space）**：描述特定任务变量的空间。
    - **高层规划器（high-level planner）**：负责粗粒度决策的规划模块。
    - **低层控制器（low-level controller）**：执行高层规划的实时控制器。

```mermaid
flowchart LR
    A["栅格化 C-space"] --> B["A* 搜索"]
    B --> C["启发函数引导"]
    C --> D["最优/可行路径"]
    D --> E["平滑与轨迹生成"]
```

#### Roadmap 与 Tree 方法对比

| 方法 | 类型 | 适用场景 | 优点 | 缺点 |
|---|---|---|---|---|
| PRM | 多查询 | 同一环境多次规划 | 预计算后查询快 | 构建 roadmap 耗时 |
| RRT | 单查询 | 高维、单次规划 | 实现简单、扩展快 | 路径通常非最优 |
| RRT* | 单查询 | 需要渐近最优 | 渐近最优 | 计算量较大 |
| A* | 搜索 | 低维栅格 | 保证最优 | 维度灾难 |

!!! note "术语解释：RRT*、渐近最优、维度灾难、预计算"
    - **RRT***：RRT 的渐近最优变种。
    - **渐近最优（asymptotic optimality）**：随着采样数增加，解收敛到最优的性质。
    - **维度灾难（curse of dimensionality）**：维度增加导致计算量指数增长。
    - **预计算（precomputation）**：在正式使用前提前计算并存储结果。

#### 全身运动规划

人形机器人全身运动规划需在 30-60 维 C-space 中同时考虑：

- 双足支撑与单足支撑切换。
- 自碰撞 avoidance。
- 平衡约束（ZMP、摩擦锥、CoP）。
- 任务约束（手臂末端位姿、视线方向）。

常用策略是**分层规划（hierarchical planning）**：高层规划 footsteps 与躯干运动，中层规划四肢关节轨迹，低层用 QP 或 MPC 实时跟踪。采样规划器常用于高层，而优化-based 方法（如 CHOMP、TrajOpt）常用于中层轨迹优化。

!!! note "术语解释：全身运动规划、分层规划、自碰撞、优化轨迹"
    - **全身运动规划（whole-body motion planning）**：同时规划全身所有自由度的运动。
    - **分层规划（hierarchical planning）**：在不同抽象层次上分别规划再协调。
    - **自碰撞（self-collision）**：机器人自身不同部分之间发生碰撞。
    - **优化轨迹（trajectory optimization）**：通过数值优化改进轨迹性能指标。

```mermaid
flowchart TD
    A["高层：footsteps/躯干路径"] --> B["中层：四肢关节轨迹"]
    B --> C["低层：QP/MPC 跟踪"]
    C --> D["实时全身运动"]
```
'''

print("Parameter identification and motion planning sections loaded.")


SECTION_WBC = r'''
#### 8.4.10 全身控制

人形机器人同时需要完成多个任务：保持平衡、跟踪期望落脚点、操作物体、避免奇异与自碰撞。**全身控制（Whole-Body Control, WBC）**通过把多个任务映射到关节空间，并在冗余自由度中协调这些任务，是现代高动态人形机器人控制的核心框架[53][54][55]。

!!! note "术语解释：全身控制（WBC）、任务空间、冗余协调、多任务控制"
    - **全身控制（Whole-Body Control, WBC）**：同时协调全身多自由度完成多项任务的控制框架。
    - **任务空间（task space）**：描述特定任务变量的空间，如质心位置、末端位姿。
    - **冗余协调（redundancy resolution）**：在冗余自由度内分配任务优先级。
    - **多任务控制（multi-task control）**：同时实现多个可能相互冲突的任务目标。

##### 8.4.10.1 任务空间逆动力学基础

最基础的 WBC 方法是**任务空间逆动力学（task-space inverse dynamics, TSID）**：给定各任务的期望加速度 \(\ddot{\mathbf{x}}_i^*\)，通过雅可比把任务加速度映射到关节加速度：

$$
\ddot{\mathbf{x}}_i = \mathbf{J}_i \dot{\mathbf{v}} + \dot{\mathbf{J}}_i \mathbf{v}
$$

其中 \(\mathbf{v}\) 为广义速度（包含浮动基速度与关节速度），\(\dot{\mathbf{v}}\) 为广义加速度。TSID 的核心思想是：先确定任务层期望的加速度，再通过逆动力学反解所需的关节力矩与接触力。

!!! note "术语解释：任务空间逆动力学（TSID）、广义速度、广义加速度、期望加速度"
    - **任务空间逆动力学（TSID）**：由任务空间期望加速度反解关节加速度与力矩的方法。
    - **广义速度（generalized velocity）**：描述系统速度的广义坐标导数。
    - **广义加速度（generalized acceleration）**：广义速度对时间的导数。
    - **期望加速度（desired acceleration）**：任务变量应达到的目标加速度。

**操作空间控制（Operational Space Control, OSC）**是另一种常见框架。它直接把任务空间力/力矩映射为关节力矩：

$$
\boldsymbol{\tau} = \sum_i \mathbf{J}_i^T \mathbf{F}_i^* + \mathbf{N}^T \boldsymbol{\tau}_0
$$

其中 \(\mathbf{F}_i^*\) 为第 \(i\) 个任务所需的虚拟力，\(\mathbf{N}\) 为投影到任务零空间的矩阵，\(\boldsymbol{\tau}_0\) 为零空间中的任意力矩。

!!! note "术语解释：操作空间控制（OSC）、虚拟力、零空间投影"
    - **操作空间控制（OSC）**：在操作空间设计控制力并映射到关节空间的控制方法。
    - **虚拟力（virtual force）**：为完成任务在任务空间中施加的等效力。
    - **零空间投影（null-space projection）**：把关节力矩投影到不干扰高优先级任务的子空间。

```mermaid
flowchart TD
    A["任务期望 x_des"] --> B["任务雅可比 J_i"]
    B --> C["虚拟力 F_i* 或期望加速度 x_ddot_i*"]
    C --> D["映射到关节力矩/加速度"]
    D --> E["执行器输出"]
```

##### 8.4.10.2 任务优先级：严格层次 vs 加权和

多任务 WBC 必须处理任务冲突。例如，手臂操作任务可能要求躯干前倾，而平衡任务要求躯干直立。常用两种策略：

1. **严格层次（strict hierarchy）**：高优先级任务必须完全满足，低优先级任务只能在高优先级任务的零空间内执行。
2. **加权和（weighted sum）**：把所有任务按重要性加权，求解一个优化问题，允许任务之间权衡。

!!! note "术语解释：严格层次、加权和、任务冲突、零空间"
    - **严格层次（strict hierarchy）**：按优先级严格排序任务的策略。
    - **加权和（weighted sum）**：把多个任务目标加权相加的优化策略。
    - **任务冲突（task conflict）**：不同任务对关节运动要求不一致。
    - **零空间（null space）**：不改变高优先级任务输出的关节运动子空间。

对于严格层次，设主任务雅可比为 \(\mathbf{J}_1\)，次级任务雅可比为 \(\mathbf{J}_2\)。关节速度可分解为：

$$
\dot{\mathbf{q}} = \mathbf{J}_1^\dagger \dot{\mathbf{x}}_1^* + \mathbf{N}_1 \mathbf{J}_2^\dagger \left( \dot{\mathbf{x}}_2^* - \mathbf{J}_2 \mathbf{J}_1^\dagger \dot{\mathbf{x}}_1^* \right)
$$

其中 \(\mathbf{N}_1 = \mathbf{I} - \mathbf{J}_1^\dagger \mathbf{J}_1\) 为投影到 \(\mathbf{J}_1\) 零空间的矩阵。上式第一项完成主任务，第二项在不影响主任务的前提下完成次级任务。

!!! note "术语解释：主任务雅可比、次级任务雅可比、零空间矩阵、伪逆"
    - **主任务雅可比（primary task Jacobian）**：最高优先级任务的雅可比矩阵。
    - **次级任务雅可比（secondary task Jacobian）**：次优先级任务的雅可比矩阵。
    - **零空间矩阵（null-space matrix）**：投影到某任务零空间的矩阵。
    - **伪逆（pseudoinverse）**：对非方或秩亏矩阵的广义逆。

对于加权和 QP，所有任务统一为优化目标：

$$
\min_{\dot{\mathbf{v}}, \boldsymbol{\tau}, \mathbf{F}_c} \ \sum_i w_i \left\| \mathbf{J}_i \dot{\mathbf{v}} + \dot{\mathbf{J}}_i \mathbf{v} - \ddot{\mathbf{x}}_i^* \right\|^2 + \text{正则项}
$$

权重 \(w_i\) 反映任务相对重要性。严格层次可通过极大权重差距近似，但精确实现需要逐层零空间投影。

!!! note "术语解释：权重、优化目标、正则项、近似层次"
    - **权重（weight）**：反映任务重要性的系数。
    - **优化目标（objective）**：需要最小化的函数。
    - **正则项（regularization）**：改善数值稳定性或避免平凡解的附加项。
    - **近似层次（approximate hierarchy）**：通过大权差近似严格任务优先级。

```mermaid
flowchart TD
    A["任务优先级栈"] --> B["主任务：平衡/CoM"]
    A --> C["次任务：足端轨迹"]
    A --> D["再次任务：手臂操作"]
    A --> E["最低优先级：姿态优化"]
    B --> F["J_1^dagger x_1_dot"]
    C --> G["N_1 J_2^dagger x_2_dot"]
    D --> H["N_12 J_3^dagger x_3_dot"]
    E --> I["零空间任务"]
    F --> J["合成关节速度/力矩"]
    G --> J
    H --> J
    I --> J
```

##### 8.4.10.3 基于 QP 的全身控制公式

现代 WBC 的主流实现是**全身 QP 控制**。它把所有任务统一为二次规划问题，同时显式施加动力学、摩擦锥、关节力矩限、关节限位等约束。

!!! note "术语解释：全身 QP 控制、二次规划、等式约束、不等式约束"
    - **全身 QP 控制（whole-body QP control）**：用二次规划求解全身控制输入的方法。
    - **二次规划（Quadratic Programming, QP）**：目标函数为二次、约束为线性的优化问题。
    - **等式约束（equality constraint）**：必须精确满足的线性等式。
    - **不等式约束（inequality constraint）**：必须满足的不等式限制。

优化变量通常包括广义加速度 \(\dot{\mathbf{v}}\)、关节力矩 \(\boldsymbol{\tau}\) 与接触力 \(\mathbf{F}_c\)。目标函数为各任务跟踪误差加权和加上正则项：

$$
\min_{\dot{\mathbf{v}}, \boldsymbol{\tau}, \mathbf{F}_c} \quad \sum_i w_i \left\| \mathbf{J}_i \dot{\mathbf{v}} + \dot{\mathbf{J}}_i \mathbf{v} - \ddot{\mathbf{x}}_i^* \right\|^2 + w_{\tau}\|\boldsymbol{\tau}\|^2 + w_{f}\|\mathbf{F}_c\|^2
$$

约束条件包括：

**动力学约束**：

$$
\mathbf{M}\dot{\mathbf{v}} + \mathbf{C}\mathbf{v} + \mathbf{g} = \mathbf{S}^T \boldsymbol{\tau} + \sum_c \mathbf{J}_{c}^T \mathbf{F}_c
$$

**摩擦锥约束**：

$$
\mathbf{F}_c \in \mathcal{C}(\mu)
$$

**关节力矩限**：

$$
\boldsymbol{\tau}_{\min} \leq \boldsymbol{\tau} \leq \boldsymbol{\tau}_{\max}
$$

**关节限位（速度级）**：

$$
\mathbf{q}_{\min} \leq \mathbf{q} + \Delta t \, \dot{\mathbf{q}} \leq \mathbf{q}_{\max}
$$

!!! note "术语解释：动力学约束、摩擦锥约束、关节力矩限、关节限位"
    - **动力学约束（dynamic constraint）**：由牛顿-欧拉或拉格朗日方程给出的等式。
    - **摩擦锥约束（friction cone constraint）**：接触力必须位于摩擦锥内的约束。
    - **关节力矩限（torque limit）**：执行器可提供的最大/最小力矩。
    - **关节限位（joint limit）**：关节角度允许的范围。

```mermaid
flowchart TD
    A["任务期望 x*_i"] --> B["QP 求解器"]
    C["动力学约束"] --> B
    D["摩擦锥约束"] --> B
    E["力矩/关节限"] --> B
    B --> F["优化变量"]
    F --> G["广义加速度 v_dot"]
    F --> H["关节力矩 tau"]
    F --> I["接触力 F_c"]
    G --> J["数值积分得到 v, q"]
    H --> K["执行器指令"]
    I --> L["稳定性/防滑验证"]
```

##### 8.4.10.4 接触力旋量锥、摩擦金字塔与 CoP 约束

真实接触不仅要求力在摩擦锥内，还要求**压力中心（Center of Pressure, CoP）**位于支撑多边形内，否则机器人会绕脚边缘倾倒。对于多接触点情况，更一般地需要约束**接触力旋量（contact wrench）**位于**力旋量锥（wrench cone）**内。

!!! note "术语解释：接触力旋量、力旋量锥、压力中心（CoP）、支撑多边形"
    - **接触力旋量（contact wrench）**：接触点处的力与力矩组合。
    - **力旋量锥（wrench cone）**：所有可行接触力旋量构成的凸锥。
    - **压力中心（Center of Pressure, CoP）**：地面反作用力在接触面上的等效作用点。
    - **支撑多边形（support polygon）**：支撑脚与地面接触点构成的凸包。

单个接触点的力旋量可表示为 \(\mathbf{w}_c = (\mathbf{f}_c, \boldsymbol{\tau}_c) \in \mathbb{R}^6\)。多个接触点的合力旋量必须能够平衡重力、惯性力与任务力。力旋量锥 \(\mathcal{W}\) 是所有满足摩擦锥与 CoP 约束的力旋量集合。

!!! note "术语解释：合力旋量、重力、惯性力、任务力"
    - **合力旋量（resultant wrench）**：多个力旋量的矢量和。
    - **重力（gravity force）**：由地球引力产生的力。
    - **惯性力（inertial force）**：由加速度引起的虚拟力。
    - **任务力（task force）**：完成任务所需的力或力矩。

为便于 QP 求解，常把圆形摩擦锥线性化为**摩擦金字塔（friction pyramid）**：

$$
|f_x| \leq \frac{\mu f_z}{\sqrt{2}}, \quad |f_y| \leq \frac{\mu f_z}{\sqrt{2}}
$$

或用四个平面近似：

$$
|f_x| \leq \mu f_z, \quad |f_y| \leq \mu f_z
$$

线性化后，摩擦约束与 CoP 约束都变为线性不等式，可直接嵌入 QP。

!!! note "术语解释：摩擦金字塔、线性化摩擦锥、线性不等式"
    - **摩擦金字塔（friction pyramid）**：用多面体近似圆形摩擦锥的线性化模型。
    - **线性化摩擦锥（linearized friction cone）**：把非线性摩擦锥约束用线性不等式近似。
    - **线性不等式（linear inequality）**：关于优化变量的线性不等式约束。

```mermaid
flowchart TD
    A["接触力 f = (fx, fy, fz)"] --> B{"线性化摩擦锥"}
    B --> C["|fx| <= mu fz"]
    B --> D["|fy| <= mu fz"]
    C --> E["力旋量锥 W"]
    D --> E
    F["CoP 在支撑多边形内"] --> E
    E --> G["QP 不等式约束"]
```

##### 8.4.10.5 基于动量的控制

除了直接跟踪任务加速度，WBC 还可以调节**质心动量（centroidal momentum）**，特别是**中心角动量（centroidal angular momentum）**。通过控制角动量，可以改善动态平衡与上身协调[41][53]。

!!! note "术语解释：质心动量、中心角动量、动量控制、上身协调"
    - **质心动量（centroidal momentum）**：机器人总线动量与相对质心总角动量的组合。
    - **中心角动量（centroidal angular momentum）**：相对于质心的总角动量。
    - **动量控制（momentum control）**：通过调节接触力控制质心动量的方法。
    - **上身协调（upper-body coordination）**：利用躯干与手臂运动补偿下肢角动量。

质心动量矩阵（CMM）\(\mathbf{A}_G\) 把广义速度映射为质心动量：

$$
\begin{bmatrix} \mathbf{P} \\ \mathbf{L}_G \end{bmatrix} = \mathbf{A}_G(\mathbf{q}) \, \mathbf{v}
$$

其时间导数满足：

$$
\frac{d}{dt} \begin{bmatrix} \mathbf{P} \\ \mathbf{L}_G \end{bmatrix} = \begin{bmatrix} m \mathbf{g} + \sum_j \mathbf{F}_j \\ \sum_j (\mathbf{r}_j - \mathbf{r}_G) \times \mathbf{F}_j \end{bmatrix}
$$

在 WBC 中，可添加动量跟踪任务：

$$
\min \, \left\| \mathbf{A}_G \dot{\mathbf{v}} + \dot{\mathbf{A}}_G \mathbf{v} - \begin{bmatrix} \dot{\mathbf{P}}^* \\ \dot{\mathbf{L}}_G^* \end{bmatrix} \right\|^2
$$

通过调节期望动量变化率 \(\dot{\mathbf{P}}^*\) 与 \(\dot{\mathbf{L}}_G^*\)，控制器可同时实现平衡与姿态调节。例如，当受到侧向推扰时，可命令角动量变化以产生恢复力矩，同时规划手臂反向摆动补偿。

!!! note "术语解释：动量跟踪任务、期望动量变化率、恢复力矩、推扰"
    - **动量跟踪任务（momentum tracking task）**：使实际动量跟踪期望动量的任务。
    - **期望动量变化率（desired momentum rate）**：期望的质心动量时间导数。
    - **恢复力矩（recovery moment）**：使机器人恢复平衡的力矩。
    - **推扰（push disturbance）**：外部推力扰动。

```mermaid
flowchart TD
    A["期望质心动量变化"] --> B["CMM 任务"]
    B --> C["QP 优化"]
    C --> D["接触力分配"]
    D --> E["线动量控制 CoM 运动"]
    D --> F["角动量控制姿态"]
```

##### 8.4.10.6 Python 算例：简化的全身 QP 控制

以下代码演示一个概念性的全身 QP 问题：一个 3 连杆平面机器人（类似简化腿或臂），希望末端跟踪期望加速度，同时满足关节力矩限制与摩擦锥约束。由于 `qpsolvers` 可能未安装，这里使用 `scipy.optimize.minimize` 的 SLSQP 算法求解。

```python
import numpy as np
from scipy.optimize import minimize

# 3 连杆平面机械臂参数
L = np.array([0.4, 0.35, 0.25])  # 连杆长度
m_total = 10.0                    # 简化总质量
g = 9.81
mu = 0.6                          # 摩擦系数

# 当前状态
q = np.array([0.2, 0.5, -0.3])    # 关节角
qd = np.array([0.1, -0.2, 0.15])  # 关节速度

# 正运动学：末端位置
def fk(q):
    x = L[0]*np.cos(q[0]) + L[1]*np.cos(q[0]+q[1]) + L[2]*np.cos(q[0]+q[1]+q[2])
    y = L[0]*np.sin(q[0]) + L[1]*np.sin(q[0]+q[1]) + L[2]*np.sin(q[0]+q[1]+q[2])
    return np.array([x, y])

# Jacobian 2x3
def jacobian(q):
    s1, c1 = np.sin(q[0]), np.cos(q[0])
    s12, c12 = np.sin(q[0]+q[1]), np.cos(q[0]+q[1])
    s123, c123 = np.sin(q[0]+q[1]+q[2]), np.cos(q[0]+q[1]+q[2])
    J = np.array([
        [-L[0]*s1 - L[1]*s12 - L[2]*s123, -L[1]*s12 - L[2]*s123, -L[2]*s123],
        [ L[0]*c1 + L[1]*c12 + L[2]*c123,  L[1]*c12 + L[2]*c123,  L[2]*c123]
    ])
    return J

# 期望末端加速度（例如向右上方加速）
x_des = np.array([1.0, 0.5])

# 优化变量：[q_ddot (3), tau (3), F_x, F_z]
# 简化模型：M*q_ddot + g_proj = tau + J^T * F
# 假设 M 为对角阵
M_diag = np.array([1.0, 0.8, 0.5])

def objective(z):
    qdd = z[:3]
    tau = z[3:6]
    F = z[6:8]
    # 末端实际加速度（忽略 J_dot * qd 项，仅示意）
    x_ddot = jacobian(q) @ qdd
    # 任务跟踪误差
    err_task = x_ddot - x_des
    # 正则项
    return np.sum(err_task**2) + 1e-4*np.sum(tau**2) + 1e-4*np.sum(F**2)

def dynamics_eq(z):
    qdd = z[:3]
    tau = z[3:6]
    F = z[6:8]
    # 简化重力投影：每个关节承受其外侧连杆重力
    g_tau = np.array([
        (L[0]*np.cos(q[0]) + L[1]*np.cos(q[0]+q[1]) + L[2]*np.cos(q[0]+q[1]+q[2])) * m_total*g/3,
        (L[1]*np.cos(q[0]+q[1]) + L[2]*np.cos(q[0]+q[1]+q[2])) * m_total*g/3,
        (L[2]*np.cos(q[0]+q[1]+q[2])) * m_total*g/3
    ])
    return M_diag * qdd + g_tau - tau - jacobian(q).T @ F

# 不等式约束：摩擦锥 |Fx| <= mu * Fz, Fz >= 0
# 用线性形式：Fx - mu*Fz <= 0, -Fx - mu*Fz <= 0, -Fz <= 0
def friction_cone(z):
    F = z[6:8]
    fx, fz = F[0], F[1]
    return np.array([mu*fz - fx, mu*fz + fx, fz])

# 初始猜测
z0 = np.zeros(8)
z0[7] = m_total * g  # 初始法向力

# 约束与边界
constraints = [
    {'type': 'eq', 'fun': dynamics_eq},
    {'type': 'ineq', 'fun': friction_cone}
]
bounds = [(-10, 10)]*3 + [(-50, 50)]*3 + [(-200, 200), (0, 500)]

res = minimize(objective, z0, method='SLSQP', bounds=bounds, constraints=constraints,
               options={'ftol': 1e-9, 'maxiter': 200})

if res.success:
    z_opt = res.x
    print("优化成功")
    print("关节加速度 q_ddot:", z_opt[:3])
    print("关节力矩 tau:", z_opt[3:6])
    print("接触力 F:", z_opt[6:8])
    print("实际末端加速度:", jacobian(q) @ z_opt[:3])
    print("期望末端加速度:", x_des)
else:
    print("优化失败:", res.message)
```

!!! note "术语解释：SLSQP、目标函数、等式约束、不等式约束、优化变量"
    - **SLSQP（Sequential Least Squares Programming）**：序列最小二乘规划优化算法。
    - **目标函数（objective function）**：优化中需要最小化的函数。
    - **优化变量（optimization variable）**：优化问题中待求解的变量。

该算例仅为概念演示：真实 WBC 需要完整的浮动基动力学、多个任务、多个接触点以及实时 QP 求解器（如 OSQP、qpOASES、ProxQP）。但其核心结构——任务跟踪目标 + 动力学等式 + 摩擦锥不等式 + 力矩限——与现代人形机器人控制器完全一致。

!!! note "术语解释：实时 QP 求解器、OSQP、qpOASES、ProxQP"
    - **实时 QP 求解器（real-time QP solver）**：能够在控制周期内求解 QP 的优化软件。
    - **OSQP**：基于算子分裂的稀疏 QP 求解器。
    - **qpOASES**：针对模型预测控制的参数化主动集 QP 求解器。
    - **ProxQP**：基于近端算法的 QP 求解器。
'''

print("WBC section loaded.")


SECTION_FORCE_CONTROL = r'''
### 8.4.11 力控制与阻抗/导纳控制

人形机器人不仅要精确控制位置，还必须与环境进行力交互：开门、拧瓶盖、与人握手、不平地面站立、落地缓冲等任务都要求控制接触力而非单纯位置。**力控制（force control）**与**柔顺控制（compliance control）**正是处理这类交互的核心技术[2][3][73]。

!!! note "术语解释：力控制、柔顺控制、接触力、环境交互、力交互"
    - **力控制（force control）**：直接控制机器人与环境之间接触力的方法。
    - **柔顺控制（compliance control）**：使机器人在受力时按期望动态响应的控制方法。
    - **接触力（contact force）**：机器人与外界接触时相互作用的力。
    - **环境交互（environment interaction）**：机器人与周围环境的物理交互。
    - **力交互（force interaction）**：通过力进行的交互行为。

#### 混合力/位置控制

在许多任务中，某些方向需要控制位置，而另一些方向需要控制力。例如，沿桌面推动物体时，水平方向控制位置，垂直方向控制接触力。**混合力/位置控制（hybrid force/position control）**通过选择矩阵 \(\boldsymbol{\Sigma}\) 把任务空间分解为位置控制子空间与力控制子空间：

$$
\boldsymbol{\Sigma} = \text{diag}(\sigma_1, \ldots, \sigma_m), \quad \sigma_i \in \{0,1\}
$$

- 若 \(\sigma_i = 1\)，第 \(i\) 个方向控制位置。
- 若 \(\sigma_i = 0\)，第 \(i\) 个方向控制力。

!!! note "术语解释：混合力/位置控制、选择矩阵、位置控制子空间、力控制子空间"
    - **混合力/位置控制（hybrid force/position control）**：同时控制力和位置的策略。
    - **选择矩阵（selection matrix）**：选择位置控制方向或力控制方向的对角矩阵。
    - **位置控制子空间（position-controlled subspace）**：由选择矩阵选中的位置控制方向。
    - **力控制子空间（force-controlled subspace）**：未被选择矩阵选中的力控制方向。

假设任务空间误差为 \(\mathbf{e} = \mathbf{x}_d - \mathbf{x}\)，力误差为 \(\mathbf{e}_F = \mathbf{F}_d - \mathbf{F}\)，则控制律为：

$$
\mathbf{F}_{\text{cmd}} = \boldsymbol{\Sigma} \, \mathbf{K}_p (\mathbf{x}_d - \mathbf{x}) + (\mathbf{I} - \boldsymbol{\Sigma}) \, \mathbf{K}_f (\mathbf{F}_d - \mathbf{F})
$$

再通过 \(\boldsymbol{\tau} = \mathbf{J}^T \mathbf{F}_{\text{cmd}}\) 映射到关节力矩。这种控制在工业装配（如插轴入孔）中广泛应用。

!!! note "术语解释：位置误差、力误差、比例增益、控制律"
    - **位置误差（position error）**：期望位置与实际位置之差。
    - **力误差（force error）**：期望力与实际力之差。
    - **比例增益（proportional gain）**：控制器中误差的比例系数。
    - **控制律（control law）**：决定控制输出的数学表达式。

```mermaid
flowchart TD
    A["任务空间"] --> B["选择矩阵 Sigma"]
    B --> C["位置控制子空间"]
    B --> D["力控制子空间"]
    C --> E["位置反馈 Kp e_x"]
    D --> F["力反馈 Kf e_F"]
    E --> G["合成任务力 F_cmd"]
    F --> G
    G --> H["tau = J^T F_cmd"]
```

#### 阻抗控制

**阻抗控制（impedance control）**不把位置与力分开控制，而是调节机器人末端表现出的**机械阻抗（mechanical impedance）**——即质量-阻尼-弹簧特性。它把力与位置/速度关系定义为：

$$
\mathbf{F} = \mathbf{M}_d (\ddot{\mathbf{x}}_d - \ddot{\mathbf{x}}) + \mathbf{D}_d (\dot{\mathbf{x}}_d - \dot{\mathbf{x}}) + \mathbf{K}_d (\mathbf{x}_d - \mathbf{x})
$$

其中 \(\mathbf{M}_d\)、\(\mathbf{D}_d\)、\(\mathbf{K}_d\) 分别为期望惯性、阻尼与刚度矩阵。该方程表明：当末端偏离期望轨迹时，机器人会产生与偏离量成比例的恢复力；当受到外部扰动时，机器人会按期望动态响应。

!!! note "术语解释：阻抗控制、机械阻抗、期望惯性、期望阻尼、期望刚度"
    - **阻抗控制（impedance control）**：控制机器人端表现出的质量-阻尼-弹簧特性的方法。
    - **机械阻抗（mechanical impedance）**：力与运动（位移、速度、加速度）之间的动态关系。
    - **期望惯性（desired inertia）\(\mathbf{M}_d\)**：期望的惯性特性矩阵。
    - **期望阻尼（desired damping）\(\mathbf{D}_d\)**：期望的阻尼特性矩阵。
    - **期望刚度（desired stiffness）\(\mathbf{K}_d\)**：期望的刚度特性矩阵。

阻抗控制可分为两类：

1. **力矩级阻抗控制（torque-level impedance）**：直接根据阻抗方程计算期望任务力，再通过 \(\boldsymbol{\tau} = \mathbf{J}^T \mathbf{F}\) 映射到关节力矩。需要力矩控制内环。
2. **位置级阻抗控制（position-level impedance）**：在位置控制外环中加入力-位置关系，通过位置指令间接实现柔顺。实现简单但带宽受限。

!!! note "术语解释：力矩级阻抗、位置级阻抗、力矩控制内环、位置控制外环"
    - **力矩级阻抗（torque-level impedance）**：直接输出关节力矩的阻抗控制。
    - **位置级阻抗（position-level impedance）**：通过位置指令实现柔顺的阻抗控制。
    - **力矩控制内环（torque control inner loop）**：快速控制关节力矩的内部回路。
    - **位置控制外环（position control outer loop）**：生成位置指令的外部回路。

在人形机器人中，阻抗控制可用于：

- **落地缓冲**：脚触地时表现为低刚度-高阻尼，吸收冲击。
- **人机交互**：手臂低刚度保证接触安全。
- **工具使用**：根据任务调整末端阻抗，如拧螺丝时高刚度，开门时中等刚度。

!!! note "术语解释：落地缓冲、人机交互安全、工具使用、刚度调节"
    - **落地缓冲（landing buffering）**：通过柔顺性减小触地冲击。
    - **人机交互安全（HRI safety）**：在人机接触中降低伤害风险。
    - **工具使用（tool use）**：机器人使用工具完成任务。
    - **刚度调节（stiffness regulation）**：根据任务调整系统刚度。

```mermaid
flowchart TD
    A["期望轨迹 x_d, v_d, a_d"] --> B["实际状态 x, v, a"]
    B --> C["阻抗方程"]
    C --> D["F = Md e_ddot + Dd e_dot + Kd e"]
    D --> E["任务力 F"]
    E --> F["tau = J^T F"]
    F --> G["关节力矩控制"]
```

#### 导纳控制

**导纳控制（admittance control）**是阻抗控制的"对偶"：它根据测得的接触力计算期望运动轨迹，再由位置/速度控制器跟踪。其基本方程为：

$$
\mathbf{M}_d (\ddot{\mathbf{x}}_d - \ddot{\mathbf{x}}_c) + \mathbf{D}_d (\dot{\mathbf{x}}_d - \dot{\mathbf{x}}_c) + \mathbf{K}_d (\mathbf{x}}_d - \mathbf{x}_c) = \mathbf{F}_{\text{ext}}
$$

其中 \(\mathbf{x}_c\) 为导纳修正后的指令轨迹，\(\mathbf{F}_{\text{ext}}\) 为外部接触力。导纳控制器输出修正轨迹，送入内环位置控制器。

!!! note "术语解释：导纳控制、导纳修正轨迹、外部接触力、位置控制内环"
    - **导纳控制（admittance control）**：根据外力生成期望运动的控制策略。
    - **导纳修正轨迹（admittance-corrected trajectory）**：经导纳控制器调整后的轨迹。
    - **外部接触力（external contact force）**：环境作用于机器人的力。
    - **位置控制内环（position control inner loop）**：跟踪导纳输出轨迹的内部位置回路。

导纳控制的优势在于：

- 可直接利用现有高精度位置控制硬件。
- 对外部力传感器噪声有一定滤波作用。
- 适合刚度较高的工业机器人与环境交互。

劣势在于：

- 受位置控制带宽限制，难以实现快速力响应。
- 若环境刚度极高，导纳控制器可能不稳定。

!!! note "术语解释：力传感器噪声、控制带宽、环境刚度、稳定性"
    - **力传感器噪声（force sensor noise）**：力传感器测量中的随机误差。
    - **控制带宽（control bandwidth）**：控制器能有效响应的频率范围。
    - **环境刚度（environment stiffness）**：接触环境的等效刚度。
    - **稳定性（stability）**：系统在扰动下保持有界响应的能力。

```mermaid
flowchart TD
    A["外部力 F_ext"] --> B["导纳控制器"]
    C["期望轨迹 x_d"] --> B
    B --> D["修正轨迹 x_c"]
    D --> E["位置控制内环"]
    E --> F["执行器"]
    F --> G["机器人运动"]
```

#### 内/外环架构

实际人形机器人通常采用**级联控制架构（cascaded control architecture）**：

- **最内环**：电流/力矩环（1 kHz 以上），由电机驱动器实现。
- **中间环**：速度/位置环或阻抗环（0.5-1 kHz）。
- **最外环**：任务规划/WBC/QP（50-200 Hz），生成期望轨迹与接触力分配。

!!! note "术语解释：级联控制架构、电流环、速度环、位置环、任务规划"
    - **级联控制架构（cascaded control architecture）**：多环嵌套的控制结构。
    - **电流环（current loop）**：控制电机电流的环，间接控制力矩。
    - **速度环（velocity loop）**：控制关节速度的环。
    - **位置环（position loop）**：控制关节位置的环。
    - **任务规划（task planning）**：生成高层任务指令的过程。

力控制与柔顺控制常位于中间环或外环：

- **力矩级阻抗**：阻抗方程直接生成力矩指令，送入电流环。
- **导纳控制**：导纳方程生成位置/速度指令，送入位置/速度环。
- **混合力/位置**：选择矩阵决定哪些方向走位置环、哪些方向走力环。

!!! note "术语解释：力矩指令、位置指令、选择方向、电流环"
    - **力矩指令（torque command）**：期望的关节输出力矩。
    - **位置指令（position command）**：期望的关节位置。
    - **选择方向（selection direction）**：混合控制中选择位置或力控制的方向。

```mermaid
flowchart TD
    A["任务规划/WBC"] --> B["导纳/阻抗控制器"]
    B --> C["位置/力矩指令"]
    C --> D["位置/力矩控制环"]
    D --> E["电流环"]
    E --> F["电机"]
    F --> G["机器人"]
    G --> H["力/位置传感器"]
    H --> D
    H --> B
```

#### 变刚度与柔性执行器

为进一步提升安全性与能效，研究者们发展了**变刚度执行器（Variable Stiffness Actuator, VSA）**与**变阻抗执行器（Variable Impedance Actuator, VIA）**。它们可在线调节输出刚度，使机器人能够在高精度阶段高刚度、在接触阶段低刚度。

!!! note "术语解释：变刚度执行器（VSA）、变阻抗执行器（VIA）、在线调节、能效"
    - **变刚度执行器（VSA）**：可主动改变输出刚度的执行器。
    - **变阻抗执行器（VIA）**：可主动改变输出阻抗的执行器。
    - **在线调节（online regulation）**：运行过程中实时调整参数。
    - **能效（energy efficiency）**：完成任务所需能量与输入能量之比。

变刚度控制律可写为：

$$
\tau = k(t) \, (\theta - \theta_0) + d(t) \, \dot{\theta}
$$

其中 \(k(t)\) 与 \(d(t)\) 为时变刚度与阻尼。通过优化 \(k(t)\)、\(d(t)\)，可以在保证任务性能的同时最小化能量消耗与接触风险。

!!! note "术语解释：时变刚度、时变阻尼、能量消耗、接触风险"
    - **时变刚度（time-varying stiffness）**：随时间变化的刚度。
    - **时变阻尼（time-varying damping）**：随时间变化的阻尼。
    - **能量消耗（energy consumption）**：系统运行消耗的能量。
    - **接触风险（contact risk）**：人机接触时造成伤害的可能性。
'''

SECTION_NEW_REFS = r'''
84. Khatib O. A unified approach for motion and force control of robot manipulators: The operational space formulation. *IEEE Journal on Robotics and Automation*, 1987, 3(1): 43–53.
85. de Lasa M, Mordatch I, Hertzmann A. Feature-based locomotion controllers. *ACM Transactions on Graphics*, 2010, 29(4): 1–10.
86. Righetti L, Buchli J, Mistry M, Kalakrishnan M, Schaal S. Optimal distribution of contact forces with inverse-dynamics control. *The International Journal of Robotics Research*, 2013, 32(3): 280–298.
87. Stephens B J, Atkeson C G. Dynamic balance force control for compliant humanoid robots. *IEEE/RSJ IROS*, 2010: 1248–1255.
88. Wieber P B. On the stability of walking systems. *Proceedings of the International Workshop on Humanoid and Human Friendly Robotics*, 2002.
89. Wieber P B, Trajectory free linear model predictive control for stable walking in the presence of strong perturbations. *IEEE-RAS International Conference on Humanoid Robots*, 2006: 137–142.
90. Bicchi A, Kumar V. Robotic grasping and contact: A review. *IEEE International Conference on Robotics and Automation*, 2000: 348–353.
91. Murray R M, Li Z, Sastry S S. *A Mathematical Introduction to Robotic Manipulation*. CRC Press, 1994.
92. Featherstone R. *Rigid Body Dynamics Algorithms*. Springer, 2008.
93. Kajita S, Hirukawa H, Harada K, Yokoi K. *Introduction to Humanoid Robotics*. Springer Tracts in Advanced Robotics, 2014.
94. Siciliano B, Khatib O. *Springer Handbook of Robotics* (2nd ed.). Springer, 2016.
95. Craig J J. *Introduction to Robotics: Mechanics and Control* (3rd ed.). Pearson, 2004.
96. Spong M W, Hutchinson S, Vidyasagar M. *Robot Modeling and Control*. Wiley, 2005.
'''

print("Force control and references loaded.")
