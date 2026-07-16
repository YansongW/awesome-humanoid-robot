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
  zh: 'This article is brought to you by AGILINK . Throughout the exhibition hall at the 2026 IEEE International Conference
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
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/agilink-contact-intelligence-robot-manipulation.
sources:
- id: src_001
  type: website
  title: 'Beyond Dexterity: Why Contact May Define the Next Era of Robotics'
  url: https://spectrum.ieee.org/agilink-contact-intelligence-robot-manipulation
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
From balloon twisting to OmniHand 3 Ultra-M, AGILINK is shaping the future of contact intelligence Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention.

## 核心内容
This article is brought to you by AGILINK . Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention. Two robotic hands were making a balloon dog. Slowly and deliberately, the robot twisted a long balloon into loops, bends, and joints without popping it. Visitors stopped, watched, and often returned with colleagues to watch again. AGILINK’s balloon dog demonstration draws a crowd at ICRA 2026. AGILINK At first glance, the demonstration appeared almost playful. Among roboticists, however, balloon twisting is widely recognized as an unusually difficult manipulation task. A balloon is lightweight, highly deformable, slippery, and extremely sensitive to force. Every twist changes its geometry and internal pressure, turning a seemingly simple activity into a continuously changing physical interaction problem. Humans navigate those changes almost intuitively. While making a balloon animal, people rarely think consciously about force regulation, slip prevention, or contact stability. They simply adjust. For robots, those adjustments remain remarkably difficult. The challenge is not merely moving fingers to the right positions. The harder part is maintaining stable interaction while the object itself is changing. Highlights from AGILINK’s ICRA 2026 demonstrations, including visuotactile sensing, in-hand manipulation, balloon-animal shaping, and other contact-rich tasks enabled by the company’s latest OmniHand platform. AGILINK That distinction helps explain why the balloon dog drew so much attention in Vienna. What appeared to be a dexterity demonstration was, in many ways, a demonstration about contact itself. As robotic manipulation continues to advance, a growing number of researchers are arriving at a similar conclusion: many of the hardest problems in robotics begin only after contact occurs. Motion and Contact Intelligence for Robot Manipulation Balloon twisting combines two challenges that robotics has traditionally struggled to solve simultaneously: long-horizon task execution and contact-rich manipulation. The first concerns motion. A balloon dog is not created through a single grasp or twist. It emerges through a carefully ordered sequence of manipulations, each setting the conditions for what follows. A small rotational error introduced early may appear insignificant at first, yet several steps later it can prevent the final structure from forming altogether. In that sense, balloon twisting is a long-horizon task. Success depends not only on performing individual actions correctly, but also on preserving the future feasibility of the entire manipulation process. To address this challenge, AGILINK began by collecting demonstrations from professional balloon artists. Human actions were mapped onto robotic hands to establish an initial manipulation policy. But successful demonstrations alone were insufficient. In practice, some of the most valuable learning occurred when execution began to drift toward failure. Whenever instability emerged, human operators intervened and corrected the manipulation in real time. Those interventions were recorded and incorporated into reinforcement-learning cycles, allowing the system to learn not only how successful demonstrations unfold, but also how experienced operators recover when things start to go wrong. Through this process, the robot gradually acquired the capabilities required for long-horizon task execution—a collection of abilities that AGILINK groups under the term motion intelligence : the ability to generate actions, coordinate bimanual behaviors, and execute extended manipulation sequences under real-world uncertainty. OmniHand 3 Ultra-M on display at ICRA 2026. AGILINK Yet motion alone does not explain why balloon twisting remains difficult. The second challenge is contact. The robot must continuously regulate force, adjust contact locations, and respond to subtle changes in the object’s state. These decisions are difficult to encode through explicit rules. Even skilled human operators often rely on tactile intuition developed through experience rather than consciously articulated strategies. Analysis of those interventions revealed that many failures did not originate from incorrect action sequences, but from the breakdown of contact itself. To better capture those interaction dynamics, AGILINK collected contact-centric intervention data and incorporated those interactions into reinforcement-learning training. Rather than learning only which motions to perform, the system also learned how humans maintain stability when contact conditions begin to deteriorate. AGILINK describes this capability as contact intelligence : the ability to establish, maintain, and adapt physical interaction as force distribution, friction, deformation, and contact geometry continuously evolve. The distinction between the two capabilities is subtle but important. Motion intelligence determines what the robot intends to do. Contact intelligence determines whether it can continue doing it. For balloon twisting, both are necessary. One provides the sequence of actions. The other keeps those actions physically viable. YouTuber KhanFlicks follows OmniHand’s motions while learning to fold a balloon dog at the AGILINK booth. AGILINK Between a balloon slipping away and a balloon bursting lies a narrow region of stability. Successful manipulation depends on finding that region—and remaining within it throughout the task. Introducing the OmniHand 3 Ultra-M Dexterous Hand The balloon dog demonstration showcased a manipulation capability. It also revealed a broader question. How much contact intelligence can be achieved through learning alone? A robot can only regulate what it can perceive. It can only respond as quickly as its hardware allows. As manipulation tasks become increasingly complex, researchers are finding that progress depends not only on better policies, but also on richer sensing and faster physical response. That realization formed the backdrop for AGILINK’s second major announcement at ICRA 2026. Alongside the balloon dog demonstration, the company introduced the OmniHand 3 Ultra-M . OmniHand 3 Ultra-M closely matches the size of an adult human hand. AGILINK The two exhibits represented different stages of the same technological trajectory. If the balloon dog demonstrated what contact intelligence can already accomplish today, Ultra-M was designed to explore what contact intelligence may require next. Building Hardware for Contact Intelligence Roughly the size of an adult human hand, the OmniHand 3 Ultra-M integrates 20 active degrees of freedom within a human-scale form factor. Its most distinctive feature is a fully direct-drive architecture. By adopting direct-drive actuation throughout the system, the hand is designed to enable faster and more transparent force regulation and higher force-control bandwidth, enabling faster response as contact conditions change. For contact-rich manipulation, responsiveness can be as important as sensing itself. By adopting direct-drive actuation throughout the system, the OmniHand 3 Ultra-M is designed to enable faster and more transparent force regulation and higher force-control bandwidth, enabling faster response as contact conditions change. The platform also incorporates tactile sensing across nearly the entire hand. Each fingertip contains a miniature vision-based tactile sensor, while more than 300 three-dimensional tactile sensing points are distributed throughout the palm. Together, they provide information not only about where contact occurs, but how contact is evolving. The system is designed to estimate pressure distribution, shear forces, local deformation, slip tendencies, and other interaction dynamics that often remain invisible to conventional position-based control systems. According to AGILINK’s tests, individual sensors achieve force resolution of approximately 0.005 N—roughly equivalent to detecting the weight of a sheet of paper resting on a fingertip. Spatial resolution reaches approximately 0.04 mm, while sensing density approaches 50,000 sensing points per square centimeter. OmniHand 3 Ultra-M recognizes feather texture through vision-based tactile sensing. AGILINK For dexterous robots, contact has traditionally been a largely hidden process. Ultra-M is designed to make that process more observable. Rather than simply detecting that contact has occurred, the system attempts to resolve where interaction is happening, how forces are distributed, whether instability is beginning to emerge, and how manipulation strategies should adapt in response. The balloon dog offered a glimpse of what contact intelligence can already accomplish. Ultra-M explores a different question: what capabilities may be required to push contact intelligence further? The Physical World Remains the Hardest Benchmark The significance of contact intelligence extends far beyond balloon animals. Many tasks that continue to resist automation involve unstable or deformable interaction: cable insertion, garment handling, flexible packaging, delicate assembly, connector mating, tool use, and household manipulation. These tasks are difficult not because robots cannot reach the correct location, but because maintaining stable interaction after contact begins remains extraordinarily hard. For decades, robotics achieved many of its successes by reducing uncertainty. Factories were engineered to make robotic motion predictable, repeatable, and highly structured. The physical world behaves differently. A growing share of robotics research is shifting toward interaction itself—understanding how robots can establish, maintain, and adapt physical contact within environments that remain fundamentally unpredictable. Objects shift. Materials deform. Friction changes. Contact evolves. Real environments rarely follow scripts. Seen through that lens, the balloon dog was never really about the balloon dog. What attracted attention at ICRA was not simply a visually impressive demonstration, but what it revealed: intelligence in the physical world is ultimately measured through interaction. As motion generation continues to mature, a growing share of robotics research is shifting toward interaction itself—understanding how robots can establish, maintain, and adapt physical contact within environments that remain fundamentally unpredictable. For robots moving beyond structured environments and into less predictable real-world settings, managing contact may become as important as motion itself. From balloon twisting to OmniHand 3 Ultra-M, AGILINK is shaping the future of contact intelligence Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention.

## 参考
- https://spectrum.ieee.org/agilink-contact-intelligence-robot-manipulation
