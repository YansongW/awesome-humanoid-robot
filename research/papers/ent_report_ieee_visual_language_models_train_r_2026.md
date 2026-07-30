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
  zh: 澳大利亚莫纳什大学Seung Chan Hong领导的研究团队训练协作机器人通过视觉语言模型（VLM）读取人类情绪，不仅分析面部表情，还结合交互中的情境因素。实验表明，VLM在情绪识别上优于传统AI系统（得分0.86 vs 0.77），但机器人情绪能力对修复因任务失败而损失的信任作用有限。该研究发表于2026年5月18日的《IEEE
    Robotics and Automation Letters》。
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
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Visual Language Models Train Robots to Read Human Emotions
  url: https://spectrum.ieee.org/robot-emotions-visual-language-models
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
随着机器人灵巧性和物理能力的提升，人机协作场景日益增多，但机器人的情绪能力如何发展才能有效配合人类？Seung Chan Hong在莫纳什大学本科论文中领导的研究，训练协作机器人使用基于Gemini 2.5的视觉语言模型（VLM）读取人类情绪，不仅依赖面部表情，还考虑手指敲击、嘴唇抿动等情境线索。通过40名志愿者的实验，VLM在情绪识别上以0.86分（满分1分）超越传统AI系统的0.77分。然而，在机器人故意犯错后的道歉实验中，尽管31/40的参与者偏好情绪自适应道歉，但任务失败仍显著降低了对机器人的信任，表明情绪能力无法弥补功能缺陷。

## 核心内容
### 研究背景与动机
- 机器人物理能力（如灵巧性）的进步使人类更可能与其协作，但情绪能力的发展同样关键。
- 现有研究多聚焦于面部表情识别，忽略了交互中的情境因素（如手势、任务上下文）。

### 方法：基于VLM的情绪识别
- 使用Gemini 2.5作为VLM基础模型，该模型类似ChatGPT等大语言模型（LLM），但能处理视觉输入。
- 训练数据：志愿者观看机器人向人类递送物体（成功程度不同）的视频，并描述人类表达的情绪。标注者需考虑整体场景，而非仅面部表情（例如：皱眉可能源于专注而非愤怒）。
- 对比基线：传统AI系统，依赖标准面部分析和目标跟踪。

### 实验设置与关键结果
- **实验1：VLM vs 传统AI**
  - 评分标准：0（与人类志愿者识别的情绪无相似性）到1（完全匹配）。
  - 传统AI得分：0.77；VLM得分：0.86。
  - 优势来源：VLM能观察整个场景（人的位置、行为、与机器人的交互），而非短暂的面部快照。

- **实验2：机器人道歉与信任评估**
  - 40名志愿者与搭载VLM的机器人协作，机器人被故意编程犯错。
  - 道歉方式：情绪自适应道歉（根据人类反应调整） vs 预设脚本道歉。
  - 偏好结果：31/40人偏好情绪自适应道歉。
  - 信任影响：无论道歉方式如何，任务失败后志愿者对机器人的信任评分均降低。Hong指出：“个性化道歉是社交润滑剂，但无法修复因物理任务失败而损失的信任。”

### 关键发现与局限性
- VLM在第三方视角下与人类观察者的情绪判断高度一致，但对照志愿者自我报告的真实情绪时，预测准确率显著下降。Hong总结：“VLM是优秀的外部社交线索观察者，但不是读心者。”
- 结论：机器人情绪能力有限，人类最终更看重协作能力而非情绪互动。

## Overview
If robots are ever going to work alongside humans more generally, they’ll need to read our moods As robots advance in

This article is part of our exclusive IEEE Journal Watch series in partnership with IEEE Xplore. As robots advance in terms of dexterity and other physical capabilities , it becomes more likely that humans may find themselves working alongside them. If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people? In a recent study, researchers trained collaborative robots to read human emotions by not only accounting for facial expressions, but also contextual factors in the interactions as well. Through experiments with 40 volunteers, the researchers then evaluated how a robot’s ability to read human emotions and adjust its behavior in turn impacted a human’s perception of the robot and its capabilities as the two collaborated on tasks. The results —which show that the emotional capabilities of robots only go so far with humans—were published 18 May in IEEE Robotics and Automation Letters . Seung Chan Hong led the study as part of his undergraduate thesis while studying at Monash University, in Melbourne, Australia. He notes that, while there has been a lot of hype in the advancing physical abilities of robots, this is only one piece of the puzzle. “We need to also innovate when it comes to them actually interacting with humans, not just their physical capabilities,” he says. This prompted him to dig deeper into the emotional aspects of human-robot interactions. First, Hong and his co-authors decided to train a robot to read human emotions using a vision language model (VLM), which is similar to large language models (LLMs) such as ChatGPT, but which can also take visual inputs. Training VLMs for Human Emotion Recognition To evaluate their VLM, which used Gemini 2.5, the researchers had volunteers watch videos of robots handing over objects to humans—with varying degrees of success—and describe the emotions the humans were expressing. Importantly, the volunteers labeling these videos were able to take into account more context in these interactions, rather than reporting solely on the facial expressions of the humans in the video. For example, a person pausing to think with a furrowed brow may simply be concentrating on their task at hand and not necessarily be angry. Contextual factors such as drumming their fingers, pursing their lips, or other behaviors can point to the real cause of a person’s furrowed brow. The researchers then compared their VLM to a conventional AI system that relies on standard facial analysis and object tracking that is used in human-robot interactions. They found that the VLM outperformed the traditional approach. On a scale from 0 (no similarity in meaning to the emotion identified by the human volunteers) to 1 (a perfect match in meaning), the conventional AI system achieved a score of 0.77. In comparison, the VLM achieved a score of 0.86. Hong says, “I think [the VLM] was able to align with what human observers were seeing a lot better, because it wasn’t just looking at the person’s face for a brief amount of time, but seeing the whole scene—where the person was and what they were doing, and how they were interacting with the robot.” In a second experiment, the research team asked 40 volunteers to interact with a robot using their VLM—but purposefully programmed the robot to make an error. The robot then had to offer either an emotionally adaptive apology that accounted for the human’s perceived response to the mistake or a pre-scripted spoken apology. Participants overwhelmingly preferred the emotionally adaptive response, with 31 out of 40 people favoring this approach over a boilerplate apology. However, their survey responses underscored how this emotional adaptivity was far less important than the robot’s functionality. After collaborating with a robot that failed in its task, many participants ranked their trust in the robot as lower, regardless of how it apologized for its mistake. “A personalized apology acts as a social lubricant, but it cannot repair the trust lost by the robot failing its physical task,” Hong says. Interestingly, the VLM classified the emotions of its human partners similarly to human volunteers who observed an interaction from a third-party perspective. But when the VLM’s assessments were measured against humans’ self-reported emotions during the second experiment—the most accurate descriptions of their true emotions—its ability to accurately predict emotions dropped significantly. “While the VLM is a good observer of outward social cues, it isn’t a mind reader,” Hong says. “It matched third-person human observers well, but it didn’t always align with the users‘ internal, self-reported feelings.” Together, these results show that robots are not perfect at reading human emotions. So while people might appreciate their efforts, they still ultimately will want competent co-workers. This story was updated on 15 June 2026 to correct where the research was conducted and clarify that the researchers evaluated the performance of a pre-trained model. If robots are ever going to work alongside humans more generally, they’ll need to read our moods As robots advance in If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people?

## Overview
If robots are ever going to work alongside humans more generally, they’ll need to read our moods. As robots advance in

## Content
This article is part of our exclusive IEEE Journal Watch series in partnership with IEEE Xplore. As robots advance in terms of dexterity and other physical capabilities, it becomes more likely that humans may find themselves working alongside them. If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people? In a recent study, researchers trained collaborative robots to read human emotions by not only accounting for facial expressions, but also contextual factors in the interactions as well. Through experiments with 40 volunteers, the researchers then evaluated how a robot’s ability to read human emotions and adjust its behavior in turn impacted a human’s perception of the robot and its capabilities as the two collaborated on tasks. The results —which show that the emotional capabilities of robots only go so far with humans—were published 18 May in IEEE Robotics and Automation Letters. Seung Chan Hong led the study as part of his undergraduate thesis while studying at Monash University, in Melbourne, Australia. He notes that, while there has been a lot of hype in the advancing physical abilities of robots, this is only one piece of the puzzle. “We need to also innovate when it comes to them actually interacting with humans, not just their physical capabilities,” he says. This prompted him to dig deeper into the emotional aspects of human-robot interactions. First, Hong and his co-authors decided to train a robot to read human emotions using a vision language model (VLM), which is similar to large language models (LLMs) such as ChatGPT, but which can also take visual inputs. Training VLMs for Human Emotion Recognition To evaluate their VLM, which used Gemini 2.5, the researchers had volunteers watch videos of robots handing over objects to humans—with varying degrees of success—and describe the emotions the humans were expressing. Importantly, the volunteers labeling these videos were able to take into account more context in these interactions, rather than reporting solely on the facial expressions of the humans in the video. For example, a person pausing to think with a furrowed brow may simply be concentrating on their task at hand and not necessarily be angry. Contextual factors such as drumming their fingers, pursing their lips, or other behaviors can point to the real cause of a person’s furrowed brow. The researchers then compared their VLM to a conventional AI system that relies on standard facial analysis and object tracking that is used in human-robot interactions. They found that the VLM outperformed the traditional approach. On a scale from 0 (no similarity in meaning to the emotion identified by the human volunteers) to 1 (a perfect match in meaning), the conventional AI system achieved a score of 0.77. In comparison, the VLM achieved a score of 0.86. Hong says, “I think [the VLM] was able to align with what human observers were seeing a lot better, because it wasn’t just looking at the person’s face for a brief amount of time, but seeing the whole scene—where the person was and what they were doing, and how they were interacting with the robot.” In a second experiment, the research team asked 40 volunteers to interact with a robot using their VLM—but purposefully programmed the robot to make an error. The robot then had to offer either an emotionally adaptive apology that accounted for the human’s perceived response to the mistake or a pre-scripted spoken apology. Participants overwhelmingly preferred the emotionally adaptive response, with 31 out of 40 people favoring this approach over a boilerplate apology. However, their survey responses underscored how this emotional adaptivity was far less important than the robot’s functionality. After collaborating with a robot that failed in its task, many participants ranked their trust in the robot as lower, regardless of how it apologized for its mistake. “A personalized apology acts as a social lubricant, but it cannot repair the trust lost by the robot failing its physical task,” Hong says. Interestingly, the VLM classified the emotions of its human partners similarly to human volunteers who observed an interaction from a third-party perspective. But when the VLM’s assessments were measured against humans’ self-reported emotions during the second experiment—the most accurate descriptions of their true emotions—its ability to accurately predict emotions dropped significantly. “While the VLM is a good observer of outward social cues, it isn’t a mind reader,” Hong says. “It matched third-person human observers well, but it didn’t always align with the users‘ internal, self-reported feelings.” Together, these results show that robots are not perfect at reading human emotions. So while people might appreciate their efforts, they still ultimately will want competent co-workers. This story was updated on 15 June 2026 to correct where the research was conducted and clarify that the researchers evaluated the performance of a pre-trained model. If robots are ever going to work alongside humans more generally, they’ll need to read our moods. As robots advance in If that happens, how will robots’ emotional capabilities need to advance for them to successfully work with people?

## 개요
로봇이 언젠가 인간과 더 일반적으로 함께 일하게 된다면, 우리의 기분을 읽을 수 있어야 할 것입니다. 로봇이 발전함에 따라

## 핵심 내용
이 기사는 IEEE Xplore와 협력하여 제공하는 독점 IEEE Journal Watch 시리즈의 일부입니다. 로봇이 손재주 및 기타 물리적 능력 측면에서 발전함에 따라 인간이 로봇과 함께 일할 가능성이 높아지고 있습니다. 그렇게 된다면, 로봇이 인간과 성공적으로 협력하기 위해 감정적 능력이 어떻게 발전해야 할까요? 최근 연구에서 연구자들은 협동 로봇이 표정뿐만 아니라 상호작용의 맥락적 요소도 고려하여 인간의 감정을 읽도록 훈련시켰습니다. 40명의 자원봉사자를 대상으로 한 실험을 통해, 연구자들은 로봇이 인간의 감정을 읽고 그에 따라 행동을 조정하는 능력이 두 사람이 협력하는 동안 로봇과 그 능력에 대한 인간의 인식에 어떤 영향을 미치는지 평가했습니다. 로봇의 감정 능력이 인간에게 한계가 있음을 보여주는 결과는 5월 18일 IEEE Robotics and Automation Letters에 게재되었습니다. Seung Chan Hong은 호주 멜버른의 Monash University에서 학부 논문의 일환으로 이 연구를 주도했습니다. 그는 로봇의 물리적 능력 향상에 대한 많은 과장이 있지만, 이것은 퍼즐의 한 조각에 불과하다고 지적합니다. "우리는 로봇이 실제로 인간과 상호작용할 때 혁신해야 하며, 단지 물리적 능력만이 아닙니다."라고 그는 말합니다. 이는 그가 인간-로봇 상호작용의 감정적 측면을 더 깊이 파고들게 했습니다. 먼저, Hong과 공동 저자들은 비전 언어 모델(VLM)을 사용하여 로봇이 인간의 감정을 읽도록 훈련시키기로 결정했습니다. VLM은 ChatGPT와 같은 대규모 언어 모델(LLM)과 유사하지만 시각적 입력도 처리할 수 있습니다. 인간 감정 인식을 위한 VLM 훈련 Gemini 2.5를 사용한 VLM을 평가하기 위해, 연구자들은 자원봉사자들에게 로봇이 인간에게 물건을 전달하는 비디오(성공 정도가 다양함)를 시청하게 하고, 인간이 표현하는 감정을 설명하도록 요청했습니다. 중요한 점은, 이 비디오에 레이블을 붙인 자원봉사자들이 비디오 속 인간의 표정만 보고하는 대신 상호작용의 더 많은 맥락을 고려할 수 있었다는 것입니다. 예를 들어, 찡그린 이마로 생각하며 멈추는 사람은 단순히 현재 작업에 집중하고 있을 뿐 반드시 화난 것은 아닙니다. 손가락을 두드리거나 입술을 오므리는 등의 맥락적 요소가 찡그린 이마의 실제 원인을 가리킬 수 있습니다. 연구자들은 그런 다음 VLM을 인간-로봇 상호작용에서 사용되는 표준 얼굴 분석 및 객체 추적에 의존하는 기존 AI 시스템과 비교했습니다. VLM이 전통적인 접근 방식보다 더 나은 성능을 보였습니다. 0(인간 자원봉사자가 식별한 감정과 의미상 유사성 없음)에서 1(의미상 완벽한 일치)까지의 척도에서 기존 AI 시스템은 0.77점을 기록했습니다. 반면 VLM은 0.86점을 기록했습니다. Hong은 "VLM이 인간 관찰자가 보는 것과 훨씬 더 잘 일치할 수 있었다고 생각합니다. 왜냐하면 잠시 동안 사람의 얼굴만 보는 것이 아니라 전체 장면(사람이 어디에 있고 무엇을 하고 있는지, 로봇과 어떻게 상호작용하는지)을 보기 때문입니다."라고 말합니다. 두 번째 실험에서 연구팀은 40명의 자원봉사자에게 VLM을 사용하는 로봇과 상호작용하도록 요청했지만, 의도적으로 로봇이 오류를 내도록 프로그래밍했습니다. 그런 다음 로봇은 인간의 실수에 대한 인식된 반응을 고려한 감정적으로 적응적인 사과나 미리 작성된 음성 사과 중 하나를 제공해야 했습니다. 참가자들은 압도적으로 감정적으로 적응적인 반응을 선호했으며, 40명 중 31명이 기본 사과보다 이 방식을 선호했습니다. 그러나 설문 조사 응답은 이러한 감정적 적응성이 로봇의 기능보다 훨씬 덜 중요하다는 점을 강조했습니다. 작업에 실패한 로봇과 협력한 후, 많은 참가자들은 로봇이 실수에 대해 어떻게 사과했는지와 관계없이 로봇에 대한 신뢰를 낮게 평가했습니다. Hong은 "개인화된 사과는 사회적 윤활제 역할을 하지만, 로봇이 물리적 작업에 실패하여 잃은 신뢰를 회복할 수는 없습니다."라고 말합니다. 흥미롭게도, VLM은 인간 파트너의 감정을 제3자 관점에서 상호작용을 관찰한 인간 자원봉사자와 유사하게 분류했습니다. 그러나 두 번째 실험에서 VLM의 평가를 인간의 자가 보고된 감정(가장 정확한 실제 감정 설명)과 비교했을 때, 감정을 정확히 예측하는 능력이 크게 떨어졌습니다. Hong은 "VLM은 외부 사회적 신호를 잘 관찰하지만, 마음을 읽는 것은 아닙니다. 제3자 인간 관찰자와는 잘 일치했지만, 사용자의 내부적 자가 보고된 감정과 항상 일치하지는 않았습니다."라고 말합니다. 종합적으로, 이러한 결과는 로봇이 인간의 감정을 완벽하게 읽지 못한다는 것을 보여줍니다. 따라서 사람들이 로봇의 노력을 인정할 수는 있지만, 궁극적으로는 유능한 동료를 원할 것입니다. 이 이야기는 연구가 수행된 장소를 수정하고 연구자들이 사전 훈련된 모델의 성능을 평가했음을 명확히 하기 위해 2026년 6월 15일에 업데이트되었습니다. 로봇이 언젠가 인간과 더 일반적으로 함께 일하게 된다면, 우리의 기분을 읽을 수 있어야 할 것입니다. 로봇이 발전함에 따라 그렇게 된다면, 로봇이 인간과 성공적으로 협력하기 위해 감정적 능력이 어떻게 발전해야 할까요?

## 参考
- https://spectrum.ieee.org/robot-emotions-visual-language-models
