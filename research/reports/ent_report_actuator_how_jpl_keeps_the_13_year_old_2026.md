---
$id: ent_report_actuator_how_jpl_keeps_the_13_year_old_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: How JPL Keeps the 13-Year-Old Curiosity Rover Doing Science
  zh: How JPL Keeps the 13-Year-Old Curiosity Rover Doing Science
  ko: How JPL Keeps the 13-Year-Old Curiosity Rover Doing Science
summary:
  en: 'Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif.,
    waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars.
    It did, and it was awesome . Since then, Curiosity (also known as Mars Science Laboratory) has traveled nearly 37 kilometers
    , drilled into and sampled 42 different rocks , and as of publication has snapped nearly 763,000 photos . The fact that
    this robot is still hard at work , getting real science done at the age of 13, is absolutely incredible—not only is Mars
    an actively hostile environment for robots, but the only kind of maintenance that JPL engineers can do is to send very,
    very careful software updates. Nevertheless, the clever folks at JPL have managed to keep Curiosity safe, warm, mobile,
    and sciencing, despite well-worn wheels and less and less power every day. One of those folks is Alexandra Holloway ,
    the assistant team chief for engineering operations for Curiosity, who spoke to IEEE Spectrum about keeping Curiosity
    roving, what its future looks like, and how JPL has used that experience to make rovers like Perseverance even more capable.
    How astonished should we be that after 13 years on Mars, Curiosity is not only still doing science, but actually getting
    more capable? Alexandra Holloway is the assistant team chief for engineering operations on the Curiosity Mars rover at
    the Jet Propulsion Laboratory. Alexandra Holloway Alexandra Holloway: I’m astonished! The longevity comes from a lot of
    ongoing work. It’s not just that Curiosity was built robustly; it’s also because we’re continuously putting in effort
    to ensure it can continue to have that lifespan. I think about all the different kinds of embedded systems there are,
    from cars to refrigerators, and none of them have the kind of longevity that we have with the rover. It’s mind-boggling,
    and it’s inspiring. Is the Perseverance rover , which is nine years younger than Curiosity, significantly different in
    terms of its hardware and software? Holloway: In terms of hardware, the rovers are actually very similar. Both use a RAD
    750 processor and have the same amount of memory. However, Perseverance has an extra processor specifically for visual
    odometry, which allows it to drive autonomously. This difference reflects their primary mission designs : Perseverance
    was designed for driving long distances, while Curiosity is a mission focused on sampling as it goes. So Perseverance’s
    onboard scheduling capabilities are there to optimize its driving. In fact, just last year, Perseverance surpassed Curiosity’s
    driving distance after only about three years on Mars. Curiosity Rover Memory and Software Fixes Do you have some examples
    of significant tweaks the team has made to keep Curiosity roving? Holloway: One of my favorite examples comes from a processor
    anomaly that happened on Sol 2172 [Ed. note: “Sol” is the term for a Martian day—about 24 hours and 40 minutes]. Curiosity
    has two computers, A and B. We landed on A, swapped to B due to a NAND memory anomaly early on (Sol 200) . For years,
    we were chugging along on B, until one day there was a problem—B booted up, but it couldn’t mount its drive partition.
    We’d never seen this before. To preserve B’s data, we swapped back to A, which we hadn’t trusted in two thousand Sols.
    A also had a degraded memory, with only two gigabytes of usable storage space instead of four. We painstakingly transferred
    data from B over to A and then down to Earth, and eventually we ran out of stuff we wanted to transfer, which was really
    good, because A then started acting funny in the same way it did on Sol 200. It was acting like its memory was coming
    unsoldered. That’s bad. We quickly swapped back to B, formatted it, and got it working again. The problem then became
    that we couldn’t trust A’s memory at all, but we needed a second computer as a “lifeboat” for diagnostics and transfers
    if B failed again. We realized we had one other place of memory: where we keep our flight software. We have four copies
    of the flight software (two current versions and two older versions) in different banks of very small amounts of memory,
    just 32 megabytes each. What if we just jettisoned the old flight software copies and used that 64-megabyte NOR memory
    as our file system for computer A? So that’s what we did . It was so elegant! Computer A is operating with less than 1
    percent of its original memory, but we can run a mission on it. A small mission, but we haven’t had to jettison any core
    capabilities. We can still drive, we can manage data, we can even theoretically do science. Everything works fine, just
    much slower and much smaller. That flight software release was even called “ R-Hope “ because we hoped it would work.
    What are the constraints on Curiosity’s lifespan? Holloway: Our biggest hardware challenge is wheel wear . It looks like
    we’re driving on this sandy terrain with some rocks in it, and our intuition said that we could just drive over these
    rocks and they’d get pushed down into the sand and it would be no big deal. But what we ended up seeing was that those
    little rocks are actually the tips of giant boulders buried in the sand, and they’re razor sharp. Our wheels were getting
    ripped apart driving over them, especially our front wheels, so we started driving backwards . We also monitor consumables.
    We consider the number of times we move our actuators. That’s a consumable. Curiosity hasn’t taken a selfie in a while,
    and one of the reasons is that it’s really hard on the joint actuators. Our onboard memory is a consumable, but surprisingly
    we’re not anywhere near our life cycle for memory. Our biggest consumable is power; we have an RTG , a nuclear power source,
    which decreases its output as it ages. Newer missions are flying Snapdragon [processors], but Curiosity’s RAD 750 is a
    power hog. One of the things that we’ve rolled out that’s going really well is a way of reducing the amount of time we
    spend with the computer powered on, by harvesting time when we finish activities early and going to sleep, which lets
    us turn off the computers and some of the heating. Another thing we’re looking at is doing stuff in parallel when we’re
    on, like being able to drive or use the arm while communicating with an orbiter. So power is decreasing, and that’s causing
    us to do all this parallelism work and become more efficient and nuanced in the way we operate. But we are not having
    any degraded science output at this time. Our wheels are still going, our arm is still okay for now, knock on wood. I
    would say maybe the bottleneck is budget. Curiosity Rover’s Impact on Future Mars Exploration What have you learned from
    Curiosity that will improve future missions? Holloway: As an embedded flight software person, I think about how we can
    change, add, or modify software capabilities during the mission. There’s definitely a sweet spot for loading and patching
    flight software—some of these concepts were pioneered on Spirit and Opportunity and then inherited by Curiosity and Perseverance,
    making it easier to understand and change the software. Some of the things that I wish we had now on [the Mars Science
    Laboratory] include a better understanding of where our power is going. I want to see how much power each component is
    drawing every minute, so that we could architect a software system that could balance loads better. We have some of this
    information that was built in by the engineers who designed the rover, but as an operator, I want something slightly different.
    So if I were building a mission, I would have those discussions earlier and get operators into the room to say, “what
    do you want your data products to look like?” The key takeaway for designing future missions is to talk to all your users
    early in the design process. It needs to happen upfront. What does Curiosity’s long-term future look like? Holloway: That’s
    a conversation that happens, and it’s a really delicate one. We have a lot of science instruments, and a lot of them have
    to do with contact science and sampling and rely on the arm. If we lose the arm, what science can we still do? Well, we
    have a lot of remote sensors too, like cameras, environmental sensors, and radiation sensors. All of these things are
    important for the future of space exploration and humans on Mars. From a power perspective, our RTG is projected to start
    degrading science output in the sixth extended mission, but we’re going to be fine through 2035 and potentially even beyond
    that. So we have a long and exciting future ahead of us. We need to figure out the best way of operating within our constraints,
    but we’re still kicking.'
  zh: NASA JPL的Alexandra Holloway介绍了13岁高龄的Curiosity火星车如何通过巧妙的软件更新和操作策略持续进行科学探测。该火星车已行驶近37公里，钻取42个岩石样本，拍摄约76.3万张照片，尽管面临车轮磨损和核电源功率下降等挑战，仍保持活跃。JPL团队通过回收空闲时间休眠、并行操作以及创造性地利用仅64MB的NOR内存作为备用计算机文件系统等创新方法，延长了其寿命。
  ko: 'Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif.,
    waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars.
    It did, and it was awesome . Since then, Curiosity (also known as Mars Science Laboratory) has traveled nearly 37 kilometers
    , drilled into and sampled 42 different rocks , and as of publication has snapped nearly 763,000 photos . The fact that
    this robot is still hard at work , getting real science done at the age of 13, is absolutely incredible—not only is Mars
    an actively hostile environment for robots, but the only kind of maintenance that JPL engineers can do is to send very,
    very careful software updates. Nevertheless, the clever folks at JPL have managed to keep Curiosity safe, warm, mobile,
    and sciencing, despite well-worn wheels and less and less power every day. One of those folks is Alexandra Holloway ,
    the assistant team chief for engineering operations for Curiosity, who spoke to IEEE Spectrum about keeping Curiosity
    roving, what its future looks like, and how JPL has used that experience to make rovers like Perseverance even more capable.
    How astonished should we be that after 13 years on Mars, Curiosity is not only still doing science, but actually getting
    more capable? Alexandra Holloway is the assistant team chief for engineering operations on the Curiosity Mars rover at
    the Jet Propulsion Laboratory. Alexandra Holloway Alexandra Holloway: I’m astonished! The longevity comes from a lot of
    ongoing work. It’s not just that Curiosity was built robustly; it’s also because we’re continuously putting in effort
    to ensure it can continue to have that lifespan. I think about all the different kinds of embedded systems there are,
    from cars to refrigerators, and none of them have the kind of longevity that we have with the rover. It’s mind-boggling,
    and it’s inspiring. Is the Perseverance rover , which is nine years younger than Curiosity, significantly different in
    terms of its hardware and software? Holloway: In terms of hardware, the rovers are actually very similar. Both use a RAD
    750 processor and have the same amount of memory. However, Perseverance has an extra processor specifically for visual
    odometry, which allows it to drive autonomously. This difference reflects their primary mission designs : Perseverance
    was designed for driving long distances, while Curiosity is a mission focused on sampling as it goes. So Perseverance’s
    onboard scheduling capabilities are there to optimize its driving. In fact, just last year, Perseverance surpassed Curiosity’s
    driving distance after only about three years on Mars. Curiosity Rover Memory and Software Fixes Do you have some examples
    of significant tweaks the team has made to keep Curiosity roving? Holloway: One of my favorite examples comes from a processor
    anomaly that happened on Sol 2172 [Ed. note: “Sol” is the term for a Martian day—about 24 hours and 40 minutes]. Curiosity
    has two computers, A and B. We landed on A, swapped to B due to a NAND memory anomaly early on (Sol 200) . For years,
    we were chugging along on B, until one day there was a problem—B booted up, but it couldn’t mount its drive partition.
    We’d never seen this before. To preserve B’s data, we swapped back to A, which we hadn’t trusted in two thousand Sols.
    A also had a degraded memory, with only two gigabytes of usable storage space instead of four. We painstakingly transferred
    data from B over to A and then down to Earth, and eventually we ran out of stuff we wanted to transfer, which was really
    good, because A then started acting funny in the same way it did on Sol 200. It was acting like its memory was coming
    unsoldered. That’s bad. We quickly swapped back to B, formatted it, and got it working again. The problem then became
    that we couldn’t trust A’s memory at all, but we needed a second computer as a “lifeboat” for diagnostics and transfers
    if B failed again. We realized we had one other place of memory: where we keep our flight software. We have four copies
    of the flight software (two current versions and two older versions) in different banks of very small amounts of memory,
    just 32 megabytes each. What if we just jettisoned the old flight software copies and used that 64-megabyte NOR memory
    as our file system for computer A? So that’s what we did . It was so elegant! Computer A is operating with less than 1
    percent of its original memory, but we can run a mission on it. A small mission, but we haven’t had to jettison any core
    capabilities. We can still drive, we can manage data, we can even theoretically do science. Everything works fine, just
    much slower and much smaller. That flight software release was even called “ R-Hope “ because we hoped it would work.
    What are the constraints on Curiosity’s lifespan? Holloway: Our biggest hardware challenge is wheel wear . It looks like
    we’re driving on this sandy terrain with some rocks in it, and our intuition said that we could just drive over these
    rocks and they’d get pushed down into the sand and it would be no big deal. But what we ended up seeing was that those
    little rocks are actually the tips of giant boulders buried in the sand, and they’re razor sharp. Our wheels were getting
    ripped apart driving over them, especially our front wheels, so we started driving backwards . We also monitor consumables.
    We consider the number of times we move our actuators. That’s a consumable. Curiosity hasn’t taken a selfie in a while,
    and one of the reasons is that it’s really hard on the joint actuators. Our onboard memory is a consumable, but surprisingly
    we’re not anywhere near our life cycle for memory. Our biggest consumable is power; we have an RTG , a nuclear power source,
    which decreases its output as it ages. Newer missions are flying Snapdragon [processors], but Curiosity’s RAD 750 is a
    power hog. One of the things that we’ve rolled out that’s going really well is a way of reducing the amount of time we
    spend with the computer powered on, by harvesting time when we finish activities early and going to sleep, which lets
    us turn off the computers and some of the heating. Another thing we’re looking at is doing stuff in parallel when we’re
    on, like being able to drive or use the arm while communicating with an orbiter. So power is decreasing, and that’s causing
    us to do all this parallelism work and become more efficient and nuanced in the way we operate. But we are not having
    any degraded science output at this time. Our wheels are still going, our arm is still okay for now, knock on wood. I
    would say maybe the bottleneck is budget. Curiosity Rover’s Impact on Future Mars Exploration What have you learned from
    Curiosity that will improve future missions? Holloway: As an embedded flight software person, I think about how we can
    change, add, or modify software capabilities during the mission. There’s definitely a sweet spot for loading and patching
    flight software—some of these concepts were pioneered on Spirit and Opportunity and then inherited by Curiosity and Perseverance,
    making it easier to understand and change the software. Some of the things that I wish we had now on [the Mars Science
    Laboratory] include a better understanding of where our power is going. I want to see how much power each component is
    drawing every minute, so that we could architect a software system that could balance loads better. We have some of this
    information that was built in by the engineers who designed the rover, but as an operator, I want something slightly different.
    So if I were building a mission, I would have those discussions earlier and get operators into the room to say, “what
    do you want your data products to look like?” The key takeaway for designing future missions is to talk to all your users
    early in the design process. It needs to happen upfront. What does Curiosity’s long-term future look like? Holloway: That’s
    a conversation that happens, and it’s a really delicate one. We have a lot of science instruments, and a lot of them have
    to do with contact science and sampling and rely on the arm. If we lose the arm, what science can we still do? Well, we
    have a lot of remote sensors too, like cameras, environmental sensors, and radiation sensors. All of these things are
    important for the future of space exploration and humans on Mars. From a power perspective, our RTG is projected to start
    degrading science output in the sixth extended mission, but we’re going to be fine through 2035 and potentially even beyond
    that. So we have a long and exciting future ahead of us. We need to figure out the best way of operating within our constraints,
    but we’re still kicking.'
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
- ieee
- iso
- report
- robotics
- sensor
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/curiosity-rover-jpl-mars-science.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1841 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: How JPL Keeps the 13-Year-Old Curiosity Rover Doing Science
  url: https://spectrum.ieee.org/curiosity-rover-jpl-mars-science
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
NASA JPL的Curiosity火星车助理工程运营主管Alexandra Holloway向IEEE Spectrum讲述了如何让这台13岁的机器人持续工作。Curiosity已行驶近37公里，钻取42个岩石样本，拍摄约76.3万张照片，尽管面临火星恶劣环境、车轮磨损和核电源功率逐年下降等挑战，JPL团队通过发送精心设计的软件更新来维持其运行。Holloway分享了团队如何通过回收任务间隙时间休眠、并行操作以及将旧飞行软件内存改造为备用计算机文件系统等创新方法，使Curiosity在硬件老化的条件下仍能保持科学产出。她还对比了Curiosity与较年轻的Perseverance火星车在硬件和任务设计上的差异，并讨论了未来任务的设计经验。

## 核心内容
### 任务概况与关键数字
- Curiosity（又称Mars Science Laboratory）于13年前成功着陆火星，至今已行驶近37公里，钻取并采样42块岩石，拍摄约76.3万张照片。
- 火星环境对机器人极为恶劣，JPL工程师只能通过发送极其谨慎的软件更新进行维护。

### 硬件与软件对比：Curiosity vs. Perseverance
- **硬件相似性**：两辆火星车均使用RAD 750处理器，内存容量相同。
- **关键差异**：Perseverance额外配备了一个专用于视觉里程计的处理器，使其能够自主驾驶。这反映了任务设计的不同——Perseverance旨在长距离行驶，而Curiosity侧重于沿途采样。
- **性能对比**：Perseverance在火星上仅约三年后，其行驶距离便超过了Curiosity。

### 内存与软件修复案例
- **处理器异常事件**：在Sol 2172（火星日，约24小时40分钟），Curiosity的B计算机启动后无法挂载驱动分区。团队被迫切换回已闲置2000个火星日的A计算机，但其内存退化，可用存储仅2GB（原为4GB）。
- **数据抢救**：团队将B计算机的数据艰难传输至A计算机并下载到地球。随后A计算机出现类似Sol 200时的内存脱焊迹象，团队迅速切回B计算机并格式化修复。
- **创新解决方案**：为保留备用“救生艇”计算机，团队决定放弃旧版飞行软件，将存放飞行软件的64MB NOR内存（原用于存储4份飞行软件，每份32MB）改造为A计算机的文件系统。这一软件版本被命名为“R-Hope”，寓意希望其能工作。目前A计算机以不到原始内存1%的容量运行，但仍能执行驾驶、数据管理甚至科学任务，只是速度更慢、规模更小。

### 寿命限制与应对策略
- **最大硬件挑战：车轮磨损**。火星表面看似沙地，实则埋藏着尖锐巨石，导致车轮（尤其是前轮）严重受损。团队因此开始倒车行驶。
- **消耗品监控**：
  - **执行器运动次数**：被视为消耗品，例如自拍对关节执行器损耗大，因此近期未进行。
  - **内存**：出乎意料地远未达到寿命周期。
  - **最大消耗品：功率**。Curiosity的核电源RTG输出随年龄下降，而RAD 750处理器功耗较高。
- **节能措施**：
  - **回收空闲时间**：提前完成任务后让计算机休眠，关闭部分加热系统。
  - **并行操作**：在保持通信的同时进行驾驶或机械臂操作。
- **当前状态**：尽管功率下降，但科学产出未受影响。车轮和机械臂仍可正常工作。Holloway指出，预算可能成为未来的瓶颈。

### 对未来任务的影响
- **软件灵活性**：Curiosity的经验表明，在任务中更改、添加或修改软件能力至关重要。Spirit和Opportunity开创的软件加载与补丁概念被Curiosity和Perseverance继承。
- **改进建议**：Holloway希望未来任务能更精细地监控每个组件的实时功耗，以便设计负载平衡软件系统。关键教训是：在设计初期就让操作人员参与讨论数据产品需求。

### 长期展望
- **科学能力**：若失去机械臂，Curiosity仍可依靠远程传感器（相机、环境传感器、辐射传感器）进行对太空探索和人类登火有重要意义的科学工作。
- **功率预测**：RTG预计在第六次扩展任务中开始影响科学产出，但Curiosity至少可正常运行至2035年甚至更久。团队正在探索在约束条件下最佳的操作方式。

## Overview
It takes some special tricks to maintain a robot 200 million kilometers from home Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif., waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars.

Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif., waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars. It did, and it was awesome . Since then, Curiosity (also known as Mars Science Laboratory) has traveled nearly 37 kilometers , drilled into and sampled 42 different rocks , and as of publication has snapped nearly 763,000 photos . The fact that this robot is still hard at work , getting real science done at the age of 13, is absolutely incredible—not only is Mars an actively hostile environment for robots, but the only kind of maintenance that JPL engineers can do is to send very, very careful software updates. Nevertheless, the clever folks at JPL have managed to keep Curiosity safe, warm, mobile, and sciencing, despite well-worn wheels and less and less power every day. One of those folks is Alexandra Holloway , the assistant team chief for engineering operations for Curiosity, who spoke to IEEE Spectrum about keeping Curiosity roving, what its future looks like, and how JPL has used that experience to make rovers like Perseverance even more capable. How astonished should we be that after 13 years on Mars, Curiosity is not only still doing science, but actually getting more capable? Alexandra Holloway is the assistant team chief for engineering operations on the Curiosity Mars rover at the Jet Propulsion Laboratory. Alexandra Holloway Alexandra Holloway: I’m astonished! The longevity comes from a lot of ongoing work. It’s not just that Curiosity was built robustly; it’s also because we’re continuously putting in effort to ensure it can continue to have that lifespan. I think about all the different kinds of embedded systems there are, from cars to refrigerators, and none of them have the kind of longevity that we have with the rover. It’s mind-boggling, and it’s inspiring. Is the Perseverance rover , which is nine years younger than Curiosity, significantly different in terms of its hardware and software? Holloway: In terms of hardware, the rovers are actually very similar. Both use a RAD 750 processor and have the same amount of memory. However, Perseverance has an extra processor specifically for visual odometry, which allows it to drive autonomously. This difference reflects their primary mission designs : Perseverance was designed for driving long distances, while Curiosity is a mission focused on sampling as it goes. So Perseverance’s onboard scheduling capabilities are there to optimize its driving. In fact, just last year, Perseverance surpassed Curiosity’s driving distance after only about three years on Mars. Curiosity Rover Memory and Software Fixes Do you have some examples of significant tweaks the team has made to keep Curiosity roving? Holloway: One of my favorite examples comes from a processor anomaly that happened on Sol 2172 [Ed. note: “Sol” is the term for a Martian day—about 24 hours and 40 minutes]. Curiosity has two computers, A and B. We landed on A, swapped to B due to a NAND memory anomaly early on (Sol 200) . For years, we were chugging along on B, until one day there was a problem—B booted up, but it couldn’t mount its drive partition. We’d never seen this before. To preserve B’s data, we swapped back to A, which we hadn’t trusted in two thousand Sols. A also had a degraded memory, with only two gigabytes of usable storage space instead of four. We painstakingly transferred data from B over to A and then down to Earth, and eventually we ran out of stuff we wanted to transfer, which was really good, because A then started acting funny in the same way it did on Sol 200. It was acting like its memory was coming unsoldered. That’s bad. We quickly swapped back to B, formatted it, and got it working again. The problem then became that we couldn’t trust A’s memory at all, but we needed a second computer as a “lifeboat” for diagnostics and transfers if B failed again. We realized we had one other place of memory: where we keep our flight software. We have four copies of the flight software (two current versions and two older versions) in different banks of very small amounts of memory, just 32 megabytes each. What if we just jettisoned the old flight software copies and used that 64-megabyte NOR memory as our file system for computer A? So that’s what we did . It was so elegant! Computer A is operating with less than 1 percent of its original memory, but we can run a mission on it. A small mission, but we haven’t had to jettison any core capabilities. We can still drive, we can manage data, we can even theoretically do science. Everything works fine, just much slower and much smaller. That flight software release was even called “ R-Hope “ because we hoped it would work. What are the constraints on Curiosity’s lifespan? Holloway: Our biggest hardware challenge is wheel wear . It looks like we’re driving on this sandy terrain with some rocks in it, and our intuition said that we could just drive over these rocks and they’d get pushed down into the sand and it would be no big deal. But what we ended up seeing was that those little rocks are actually the tips of giant boulders buried in the sand, and they’re razor sharp. Our wheels were getting ripped apart driving over them, especially our front wheels, so we started driving backwards . We also monitor consumables. We consider the number of times we move our actuators. That’s a consumable. Curiosity hasn’t taken a selfie in a while, and one of the reasons is that it’s really hard on the joint actuators. Our onboard memory is a consumable, but surprisingly we’re not anywhere near our life cycle for memory. Our biggest consumable is power; we have an RTG , a nuclear power source, which decreases its output as it ages. Newer missions are flying Snapdragon [processors], but Curiosity’s RAD 750 is a power hog. One of the things that we’ve rolled out that’s going really well is a way of reducing the amount of time we spend with the computer powered on, by harvesting time when we finish activities early and going to sleep, which lets us turn off the computers and some of the heating. Another thing we’re looking at is doing stuff in parallel when we’re on, like being able to drive or use the arm while communicating with an orbiter. So power is decreasing, and that’s causing us to do all this parallelism work and become more efficient and nuanced in the way we operate. But we are not having any degraded science output at this time. Our wheels are still going, our arm is still okay for now, knock on wood. I would say maybe the bottleneck is budget. Curiosity Rover’s Impact on Future Mars Exploration What have you learned from Curiosity that will improve future missions? Holloway: As an embedded flight software person, I think about how we can change, add, or modify software capabilities during the mission. There’s definitely a sweet spot for loading and patching flight software—some of these concepts were pioneered on Spirit and Opportunity and then inherited by Curiosity and Perseverance, making it easier to understand and change the software. Some of the things that I wish we had now on [the Mars Science Laboratory] include a better understanding of where our power is going. I want to see how much power each component is drawing every minute, so that we could architect a software system that could balance loads better. We have some of this information that was built in by the engineers who designed the rover, but as an operator, I want something slightly different. So if I were building a mission, I would have those discussions earlier and get operators into the room to say, “what do you want your data products to look like?” The key takeaway for designing future missions is to talk to all your users early in the design process. It needs to happen upfront. What does Curiosity’s long-term future look like? Holloway: That’s a conversation that happens, and it’s a really delicate one. We have a lot of science instruments, and a lot of them have to do with contact science and sampling and rely on the arm. If we lose the arm, what science can we still do? Well, we have a lot of remote sensors too, like cameras, environmental sensors, and radiation sensors. All of these things are important for the future of space exploration and humans on Mars. From a power perspective, our RTG is projected to start degrading science output in the sixth extended mission, but we’re going to be fine through 2035 and potentially even beyond that. So we have a long and exciting future ahead of us. We need to figure out the best way of operating within our constraints, but we’re still kicking. It takes some special tricks to maintain a robot 200 million kilometers from home Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif., waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars. It did, and it was awesome .

## Overview
It takes some special tricks to maintain a robot 200 million kilometers from home. Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif., waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars.

## Content
Thirteen years ago last August, I was camped out in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif., waiting to see whether the Curiosity rover would survive its descent and skycrane-assisted landing on the surface of Mars. It did, and it was awesome. Since then, Curiosity (also known as Mars Science Laboratory) has traveled nearly 37 kilometers, drilled into and sampled 42 different rocks, and as of publication has snapped nearly 763,000 photos. The fact that this robot is still hard at work, getting real science done at the age of 13, is absolutely incredible—not only is Mars an actively hostile environment for robots, but the only kind of maintenance that JPL engineers can do is to send very, very careful software updates. Nevertheless, the clever folks at JPL have managed to keep Curiosity safe, warm, mobile, and sciencing, despite well-worn wheels and less and less power every day. One of those folks is Alexandra Holloway, the assistant team chief for engineering operations for Curiosity, who spoke to IEEE Spectrum about keeping Curiosity roving, what its future looks like, and how JPL has used that experience to make rovers like Perseverance even more capable. How astonished should we be that after 13 years on Mars, Curiosity is not only still doing science, but actually getting more capable? Alexandra Holloway is the assistant team chief for engineering operations on the Curiosity Mars rover at the Jet Propulsion Laboratory. Alexandra Holloway: I’m astonished! The longevity comes from a lot of ongoing work. It’s not just that Curiosity was built robustly; it’s also because we’re continuously putting in effort to ensure it can continue to have that lifespan. I think about all the different kinds of embedded systems there are, from cars to refrigerators, and none of them have the kind of longevity that we have with the rover. It’s mind-boggling, and it’s inspiring. Is the Perseverance rover, which is nine years younger than Curiosity, significantly different in terms of its hardware and software? Holloway: In terms of hardware, the rovers are actually very similar. Both use a RAD 750 processor and have the same amount of memory. However, Perseverance has an extra processor specifically for visual odometry, which allows it to drive autonomously. This difference reflects their primary mission designs: Perseverance was designed for driving long distances, while Curiosity is a mission focused on sampling as it goes. So Perseverance’s onboard scheduling capabilities are there to optimize its driving. In fact, just last year, Perseverance surpassed Curiosity’s driving distance after only about three years on Mars. Curiosity Rover Memory and Software Fixes Do you have some examples of significant tweaks the team has made to keep Curiosity roving? Holloway: One of my favorite examples comes from a processor anomaly that happened on Sol 2172 [Ed. note: “Sol” is the term for a Martian day—about 24 hours and 40 minutes]. Curiosity has two computers, A and B. We landed on A, swapped to B due to a NAND memory anomaly early on (Sol 200). For years, we were chugging along on B, until one day there was a problem—B booted up, but it couldn’t mount its drive partition. We’d never seen this before. To preserve B’s data, we swapped back to A, which we hadn’t trusted in two thousand Sols. A also had a degraded memory, with only two gigabytes of usable storage space instead of four. We painstakingly transferred data from B over to A and then down to Earth, and eventually we ran out of stuff we wanted to transfer, which was really good, because A then started acting funny in the same way it did on Sol 200. It was acting like its memory was coming unsoldered. That’s bad. We quickly swapped back to B, formatted it, and got it working again. The problem then became that we couldn’t trust A’s memory at all, but we needed a second computer as a “lifeboat” for diagnostics and transfers if B failed again. We realized we had one other place of memory: where we keep our flight software. We have four copies of the flight software (two current versions and two older versions) in different banks of very small amounts of memory, just 32 megabytes each. What if we just jettisoned the old flight software copies and used that 64-megabyte NOR memory as our file system for computer A? So that’s what we did. It was so elegant! Computer A is operating with less than 1 percent of its original memory, but we can run a mission on it. A small mission, but we haven’t had to jettison any core capabilities. We can still drive, we can manage data, we can even theoretically do science. Everything works fine, just much slower and much smaller. That flight software release was even called “R-Hope” because we hoped it would work. What are the constraints on Curiosity’s lifespan? Holloway: Our biggest hardware challenge is wheel wear. It looks like we’re driving on this sandy terrain with some rocks in it, and our intuition said that we could just drive over these rocks and they’d get pushed down into the sand and it would be no big deal. But what we ended up seeing was that those little rocks are actually the tips of giant boulders buried in the sand, and they’re razor sharp. Our wheels were getting ripped apart driving over them, especially our front wheels, so we started driving backwards. We also monitor consumables. We consider the number of times we move our actuators. That’s a consumable. Curiosity hasn’t taken a selfie in a while, and one of the reasons is that it’s really hard on the joint actuators. Our onboard memory is a consumable, but surprisingly we’re not anywhere near our life cycle for memory. Our biggest consumable is power; we have an RTG, a nuclear power source, which decreases its output as it ages. Newer missions are flying Snapdragon [processors], but Curiosity’s RAD 750 is a power hog. One of the things that we’ve rolled out that’s going really well is a way of reducing the amount of time we spend with the computer powered on, by harvesting time when we finish activities early and going to sleep, which lets us turn off the computers and some of the heating. Another thing we’re looking at is doing stuff in parallel when we’re on, like being able to drive or use the arm while communicating with an orbiter. So power is decreasing, and that’s causing us to do all this parallelism work and become more efficient and nuanced in the way we operate. But we are not having any degraded science output at this time. Our wheels are still going, our arm is still okay for now, knock on wood. I would say maybe the bottleneck is bu

## 参考
- https://spectrum.ieee.org/curiosity-rover-jpl-mars-science

## 개요
NASA JPL의 큐리오시티 로버 부공정 운영 책임자 알렉산드라 할로웨이가 IEEE Spectrum에 13년 된 이 로봇을 계속 작동시키는 방법에 대해 설명했다. 큐리오시티는 약 37km를 주행하고, 42개의 암석 샘플을 채취했으며, 약 76만 3천 장의 사진을 촬영했다. 화성의 혹독한 환경, 바퀴 마모, 핵전원 출력의 연간 감소 등의 도전에도 불구하고, JPL 팀은 신중하게 설계된 소프트웨어 업데이트를 전송하여 로버를 유지하고 있다. 할로웨이는 임무 간격 시간을 활용한 절전, 병렬 작업, 그리고 오래된 비행 소프트웨어 메모리를 예비 컴퓨터 파일 시스템으로 개조하는 혁신적인 방법을 통해 하드웨어 노후화 조건에서도 큐리오시티가 과학적 생산성을 유지할 수 있었던 방법을 공유했다. 또한 그녀는 큐리오시티와 더 젊은 퍼서비어런스 로버 간의 하드웨어 및 임무 설계 차이를 비교하고, 향후 임무를 위한 설계 교훈에 대해 논의했다.

## 핵심 내용
### 임무 개요 및 주요 수치
- 큐리오시티(화성 과학 연구소라고도 함)는 13년 전 화성에 성공적으로 착륙했으며, 현재까지 약 37km를 주행하고, 42개의 암석을 채취 및 샘플링했으며, 약 76만 3천 장의 사진을 촬영했다.
- 화성 환경은 로봇에게 극도로 가혹하며, JPL 엔지니어들은 매우 신중한 소프트웨어 업데이트를 전송하는 방식으로만 유지보수를 수행할 수 있다.

### 하드웨어 및 소프트웨어 비교: 큐리오시티 vs. 퍼서비어런스
- **하드웨어 유사성**: 두 로버 모두 RAD 750 프로세서를 사용하며, 메모리 용량이 동일하다.
- **핵심 차이점**: 퍼서비어런스에는 시각적 주행 거리 측정 전용 프로세서가 추가로 장착되어 자율 주행이 가능하다. 이는 임무 설계의 차이를 반영한다—퍼서비어런스는 장거리 주행을 목표로 하는 반면, 큐리오시티는 경로상 샘플링에 중점을 둔다.
- **성능 비교**: 퍼서비어런스는 화성에서 약 3년 만에 주행 거리에서 큐리오시티를 초과했다.

### 메모리 및 소프트웨어 수리 사례
- **프로세서 이상 이벤트**: Sol 2172(화성일, 약 24시간 40분)에서 큐리오시티의 B 컴퓨터가 부팅 후 드라이브 파티션을 마운트하지 못했다. 팀은 2000화성일 동안 유휴 상태였던 A 컴퓨터로 전환할 수밖에 없었지만, 해당 컴퓨터의 메모리는 열화되어 사용 가능한 저장 공간이 2GB(원래 4GB)에 불과했다.
- **데이터 구조 작업**: 팀은 B 컴퓨터의 데이터를 어렵게 A 컴퓨터로 전송한 후 지구로 다운로드했다. 이후 A 컴퓨터에서 Sol 200 시절의 메모리 납땜 불량 징후가 나타나자, 팀은 신속히 B 컴퓨터로 전환하고 포맷하여 수리했다.
- **혁신적 해결책**: 예비 "구명정" 컴퓨터를 유지하기 위해, 팀은 구형 비행 소프트웨어를 포기하고, 비행 소프트웨어를 저장하던 64MB NOR 메모리(원래 4개의 비행 소프트웨어 사본을 각각 32MB씩 저장하던 공간)를 A 컴퓨터의 파일 시스템으로 개조하기로 결정했다. 이 소프트웨어 버전은 "R-Hope"으로 명명되었으며, 작동하기를 바라는 의미를 담고 있다. 현재 A 컴퓨터는 원래 메모리의 1% 미만 용량으로 작동하지만, 여전히 주행, 데이터 관리, 심지어 과학 임무까지 수행할 수 있으며, 다만 속도가 느리고 규모가 작다.

### 수명 제한 및 대응 전략
- **최대 하드웨어 과제: 바퀴 마모**. 화성 표면은 모래처럼 보이지만 실제로는 날카로운 바위가 묻혀 있어 바퀴(특히 앞바퀴)가 심각하게 손상되었다. 팀은 이로 인해 후진 주행을 시작했다.
- **소모품 모니터링**:
  - **액추에이터 작동 횟수**: 소모품으로 간주되며, 예를 들어 셀카 촬영은 관절 액추에이터에 큰 부담을 주어 최근에는 수행되지 않았다.
  - **메모리**: 예상외로 수명 주기에 훨씬 못 미치는 수준이다.
  - **최대 소모품: 전력**. 큐리오시티의 핵전원 RTG 출력은 노후화에 따라 감소하며, RAD 750 프로세서는 전력 소모가 높다.
- **절전 조치**:
  - **유휴 시간 회수**: 작업을 일찍 완료한 후 컴퓨터를 절전 모드로 전환하고 일부 난방 시스템을 끈다.
  - **병렬 작업**: 통신을 유지하면서 주행 또는 로봇 팔 작업을 동시에 수행한다.
- **현재 상태**: 전력 감소에도 불구하고 과학적 생산성은 영향을 받지 않았다. 바퀴와 로봇 팔은 여전히 정상 작동한다. 할로웨이는 예산이 향후 병목 현상이 될 수 있다고 지적했다.

### 향후 임무에 대한 영향
- **소프트웨어 유연성**: 큐리오시티의 경험은 임무 중 소프트웨어 기능을 변경, 추가 또는 수정하는 것이 중요함을 보여준다. 스피릿과 오퍼튜니티가 개척한 소프트웨어 로딩 및 패치 개념은 큐리오시티와 퍼서비어런스가 계승했다.
- **개선 제안**: 할로웨이는 향후 임무에서 각 구성 요소의 실시간 전력 소모를 더 정밀하게 모니터링하여 부하 균형 소프트웨어 시스템을 설계할 수 있기를 희망한다. 핵심 교훈은 설계 초기 단계에서 운영 담당자가 데이터 제품 요구 사항 논의에 참여해야 한다는 것이다.

### 장기 전망
- **과학적 능력**: 로봇 팔을 잃더라도 큐리오시티는 원격 센서(카메라, 환경 센서, 방사선 센서)에 의존하여 우주 탐사와 인간의 화성 착륙에 중요한 과학적 작업을 계속 수행할 수 있다.
- **전력 예측**: RTG는 여섯 번째 확장 임무에서 과학적 생산성에 영향을 미치기 시작할 것으로 예상되지만, 큐리오시티는 최소 2035년까지 또는 그 이상 정상 작동할 수 있다. 팀은 제약 조건 하에서 최적의 운영 방식을 모색하고 있다.
