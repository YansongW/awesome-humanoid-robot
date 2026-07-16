---
$id: ent_report_ieee_visual_language_models_train_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: Visual Language Models Train Robots to Read Human Emotions
  zh: Visual Language Models Train Robots to Read Human Emotions
  ko: Visual Language Models Train Robots to Read Human Emotions
summary:
  en: This article is part of our exclusive IEEE Journal Watch series in partnership with IEEE Xplore. As robots advance in
    terms of dexterity and other physical capabilities , it becomes more likely that humans may find themselves working alongside
    them. If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people?
    In a recent study, researchers trained collaborative robots to read human emotions by not only accounting for facial expressions,
    but also contextual factors in the interactions as well. Through experiments with 40 volunteers, the researchers then
    evaluated how a robot’s ability to read human emotions and adjust its behavior in turn impacted a human’s perception of
    the robot and its capabilities as the two collaborated on tasks. The results —which show that the emotional capabilities
    of robots only go so far with humans—were published 18 May in IEEE Robotics and Automation Letters . Seung Chan Hong led
    the study as part of his undergraduate thesis while studying at Monash University, in Melbourne, Australia. He notes that,
    while there has been a lot of hype in the advancing physical abilities of robots, this is only one piece of the puzzle.
    “We need to also innovate when it comes to them actually interacting with humans, not just their physical capabilities,”
    he says. This prompted him to dig deeper into the emotional aspects of human-robot interactions. First, Hong and his co-authors
    decided to train a robot to read human emotions using a vision language model (VLM), which is similar to large language
    models (LLMs) such as ChatGPT, but which can also take visual inputs. Training VLMs for Human Emotion Recognition To evaluate
    their VLM, which used Gemini 2.5, the researchers had volunteers watch videos of robots handing over objects to humans—with
    varying degrees of success—and describe the emotions the humans were expressing. Importantly, the volunteers labeling
    these videos were able to take into account more context in these interactions, rather than reporting solely on the facial
    expressions of the humans in the video. For example, a person pausing to think with a furrowed brow may simply be concentrating
    on their task at hand and not necessarily be angry. Contextual factors such as drumming their fingers, pursing their lips,
    or other behaviors can point to the real cause of a person’s furrowed brow. The researchers then compared their VLM to
    a conventional AI system that relies on standard facial analysis and object tracking that is used in human-robot interactions.
    They found that the VLM outperformed the traditional approach. On a scale from 0 (no similarity in meaning to the emotion
    identified by the human volunteers) to 1 (a perfect match in meaning), the conventional AI system achieved a score of
    0.77. In comparison, the VLM achieved a score of 0.86. Hong says, “I think [the VLM] was able to align with what human
    observers were seeing a lot better, because it wasn’t just looking at the person’s face for a brief amount of time, but
    seeing the whole scene—where the person was and what they were doing, and how they were interacting with the robot.” In
    a second experiment, the research team asked 40 volunteers to interact with a robot using their VLM—but purposefully programmed
    the robot to make an error. The robot then had to offer either an emotionally adaptive apology that accounted for the
    human’s perceived response to the mistake or a pre-scripted spoken apology. Participants overwhelmingly preferred the
    emotionally adaptive response, with 31 out of 40 people favoring this approach over a boilerplate apology. However, their
    survey responses underscored how this emotional adaptivity was far less important than the robot’s functionality. After
    collaborating with a robot that failed in its task, many participants ranked their trust in the robot as lower, regardless
    of how it apologized for its mistake. “A personalized apology acts as a social lubricant, but it cannot repair the trust
    lost by the robot failing its physical task,” Hong says. Interestingly, the VLM classified the emotions of its human partners
    similarly to human volunteers who observed an interaction from a third-party perspective. But when the VLM’s assessments
    were measured against humans’ self-reported emotions during the second experiment—the most accurate descriptions of their
    true emotions—its ability to accurately predict emotions dropped significantly. “While the VLM is a good observer of outward
    social cues, it isn’t a mind reader,” Hong says. “It matched third-person human observers well, but it didn’t always align
    with the users‘ internal, self-reported feelings.” Together, these results show that robots are not perfect at reading
    human emotions. So while people might appreciate their efforts, they still ultimately will want competent co-workers.
    This story was updated on 15 June 2026 to correct where the research was conducted and clarify that the researchers evaluated
    the performance of a pre-trained model.
  zh: This article is part of our exclusive IEEE Journal Watch series in partnership with IEEE Xplore. As robots advance in
    terms of dexterity and other physical capabilities , it becomes more likely that humans may find themselves working alongside
    them. If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people?
    In a recent study, researchers trained collaborative robots to read human emotions by not only accounting for facial expressions,
    but also contextual factors in the interactions as well. Through experiments with 40 volunteers, the researchers then
    evaluated how a robot’s ability to read human emotions and adjust its behavior in turn impacted a human’s perception of
    the robot and its capabilities as the two collaborated on tasks. The results —which show that the emotional capabilities
    of robots only go so far with humans—were published 18 May in IEEE Robotics and Automation Letters . Seung Chan Hong led
    the study as part of his undergraduate thesis while studying at Monash University, in Melbourne, Australia. He notes that,
    while there has been a lot of hype in the advancing physical abilities of robots, this is only one piece of the puzzle.
    “We need to also innovate when it comes to them actually interacting with humans, not just their physical capabilities,”
    he says. This prompted him to dig deeper into the emotional aspects of human-robot interactions. First, Hong and his co-authors
    decided to train a robot to read human emotions using a vision language model (VLM), which is similar to large language
    models (LLMs) such as ChatGPT, but which can also take visual inputs. Training VLMs for Human Emotion Recognition To evaluate
    their VLM, which used Gemini 2.5, the researchers had volunteers watch videos of robots handing over objects to humans—with
    varying degrees of success—and describe the emotions the humans were expressing. Importantly, the volunteers labeling
    these videos were able to take into account more context in these interactions, rather than reporting solely on the facial
    expressions of the humans in the video. For example, a person pausing to think with a furrowed brow may simply be concentrating
    on their task at hand and not necessarily be angry. Contextual factors such as drumming their fingers, pursing their lips,
    or other behaviors can point to the real cause of a person’s furrowed brow. The researchers then compared their VLM to
    a conventional AI system that relies on standard facial analysis and object tracking that is used in human-robot interactions.
    They found that the VLM outperformed the traditional approach. On a scale from 0 (no similarity in meaning to the emotion
    identified by the human volunteers) to 1 (a perfect match in meaning), the conventional AI system achieved a score of
    0.77. In comparison, the VLM achieved a score of 0.86. Hong says, “I think [the VLM] was able to align with what human
    observers were seeing a lot better, because it wasn’t just looking at the person’s face for a brief amount of time, but
    seeing the whole scene—where the person was and what they were doing, and how they were interacting with the robot.” In
    a second experiment, the research team asked 40 volunteers to interact with a robot using their VLM—but purposefully programmed
    the robot to make an error. The robot then had to offer either an emotionally adaptive apology that accounted for the
    human’s perceived response to the mistake or a pre-scripted spoken apology. Participants overwhelmingly preferred the
    emotionally adaptive response, with 31 out of 40 people favoring this approach over a boilerplate apology. However, their
    survey responses underscored how this emotional adaptivity was far less important than the robot’s functionality. After
    collaborating with a robot that failed in its task, many participants ranked their trust in the robot as lower, regardless
    of how it apologized for its mistake. “A personalized apology acts as a social lubricant, but it cannot repair the trust
    lost by the robot failing its physical task,” Hong says. Interestingly, the VLM classified the emotions of its human partners
    similarly to human volunteers who observed an interaction from a third-party perspective. But when the VLM’s assessments
    were measured against humans’ self-reported emotions during the second experiment—the most accurate descriptions of their
    true emotions—its ability to accurately predict emotions dropped significantly. “While the VLM is a good observer of outward
    social cues, it isn’t a mind reader,” Hong says. “It matched third-person human observers well, but it didn’t always align
    with the users‘ internal, self-reported feelings.” Together, these results show that robots are not perfect at reading
    human emotions. So while people might appreciate their efforts, they still ultimately will want competent co-workers.
    This story was updated on 15 June 2026 to correct where the research was conducted and clarify that the researchers evaluated
    the performance of a pre-trained model.
  ko: This article is part of our exclusive IEEE Journal Watch series in partnership with IEEE Xplore. As robots advance in
    terms of dexterity and other physical capabilities , it becomes more likely that humans may find themselves working alongside
    them. If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people?
    In a recent study, researchers trained collaborative robots to read human emotions by not only accounting for facial expressions,
    but also contextual factors in the interactions as well. Through experiments with 40 volunteers, the researchers then
    evaluated how a robot’s ability to read human emotions and adjust its behavior in turn impacted a human’s perception of
    the robot and its capabilities as the two collaborated on tasks. The results —which show that the emotional capabilities
    of robots only go so far with humans—were published 18 May in IEEE Robotics and Automation Letters . Seung Chan Hong led
    the study as part of his undergraduate thesis while studying at Monash University, in Melbourne, Australia. He notes that,
    while there has been a lot of hype in the advancing physical abilities of robots, this is only one piece of the puzzle.
    “We need to also innovate when it comes to them actually interacting with humans, not just their physical capabilities,”
    he says. This prompted him to dig deeper into the emotional aspects of human-robot interactions. First, Hong and his co-authors
    decided to train a robot to read human emotions using a vision language model (VLM), which is similar to large language
    models (LLMs) such as ChatGPT, but which can also take visual inputs. Training VLMs for Human Emotion Recognition To evaluate
    their VLM, which used Gemini 2.5, the researchers had volunteers watch videos of robots handing over objects to humans—with
    varying degrees of success—and describe the emotions the humans were expressing. Importantly, the volunteers labeling
    these videos were able to take into account more context in these interactions, rather than reporting solely on the facial
    expressions of the humans in the video. For example, a person pausing to think with a furrowed brow may simply be concentrating
    on their task at hand and not necessarily be angry. Contextual factors such as drumming their fingers, pursing their lips,
    or other behaviors can point to the real cause of a person’s furrowed brow. The researchers then compared their VLM to
    a conventional AI system that relies on standard facial analysis and object tracking that is used in human-robot interactions.
    They found that the VLM outperformed the traditional approach. On a scale from 0 (no similarity in meaning to the emotion
    identified by the human volunteers) to 1 (a perfect match in meaning), the conventional AI system achieved a score of
    0.77. In comparison, the VLM achieved a score of 0.86. Hong says, “I think [the VLM] was able to align with what human
    observers were seeing a lot better, because it wasn’t just looking at the person’s face for a brief amount of time, but
    seeing the whole scene—where the person was and what they were doing, and how they were interacting with the robot.” In
    a second experiment, the research team asked 40 volunteers to interact with a robot using their VLM—but purposefully programmed
    the robot to make an error. The robot then had to offer either an emotionally adaptive apology that accounted for the
    human’s perceived response to the mistake or a pre-scripted spoken apology. Participants overwhelmingly preferred the
    emotionally adaptive response, with 31 out of 40 people favoring this approach over a boilerplate apology. However, their
    survey responses underscored how this emotional adaptivity was far less important than the robot’s functionality. After
    collaborating with a robot that failed in its task, many participants ranked their trust in the robot as lower, regardless
    of how it apologized for its mistake. “A personalized apology acts as a social lubricant, but it cannot repair the trust
    lost by the robot failing its physical task,” Hong says. Interestingly, the VLM classified the emotions of its human partners
    similarly to human volunteers who observed an interaction from a third-party perspective. But when the VLM’s assessments
    were measured against humans’ self-reported emotions during the second experiment—the most accurate descriptions of their
    true emotions—its ability to accurately predict emotions dropped significantly. “While the VLM is a good observer of outward
    social cues, it isn’t a mind reader,” Hong says. “It matched third-person human observers well, but it didn’t always align
    with the users‘ internal, self-reported feelings.” Together, these results show that robots are not perfect at reading
    human emotions. So while people might appreciate their efforts, they still ultimately will want competent co-workers.
    This story was updated on 15 June 2026 to correct where the research was conducted and clarify that the researchers evaluated
    the performance of a pre-trained model.
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
- iso
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
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/robot-emotions-visual-language-models.
sources:
- id: src_001
  type: website
  title: Visual Language Models Train Robots to Read Human Emotions
  url: https://spectrum.ieee.org/robot-emotions-visual-language-models
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
If robots are ever going to work alongside humans more generally, they’ll need to read our moods As robots advance in

## 核心内容
This article is part of our exclusive IEEE Journal Watch series in partnership with IEEE Xplore. As robots advance in terms of dexterity and other physical capabilities , it becomes more likely that humans may find themselves working alongside them. If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people? In a recent study, researchers trained collaborative robots to read human emotions by not only accounting for facial expressions, but also contextual factors in the interactions as well. Through experiments with 40 volunteers, the researchers then evaluated how a robot’s ability to read human emotions and adjust its behavior in turn impacted a human’s perception of the robot and its capabilities as the two collaborated on tasks. The results —which show that the emotional capabilities of robots only go so far with humans—were published 18 May in IEEE Robotics and Automation Letters . Seung Chan Hong led the study as part of his undergraduate thesis while studying at Monash University, in Melbourne, Australia. He notes that, while there has been a lot of hype in the advancing physical abilities of robots, this is only one piece of the puzzle. “We need to also innovate when it comes to them actually interacting with humans, not just their physical capabilities,” he says. This prompted him to dig deeper into the emotional aspects of human-robot interactions. First, Hong and his co-authors decided to train a robot to read human emotions using a vision language model (VLM), which is similar to large language models (LLMs) such as ChatGPT, but which can also take visual inputs. Training VLMs for Human Emotion Recognition To evaluate their VLM, which used Gemini 2.5, the researchers had volunteers watch videos of robots handing over objects to humans—with varying degrees of success—and describe the emotions the humans were expressing. Importantly, the volunteers labeling these videos were able to take into account more context in these interactions, rather than reporting solely on the facial expressions of the humans in the video. For example, a person pausing to think with a furrowed brow may simply be concentrating on their task at hand and not necessarily be angry. Contextual factors such as drumming their fingers, pursing their lips, or other behaviors can point to the real cause of a person’s furrowed brow. The researchers then compared their VLM to a conventional AI system that relies on standard facial analysis and object tracking that is used in human-robot interactions. They found that the VLM outperformed the traditional approach. On a scale from 0 (no similarity in meaning to the emotion identified by the human volunteers) to 1 (a perfect match in meaning), the conventional AI system achieved a score of 0.77. In comparison, the VLM achieved a score of 0.86. Hong says, “I think [the VLM] was able to align with what human observers were seeing a lot better, because it wasn’t just looking at the person’s face for a brief amount of time, but seeing the whole scene—where the person was and what they were doing, and how they were interacting with the robot.” In a second experiment, the research team asked 40 volunteers to interact with a robot using their VLM—but purposefully programmed the robot to make an error. The robot then had to offer either an emotionally adaptive apology that accounted for the human’s perceived response to the mistake or a pre-scripted spoken apology. Participants overwhelmingly preferred the emotionally adaptive response, with 31 out of 40 people favoring this approach over a boilerplate apology. However, their survey responses underscored how this emotional adaptivity was far less important than the robot’s functionality. After collaborating with a robot that failed in its task, many participants ranked their trust in the robot as lower, regardless of how it apologized for its mistake. “A personalized apology acts as a social lubricant, but it cannot repair the trust lost by the robot failing its physical task,” Hong says. Interestingly, the VLM classified the emotions of its human partners similarly to human volunteers who observed an interaction from a third-party perspective. But when the VLM’s assessments were measured against humans’ self-reported emotions during the second experiment—the most accurate descriptions of their true emotions—its ability to accurately predict emotions dropped significantly. “While the VLM is a good observer of outward social cues, it isn’t a mind reader,” Hong says. “It matched third-person human observers well, but it didn’t always align with the users‘ internal, self-reported feelings.” Together, these results show that robots are not perfect at reading human emotions. So while people might appreciate their efforts, they still ultimately will want competent co-workers. This story was updated on 15 June 2026 to correct where the research was conducted and clarify that the researchers evaluated the performance of a pre-trained model. If robots are ever going to work alongside humans more generally, they’ll need to read our moods As robots advance in If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people?

## 参考
- https://spectrum.ieee.org/robot-emotions-visual-language-models
