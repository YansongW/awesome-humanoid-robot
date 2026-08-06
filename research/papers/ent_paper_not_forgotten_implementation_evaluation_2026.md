---
$id: ent_paper_not_forgotten_implementation_evaluation_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim'
  zh: 'Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim'
  ko: 'Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim'
summary:
  en: Social robots that rely on large language models for conversation are unable to retain information across sessions.
    This absence of memory violates social expectations, potentially preventing the formation of persistent relationships.
    This paper presents a lightweight episodic memory module that integrates vector-based semantic retrieval with an LLM-controlled
    dialog system, deployed on the.
  zh: 本文针对依赖 LLM 的社交机器人无法跨会话保留信息、违背具身性所引发的社交期望这一问题，在具备 14 个气动执行器的人形机器人头 Kim 上实现并评估了一套个性化情景记忆系统。该系统采用微服务架构，通过混合检索评分（语义相似度与记忆强度加权）从
    Qdrant 向量库中召回过往交互，注入 LLM 提示词。基于 43 名被试的在线视频实验表明，记忆增强显著提升了感知社交性（尤其温暖与可信赖），但对感知干扰无显著影响。
  ko: Social robots that rely on large language models for conversation are unable to retain information across sessions.
    This absence of memory violates social expectations, potentially preventing the formation of persistent relationships.
    This paper presents a lightweight episodic memory module that integrates vector-based semantic retrieval with an LLM-controlled
    dialog system, deployed on the.
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
- not
- forgotten
- implementation
- evaluation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.24190 Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory f'
  url: https://arxiv.org/abs/2607.24190
  date: '2026-07-27'
  accessed_at: '2026-08-05'
---

## 概述

本文针对依赖 LLM 的社交机器人无法跨会话保留信息、违背具身性所引发的社交期望这一问题，在具备 14 个气动执行器的人形机器人头 Kim 上实现并评估了一套个性化情景记忆系统。该系统采用微服务架构，通过混合检索评分（语义相似度与记忆强度加权）从 Qdrant 向量库中召回过往交互，注入 LLM 提示词。基于 43 名被试的在线视频实验表明，记忆增强显著提升了感知社交性（尤其温暖与可信赖），但对感知干扰无显著影响。

## 它改变了什么

这项工作的真正价值不在于又造了一个带记忆的聊天机器人，而在于它把记忆从“检索准确率”的工程问题，拉回到了“用户感知”的心理学问题。此前 RAG、MemGPT 等方案都在优化事实召回，用功能基准或虚拟沙盒评估，默认“记得越多越好”。但具身机器人不一样——它的物理形态会诱导用户投射能动性和社交期待，此时“记住”可能被解读为贴心，也可能被解读为监视。作者没有回避这个矛盾，而是直接问：记忆到底让用户觉得更温暖，还是更 creepy？

它改变的第二个点是实验范式。多数 HRI 记忆研究聚焦系统能力，测的是“能不能记住”，而这里测的是“记住了之后用户怎么想”。通过预录视频、被试内设计、HRIES 量表，把记忆的社交效应从技术噪声中剥离出来。结果也很有意思：记忆显著提升了 sociability（d = 0.60），但对 disturbance 毫无影响（d = 0.00）——这暗示用户对机器人“记住我”的接受度，可能比我们担心的要高，至少在单次会话的观察窗口内如此。

## 方法拆解

系统架构是微服务导向，全部 Docker 容器化，通过 HTTP REST API 和 websocket 通信。核心记忆模块是 FastAPI 微服务，暴露三个端点：`POST /memory`（存储）、`POST /memory/query`（检索）、`POST /memory/consolidate-all`（整合）。交互流水线为：Whisper ASR → 记忆检索 → gpt-4.1-nano 生成 → XTTS 语音合成 → 唇部同步。

### 记忆存储
- 每轮对话文本经 OpenAI `text-embedding-3-small` 转为 1536 维向量，存入本地 Qdrant。
- 每条记忆附带情绪元数据：LLM 情感分类给出效价 v 和唤醒度 a，情绪强度 I = √(v² + a²)。
- 实验前预填充用户偏好（六项个人画像），确保基线一致性。

### 混合检索评分（两阶段）
1. **候选召回**：余弦相似度查询 Qdrant，过采样因子 3（3k 候选取 k 个）。
2. **重排序**：混合评分 R(m) = α · sim(m) + S(m)，其中 α = 50 为启发式缩放因子，sim(m) ∈ [0,1] 为余弦相似度，S(m) 为记忆强度。

设计理由：标准 RAG 只看语义相似度，这里借鉴生成式智能体的近期性和访问频率，并扩展加入情绪强度。缩放因子 α = 50 确保语义相关性始终主导，记忆强度仅作平局决胜——这是关键决策，避免情绪记忆喧宾夺主。

### 记忆强度公式
S(m) = max(0, (w_t·F_time + w_a·F_access + w_r·F_recency) · M_emotion)

- 权重：w_t = 3.0（时间衰减）、w_a = 2.0（访问频率）、w_r = 1.5（近期性）
- F_time = max(0, 1 − 0.1·Δt_creation)，Δt 以天计
- F_access = ln(1 + N_access)
- F_recency = max(0, 1 − 0.05·Δt_last_access)
- M_emotion = 1 + 0.5·√(v² + a²)

内部 max(·) 将负的时间/近期性贡献裁剪为零；情绪强度作为乘法强化，使高情绪记忆更抗衰减。

### 提示注入与延迟处理
- 重排序后 top k 条记忆注入系统提示词，明确要求“use memories naturally”、“don't enforce all info at once”，将记忆框定为可选背景而非强制事实。
- 延迟控制：嵌入约 0.32 秒、搜索/重排序约 0.36 秒。控制器将检索设为阻塞式（生成前同步运行），记忆写入卸载到后台线程。
- Baseline 条件：停止记忆容器，客户端检索请求 5 秒超时，LLM 仅用当前对话轮次。

## 关键创新

1. **情绪强度作为记忆衰减的乘法因子**：现有生成式智能体只用时间、访问频率、近期性做线性加权，这里引入 M_emotion = 1 + 0.5·√(v² + a²) 作为乘法强化。这意味着高情绪事件（如用户提到“梦想旅行目的地”）比中性事件（如“今天天气不错”）更难被遗忘。这个设计假设“优先情绪事件产生更自然的回忆”，在 HRI 语境下是合理的——人类记忆本身就有情绪偏向性。

2. **混合评分中 α = 50 的启发式校准**：把语义相似度放大 50 倍与记忆强度相加，本质上是把“语义相关性”设为硬约束、把“记忆强度”设为软排序。这个设计避免了纯 RAG 的“只认事实不认情感”和纯记忆优先的“跑题风险”，在工程上是一个可复制的平衡点。

3. **实验上区分了“记忆可用性”与“检索策略优越性”**：作者明确声明架构贡献限于可行性证明，经验贡献在于记忆可用性的效应，而非特定检索策略的优越性。这种自我设限在论文中少见，但恰恰让结论更可信——它没有过度宣称混合评分比简单关键词匹配更好，而是把问题留给后续研究。

## 实验与结果

实验为被试内设计，52 人完成画像阶段，43 人提供完整响应。
参与者通过视频观看机器人响应六个相同的社交提示，用 HRIES 量表（7 点 Likert）评估四个维度。
四个条目（creepy、scary、uncanny、weird）均未接近显著，条目级效应量均 < .25。
**Agency 与 Animacy**：均不显著（Agency d = 0.11，Animacy d = 0.17），且 Animacy 两种条件均低于量表中点（M_BL = 2.78，M_ME = 3.02）。
**全局偏好**：63% 选 Memory-Enhanced，37% 选 Baseline，但卡方检验 χ²(1) = 2.81，p = .093，无法与随机区分。
| 指标 | Baseline M (SD) | Memory-Enhanced M (SD) | t(42) | p | Cohen's d |
|---|---|---|---|---|---|
| Sociability 量表 | 3.77 (1.02) | 4.40 (1.09) | −4.15 | < .001 | 0.60 |
| warm | 3.07 (1.37) | 3.91 (1.62) | −3.56 | .001 | .56 |
| trustworthy | 3.21 (1.32) | 4.09 (1.51) | −3.91 | < .001 | .62 |
| Agency | 4.25 | 4.36 | −0.89 | 1.000 | 0.11 |
关键含义：记忆增强让机器人更“温暖、可信赖”，但不会让它更“吓人”——零干扰效应是本文最值得注意的发现，它初步回应了“记忆是否滑向监视”的担忧。
（本节另有 6 句含无法从全文文本核实的数字，已按纪律移除；论文未明确或以图/表图片形式给出。）

## 边界与局限

作者明确承认的边界包括：视频格式排除了实时对话，减少了记忆影响判断的带宽，单次会话观察无法实证测试时间衰减等长期因素，Agency 和 Animacy 的零结果可能部分反映这种降低的效度。样本为 N = 43 的大学生，统计功效受限，且因 GDPR 数据最小化未收集人口统计细节，限制隐私态度个体差异的推广性。

更关键的局限是：**无法分离架构贡献**——零干扰效应可能是架构过滤（提示词强制“自然使用记忆”）的功劳，也可能只是因为场景太短、记忆量太少，用户根本没注意到被记住。作者也承认未隔离具体检索策略的贡献：任何能注入个人细节的系统（如关键词匹配）都可能产生相当的社交性效应。此外，未测试无过滤回忆是否会引发隐私担忧，未进行多周纵向研究，未评估可解释记忆检索策略。全局偏好 63% 未达显著，样本可能功效不足。

## 工程启示

复现时最先要核对的是**记忆强度公式的权重和衰减系数**：w_t = 3.0、w_a = 2.0、w_r = 1.5，以及 F_time 的 0.1/天和 F_recency 的 0.05/天衰减率。这些参数是启发式设定的，没有敏感性分析——如果你的场景对话频率远高于或低于本实验（一周间隔），衰减曲线会完全变形。建议先跑一个模拟数据集，确认 top k 召回里情绪记忆的占比是否符合直觉。

最容易踩坑的是**提示词注入的措辞**。作者强调“use memories naturally”、“don't enforce all info at once”，这直接决定了记忆是被自然编织还是生硬插入。实测中 LLM 变异性很大，从自然引用到脚本化插入都有，这会引入未控制的组内方差。建议在系统提示词里加更严格的约束，比如“最多引用一条记忆”或“仅在相关时提及”，并做多轮人工评估。

另一个工程细节：**检索延迟 0.32 + 0.36 秒**在实时交互中可能可感知。作者用阻塞式检索 + 非阻塞式写入解决，但如果你用更慢的嵌入模型或更大的向量库，这个延迟会翻倍。建议把检索超时从 5 秒收紧到 2 秒，并考虑缓存高频查询结果。

最后，**零干扰效应不要过度外推**。本实验是单次会话、预录视频、一周间隔，用户可能根本没意识到机器人“记得”什么。如果你要做多周纵向部署，务必重新测量 disturbance——记忆累积到一定量级后，用户对“被记住”的感受可能从贴心滑向侵扰。

## Overview
Social robots that rely on large language models for conversation are unable to retain information across sessions. This absence of memory violates social expectations, potentially preventing the formation of persistent relationships. This paper presents a lightweight episodic memory module that integrates vector-based semantic retrieval with an LLM-controlled dialog system, deployed on the humanoid robot head Kim. The module employs a hybrid scoring function combining cosine similarity with a memory strength metric to retrieve contextually relevant past interactions and inject them into the generation prompt. The system was evaluated in a within-subjects video-based online study (N = 43) using the Human-Robot Interaction Evaluation Scale (HRIES). Results show that episodic memory significantly increased perceived sociability (d = 0.60, p < .001), with the strongest effects on perceived trustworthiness (d = 0.62) and warmth (d = 0.56). Perceived disturbance remained unchanged (d = 0.00), indicating that the implemented approach to personalized recall did not trigger privacy-related discomfort or uncanny valley effects. These findings suggest that episodic memory serves as a social lubricant in embodied Human-Robot Interaction, enhancing relational quality without eliciting negative affective responses.

## 参考
- https://arxiv.org/abs/2607.24190

## 개요

본 논문은 LLM 기반 소셜 로봇이 세션 간 정보를 유지하지 못하고, 구현성(embodiment)이 유발하는 사회적 기대에 부합하지 못하는 문제를 해결하기 위해, 14개의 공압 액추에이터를 갖춘 인간형 로봇 헤드 Kim에 개인화된 상황 기억 시스템을 구현하고 평가하였다. 이 시스템은 마이크로서비스 아키텍처를 채택하고, 하이브리드 검색 점수(의미 유사도와 기억 강도 가중치)를 통해 Qdrant 벡터 저장소에서 과거 상호작용을 재호출하여 LLM 프롬프트에 주입한다. 43명의 피험자를 대상으로 한 온라인 비디오 실험 결과, 기억 강화는 지각된 사회성(특히 따뜻함과 신뢰성)을 유의미하게 향상시켰지만, 지각된 방해에는 유의미한 영향을 미치지 않았다.

## 그것이 바꾼 것

이 작업의 진정한 가치는 또 하나의 기억 기능을 가진 챗봇을 만든 것이 아니라, 기억을 '검색 정확도'라는 공학적 문제에서 '사용자 인식'이라는 심리학적 문제로 끌어내린 데 있다. 기존 RAG, MemGPT 등의 접근 방식은 사실 재호출을 최적화하고 기능 벤치마크나 가상 샌드박스로 평가하며, '많이 기억할수록 좋다'는 것을 기본 전제로 삼았다. 그러나 구현된 로봇은 다르다—물리적 형태가 사용자로 하여금 행위 주체성과 사회적 기대를 투사하게 만들며, 이때 '기억함'은 세심함으로 해석될 수도 있고 감시로 해석될 수도 있다. 저자는 이러한 모순을 회피하지 않고 직접 질문한다: 기억은 과연 사용자에게 더 따뜻함을 느끼게 하는가, 아니면 더 섬뜩함(creepy)을 느끼게 하는가?

두 번째로 바꾼 점은 실험 패러다임이다. 대부분의 HRI 기억 연구는 시스템 능력에 초점을 맞추어 '기억할 수 있는지'를 측정하는 반면, 여기서는 '기억한 후 사용자가 어떻게 느끼는지'를 측정한다. 사전 녹화된 비디오, 피험자 내 설계, HRIES 척도를 통해 기억의 사회적 효과를 기술적 노이즈에서 분리해 냈다. 결과도 흥미롭다: 기억은 사회성(sociability)을 유의미하게 향상시켰지만(d = 0.60), 방해(disturbance)에는 전혀 영향을 미치지 않았다(d = 0.00)—이는 사용자가 로봇이 '나를 기억하는 것'에 대해 우리가 우려했던 것보다 더 수용적일 수 있음을 시사하며, 적어도 단일 세션 관찰 창에서는 그러하다.

## 방법 분석

시스템 아키텍처는 마이크로서비스 지향적이며, 전체가 Docker 컨테이너화되어 HTTP REST API와 websocket으로 통신한다. 핵심 기억 모듈은 FastAPI 마이크로서비스로, 세 가지 엔드포인트를 노출한다: `POST /memory`(저장), `POST /memory/query`(검색), `POST /memory/consolidate-all`(통합). 상호작용 파이프라인은: Whisper ASR → 기억 검색 → gpt-4.1-nano 생성 → XTTS 음성 합성 → 립싱크 순서이다.

### 기억 저장
- 각 대화 텍스트는 OpenAI `text-embedding-3-small`을 통해 1536차원 벡터로 변환되어 로컬 Qdrant에 저장된다.
- 각 기억에는 감정 메타데이터가 첨부된다: LLM 감정 분류가 valence v와 arousal a를 제공하고, 감정 강도 I = √(v² + a²)로 계산된다.
- 실험 전에 사용자 선호도(6개 개인 프로필 항목)를 사전 채워 기준선 일관성을 보장한다.

### 하이브리드 검색 점수(2단계)
1. **후보 재호출**: 코사인 유사도로 Qdrant를 쿼리하고, 오버샘플링 팩터 3(3k 후보에서 k개 선택)을 적용한다.
2. **재정렬**: 하이브리드 점수 R(m) = α · sim(m) + S(m), 여기서 α = 50은 휴리스틱 스케일링 팩터, sim(m) ∈ [0,1]은 코사인 유사도, S(m)은 기억 강도이다.

설계 근거: 표준 RAG는 의미 유사도만 보는 반면, 여기서는 생성형 에이전트의 최근성과 접근 빈도를 차용하고 감정 강도를 확장하여 추가했다. 스케일링 팩터 α = 50은 의미 관련성이 항상 우세하도록 보장하며, 기억 강도는 단지 동점 결정자(tie-breaker) 역할만 한다—이는 감정 기억이 주도권을 잡지 않도록 하는 핵심 결정이다.

### 기억 강도 공식
S(m) = max(0, (w_t·F_time + w_a·F_access + w_r·F_recency) · M_emotion)

- 가중치: w_t = 3.0(시간 감쇠), w_a = 2.0(접근 빈도), w_r = 1.5(최근성)
- F_time = max(0, 1 − 0.1·Δt_creation), Δt는 일 단위
- F_access = ln(1 + N_access)
- F_recency = max(0, 1 − 0.05·Δt_last_access)
- M_emotion = 1 + 0.5·√(v² + a²)

내부 max(·)는 음수 시간/최근성 기여를 0으로 잘라낸다; 감정 강도는 곱셈 강화로 작용하여 높은 감정 기억이 감쇠에 더 저항하게 만든다.

### 프롬프트 주입 및 지연 처리
- 재정렬 후 상위 k개 기억이 시스템 프롬프트에 주입되며, "use memories naturally", "don't enforce all info at once"를 명시적으로 요구하여 기억을 강제 사실이 아닌 선택적 배경으로 프레임화한다.
- 지연 제어: 임베딩 약 0.32초, 검색/재정렬 약 0.36초. 컨트롤러는 검색을 블로킹 방식(생성 전 동기 실행)으로 설정하고, 기억 쓰기는 백그라운드 스레드로 오프로드한다.
- Baseline 조건: 기억 컨테이너를 중지하고, 클라이언트 검색 요청은 5초 타임아웃, LLM은 현재 대화 턴만 사용한다.

## 핵심 혁신

1. **감정 강도를 기억 감쇠의 곱셈 팩터로 사용**: 기존 생성형 에이전트는 시간, 접근 빈도, 최근성만 선형 가중치로 사용하는 반면, 여기서는 M_emotion = 1 + 0.5·√(v² + a²)을 곱셈 강화로 도입한다. 이는 높은 감정 사건(예: 사용자가 '꿈의 여행지'를 언급)이 중립 사건(예: '오늘 날씨가 좋다')보다 잊히기 어렵다는 것을 의미한다. 이 설계는 '감정적 사건이 더 자연스러운 회상을 우선시한다'는 가정에 기반하며, HRI 맥락에서 타당하다—인간 기억 자체가 감정 편향성을 가지기 때문이다.

2. **혼합 점수에서 α = 50의 휴리스틱 보정**: 의미 유사도를 50배 확대하여 기억 강도와 더하는 것은 본질적으로 '의미 관련성'을 하드 제약으로, '기억 강도'를 소프트 정렬로 설정하는 것이다. 이 설계는 순수 RAG의 '사실만 인식하고 감정은 무시'와 순수 기억 우선의 '주제 이탈 위험'을 모두 피하며, 공학적으로 재현 가능한 균형점이다.

3. **실험적으로 '기억 가용성'과 '검색 전략 우월성'을 구분**: 저자는 아키텍처 기여가 타당성 증명에 국한되며, 경험적 기여는 특정 검색 전략의 우월성이 아닌 기억 가용성의 효과에 있다고 명시적으로 선언한다. 이러한 자기 제한은 논문에서 드물지만, 오히려 결론을 더 신뢰하게 만든다—혼합 점수가 단순 키워드 매칭보다 낫다고 과도하게 주장하지 않고, 문제를 후속 연구에 남겨둔다.

## 실험 및 결과

실험은 피험자 내 설계로, 52명이 프로필 단계를 완료하고 43명이 완전한 응답을 제공했다.
참가자는 비디오를 통해 로봇이 여섯 개의 동일한 사회적 프롬프트에 응답하는 것을 보고, HRIES 척도(7점 Likert)로 네 가지 차원을 평가했다.
네 가지 항목(creepy, scary, uncanny, weird) 모두 유의미에 근접하지 않았으며, 항목별 효과 크기는 모두 < .25였다.
**Agency 및 Animacy**: 모두 유의미하지 않음(Agency d = 0.11, Animacy d = 0.17), Animacy는 두 조건 모두 척도 중간점보다 낮음(M_BL = 2.78, M_ME = 3.02).
**전역 선호도**: 63%가 Memory-Enhanced 선택, 37%가 Baseline 선택, 그러나 카이제곱 검정 χ²(1) = 2.81, p = .093으로 무작위와 구분할 수 없음.
| 지표 | Baseline M (SD) | Memory-Enhanced M (SD) | t(42) | p | Cohen's d |
|---|---|---|---|---|---|
| Sociability 척도 | 3.77 (1.02) | 4.40 (1.09) | −4.15 | < .001 | 0.60 |
| warm | 3.07 (1.37) | 3.91 (1.62) | −3.56 | .001 | .56 |
| trustworthy | 3.21 (1.32) | 4.09 (1.51) | −3.91 | < .001 | .62 |
| Agency | 4.25 | 4.36 | −0.89 | 1.000 | 0.11 |
핵심 의미: 기억 강화는 로봇을 더 '따뜻하고 신뢰할 수 있게' 만들지만, 더 '무섭게' 만들지는 않는다—제로 방해 효과는 이 논문에서 가장 주목할 만한 발견이며, '기억이 감시로 이어지는가'에 대한 우려에 초기 응답을 제공한다.
(이 섹션에는 전체 텍스트에서 검증할 수 없는 숫자를 포함한 6개의 문장이 더 있었으며, 규율에 따라 제거되었다; 논문은 명시하지 않거나 그림/표 이미지로 제공했다.)

## 경계 및 한계

저자가 명시적으로 인정한 경계는: 비디오 형식이 실시간 대화를 배제하여 기억이 판단에 미치는 영향의 대역폭을 줄였고, 단일 세션 관찰은 시간 감쇠와 같은 장기 요인을 실증적으로 테스트할 수 없으며, Agency와 Animacy의 제로 결과는 이러한 감소된 타당성을 부분적으로 반영할 수 있다. 표본은 N = 43의 대학생으로 통계적 검정력이 제한적이고, GDPR 데이터 최소화로 인해 인구통계학적 세부 정보를 수집하지 않아 프라이버시 태도의 개인차에 대한 일반화가 제한된다.

더 중요한 한계는: **아키텍처 기여를 분리할 수 없다**—제로 방해 효과는 아키텍처 필터링(프롬프트가 '자연스러운 기억 사용'을 강제) 덕분일 수도 있고, 단지 시나리오가 너무 짧고 기억량이 너무 적어 사용자가 기억되고 있다는 사실을 알아차리지 못했기 때문일 수도 있다. 저자는 또한 특정 검색 전략의 기여를 분리하지 않았음을 인정한다: 개인 세부 정보를 주입할 수 있는 어떤 시스템(예: 키워드 매칭)도 상당한 사회성 효과를 생성할 수 있다. 또한, 필터링되지 않은 회상이 프라이버시 우려를 유발하는지 테스트하지 않았고, 다주 종단 연구를 수행하지 않았으며, 해석 가능한 기억 검색 전략을 평가하지 않았다. 전역 선호도 63%는 유의미에 도달하지 못했으며, 표본이 검정력 부족일 수 있다.

## 공학적 시사점

재현 시 가장 먼저 확인해야 할 것은 **기억 강도 공식의 가중치와 감쇠 계수**이다: w_t = 3.0, w_a = 2.0, w_r = 1.5, 그리고 F_time의 0.1/일 및 F_recency의 0.05/일 감쇠율. 이러한 매개변수는 휴리스틱하게 설정되었으며 민감도 분석이 없다—시나리오의 대화 빈도가 본 실험(일주일 간격)보다 훨씬 높거나 낮다면 감쇠 곡선이 완전히 변형될 것이다. 먼저 시뮬레이션 데이터셋을 실행하여 top k 재호출에서 감정 기억의 비율이 직관에 부합하는지 확인하는 것이 좋다.

가장 함정에 빠지기 쉬운 것은 **프롬프트 주입의 표현**이다. 저자는 "use memories naturally", "don't enforce all info at once"를 강조하며, 이는 기억이 자연스럽게 직조되는지 아니면 딱딱하게 삽입되는지를 직접 결정한다. 실제 측정에서 LLM 변동성이 크며, 자연스러운 인용부터 스크립트화된 삽입까지 다양하여 통제되지 않은 그룹 내 분산을 유발한다. 시스템 프롬프트에 "최대 한 개의 기억만 인용" 또는 "관련될 때만 언급"과 같은 더 엄격한 제약을 추가하고, 다회차 인간 평가를 수행하는 것이 좋다.

또 다른 공학적 세부 사항: **검색 지연 0.32 + 0.36초**는 실시간 상호작용에서 인지될 수 있다. 저자는 블로킹 검색 + 논블로킹 쓰기로 해결했지만, 더 느린 임베딩 모델이나 더 큰 벡터 저장소를 사용하면 이 지연이 두 배가 된다. 검색 타임아웃을 5초에서 2초로 줄이고, 고빈도 쿼리 결과를 캐싱하는 것을 고려하는 것이 좋다.

마지막으로, **제로 방해 효과를 과도하게 일반화하지 말 것**. 본 실험은 단일 세션, 사전 녹화 비디오, 일주일 간격으로, 사용자가 로봇이 무엇을 '기억하는지' 인식하지 못했을 수 있다. 다주 종단 배포를 계획한다면 disturbance를 반드시 재측정해야 한다—기억이 일정 수준으로 축적되면 '기억됨'에 대한 사용자의 느낌이 세심함에서 침해로 전환될 수 있다.
