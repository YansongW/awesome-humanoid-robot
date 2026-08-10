---
$id: ent_paper_breaking_15_barrier_real_world_data_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Breaking the 15% Barrier: A Real-World Data-Driven System for Proactive Social Robot Triggered by User Nonverbal Cues'
  zh: 'Breaking the 15% Barrier: A Real-World Data-Driven System for Proactive Social Robot Triggered by User Nonverbal Cues'
  ko: 'Breaking the 15% Barrier: A Real-World Data-Driven System for Proactive Social Robot Triggered by User Nonverbal Cues'
summary:
  en: Service robots in retail stores increasingly rely on cascaded speech pipelines (STT-LLM-TTS), yet many customer-robot
    interactions are initiated or guided by nonverbal behaviors such as approaching, waving, pointing, or showing items. This
    paper studies such cues in a real-world store deployment with a teleoperated humanoid robot and shows that a non-negligible
    portion of robot turns are.
  zh: 本文提出一套面向真实零售环境的主动社交机器人系统，由用户非语言行为（接近、挥手、指点等）触发对话。作者在真实药妆店远程操控人形机器人收集数据，构建了基于V-JEPA2的非语言行为识别器与LLM对话框架，将识别标签作为提示token注入对话历史。核心贡献在于量化了非语言触发话语占比（15.3%），并验证了轻量识别器（约8
    FPS）可满足实时性要求。
  ko: Service robots in retail stores increasingly rely on cascaded speech pipelines (STT-LLM-TTS), yet many customer-robot
    interactions are initiated or guided by nonverbal behaviors such as approaching, waving, pointing, or showing items. This
    paper studies such cues in a real-world store deployment with a teleoperated humanoid robot and shows that a non-negligible
    portion of robot turns are.
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
- breaking
- '15'
- barrier
- real
- world
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
  title: 'arXiv:2607.11633 Breaking the 15% Barrier: A Real-World Data-Driven System for Proactive Social R'
  url: https://arxiv.org/abs/2607.11633
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一套面向真实零售环境的主动社交机器人系统，由用户非语言行为（接近、挥手、指点等）触发对话。作者在真实药妆店远程操控人形机器人收集数据，构建了基于V-JEPA2的非语言行为识别器与LLM对话框架，将识别标签作为提示token注入对话历史。核心贡献在于量化了非语言触发话语占比（15.3%），并验证了轻量识别器（约8 FPS）可满足实时性要求。

## 它改变了什么

现有服务机器人对话系统几乎全部依赖级联语音管道（STT–LLM–TTS），将交互起点限定为口语。但真实零售场景中，大量客户-机器人互动由非语言行为发起或引导，仅音频输入的系统会系统性错失这些互动机会。作者通过真实部署数据证明，这类非语言触发话语占全部机器人话语的15.3%——这不是边缘情况，而是不可忽视的交互模式。

真正被改变的是“对话系统输入模态”的边界。以往多模态对话研究多聚焦于视觉内容理解（如识别物体、场景），而本文关注的是“人的行为意图”作为对话触发信号。作者没有用重型VLM做逐帧理解，而是设计了一个轻量识别器（约8 FPS）与LLM并行运行，将行为标签作为离散token注入对话历史。这种“识别-注入”架构避免了VLM实时推理的高延迟（Gemini 3.5 Flash需6.63秒），使非语言信号能真正进入对话决策循环。

## 方法拆解

### 数据收集与注释
- 在真实药妆店部署远程操控人形机器人Sota（约0.3米高，8自由度），运营32小时（6天）
- 仅注释1小时42分钟，获得2,178个机器人话语，其中334个（15.3%）为非语言触发
- 4名无利益冲突注释者将话语分为“对口语的回应”和“非语言触发话语”，后者进一步标注触发行为类别和话语意图（5类）

### 行为选择
从21种触发行为中选出9种重要行为，选择标准基于频率、客服场景特征和视频可稳定检测性：
- 高频行为：Approached（29.2%）、Waved（11.6%）、Walked away（7.9%）
- 低频但强关联：Touched belongings（0.7%），因其与任务指导强关联（66.7%触发Task-related info & directives）

### 识别模型架构
- 输入：视频片段 + 每人的边界框序列
- 特征提取：Vision Transformer（V-JEPA2）提取场景特征，MLP提取位置特征
- 融合：Hadamard积融合两类特征，注意力池化聚合，MLP分类器输出多标签logits
- 损失：加权二元交叉熵（权重为类别正例数的倒数），应对类别不平衡

### 对话框架
- 非语言识别与对话系统并行运行
- 识别标签作为提示token（如[waved]、[pointed]）附加到对话历史
- LLM（Gemini 2.5 Flash）生成响应，采用最小提示设置，避免为每个标签设置显式规则
- 仅当检测到Showed items时额外使用VLM识别物品

### 训练配置
- PyTorch实现，20个epoch，batch size 16，5折交叉验证
- 滑动窗口步长w帧，推理滑动窗口8帧

## 关键创新

1. **真实场景数据驱动的行为-意图映射**：不同于实验室合成数据，本文基于32小时真实药妆店运营数据，量化了9种非语言行为与5类话语意图的对应关系。例如Approached主要触发Social & Greeting（66.4%），而Touched belongings几乎专门触发Task-related info & directives（66.7%）。这种映射关系为后续系统设计提供了实证基础。

2. **轻量识别器+LLM的并行架构**：将非语言识别从对话生成中解耦，识别器以约8 FPS运行（排除人检测/跟踪），满足实时要求（>1 FPS）。识别标签作为离散token注入对话历史，避免了VLM逐帧推理的高延迟（Gemini 3.5 Flash需6.63秒，远超一秒响应预算）。这种设计使系统能在消费级GPU（RTX 3080）上部署。

3. **最小提示设计**：不针对每个行为标签设置显式规则，而是让LLM从对话历史中的标签token自行推断响应策略。这降低了工程复杂度，同时保持了对话的自然性——离线评估中整体意图一致性达49.1%，超过多数类基线44.0%。

## 实验与结果

### 识别性能（Table IV，micro Avg.）
| 指标 | 数值 |
|------|------|
| Precision | 0.89 |
| Recall | 0.73 |
| F1 | 0.80 |
| Accuracy | 0.97 |

### 各类别F1表现
| 行为 | F1 | 备注 |
|------|-----|------|
| Approached | 0.90 | 高频，性能最佳 |
| Showed items | 0.88 | 低频但识别稳定 |
| Peered into robot | 0.79 | 中频，性能良好 |
| Nodded | 0.65 | 低频，性能一般 |
| Pointed | 0.62 | 低频，精度低（0.57） |
| Waved | 0.59 | 中频，精度低（0.57） |
| Walked away | 0.62 | 中频，精度低（0.50） |
| Touched belongings | 0.61 | 极低频，F1尚可 |
| User–user interaction | 0.47 | 召回低（0.31） |

### 离线话语生成
- 334个非语言触发话语上，整体意图一致性49.1%
- Social & Greeting准确率69%
- Task-related info & directives准确率低，因标签稀少（Touched belongings仅0.7%）且需环境特定细节

### 推理速度
- 识别器（排除人检测/跟踪）约8 FPS，满足实时要求
- VLM参考延迟：Gemini 3.5 Flash 6.63 ± 1.19秒，Gemini 3.5 Flash Lite 2.54 ± 0.58秒，均超过一秒响应预算

## 边界与局限

- 评估主要离线，未完全捕捉真实错误（如人检测/跟踪）在管道中的传播；需要在线端到端评估和用户体验指标
- 数据来自单一商店入口的远程操控服务，跨商店类型、人群密度、布局和操作员策略的泛化有限
- 意图不平衡可能影响估计和学习——Task-related info & directives仅占10.5%，且关联行为Touched belongings仅0.7%
- 话语生成评估仅基于意图标签一致性，未惩罚缺失任务指导，未纳入用户体验测量
- 操作员有时在忽略上下文时机产生任务相关话语，可能污染训练数据

## 工程启示

- **先核对行为-意图映射的稳定性**：Approached→Social & Greeting（66.4%）和Touched belongings→Task-related info & directives（66.7%）是强关联，但Waved→Social & Greeting（65.9%）与Walked away→Social & Greeting（73.3%）的区分度不足，复现时需注意行为定义的边界
- **类别不平衡是主要陷阱**：Touched belongings仅0.7%但F1达0.61，得益于加权损失；若下游场景中该行为更罕见，需重新调整权重或考虑few-shot策略
- **识别器与对话系统的时序同步**：识别器约8 FPS，但LLM生成需数秒，需设计缓冲机制确保行为标签在对话历史中的位置正确；建议在标签token中加入时间戳
- **VLM仅用于Showed items是明智的取舍**：该行为仅占1.2%，但触发User/state comment & empathy（50.0%），按需调用VLM可控制延迟；若场景中该行为频率上升，需考虑异步预取
- **离线评估的意图一致性49.1%是下限**：多数类基线44.0%，提升仅5.1个百分点；若下游任务对意图准确性要求高，需引入在线强化学习或人工反馈微调

## Overview
Service robots in retail stores increasingly rely on cascaded speech pipelines (STT-LLM-TTS), yet many customer-robot interactions are initiated or guided by nonverbal behaviors such as approaching, waving, pointing, or showing items. This paper studies such cues in a real-world store deployment with a teleoperated humanoid robot and shows that a non-negligible portion of robot turns are triggered by nonverbal behaviors rather than spoken input, revealing a limitation of audio-only dialogue systems. In a 6-day in-the-wild deployment, 15.3\% of robot utterances were initiated by users' nonverbal behaviors rather than spoken input. Based on an analysis of observed customer behaviors, we define a set of frequent, service-relevant nonverbal cues and develop a real-time multi-person, multi-label recognizer that runs online from video. We then propose a dialogue framework that conditions LLM-based utterance generation on recognized nonverbal cue tokens, and optionally leverages a vision-language model when items are shown, enabling proactive robot responses without hand-crafted rules. We evaluate the approach offline on nonverbal-triggered turns and demonstrate an online prototype that reacts to users' nonverbal cues in real time.

## 参考
- https://arxiv.org/abs/2607.11633

## 개요

본 논문은 실제 소매 환경을 위한 능동적 소셜 로봇 시스템을 제안하며, 사용자의 비언어적 행동(접근, 손짓, 지적 등)에 의해 대화가 촉발된다. 저자는 실제 약국에서 휴머노이드 로봇을 원격 조종하여 데이터를 수집하고, V-JEPA2 기반의 비언어적 행동 인식기와 LLM 대화 프레임워크를 구축하여 인식 라벨을 프롬프트 토큰으로 대화 기록에 주입한다. 핵심 기여는 비언어적 촉발 발화 비율(15.3%)을 정량화하고, 경량 인식기(약 8 FPS)가 실시간 요구 사항을 충족할 수 있음을 검증한 것이다.

## 그것이 바꾼 것

기존 서비스 로봇 대화 시스템은 거의 전적으로 계단식 음성 파이프라인(STT–LLM–TTS)에 의존하며, 상호작용의 시작점을 음성으로 한정한다. 그러나 실제 소매 환경에서는 많은 고객-로봇 상호작용이 비언어적 행동에 의해 시작되거나 유도되며, 오디오 입력만 있는 시스템은 이러한 상호작용 기회를 체계적으로 놓치게 된다. 저자는 실제 배포 데이터를 통해 이러한 비언어적 촉발 발화가 전체 로봇 발화의 15.3%를 차지함을 증명한다——이는 주변부 사례가 아니라 무시할 수 없는 상호작용 패턴이다.

실제로 바뀐 것은 "대화 시스템 입력 양식"의 경계이다. 기존의 다중 모달 대화 연구는 주로 시각적 콘텐츠 이해(예: 객체, 장면 인식)에 초점을 맞춘 반면, 본 논문은 "사람의 행동 의도"를 대화 촉발 신호로 주목한다. 저자는 무거운 VLM을 사용한 프레임별 이해 대신, 경량 인식기(약 8 FPS)를 LLM과 병렬로 실행하고 행동 라벨을 이산 토큰으로 대화 기록에 주입하는 방식을 설계했다. 이러한 "인식-주입" 아키텍처는 VLM 실시간 추론의 높은 지연 시간(Gemini 3.5 Flash는 6.63초 필요)을 피하여, 비언어적 신호가 실제로 대화 결정 루프에 진입할 수 있게 한다.

## 방법 분해

### 데이터 수집 및 주석
- 실제 약국에 원격 조종 휴머노이드 로봇 Sota(약 0.3m 높이, 8자유도)를 배포하여 32시간(6일) 운영
- 1시간 42분만 주석하여 2,178개의 로봇 발화를 확보했으며, 그중 334개(15.3%)가 비언어적 촉발
- 이해관계가 없는 4명의 주석자가 발화를 "음성에 대한 응답"과 "비언어적 촉발 발화"로 분류하고, 후자는 촉발 행동 범주와 발화 의도(5개 클래스)로 추가 주석

### 행동 선택
21가지 촉발 행동 중 9가지 중요한 행동을 선정했으며, 선택 기준은 빈도, 고객 서비스 시나리오 특성, 비디오에서의 안정적 감지 가능성에 기반한다:
- 고빈도 행동: Approached(29.2%), Waved(11.6%), Walked away(7.9%)
- 저빈도지만 강한 연관성: Touched belongings(0.7%), 작업 지시와 강한 연관성(66.7%가 Task-related info & directives 촉발)

### 인식 모델 아키텍처
- 입력: 비디오 클립 + 각 인물의 경계 상자 시퀀스
- 특징 추출: Vision Transformer(V-JEPA2)가 장면 특징을 추출하고, MLP가 위치 특징을 추출
- 융합: Hadamard 곱으로 두 특징을 융합하고, 어텐션 풀링으로 집계한 후 MLP 분류기가 다중 라벨 로짓을 출력
- 손실: 가중 이진 교차 엔트로피(가중치는 클래스 양성 예시 수의 역수), 클래스 불균형 대응

### 대화 프레임워크
- 비언어적 인식과 대화 시스템이 병렬로 실행
- 인식 라벨이 프롬프트 토큰(예: [waved], [pointed])으로 대화 기록에 추가
- LLM(Gemini 2.5 Flash)이 응답을 생성하며, 최소 프롬프트 설정을 사용하여 각 라벨에 대한 명시적 규칙을 피함
- Showed items가 감지된 경우에만 추가로 VLM을 사용하여 물품 식별

### 훈련 구성
- PyTorch 구현, 20 에포크, 배치 크기 16, 5겹 교차 검증
- 슬라이딩 윈도우 스텝 w 프레임, 추론 슬라이딩 윈도우 8 프레임

## 핵심 혁신

1. **실제 시나리오 데이터 기반 행동-의도 매핑**: 실험실 합성 데이터와 달리, 본 논문은 32시간의 실제 약국 운영 데이터를 기반으로 9가지 비언어적 행동과 5가지 발화 의도의 대응 관계를 정량화한다. 예를 들어 Approached는 주로 Social & Greeting(66.4%)을 촉발하고, Touched belongings는 거의 전적으로 Task-related info & directives(66.7%)를 촉발한다. 이러한 매핑 관계는 후속 시스템 설계에 실증적 기반을 제공한다.

2. **경량 인식기+LLM 병렬 아키텍처**: 비언어적 인식을 대화 생성에서 분리하여, 인식기는 약 8 FPS(사람 감지/추적 제외)로 실행되어 실시간 요구 사항(>1 FPS)을 충족한다. 인식 라벨은 이산 토큰으로 대화 기록에 주입되어 VLM의 프레임별 추론의 높은 지연 시간(Gemini 3.5 Flash는 6.63초 필요, 1초 응답 예산을 크게 초과)을 피한다. 이러한 설계는 시스템을 소비자급 GPU(RTX 3080)에서 배포할 수 있게 한다.

3. **최소 프롬프트 설계**: 각 행동 라벨에 대한 명시적 규칙을 설정하지 않고, LLM이 대화 기록의 라벨 토큰에서 응답 전략을 스스로 추론하도록 한다. 이는 엔지니어링 복잡성을 줄이면서 대화의 자연스러움을 유지한다——오프라인 평가에서 전체 의도 일치율 49.1%로, 다수 클래스 기준선 44.0%를 초과한다.

## 실험 및 결과

### 인식 성능(Table IV, micro Avg.)
| 지표 | 값 |
|------|------|
| Precision | 0.89 |
| Recall | 0.73 |
| F1 | 0.80 |
| Accuracy | 0.97 |

### 각 클래스별 F1 성능
| 행동 | F1 | 비고 |
|------|-----|------|
| Approached | 0.90 | 고빈도, 최고 성능 |
| Showed items | 0.88 | 저빈도지만 인식 안정적 |
| Peered into robot | 0.79 | 중빈도, 성능 양호 |
| Nodded | 0.65 | 저빈도, 성능 보통 |
| Pointed | 0.62 | 저빈도, 정밀도 낮음(0.57) |
| Waved | 0.59 | 중빈도, 정밀도 낮음(0.57) |
| Walked away | 0.62 | 중빈도, 정밀도 낮음(0.50) |
| Touched belongings | 0.61 | 극저빈도, F1 양호 |
| User–user interaction | 0.47 | 재현율 낮음(0.31) |

### 오프라인 발화 생성
- 334개의 비언어적 촉발 발화에서 전체 의도 일치율 49.1%
- Social & Greeting 정확도 69%
- Task-related info & directives 정확도 낮음, 라벨이 희소하고( Touched belongings는 0.7%에 불과) 환경 특정 세부 정보가 필요하기 때문

### 추론 속도
- 인식기(사람 감지/추적 제외) 약 8 FPS, 실시간 요구 사항 충족
- VLM 참조 지연 시간: Gemini 3.5 Flash 6.63 ± 1.19초, Gemini 3.5 Flash Lite 2.54 ± 0.58초, 모두 1초 응답 예산 초과

## 경계 및 한계

- 평가는 주로 오프라인이며, 파이프라인에서 실제 오류(예: 사람 감지/추적)의 전파를 완전히 포착하지 못함; 온라인 종단 간 평가와 사용자 경험 지표가 필요
- 데이터는 단일 매장 입구의 원격 조종 서비스에서 나왔으며, 매장 유형, 인구 밀도, 레이아웃, 운영자 전략에 따른 일반화가 제한적
- 의도 불균형이 추정과 학습에 영향을 미칠 수 있음——Task-related info & directives는 10.5%에 불과하고, 관련 행동 Touched belongings는 0.7%에 불과
- 발화 생성 평가는 의도 라벨 일치성에만 기반하며, 누락된 작업 지시를 처벌하지 않고 사용자 경험 측정을 포함하지 않음
- 운영자가 때때로 상황적 타이밍을 무시하고 작업 관련 발화를 생성하여 훈련 데이터를 오염시킬 수 있음

## 엔지니어링 시사점

- **먼저 행동-의도 매핑의 안정성을 확인하라**: Approached→Social & Greeting(66.4%)과 Touched belongings→Task-related info & directives(66.7%)는 강한 연관성이지만, Waved→Social & Greeting(65.9%)과 Walked away→Social & Greeting(73.3%)의 구분력은 충분하지 않으므로, 재현 시 행동 정의의 경계에 주의해야 함
- **클래스 불균형이 주요 함정이다**: Touched belongings는 0.7%에 불과하지만 F1이 0.61에 달하는 것은 가중 손실 덕분; 다운스트림 시나리오에서 이 행동이 더 드물다면 가중치를 재조정하거나 few-shot 전략을 고려해야 함
- **인식기와 대화 시스템의 시간 동기화**: 인식기는 약 8 FPS이지만 LLM 생성은 수 초가 걸리므로, 행동 라벨이 대화 기록에서 올바른 위치에 있도록 버퍼링 메커니즘을 설계해야 함; 라벨 토큰에 타임스탬프를 추가할 것을 권장
- **VLM을 Showed items에만 사용하는 것은 현명한 절충이다**: 이 행동은 1.2%에 불과하지만 User/state comment & empathy(50.0%)를 촉발하므로, 필요 시 VLM을 호출하여 지연 시간을 제어할 수 있음; 시나리오에서 이 행동의 빈도가 증가하면 비동기 프리페치를 고려해야 함
- **오프라인 평가의 의도 일치율 49.1%는 하한선이다**: 다수 클래스 기준선 44.0%와 비교해 개선은 5.1% 포인트에 불과; 다운스트림 작업이 의도 정확성에 대한 요구가 높다면 온라인 강화 학습이나 인간 피드백 미세 조정을 도입해야 함
