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
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/dull-dirty-dangerous-robots.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1895 chars, DeepSeek).'
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

## 参考
- https://spectrum.ieee.org/dull-dirty-dangerous-robots

## 개요
RAI Institute의 연구팀은 1980년부터 2024년까지의 로봇공학 문헌을 분석한 결과, 논문의 2.7%만이 DDD를 명확히 정의했고, 8.7%만이 작업 예시를 제공했으며, 정의 간 차이가 크고 예시가 포괄적임을 발견했습니다. 이후 그들은 인류학, 경제학 등 사회과학 문헌을 참고하여 'dull', 'dirty', 'dangerous'에 대해 더 세밀한 정의를 제안했습니다: 위험 작업은 부상 위험을 수반하지만, 데이터는 종종 과소평가되고 성별 등의 특성별로 세분화되지 않습니다; 더러운 작업은 물리적 오염뿐만 아니라 사회적 낙인과 도덕적 낙인도 포함합니다; 지루한 작업은 작업자의 자율성과 반복성 경험에 달려 있습니다. 이를 바탕으로 팀은 로봇공학자들이 작업자 관점과 구체적 환경(예: 물리적·사회적 환경)을 결합하여 작업이 진정으로 DDD에 해당하는지 평가할 수 있도록 돕는 실행 가능한 프레임워크를 개발했으며, 자동화로 인해 작업자가 소중히 여기는 작업 요소가 사라지지 않도록 하는 것을 강조합니다.

## 핵심 내용
### 연구 배경 및 동기
로봇공학 분야는 오랫동안 'dull, dirty, and dangerous'(DDD)를 자동화에 적합한 작업을 설명하는 데 사용해 왔지만, 이 개념의 정의는 모호하고 실증적 기반이 부족합니다. 예를 들어, 전형적인 DDD 작업은 '고온의 공장 바닥에서 중장비를 사용하는 반복적인 육체노동'으로 설명되지만, 어떤 작업이 실제로 이러한 범주에 해당하는지는 명확하지 않습니다.

### 방법: 문헌 분석 및 사회과학 통합
- **문헌 분석**: 팀은 1980년부터 2024년까지 DDD를 언급한 로봇공학 출판물을 검색한 결과, 2.7%만이 명확한 정의를 제공했고 8.7%만이 작업 예시를 제공했습니다. 대부분의 예시는 구체성이 부족했으며(예: '산업 제조', '가정 간호'), 정의 간 차이도 컸습니다.
- **사회과학 검토**: 인류학, 경제학, 정치학, 심리학, 사회학 문헌에서 더 정밀한 정의를 도출했습니다:
  - **위험 작업(Dangerous Work)**: 부상 또는 부상 위험을 초래하는 직업이나 작업을 의미합니다. 행정 기록과 설문 데이터로 측정할 수 있지만, 세 가지 주요 문제가 있습니다: 부상 누락률이 최대 70%에 달함; 데이터가 성별, 이민자 신분, 공식/비공식 고용 등의 특성별로 세분화되지 않음; 개인 보호 장비(예: 마스크, 조끼, 장갑)가 대부분 남성 치수로 설계되어 여성이 더 높은 안전 위험에 노출됨.
  - **더러운 작업(Dirty Work)**: 물리적 오염(예: 쓰레기 수거, 위험 물질 처리)뿐만 아니라 사회적 낙인(예: 낙인찍힌 집단과 상호작용하는 작업)과 도덕적 낙인(예: 유죄 또는 기만적인 것으로 간주되는 작업)도 포함합니다. 직업 명성 조사나 민족지학적 인터뷰로 측정할 수 있습니다. 주목할 점은 낮은 명성의 작업이 작업자 자신에게는 존엄하고 의미 있는 것으로 여겨질 수 있다는 것입니다.
  - **지루한 작업(Dull Work)**: 핵심은 작업자의 주관적 경험입니다. 외부 관찰자는 종종 특정 작업이 가치 없다고 잘못 가정하지만, 반복적인 작업은 기술 개발(예: 목공에 필요한 집중력)이나 사회적 지원(예: 팀 협력)의 조건을 만들 수 있습니다. 따라서 작업자가 작업을 어떻게 경험하고 그 목적이 무엇인지 이해하기 위해 정성적 데이터가 필요합니다.

### 프레임워크: DDD의 실행 가능화
팀은 로봇 커뮤니티가 자동화가 특정 작업에 미치는 영향을 평가하도록 돕는 분석 프레임워크를 제안했습니다:
- **핵심 요소**: 각 D 차원에 대해 핵심 정보를 수집하고, 작업의 물리적 또는 사회적 속성이 진정으로 DDD에 해당하는지 반성합니다. 작업자 관점은 세 차원의 공통 핵심입니다.
- **환경 인식**: 직업과 산업의 물리적·사회적 환경이 작업의 DDD 성격에 영향을 미친다는 점을 강조합니다. 예를 들어, 쓰레기 수거 산업은 모든 D 차원에 해당하는 것처럼 보이지만, 작업자들은 동료와의 일상적 상호작용(내부 용어, 작업 요령, 상호 지원 그룹 포함)과 작업 다양성(예: 차량 점검, 트럭 운전, 팀 조정, 쓰레기 분류 등)을 소중히 여깁니다.
- **데이터 출처 및 편향**: 함께 제공되는 워크시트는 기존 데이터 출처(예: 직업 부상 기록, 명성 조사)를 사용하도록 제안하면서도, 다양한 관점을 구하고 정보의 잠재적 편향을 고려하도록 권장합니다.

### 사례: 쓰레기 수거 산업
- **글로벌 배경**: 전 세계적으로 매년 20억 톤 이상의 쓰레기가 발생하며, 2050년에는 약 40억 톤으로 증가할 것으로 예상됩니다.
- **DDD 분석**:
  - **위험(Dangerous)**: 작업자는 상당한 건강 위험(예: 부상, 질병)에 노출됩니다.
  - **더러움(Dirty)**: 쓰레기 수거는 낮은 지위의 작업으로 분류되지만, 많은 작업자는 기본 서비스를 제공한다는 자부심을 느낍니다.
  - **지루함(Dull)**: 작업은 반복적이지만, 작업자는 일상적 상호작용과 작업 다양성 덕분에 지루하지 않다고 생각합니다.
- **자동화 시사점**: NIOSH는 자동 측면 적재 트럭과 충돌 방지 시스템을 권장하며, 이는 안전성을 높이지만 단일 작업자가 조이스틱을 조작하고 센서와 카메라로 모니터링되는 결과를 초래하여 작업자가 소중히 여기는 사회적·다양성 요소를 제거합니다. 프레임워크는 안전성을 높이면서도 작업 의미를 파괴하지 않는 솔루션 설계를 장려합니다.

### 결론 및 전망
DDD는 자동화 작업을 분류하는 여러 방법 중 하나일 뿐입니다(다른 방법으로는 경제적 영향, 환경 지속 가능성 등이 있습니다). 팀은 DDD에 대한 더 많은 데이터 수집과 프레임워크 구축을 촉진하고자 합니다. RAI Institute는 로봇공학과 사회과학의 융합이 사회적 영향을 중시하는 로봇 실무자에게 새로운 정보, 관점, 도구를 제공할 수 있다고 믿습니다. 이 연구는 Nozomi Nakajima, Pedro Reynolds-Cuéllar, Caitrin Lynch, Kate Darling이 수행했으며, 제21회 ACM/IEEE 인간-로봇 상호작용 국제 회의(HRI)에 게재되었습니다.
