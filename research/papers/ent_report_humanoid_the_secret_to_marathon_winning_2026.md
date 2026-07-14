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
  en: 'On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in
    50 minutes and 26 seconds , beating the human world record by 7 minutes and the
    best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some
    magical technology or technique that unlocked this performance? How did the company
    beat the significantly better-known Unitree (which reportedly had to supply its
    robot with an ice backpack to try and complete the race without overheating)?
    My doctoral thesis involved building and controlling hopping and running robots
    , and since then I’ve tried to design and build efficient commercial legged robots
    , giving me a decent idea of the constraints involved. In this article, we take
    a look at the fundamental underlying constraints to try and answer these questions.
    The Physics of Running Running consists of alternating phases of a leg pushing
    against the ground (“stance phase”) and the body flying through the air (“aerial
    phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum.
    The leg in stance phase pushes against the ground to redirect the vertical momentum
    upward, while the other leg swings forward to reposition for the next foothold.
    Electric motors use energy to produce torque—the higher the torque, the more energy
    is lost as heat. Adding a gear train after the motor amplifies its torque and
    reduces its speed. A large reduction helps with torque production, but since the
    rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating
    its output. This is obviously bad for the swing phase described above. These competing
    effects mean that for a particular motor, there is usually a sweet spot for the
    gear ratio: The power consumed by a robot leg is minimized at an optimal gear
    ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s
    motor specifications are not published, the hip and knee motors roughly have a
    110-to-150-millimeter outer diameter. For an approximate set of motor parameters,
    I looked to the ILM115x25 motor due to its relevant size and detailed specifications.
    We can use a simple physics model to estimate the power consumption for running
    at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio
    varies: The light blue curve shows how to pick the optimal gearing (45:1). The
    dark blue curve shows how much heat will be produced in the knee motor, ~150W
    for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not
    magical: with a gear ratio chosen for this task (we’ll return to this below),
    the approximate robot power consumption would be a very reasonable 400 watts.
    However, the dissipated knee power ( typically the main thermal limiting factor)
    is approximately 150 W. This is almost an unavoidable consequence—running at human
    speeds with a humanoid-size robot will inevitably generate this amount of heat!
    Over a prolonged period, keeping the motor from overheating would be a challenge,
    but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling
    pipes penetrate deep into the motors like capillaries. The high-power liquid pump
    has a heat-exchange flow rate of more than 4 liters per minute. Each of the four
    drive motors in the lower limbs is equipped with an independent liquid-cooling
    circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has
    shown up in research periodically, and on the commercial side Apptronik tried
    it for a few of its prototypes but (to my knowledge) does not use it on its main
    Apollo platform. Basic air-convection-based cooling would not continuously be
    able to extract 150 W out of the knee motor, and so the cooling technology is
    a key enabler of this type of performance. Why Others Couldn’t Compete Why did
    Honor’s competitors, including more established and widely shipped humanoids such
    as from Unitree or Agibot , not compete as well? We can use the same model to
    generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest
    but potentially more common activity for a commercial humanoid robot: The solid
    and dashed light blue lines show a running-optimized design, while green lines
    show a walking-optimized design. The optimal ratio for walking is much lower (30:1
    vs. 45:1). However, the power dissipated in the knee motor while running [dark
    blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized
    design. Avik De/Datawrapper The plot adds a new green curve for the walking power,
    and the optimal gearing is significantly different! Let’s say you design your
    robot to excel at the normal walking task and choose the green design with 30:1
    gearing. The knee motor power to run a half marathon is over 300 W (red arrow),
    more than two times what we had with the running-optimized design. It wouldn’t
    be so surprising to need ice packs! Conversely, visually following the green curve
    shows that the running-optimized robot wastes more power for walking. Using larger
    motors sized for running increases the weight of the robot and wastes power when
    it is standing or walking. The larger motors also pose practical issues like bumping
    into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon
    performance was an impressive engineering effort and result. It didn’t need any
    magical leaps in technology, but the deployment of the capillary motor cooling
    solution is a notable advance without which this running pace would have been
    unsustainable. The cooling, weight optimization, and robustness advances may well
    be useful for more practical purposes like carrying heavy payloads down the line.
    The Honor Lighting robot [right] has much larger motors driving its legs than
    the Unitree H1 robot, making it a more efficient runner but a less efficient walker.
    Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty
    Images However, the Lightning is not as well-suited to other tasks as a robot
    designed for greater versatility. Engineering is always characterized by trade-offs,
    and making the correct ones separates good products from great ones. With consistently
    improving AI language models, this very human skill is becoming the most valuable
    one an engineer can have. The news coverage seemed to overly focus on the fact
    that the human half-marathon record had been broken by a robot. Machines and humans
    have very different capabilities and constraints, so why should we ever have expected
    the half-marathon time for a robot and human to be related? As in Deep Blue’s
    1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the
    pieces, the Honor robot’s capabilities are much narrower than a human running
    elbow to elbow with other runners while visually navigating the course without
    GPS. Comparing the robot runner to a human runner is just an apples-to-oranges
    comparison, which only risks diminishing Honor’s engineering achievement on one
    hand and human athletic achievement on the other.'
  zh: 'On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in
    50 minutes and 26 seconds , beating the human world record by 7 minutes and the
    best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some
    magical technology or technique that unlocked this performance? How did the company
    beat the significantly better-known Unitree (which reportedly had to supply its
    robot with an ice backpack to try and complete the race without overheating)?
    My doctoral thesis involved building and controlling hopping and running robots
    , and since then I’ve tried to design and build efficient commercial legged robots
    , giving me a decent idea of the constraints involved. In this article, we take
    a look at the fundamental underlying constraints to try and answer these questions.
    The Physics of Running Running consists of alternating phases of a leg pushing
    against the ground (“stance phase”) and the body flying through the air (“aerial
    phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum.
    The leg in stance phase pushes against the ground to redirect the vertical momentum
    upward, while the other leg swings forward to reposition for the next foothold.
    Electric motors use energy to produce torque—the higher the torque, the more energy
    is lost as heat. Adding a gear train after the motor amplifies its torque and
    reduces its speed. A large reduction helps with torque production, but since the
    rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating
    its output. This is obviously bad for the swing phase described above. These competing
    effects mean that for a particular motor, there is usually a sweet spot for the
    gear ratio: The power consumed by a robot leg is minimized at an optimal gear
    ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s
    motor specifications are not published, the hip and knee motors roughly have a
    110-to-150-millimeter outer diameter. For an approximate set of motor parameters,
    I looked to the ILM115x25 motor due to its relevant size and detailed specifications.
    We can use a simple physics model to estimate the power consumption for running
    at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio
    varies: The light blue curve shows how to pick the optimal gearing (45:1). The
    dark blue curve shows how much heat will be produced in the knee motor, ~150W
    for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not
    magical: with a gear ratio chosen for this task (we’ll return to this below),
    the approximate robot power consumption would be a very reasonable 400 watts.
    However, the dissipated knee power ( typically the main thermal limiting factor)
    is approximately 150 W. This is almost an unavoidable consequence—running at human
    speeds with a humanoid-size robot will inevitably generate this amount of heat!
    Over a prolonged period, keeping the motor from overheating would be a challenge,
    but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling
    pipes penetrate deep into the motors like capillaries. The high-power liquid pump
    has a heat-exchange flow rate of more than 4 liters per minute. Each of the four
    drive motors in the lower limbs is equipped with an independent liquid-cooling
    circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has
    shown up in research periodically, and on the commercial side Apptronik tried
    it for a few of its prototypes but (to my knowledge) does not use it on its main
    Apollo platform. Basic air-convection-based cooling would not continuously be
    able to extract 150 W out of the knee motor, and so the cooling technology is
    a key enabler of this type of performance. Why Others Couldn’t Compete Why did
    Honor’s competitors, including more established and widely shipped humanoids such
    as from Unitree or Agibot , not compete as well? We can use the same model to
    generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest
    but potentially more common activity for a commercial humanoid robot: The solid
    and dashed light blue lines show a running-optimized design, while green lines
    show a walking-optimized design. The optimal ratio for walking is much lower (30:1
    vs. 45:1). However, the power dissipated in the knee motor while running [dark
    blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized
    design. Avik De/Datawrapper The plot adds a new green curve for the walking power,
    and the optimal gearing is significantly different! Let’s say you design your
    robot to excel at the normal walking task and choose the green design with 30:1
    gearing. The knee motor power to run a half marathon is over 300 W (red arrow),
    more than two times what we had with the running-optimized design. It wouldn’t
    be so surprising to need ice packs! Conversely, visually following the green curve
    shows that the running-optimized robot wastes more power for walking. Using larger
    motors sized for running increases the weight of the robot and wastes power when
    it is standing or walking. The larger motors also pose practical issues like bumping
    into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon
    performance was an impressive engineering effort and result. It didn’t need any
    magical leaps in technology, but the deployment of the capillary motor cooling
    solution is a notable advance without which this running pace would have been
    unsustainable. The cooling, weight optimization, and robustness advances may well
    be useful for more practical purposes like carrying heavy payloads down the line.
    The Honor Lighting robot [right] has much larger motors driving its legs than
    the Unitree H1 robot, making it a more efficient runner but a less efficient walker.
    Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty
    Images However, the Lightning is not as well-suited to other tasks as a robot
    designed for greater versatility. Engineering is always characterized by trade-offs,
    and making the correct ones separates good products from great ones. With consistently
    improving AI language models, this very human skill is becoming the most valuable
    one an engineer can have. The news coverage seemed to overly focus on the fact
    that the human half-marathon record had been broken by a robot. Machines and humans
    have very different capabilities and constraints, so why should we ever have expected
    the half-marathon time for a robot and human to be related? As in Deep Blue’s
    1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the
    pieces, the Honor robot’s capabilities are much narrower than a human running
    elbow to elbow with other runners while visually navigating the course without
    GPS. Comparing the robot runner to a human runner is just an apples-to-oranges
    comparison, which only risks diminishing Honor’s engineering achievement on one
    hand and human athletic achievement on the other.'
  ko: 'On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in
    50 minutes and 26 seconds , beating the human world record by 7 minutes and the
    best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some
    magical technology or technique that unlocked this performance? How did the company
    beat the significantly better-known Unitree (which reportedly had to supply its
    robot with an ice backpack to try and complete the race without overheating)?
    My doctoral thesis involved building and controlling hopping and running robots
    , and since then I’ve tried to design and build efficient commercial legged robots
    , giving me a decent idea of the constraints involved. In this article, we take
    a look at the fundamental underlying constraints to try and answer these questions.
    The Physics of Running Running consists of alternating phases of a leg pushing
    against the ground (“stance phase”) and the body flying through the air (“aerial
    phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum.
    The leg in stance phase pushes against the ground to redirect the vertical momentum
    upward, while the other leg swings forward to reposition for the next foothold.
    Electric motors use energy to produce torque—the higher the torque, the more energy
    is lost as heat. Adding a gear train after the motor amplifies its torque and
    reduces its speed. A large reduction helps with torque production, but since the
    rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating
    its output. This is obviously bad for the swing phase described above. These competing
    effects mean that for a particular motor, there is usually a sweet spot for the
    gear ratio: The power consumed by a robot leg is minimized at an optimal gear
    ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s
    motor specifications are not published, the hip and knee motors roughly have a
    110-to-150-millimeter outer diameter. For an approximate set of motor parameters,
    I looked to the ILM115x25 motor due to its relevant size and detailed specifications.
    We can use a simple physics model to estimate the power consumption for running
    at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio
    varies: The light blue curve shows how to pick the optimal gearing (45:1). The
    dark blue curve shows how much heat will be produced in the knee motor, ~150W
    for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not
    magical: with a gear ratio chosen for this task (we’ll return to this below),
    the approximate robot power consumption would be a very reasonable 400 watts.
    However, the dissipated knee power ( typically the main thermal limiting factor)
    is approximately 150 W. This is almost an unavoidable consequence—running at human
    speeds with a humanoid-size robot will inevitably generate this amount of heat!
    Over a prolonged period, keeping the motor from overheating would be a challenge,
    but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling
    pipes penetrate deep into the motors like capillaries. The high-power liquid pump
    has a heat-exchange flow rate of more than 4 liters per minute. Each of the four
    drive motors in the lower limbs is equipped with an independent liquid-cooling
    circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has
    shown up in research periodically, and on the commercial side Apptronik tried
    it for a few of its prototypes but (to my knowledge) does not use it on its main
    Apollo platform. Basic air-convection-based cooling would not continuously be
    able to extract 150 W out of the knee motor, and so the cooling technology is
    a key enabler of this type of performance. Why Others Couldn’t Compete Why did
    Honor’s competitors, including more established and widely shipped humanoids such
    as from Unitree or Agibot , not compete as well? We can use the same model to
    generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest
    but potentially more common activity for a commercial humanoid robot: The solid
    and dashed light blue lines show a running-optimized design, while green lines
    show a walking-optimized design. The optimal ratio for walking is much lower (30:1
    vs. 45:1). However, the power dissipated in the knee motor while running [dark
    blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized
    design. Avik De/Datawrapper The plot adds a new green curve for the walking power,
    and the optimal gearing is significantly different! Let’s say you design your
    robot to excel at the normal walking task and choose the green design with 30:1
    gearing. The knee motor power to run a half marathon is over 300 W (red arrow),
    more than two times what we had with the running-optimized design. It wouldn’t
    be so surprising to need ice packs! Conversely, visually following the green curve
    shows that the running-optimized robot wastes more power for walking. Using larger
    motors sized for running increases the weight of the robot and wastes power when
    it is standing or walking. The larger motors also pose practical issues like bumping
    into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon
    performance was an impressive engineering effort and result. It didn’t need any
    magical leaps in technology, but the deployment of the capillary motor cooling
    solution is a notable advance without which this running pace would have been
    unsustainable. The cooling, weight optimization, and robustness advances may well
    be useful for more practical purposes like carrying heavy payloads down the line.
    The Honor Lighting robot [right] has much larger motors driving its legs than
    the Unitree H1 robot, making it a more efficient runner but a less efficient walker.
    Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty
    Images However, the Lightning is not as well-suited to other tasks as a robot
    designed for greater versatility. Engineering is always characterized by trade-offs,
    and making the correct ones separates good products from great ones. With consistently
    improving AI language models, this very human skill is becoming the most valuable
    one an engineer can have. The news coverage seemed to overly focus on the fact
    that the human half-marathon record had been broken by a robot. Machines and humans
    have very different capabilities and constraints, so why should we ever have expected
    the half-marathon time for a robot and human to be related? As in Deep Blue’s
    1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the
    pieces, the Honor robot’s capabilities are much narrower than a human running
    elbow to elbow with other runners while visually navigating the course without
    GPS. Comparing the robot runner to a human runner is just an apples-to-oranges
    comparison, which only risks diminishing Honor’s engineering achievement on one
    hand and human athletic achievement on the other.'
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website.
sources:
- id: src_001
  type: website
  title: The Secret to Marathon-Winning Humanoid Robots
  url: https://spectrum.ieee.org/china-humanoid-robot-marathon
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds , beating the human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some magical technology or technique that unlocked this performance? How did the company beat the significantly better-known Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)? My doctoral thesis involved building and controlling hopping and running robots , and since then I’ve tried to design and build efficient commercial legged robots , giving me a decent idea of the constraints involved. In this article, we take a look at the fundamental underlying constraints to try and answer these questions. The Physics of Running Running consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for the next foothold. Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat. Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production, but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there is usually a sweet spot for the gear ratio: The power consumed by a robot leg is minimized at an optimal gear ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s motor specifications are not published, the hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio varies: The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much heat will be produced in the knee motor, ~150W for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption would be a very reasonable 400 watts. However, the dissipated knee power ( typically the main thermal limiting factor) is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge, but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling pipes penetrate deep into the motors like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key enabler of this type of performance. Why Others Couldn’t Compete Why did Honor’s competitors, including more established and widely shipped humanoids such as from Unitree or Agibot , not compete as well? We can use the same model to generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial humanoid robot: The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design. Avik De/Datawrapper The plot adds a new green curve for the walking power, and the optimal gearing is significantly different! Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon performance was an impressive engineering effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization, and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line. The Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient runner but a less efficient walker. Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently improving AI language models, this very human skill is becoming the most valuable one an engineer can have. The news coverage seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while visually navigating the course without GPS. Comparing the robot runner to a human runner is just an apples-to-oranges comparison, which only risks diminishing Honor’s engineering achievement on one hand and human athletic achievement on the other.

## Overview
On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds , beating the human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some magical technology or technique that unlocked this performance? How did the company beat the significantly better-known Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)? My doctoral thesis involved building and controlling hopping and running robots , and since then I’ve tried to design and build efficient commercial legged robots , giving me a decent idea of the constraints involved. In this article, we take a look at the fundamental underlying constraints to try and answer these questions. The Physics of Running Running consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for the next foothold. Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat. Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production, but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there is usually a sweet spot for the gear ratio: The power consumed by a robot leg is minimized at an optimal gear ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s motor specifications are not published, the hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio varies: The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much heat will be produced in the knee motor, ~150W for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption would be a very reasonable 400 watts. However, the dissipated knee power ( typically the main thermal limiting factor) is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge, but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling pipes penetrate deep into the motors like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key enabler of this type of performance. Why Others Couldn’t Compete Why did Honor’s competitors, including more established and widely shipped humanoids such as from Unitree or Agibot , not compete as well? We can use the same model to generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial humanoid robot: The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design. Avik De/Datawrapper The plot adds a new green curve for the walking power, and the optimal gearing is significantly different! Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon performance was an impressive engineering effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization, and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line. The Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient runner but a less efficient walker. Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently improving AI language models, this very human skill is becoming the most valuable one an engineer can have. The news coverage seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while visually navigating the course without GPS. Comparing the robot runner to a human runner is just an apples-to-oranges comparison, which only risks diminishing Honor’s engineering achievement on one hand and human athletic achievement on the other.

## 개요
On 19 April 2026, the Honor Lightning humanoid robot ran a half-marathon in 50 minutes and 26 seconds , beating the human world record by 7 minutes and the best robot time from 2025 by almost 2 hours. How did Honor do it? Is there some magical technology or technique that unlocked this performance? How did the company beat the significantly better-known Unitree (which reportedly had to supply its robot with an ice backpack to try and complete the race without overheating)? My doctoral thesis involved building and controlling hopping and running robots , and since then I’ve tried to design and build efficient commercial legged robots , giving me a decent idea of the constraints involved. In this article, we take a look at the fundamental underlying constraints to try and answer these questions. The Physics of Running Running consists of alternating phases of a leg pushing against the ground (“stance phase”) and the body flying through the air (“aerial phase”). In the aerial phase, the body falls due to gravity, losing vertical momentum. The leg in stance phase pushes against the ground to redirect the vertical momentum upward, while the other leg swings forward to reposition for the next foothold. Electric motors use energy to produce torque—the higher the torque, the more energy is lost as heat. Adding a gear train after the motor amplifies its torque and reduces its speed. A large reduction helps with torque production, but since the rotor of the motor itself has to spin faster, it becomes very sluggish at accelerating its output. This is obviously bad for the swing phase described above. These competing effects mean that for a particular motor, there is usually a sweet spot for the gear ratio: The power consumed by a robot leg is minimized at an optimal gear ratio (30:1 in this example). Avik De/Datawrapper How Honor Did It While the Lightning’s motor specifications are not published, the hip and knee motors roughly have a 110-to-150-millimeter outer diameter. For an approximate set of motor parameters, I looked to the ILM115x25 motor due to its relevant size and detailed specifications. We can use a simple physics model to estimate the power consumption for running at 7 meters per second (the Lightning’s average half-marathon speed) as gear ratio varies: The light blue curve shows how to pick the optimal gearing (45:1). The dark blue curve shows how much heat will be produced in the knee motor, ~150W for the optimal gearing. Avik De/Datawrapper We see that the drivetrain is not magical: with a gear ratio chosen for this task (we’ll return to this below), the approximate robot power consumption would be a very reasonable 400 watts. However, the dissipated knee power ( typically the main thermal limiting factor) is approximately 150 W. This is almost an unavoidable consequence—running at human speeds with a humanoid-size robot will inevitably generate this amount of heat! Over a prolonged period, keeping the motor from overheating would be a challenge, but the Lightning has a trick up its sleeve : According to Honor, the liquid-cooling pipes penetrate deep into the motors like capillaries. The high-power liquid pump has a heat-exchange flow rate of more than 4 liters per minute. Each of the four drive motors in the lower limbs is equipped with an independent liquid-cooling circuit. Liquid cooling is not new, but it’s definitely not a commodity. It has shown up in research periodically, and on the commercial side Apptronik tried it for a few of its prototypes but (to my knowledge) does not use it on its main Apollo platform. Basic air-convection-based cooling would not continuously be able to extract 150 W out of the knee motor, and so the cooling technology is a key enabler of this type of performance. Why Others Couldn’t Compete Why did Honor’s competitors, including more established and widely shipped humanoids such as from Unitree or Agibot , not compete as well? We can use the same model to generate an equivalent energetics plot for walking at 1.5 m/s, a much more modest but potentially more common activity for a commercial humanoid robot: The solid and dashed light blue lines show a running-optimized design, while green lines show a walking-optimized design. The optimal ratio for walking is much lower (30:1 vs. 45:1). However, the power dissipated in the knee motor while running [dark blue] is much higher at 30:1 vs. 45:1—the price to pay for running with a walking-optimized design. Avik De/Datawrapper The plot adds a new green curve for the walking power, and the optimal gearing is significantly different! Let’s say you design your robot to excel at the normal walking task and choose the green design with 30:1 gearing. The knee motor power to run a half marathon is over 300 W (red arrow), more than two times what we had with the running-optimized design. It wouldn’t be so surprising to need ice packs! Conversely, visually following the green curve shows that the running-optimized robot wastes more power for walking. Using larger motors sized for running increases the weight of the robot and wastes power when it is standing or walking. The larger motors also pose practical issues like bumping into objects while operating in homes or factories. Closing Thoughts Honor’s half-marathon performance was an impressive engineering effort and result. It didn’t need any magical leaps in technology, but the deployment of the capillary motor cooling solution is a notable advance without which this running pace would have been unsustainable. The cooling, weight optimization, and robustness advances may well be useful for more practical purposes like carrying heavy payloads down the line. The Honor Lighting robot [right] has much larger motors driving its legs than the Unitree H1 robot, making it a more efficient runner but a less efficient walker. Left: Wei Zhiyang/Zhejiang Daily Press Group/VCG/Getty Images; Right: VCG/Getty Images However, the Lightning is not as well-suited to other tasks as a robot designed for greater versatility. Engineering is always characterized by trade-offs, and making the correct ones separates good products from great ones. With consistently improving AI language models, this very human skill is becoming the most valuable one an engineer can have. The news coverage seemed to overly focus on the fact that the human half-marathon record had been broken by a robot. Machines and humans have very different capabilities and constraints, so why should we ever have expected the half-marathon time for a robot and human to be related? As in Deep Blue’s 1997 defeat of Garry Kasparov in chess , where it couldn’t physically move the pieces, the Honor robot’s capabilities are much narrower than a human running elbow to elbow with other runners while visually navigating the course without GPS. Comparing the robot runner to a human runner is just an apples-to-oranges comparison, which only risks diminishing Honor’s engineering achievement on one hand and human athletic achievement on the other.
