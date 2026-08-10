---
$id: ent_paper_bayesian_framework_uncanny_valley_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Bayesian framework for the uncanny valley in humanoid robot design
  zh: A Bayesian framework for the uncanny valley in humanoid robot design
  ko: A Bayesian framework for the uncanny valley in humanoid robot design
summary:
  en: 'The uncanny valley is a long-standing empirical rule in humanoid robot design: making robots more human-like can reduce,
    rather than increase, affinity. Yet existing guidelines, such as adopting robot-like appearances, avoiding excessive realism,
    and reducing cross-modal mismatches, remain difficult to use for algorithmic design because they are not expressed as
    manipulable variables. Here, we.'
  zh: 本文提出一个层次贝叶斯生成模型，将仿人机器人的亲和度定义为后验加权的负类别条件惊奇，从而把恐怖谷经验法则转化为可计算的设计变量。作者来自东京大学，通过模拟与33名被试的行为实验验证了模型对预测不确定性与观测不确定性的预测，其中三个假设获支持、一个未获支持。
  ko: 'The uncanny valley is a long-standing empirical rule in humanoid robot design: making robots more human-like can reduce,
    rather than increase, affinity. Yet existing guidelines, such as adopting robot-like appearances, avoiding excessive realism,
    and reducing cross-modal mismatches, remain difficult to use for algorithmic design because they are not expressed as
    manipulable variables. Here, we.'
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
- bayesian
- framework
- uncanny
- valley
- humano
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
  title: arXiv:2607.13060 A Bayesian framework for the uncanny valley in humanoid robot design
  url: https://arxiv.org/abs/2607.13060
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一个层次贝叶斯生成模型，将仿人机器人的亲和度定义为后验加权的负类别条件惊奇，从而把恐怖谷经验法则转化为可计算的设计变量。作者来自东京大学，通过模拟与33名被试的行为实验验证了模型对预测不确定性与观测不确定性的预测，其中三个假设获支持、一个未获支持。

## 它改变了什么

恐怖谷研究长期停留在经验描述层面：Mori的曲线、Moore的贝叶斯类别感知模型、Ueyama的治疗应用，都没有把设计指南变成设计者能直接操作的变量。本文真正改变的是把“避免过度逼真”“减少跨模态不匹配”这类口号，翻译成四个可计算的量：与机器人类别预测均值的距离、跨模态不匹配度、预测不确定性、观测不确定性。这意味着恐怖谷从“事后解释现象”变成“事前预测曲线”的工程工具。

但本文的野心不止于形式化。它试图回答一个更尖锐的问题：既然恐怖谷不可避免，设计者能否通过操纵不确定性来“绕过”它？模拟显示，提高观测不确定性（如模糊化刺激）可以在中间拟人度区域显著提升亲和度，而提高预测不确定性则只在机器人样外观下有害。这直接挑战了“越清晰越好”的直觉，为设计提供了反直觉但可验证的策略。

## 方法拆解

### 生成模型
- 类别c∈{R,H}（机器人/人类）生成潜在人类相似度x，x再生成观测y：p(c,x,y)=p(c)p(x|c)p(y|x)
- 基线假设：p(x|c)=𝒩(x; μ_c, σ_c²)，p(y|x)=𝒩(y; x, σ_l²)，边际化得p(y|c)=𝒩(y; μ_c, σ_c²+σ_l²)

### 亲和度定义
- 类别条件惊奇：S_c(y)=−ln p(y|c)；类别条件亲和度：A_c(y)=ln p(y|c)
- 最终亲和度：A(y)=Σ_{c∈{R,H}} p(c|y)·A_c(y)，其中后验p(c|y)=π_c·exp{A_c(y)} / Σ_{c'}π_{c'}·exp{A_{c'}(y)}

### 四个设计变量
1. |y−μ_R|：与机器人类别预测均值的距离，操作化“第一峰值”指南
2. (y_a−y_m)²：跨模态感知不匹配，来自多模态扩展p(c,x,y_a,y_m)=p(c)p(x|c)p(y_a|x)p(y_m|x)
3. σ_R²：机器人类别预测不确定性，实验中映射为先验刺激模糊度
4. σ_l²：观测不确定性，实验中映射为评估刺激模糊度

### 关键设计决策
- 用后验加权而非简单平均，使亲和度在类别边界处平滑过渡
- 引入ϵ-floor似然p_ϵ(y|x)=[𝒩(y; x, σ_l²)+ϵ]/(1+ϵ)，避免高斯似然对极端预测误差过度惩罚；ϵ=0时退化为基线
- 多模态亲和度中，(y_a−y_m)²项显式编码跨模态不一致，D_c=σ_a²σ_m²+σ_a²σ_c²+σ_m²σ_c²

## 关键创新

1. **把恐怖谷从曲线变成函数**：首次将亲和度表达为可微的闭式表达式，设计变量直接对应模型参数，使“优化亲和度”成为可计算的优化问题，而非启发式调参。
2. **不确定性作为设计杠杆**：模拟与实验共同表明，观测不确定性σ_l²可以在中间拟人度区域显著提升亲和度（h=2至h=6均显著），这为“模糊化处理”提供了理论依据，而非仅凭直觉。
3. **多模态不匹配的显式编码**：通过共享潜在人类相似度x，将外观与运动的不一致量化为(y_a−y_m)²项，使跨模态设计指南首次获得解析表达。

## 实验与结果

被试内设计，33名成年人，8级拟人度×2预测不确定性×2观测不确定性共32条件。关键结果：

| 效应 | F值 | P值 | 结论 |
|------|-----|-----|------|
| 外观拟人度主效应 | 43.700 | <0.001 | 拟人度显著影响熟悉度 |
| 预测不确定性（先验模糊） | 4.486 | 0.034 | 弱模糊>强模糊，支持EH1-1 |
| 预测不确定性×拟人度 | 1.036 | 0.404 | 无交互，EH1-2未获支持 |
| 观测不确定性（评估模糊） | 53.187 | <0.001 | 强模糊>弱模糊，支持EH2 |
| 观测不确定性×拟人度 | 2.108 | 0.040 | 显著交互，支持EH3 |

简单主效应检验显示，高模糊评估刺激在h=2（F=6.031, P=0.015）、h=3（F=20.394, P<0.001）、h=4（F=20.933, P<0.001）、h=5（F=9.493, P=0.003）、h=6（F=8.989, P=0.003）显著提升熟悉度，而h=1、h=7、h=8不显著。四个假设中三个获支持，EH1-2未获支持，作者用ϵ-floor模型（ε=0.01）解释为基线模型可能高估了预测不确定性效应。

## 边界与局限

- EH1-2未获实验支持，且ϵ-floor模型仅“减弱”而非“消除”预测不确定性效应反转的预测，说明基线模型对σ_R²的效应量估计可能偏大
- 实验仅操作了σ_R²和σ_l²两个观测者侧变量，|y−μ_R|和(y_a−y_m)²未在实验中单独操纵
- 仅使用单模态外观刺激，多模态不匹配预测未经验证
- 样本量基于可行性与先前研究确定，未进行功效分析（论文未明确）
- 模型未涵盖真实机器人交互中的运动、声音、具身与情境因素，未做个性化参数拟合

## 工程启示

复现时先核对两个最容易出错的点：一是模糊操作的核大小与标准差（低模糊3×3、高模糊81×81，标准差均为−1），二是先验刺激与评估刺激必须使用相同模糊设置，否则预测不确定性操作会与观测不确定性混淆。统计上注意使用对齐秩变换（ART）而非标准ANOVA，因为部分条件违反正态性。

对下游设计团队，最可操作的结论是：在中间拟人度区域（h=2至h=6），提高观测不确定性（如哑光表面、柔和纹理、减少细节锐度）可以显著提升亲和度，且这一效应在h=3和h=4最强（F值超过20）。但不要指望通过模糊先验刺激来提升中间拟人度区域的亲和度——EH1-2的失败提示这条路径可能无效。多模态不匹配的预测虽未实验验证，但模型给出的(y_a−y_m)²项值得在真实机器人上做对照测试。

## Overview
The uncanny valley is a long-standing empirical rule in humanoid robot design: making robots more human-like can reduce, rather than increase, affinity. Yet existing guidelines, such as adopting robot-like appearances, avoiding excessive realism, and reducing cross-modal mismatches, remain difficult to use for algorithmic design because they are not expressed as manipulable variables. Here, we propose a hierarchical Bayesian generative model that operationalizes these guidelines as mathematical design variables. The model represents affinity toward humanoid robots as posterior-weighted negative category-conditional surprise and explains category ambiguity and perceptual mismatch as increases in surprise. It maps uncanny-valley mechanisms onto four variables: deviation from the predicted robot-category mean, inconsistency in human likeness across modalities, prediction uncertainty, and observational uncertainty. Simulations showed that category ambiguity and appearance--motion mismatch can produce affinity reductions, and that uncertainty reshapes the valley. In a human-subject experiment with robot--human morphing images, we manipulated prediction uncertainty using blurred prior robot stimuli and observational uncertainty using blurred evaluation stimuli. Increased observational uncertainty attenuated the decrease in familiarity ratings at intermediate human likeness, whereas low prediction uncertainty increased ratings for robot-like appearances. This framework turns empirical uncanny-valley heuristics into a computational basis for algorithmically evaluating and optimizing humanoid robot appearance and behavior.

## 参考
- https://arxiv.org/abs/2607.13060

## 개요

본 논문은 인간형 로봇의 친화도를 사후 가중 음의 범주 조건부 서프라이즈로 정의하는 계층적 베이즈 생성 모델을 제안하여, 언캐니 밸리 경험칙을 계산 가능한 설계 변수로 전환한다. 저자는 도쿄 대학 소속이며, 시뮬레이션과 33명의 피험자 행동 실험을 통해 예측 불확실성과 관측 불확실성에 대한 모델의 예측을 검증했으며, 세 가지 가설은 지지되고 하나는 지지되지 않았다.

## 그것이 바꾸는 것

언캐니 밸리 연구는 오랫동안 경험적 기술 수준에 머물러 있었다. Mori의 곡선, Moore의 베이즈 범주 지각 모델, Ueyama의 치료적 적용 모두 설계 지침을 설계자가 직접 조작할 수 있는 변수로 만들지 못했다. 본 논문이 실제로 바꾸는 것은 "과도한 사실성 회피", "교차 양상 불일치 감소"와 같은 구호를 네 가지 계산 가능한 양, 즉 로봇 범주 예측 평균과의 거리, 교차 양상 불일치도, 예측 불확실성, 관측 불확실성으로 번역한 것이다. 이는 언캐니 밸리를 "사후 현상 설명"에서 "사전 곡선 예측"의 공학적 도구로 전환함을 의미한다.

그러나 본 논문의 야망은 형식화에 그치지 않는다. 더 날카로운 질문에 답하려 한다. 언캐니 밸리가 불가피하다면, 설계자가 불확실성을 조작하여 이를 "우회"할 수 있는가? 시뮬레이션은 관측 불확실성(예: 자극 흐림)을 높이면 중간 인간 유사도 영역에서 친화도가 유의미하게 향상될 수 있음을 보여주는 반면, 예측 불확실성을 높이는 것은 로봇 같은 외관에서만 해로웠다. 이는 "선명할수록 좋다"는 직관에 직접 도전하며, 반직관적이지만 검증 가능한 설계 전략을 제공한다.

## 방법 분해

### 생성 모델
- 범주 c∈{R,H}(로봇/인간)가 잠재 인간 유사도 x를 생성하고, x가 다시 관측 y를 생성한다: p(c,x,y)=p(c)p(x|c)p(y|x)
- 기준 가정: p(x|c)=𝒩(x; μ_c, σ_c²), p(y|x)=𝒩(y; x, σ_l²), 주변화하면 p(y|c)=𝒩(y; μ_c, σ_c²+σ_l²)

### 친화도 정의
- 범주 조건부 서프라이즈: S_c(y)=−ln p(y|c); 범주 조건부 친화도: A_c(y)=ln p(y|c)
- 최종 친화도: A(y)=Σ_{c∈{R,H}} p(c|y)·A_c(y), 여기서 사후 p(c|y)=π_c·exp{A_c(y)} / Σ_{c'}π_{c'}·exp{A_{c'}(y)}

### 네 가지 설계 변수
1. |y−μ_R|: 로봇 범주 예측 평균과의 거리, "첫 번째 피크" 지침을 조작화
2. (y_a−y_m)²: 교차 양상 지각 불일치, 다중 양상 확장 p(c,x,y_a,y_m)=p(c)p(x|c)p(y_a|x)p(y_m|x)에서 유래
3. σ_R²: 로봇 범주 예측 불확실성, 실험에서 선험적 자극 흐림도로 매핑
4. σ_l²: 관측 불확실성, 실험에서 평가 자극 흐림도로 매핑

### 핵심 설계 결정
- 단순 평균 대신 사후 가중을 사용하여 범주 경계에서 친화도가 매끄럽게 전이되도록 함
- ϵ-floor 우도 p_ϵ(y|x)=[𝒩(y; x, σ_l²)+ϵ]/(1+ϵ)를 도입하여 가우시안 우도가 극단적 예측 오차를 과도하게 처벌하는 것을 방지; ϵ=0이면 기준 모델로 퇴화
- 다중 양상 친화도에서 (y_a−y_m)² 항이 교차 양상 불일치를 명시적으로 부호화하며, D_c=σ_a²σ_m²+σ_a²σ_c²+σ_m²σ_c²

## 핵심 혁신

1. **언캐니 밸리를 곡선에서 함수로 전환**: 처음으로 친화도를 미분 가능한 폐쇄형 표현식으로 제시하고, 설계 변수가 모델 파라미터에 직접 대응하여 "친화도 최적화"를 휴리스틱 파라미터 튜닝이 아닌 계산 가능한 최적화 문제로 만든다.
2. **불확실성을 설계 레버로 활용**: 시뮬레이션과 실험이 공통적으로 관측 불확실성 σ_l²이 중간 인간 유사도 영역(h=2~h=6 모두 유의)에서 친화도를 유의미하게 향상시킬 수 있음을 보여주며, 이는 직관에만 의존하지 않는 "흐림 처리"의 이론적 근거를 제공한다.
3. **교차 양상 불일치의 명시적 부호화**: 공유 잠재 인간 유사도 x를 통해 외관과 운동의 불일치를 (y_a−y_m)² 항으로 정량화하여, 교차 양상 설계 지침에 처음으로 해석적 표현을 부여한다.

## 실험 및 결과

피험자 내 설계, 33명의 성인, 8단계 인간 유사도×2 예측 불확실성×2 관측 불확실성 총 32조건. 주요 결과:

| 효과 | F값 | P값 | 결론 |
|------|-----|-----|------|
| 외관 인간 유사도 주효과 | 43.700 | <0.001 | 인간 유사도가 친숙도에 유의미한 영향 |
| 예측 불확실성(선험적 흐림) | 4.486 | 0.034 | 약한 흐림>강한 흐림, EH1-1 지지 |
| 예측 불확실성×인간 유사도 | 1.036 | 0.404 | 상호작용 없음, EH1-2 미지지 |
| 관측 불확실성(평가 흐림) | 53.187 | <0.001 | 강한 흐림>약한 흐림, EH2 지지 |
| 관측 불확실성×인간 유사도 | 2.108 | 0.040 | 유의미한 상호작용, EH3 지지 |

단순 주효과 검정은 높은 흐림 평가 자극이 h=2(F=6.031, P=0.015), h=3(F=20.394, P<0.001), h=4(F=20.933, P<0.001), h=5(F=9.493, P=0.003), h=6(F=8.989, P=0.003)에서 친숙도를 유의미하게 향상시킨 반면, h=1, h=7, h=8에서는 유의하지 않음을 보여주었다. 네 가지 가설 중 세 가지가 지지되었고 EH1-2는 지지되지 않았으며, 저자는 ϵ-floor 모델(ε=0.01)로 기준 모델이 예측 불확실성 효과를 과대 추정했을 수 있다고 설명한다.

## 경계 및 한계

- EH1-2는 실험적 지지를 받지 못했고, ϵ-floor 모델은 예측 불확실성 효과 반전 예측을 "제거"가 아닌 "약화"만 하므로 기준 모델의 σ_R² 효과 크기 추정이 과대할 수 있음
- 실험은 σ_R²와 σ_l² 두 관찰자 측 변수만 조작했으며, |y−μ_R|와 (y_a−y_m)²는 실험에서 개별적으로 조작되지 않음
- 단일 양상 외관 자극만 사용하여 다중 양상 불일치 예측은 검증되지 않음
- 표본 크기는 실행 가능성과 이전 연구에 기반하여 결정되었으며, 검정력 분석은 수행되지 않음(논문에 명시되지 않음)
- 모델은 실제 로봇 상호작용의 운동, 소리, 체화, 상황 요인을 포함하지 않으며, 개인화 파라미터 피팅도 수행되지 않음

## 공학적 시사점

재현 시 가장 오류가 발생하기 쉬운 두 지점을 먼저 확인해야 한다. 첫째는 흐림 연산의 커널 크기와 표준 편차(낮은 흐림 3×3, 높은 흐림 81×81, 표준 편차는 모두 −1)이고, 둘째는 선험적 자극과 평가 자극이 반드시 동일한 흐림 설정을 사용해야 한다는 점이다. 그렇지 않으면 예측 불확실성 조작이 관측 불확실성과 혼동된다. 통계적으로는 일부 조건이 정규성을 위반하므로 표준 ANOVA 대신 정렬 순위 변환(ART)을 사용해야 한다.

하위 설계 팀에게 가장 실행 가능한 결론은 중간 인간 유사도 영역(h=2~h=6)에서 관측 불확실성을 높이면(예: 무광택 표면, 부드러운 질감, 세부 선명도 감소) 친화도를 유의미하게 향상시킬 수 있으며, 이 효과는 h=3과 h=4에서 가장 강하다(F값 20 초과)는 것이다. 그러나 선험적 자극을 흐리게 하여 중간 인간 유사도 영역의 친화도를 높이는 것은 기대하지 말아야 한다. EH1-2의 실패는 이 경로가 무효일 수 있음을 시사한다. 다중 양상 불일치 예측은 실험적으로 검증되지 않았지만, 모델이 제시한 (y_a−y_m)² 항은 실제 로봇에서 대조 테스트를 수행할 가치가 있다.
