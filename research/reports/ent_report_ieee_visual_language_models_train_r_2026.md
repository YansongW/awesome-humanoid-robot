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
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://spectrum.ieee.org/robot-emotions-visual-language-models.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (1058 chars, DeepSeek).'
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

## 参考
- https://spectrum.ieee.org/robot-emotions-visual-language-models

## 개요
로봇의 손재주와 물리적 능력이 향상됨에 따라 인간-로봇 협업 시나리오가 증가하고 있지만, 로봇의 감정 능력이 어떻게 발전해야 인간을 효과적으로 보조할 수 있을까? Seung Chan Hong이 Monash University 학부 논문에서 주도한 연구는 Gemini 2.5 기반의 비전-언어 모델(VLM)을 사용하여 협업 로봇이 인간의 감정을 읽도록 훈련했으며, 얼굴 표정뿐만 아니라 손가락 두드리기, 입술을 다무는 행동과 같은 상황적 단서도 고려했습니다. 40명의 자원자를 대상으로 한 실험에서 VLM은 감정 인식에서 1점 만점에 0.86점을 기록하며 기존 AI 시스템의 0.77점을 능가했습니다. 그러나 로봇이 의도적으로 실수를 저지른 후 사과하는 실험에서는 31/40의 참가자가 감정 적응형 사과를 선호했지만, 작업 실패는 여전히 로봇에 대한 신뢰를 크게 낮추어 감정 능력이 기능적 결함을 보완할 수 없음을 보여주었습니다.

## 핵심 내용
### 연구 배경 및 동기
- 로봇의 물리적 능력(예: 손재주)의 발전으로 인간과의 협업 가능성이 높아졌지만, 감정 능력의 발전도 동일하게 중요합니다.
- 기존 연구는 주로 얼굴 표정 인식에 초점을 맞추었으며, 상호작용 중의 상황적 요소(예: 제스처, 작업 맥락)를 간과했습니다.

### 방법: VLM 기반 감정 인식
- Gemini 2.5를 VLM 기반 모델로 사용했으며, 이 모델은 ChatGPT와 같은 대규모 언어 모델(LLM)과 유사하지만 시각적 입력을 처리할 수 있습니다.
- 훈련 데이터: 자원자들이 로봇이 인간에게 물체를 전달하는(성공 정도가 다른) 비디오를 시청하고 인간이 표현한 감정을 설명했습니다. 주석자는 얼굴 표정만이 아닌 전체 장면을 고려해야 했습니다(예: 찡그림은 분노가 아닌 집중에서 비롯될 수 있음).
- 비교 기준: 표준 얼굴 분석 및 객체 추적에 의존하는 기존 AI 시스템.

### 실험 설정 및 주요 결과
- **실험 1: VLM vs 기존 AI**
  - 평가 기준: 0(인간 자원자가 식별한 감정과 유사성 없음)부터 1(완전 일치)까지.
  - 기존 AI 점수: 0.77; VLM 점수: 0.86.
  - 우위 요인: VLM은 짧은 얼굴 스냅샷이 아닌 전체 장면(인간의 위치, 행동, 로봇과의 상호작용)을 관찰할 수 있습니다.

- **실험 2: 로봇 사과 및 신뢰 평가**
  - 40명의 자원자가 VLM을 탑재한 로봇과 협업했으며, 로봇은 의도적으로 실수를 하도록 프로그래밍되었습니다.
  - 사과 방식: 감정 적응형 사과(인간 반응에 따라 조정) vs 사전 설정된 스크립트 사과.
  - 선호 결과: 31/40명이 감정 적응형 사과를 선호했습니다.
  - 신뢰 영향: 사과 방식과 관계없이 작업 실패 후 자원자의 로봇에 대한 신뢰 점수는 모두 낮아졌습니다. Hong은 "개인화된 사과는 사회적 윤활제이지만, 물리적 작업 실패로 인해 상실된 신뢰를 복구할 수는 없습니다."라고 지적했습니다.

### 주요 발견 및 한계
- VLM은 제3자 관점에서 인간 관찰자의 감정 판단과 높은 일치를 보였지만, 자원자가 스스로 보고한 실제 감정과 비교했을 때 예측 정확도는 크게 떨어졌습니다. Hong은 "VLM은 훌륭한 외부 사회적 단서 관찰자이지만, 마음을 읽는 자는 아닙니다."라고 요약했습니다.
- 결론: 로봇의 감정 능력은 제한적이며, 인간은 궁극적으로 감정적 상호작용보다 협업 능력을 더 중요하게 여깁니다.
