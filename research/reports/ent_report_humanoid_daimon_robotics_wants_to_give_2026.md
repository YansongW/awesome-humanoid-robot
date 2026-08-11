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
  zh: 香港公司DAIMON Robotics于2025年4月发布了Daimon-Infinity，号称是物理AI领域最大的全模态机器人数据集，涵盖从家庭叠衣到工厂装配线等多种任务。该项目由Google DeepMind、西北大学和新加坡国立大学等全球合作伙伴支持，并开源了10,000小时数据。公司联合创始人兼首席科学家王煜教授提出了Vision-Tactile-Language-Action
    (VTLA)架构，将触觉提升到与视觉同等重要的模态。
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
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/daimon-robotics-physical-ai.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1804 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: DAIMON Robotics Wants to Give Robot Hands a Sense of Touch
  url: https://spectrum.ieee.org/daimon-robotics-physical-ai
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
DAIMON Robotics是一家成立两年半的公司，以其先进的触觉传感器硬件闻名，特别是单色视觉触觉传感器，能在指尖大小的模块中集成超过110,000个有效传感单元。公司利用高分辨率触觉传感技术和分布式实验室外数据采集网络，每年可生成数百万小时的数据，构建包含大量触觉数据的大规模机器人操作数据集。王煜教授在卡内基梅隆大学获得博士学位，师从Matt Mason，后创立香港科技大学机器人研究所，拥有约四十年领域经验。他主导的VTLA架构旨在解决当前主流Vision-Language-Action (VLA)模型在机器人操作中缺乏触觉感知的问题，使机器人能更可靠地执行精细操作。

## 核心内容
### 数据集倡议
DAIMON Robotics与多家顶尖学术机构和企业合作，发布了最大、最全面的机器人操作数据集。公司认为数据稀缺是机器人学习的主要瓶颈，尤其是物理交互数据的缺乏。其视觉触觉技术不仅能捕捉基本接触力，还能记录变形、滑动与摩擦、材料属性和表面纹理，实现物理交互的全面重建。公司开发了稳健的数据处理管道，将触觉反馈与视觉、运动轨迹和自然语言无缝集成，将原始输入转化为机器学习模型可用的训练数据集。DAIMON已建成全球最大的分布式实验室外数据采集网络，每年可生成数百万小时的数据。为推动整个具身AI领域的发展，公司开源了10,000小时的数据集。

### 从VLA到VTLA：触觉感知改变规则
当前机器人领域的主流范式是Vision-Language-Action (VLA)模型，但DAIMON团队提出了Vision-Tactile-Language-Action (VTLA)模型。触觉信息对于提供接触状态反馈至关重要，使机器人能引导手和手指执行可靠操作。没有触觉感知，机器人在黑暗环境中定位物体困难，缺乏滑动检测容易掉落易碎物品，无法精确控制力常导致操作失败或物理损坏。DAIMON的触觉传感器基于视觉，能捕捉指尖表面变形的视觉图像，通过时间序列图像编码接触信息，可推断力和其他接触状态。这种视觉图像格式的触觉信息天然适合集成到VLA框架中，转化为VTLA系统。

### 技术：单色视觉触觉感知
DAIMON开发了全球首个单色视觉触觉传感技术，旨在模拟人类指尖皮肤下的感知能力。其传感器核心优势在于分布式力测量的密度和指尖区域变形的捕捉能力，拥有最高的传感单元密度。动态性能方面，传感器能快速检测力变化、传输信号并实时处理。其他重要工程特性包括可靠性、漂移、软表面耐久性以及抗磁、光或环境干扰能力。一个潜在客户正在便利店部署人形机器人，需要在密集货架间的狭小空间取物，这需要至少三个细长手指来触摸和滚动物体，凸显了触觉感知能力的必要性。

### 从学术界到创业
王煜教授在卡内基梅隆大学攻读博士期间开始学习机器人学，后在香港科技大学创立机器人研究所。他与博士后段江华博士共同创立DAIMON Robotics，利用资本和人才资源推动触觉传感技术的商业化。配备DAIMON技术的机器人已在工厂环境中部署，公司目标是使机器人实现“具身智能”，缩小视觉与触觉之间的差距。

### 商业模式与商业策略
DAIMON的商业模式可概括为“3D”：Devices（设备）、Data（数据）和Deployment（部署）。公司构建用于数据收集的设备、自有生态系统，并在合作伙伴的潜在应用领域部署，实现真实世界触觉丰富数据的收集和完整的闭环验证。

### 具身技能与融合时刻
王煜教授提出“具身技能”概念，认为人形机器人需要超越先进的AI“大脑”。过去二十年，电气、电子和机电硬件技术飞速发展，机器人已完全电动化。AI的发展，特别是大语言模型，正被泛化为世界模型，使物理AI能力成为可能。家庭环境中更偏好人类尺寸的机器人，这是一个令人兴奋的领域，有望实现安全、可靠且成本效益高的机器人。

### 真实世界部署之路
通用机器人的大规模部署道路仍然漫长，但特定领域已出现可行性迹象。中国几乎所有主要酒店都已部署配送机器人（无手臂，仅车辆），负责从大堂取物品并导航到客房。酒店和餐厅机器人被视为在特定领域（如夜间药店和便利店）部署人形机器人的模型。预计这些场景将在短期内实现完全部署，随后扩展到其他应用。最终愿景是机器人获得稳健的操作能力，演变为人类的可靠伙伴，无缝融入家庭和日常生活。

## Overview
A powerful embodied AI dataset will enable robots to perform dexterous manipulation This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines.

This article is brought to you by DAIMON Robotics . This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang, co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief of IEEE Transactions on Automation Science and Engineering , he has spent roughly four decades in the field. His objective is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation, how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative This month, DAIMON Robotics release d the largest and most comprehensive robotic manipulation dataset with multiple leading academic institutions and enterprises. Why releas ing the dataset now, rather than continuing to focus on product development? What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics companies. As embodied AI continues to advance, the critical role of data has been clearer. Data scarcity remains a primary bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality, multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion trajectories, and natural language, transforming raw inputs into training-ready dataset for machine learning models. Recognizing the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile sensing technology and innovative data collection paradigm enable us to build large-scale dataset. Our approach is to broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its development, and how will the dataset benefit their research and products? Besides China based teams, our partners include leading research groups from universities, such as Northwestern University and the National University of Singapore, as well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong testament to the value of our tactile-rich dataset. Among the companies involved there are some that have already built their own models but are now incorporating tactile information. By deploying our data collection devices across research, manufacturing and other real-world scenarios, they help us to gather highly practical, application-driven data. In turn, our partners leverage the data to train models tailored to their specific use cases. Furthermore, to drive the advancement of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community. Equipped with Daimon’s visuotactile sensor, the gripper delicately senses contact and precisely controls force to pick up a fragile eggshell. Daimon Robotics From VLA to VTLA: Why Tactile Sensing Changes the Equation The mainstream paradigm in robotics is currently the Vision-Language-Action (VLA) model, but your team has proposed a Vision-Tactile-Language-Action (VTLA) model. Why is it necessary to incorporate tactile sensing? What does it enable robots to achieve, and which tasks are likely to fail without tactile feedback? Over these years of working to make generalist robots capable of performing manipulation tasks, especially dexterous manipulation — not just power grasping or holding an object, but manipulating objects and using tools to impart forces and motion onto parts — we see these robots being used in household as well as industrial assembly settings. It is well established that tactile information is essential for providing feedback about contact states so that robots can guide their hands and fingers to perform reliable manipulation. Without tactile sensing, robots are severely limited. They struggle to locate objects in dark environments, and without slip detection, they can easily drop fragile items like glass. Furthermore, the inability to precisely control force often leads to failed manipulation tasks or, in severe cases, physical damage. Naturally, the VLA approach needs to be enhanced to incorporate tactile information. We expanded the VLA framework to incorporate tactile data, creating the VTLA model. An additional benefit of our tactile sensor is that it is vision-based: We capture visual images of the deformation on the fingertip surface. We capture multiple images in a time sequence that encodes contact information, from which we can infer forces and other contact states. This aligns well with the visual framework that VLA is based upon. Having tactile information in a visual image format makes it naturally suitable for integration into the VLA framework, transforming it into a VTLA system. That is the key advantage: Vision-based tactile sensors provide very high resolution at the pixel level, and this data can be incorporated into the framework, whether it is an end-to-end model or another type of architecture. DAIMON has been known for its vision-based tactile sensors that can pack over 110,000 effective sensing units. DAIMON Robotics The Technology: Monochromatic Vision-based Tactile Sensing You and your team have spent many years deeply engaged in vision-based tactile sensing and have developed the world’s first monochromatic vision-based tactile sensing technology. Why did you choose this technical path? Once we started investigating tactile sensors, we understood our needs. We wanted sensors that closely mimic what we have under our fingertip skin. Physiological studies have well documented the capabilities humans have at their fingertips — knowing what we touch, what kind of material it is, how forces are distributed, and whether it is moving into the right position as our brain controls our hands. We knew that replicating these capabilities on a robot hand’s fingertips would help considerably. When we surveyed existing technologies, we found many types, including vision-based tactile sensors with tri-color optics and other simpler designs. We decided to integrate the best of these into an engineering-robust solution that works well without being overly complicated, keeping cost, reliability, and sensitivity within a satisfactory range, thus ultimately developing a monochromatic vision-based tactile sensing technique. This is fundamentally an engineering approach rather than a purely scientific one, since a great deal of foundational research already existed. With the growing realization of the necessity of tactile data, all of this will advance hand in hand. DAIMON vision-based tactile sensor captures high-quality, multimodal tactile data. DAIMON Robotics Last year, DAIMON launched a multi-dimensional, high-resolution, high-frequency vision-based tactile sensor. Compared with traditional tactile sensors, where does its core advantage lie? Which industries could it potentially transform? The key features of our sensors are the density of distributed force measurement and the deformation we can capture over the area of a fingertip. I believe we have the highest density in terms of sensing units. That is one very important metric. The other is dynamics: the frequency and bandwidth — how quickly we can detect force changes, transmit signals, and process them in real time. Other important aspects are largely engineering-related, such as reliability, drift, durability of the soft surface, and resistance to interference from magnetic, optical, or environmental factors. A growing number of researchers and companies are recognizing the importance of tactile sensing and adopting our technology. I believe the advances in tactile sensing will elevate the entire community and industry to a higher level. One of our potential customers is deploying humanoid robots in a small convenience store, with densely packed shelves where shelf space is at a premium. The robot needs to reach into very tight spaces — tighter than books on a shelf — to pick out an object. Current two-jaw parallel grippers cannot fit into most of these spaces. Observing how humans pick up objects, you clearly need at least three slim fingers to touch and roll the object toward you and secure it. Thus, we are starting to see very specific needs where tactile sensing capabilities are essential. From Academia to Startup After 40 years in academia — founding the HKUST Robotics Institute, earning prestigious honors including IEEE Fellow, and serving as Editor-in-Chief of IEEE TASE — what motivated you to found DAIMON Robotics? I have come a long way. I started learning robotics during my PhD at Carnegie Mellon, where there were truly remarkable groups working on locomotion under Marc Raibert, who founded Boston Dynamics, and on manipulation under my advisor, Matt Mason, a leader in the field. We have been working on dexterous manipulation, not only at Carnegie Mellon, but globally for many years. However, progress has been limited for a long time, especially in building dexterous hands and making them work. Only recently have locomotion robots truly taken off, and only in the last few years have we begun to see major advancements in robot hands. There is clearly room for advancing manipulation capabilities, which would enable robots to do work like humans. While at Hong Kong University of Science and Technology, I saw increasingly greater people entering this area in the form of students and postdoctoral researchers. We wanted to jumpstart our effort by leveraging the available capital and talent resources. Fortunately, one of my postdocs, Dr. Duan Jianghua , has a strong sense for commercial opportunities. Recognizing the rapid growth of robotics market and the unique value that our vision-based tactile sensing technology could bring, together we started DAIMON Robotics, and it has progressed well. The community has grown tremendously in China, Japan, Korea, the U.S., and Europe. Robots equipped with DAIMON technology have been deployed in factory settings. The company aims to enable robots to achieve “embodied intelligence” and close the gap between what they can see and what they can feel. DAIMON Robotics Business Model and Commercial Strategy What is DAIMON’s current business model and strategic focus? What role does the dataset release play in your commercial strategy? We started as a device company focused on making highly capable tactile sensors, especially for robot hands. But as technology and business developed, everyone realized it is not just about one component, rather the entire technology chain: devices, data of adequate quality and quantity, and finally the right framework to build, train, and deploy models on robots in real application environments. Our business strategy is best described as “3D”: Devices, Data, and Deployment. We build devices for data collection, our own ecosystem, and for deploying them in our partners’ potential application domains. This enables the collection of real-world tactile-rich data and complete closed-loop validation. This will become an integral part of the 3D business model. Most startups in this space are following a similar path until eventually some may become more specialized or more tightly integrated with other companies. For now, it is mostly vertical integration. Embodied Skills and the Convergence Moment You’ve introduced the concept of “embodied skills” as essential for humanoid robots to move beyond having just an advanced AI “brain.” What prompted this insight? What new capabilities could embodied skills enable? After the rapid evolution of models and hardware over the past two years, has your definition or roadmap for embodied skills evolved? We have come a long way now see a convergence point where electrical, electronic, and mechatronic hardware technologies have advanced tremendously in last two decades. Robots are now fully electric, do not require hydraulics, because hardware has evolved rapidly. Modern electronics provide tremendous bandwidth with high torques. If we can build intelligence into these systems, we can create truly humanoid robots with the ability to operate in unstructured environments, make decisions, and take actions autonomously. “Our vision is for robots to achieve robust manipulation capabilities and evolve into reliable partners for humans.” —Prof. Michael Yu Wang, DAIMON Robotics AI has arrived at exactly the right time. Enormous resources have been invested in AI development, especially large language models, which are now being generalized into world models that enable physical AI capabilities. We would like to see these manifested in real-world systems. While both AI and core hardware technologies continue to evolve, the focus is much clearer now. For example, human-sized robots are preferred in a home environment. This is an exciting domain with a promise of great societal benefit if we can eventually achieve safe, reliable, and cost-effective robots. The Road to Real-World Deployment Today, many robots can deliver impressive demos, yet there remains a gap before they truly enter real-world applications. What could be a potential trigger for real-world deployment? Which scenarios are most likely to achieve large-scale deployment first? I think the road toward large-scale deployment of generalist robots is still long, but we are starting to see signs of feasibility within specific domains. It is very similar to autonomous vehicles, where we are yet to see full deployment of robo-taxis, while we have already started to find mobile robots and smaller vehicles widely deployed in the hospitality industry. Virtually every major hotel in China now has a delivery robot — no arms, just a vehicle that picks up items from the hotel lobby (e.g., food deliveries). The delivery person just loads the food and selects the room number. It is up to the robot thereafter to navigate and reach the guest’s room, which includes using the elevator, to deliver the food. This is already nearly 100 percent deployed in major Chinese hotels. Hotel and restaurant robots are viewed as a model for deploying humanoid robots in specific domains like overnight drugstores and convenience stores. I expect complete deployment in such settings within a short timeframe, followed by other applications. Overall, we can expect autonomous robots, including humanoids, to progressively penetrate specific sectors, delivering value in each and expanding into others. Ultimately, our vision is for robots to achieve robust manipulation capabilities and evolve into reliable partners for humans. By seamlessly integrating into our homes and daily lives, they will genuinely benefit and serve humanity. This interview has been edited for length and clarity. A powerful embodied AI dataset will enable robots to perform dexterous manipulation This April, Hong Kong-based DAIMON Robotics has released Daimon-Infinity , which it describes as the largest omni-modal robotic dataset for physical AI, featuring high resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project is supported by collaborative efforts of partners across China and the globe, including Google DeepMind , Northwestern University, and the National University of Singapore.

## Overview
A powerful embodied AI dataset will enable robots to perform dexterous manipulation. This April, Hong Kong-based DAIMON Robotics released Daimon-Infinity, which it describes as the largest omni-modal robotic dataset for physical AI, featuring high-resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines.

## Content
This article is brought to you by DAIMON Robotics. This April, Hong Kong-based DAIMON Robotics released Daimon-Infinity, which it describes as the largest omni-modal robotic dataset for physical AI, featuring high-resolution tactile sensing and spanning a wide range of tasks from folding laundry at home to manufacturing on factory assembly lines. The project is supported by collaborative efforts of partners across China and the globe, including Google DeepMind, Northwestern University, and the National University of Singapore. The move signals a key strategic initiative for DAIMON, a two-and-a-half-year-old company known for its advanced tactile sensor hardware, most notably a monochromatic, vision-based tactile sensor that packs over 110,000 effective sensing units into a fingertip-sized module. Drawing on its high-resolution tactile sensing technology and a distributed out-of-lab collection network capable of generating millions of hours of data annually, DAIMON is building large-scale robot manipulation datasets that include vast amounts of tactile sensing data. To accelerate the real-world deployment of embodied AI, the company has also open-sourced 10,000 hours of its data. Prof. Michael Yu Wang, co-founder and chief scientist at DAIMON Robotics, has pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. DAIMON Robotics Behind the strategy is Prof. Michael Yu Wang, DAIMON’s co-founder and chief scientist. Prof. Wang earned his PhD at Carnegie Mellon — studying manipulation under Matt Mason — and went on to found the Robotics Institute at the Hong Kong University of Science and Technology. An IEEE Fellow and former Editor-in-Chief of *IEEE Transactions on Automation Science and Engineering*, he has spent roughly four decades in the field. His objective is to address the missing “insensitivity” of robot manipulation, which practically relies on the dominant Vision-Language-Action (VLA) model. He and his team have pioneered Vision-Tactile-Language-Action (VTLA) architecture, elevating the tactile to a modality on par with vision. We spoke with Prof. Wang about how tactile feedback aims to change dexterous manipulation, how the dataset initiative is foreseen to improve our understanding of robotic hands in natural environments, and where — from hotels to convenience stores in China — he sees touch-enabled robots making their first real-world inroads. Daimon-Infinity is the world’s largest omni-modal dataset for Physical AI, featuring million-hour scale multimodal data, ultra-high-res tactile feedback, data from 80+ real scenarios and 2,000+ human skills, and more. DAIMON Robotics The Dataset Initiative This month, DAIMON Robotics released the largest and most comprehensive robotic manipulation dataset with multiple leading academic institutions and enterprises. Why release the dataset now, rather than continuing to focus on product development? What impact will this have on the embodied intelligence industry? DAIMON Robotics has been around for almost two and a half years. We have been committed to developing high-resolution, multimodal tactile sensing devices to perceive the interaction between a robot’s hand (particularly its fingertips) and objects. Our devices have become quite robust. They are now accepted and used by a large segment of users, including academic and research institutes as well as leading humanoid robotics companies. As embodied AI continues to advance, the critical role of data has become clearer. Data scarcity remains a primary bottleneck in robot learning, particularly the lack of physical interaction data, which is essential for robots to operate effectively in the real world. Consequently, data quality, reliability, and cost have become major concerns in both research and commercial development. This is exactly where DAIMON excels. Our vision-based tactile technology captures high-quality, multimodal tactile data. Beyond basic contact forces, it records deformation, slip and friction, material properties and surface textures — enabling a comprehensive reconstruction of physical interactions. Building on our expertise in multimodal fusion, we have developed a robust data processing pipeline that seamlessly integrates tactile feedback with vision, motion trajectories, and natural language, transforming raw inputs into training-ready datasets for machine learning models. Recognizing the industry-wide data gap, we view large-scale data collection not only as our unique competitive advantage, but as a responsibility to the broader community. By building and open-sourcing the dataset, we aim to provide the high-quality “fuel” needed to power embodied AI, ultimately accelerating the real-world deployment of general-purpose robotic foundation models. The robotics industry is highly competitive, and many teams have chosen to focus on data. DAIMON is releasing a large and highly comprehensive cross-embodiment, vision-based tactile multimodal robotic manipulation dataset. How were you able to achieve this? We have a dedicated in-house team focused on expanding our capabilities, including building hardware devices and developing our own large-scale model. Although we are a relatively small company, our core tactile sensing technology and innovative data collection paradigm enable us to build large-scale datasets. Our approach is to broaden our offering. We have built the world’s largest distributed out-of-lab data collection network. Rather than relying on centralized data factories, this lightweight and scalable system allows data to be gathered across diverse real-world environments, enabling us to generate millions of hours of data per year. “To drive the advancement of the entire embodied AI field, we have open-sourced 10,000 hours of the dataset for the broader community.” —Prof. Michael Yu Wang, DAIMON Robotics This dataset is being jointly developed with several institutions worldwide. What roles did they play in its development, and how will the dataset benefit their research and products? Besides China-based teams, our partners include leading research groups from universities, such as Northwestern University and the National University of Singapore, as well as top global enterprises like Google DeepMind and China Mobile. Their decision to partner with DAIMON is a strong testament to the value of our tactile-rich dataset. Among the companies involved, there are some that have already built their own models but are now incorporating tactile information. By deploying our data collection

## 参考
- https://spectrum.ieee.org/daimon-robotics-physical-ai

## 개요
DAIMON Robotics는 설립 2년 반 된 회사로, 첨단 촉각 센서 하드웨어, 특히 단색 시각 촉각 센서로 유명하며, 손끝 크기의 모듈에 110,000개 이상의 유효 감지 셀을 통합할 수 있습니다. 회사는 고해상도 촉각 센싱 기술과 분산형 실외 데이터 수집 네트워크를 활용하여 연간 수백만 시간의 데이터를 생성하고, 대규모 촉각 데이터를 포함한 대규모 로봇 조작 데이터셋을 구축합니다. 왕위(Wang Yu) 교수는 카네기멜론 대학에서 Matt Mason의 지도로 박사 학위를 받았으며, 이후 홍콩과학기술대학 로봇 연구소를 설립하여 약 40년의 현장 경험을 보유하고 있습니다. 그가 주도하는 VTLA 아키텍처는 현재 주류 Vision-Language-Action(VLA) 모델이 로봇 조작에서 촉각 인식이 부족한 문제를 해결하여 로봇이 정밀한 조작을 더욱 안정적으로 수행할 수 있도록 하는 것을 목표로 합니다.

## 핵심 내용
### 데이터셋 이니셔티브
DAIMON Robotics는 여러 최고 수준의 학술 기관 및 기업과 협력하여 가장 크고 포괄적인 로봇 조작 데이터셋을 공개했습니다. 회사는 데이터 부족이 로봇 학습의 주요 병목이며, 특히 물리적 상호작용 데이터의 부족이 핵심이라고 판단합니다. 이들의 시각 촉각 기술은 기본 접촉력뿐만 아니라 변형, 슬립 및 마찰, 재료 특성, 표면 질감을 포착하여 물리적 상호작용의 완전한 재구성을 가능하게 합니다. 회사는 촉각 피드백을 시각, 운동 궤적, 자연어와 원활하게 통합하는 견고한 데이터 처리 파이프라인을 개발하여 원시 입력을 머신러닝 모델에 사용 가능한 훈련 데이터셋으로 변환합니다. DAIMON은 세계 최대의 분산형 실외 데이터 수집 네트워크를 구축하여 연간 수백만 시간의 데이터를 생성할 수 있습니다. 임베디드 AI 분야 전체의 발전을 촉진하기 위해 회사는 10,000시간 분량의 데이터셋을 오픈소스로 공개했습니다.

### VLA에서 VTLA로: 촉각 인식이 규칙을 바꾼다
현재 로봇 분야의 주류 패러다임은 Vision-Language-Action(VLA) 모델이지만, DAIMON 팀은 Vision-Tactile-Language-Action(VTLA) 모델을 제안합니다. 촉각 정보는 접촉 상태 피드백을 제공하여 로봇이 손과 손가락을 안정적으로 조작하도록 안내하는 데 필수적입니다. 촉각 인식이 없으면 로봇은 어두운 환경에서 물체를 찾기 어렵고, 슬립 감지 부족으로 깨지기 쉬운 물체를 떨어뜨리며, 힘을 정밀하게 제어하지 못해 조작 실패나 물리적 손상이 자주 발생합니다. DAIMON의 촉각 센서는 시각 기반으로, 손끝 표면 변형의 시각적 이미지를 포착하고 시계열 이미지를 통해 접촉 정보를 인코딩하여 힘 및 기타 접촉 상태를 추론할 수 있습니다. 이러한 시각적 이미지 형식의 촉각 정보는 VLA 프레임워크에 자연스럽게 통합되어 VTLA 시스템으로 전환됩니다.

### 기술: 단색 시각 촉각 인식
DAIMON은 인간 손끝 피부 아래의 인식 능력을 모방하기 위해 세계 최초의 단색 시각 촉각 센싱 기술을 개발했습니다. 이 센서의 핵심 강점은 분산 힘 측정의 밀도와 손끝 영역 변형 포착 능력에 있으며, 가장 높은 센싱 셀 밀도를 보유합니다. 동적 성능 측면에서 센서는 힘 변화를 빠르게 감지하고 신호를 전송하며 실시간으로 처리할 수 있습니다. 기타 중요한 엔지니어링 특성으로는 신뢰성, 드리프트, 소프트 표면 내구성, 자기장·광·환경 간섭에 대한 저항성이 있습니다. 잠재 고객 중 하나는 편의점에 휴머노이드 로봇을 배치하려고 하며, 밀집된 선반 사이의 좁은 공간에서 물체를 집기 위해 최소 세 개의 가느다란 손가락으로 물체를 만지고 굴려야 하는 상황을 요구합니다. 이는 촉각 인식 능력의 필요성을 강조합니다.

### 학계에서 창업으로
왕위 교수는 카네기멜론 대학에서 박사 과정 중 로봇학을 배우기 시작했으며, 이후 홍콩과학기술대학에 로봇 연구소를 설립했습니다. 그는 박사후 연구원인 두안장화(Duan Jianghua) 박사와 함께 DAIMON Robotics를 공동 창업하여 자본과 인재 자원을 활용해 촉각 센싱 기술의 상용화를 추진했습니다. DAIMON 기술을 장착한 로봇은 이미 공장 환경에 배치되었으며, 회사의 목표는 로봇이 '임베디드 지능'을 구현하여 시각과 촉각 사이의 격차를 줄이는 것입니다.

### 비즈니스 모델 및 상업 전략
DAIMON의 비즈니스 모델은 '3D'로 요약할 수 있습니다: Devices(장치), Data(데이터), Deployment(배포). 회사는 데이터 수집을 위한 장치를 구축하고, 자체 생태계를 보유하며, 파트너의 잠재 응용 분야에 배치하여 실제 세계의 촉각 풍부 데이터를 수집하고 완전한 폐쇄 루프 검증을 실현합니다.

### 임베디드 스킬과 융합의 순간
왕위 교수는 '임베디드 스킬' 개념을 제안하며, 휴머노이드 로봇이 고급 AI '두뇌'를 넘어서야 한다고 주장합니다. 지난 20년 동안 전기, 전자, 전기기계 하드웨어 기술이 급속도로 발전하여 로봇은 완전히 전동화되었습니다. AI의 발전, 특히 대규모 언어 모델은 세계 모델로 일반화되면서 물리적 AI 능력을 가능하게 하고 있습니다. 가정 환경에서는 인간 크기의 로봇이 더 선호되며, 이는 안전하고 신뢰할 수 있으며 비용 효율적인 로봇을 실현할 수 있는 흥미로운 분야입니다.

### 실제 세계 배치로 가는 길
범용 로봇의 대규모 배치에는 아직 갈 길이 멀지만, 특정 분야에서는 실현 가능성의 징후가 나타나고 있습니다. 중국의 거의 모든 주요 호텔에는 배송 로봇(팔 없는 차량 형태)이 배치되어 로비에서 물건을 가져와 객실까지 안내합니다. 호텔 및 레스토랑 로봇은 야간 약국과 편의점 같은 특정 분야에서 휴머노이드 로봇을 배치하기 위한 모델로 간주됩니다. 이러한 시나리오는 단기간 내에 완전히 배치될 것으로 예상되며, 이후 다른 응용 분야로 확장될 것입니다. 최종 비전은 로봇이 견고한 조작 능력을 획득하여 인간의 신뢰할 수 있는 파트너로 진화하고, 가정과 일상생활에 원활하게 통합되는 것입니다.
