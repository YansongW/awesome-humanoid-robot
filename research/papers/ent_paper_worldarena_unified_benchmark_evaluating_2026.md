---
$id: ent_paper_worldarena_unified_benchmark_evaluating_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models'
  zh: 'WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models'
  ko: 'WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models'
summary:
  en: While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental
    dynamics through action-conditioned prediction, their evaluation remains fragmented. Current evaluation of embodied world
    models has largely focused on perceptual fidelity (e.g., video generation quality), overlooking the functional utility
    of these models in downstream.
  zh: WorldArena 是一个面向具身世界模型（EWM）的统一基准，由研究团队提出，首次将感知质量评估与三种功能效用评估（数据引擎、策略评估器、动作规划器）整合于同一框架。核心贡献在于建立了一个包含 16 个客观指标、3 个闭环下游任务和人类主观评估的综合评测体系，并发布了
    EWMScore 聚合分数。
  ko: While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental
    dynamics through action-conditioned prediction, their evaluation remains fragmented. Current evaluation of embodied world
    models has largely focused on perceptual fidelity (e.g., video generation quality), overlooking the functional utility
    of these models in downstream.
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
- worldarena
- unified
- benchmark
- evaluating
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P116. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2602.08971 WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility'
  url: https://arxiv.org/abs/2602.08971
  date: '2026-02-09'
  accessed_at: '2026-08-05'
---

## 概述

WorldArena 是一个面向具身世界模型（EWM）的统一基准，由研究团队提出，首次将感知质量评估与三种功能效用评估（数据引擎、策略评估器、动作规划器）整合于同一框架。核心贡献在于建立了一个包含 16 个客观指标、3 个闭环下游任务和人类主观评估的综合评测体系，并发布了 EWMScore 聚合分数。

## 它改变了什么

现有具身世界模型评估的碎片化问题已经到了阻碍领域发展的程度：视频生成指标（如 FVD、IS）只能反映像素级保真度，却无法回答"这个模型能否帮助机器人学会操作"这一根本问题。此前虽有工作尝试用闭环动作执行来评估世界模型，但覆盖面仅限于单一角色，忽略了世界模型作为合成数据引擎、策略评估工具等更广泛的应用场景。

WorldArena 真正改变的是评估的"功能导向"——它不再问"视频像不像真的"，而是问"这个模型能不能当数据生成器、能不能当策略裁判、能不能当动作规划器"。这种转变将评估从视觉质量竞赛拉回到具身智能的实际需求，迫使研究者重新审视：一个在视频指标上表现优异的模型，是否真的具备可用的物理世界预测能力。

## 方法拆解

### 视频质量评估：六维十六指标
- **视觉质量**：MUSIQ 图像质量、LAION 美学预测、V-JEPA 特征分布的 MMD（二阶多项式核，α=40）
- **运动质量**：RAFT 光流动态程度（前 5% 活跃像素）、平均光流幅度、VFI-Mamba 帧插值平滑度
- **内容一致性**：DINO 主体一致性、CLIP 背景一致性、前后向光流往返扭曲的 AEPE
- **物理遵循**：Qwen3-VL 交互质量评分（1-5 分归一化）、SAM 3 轨迹提取后的 NDTW 距离
- **3D 准确性**：Depth-Anything 单目深度估计（中位数缩放对齐）、Qwen3-VL 透视性判断
- **可控性**：Qwen3-VL 指令遵循、Qwen2.5-VL 描述与 CLIP 编码的语义对齐、多指令生成视频的成对特征不相似度

### 具身任务评估：三种闭环角色
- **数据引擎**：两阶段训练——先在 RoboTwin 2.0 上微调世界模型生成合成视频，再冻结世界模型权重、集成逆动力学模型（IDM）提取动作，用合成数据训练 π0.5 策略模型
- **策略评估器**：训练五个不同能力的 π0.5 策略，与动作可控世界模型交互 rollout（超过真实视频帧数 20%），成功率由 VLM 判定，与 RoboTwin 模拟器结果比较相关性
- **动作规划器**：世界模型 + IDM 配对，输入文本指令和初始帧输出动作序列，在模拟器中执行并测量成功率

### 分数聚合
EWMScore 对 16 个指标采用经验边界线性归一化（99 百分位为最大值、1 百分位为最小值），映射至 [0,100] 后取算术平均。

## 关键创新

**功能效用与感知质量并重的评估范式**：此前基准要么只看视频质量，要么只看单一闭环任务。WorldArena 首次将三种功能角色（数据引擎、策略评估器、动作规划器）纳入统一框架，使评估结果能直接反映世界模型在真实机器人学习流程中的价值。

**VLM 作为物理合理性裁判**：用 Qwen3-VL 对交互质量、透视性、指令遵循进行 1-5 分 Likert 评分，并设计了容忍渲染伪影的策略成功判定协议（比较 GT 与生成帧的最终状态、手臂选择、动作意图）。这解决了传统指标无法捕捉的"物理常识错误"问题。

**交叉维度相关性分析**：图 5 显示 EWMScore 与人类判断强相关（Pearson r=0.825），但与数据合成性能中等相关（r=0.600）、与动作规划性能弱相关（r=0.360）。这一发现揭示了感知质量与功能效用之间的非对称关系，是此前工作未系统量化的。

## 实验与结果

**测试模型**：14 个代表性世界模型，涵盖通用视频模型（CogvideoX、Wan 2.2、Wan 2.6、Veo 3.1）、文本条件具身模型（Genie Envisioner、GigaWorld、TesserAct、Cosmos-Predict 2.5、WOW、RoboMaster、Vidar）和动作条件模型（IRASim、Cosmos-Predict 2.5 (action)、CtrlWorld）。

**视频质量评估关键结果**（表 2、表 3 节选）：

| 模型 | 图像质量 | JEPA相似性 | 交互质量 | 轨迹准确性 | 指令遵循 |
|------|---------|-----------|---------|-----------|---------|
| Wan 2.6 | 0.6824 | 0.7229 | 0.7280 | 0.1182 | 0.8536 |
| Veo 3.1 | 0.6605 | 0.5694 | 0.7872 | 0.1231 | 0.9328 |
| CtrlWorld | 0.3522 | 0.9185 | 0.6212 | 0.4766 | 0.7272 |
| Genie Envisioner | 0.2305 | 0.3340 | 0.2052 | 0.0679 | 0.2028 |

**数据引擎任务成功率**（表 4）：WoW 表现最佳（任务 1 为 45%、任务 2 为 71%），Genie Envisioner 最差（任务 1 为 7%、任务 2 为 21%）。真实数据训练的 π0.5 策略为任务 1 为 77%、任务 2 为 66%。

**动作规划器任务成功率**（表 5）：所有世界模型均显著低于真实数据训练的 π0.5 策略（任务 1 为 77%、任务 2 为 66%），WoW 相对最好（任务 1 为 20%、任务 2 为 21%）。

**策略评估器**：CtrlWorld 与 RoboTwin 模拟器评估结果强相关，Cosmos-Predict 2.5 相关性较弱；两个模型成功率均高于模拟器测量值。

**人类评估**：70 名标注者评估 3500 个视频。商业模型（Veo 3.1、Wan 2.6）在整体质量、指令遵循和物理遵循上得分最高；动作条件方法（CtrlWorld）比纯文本对应方法物理遵循和胜率更好。

## 边界与局限

作者明确承认：合成数据质量仍不足以有效训练策略，当前具身世界模型尚不可靠作为下游学习的数据源；世界模型在闭环任务执行中仍难以可靠支持长时程任务；合成数据尽管视觉保真度高，仍不足以提供强预测或决策相关信号用于复杂具身推理。感知真实感是获得良好人类评价的必要条件，但不直接转化为下游具身任务的成比例收益。

评估基于 RoboTwin 2.0 单一平台（50 个任务场景、2500 个视频），结论的泛化性受限于该模拟器的物理保真度和任务分布。策略评估器任务中 VLM 判定协议对"任务基本完成"的阈值定义存在主观性，不同 VLM 版本可能导致结果波动。论文未明确硬件配置和推理时间成本。

## 工程启示

复现时先核对归一化边界：表 6 的经验边界（如 Photometric Consistency 最大 6.7899、最小 0.1257）是基于 8 个模型生成视频的 99/1 百分位计算的，更换模型集合会改变边界值，导致跨论文分数不可直接比较。最易踩坑的是动作跟随指标——它要求对同一指令生成多个不同动作的视频，计算成对特征不相似度，若生成器对指令不敏感（如 Genie Envisioner 的 0.0109），该指标会严重低估模型能力。

下游团队选型建议：若目标是数据增强，优先考虑 WoW（数据引擎任务成功率最高）；若需要策略评估，CtrlWorld 与模拟器相关性最强；若追求视频质量与人类观感，直接选商业模型 Veo 3.1 或 Wan 2.6。注意动作条件模型（如 CtrlWorld）在物理遵循上系统性优于文本条件模型，但轨迹准确性指标（NDTW）对动作条件模型更友好，比较时需区分模型类型。

## Overview
While world models have emerged as a cornerstone of embodied intelligence by enabling agents to reason about environmental dynamics through action-conditioned prediction, their evaluation remains fragmented. Current evaluation of embodied world models has largely focused on perceptual fidelity (e.g., video generation quality), overlooking the functional utility of these models in downstream decision-making tasks. In this work, we introduce WorldArena, a unified benchmark designed to systematically evaluate embodied world models across both perceptual and functional dimensions. WorldArena assesses models through three dimensions: video perception quality, measured with 16 metrics across six sub-dimensions; embodied task functionality, which evaluates world models as data engines, policy evaluators, and action planners integrating with subjective human evaluation. Furthermore, we propose EWMScore, a holistic metric integrating multi-dimensional performance into a single interpretable index. Through extensive experiments on 14 representative models, we reveal a significant perception-functionality gap, showing that high visual quality does not necessarily translate into strong embodied task capability. WorldArena benchmark with the public leaderboard is released at https://world-arena.ai, providing a framework for tracking progress toward truly functional world models in embodied AI.

## 参考
- https://arxiv.org/abs/2602.08971

## 개요

WorldArena는 연구팀이 제안한 임베디드 월드 모델(EWM)을 위한 통합 벤치마크로, 지각 품질 평가와 세 가지 기능적 효용 평가(데이터 엔진, 정책 평가기, 행동 플래너)를 최초로 동일한 프레임워크에 통합했습니다. 핵심 기여는 16개의 객관적 지표, 3개의 폐루프 다운스트림 태스크, 인간 주관 평가를 포함하는 종합 평가 체계를 구축하고 EWMScore 집계 점수를 발표한 것입니다.

## 무엇을 바꾸었는가

기존 임베디드 월드 모델 평가의 파편화 문제는 분야 발전을 저해할 정도에 이르렀습니다: 비디오 생성 지표(예: FVD, IS)는 픽셀 수준의 충실도만 반영할 뿐, "이 모델이 로봇이 조작을 학습하는 데 도움이 될 수 있는가"라는 근본적인 질문에는 답할 수 없습니다. 이전에도 폐루프 행동 실행으로 월드 모델을 평가하려는 시도가 있었지만, 적용 범위가 단일 역할에 국한되어 월드 모델이 합성 데이터 엔진, 정책 평가 도구 등으로 사용되는 더 넓은 응용 시나리오를 간과했습니다.

WorldArena가 진정으로 바꾼 것은 평가의 "기능 지향성"입니다—더 이상 "비디오가 실제처럼 보이는가"를 묻지 않고, "이 모델이 데이터 생성기로 사용될 수 있는가, 정책 심판으로 사용될 수 있는가, 행동 플래너로 사용될 수 있는가"를 묻습니다. 이러한 전환은 평가를 시각적 품질 경쟁에서 임베디드 지능의 실제 요구로 되돌려 놓았으며, 연구자들이 비디오 지표에서 우수한 성능을 보이는 모델이 실제로 사용 가능한 물리적 세계 예측 능력을 갖추었는지 재검토하도록 강제합니다.

## 방법 분석

### 비디오 품질 평가: 6차원 16지표
- **시각적 품질**: MUSIQ 이미지 품질, LAION 미학 예측, V-JEPA 특징 분포의 MMD(2차 다항식 커널, α=40)
- **모션 품질**: RAFT 광학 흐름 역동성(상위 5% 활성 픽셀), 평균 광학 흐름 크기, VFI-Mamba 프레임 보간 평활도
- **내용 일관성**: DINO 객체 일관성, CLIP 배경 일관성, 전방/후방 광학 흐름 왕복 왜곡의 AEPE
- **물리적 준수**: Qwen3-VL 상호작용 품질 점수(1-5점 정규화), SAM 3 궤적 추출 후 NDTW 거리
- **3D 정확성**: Depth-Anything 단안 깊이 추정(중앙값 스케일링 정렬), Qwen3-VL 원근 판단
- **제어 가능성**: Qwen3-VL 명령 준수, Qwen2.5-VL 설명과 CLIP 인코딩의 의미 정렬, 다중 명령 생성 비디오의 쌍별 특징 비유사도

### 임베디드 태스크 평가: 세 가지 폐루프 역할
- **데이터 엔진**: 2단계 훈련—먼저 RoboTwin 2.0에서 월드 모델을 미세 조정하여 합성 비디오 생성, 이후 월드 모델 가중치를 동결하고 역동역학 모델(IDM)을 통합하여 행동 추출, 합성 데이터로 π0.5 정책 모델 훈련
- **정책 평가기**: 서로 다른 능력을 가진 5개의 π0.5 정책을 훈련하고, 행동 제어 가능한 월드 모델과 상호작용 rollout(실제 비디오 프레임 수보다 20% 초과), 성공률은 VLM이 판정하며 RoboTwin 시뮬레이터 결과와 상관관계 비교
- **행동 플래너**: 월드 모델 + IDM 페어링, 텍스트 명령과 초기 프레임을 입력으로 행동 시퀀스 출력, 시뮬레이터에서 실행하고 성공률 측정

### 점수 집계
EWMScore는 16개 지표에 대해 경험적 경계 선형 정규화(99 백분위수를 최대값, 1 백분위수를 최소값)를 적용하여 [0,100]으로 매핑한 후 산술 평균을 취합니다.

## 핵심 혁신

**기능 효용과 지각 품질을 동시에 중시하는 평가 패러다임**: 기존 벤치마크는 비디오 품질만 보거나 단일 폐루프 태스크만 보았습니다. WorldArena는 세 가지 기능적 역할(데이터 엔진, 정책 평가기, 행동 플래너)을 통합 프레임워크에 처음으로 포함시켜 평가 결과가 실제 로봇 학습 프로세스에서 월드 모델의 가치를 직접 반영할 수 있게 했습니다.

**VLM을 물리적 합리성 심판으로 사용**: Qwen3-VL로 상호작용 품질, 원근, 명령 준수를 1-5점 Likert 척도로 평가하고, 렌더링 아티팩트를 허용하는 정책 성공 판정 프로토콜(GT와 생성 프레임의 최종 상태, 팔 선택, 행동 의도 비교)을 설계했습니다. 이는 전통적 지표가 포착할 수 없는 "물리적 상식 오류" 문제를 해결합니다.

**교차 차원 상관관계 분석**: 그림 5는 EWMScore가 인간 판단과 강한 상관관계(Pearson r=0.825)를 보이지만, 데이터 합성 성능과는 중간 상관관계(r=0.600), 행동 계획 성능과는 약한 상관관계(r=0.360)를 보임을 보여줍니다. 이 발견은 지각 품질과 기능 효용 사이의 비대칭적 관계를 밝혀내며, 이전 연구에서 체계적으로 정량화되지 않았던 부분입니다.

## 실험 및 결과

**테스트 모델**: 14개의 대표적인 월드 모델로, 범용 비디오 모델(CogvideoX, Wan 2.2, Wan 2.6, Veo 3.1), 텍스트 조건 임베디드 모델(Genie Envisioner, GigaWorld, TesserAct, Cosmos-Predict 2.5, WOW, RoboMaster, Vidar), 행동 조건 모델(IRASim, Cosmos-Predict 2.5 (action), CtrlWorld)을 포함합니다.

**비디오 품질 평가 핵심 결과**(표 2, 표 3 발췌):

| 모델 | 이미지 품질 | JEPA 유사성 | 상호작용 품질 | 궤적 정확성 | 명령 준수 |
|------|---------|-----------|---------|-----------|---------|
| Wan 2.6 | 0.6824 | 0.7229 | 0.7280 | 0.1182 | 0.8536 |
| Veo 3.1 | 0.6605 | 0.5694 | 0.7872 | 0.1231 | 0.9328 |
| CtrlWorld | 0.3522 | 0.9185 | 0.6212 | 0.4766 | 0.7272 |
| Genie Envisioner | 0.2305 | 0.3340 | 0.2052 | 0.0679 | 0.2028 |

**데이터 엔진 태스크 성공률**(표 4): WoW가 가장 우수(태스크 1: 45%, 태스크 2: 71%), Genie Envisioner가 가장 낮음(태스크 1: 7%, 태스크 2: 21%). 실제 데이터로 훈련된 π0.5 정책은 태스크 1: 77%, 태스크 2: 66%.

**행동 플래너 태스크 성공률**(표 5): 모든 월드 모델이 실제 데이터로 훈련된 π0.5 정책(태스크 1: 77%, 태스크 2: 66%)보다 현저히 낮았으며, WoW가 상대적으로 가장 우수(태스크 1: 20%, 태스크 2: 21%).

**정책 평가기**: CtrlWorld가 RoboTwin 시뮬레이터 평가 결과와 강한 상관관계를 보였고, Cosmos-Predict 2.5는 상관관계가 약함; 두 모델 모두 성공률이 시뮬레이터 측정값보다 높았습니다.

**인간 평가**: 70명의 평가자가 3500개의 비디오를 평가했습니다. 상용 모델(Veo 3.1, Wan 2.6)이 전반적 품질, 명령 준수, 물리적 준수에서 가장 높은 점수를 받았습니다; 행동 조건 방법(CtrlWorld)이 순수 텍스트 대응 방법보다 물리적 준수와 승률이 더 좋았습니다.

## 경계와 한계

저자들은 명시적으로 인정합니다: 합성 데이터 품질은 여전히 정책을 효과적으로 훈련하기에 충분하지 않으며, 현재 임베디드 월드 모델은 다운스트림 학습의 데이터 소스로 신뢰할 수 없습니다; 월드 모델은 폐루프 태스크 실행에서 장기 태스크를 안정적으로 지원하기 어렵습니다; 합성 데이터는 시각적 충실도가 높음에도 불구하고 복잡한 임베디드 추론을 위한 강력한 예측 또는 의사 결정 관련 신호를 제공하기에 여전히 부족합니다. 지각적 사실감은 좋은 인간 평가를 얻기 위한 필요 조건이지만, 다운스트림 임베디드 태스크의 비례적 이득으로 직접 전환되지는 않습니다.

평가는 RoboTwin 2.0 단일 플랫폼(50개 태스크 시나리오, 2500개 비디오)을 기반으로 하며, 결론의 일반화 가능성은 해당 시뮬레이터의 물리적 충실도와 태스크 분포에 제한됩니다. 정책 평가기 태스크에서 VLM 판정 프로토콜의 "태스크 기본 완료" 임계값 정의에는 주관성이 존재하며, 다른 VLM 버전에 따라 결과가 변동될 수 있습니다. 논문은 하드웨어 구성과 추론 시간 비용을 명시하지 않았습니다.

## 엔지니어링 시사점

재현 시 먼저 정규화 경계를 확인하세요: 표 6의 경험적 경계(예: Photometric Consistency 최대 6.7899, 최소 0.1257)는 8개 모델 생성 비디오의 99/1 백분위수를 기반으로 계산되었으며, 모델 집합을 변경하면 경계값이 달라져 논문 간 점수를 직접 비교할 수 없습니다. 가장 함정에 빠지기 쉬운 지표는 행동 추종 지표입니다—동일한 명령에 대해 여러 다른 행동의 비디오를 생성하고 쌍별 특징 비유사도를 계산해야 하며, 생성기가 명령에 둔감한 경우(예: Genie Envisioner의 0.0109) 이 지표는 모델 능력을 심각하게 과소평가합니다.

다운스트림 팀 선택 권장 사항: 데이터 증강이 목표라면 WoW를 우선 고려(데이터 엔진 태스크 성공률 최고); 정책 평가가 필요하다면 CtrlWorld가 시뮬레이터와 상관관계가 가장 강함; 비디오 품질과 인간 관람감을 추구한다면 상용 모델 Veo 3.1 또는 Wan 2.6을 직접 선택하세요. 행동 조건 모델(예: CtrlWorld)이 물리적 준수에서 텍스트 조건 모델보다 체계적으로 우수하지만, 궤적 정확성 지표(NDTW)는 행동 조건 모델에 더 유리하므로 비교 시 모델 유형을 구분해야 합니다.
