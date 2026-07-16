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

## Overview
A powerful embodied AI dataset will enable robots to perform dexterous manipulation. This April, Hong Kong-based DAIMON Robotics released Daimon-Infinity, which it describes as the largest omni-modal robotic dataset for physical AI, featuring high-resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines.

## Content
This article is brought to you by DAIMON Robotics. This April, Hong Kong-based DAIMON Robotics released Daimon-Infinity, which it describes as the largest omni-modal robotic dataset for physical AI, featuring high-resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang, co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief of *IEEE Transactions on Automation Science and Engineering*, he has spent roughly four decades in the field. His objective is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation, how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative This month, DAIMON Robotics released the largest and most comprehensive robotic manipulation dataset with multiple leading academic institutions and enterprises. Why release the dataset now, rather than continuing to focus on product development? What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics companies. As embodied AI continues to advance, the critical role of data has become clearer. Data scarcity remains a primary bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality, multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion trajectories, and natural language, transforming raw inputs into training-ready datasets for machine learning models. Recognizing the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile sensing technology and innovative data collection paradigm enable us to build large-scale datasets. Our approach is to broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its development, and how will the dataset benefit their research and products? Besides China-based teams, our partners include leading research groups from universities, such as Northwestern University and the National University of Singapore, as well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong testament to the value of our tactile-rich dataset. Among the companies involved, there are some that have already built their own models but are now incorporating tactile information. By deploying our data collection

## 개요  
강력한 임베디드 AI 데이터셋은 로봇이 정밀한 조작을 수행할 수 있게 해줍니다. 올해 4월, 홍콩에 본사를 둔 DAIMON Robotics는 물리적 AI를 위한 가장 큰 전모달 로봇 데이터셋이라고 설명하는 Daimon-Infinity를 출시했습니다. 이 데이터셋은 고해상도 촉각 감지를 특징으로 하며, 집에서 빨래 개기부터 공장 조립 라인에서의 제조까지 다양한 작업을 포괄합니다.

## 핵심 내용  
이 기사는 DAIMON Robotics가 제공합니다. 올해 4월, 홍콩에 본사를 둔 DAIMON Robotics는 물리적 AI를 위한 가장 큰 전모달 로봇 데이터셋이라고 설명하는 Daimon-Infinity를 출시했습니다. 이 데이터셋은 고해상도 촉각 감지를 특징으로 하며, 집에서 빨래 개기부터 공장 조립 라인에서의 제조까지 다양한 작업을 포괄합니다. 이 프로젝트는 Google DeepMind, 노스웨스턴 대학교, 싱가포르 국립 대학교를 포함한 중국 및 전 세계 파트너들의 협력 노력으로 지원됩니다. 이 움직임은 2년 반 된 회사로, 고급 촉각 센서 하드웨어, 특히 손가락 끝 크기의 모듈에 110,000개 이상의 유효 감지 유닛을 탑재한 단색 비전 기반 촉각 센서로 유명한 DAIMON의 주요 전략적 이니셔티브를 나타냅니다. 고해상도 촉각 감지 기술과 연간 수백만 시간의 데이터를 생성할 수 있는 분산형 실외 수집 네트워크를 활용하여 DAIMON은 방대한 양의 촉각 감지 데이터를 포함하는 대규모 로봇 조작 데이터셋을 구축하고 있습니다. 임베디드 AI의 실제 배포를 가속화하기 위해 회사는 10,000시간의 데이터를 오픈소스로 공개했습니다. DAIMON Robotics의 공동 창립자이자 수석 과학자인 Michael Yu Wang 교수는 Vision-Tactile-Language-Action(VTLA) 아키텍처를 개척하여 촉각을 시각과 동등한 모달리티로 격상시켰습니다.  
DAIMON Robotics  
이 전략 뒤에는 DAIMON의 공동 창립자이자 수석 과학자인 Michael Yu Wang 교수가 있습니다. Wang 교수는 카네기 멜론 대학교에서 Matt Mason 밑에서 조작을 연구하며 박사 학위를 받았고, 이후 홍콩 과학 기술 대학교에 로봇 공학 연구소를 설립했습니다. IEEE 펠로우이자 IEEE Transactions on Automation Science and Engineering의 전 편집장으로서, 그는 이 분야에서 약 40년을 보냈습니다. 그의 목표는 주로 Vision-Language-Action(VLA) 모델에 의존하는 로봇 조작의 "둔감함" 문제를 해결하는 것입니다. 그와 그의 팀은 Vision-Tactile-Language-Action(VTLA) 아키텍처를 개척하여 촉각을 시각과 동등한 모달리티로 격상시켰습니다. 우리는 Wang 교수와 촉각 피드백이 정밀 조작을 어떻게 변화시키려는지, 데이터셋 이니셔티브가 자연 환경에서 로봇 손에 대한 이해를 어떻게 개선할 것으로 예상되는지, 그리고 중국의 호텔과 편의점에서 촉각 지원 로봇이 처음으로 실제 진출을 할 곳에 대해 이야기했습니다.  
Daimon-Infinity는 물리적 AI를 위한 세계 최대의 전모달 데이터셋으로, 백만 시간 규모의 멀티모달 데이터, 초고해상도 촉각 피드백, 80개 이상의 실제 시나리오와 2,000개 이상의 인간 기술 데이터 등을 특징으로 합니다.  
DAIMON Robotics  
데이터셋 이니셔티브  
이번 달, DAIMON Robotics는 여러 주요 학술 기관 및 기업과 함께 가장 크고 포괄적인 로봇 조작 데이터셋을 출시했습니다. 왜 제품 개발에 계속 집중하지 않고 지금 데이터셋을 출시했습니까? 이것이 임베디드 지능 산업에 어떤 영향을 미칠까요?  
DAIMON Robotics는 거의 2년 반 동안 운영되어 왔습니다. 우리는 로봇 손(특히 손가락 끝)과 물체 간의 상호 작용을 감지하기 위해 고해상도 멀티모달 촉각 감지 장치를 개발하는 데 전념해 왔습니다. 우리의 장치는 상당히 견고해졌습니다. 현재 학술 및 연구 기관, 주요 휴머노이드 로봇 회사를 포함한 많은 사용자들이 이를 수용하고 사용하고 있습니다. 임베디드 AI가 계속 발전함에 따라 데이터의 중요한 역할이 더욱 명확해졌습니다. 데이터 부족은 로봇 학습의 주요 병목 현상으로 남아 있으며, 특히 로봇이 실제 세계에서 효과적으로 작동하는 데 필수적인 물리적 상호 작용 데이터의 부족이 두드러집니다. 결과적으로 데이터 품질, 신뢰성 및 비용은 연구 및 상업 개발 모두에서 주요 관심사가 되었습니다. 이것이 바로 DAIMON이 뛰어난 분야입니다. 우리의 비전 기반 촉각 기술은 고품질의 멀티모달 촉각 데이터를 포착합니다. 기본 접촉 힘을 넘어 변형, 미끄러짐 및 마찰, 재료 특성 및 표면 질감을 기록하여 물리적 상호 작용의 포괄적인 재구성을 가능하게 합니다. 멀티모달 융합에 대한 전문성을 바탕으로 우리는 촉각 피드백을 시각, 운동 궤적 및 자연어와 원활하게 통합하여 원시 입력을 기계 학습 모델을 위한 훈련 준비 데이터셋으로 변환하는 강력한 데이터 처리 파이프라인을 개발했습니다. 업계 전반의 데이터 격차를 인식하여 우리는 대규모 데이터 수집을 독특한 경쟁 우위뿐만 아니라 더 넓은 커뮤니티에 대한 책임으로 봅니다. 데이터셋을 구축하고 오픈소스화함으로써 우리는 임베디드 AI에 필요한 고품질 "연료"를 제공하여 궁극적으로 범용 로봇 기반 모델의 실제 배포를 가속화하는 것을 목표로 합니다.  
로봇 공학 산업은 매우 경쟁적이며, 많은 팀이 데이터에 집중하기로 선택했습니다. DAIMON은 크고 매우 포괄적인 교차 체형, 비전 기반 촉각 멀티모달 로봇 조작 데이터셋을 출시하고 있습니다. 어떻게 이것을 달성할 수 있었습니까?  
우리는 하드웨어 장치 구축 및 자체 대규모 모델 개발을 포함한 역량 확장에 전념하는 전담 사내 팀을 보유하고 있습니다. 비교적 작은 회사이지만, 우리의 핵심 촉각 감지 기술과 혁신적인 데이터 수집 패러다임을 통해 대규모 데이터셋을 구축할 수 있습니다. 우리의 접근 방식은 제공 범위를 확장하는 것입니다. 우리는 세계 최대의 분산형 실외 데이터 수집 네트워크를 구축했습니다. 중앙 집중식 데이터 공장에 의존하지 않고 이 가볍고 확장 가능한 시스템은 다양한 실제 환경에서 데이터를 수집할 수 있게 하여 연간 수백만 시간의 데이터를 생성할 수 있습니다.  
"전체 임베디드 AI 분야의 발전을 촉진하기 위해 우리는 더 넓은 커뮤니티를 위해 데이터셋의 10,000시간을 오픈소스화했습니다." —Michael Yu Wang 교수, DAIMON Robotics  
이 데이터셋은 전 세계 여러 기관과 공동으로 개발되고 있습니다. 그들은 개발에서 어떤 역할을 했으며, 데이터셋이 그들의 연구와 제품에 어떻게 도움이 될까요?  
중국 기반 팀 외에도 우리의 파트너에는 노스웨스턴 대학교와 싱가포르 국립 대학교 같은 대학의 주요 연구 그룹, 그리고 Google DeepMind와 중국 모바일 같은 글로벌 선도 기업이 포함됩니다. 그들이 DAIMON과 파트너십을 맺기로 한 결정은 우리의 촉각 풍부 데이터셋의 가치를 강력히 증명합니다. 관련된 회사 중에는 이미 자체 모델을 구축했지만 이제 촉각 정보를 통합하고 있는 곳도 있습니다. 우리의 데이터 수집을 배포함으로써
