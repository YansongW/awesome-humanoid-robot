---
$id: ent_report_actuator_will_robotics_have_a_chatgpt_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: Will Robotics Have a ChatGPT Moment?
  zh: Will Robotics Have a ChatGPT Moment?
  ko: Will Robotics Have a ChatGPT Moment?
summary:
  en: 'Over the next few decades, billions of autonomous, AI-powered robots will work alongside people in factories, perform
    tedious tasks in warehouses, care for the elderly, assist in unsafe disaster areas , deliver packages and food to our
    doorsteps, and eventually help out in our homes. Some will look like us, and many won’t. What is certain is that regardless
    of form factor, robots will all rely heavily on AI in order to deliver real-world value. In 2025, total investments in
    robotics companies reached a record US $40.7 billion, accounting for 9 percent of all venture funding . The multibillion
    dollar question therefore is this: What will it take for AI-powered robots to begin to have a serious economic impact?
    Many of today’s robotics and AI companies are making bold claims, such as that humanoid robots will soon be coming into
    our homes , but there’s still a big gap between promise and reality. The promise of robots that live and work alongside
    us has been the stuff of science fiction for a very long time. And while many programmers have tried to make that promise
    a reality, the physical world is just too complicated for traditional computer programs to handle the endless complexity
    it presents. Thanks to AI, robots are no longer being programmed—instead, they learn to operate in the real world. With
    enough practice, they can learn to perceive and understand the world around them, reason about that world, and use that
    reason and understanding to perform tasks that are useful, reliable, and safe. The two of us have worked at the forefront
    of AI and robotics for the last decade, as a Professor in Robotics at Oregon State University and Co-Founder of Agility
    Robotics , and as former CEO of the Everyday Robots moonshot at Google X . Our experience deploying AI-powered robots
    in real-world settings has given us a perspective on where AI can be used to great benefit in complex robotic systems
    in the near term and where we are still on the frontier of science fiction. We believe AI will enable an inflection point
    in robotics advances, but that it will be through the well-engineered application of coordinated systems of different
    AI tools rather than a single ChatGPT-style breakthrough. As the excitement around AI is matched only by the uncertainty
    of what will be possible, here are five hard truths that will define AI in robotics. 1. The YouTube-to-Reality Gap Is
    Real For years, we have been seeing videos on YouTube with humanoid robots performing amazing moves on everything from
    a dance floor to an obstacle course. The inside knowledge in robotics is to “never trust a YouTube robot video.” The gap
    between real robots that can perform real work in unstructured human environments and carefully scripted and edited robot
    performances remains significant. The latest performance to get a lot of attention was a martial arts show featuring Unitree
    humanoid robots performing with children at the Chinese 2026 Spring Festival Gala. While impressive, this falls into a
    long lineage of tightly scripted robotic performances, where everything has been carefully choreographed and planned in
    advance. The low-level controls, synchronization, and choreography were stunning, yet the Spring Gala robot performance
    showed a level of autonomy and intelligence much closer to industrial robots building cars in a factory than something
    that will show up in your living room any time soon. Seeing these kinds of demos nevertheless raises questions about where
    robotics really is. If robots can perform kung fu moves and do backflips and dance, why aren’t they also showing up on
    factory floors yet? And why can’t they do the dishes in my home after dinner? The simple answer is this: Making AI-powered
    robots capable of performing general tasks in varied human environments is still really hard. While impressive technological
    feats like those at the Spring Festival may make it look like we could be very close, the use of AI in these demos is
    only for low-level motor control (to keep the robots from falling over) and therefore is only a small part of the solution
    for robots to be general purpose in the real, unstructured spaces where we humans live and work. 2. Data Is An Unsolved
    Challenge Large Language Models (LLMs) like OpenAI’s ChatGPT and Anthropic’s Claude were initially trained on an internet-scale
    database of text. The world woke up one day in late 2022 to ChatGPT demonstrating that AI computers could suddenly “speak”
    to us in prose or verse and about seemingly any topic. LLMs have turned out to generalize well and are now able to take
    multimodal input (text, images, video) and produce multimodal output. Importantly, the corpus of training data was both
    enormous and human-generated, which are characteristics that form the gold standard for AI training. The fastest path
    to robots as part of everyday life may emerge through a range of robot forms performing increasingly sophisticated applications
    and employing a range of AI tools. Agility Robotics Giving AI a body (in the form of a robot), so that it can engage with
    people in the physical world, continues to be a very difficult and broadly unsolved problem. AI models for general-purpose
    robotics must simultaneously satisfy multiple, often conflicting, physical, geometric, and temporal limitations while
    operating in unstructured, dynamic environments. In order to generalize, robot models need to be trained on data gathered
    in a high-dimensional configuration space, where “dimensions” represent text, lighting conditions, degrees of freedom,
    joint limits, velocities, force, and safety boundaries, just to mention a few. Importantly, this must be good data—it
    must contain many examples from what amounts to an infinite number of possible configurations in the physical world. Since
    there are very few existing sources of data like this, approaches like teleoperation, video analysis, motion capture of
    humans, and self-exploration in simulation and in the real world are all seen as important ways to collect data. It’s
    a herculean task. For example, at Everyday Robots at Google X, we ran 240 million robot instances in our simulator over
    the course of 2022 to collect training data, mostly to train a trash-sorting model. Similar amounts of data will be needed
    for every skill to get to a similar level of capability, which is not yet human level. 3. There Will Be No Single Robot
    AI We are far away from a moment where a single AI model might allow general-purpose robots to live and work alongside
    us. General-purpose robots can have wheels or legs. They can have one, two, three, or more arms. Some have propellers
    and can fly, while others may be designed to operate under water. Some will drive on busy roads. The physical world is
    infinitely varied and complex. And then there are all the people and other animals that will be surrounding the robots.
    How do you train a model to operate a robot safely and reliably in all of these settings? The simple answer is: You don’t.
    At least not for quite some time. We believe the winning AI architecture leading to the next big breakthroughs in general-purpose
    robotics will be “agentic AI” for robots, which are high-level coordinating models that can reason, plan, use tools, and
    learn from outcomes to execute complex tasks with limited supervision. Agentic, high-level models running on robots will
    invoke a system of specialized ones for different types of tasks. We will likely soon see multiple robots collaborating
    and coordinating with each other through their onboard agentic AI models. AI tools are unlocking new and powerful capabilities
    in robotics, which in turn will enable new solutions and new markets. It’s encouraging to see these new models being made
    broadly available, some even as open-source solutions. This availability is akin to what happened with the internet: Real
    progress occurred when it became ubiquitous. We anticipate an inevitable democratization of complex behaviors in robotics
    with wide access to these AI tools and technologies. 4. Hardware Is Still Very Hard Robots are complex systems with many
    parts that all need to work together with great precision. For a robot to be useful and safe, every part of it must be
    coordinated, from its perception systems to the computer controlling it, all the way down to its individual actuators.
    Actuators—that is, the motors and gears—are a good example of an important part of the robot where what got us here won’t
    get us there. The actuators used at scale by most industrial robots will not work for robots that will operate in human
    environments. If these robots accidentally collide with an obstacle, the resulting impacts are harsh, forces are high,
    and things break. Humans don’t move in this way. We are far more compliant in how we interact with the world, and we’re
    constantly making contact with our environment and using that contact to help us accomplish things. Consider the challenge
    of inserting a key in a lock: Humans typically don’t do this by aligning the key perfectly with the keyhole. Instead,
    we just feel for the edge of the keyhole and jiggle the key in. Robots need to be able to operate in novel ways to achieve
    comparable capabilities by using a new class of actuators that are sensitive to force and able to have a compliant interaction
    with the environment. While these kinds of actuators do exist, they are not yet generally available at scale for robot
    systems designed to operate around people. 5. Real Value Comes From “Easy” Tasks There’s a big difference between tasks
    that look impressive and real-world tasks that provide value. Robotics is a perfect example of Moravec’s paradox , which
    states that tasks that are hard for humans are easy for computers (like multiplying two big numbers), and tasks easy for
    humans (like a toddler’s movements) are extremely difficult for computers and robots. Serving customers is an unforgiving
    reality check, because customers only care about solving the real problems they have. If we are to deploy AI-based robot
    solutions, they must outperform the way things are currently done while demonstrating reliable performance metrics and
    safety. Agility Robotics’ early work to deploy our humanoid robot Digit in customer locations led to the realization that
    our first obstacle was safety: Robots that balance and manipulate objects in human spaces bring new types of risk to the
    workplace. In the first humanoid deployments , physical barriers were necessary, and Agility kicked off a multi-year engineering
    effort to solve the safety challenge, touching nearly every aspect of robot design and relying heavily on new AI-based
    approaches to human detection and behavior control. Everyday Robots at Google deployed robots in 2019 that worked autonomously
    in office buildings doing chores like cleaning cafe tables and sorting trash. We quickly learned how “messy” and difficult
    the real world is for a robot. This experience informed the architecture and deployment of our AI systems while also gathering
    real-world data that could be combined with simulation data for training and improving models. This focus on creating
    a product to meet specific customer needs and deploying robots in real-world settings is the only way to inform the structure
    of the AI tools and infrastructure for near-term utility on a path towards long-term broader capability and generality.
    There will be no “aha” moment, no silver bullet algorithm, and no volume of data sufficient to produce a general-purpose
    robot without extensive real-world experience. AI Robots Are Coming, One Step at a Time As we look to the future, there
    is no doubt that the world is bringing AI into the physical world through robots. We are at the beginning of a “ Cambrian
    explosion “ of useful, intelligent machines. We believe AI is not one tool, but a huge frontier of technical approaches
    that is unlocking new capabilities so powerful, they will define our economy moving forward. This will happen not in one
    single definitive moment, but as an ongoing set of small and large breakthroughs, where AI-driven robots begin to provide
    real value in a few tasks, and then a few more, with impacts unfolding across numerous $100 billion-plus markets that
    will dramatically improve the quality of our lives.'
  zh: 本报告由Oregon State University教授兼Agility Robotics联合创始人以及前Google X Everyday Robots CEO共同撰写，探讨AI机器人实现经济影响所需的条件。核心观点是：机器人领域的突破不会来自单一ChatGPT式模型，而是通过协调多种AI工具的系统化工程应用来实现。报告提出了五个关键挑战：演示与现实差距、数据难题、单一AI模型不可行、硬件困难以及真正价值来自“简单”任务。
  ko: 'Over the next few decades, billions of autonomous, AI-powered robots will work alongside people in factories, perform
    tedious tasks in warehouses, care for the elderly, assist in unsafe disaster areas , deliver packages and food to our
    doorsteps, and eventually help out in our homes. Some will look like us, and many won’t. What is certain is that regardless
    of form factor, robots will all rely heavily on AI in order to deliver real-world value. In 2025, total investments in
    robotics companies reached a record US $40.7 billion, accounting for 9 percent of all venture funding . The multibillion
    dollar question therefore is this: What will it take for AI-powered robots to begin to have a serious economic impact?
    Many of today’s robotics and AI companies are making bold claims, such as that humanoid robots will soon be coming into
    our homes , but there’s still a big gap between promise and reality. The promise of robots that live and work alongside
    us has been the stuff of science fiction for a very long time. And while many programmers have tried to make that promise
    a reality, the physical world is just too complicated for traditional computer programs to handle the endless complexity
    it presents. Thanks to AI, robots are no longer being programmed—instead, they learn to operate in the real world. With
    enough practice, they can learn to perceive and understand the world around them, reason about that world, and use that
    reason and understanding to perform tasks that are useful, reliable, and safe. The two of us have worked at the forefront
    of AI and robotics for the last decade, as a Professor in Robotics at Oregon State University and Co-Founder of Agility
    Robotics , and as former CEO of the Everyday Robots moonshot at Google X . Our experience deploying AI-powered robots
    in real-world settings has given us a perspective on where AI can be used to great benefit in complex robotic systems
    in the near term and where we are still on the frontier of science fiction. We believe AI will enable an inflection point
    in robotics advances, but that it will be through the well-engineered application of coordinated systems of different
    AI tools rather than a single ChatGPT-style breakthrough. As the excitement around AI is matched only by the uncertainty
    of what will be possible, here are five hard truths that will define AI in robotics. 1. The YouTube-to-Reality Gap Is
    Real For years, we have been seeing videos on YouTube with humanoid robots performing amazing moves on everything from
    a dance floor to an obstacle course. The inside knowledge in robotics is to “never trust a YouTube robot video.” The gap
    between real robots that can perform real work in unstructured human environments and carefully scripted and edited robot
    performances remains significant. The latest performance to get a lot of attention was a martial arts show featuring Unitree
    humanoid robots performing with children at the Chinese 2026 Spring Festival Gala. While impressive, this falls into a
    long lineage of tightly scripted robotic performances, where everything has been carefully choreographed and planned in
    advance. The low-level controls, synchronization, and choreography were stunning, yet the Spring Gala robot performance
    showed a level of autonomy and intelligence much closer to industrial robots building cars in a factory than something
    that will show up in your living room any time soon. Seeing these kinds of demos nevertheless raises questions about where
    robotics really is. If robots can perform kung fu moves and do backflips and dance, why aren’t they also showing up on
    factory floors yet? And why can’t they do the dishes in my home after dinner? The simple answer is this: Making AI-powered
    robots capable of performing general tasks in varied human environments is still really hard. While impressive technological
    feats like those at the Spring Festival may make it look like we could be very close, the use of AI in these demos is
    only for low-level motor control (to keep the robots from falling over) and therefore is only a small part of the solution
    for robots to be general purpose in the real, unstructured spaces where we humans live and work. 2. Data Is An Unsolved
    Challenge Large Language Models (LLMs) like OpenAI’s ChatGPT and Anthropic’s Claude were initially trained on an internet-scale
    database of text. The world woke up one day in late 2022 to ChatGPT demonstrating that AI computers could suddenly “speak”
    to us in prose or verse and about seemingly any topic. LLMs have turned out to generalize well and are now able to take
    multimodal input (text, images, video) and produce multimodal output. Importantly, the corpus of training data was both
    enormous and human-generated, which are characteristics that form the gold standard for AI training. The fastest path
    to robots as part of everyday life may emerge through a range of robot forms performing increasingly sophisticated applications
    and employing a range of AI tools. Agility Robotics Giving AI a body (in the form of a robot), so that it can engage with
    people in the physical world, continues to be a very difficult and broadly unsolved problem. AI models for general-purpose
    robotics must simultaneously satisfy multiple, often conflicting, physical, geometric, and temporal limitations while
    operating in unstructured, dynamic environments. In order to generalize, robot models need to be trained on data gathered
    in a high-dimensional configuration space, where “dimensions” represent text, lighting conditions, degrees of freedom,
    joint limits, velocities, force, and safety boundaries, just to mention a few. Importantly, this must be good data—it
    must contain many examples from what amounts to an infinite number of possible configurations in the physical world. Since
    there are very few existing sources of data like this, approaches like teleoperation, video analysis, motion capture of
    humans, and self-exploration in simulation and in the real world are all seen as important ways to collect data. It’s
    a herculean task. For example, at Everyday Robots at Google X, we ran 240 million robot instances in our simulator over
    the course of 2022 to collect training data, mostly to train a trash-sorting model. Similar amounts of data will be needed
    for every skill to get to a similar level of capability, which is not yet human level. 3. There Will Be No Single Robot
    AI We are far away from a moment where a single AI model might allow general-purpose robots to live and work alongside
    us. General-purpose robots can have wheels or legs. They can have one, two, three, or more arms. Some have propellers
    and can fly, while others may be designed to operate under water. Some will drive on busy roads. The physical world is
    infinitely varied and complex. And then there are all the people and other animals that will be surrounding the robots.
    How do you train a model to operate a robot safely and reliably in all of these settings? The simple answer is: You don’t.
    At least not for quite some time. We believe the winning AI architecture leading to the next big breakthroughs in general-purpose
    robotics will be “agentic AI” for robots, which are high-level coordinating models that can reason, plan, use tools, and
    learn from outcomes to execute complex tasks with limited supervision. Agentic, high-level models running on robots will
    invoke a system of specialized ones for different types of tasks. We will likely soon see multiple robots collaborating
    and coordinating with each other through their onboard agentic AI models. AI tools are unlocking new and powerful capabilities
    in robotics, which in turn will enable new solutions and new markets. It’s encouraging to see these new models being made
    broadly available, some even as open-source solutions. This availability is akin to what happened with the internet: Real
    progress occurred when it became ubiquitous. We anticipate an inevitable democratization of complex behaviors in robotics
    with wide access to these AI tools and technologies. 4. Hardware Is Still Very Hard Robots are complex systems with many
    parts that all need to work together with great precision. For a robot to be useful and safe, every part of it must be
    coordinated, from its perception systems to the computer controlling it, all the way down to its individual actuators.
    Actuators—that is, the motors and gears—are a good example of an important part of the robot where what got us here won’t
    get us there. The actuators used at scale by most industrial robots will not work for robots that will operate in human
    environments. If these robots accidentally collide with an obstacle, the resulting impacts are harsh, forces are high,
    and things break. Humans don’t move in this way. We are far more compliant in how we interact with the world, and we’re
    constantly making contact with our environment and using that contact to help us accomplish things. Consider the challenge
    of inserting a key in a lock: Humans typically don’t do this by aligning the key perfectly with the keyhole. Instead,
    we just feel for the edge of the keyhole and jiggle the key in. Robots need to be able to operate in novel ways to achieve
    comparable capabilities by using a new class of actuators that are sensitive to force and able to have a compliant interaction
    with the environment. While these kinds of actuators do exist, they are not yet generally available at scale for robot
    systems designed to operate around people. 5. Real Value Comes From “Easy” Tasks There’s a big difference between tasks
    that look impressive and real-world tasks that provide value. Robotics is a perfect example of Moravec’s paradox , which
    states that tasks that are hard for humans are easy for computers (like multiplying two big numbers), and tasks easy for
    humans (like a toddler’s movements) are extremely difficult for computers and robots. Serving customers is an unforgiving
    reality check, because customers only care about solving the real problems they have. If we are to deploy AI-based robot
    solutions, they must outperform the way things are currently done while demonstrating reliable performance metrics and
    safety. Agility Robotics’ early work to deploy our humanoid robot Digit in customer locations led to the realization that
    our first obstacle was safety: Robots that balance and manipulate objects in human spaces bring new types of risk to the
    workplace. In the first humanoid deployments , physical barriers were necessary, and Agility kicked off a multi-year engineering
    effort to solve the safety challenge, touching nearly every aspect of robot design and relying heavily on new AI-based
    approaches to human detection and behavior control. Everyday Robots at Google deployed robots in 2019 that worked autonomously
    in office buildings doing chores like cleaning cafe tables and sorting trash. We quickly learned how “messy” and difficult
    the real world is for a robot. This experience informed the architecture and deployment of our AI systems while also gathering
    real-world data that could be combined with simulation data for training and improving models. This focus on creating
    a product to meet specific customer needs and deploying robots in real-world settings is the only way to inform the structure
    of the AI tools and infrastructure for near-term utility on a path towards long-term broader capability and generality.
    There will be no “aha” moment, no silver bullet algorithm, and no volume of data sufficient to produce a general-purpose
    robot without extensive real-world experience. AI Robots Are Coming, One Step at a Time As we look to the future, there
    is no doubt that the world is bringing AI into the physical world through robots. We are at the beginning of a “ Cambrian
    explosion “ of useful, intelligent machines. We believe AI is not one tool, but a huge frontier of technical approaches
    that is unlocking new capabilities so powerful, they will define our economy moving forward. This will happen not in one
    single definitive moment, but as an ongoing set of small and large breakthroughs, where AI-driven robots begin to provide
    real value in a few tasks, and then a few more, with impacts unfolding across numerous $100 billion-plus markets that
    will dramatically improve the quality of our lives.'
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
- actuator
- funding
- humanoid
- ieee
- investment
- motor
- report
- robotics
- safety
- standard
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/robotics-ai-breakthrough.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1561 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Will Robotics Have a ChatGPT Moment?
  url: https://spectrum.ieee.org/robotics-ai-breakthrough
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
报告指出，尽管2025年机器人公司投资创下407亿美元纪录，但AI机器人要产生重大经济影响仍面临严峻挑战。作者基于在Agility Robotics和Google X Everyday Robots的实战经验，强调机器人AI的突破不会来自单一模型，而是需要协调多种AI工具的系统化方法。报告揭示了五个“硬真相”：YouTube演示与现实之间存在巨大差距；机器人训练数据收集仍是未解难题；通用机器人需要“代理型AI”架构而非单一模型；硬件特别是执行器技术仍需突破；真正的商业价值来自看似简单但实用的任务。作者认为，AI机器人将经历一场“寒武纪大爆发”，通过持续的小型和中型突破逐步实现价值。

## 核心内容
### 核心论点：机器人领域不会出现ChatGPT式时刻

作者基于在Oregon State University、Agility Robotics和Google X Everyday Robots的十年前沿经验，认为AI将推动机器人技术达到转折点，但这需要通过精心设计的多种AI工具协调系统来实现，而非单一突破性模型。

### 五个关键挑战

#### 1. YouTube与现实之间的鸿沟真实存在
- 2026年中国春晚中Unitree人形机器人与儿童表演武术的演示令人印象深刻，但属于精心编排的表演
- 这些演示中的AI仅用于低级运动控制（防止机器人摔倒），与通用机器人所需的自主智能相去甚远
- 在非结构化人类环境中执行通用任务仍然极其困难

#### 2. 数据收集是未解难题
- LLM（如ChatGPT、Claude）的成功依赖于互联网规模的文本数据，但机器人训练数据缺乏类似资源
- 通用机器人模型需要在高维配置空间中训练，涉及文本、光照条件、自由度、关节限制、速度、力和安全边界等多个维度
- 案例：Google X的Everyday Robots在2022年运行了2.4亿次机器人实例来收集训练数据，主要用于训练垃圾分类模型
- 每个技能都需要类似规模的数据才能达到接近人类的能力水平

#### 3. 不存在单一的机器人AI
- 通用机器人形态各异（轮式、腿式、多臂、飞行、水下），物理世界无限复杂
- 作者认为突破性架构将是“代理型AI”（agentic AI）：高层协调模型负责推理、规划、使用工具和学习结果
- 机器人上的代理型高层模型将调用专门化的子系统执行不同任务
- 多个机器人将通过各自的代理型AI模型进行协作和协调

#### 4. 硬件仍然非常困难
- 传统工业机器人使用的执行器不适合人类环境，碰撞时冲击力大、易损坏
- 人类与环境交互时具有柔顺性，例如插入钥匙时通过触觉摸索而非精确定位
- 机器人需要新型力敏感执行器，能够与环境进行柔顺交互
- 这类执行器虽然存在，但尚未大规模应用于设计在人类周围工作的机器人系统

#### 5. 真正价值来自“简单”任务
- Moravec悖论：对人类困难的任务对计算机容易，对人类容易的任务对计算机和机器人极其困难
- Agility Robotics在部署Digit人形机器人时发现首要障碍是安全，需要物理屏障和多年工程努力
- Everyday Robots在2019年部署的办公室清洁机器人揭示了现实世界的“混乱”和困难
- 只有通过创建满足特定客户需求的产品并在真实环境中部署，才能指导AI工具和基础设施的构建

### 结论：AI机器人正在逐步到来

作者预测将出现一场“寒武纪大爆发”式的智能机器进化，AI不是单一工具，而是一个巨大的技术前沿。突破不会发生在某个决定性时刻，而是通过持续的小型和中型突破，AI驱动的机器人将先在少数任务中提供真实价值，然后逐步扩展到更多领域，影响覆盖数千亿美元的市场。

## Overview
A single breakthrough AI moment in robotics may not be the answer Hans Peter Brøndmo was a VP at Google X from 2016 to 2023, where he started and led Everyday Robots.

Over the next few decades, billions of autonomous, AI-powered robots will work alongside people in factories, perform tedious tasks in warehouses, care for the elderly, assist in unsafe disaster areas , deliver packages and food to our doorsteps, and eventually help out in our homes. Some will look like us, and many won’t. What is certain is that regardless of form factor, robots will all rely heavily on AI in order to deliver real-world value. In 2025, total investments in robotics companies reached a record US $40.7 billion, accounting for 9 percent of all venture funding . The multibillion dollar question therefore is this: What will it take for AI-powered robots to begin to have a serious economic impact? Many of today’s robotics and AI companies are making bold claims, such as that humanoid robots will soon be coming into our homes , but there’s still a big gap between promise and reality. The promise of robots that live and work alongside us has been the stuff of science fiction for a very long time. And while many programmers have tried to make that promise a reality, the physical world is just too complicated for traditional computer programs to handle the endless complexity it presents. Thanks to AI, robots are no longer being programmed—instead, they learn to operate in the real world. With enough practice, they can learn to perceive and understand the world around them, reason about that world, and use that reason and understanding to perform tasks that are useful, reliable, and safe. The two of us have worked at the forefront of AI and robotics for the last decade, as a Professor in Robotics at Oregon State University and Co-Founder of Agility Robotics , and as former CEO of the Everyday Robots moonshot at Google X . Our experience deploying AI-powered robots in real-world settings has given us a perspective on where AI can be used to great benefit in complex robotic systems in the near term and where we are still on the frontier of science fiction. We believe AI will enable an inflection point in robotics advances, but that it will be through the well-engineered application of coordinated systems of different AI tools rather than a single ChatGPT-style breakthrough. As the excitement around AI is matched only by the uncertainty of what will be possible, here are five hard truths that will define AI in robotics. 1. The YouTube-to-Reality Gap Is Real For years, we have been seeing videos on YouTube with humanoid robots performing amazing moves on everything from a dance floor to an obstacle course. The inside knowledge in robotics is to “never trust a YouTube robot video.” The gap between real robots that can perform real work in unstructured human environments and carefully scripted and edited robot performances remains significant. The latest performance to get a lot of attention was a martial arts show featuring Unitree humanoid robots performing with children at the Chinese 2026 Spring Festival Gala. While impressive, this falls into a long lineage of tightly scripted robotic performances, where everything has been carefully choreographed and planned in advance. The low-level controls, synchronization, and choreography were stunning, yet the Spring Gala robot performance showed a level of autonomy and intelligence much closer to industrial robots building cars in a factory than something that will show up in your living room any time soon. Seeing these kinds of demos nevertheless raises questions about where robotics really is. If robots can perform kung fu moves and do backflips and dance, why aren’t they also showing up on factory floors yet? And why can’t they do the dishes in my home after dinner? The simple answer is this: Making AI-powered robots capable of performing general tasks in varied human environments is still really hard. While impressive technological feats like those at the Spring Festival may make it look like we could be very close, the use of AI in these demos is only for low-level motor control (to keep the robots from falling over) and therefore is only a small part of the solution for robots to be general purpose in the real, unstructured spaces where we humans live and work. 2. Data Is An Unsolved Challenge Large Language Models (LLMs) like OpenAI’s ChatGPT and Anthropic’s Claude were initially trained on an internet-scale database of text. The world woke up one day in late 2022 to ChatGPT demonstrating that AI computers could suddenly “speak” to us in prose or verse and about seemingly any topic. LLMs have turned out to generalize well and are now able to take multimodal input (text, images, video) and produce multimodal output. Importantly, the corpus of training data was both enormous and human-generated, which are characteristics that form the gold standard for AI training. The fastest path to robots as part of everyday life may emerge through a range of robot forms performing increasingly sophisticated applications and employing a range of AI tools. Agility Robotics Giving AI a body (in the form of a robot), so that it can engage with people in the physical world, continues to be a very difficult and broadly unsolved problem. AI models for general-purpose robotics must simultaneously satisfy multiple, often conflicting, physical, geometric, and temporal limitations while operating in unstructured, dynamic environments. In order to generalize, robot models need to be trained on data gathered in a high-dimensional configuration space, where “dimensions” represent text, lighting conditions, degrees of freedom, joint limits, velocities, force, and safety boundaries, just to mention a few. Importantly, this must be good data—it must contain many examples from what amounts to an infinite number of possible configurations in the physical world. Since there are very few existing sources of data like this, approaches like teleoperation, video analysis, motion capture of humans, and self-exploration in simulation and in the real world are all seen as important ways to collect data. It’s a herculean task. For example, at Everyday Robots at Google X, we ran 240 million robot instances in our simulator over the course of 2022 to collect training data, mostly to train a trash-sorting model. Similar amounts of data will be needed for every skill to get to a similar level of capability, which is not yet human level. 3. There Will Be No Single Robot AI We are far away from a moment where a single AI model might allow general-purpose robots to live and work alongside us. General-purpose robots can have wheels or legs. They can have one, two, three, or more arms. Some have propellers and can fly, while others may be designed to operate under water. Some will drive on busy roads. The physical world is infinitely varied and complex. And then there are all the people and other animals that will be surrounding the robots. How do you train a model to operate a robot safely and reliably in all of these settings? The simple answer is: You don’t. At least not for quite some time. We believe the winning AI architecture leading to the next big breakthroughs in general-purpose robotics will be “agentic AI” for robots, which are high-level coordinating models that can reason, plan, use tools, and learn from outcomes to execute complex tasks with limited supervision. Agentic, high-level models running on robots will invoke a system of specialized ones for different types of tasks. We will likely soon see multiple robots collaborating and coordinating with each other through their onboard agentic AI models. AI tools are unlocking new and powerful capabilities in robotics, which in turn will enable new solutions and new markets. It’s encouraging to see these new models being made broadly available, some even as open-source solutions. This availability is akin to what happened with the internet: Real progress occurred when it became ubiquitous. We anticipate an inevitable democratization of complex behaviors in robotics with wide access to these AI tools and technologies. 4. Hardware Is Still Very Hard Robots are complex systems with many parts that all need to work together with great precision. For a robot to be useful and safe, every part of it must be coordinated, from its perception systems to the computer controlling it, all the way down to its individual actuators. Actuators—that is, the motors and gears—are a good example of an important part of the robot where what got us here won’t get us there. The actuators used at scale by most industrial robots will not work for robots that will operate in human environments. If these robots accidentally collide with an obstacle, the resulting impacts are harsh, forces are high, and things break. Humans don’t move in this way. We are far more compliant in how we interact with the world, and we’re constantly making contact with our environment and using that contact to help us accomplish things. Consider the challenge of inserting a key in a lock: Humans typically don’t do this by aligning the key perfectly with the keyhole. Instead, we just feel for the edge of the keyhole and jiggle the key in. Robots need to be able to operate in novel ways to achieve comparable capabilities by using a new class of actuators that are sensitive to force and able to have a compliant interaction with the environment. While these kinds of actuators do exist, they are not yet generally available at scale for robot systems designed to operate around people. 5. Real Value Comes From “Easy” Tasks There’s a big difference between tasks that look impressive and real-world tasks that provide value. Robotics is a perfect example of Moravec’s paradox , which states that tasks that are hard for humans are easy for computers (like multiplying two big numbers), and tasks easy for humans (like a toddler’s movements) are extremely difficult for computers and robots. Serving customers is an unforgiving reality check, because customers only care about solving the real problems they have. If we are to deploy AI-based robot solutions, they must outperform the way things are currently done while demonstrating reliable performance metrics and safety. Agility Robotics’ early work to deploy our humanoid robot Digit in customer locations led to the realization that our first obstacle was safety: Robots that balance and manipulate objects in human spaces bring new types of risk to the workplace. In the first humanoid deployments , physical barriers were necessary, and Agility kicked off a multi-year engineering effort to solve the safety challenge, touching nearly every aspect of robot design and relying heavily on new AI-based approaches to human detection and behavior control. Everyday Robots at Google deployed robots in 2019 that worked autonomously in office buildings doing chores like cleaning cafe tables and sorting trash. We quickly learned how “messy” and difficult the real world is for a robot. This experience informed the architecture and deployment of our AI systems while also gathering real-world data that could be combined with simulation data for training and improving models. This focus on creating a product to meet specific customer needs and deploying robots in real-world settings is the only way to inform the structure of the AI tools and infrastructure for near-term utility on a path towards long-term broader capability and generality. There will be no “aha” moment, no silver bullet algorithm, and no volume of data sufficient to produce a general-purpose robot without extensive real-world experience. AI Robots Are Coming, One Step at a Time As we look to the future, there is no doubt that the world is bringing AI into the physical world through robots. We are at the beginning of a “ Cambrian explosion “ of useful, intelligent machines. We believe AI is not one tool, but a huge frontier of technical approaches that is unlocking new capabilities so powerful, they will define our economy moving forward. This will happen not in one single definitive moment, but as an ongoing set of small and large breakthroughs, where AI-driven robots begin to provide real value in a few tasks, and then a few more, with impacts unfolding across numerous $100 billion-plus markets that will dramatically improve the quality of our lives. A single breakthrough AI moment in robotics may not be the answer Hans Peter Brøndmo was a VP at Google X from 2016 to 2023, where he started and led Everyday Robots.

## Overview
A single breakthrough AI moment in robotics may not be the answer. Hans Peter Brøndmo was a VP at Google X from 2016 to 2023, where he started and led Everyday Robots.

## Content
Over the next few decades, billions of autonomous, AI-powered robots will work alongside people in factories, perform tedious tasks in warehouses, care for the elderly, assist in unsafe disaster areas, deliver packages and food to our doorsteps, and eventually help out in our homes. Some will look like us, and many won’t. What is certain is that regardless of form factor, robots will all rely heavily on AI in order to deliver real-world value. In 2025, total investments in robotics companies reached a record US $40.7 billion, accounting for 9 percent of all venture funding. The multibillion dollar question therefore is this: What will it take for AI-powered robots to begin to have a serious economic impact? Many of today’s robotics and AI companies are making bold claims, such as that humanoid robots will soon be coming into our homes, but there’s still a big gap between promise and reality. The promise of robots that live and work alongside us has been the stuff of science fiction for a very long time. And while many programmers have tried to make that promise a reality, the physical world is just too complicated for traditional computer programs to handle the endless complexity it presents. Thanks to AI, robots are no longer being programmed—instead, they learn to operate in the real world. With enough practice, they can learn to perceive and understand the world around them, reason about that world, and use that reason and understanding to perform tasks that are useful, reliable, and safe. The two of us have worked at the forefront of AI and robotics for the last decade, as a Professor in Robotics at Oregon State University and Co-Founder of Agility Robotics, and as former CEO of the Everyday Robots moonshot at Google X. Our experience deploying AI-powered robots in real-world settings has given us a perspective on where AI can be used to great benefit in complex robotic systems in the near term and where we are still on the frontier of science fiction. We believe AI will enable an inflection point in robotics advances, but that it will be through the well-engineered application of coordinated systems of different AI tools rather than a single ChatGPT-style breakthrough. As the excitement around AI is matched only by the uncertainty of what will be possible, here are five hard truths that will define AI in robotics. 1. The YouTube-to-Reality Gap Is Real For years, we have been seeing videos on YouTube with humanoid robots performing amazing moves on everything from a dance floor to an obstacle course. The inside knowledge in robotics is to “never trust a YouTube robot video.” The gap between real robots that can perform real work in unstructured human environments and carefully scripted and edited robot performances remains significant. The latest performance to get a lot of attention was a martial arts show featuring Unitree humanoid robots performing with children at the Chinese 2026 Spring Festival Gala. While impressive, this falls into a long lineage of tightly scripted robotic performances, where everything has been carefully choreographed and planned in advance. The low-level controls, synchronization, and choreography were stunning, yet the Spring Gala robot performance showed a level of autonomy and intelligence much closer to industrial robots building cars in a factory than something that will show up in your living room any time soon. Seeing these kinds of demos nevertheless raises questions about where robotics really is. If robots can perform kung fu moves and do backflips and dance, why aren’t they also showing up on factory floors yet? And why can’t they do the dishes in my home after dinner? The simple answer is this: Making AI-powered robots capable of performing general tasks in varied human environments is still really hard. While impressive technological feats like those at the Spring Festival may make it look like we could be very close, the use of AI in these demos is only for low-level motor control (to keep the robots from falling over) and therefore is only a small part of the solution for robots to be general purpose in the real, unstructured spaces where we humans live and work. 2. Data Is An Unsolved Challenge Large Language Models (LLMs) like OpenAI’s ChatGPT and Anthropic’s Claude were initially trained on an internet-scale database of text. The world woke up one day in late 2022 to ChatGPT demonstrating that AI computers could suddenly “speak” to us in prose or verse and about seemingly any topic. LLMs have turned out to generalize well and are now able to take multimodal input (text, images, video) and produce multimodal output. Importantly, the corpus of training data was both enormous and human-generated, which are characteristics that form the gold standard for AI training. The fastest path to robots as part of everyday life may emerge through a range of robot forms performing increasingly sophisticated applications and employing a range of AI tools. Agility Robotics Giving AI a body (in the form of a robot), so that it can engage with people in the physical world, continues to be a very difficult and broadly unsolved problem. AI models for general-purpose robotics must simultaneously satisfy multiple, often conflicting, physical, geometric, and temporal limitations while operating in unstructured, dynamic environments. In order to generalize, robot models need to be trained on data gathered in a high-dimensional configuration space, where “dimensions” represent text, lighting conditions, degrees of freedom, joint limits, velocities, force, and safety boundaries, just to mention a few. Importantly, this must be good data—it must contain many examples from what amounts to an infinite number of possible configurations in the physical world. Since there are very few existing sources of data like this, approaches like teleoperation, video analysis, motion capture of humans, and self-exploration in simulation and in the real world are all seen as important ways to collect data. It’s a herculean task. For example, at Everyday Robots at Google X, we ran 240 million robot instances in our simulator over the course of 2022 to collect training data, mostly to train a trash-sorting model. Similar amounts of data will be needed for every skill to get to a similar level of capability, which is not yet human level. 3. There Will Be No Single Robot AI We are far away from a moment where a single AI model might allow general-purpose robots to live and work alongside us. General-purpose robots can have wheels or legs. They can have one, two, three, or more arms. Some have propellers and can fly, while others may be designed to operate under water. Some will drive on busy roads. The physical world is infinitely varied and complex. And then there are all the people

## 参考
- https://spectrum.ieee.org/robotics-ai-breakthrough

## 개요
보고서는 2025년 로보틱스 기업 투자가 407억 달러라는 기록을 세웠음에도 불구하고, AI 로봇이 중대한 경제적 영향을 창출하기까지는 여전히 심각한 도전 과제가 남아 있다고 지적한다. 저자는 Agility Robotics와 Google X Everyday Robots에서의 실전 경험을 바탕으로, 로봇 AI의 돌파구는 단일 모델에서 나오는 것이 아니라 다양한 AI 도구를 조율하는 체계적인 접근 방식이 필요하다고 강조한다. 보고서는 다섯 가지 '냉혹한 진실'을 제시한다: YouTube 데모와 현실 사이에는 큰 격차가 존재한다; 로봇 훈련 데이터 수집은 여전히 미해결 과제다; 범용 로봇은 단일 모델이 아닌 '에이전트형 AI' 아키텍처를 필요로 한다; 하드웨어, 특히 액추에이터 기술은 여전히 돌파구가 필요하다; 진정한 상업적 가치는 단순해 보이지만 실용적인 작업에서 나온다. 저자는 AI 로봇이 지속적인 소형 및 중형 돌파구를 통해 점진적으로 가치를 실현하는 '캄브리아기 대폭발'을 겪을 것이라고 전망한다.

## 핵심 내용
### 핵심 논점: 로봇 분야에는 ChatGPT식 순간이 나타나지 않을 것이다

저자는 Oregon State University, Agility Robotics, Google X Everyday Robots에서의 10년간의 최전선 경험을 바탕으로, AI가 로봇 기술을 전환점으로 이끌 것이라고 본다. 그러나 이는 단일 돌파구 모델이 아닌, 정교하게 설계된 다양한 AI 도구의 조율 시스템을 통해 달성될 것이다.

### 다섯 가지 핵심 도전 과제

#### 1. YouTube와 현실 사이의 격차는 실재한다
- 2026년 중국 춘완(춘절 갈라)에서 Unitree 휴머노이드 로봇이 어린이들과 무술을 선보인 데모는 인상적이지만, 정교하게 연출된 공연에 불과하다
- 이러한 데모에서 AI는 저수준 운동 제어(로봇이 넘어지지 않도록 방지)에만 사용되며, 범용 로봇에 필요한 자율 지능과는 거리가 멀다
- 비구조화된 인간 환경에서 범용 작업을 수행하는 것은 여전히 극도로 어렵다

#### 2. 데이터 수집은 미해결 과제다
- LLM(예: ChatGPT, Claude)의 성공은 인터넷 규모의 텍스트 데이터에 의존하지만, 로봇 훈련 데이터에는 이와 유사한 자원이 부족하다
- 범용 로봇 모델은 고차원 구성 공간에서 훈련해야 하며, 텍스트, 조명 조건, 자유도, 관절 제한, 속도, 힘, 안전 경계 등 여러 차원을 포함한다
- 사례: Google X의 Everyday Robots는 2022년에 2억 4천만 회의 로봇 인스턴스를 실행하여 훈련 데이터를 수집했으며, 주로 쓰레기 분류 모델 훈련에 사용되었다
- 각 스킬은 인간 수준에 근접한 능력에 도달하기 위해 유사한 규모의 데이터가 필요하다

#### 3. 단일 로봇 AI는 존재하지 않는다
- 범용 로봇은 형태가 다양하며(바퀴형, 다리형, 다중 팔, 비행형, 수중형), 물리적 세계는 무한히 복잡하다
- 저자는 돌파구 아키텍처가 '에이전트형 AI'(agentic AI)가 될 것이라고 본다: 고수준 조율 모델이 추론, 계획, 도구 사용, 결과 학습을 담당한다
- 로봇의 에이전트형 고수준 모델은 전문화된 하위 시스템을 호출하여 다양한 작업을 수행한다
- 여러 로봇은 각자의 에이전트형 AI 모델을 통해 협력하고 조율된다

#### 4. 하드웨어는 여전히 매우 어렵다
- 전통적인 산업용 로봇에 사용되는 액추에이터는 인간 환경에 적합하지 않으며, 충돌 시 충격력이 크고 손상되기 쉽다
- 인간은 환경과 상호작용할 때 유연성을 갖는다. 예를 들어 열쇠를 삽입할 때 정밀한 위치 지정이 아닌 촉각을 통한 탐색을 사용한다
- 로봇은 환경과 유연하게 상호작용할 수 있는 새로운 힘 감지 액추에이터가 필요하다
- 이러한 액추에이터는 존재하지만, 인간 주변에서 작동하도록 설계된 로봇 시스템에 아직 대규모로 적용되지 않았다

#### 5. 진정한 가치는 '단순한' 작업에서 나온다
- Moravec의 역설: 인간에게 어려운 작업은 컴퓨터에게 쉬운 반면, 인간에게 쉬운 작업은 컴퓨터와 로봇에게 극도로 어렵다
- Agility Robotics는 Digit 휴머노이드 로봇을 배포할 때 첫 번째 장애물이 안전임을 발견했으며, 물리적 장벽과 수년간의 엔지니어링 노력이 필요했다
- Everyday Robots가 2019년에 배포한 사무실 청소 로봇은 현실 세계의 '혼란'과 어려움을 드러냈다
- 특정 고객 요구를 충족하는 제품을 만들고 실제 환경에 배포해야만 AI 도구와 인프라 구축을 안내할 수 있다

### 결론: AI 로봇은 점진적으로 도래하고 있다

저자는 '캄브리아기 대폭발'과 같은 지능형 기계의 진화가 나타날 것이라고 전망한다. AI는 단일 도구가 아니라 거대한 기술 프론티어다. 돌파구는 결정적인 순간에 발생하는 것이 아니라 지속적인 소형 및 중형 돌파구를 통해 이루어지며, AI 기반 로봇은 먼저 소수의 작업에서 실제 가치를 제공한 후 점차 더 많은 영역으로 확장되어 수천억 달러 규모의 시장에 영향을 미칠 것이다.
