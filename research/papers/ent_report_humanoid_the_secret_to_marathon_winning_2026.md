---
$id: ent_report_humanoid_the_secret_to_marathon_winning_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: The Secret to Marathon-Winning Humanoid Robots
  zh: The Secret to Marathon-Winning Humanoid Robots
  ko: The Secret to Marathon-Winning Humanoid Robots
summary:
  en: 'On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds , beating the
    human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some
    magical technology or technique that unlocked this performance? How did the company beat the significantly better-known
    Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)?
    My doctoral thesis involved building and controlling hopping and running robots , and since then I’ve tried to design
    and build efficient commercial legged robots , giving me a decent idea of the constraints involved. In this article, we
    take a look at the fundamental underlying constraints to try and answer these questions. The Physics of Running Running
    consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air
    (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase
    pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for
    the next foothold. Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat.
    Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production,
    but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This
    is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there
    is usually a sweet spot for the gear ratio: The power consumed by a robot leg is minimized at an optimal gear ratio (30:1
    in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s motor specifications are not published, the
    hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I
    looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model
    to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as
    gear ratio varies: The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much
    heat will be produced in the knee motor, ~150W for the optimal gearing. Avik De/Datawrapper We see that the drivetrain
    is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption
    would be a very reasonable 400 watts. However, the dissipated knee power ( typically the main thermal limiting factor)
    is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will
    inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge,
    but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling pipes penetrate deep into the motors
    like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the
    four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit. Liquid cooling is not new,
    but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried
    it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based
    cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key
    enabler of this type of performance. Why Others Couldn’t Compete Why did Honor’s competitors, including more established
    and widely shipped humanoids such as from Unitree or Agibot , not compete as well? We can use the same model to generate
    an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial
    humanoid robot: The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized
    design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while
    running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design. Avik
    De/Datawrapper The plot adds a new green curve for the walking power, and the optimal gearing is significantly different!
    Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The
    knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized
    design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the
    running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the
    robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into
    objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon performance was an impressive engineering
    effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution
    is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization,
    and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line. The
    Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient
    runner but a less efficient walker. Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images
    However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is
    always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently
    improving AI language models, this very human skill is becoming the most valuable one an engineer can have. The news coverage
    seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans
    have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot
    and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess , where it couldn’t physically move
    the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while
    visually navigating the course without GPS. Comparing the robot runner to a human runner is just an apples-to-oranges
    comparison, which only risks diminishing Honor’s engineering achievement on one hand and human athletic achievement on
    the other.'
  zh: 2026年4月19日，Honor Lightning人形机器人以50分26秒完成半程马拉松，比人类世界纪录快7分钟，比2025年最佳机器人成绩快近2小时。核心突破在于针对跑步任务优化了齿轮比（45:1），并采用毛细管液体冷却系统解决电机过热问题，使持续高速奔跑成为可能。
  ko: 'On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds , beating the
    human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some
    magical technology or technique that unlocked this performance? How did the company beat the significantly better-known
    Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)?
    My doctoral thesis involved building and controlling hopping and running robots , and since then I’ve tried to design
    and build efficient commercial legged robots , giving me a decent idea of the constraints involved. In this article, we
    take a look at the fundamental underlying constraints to try and answer these questions. The Physics of Running Running
    consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air
    (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase
    pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for
    the next foothold. Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat.
    Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production,
    but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This
    is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there
    is usually a sweet spot for the gear ratio: The power consumed by a robot leg is minimized at an optimal gear ratio (30:1
    in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s motor specifications are not published, the
    hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I
    looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model
    to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as
    gear ratio varies: The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much
    heat will be produced in the knee motor, ~150W for the optimal gearing. Avik De/Datawrapper We see that the drivetrain
    is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption
    would be a very reasonable 400 watts. However, the dissipated knee power ( typically the main thermal limiting factor)
    is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will
    inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge,
    but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling pipes penetrate deep into the motors
    like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the
    four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit. Liquid cooling is not new,
    but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried
    it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based
    cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key
    enabler of this type of performance. Why Others Couldn’t Compete Why did Honor’s competitors, including more established
    and widely shipped humanoids such as from Unitree or Agibot , not compete as well? We can use the same model to generate
    an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial
    humanoid robot: The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized
    design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while
    running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design. Avik
    De/Datawrapper The plot adds a new green curve for the walking power, and the optimal gearing is significantly different!
    Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The
    knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized
    design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the
    running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the
    robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into
    objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon performance was an impressive engineering
    effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution
    is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization,
    and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line. The
    Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient
    runner but a less efficient walker. Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images
    However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is
    always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently
    improving AI language models, this very human skill is becoming the most valuable one an engineer can have. The news coverage
    seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans
    have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot
    and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess , where it couldn’t physically move
    the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while
    visually navigating the course without GPS. Comparing the robot runner to a human runner is just an apples-to-oranges
    comparison, which only risks diminishing Honor’s engineering achievement on one hand and human athletic achievement on
    the other.'
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
- motor
- report
- robotics
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/china-humanoid-robot-marathon.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: The Secret to Marathon-Winning Humanoid Robots
  url: https://spectrum.ieee.org/china-humanoid-robot-marathon
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Honor Lightning的成功并非依赖魔法技术，而是基于对跑步物理原理的深刻理解。跑步由支撑相和腾空相交替组成，电机在产生扭矩时会产生大量热量，而齿轮比的选择直接影响功率消耗和散热需求。Honor通过将齿轮比从常规步行优化的30:1调整为跑步优化的45:1，将膝关节电机功耗控制在约150W，同时采用深入电机内部的液体冷却系统（流量超过4升/分钟）实现高效散热。相比之下，Unitree等竞争对手因采用步行优化设计，在跑步时膝关节功耗超过300W，不得不使用冰袋辅助散热。

## 核心内容
### 核心原理
- 跑步的物理本质：支撑相腿部推地产生向上动量，腾空相身体因重力下落。电机扭矩越大，热损耗越高；齿轮箱可放大扭矩但降低输出加速度，存在最优齿轮比（本例中为30:1）。
- Honor Lightning的电机规格未公开，但髋部和膝部电机外径约110-150mm，作者参考ILM115x25电机参数进行建模。

### 关键技术
- **齿轮比优化**：针对7m/s（半马平均速度）的跑步任务，最优齿轮比为45:1，此时机器人总功耗约400W，膝关节散热约150W。
- **液体冷却系统**：冷却管道像毛细血管一样深入电机内部，高功率液泵热交换流量超过4升/分钟，下肢四个驱动电机各有独立冷却回路。传统空气对流冷却无法持续排出150W热量，这是性能突破的关键。

### 竞争对比
- Unitree和Agibot等竞争对手采用步行优化设计（齿轮比30:1），在跑步时膝关节功耗超过300W，是Honor的两倍以上，因此需要冰袋辅助。
- 跑步优化设计（45:1）在步行时效率较低，且大尺寸电机增加重量、占用空间，影响在家庭或工厂中的实用性。

### 结论
- Honor的成就源于工程权衡：为特定任务（半马）优化齿轮比和冷却系统，而非追求通用性。
- 与人类比较无意义：机器人不具备人类视觉导航、避障等能力，如同1997年Deep Blue击败Kasparov但无法移动棋子。
- 冷却、重量优化和鲁棒性提升对未来承载重物等实用场景具有潜在价值。

## Overview
This impressive athletic performance isn’t magic, it’s motors and gear ratios from UPenn and a post-doc from Harvard who co-founded Ghost Robotics.

On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds , beating the human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some magical technology or technique that unlocked this performance? How did the company beat the significantly better-known Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)? My doctoral thesis involved building and controlling hopping and running robots , and since then I’ve tried to design and build efficient commercial legged robots , giving me a decent idea of the constraints involved. In this article, we take a look at the fundamental underlying constraints to try and answer these questions. The Physics of Running Running consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for the next foothold. Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat. Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production, but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there is usually a sweet spot for the gear ratio: The power consumed by a robot leg is minimized at an optimal gear ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s motor specifications are not published, the hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio varies: The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much heat will be produced in the knee motor, ~150W for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption would be a very reasonable 400 watts. However, the dissipated knee power ( typically the main thermal limiting factor) is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge, but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling pipes penetrate deep into the motors like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key enabler of this type of performance. Why Others Couldn’t Compete Why did Honor’s competitors, including more established and widely shipped humanoids such as from Unitree or Agibot , not compete as well? We can use the same model to generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial humanoid robot: The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design. Avik De/Datawrapper The plot adds a new green curve for the walking power, and the optimal gearing is significantly different! Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon performance was an impressive engineering effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization, and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line. The Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient runner but a less efficient walker. Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently improving AI language models, this very human skill is becoming the most valuable one an engineer can have. The news coverage seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while visually navigating the course without GPS. Comparing the robot runner to a human runner is just an apples-to-oranges comparison, which only risks diminishing Honor’s engineering achievement on one hand and human athletic achievement on the other. This impressive athletic performance isn’t magic, it’s motors and gear ratios from UPenn and a post-doc from Harvard who co-founded Ghost Robotics. Honor’s Lightning humanoid robot sprints to the finish of a half-marathon in China.

## Content
On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds, beating the human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some magical technology or technique that unlocked this performance? How did the company beat the significantly better-known Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)? My doctoral thesis involved building and controlling hopping and running robots, and since then I’ve tried to design and build efficient commercial legged robots, giving me a decent idea of the constraints involved. In this article, we take a look at the fundamental underlying constraints to try and answer these questions.

### The Physics of Running
Running consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for the next foothold.

Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat. Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production, but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there is usually a sweet spot for the gear ratio:

The power consumed by a robot leg is minimized at an optimal gear ratio (30:1 in this example).  
*Avik De/Datawrapper*

### How Honor Did It
While the Lightning’s motor specifications are not published, the hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio varies:

The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much heat will be produced in the knee motor, ~150W for the optimal gearing.  
*Avik De/Datawrapper*

We see that the drivetrain is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption would be a very reasonable 400 watts. However, the dissipated knee power (typically the main thermal limiting factor) is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge, but the Lightning has a trick up its sleeve: According to Honor, the liquid-cooling pipes penetrate deep into the motors like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit.

Liquid cooling is not new, but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key enabler of this type of performance.

### Why Others Couldn’t Compete
Why did Honor’s competitors, including more established and widely shipped humanoids such as from Unitree or Agibot, not compete as well? We can use the same model to generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial humanoid robot:

The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design.  
*Avik De/Datawrapper*

The plot adds a new green curve for the walking power, and the optimal gearing is significantly different! Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into objects while operating in homes or factories.

### Closing Thoughts
Honor’s half-marathon performance was an impressive engineering effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization, and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line.

The Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient runner but a less efficient walker.  
*Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images*

However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently improving AI language models, this very human skill is becoming the most valuable one an engineer can have.

The news coverage seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess, where it couldn’t physically move the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while visually navigating the course without GPS.

## 개요
이 인상적인 운동 능력은 마법이 아닙니다. 펜실베이니아 대학의 모터와 기어비, 그리고 고스트 로보틱스를 공동 창업한 하버드 출신 박사후 연구원의 결과물입니다.

## 핵심 내용
2026년 4월 19일, 아너 라이트닝 휴머노이드 로봇이 50분 26초 만에 하프 마라톤을 완주하며 인간 세계 기록을 7분, 2025년 최고 로봇 기록을 거의 2시간 앞질렀습니다. 아너는 어떻게 이를 해냈을까요? 이 성과를 가능하게 한 마법 같은 기술이나 기법이 있을까요? 어떻게 이 회사는 훨씬 더 잘 알려진 유니트리(얼음 배낭을 로봇에 장착해 과열 없이 경주를 완주하려 했다고 알려짐)를 능가할 수 있었을까요? 제 박사 논문은 도약 및 주행 로봇의 구축과 제어에 관한 것이었고, 이후 효율적인 상업용 보행 로봇을 설계하고 구축하려 노력해 왔기에 관련 제약 조건을 어느 정도 이해하고 있습니다. 이 글에서는 근본적인 제약 조건을 살펴보며 이러한 질문에 답하고자 합니다.

### 달리기의 물리학
달리기는 다리가 땅을 밀며 지지하는 '입각기'와 몸이 공중에 떠 있는 '공중기'가 번갈아 나타나는 것으로 구성됩니다. 공중기에는 몸이 중력에 의해 떨어지며 수직 운동량을 잃습니다. 입각기의 다리는 땅을 밀어 수직 운동량을 위쪽으로 전환하고, 다른 다리는 앞으로 흔들려 다음 발 디딜 위치를 준비합니다. 전기 모터는 에너지를 사용해 토크를 생성하며, 토크가 높을수록 더 많은 에너지가 열로 손실됩니다. 모터 뒤에 기어 트레인을 추가하면 토크는 증폭되고 속도는 감소합니다. 큰 감속비는 토크 생성에 도움이 되지만, 모터 자체의 회전자가 더 빨리 돌아야 하므로 출력 가속이 매우 느려집니다. 이는 위에서 설명한 스윙 단계에 분명히 불리합니다. 이러한 상충 효과로 인해 특정 모터에는 일반적으로 최적의 기어비가 존재합니다. 로봇 다리가 소비하는 전력은 최적 기어비(이 예에서는 30:1)에서 최소화됩니다.

### 아너가 해낸 방법
라이트닝의 모터 사양은 공개되지 않았지만, 엉덩이와 무릎 모터의 외경은 대략 110~150mm입니다. 대략적인 모터 파라미터 세트를 위해 관련 크기와 상세 사양을 가진 ILM115x25 모터를 참고했습니다. 간단한 물리 모델을 사용해 기어비 변화에 따른 초속 7미터(라이트닝의 평균 하프 마라톤 속도) 주행 시 전력 소비를 추정할 수 있습니다. 연한 파란색 곡선은 최적 기어비(45:1)를 선택하는 방법을 보여줍니다. 진한 파란색 곡선은 최적 기어비에서 무릎 모터에서 발생하는 열(약 150W)을 나타냅니다. 구동계가 마법 같지는 않습니다. 이 작업에 맞춰 선택된 기어비(이에 대해서는 아래에서 다시 다루겠습니다)에서 로봇의 대략적인 전력 소비는 매우 합리적인 400와트가 됩니다. 그러나 무릎에서 소산되는 전력(일반적으로 주요 열 제한 요소)은 약 150W입니다. 이는 거의 피할 수 없는 결과입니다. 인간 크기의 휴머노이드 로봇이 인간 속도로 달리면 필연적으로 이 정도의 열이 발생합니다! 장시간 동안 모터 과열을 막는 것은 어려운 일이지만, 라이트닝에는 비장의 카드가 있습니다. 아너에 따르면 액체 냉각 파이프가 모세혈관처럼 모터 내부 깊숙이 침투합니다. 고출력 액체 펌프는 분당 4리터 이상의 열교환 유량을 가집니다. 하체의 4개 구동 모터 각각에는 독립적인 액체 냉각 회로가 장착되어 있습니다. 액체 냉각은 새로운 기술은 아니지만, 확실히 일반적인 기술은 아닙니다. 연구 분야에서 주기적으로 등장했으며, 상업적으로는 앱트로닉이 일부 프로토타입에서 시도했지만(제가 알기로는) 주력 플랫폼인 아폴로에는 사용하지 않습니다. 기본적인 공기 대류 기반 냉각으로는 무릎 모터에서 지속적으로 150W를 추출할 수 없으므로, 냉각 기술이 이러한 성능의 핵심 요소입니다.

### 경쟁사들이 따라올 수 없었던 이유
유니트리나 아지봇과 같은 더 잘 알려지고 널리 출시된 휴머노이드 로봇을 포함한 아너의 경쟁사들은 왜 경쟁력이 없었을까요? 동일한 모델을 사용해 상업용 휴머노이드 로봇에게 훨씬 더 보편적이지만 덜 격렬한 활동인 초속 1.5미터 보행에 대한 등가 에너지 그래프를 생성할 수 있습니다. 실선과 점선의 연한 파란색 선은 주행 최적화 설계를, 녹색 선은 보행 최적화 설계를 나타냅니다. 보행에 최적화된 기어비는 훨씬 낮습니다(45:1 대비 30:1). 그러나 주행 시 무릎 모터에서 소산되는 전력(진한 파란색)은 45:1 대비 30:1에서 훨씬 높습니다. 이는 보행 최적화 설계로 달리기 위한 대가입니다. 그래프에 보행 전력에 대한 새로운 녹색 곡선이 추가되었으며, 최적 기어비는 크게 다릅니다! 로봇을 일반적인 보행 작업에 탁월하게 설계하고 30:1 기어비의 녹색 설계를 선택한다고 가정해 봅시다. 하프 마라톤을 달리기 위한 무릎 모터 전력은 300W 이상(빨간색 화살표)으로, 주행 최적화 설계의 두 배 이상입니다. 얼음 팩이 필요해도 놀랍지 않을 것입니다! 반대로, 녹색 곡선을 따라가면 주행 최적화 로봇이 보행 시 더 많은 전력을 낭비한다는 것을 알 수 있습니다. 주행에 맞춰 크기가 큰 모터를 사용하면 로봇의 무게가 증가하고, 서 있거나 걸을 때 전력을 낭비합니다. 또한 큰 모터는 가정이나 공장에서 작업 시 물체에 부딪히는 등의 실용적인 문제를 야기합니다.

### 마무리 생각
아너의 하프 마라톤 성과는 인상적인 엔지니어링 노력과 결과였습니다. 마법 같은 기술적 도약은 필요하지 않았지만, 모세관 모터 냉각 솔루션의 배치는 주목할 만한 발전이며, 이것 없이는 이러한 달리기 속도를 유지할 수 없었을 것입니다. 냉각, 무게 최적화, 내구성 향상은 향후 무거운 탑재물 운반과 같은 더 실용적인 목적에 유용하게 쓰일 수 있습니다. 아너 라이팅 로봇(오른쪽)은 유니트리 H1 로봇보다 다리를 구동하는 모터가 훨씬 커서 달리기에는 더 효율적이지만 보행에는 덜 효율적입니다. 그러나 라이트닝은 더 다재다능하게 설계된 로봇만큼 다른 작업에 적합하지는 않습니다. 엔지니어링은 항상 트레이드오프로 특징지어지며, 올바른 선택을 하는 것이 좋은 제품과 훌륭한 제품을 구분짓습니다. 지속적으로 개선되는 AI 언어 모델과 함께, 이러한 인간의 기술은 엔지니어가 가질 수 있는 가장 가치 있는 능력이 되고 있습니다. 언론 보도는 인간 하프 마라톤 기록이 로봇에 의해 깨졌다는 사실에 지나치게 집중하는 경향이 있었습니다. 기계와 인간은 매우 다른 능력과 제약 조건을 가지고 있는데, 왜 로봇과 인간의 하프 마라톤 시간이 관련될 것이라고 기대했을까요? 1997년 딥 블루가 체스에서 게리 카스파로프를 이겼지만 물리적으로 말을 움직일 수 없었던 것처럼, 아너 로봇의 능력은 GPS 없이 시각적으로 코스를 탐색하며 다른 주자들과 나란히 달리는 인간에 비해 훨씬 좁습니다.

## 参考
- https://spectrum.ieee.org/china-humanoid-robot-marathon
