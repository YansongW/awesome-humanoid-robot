---
$id: ent_report_ieee_what_makes_a_job_dull_dirty_or_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: What Makes a Job Dull, Dirty, or Dangerous?
  zh: What Makes a Job Dull, Dirty, or Dangerous?
  ko: What Makes a Job Dull, Dirty, or Dangerous?
summary:
  en: 'For years, the field of robotics has used the terms “dull, dirty, and dangerous” (DDD) to describe the types of tasks
    or jobs where robots might be useful—by doing work that’s undesirable for people. A classic example of a DDD job is one
    of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.”
    But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is
    a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is
    there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which
    was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for
    our technology. First, we did an empirical analysis of robotics publications between 1980 and 2024 that mention DDD and
    found that only 2.7 percent define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions vary, and
    many of the examples aren’t particularly specific (for example, “industrial manufacturing,” “home care”). Next, we reviewed
    the social science literature in anthropology, economics, political science, psychology, and sociology to develop better
    definitions for “dull,” “dirty,” and “dangerous” work. Again, while it might seem intuitive which tasks to put into these
    buckets, it turns out that there are some underlying social, economic, and cultural factors that matter. Dangerous Work:
    Occupations or tasks that result in injury or risk of harm It’s possible to measure the danger of a task or job by using
    reported information. There are administrative records and surveys that provide numbers on occupational injury rates and
    hazardous risk factors. While that seems straightforward, it’s important to understand how this data was collected, reported,
    and verified. First, occupational injuries tend to be underreported, with some studies estimating up to 70 percent of
    cases missing in administrative databases . Second, injuries and risk factors are rarely disaggregated by characteristics
    like gender, migration status, formal/informal employment, and work activities . For example, because most personal protective
    equipment—such as masks, vests, and gloves—are sized for men, women in dangerous work environments face increased safety
    risks . These caveats are an opportunity for robotics to be helpful. If we went out and looked for it, we could probably
    find some less obviously dangerous work where robotics might be an important intervention, not to mention some groups
    that are disproportionately affected and would benefit from more workplace safety. Dirty Work: Occupations or tasks that
    are physically, socially, or morally tainted Colloquially, most people might think of dirty work as involving physical
    dirtiness, such as trash removal, cleaning, or dealing with hazardous substances. But social science literature makes
    clear that dirty work is also about stigma . Socially tainted jobs are often servile or involve interacting with stigmatized
    groups (for example, correctional officers), and morally tainted jobs include tasks that people commonly perceive as sinful,
    deceptive, or otherwise defying norms of civility (like a stripper or a collection agent). “Dirty work” is a social construct
    that can vary across time (like tattoo industry stigma in the United States) and culture (such as nursing in the U.S .
    versus in Bangladesh ). One way to measure whether work is “dirty” is by using the closely related concept of occupational
    prestige, captured through quantitative surveys where people rank jobs. Another way to measure it is through qualitative
    data, like ethnographies and interviews. Similar to “dangerous,” we see some hidden opportunities for robotics in “dirty”
    work. But one of our more interesting takeaways from the data is that a lower-ranked job can be something that the workers
    themselves enjoy or find immense pride and meaning in . If we care about what tasks are truly undesirable, understanding
    this worker perspective is important. Dull Work: Occupations or tasks that are repetitive and lacking in autonomy When
    it comes to defining dull work, what matters most is workers’ own experiences. Outsiders can make a lot of false assumptions
    about what tasks have value and meaning. Sometimes things that seem boring or routine create the right conditions for
    developing skills and competence , such as the concentration needed for woodworking, or for socializing and support ,
    when tasks are done alongside others. Instead of assuming that repetitive work is negative, it’s important to examine
    qualitative data on how people experience the work and what purpose it serves for them . DDD: An actionable framework
    In our paper, we propose a framework to help the robotics community explore how automation impacts individual jobs. For
    each term—dull, dirty, and dangerous—the framework gathers key pieces of information to reflect on what physical or social
    aspects of the task are, in fact, DDD. Worker perspective is an important part of all three considerations. The framework
    also emphasizes awareness of context—meaning the physical and social environment of an occupation and industry that can
    influence the DDD nature of a task. Our corresponding worksheet suggests existing data sources to draw on and encourages
    us to seek out multiple perspectives and consider potential sources of bias in the information. What makes tasks dull,
    dirty, or dangerous depends on the perspective of the humans doing those tasks. RAI Let’s take, for example, the waste
    and recycling industry . The world generates over 2 billion tonnes of waste annually, and this figure is expected to rise
    to nearly 4 billion tonnes by 2050 . Intuitively, trash collection seems like a job that hits all the Ds. Going through
    our worksheet, we confirm that globally, workers in this industry face significant health hazards (dangerous), and waste
    collection is ranked as a low-status job (dirty), although interestingly, many workers take pride in providing this essential
    service . The job is also repetitive, but there are aspects that make it not dull . Specifically, workers cite the day-to-day
    interaction with their coworkers (which includes extensive insider vocabulary, work hacks, and mutual aid groups) and
    task variety as two of the most enjoyable aspects of the job. Task variety includes inspecting their vehicle and equipment,
    driving their truck, coordinating with crew members, lifting bins and bags, detecting incorrect sorting of waste, and
    unloading at the end destination. This finding matters because some types of robotic solutions will eliminate the parts
    of the job that workers most appreciate. For instance, the National Institute for Occupational Safety and Health (NIOSH)
    recommends the adoption of automated side loader trucks and collision avoidance systems . This innovation increases safety,
    which is great, but it also results in a sole worker operating a joystick in a cab, surrounded by sensor and camera surveillance.
    Instead, we should challenge ourselves to think of solutions that make jobs safer without making them terrible in a different
    way. To do this, we need to understand all aspects of what makes a job dull, dirty, or dangerous (or not). Our framework
    aims to facilitate this understanding. Finally, it’s important to note that DDD is only one of many possible approaches
    to classify what work might be better served by robots. There are lots of ways we could think about which types of tasks
    or jobs to automate (for example, economic impact or environmental sustainability). Given the popularity of DDD in robotics,
    we chose this common phrase as a starting point. We would love to see more work in this space, whether it’s data collection
    on DDD itself or the creation of other frameworks. At RAI , we believe that the fusion of robotics and social sciences
    opens a whole new world of information, perspectives, opportunities, and value. It fosters a culture of curiosity and
    mutual learning, and allows us to create actionable tools for anyone in robotics who cares about societal impact. Dull,
    Dirty, Dangerous: Understanding the Past, Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro
    Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was presented at the 21st ACM/IEEE International
    Conference on Human-Robot Interaction (HRI) in Edinburgh, Scotland.'
  zh: RAI Institute 的研究重新定义了机器人学中“dull, dirty, and dangerous”（DDD）的概念，并提出一个分析框架。该框架强调从工人视角和社会文化背景出发，而非仅凭直觉判断任务是否适合自动化。研究发现，仅
    2.7% 的机器人学出版物明确定义了 DDD，且现有定义常忽略社会污名、职业声望等关键因素。
  ko: 'For years, the field of robotics has used the terms “dull, dirty, and dangerous” (DDD) to describe the types of tasks
    or jobs where robots might be useful—by doing work that’s undesirable for people. A classic example of a DDD job is one
    of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.”
    But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is
    a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is
    there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which
    was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for
    our technology. First, we did an empirical analysis of robotics publications between 1980 and 2024 that mention DDD and
    found that only 2.7 percent define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions vary, and
    many of the examples aren’t particularly specific (for example, “industrial manufacturing,” “home care”). Next, we reviewed
    the social science literature in anthropology, economics, political science, psychology, and sociology to develop better
    definitions for “dull,” “dirty,” and “dangerous” work. Again, while it might seem intuitive which tasks to put into these
    buckets, it turns out that there are some underlying social, economic, and cultural factors that matter. Dangerous Work:
    Occupations or tasks that result in injury or risk of harm It’s possible to measure the danger of a task or job by using
    reported information. There are administrative records and surveys that provide numbers on occupational injury rates and
    hazardous risk factors. While that seems straightforward, it’s important to understand how this data was collected, reported,
    and verified. First, occupational injuries tend to be underreported, with some studies estimating up to 70 percent of
    cases missing in administrative databases . Second, injuries and risk factors are rarely disaggregated by characteristics
    like gender, migration status, formal/informal employment, and work activities . For example, because most personal protective
    equipment—such as masks, vests, and gloves—are sized for men, women in dangerous work environments face increased safety
    risks . These caveats are an opportunity for robotics to be helpful. If we went out and looked for it, we could probably
    find some less obviously dangerous work where robotics might be an important intervention, not to mention some groups
    that are disproportionately affected and would benefit from more workplace safety. Dirty Work: Occupations or tasks that
    are physically, socially, or morally tainted Colloquially, most people might think of dirty work as involving physical
    dirtiness, such as trash removal, cleaning, or dealing with hazardous substances. But social science literature makes
    clear that dirty work is also about stigma . Socially tainted jobs are often servile or involve interacting with stigmatized
    groups (for example, correctional officers), and morally tainted jobs include tasks that people commonly perceive as sinful,
    deceptive, or otherwise defying norms of civility (like a stripper or a collection agent). “Dirty work” is a social construct
    that can vary across time (like tattoo industry stigma in the United States) and culture (such as nursing in the U.S .
    versus in Bangladesh ). One way to measure whether work is “dirty” is by using the closely related concept of occupational
    prestige, captured through quantitative surveys where people rank jobs. Another way to measure it is through qualitative
    data, like ethnographies and interviews. Similar to “dangerous,” we see some hidden opportunities for robotics in “dirty”
    work. But one of our more interesting takeaways from the data is that a lower-ranked job can be something that the workers
    themselves enjoy or find immense pride and meaning in . If we care about what tasks are truly undesirable, understanding
    this worker perspective is important. Dull Work: Occupations or tasks that are repetitive and lacking in autonomy When
    it comes to defining dull work, what matters most is workers’ own experiences. Outsiders can make a lot of false assumptions
    about what tasks have value and meaning. Sometimes things that seem boring or routine create the right conditions for
    developing skills and competence , such as the concentration needed for woodworking, or for socializing and support ,
    when tasks are done alongside others. Instead of assuming that repetitive work is negative, it’s important to examine
    qualitative data on how people experience the work and what purpose it serves for them . DDD: An actionable framework
    In our paper, we propose a framework to help the robotics community explore how automation impacts individual jobs. For
    each term—dull, dirty, and dangerous—the framework gathers key pieces of information to reflect on what physical or social
    aspects of the task are, in fact, DDD. Worker perspective is an important part of all three considerations. The framework
    also emphasizes awareness of context—meaning the physical and social environment of an occupation and industry that can
    influence the DDD nature of a task. Our corresponding worksheet suggests existing data sources to draw on and encourages
    us to seek out multiple perspectives and consider potential sources of bias in the information. What makes tasks dull,
    dirty, or dangerous depends on the perspective of the humans doing those tasks. RAI Let’s take, for example, the waste
    and recycling industry . The world generates over 2 billion tonnes of waste annually, and this figure is expected to rise
    to nearly 4 billion tonnes by 2050 . Intuitively, trash collection seems like a job that hits all the Ds. Going through
    our worksheet, we confirm that globally, workers in this industry face significant health hazards (dangerous), and waste
    collection is ranked as a low-status job (dirty), although interestingly, many workers take pride in providing this essential
    service . The job is also repetitive, but there are aspects that make it not dull . Specifically, workers cite the day-to-day
    interaction with their coworkers (which includes extensive insider vocabulary, work hacks, and mutual aid groups) and
    task variety as two of the most enjoyable aspects of the job. Task variety includes inspecting their vehicle and equipment,
    driving their truck, coordinating with crew members, lifting bins and bags, detecting incorrect sorting of waste, and
    unloading at the end destination. This finding matters because some types of robotic solutions will eliminate the parts
    of the job that workers most appreciate. For instance, the National Institute for Occupational Safety and Health (NIOSH)
    recommends the adoption of automated side loader trucks and collision avoidance systems . This innovation increases safety,
    which is great, but it also results in a sole worker operating a joystick in a cab, surrounded by sensor and camera surveillance.
    Instead, we should challenge ourselves to think of solutions that make jobs safer without making them terrible in a different
    way. To do this, we need to understand all aspects of what makes a job dull, dirty, or dangerous (or not). Our framework
    aims to facilitate this understanding. Finally, it’s important to note that DDD is only one of many possible approaches
    to classify what work might be better served by robots. There are lots of ways we could think about which types of tasks
    or jobs to automate (for example, economic impact or environmental sustainability). Given the popularity of DDD in robotics,
    we chose this common phrase as a starting point. We would love to see more work in this space, whether it’s data collection
    on DDD itself or the creation of other frameworks. At RAI , we believe that the fusion of robotics and social sciences
    opens a whole new world of information, perspectives, opportunities, and value. It fosters a culture of curiosity and
    mutual learning, and allows us to create actionable tools for anyone in robotics who cares about societal impact. Dull,
    Dirty, Dangerous: Understanding the Past, Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro
    Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was presented at the 21st ACM/IEEE International
    Conference on Human-Robot Interaction (HRI) in Edinburgh, Scotland.'
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
- safety
- sensor
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/dull-dirty-dangerous-robots.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: What Makes a Job Dull, Dirty, or Dangerous?
  url: https://spectrum.ieee.org/dull-dirty-dangerous-robots
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
RAI Institute 的研究团队通过分析 1980 至 2024 年的机器人学文献，发现仅有 2.7% 的论文明确定义了 DDD，8.7% 提供了任务示例，且定义差异大、示例笼统。随后，他们借鉴人类学、经济学等社会科学文献，为“dull”“dirty”“dangerous”提出了更细致的定义：危险工作涉及伤害风险，但数据常低估且未按性别等特征细分；肮脏工作不仅指物理污染，还包括社会污名和道德污名；枯燥工作则取决于工人的自主性和重复性体验。基于此，团队开发了一个可操作的框架，帮助机器人学家结合工人视角和具体环境（如物理与社会环境）评估任务是否真正属于 DDD，并强调避免因自动化而消除工人珍视的工作要素。

## 核心内容
### 研究背景与动机
机器人学领域长期使用“dull, dirty, and dangerous”（DDD）来描述适合自动化的任务，但这一概念的定义模糊且缺乏实证基础。例如，典型的 DDD 工作被描述为“在高温工厂地板上使用重型机械的重复性体力劳动”，但哪些任务真正符合这些类别并不明确。

### 方法：文献分析与社会科学整合
- **文献分析**：团队检索了 1980 至 2024 年间提及 DDD 的机器人学出版物，发现仅 2.7% 提供了明确定义，8.7% 给出了任务示例。多数示例缺乏具体性（如“工业制造”“家庭护理”），且定义差异显著。
- **社会科学回顾**：从人类学、经济学、政治学、心理学和社会学文献中提炼更精确的定义：
  - **Dangerous Work**：指导致伤害或伤害风险的职业或任务。可通过行政记录和调查数据测量，但存在三大问题：伤害漏报率高达 70%；数据未按性别、移民身份、正式/非正式就业等特征细分；个人防护装备（如口罩、背心、手套）多按男性尺寸设计，导致女性面临更高安全风险。
  - **Dirty Work**：不仅包括物理污染（如垃圾清理、危险物质处理），还涉及社会污名（如与受污名群体互动的工作）和道德污名（如被认为有罪或欺骗性的工作）。可通过职业声望调查或民族志访谈测量。值得注意的是，低声望工作可能被工人自身视为有尊严和意义的。
  - **Dull Work**：核心是工人的主观体验。外部观察者常错误假设某些任务缺乏价值，但重复性工作可能为技能发展（如木工所需的专注）或社交支持（如团队协作）创造条件。因此，需通过定性数据了解工人如何体验工作及其目的。

### 框架：DDD 的可操作化
团队提出了一个分析框架，帮助机器人社区评估自动化对具体工作的影响：
- **核心要素**：针对每个 D 维度，收集关键信息，反思任务的物理或社会属性是否真正属于 DDD。工人视角是三个维度的共同核心。
- **环境意识**：强调职业和行业的物理与社会环境会影响任务的 DDD 性质。例如，垃圾回收行业看似符合所有 D 维度，但工人珍视与同事的日常互动（包括内部术语、工作技巧和互助小组）以及任务多样性（如检查车辆、驾驶卡车、协调团队、分类垃圾等）。
- **数据来源与偏差**：配套工作表建议使用现有数据源（如职业伤害记录、声望调查），同时鼓励寻求多元视角并考虑信息中的潜在偏差。

### 案例：垃圾回收行业
- **全球背景**：全球每年产生超过 20 亿吨垃圾，预计 2050 年将增至近 40 亿吨。
- **DDD 分析**：
  - **Dangerous**：工人面临显著健康危害（如受伤、疾病）。
  - **Dirty**：垃圾收集被列为低地位工作，但许多工人因提供基本服务而自豪。
  - **Dull**：工作虽重复，但工人认为日常互动和任务多样性使其不枯燥。
- **自动化启示**：NIOSH 推荐采用自动侧装卡车和防撞系统，这虽提升安全性，但导致单人操作操纵杆、被传感器和摄像头监控，消除了工人珍视的社交和多样性要素。框架鼓励设计既能提升安全又不破坏工作意义的解决方案。

### 结论与展望
DDD 仅是分类自动化任务的多种方法之一（其他包括经济影响、环境可持续性等）。团队希望推动更多关于 DDD 的数据收集和框架创建。RAI Institute 认为，机器人学与社会科学的融合能提供新的信息、视角和工具，帮助关注社会影响的机器人从业者。该研究由 Nozomi Nakajima、Pedro Reynolds-Cuéllar、Caitrin Lynch 和 Kate Darling 完成，发表于第 21 届 ACM/IEEE 人机交互国际会议（HRI）。

## Overview
Research from the RAI Institute redefines undesirable work for robotics A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems.

Research from the RAI Institute redefines undesirable work for robotics A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for our technology.

## Overview
Research from the RAI Institute redefines undesirable work for robotics. A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems.

## Content
Research from the RAI Institute redefines undesirable work for robotics. A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for our technology.

## 개요
RAI 연구소의 연구는 로봇 공학에서 바람직하지 않은 작업을 재정의합니다. DDD 작업의 전형적인 예는 "생명과 신체를 위협하는 중장비가 있는 뜨겁고 습한 공장 바닥에서의 반복적인 육체 노동"입니다. 그러나 어떤 인간 활동이 이러한 범주에 속하는지 결정하는 것은 보이는 것처럼 간단하지 않습니다.

## 핵심 내용
RAI 연구소의 연구는 로봇 공학에서 바람직하지 않은 작업을 재정의합니다. DDD 작업의 전형적인 예는 "생명과 신체를 위협하는 중장비가 있는 뜨겁고 습한 공장 바닥에서의 반복적인 육체 노동"입니다. 그러나 어떤 인간 활동이 이러한 범주에 속하는지 결정하는 것은 보이는 것처럼 간단하지 않습니다. 정확히 "지루한" 작업이란 무엇이며, 누가 그 가정을 하는가? "더러운" 작업은 단순히 나중에 손을 씻어야 하는 것에 관한 것인가, 아니면 사회적 낙인이라는 측면도 있는가? 작업을 "위험한" 것으로 분류하기 위해 어떤 데이터에 의존할 수 있는가? 우리의 최근 연구(전혀 지루하지 않았던)는 이러한 질문을 다루며, 로봇 공학자들이 우리 기술의 작업 맥락을 이해할 수 있도록 돕는 프레임워크를 제안합니다.

## 参考
- https://spectrum.ieee.org/dull-dirty-dangerous-robots
