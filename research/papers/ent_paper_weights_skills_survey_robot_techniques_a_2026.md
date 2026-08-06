---
$id: ent_paper_weights_skills_survey_robot_techniques_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their
    Own Skills'
  zh: 'Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their
    Own Skills'
  ko: 'Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their
    Own Skills'
summary:
  en: 'Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action,
    or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field
    around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy
    methods by their degree of.'
  zh: 这篇综述由 Jena 等人撰写，系统梳理了机器人学习中“冻结权重”（VLA 模型）与“可执行技能”（code-as-policy）两条技术路线，并提出了一个以“自我改进程度”为核心的组织分类学。核心贡献在于定义了从零样本合成到完整自我改进循环的五级阶梯，并识别出仅
    ASPIRE、ENPIRE、RoboClaw 三个系统占据最高梯级，同时将技能市场（如 Unitree UniStore）纳入分析框架，指出其承诺与实现之间的断层。
  ko: 'Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action,
    or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field
    around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy
    methods by their degree of.'
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
- weights
- skills
- survey
- robot
- techniques
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.01851 Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting'
  url: https://arxiv.org/abs/2608.01851
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

这篇综述由 Jena 等人撰写，系统梳理了机器人学习中“冻结权重”（VLA 模型）与“可执行技能”（code-as-policy）两条技术路线，并提出了一个以“自我改进程度”为核心的组织分类学。核心贡献在于定义了从零样本合成到完整自我改进循环的五级阶梯，并识别出仅 ASPIRE、ENPIRE、RoboClaw 三个系统占据最高梯级，同时将技能市场（如 Unitree UniStore）纳入分析框架，指出其承诺与实现之间的断层。

## 它改变了什么

这篇综述真正改变的是看待机器人学习版图的方式。此前领域内综述要么按算法家族（模仿学习、RL、LLM 规划）切分，要么按任务类型（操作、导航、运动）组织，从未有人以“交付物是什么”以及“系统能否在部署后自我改进”作为主轴。作者将“技能”一词的五种含义（潜在策略、选项/原语、代码、机器人应用、市场产品）摊开，指出只有“代码”这一含义同时具备可检查、可适应、可组合性，而只有“应用”和“市场产品”具备可分发性——这个不匹配正是“技能经济”必须弥合的鸿沟。

更尖锐的洞察在于对商业现实的审视。Unitree UniStore 这类技能市场提供一键跨模型动作下载，但所有技能都是静态回放，处于分类学中能力最弱的点。市场承诺的价值（如“根据水果调整抓握力度以免碰伤”）依赖设备端自我改进，而目前没有任何已发布的技能实现这一点。这把一个纯学术分类问题变成了对产业现状的批判：如果技能不能自我改进，所谓“技能经济”就只是动作包的批发市场，而非可进化能力的交易平台。

## 方法拆解

### 语料构建（PRISMA 2020 风格）
- 两轮构建，覆盖 2016 年 1 月至 2026 年 7 月窗口
- 第一轮：种子与滚雪球方式筛选 77 个分类学系统
- 第二轮：5 次结构化网络搜索收集 225 个景观语料
- 纳入标准：关注具身智能体的技能/策略编写、学习、迁移、评估或分发；携带可验证元数据
- 排除标准：纯感知、导航和运动工作（除非直接涉及操作技能编写与改进）、元数据无法验证、重复项

### 分类学组织轴
- 以“交付什么”为分界：冻结权重（§3.2）还是可执行技能（§3.1）
- 三个机制的运行定义（表 3）：
  - **反馈 (F)**：读取执行接地信号并用于任务内修订代码。不计入：新的人类指令、从未在运行时查询的固定预训练价值函数
  - **记忆 (M)**：运行时写入的内容跨任务边界存储并在后续任务中检索。不计入：模型冻结的预训练权重、任务内暂存器
  - **搜索 (S)**：维护多个候选程序，按执行评分并选择/变异。不计入：单链修复链、无选择的一次性采样

### 自我改进阶梯五问
按顺序判定：(i) 是否编写控制代码；(ii) 是否在任务内从执行反馈修复代码；(iii) 是否跨任务记住已验证代码；(iv) 是否搜索程序群体；(v) 是否将全部闭环为一个开放循环。

- §3.1.1 零样本合成：F✘M✘S✘
- §3.1.2 闭环自我修复：F✔M✘S✘
- §3.1.3 技能库积累：F✘M✔S✘（DROC 为 F✔M✔S✘）
- §3.1.4 进化程序搜索：F✔M✘S✔
- §3.1.5 完整自我改进循环：F✔M✔S✔

### VLA 架构对比
- 共享骨干-动作头分解：视觉-语言骨干编码场景和指令，可插拔动作头映射为电机命令
- 离散 token 头（RT-1/RT-2）简单但粗糙；连续头（π0 流匹配头、CogACT 扩散-变换器）以少量额外参数换取更少推理步数和更高精度
- GR00T N1：慢速 System-2 推理器与快速 System-1 扩散变换器配对

## 关键创新

1. **自我改进阶梯作为组织轴**：这是首次将 code-as-policy 方法按“能否在部署后无梯度更新地自我改进”排列，从零样本合成到完整闭环。五问判定法（F/M/S 三机制）提供了可操作的标准，而非模糊的“智能程度”描述。这使得不同系统之间可以严格比较能力边界，而非仅比较任务成功率。

2. **识别出完整自我改进循环单元**：在 302 个系统语料中，仅 ASPIRE、ENPIRE、RoboClaw 三个系统同时具备反馈、记忆、搜索三机制并闭环为开放循环。这个发现将“持续学习”从口号变成了可验证的稀缺属性——绝大多数系统要么只修复当前任务（反馈），要么只积累库（记忆），要么只搜索候选（搜索），三者合取极为罕见。

3. **技能经济框架**：将商业技能市场（UniStore）纳入学术分类学，指出其处于能力最弱层（静态回放），而承诺的价值（设备端自适应）依赖尚未实现的第 3 层（Adapt）。这把综述从文献编目提升为对产业路线图的批判性评估，为“技能可分发性 vs 可改进性”的矛盾提供了分析框架。

## 实验与结果

语料规模与分布（302 个系统）：

| 指标 | 数值 |
|------|------|
| 分类学系统 | 77 |
| 景观语料 | 225 |
| 参考文献总数 | 310 |
| 领域分支 | 6 |
| 自我改进梯级 | 5 |
| 时间跨度 | 2016–2026 |

景观语料按领域分布（225 个）：端到端/通用 28、模仿/扩散 21、LLM 规划/TAMP 30、奖励/数据生成 17、技能发现/分层 RL 25、世界/基于模型 24、表征/离线 RL 17、操作/灵巧性 16、运动/人形 16、导航/触觉 15、数据集/基准/模拟器 16。

两极随时间分布（按首次发布年份）：2022 年权重 0/技能 1；2023 年权重 2/技能 9；2024 年权重 5/技能 9；2025 年权重 4/技能 2；2026 年权重 0/技能 6（截至 7 月，部分数据）。

表 4 中 30 个 code-as-policy 阶梯系统分布：13 个零样本合成、6 个闭环自我修复、5 个技能库积累、3 个进化程序搜索、3 个完整自我改进循环。

关键基准数字：Eureka 在 29 任务 IsaacGym 套件中 83% 任务超过专家人类奖励；Open X-Embodiment 汇集 21 个机构 60 个数据集、超过 100 万条轨迹、覆盖 22 种具身；CrossFormer 在 20 种具身、900K 轨迹上训练；RoboCat 从最少 100 个演示适应新任务。

结果的含义：完整自我改进循环单元仅由 3 个系统占据，说明该领域仍处于早期；2026 年技能极数量（6）显著超过权重极（0），暗示趋势正在转向代码即策略方向（由表内数值 0→6 计算）。

## 边界与局限

作者明确承认这是刻意聚焦的综述而非穷尽式普查，未对领域进行详尽编目。组织轴“自我改进程度”是刻意以代码为中心的，将基于权重的策略和 RL 技能发现视为背景而非分类对象——这意味着 VLA 路线的支持者可能认为该框架有失偏颇。

前沿系统（§3.1.5）非常新，部分为同期系统，基准数字不可直接比较，因此作者定性报告能力而非排名。领域变化快，2025–2026 年引用的系统在写作时刚发布，覆盖应视为快照而非稳定状态。“技能经济”框架基于新兴商业趋势（写作时仅一个供应商的市场），视为开放问题的动机而非成熟结果。

元数据无法验证的候选在收获时被丢弃，其数量未记录而非估计。77/225 的划分是关于分析角色的陈述（锐利范例 vs 代表性广度），而非关于工作质量或重要性的陈述。2026 年数据为部分（截至 7 月）。

## 工程启示

对复现和下游团队，先核对三件事：第一，确认你关注的系统在 F/M/S 三机制上的真实状态——很多论文声称“持续学习”但实际只有反馈（F）而无记忆（M）或搜索（S），用表 3 的运行定义逐一核对，避免被术语误导。第二，注意“技能”一词在文献中的五种含义混用，明确你讨论的是代码、潜在策略还是市场产品，否则对比会失真。

最容易踩坑的地方是搜索（S）的判定：单链修复（反馈）与多候选选择（搜索）的边界容易被模糊。如果系统只是对同一程序反复打补丁，那是反馈而非搜索；只有维护多个候选并按执行评分选择/变异才算搜索。另一个坑是记忆（M）的判定：预训练权重和固定 API 库不计入，必须是运行时写入且跨任务检索的内容。

对工程选型，如果目标是部署后自适应，优先考虑具备 F✔M✔S✔ 三机制的系统（目前仅 ASPIRE、ENPIRE、RoboClaw），否则你得到的只是静态技能包。对市场类产品（如 UniStore），务必审计其是否具备第 3 层（Adapt）能力，否则“根据水果调整抓握力度”这类承诺无法兑现。表 9 提出的四个可测量量（成功-交互曲线、技能库复用率、跨具身迁移下降、来源检查）可作为评估任何技能系统的标准模板。

## Overview
Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action, or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy methods by their degree of self-improvement, from zero-shot program synthesis, through closed-loop self-repair and persistent skill memory, to the sparsely populated cell in which execution feedback, skill memory, and evolutionary search combine into one open-ended loop; only a few very recent systems (for example ASPIRE, ENPIRE, and RoboClaw) occupy that cell. We map the complementary "skills" pole, from unsupervised reinforcement-learning skill discovery to large-language-model skill libraries, and show that the word "skill" is used in at least five distinct senses, of which only the code sense self-improves without gradient updates. We then connect the taxonomy to the emerging skill economy: commercial robot-skill marketplaces now distribute one-tap skills across robots but ship only static playback, which surfaces open problems of adaptation, cross-embodiment portability, provenance, safety verification, composition, and standardisation. This is a deliberately focused survey. Rather than cataloguing the field exhaustively, it examines 77 representative systems across six technique families through one taxonomy and a set of contrast tables, and it supplies operational definitions of the self-improvement mechanisms together with a statement of what each family cannot do.

## 参考
- https://arxiv.org/abs/2608.01851

## 개요

이 리뷰는 Jena 등이 작성했으며, 로봇 학습에서의 '고정 가중치'(VLA 모델)와 '실행 가능한 스킬'(code-as-policy)이라는 두 가지 기술 경로를 체계적으로 정리하고, '자기 개선 정도'를 핵심으로 하는 조직적 분류 체계를 제안합니다. 핵심 기여는 제로샷 합성부터 완전한 자기 개선 루프까지의 5단계 사다리를 정의하고, ASPIRE, ENPIRE, RoboClaw 세 시스템만이 최상위 단계를 차지한다는 점을 식별한 것입니다. 또한 스킬 마켓(예: Unitree UniStore)을 분석 프레임워크에 포함시켜 그 약속과 실제 구현 사이의 단절을 지적합니다.

## 무엇을 바꾸었는가

이 리뷰가 진정으로 바꾼 것은 로봇 학습 지형을 바라보는 방식입니다. 이전의 리뷰들은 알고리즘 계열(모방 학습, RL, LLM 계획)이나 작업 유형(조작, 내비게이션, 운동)에 따라 분류했지만, '산출물이 무엇인가'와 '시스템이 배포 후 자기 개선이 가능한가'를 축으로 삼은 경우는 없었습니다. 저자들은 '스킬'이라는 단어의 다섯 가지 의미(잠재 정책, 옵션/프리미티브, 코드, 로봇 애플리케이션, 마켓 제품)를 펼쳐 보이며, '코드'만이 검사 가능성, 적응성, 조합성을 동시에 갖추고 있으며, '애플리케이션'과 '마켓 제품'만이 배포 가능성을 갖추고 있다는 점을 지적합니다. 이러한 불일치가 바로 '스킬 경제'가 해소해야 할 간극입니다.

더 날카로운 통찰은 상업적 현실에 대한 검토에서 나옵니다. Unitree UniStore와 같은 스킬 마켓은 원클릭 크로스-모델 동작 다운로드를 제공하지만, 모든 스킬은 정적 재생에 불과하며 분류 체계에서 가장 약한 능력 지점에 위치합니다. 마켓이 약속하는 가치(예: '과일에 따라 그립 강도를 조정하여 손상 방지')는 디바이스 측 자기 개선에 의존하지만, 현재 출시된 어떤 스킬도 이를 구현하지 못합니다. 이는 순수한 학술적 분류 문제를 산업 현황에 대한 비판으로 전환시킵니다: 스킬이 자기 개선을 할 수 없다면, 이른바 '스킬 경제'는 진화 가능한 능력의 거래 플랫폼이 아니라 단지 동작 패키지의 도매 시장일 뿐입니다.

## 방법론 분석

### 코퍼스 구축 (PRISMA 2020 스타일)
- 2라운드 구축, 2016년 1월부터 2026년 7월까지의 기간을 포괄
- 1라운드: 시드 및 스노우볼 방식으로 77개 분류 체계 시스템 선별
- 2라운드: 5회의 구조화된 웹 검색으로 225개 랜드스케이프 코퍼스 수집
- 포함 기준: 임베디드 에이전트의 스킬/정책 작성, 학습, 전이, 평가 또는 배포에 초점; 검증 가능한 메타데이터 보유
- 제외 기준: 순수 인식, 내비게이션 및 운동 작업(조작 스킬 작성 및 개선에 직접 관련되지 않는 한), 메타데이터 검증 불가, 중복 항목

### 분류 체계 조직 축
- '무엇을 산출하는가'를 기준으로 구분: 고정 가중치(§3.2) 또는 실행 가능한 스킬(§3.1)
- 세 가지 메커니즘의 운영 정의(표 3):
  - **피드백 (F)**: 실행 접지 신호를 읽고 작업 내 코드 수정에 사용. 포함하지 않음: 새로운 인간 지시, 런타임에 쿼리되지 않는 고정 사전 훈련 가치 함수
  - **메모리 (M)**: 런타임에 기록된 내용이 작업 경계를 넘어 저장되고 후속 작업에서 검색. 포함하지 않음: 모델의 고정 사전 훈련 가중치, 작업 내 임시 레지스터
  - **검색 (S)**: 여러 후보 프로그램을 유지하고, 실행 점수에 따라 선택/변이. 포함하지 않음: 단일 체인 수리, 선택 없는 일회성 샘플링

### 자기 개선 사다리 5가지 질문
순서대로 판정: (i) 제어 코드를 작성하는가; (ii) 작업 내에서 실행 피드백으로 코드를 수리하는가; (iii) 검증된 코드를 작업 간에 기억하는가; (iv) 프로그램 집단을 검색하는가; (v) 전체를 하나의 개방 루프로 폐쇄하는가.

- §3.1.1 제로샷 합성: F✘M✘S✘
- §3.1.2 폐쇄 루프 자기 수리: F✔M✘S✘
- §3.1.3 스킬 라이브러리 축적: F✘M✔S✘ (DROC는 F✔M✔S✘)
- §3.1.4 진화적 프로그램 검색: F✔M✘S✔
- §3.1.5 완전한 자기 개선 루프: F✔M✔S✔

### VLA 아키텍처 비교
- 공유 백본-액션 헤드 분해: 비전-언어 백본이 장면과 지시를 인코딩하고, 플러그형 액션 헤드가 모터 명령으로 매핑
- 이산 토큰 헤드(RT-1/RT-2)는 단순하지만 조잡함; 연속 헤드(π0 흐름 매칭 헤드, CogACT 확산-트랜스포머)는 소량의 추가 파라미터로 더 적은 추론 단계와 더 높은 정밀도를 얻음
- GR00T N1: 느린 System-2 추론기와 빠른 System-1 확산 트랜스포머의 페어링

## 핵심 혁신

1. **자기 개선 사다리를 조직 축으로**: code-as-policy 방법을 '배포 후 그래디언트 업데이트 없이 자기 개선이 가능한가'에 따라 제로샷 합성부터 완전한 폐쇄 루프까지 배열한 최초의 시도. 5가지 질문 판정법(F/M/S 세 메커니즘)은 모호한 '지능 수준' 설명이 아닌 실행 가능한 기준을 제공합니다. 이를 통해 서로 다른 시스템 간에 작업 성공률만 비교하는 것이 아니라 능력 경계를 엄격하게 비교할 수 있습니다.

2. **완전한 자기 개선 루프 유닛 식별**: 302개 시스템 코퍼스 중 ASPIRE, ENPIRE, RoboClaw 세 시스템만이 피드백, 메모리, 검색 세 메커니즘을 모두 갖추고 개방 루프로 폐쇄합니다. 이 발견은 '지속 학습'을 구호에서 검증 가능한 희소 속성으로 전환시킵니다 — 대부분의 시스템은 현재 작업만 수리하거나(피드백), 라이브러리만 축적하거나(메모리), 후보만 검색하거나(검색) 하며, 세 가지의 결합은 극히 드뭅니다.

3. **스킬 경제 프레임워크**: 상업적 스킬 마켓(UniStore)을 학술 분류 체계에 통합하여, 그것이 가장 약한 능력 계층(정적 재생)에 위치하며 약속된 가치(디바이스 측 적응)는 아직 구현되지 않은 3단계(Adapt)에 의존한다는 점을 지적합니다. 이는 리뷰를 문헌 목록에서 산업 로드맵에 대한 비판적 평가로 승격시키며, '스킬 배포 가능성 vs 개선 가능성'의 모순에 대한 분석 프레임워크를 제공합니다.

## 실험 및 결과

코퍼스 규모 및 분포 (302개 시스템):

| 지표 | 값 |
|------|------|
| 분류 체계 시스템 | 77 |
| 랜드스케이프 코퍼스 | 225 |
| 총 참고문헌 수 | 310 |
| 도메인 분기 | 6 |
| 자기 개선 단계 | 5 |
| 시간 범위 | 2016–2026 |

랜드스케이프 코퍼스의 도메인별 분포 (225개): 엔드투엔드/범용 28, 모방/확산 21, LLM 계획/TAMP 30, 보상/데이터 생성 17, 스킬 발견/계층적 RL 25, 월드/모델 기반 24, 표현/오프라인 RL 17, 조작/손재주 16, 운동/휴머노이드 16, 내비게이션/촉각 15, 데이터셋/벤치마크/시뮬레이터 16.

양극의 시간적 분포 (최초 발표 연도 기준): 2022년 가중치 0/스킬 1; 2023년 가중치 2/스킬 9; 2024년 가중치 5/스킬 9; 2025년 가중치 4/스킬 2; 2026년 가중치 0/스킬 6 (7월 기준, 일부 데이터).

표 4의 30개 code-as-policy 사다리 시스템 분포: 13개 제로샷 합성, 6개 폐쇄 루프 자기 수리, 5개 스킬 라이브러리 축적, 3개 진화적 프로그램 검색, 3개 완전한 자기 개선 루프.

주요 벤치마크 수치: Eureka는 29개 작업 IsaacGym 스위트에서 83%의 작업이 전문가 인간 보상을 초과; Open X-Embodiment는 21개 기관의 60개 데이터셋, 100만 개 이상의 궤적, 22가지 임베디드를 포괄; CrossFormer는 20가지 임베디드, 900K 궤적으로 훈련; RoboCat은 최소 100개의 데모에서 새로운 작업에 적응.

결과의 의미: 완전한 자기 개선 루프 유닛은 단 3개 시스템만이 차지하고 있어, 이 분야가 아직 초기 단계임을 시사; 2026년 스킬 극의 수(6)가 가중치 극(0)을 크게 초과하여, 코드-애즈-폴리시 방향으로의 추세 전환을 암시 (표 내 수치 0→6으로 계산).

## 경계 및 한계

저자들은 이것이 의도적으로 초점을 맞춘 리뷰이지 완전한 조사가 아니며, 분야를 철저히 목록화하지 않았다는 점을 명시적으로 인정합니다. 조직 축인 '자기 개선 정도'는 의도적으로 코드 중심이며, 가중치 기반 정책과 RL 스킬 발견을 분류 대상이 아닌 배경으로 취급합니다 — 이는 VLA 경로 지지자들이 프레임워크가 편향되었다고 생각할 수 있음을 의미합니다.

최첨단 시스템(§3.1.5)은 매우 새롭고 일부는 동시기 시스템으로, 벤치마크 수치를 직접 비교할 수 없으므로 저자들은 순위가 아닌 능력을 정성적으로 보고합니다. 분야 변화가 빠르며, 2025–2026년에 인용된 시스템은 작성 시점에 막 출시된 것으로, 포괄 범위는 안정 상태가 아닌 스냅샷으로 간주해야 합니다. '스킬 경제' 프레임워크는 신흥 상업 트렌드(작성 시점에 공급업체 하나의 마켓만 존재)에 기반하며, 성숙한 결과가 아닌 개방형 문제의 동기로 간주합니다.

메타데이터를 검증할 수 없는 후보는 수집 시 폐기되었으며, 그 수는 추정이 아닌 미기록 상태입니다. 77/225 구분은 분석 역할에 대한 진술(날카로운 예시 vs 대표적 폭)이며, 작업 품질이나 중요성에 대한 진술이 아닙니다. 2026년 데이터는 부분적입니다(7월 기준).

## 공학적 시사점

재현 및 다운스트림 팀을 위해 먼저 세 가지를 확인하십시오: 첫째, 관심 있는 시스템의 F/M/S 세 메커니즘 실제 상태를 확인하십시오 — 많은 논문이 '지속 학습'을 주장하지만 실제로는 피드백(F)만 있고 메모리(M)나 검색(S)이 없는 경우가 많습니다. 표 3의 운영 정의로 하나씩 대조하여 용어에 속지 않도록 하십시오. 둘째, '스킬'이라는 단어가 문헌에서 다섯 가지 의미로 혼용된다는 점을 인지하고, 코드, 잠재 정책, 마켓 제품 중 무엇을 논의하는지 명확히 하지 않으면 비교가 왜곡됩니다.

가장 함정에 빠지기 쉬운 곳은 검색(S)의 판정입니다: 단일 체인 수리(피드백)와 다중 후보 선택(검색)의 경계가 모호해지기 쉽습니다. 시스템이 동일한 프로그램에 반복적으로 패치를 가하는 것이라면 그것은 검색이 아닌 피드백입니다; 여러 후보를 유지하고 실행 점수에 따라 선택/변이해야만 검색입니다. 또 다른 함정은 메모리(M)의 판정입니다: 사전 훈련 가중치와 고정 API 라이브러리는 포함되지 않으며, 런타임에 기록되고 작업 간에 검색되는 내용만 해당합니다.

엔지니어링 선택 측면에서, 배포 후 적응이 목표라면 F✔M✔S✔ 세 메커니즘을 갖춘 시스템(현재 ASPIRE, ENPIRE, RoboClaw뿐)을 우선 고려하십시오. 그렇지 않으면 얻는 것은 정적 스킬 패키지에 불과합니다. 마켓형 제품(예: UniStore)의 경우 3단계(Adapt) 능력을 보유했는지 반드시 감사하십시오. 그렇지 않으면 '과일에 따라 그립 강도 조정'과 같은 약속은 이행될 수 없습니다. 표 9에서 제안된 네 가지 측정 가능한 지표(성공-상호작용 곡선, 스킬 라이브러리 재사용률, 크로스-임베디드 전이 하락, 출처 검사)는 모든 스킬 시스템 평가의 표준 템플릿으로 사용할 수 있습니다.
