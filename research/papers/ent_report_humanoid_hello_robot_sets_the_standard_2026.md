---
$id: ent_report_humanoid_hello_robot_sets_the_standard_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: Hello Robot Sets the Standard for Practical, Safe Home Robots
  zh: Hello Robot Sets the Standard for Practical, Safe Home Robots
  ko: Hello Robot Sets the Standard for Practical, Safe Home Robots
summary:
  en: 'Many roboticists (and at least one robotics journalist) have been seduced by the dream of a robot butler. And the rampant
    popularity of videos showing humanoid robots doing household tasks in improbably clean kitchens and unrealistically tidy
    bedrooms suggests that we’re not the only ones interested in a robot that can do our chores. But for all kinds of reasons
    , legged humanoids are not yet ready for industrial or commercial applications at scale, and home applications ( if people
    even want them ), I would argue, are even farther away. Even so, ludicrously well-funded humanoid robotics companies are
    now ramping production while explicitly promising that their robots will be doing ‘ housework .’ So what about that robot
    butler dream, then? It still exists! All you have to do is forget about legs, arms, hands, faces, and focus on what really
    matters: mobility and manipulation. This is what Hello Robot’s Stretch robot is unapologetically all about, and the newest
    version being announced today, Stretch 4, is closer than ever to a robot that could safely do practical work in the home
    at an accessible cost. Hello Robot says Stretch 4 is “built for the real world.” Hello Robot “With Stretch 4, we wanted
    to make the transition from a research platform to something that is truly deployable,” explains Aaron Edsinger , Hello
    Robot co-founder and CEO. This version, while ready for research and enterprise customers now, is designed for pilot deployments
    to help Hello Robot understand how to scale in the home. “This has been our most difficult design process,” adds co-founder
    and CTO Charlie Kemp . “We had a lot of fear of ‘second-system syndrome,’ where you add all the features you didn’t get
    to initially and end up with a monstrosity. But since we founded the company on making simple, minimalist robots, every
    time we added complexity it was an emotional challenge. Navigating that fear resulted in a nice compromise that sits in
    a great spot, rather than being a maximalist humanoid.” Stretch 4 Upgrades The biggest change from the previous version
    of Stretch is the addition of an omnidirectional base, meaning that the robot can translate in any direction without having
    to turn first. This makes it much easier to control (especially for novice users), but omnidirectional bases are significantly
    more complicated to design and build. What ultimately made it possible for Stretch were new types of omnidirectional wheels
    developed for powered wheelchairs, along with a solid six months of focused development by Hello Robot. A redesigned sensorized
    head gives Stretch more options for teleoperation and autonomy. Hello Robot Stretch 4 also ditches the cute little pan-tilt
    head for a more complex sensor suite with a much wider field of view. “We started out wanting to use lots of cheap cameras
    to keep costs low, like Tesla does,” Edsinger tells us. “But we ended up with an approach closer to Waymo’s: the richer
    and more reliable your data, the safer and more intelligent the robot can be.” There are a pair of hemispherical lidars,
    Luxonis cameras for vision and navigation, and a wrist-mounted depth camera for manipulation. The robot’s primary system
    runs on an Intel NUC 15, plus an Nvidia Jetson Orin NX for researchers to play with for visual processing or AI. Philosophy
    on Autonomy Hello Robot’s general philosophy on autonomy is to have a human in the loop, but that can take many different
    forms ranging from direct control to purely supervisory control. The robot will ship with a baseline of autonomous capabilities
    that include mapping, navigation, and self-charging, along with demo-ready features like autonomous grasping. But unlike
    most other robotics companies, Hello Robot isn’t looking to use their hardware to collect a stupendous amount of data
    in the concerningly vague hope that commercially viable autonomy will follow. “Stretch has huge advantages in safety,
    cost, and capability,” Kemp says. “I’d much rather be the platform that foundation model developers target.” Edsinger
    agrees: “We do want to partner with foundation model companies to explore things like dexterous in-home manipulation,
    but we aren’t the ones to build those foundation models.” In-Home Pilots While earlier versions of Stretch were primarily
    for research, Kemp tells us that Stretch 4 has been explicitly designed to be piloted in the homes of people with severe
    mobility impairments. Hello Robot will be happy to sell you one (or lots, I’m guessing) for commercial or industrial applications,
    but the broader goal with Stretch 4 is to use remote testing and in-home evaluations to work towards a robot that’s useful
    and reliable enough that it can provide consistent daily value for disabled users. A holonomic base and an extendable
    arm make for a capable robot without the complexity. Hello Robot Part of why I’m optimistic about Stretch finding near-term
    success in this role is precisely because it’s not a humanoid. One of the primary arguments for humanoids is that they’re
    worth pursuing because they can better operate in environments designed for humans, where legs and five-fingered hands
    are tangible advantages. But those very same environments often exclude an entire subset of humanity—a subset of humanity
    that we will all likely join at some point, because the best that any of us can ever say is that we are not disabled yet
    . Why Not Humanoids? A key partner for Hello Robot throughout the Stretch development process has been Henry Evans . Evans
    is paralyzed and cannot speak, although he can use a computer (for controlling robots, among other things) and type at
    about 15 words per minute. I spoke with Evans about his thoughts on the idea of a humanoid assistive robot, compared to
    a robot like Stretch. “The question is: What benefit does a bipedal robot offer to a person who can’t walk?” Evans asks.
    “Their entire environment has been modified to accommodate wheeled conveyances. Automobiles don’t have legs, and neither
    should home robots. Wheels are cheap, stable, precise, require very few controls, and don’t have to be invented.” Henry
    Evans has been testing a Stretch 4 as a home assistive robot. Hello Robot Evans also points out that humanoids can require
    the simultaneous control of dozens of degrees of freedom. “A paralyzed person who can’t talk (like yours truly) can control
    maybe one or two joints at a time with today’s control mechanisms, if they are lucky.” Evans believes that AI, along with
    Brain Computer Interfaces (BCIs), show promise for dramatically increasing what he can do when it comes to motion. “Remember,
    though, a paralyzed person has no movements to mimic, so until a perfectly tuned BCI gets here and facilitates a true
    humanoid body surrogate, I don’t think it will work. And even then, I don’t see the advantage of legs for assistive care
    robots. I am willing to be proven wrong, though, and will test-drive almost anything once, so bring it on!” Kemp and Edsinger,
    who have many decades of humanoid experience between them, feel similarly. “There are applications where the human form
    is fundamental,” Kemp says. “But for many applications, the value of the human form is unclear or even problematic. Jumping
    to the conclusion that robots must be humanoid means missing opportunities to take advantage of the structured indoor
    environments that we’ve already created.” Georgena Moran and her sisters tested Stretch 4 at the California Academy of
    Sciences Museum, allowing her to interact with the exhibits from home. Hello Robot And of course there’s the question
    of safety, which Evans brings up. “My caregivers and I have been testing robots in my home to assist us for about 15 years,
    and the very first concerns are: Where is the emergency stop, and how do you activate it? It gets used surprisingly often.
    The thing is, when a wheeled robot gets emergency stopped, it freezes in place. When a bipedal robot gets run-stopped,
    it collapses on anything under it, including the patient.” Kemp agrees. “The safety aspect of humanoids in a home freaks
    me out. I don’t know how someone can confidently think about safety with a humanoid in a home.” Robots for Sale However
    you feel about humanoids, here’s one more reason why Stretch feels like a much more realistic solution for in-home assistive
    robots right now: You can actually buy one, and at US $29,950, it’s very affordable, as mobile manipulators go . Edsinger
    and Kemp are planning to leverage in-home Stretch 4 pilot deployments to make the next version of Stretch the one that
    can be commercially sold for home assistance. At the rate that Hello Robot has been releasing new hardware, that could
    easily be within the next year or so—and my guess is that Stretch 5 is very likely to be the first practical, affordable
    assistive robot for home use. It may not look like Rosie, but it promises to be safe, and it works.'
  zh: Hello Robot 发布 Stretch 4 移动操作机器人，放弃人形设计，专注于轮式移动与机械臂操作。该机器人以安全、低成本（29,950 美元）和实用性为核心，专为家庭辅助场景设计，尤其关注严重行动障碍用户。核心升级包括全向底盘、增强传感器套件，并强调人类在环的自主性哲学。
  ko: 'Many roboticists (and at least one robotics journalist) have been seduced by the dream of a robot butler. And the rampant
    popularity of videos showing humanoid robots doing household tasks in improbably clean kitchens and unrealistically tidy
    bedrooms suggests that we’re not the only ones interested in a robot that can do our chores. But for all kinds of reasons
    , legged humanoids are not yet ready for industrial or commercial applications at scale, and home applications ( if people
    even want them ), I would argue, are even farther away. Even so, ludicrously well-funded humanoid robotics companies are
    now ramping production while explicitly promising that their robots will be doing ‘ housework .’ So what about that robot
    butler dream, then? It still exists! All you have to do is forget about legs, arms, hands, faces, and focus on what really
    matters: mobility and manipulation. This is what Hello Robot’s Stretch robot is unapologetically all about, and the newest
    version being announced today, Stretch 4, is closer than ever to a robot that could safely do practical work in the home
    at an accessible cost. Hello Robot says Stretch 4 is “built for the real world.” Hello Robot “With Stretch 4, we wanted
    to make the transition from a research platform to something that is truly deployable,” explains Aaron Edsinger , Hello
    Robot co-founder and CEO. This version, while ready for research and enterprise customers now, is designed for pilot deployments
    to help Hello Robot understand how to scale in the home. “This has been our most difficult design process,” adds co-founder
    and CTO Charlie Kemp . “We had a lot of fear of ‘second-system syndrome,’ where you add all the features you didn’t get
    to initially and end up with a monstrosity. But since we founded the company on making simple, minimalist robots, every
    time we added complexity it was an emotional challenge. Navigating that fear resulted in a nice compromise that sits in
    a great spot, rather than being a maximalist humanoid.” Stretch 4 Upgrades The biggest change from the previous version
    of Stretch is the addition of an omnidirectional base, meaning that the robot can translate in any direction without having
    to turn first. This makes it much easier to control (especially for novice users), but omnidirectional bases are significantly
    more complicated to design and build. What ultimately made it possible for Stretch were new types of omnidirectional wheels
    developed for powered wheelchairs, along with a solid six months of focused development by Hello Robot. A redesigned sensorized
    head gives Stretch more options for teleoperation and autonomy. Hello Robot Stretch 4 also ditches the cute little pan-tilt
    head for a more complex sensor suite with a much wider field of view. “We started out wanting to use lots of cheap cameras
    to keep costs low, like Tesla does,” Edsinger tells us. “But we ended up with an approach closer to Waymo’s: the richer
    and more reliable your data, the safer and more intelligent the robot can be.” There are a pair of hemispherical lidars,
    Luxonis cameras for vision and navigation, and a wrist-mounted depth camera for manipulation. The robot’s primary system
    runs on an Intel NUC 15, plus an Nvidia Jetson Orin NX for researchers to play with for visual processing or AI. Philosophy
    on Autonomy Hello Robot’s general philosophy on autonomy is to have a human in the loop, but that can take many different
    forms ranging from direct control to purely supervisory control. The robot will ship with a baseline of autonomous capabilities
    that include mapping, navigation, and self-charging, along with demo-ready features like autonomous grasping. But unlike
    most other robotics companies, Hello Robot isn’t looking to use their hardware to collect a stupendous amount of data
    in the concerningly vague hope that commercially viable autonomy will follow. “Stretch has huge advantages in safety,
    cost, and capability,” Kemp says. “I’d much rather be the platform that foundation model developers target.” Edsinger
    agrees: “We do want to partner with foundation model companies to explore things like dexterous in-home manipulation,
    but we aren’t the ones to build those foundation models.” In-Home Pilots While earlier versions of Stretch were primarily
    for research, Kemp tells us that Stretch 4 has been explicitly designed to be piloted in the homes of people with severe
    mobility impairments. Hello Robot will be happy to sell you one (or lots, I’m guessing) for commercial or industrial applications,
    but the broader goal with Stretch 4 is to use remote testing and in-home evaluations to work towards a robot that’s useful
    and reliable enough that it can provide consistent daily value for disabled users. A holonomic base and an extendable
    arm make for a capable robot without the complexity. Hello Robot Part of why I’m optimistic about Stretch finding near-term
    success in this role is precisely because it’s not a humanoid. One of the primary arguments for humanoids is that they’re
    worth pursuing because they can better operate in environments designed for humans, where legs and five-fingered hands
    are tangible advantages. But those very same environments often exclude an entire subset of humanity—a subset of humanity
    that we will all likely join at some point, because the best that any of us can ever say is that we are not disabled yet
    . Why Not Humanoids? A key partner for Hello Robot throughout the Stretch development process has been Henry Evans . Evans
    is paralyzed and cannot speak, although he can use a computer (for controlling robots, among other things) and type at
    about 15 words per minute. I spoke with Evans about his thoughts on the idea of a humanoid assistive robot, compared to
    a robot like Stretch. “The question is: What benefit does a bipedal robot offer to a person who can’t walk?” Evans asks.
    “Their entire environment has been modified to accommodate wheeled conveyances. Automobiles don’t have legs, and neither
    should home robots. Wheels are cheap, stable, precise, require very few controls, and don’t have to be invented.” Henry
    Evans has been testing a Stretch 4 as a home assistive robot. Hello Robot Evans also points out that humanoids can require
    the simultaneous control of dozens of degrees of freedom. “A paralyzed person who can’t talk (like yours truly) can control
    maybe one or two joints at a time with today’s control mechanisms, if they are lucky.” Evans believes that AI, along with
    Brain Computer Interfaces (BCIs), show promise for dramatically increasing what he can do when it comes to motion. “Remember,
    though, a paralyzed person has no movements to mimic, so until a perfectly tuned BCI gets here and facilitates a true
    humanoid body surrogate, I don’t think it will work. And even then, I don’t see the advantage of legs for assistive care
    robots. I am willing to be proven wrong, though, and will test-drive almost anything once, so bring it on!” Kemp and Edsinger,
    who have many decades of humanoid experience between them, feel similarly. “There are applications where the human form
    is fundamental,” Kemp says. “But for many applications, the value of the human form is unclear or even problematic. Jumping
    to the conclusion that robots must be humanoid means missing opportunities to take advantage of the structured indoor
    environments that we’ve already created.” Georgena Moran and her sisters tested Stretch 4 at the California Academy of
    Sciences Museum, allowing her to interact with the exhibits from home. Hello Robot And of course there’s the question
    of safety, which Evans brings up. “My caregivers and I have been testing robots in my home to assist us for about 15 years,
    and the very first concerns are: Where is the emergency stop, and how do you activate it? It gets used surprisingly often.
    The thing is, when a wheeled robot gets emergency stopped, it freezes in place. When a bipedal robot gets run-stopped,
    it collapses on anything under it, including the patient.” Kemp agrees. “The safety aspect of humanoids in a home freaks
    me out. I don’t know how someone can confidently think about safety with a humanoid in a home.” Robots for Sale However
    you feel about humanoids, here’s one more reason why Stretch feels like a much more realistic solution for in-home assistive
    robots right now: You can actually buy one, and at US $29,950, it’s very affordable, as mobile manipulators go . Edsinger
    and Kemp are planning to leverage in-home Stretch 4 pilot deployments to make the next version of Stretch the one that
    can be commercially sold for home assistance. At the rate that Hello Robot has been releasing new hardware, that could
    easily be within the next year or so—and my guess is that Stretch 5 is very likely to be the first practical, affordable
    assistive robot for home use. It may not look like Rosie, but it promises to be safe, and it works.'
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
- manipulation
- report
- robotics
- safety
- sensor
- standard
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/stretch-4-home-robot. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Hello Robot Sets the Standard for Practical, Safe Home Robots
  url: https://spectrum.ieee.org/stretch-4-home-robot
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Stretch 4 是 Hello Robot 推出的最新版移动操作机器人，其设计哲学明确反对人形机器人路线，认为腿、手、脸等复杂结构对家庭应用并非必要。机器人采用全向轮底盘和可伸缩机械臂，可在不转向的情况下任意平移，大幅提升易用性。传感器系统从简单的云台升级为双半球激光雷达、Luxonis 视觉相机和腕部深度相机，数据质量接近 Waymo 而非 Tesla 的低成本方案。Hello Robot 不追求通过海量数据训练通用自主性，而是与基础模型公司合作，专注于安全、可靠的家庭部署。

## 核心内容
### 核心设计理念
- **反对人形机器人**：联合创始人 Aaron Edsinger 和 Charlie Kemp 认为，人形机器人在家庭环境中存在安全风险（如紧急停止时可能倒塌压人），且对无法行走的用户毫无优势。轮椅用户 Henry Evans 指出，其生活环境已为轮式工具改造，双腿反而增加控制复杂度。
- **极简主义**：团队刻意避免“第二系统综合征”，每次增加复杂度都经过情感挑战，最终在功能与简洁间取得平衡。

### 硬件升级
- **全向底盘**：采用电动轮椅用新型全向轮，经过六个月专项开发实现。机器人可任意方向平移，无需转向，新手也能轻松控制。
- **传感器套件**：
  - 双半球激光雷达（LIDAR）用于环境感知
  - Luxonis 相机用于视觉与导航
  - 腕部深度相机用于操作
- **计算平台**：主系统运行 Intel NUC 15，另配 Nvidia Jetson Orin NX 供研究人员处理视觉与 AI 任务。

### 自主性哲学
- **人类在环**：支持从直接控制到纯监督的多种模式。
- **出厂能力**：包含建图、导航、自动充电及自主抓取等演示级功能。
- **合作策略**：不自行构建基础模型，而是与基础模型公司合作，探索灵巧家庭操作。

### 家庭试点与安全
- **目标用户**：严重行动障碍者，已与 Henry Evans 等用户进行远程测试与家庭评估。
- **安全优势**：轮式机器人紧急停止时原地冻结，而人形机器人可能倒塌压人。Kemp 直言“人形机器人在家庭中的安全性让我害怕”。
- **价格与可用性**：售价 29,950 美元，现可购买。计划通过 Stretch 4 试点部署，推动 Stretch 5 成为首款实用、可负担的家庭辅助机器人。

### 结论
Stretch 4 以轮式移动和机械臂操作替代人形设计，在安全、成本与实用性上取得突破。其不追求通用自主性，而是通过人类在环与基础模型合作，为家庭辅助机器人提供了更现实的路径。

## Overview
Forget legs or hands—Stretch 4 is a useful robot that can actually work in homes And the rampant popularity of videos showing humanoid robots doing household tasks in improbably clean kitchens and unrealistically tidy bedrooms suggests that we’re not the only ones interested in a robot that can do our chores.

Forget legs or hands—Stretch 4 is a useful robot that can actually work in homes And the rampant popularity of videos showing humanoid robots doing household tasks in improbably clean kitchens and unrealistically tidy bedrooms suggests that we’re not the only ones interested in a robot that can do our chores. But for all kinds of reasons , legged humanoids are not yet ready for industrial or commercial applications at scale, and home applications ( if people even want them ), I would argue, are even farther away. Even so, ludicrously well-funded humanoid robotics companies are now ramping production while explicitly promising that their robots will be doing ‘ housework .’ So what about that robot butler dream, then? All you have to do is forget about legs, arms, hands, faces, and focus on what really matters: mobility and manipulation. This is what Hello Robot’s Stretch robot is unapologetically all about, and the newest version being announced today, Stretch 4, is closer than ever to a robot that could safely do practical work in the home at an accessible cost.

## Overview
Forget legs or hands—Stretch 4 is a useful robot that can actually work in homes. And the rampant popularity of videos showing humanoid robots doing household tasks in improbably clean kitchens and unrealistically tidy bedrooms suggests that we’re not the only ones interested in a robot that can do our chores.

## Content
Forget legs or hands—Stretch 4 is a useful robot that can actually work in homes. And the rampant popularity of videos showing humanoid robots doing household tasks in improbably clean kitchens and unrealistically tidy bedrooms suggests that we’re not the only ones interested in a robot that can do our chores. But for all kinds of reasons, legged humanoids are not yet ready for industrial or commercial applications at scale, and home applications (if people even want them), I would argue, are even farther away. Even so, ludicrously well-funded humanoid robotics companies are now ramping production while explicitly promising that their robots will be doing ‘housework.’ So what about that robot butler dream, then? All you have to do is forget about legs, arms, hands, faces, and focus on what really matters: mobility and manipulation. This is what Hello Robot’s Stretch robot is unapologetically all about, and the newest version being announced today, Stretch 4, is closer than ever to a robot that could safely do practical work in the home at an accessible cost.

## 개요
다리나 손은 잊어라—Stretch 4는 실제로 가정에서 일할 수 있는 유용한 로봇이다. 그리고 인간형 로봇이 비현실적으로 깨끗한 주방과 지나치게 정돈된 침실에서 가사일을 하는 영상이 널리 유행하는 것은, 우리만 집안일을 해줄 로봇에 관심이 있는 것이 아님을 시사한다.

## 핵심 내용
다리나 손은 잊어라—Stretch 4는 실제로 가정에서 일할 수 있는 유용한 로봇이다. 그리고 인간형 로봇이 비현실적으로 깨끗한 주방과 지나치게 정돈된 침실에서 가사일을 하는 영상이 널리 유행하는 것은, 우리만 집안일을 해줄 로봇에 관심이 있는 것이 아님을 시사한다. 그러나 여러 이유로 인해, 다리가 있는 인간형 로봇은 아직 대규모 산업 또는 상업용 응용에 준비되지 않았으며, 가정용 응용(사람들이 원한다고 해도)은 훨씬 더 먼 미래의 일이라고 나는 주장한다. 그럼에도 불구하고, 엄청난 자금을 지원받는 인간형 로봇 회사들은 이제 로봇이 '가사일'을 할 것이라고 명시적으로 약속하면서 생산을 늘리고 있다. 그렇다면 로봇 집사 꿈은 어떻게 되는 걸까? 여러분이 해야 할 일은 다리, 팔, 손, 얼굴을 잊고 진정으로 중요한 것, 즉 이동성과 조작 능력에 집중하는 것이다. 이것이 바로 Hello Robot의 Stretch 로봇이 주저함 없이 추구하는 바이며, 오늘 발표되는 최신 버전인 Stretch 4는 저렴한 비용으로 가정에서 안전하게 실용적인 작업을 수행할 수 있는 로봇에 그 어느 때보다 가까워졌다.

## 参考
- https://spectrum.ieee.org/stretch-4-home-robot
