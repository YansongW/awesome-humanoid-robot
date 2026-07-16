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

## Overview
On platforms like Hugging Face, AI models for robotics are gaining traction. When a group of academics started making open-source robotics hardware, a generation of roboticists got years of their lives back.

## Content
When a group of academics started making open-source robotics hardware, a generation of roboticists got years of their lives back. Now, the bigger challenge is getting robots to think—and that’s starting to be open sourced too. The shift is still early, but companies including Hugging Face, Nvidia, and Alibaba have all made significant bets on open-source robotics in the last two years, releasing tools and models aimed at the higher-level work of getting robots to reason, decide, and act. The open source movement that accelerated other AI applications is now being applied to the problem of making robots smarter. If these attempts to bring AI to robotics with open-source platforms succeed, the barrier to building a capable robot could fall as fast as the barrier to building an AI application did. The world ROS built Open-source robotics software has been around since the mid-1990s, with early projects like Carnegie Mellon University’s Inter-Process Communication package and the Player Project in the early 2000s laying the groundwork. But these were often tied to specific research groups, and the field remained fragmented. The Robot Operating System, ROS, changed that when it made its debut in 2007. By bundling tools and attracting more users, it became the de facto standard. The story of open-source robotics, in many ways, starts there. Despite its name, ROS is not actually an operating system. Rather, it is a software framework that sits on top of Linux and handles robotic fundamentals like moving data between components, talking to hardware, building maps, planning paths, and supporting developer tools, such as data logging and visualization. Before ROS, every robotics team wrote that infrastructure themselves. It often took a year or two before a lab could get to the research it actually cared about. Brian Gerkey, who helped build ROS in the mid-2000s, says he was drawn to the project because of how much open source had already changed the world, pointing out that nearly the entire internet is built on it. “I’m a tool builder, and I like to share everything as openly as I possibly can, because I think that’s where we get the most impact out of what we build,” says Gerkey, board chair of Open Robotics and now CTO at Intrinsic, a robotics and AI unit of Google. As it was developing, the AI community largely took the same approach, sharing research, models, and data openly, and the field accelerated faster than almost anyone predicted. Now some of those same advancements are arriving in robotics. Open-source AI for robotics Computer vision, once a hard problem, has advanced dramatically in just a few years, says Spencer Huang, Nvidia’s director of product for robotics. What once required significant expertise can now be done in a few lines of code. Simulation tools have become accurate enough to be useful for training, and access to the tooling that once required a specialized lab is now widely available, much of it open source. “To get into robotics, you no longer need a Ph.D.,” he says. The result is a much larger pool of people who can contribute, and the field is starting to look less like a specialized discipline and more like a platform that anyone can build on. Nvidia has built out an open-source robotics stack that covers the full development pipeline. Its Cosmos world models generate synthetic training data and simulate physical environments. Its GR00T models give robots the ability to reason through and execute complex tasks. And its Isaac frameworks handle the orchestration that ties training, simulation, and deployment together. Not everyone needs to train the robots from scratch, Huang says, and most people probably shouldn’t. “If you gate pre-training, the field just never grows,” he says. “We should be able to provide a high-quality, state-of-the-art pre-trained model that anyone can go and take and fine tune for their own purposes.” All of Nvidia’s open-source models live on Hugging Face, the open-source AI platform that has become the default place to share models and datasets. Hugging Face launched LeRobot, a community platform for robotics AI, in May 2024. Since its launch, the number of robotics datasets on the platform grew from 1,145 at the end of 2024 to more than 58,000 today, making it the single largest dataset category on the hub. Hugging Face has also moved into hardware, acquiring robotics company Pollen Robotics. The acquisition came from a realization that software alone was not enough, according to Clement Delangue, Hugging Face’s CEO. The goal, as with the software, was to bring more people in. The contributors to LeRobot include the biggest names in the industry, academic labs, and hobbyists building robots in their spare time. For instance, earlier this year, Alibaba released RynnBrain, an open-source foundation model for physical AI that the company claims outperforms comparable offerings from Google and Nvidia on benchmarks. That diversity of projects, Delangue says, is important. “It is not just one model or one dataset or one hardware,” he says. “It is a lot of small contributions that everyone can be part of.” Commercial incentives muddle the field The stakes, Delangue says, go beyond convenience. A world where only a few proprietary systems control the robots in people’s homes is a concerning one. “Having robots at home that you don’t really understand, that you don’t really control, that a few people in Silicon Valley control is a scary thought,” he says. “Open source gives an alternative path.” But getting there is not straightforward. The open sourcing happening now looks different from what produced ROS, which emerged largely from academics pooling their work with no commercial stake in the outcome. The biggest contributors today are companies with clear business reasons to want more people building on their platforms. That’s not necessarily a bad thing, says Bill Smart, a professor at Oregon State University, in Corvallis, who was part of the early open-source robotics community. But the incentives are worth being aware of. He also worries that the lowered barrier to entry has a downside. Researchers coming from AI without a robotics background are sometimes solving problems the field already solved. A newcomer might spend a week training a neural network to move a robot’s hand from one point to another, unaware that the same task can be accomplished with a few lines of code using decades-old techniques. The incentives are not always pointing in the same direction as the progress. Smart is not without hope though. Whatever the motives behind the open sourcing, he says, the effect is real. More people are in the field than ever before, the tools are genuinely easier to use, and the community is bigger a

## 개요
Hugging Face와 같은 플랫폼에서 로봇공학용 AI 모델이 주목받고 있습니다. 한 무리의 학자들이 오픈소스 로봇공학 하드웨어를 만들기 시작했을 때, 한 세대의 로봇공학자들은 몇 년의 시간을 되찾았습니다.

## 핵심 내용
한 무리의 학자들이 오픈소스 로봇공학 하드웨어를 만들기 시작했을 때, 한 세대의 로봇공학자들은 몇 년의 시간을 되찾았습니다. 이제 더 큰 과제는 로봇이 생각하게 하는 것이며, 이것 역시 오픈소스화되기 시작했습니다. 이러한 변화는 아직 초기 단계이지만, Hugging Face, Nvidia, Alibaba를 포함한 기업들은 지난 2년 동안 오픈소스 로봇공학에 상당한 투자를 하며, 로봇이 추론하고, 결정하고, 행동하게 하는 고차원 작업을 목표로 하는 도구와 모델을 출시했습니다. 다른 AI 애플리케이션을 가속화했던 오픈소스 운동이 이제 로봇을 더 똑똑하게 만드는 문제에 적용되고 있습니다. 이러한 오픈소스 플랫폼을 통해 AI를 로봇공학에 도입하려는 시도가 성공한다면, 유능한 로봇을 구축하는 장벽은 AI 애플리케이션을 구축하는 장벽이 무너졌던 것처럼 빠르게 낮아질 수 있습니다. ROS가 구축한 세계 오픈소스 로봇공학 소프트웨어는 1990년대 중반부터 존재해 왔으며, 카네기 멜론 대학의 프로세스 간 통신 패키지와 2000년대 초반의 Player Project와 같은 초기 프로젝트가 기반을 마련했습니다. 그러나 이러한 프로젝트는 종종 특정 연구 그룹에 국한되었고, 해당 분야는 여전히 파편화되어 있었습니다. 로봇 운영 체제(ROS)는 2007년에 등장하면서 이를 변화시켰습니다. 도구를 묶고 더 많은 사용자를 유치함으로써 사실상의 표준이 되었습니다. 오픈소스 로봇공학의 이야기는 여러모로 거기서 시작됩니다. 이름과 달리 ROS는 실제 운영 체제가 아닙니다. 오히려 Linux 위에 위치하며, 구성 요소 간 데이터 이동, 하드웨어 통신, 지도 구축, 경로 계획, 데이터 로깅 및 시각화와 같은 개발자 도구 지원 등 로봇공학의 기본 기능을 처리하는 소프트웨어 프레임워크입니다. ROS 이전에는 모든 로봇공학 팀이 해당 인프라를 직접 작성해야 했습니다. 연구실이 실제로 관심 있는 연구를 시작하기까지 종종 1~2년이 걸렸습니다. 2000년대 중반 ROS 구축을 도왔던 Brian Gerkey는 오픈소스가 이미 세상을 얼마나 변화시켰는지 때문에 이 프로젝트에 매료되었다고 말하며, 거의 모든 인터넷이 오픈소스 위에 구축되어 있다고 지적합니다. "저는 도구 제작자이며, 가능한 한 모든 것을 공개적으로 공유하는 것을 좋아합니다. 그것이 우리가 만든 것에서 가장 큰 영향을 얻을 수 있는 방법이라고 생각하기 때문입니다."라고 Open Robotics의 이사회 의장이자 현재 Google의 로봇공학 및 AI 부서인 Intrinsic의 CTO인 Gerkey는 말합니다. 개발 과정에서 AI 커뮤니티는 대체로 동일한 접근 방식을 취하여 연구, 모델, 데이터를 공개적으로 공유했으며, 해당 분야는 거의 예측을 뛰어넘는 속도로 가속화되었습니다. 이제 이러한 발전 중 일부가 로봇공학에 도달하고 있습니다. 로봇공학을 위한 오픈소스 AI 한때 어려운 문제였던 컴퓨터 비전은 불과 몇 년 만에 극적으로 발전했다고 Nvidia의 로봇공학 제품 디렉터 Spencer Huang은 말합니다. 한때 상당한 전문 지식이 필요했던 작업이 이제는 몇 줄의 코드로 가능해졌습니다. 시뮬레이션 도구는 훈련에 유용할 만큼 정확해졌으며, 한때 전문 연구실이 필요했던 도구에 대한 접근이 이제는 널리 가능해졌고, 대부분 오픈소스입니다. "로봇공학에 입문하기 위해 더 이상 박사 학위가 필요하지 않습니다."라고 그는 말합니다. 그 결과 기여할 수 있는 사람들의 풀이 훨씬 더 넓어졌으며, 해당 분야는 더 이상 전문 분야처럼 보이지 않고 누구나 구축할 수 있는 플랫폼처럼 보이기 시작했습니다. Nvidia는 전체 개발 파이프라인을 포괄하는 오픈소스 로봇공학 스택을 구축했습니다. Cosmos 월드 모델은 합성 훈련 데이터를 생성하고 물리적 환경을 시뮬레이션합니다. GR00T 모델은 로봇이 복잡한 작업을 추론하고 실행할 수 있는 능력을 제공합니다. Isaac 프레임워크는 훈련, 시뮬레이션, 배포를 연결하는 오케스트레이션을 처리합니다. 모든 사람이 처음부터 로봇을 훈련할 필요는 없으며, 대부분의 사람들은 그렇게 해서는 안 된다고 Huang은 말합니다. "사전 훈련을 제한하면 해당 분야는 결코 성장하지 않습니다."라고 그는 말합니다. "우리는 누구나 가져가서 자신의 목적에 맞게 미세 조정할 수 있는 고품질의 최첨단 사전 훈련 모델을 제공할 수 있어야 합니다." Nvidia의 모든 오픈소스 모델은 모델과 데이터셋을 공유하는 기본 플랫폼이 된 오픈소스 AI 플랫폼 Hugging Face에 있습니다. Hugging Face는 2024년 5월 로봇공학 AI를 위한 커뮤니티 플랫폼인 LeRobot을 출시했습니다. 출시 이후 플랫폼의 로봇공학 데이터셋 수는 2024년 말 1,145개에서 현재 58,000개 이상으로 증가하여 허브에서 가장 큰 단일 데이터셋 범주가 되었습니다. Hugging Face는 또한 하드웨어 분야로 진출하여 로봇공학 회사 Pollen Robotics를 인수했습니다. 이 인수는 소프트웨어만으로는 충분하지 않다는 인식에서 비롯되었다고 Hugging Face의 CEO Clement Delangue는 말합니다. 소프트웨어와 마찬가지로 목표는 더 많은 사람들을 참여시키는 것이었습니다. LeRobot에 기여하는 곳은 업계의 가장 큰 이름, 학술 연구실, 여가 시간에 로봇을 만드는 취미인 등 다양합니다. 예를 들어, 올해 초 Alibaba는 물리적 AI를 위한 오픈소스 기반 모델인 RynnBrain을 출시했으며, 이 모델은 벤치마크에서 Google 및 Nvidia의 유사 제품보다 성능이 뛰어나다고 주장합니다. 이러한 프로젝트의 다양성은 중요하다고 Delangue는 말합니다. "단지 하나의 모델이나 하나의 데이터셋 또는 하나의 하드웨어가 아닙니다."라고 그는 말합니다. "모든 사람이 참여할 수 있는 많은 소규모 기여입니다." 상업적 인센티브가 분야를 혼란스럽게 하다 Delangue에 따르면, 그 중요성은 편리함을 넘어섭니다. 소수의 독점 시스템만이 사람들의 집에 있는 로봇을 통제하는 세상은 우려스러운 일입니다. "이해하지 못하고, 통제하지 못하며, 실리콘 밸리의 소수만이 통제하는 집 안의 로봇을 갖는 것은 무서운 생각입니다."라고 그는 말합니다. "오픈소스는 대안적인 경로를 제공합니다." 그러나 거기에 도달하는 것은 간단하지 않습니다. 현재 진행 중인 오픈소스화는 결과에 상업적 이해관계 없이 주로 학자들이 작업을 모아서 탄생한 ROS와는 다르게 보입니다. 오늘날 가장 큰 기여자는 더 많은 사람들이 자신들의 플랫폼에서 구축하도록 하려는 명확한 비즈니스 이유를 가진 기업들입니다. 이것이 반드시 나쁜 것은 아니라고 코발리스에 있는 오리건 주립 대학의 교수이자 초기 오픈소스 로봇공학 커뮤니티의 일원이었던 Bill Smart는 말합니다. 그러나 인센티브를 인식할 가치는 있습니다. 그는 또한 진입 장벽이 낮아진 것에 단점이 있다고 우려합니다. 로봇공학 배경 없이 AI에서 온 연구자들은 때때로 해당 분야에서 이미 해결된 문제를 해결하고 있습니다. 신규 이자는 수십 년 된 기술을 사용하여 몇 줄의 코드로 동일한 작업을 수행할 수 있다는 사실을 모른 채 로봇의 손을 한 지점에서 다른 지점으로 움직이도록 신경망을 훈련하는 데 일주일을 보낼 수 있습니다. 인센티브가 항상 진보와 같은 방향을 가리키는 것은 아닙니다. 그러나 Smart는 희망을 완전히 잃지는 않았습니다. 오픈소스화의 동기가 무엇이든, 그 효과는 실질적이라고 그는 말합니다. 그 어느 때보다 더 많은 사람들이 해당 분야에 참여하고 있으며, 도구는 진정으로 사용하기 쉬워졌고, 커뮤니티는 더 커졌습니다.
