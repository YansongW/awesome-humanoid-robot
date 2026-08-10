---
$id: ent_report_ieee_open_source_software_is_starti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: Open-Source Software Is Starting to Help Robots Think
  zh: Open-Source Software Is Starting to Help Robots Think
  ko: Open-Source Software Is Starting to Help Robots Think
summary:
  en: When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their
    lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too. The shift
    is still early, but companies including Hugging Face, Nvidia, and Alibaba have all made significant bets on open-source
    robotics in the last two years, releasing tools and models aimed at the higher-level work of getting robots to reason,
    decide, and act. The open source movement that accelerated other AI applications is now being applied to the problem of
    making robots smarter. If these attempts to bring AI to robotics with open-source platforms succeed, the barrier to building
    a capable robot could fall as fast as the barrier to building an AI application did. The world ROS built Open-source robotics
    software has been around since the mid-1990s, with early projects like Carnegie Mellon University’s Inter-Process Communication
    package and the Player Project in the early 2000s laying the groundwork. But these were often tied to specific research
    groups, and the field remained fragmented. The Robot Operating System, ROS, changed that when it made its debut in 2007.
    By bundling tools and attracting more users, it became the de facto standard. The story of open-source robotics, in many
    ways, starts there. Despite its name, ROS is not actually an operating system. Rather, it is a software framework that
    sits on top of Linux and handles robotic fundamentals like moving data between components, talking to hardware, building
    maps, planning paths, and supporting developer tools, such as data logging and visualization. Before ROS, every robotics
    team wrote that infrastructure themselves. It often took a year or two before a lab could get to the research it actually
    cared about. Brian Gerkey , who helped build ROS in the mid-2000s, says he was drawn to the project because of how much
    open source had already changed the world, pointing out that nearly the entire internet is built on it . “I’m a tool builder,
    and I like to share everything as openly as I possibly can, because I think that’s where we get the most impact out of
    what we build,” says Gerkey, board chair of Open Robotics and now CTO at Intrinsic , a robotics and AI unit of Google.
    As it was developing, the AI community largely took the same approach, sharing research, models, and data openly, and
    the field accelerated faster than almost anyone predicted. Now some of those same advancements are arriving in robotics.
    Open-source AI for robotics Computer vision, once a hard problem, has advanced dramatically in just a few years, says
    Spencer Huang , Nvidia’s director of product for robotics. What once required significant expertise can now be done in
    a few lines of code. Simulation tools have become accurate enough to be useful for training, and access to the tooling
    that once required a specialized lab is now widely available, much of it open source. “To get into robotics, you no longer
    need a Ph.D.,” he says. The result is a much larger pool of people who can contribute, and the field is starting to look
    less like a specialized discipline and more like a platform that anyone can build on. Nvidia has built out an open-source
    robotics stack that covers the full development pipeline. Its Cosmos world models generate synthetic training data and
    simulate physical environments. Its GR00T models give robots the ability to reason through and execute complex tasks.
    And its Isaac frameworks handle the orchestration that ties training, simulation, and deployment together. Not everyone
    needs to train the robots from scratch, Huang says, and most people probably shouldn’t. “If you gate pre-training, the
    field just never grows,” he says. “We should be able to provide a high-quality, state-of-the-art pre-trained model that
    anyone can go and take and fine tune for their own purposes.” All of Nvidia’s open-source models live on Hugging Face,
    the open-source AI platform that has become the default place to share models and datasets. Hugging Face launched LeRobot
    , a community platform for robotics AI, in May 2024. Since its launch, the number of robotics datasets on the platform
    grew from 1,145 at the end of 2024 to more than 58,000 today, making it the single largest dataset category on the hub.
    Hugging Face has also moved into hardware, acquiring robotics company Pollen Robotics . The acquisition came from a realization
    that software alone was not enough, according to Clement Delangue , Hugging Face’s CEO. The goal, as with the software,
    was to bring more people in. The contributors to LeRobot include the biggest names in the industry, academic labs, and
    hobbyists building robots in their spare time. For instance, earlier this year, Alibaba released RynnBrain , an open-source
    foundation model for physical AI that the company claims outperforms comparable offerings from Google and Nvidia on benchmarks.
    That diversity of projects, Delangue says, is important. “It is not just one model or one dataset or one hardware,” he
    says. “It is a lot of small contributions that everyone can be part of.” Commercial incentives muddle the field The stakes,
    Delangue says, go beyond convenience. A world where only a few proprietary systems control the robots in people’s homes
    is a concerning one. “Having robots at home that you don’t really understand, that you don’t really control, that a few
    people in Silicon Valley control is a scary thought,” he says. “Open source gives an alternative path.” But getting there
    is not straightforward. The open sourcing happening now looks different from what produced ROS, which emerged largely
    from academics pooling their work with no commercial stake in the outcome. The biggest contributors today are companies
    with clear business reasons to want more people building on their platforms. That’s not necessarily a bad thing, says
    Bill Smart , a professor at Oregon State University, in Corvallis, who was part of the early open-source robotics community.
    But the incentives are worth being aware of. He also worries that the lowered barrier to entry has a downside. Researchers
    coming from AI without a robotics background are sometimes solving problems the field already solved. A newcomer might
    spend a week training a neural network to move a robot’s hand from one point to another, unaware that the same task can
    be accomplished with a few lines of code using decades-old techniques. The incentives are not always pointing in the same
    direction as the progress. Smart is not without hope though. Whatever the motives behind the open sourcing, he says, the
    effect is real. More people are in the field than ever before, the tools are genuinely easier to use, and the community
    is bigger and more diverse than anything that existed when ROS was getting started. “Anyone can make a robot move now,”
    he says. “As an old tech guy, that makes me happy and sad, because I’m no longer special.”
  zh: 本文探讨了开源软件如何推动机器人领域从硬件走向“思考”能力。Hugging Face、Nvidia、Alibaba 等公司近两年大力投入开源机器人工具与模型，旨在降低开发门槛。若成功，构建智能机器人的壁垒将像AI应用一样迅速下降。
  ko: When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their
    lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too. The shift
    is still early, but companies including Hugging Face, Nvidia, and Alibaba have all made significant bets on open-source
    robotics in the last two years, releasing tools and models aimed at the higher-level work of getting robots to reason,
    decide, and act. The open source movement that accelerated other AI applications is now being applied to the problem of
    making robots smarter. If these attempts to bring AI to robotics with open-source platforms succeed, the barrier to building
    a capable robot could fall as fast as the barrier to building an AI application did. The world ROS built Open-source robotics
    software has been around since the mid-1990s, with early projects like Carnegie Mellon University’s Inter-Process Communication
    package and the Player Project in the early 2000s laying the groundwork. But these were often tied to specific research
    groups, and the field remained fragmented. The Robot Operating System, ROS, changed that when it made its debut in 2007.
    By bundling tools and attracting more users, it became the de facto standard. The story of open-source robotics, in many
    ways, starts there. Despite its name, ROS is not actually an operating system. Rather, it is a software framework that
    sits on top of Linux and handles robotic fundamentals like moving data between components, talking to hardware, building
    maps, planning paths, and supporting developer tools, such as data logging and visualization. Before ROS, every robotics
    team wrote that infrastructure themselves. It often took a year or two before a lab could get to the research it actually
    cared about. Brian Gerkey , who helped build ROS in the mid-2000s, says he was drawn to the project because of how much
    open source had already changed the world, pointing out that nearly the entire internet is built on it . “I’m a tool builder,
    and I like to share everything as openly as I possibly can, because I think that’s where we get the most impact out of
    what we build,” says Gerkey, board chair of Open Robotics and now CTO at Intrinsic , a robotics and AI unit of Google.
    As it was developing, the AI community largely took the same approach, sharing research, models, and data openly, and
    the field accelerated faster than almost anyone predicted. Now some of those same advancements are arriving in robotics.
    Open-source AI for robotics Computer vision, once a hard problem, has advanced dramatically in just a few years, says
    Spencer Huang , Nvidia’s director of product for robotics. What once required significant expertise can now be done in
    a few lines of code. Simulation tools have become accurate enough to be useful for training, and access to the tooling
    that once required a specialized lab is now widely available, much of it open source. “To get into robotics, you no longer
    need a Ph.D.,” he says. The result is a much larger pool of people who can contribute, and the field is starting to look
    less like a specialized discipline and more like a platform that anyone can build on. Nvidia has built out an open-source
    robotics stack that covers the full development pipeline. Its Cosmos world models generate synthetic training data and
    simulate physical environments. Its GR00T models give robots the ability to reason through and execute complex tasks.
    And its Isaac frameworks handle the orchestration that ties training, simulation, and deployment together. Not everyone
    needs to train the robots from scratch, Huang says, and most people probably shouldn’t. “If you gate pre-training, the
    field just never grows,” he says. “We should be able to provide a high-quality, state-of-the-art pre-trained model that
    anyone can go and take and fine tune for their own purposes.” All of Nvidia’s open-source models live on Hugging Face,
    the open-source AI platform that has become the default place to share models and datasets. Hugging Face launched LeRobot
    , a community platform for robotics AI, in May 2024. Since its launch, the number of robotics datasets on the platform
    grew from 1,145 at the end of 2024 to more than 58,000 today, making it the single largest dataset category on the hub.
    Hugging Face has also moved into hardware, acquiring robotics company Pollen Robotics . The acquisition came from a realization
    that software alone was not enough, according to Clement Delangue , Hugging Face’s CEO. The goal, as with the software,
    was to bring more people in. The contributors to LeRobot include the biggest names in the industry, academic labs, and
    hobbyists building robots in their spare time. For instance, earlier this year, Alibaba released RynnBrain , an open-source
    foundation model for physical AI that the company claims outperforms comparable offerings from Google and Nvidia on benchmarks.
    That diversity of projects, Delangue says, is important. “It is not just one model or one dataset or one hardware,” he
    says. “It is a lot of small contributions that everyone can be part of.” Commercial incentives muddle the field The stakes,
    Delangue says, go beyond convenience. A world where only a few proprietary systems control the robots in people’s homes
    is a concerning one. “Having robots at home that you don’t really understand, that you don’t really control, that a few
    people in Silicon Valley control is a scary thought,” he says. “Open source gives an alternative path.” But getting there
    is not straightforward. The open sourcing happening now looks different from what produced ROS, which emerged largely
    from academics pooling their work with no commercial stake in the outcome. The biggest contributors today are companies
    with clear business reasons to want more people building on their platforms. That’s not necessarily a bad thing, says
    Bill Smart , a professor at Oregon State University, in Corvallis, who was part of the early open-source robotics community.
    But the incentives are worth being aware of. He also worries that the lowered barrier to entry has a downside. Researchers
    coming from AI without a robotics background are sometimes solving problems the field already solved. A newcomer might
    spend a week training a neural network to move a robot’s hand from one point to another, unaware that the same task can
    be accomplished with a few lines of code using decades-old techniques. The incentives are not always pointing in the same
    direction as the progress. Smart is not without hope though. Whatever the motives behind the open sourcing, he says, the
    effect is real. More people are in the field than ever before, the tools are genuinely easier to use, and the community
    is bigger and more diverse than anything that existed when ROS was getting started. “Anyone can make a robot move now,”
    he says. “As an old tech guy, that makes me happy and sad, because I’m no longer special.”
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
- ieee
- report
- robotics
- standard
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/open-source-robot-ai-platforms.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1629 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Open-Source Software Is Starting to Help Robots Think
  url: https://spectrum.ieee.org/open-source-robot-ai-platforms
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
报告指出，开源机器人软件始于1990年代，但直到2007年ROS（Robot Operating System）的出现才统一了碎片化的领域，使研究人员免于重复构建底层基础设施。如今，开源运动正从硬件转向让机器人具备推理、决策和行动能力的高层智能。Nvidia 推出了涵盖训练、模拟和部署的开源机器人栈，包括Cosmos世界模型和GR00T模型；Hugging Face 则通过LeRobot平台和收购Pollen Robotics，将机器人数据集从1145个激增至超过58000个。Alibaba 也发布了声称性能超越Google和Nvidia的RynnBrain基础模型。然而，商业动机的介入使局面复杂化，部分AI背景的新研究者可能重复解决旧问题，但整体上，更低的门槛吸引了更多元化的贡献者。

## 核心内容
### 开源机器人软件的演变
- **早期基础**：1990年代中期的Carnegie Mellon University的Inter-Process Communication包和2000年代初的Player Project奠定了早期基础，但项目常局限于特定研究组，领域碎片化。
- **ROS的变革**：2007年推出的Robot Operating System（ROS）并非操作系统，而是基于Linux的软件框架，处理数据移动、硬件通信、地图构建、路径规划及开发者工具（如数据记录和可视化）。在ROS之前，每个团队需花一两年自建基础设施，ROS通过整合工具成为事实标准。
- **关键人物**：Open Robotics董事会主席、现Google旗下Intrinsic CTO的Brian Gerkey指出，开源已改变世界（如互联网），他作为工具构建者倾向于开放分享以最大化影响力。

### 开源AI进入机器人领域
- **技术进步**：Nvidia机器人产品总监Spencer Huang表示，计算机视觉在几年内大幅进步，过去需专业知识的任务现在几行代码即可完成。模拟工具足够精确用于训练，开源工具普及使“进入机器人领域不再需要博士学位”。
- **Nvidia的开源栈**：
  - **Cosmos世界模型**：生成合成训练数据并模拟物理环境。
  - **GR00T模型**：赋予机器人推理和执行复杂任务的能力。
  - **Isaac框架**：协调训练、模拟和部署的编排。
  - Huang强调，提供高质量预训练模型供微调比让所有人从头训练更利于领域发展。
- **Hugging Face的贡献**：
  - 2024年5月推出LeRobot社区平台，机器人数据集从2024年底的1145个增长至超过58000个，成为该平台最大数据集类别。
  - 收购机器人公司Pollen Robotics，CEO Clement Delangue表示软件不足，需硬件吸引更多人参与。
  - 贡献者包括行业巨头、学术实验室和业余爱好者。
- **Alibaba的RynnBrain**：2025年初发布的开源物理AI基础模型，声称在基准测试中优于Google和Nvidia的同类产品。

### 商业动机与挑战
- **开源现状**：当前开源模式与ROS时代不同，主要贡献者是有商业动机的公司（如Nvidia、Hugging Face、Alibaba），希望更多人基于其平台开发。Oregon State University教授Bill Smart认为这并非坏事，但需警惕激励偏差。
- **潜在问题**：来自AI背景的新研究者可能重复解决机器人领域已解决的旧问题（如用神经网络训练手部移动，而传统方法几行代码即可完成）。
- **积极展望**：尽管动机复杂，实际效果显著——更多人进入领域，工具更易用，社区比ROS初期更大更多元。Smart总结：“现在任何人都能让机器人动起来，作为老技术人，这让我既高兴又伤感。”

## Overview
On platforms like Hugging Face, AI models for robotics gain traction When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their lives back.

When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too. The shift is still early, but companies including Hugging Face, Nvidia, and Alibaba have all made significant bets on open-source robotics in the last two years, releasing tools and models aimed at the higher-level work of getting robots to reason, decide, and act. The open source movement that accelerated other AI applications is now being applied to the problem of making robots smarter. If these attempts to bring AI to robotics with open-source platforms succeed, the barrier to building a capable robot could fall as fast as the barrier to building an AI application did. The world ROS built Open-source robotics software has been around since the mid-1990s, with early projects like Carnegie Mellon University’s Inter-Process Communication package and the Player Project in the early 2000s laying the groundwork. But these were often tied to specific research groups, and the field remained fragmented. The Robot Operating System, ROS, changed that when it made its debut in 2007. By bundling tools and attracting more users, it became the de facto standard. The story of open-source robotics, in many ways, starts there. Despite its name, ROS is not actually an operating system. Rather, it is a software framework that sits on top of Linux and handles robotic fundamentals like moving data between components, talking to hardware, building maps, planning paths, and supporting developer tools, such as data logging and visualization. Before ROS, every robotics team wrote that infrastructure themselves. It often took a year or two before a lab could get to the research it actually cared about. Brian Gerkey , who helped build ROS in the mid-2000s, says he was drawn to the project because of how much open source had already changed the world, pointing out that nearly the entire internet is built on it . “I’m a tool builder, and I like to share everything as openly as I possibly can, because I think that’s where we get the most impact out of what we build,” says Gerkey, board chair of Open Robotics and now CTO at Intrinsic , a robotics and AI unit of Google. As it was developing, the AI community largely took the same approach, sharing research, models, and data openly, and the field accelerated faster than almost anyone predicted. Now some of those same advancements are arriving in robotics. Open-source AI for robotics Computer vision, once a hard problem, has advanced dramatically in just a few years, says Spencer Huang , Nvidia’s director of product for robotics. What once required significant expertise can now be done in a few lines of code. Simulation tools have become accurate enough to be useful for training, and access to the tooling that once required a specialized lab is now widely available, much of it open source. “To get into robotics, you no longer need a Ph.D.,” he says. The result is a much larger pool of people who can contribute, and the field is starting to look less like a specialized discipline and more like a platform that anyone can build on. Nvidia has built out an open-source robotics stack that covers the full development pipeline. Its Cosmos world models generate synthetic training data and simulate physical environments. Its GR00T models give robots the ability to reason through and execute complex tasks. And its Isaac frameworks handle the orchestration that ties training, simulation, and deployment together. Not everyone needs to train the robots from scratch, Huang says, and most people probably shouldn’t. “If you gate pre-training, the field just never grows,” he says. “We should be able to provide a high-quality, state-of-the-art pre-trained model that anyone can go and take and fine tune for their own purposes.” All of Nvidia’s open-source models live on Hugging Face, the open-source AI platform that has become the default place to share models and datasets. Hugging Face launched LeRobot , a community platform for robotics AI, in May 2024. Since its launch, the number of robotics datasets on the platform grew from 1,145 at the end of 2024 to more than 58,000 today, making it the single largest dataset category on the hub. Hugging Face has also moved into hardware, acquiring robotics company Pollen Robotics . The acquisition came from a realization that software alone was not enough, according to Clement Delangue , Hugging Face’s CEO. The goal, as with the software, was to bring more people in. The contributors to LeRobot include the biggest names in the industry, academic labs, and hobbyists building robots in their spare time. For instance, earlier this year, Alibaba released RynnBrain , an open-source foundation model for physical AI that the company claims outperforms comparable offerings from Google and Nvidia on benchmarks. That diversity of projects, Delangue says, is important. “It is not just one model or one dataset or one hardware,” he says. “It is a lot of small contributions that everyone can be part of.” Commercial incentives muddle the field The stakes, Delangue says, go beyond convenience. A world where only a few proprietary systems control the robots in people’s homes is a concerning one. “Having robots at home that you don’t really understand, that you don’t really control, that a few people in Silicon Valley control is a scary thought,” he says. “Open source gives an alternative path.” But getting there is not straightforward. The open sourcing happening now looks different from what produced ROS, which emerged largely from academics pooling their work with no commercial stake in the outcome. The biggest contributors today are companies with clear business reasons to want more people building on their platforms. That’s not necessarily a bad thing, says Bill Smart , a professor at Oregon State University, in Corvallis, who was part of the early open-source robotics community. But the incentives are worth being aware of. He also worries that the lowered barrier to entry has a downside. Researchers coming from AI without a robotics background are sometimes solving problems the field already solved. A newcomer might spend a week training a neural network to move a robot’s hand from one point to another, unaware that the same task can be accomplished with a few lines of code using decades-old techniques. The incentives are not always pointing in the same direction as the progress. Smart is not without hope though. Whatever the motives behind the open sourcing, he says, the effect is real. More people are in the field than ever before, the tools are genuinely easier to use, and the community is bigger and more diverse than anything that existed when ROS was getting started. “Anyone can make a robot move now,” he says. “As an old tech guy, that makes me happy and sad, because I’m no longer special.” On platforms like Hugging Face, AI models for robotics gain traction When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too.

## Overview
On platforms like Hugging Face, AI models for robotics are gaining traction. When a group of academics started making open-source robotics hardware, a generation of roboticists got years of their lives back.

## Content
When a group of academics started making open-source robotics hardware, a generation of roboticists got years of their lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too. The shift is still early, but companies including Hugging Face, Nvidia, and Alibaba have all made significant bets on open-source robotics in the last two years, releasing tools and models aimed at the higher-level work of getting robots to reason, decide, and act. The open source movement that accelerated other AI applications is now being applied to the problem of making robots smarter. If these attempts to bring AI to robotics with open-source platforms succeed, the barrier to building a capable robot could fall as fast as the barrier to building an AI application did. The world ROS built Open-source robotics software has been around since the mid-1990s, with early projects like Carnegie Mellon University’s Inter-Process Communication package and the Player Project in the early 2000s laying the groundwork. But these were often tied to specific research groups, and the field remained fragmented. The Robot Operating System, ROS, changed that when it made its debut in 2007. By bundling tools and attracting more users, it became the de facto standard. The story of open-source robotics, in many ways, starts there. Despite its name, ROS is not actually an operating system. Rather, it is a software framework that sits on top of Linux and handles robotic fundamentals like moving data between components, talking to hardware, building maps, planning paths, and supporting developer tools, such as data logging and visualization. Before ROS, every robotics team wrote that infrastructure themselves. It often took a year or two before a lab could get to the research it actually cared about. Brian Gerkey, who helped build ROS in the mid-2000s, says he was drawn to the project because of how much open source had already changed the world, pointing out that nearly the entire internet is built on it. “I’m a tool builder, and I like to share everything as openly as I possibly can, because I think that’s where we get the most impact out of what we build,” says Gerkey, board chair of Open Robotics and now CTO at Intrinsic, a robotics and AI unit of Google. As it was developing, the AI community largely took the same approach, sharing research, models, and data openly, and the field accelerated faster than almost anyone predicted. Now some of those same advancements are arriving in robotics. Open-source AI for robotics Computer vision, once a hard problem, has advanced dramatically in just a few years, says Spencer Huang, Nvidia’s director of product for robotics. What once required significant expertise can now be done in a few lines of code. Simulation tools have become accurate enough to be useful for training, and access to the tooling that once required a specialized lab is now widely available, much of it open source. “To get into robotics, you no longer need a Ph.D.,” he says. The result is a much larger pool of people who can contribute, and the field is starting to look less like a specialized discipline and more like a platform that anyone can build on. Nvidia has built out an open-source robotics stack that covers the full development pipeline. Its Cosmos world models generate synthetic training data and simulate physical environments. Its GR00T models give robots the ability to reason through and execute complex tasks. And its Isaac frameworks handle the orchestration that ties training, simulation, and deployment together. Not everyone needs to train the robots from scratch, Huang says, and most people probably shouldn’t. “If you gate pre-training, the field just never grows,” he says. “We should be able to provide a high-quality, state-of-the-art pre-trained model that anyone can go and take and fine tune for their own purposes.” All of Nvidia’s open-source models live on Hugging Face, the open-source AI platform that has become the default place to share models and datasets. Hugging Face launched LeRobot, a community platform for robotics AI, in May 2024. Since its launch, the number of robotics datasets on the platform grew from 1,145 at the end of 2024 to more than 58,000 today, making it the single largest dataset category on the hub. Hugging Face has also moved into hardware, acquiring robotics company Pollen Robotics. The acquisition came from a realization that software alone was not enough, according to Clement Delangue, Hugging Face’s CEO. The goal, as with the software, was to bring more people in. The contributors to LeRobot include the biggest names in the industry, academic labs, and hobbyists building robots in their spare time. For instance, earlier this year, Alibaba released RynnBrain, an open-source foundation model for physical AI that the company claims outperforms comparable offerings from Google and Nvidia on benchmarks. That diversity of projects, Delangue says, is important. “It is not just one model or one dataset or one hardware,” he says. “It is a lot of small contributions that everyone can be part of.” Commercial incentives muddle the field The stakes, Delangue says, go beyond convenience. A world where only a few proprietary systems control the robots in people’s homes is a concerning one. “Having robots at home that you don’t really understand, that you don’t really control, that a few people in Silicon Valley control is a scary thought,” he says. “Open source gives an alternative path.” But getting there is not straightforward. The open sourcing happening now looks different from what produced ROS, which emerged largely from academics pooling their work with no commercial stake in the outcome. The biggest contributors today are companies with clear business reasons to want more people building on their platforms. That’s not necessarily a bad thing, says Bill Smart, a professor at Oregon State University, in Corvallis, who was part of the early open-source robotics community. But the incentives are worth being aware of. He also worries that the lowered barrier to entry has a downside. Researchers coming from AI without a robotics background are sometimes solving problems the field already solved. A newcomer might spend a week training a neural network to move a robot’s hand from one point to another, unaware that the same task can be accomplished with a few lines of code using decades-old techniques. The incentives are not always pointing in the same direction as the progress. Smart is not without hope though. Whatever the motives behind the open sourcing, he says, the effect is real. More people are in the field than ever before, the tools are genuinely easier to use, and the community is bigger a

## 参考
- https://spectrum.ieee.org/open-source-robot-ai-platforms

## 개요
보고서는 오픈소스 로봇 소프트웨어가 1990년대에 시작되었지만, 2007년 ROS(Robot Operating System)의 등장 이후에야 파편화된 분야가 통합되어 연구자들이 기본 인프라를 반복적으로 구축하는 수고를 덜게 되었다고 지적한다. 현재 오픈소스 운동은 하드웨어에서 로봇이 추론, 의사 결정, 행동을 수행할 수 있게 하는 고수준 지능으로 초점을 옮기고 있다. Nvidia는 Cosmos 세계 모델과 GR00T 모델을 포함한 훈련, 시뮬레이션, 배포를 아우르는 오픈소스 로봇 스택을 출시했으며, Hugging Face는 LeRobot 플랫폼과 Pollen Robotics 인수를 통해 로봇 데이터셋을 1,145개에서 58,000개 이상으로 급증시켰다. Alibaba도 Google과 Nvidia를 능가하는 성능을 주장하는 RynnBrain 기반 모델을 공개했다. 그러나 상업적 동기가 개입하면서 상황이 복잡해졌고, AI 배경의 일부 신규 연구자들이 기존 문제를 반복적으로 해결할 수 있지만, 전반적으로 진입 장벽이 낮아지면서 더 다양한 기여자들이 유입되고 있다.

## 핵심 내용
### 오픈소스 로봇 소프트웨어의 진화
- **초기 기반**: 1990년대 중반 Carnegie Mellon University의 Inter-Process Communication 패키지와 2000년대 초반 Player Project가 초기 기반을 마련했지만, 프로젝트는 종종 특정 연구 그룹에 국한되어 분야가 파편화되었다.
- **ROS의 혁신**: 2007년에 출시된 Robot Operating System(ROS)은 운영체제가 아니라 Linux 기반 소프트웨어 프레임워크로, 데이터 이동, 하드웨어 통신, 지도 구축, 경로 계획 및 데이터 기록과 시각화 같은 개발자 도구를 처리한다. ROS 이전에는 각 팀이 1~2년을 들여 자체 인프라를 구축해야 했지만, ROS는 도구를 통합하여 사실상의 표준이 되었다.
- **핵심 인물**: Open Robotics 이사회 의장이자 현재 Google 산하 Intrinsic의 CTO인 Brian Gerkey는 오픈소스가 세상을 바꿨다(예: 인터넷)고 지적하며, 도구를 만드는 사람으로서 영향력을 극대화하기 위해 공개 공유를 선호한다고 밝혔다.

### 오픈소스 AI의 로봇 분야 진출
- **기술 발전**: Nvidia 로봇 제품 디렉터 Spencer Huang는 컴퓨터 비전이 몇 년 사이 크게 발전하여, 과거에는 전문 지식이 필요했던 작업이 이제는 몇 줄의 코드로 가능해졌다고 말한다. 시뮬레이션 도구는 훈련에 충분히 정밀해졌고, 오픈소스 도구의 보급으로 "로봇 분야에 진입하는 데 더 이상 박사 학위가 필요하지 않다."
- **Nvidia의 오픈소스 스택**:
  - **Cosmos 세계 모델**: 합성 훈련 데이터를 생성하고 물리적 환경을 시뮬레이션한다.
  - **GR00T 모델**: 로봇에게 복잡한 작업을 추론하고 실행하는 능력을 부여한다.
  - **Isaac 프레임워크**: 훈련, 시뮬레이션, 배포를 조율하는 오케스트레이션 도구.
  - Huang은 모든 사람이 처음부터 훈련하는 것보다 고품질 사전 훈련 모델을 제공하여 미세 조정을 지원하는 것이 분야 발전에 더 유리하다고 강조한다.
- **Hugging Face의 기여**:
  - 2024년 5월 LeRobot 커뮤니티 플랫폼을 출시하여 로봇 데이터셋이 2024년 말 1,145개에서 58,000개 이상으로 성장하며 플랫폼에서 가장 큰 데이터셋 범주가 되었다.
  - 로봇 기업 Pollen Robotics를 인수했으며, CEO Clement Delangue는 소프트웨어만으로는 부족하고 더 많은 사람의 참여를 위해 하드웨어가 필요하다고 말한다.
  - 기여자는 업계 대기업, 학술 연구소, 취미 개발자까지 다양하다.
- **Alibaba의 RynnBrain**: 2025년 초 공개된 오픈소스 물리 AI 기반 모델로, 벤치마크 테스트에서 Google과 Nvidia의 유사 제품보다 우수하다고 주장한다.

### 상업적 동기와 도전 과제
- **오픈소스 현황**: 현재 오픈소스 모델은 ROS 시대와 다르며, 주요 기여자는 상업적 동기를 가진 기업(예: Nvidia, Hugging Face, Alibaba)으로, 더 많은 사람이 자사 플랫폼을 기반으로 개발하길 원한다. Oregon State University 교수 Bill Smart는 이것이 나쁜 것은 아니지만 인센티브 편향에 주의해야 한다고 본다.
- **잠재적 문제**: AI 배경의 신규 연구자들이 로봇 분야에서 이미 해결된 기존 문제를 반복할 수 있다(예: 신경망으로 손 움직임을 훈련하는 반면, 전통적 방법은 몇 줄의 코드로 충분한 경우).
- **긍정적 전망**: 동기가 복잡하더라도 실제 효과는 뚜렷하다—더 많은 사람이 분야에 진입하고, 도구가 더 사용하기 쉬워졌으며, 커뮤니티는 ROS 초기보다 더 크고 다양해졌다. Smart는 "이제 누구나 로봇을 움직일 수 있다. 오래된 기술자로서 이는 기쁘면서도 씁쓸하다."라고 요약한다.
