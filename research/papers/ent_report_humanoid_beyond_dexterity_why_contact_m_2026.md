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

## Overview
From balloon twisting to OmniHand 3 Ultra-M, AGILINK is shaping the future of contact intelligence. Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention.

## Content
This article is brought to you by AGILINK. Throughout the exhibition hall at the 2026 IEEE International Conference on Robotics (ICRA), in Vienna, one demonstration seemed to attract a disproportionate amount of attention. Two robotic hands were making a balloon dog. Slowly and deliberately, the robot twisted a long balloon into loops, bends, and joints without popping it. Visitors stopped, watched, and often returned with colleagues to watch again. AGILINK’s balloon dog demonstration draws a crowd at ICRA 2026. AGILINK At first glance, the demonstration appeared almost playful. Among roboticists, however, balloon twisting is widely recognized as an unusually difficult manipulation task. A balloon is lightweight, highly deformable, slippery, and extremely sensitive to force. Every twist changes its geometry and internal pressure, turning a seemingly simple activity into a continuously changing physical interaction problem. Humans navigate those changes almost intuitively. While making a balloon animal, people rarely think consciously about force regulation, slip prevention, or contact stability. They simply adjust. For robots, those adjustments remain remarkably difficult. The challenge is not merely moving fingers to the right positions. The harder part is maintaining stable interaction while the object itself is changing. Highlights from AGILINK’s ICRA 2026 demonstrations, including visuotactile sensing, in-hand manipulation, balloon-animal shaping, and other contact-rich tasks enabled by the company’s latest OmniHand platform. AGILINK That distinction helps explain why the balloon dog drew so much attention in Vienna. What appeared to be a dexterity demonstration was, in many ways, a demonstration about contact itself. As robotic manipulation continues to advance, a growing number of researchers are arriving at a similar conclusion: many of the hardest problems in robotics begin only after contact occurs. Motion and Contact Intelligence for Robot Manipulation Balloon twisting combines two challenges that robotics has traditionally struggled to solve simultaneously: long-horizon task execution and contact-rich manipulation. The first concerns motion. A balloon dog is not created through a single grasp or twist. It emerges through a carefully ordered sequence of manipulations, each setting the conditions for what follows. A small rotational error introduced early may appear insignificant at first, yet several steps later it can prevent the final structure from forming altogether. In that sense, balloon twisting is a long-horizon task. Success depends not only on performing individual actions correctly, but also on preserving the future feasibility of the entire manipulation process. To address this challenge, AGILINK began by collecting demonstrations from professional balloon artists. Human actions were mapped onto robotic hands to establish an initial manipulation policy. But successful demonstrations alone were insufficient. In practice, some of the most valuable learning occurred when execution began to drift toward failure. Whenever instability emerged, human operators intervened and corrected the manipulation in real time. Those interventions were recorded and incorporated into reinforcement-learning cycles, allowing the system to learn not only how successful demonstrations unfold, but also how experienced operators recover when things start to go wrong. Through this process, the robot gradually acquired the capabilities required for long-horizon task execution—a collection of abilities that AGILINK groups under the term motion intelligence: the ability to generate actions, coordinate bimanual behaviors, and execute extended manipulation sequences under real-world uncertainty. OmniHand 3 Ultra-M on display at ICRA 2026. AGILINK Yet motion alone does not explain why balloon twisting remains difficult. The second challenge is contact. The robot must continuously regulate force, adjust contact locations, and respond to subtle changes in the object’s state. These decisions are difficult to encode through explicit rules. Even skilled human operators often rely on tactile intuition developed through experience rather than consciously articulated strategies. Analysis of those interventions revealed that many failures did not originate from incorrect action sequences, but from the breakdown of contact itself. To better capture those interaction dynamics, AGILINK collected contact-centric intervention data and incorporated those interactions into reinforcement-learning training. Rather than learning only which motions to perform, the system also learned how humans maintain stability when contact conditions begin to deteriorate. AGILINK describes this capability as contact intelligence: the ability to establish, maintain, and adapt physical interaction as force distribution, friction, deformation, and contact geometry continuously evolve. The distinction between the two capabilities is subtle but important. Motion intelligence determines what the robot intends to do. Contact intelligence determines whether it can continue doing it. For balloon twisting, both are necessary. One provides the sequence of actions. The other keeps those actions physically viable. YouTuber KhanFlicks follows OmniHand’s motions while learning to fold a balloon dog at the AGILINK booth. AGILINK Between a balloon slipping away and a balloon bursting lies a narrow region of stability. Successful manipulation depends on finding that region—and remaining within it throughout the task. Introducing the OmniHand 3 Ultra-M Dexterous Hand The balloon dog demonstration showcased a manipulation capability. It also revealed a broader question. How much contact intelligence can be achieved through learning alone? A robot can only regulate what it can perceive. It can only respond as quickly as its hardware allows. As manipulation tasks become increasingly complex, researchers are finding that progress depends not only on better policies, but also on richer sensing and faster physical response. That realization formed the backdrop for AGILINK’s second major announcement at ICRA 2026. Alongside the balloon dog demonstration, the company introduced the OmniHand 3 Ultra-M. OmniHand 3 Ultra-M closely matches the size of an adult human hand. AGILINK The two exhibits represented different stages of the same technological trajectory. If the balloon dog demonstrated what contact intelligence can already accomplish today, Ultra-M was designed to explore what contact intelligence may require next. Building Hardware for Contact Intelligence Roughly the size of an adult human hand, the OmniHand 3 Ultra-M integrates 20 active de

## 개요
풍선 꼬기부터 OmniHand 3 Ultra-M까지, AGILINK는 접촉 지능의 미래를 형성하고 있습니다. 2026년 IEEE 국제 로봇 공학 컨퍼런스(ICRA)가 열린 비엔나 전시장에서는 한 데모가 특히 큰 주목을 받았습니다.

## 핵심 내용
이 기사는 AGILINK가 제공합니다. 2026년 IEEE 국제 로봇 공학 컨퍼런스(ICRA)가 열린 비엔나 전시장에서는 한 데모가 특히 큰 주목을 받았습니다. 두 개의 로봇 손이 풍선 개를 만들고 있었습니다. 로봇은 천천히 그리고 신중하게 긴 풍선을 고리, 굽힘, 관절로 꼬아 터뜨리지 않았습니다. 방문객들은 멈춰 서서 지켜보았고, 종종 동료와 함께 다시 보러 돌아오기도 했습니다. AGILINK의 풍선 개 데모는 ICRA 2026에서 군중을 끌어모았습니다. AGILINK 언뜻 보기에 이 데모는 거의 장난처럼 보였습니다. 그러나 로봇 공학자들 사이에서 풍선 꼬기는 비정상적으로 어려운 조작 작업으로 널리 인정받고 있습니다. 풍선은 가볍고, 변형이 매우 쉽고, 미끄럽고, 힘에 극도로 민감합니다. 모든 꼬임은 기하학적 구조와 내부 압력을 변화시켜, 겉보기에 단순한 활동을 지속적으로 변화하는 물리적 상호작용 문제로 만듭니다. 인간은 이러한 변화를 거의 직관적으로 탐색합니다. 풍선 동물을 만들 때 사람들은 힘 조절, 미끄러짐 방지 또는 접촉 안정성에 대해 의식적으로 거의 생각하지 않습니다. 그저 조정할 뿐입니다. 로봇에게 이러한 조정은 여전히 매우 어렵습니다. 문제는 단순히 손가락을 올바른 위치로 움직이는 것이 아닙니다. 더 어려운 부분은 물체 자체가 변화하는 동안 안정적인 상호작용을 유지하는 것입니다. AGILINK의 ICRA 2026 데모 하이라이트: 시각-촉각 감지, 손 안 조작, 풍선 동물 성형 및 회사의 최신 OmniHand 플랫폼이 가능하게 한 기타 접촉이 많은 작업. AGILINK 이러한 차이점은 비엔나에서 풍선 개가 왜 그렇게 많은 관심을 끌었는지 설명하는 데 도움이 됩니다. 손재주 데모로 보였던 것은 여러 면에서 접촉 자체에 대한 데모였습니다. 로봇 조작이 계속 발전함에 따라 점점 더 많은 연구자들이 비슷한 결론에 도달하고 있습니다. 로봇 공학에서 가장 어려운 문제 중 상당수는 접촉이 발생한 후에야 시작된다는 것입니다. 로봇 조작을 위한 운동 및 접촉 지능 풍선 꼬기는 로봇 공학이 전통적으로 동시에 해결하는 데 어려움을 겪어온 두 가지 도전 과제, 즉 장기 작업 실행과 접촉이 많은 조작을 결합합니다. 첫 번째는 운동에 관한 것입니다. 풍선 개는 단일 잡기나 꼬임으로 만들어지지 않습니다. 신중하게 순서가 정해진 일련의 조작을 통해 나타나며, 각 조작은 다음 단계를 위한 조건을 설정합니다. 초기에 도입된 작은 회전 오류는 처음에는 사소해 보일 수 있지만, 몇 단계 후에는 최종 구조가 전혀 형성되는 것을 방해할 수 있습니다. 그런 의미에서 풍선 꼬기는 장기 작업입니다. 성공은 개별 동작을 올바르게 수행하는 것뿐만 아니라 전체 조작 과정의 미래 실행 가능성을 보존하는 데 달려 있습니다. 이 문제를 해결하기 위해 AGILINK는 전문 풍선 아티스트의 시연을 수집하는 것으로 시작했습니다. 인간의 동작을 로봇 손에 매핑하여 초기 조작 정책을 수립했습니다. 그러나 성공적인 시연만으로는 충분하지 않았습니다. 실제로 가장 가치 있는 학습 중 일부는 실행이 실패 쪽으로 흐르기 시작할 때 발생했습니다. 불안정성이 발생할 때마다 인간 운영자가 개입하여 실시간으로 조작을 수정했습니다. 이러한 개입은 기록되어 강화 학습 주기에 통합되어, 시스템이 성공적인 시연이 어떻게 전개되는지뿐만 아니라 상황이 잘못되기 시작할 때 숙련된 운영자가 어떻게 회복하는지도 학습할 수 있게 했습니다. 이 과정을 통해 로봇은 점차 장기 작업 실행에 필요한 능력, 즉 AGILINK가 운동 지능이라는 용어로 묶는 능력 집합(실제 세계의 불확실성 하에서 동작을 생성하고, 양손 행동을 조정하며, 확장된 조작 시퀀스를 실행하는 능력)을 획득했습니다. ICRA 2026에 전시된 OmniHand 3 Ultra-M. AGILINK 그러나 운동만으로는 풍선 꼬기가 여전히 어려운 이유를 설명하지 못합니다. 두 번째 도전 과제는 접촉입니다. 로봇은 지속적으로 힘을 조절하고, 접촉 위치를 조정하며, 물체 상태의 미묘한 변화에 반응해야 합니다. 이러한 결정은 명시적인 규칙을 통해 인코딩하기 어렵습니다. 숙련된 인간 운영자조차도 의식적으로 명확히 표현된 전략보다는 경험을 통해 개발된 촉각적 직관에 의존하는 경우가 많습니다. 이러한 개입에 대한 분석은 많은 실패가 잘못된 동작 순서에서 비롯된 것이 아니라 접촉 자체의 붕괴에서 비롯되었음을 밝혀냈습니다. 이러한 상호작용 역학을 더 잘 포착하기 위해 AGILINK는 접촉 중심의 개입 데이터를 수집하고 이러한 상호작용을 강화 학습 훈련에 통합했습니다. 시스템은 수행할 동작만 학습하는 것이 아니라 접촉 조건이 악화되기 시작할 때 인간이 어떻게 안정성을 유지하는지도 학습했습니다. AGILINK는 이 능력을 접촉 지능이라고 설명합니다. 즉, 힘 분포, 마찰, 변형 및 접촉 기하학이 지속적으로 진화함에 따라 물리적 상호작용을 설정, 유지 및 적응시키는 능력입니다. 두 능력의 차이는 미묘하지만 중요합니다. 운동 지능은 로봇이 무엇을 하려는지 결정합니다. 접촉 지능은 로봇이 그것을 계속할 수 있는지 여부를 결정합니다. 풍선 꼬기의 경우 둘 다 필요합니다. 하나는 동작 순서를 제공합니다. 다른 하나는 이러한 동작을 물리적으로 실행 가능하게 유지합니다. YouTube 사용자 KhanFlicks가 AGILINK 부스에서 풍선 개 접는 법을 배우면서 OmniHand의 동작을 따라합니다. AGILINK 풍선이 미끄러지는 것과 풍선이 터지는 것 사이에는 좁은 안정성 영역이 있습니다. 성공적인 조작은 그 영역을 찾고 작업 내내 그 안에 머무는 데 달려 있습니다. OmniHand 3 Ultra-M 고급 손 소개 풍선 개 데모는 조작 능력을 보여주었습니다. 또한 더 광범위한 질문을 제기했습니다. 학습만으로 얼마나 많은 접촉 지능을 달성할 수 있을까요? 로봇은 인지할 수 있는 것만 조절할 수 있습니다. 하드웨어가 허용하는 만큼만 빠르게 반응할 수 있습니다. 조작 작업이 점점 더 복잡해짐에 따라 연구자들은 진전이 더 나은 정책뿐만 아니라 더 풍부한 감지와 더 빠른 물리적 반응에도 달려 있음을 발견하고 있습니다. 이러한 인식은 ICRA 2026에서 AGILINK의 두 번째 주요 발표의 배경을 형성했습니다. 풍선 개 데모와 함께 회사는 OmniHand 3 Ultra-M을 소개했습니다. OmniHand 3 Ultra-M은 성인 인간 손의 크기와 거의 일치합니다. AGILINK 두 전시물은 동일한 기술 궤적의 다른 단계를 나타냈습니다. 풍선 개가 접촉 지능이 오늘날 이미 무엇을 달성할 수 있는지 보여주었다면, Ultra-M은 접촉 지능이 다음에 무엇을 필요로 할지 탐구하도록 설계되었습니다. 접촉 지능을 위한 하드웨어 구축 대략 성인 인간 손 크기인 OmniHand 3 Ultra-M은 20개의 능동
