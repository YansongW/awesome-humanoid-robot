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
  en: 'For years, the field of robotics has used the terms “dull, dirty, and dangerous”
    (DDD) to describe the types of tasks or jobs where robots might be useful—by doing
    work that’s undesirable for people. A classic example of a DDD job is one of “repetitive
    physical labor on a steaming hot factory floor involving heavy machinery that
    threatens life and limb.” But determining which human activities fit into these
    categories is not as straightforward as it seems. What exactly is a “dull” task,
    and who makes that assumption? Is “dirty” work just about needing to wash your
    hands afterwards, or is there also an aspect of social stigma? What data can we
    rely on to classify jobs as “dangerous?” Our recent work (which was not dull at
    all) tackles these questions and proposes a framework to help roboticists understand
    the job context for our technology. First, we did an empirical analysis of robotics
    publications between 1980 and 2024 that mention DDD and found that only 2.7 percent
    define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions
    vary, and many of the examples aren’t particularly specific (for example, “industrial
    manufacturing,” “home care”). Next, we reviewed the social science literature
    in anthropology, economics, political science, psychology, and sociology to develop
    better definitions for “dull,” “dirty,” and “dangerous” work. Again, while it
    might seem intuitive which tasks to put into these buckets, it turns out that
    there are some underlying social, economic, and cultural factors that matter.
    Dangerous Work: Occupations or tasks that result in injury or risk of harm It’s
    possible to measure the danger of a task or job by using reported information.
    There are administrative records and surveys that provide numbers on occupational
    injury rates and hazardous risk factors. While that seems straightforward, it’s
    important to understand how this data was collected, reported, and verified. First,
    occupational injuries tend to be underreported, with some studies estimating up
    to 70 percent of cases missing in administrative databases . Second, injuries
    and risk factors are rarely disaggregated by characteristics like gender, migration
    status, formal/informal employment, and work activities . For example, because
    most personal protective equipment—such as masks, vests, and gloves—are sized
    for men, women in dangerous work environments face increased safety risks . These
    caveats are an opportunity for robotics to be helpful. If we went out and looked
    for it, we could probably find some less obviously dangerous work where robotics
    might be an important intervention, not to mention some groups that are disproportionately
    affected and would benefit from more workplace safety. Dirty Work: Occupations
    or tasks that are physically, socially, or morally tainted Colloquially, most
    people might think of dirty work as involving physical dirtiness, such as trash
    removal, cleaning, or dealing with hazardous substances. But social science literature
    makes clear that dirty work is also about stigma . Socially tainted jobs are often
    servile or involve interacting with stigmatized groups (for example, correctional
    officers), and morally tainted jobs include tasks that people commonly perceive
    as sinful, deceptive, or otherwise defying norms of civility (like a stripper
    or a collection agent). “Dirty work” is a social construct that can vary across
    time (like tattoo industry stigma in the United States) and culture (such as nursing
    in the U.S . versus in Bangladesh ). One way to measure whether work is “dirty”
    is by using the closely related concept of occupational prestige, captured through
    quantitative surveys where people rank jobs. Another way to measure it is through
    qualitative data, like ethnographies and interviews. Similar to “dangerous,” we
    see some hidden opportunities for robotics in “dirty” work. But one of our more
    interesting takeaways from the data is that a lower-ranked job can be something
    that the workers themselves enjoy or find immense pride and meaning in . If we
    care about what tasks are truly undesirable, understanding this worker perspective
    is important. Dull Work: Occupations or tasks that are repetitive and lacking
    in autonomy When it comes to defining dull work, what matters most is workers’
    own experiences. Outsiders can make a lot of false assumptions about what tasks
    have value and meaning. Sometimes things that seem boring or routine create the
    right conditions for developing skills and competence , such as the concentration
    needed for woodworking, or for socializing and support , when tasks are done alongside
    others. Instead of assuming that repetitive work is negative, it’s important to
    examine qualitative data on how people experience the work and what purpose it
    serves for them . DDD: An actionable framework In our paper, we propose a framework
    to help the robotics community explore how automation impacts individual jobs.
    For each term—dull, dirty, and dangerous—the framework gathers key pieces of information
    to reflect on what physical or social aspects of the task are, in fact, DDD. Worker
    perspective is an important part of all three considerations. The framework also
    emphasizes awareness of context—meaning the physical and social environment of
    an occupation and industry that can influence the DDD nature of a task. Our corresponding
    worksheet suggests existing data sources to draw on and encourages us to seek
    out multiple perspectives and consider potential sources of bias in the information.
    What makes tasks dull, dirty, or dangerous depends on the perspective of the humans
    doing those tasks. RAI Let’s take, for example, the waste and recycling industry
    . The world generates over 2 billion tonnes of waste annually, and this figure
    is expected to rise to nearly 4 billion tonnes by 2050 . Intuitively, trash collection
    seems like a job that hits all the Ds. Going through our worksheet, we confirm
    that globally, workers in this industry face significant health hazards (dangerous),
    and waste collection is ranked as a low-status job (dirty), although interestingly,
    many workers take pride in providing this essential service . The job is also
    repetitive, but there are aspects that make it not dull . Specifically, workers
    cite the day-to-day interaction with their coworkers (which includes extensive
    insider vocabulary, work hacks, and mutual aid groups) and task variety as two
    of the most enjoyable aspects of the job. Task variety includes inspecting their
    vehicle and equipment, driving their truck, coordinating with crew members, lifting
    bins and bags, detecting incorrect sorting of waste, and unloading at the end
    destination. This finding matters because some types of robotic solutions will
    eliminate the parts of the job that workers most appreciate. For instance, the
    National Institute for Occupational Safety and Health (NIOSH) recommends the adoption
    of automated side loader trucks and collision avoidance systems . This innovation
    increases safety, which is great, but it also results in a sole worker operating
    a joystick in a cab, surrounded by sensor and camera surveillance. Instead, we
    should challenge ourselves to think of solutions that make jobs safer without
    making them terrible in a different way. To do this, we need to understand all
    aspects of what makes a job dull, dirty, or dangerous (or not). Our framework
    aims to facilitate this understanding. Finally, it’s important to note that DDD
    is only one of many possible approaches to classify what work might be better
    served by robots. There are lots of ways we could think about which types of tasks
    or jobs to automate (for example, economic impact or environmental sustainability).
    Given the popularity of DDD in robotics, we chose this common phrase as a starting
    point. We would love to see more work in this space, whether it’s data collection
    on DDD itself or the creation of other frameworks. At RAI , we believe that the
    fusion of robotics and social sciences opens a whole new world of information,
    perspectives, opportunities, and value. It fosters a culture of curiosity and
    mutual learning, and allows us to create actionable tools for anyone in robotics
    who cares about societal impact. Dull, Dirty, Dangerous: Understanding the Past,
    Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro
    Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was
    presented at the 21st ACM/IEEE International Conference on Human-Robot Interaction
    (HRI) in Edinburgh, Scotland.'
  zh: 'For years, the field of robotics has used the terms “dull, dirty, and dangerous”
    (DDD) to describe the types of tasks or jobs where robots might be useful—by doing
    work that’s undesirable for people. A classic example of a DDD job is one of “repetitive
    physical labor on a steaming hot factory floor involving heavy machinery that
    threatens life and limb.” But determining which human activities fit into these
    categories is not as straightforward as it seems. What exactly is a “dull” task,
    and who makes that assumption? Is “dirty” work just about needing to wash your
    hands afterwards, or is there also an aspect of social stigma? What data can we
    rely on to classify jobs as “dangerous?” Our recent work (which was not dull at
    all) tackles these questions and proposes a framework to help roboticists understand
    the job context for our technology. First, we did an empirical analysis of robotics
    publications between 1980 and 2024 that mention DDD and found that only 2.7 percent
    define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions
    vary, and many of the examples aren’t particularly specific (for example, “industrial
    manufacturing,” “home care”). Next, we reviewed the social science literature
    in anthropology, economics, political science, psychology, and sociology to develop
    better definitions for “dull,” “dirty,” and “dangerous” work. Again, while it
    might seem intuitive which tasks to put into these buckets, it turns out that
    there are some underlying social, economic, and cultural factors that matter.
    Dangerous Work: Occupations or tasks that result in injury or risk of harm It’s
    possible to measure the danger of a task or job by using reported information.
    There are administrative records and surveys that provide numbers on occupational
    injury rates and hazardous risk factors. While that seems straightforward, it’s
    important to understand how this data was collected, reported, and verified. First,
    occupational injuries tend to be underreported, with some studies estimating up
    to 70 percent of cases missing in administrative databases . Second, injuries
    and risk factors are rarely disaggregated by characteristics like gender, migration
    status, formal/informal employment, and work activities . For example, because
    most personal protective equipment—such as masks, vests, and gloves—are sized
    for men, women in dangerous work environments face increased safety risks . These
    caveats are an opportunity for robotics to be helpful. If we went out and looked
    for it, we could probably find some less obviously dangerous work where robotics
    might be an important intervention, not to mention some groups that are disproportionately
    affected and would benefit from more workplace safety. Dirty Work: Occupations
    or tasks that are physically, socially, or morally tainted Colloquially, most
    people might think of dirty work as involving physical dirtiness, such as trash
    removal, cleaning, or dealing with hazardous substances. But social science literature
    makes clear that dirty work is also about stigma . Socially tainted jobs are often
    servile or involve interacting with stigmatized groups (for example, correctional
    officers), and morally tainted jobs include tasks that people commonly perceive
    as sinful, deceptive, or otherwise defying norms of civility (like a stripper
    or a collection agent). “Dirty work” is a social construct that can vary across
    time (like tattoo industry stigma in the United States) and culture (such as nursing
    in the U.S . versus in Bangladesh ). One way to measure whether work is “dirty”
    is by using the closely related concept of occupational prestige, captured through
    quantitative surveys where people rank jobs. Another way to measure it is through
    qualitative data, like ethnographies and interviews. Similar to “dangerous,” we
    see some hidden opportunities for robotics in “dirty” work. But one of our more
    interesting takeaways from the data is that a lower-ranked job can be something
    that the workers themselves enjoy or find immense pride and meaning in . If we
    care about what tasks are truly undesirable, understanding this worker perspective
    is important. Dull Work: Occupations or tasks that are repetitive and lacking
    in autonomy When it comes to defining dull work, what matters most is workers’
    own experiences. Outsiders can make a lot of false assumptions about what tasks
    have value and meaning. Sometimes things that seem boring or routine create the
    right conditions for developing skills and competence , such as the concentration
    needed for woodworking, or for socializing and support , when tasks are done alongside
    others. Instead of assuming that repetitive work is negative, it’s important to
    examine qualitative data on how people experience the work and what purpose it
    serves for them . DDD: An actionable framework In our paper, we propose a framework
    to help the robotics community explore how automation impacts individual jobs.
    For each term—dull, dirty, and dangerous—the framework gathers key pieces of information
    to reflect on what physical or social aspects of the task are, in fact, DDD. Worker
    perspective is an important part of all three considerations. The framework also
    emphasizes awareness of context—meaning the physical and social environment of
    an occupation and industry that can influence the DDD nature of a task. Our corresponding
    worksheet suggests existing data sources to draw on and encourages us to seek
    out multiple perspectives and consider potential sources of bias in the information.
    What makes tasks dull, dirty, or dangerous depends on the perspective of the humans
    doing those tasks. RAI Let’s take, for example, the waste and recycling industry
    . The world generates over 2 billion tonnes of waste annually, and this figure
    is expected to rise to nearly 4 billion tonnes by 2050 . Intuitively, trash collection
    seems like a job that hits all the Ds. Going through our worksheet, we confirm
    that globally, workers in this industry face significant health hazards (dangerous),
    and waste collection is ranked as a low-status job (dirty), although interestingly,
    many workers take pride in providing this essential service . The job is also
    repetitive, but there are aspects that make it not dull . Specifically, workers
    cite the day-to-day interaction with their coworkers (which includes extensive
    insider vocabulary, work hacks, and mutual aid groups) and task variety as two
    of the most enjoyable aspects of the job. Task variety includes inspecting their
    vehicle and equipment, driving their truck, coordinating with crew members, lifting
    bins and bags, detecting incorrect sorting of waste, and unloading at the end
    destination. This finding matters because some types of robotic solutions will
    eliminate the parts of the job that workers most appreciate. For instance, the
    National Institute for Occupational Safety and Health (NIOSH) recommends the adoption
    of automated side loader trucks and collision avoidance systems . This innovation
    increases safety, which is great, but it also results in a sole worker operating
    a joystick in a cab, surrounded by sensor and camera surveillance. Instead, we
    should challenge ourselves to think of solutions that make jobs safer without
    making them terrible in a different way. To do this, we need to understand all
    aspects of what makes a job dull, dirty, or dangerous (or not). Our framework
    aims to facilitate this understanding. Finally, it’s important to note that DDD
    is only one of many possible approaches to classify what work might be better
    served by robots. There are lots of ways we could think about which types of tasks
    or jobs to automate (for example, economic impact or environmental sustainability).
    Given the popularity of DDD in robotics, we chose this common phrase as a starting
    point. We would love to see more work in this space, whether it’s data collection
    on DDD itself or the creation of other frameworks. At RAI , we believe that the
    fusion of robotics and social sciences opens a whole new world of information,
    perspectives, opportunities, and value. It fosters a culture of curiosity and
    mutual learning, and allows us to create actionable tools for anyone in robotics
    who cares about societal impact. Dull, Dirty, Dangerous: Understanding the Past,
    Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro
    Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was
    presented at the 21st ACM/IEEE International Conference on Human-Robot Interaction
    (HRI) in Edinburgh, Scotland.'
  ko: 'For years, the field of robotics has used the terms “dull, dirty, and dangerous”
    (DDD) to describe the types of tasks or jobs where robots might be useful—by doing
    work that’s undesirable for people. A classic example of a DDD job is one of “repetitive
    physical labor on a steaming hot factory floor involving heavy machinery that
    threatens life and limb.” But determining which human activities fit into these
    categories is not as straightforward as it seems. What exactly is a “dull” task,
    and who makes that assumption? Is “dirty” work just about needing to wash your
    hands afterwards, or is there also an aspect of social stigma? What data can we
    rely on to classify jobs as “dangerous?” Our recent work (which was not dull at
    all) tackles these questions and proposes a framework to help roboticists understand
    the job context for our technology. First, we did an empirical analysis of robotics
    publications between 1980 and 2024 that mention DDD and found that only 2.7 percent
    define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions
    vary, and many of the examples aren’t particularly specific (for example, “industrial
    manufacturing,” “home care”). Next, we reviewed the social science literature
    in anthropology, economics, political science, psychology, and sociology to develop
    better definitions for “dull,” “dirty,” and “dangerous” work. Again, while it
    might seem intuitive which tasks to put into these buckets, it turns out that
    there are some underlying social, economic, and cultural factors that matter.
    Dangerous Work: Occupations or tasks that result in injury or risk of harm It’s
    possible to measure the danger of a task or job by using reported information.
    There are administrative records and surveys that provide numbers on occupational
    injury rates and hazardous risk factors. While that seems straightforward, it’s
    important to understand how this data was collected, reported, and verified. First,
    occupational injuries tend to be underreported, with some studies estimating up
    to 70 percent of cases missing in administrative databases . Second, injuries
    and risk factors are rarely disaggregated by characteristics like gender, migration
    status, formal/informal employment, and work activities . For example, because
    most personal protective equipment—such as masks, vests, and gloves—are sized
    for men, women in dangerous work environments face increased safety risks . These
    caveats are an opportunity for robotics to be helpful. If we went out and looked
    for it, we could probably find some less obviously dangerous work where robotics
    might be an important intervention, not to mention some groups that are disproportionately
    affected and would benefit from more workplace safety. Dirty Work: Occupations
    or tasks that are physically, socially, or morally tainted Colloquially, most
    people might think of dirty work as involving physical dirtiness, such as trash
    removal, cleaning, or dealing with hazardous substances. But social science literature
    makes clear that dirty work is also about stigma . Socially tainted jobs are often
    servile or involve interacting with stigmatized groups (for example, correctional
    officers), and morally tainted jobs include tasks that people commonly perceive
    as sinful, deceptive, or otherwise defying norms of civility (like a stripper
    or a collection agent). “Dirty work” is a social construct that can vary across
    time (like tattoo industry stigma in the United States) and culture (such as nursing
    in the U.S . versus in Bangladesh ). One way to measure whether work is “dirty”
    is by using the closely related concept of occupational prestige, captured through
    quantitative surveys where people rank jobs. Another way to measure it is through
    qualitative data, like ethnographies and interviews. Similar to “dangerous,” we
    see some hidden opportunities for robotics in “dirty” work. But one of our more
    interesting takeaways from the data is that a lower-ranked job can be something
    that the workers themselves enjoy or find immense pride and meaning in . If we
    care about what tasks are truly undesirable, understanding this worker perspective
    is important. Dull Work: Occupations or tasks that are repetitive and lacking
    in autonomy When it comes to defining dull work, what matters most is workers’
    own experiences. Outsiders can make a lot of false assumptions about what tasks
    have value and meaning. Sometimes things that seem boring or routine create the
    right conditions for developing skills and competence , such as the concentration
    needed for woodworking, or for socializing and support , when tasks are done alongside
    others. Instead of assuming that repetitive work is negative, it’s important to
    examine qualitative data on how people experience the work and what purpose it
    serves for them . DDD: An actionable framework In our paper, we propose a framework
    to help the robotics community explore how automation impacts individual jobs.
    For each term—dull, dirty, and dangerous—the framework gathers key pieces of information
    to reflect on what physical or social aspects of the task are, in fact, DDD. Worker
    perspective is an important part of all three considerations. The framework also
    emphasizes awareness of context—meaning the physical and social environment of
    an occupation and industry that can influence the DDD nature of a task. Our corresponding
    worksheet suggests existing data sources to draw on and encourages us to seek
    out multiple perspectives and consider potential sources of bias in the information.
    What makes tasks dull, dirty, or dangerous depends on the perspective of the humans
    doing those tasks. RAI Let’s take, for example, the waste and recycling industry
    . The world generates over 2 billion tonnes of waste annually, and this figure
    is expected to rise to nearly 4 billion tonnes by 2050 . Intuitively, trash collection
    seems like a job that hits all the Ds. Going through our worksheet, we confirm
    that globally, workers in this industry face significant health hazards (dangerous),
    and waste collection is ranked as a low-status job (dirty), although interestingly,
    many workers take pride in providing this essential service . The job is also
    repetitive, but there are aspects that make it not dull . Specifically, workers
    cite the day-to-day interaction with their coworkers (which includes extensive
    insider vocabulary, work hacks, and mutual aid groups) and task variety as two
    of the most enjoyable aspects of the job. Task variety includes inspecting their
    vehicle and equipment, driving their truck, coordinating with crew members, lifting
    bins and bags, detecting incorrect sorting of waste, and unloading at the end
    destination. This finding matters because some types of robotic solutions will
    eliminate the parts of the job that workers most appreciate. For instance, the
    National Institute for Occupational Safety and Health (NIOSH) recommends the adoption
    of automated side loader trucks and collision avoidance systems . This innovation
    increases safety, which is great, but it also results in a sole worker operating
    a joystick in a cab, surrounded by sensor and camera surveillance. Instead, we
    should challenge ourselves to think of solutions that make jobs safer without
    making them terrible in a different way. To do this, we need to understand all
    aspects of what makes a job dull, dirty, or dangerous (or not). Our framework
    aims to facilitate this understanding. Finally, it’s important to note that DDD
    is only one of many possible approaches to classify what work might be better
    served by robots. There are lots of ways we could think about which types of tasks
    or jobs to automate (for example, economic impact or environmental sustainability).
    Given the popularity of DDD in robotics, we chose this common phrase as a starting
    point. We would love to see more work in this space, whether it’s data collection
    on DDD itself or the creation of other frameworks. At RAI , we believe that the
    fusion of robotics and social sciences opens a whole new world of information,
    perspectives, opportunities, and value. It fosters a culture of curiosity and
    mutual learning, and allows us to create actionable tools for anyone in robotics
    who cares about societal impact. Dull, Dirty, Dangerous: Understanding the Past,
    Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro
    Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was
    presented at the 21st ACM/IEEE International Conference on Human-Robot Interaction
    (HRI) in Edinburgh, Scotland.'
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website.
sources:
- id: src_001
  type: website
  title: What Makes a Job Dull, Dirty, or Dangerous?
  url: https://spectrum.ieee.org/dull-dirty-dangerous-robots
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
For years, the field of robotics has used the terms “dull, dirty, and dangerous” (DDD) to describe the types of tasks or jobs where robots might be useful—by doing work that’s undesirable for people. A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for our technology. First, we did an empirical analysis of robotics publications between 1980 and 2024 that mention DDD and found that only 2.7 percent define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions vary, and many of the examples aren’t particularly specific (for example, “industrial manufacturing,” “home care”). Next, we reviewed the social science literature in anthropology, economics, political science, psychology, and sociology to develop better definitions for “dull,” “dirty,” and “dangerous” work. Again, while it might seem intuitive which tasks to put into these buckets, it turns out that there are some underlying social, economic, and cultural factors that matter. Dangerous Work: Occupations or tasks that result in injury or risk of harm It’s possible to measure the danger of a task or job by using reported information. There are administrative records and surveys that provide numbers on occupational injury rates and hazardous risk factors. While that seems straightforward, it’s important to understand how this data was collected, reported, and verified. First, occupational injuries tend to be underreported, with some studies estimating up to 70 percent of cases missing in administrative databases . Second, injuries and risk factors are rarely disaggregated by characteristics like gender, migration status, formal/informal employment, and work activities . For example, because most personal protective equipment—such as masks, vests, and gloves—are sized for men, women in dangerous work environments face increased safety risks . These caveats are an opportunity for robotics to be helpful. If we went out and looked for it, we could probably find some less obviously dangerous work where robotics might be an important intervention, not to mention some groups that are disproportionately affected and would benefit from more workplace safety. Dirty Work: Occupations or tasks that are physically, socially, or morally tainted Colloquially, most people might think of dirty work as involving physical dirtiness, such as trash removal, cleaning, or dealing with hazardous substances. But social science literature makes clear that dirty work is also about stigma . Socially tainted jobs are often servile or involve interacting with stigmatized groups (for example, correctional officers), and morally tainted jobs include tasks that people commonly perceive as sinful, deceptive, or otherwise defying norms of civility (like a stripper or a collection agent). “Dirty work” is a social construct that can vary across time (like tattoo industry stigma in the United States) and culture (such as nursing in the U.S . versus in Bangladesh ). One way to measure whether work is “dirty” is by using the closely related concept of occupational prestige, captured through quantitative surveys where people rank jobs. Another way to measure it is through qualitative data, like ethnographies and interviews. Similar to “dangerous,” we see some hidden opportunities for robotics in “dirty” work. But one of our more interesting takeaways from the data is that a lower-ranked job can be something that the workers themselves enjoy or find immense pride and meaning in . If we care about what tasks are truly undesirable, understanding this worker perspective is important. Dull Work: Occupations or tasks that are repetitive and lacking in autonomy When it comes to defining dull work, what matters most is workers’ own experiences. Outsiders can make a lot of false assumptions about what tasks have value and meaning. Sometimes things that seem boring or routine create the right conditions for developing skills and competence , such as the concentration needed for woodworking, or for socializing and support , when tasks are done alongside others. Instead of assuming that repetitive work is negative, it’s important to examine qualitative data on how people experience the work and what purpose it serves for them . DDD: An actionable framework In our paper, we propose a framework to help the robotics community explore how automation impacts individual jobs. For each term—dull, dirty, and dangerous—the framework gathers key pieces of information to reflect on what physical or social aspects of the task are, in fact, DDD. Worker perspective is an important part of all three considerations. The framework also emphasizes awareness of context—meaning the physical and social environment of an occupation and industry that can influence the DDD nature of a task. Our corresponding worksheet suggests existing data sources to draw on and encourages us to seek out multiple perspectives and consider potential sources of bias in the information. What makes tasks dull, dirty, or dangerous depends on the perspective of the humans doing those tasks. RAI Let’s take, for example, the waste and recycling industry . The world generates over 2 billion tonnes of waste annually, and this figure is expected to rise to nearly 4 billion tonnes by 2050 . Intuitively, trash collection seems like a job that hits all the Ds. Going through our worksheet, we confirm that globally, workers in this industry face significant health hazards (dangerous), and waste collection is ranked as a low-status job (dirty), although interestingly, many workers take pride in providing this essential service . The job is also repetitive, but there are aspects that make it not dull . Specifically, workers cite the day-to-day interaction with their coworkers (which includes extensive insider vocabulary, work hacks, and mutual aid groups) and task variety as two of the most enjoyable aspects of the job. Task variety includes inspecting their vehicle and equipment, driving their truck, coordinating with crew members, lifting bins and bags, detecting incorrect sorting of waste, and unloading at the end destination. This finding matters because some types of robotic solutions will eliminate the parts of the job that workers most appreciate. For instance, the National Institute for Occupational Safety and Health (NIOSH) recommends the adoption of automated side loader trucks and collision avoidance systems . This innovation increases safety, which is great, but it also results in a sole worker operating a joystick in a cab, surrounded by sensor and camera surveillance. Instead, we should challenge ourselves to think of solutions that make jobs safer without making them terrible in a different way. To do this, we need to understand all aspects of what makes a job dull, dirty, or dangerous (or not). Our framework aims to facilitate this understanding. Finally, it’s important to note that DDD is only one of many possible approaches to classify what work might be better served by robots. There are lots of ways we could think about which types of tasks or jobs to automate (for example, economic impact or environmental sustainability). Given the popularity of DDD in robotics, we chose this common phrase as a starting point. We would love to see more work in this space, whether it’s data collection on DDD itself or the creation of other frameworks. At RAI , we believe that the fusion of robotics and social sciences opens a whole new world of information, perspectives, opportunities, and value. It fosters a culture of curiosity and mutual learning, and allows us to create actionable tools for anyone in robotics who cares about societal impact. Dull, Dirty, Dangerous: Understanding the Past, Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was presented at the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI) in Edinburgh, Scotland.

## Overview
For years, the field of robotics has used the terms “dull, dirty, and dangerous” (DDD) to describe the types of tasks or jobs where robots might be useful—by doing work that’s undesirable for people. A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for our technology. First, we did an empirical analysis of robotics publications between 1980 and 2024 that mention DDD and found that only 2.7 percent define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions vary, and many of the examples aren’t particularly specific (for example, “industrial manufacturing,” “home care”). Next, we reviewed the social science literature in anthropology, economics, political science, psychology, and sociology to develop better definitions for “dull,” “dirty,” and “dangerous” work. Again, while it might seem intuitive which tasks to put into these buckets, it turns out that there are some underlying social, economic, and cultural factors that matter. Dangerous Work: Occupations or tasks that result in injury or risk of harm It’s possible to measure the danger of a task or job by using reported information. There are administrative records and surveys that provide numbers on occupational injury rates and hazardous risk factors. While that seems straightforward, it’s important to understand how this data was collected, reported, and verified. First, occupational injuries tend to be underreported, with some studies estimating up to 70 percent of cases missing in administrative databases . Second, injuries and risk factors are rarely disaggregated by characteristics like gender, migration status, formal/informal employment, and work activities . For example, because most personal protective equipment—such as masks, vests, and gloves—are sized for men, women in dangerous work environments face increased safety risks . These caveats are an opportunity for robotics to be helpful. If we went out and looked for it, we could probably find some less obviously dangerous work where robotics might be an important intervention, not to mention some groups that are disproportionately affected and would benefit from more workplace safety. Dirty Work: Occupations or tasks that are physically, socially, or morally tainted Colloquially, most people might think of dirty work as involving physical dirtiness, such as trash removal, cleaning, or dealing with hazardous substances. But social science literature makes clear that dirty work is also about stigma . Socially tainted jobs are often servile or involve interacting with stigmatized groups (for example, correctional officers), and morally tainted jobs include tasks that people commonly perceive as sinful, deceptive, or otherwise defying norms of civility (like a stripper or a collection agent). “Dirty work” is a social construct that can vary across time (like tattoo industry stigma in the United States) and culture (such as nursing in the U.S . versus in Bangladesh ). One way to measure whether work is “dirty” is by using the closely related concept of occupational prestige, captured through quantitative surveys where people rank jobs. Another way to measure it is through qualitative data, like ethnographies and interviews. Similar to “dangerous,” we see some hidden opportunities for robotics in “dirty” work. But one of our more interesting takeaways from the data is that a lower-ranked job can be something that the workers themselves enjoy or find immense pride and meaning in . If we care about what tasks are truly undesirable, understanding this worker perspective is important. Dull Work: Occupations or tasks that are repetitive and lacking in autonomy When it comes to defining dull work, what matters most is workers’ own experiences. Outsiders can make a lot of false assumptions about what tasks have value and meaning. Sometimes things that seem boring or routine create the right conditions for developing skills and competence , such as the concentration needed for woodworking, or for socializing and support , when tasks are done alongside others. Instead of assuming that repetitive work is negative, it’s important to examine qualitative data on how people experience the work and what purpose it serves for them . DDD: An actionable framework In our paper, we propose a framework to help the robotics community explore how automation impacts individual jobs. For each term—dull, dirty, and dangerous—the framework gathers key pieces of information to reflect on what physical or social aspects of the task are, in fact, DDD. Worker perspective is an important part of all three considerations. The framework also emphasizes awareness of context—meaning the physical and social environment of an occupation and industry that can influence the DDD nature of a task. Our corresponding worksheet suggests existing data sources to draw on and encourages us to seek out multiple perspectives and consider potential sources of bias in the information. What makes tasks dull, dirty, or dangerous depends on the perspective of the humans doing those tasks. RAI Let’s take, for example, the waste and recycling industry . The world generates over 2 billion tonnes of waste annually, and this figure is expected to rise to nearly 4 billion tonnes by 2050 . Intuitively, trash collection seems like a job that hits all the Ds. Going through our worksheet, we confirm that globally, workers in this industry face significant health hazards (dangerous), and waste collection is ranked as a low-status job (dirty), although interestingly, many workers take pride in providing this essential service . The job is also repetitive, but there are aspects that make it not dull . Specifically, workers cite the day-to-day interaction with their coworkers (which includes extensive insider vocabulary, work hacks, and mutual aid groups) and task variety as two of the most enjoyable aspects of the job. Task variety includes inspecting their vehicle and equipment, driving their truck, coordinating with crew members, lifting bins and bags, detecting incorrect sorting of waste, and unloading at the end destination. This finding matters because some types of robotic solutions will eliminate the parts of the job that workers most appreciate. For instance, the National Institute for Occupational Safety and Health (NIOSH) recommends the adoption of automated side loader trucks and collision avoidance systems . This innovation increases safety, which is great, but it also results in a sole worker operating a joystick in a cab, surrounded by sensor and camera surveillance. Instead, we should challenge ourselves to think of solutions that make jobs safer without making them terrible in a different way. To do this, we need to understand all aspects of what makes a job dull, dirty, or dangerous (or not). Our framework aims to facilitate this understanding. Finally, it’s important to note that DDD is only one of many possible approaches to classify what work might be better served by robots. There are lots of ways we could think about which types of tasks or jobs to automate (for example, economic impact or environmental sustainability). Given the popularity of DDD in robotics, we chose this common phrase as a starting point. We would love to see more work in this space, whether it’s data collection on DDD itself or the creation of other frameworks. At RAI , we believe that the fusion of robotics and social sciences opens a whole new world of information, perspectives, opportunities, and value. It fosters a culture of curiosity and mutual learning, and allows us to create actionable tools for anyone in robotics who cares about societal impact. Dull, Dirty, Dangerous: Understanding the Past, Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was presented at the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI) in Edinburgh, Scotland.

## 개요
For years, the field of robotics has used the terms “dull, dirty, and dangerous” (DDD) to describe the types of tasks or jobs where robots might be useful—by doing work that’s undesirable for people. A classic example of a DDD job is one of “repetitive physical labor on a steaming hot factory floor involving heavy machinery that threatens life and limb.” But determining which human activities fit into these categories is not as straightforward as it seems. What exactly is a “dull” task, and who makes that assumption? Is “dirty” work just about needing to wash your hands afterwards, or is there also an aspect of social stigma? What data can we rely on to classify jobs as “dangerous?” Our recent work (which was not dull at all) tackles these questions and proposes a framework to help roboticists understand the job context for our technology. First, we did an empirical analysis of robotics publications between 1980 and 2024 that mention DDD and found that only 2.7 percent define DDD and only 8.7 percent provide examples of tasks or jobs. The definitions vary, and many of the examples aren’t particularly specific (for example, “industrial manufacturing,” “home care”). Next, we reviewed the social science literature in anthropology, economics, political science, psychology, and sociology to develop better definitions for “dull,” “dirty,” and “dangerous” work. Again, while it might seem intuitive which tasks to put into these buckets, it turns out that there are some underlying social, economic, and cultural factors that matter. Dangerous Work: Occupations or tasks that result in injury or risk of harm It’s possible to measure the danger of a task or job by using reported information. There are administrative records and surveys that provide numbers on occupational injury rates and hazardous risk factors. While that seems straightforward, it’s important to understand how this data was collected, reported, and verified. First, occupational injuries tend to be underreported, with some studies estimating up to 70 percent of cases missing in administrative databases . Second, injuries and risk factors are rarely disaggregated by characteristics like gender, migration status, formal/informal employment, and work activities . For example, because most personal protective equipment—such as masks, vests, and gloves—are sized for men, women in dangerous work environments face increased safety risks . These caveats are an opportunity for robotics to be helpful. If we went out and looked for it, we could probably find some less obviously dangerous work where robotics might be an important intervention, not to mention some groups that are disproportionately affected and would benefit from more workplace safety. Dirty Work: Occupations or tasks that are physically, socially, or morally tainted Colloquially, most people might think of dirty work as involving physical dirtiness, such as trash removal, cleaning, or dealing with hazardous substances. But social science literature makes clear that dirty work is also about stigma . Socially tainted jobs are often servile or involve interacting with stigmatized groups (for example, correctional officers), and morally tainted jobs include tasks that people commonly perceive as sinful, deceptive, or otherwise defying norms of civility (like a stripper or a collection agent). “Dirty work” is a social construct that can vary across time (like tattoo industry stigma in the United States) and culture (such as nursing in the U.S . versus in Bangladesh ). One way to measure whether work is “dirty” is by using the closely related concept of occupational prestige, captured through quantitative surveys where people rank jobs. Another way to measure it is through qualitative data, like ethnographies and interviews. Similar to “dangerous,” we see some hidden opportunities for robotics in “dirty” work. But one of our more interesting takeaways from the data is that a lower-ranked job can be something that the workers themselves enjoy or find immense pride and meaning in . If we care about what tasks are truly undesirable, understanding this worker perspective is important. Dull Work: Occupations or tasks that are repetitive and lacking in autonomy When it comes to defining dull work, what matters most is workers’ own experiences. Outsiders can make a lot of false assumptions about what tasks have value and meaning. Sometimes things that seem boring or routine create the right conditions for developing skills and competence , such as the concentration needed for woodworking, or for socializing and support , when tasks are done alongside others. Instead of assuming that repetitive work is negative, it’s important to examine qualitative data on how people experience the work and what purpose it serves for them . DDD: An actionable framework In our paper, we propose a framework to help the robotics community explore how automation impacts individual jobs. For each term—dull, dirty, and dangerous—the framework gathers key pieces of information to reflect on what physical or social aspects of the task are, in fact, DDD. Worker perspective is an important part of all three considerations. The framework also emphasizes awareness of context—meaning the physical and social environment of an occupation and industry that can influence the DDD nature of a task. Our corresponding worksheet suggests existing data sources to draw on and encourages us to seek out multiple perspectives and consider potential sources of bias in the information. What makes tasks dull, dirty, or dangerous depends on the perspective of the humans doing those tasks. RAI Let’s take, for example, the waste and recycling industry . The world generates over 2 billion tonnes of waste annually, and this figure is expected to rise to nearly 4 billion tonnes by 2050 . Intuitively, trash collection seems like a job that hits all the Ds. Going through our worksheet, we confirm that globally, workers in this industry face significant health hazards (dangerous), and waste collection is ranked as a low-status job (dirty), although interestingly, many workers take pride in providing this essential service . The job is also repetitive, but there are aspects that make it not dull . Specifically, workers cite the day-to-day interaction with their coworkers (which includes extensive insider vocabulary, work hacks, and mutual aid groups) and task variety as two of the most enjoyable aspects of the job. Task variety includes inspecting their vehicle and equipment, driving their truck, coordinating with crew members, lifting bins and bags, detecting incorrect sorting of waste, and unloading at the end destination. This finding matters because some types of robotic solutions will eliminate the parts of the job that workers most appreciate. For instance, the National Institute for Occupational Safety and Health (NIOSH) recommends the adoption of automated side loader trucks and collision avoidance systems . This innovation increases safety, which is great, but it also results in a sole worker operating a joystick in a cab, surrounded by sensor and camera surveillance. Instead, we should challenge ourselves to think of solutions that make jobs safer without making them terrible in a different way. To do this, we need to understand all aspects of what makes a job dull, dirty, or dangerous (or not). Our framework aims to facilitate this understanding. Finally, it’s important to note that DDD is only one of many possible approaches to classify what work might be better served by robots. There are lots of ways we could think about which types of tasks or jobs to automate (for example, economic impact or environmental sustainability). Given the popularity of DDD in robotics, we chose this common phrase as a starting point. We would love to see more work in this space, whether it’s data collection on DDD itself or the creation of other frameworks. At RAI , we believe that the fusion of robotics and social sciences opens a whole new world of information, perspectives, opportunities, and value. It fosters a culture of curiosity and mutual learning, and allows us to create actionable tools for anyone in robotics who cares about societal impact. Dull, Dirty, Dangerous: Understanding the Past, Present, and Future of a Key Motivation for Robotics , by Nozomi Nakajima, Pedro Reynolds-Cuéllar, Caitrin Lynch, and Kate Darling from the RAI Institute, was presented at the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI) in Edinburgh, Scotland.
