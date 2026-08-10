---
$id: ent_report_humanoid_beyond_dexterity_why_contact_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: 'Beyond Dexterity: Why Contact May Define the Next Era of Robotics'
  zh: 'Beyond Dexterity: Why Contact May Define the Next Era of Robotics'
  ko: 'Beyond Dexterity: Why Contact May Define the Next Era of Robotics'
summary:
  en: 'This article is brought to you by AGILINK . Throughout the exhibition hall at the 2026 IEEE International Conference
    on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention. Two robotic
    hands were making a balloon dog. Slowly and deliberately, the robot twisted a long balloon into loops, bends, and joints
    without popping it. Visitors stopped, watched, and often returned with colleagues to watch again. AGILINK’s balloon dog
    demonstration draws a crowd at ICRA 2026. AGILINK At first glance, the demonstration appeared almost playful. Among roboticists,
    however, balloon twisting is widely recognized as an unusually difficult manipulation task. A balloon is lightweight,
    highly deformable, slippery, and extremely sensitive to force. Every twist changes its geometry and internal pressure,
    turning a seemingly simple activity into a continuously changing physical interaction problem. Humans navigate those changes
    almost intuitively. While making a balloon animal, people rarely think consciously about force regulation, slip prevention,
    or contact stability. They simply adjust. For robots, those adjustments remain remarkably difficult. The challenge is
    not merely moving fingers to the right positions. The harder part is maintaining stable interaction while the object itself
    is changing. Highlights from AGILINK’s ICRA 2026 demonstrations, including visuotactile sensing, in-hand manipulation,
    balloon-animal shaping, and other contact-rich tasks enabled by the company’s latest OmniHand platform. AGILINK That distinction
    helps explain why the balloon dog drew so much attention in Vienna. What appeared to be a dexterity demonstration was,
    in many ways, a demonstration about contact itself. As robotic manipulation continues to advance, a growing number of
    researchers are arriving at a similar conclusion: many of the hardest problems in robotics begin only after contact occurs.
    Motion and Contact Intelligence for Robot Manipulation Balloon twisting combines two challenges that robotics has traditionally
    struggled to solve simultaneously: long-horizon task execution and contact-rich manipulation. The first concerns motion.
    A balloon dog is not created through a single grasp or twist. It emerges through a carefully ordered sequence of manipulations,
    each setting the conditions for what follows. A small rotational error introduced early may appear insignificant at first,
    yet several steps later it can prevent the final structure from forming altogether. In that sense, balloon twisting is
    a long-horizon task. Success depends not only on performing individual actions correctly, but also on preserving the future
    feasibility of the entire manipulation process. To address this challenge, AGILINK began by collecting demonstrations
    from professional balloon artists. Human actions were mapped onto robotic hands to establish an initial manipulation policy.
    But successful demonstrations alone were insufficient. In practice, some of the most valuable learning occurred when execution
    began to drift toward failure. Whenever instability emerged, human operators intervened and corrected the manipulation
    in real time. Those interventions were recorded and incorporated into reinforcement-learning cycles, allowing the system
    to learn not only how successful demonstrations unfold, but also how experienced operators recover when things start to
    go wrong. Through this process, the robot gradually acquired the capabilities required for long-horizon task execution—a
    collection of abilities that AGILINK groups under the term motion intelligence : the ability to generate actions, coordinate
    bimanual behaviors, and execute extended manipulation sequences under real-world uncertainty. OmniHand 3 Ultra-M on display
    at ICRA 2026. AGILINK Yet motion alone does not explain why balloon twisting remains difficult. The second challenge is
    contact. The robot must continuously regulate force, adjust contact locations, and respond to subtle changes in the object’s
    state. These decisions are difficult to encode through explicit rules. Even skilled human operators often rely on tactile
    intuition developed through experience rather than consciously articulated strategies. Analysis of those interventions
    revealed that many failures did not originate from incorrect action sequences, but from the breakdown of contact itself.
    To better capture those interaction dynamics, AGILINK collected contact-centric intervention data and incorporated those
    interactions into reinforcement-learning training. Rather than learning only which motions to perform, the system also
    learned how humans maintain stability when contact conditions begin to deteriorate. AGILINK describes this capability
    as contact intelligence : the ability to establish, maintain, and adapt physical interaction as force distribution, friction,
    deformation, and contact geometry continuously evolve. The distinction between the two capabilities is subtle but important.
    Motion intelligence determines what the robot intends to do. Contact intelligence determines whether it can continue doing
    it. For balloon twisting, both are necessary. One provides the sequence of actions. The other keeps those actions physically
    viable. YouTuber KhanFlicks follows OmniHand’s motions while learning to fold a balloon dog at the AGILINK booth. AGILINK
    Between a balloon slipping away and a balloon bursting lies a narrow region of stability. Successful manipulation depends
    on finding that region—and remaining within it throughout the task. Introducing the OmniHand 3 Ultra-M Dexterous Hand
    The balloon dog demonstration showcased a manipulation capability. It also revealed a broader question. How much contact
    intelligence can be achieved through learning alone? A robot can only regulate what it can perceive. It can only respond
    as quickly as its hardware allows. As manipulation tasks become increasingly complex, researchers are finding that progress
    depends not only on better policies, but also on richer sensing and faster physical response. That realization formed
    the backdrop for AGILINK’s second major announcement at ICRA 2026. Alongside the balloon dog demonstration, the company
    introduced the OmniHand 3 Ultra-M . OmniHand 3 Ultra-M closely matches the size of an adult human hand. AGILINK The two
    exhibits represented different stages of the same technological trajectory. If the balloon dog demonstrated what contact
    intelligence can already accomplish today, Ultra-M was designed to explore what contact intelligence may require next.
    Building Hardware for Contact Intelligence Roughly the size of an adult human hand, the OmniHand 3 Ultra-M integrates
    20 active degrees of freedom within a human-scale form factor. Its most distinctive feature is a fully direct-drive architecture.
    By adopting direct-drive actuation throughout the system, the hand is designed to enable faster and more transparent force
    regulation and higher force-control bandwidth, enabling faster response as contact conditions change. For contact-rich
    manipulation, responsiveness can be as important as sensing itself. By adopting direct-drive actuation throughout the
    system, the OmniHand 3 Ultra-M is designed to enable faster and more transparent force regulation and higher force-control
    bandwidth, enabling faster response as contact conditions change. The platform also incorporates tactile sensing across
    nearly the entire hand. Each fingertip contains a miniature vision-based tactile sensor, while more than 300 three-dimensional
    tactile sensing points are distributed throughout the palm. Together, they provide information not only about where contact
    occurs, but how contact is evolving. The system is designed to estimate pressure distribution, shear forces, local deformation,
    slip tendencies, and other interaction dynamics that often remain invisible to conventional position-based control systems.
    According to AGILINK’s tests, individual sensors achieve force resolution of approximately 0.005 N—roughly equivalent
    to detecting the weight of a sheet of paper resting on a fingertip. Spatial resolution reaches approximately 0.04 mm,
    while sensing density approaches 50,000 sensing points per square centimeter. OmniHand 3 Ultra-M recognizes feather texture
    through vision-based tactile sensing. AGILINK For dexterous robots, contact has traditionally been a largely hidden process.
    Ultra-M is designed to make that process more observable. Rather than simply detecting that contact has occurred, the
    system attempts to resolve where interaction is happening, how forces are distributed, whether instability is beginning
    to emerge, and how manipulation strategies should adapt in response. The balloon dog offered a glimpse of what contact
    intelligence can already accomplish. Ultra-M explores a different question: what capabilities may be required to push
    contact intelligence further? The Physical World Remains the Hardest Benchmark The significance of contact intelligence
    extends far beyond balloon animals. Many tasks that continue to resist automation involve unstable or deformable interaction:
    cable insertion, garment handling, flexible packaging, delicate assembly, connector mating, tool use, and household manipulation.
    These tasks are difficult not because robots cannot reach the correct location, but because maintaining stable interaction
    after contact begins remains extraordinarily hard. For decades, robotics achieved many of its successes by reducing uncertainty.
    Factories were engineered to make robotic motion predictable, repeatable, and highly structured. The physical world behaves
    differently. A growing share of robotics research is shifting toward interaction itself—understanding how robots can establish,
    maintain, and adapt physical contact within environments that remain fundamentally unpredictable. Objects shift. Materials
    deform. Friction changes. Contact evolves. Real environments rarely follow scripts. Seen through that lens, the balloon
    dog was never really about the balloon dog. What attracted attention at ICRA was not simply a visually impressive demonstration,
    but what it revealed: intelligence in the physical world is ultimately measured through interaction. As motion generation
    continues to mature, a growing share of robotics research is shifting toward interaction itself—understanding how robots
    can establish, maintain, and adapt physical contact within environments that remain fundamentally unpredictable. For robots
    moving beyond structured environments and into less predictable real-world settings, managing contact may become as important
    as motion itself.'
  zh: AGILINK 在 2026 年 ICRA 上展示了机器人用双手拧气球狗，这一看似简单的演示实则揭示了机器人操作领域最核心的挑战：接触智能。该公司提出了“运动智能”与“接触智能”的区分，并发布了集成全直驱架构与高密度触觉传感的 OmniHand
    3 Ultra-M 灵巧手，旨在推动机器人从精确运动向稳定交互演进。
  ko: 'This article is brought to you by AGILINK . Throughout the exhibition hall at the 2026 IEEE International Conference
    on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention. Two robotic
    hands were making a balloon dog. Slowly and deliberately, the robot twisted a long balloon into loops, bends, and joints
    without popping it. Visitors stopped, watched, and often returned with colleagues to watch again. AGILINK’s balloon dog
    demonstration draws a crowd at ICRA 2026. AGILINK At first glance, the demonstration appeared almost playful. Among roboticists,
    however, balloon twisting is widely recognized as an unusually difficult manipulation task. A balloon is lightweight,
    highly deformable, slippery, and extremely sensitive to force. Every twist changes its geometry and internal pressure,
    turning a seemingly simple activity into a continuously changing physical interaction problem. Humans navigate those changes
    almost intuitively. While making a balloon animal, people rarely think consciously about force regulation, slip prevention,
    or contact stability. They simply adjust. For robots, those adjustments remain remarkably difficult. The challenge is
    not merely moving fingers to the right positions. The harder part is maintaining stable interaction while the object itself
    is changing. Highlights from AGILINK’s ICRA 2026 demonstrations, including visuotactile sensing, in-hand manipulation,
    balloon-animal shaping, and other contact-rich tasks enabled by the company’s latest OmniHand platform. AGILINK That distinction
    helps explain why the balloon dog drew so much attention in Vienna. What appeared to be a dexterity demonstration was,
    in many ways, a demonstration about contact itself. As robotic manipulation continues to advance, a growing number of
    researchers are arriving at a similar conclusion: many of the hardest problems in robotics begin only after contact occurs.
    Motion and Contact Intelligence for Robot Manipulation Balloon twisting combines two challenges that robotics has traditionally
    struggled to solve simultaneously: long-horizon task execution and contact-rich manipulation. The first concerns motion.
    A balloon dog is not created through a single grasp or twist. It emerges through a carefully ordered sequence of manipulations,
    each setting the conditions for what follows. A small rotational error introduced early may appear insignificant at first,
    yet several steps later it can prevent the final structure from forming altogether. In that sense, balloon twisting is
    a long-horizon task. Success depends not only on performing individual actions correctly, but also on preserving the future
    feasibility of the entire manipulation process. To address this challenge, AGILINK began by collecting demonstrations
    from professional balloon artists. Human actions were mapped onto robotic hands to establish an initial manipulation policy.
    But successful demonstrations alone were insufficient. In practice, some of the most valuable learning occurred when execution
    began to drift toward failure. Whenever instability emerged, human operators intervened and corrected the manipulation
    in real time. Those interventions were recorded and incorporated into reinforcement-learning cycles, allowing the system
    to learn not only how successful demonstrations unfold, but also how experienced operators recover when things start to
    go wrong. Through this process, the robot gradually acquired the capabilities required for long-horizon task execution—a
    collection of abilities that AGILINK groups under the term motion intelligence : the ability to generate actions, coordinate
    bimanual behaviors, and execute extended manipulation sequences under real-world uncertainty. OmniHand 3 Ultra-M on display
    at ICRA 2026. AGILINK Yet motion alone does not explain why balloon twisting remains difficult. The second challenge is
    contact. The robot must continuously regulate force, adjust contact locations, and respond to subtle changes in the object’s
    state. These decisions are difficult to encode through explicit rules. Even skilled human operators often rely on tactile
    intuition developed through experience rather than consciously articulated strategies. Analysis of those interventions
    revealed that many failures did not originate from incorrect action sequences, but from the breakdown of contact itself.
    To better capture those interaction dynamics, AGILINK collected contact-centric intervention data and incorporated those
    interactions into reinforcement-learning training. Rather than learning only which motions to perform, the system also
    learned how humans maintain stability when contact conditions begin to deteriorate. AGILINK describes this capability
    as contact intelligence : the ability to establish, maintain, and adapt physical interaction as force distribution, friction,
    deformation, and contact geometry continuously evolve. The distinction between the two capabilities is subtle but important.
    Motion intelligence determines what the robot intends to do. Contact intelligence determines whether it can continue doing
    it. For balloon twisting, both are necessary. One provides the sequence of actions. The other keeps those actions physically
    viable. YouTuber KhanFlicks follows OmniHand’s motions while learning to fold a balloon dog at the AGILINK booth. AGILINK
    Between a balloon slipping away and a balloon bursting lies a narrow region of stability. Successful manipulation depends
    on finding that region—and remaining within it throughout the task. Introducing the OmniHand 3 Ultra-M Dexterous Hand
    The balloon dog demonstration showcased a manipulation capability. It also revealed a broader question. How much contact
    intelligence can be achieved through learning alone? A robot can only regulate what it can perceive. It can only respond
    as quickly as its hardware allows. As manipulation tasks become increasingly complex, researchers are finding that progress
    depends not only on better policies, but also on richer sensing and faster physical response. That realization formed
    the backdrop for AGILINK’s second major announcement at ICRA 2026. Alongside the balloon dog demonstration, the company
    introduced the OmniHand 3 Ultra-M . OmniHand 3 Ultra-M closely matches the size of an adult human hand. AGILINK The two
    exhibits represented different stages of the same technological trajectory. If the balloon dog demonstrated what contact
    intelligence can already accomplish today, Ultra-M was designed to explore what contact intelligence may require next.
    Building Hardware for Contact Intelligence Roughly the size of an adult human hand, the OmniHand 3 Ultra-M integrates
    20 active degrees of freedom within a human-scale form factor. Its most distinctive feature is a fully direct-drive architecture.
    By adopting direct-drive actuation throughout the system, the hand is designed to enable faster and more transparent force
    regulation and higher force-control bandwidth, enabling faster response as contact conditions change. For contact-rich
    manipulation, responsiveness can be as important as sensing itself. By adopting direct-drive actuation throughout the
    system, the OmniHand 3 Ultra-M is designed to enable faster and more transparent force regulation and higher force-control
    bandwidth, enabling faster response as contact conditions change. The platform also incorporates tactile sensing across
    nearly the entire hand. Each fingertip contains a miniature vision-based tactile sensor, while more than 300 three-dimensional
    tactile sensing points are distributed throughout the palm. Together, they provide information not only about where contact
    occurs, but how contact is evolving. The system is designed to estimate pressure distribution, shear forces, local deformation,
    slip tendencies, and other interaction dynamics that often remain invisible to conventional position-based control systems.
    According to AGILINK’s tests, individual sensors achieve force resolution of approximately 0.005 N—roughly equivalent
    to detecting the weight of a sheet of paper resting on a fingertip. Spatial resolution reaches approximately 0.04 mm,
    while sensing density approaches 50,000 sensing points per square centimeter. OmniHand 3 Ultra-M recognizes feather texture
    through vision-based tactile sensing. AGILINK For dexterous robots, contact has traditionally been a largely hidden process.
    Ultra-M is designed to make that process more observable. Rather than simply detecting that contact has occurred, the
    system attempts to resolve where interaction is happening, how forces are distributed, whether instability is beginning
    to emerge, and how manipulation strategies should adapt in response. The balloon dog offered a glimpse of what contact
    intelligence can already accomplish. Ultra-M explores a different question: what capabilities may be required to push
    contact intelligence further? The Physical World Remains the Hardest Benchmark The significance of contact intelligence
    extends far beyond balloon animals. Many tasks that continue to resist automation involve unstable or deformable interaction:
    cable insertion, garment handling, flexible packaging, delicate assembly, connector mating, tool use, and household manipulation.
    These tasks are difficult not because robots cannot reach the correct location, but because maintaining stable interaction
    after contact begins remains extraordinarily hard. For decades, robotics achieved many of its successes by reducing uncertainty.
    Factories were engineered to make robotic motion predictable, repeatable, and highly structured. The physical world behaves
    differently. A growing share of robotics research is shifting toward interaction itself—understanding how robots can establish,
    maintain, and adapt physical contact within environments that remain fundamentally unpredictable. Objects shift. Materials
    deform. Friction changes. Contact evolves. Real environments rarely follow scripts. Seen through that lens, the balloon
    dog was never really about the balloon dog. What attracted attention at ICRA was not simply a visually impressive demonstration,
    but what it revealed: intelligence in the physical world is ultimately measured through interaction. As motion generation
    continues to mature, a growing share of robotics research is shifting toward interaction itself—understanding how robots
    can establish, maintain, and adapt physical contact within environments that remain fundamentally unpredictable. For robots
    moving beyond structured environments and into less predictable real-world settings, managing contact may become as important
    as motion itself.'
domains:
- 11_applications_markets
- 07_ai_models_algorithms
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- ieee
- manipulation
- report
- robotics
- sensor
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/agilink-contact-intelligence-robot-manipulation.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1637 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'Beyond Dexterity: Why Contact May Define the Next Era of Robotics'
  url: https://spectrum.ieee.org/agilink-contact-intelligence-robot-manipulation
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
在 2026 年维也纳 ICRA 展会上，AGILINK 的机器人用双手拧气球狗的演示吸引了大量关注。气球因其轻质、易变形、表面光滑且对力极其敏感的特性，被视为一项异常困难的操控任务，其难点不在于手指的定位，而在于物体状态持续变化时维持稳定的接触。AGILINK 通过收集专业气球艺人的演示并结合人工干预的强化学习，让机器人掌握了执行长时域任务所需的“运动智能”。然而，分析发现许多失败源于接触本身的崩溃，而非动作序列错误，这促使公司进一步提炼出“接触智能”的概念。为突破这一瓶颈，AGILINK 推出了 OmniHand 3 Ultra-M，该手采用全直驱设计以实现更快的力控带宽，并在指尖和手掌集成了超过 300 个三维触觉传感点，力分辨率可达 0.005 N，旨在让接触过程变得可观测、可调节。

## 核心内容
### 从气球狗看机器人操作的两大挑战

AGILINK 在 2026 年 ICRA 上的气球狗演示，揭示了机器人操作中两个长期难以同时解决的问题：**长时域任务执行**与**接触丰富型操作**。

*   **运动智能 (Motion Intelligence)**：气球狗的制作需要一系列精心排序的操作，早期微小的旋转误差会在后续步骤中被放大，导致最终结构无法成型。AGILINK 的解决方案是：先收集专业气球艺人的演示数据，将人类动作映射到机器人手上建立初始策略。更关键的是，当执行过程出现不稳定时，人类操作员会实时介入并纠正，这些干预数据被记录并纳入强化学习循环。系统不仅学习成功演示，更学习专家如何从失败中恢复，从而逐步获得在真实不确定性下生成动作、协调双臂行为并执行长序列操作的能力。
*   **接触智能 (Contact Intelligence)**：即便动作序列正确，气球仍可能因力控不当而滑脱或爆裂。AGILINK 发现许多失败源于接触本身的崩溃。为此，他们收集了以接触为中心的干预数据，让系统学习人类如何在接触条件恶化时维持稳定。这种能力被定义为：在力分布、摩擦、形变和接触几何形状持续变化时，建立、维持并适应物理交互的能力。简而言之，运动智能决定机器人“想做什么”，而接触智能决定它“能否继续做下去”。

### OmniHand 3 Ultra-M：为接触智能打造的硬件平台

为突破学习算法的感知与响应速度瓶颈，AGILINK 发布了 OmniHand 3 Ultra-M 灵巧手，其设计目标直指提升接触智能的物理基础。

*   **全直驱架构**：该手在成人手掌大小的尺寸内集成了 20 个主动自由度，并采用全直驱驱动。这一设计旨在实现更快、更透明的力调节和更高的力控带宽，使机器人能在接触条件变化时做出更迅速的响应。
*   **高密度触觉传感**：每个指尖内置微型视觉触觉传感器，手掌上分布超过 300 个三维触觉传感点。系统不仅能检测接触发生的位置，还能估算压力分布、剪切力、局部形变和滑移趋势。据 AGILINK 测试，单个传感器的力分辨率约为 **0.005 N**（相当于感知一张纸的重量），空间分辨率约 **0.04 mm**，传感密度接近 **50,000 点/平方厘米**。
*   **从检测到适应**：Ultra-M 的设计目标不是简单检测接触是否发生，而是解析交互发生在哪里、力如何分布、不稳定性是否开始出现，以及操作策略应如何相应调整。

### 物理世界：最难的基准

接触智能的意义远超气球动物。许多难以自动化的任务——如线缆插入、衣物处理、柔性包装、精密装配、连接器插拔、工具使用和家务操作——其难点不在于机器人无法到达正确位置，而在于接触开始后维持稳定交互极其困难。随着运动生成技术日趋成熟，机器人研究正越来越多地转向交互本身：理解机器人如何在根本上不可预测的环境中建立、维持并适应物理接触。对于走出结构化环境、迈向真实世界的机器人而言，管理接触可能变得与管理运动同等重要。

## Overview
From balloon twisting to OmniHand 3 Ultra-M, AGILINK is shaping the future of contact intelligence Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention.

This article is brought to you by AGILINK . Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention. Two robotic hands were making a balloon dog. Slowly and deliberately, the robot twisted a long balloon into loops, bends, and joints without popping it. Visitors stopped, watched, and often returned with colleagues to watch again. AGILINK’s balloon dog demonstration draws a crowd at ICRA 2026. AGILINK At first glance, the demonstration appeared almost playful. Among roboticists, however, balloon twisting is widely recognized as an unusually difficult manipulation task. A balloon is lightweight, highly deformable, slippery, and extremely sensitive to force. Every twist changes its geometry and internal pressure, turning a seemingly simple activity into a continuously changing physical interaction problem. Humans navigate those changes almost intuitively. While making a balloon animal, people rarely think consciously about force regulation, slip prevention, or contact stability. They simply adjust. For robots, those adjustments remain remarkably difficult. The challenge is not merely moving fingers to the right positions. The harder part is maintaining stable interaction while the object itself is changing. Highlights from AGILINK’s ICRA 2026 demonstrations, including visuotactile sensing, in-hand manipulation, balloon-animal shaping, and other contact-rich tasks enabled by the company’s latest OmniHand platform. AGILINK That distinction helps explain why the balloon dog drew so much attention in Vienna. What appeared to be a dexterity demonstration was, in many ways, a demonstration about contact itself. As robotic manipulation continues to advance, a growing number of researchers are arriving at a similar conclusion: many of the hardest problems in robotics begin only after contact occurs. Motion and Contact Intelligence for Robot Manipulation Balloon twisting combines two challenges that robotics has traditionally struggled to solve simultaneously: long-horizon task execution and contact-rich manipulation. The first concerns motion. A balloon dog is not created through a single grasp or twist. It emerges through a carefully ordered sequence of manipulations, each setting the conditions for what follows. A small rotational error introduced early may appear insignificant at first, yet several steps later it can prevent the final structure from forming altogether. In that sense, balloon twisting is a long-horizon task. Success depends not only on performing individual actions correctly, but also on preserving the future feasibility of the entire manipulation process. To address this challenge, AGILINK began by collecting demonstrations from professional balloon artists. Human actions were mapped onto robotic hands to establish an initial manipulation policy. But successful demonstrations alone were insufficient. In practice, some of the most valuable learning occurred when execution began to drift toward failure. Whenever instability emerged, human operators intervened and corrected the manipulation in real time. Those interventions were recorded and incorporated into reinforcement-learning cycles, allowing the system to learn not only how successful demonstrations unfold, but also how experienced operators recover when things start to go wrong. Through this process, the robot gradually acquired the capabilities required for long-horizon task execution—a collection of abilities that AGILINK groups under the term motion intelligence : the ability to generate actions, coordinate bimanual behaviors, and execute extended manipulation sequences under real-world uncertainty. OmniHand 3 Ultra-M on display at ICRA 2026. AGILINK Yet motion alone does not explain why balloon twisting remains difficult. The second challenge is contact. The robot must continuously regulate force, adjust contact locations, and respond to subtle changes in the object’s state. These decisions are difficult to encode through explicit rules. Even skilled human operators often rely on tactile intuition developed through experience rather than consciously articulated strategies. Analysis of those interventions revealed that many failures did not originate from incorrect action sequences, but from the breakdown of contact itself. To better capture those interaction dynamics, AGILINK collected contact-centric intervention data and incorporated those interactions into reinforcement-learning training. Rather than learning only which motions to perform, the system also learned how humans maintain stability when contact conditions begin to deteriorate. AGILINK describes this capability as contact intelligence : the ability to establish, maintain, and adapt physical interaction as force distribution, friction, deformation, and contact geometry continuously evolve. The distinction between the two capabilities is subtle but important. Motion intelligence determines what the robot intends to do. Contact intelligence determines whether it can continue doing it. For balloon twisting, both are necessary. One provides the sequence of actions. The other keeps those actions physically viable. YouTuber KhanFlicks follows OmniHand’s motions while learning to fold a balloon dog at the AGILINK booth. AGILINK Between a balloon slipping away and a balloon bursting lies a narrow region of stability. Successful manipulation depends on finding that region—and remaining within it throughout the task. Introducing the OmniHand 3 Ultra-M Dexterous Hand The balloon dog demonstration showcased a manipulation capability. It also revealed a broader question. How much contact intelligence can be achieved through learning alone? A robot can only regulate what it can perceive. It can only respond as quickly as its hardware allows. As manipulation tasks become increasingly complex, researchers are finding that progress depends not only on better policies, but also on richer sensing and faster physical response. That realization formed the backdrop for AGILINK’s second major announcement at ICRA 2026. Alongside the balloon dog demonstration, the company introduced the OmniHand 3 Ultra-M . OmniHand 3 Ultra-M closely matches the size of an adult human hand. AGILINK The two exhibits represented different stages of the same technological trajectory. If the balloon dog demonstrated what contact intelligence can already accomplish today, Ultra-M was designed to explore what contact intelligence may require next. Building Hardware for Contact Intelligence Roughly the size of an adult human hand, the OmniHand 3 Ultra-M integrates 20 active degrees of freedom within a human-scale form factor. Its most distinctive feature is a fully direct-drive architecture. By adopting direct-drive actuation throughout the system, the hand is designed to enable faster and more transparent force regulation and higher force-control bandwidth, enabling faster response as contact conditions change. For contact-rich manipulation, responsiveness can be as important as sensing itself. By adopting direct-drive actuation throughout the system, the OmniHand 3 Ultra-M is designed to enable faster and more transparent force regulation and higher force-control bandwidth, enabling faster response as contact conditions change. The platform also incorporates tactile sensing across nearly the entire hand. Each fingertip contains a miniature vision-based tactile sensor, while more than 300 three-dimensional tactile sensing points are distributed throughout the palm. Together, they provide information not only about where contact occurs, but how contact is evolving. The system is designed to estimate pressure distribution, shear forces, local deformation, slip tendencies, and other interaction dynamics that often remain invisible to conventional position-based control systems. According to AGILINK’s tests, individual sensors achieve force resolution of approximately 0.005 N—roughly equivalent to detecting the weight of a sheet of paper resting on a fingertip. Spatial resolution reaches approximately 0.04 mm, while sensing density approaches 50,000 sensing points per square centimeter. OmniHand 3 Ultra-M recognizes feather texture through vision-based tactile sensing. AGILINK For dexterous robots, contact has traditionally been a largely hidden process. Ultra-M is designed to make that process more observable. Rather than simply detecting that contact has occurred, the system attempts to resolve where interaction is happening, how forces are distributed, whether instability is beginning to emerge, and how manipulation strategies should adapt in response. The balloon dog offered a glimpse of what contact intelligence can already accomplish. Ultra-M explores a different question: what capabilities may be required to push contact intelligence further? The Physical World Remains the Hardest Benchmark The significance of contact intelligence extends far beyond balloon animals. Many tasks that continue to resist automation involve unstable or deformable interaction: cable insertion, garment handling, flexible packaging, delicate assembly, connector mating, tool use, and household manipulation. These tasks are difficult not because robots cannot reach the correct location, but because maintaining stable interaction after contact begins remains extraordinarily hard. For decades, robotics achieved many of its successes by reducing uncertainty. Factories were engineered to make robotic motion predictable, repeatable, and highly structured. The physical world behaves differently. A growing share of robotics research is shifting toward interaction itself—understanding how robots can establish, maintain, and adapt physical contact within environments that remain fundamentally unpredictable. Objects shift. Materials deform. Friction changes. Contact evolves. Real environments rarely follow scripts. Seen through that lens, the balloon dog was never really about the balloon dog. What attracted attention at ICRA was not simply a visually impressive demonstration, but what it revealed: intelligence in the physical world is ultimately measured through interaction. As motion generation continues to mature, a growing share of robotics research is shifting toward interaction itself—understanding how robots can establish, maintain, and adapt physical contact within environments that remain fundamentally unpredictable. For robots moving beyond structured environments and into less predictable real-world settings, managing contact may become as important as motion itself. From balloon twisting to OmniHand 3 Ultra-M, AGILINK is shaping the future of contact intelligence Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention.

## Overview
From balloon twisting to OmniHand 3 Ultra-M, AGILINK is shaping the future of contact intelligence. Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention.

## Content
This article is brought to you by AGILINK. Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention. Two robotic hands were making a balloon dog. Slowly and deliberately, the robot twisted a long balloon into loops, bends, and joints without popping it. Visitors stopped, watched, and often returned with colleagues to watch again. AGILINK’s balloon dog demonstration draws a crowd at ICRA 2026. AGILINK At first glance, the demonstration appeared almost playful. Among roboticists, however, balloon twisting is widely recognized as an unusually difficult manipulation task. A balloon is lightweight, highly deformable, slippery, and extremely sensitive to force. Every twist changes its geometry and internal pressure, turning a seemingly simple activity into a continuously changing physical interaction problem. Humans navigate those changes almost intuitively. While making a balloon animal, people rarely think consciously about force regulation, slip prevention, or contact stability. They simply adjust. For robots, those adjustments remain remarkably difficult. The challenge is not merely moving fingers to the right positions. The harder part is maintaining stable interaction while the object itself is changing. Highlights from AGILINK’s ICRA 2026 demonstrations, including visuotactile sensing, in-hand manipulation, balloon-animal shaping, and other contact-rich tasks enabled by the company’s latest OmniHand platform. AGILINK That distinction helps explain why the balloon dog drew so much attention in Vienna. What appeared to be a dexterity demonstration was, in many ways, a demonstration about contact itself. As robotic manipulation continues to advance, a growing number of researchers are arriving at a similar conclusion: many of the hardest problems in robotics begin only after contact occurs. Motion and Contact Intelligence for Robot Manipulation Balloon twisting combines two challenges that robotics has traditionally struggled to solve simultaneously: long-horizon task execution and contact-rich manipulation. The first concerns motion. A balloon dog is not created through a single grasp or twist. It emerges through a carefully ordered sequence of manipulations, each setting the conditions for what follows. A small rotational error introduced early may appear insignificant at first, yet several steps later it can prevent the final structure from forming altogether. In that sense, balloon twisting is a long-horizon task. Success depends not only on performing individual actions correctly, but also on preserving the future feasibility of the entire manipulation process. To address this challenge, AGILINK began by collecting demonstrations from professional balloon artists. Human actions were mapped onto robotic hands to establish an initial manipulation policy. But successful demonstrations alone were insufficient. In practice, some of the most valuable learning occurred when execution began to drift toward failure. Whenever instability emerged, human operators intervened and corrected the manipulation in real time. Those interventions were recorded and incorporated into reinforcement-learning cycles, allowing the system to learn not only how successful demonstrations unfold, but also how experienced operators recover when things start to go wrong. Through this process, the robot gradually acquired the capabilities required for long-horizon task execution—a collection of abilities that AGILINK groups under the term motion intelligence: the ability to generate actions, coordinate bimanual behaviors, and execute extended manipulation sequences under real-world uncertainty. OmniHand 3 Ultra-M on display at ICRA 2026. AGILINK Yet motion alone does not explain why balloon twisting remains difficult. The second challenge is contact. The robot must continuously regulate force, adjust contact locations, and respond to subtle changes in the object’s state. These decisions are difficult to encode through explicit rules. Even skilled human operators often rely on tactile intuition developed through experience rather than consciously articulated strategies. Analysis of those interventions revealed that many failures did not originate from incorrect action sequences, but from the breakdown of contact itself. To better capture those interaction dynamics, AGILINK collected contact-centric intervention data and incorporated those interactions into reinforcement-learning training. Rather than learning only which motions to perform, the system also learned how humans maintain stability when contact conditions begin to deteriorate. AGILINK describes this capability as contact intelligence: the ability to establish, maintain, and adapt physical interaction as force distribution, friction, deformation, and contact geometry continuously evolve. The distinction between the two capabilities is subtle but important. Motion intelligence determines what the robot intends to do. Contact intelligence determines whether it can continue doing it. For balloon twisting, both are necessary. One provides the sequence of actions. The other keeps those actions physically viable. YouTuber KhanFlicks follows OmniHand’s motions while learning to fold a balloon dog at the AGILINK booth. AGILINK Between a balloon slipping away and a balloon bursting lies a narrow region of stability. Successful manipulation depends on finding that region—and remaining within it throughout the task. Introducing the OmniHand 3 Ultra-M Dexterous Hand The balloon dog demonstration showcased a manipulation capability. It also revealed a broader question. How much contact intelligence can be achieved through learning alone? A robot can only regulate what it can perceive. It can only respond as quickly as its hardware allows. As manipulation tasks become increasingly complex, researchers are finding that progress depends not only on better policies, but also on richer sensing and faster physical response. That realization formed the backdrop for AGILINK’s second major announcement at ICRA 2026. Alongside the balloon dog demonstration, the company introduced the OmniHand 3 Ultra-M. OmniHand 3 Ultra-M closely matches the size of an adult human hand. AGILINK The two exhibits represented different stages of the same technological trajectory. If the balloon dog demonstrated what contact intelligence can already accomplish today, Ultra-M was designed to explore what contact intelligence may require next. Building Hardware for Contact Intelligence Roughly the size of an adult human hand, the OmniHand 3 Ultra-M integrates 20 active de

## 参考
- https://spectrum.ieee.org/agilink-contact-intelligence-robot-manipulation

## 개요
2026년 비엔나 ICRA 전시회에서 AGILINK의 로봇이 두 손으로 풍선 개를 만드는 시연은 큰 주목을 받았다. 풍선은 가볍고 변형되기 쉬우며 표면이 매끄럽고 힘에 극도로 민감한 특성 때문에 비정상적으로 어려운 조작 작업으로 간주되며, 그 난점은 손가락의 위치 결정이 아니라 물체 상태가 지속적으로 변화할 때 안정적인 접촉을 유지하는 데 있다. AGILINK는 전문 풍선 아티스트의 시연을 수집하고 인간 개입을 결합한 강화 학습을 통해 로봇이 장시간 작업 실행에 필요한 '운동 지능'을 습득하도록 했다. 그러나 분석 결과 많은 실패가 동작 시퀀스 오류가 아닌 접촉 자체의 붕괴에서 비롯된 것으로 밝혀졌으며, 이는 회사가 '접촉 지능'이라는 개념을 더욱 정제하도록 이끌었다. 이 병목을 돌파하기 위해 AGILINK는 OmniHand 3 Ultra-M을 출시했으며, 이 손은 더 빠른 힘 제어 대역폭을 위해 전체 직접 구동 설계를 채택하고 손끝과 손바닥에 300개 이상의 3차원 촉각 센싱 포인트를 통합하여 힘 분해능이 0.005 N에 달하며, 접촉 과정을 관찰 가능하고 조절 가능하게 만드는 것을 목표로 한다.

## 핵심 내용
### 풍선 개에서 본 로봇 조작의 두 가지 주요 도전 과제

AGILINK의 2026년 ICRA 풍선 개 시연은 로봇 조작에서 오랫동안 동시에 해결하기 어려웠던 두 가지 문제, 즉 **장시간 작업 실행**과 **접촉 풍부형 조작**을 드러냈다.

*   **운동 지능 (Motion Intelligence)**: 풍선 개 제작은 일련의 정교하게 순서가 정해진 조작을 필요로 하며, 초기의 작은 회전 오류는 후속 단계에서 증폭되어 최종 구조가 형성되지 못하게 할 수 있다. AGILINK의 해결책은 먼저 전문 풍선 아티스트의 시연 데이터를 수집하고 인간의 동작을 로봇 손에 매핑하여 초기 정책을 구축하는 것이다. 더 중요한 것은 실행 과정에서 불안정이 발생할 때 인간 조작자가 실시간으로 개입하여 교정하며, 이러한 개입 데이터는 기록되어 강화 학습 루프에 포함된다. 시스템은 성공적인 시연뿐만 아니라 전문가가 실패에서 어떻게 회복하는지도 학습하여, 실제 불확실성 하에서 동작을 생성하고 양팔 동작을 조정하며 긴 시퀀스 조작을 실행하는 능력을 점진적으로 획득한다.
*   **접촉 지능 (Contact Intelligence)**: 동작 시퀀스가 정확하더라도 풍선은 힘 제어 부적절로 인해 미끄러지거나 터질 수 있다. AGILINK는 많은 실패가 접촉 자체의 붕괴에서 비롯됨을 발견했다. 이를 위해 접촉 중심의 개입 데이터를 수집하여 시스템이 접촉 조건이 악화될 때 인간이 어떻게 안정성을 유지하는지 학습하도록 했다. 이 능력은 힘 분포, 마찰, 변형 및 접촉 기하학이 지속적으로 변화할 때 물리적 상호작용을 구축, 유지 및 적응시키는 능력으로 정의된다. 간단히 말해, 운동 지능은 로봇이 '무엇을 하려는지'를 결정하고, 접촉 지능은 '계속 할 수 있는지'를 결정한다.

### OmniHand 3 Ultra-M: 접촉 지능을 위한 하드웨어 플랫폼

학습 알고리즘의 인식 및 응답 속도 병목을 돌파하기 위해 AGILINK는 OmniHand 3 Ultra-M 정교한 손을 출시했으며, 그 설계 목표는 접촉 지능의 물리적 기반을 향상시키는 데 직접적으로 있다.

*   **전체 직접 구동 아키텍처**: 이 손은 성인 손바닥 크기 내에 20개의 능동 자유도를 통합하고 전체 직접 구동 방식을 채택한다. 이 설계는 더 빠르고 투명한 힘 조절과 더 높은 힘 제어 대역폭을 구현하여 로봇이 접촉 조건 변화에 더 신속하게 대응할 수 있게 한다.
*   **고밀도 촉각 센싱**: 각 손끝에는 소형 비전 기반 촉각 센서가 내장되어 있고, 손바닥에는 300개 이상의 3차원 촉각 센싱 포인트가 분포한다. 시스템은 접촉이 발생한 위치를 감지할 뿐만 아니라 압력 분포, 전단력, 국부 변형 및 미끄러짐 경향을 추정할 수 있다. AGILINK 테스트에 따르면 단일 센서의 힘 분해능은 약 **0.005 N** (종이 한 장의 무게를 감지하는 수준), 공간 분해능은 약 **0.04 mm**, 센싱 밀도는 **50,000 포인트/제곱센티미터**에 가깝다.
*   **감지에서 적응까지**: Ultra-M의 설계 목표는 접촉 발생 여부를 단순히 감지하는 것이 아니라 상호작용이 어디서 발생하는지, 힘이 어떻게 분포되는지, 불안정성이 나타나기 시작하는지, 그리고 조작 전략이 어떻게 그에 따라 조정되어야 하는지를 해석하는 것이다.

### 물리적 세계: 가장 어려운 기준

접촉 지능의 의미는 풍선 동물을 훨씬 넘어선다. 자동화하기 어려운 많은 작업(예: 케이블 삽입, 의류 처리, 유연 포장, 정밀 조립, 커넥터 삽입, 도구 사용 및 가사 작업)의 난점은 로봇이 올바른 위치에 도달하지 못하는 것이 아니라 접촉이 시작된 후 안정적인 상호작용을 유지하는 것이 극도로 어렵다는 데 있다. 동작 생성 기술이 점점 성숙해짐에 따라 로봇 연구는 점점 더 상호작용 자체로 전환되고 있다: 로봇이 근본적으로 예측 불가능한 환경에서 물리적 접촉을 어떻게 구축, 유지 및 적응시키는지 이해하는 것이다. 구조화된 환경을 벗어나 실제 세계로 나아가는 로봇에게 접촉 관리의 중요성은 운동 관리와 동등해질 수 있다.
