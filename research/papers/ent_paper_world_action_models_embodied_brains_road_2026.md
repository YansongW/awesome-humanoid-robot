---
$id: ent_paper_world_action_models_embodied_brains_road_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence'
  zh: 'From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence'
  ko: 'From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence'
summary:
  en: 'Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models,
    vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly
    promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented:
    models use incompatible action.'
  zh: 这是一篇由机器人领域研究者撰写的路线图/立场论文，提出将“世界行动模型（WAM）”作为通往“具身大脑（embodied brain）”的实验路径，核心贡献是定义了WAM预测契约、大脑意图接口、物理栈（harness）及配套的Embodiment/Task/Trace
    Card记录协议。论文主张通过显式化预测-行动接口、统一数据与评估语义，解决物理智能中模型、目标与生态系统三个耦合鸿沟，实现跨具身、跨任务的累积式进步。
  ko: 'Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models,
    vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly
    promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented:
    models use incompatible action.'
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
- world
- action
- models
- embodied
- brains
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
  title: 'arXiv:2607.11689 From World Action Models to Embodied Brains: A Roadmap for Open-World Physical I'
  url: https://arxiv.org/abs/2607.11689
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

这是一篇由机器人领域研究者撰写的路线图/立场论文，提出将“世界行动模型（WAM）”作为通往“具身大脑（embodied brain）”的实验路径，核心贡献是定义了WAM预测契约、大脑意图接口、物理栈（harness）及配套的Embodiment/Task/Trace Card记录协议。论文主张通过显式化预测-行动接口、统一数据与评估语义，解决物理智能中模型、目标与生态系统三个耦合鸿沟，实现跨具身、跨任务的累积式进步。

## 它改变了什么

这篇论文真正改变的是物理智能领域的“接口观”。当前机器人学习社区的主流做法是端到端训练或模块化堆叠，但每个模块（预测模型、策略、控制器、数据集）都隐式编码了具身假设——更换一个夹爪或控制器，往往意味着整个模型级推理需要重新学习。作者指出，障碍不是数据多样性本身，而是“语义仍然隐藏的多样性”：预测接口暴露不同后果变量，数据标注描述不同决策上下文，运行时逻辑隐藏表征转换。这使得即使单个系统在改进，组件也无法独立替换、跨项目经验无法积累。

论文将问题系统化为三个耦合鸿沟：模型与表示差距（缺乏持久可操作的物理状态描述）、目标与标准化差距（端任务成功掩盖预测正确性与控制器依赖）、生态系统与系统差距（缺乏类似数字智能体的成熟接口处理空间关系、坐标系与不确定性）。这改变了讨论框架——从“谁的模型更强”转向“谁定义了可比较的接口”，为跨团队、跨具身的协作提供了共同语言。

## 方法拆解

### 核心架构：大脑-外设分离
- **具身大脑（embodied brain）**：负责物理推理与意图表达，输出“中间意图表示”（预期状态转换或能力请求），而非执行器命令。
- **物理栈（physical harness）**：将意图落地为可执行链，负责意图接地、能力解析、验证、执行协调与恢复。
- **工具（tool）与工具模型（tool model）**：工具是物理/数字能力端点（夹爪、基座、相机）；工具模型是支持能力的学得模块（抓取规划器、导航策略）。

### WAM预测契约
给定物理上下文与候选干预，模型须暴露决策相关后果，并声明四个属性：
- **预测时域（horizon）**：后果有效的时间范围
- **参考框架（reference frame）**：后果在哪个坐标系/实体上定义
- **不确定性（uncertainty）**：置信度估计
- **有效性条件（validity conditions）**：预测成立的前提

后果表示可为视频、几何、结构化状态、预测性潜在表示或混合形式。

### 三个轻量记录协议
- **Embodiment Card**：形态、传感器、坐标约定、校准、控制速率、动作边界、可用工具、安全限制
- **Task Card**：目标、场景上下文、允许观察与能力、约束、成功标准、有意义失败模式
- **Trace Card**：将同步观察链接到大脑请求、表示版本、所选工具链、验证器决策、控制器状态、执行结果、修正与数据质量标志

### 三种预测-控制接口家族（非互斥）
1. **显式观测/几何预测**：像素空间视觉轨迹、生成视频、文本计划、预测物体流
2. **预测性潜在表示**：视频扩散模型内的预测特征、联合视频/行动扩散
3. **潜在转换/行动抽象**：离散帧间潜在行动、预测未来潜在状态

### 关键设计决策
- 接口选择与架构是否模块化/联合训练**正交**——联合训练允许，但中间责任与变换须保持可检查
- 表征标准化分两时域：近期统一语义字段（允许语言、结构化状态、学习令牌、视频、几何竞争）；长期共享世界中心3D/4D表示是研究目标而非既定方案
- 五阶段共同演化路径：大脑模型→工具模型+harness→数据+任务→闭环学习→生态系统协调；已接纳轨迹反馈更新各层

## 关键创新

1. **预测契约作为一等公民**：首次将“后果声明”（时域、框架、不确定性、有效性条件）提升为WAM的核心接口要求。这改变了评估方式——不再只看端任务成功率，而是检查模型是否暴露了决策相关的中间信号。其新颖性在于把“预测什么”从“怎么预测”中解耦，使不同架构（视频生成、潜在表示、结构化状态）可在同一契约下比较。

2. **大脑-外设分离的“能力契约”**：不是简单的模块化主张，而是定义了工具分层组合的语义——例如“驱动钉子”可分解为手臂运动、夹爪控制、锤子获取与受限冲击。这使工具替换（换夹爪、换控制器）只改变能力声明与适配器，不迫使模型级推理重学。其重要性在于将“可替换性”从工程愿望变为可测试的设计假设。

3. **Trace Card作为可回放的物理记录**：将决策上下文、转换过程、执行状态、验证器输出与结果组织为统一记录格式。这使失败归因成为可能——区分意图错误、翻译错误、工具选择错误、控制错误与环境响应错误。这是从“收集数据”到“构建可复用决策上下文”的范式转变，直接支撑闭环后训练与回归门控。

## 实验与结果

论文为路线图/综述性质，未报告成功率、误差或参数数量等定量实验结果。其“实验”体现为对现有数据资源与系统的系统化盘点：

| 数据集 | 关键数字（逐字来自白名单） |
|---|---|
| Something-Something V2 | 220847 clips（官方V2版本） |
| Ego4D | 3670 hours，74 locations（论文未明确） |
| EPIC-KITCHENS-100 | 100 hours，90k action segments（论文未明确），45 kitchens（论文未明确） |
| Open X-Embodiment | 22 robot embodiments，527 skills |
| DROID | 76000 trajectories，350 hours，564 scenes，86 tasks |
| BridgeData V2 | 50365 demonstrations + 9731 scripted rollouts，24 environments |
| AgiBotWorld Colosseo | 超过100万 trajectories（论文未明确），217 tasks，5 scenarios |
| LIBERO | Four suites，130 tasks |
| Meta-World | 50 distinct tasks |

表1比较了代表性预测-控制接口系统（UniPi、VLP、Gen2Act、π₀.₇、UWM、LAPA等），但作者明确指出评估设置在不同机器人、任务与协议间**不可直接比较**。论文提出四层互补证据层（表3）与七层分层评估协议（预测性物理推理、大脑-外设接地、策略与控制、工具编排、验证与安全、外设与可追溯性、自我改进），但均为提议维度，未附数值。

## 边界与局限

作者明确承认以下边界：
- **模块化分离是设计假设，不是保证结果**——需通过表示落地、工具替换与跨具身适应来测试，论文未提供验证
- **预测性潜在表示的物理内容不可直接检查**——必须通过下游消融与控制实验建立，不能仅从表示本身假设
- **潜在行动不自动是机器人行动**——可能编码运动、视角变化或其他视觉变化，与特定具身控制空间的对应关系须被学习和评估
- **统一架构是否在跨具身或控制机制上更优尚未确立**
- **自主交互数据的实用性取决于轨迹质量、结果归因与防止强化模型错误的保障措施**——π₀.₇的自主数据规模未公开指定
- **人类视频包含相机运动、部分可观测性与人类特定运动学**，且缺乏目标机器人行动空间中的时间对齐命令流
- **规模本身不能解决传感、行动空间、控制频率、任务定义或收集协议中的差异**
- 图7-图12中的连接表示分析/设计依赖，非经验确立的因果效应；论文未提供训练配置、推理频率或硬件细节

## 工程启示

对复现与工程选型的直接指导：

1. **先核对接口语义，再比较性能**：任何跨系统比较前，先确认各方法是否声明了预测时域、参考框架、不确定性与有效性条件。若未声明，端任务分数对比无意义——可能一个系统利用了狭窄基准规律性，另一个在正确预测后果但控制器较弱。

2. **最容易踩坑处：潜在表示的“假接地”**：学习到的视觉token对控制器无操作意义，除非控制器共享其表示或接收适配器。复现LAPA、UWM类方法时，务必检查视觉转换代码与机器人行动空间的对应关系是否被显式学习——否则“预测成功”可能只是视觉相似，而非物理后果正确。

3. **Trace Card是调试利器，但字段设计决定成败**：建议从最小字段集开始（观察、大脑请求、所选工具链、验证器输出、控制器状态、结果），先验证失败归因能力，再扩展。字段过少无法区分意图错误与控制错误，过多则标注成本失控。

4. **数据收集应记录决策上下文，而非仅轨迹**：一条操作轨迹若缺少校准、参考框架、动作边界、控制器假设或失败标注，对后果建模与工具替换提供的证据较弱。BridgeData V2的50365条演示与9731条脚本rollout（由表内数值计算）若未附Embodiment Card，其复用价值将大打折扣。

5. **闭环学习须设准入闸门**：候选更新在晋升前须通过回归与安全门（如LIBERO-Safety、ROBOSHACKLES检查安全失败）。否则自主交互数据会强化模型自身错误——这是π₀.₇类方法最需警惕的自我强化循环。

## Overview
Artificial general intelligence ultimately requires agents that can reason and act in the physical world. Action models, vision-language-action policies, and world models have advanced this goal, while World Action Models (WAMs) are particularly promising because they connect candidate interventions with predicted consequences. However, progress remains fragmented: models use incompatible action spaces and prediction targets, datasets and tasks follow different conventions, and runtime systems expose limited interfaces for reuse and evaluation. We review the evolution toward WAMs and organize these limitations into three coupled gaps: model roles and representations, objectives and standardization, and system composition. Building on this analysis, we propose a co-evolution roadmap for physical intelligence centered on the \emph{embodied brain}, a long-term model target for integrating multimodal context, comparing candidate interventions, and issuing state-transition or capability requests rather than direct actuator commands. WAMs provide promising prototypes for its predictive functions, while a physical harness grounds model outputs through tools, controllers, verification, and trace logging. Shared contracts align heterogeneous models, data, tasks, and embodiments, and closed-loop post-training converts verified interaction into reusable experience. Together, these components define a modular physical-intelligence stack for adaptive and self-improving embodied agents.

## 参考
- https://arxiv.org/abs/2607.11689

## 개요

이 논문은 로봇공학 연구자들이 작성한 로드맵/입장 논문으로, '세계 행동 모델(WAM)'을 '구현된 뇌(embodied brain)'로 가는 실험적 경로로 제안한다. 핵심 기여는 WAM 예측 계약, 뇌-의도 인터페이스, 물리 스택(harness), 그리고 이에 수반되는 Embodiment/Task/Trace Card 기록 프로토콜을 정의한 것이다. 논문은 예측-행동 인터페이스를 명시화하고 데이터와 평가 의미론을 통일함으로써, 물리적 지능에서 모델, 목표, 생태계라는 세 가지 결합된 간극을 해결하고, 구현체와 작업을 아우르는 누적적 발전을 실현하고자 주장한다.

## 무엇을 바꾸는가

이 논문이 진정으로 바꾸는 것은 물리적 지능 분야의 '인터페이스 관점'이다. 현재 로봇 학습 커뮤니티의 주류 접근 방식은 엔드투엔드 훈련 또는 모듈식 적층이지만, 각 모듈(예측 모델, 정책, 제어기, 데이터셋)은 구현체 가정을 암시적으로 인코딩한다—그리퍼나 제어기를 교체하면 종종 모델 수준 추론 전체를 다시 학습해야 한다. 저자들은 장애물이 데이터 다양성 자체가 아니라 '의미론이 여전히 숨겨진 다양성'임을 지적한다: 예측 인터페이스는 서로 다른 결과 변수를 노출하고, 데이터 주석은 서로 다른 결정 맥락을 설명하며, 런타임 로직은 표현 변환을 숨긴다. 이로 인해 개별 시스템이 개선되더라도 구성 요소를 독립적으로 교체할 수 없고, 프로젝트 간 경험이 축적되지 않는다.

논문은 문제를 세 가지 결합된 간극으로 체계화한다: 모델과 표현 간극(지속적이고 조작 가능한 물리 상태 설명 부재), 목표와 표준화 간극(최종 작업 성공이 예측 정확성과 제어기 의존성을 가림), 생태계와 시스템 간극(디지털 지능체와 같은 성숙한 인터페이스가 공간 관계, 좌표계, 불확실성을 처리하는 데 부재). 이는 논의 프레임워크를 '누구의 모델이 더 강한가'에서 '누가 비교 가능한 인터페이스를 정의하는가'로 바꾸며, 팀 간·구현체 간 협업을 위한 공통 언어를 제공한다.

## 방법 분해

### 핵심 아키텍처: 뇌-주변기기 분리
- **구현된 뇌(embodied brain)**: 물리적 추론과 의도 표현을 담당하며, 실행기 명령이 아닌 '중간 의도 표현'(예상 상태 전환 또는 능력 요청)을 출력한다.
- **물리 스택(physical harness)**: 의도를 실행 가능한 체인으로 구체화하며, 의도 접지, 능력 해석, 검증, 실행 조정, 복구를 담당한다.
- **도구(tool)와 도구 모델(tool model)**: 도구는 물리적/디지털 능력 엔드포인트(그리퍼, 베이스, 카메라)이고, 도구 모델은 능력을 지원하는 학습된 모듈(파지 플래너, 내비게이션 정책)이다.

### WAM 예측 계약
물리적 맥락과 후보 개입이 주어졌을 때, 모델은 결정 관련 결과를 노출하고 네 가지 속성을 선언해야 한다:
- **예측 시간 지평(horizon)**: 결과가 유효한 시간 범위
- **참조 프레임(reference frame)**: 결과가 정의되는 좌표계/개체
- **불확실성(uncertainty)**: 신뢰도 추정
- **유효성 조건(validity conditions)**: 예측이 성립하는 전제 조건

결과 표현은 비디오, 기하, 구조화된 상태, 예측적 잠재 표현 또는 혼합 형태일 수 있다.

### 세 가지 경량 기록 프로토콜
- **Embodiment Card**: 형태, 센서, 좌표 규약, 캘리브레이션, 제어 주기, 행동 경계, 사용 가능한 도구, 안전 제한
- **Task Card**: 목표, 장면 맥락, 허용된 관찰과 능력, 제약, 성공 기준, 의미 있는 실패 모드
- **Trace Card**: 동기화된 관찰을 뇌 요청, 표현 버전, 선택된 도구 체인, 검증기 결정, 제어기 상태, 실행 결과, 수정 사항, 데이터 품질 플래그에 연결한다.

### 세 가지 예측-제어 인터페이스 패밀리(상호 배타적 아님)
1. **명시적 관찰/기하 예측**: 픽셀 공간 시각 궤적, 생성 비디오, 텍스트 계획, 예측 객체 흐름
2. **예측적 잠재 표현**: 비디오 확산 모델 내 예측 특징, 결합 비디오/행동 확산
3. **잠재 전환/행동 추상화**: 이산 프레임 간 잠재 행동, 미래 잠재 상태 예측

### 핵심 설계 결정
- 인터페이스 선택과 아키텍처의 모듈화/연합 훈련 여부는 **직교**한다—연합 훈련은 허용되지만, 중간 책임과 변환은 검사 가능해야 한다.
- 표현 표준화는 두 시기로 나뉜다: 단기적으로는 통일된 의미론 필드(언어, 구조화된 상태, 학습 토큰, 비디오, 기하가 경쟁하도록 허용); 장기적으로는 세계 중심 3D/4D 표현 공유가 연구 목표이지 확정된 방안이 아니다.
- 5단계 공진화 경로: 뇌 모델→도구 모델+harness→데이터+작업→폐루프 학습→생태계 조정; 궤적 피드백을 수용하여 각 계층을 업데이트한다.

## 핵심 혁신

1. **예측 계약을 일급 시민으로**: '결과 선언'(시간 지평, 프레임, 불확실성, 유효성 조건)을 WAM의 핵심 인터페이스 요구사항으로 처음으로 격상시켰다. 이는 평가 방식을 바꾼다—최종 작업 성공률만 보는 것이 아니라, 모델이 결정 관련 중간 신호를 노출하는지 검사한다. 그 참신함은 '무엇을 예측할지'를 '어떻게 예측할지'에서 분리하여, 서로 다른 아키텍처(비디오 생성, 잠재 표현, 구조화된 상태)가 동일한 계약 아래 비교될 수 있게 한 데 있다.

2. **뇌-주변기기 분리의 '능력 계약'**: 단순한 모듈화 주장이 아니라, 도구의 계층적 조합 의미론을 정의한다—예를 들어 '못 박기'는 팔 운동, 그리퍼 제어, 망치 획득, 제한된 충격으로 분해될 수 있다. 이는 도구 교체(그리퍼 교체, 제어기 교체)가 능력 선언과 어댑터만 변경하게 하여, 모델 수준 추론 재학습을 강요하지 않는다. 그 중요성은 '교체 가능성'을 공학적 바람에서 테스트 가능한 설계 가정으로 전환한 데 있다.

3. **Trace Card를 재생 가능한 물리 기록으로**: 결정 맥락, 전환 과정, 실행 상태, 검증기 출력, 결과를 통일된 기록 형식으로 조직한다. 이는 실패 귀인을 가능하게 한다—의도 오류, 번역 오류, 도구 선택 오류, 제어 오류, 환경 응답 오류를 구분한다. 이는 '데이터 수집'에서 '재사용 가능한 결정 맥락 구축'으로의 패러다임 전환이며, 폐루프 후훈련과 회귀 게이팅을 직접 지원한다.

## 실험과 결과

이 논문은 로드맵/리뷰 성격으로, 성공률, 오류, 파라미터 수 등의 정량적 실험 결과를 보고하지 않는다. 그 '실험'은 기존 데이터 자원과 시스템의 체계적 목록화로 나타난다:

| 데이터셋 | 핵심 수치(화이트리스트에서 그대로 인용) |
|---|---|
| Something-Something V2 | 220847 clips(공식 V2 버전) |
| Ego4D | 3670 hours, 74 locations(논문에서 명시 안 함) |
| EPIC-KITCHENS-100 | 100 hours, 90k action segments(논문에서 명시 안 함), 45 kitchens(논문에서 명시 안 함) |
| Open X-Embodiment | 22 robot embodiments, 527 skills |
| DROID | 76000 trajectories, 350 hours, 564 scenes, 86 tasks |
| BridgeData V2 | 50365 demonstrations + 9731 scripted rollouts, 24 environments |
| AgiBotWorld Colosseo | 100만 개 이상 trajectories(논문에서 명시 안 함), 217 tasks, 5 scenarios |
| LIBERO | Four suites, 130 tasks |
| Meta-World | 50 distinct tasks |

표 1은 대표적인 예측-제어 인터페이스 시스템(UniPi, VLP, Gen2Act, π₀.₇, UWM, LAPA 등)을 비교하지만, 저자들은 평가 설정이 서로 다른 로봇, 작업, 프로토콜 간에 **직접 비교 불가능**함을 명확히 지적한다. 논문은 4계층 보완 증거 계층(표 3)과 7계층 계층적 평가 프로토콜(예측적 물리 추론, 뇌-주변기기 접지, 정책과 제어, 도구 오케스트레이션, 검증과 안전, 주변기기와 추적 가능성, 자기 개선)을 제안하지만, 모두 제안된 차원일 뿐 수치가 첨부되지 않았다.

## 경계와 한계

저자들은 다음 경계를 명시적으로 인정한다:
- **모듈식 분리는 설계 가정이지 보장된 결과가 아니다**—표현 구현, 도구 교체, 구현체 간 적응을 통해 테스트되어야 하며, 논문은 검증을 제공하지 않는다.
- **예측적 잠재 표현의 물리적 내용은 직접 검사할 수 없다**—하위 작업 절제와 제어 실험을 통해 확립되어야 하며, 표현 자체에서 가정할 수 없다.
- **잠재 행동은 자동으로 로봇 행동이 아니다**—운동, 시점 변화 또는 기타 시각적 변화를 인코딩할 수 있으며, 특정 구현체 제어 공간과의 대응 관계는 학습되고 평가되어야 한다.
- **통일 아키텍처가 구현체 간 또는 제어 메커니즘에서 더 우수한지 여부는 아직 확립되지 않았다.**
- **자율 상호작용 데이터의 실용성은 궤적 품질, 결과 귀인, 모델 오류 강화를 방지하는 보호 장치에 달려 있다**—π₀.₇의 자율 데이터 규모는 공개적으로 명시되지 않았다.
- **인간 비디오는 카메라 운동, 부분 관측 가능성, 인간 특유의 운동학을 포함**하며, 목표 로봇 행동 공간에서 시간 정렬된 명령 흐름이 부족하다.
- **규모 자체로는 센싱, 행동 공간, 제어 주기, 작업 정의 또는 수집 프로토콜의 차이를 해결할 수 없다.**
- 그림 7-12의 연결 표현은 분석/설계 의존성일 뿐, 경험적으로 확립된 인과 효과가 아니다; 논문은 훈련 구성, 추론 주기 또는 하드웨어 세부 사항을 제공하지 않는다.

## 공학적 시사점

재현과 엔지니어링 선택에 대한 직접적인 지침:

1. **성능을 비교하기 전에 먼저 인터페이스 의미론을 확인하라**: 어떤 교차 시스템 비교든, 각 방법이 예측 시간 지평, 참조 프레임, 불확실성, 유효성 조건을 선언했는지 먼저 확인하라. 선언되지 않았다면 최종 작업 점수 비교는 무의미하다—한 시스템은 좁은 벤치마크 규칙성을 활용하고, 다른 시스템은 결과를 올바르게 예측하지만 제어기가 약할 수 있다.

2. **가장 쉽게 함정에 빠지는 곳: 잠재 표현의 '가짜 접지'**: 학습된 시각 토큰은 제어기가 해당 표현을 공유하거나 어댑터를 받지 않는 한 제어기에 조작적 의미가 없다. LAPA, UWM류 방법을 재현할 때는 시각 전환 코드와 로봇 행동 공간의 대응 관계가 명시적으로 학습되는지 반드시 확인하라—그렇지 않으면 '예측 성공'은 물리적 결과가 올바른 것이 아니라 시각적 유사성일 뿐이다.

3. **Trace Card는 디버깅에 유용하지만, 필드 설계가 성패를 결정한다**: 최소 필드 집합(관찰, 뇌 요청, 선택된 도구 체인, 검증기 출력, 제어기 상태, 결과)에서 시작하여 실패 귀인 능력을 먼저 검증한 후 확장하라. 필드가 너무 적으면 의도 오류와 제어 오류를 구분할 수 없고, 너무 많으면 주석 비용이 통제 불능이 된다.

4. **데이터 수집은 궤적만이 아니라 결정 맥락을 기록해야 한다**: 캘리브레이션, 참조 프레임, 행동 경계, 제어기 가정 또는 실패 주석이 없는 조작 궤적은 결과 모델링과 도구 교체에 약한 증거를 제공한다. BridgeData V2의 50365개 데모와 9731개 스크립트 rollout(표 내 수치로 계산)이 Embodiment Card를 첨부하지 않으면 재사용 가치가 크게 떨어진다.

5. **폐루프 학습은 승인 게이트를 설정해야 한다**: 후보 업데이트는 승격 전에 회귀 및 안전 게이트(예: LIBERO-Safety, ROBOSHACKLES의 안전 실패 검사)를 통과해야 한다. 그렇지 않으면 자율 상호작용 데이터가 모델 자체 오류를 강화한다—이것이 π₀.₇류 방법이 가장 경계해야 할 자기 강화 루프이다.
