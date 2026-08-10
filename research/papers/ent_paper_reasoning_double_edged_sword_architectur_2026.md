---
$id: ent_paper_reasoning_double_edged_sword_architectur_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models'
  zh: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models'
  ko: 'Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models'
summary:
  en: Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy
    that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions.
    We test this premise head-on across three models that span the reasoning spectrum (no reasoning, a text chain-of-thought,
    and a latent iterative loop),.
  zh: 本文系统比较了三种推理架构的视觉-语言-动作（VLA）模型在跨阶段扰动下的鲁棒性，发现推理设计是决定脆弱性的主导因素：潜在迭代推理（RD-VLA）在视觉噪声下崩溃至14.8%成功率，而文本链式思维（DT）和无推理（OFT）保持约90%。作者进一步证明推理放大是结构性而非乘法累积的，并揭示基于计划一致性的运行时监控器在自适应攻击下失效。
  ko: Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy
    that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions.
    We test this premise head-on across three models that span the reasoning spectrum (no reasoning, a text chain-of-thought,
    and a latent iterative loop),.
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
- reasoning
- double
- edged
- sword
- architectur
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
  title: 'arXiv:2607.17786 Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vi'
  url: https://arxiv.org/abs/2607.17786
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

本文系统比较了三种推理架构的视觉-语言-动作（VLA）模型在跨阶段扰动下的鲁棒性，发现推理设计是决定脆弱性的主导因素：潜在迭代推理（RD-VLA）在视觉噪声下崩溃至14.8%成功率，而文本链式思维（DT）和无推理（OFT）保持约90%。作者进一步证明推理放大是结构性而非乘法累积的，并揭示基于计划一致性的运行时监控器在自适应攻击下失效。

## 它改变了什么

这项工作的真正贡献在于把VLA鲁棒性研究从“黑盒成功率对比”推进到“阶段级机制归因”。此前LIBERO-Plus等基准只报告整体性能下降，无法回答扰动在视觉编码、推理、动作解码各阶段如何传播。作者用跨阶段攻击矩阵（一次只扰动一个阶段）隔离出推理阶段作为关键放大节点，这改变了我们对“推理是否有助于鲁棒性”的认知——直觉上推理应帮助模型吸收噪声，但结果显示推理类型决定了脆弱性方向：文本推理（DT）在视觉攻击下优于无推理（OFT）约27.7个百分点（FGSM ε=8/255），而潜在迭代推理（RD-VLA）反而比两者脆弱一个数量级。

更重要的改变在于对“推理放大机制”的证伪。作者通过K-sweep测试（K∈{4,8,12}）直接检验“每迭代乘法放大”假设，发现放大比ρ(K)几乎不随深度变化（ρ(12)/ρ(8)=1.005，而乘法预测为2.0），从而将机制从“深度累积”修正为“结构性放大”——即放大发生在推理阶段的入口而非循环内部。这一区分对防御设计有直接含义：与其减少推理深度，不如平滑编码器输出或稳定不动点。

## 方法拆解

### 模型谱系与攻击矩阵
- **OpenVLA-OFT**：无推理，7B参数，Prismatic骨干（SigLIP+DINOv2），MLPResNet动作头（4层：28672→4096→4096→4096→7），输出 a_t ∈ ℝ⁷
- **DeepThinkVLA (DT)**：文本CoT，3B参数，PaliGemma骨干，离散动作token（2048 bins），输出 a_t ∈ ℝ⁷
- **RD-VLA**：潜在迭代推理，K=12权重共享循环，0.5B参数，Prismatic骨干，线性投影 7×896，输出 a_t ∈ ℝ⁷

### 跨阶段攻击设计
- **视觉阶段**：FGSM（ε∈{2,4,8,16,32}/255）、高斯噪声（σ∈{0.01,0.02,0.05,0.1,0.2}）、PGD-10（L∞，步长ε/4，ε∈{4,8,16}/255）
- **推理阶段（仅DT）**：实体交换CoT损坏——将CoT中任务相关对象替换为LIBERO 29对象词汇表中的随机替代物，保持句法良好但反转动作目标
- **动作阶段**：7-DOF输出加性高斯噪声（不含夹爪），σ∈{0.01,0.05,0.1,0.5,1.0}

### 关键分析工具
- **放大比**：ρ = ‖a_pert − a_clean‖₂ / ε（式5）
- **K-sweep证伪**：自由截距对数线性拟合 ρ(K)=48.507·1.0007^K，MAFE 0.1%，直接拒绝乘法假设
- **一致性探针**：s = w_e·S_entity + w_d·S_direction + w_g·S_gripper + w_p·S_parse，权重(0.5, 0.2, 0.15, 0.15)
- **阶段融合监控器**：s_t = α·(1−φ_t) + (1−α)·ψ_t，α∈[0,1]，阈值τ通过留一种子交叉验证校准至8%干净情节级假阳性率

### 混淆控制
- RD-VLA与OFT共享Prismatic骨干，排除骨干差异
- DT的CoT禁用消融（空CoT）保持骨干、规模、动作头恒定，TOST等价检验将CoT效应置于±5 pp内
- RD-VLA输出投影谱范数σ₁=0.091（收缩），排除动作头放大

## 关键创新

**1. 跨阶段攻击矩阵作为诊断工具**：这是首次将VLA鲁棒性分析分解到视觉、推理、动作三个阶段，而非整体黑盒评估。通过一次只扰动一个阶段，作者能明确归因脆弱性来源——例如RD-VLA在视觉噪声σ=0.2下崩溃至14.8%，而DT和OFT保持约90%，证明脆弱性源于推理阶段而非视觉编码。

**2. K-sweep证伪乘法放大假设**：通过推理时变化K∈{4,8,12}（无需重训练，利用循环的num_iter标志），直接检验“每迭代放大19.2%”的预测。实测ρ(12)/ρ(8)=1.005，与乘法预测2.0矛盾，将机制修正为结构性放大——放大在推理入口一次性发生，而非随深度累积。这一发现改变了防御设计方向：不应减少推理深度，而应平滑编码器输出或稳定不动点。

**3. 计划-动作一致性探针及其失效分析**：利用DT显式CoT作为运行时安全检查，探针在朴素实体交换攻击下AUC达0.996，但在自适应隐身攻击下崩溃至0.493（机会水平）。这揭示了基于语义一致性的防御根本局限：攻击者只需将实体替换为原始指令对象即可绕过检测，同时保持任务破坏力（−8 pp SR）。这一结果为防御研究划定了边界——任何依赖可读计划一致性的监控器都可被自适应攻击者规避。

## 实验与结果

### 干净与攻击下成功率（SR%，N=12，LIBERO 4套件×3种子）

| 条件 | OpenVLA-OFT | DeepThinkVLA | RD-VLA |
|---|---|---|---|
| 干净 | 96.5 | 93.0 | 89.2 |
| 高斯 σ=0.2 | 89.0 | 92.7 | 14.8 |
| FGSM ε=8/255 | 83.5 | 55.8 | 65.2（迁移） |
| PGD-10 ε=8/255 | 18.2 | 49.8 | 0.0 |

### 关键对比
- **DT vs OFT（高斯σ=0.2）**：92.7 vs 89.0，p=0.30，d=0.87——文本推理不显著优于无推理
- **RD-VLA vs 两者（高斯σ=0.2）**：14.8 vs 约90，p<0.01，d=6.5——潜在迭代推理脆弱一个数量级
- **放大比**：ρ_RD-VLA/ρ_OFT=8.22（σ=0.2），由反解L̂_iter=1.192（每迭代约19.2%放大）
- **K-sweep**：ρ(8)=48.70，ρ(12)=48.96，SE≤0.6；自由截距拟合ρ(K)=48.507·1.0007^K，MAFE 0.1%——乘法预测2.0被拒绝
- **一致性探针AUC**：朴素实体交换0.996 → 自适应隐身0.493 → 完全自适应0.259
- **阶段融合监控器（DT，PGD-10 ε=8/255）**：α=0时防御SR 42.2%（Δ=−7.7 pp），α=1时48.8%（Δ=−1.0 pp）——融合监控器在最佳配置下仅恢复1.0 pp
- **检查器感知自适应PGD-10**：最坏情况防御SR降至object 46.0%、spatial 50.7%，均低于同攻击下未防御SR——监控器在自适应攻击下不仅无效反而有害

### 结果含义
- 推理类型（而非规模或骨干）是鲁棒性主导因素：RD-VLA（0.5B）比OFT（7B）脆弱9.9倍（σ=0.2），但DT（3B）与OFT（7B）无显著差异
- 放大是结构性的：K-sweep显示深度不放大扰动，放大发生在推理入口
- 基于计划一致性的防御在自适应攻击下彻底失效：隐身攻击将探针标记率从98.9%降至5.5%，与6.3%干净假阳性率不可区分

## 边界与局限

- **每个推理范式仅由一个模型代表**（N=3），骨干、规模、训练数据与推理家族混淆；范式级陈述实为模型级观察
- **仅限LIBERO模拟**，SimplerEnv仅作单一架构健全性检查；sim-to-real迁移未解决
- **推理阶段损坏仅限文本CoT**：RD-VLA无可寻址推理面，OFT无推理阶段；视觉推理（CoT-VLA）不在研究范围内
- **不扰动自然语言指令本身**：指令级攻击（改写、提示注入）形成独立威胁类别
- **EOT测试T=2**，低于文献规范T∈{8,16}；曲率结论经100查询Square Attack交叉检查但非无懈可击
- **CoT禁用消融将推理文本设为零token**，相对于分布内skip-CoT比较器为离流形，±5 pp等价界为保守解读
- **阶段融合监控器为事后评估**，自适应评估仅覆盖针对动作异常项的攻击者，未与文本一致性项联合
- **噪声过滤贡献低于功率阈值**（N=12，最小可检测效应d≈0.85）；自然测试是更高N的复制实验
- **作者明确不提出防御方法**，将结果定性为防御工作的前提条件而非no-go定理

## 工程启示

- **复现时先核对统计配置**：每条件N=12（4套件×3种子），每单元50集（10任务×5试验）；配对Wilcoxon符号秩检验+Holm-Bonferroni校正（13检验家族）；bootstrap CI（n=10000）。若你的N不同，最小可检测效应d≈0.85将不适用
- **RD-VLA白盒PGD-10需梯度检查点**：通过K=12循环反向传播，峰值3.5 GB（A100-40GB）；FGSM单元格是DT→RD-VLA迁移攻击，仅提供白盒脆弱性下界
- **最容易踩坑的是K-sweep实现**：需利用循环的num_iter标志在推理时变化K∈{4,8,12}，无需重训练；若你的模型不支持动态深度，此证伪实验无法复现
- **一致性探针的实体提取**：使用完整LIBERO 29对象词汇表，最长优先子串匹配；方向关键词（left, right, up, down, forward, backward, toward, away）和夹爪关键词（open, close, grasp, release, grip, pick, place）需精确匹配
- **阈值τ=0.7从阈值扫描选取**（τ=0.5：84% TPR/0% FPR；τ=0.7：100%/0%；τ=0.9：100%/95%）；无匹配FPR校准的基线会在40–67%干净情节上弃权
- **下游团队若考虑部署基于计划一致性的监控器**：务必先测试自适应隐身攻击（实体交换+重新注入原始指令对象），其可将AUC从0.996降至0.493，标记率从98.9%降至5.5%——朴素一致性检查在对抗环境下不可靠
- **计算预算参考**：总约635 GPU小时（909实验，0失败）；FGSM每episode约2.5倍干净推理，PGD-10约10倍；RD-VLA PGD-10额外约35 GPU小时

## Overview
Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions. We test this premise head-on across three models that span the reasoning spectrum (no reasoning, a text chain-of-thought, and a latent iterative loop), perturbing each at the vision, reasoning, and action stages on LIBERO and SimplerEnv. Two questions organize the study: does the reasoning design shift robustness, and can the reasoning be read back at runtime as a safety signal? We find that the latent-iterative model is by far the least robust: under both stochastic noise and white-box perturbation its task success collapses, while the other two hold. This fragility is structural rather than cumulative: varying the reasoning depth at inference barely moves it. Reasoning outputs can in principle be monitored, but the monitors fail under fair tests. A plan--action consistency probe that looks near-perfect under naive evaluation falls to chance under adaptive attack. Under matched-FPR calibration, fusing it with an action-anomaly probe never lifts defended success above undefended. Scoped to these output-level behavioral probes under white-box vision-stage attack, this ceiling is a precondition that any viable defense must first satisfy.

## 参考
- https://arxiv.org/abs/2607.17786

## 개요

본 논문은 세 가지 추론 아키텍처의 시각-언어-행동(VLA) 모델이 교차 단계 교란(cross-stage perturbation) 하에서 보이는 강건성을 체계적으로 비교하며, 추론 설계가 취약성을 결정하는 지배적 요인임을 발견했다. 잠재 반복 추론(RD-VLA)은 시각적 노이즈 하에서 14.8% 성공률로 붕괴한 반면, 텍스트 체인오브생각(DT)과 무추론(OFT)은 약 90%를 유지했다. 저자들은 나아가 추론 증폭이 구조적이며 곱셈적 누적이 아님을 증명하고, 계획 일관성 기반 런타임 모니터가 적응형 공격 하에서 무력화됨을 밝혔다.

## 그것이 바꾸는 것

이 작업의 진정한 기여는 VLA 강건성 연구를 "블랙박스 성공률 비교"에서 "단계별 메커니즘 귀인"으로 전환한 데 있다. 기존 LIBERO-Plus 등의 벤치마크는 전체 성능 저하만 보고할 뿐, 교란이 시각 인코딩, 추론, 행동 디코딩 각 단계에서 어떻게 전파되는지 답할 수 없었다. 저자들은 교차 단계 공격 행렬(한 번에 한 단계만 교란)을 사용해 추론 단계를 핵심 증폭 노드로 분리했으며, 이는 "추론이 강건성에 도움이 되는가"에 대한 인식을 바꾼다. 직관적으로 추론은 모델이 노이즈를 흡수하도록 도와야 하지만, 결과는 추론 유형이 취약성의 방향을 결정함을 보여준다. 텍스트 추론(DT)은 시각 공격 하에서 무추론(OFT)보다 약 27.7% 포인트 우수했지만(FGSM ε=8/255), 잠재 반복 추론(RD-VLA)은 오히려 둘보다 한 자릿수 더 취약했다.

더 중요한 변화는 "추론 증폭 메커니즘"의 반증에 있다. 저자들은 K-sweep 테스트(K∈{4,8,12})를 통해 "반복당 곱셈 증폭" 가설을 직접 검증했고, 증폭비 ρ(K)가 깊이에 따라 거의 변하지 않음을 발견했다(ρ(12)/ρ(8)=1.005, 곱셈 예측은 2.0). 이를 통해 메커니즘을 "깊이 누적"에서 "구조적 증폭"으로 수정했다. 즉, 증폭은 순환 내부가 아닌 추론 단계의 진입점에서 발생한다. 이 구분은 방어 설계에 직접적인 함의를 가진다. 추론 깊이를 줄이는 대신 인코더 출력을 평활화하거나 고정점을 안정화해야 한다.

## 방법 분해

### 모델 계보와 공격 행렬
- **OpenVLA-OFT**: 무추론, 7B 파라미터, Prismatic 백본(SigLIP+DINOv2), MLPResNet 행동 헤드(4층: 28672→4096→4096→4096→7), 출력 a_t ∈ ℝ⁷
- **DeepThinkVLA (DT)**: 텍스트 CoT, 3B 파라미터, PaliGemma 백본, 이산 행동 토큰(2048 bins), 출력 a_t ∈ ℝ⁷
- **RD-VLA**: 잠재 반복 추론, K=12 가중치 공유 순환, 0.5B 파라미터, Prismatic 백본, 선형 투영 7×896, 출력 a_t ∈ ℝ⁷

### 교차 단계 공격 설계
- **시각 단계**: FGSM(ε∈{2,4,8,16,32}/255), 가우시안 노이즈(σ∈{0.01,0.02,0.05,0.1,0.2}), PGD-10(L∞, 스텝 ε/4, ε∈{4,8,16}/255)
- **추론 단계(DT만 해당)**: 엔티티 교체 CoT 손상 — CoT 내 작업 관련 객체를 LIBERO 29개 객체 어휘에서 무작위 대체물로 교체, 문법은 유지하되 행동 목표를 반전
- **행동 단계**: 7-DOF 출력에 가산성 가우시안 노이즈(그리퍼 제외), σ∈{0.01,0.05,0.1,0.5,1.0}

### 핵심 분석 도구
- **증폭비**: ρ = ‖a_pert − a_clean‖₂ / ε (식 5)
- **K-sweep 반증**: 자유 절편 로그-선형 피팅 ρ(K)=48.507·1.0007^K, MAFE 0.1%, 곱셈 가설을 직접 기각
- **일관성 프로브**: s = w_e·S_entity + w_d·S_direction + w_g·S_gripper + w_p·S_parse, 가중치(0.5, 0.2, 0.15, 0.15)
- **단계 융합 모니터**: s_t = α·(1−φ_t) + (1−α)·ψ_t, α∈[0,1], 임계값 τ는 leave-one-seed 교차 검증을 통해 8% 클린 에피소드 수준 거짓 양성률로 보정

### 혼동 통제
- RD-VLA와 OFT는 Prismatic 백본을 공유하여 백본 차이를 배제
- DT의 CoT 비활성화 절제(빈 CoT)는 백본, 규모, 행동 헤드를 일정하게 유지, TOST 동등성 검정은 CoT 효과를 ±5 pp 이내로 제한
- RD-VLA 출력 투영 스펙트럼 노름 σ₁=0.091(수축), 행동 헤드 증폭 배제

## 핵심 혁신

**1. 교차 단계 공격 행렬을 진단 도구로 사용**: 이는 VLA 강건성 분석을 전체 블랙박스 평가가 아닌 시각, 추론, 행동의 세 단계로 분해한 최초의 시도다. 한 번에 한 단계만 교란함으로써 저자들은 취약성의 원인을 명확히 귀인할 수 있다. 예를 들어 RD-VLA는 시각 노이즈 σ=0.2에서 14.8%로 붕괴하는 반면 DT와 OFT는 약 90%를 유지하며, 이는 취약성이 시각 인코딩이 아닌 추론 단계에서 비롯됨을 증명한다.

**2. K-sweep을 통한 곱셈 증폭 가설 반증**: 추론 시 K∈{4,8,12}를 변화시켜(재훈련 불필요, 순환의 num_iter 플래그 활용) "반복당 19.2% 증폭" 예측을 직접 검증했다. 실측 ρ(12)/ρ(8)=1.005는 곱셈 예측 2.0과 모순되며, 메커니즘을 구조적 증폭으로 수정한다. 즉, 증폭은 추론 진입점에서 한 번에 발생하며 깊이에 따라 누적되지 않는다. 이 발견은 방어 설계 방향을 바꾼다. 추론 깊이를 줄이는 대신 인코더 출력을 평활화하거나 고정점을 안정화해야 한다.

**3. 계획-행동 일관성 프로브와 그 실패 분석**: DT의 명시적 CoT를 런타임 안전 검사로 활용, 프로브는 단순 엔티티 교체 공격에서 AUC 0.996을 달성했지만 적응형 은닉 공격에서는 0.493(확률 수준)으로 붕괴했다. 이는 의미적 일관성 기반 방어의 근본적 한계를 드러낸다. 공격자는 엔티티를 원래 지시 객체로 교체하기만 하면 탐지를 우회하면서도 작업 파괴력(−8 pp SR)을 유지할 수 있다. 이 결과는 방어 연구의 경계를 설정한다. 가독 가능한 계획 일관성에 의존하는 모든 모니터는 적응형 공격자에 의해 우회될 수 있다.

## 실험과 결과

### 클린 및 공격 하 성공률(SR%, N=12, LIBERO 4개 스위트×3개 시드)

| 조건 | OpenVLA-OFT | DeepThinkVLA | RD-VLA |
|---|---|---|---|
| 클린 | 96.5 | 93.0 | 89.2 |
| 가우시안 σ=0.2 | 89.0 | 92.7 | 14.8 |
| FGSM ε=8/255 | 83.5 | 55.8 | 65.2(전이) |
| PGD-10 ε=8/255 | 18.2 | 49.8 | 0.0 |

### 핵심 비교
- **DT vs OFT(가우시안 σ=0.2)**: 92.7 vs 89.0, p=0.30, d=0.87 — 텍스트 추론은 무추론보다 유의미하게 우수하지 않음
- **RD-VLA vs 둘 다(가우시안 σ=0.2)**: 14.8 vs 약 90, p<0.01, d=6.5 — 잠재 반복 추론은 한 자릿수 더 취약
- **증폭비**: ρ_RD-VLA/ρ_OFT=8.22(σ=0.2), 역산 L̂_iter=1.192(반복당 약 19.2% 증폭)
- **K-sweep**: ρ(8)=48.70, ρ(12)=48.96, SE≤0.6; 자유 절편 피팅 ρ(K)=48.507·1.0007^K, MAFE 0.1% — 곱셈 예측 2.0 기각
- **일관성 프로브 AUC**: 단순 엔티티 교체 0.996 → 적응형 은닉 0.493 → 완전 적응형 0.259
- **단계 융합 모니터(DT, PGD-10 ε=8/255)**: α=0일 때 방어 SR 42.2%(Δ=−7.7 pp), α=1일 때 48.8%(Δ=−1.0 pp) — 융합 모니터는 최적 구성에서도 1.0 pp만 회복
- **검사기 인지 적응형 PGD-10**: 최악의 경우 방어 SR이 object 46.0%, spatial 50.7%로 감소, 모두 동일 공격 하 미방어 SR보다 낮음 — 모니터는 적응형 공격 하에서 무효할 뿐만 아니라 오히려 해로움

### 결과 함의
- 추론 유형(규모나 백본이 아닌)이 강건성의 지배적 요인: RD-VLA(0.5B)는 OFT(7B)보다 9.9배 취약(σ=0.2)하지만, DT(3B)와 OFT(7B)는 유의미한 차이 없음
- 증폭은 구조적: K-sweep은 깊이가 교란을 증폭하지 않음을 보여주며, 증폭은 추론 진입점에서 발생
- 계획 일관성 기반 방어는 적응형 공격 하에서 완전히 무력화: 은닉 공격은 프로브 표시율을 98.9%에서 5.5%로 낮추며, 6.3% 클린 거짓 양성률과 구분 불가능

## 경계와 한계

- **각 추론 패러다임은 단일 모델로만 대표됨**(N=3), 백본, 규모, 훈련 데이터가 추론 계열과 혼동됨; 패러다임 수준 진술은 실질적으로 모델 수준 관찰
- **LIBERO 시뮬레이션에 한정**, SimplerEnv는 단일 아키텍처 건전성 검사로만 사용; sim-to-real 전이는 해결되지 않음
- **추론 단계 손상은 텍스트 CoT에 한정**: RD-VLA는 주소 지정 가능한 추론 표면이 없고, OFT는 추론 단계가 없음; 시각 추론(CoT-VLA)은 연구 범위 밖
- **자연어 지시 자체는 교란하지 않음**: 지시 수준 공격(재작성, 프롬프트 주입)은 별도의 위협 범주를 형성
- **EOT 테스트 T=2**, 문헌 표준 T∈{8,16}보다 낮음; 곡률 결론은 100개 쿼리 Square Attack으로 교차 확인되었지만 완벽하지는 않음
- **CoT 비활성화 절제는 추론 텍스트를 제로 토큰으로 설정**, 분포 내 skip-CoT 비교기 대비 off-manifold이며, ±5 pp 동등성 경계는 보수적 해석
- **단계 융합 모니터는 사후 평가**, 적응형 평가는 행동 이상 항목을 대상으로 하는 공격자만 다루며 텍스트 일관성 항목과 결합되지 않음
- **노이즈 필터링 기여는 검정력 임계값 미만**(N=12, 최소 감지 가능 효과 d≈0.85); 자연 테스트는 더 높은 N의 복제 실험
- **저자들은 방어 방법을 제안하지 않음을 명시**, 결과를 방어 작업의 전제 조건으로 규정하며 no-go 정리로 보지 않음

## 공학적 시사점

- **재현 시 통계 구성을 먼저 확인**: 조건당 N=12(4개 스위트×3개 시드), 유닛당 50개 에피소드(10개 작업×5개 시행); 짝지은 Wilcoxon 부호 순위 검정 + Holm-Bonferroni 보정(13개 검정 계열); bootstrap CI(n=10000). N이 다르면 최소 감지 가능 효과 d≈0.85는 적용되지 않음
- **RD-VLA 화이트박스 PGD-10은 그래디언트 체크포인팅 필요**: K=12 순환 역전파, 최대 3.5 GB(A100-40GB); FGSM 셀은 DT→RD-VLA 전이 공격이며 화이트박스 취약성의 하한만 제공
- **가장 함정에 빠지기 쉬운 것은 K-sweep 구현**: 순환의 num_iter 플래그를 활용해 추론 시 K∈{4,8,12}를 변화시켜야 하며 재훈련 불필요; 모델이 동적 깊이를 지원하지 않으면 이 반증 실험은 재현 불가
- **일관성 프로브의 엔티티 추출**: 전체 LIBERO 29개 객체 어휘 사용, 최장 우선 부분 문자열 매칭; 방향 키워드(left, right, up, down, forward, backward, toward, away)와 그리퍼 키워드(open, close, grasp, release, grip, pick, place)는 정확히 일치해야 함
- **임계값 τ=0.7은 임계값 스캔에서 선택**(τ=0.5: 84% TPR/0% FPR; τ=0.7: 100%/0%; τ=0.9: 100%/95%); 매칭 없는 FPR 보정 기준선은 40–67% 클린 에피소드에서 기권
- **하위 팀이 계획 일관성 기반 모니터 배포를 고려한다면**: 먼저 적응형 은닉 공격(엔티티 교체 + 원래 지시 객체 재주입)을 테스트해야 하며, 이는 AUC를 0.996에서 0.493으로, 표시율을 98.9%에서 5.5%로 낮출 수 있음 — 단순 일관성 검사는 적대적 환경에서 신뢰할 수 없음
- **계산 예산 참고**: 총 약 635 GPU 시간(909개 실험, 0개 실패); FGSM은 에피소드당 클린 추론의 약 2.5배, PGD-10은 약 10배; RD-VLA PGD-10은 추가로 약 35 GPU 시간
