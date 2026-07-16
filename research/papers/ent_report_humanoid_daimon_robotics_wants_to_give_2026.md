---
$id: ent_report_humanoid_daimon_robotics_wants_to_give_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: DAIMON Robotics Wants to Give Robot Hands a Sense of Touch
  zh: DAIMON Robotics Wants to Give Robot Hands a Sense of Touch
  ko: DAIMON Robotics Wants to Give Robot Hands a Sense of Touch
summary:
  en: 'This article is brought to you by DAIMON Robotics . This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity
    , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing
    and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project
    is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern
    University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old
    company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that
    packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing
    technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON
    is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the
    real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang,
    co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating
    the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder
    and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went
    on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief
    of IEEE Transactions on Automation Science and Engineering , he has spent roughly four decades in the field. His objective
    is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action
    (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile
    to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation,
    how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where
    — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity
    is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res
    tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative
    This month, DAIMON Robotics release d the largest and most comprehensive robotic manipulation dataset with multiple leading
    academic institutions and enterprises. Why releas ing the dataset now, rather than continuing to focus on product development?
    What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a
    half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction
    between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted
    and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics
    companies. As embodied AI continues to advance, the critical role of data has been clearer. Data scarcity remains a primary
    bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate
    effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research
    and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality,
    multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and
    surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal
    fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion
    trajectories, and natural language, transforming raw inputs into training-ready dataset for machine learning models. Recognizing
    the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a
    responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality
    “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation
    models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing
    a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were
    you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building
    hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile
    sensing technology and innovative data collection paradigm enable us to build large-scale dataset. Our approach is to
    broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying
    on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world
    environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied
    AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON
    Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its
    development, and how will the dataset benefit their research and products? Besides China based teams, our partners include
    leading research groups from universities, such as Northwestern University and the National University of Singapore, as
    well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong
    testament to the value of our tactile-rich dataset. Among the companies involved there are some that have already built
    their own models but are now incorporating tactile information. By deploying our data collection devices across research,
    manufacturing and other real-world scenarios, they help us to gather highly practical, application-driven data. In turn,
    our partners leverage the data to train models tailored to their specific use cases. Furthermore, to drive the advancement
    of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community. Equipped
    with Daimon’s visuotactile sensor, the gripper delicately senses contact and precisely controls force to pick up a fragile
    eggshell. Daimon Robotics From VLA to VTLA: Why Tactile Sensing Changes the Equation The mainstream paradigm in robotics
    is currently the Vision-Language-Action (VLA) model, but your team has proposed a Vision-Tactile-Language-Action (VTLA)
    model. Why is it necessary to incorporate tactile sensing? What does it enable robots to achieve, and which tasks are
    likely to fail without tactile feedback? Over these years of working to make generalist robots capable of performing manipulation
    tasks, especially dexterous manipulation — not just power grasping or holding an object, but manipulating objects and
    using tools to impart forces and motion onto parts — we see these robots being used in household as well as industrial
    assembly settings. It is well established that tactile information is essential for providing feedback about contact states
    so that robots can guide their hands and fingers to perform reliable manipulation. Without tactile sensing, robots are
    severely limited. They struggle to locate objects in dark environments, and without slip detection, they can easily drop
    fragile items like glass. Furthermore, the inability to precisely control force often leads to failed manipulation tasks
    or, in severe cases, physical damage. Naturally, the VLA approach needs to be enhanced to incorporate tactile information.
    We expanded the VLA framework to incorporate tactile data, creating the VTLA model. An additional benefit of our tactile
    sensor is that it is vision-based: We capture visual images of the deformation on the fingertip surface. We capture multiple
    images in a time sequence that encodes contact information, from which we can infer forces and other contact states. This
    aligns well with the visual framework that VLA is based upon. Having tactile information in a visual image format makes
    it naturally suitable for integration into the VLA framework, transforming it into a VTLA system. That is the key advantage:
    Vision-based tactile sensors provide very high resolution at the pixel level, and this data can be incorporated into the
    framework, whether it is an end-to-end model or another type of architecture. DAIMON has been known for its vision-based
    tactile sensors that can pack over 110,000 effective sensing units. DAIMON Robotics The Technology: Monochromatic Vision-based
    Tactile Sensing You and your team have spent many years deeply engaged in vision-based tactile sensing and have developed
    the world’s first monochromatic vision-based tactile sensing technology. Why did you choose this technical path? Once
    we started investigating tactile sensors, we understood our needs. We wanted sensors that closely mimic what we have under
    our fingertip skin. Physiological studies have well documented the capabilities humans have at their fingertips — knowing
    what we touch, what kind of material it is, how forces are distributed, and whether it is moving into the right position
    as our brain controls our hands. We knew that replicating these capabilities on a robot hand’s fingertips would help considerably.
    When we surveyed existing technologies, we found many types, including vision-based tactile sensors with tri-color optics
    and other simpler designs. We decided to integrate the best of these into an engineering-robust solution that works well
    without being overly complicated, keeping cost, reliability, and sensitivity within a satisfactory range, thus ultimately
    developing a monochromatic vision-based tactile sensing technique. This is fundamentally an engineering approach rather
    than a purely scientific one, since a great deal of foundational research already existed. With the growing realization
    of the necessity of tactile data, all of this will advance hand in hand. DAIMON vision-based tactile sensor captures high-quality,
    multimodal tactile data. DAIMON Robotics Last year, DAIMON launched a multi-dimensional, high-resolution, high-frequency
    vision-based tactile sensor. Compared with traditional tactile sensors, where does its core advantage lie? Which industries
    could it potentially transform? The key features of our sensors are the density of distributed force measurement and the
    deformation we can capture over the area of a fingertip. I believe we have the highest density in terms of sensing units.
    That is one very important metric. The other is dynamics: the frequency and bandwidth — how quickly we can detect force
    changes, transmit signals, and process them in real time. Other important aspects are largely engineering-related, such
    as reliability, drift, durability of the soft surface, and resistance to interference from magnetic, optical, or environmental
    factors. A growing number of researchers and companies are recognizing the importance of tactile sensing and adopting
    our technology. I believe the advances in tactile sensing will elevate the entire community and industry to a higher level.
    One of our potential customers is deploying humanoid robots in a small convenience store, with densely packed shelves
    where shelf space is at a premium. The robot needs to reach into very tight spaces — tighter than books on a shelf — to
    pick out an object. Current two-jaw parallel grippers cannot fit into most of these spaces. Observing how humans pick
    up objects, you clearly need at least three slim fingers to touch and roll the object toward you and secure it. Thus,
    we are starting to see very specific needs where tactile sensing capabilities are essential. From Academia to Startup
    After 40 years in academia — founding the HKUST Robotics Institute, earning prestigious honors including IEEE Fellow,
    and serving as Editor-in-Chief of IEEE TASE — what motivated you to found DAIMON Robotics? I have come a long way. I started
    learning robotics during my PhD at Carnegie Mellon, where there were truly remarkable groups working on locomotion under
    Marc Raibert, who founded Boston Dynamics, and on manipulation under my advisor, Matt Mason, a leader in the field. We
    have been working on dexterous manipulation, not only at Carnegie Mellon, but globally for many years. However, progress
    has been limited for a long time, especially in building dexterous hands and making them work. Only recently have locomotion
    robots truly taken off, and only in the last few years have we begun to see major advancements in robot hands. There is
    clearly room for advancing manipulation capabilities, which would enable robots to do work like humans. While at Hong
    Kong University of Science and Technology, I saw increasingly greater people entering this area in the form of students
    and postdoctoral researchers. We wanted to jumpstart our effort by leveraging the available capital and talent resources.
    Fortunately, one of my postdocs, Dr. Duan Jianghua , has a strong sense for commercial opportunities. Recognizing the
    rapid growth of robotics market and the unique value that our vision-based tactile sensing technology could bring, together
    we started DAIMON Robotics, and it has progressed well. The community has grown tremendously in China, Japan, Korea, the
    U.S., and Europe. Robots equipped with DAIMON technology have been deployed in factory settings. The company aims to enable
    robots to achieve “embodied intelligence” and close the gap between what they can see and what they can feel. DAIMON Robotics
    Business Model and Commercial Strategy What is DAIMON’s current business model and strategic focus? What role does the
    dataset release play in your commercial strategy? We started as a device company focused on making highly capable tactile
    sensors, especially for robot hands. But as technology and business developed, everyone realized it is not just about
    one component, rather the entire technology chain: devices, data of adequate quality and quantity, and finally the right
    framework to build, train, and deploy models on robots in real application environments. Our business strategy is best
    described as “3D”: Devices, Data, and Deployment. We build devices for data collection, our own ecosystem, and for deploying
    them in our partners’ potential application domains. This enables the collection of real-world tactile-rich data and complete
    closed-loop validation. This will become an integral part of the 3D business model. Most startups in this space are following
    a similar path until eventually some may become more specialized or more tightly integrated with other companies. For
    now, it is mostly vertical integration. Embodied Skills and the Convergence Moment You’ve introduced the concept of “embodied
    skills” as essential for humanoid robots to move beyond having just an advanced AI “brain.” What prompted this insight?
    What new capabilities could embodied skills enable? After the rapid evolution of models and hardware over the past two
    years, has your definition or roadmap for embodied skills evolved? We have come a long way now see a convergence point
    where electrical, electronic, and mechatronic hardware technologies have advanced tremendously in last two decades. Robots
    are now fully electric, do not require hydraulics, because hardware has evolved rapidly. Modern electronics provide tremendous
    bandwidth with high torques. If we can build intelligence into these systems, we can create truly humanoid robots with
    the ability to operate in unstructured environments, make decisions, and take actions autonomously. “Our vision is for
    robots to achieve robust manipulation capabilities and evolve into reliable partners for humans.” —Prof. Michael Yu Wang,
    DAIMON Robotics AI has arrived at exactly the right time. Enormous resources have been invested in AI development, especially
    large language models, which are now being generalized into world models that enable physical AI capabilities. We would
    like to see these manifested in real-world systems. While both AI and core hardware technologies continue to evolve, the
    focus is much clearer now. For example, human-sized robots are preferred in a home environment. This is an exciting domain
    with a promise of great societal benefit if we can eventually achieve safe, reliable, and cost-effective robots. The Road
    to Real-World Deployment Today, many robots can deliver impressive demos, yet there remains a gap before they truly enter
    real-world applications. What could be a potential trigger for real-world deployment? Which scenarios are most likely
    to achieve large-scale deployment first? I think the road toward large-scale deployment of generalist robots is still
    long, but we are starting to see signs of feasibility within specific domains. It is very similar to autonomous vehicles,
    where we are yet to see full deployment of robo-taxis, while we have already started to find mobile robots and smaller
    vehicles widely deployed in the hospitality industry. Virtually every major hotel in China now has a delivery robot —
    no arms, just a vehicle that picks up items from the hotel lobby (e.g., food deliveries). The delivery person just loads
    the food and selects the room number. It is up to the robot thereafter to navigate and reach the guest’s room, which includes
    using the elevator, to deliver the food. This is already nearly 100 percent deployed in major Chinese hotels. Hotel and
    restaurant robots are viewed as a model for deploying humanoid robots in specific domains like overnight drugstores and
    convenience stores. I expect complete deployment in such settings within a short timeframe, followed by other applications.
    Overall, we can expect autonomous robots, including humanoids, to progressively penetrate specific sectors, delivering
    value in each and expanding into others. Ultimately, our vision is for robots to achieve robust manipulation capabilities
    and evolve into reliable partners for humans. By seamlessly integrating into our homes and daily lives, they will genuinely
    benefit and serve humanity. This interview has been edited for length and clarity.'
  zh: 'This article is brought to you by DAIMON Robotics . This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity
    , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing
    and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project
    is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern
    University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old
    company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that
    packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing
    technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON
    is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the
    real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang,
    co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating
    the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder
    and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went
    on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief
    of IEEE Transactions on Automation Science and Engineering , he has spent roughly four decades in the field. His objective
    is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action
    (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile
    to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation,
    how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where
    — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity
    is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res
    tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative
    This month, DAIMON Robotics release d the largest and most comprehensive robotic manipulation dataset with multiple leading
    academic institutions and enterprises. Why releas ing the dataset now, rather than continuing to focus on product development?
    What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a
    half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction
    between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted
    and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics
    companies. As embodied AI continues to advance, the critical role of data has been clearer. Data scarcity remains a primary
    bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate
    effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research
    and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality,
    multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and
    surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal
    fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion
    trajectories, and natural language, transforming raw inputs into training-ready dataset for machine learning models. Recognizing
    the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a
    responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality
    “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation
    models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing
    a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were
    you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building
    hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile
    sensing technology and innovative data collection paradigm enable us to build large-scale dataset. Our approach is to
    broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying
    on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world
    environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied
    AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON
    Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its
    development, and how will the dataset benefit their research and products? Besides China based teams, our partners include
    leading research groups from universities, such as Northwestern University and the National University of Singapore, as
    well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong
    testament to the value of our tactile-rich dataset. Among the companies involved there are some that have already built
    their own models but are now incorporating tactile information. By deploying our data collection devices across research,
    manufacturing and other real-world scenarios, they help us to gather highly practical, application-driven data. In turn,
    our partners leverage the data to train models tailored to their specific use cases. Furthermore, to drive the advancement
    of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community. Equipped
    with Daimon’s visuotactile sensor, the gripper delicately senses contact and precisely controls force to pick up a fragile
    eggshell. Daimon Robotics From VLA to VTLA: Why Tactile Sensing Changes the Equation The mainstream paradigm in robotics
    is currently the Vision-Language-Action (VLA) model, but your team has proposed a Vision-Tactile-Language-Action (VTLA)
    model. Why is it necessary to incorporate tactile sensing? What does it enable robots to achieve, and which tasks are
    likely to fail without tactile feedback? Over these years of working to make generalist robots capable of performing manipulation
    tasks, especially dexterous manipulation — not just power grasping or holding an object, but manipulating objects and
    using tools to impart forces and motion onto parts — we see these robots being used in household as well as industrial
    assembly settings. It is well established that tactile information is essential for providing feedback about contact states
    so that robots can guide their hands and fingers to perform reliable manipulation. Without tactile sensing, robots are
    severely limited. They struggle to locate objects in dark environments, and without slip detection, they can easily drop
    fragile items like glass. Furthermore, the inability to precisely control force often leads to failed manipulation tasks
    or, in severe cases, physical damage. Naturally, the VLA approach needs to be enhanced to incorporate tactile information.
    We expanded the VLA framework to incorporate tactile data, creating the VTLA model. An additional benefit of our tactile
    sensor is that it is vision-based: We capture visual images of the deformation on the fingertip surface. We capture multiple
    images in a time sequence that encodes contact information, from which we can infer forces and other contact states. This
    aligns well with the visual framework that VLA is based upon. Having tactile information in a visual image format makes
    it naturally suitable for integration into the VLA framework, transforming it into a VTLA system. That is the key advantage:
    Vision-based tactile sensors provide very high resolution at the pixel level, and this data can be incorporated into the
    framework, whether it is an end-to-end model or another type of architecture. DAIMON has been known for its vision-based
    tactile sensors that can pack over 110,000 effective sensing units. DAIMON Robotics The Technology: Monochromatic Vision-based
    Tactile Sensing You and your team have spent many years deeply engaged in vision-based tactile sensing and have developed
    the world’s first monochromatic vision-based tactile sensing technology. Why did you choose this technical path? Once
    we started investigating tactile sensors, we understood our needs. We wanted sensors that closely mimic what we have under
    our fingertip skin. Physiological studies have well documented the capabilities humans have at their fingertips — knowing
    what we touch, what kind of material it is, how forces are distributed, and whether it is moving into the right position
    as our brain controls our hands. We knew that replicating these capabilities on a robot hand’s fingertips would help considerably.
    When we surveyed existing technologies, we found many types, including vision-based tactile sensors with tri-color optics
    and other simpler designs. We decided to integrate the best of these into an engineering-robust solution that works well
    without being overly complicated, keeping cost, reliability, and sensitivity within a satisfactory range, thus ultimately
    developing a monochromatic vision-based tactile sensing technique. This is fundamentally an engineering approach rather
    than a purely scientific one, since a great deal of foundational research already existed. With the growing realization
    of the necessity of tactile data, all of this will advance hand in hand. DAIMON vision-based tactile sensor captures high-quality,
    multimodal tactile data. DAIMON Robotics Last year, DAIMON launched a multi-dimensional, high-resolution, high-frequency
    vision-based tactile sensor. Compared with traditional tactile sensors, where does its core advantage lie? Which industries
    could it potentially transform? The key features of our sensors are the density of distributed force measurement and the
    deformation we can capture over the area of a fingertip. I believe we have the highest density in terms of sensing units.
    That is one very important metric. The other is dynamics: the frequency and bandwidth — how quickly we can detect force
    changes, transmit signals, and process them in real time. Other important aspects are largely engineering-related, such
    as reliability, drift, durability of the soft surface, and resistance to interference from magnetic, optical, or environmental
    factors. A growing number of researchers and companies are recognizing the importance of tactile sensing and adopting
    our technology. I believe the advances in tactile sensing will elevate the entire community and industry to a higher level.
    One of our potential customers is deploying humanoid robots in a small convenience store, with densely packed shelves
    where shelf space is at a premium. The robot needs to reach into very tight spaces — tighter than books on a shelf — to
    pick out an object. Current two-jaw parallel grippers cannot fit into most of these spaces. Observing how humans pick
    up objects, you clearly need at least three slim fingers to touch and roll the object toward you and secure it. Thus,
    we are starting to see very specific needs where tactile sensing capabilities are essential. From Academia to Startup
    After 40 years in academia — founding the HKUST Robotics Institute, earning prestigious honors including IEEE Fellow,
    and serving as Editor-in-Chief of IEEE TASE — what motivated you to found DAIMON Robotics? I have come a long way. I started
    learning robotics during my PhD at Carnegie Mellon, where there were truly remarkable groups working on locomotion under
    Marc Raibert, who founded Boston Dynamics, and on manipulation under my advisor, Matt Mason, a leader in the field. We
    have been working on dexterous manipulation, not only at Carnegie Mellon, but globally for many years. However, progress
    has been limited for a long time, especially in building dexterous hands and making them work. Only recently have locomotion
    robots truly taken off, and only in the last few years have we begun to see major advancements in robot hands. There is
    clearly room for advancing manipulation capabilities, which would enable robots to do work like humans. While at Hong
    Kong University of Science and Technology, I saw increasingly greater people entering this area in the form of students
    and postdoctoral researchers. We wanted to jumpstart our effort by leveraging the available capital and talent resources.
    Fortunately, one of my postdocs, Dr. Duan Jianghua , has a strong sense for commercial opportunities. Recognizing the
    rapid growth of robotics market and the unique value that our vision-based tactile sensing technology could bring, together
    we started DAIMON Robotics, and it has progressed well. The community has grown tremendously in China, Japan, Korea, the
    U.S., and Europe. Robots equipped with DAIMON technology have been deployed in factory settings. The company aims to enable
    robots to achieve “embodied intelligence” and close the gap between what they can see and what they can feel. DAIMON Robotics
    Business Model and Commercial Strategy What is DAIMON’s current business model and strategic focus? What role does the
    dataset release play in your commercial strategy? We started as a device company focused on making highly capable tactile
    sensors, especially for robot hands. But as technology and business developed, everyone realized it is not just about
    one component, rather the entire technology chain: devices, data of adequate quality and quantity, and finally the right
    framework to build, train, and deploy models on robots in real application environments. Our business strategy is best
    described as “3D”: Devices, Data, and Deployment. We build devices for data collection, our own ecosystem, and for deploying
    them in our partners’ potential application domains. This enables the collection of real-world tactile-rich data and complete
    closed-loop validation. This will become an integral part of the 3D business model. Most startups in this space are following
    a similar path until eventually some may become more specialized or more tightly integrated with other companies. For
    now, it is mostly vertical integration. Embodied Skills and the Convergence Moment You’ve introduced the concept of “embodied
    skills” as essential for humanoid robots to move beyond having just an advanced AI “brain.” What prompted this insight?
    What new capabilities could embodied skills enable? After the rapid evolution of models and hardware over the past two
    years, has your definition or roadmap for embodied skills evolved? We have come a long way now see a convergence point
    where electrical, electronic, and mechatronic hardware technologies have advanced tremendously in last two decades. Robots
    are now fully electric, do not require hydraulics, because hardware has evolved rapidly. Modern electronics provide tremendous
    bandwidth with high torques. If we can build intelligence into these systems, we can create truly humanoid robots with
    the ability to operate in unstructured environments, make decisions, and take actions autonomously. “Our vision is for
    robots to achieve robust manipulation capabilities and evolve into reliable partners for humans.” —Prof. Michael Yu Wang,
    DAIMON Robotics AI has arrived at exactly the right time. Enormous resources have been invested in AI development, especially
    large language models, which are now being generalized into world models that enable physical AI capabilities. We would
    like to see these manifested in real-world systems. While both AI and core hardware technologies continue to evolve, the
    focus is much clearer now. For example, human-sized robots are preferred in a home environment. This is an exciting domain
    with a promise of great societal benefit if we can eventually achieve safe, reliable, and cost-effective robots. The Road
    to Real-World Deployment Today, many robots can deliver impressive demos, yet there remains a gap before they truly enter
    real-world applications. What could be a potential trigger for real-world deployment? Which scenarios are most likely
    to achieve large-scale deployment first? I think the road toward large-scale deployment of generalist robots is still
    long, but we are starting to see signs of feasibility within specific domains. It is very similar to autonomous vehicles,
    where we are yet to see full deployment of robo-taxis, while we have already started to find mobile robots and smaller
    vehicles widely deployed in the hospitality industry. Virtually every major hotel in China now has a delivery robot —
    no arms, just a vehicle that picks up items from the hotel lobby (e.g., food deliveries). The delivery person just loads
    the food and selects the room number. It is up to the robot thereafter to navigate and reach the guest’s room, which includes
    using the elevator, to deliver the food. This is already nearly 100 percent deployed in major Chinese hotels. Hotel and
    restaurant robots are viewed as a model for deploying humanoid robots in specific domains like overnight drugstores and
    convenience stores. I expect complete deployment in such settings within a short timeframe, followed by other applications.
    Overall, we can expect autonomous robots, including humanoids, to progressively penetrate specific sectors, delivering
    value in each and expanding into others. Ultimately, our vision is for robots to achieve robust manipulation capabilities
    and evolve into reliable partners for humans. By seamlessly integrating into our homes and daily lives, they will genuinely
    benefit and serve humanity. This interview has been edited for length and clarity.'
  ko: 'This article is brought to you by DAIMON Robotics . This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity
    , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing
    and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project
    is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern
    University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old
    company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that
    packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing
    technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON
    is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the
    real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang,
    co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating
    the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder
    and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went
    on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief
    of IEEE Transactions on Automation Science and Engineering , he has spent roughly four decades in the field. His objective
    is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action
    (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile
    to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation,
    how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where
    — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity
    is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res
    tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative
    This month, DAIMON Robotics release d the largest and most comprehensive robotic manipulation dataset with multiple leading
    academic institutions and enterprises. Why releas ing the dataset now, rather than continuing to focus on product development?
    What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a
    half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction
    between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted
    and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics
    companies. As embodied AI continues to advance, the critical role of data has been clearer. Data scarcity remains a primary
    bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate
    effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research
    and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality,
    multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and
    surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal
    fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion
    trajectories, and natural language, transforming raw inputs into training-ready dataset for machine learning models. Recognizing
    the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a
    responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality
    “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation
    models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing
    a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were
    you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building
    hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile
    sensing technology and innovative data collection paradigm enable us to build large-scale dataset. Our approach is to
    broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying
    on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world
    environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied
    AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON
    Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its
    development, and how will the dataset benefit their research and products? Besides China based teams, our partners include
    leading research groups from universities, such as Northwestern University and the National University of Singapore, as
    well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong
    testament to the value of our tactile-rich dataset. Among the companies involved there are some that have already built
    their own models but are now incorporating tactile information. By deploying our data collection devices across research,
    manufacturing and other real-world scenarios, they help us to gather highly practical, application-driven data. In turn,
    our partners leverage the data to train models tailored to their specific use cases. Furthermore, to drive the advancement
    of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community. Equipped
    with Daimon’s visuotactile sensor, the gripper delicately senses contact and precisely controls force to pick up a fragile
    eggshell. Daimon Robotics From VLA to VTLA: Why Tactile Sensing Changes the Equation The mainstream paradigm in robotics
    is currently the Vision-Language-Action (VLA) model, but your team has proposed a Vision-Tactile-Language-Action (VTLA)
    model. Why is it necessary to incorporate tactile sensing? What does it enable robots to achieve, and which tasks are
    likely to fail without tactile feedback? Over these years of working to make generalist robots capable of performing manipulation
    tasks, especially dexterous manipulation — not just power grasping or holding an object, but manipulating objects and
    using tools to impart forces and motion onto parts — we see these robots being used in household as well as industrial
    assembly settings. It is well established that tactile information is essential for providing feedback about contact states
    so that robots can guide their hands and fingers to perform reliable manipulation. Without tactile sensing, robots are
    severely limited. They struggle to locate objects in dark environments, and without slip detection, they can easily drop
    fragile items like glass. Furthermore, the inability to precisely control force often leads to failed manipulation tasks
    or, in severe cases, physical damage. Naturally, the VLA approach needs to be enhanced to incorporate tactile information.
    We expanded the VLA framework to incorporate tactile data, creating the VTLA model. An additional benefit of our tactile
    sensor is that it is vision-based: We capture visual images of the deformation on the fingertip surface. We capture multiple
    images in a time sequence that encodes contact information, from which we can infer forces and other contact states. This
    aligns well with the visual framework that VLA is based upon. Having tactile information in a visual image format makes
    it naturally suitable for integration into the VLA framework, transforming it into a VTLA system. That is the key advantage:
    Vision-based tactile sensors provide very high resolution at the pixel level, and this data can be incorporated into the
    framework, whether it is an end-to-end model or another type of architecture. DAIMON has been known for its vision-based
    tactile sensors that can pack over 110,000 effective sensing units. DAIMON Robotics The Technology: Monochromatic Vision-based
    Tactile Sensing You and your team have spent many years deeply engaged in vision-based tactile sensing and have developed
    the world’s first monochromatic vision-based tactile sensing technology. Why did you choose this technical path? Once
    we started investigating tactile sensors, we understood our needs. We wanted sensors that closely mimic what we have under
    our fingertip skin. Physiological studies have well documented the capabilities humans have at their fingertips — knowing
    what we touch, what kind of material it is, how forces are distributed, and whether it is moving into the right position
    as our brain controls our hands. We knew that replicating these capabilities on a robot hand’s fingertips would help considerably.
    When we surveyed existing technologies, we found many types, including vision-based tactile sensors with tri-color optics
    and other simpler designs. We decided to integrate the best of these into an engineering-robust solution that works well
    without being overly complicated, keeping cost, reliability, and sensitivity within a satisfactory range, thus ultimately
    developing a monochromatic vision-based tactile sensing technique. This is fundamentally an engineering approach rather
    than a purely scientific one, since a great deal of foundational research already existed. With the growing realization
    of the necessity of tactile data, all of this will advance hand in hand. DAIMON vision-based tactile sensor captures high-quality,
    multimodal tactile data. DAIMON Robotics Last year, DAIMON launched a multi-dimensional, high-resolution, high-frequency
    vision-based tactile sensor. Compared with traditional tactile sensors, where does its core advantage lie? Which industries
    could it potentially transform? The key features of our sensors are the density of distributed force measurement and the
    deformation we can capture over the area of a fingertip. I believe we have the highest density in terms of sensing units.
    That is one very important metric. The other is dynamics: the frequency and bandwidth — how quickly we can detect force
    changes, transmit signals, and process them in real time. Other important aspects are largely engineering-related, such
    as reliability, drift, durability of the soft surface, and resistance to interference from magnetic, optical, or environmental
    factors. A growing number of researchers and companies are recognizing the importance of tactile sensing and adopting
    our technology. I believe the advances in tactile sensing will elevate the entire community and industry to a higher level.
    One of our potential customers is deploying humanoid robots in a small convenience store, with densely packed shelves
    where shelf space is at a premium. The robot needs to reach into very tight spaces — tighter than books on a shelf — to
    pick out an object. Current two-jaw parallel grippers cannot fit into most of these spaces. Observing how humans pick
    up objects, you clearly need at least three slim fingers to touch and roll the object toward you and secure it. Thus,
    we are starting to see very specific needs where tactile sensing capabilities are essential. From Academia to Startup
    After 40 years in academia — founding the HKUST Robotics Institute, earning prestigious honors including IEEE Fellow,
    and serving as Editor-in-Chief of IEEE TASE — what motivated you to found DAIMON Robotics? I have come a long way. I started
    learning robotics during my PhD at Carnegie Mellon, where there were truly remarkable groups working on locomotion under
    Marc Raibert, who founded Boston Dynamics, and on manipulation under my advisor, Matt Mason, a leader in the field. We
    have been working on dexterous manipulation, not only at Carnegie Mellon, but globally for many years. However, progress
    has been limited for a long time, especially in building dexterous hands and making them work. Only recently have locomotion
    robots truly taken off, and only in the last few years have we begun to see major advancements in robot hands. There is
    clearly room for advancing manipulation capabilities, which would enable robots to do work like humans. While at Hong
    Kong University of Science and Technology, I saw increasingly greater people entering this area in the form of students
    and postdoctoral researchers. We wanted to jumpstart our effort by leveraging the available capital and talent resources.
    Fortunately, one of my postdocs, Dr. Duan Jianghua , has a strong sense for commercial opportunities. Recognizing the
    rapid growth of robotics market and the unique value that our vision-based tactile sensing technology could bring, together
    we started DAIMON Robotics, and it has progressed well. The community has grown tremendously in China, Japan, Korea, the
    U.S., and Europe. Robots equipped with DAIMON technology have been deployed in factory settings. The company aims to enable
    robots to achieve “embodied intelligence” and close the gap between what they can see and what they can feel. DAIMON Robotics
    Business Model and Commercial Strategy What is DAIMON’s current business model and strategic focus? What role does the
    dataset release play in your commercial strategy? We started as a device company focused on making highly capable tactile
    sensors, especially for robot hands. But as technology and business developed, everyone realized it is not just about
    one component, rather the entire technology chain: devices, data of adequate quality and quantity, and finally the right
    framework to build, train, and deploy models on robots in real application environments. Our business strategy is best
    described as “3D”: Devices, Data, and Deployment. We build devices for data collection, our own ecosystem, and for deploying
    them in our partners’ potential application domains. This enables the collection of real-world tactile-rich data and complete
    closed-loop validation. This will become an integral part of the 3D business model. Most startups in this space are following
    a similar path until eventually some may become more specialized or more tightly integrated with other companies. For
    now, it is mostly vertical integration. Embodied Skills and the Convergence Moment You’ve introduced the concept of “embodied
    skills” as essential for humanoid robots to move beyond having just an advanced AI “brain.” What prompted this insight?
    What new capabilities could embodied skills enable? After the rapid evolution of models and hardware over the past two
    years, has your definition or roadmap for embodied skills evolved? We have come a long way now see a convergence point
    where electrical, electronic, and mechatronic hardware technologies have advanced tremendously in last two decades. Robots
    are now fully electric, do not require hydraulics, because hardware has evolved rapidly. Modern electronics provide tremendous
    bandwidth with high torques. If we can build intelligence into these systems, we can create truly humanoid robots with
    the ability to operate in unstructured environments, make decisions, and take actions autonomously. “Our vision is for
    robots to achieve robust manipulation capabilities and evolve into reliable partners for humans.” —Prof. Michael Yu Wang,
    DAIMON Robotics AI has arrived at exactly the right time. Enormous resources have been invested in AI development, especially
    large language models, which are now being generalized into world models that enable physical AI capabilities. We would
    like to see these manifested in real-world systems. While both AI and core hardware technologies continue to evolve, the
    focus is much clearer now. For example, human-sized robots are preferred in a home environment. This is an exciting domain
    with a promise of great societal benefit if we can eventually achieve safe, reliable, and cost-effective robots. The Road
    to Real-World Deployment Today, many robots can deliver impressive demos, yet there remains a gap before they truly enter
    real-world applications. What could be a potential trigger for real-world deployment? Which scenarios are most likely
    to achieve large-scale deployment first? I think the road toward large-scale deployment of generalist robots is still
    long, but we are starting to see signs of feasibility within specific domains. It is very similar to autonomous vehicles,
    where we are yet to see full deployment of robo-taxis, while we have already started to find mobile robots and smaller
    vehicles widely deployed in the hospitality industry. Virtually every major hotel in China now has a delivery robot —
    no arms, just a vehicle that picks up items from the hotel lobby (e.g., food deliveries). The delivery person just loads
    the food and selects the room number. It is up to the robot thereafter to navigate and reach the guest’s room, which includes
    using the elevator, to deliver the food. This is already nearly 100 percent deployed in major Chinese hotels. Hotel and
    restaurant robots are viewed as a model for deploying humanoid robots in specific domains like overnight drugstores and
    convenience stores. I expect complete deployment in such settings within a short timeframe, followed by other applications.
    Overall, we can expect autonomous robots, including humanoids, to progressively penetrate specific sectors, delivering
    value in each and expanding into others. Ultimately, our vision is for robots to achieve robust manipulation capabilities
    and evolve into reliable partners for humans. By seamlessly integrating into our homes and daily lives, they will genuinely
    benefit and serve humanity. This interview has been edited for length and clarity.'
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
- iso
- locomotion
- manipulation
- report
- robotics
- sensor
- startup
- technology
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/daimon-robotics-physical-ai.
sources:
- id: src_001
  type: website
  title: DAIMON Robotics Wants to Give Robot Hands a Sense of Touch
  url: https://spectrum.ieee.org/daimon-robotics-physical-ai
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
A powerful embodied AI dataset will enable robots to perform dexterous manipulation This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines.

## 核心内容
This article is brought to you by DAIMON Robotics . This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang, co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief of IEEE Transactions on Automation Science and Engineering , he has spent roughly four decades in the field. His objective is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation, how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative This month, DAIMON Robotics release d the largest and most comprehensive robotic manipulation dataset with multiple leading academic institutions and enterprises. Why releas ing the dataset now, rather than continuing to focus on product development? What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics companies. As embodied AI continues to advance, the critical role of data has been clearer. Data scarcity remains a primary bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality, multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion trajectories, and natural language, transforming raw inputs into training-ready dataset for machine learning models. Recognizing the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile sensing technology and innovative data collection paradigm enable us to build large-scale dataset. Our approach is to broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its development, and how will the dataset benefit their research and products? Besides China based teams, our partners include leading research groups from universities, such as Northwestern University and the National University of Singapore, as well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong testament to the value of our tactile-rich dataset. Among the companies involved there are some that have already built their own models but are now incorporating tactile information. By deploying our data collection devices across research, manufacturing and other real-world scenarios, they help us to gather highly practical, application-driven data. In turn, our partners leverage the data to train models tailored to their specific use cases. Furthermore, to drive the advancement of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community. Equipped with Daimon’s visuotactile sensor, the gripper delicately senses contact and precisely controls force to pick up a fragile eggshell. Daimon Robotics From VLA to VTLA: Why Tactile Sensing Changes the Equation The mainstream paradigm in robotics is currently the Vision-Language-Action (VLA) model, but your team has proposed a Vision-Tactile-Language-Action (VTLA) model. Why is it necessary to incorporate tactile sensing? What does it enable robots to achieve, and which tasks are likely to fail without tactile feedback? Over these years of working to make generalist robots capable of performing manipulation tasks, especially dexterous manipulation — not just power grasping or holding an object, but manipulating objects and using tools to impart forces and motion onto parts — we see these robots being used in household as well as industrial assembly settings. It is well established that tactile information is essential for providing feedback about contact states so that robots can guide their hands and fingers to perform reliable manipulation. Without tactile sensing, robots are severely limited. They struggle to locate objects in dark environments, and without slip detection, they can easily drop fragile items like glass. Furthermore, the inability to precisely control force often leads to failed manipulation tasks or, in severe cases, physical damage. Naturally, the VLA approach needs to be enhanced to incorporate tactile information. We expanded the VLA framework to incorporate tactile data, creating the VTLA model. An additional benefit of our tactile sensor is that it is vision-based: We capture visual images of the deformation on the fingertip surface. We capture multiple images in a time sequence that encodes contact information, from which we can infer forces and other contact states. This aligns well with the visual framework that VLA is based upon. Having tactile information in a visual image format makes it naturally suitable for integration into the VLA framework, transforming it into a VTLA system. That is the key advantage: Vision-based tactile sensors provide very high resolution at the pixel level, and this data can be incorporated into the framework, whether it is an end-to-end model or another type of architecture. DAIMON has been known for its vision-based tactile sensors that can pack over 110,000 effective sensing units. DAIMON Robotics The Technology: Monochromatic Vision-based Tactile Sensing You and your team have spent many years deeply engaged in vision-based tactile sensing and have developed the world’s first monochromatic vision-based tactile sensing technology. Why did you choose this technical path? Once we started investigating tactile sensors, we understood our needs. We wanted sensors that closely mimic what we have under our fingertip skin. Physiological studies have well documented the capabilities humans have at their fingertips — knowing what we touch, what kind of material it is, how forces are distributed, and whether it is moving into the right position as our brain controls our hands. We knew that replicating these capabilities on a robot hand’s fingertips would help considerably. When we surveyed existing technologies, we found many types, including vision-based tactile sensors with tri-color optics and other simpler designs. We decided to integrate the best of these into an engineering-robust solution that works well without being overly complicated, keeping cost, reliability, and sensitivity within a satisfactory range, thus ultimately developing a monochromatic vision-based tactile sensing technique. This is fundamentally an engineering approach rather than a purely scientific one, since a great deal of foundational research already existed. With the growing realization of the necessity of tactile data, all of this will advance hand in hand. DAIMON vision-based tactile sensor captures high-quality, multimodal tactile data. DAIMON Robotics Last year, DAIMON launched a multi-dimensional, high-resolution, high-frequency vision-based tactile sensor. Compared with traditional tactile sensors, where does its core advantage lie? Which industries could it potentially transform? The key features of our sensors are the density of distributed force measurement and the deformation we can capture over the area of a fingertip. I believe we have the highest density in terms of sensing units. That is one very important metric. The other is dynamics: the frequency and bandwidth — how quickly we can detect force changes, transmit signals, and process them in real time. Other important aspects are largely engineering-related, such as reliability, drift, durability of the soft surface, and resistance to interference from magnetic, optical, or environmental factors. A growing number of researchers and companies are recognizing the importance of tactile sensing and adopting our technology. I believe the advances in tactile sensing will elevate the entire community and industry to a higher level. One of our potential customers is deploying humanoid robots in a small convenience store, with densely packed shelves where shelf space is at a premium. The robot needs to reach into very tight spaces — tighter than books on a shelf — to pick out an object. Current two-jaw parallel grippers cannot fit into most of these spaces. Observing how humans pick up objects, you clearly need at least three slim fingers to touch and roll the object toward you and secure it. Thus, we are starting to see very specific needs where tactile sensing capabilities are essential. From Academia to Startup After 40 years in academia — founding the HKUST Robotics Institute, earning prestigious honors including IEEE Fellow, and serving as Editor-in-Chief of IEEE TASE — what motivated you to found DAIMON Robotics? I have come a long way. I started learning robotics during my PhD at Carnegie Mellon, where there were truly remarkable groups working on locomotion under Marc Raibert, who founded Boston Dynamics, and on manipulation under my advisor, Matt Mason, a leader in the field. We have been working on dexterous manipulation, not only at Carnegie Mellon, but globally for many years. However, progress has been limited for a long time, especially in building dexterous hands and making them work. Only recently have locomotion robots truly taken off, and only in the last few years have we begun to see major advancements in robot hands. There is clearly room for advancing manipulation capabilities, which would enable robots to do work like humans. While at Hong Kong University of Science and Technology, I saw increasingly greater people entering this area in the form of students and postdoctoral researchers. We wanted to jumpstart our effort by leveraging the available capital and talent resources. Fortunately, one of my postdocs, Dr. Duan Jianghua , has a strong sense for commercial opportunities. Recognizing the rapid growth of robotics market and the unique value that our vision-based tactile sensing technology could bring, together we started DAIMON Robotics, and it has progressed well. The community has grown tremendously in China, Japan, Korea, the U.S., and Europe. Robots equipped with DAIMON technology have been deployed in factory settings. The company aims to enable robots to achieve “embodied intelligence” and close the gap between what they can see and what they can feel. DAIMON Robotics Business Model and Commercial Strategy What is DAIMON’s current business model and strategic focus? What role does the dataset release play in your commercial strategy? We started as a device company focused on making highly capable tactile sensors, especially for robot hands. But as technology and business developed, everyone realized it is not just about one component, rather the entire technology chain: devices, data of adequate quality and quantity, and finally the right framework to build, train, and deploy models on robots in real application environments. Our business strategy is best described as “3D”: Devices, Data, and Deployment. We build devices for data collection, our own ecosystem, and for deploying them in our partners’ potential application domains. This enables the collection of real-world tactile-rich data and complete closed-loop validation. This will become an integral part of the 3D business model. Most startups in this space are following a similar path until eventually some may become more specialized or more tightly integrated with other companies. For now, it is mostly vertical integration. Embodied Skills and the Convergence Moment You’ve introduced the concept of “embodied skills” as essential for humanoid robots to move beyond having just an advanced AI “brain.” What prompted this insight? What new capabilities could embodied skills enable? After the rapid evolution of models and hardware over the past two years, has your definition or roadmap for embodied skills evolved? We have come a long way now see a convergence point where electrical, electronic, and mechatronic hardware technologies have advanced tremendously in last two decades. Robots are now fully electric, do not require hydraulics, because hardware has evolved rapidly. Modern electronics provide tremendous bandwidth with high torques. If we can build intelligence into these systems, we can create truly humanoid robots with the ability to operate in unstructured environments, make decisions, and take actions autonomously. “Our vision is for robots to achieve robust manipulation capabilities and evolve into reliable partners for humans.” —Prof. Michael Yu Wang, DAIMON Robotics AI has arrived at exactly the right time. Enormous resources have been invested in AI development, especially large language models, which are now being generalized into world models that enable physical AI capabilities. We would like to see these manifested in real-world systems. While both AI and core hardware technologies continue to evolve, the focus is much clearer now. For example, human-sized robots are preferred in a home environment. This is an exciting domain with a promise of great societal benefit if we can eventually achieve safe, reliable, and cost-effective robots. The Road to Real-World Deployment Today, many robots can deliver impressive demos, yet there remains a gap before they truly enter real-world applications. What could be a potential trigger for real-world deployment? Which scenarios are most likely to achieve large-scale deployment first? I think the road toward large-scale deployment of generalist robots is still long, but we are starting to see signs of feasibility within specific domains. It is very similar to autonomous vehicles, where we are yet to see full deployment of robo-taxis, while we have already started to find mobile robots and smaller vehicles widely deployed in the hospitality industry. Virtually every major hotel in China now has a delivery robot — no arms, just a vehicle that picks up items from the hotel lobby (e.g., food deliveries). The delivery person just loads the food and selects the room number. It is up to the robot thereafter to navigate and reach the guest’s room, which includes using the elevator, to deliver the food. This is already nearly 100 percent deployed in major Chinese hotels. Hotel and restaurant robots are viewed as a model for deploying humanoid robots in specific domains like overnight drugstores and convenience stores. I expect complete deployment in such settings within a short timeframe, followed by other applications. Overall, we can expect autonomous robots, including humanoids, to progressively penetrate specific sectors, delivering value in each and expanding into others. Ultimately, our vision is for robots to achieve robust manipulation capabilities and evolve into reliable partners for humans. By seamlessly integrating into our homes and daily lives, they will genuinely benefit and serve humanity. This interview has been edited for length and clarity. A powerful embodied AI dataset will enable robots to perform dexterous manipulation This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project is supported by collaborative efforts of partners across China and the globe, including Google DeepMind , Northwestern University, and the National University of Singapore.

## 参考
- https://spectrum.ieee.org/daimon-robotics-physical-ai
