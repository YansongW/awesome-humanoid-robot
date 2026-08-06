---
$id: ent_paper_survey_vision_language_action_models_emb_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Survey on Vision-Language-Action Models for Embodied AI
  zh: A Survey on Vision-Language-Action Models for Embodied AI
  ko: A Survey on Vision-Language-Action Models for Embodied AI
summary:
  en: Embodied AI is widely recognized as a cornerstone of artificial general intelligence (AGI) because it involves controlling
    embodied agents to perform tasks in the physical world. Building on the success of large language models (LLMs) and vision-language
    models (VLMs), a new category of multimodal models -- referred to as vision-language-action (VLA) models -- has emerged
    to address.
  zh: 这篇综述系统梳理了从单模态视觉、语言、强化学习模型到视觉-语言模型（VLM），再到视觉-语言-动作模型（VLA）的完整技术脉络，并专门总结了具身问答（EQA）基准的现状。作者的核心贡献在于为具身智能研究者提供了一份横跨三大模态基础组件与最新VLA范式的技术地图，并指出了各组件在机器人学习中的适用边界。
  ko: Embodied AI is widely recognized as a cornerstone of artificial general intelligence (AGI) because it involves controlling
    embodied agents to perform tasks in the physical world. Building on the success of large language models (LLMs) and vision-language
    models (VLMs), a new category of multimodal models -- referred to as vision-language-action (VLA) models -- has emerged
    to address.
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
- survey
- vision
- language
- action
- models
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P071. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: arXiv:2405.14093 A Survey on Vision-Language-Action Models for Embodied AI
  url: https://arxiv.org/abs/2405.14093
  date: '2024-05-23'
  accessed_at: '2026-08-05'
---

## 概述

这篇综述系统梳理了从单模态视觉、语言、强化学习模型到视觉-语言模型（VLM），再到视觉-语言-动作模型（VLA）的完整技术脉络，并专门总结了具身问答（EQA）基准的现状。作者的核心贡献在于为具身智能研究者提供了一份横跨三大模态基础组件与最新VLA范式的技术地图，并指出了各组件在机器人学习中的适用边界。

## 它改变了什么

这篇综述真正改变的是“具身智能研究者的文献检索方式”。在此之前，VLA领域的研究散落在CV、NLP、RL三大顶会的论文中，研究者往往需要自行跨领域追踪单模态模型的进展，再费力推断其与机器人控制的关联。作者将这一隐性工作显性化，直接给出了“哪些视觉模型适合做感知、哪些语言模型适合做指令理解、哪些RL算法适合做策略优化”的对应关系，这实际上为入门者节省了数月文献调研时间，也为资深研究者提供了一个结构化的对比框架。

更重要的是，它改变了人们对“VLA模型”这一概念的认知边界。作者没有将VLA局限为“端到端的大模型”，而是将其拆解为视觉编码器、语言模型、策略网络（或RL组件）的有机组合，并指出许多VLA实际上是在复用单模态预训练模型。这种“组件化”视角使得研究者可以独立评估和替换每个模块，而非将VLA视为不可拆分的黑盒，这对工程实践中的模块复用与故障定位具有直接指导意义。

## 方法拆解

### 视觉模态：从CNN到Transformer的演进
- **CNN脉络**：LeNet（手写数字识别）→ AlexNet（2012年ImageNet冠军）→ VGG（深度增益）→ GoogLeNet（Inception块）→ ResNet（残差连接）→ ResNeXt（split-transform-merge）→ SENet（squeeze-and-excitation注意力）→ EfficientNet（compound scaling平衡效率与性能）。
- **目标检测**：区域方法（R-CNN系列）与网格方法（YOLO）并行发展，FPN、RetinaNet采用自底向上-自顶向下策略。
- **图像分割**：主流为编码器-解码器架构（FCN、SegNet、U-Net），编码器提取全局与局部上下文，解码器生成分割图。
- **Vision Transformer**：将图像分解为16×16像素patch，每个patch视为token，采用BERT式编码，在分类任务上超越多数传统CNN。
- **DETR**：编码器-解码器Transformer，引入可学习object queries，通过交叉注意力从编码器输出提取对象级信息。
- **3D视觉**：深度图（Kinect/RealSense捕获或从RGB恢复）、点云（LiDAR/扫描仪）、体素/八叉树（信息更丰富）、网格（不规则性对神经网络有挑战）。

### 语言模态：从词嵌入到LLM
- **早期**：word2vec、GloVe词嵌入；RNN（LSTM、GRU、ELMo）与CNN（WordCNN、CharCNN）并行。
- **Transformer**：BERT（编码器堆栈，擅长理解）、GPT（解码器堆栈，擅长生成）；改进工作包括RoBERTa、ALBERT、ELECTRA、XLNet、BART、T5。
- **LLM扩展**：ChatGPT引发关注，后续有GPT-4、PaLM、LLaMA（少数开源LLM之一）等；指令微调（InstructGPT、FLAN）使预训练模型高效适配下游任务；提示工程取代任务特定微调。

### 强化学习：从DQN到RL Transformer
- **深度RL**：DQN、Double DQN（解决高估）、HER（稀疏奖励）、BCQ/BEAR/CQL（离策略约束）。
- **策略搜索**：DDPG、A3C、TRPO、PPO（信任区域稳定策略梯度），Soft AC（最大熵）。
- **RL Transformer**：Decision Transformer（建模动作）、Trajectory Transformer（建模状态与回报）、Gato（多模态多任务多具身）。
- **机器人RL**：E2E-DVP（最早端到端控制）、Levine大规模抓取CNN、QT-Opt（闭环控制）、Dreamer（长时程任务）、OpenAI灵巧手（解魔方）。

### 图模型
- **卷积GNN**：谱方法（ChebNet、GCN）与空间方法（NN4G、MPNN、GraphSage、GAT）。
- **图与视觉/语言**：场景图表达对象关系；词级图（依存图、AMR图）显式表示句法语义；文档级图（知识图）用于检索聚类。

### VLM架构演进
- **早期多流**：ViLBERT（双流+共注意力）、LXMERT（三目标预训练）。
- **单流简化**：VL-BERT、VisualBERT、UNITER（词-区域对齐损失）、ViLT（线性投影取代区域特征）。
- **对比学习**：CLIP（大规模图像-文本对）、FILIP（token级对比）、ALIGN（无过滤噪声数据）。
- **大规模LMM**：Flamingo（门控交叉注意力连接冻结NFNet与Chinchilla）、BLIP-2（Q-Former连接冻结视觉与语言模型）、PaLI/PaLI-X（联合扩展视觉与语言）。
- **指令微调**：LLaMA-Adapter（参数高效微调）、Kosmos-1/2（交错输入+接地）、InstructBLIP（指令感知Q-Former）、LLaVA/MiniGPT-4（单线性层连接+两阶段训练）。

## 关键创新

1. **组件化视角的VLA解构**：作者将VLA拆解为视觉编码器、语言模型、策略/RL组件的组合，而非视为单一端到端模型。这一视角使得研究者可以独立评估每个模块的贡献，也为模块替换与故障定位提供了方法论基础。其重要性在于，VLA领域目前缺乏统一的评估框架，组件化视角为建立模块级基准提供了可能。

2. **跨模态技术脉络的首次系统对齐**：虽然CV、NLP、RL各有综述，但将三者按“VLA组件”逻辑统一梳理，并明确标注每个模型在机器人学习中的适用场景（如视觉部分强调图像分类/检测/分割与机器人学习的相关性），这是首次。这种对齐使得研究者可以快速判断“我的机器人任务需要哪种视觉模型”，而非盲目追随最新SOTA。

3. **EQA基准的横向对比表**：作者整理了10个具身问答基准（EQA、IQUAD、MT-EQA、MP3D-EQA、EgoVQA、EgoTaskQA、EgoPlan、OpenEQA、EgoCOT、EQA-MX、LoTa-Bench），统一标注了QA数量、视频来源、答案类型、是否主动、数据收集方式与评估指标。这一对比表为选择基准提供了直接依据，填补了该领域缺乏系统性对比的空白。

## 实验与结果

论文未提供统一的实验对比，而是以表格形式汇总了VLM模型参数与EQA基准特征。关键数字汇总如下：

| 模型/基准 | 关键参数/规模 | 备注 |
|---|---|---|
| ViLBERT | 视觉44M + 语言221M | 双流+共注意力 |
| LXMERT | 视觉44M + 语言183M | 三目标预训练 |
| ViLT | 视觉2.4M + 语言85M | 线性投影取代区域特征 |
| CLIP | 视觉428M + 语言63M | 对比预训练 |
| BLIP-2 | 视觉428M/1B + Q-Former + 语言6.7B/3B/11B | Q-Former连接 |
| Flamingo | 视觉438M + 语言70B | 门控交叉注意力 |
| PaLI-X | 视觉22B + 语言32B | 联合扩展 |
| EQA | 5K QA / 750 envs | House3D模拟器 |
| EgoTaskQA | 40K QA / 2K videos | LEMMA数据集 |
| OpenEQA | 557+1079 QA / 180 envs | 开放答案+LLM评分 |
| EQA-MX | 8.2M QA / 750K images | CAESAR模拟器 |

这些数字表明：VLM领域存在明显的规模分化（从2.4M到70B），而EQA基准在数据规模（从600到8.2M）与任务形式（多项选择、开放答案、规划）上差异巨大，选择基准时需匹配任务需求。

## 边界与局限

论文未明确列出作者承认的局限，但可从内容推断以下边界：
- **视觉部分仅覆盖图像分类、检测、分割**，未涉及视频理解、光流、深度估计等与机器人感知直接相关的任务，尽管这些任务在机器人领域同样重要。
- **NLP与RL部分仅为简要概述**，作者明确指向其他综述，因此对LLM的RLHF、RL的离线学习等前沿方向未深入展开。
- **VLM表格仅包含代表性模型**，作者指出“由于篇幅有限，我们仅包含代表性的多模态数据集”，因此大量近期模型（如GPT-4V、Gemini）未被纳入。
- **EQA基准表未包含主动感知的评估指标细节**，如LoTa-Bench的Success指标定义未展开。
- **GPT-4的模型规模为估计值**，因为官方未公开。

## 工程启示

1. **先核对视觉编码器的选择**：若任务需要细粒度对象理解（如抓取），优先考虑Faster R-CNN类区域特征（ViLBERT、UNITER采用）；若任务需要全局语义对齐（如场景描述），ViT类patch特征（ViLT、CLIP）更合适。注意ViT的patch大小为16×16像素，这决定了最小可感知对象的尺度。

2. **语言模型选型需匹配指令复杂度**：简单指令（如“拿起红色杯子”）用BERT-base（110M）即可；复杂推理或长对话需LLaMA（7B）级模型。注意LLaMA-Adapter、LLaVA等采用单线性层连接，训练成本低但可能限制跨模态对齐能力；BLIP-2的Q-Former提供了更灵活的对齐机制，但需额外训练。

3. **EQA基准选择最容易踩坑的点是“Active”标记**：EQA、IQUAD、MT-EQA、MP3D-EQA支持主动感知（Agent可移动），而EgoVQA、EgoTaskQA、OpenEQA等为被动视频问答。若研究主动探索策略，必须选择Active=Yes的基准；否则评估结果无法反映具身交互能力。

4. **数据规模差异极大**：从EgoVQA的600 QA到EQA-MX的8.2M QA，选择基准时需考虑训练成本。小规模基准（如EgoVQA）适合快速验证，大规模基准（如EQA-MX）适合最终评估，但需确认模拟器（CAESAR）与真实场景的域差距。

5. **复现时优先检查数据来源**：多个模型使用自收集数据集（FILIP300M、FLD-900M、ALIGN dataset），这些数据不公开，复现时需自行构造或改用公开替代（如LAION）。Vicuna依赖ShareGPT对话，LLaVA依赖GPT辅助指令生成，这些数据生成流程需复现时特别注意。

## Overview
Embodied AI is widely recognized as a cornerstone of artificial general intelligence (AGI) because it involves controlling embodied agents to perform tasks in the physical world. Building on the success of large language models (LLMs) and vision-language models (VLMs), a new category of multimodal models -- referred to as vision-language-action (VLA) models -- has emerged to address language-conditioned robotic tasks in embodied AI by leveraging their distinct ability to generate actions. The recent proliferation of VLAs necessitates a comprehensive survey to capture the rapidly evolving landscape. To this end, we present the first survey on VLAs for embodied AI. This work provides a detailed taxonomy of VLAs, organized into three major lines of research. The first line focuses on individual components of VLAs. The second line is dedicated to developing VLA-based control policies adept at predicting low-level actions. The third line comprises high-level task planners capable of decomposing long-horizon tasks into a sequence of subtasks, thereby guiding VLAs to follow more general user instructions. Furthermore, we provide an extensive summary of relevant resources, including datasets, simulators, and benchmarks. Finally, we discuss the challenges facing VLAs and outline promising future directions in embodied AI. A curated repository associated with this survey is available at: https://github.com/yueen-ma/Awesome-VLA.

## 参考
- https://arxiv.org/abs/2405.14093

## 개요

이 리뷰 논문은 단일 모달리티 비전, 언어, 강화학습 모델에서 비전-언어 모델(VLM), 나아가 비전-언어-행동 모델(VLA)에 이르는 전체 기술 흐름을 체계적으로 정리하고, 임베디드 질의응답(EQA) 벤치마크의 현황을专门적으로 요약합니다. 저자의 핵심 기여는 임베디드 지능 연구자들에게 세 가지 주요 모달리티 기반 구성 요소와 최신 VLA 패러다임을 아우르는 기술 지도를 제공하고, 각 구성 요소가 로봇 학습에서 갖는 적용 경계를 제시한 데 있습니다.

## 그것이 바꾼 것

이 리뷰가 실제로 바꾼 것은 "임베디드 지능 연구자의 문헌 검색 방식"입니다. 그 이전에는 VLA 분야의 연구가 CV, NLP, RL 세 가지 주요 학회의 논문에 분산되어 있어, 연구자들은 종종 스스로 학제 간 단일 모달리티 모델의 발전을 추적하고 로봇 제어와의 연관성을 힘들게 추론해야 했습니다. 저자는 이러한 암묵적 작업을 명시화하여 "어떤 비전 모델이 인식에 적합하고, 어떤 언어 모델이 명령 이해에 적합하며, 어떤 RL 알고리즘이 정책 최적화에 적합한지"에 대한 대응 관계를 직접 제시했습니다. 이는 실제로 입문자에게 수개월의 문헌 조사 시간을 절약해 주고, 경력 연구자에게도 구조화된 비교 프레임워크를 제공합니다.

더 중요하게는, 이 리뷰는 "VLA 모델"이라는 개념의 인식 경계를 바꾸었습니다. 저자는 VLA를 "엔드투엔드 대형 모델"로 한정하지 않고, 비전 인코더, 언어 모델, 정책 네트워크(또는 RL 구성 요소)의 유기적 결합으로 분해하며, 많은 VLA가 실제로 단일 모달리티 사전 학습 모델을 재사용하고 있음을 지적합니다. 이러한 "구성 요소화" 관점은 연구자가 VLA를 분해 불가능한 블랙박스로 보지 않고 각 모듈을 독립적으로 평가하고 교체할 수 있게 하며, 이는 엔지니어링 실무에서 모듈 재사용과 장애 위치 파악에 직접적인 지침을 제공합니다.

## 방법 분해

### 비전 모달리티: CNN에서 Transformer로의 진화
- **CNN 계보**: LeNet(손글씨 숫자 인식) → AlexNet(2012년 ImageNet 우승) → VGG(깊이 이점) → GoogLeNet(Inception 블록) → ResNet(잔차 연결) → ResNeXt(split-transform-merge) → SENet(squeeze-and-excitation 어텐션) → EfficientNet(compound scaling으로 효율과 성능 균형).
- **객체 검출**: 영역 기반 방법(R-CNN 시리즈)과 그리드 기반 방법(YOLO)이 병행 발전, FPN, RetinaNet은 bottom-up-top-down 전략 채택.
- **이미지 분할**: 주류는 인코더-디코더 아키텍처(FCN, SegNet, U-Net)이며, 인코더는 전역 및 지역 컨텍스트를 추출하고 디코더는 분할 맵을 생성.
- **Vision Transformer**: 이미지를 16×16 픽셀 패치로 분해하고 각 패치를 토큰으로 간주, BERT 방식 인코딩을 사용하여 분류 작업에서 대부분의 기존 CNN을 능가.
- **DETR**: 인코더-디코더 Transformer로 학습 가능한 object queries를 도입, 교차 어텐션을 통해 인코더 출력에서 객체 수준 정보를 추출.
- **3D 비전**: 깊이 맵(Kinect/RealSense 캡처 또는 RGB에서 복원), 포인트 클라우드(LiDAR/스캐너), 복셀/옥트리(정보 더 풍부), 메시(불규칙성으로 신경망에 도전적).

### 언어 모달리티: 단어 임베딩에서 LLM까지
- **초기**: word2vec, GloVe 단어 임베딩; RNN(LSTM, GRU, ELMo)과 CNN(WordCNN, CharCNN) 병행.
- **Transformer**: BERT(인코더 스택, 이해에 강점), GPT(디코더 스택, 생성에 강점); 개선 작업에는 RoBERTa, ALBERT, ELECTRA, XLNet, BART, T5 포함.
- **LLM 확장**: ChatGPT가 주목을 불러일으켰고, 이후 GPT-4, PaLM, LLaMA(소수의 오픈소스 LLM 중 하나) 등이 등장; 명령 미세 조정(InstructGPT, FLAN)으로 사전 학습 모델이 하위 작업에 효율적으로 적응; 프롬프트 엔지니어링이 작업별 미세 조정을 대체.

### 강화학습: DQN에서 RL Transformer까지
- **심층 RL**: DQN, Double DQN(과대평가 해결), HER(희소 보상), BCQ/BEAR/CQL(오프폴리시 제약).
- **정책 탐색**: DDPG, A3C, TRPO, PPO(신뢰 영역 안정 정책 그래디언트), Soft AC(최대 엔트로피).
- **RL Transformer**: Decision Transformer(행동 모델링), Trajectory Transformer(상태와 보상 모델링), Gato(다중 모달리티 다중 작업 다중 임베디드).
- **로봇 RL**: E2E-DVP(최초 엔드투엔드 제어), Levine 대규모 그리핑 CNN, QT-Opt(폐루프 제어), Dreamer(장기 작업), OpenAI 손(큐브 해제).

### 그래프 모델
- **컨볼루션 GNN**: 스펙트럼 방법(ChebNet, GCN)과 공간 방법(NN4G, MPNN, GraphSage, GAT).
- **그래프와 비전/언어**: 장면 그래프가 객체 관계 표현; 단어 수준 그래프(의존 그래프, AMR 그래프)가 구문 의미를 명시적으로 표현; 문서 수준 그래프(지식 그래프)가 검색 클러스터링에 사용.

### VLM 아키텍처 진화
- **초기 다중 스트림**: ViLBERT(이중 스트림 + 공동 어텐션), LXMERT(세 가지 목표 사전 학습).
- **단일 스트림 단순화**: VL-BERT, VisualBERT, UNITER(단어-영역 정렬 손실), ViLT(선형 투영이 지역 특징 대체).
- **대조 학습**: CLIP(대규모 이미지-텍스트 쌍), FILIP(토큰 수준 대조), ALIGN(필터링 없는 노이즈 데이터).
- **대규모 LMM**: Flamingo(게이트 교차 어텐션으로 동결 NFNet과 Chinchilla 연결), BLIP-2(Q-Former로 동결 비전 및 언어 모델 연결), PaLI/PaLI-X(비전과 언어 공동 확장).
- **명령 미세 조정**: LLaMA-Adapter(파라미터 효율적 미세 조정), Kosmos-1/2(교차 입력 + 접지), InstructBLIP(명령 인식 Q-Former), LLaVA/MiniGPT-4(단일 선형 레이어 연결 + 2단계 훈련).

## 핵심 혁신

1. **구성 요소화 관점의 VLA 분해**: 저자는 VLA를 단일 엔드투엔드 모델이 아닌 비전 인코더, 언어 모델, 정책/RL 구성 요소의 조합으로 분해합니다. 이 관점은 연구자가 각 모듈의 기여를 독립적으로 평가할 수 있게 하며, 모듈 교체와 장애 위치 파악을 위한 방법론적 기반을 제공합니다. 그 중요성은 VLA 분야에 현재 통일된 평가 프레임워크가 부족하다는 점에서, 구성 요소화 관점이 모듈 수준 벤치마크 구축의 가능성을 열어준다는 데 있습니다.

2. **크로스 모달리티 기술 흐름의 최초 체계적 정렬**: CV, NLP, RL 각각에 대한 리뷰는 존재하지만, 세 가지를 "VLA 구성 요소" 논리로 통합 정리하고 각 모델의 로봇 학습 적용 시나리오를 명시적으로 표시한 것(예: 비전 부분에서 이미지 분류/검출/분할과 로봇 학습의 관련성 강조)은 이번이 처음입니다. 이러한 정렬은 연구자가 최신 SOTA를 맹목적으로 따르는 대신 "내 로봇 작업에 어떤 비전 모델이 필요한지"를 빠르게 판단할 수 있게 합니다.

3. **EQA 벤치마크의 횡적 비교표**: 저자는 10개의 임베디드 질의응답 벤치마크(EQA, IQUAD, MT-EQA, MP3D-EQA, EgoVQA, EgoTaskQA, EgoPlan, OpenEQA, EgoCOT, EQA-MX, LoTa-Bench)를 정리하고, QA 수, 비디오 출처, 답변 유형, 능동성 여부, 데이터 수집 방식, 평가 지표를 통일적으로 표시했습니다. 이 비교표는 벤치마크 선택의 직접적인 근거를 제공하며, 해당 분야의 체계적 비교 부재라는 공백을 메웠습니다.

## 실험 및 결과

이 논문은 통일된 실험 비교를 제공하지 않고, VLM 모델 파라미터와 EQA 벤치마크 특징을 표 형식으로 요약합니다. 주요 수치 요약은 다음과 같습니다:

| 모델/벤치마크 | 주요 파라미터/규모 | 비고 |
|---|---|---|
| ViLBERT | 비전 44M + 언어 221M | 이중 스트림 + 공동 어텐션 |
| LXMERT | 비전 44M + 언어 183M | 세 가지 목표 사전 학습 |
| ViLT | 비전 2.4M + 언어 85M | 선형 투영이 지역 특징 대체 |
| CLIP | 비전 428M + 언어 63M | 대조 사전 학습 |
| BLIP-2 | 비전 428M/1B + Q-Former + 언어 6.7B/3B/11B | Q-Former 연결 |
| Flamingo | 비전 438M + 언어 70B | 게이트 교차 어텐션 |
| PaLI-X | 비전 22B + 언어 32B | 공동 확장 |
| EQA | 5K QA / 750 envs | House3D 시뮬레이터 |
| EgoTaskQA | 40K QA / 2K videos | LEMMA 데이터셋 |
| OpenEQA | 557+1079 QA / 180 envs | 개방형 답변 + LLM 평가 |
| EQA-MX | 8.2M QA / 750K images | CAESAR 시뮬레이터 |

이 수치들은 VLM 분야에 뚜렷한 규모 분화(2.4M에서 70B)가 존재하며, EQA 벤치마크는 데이터 규모(600에서 8.2M)와 작업 형태(객관식, 개방형 답변, 계획)에서 큰 차이를 보여, 벤치마크 선택 시 작업 요구사항과의 일치가 필요함을 시사합니다.

## 경계와 한계

이 논문은 저자가 인정한 한계를 명시적으로 나열하지 않았지만, 내용에서 다음과 같은 경계를 추론할 수 있습니다:
- **비전 부분은 이미지 분류, 검출, 분할만 다루며**, 로봇 인식과 직접 관련된 비디오 이해, 광학 흐름, 깊이 추정 등의 작업은 포함하지 않습니다. 이러한 작업도 로봇 분야에서 동등하게 중요합니다.
- **NLP와 RL 부분은 간략한 개요에 불과**하며, 저자는 명시적으로 다른 리뷰를 참조하므로 LLM의 RLHF, RL의 오프라인 학습 등 최신 방향에 대한 심층 논의는 없습니다.
- **VLM 표는 대표 모델만 포함**하며, 저자는 "지면 제한으로 대표적인 다중 모달리티 데이터셋만 포함한다"고 밝혀, GPT-4V, Gemini 등 많은 최근 모델이 제외되었습니다.
- **EQA 벤치마크 표는 능동 인식 평가 지표의 세부 사항을 포함하지 않으며**, 예를 들어 LoTa-Bench의 Success 지표 정의가 자세히 설명되지 않았습니다.
- **GPT-4의 모델 규모는 추정치**입니다. 공식적으로 공개되지 않았기 때문입니다.

## 엔지니어링 시사점

1. **먼저 비전 인코더 선택을 검토하세요**: 작업에 세밀한 객체 이해가 필요한 경우(예: 그리핑), Faster R-CNN 계열 지역 특징(ViLBERT, UNITER 채택)을 우선 고려하세요; 전역 의미 정렬이 필요한 경우(예: 장면 설명), ViT 계열 패치 특징(ViLT, CLIP)이 더 적합합니다. ViT의 패치 크기가 16×16 픽셀임을 주의하세요. 이는 인식 가능한 최소 객체의 스케일을 결정합니다.

2. **언어 모델 선택은 명령 복잡도와 일치해야 합니다**: 간단한 명령(예: "빨간 컵 집어")은 BERT-base(110M)로 충분합니다; 복잡한 추론이나 긴 대화는 LLaMA(7B)급 모델이 필요합니다. LLaMA-Adapter, LLaVA 등은 단일 선형 레이어 연결을 사용하여 훈련 비용이 낮지만 크로스 모달리티 정렬 능력이 제한될 수 있습니다; BLIP-2의 Q-Former는 더 유연한 정렬 메커니즘을 제공하지만 추가 훈련이 필요합니다.

3. **EQA 벤치마크 선택에서 가장 쉽게 함정에 빠지는 지점은 "Active" 표시입니다**: EQA, IQUAD, MT-EQA, MP3D-EQA는 능동 인식(에이전트 이동 가능)을 지원하는 반면, EgoVQA, EgoTaskQA, OpenEQA 등은 수동 비디오 질의응답입니다. 능동 탐색 전략을 연구한다면 반드시 Active=Yes인 벤치마크를 선택해야 합니다; 그렇지 않으면 평가 결과가 임베디드 상호작용 능력을 반영하지 못합니다.

4. **데이터 규모 차이가 매우 큽니다**: EgoVQA의 600 QA에서 EQA-MX의 8.2M QA까지, 벤치마크 선택 시 훈련 비용을 고려해야 합니다. 소규모 벤치마크(예: EgoVQA)는 빠른 검증에 적합하고, 대규모 벤치마크(예: EQA-MX)는 최종 평가에 적합하지만, 시뮬레이터(CAESAR)와 실제 장면 간의 도메인 격차를 확인해야 합니다.

5. **재현 시 데이터 출처를 우선 확인하세요**: 여러 모델이 자체 수집 데이터셋(FILIP300M, FLD-900M, ALIGN dataset)을 사용하며, 이러한 데이터는 공개되지 않아 재현 시 직접 구성하거나 공개 대안(예: LAION)으로 대체해야 합니다. Vicuna는 ShareGPT 대화에 의존하고, LLaVA는 GPT 보조 명령 생성에 의존하므로, 이러한 데이터 생성 프로세스는 재현 시 특별히 주의해야 합니다.
