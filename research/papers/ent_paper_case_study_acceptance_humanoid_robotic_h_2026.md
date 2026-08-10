---
$id: ent_paper_case_study_acceptance_humanoid_robotic_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Case Study on the Acceptance of a Humanoid Robotic Head Employed in Three Public Spaces
  zh: A Case Study on the Acceptance of a Humanoid Robotic Head Employed in Three Public Spaces
  ko: A Case Study on the Acceptance of a Humanoid Robotic Head Employed in Three Public Spaces
summary:
  en: Previous research has shown that a human-like robot's acceptance heavily depends on the setting in which it operates
    and its ability to perform relevant tasks. This paper, first, reports on how our robot processes natural language to generate
    a multimodal, verbal response integrating emotional expressions based on an emotion simulation backend. Then, it describes
    how visitors were invited to.
  zh: 本研究首次对同一台类人机器人头（Kim）在三个真实公共空间（旅游信息中心、建筑管理局、市图书馆）的接受度进行对比，使用基于 TAM2 的问卷测量。结果显示地点间无统计学显著差异，所有 TAM2 子量表得分中位数均高于中性值，但样本量小且存在未受控变量。
  ko: Previous research has shown that a human-like robot's acceptance heavily depends on the setting in which it operates
    and its ability to perform relevant tasks. This paper, first, reports on how our robot processes natural language to generate
    a multimodal, verbal response integrating emotional expressions based on an emotion simulation backend. Then, it describes
    how visitors were invited to.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- case
- study
- acceptance
- humanoid
- robotic
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.24113 A Case Study on the Acceptance of a Humanoid Robotic Head Employed in Three Publ
  url: https://arxiv.org/abs/2607.24113
  date: '2026-07-27'
  accessed_at: '2026-08-05'
---

## 概述

本研究首次对同一台类人机器人头（Kim）在三个真实公共空间（旅游信息中心、建筑管理局、市图书馆）的接受度进行对比，使用基于 TAM2 的问卷测量。结果显示地点间无统计学显著差异，所有 TAM2 子量表得分中位数均高于中性值，但样本量小且存在未受控变量。

## 它改变了什么

此前类人机器人接受度研究多局限于单一环境或实验室，缺乏对同一平台跨场所表现的直接比较。作者试图回答一个实际部署问题：公共信息类场所是否比办公环境更适合交互式机器人头。这项工作的真正价值在于将评估从“机器人能否工作”推进到“同一机器人在不同社会情境中是否被同样接纳”，并暴露了真实部署中统计功效与情境控制的根本矛盾——当样本量受限于现场流量时，即使存在效应也难以检测。

## 方法拆解

### 硬件与感知
- 机器人头 Kim 由日本制造商生产，14 个气动执行器通过 RS-485 以 25 赫兹频率接收 0–255 整数值控制面部运动。
- 眼睛无摄像头，后方网络摄像头配合 posenet 实时检测并注视最近的人；外部麦克风录音，扬声器输出。
- 软件运行于 Nvidia Jetson Orin，压缩空气与电力驱动执行器。

### 对话流水线
1. 麦克风触发“聆听”动画，关闭后切换“思考”动画。
2. OpenAI Whisper（whisper-large-v3-turbo）完成多语言语音转文字。
3. 文本发送至 OpenAI ChatGPT 4.1（gpt-4.1），结合检索增强生成（RAG）与位置特定系统提示生成回答。
4. XTTS 合成语音（17 种语言），使用克隆的与设计一致的语音。
5. FaceXHubert 编码唇形同步动画。
6. 随机眨眼，长时间无交互时打哈欠。

### 情感模拟
- WASABI 作为并发进程运行，OpenAI 助手计算用户最后一句话的效价（-100 到 +100）并发送给 WASABI。
- WASABI 返回七种情感可能性（happy、sad、angry、fearful、disgusted、surprised、neutral），无输入时回归 neutral。
- 情感通过验证过的静态面部表情表达，思考和说话动画优先级更高。

### 主动聆听决策
- 作者明确放弃主动聆听，因公共空间噪声大、误激活概率高。

### 问卷与统计
- 基于 TAM2 德语翻译版，7 点 Likert 量表（1 = 强烈不同意，7 = 强烈同意）。
- ITU 用 2 个条目，PU 用 4 个条目，PEOU 用 4 个条目，情感相关 3 个条目。
- 最终问题“How useful do you think would it be to use this robot here today?”使用 0–10 独立量表，用于与 Andrea 博物馆研究对比。
- Shapiro-Wilk 检验评估正态性，因部分数据不满足假设，使用非参数 Kruskal-Wallis 检验比较地点。

## 关键创新

1. **同一平台跨场所对比**：首次对同一台类人机器人在三个真实公共空间进行系统比较，排除了硬件差异对接受度的影响，使场所因素成为唯一自变量。
2. **TAM2 在真实世界多场所的验证应用**：将原本用于信息系统接受的 TAM2 框架迁移至类人机器人现场评估，并采用非参数检验处理真实数据的非正态性，为后续现场研究提供了统计方法参考。
3. **多语言与情感模拟的集成部署**：在单一嵌入式平台（Jetson Orin）上同时运行 STT、LLM、TTS、唇形同步、人脸追踪与情感模拟，展示了复杂交互流水线的工程可行性。

## 实验与结果

### 部署与样本
| 地点 | 时间 | 完成问卷数 |
|------|------|------------|
| 旅游信息中心 | 2025 年 5 月 26 日至 30 日，10:00–18:00 | N₁ = 19 |
| 建筑管理局 | 2025 年 6 月 3 日至 6 日，时段不等 | N₂ = 7 |
| 市图书馆 | 2025 年 6 月 10 日至 14 日，9:00–18:00 | N₃ = 23 |

### 统计结果
- Shapiro-Wilk 检验显示多个组显著偏离正态分布（p < 0.05），包括旅游信息中心的“ITU”“PEOU”及最终问题，市图书馆同样如此。
- Kruskal-Wallis 检验所有 p 值均超过显著性阈值（α = 0.05），表明地点间无统计学显著差异。

### 关键发现
| 指标 | 数值 |
|------|------|
| 总受访者 | 49 |
| 提前知晓机器人 | 18/49 |
| 专门前来体验 | 9/18 |
| 所有 TAM2 子量表得分中位数 | 均大于 4（7 点量表） |
| 平均交互时间 | 7 分钟 |
| 交互时间中位数 | 5 分钟 |
| 提到响应时间过长 | 10/49 |
| 评论令人不安 | 5/49 |
| 评论有趣/友好/创新 | 7/49 |
| 使用语言种类 | 17 种（德语 40 次最多） |

情感感知方面，机器人头被认为相当有情感（前两个问题中位数大于 4），但被认为没有情绪波动（最后一个问题中位数小于 4）。

## 边界与局限

- 参与者数量较少，尤其建筑管理局（N₂ = 7），统计功效不足，可能无法检测真实的地点间差异。
- 公共环境交互动态不受控制，多人同时观看和交互，访客可能与他人讨论问卷答案。
- 未进行长期部署，无法评估持续接受度。
- 地点选择受实际可用性和意愿影响，而非理论驱动。
- 机器人服装受主办地点建议影响，未严格控制外观，可能对感知产生未受控影响。
- 与 Andrea 博物馆研究结果相似，多语言能力虽被口头赞赏但未反映在感知有用性上，需控制外观、地点等因素才能明确结论。
- 未在更受控环境中验证，未比较不同拟人化程度机器人。

## 工程启示

- 复现时优先核对样本量：建筑管理局仅 7 份问卷，任何跨地点结论都需谨慎，建议延长部署时间或增加地点数量以提升统计功效。
- 最容易踩坑的是外观控制——机器人服装随地点变化（如旅游信息中心戴 Stuttgart 品牌帽子），这会混淆场所与外观对接受度的影响，设计实验时应固定外观或将其作为独立变量。
- 响应时间是被提及最多的负面问题（10/49），部署前应实测端到端延迟（STT + LLM + TTS + 动画），考虑缓存常见回答或降低模型复杂度。
- 多语言能力虽被赞赏但未提升感知有用性，提示下游团队不要将功能丰富度等同于用户价值，需通过任务导向设计让能力可见。
- 统计上注意非正态性：多个子量表偏离正态，必须使用非参数检验（如 Kruskal-Wallis），不要默认 ANOVA。
- 主动聆听在噪声环境被放弃是合理决策，但需在安静场所重新评估，否则可能丢失关键交互线索。

## Overview
Previous research has shown that a human-like robot's acceptance heavily depends on the setting in which it operates and its ability to perform relevant tasks. This paper, first, reports on how our robot processes natural language to generate a multimodal, verbal response integrating emotional expressions based on an emotion simulation backend. Then, it describes how visitors were invited to speak with our robot in their own language at three different, public locations, where the robot was running continuously for several days. The TAM2 questionnaire results reveal that on average users were motivated to use the robot and found it rather useful and easy to use regardless of the specific location. However, public spaces like the tourist information and the city library seem to be a better fit for our interactive, robotic head than an office environment such as the building authority, where the willingness to interact was lower. Overall, the robot's multi-lingual responses were very much appreciated, but every fifth user found the response time too slow impeding the dialog flow, which remains to be improved in future work.

## 参考
- https://arxiv.org/abs/2607.24113

## 개요

본 연구는 동일한 휴머노이드 로봇 헤드(Kim)에 대한 수용도를 세 개의 실제 공공 공간(관광 안내소, 건축 관리청, 시립 도서관)에서 처음으로 비교했으며, TAM2 기반 설문지를 사용하여 측정했습니다. 결과는 장소 간 통계적으로 유의미한 차이가 없었고, 모든 TAM2 하위 척도 점수의 중앙값이 중립값보다 높았지만, 표본 크기가 작고 통제되지 않은 변수가 존재했습니다.

## 그것이 바꾼 것

이전의 휴머노이드 로봇 수용도 연구는 주로 단일 환경이나 실험실에 국한되어 있어, 동일한 플랫폼의 장소 간 성능을 직접 비교한 사례가 없었습니다. 저자들은 실제 배포 문제, 즉 공공 정보 제공 장소가 사무 환경보다 대화형 로봇 헤드에 더 적합한지에 대한 질문에 답하려 했습니다. 이 작업의 진정한 가치는 평가를 "로봇이 작동할 수 있는가"에서 "동일한 로봇이 다양한 사회적 맥락에서 동일하게 수용되는가"로 발전시키고, 실제 배포에서 통계적 검정력과 상황 통제의 근본적 모순을 드러낸 데 있습니다. 현장 유동인구에 의해 표본 크기가 제한될 때, 효과가 존재하더라도 이를 감지하기 어렵습니다.

## 방법 분석

### 하드웨어 및 인식
- 로봇 헤드 Kim은 일본 제조업체에서 생산되었으며, 14개의 공압 액추에이터가 RS-485를 통해 25Hz 주파수로 0–255 정수 값을 수신하여 얼굴 움직임을 제어합니다.
- 눈에는 카메라가 없으며, 후면 웹캠이 posenet과 함께 실시간으로 가장 가까운 사람을 감지하고 응시합니다. 외부 마이크로 녹음하고 스피커로 출력합니다.
- 소프트웨어는 Nvidia Jetson Orin에서 실행되며, 압축 공기와 전력으로 액추에이터를 구동합니다.

### 대화 파이프라인
1. 마이크가 "듣기" 애니메이션을 트리거하고, 종료 후 "생각" 애니메이션으로 전환합니다.
2. OpenAI Whisper(whisper-large-v3-turbo)가 다국어 음성-텍스트 변환을 수행합니다.
3. 텍스트가 OpenAI ChatGPT 4.1(gpt-4.1)로 전송되어 검색 증강 생성(RAG) 및 위치별 시스템 프롬프트와 결합하여 응답을 생성합니다.
4. XTTS가 음성을 합성하며(17개 언어), 디자인과 일치하는 복제된 음성을 사용합니다.
5. FaceXHubert가 립싱크 애니메이션을 인코딩합니다.
6. 무작위 눈 깜빡임, 장시간 상호작용이 없으면 하품을 합니다.

### 감정 시뮬레이션
- WASABI가 동시 프로세스로 실행되며, OpenAI 어시스턴트가 사용자의 마지막 문장의 정서가(-100 ~ +100)를 계산하여 WASABI로 전송합니다.
- WASABI는 7가지 감정 가능성(happy, sad, angry, fearful, disgusted, surprised, neutral)을 반환하며, 입력이 없으면 neutral로 회귀합니다.
- 감정은 검증된 정적 표정으로 표현되며, 생각 및 말하기 애니메이션이 더 높은 우선순위를 가집니다.

### 능동적 듣기 결정
- 저자들은 공공 공간의 소음과 오작동 확률이 높아 능동적 듣기를 명시적으로 포기했습니다.

### 설문지 및 통계
- TAM2 독일어 번역판 기반, 7점 Likert 척도(1 = 전혀 동의하지 않음, 7 = 매우 동의함).
- ITU는 2개 항목, PU는 4개 항목, PEOU는 4개 항목, 감정 관련 3개 항목.
- 마지막 질문 "How useful do you think would it be to use this robot here today?"는 0–10 독립 척도를 사용하여 Andrea 박물관 연구와 비교했습니다.
- Shapiro-Wilk 검정으로 정규성을 평가했으며, 일부 데이터가 가정을 충족하지 않아 비모수 Kruskal-Wallis 검정으로 장소를 비교했습니다.

## 핵심 혁신

1. **동일 플랫폼의 장소 간 비교**: 동일한 휴머노이드 로봇을 세 개의 실제 공공 공간에서 체계적으로 비교한 최초의 사례로, 하드웨어 차이가 수용도에 미치는 영향을 배제하여 장소 요인을 유일한 독립 변수로 만들었습니다.
2. **실제 세계 다중 장소에서의 TAM2 검증 적용**: 원래 정보 시스템 수용을 위해 설계된 TAM2 프레임워크를 휴머노이드 로봇 현장 평가로 이전하고, 실제 데이터의 비정규성을 처리하기 위해 비모수 검정을 채택하여 후속 현장 연구에 통계적 방법 참고 자료를 제공했습니다.
3. **다국어 및 감정 시뮬레이션의 통합 배포**: 단일 임베디드 플랫폼(Jetson Orin)에서 STT, LLM, TTS, 립싱크, 얼굴 추적 및 감정 시뮬레이션을 동시에 실행하여 복잡한 대화 파이프라인의 엔지니어링 가능성을 보여주었습니다.

## 실험 및 결과

### 배포 및 표본
| 장소 | 시간 | 완료 설문지 수 |
|------|------|------------|
| 관광 안내소 | 2025년 5월 26일~30일, 10:00–18:00 | N₁ = 19 |
| 건축 관리청 | 2025년 6월 3일~6일, 시간대 상이 | N₂ = 7 |
| 시립 도서관 | 2025년 6월 10일~14일, 9:00–18:00 | N₃ = 23 |

### 통계 결과
- Shapiro-Wilk 검정에서 여러 그룹이 정규 분포에서 유의미하게 벗어남(p < 0.05). 관광 안내소의 "ITU", "PEOU" 및 마지막 질문, 시립 도서관도 동일.
- Kruskal-Wallis 검정의 모든 p 값이 유의성 임계값(α = 0.05)을 초과하여 장소 간 통계적으로 유의미한 차이가 없음을 나타냄.

### 주요 발견
| 지표 | 값 |
|------|------|
| 총 응답자 | 49 |
| 로봇을 사전에 알고 있었던 사람 | 18/49 |
| 로봇을 위해 특별히 방문한 사람 | 9/18 |
| 모든 TAM2 하위 척도 점수의 중앙값 | 모두 4보다 큼(7점 척도) |
| 평균 상호작용 시간 | 7분 |
| 상호작용 시간 중앙값 | 5분 |
| 응답 시간이 너무 길다고 언급 | 10/49 |
| 불안하다고 언급 | 5/49 |
| 재미/친근/혁신적이라고 언급 | 7/49 |
| 사용 언어 수 | 17개(독일어 40회로 최다) |

감정 인식 측면에서 로봇 헤드는 상당히 감정적인 것으로 인식되었지만(처음 두 질문의 중앙값 > 4), 감정 변화가 없다고 인식되었습니다(마지막 질문의 중앙값 < 4).

## 경계 및 한계

- 참가자 수가 적고, 특히 건축 관리청(N₂ = 7)의 경우 통계적 검정력이 부족하여 실제 장소 간 차이를 감지하지 못했을 수 있습니다.
- 공공 환경의 상호작용 역학은 통제되지 않으며, 여러 사람이 동시에 관람하고 상호작용하며, 방문객이 다른 사람과 설문지 답변을 논의할 수 있습니다.
- 장기 배포가 수행되지 않아 지속적 수용도를 평가할 수 없습니다.
- 장소 선택은 이론적 동기보다는 실제 가용성과 의지에 영향을 받았습니다.
- 로봇 의상은 주최 장소의 제안에 영향을 받아 외관이 엄격히 통제되지 않았으며, 인식에 통제되지 않은 영향을 미칠 수 있습니다.
- Andrea 박물관 연구 결과와 유사하게, 다국어 능력은 구두로 칭찬받았지만 지각된 유용성에는 반영되지 않았으며, 외관, 장소 등의 요인을 통제해야 명확한 결론을 내릴 수 있습니다.
- 더 통제된 환경에서 검증되지 않았고, 다양한 의인화 수준의 로봇을 비교하지 않았습니다.

## 엔지니어링 시사점

- 재현 시 표본 크기를 우선 확인하세요. 건축 관리청은 설문지가 7개뿐이므로 장소 간 결론은 신중해야 하며, 배포 시간을 연장하거나 장소 수를 늘려 통계적 검정력을 높이는 것이 좋습니다.
- 가장 쉽게 함정에 빠지는 부분은 외관 통제입니다. 로봇 의상이 장소에 따라 달라지며(예: 관광 안내소에서 Stuttgart 브랜드 모자 착용), 이는 장소와 외관이 수용도에 미치는 영향을 혼동시킵니다. 실험 설계 시 외관을 고정하거나 독립 변수로 취급해야 합니다.
- 응답 시간은 가장 많이 언급된 부정적 문제(10/49)이므로, 배포 전에 종단 간 지연(STT + LLM + TTS + 애니메이션)을 실제로 측정하고, 일반적인 응답을 캐싱하거나 모델 복잡도를 낮추는 것을 고려하세요.
- 다국어 능력은 칭찬받았지만 지각된 유용성을 높이지 않았습니다. 이는 기능의 풍부함을 사용자 가치와 동일시하지 말고, 작업 지향 설계를 통해 능력을 가시화해야 함을 시사합니다.
- 통계적으로 비정규성에 주의하세요. 여러 하위 척도가 정규 분포에서 벗어나므로, ANOVA를 기본으로 사용하지 말고 반드시 비모수 검정(예: Kruskal-Wallis)을 사용해야 합니다.
- 소음 환경에서 능동적 듣기를 포기한 것은 합리적인 결정이지만, 조용한 장소에서 재평가해야 합니다. 그렇지 않으면 핵심 상호작용 단서를 잃을 수 있습니다.
