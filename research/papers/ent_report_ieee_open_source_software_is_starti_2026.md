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
  zh: When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their
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
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/open-source-robot-ai-platforms.
sources:
- id: src_001
  type: website
  title: Open-Source Software Is Starting to Help Robots Think
  url: https://spectrum.ieee.org/open-source-robot-ai-platforms
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
On platforms like Hugging Face, AI models for robotics gain traction When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their lives back.

## 核心内容
When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too. The shift is still early, but companies including Hugging Face, Nvidia, and Alibaba have all made significant bets on open-source robotics in the last two years, releasing tools and models aimed at the higher-level work of getting robots to reason, decide, and act. The open source movement that accelerated other AI applications is now being applied to the problem of making robots smarter. If these attempts to bring AI to robotics with open-source platforms succeed, the barrier to building a capable robot could fall as fast as the barrier to building an AI application did. The world ROS built Open-source robotics software has been around since the mid-1990s, with early projects like Carnegie Mellon University’s Inter-Process Communication package and the Player Project in the early 2000s laying the groundwork. But these were often tied to specific research groups, and the field remained fragmented. The Robot Operating System, ROS, changed that when it made its debut in 2007. By bundling tools and attracting more users, it became the de facto standard. The story of open-source robotics, in many ways, starts there. Despite its name, ROS is not actually an operating system. Rather, it is a software framework that sits on top of Linux and handles robotic fundamentals like moving data between components, talking to hardware, building maps, planning paths, and supporting developer tools, such as data logging and visualization. Before ROS, every robotics team wrote that infrastructure themselves. It often took a year or two before a lab could get to the research it actually cared about. Brian Gerkey , who helped build ROS in the mid-2000s, says he was drawn to the project because of how much open source had already changed the world, pointing out that nearly the entire internet is built on it . “I’m a tool builder, and I like to share everything as openly as I possibly can, because I think that’s where we get the most impact out of what we build,” says Gerkey, board chair of Open Robotics and now CTO at Intrinsic , a robotics and AI unit of Google. As it was developing, the AI community largely took the same approach, sharing research, models, and data openly, and the field accelerated faster than almost anyone predicted. Now some of those same advancements are arriving in robotics. Open-source AI for robotics Computer vision, once a hard problem, has advanced dramatically in just a few years, says Spencer Huang , Nvidia’s director of product for robotics. What once required significant expertise can now be done in a few lines of code. Simulation tools have become accurate enough to be useful for training, and access to the tooling that once required a specialized lab is now widely available, much of it open source. “To get into robotics, you no longer need a Ph.D.,” he says. The result is a much larger pool of people who can contribute, and the field is starting to look less like a specialized discipline and more like a platform that anyone can build on. Nvidia has built out an open-source robotics stack that covers the full development pipeline. Its Cosmos world models generate synthetic training data and simulate physical environments. Its GR00T models give robots the ability to reason through and execute complex tasks. And its Isaac frameworks handle the orchestration that ties training, simulation, and deployment together. Not everyone needs to train the robots from scratch, Huang says, and most people probably shouldn’t. “If you gate pre-training, the field just never grows,” he says. “We should be able to provide a high-quality, state-of-the-art pre-trained model that anyone can go and take and fine tune for their own purposes.” All of Nvidia’s open-source models live on Hugging Face, the open-source AI platform that has become the default place to share models and datasets. Hugging Face launched LeRobot , a community platform for robotics AI, in May 2024. Since its launch, the number of robotics datasets on the platform grew from 1,145 at the end of 2024 to more than 58,000 today, making it the single largest dataset category on the hub. Hugging Face has also moved into hardware, acquiring robotics company Pollen Robotics . The acquisition came from a realization that software alone was not enough, according to Clement Delangue , Hugging Face’s CEO. The goal, as with the software, was to bring more people in. The contributors to LeRobot include the biggest names in the industry, academic labs, and hobbyists building robots in their spare time. For instance, earlier this year, Alibaba released RynnBrain , an open-source foundation model for physical AI that the company claims outperforms comparable offerings from Google and Nvidia on benchmarks. That diversity of projects, Delangue says, is important. “It is not just one model or one dataset or one hardware,” he says. “It is a lot of small contributions that everyone can be part of.” Commercial incentives muddle the field The stakes, Delangue says, go beyond convenience. A world where only a few proprietary systems control the robots in people’s homes is a concerning one. “Having robots at home that you don’t really understand, that you don’t really control, that a few people in Silicon Valley control is a scary thought,” he says. “Open source gives an alternative path.” But getting there is not straightforward. The open sourcing happening now looks different from what produced ROS, which emerged largely from academics pooling their work with no commercial stake in the outcome. The biggest contributors today are companies with clear business reasons to want more people building on their platforms. That’s not necessarily a bad thing, says Bill Smart , a professor at Oregon State University, in Corvallis, who was part of the early open-source robotics community. But the incentives are worth being aware of. He also worries that the lowered barrier to entry has a downside. Researchers coming from AI without a robotics background are sometimes solving problems the field already solved. A newcomer might spend a week training a neural network to move a robot’s hand from one point to another, unaware that the same task can be accomplished with a few lines of code using decades-old techniques. The incentives are not always pointing in the same direction as the progress. Smart is not without hope though. Whatever the motives behind the open sourcing, he says, the effect is real. More people are in the field than ever before, the tools are genuinely easier to use, and the community is bigger and more diverse than anything that existed when ROS was getting started. “Anyone can make a robot move now,” he says. “As an old tech guy, that makes me happy and sad, because I’m no longer special.” On platforms like Hugging Face, AI models for robotics gain traction When a group of academics started making open-source robotics hardware , a generation of roboticists got years of their lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too.

## 参考
- https://spectrum.ieee.org/open-source-robot-ai-platforms
