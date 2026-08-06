---
$id: ent_paper_gate_not_cache_gate_provenance_bounds_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping'
  zh: 'The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping'
  ko: 'The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping'
summary:
  en: Token skipping is a widely used training-free way to accelerate vision--language--action (VLA) models by bypassing computation
    for most visual tokens at each control step according to a gate. When the next gate is harvested from the previous accelerated
    forward, however, the tokens skipped at one step are also the ones least visible to the next gate, and the damage can
    compound across control.
  zh: 本文由机器人学习与系统领域研究者提出，针对训练无关的视觉token跳过（training-free token skipping）在视觉-语言-动作（VLA）模型闭环控制中的可靠性问题，通过受控因子实验隔离出决定性变量：门控信号的来源（gate
    provenance），而非跳过机制本身（reuse或deletion）。核心贡献是提出“执行间隙刷新”（actuation-slack refresh）策略，利用机器人执行动作块的约400 ms空闲窗口运行稠密前向，提供干净的下一步门控与新鲜KV基座，在不占用关键路径的前提下将闭环成功率恢复至与稠密推理统计不可区分的水平。
  ko: Token skipping is a widely used training-free way to accelerate vision--language--action (VLA) models by bypassing computation
    for most visual tokens at each control step according to a gate. When the next gate is harvested from the previous accelerated
    forward, however, the tokens skipped at one step are also the ones least visible to the next gate, and the damage can
    compound across control.
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
- gate
- not
- cache
- gate
- provenance
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
  title: 'arXiv:2608.00391 The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of T'
  url: https://arxiv.org/abs/2608.00391
  date: '2026-08-01'
  accessed_at: '2026-08-05'
---

## 概述

本文由机器人学习与系统领域研究者提出，针对训练无关的视觉token跳过（training-free token skipping）在视觉-语言-动作（VLA）模型闭环控制中的可靠性问题，通过受控因子实验隔离出决定性变量：门控信号的来源（gate provenance），而非跳过机制本身（reuse或deletion）。核心贡献是提出“执行间隙刷新”（actuation-slack refresh）策略，利用机器人执行动作块的约400 ms空闲窗口运行稠密前向，提供干净的下一步门控与新鲜KV基座，在不占用关键路径的前提下将闭环成功率恢复至与稠密推理统计不可区分的水平。

## 它改变了什么

现有加速方法（如VLA-Cache的KV复用、VLA-Pruner的token删除）在发布的工作点（如0.9 skip ratio）报告近乎无损的成功率，但作者指出这些结论建立在未隔离反馈回路的基础上：当下一步门控从前一步的加速前向中获取时，被跳过的token对门控信号的可见性最低，损伤在控制步间累积直至任务失败。这改变了领域对“跳过机制决定可靠性”的默认假设——真正决定闭环可靠性的不是token被复用还是删除，而是门控信号是否来自稠密前向。

这一判断的工程意义在于：现有方法（包括带触发刷新的SAFE-Pruner）都试图通过反应式检测器在损伤累积到可观测程度时触发恢复，但作者证明这类检测器在早期窗口的AUROC仅0.45–0.65（条件化后降至0.26–0.44），无法可靠捕捉静默失败。因此，可靠性不能依赖“检测-响应”范式，而应通过架构性保证（无条件刷新）来消除反馈回路。

## 方法拆解

### 门控来源与跳过机制的因子分解
- **自收获门控（self-harvested gate）**：从服务当前动作块的稀疏前向中获取门控信号，即 \( G_{t+1} = g_r(A_t^{sparse}, S_{t+1}^{live}) \)。
- **干净门控（clean gate）**：从同一帧的稠密前向（丢弃动作输出）中获取，即 \( G_{t+1} = g_r(A_t^{dense}, S_{t+1}^{live}) \)。
- **跳过机制**：复用（reuse，KV从跨步缓存中取，如VLA-Cache）与删除（deletion，token直接移除，如VLA-Pruner）。

### 执行间隙刷新（Actuation-Slack Refresh）
- 在机器人执行当前动作块期间（约400 ms窗口），运行一次稠密前向，提供下一步的干净门控 \( G_{t+1} \) 和新鲜KV基座 \( B_{t+1} = \{K_{t,V}^{(l),dense}, V_{t,V}^{(l),dense}\}_{l=1}^{L} \)。
- 刷新是无条件的（unconditional），因为测量的反应式检测器无法可靠触发（早期窗口AUROC 0.45–0.65，条件化后0.26–0.44）。
- 关键设计决策：固定选择规则 \( g_r \)（包括比例 \( r \)），只改变其时间注意力来源；第一个块始终稠密运行，因为没有门控或KV基座可用。

### 与SAFE-Pruner的对比
- SAFE-Pruner使用自收获的一致性分数触发刷新，但该触发器无法看到被剪枝token中的关键变化（其触发率在Object任务上仅0.09%，3,222次编码中触发3次，而该任务成功率仅0.19）。

## 关键创新

1. **隔离门控来源作为独立变量**：首次通过受控因子实验（门控来源 × KV来源）证明，在0.9 skip ratio下，干净门控+新鲜KV达到0.98成功率，而自收获门控+新鲜KV仅0.68；干净门控+累积KV仍达0.96，说明门控来源是主导因素，KV新鲜度是次要因素。这推翻了“跳过机制决定可靠性”的直觉。

2. **利用执行间隙的离路径稠密前向**：将稠密计算嵌入机器人固有的执行空闲窗口（约400 ms），而非压缩关键路径。H100上离路径稠密前向p50为63.6 ms，远小于执行窗口，且561次刷新p99为79.9 ms，无截止时间错过。这使得刷新在延迟上几乎“免费”，同时将计算量增至约1.6×稠密FLOPs。

3. **无条件刷新优于触发式刷新**：作者证明oracle驱动的触发调度（即使排除干净信号成本）在测试阈值上仅达0.66–0.92，低于无条件使用干净产品的0.98。这挑战了“按需刷新”的直觉，指出在门控信号不可靠时，架构性保证优于反应式检测。

## 实验与结果

### 受控因子实验（LIBERO-Object，skip ratio 0.9）
| 门控来源 | KV来源 | 成功率 |
|---------|--------|-------|
| 自收获 | 新鲜 | 0.68 |
| 自收获 | 累积 | 0.43 |
| 干净 | 新鲜 | 0.98 |
| 干净 | 累积 | 0.96 |

干净门控下reuse和deletion均达0.98，与稠密1.00统计不可区分；自收获门控下reuse降至0.68，deletion降至0.31。

### 闭环成功率（表2，skip ratio 0.9）
| 基准 | 任务 | dense | VC / +R | VP / +R |
|------|------|-------|---------|---------|
| LIBERO | Object | 1.00 | 0.66 / 0.96 | 0.98 / 0.98 |
| LIBERO | 平均 | 0.95 | 0.80 / 0.90 | 0.95 / 0.97 |
| SIMPLER | put-in-drawer | 0.32 | 0.02 / 0.02 | 0.16 / 0.19 |
| SIMPLER | 平均 | 0.68 | 0.28 / 0.34 | 0.59 / 0.58 |

刷新（+R）在LIBERO上显著恢复VC（0.66→0.96），但在SIMPLER put-in-drawer上无效（0.02→0.02），说明任务难度与基座差异影响刷新收益。

### 刷新配置（表3，VLA-Cache，0.9 skip ratio）
| 配置 | Object | drawer |
|------|--------|--------|
| dense | 1.00 | 0.80 |
| no refresh | 0.66 | 0.52 |
| shallow recompute | 0.81 | 0.58 |
| actuation-slack refresh | 0.96 | 0.69 |

### 高比例边界（图5、6）
- 自收获门控在0.6 skip ratio前与稠密无显著差异，0.65首次分离，0.97时VC降至0.06，+R保持0.76，VP保持0.98。
- 干净门控在0.97前每个测试点与稠密统计上不可区分。

### 延迟（图7，0.9 skip ratio，毫秒）
| 硬件 | dense | VC | VP | ours |
|------|-------|----|----|------|
| H100 | 63.4 | 53.9 | 56.1 | 52.0 |
| RTX 4090 | 123.3 | 101.2 | 108.0 | 97.0 |

真实机器人（RTX 5880 Ada）：dense 125.6 ms，VC 102.8 ms（↓18.2%），VP 109.7 ms（↓12.7%），ours 98.1 ms（↓21.9%）。

## 边界与局限

- 刷新增加计算量至约1.6×稠密FLOPs，能量增加约18%每块，作者未提供能效与延迟的联合优化方案。
- 可靠性评估限于2个策略（OpenVLA-OFT、CogACT-Base）、4个LIBERO套件、4个SIMPLER任务；物理平台仅验证延迟，未验证成功率。
- 刷新解决自收获门控导致的失败，但不解决门控设计或模型基座的限制；操作边界可能因任务、基座和门控族而异。
- 并发检测器（针对分布偏移或开环偏差）未在此测试；反应式信号（mid-chunk re-query分歧、proprioceptive跟踪偏差）早期窗口AUROC 0.45–0.65，全episode AUROC 0.80是长度伪影，条件化后0.26–0.44。
- 结论限于OFT上测试的触发器；CogACT上oracle触发器在γ=0.90达到稠密成功率，说明触发失败结论为基座特定。

## 工程启示

- **复现时先核对门控来源**：任何token skipping方法的闭环评估必须报告门控信号是来自稀疏前向还是稠密前向。若门控来自加速前向，0.9 skip ratio下的成功率可能从0.98跌至0.68（reuse）或0.31（deletion），这是最易踩坑的混淆点。
- **刷新窗口的时序验证**：执行间隙刷新依赖约400 ms的执行窗口。在H100上离路径稠密前向p50为63.6 ms、p99为79.9 ms，均远小于窗口；但在RTX 4090上p50为122.2 ms，若执行窗口缩短或硬件更慢，需重新验证截止时间。建议先测量目标平台的稠密前向延迟与执行窗口的比值。
- **触发式刷新不可靠**：SAFE-Pruner的触发率在Object任务上仅0.09%（3,222次编码触发3次），而该任务成功率仅0.19。若下游团队计划采用触发式刷新，应预期在门控信号不可靠时触发器会静默失效；无条件刷新是更稳妥的架构选择。
- **高skip ratio边界**：干净门控在0.97 skip ratio前与稠密统计不可区分，而自收获门控在0.65即开始分离。若需在0.9以上skip ratio工作，必须保证门控来源为稠密前向，否则成功率可能降至0.06（VC在0.97时）。

## Overview
Token skipping is a widely used training-free way to accelerate vision--language--action (VLA) models by bypassing computation for most visual tokens at each control step according to a gate. When the next gate is harvested from the previous accelerated forward, however, the tokens skipped at one step are also the ones least visible to the next gate, and the damage can compound across control steps until the task fails. We study the two mechanisms this class is built on, reuse and deletion, crossing each against where its gate signal comes from on identical episodes. At a skip ratio of 0.9 on LIBERO-Object, both collapse when the gate comes from the model's own accelerated forwards, to 0.68 under reuse and to 0.31 under deletion against a dense 1.00, and the collapse is invisible to the action-level detectors we evaluate. What separates collapse from dense-level operation is not the mechanism but whether the gate is clean, computed by a forward that skipped nothing. We therefore propose actuation-slack refresh, one dense pass run while the robot executes its current action chunk, off the critical path, that hands the next step a clean gate and a fresh KV base. Since the measured detectors do not reliably reveal the failure, the refresh is unconditional rather than triggered. Both mechanisms then recover to 0.98, keeping the speed of skipping and the information of a dense pass. We then integrate the refresh into state-of-the-art caching and pruning methods across two VLA policies, 4 LIBERO suites, and 4 SIMPLER tasks, where it repairs every collapse caused by using a self-harvested gate. Serve latency drops 18--22\% below dense, measured both in simulation and on a physical robot. Where the gate signal comes from, not how tokens are skipped, decides closed-loop reliability for accelerated VLAs.

## 参考
- https://arxiv.org/abs/2608.00391

## 개요

본 논문은 로봇 학습 및 시스템 분야 연구자들이 제안한 것으로, 훈련 독립적 시각 토큰 스킵핑(training-free token skipping)이 시각-언어-행동(VLA) 모델 폐루프 제어에서의 신뢰성 문제를 다룹니다. 통제된 요인 실험을 통해 결정적 변수를 분리해냈습니다: 스킵 메커니즘 자체(reuse 또는 deletion)가 아닌, 게이팅 신호의 출처(gate provenance)입니다. 핵심 기여는 "실행 간격 새로고침"(actuation-slack refresh) 전략을 제안한 것으로, 로봇이 동작 블록을 실행하는 약 400ms의 유휴 창을 활용해 밀집 전방향(dense forward)을 실행하여, 깨끗한 다음 단계 게이팅과 새로운 KV 기반을 제공합니다. 이는 핵심 경로를 점유하지 않으면서 폐루프 성공률을 밀집 추론과 통계적으로 구별 불가능한 수준으로 회복시킵니다.

## 그것이 바꾸는 것

기존 가속 방법들(예: VLA-Cache의 KV 재사용, VLA-Pruner의 토큰 삭제)은 발표된 작업 지점(예: 0.9 skip ratio)에서 거의 손실 없는 성공률을 보고하지만, 저자들은 이러한 결론이 피드백 루프를 분리하지 않은 상태에서 도출되었음을 지적합니다: 다음 단계 게이팅이 이전 단계의 가속 전방향에서 얻어질 때, 스킵된 토큰은 게이팅 신호에 대한 가시성이 가장 낮아지며, 손상은 제어 단계 간에 누적되어 결국 작업 실패로 이어집니다. 이는 "스킵 메커니즘이 신뢰성을 결정한다"는 분야의 기본 가정을 바꿉니다—폐루프 신뢰성을 실제로 결정하는 것은 토큰이 재사용되거나 삭제되는지가 아니라, 게이팅 신호가 밀집 전방향에서 오는지 여부입니다.

이 판단의 공학적 의미는 다음과 같습니다: 기존 방법들(트리거 새로고침이 있는 SAFE-Pruner 포함)은 손상이 관측 가능한 수준으로 누적될 때 반응적 감지기를 통해 복구를 시도하지만, 저자들은 이러한 감지기가 초기 창에서 AUROC 0.45–0.65(조건화 후 0.26–0.44로 하락)에 불과하여 조용한 실패를 안정적으로 포착할 수 없음을 증명합니다. 따라서 신뢰성은 "감지-대응" 패러다임에 의존할 수 없으며, 구조적 보장(무조건적 새로고침)을 통해 피드백 루프를 제거해야 합니다.

## 방법 분해

### 게이팅 출처와 스킵 메커니즘의 요인 분해
- **자체 수확 게이팅(self-harvested gate)**: 현재 동작 블록을 서비스하는 희소 전방향에서 게이팅 신호를 얻습니다, 즉 \( G_{t+1} = g_r(A_t^{sparse}, S_{t+1}^{live}) \).
- **깨끗한 게이팅(clean gate)**: 동일한 프레임의 밀집 전방향(동작 출력은 버림)에서 얻습니다, 즉 \( G_{t+1} = g_r(A_t^{dense}, S_{t+1}^{live}) \).
- **스킵 메커니즘**: 재사용(reuse, KV를 크로스 스텝 캐시에서 가져옴, 예: VLA-Cache)과 삭제(deletion, 토큰을 직접 제거, 예: VLA-Pruner).

### 실행 간격 새로고침(Actuation-Slack Refresh)
- 로봇이 현재 동작 블록을 실행하는 동안(약 400ms 창), 밀집 전방향을 한 번 실행하여 다음 단계의 깨끗한 게이팅 \( G_{t+1} \)과 새로운 KV 기반 \( B_{t+1} = \{K_{t,V}^{(l),dense}, V_{t,V}^{(l),dense}\}_{l=1}^{L} \)을 제공합니다.
- 새로고침은 무조건적(unconditional)입니다. 측정된 반응적 감지기가 안정적으로 트리거할 수 없기 때문입니다(초기 창 AUROC 0.45–0.65, 조건화 후 0.26–0.44).
- 핵심 설계 결정: 선택 규칙 \( g_r \)(비율 \( r \) 포함)을 고정하고, 시간적 주의 출처만 변경합니다; 첫 번째 블록은 항상 밀집으로 실행됩니다. 게이팅이나 KV 기반을 사용할 수 없기 때문입니다.

### SAFE-Pruner와의 비교
- SAFE-Pruner는 자체 수확 일관성 점수를 사용하여 새로고침을 트리거하지만, 해당 트리거는 프루닝된 토큰의 중요한 변화를 볼 수 없습니다(트리거율은 Object 작업에서 0.09%에 불과하며, 3,222회 인코딩 중 3회 트리거, 해당 작업 성공률은 0.19).

## 핵심 혁신

1. **게이팅 출처를 독립 변수로 분리**: 통제된 요인 실험(게이팅 출처 × KV 출처)을 통해 처음으로 0.9 skip ratio에서 깨끗한 게이팅+새로운 KV가 0.98 성공률을 달성하는 반면, 자체 수확 게이팅+새로운 KV는 0.68에 불과함을 증명했습니다; 깨끗한 게이팅+누적 KV는 여전히 0.96을 달성하여, 게이팅 출처가 지배적 요인이고 KV 신선도는 부차적 요인임을 보여줍니다. 이는 "스킵 메커니즘이 신뢰성을 결정한다"는 직관을 뒤집습니다.

2. **실행 간격을 활용한 경로 외 밀집 전방향**: 밀집 계산을 로봇 고유의 실행 유휴 창(약 400ms)에 내장하여 핵심 경로를 압축하지 않습니다. H100에서 경로 외 밀집 전방향 p50은 63.6ms로 실행 창보다 훨씬 작으며, 561회 새로고침의 p99는 79.9ms로 데드라인을 놓치지 않습니다.这使得 새로고침이 지연 측면에서 거의 "무료"이면서도 계산량을 약 1.6× 밀집 FLOPs로 증가시킵니다.

3. **무조건적 새로고침이 트리거 기반 새로고침보다 우수**: 저자들은 oracle 기반 트리거 스케줄링(깨끗한 신호 비용을 제외하더라도)이 테스트 임계값에서 0.66–0.92에 불과하여, 무조건적 깨끗한 제품 사용의 0.98보다 낮음을 증명합니다. 이는 "주문형 새로고침"의 직관에 도전하며, 게이팅 신호가 불신뢰할 때 구조적 보장이 반응적 감지보다 우월함을 지적합니다.

## 실험 및 결과

### 통제된 요인 실험(LIBERO-Object, skip ratio 0.9)
| 게이팅 출처 | KV 출처 | 성공률 |
|---------|--------|-------|
| 자체 수확 | 새로운 | 0.68 |
| 자체 수확 | 누적 | 0.43 |
| 깨끗한 | 새로운 | 0.98 |
| 깨끗한 | 누적 | 0.96 |

깨끗한 게이팅에서 reuse와 deletion 모두 0.98을 달성하여 밀집 1.00과 통계적으로 구별 불가능; 자체 수확 게이팅에서 reuse는 0.68로, deletion은 0.31로 하락.

### 폐루프 성공률(표 2, skip ratio 0.9)
| 벤치마크 | 작업 | dense | VC / +R | VP / +R |
|------|------|-------|---------|---------|
| LIBERO | Object | 1.00 | 0.66 / 0.96 | 0.98 / 0.98 |
| LIBERO | 평균 | 0.95 | 0.80 / 0.90 | 0.95 / 0.97 |
| SIMPLER | put-in-drawer | 0.32 | 0.02 / 0.02 | 0.16 / 0.19 |
| SIMPLER | 평균 | 0.68 | 0.28 / 0.34 | 0.59 / 0.58 |

새로고침(+R)은 LIBERO에서 VC를 크게 회복시키지만(0.66→0.96), SIMPLER put-in-drawer에서는 효과가 없습니다(0.02→0.02). 이는 작업 난이도와 기반 차이가 새로고침 이점에 영향을 미침을 시사합니다.

### 새로고침 구성(표 3, VLA-Cache, 0.9 skip ratio)
| 구성 | Object | drawer |
|------|--------|--------|
| dense | 1.00 | 0.80 |
| no refresh | 0.66 | 0.52 |
| shallow recompute | 0.81 | 0.58 |
| actuation-slack refresh | 0.96 | 0.69 |

### 높은 비율 경계(그림 5, 6)
- 자체 수확 게이팅은 0.6 skip ratio까지 밀집과 유의미한 차이가 없으며, 0.65에서 처음 분리되고, 0.97에서 VC는 0.06으로 하락, +R은 0.76 유지, VP는 0.98 유지.
- 깨끗한 게이팅은 0.97 이전의 모든 테스트 지점에서 밀집과 통계적으로 구별 불가능.

### 지연(그림 7, 0.9 skip ratio, 밀리초)
| 하드웨어 | dense | VC | VP | ours |
|------|-------|----|----|------|
| H100 | 63.4 | 53.9 | 56.1 | 52.0 |
| RTX 4090 | 123.3 | 101.2 | 108.0 | 97.0 |

실제 로봇(RTX 5880 Ada): dense 125.6 ms, VC 102.8 ms(↓18.2%), VP 109.7 ms(↓12.7%), ours 98.1 ms(↓21.9%).

## 경계 및 한계

- 새로고침은 계산량을 약 1.6× 밀집 FLOPs로 증가시키고, 블록당 에너지가 약 18% 증가합니다. 저자들은 에너지 효율과 지연의 통합 최적화 방안을 제공하지 않습니다.
- 신뢰성 평가는 2개 정책(OpenVLA-OFT, CogACT-Base), 4개 LIBERO 스위트, 4개 SIMPLER 작업으로 제한됩니다; 물리적 플랫폼은 지연만 검증하고 성공률은 검증하지 않았습니다.
- 새로고침은 자체 수확 게이팅으로 인한 실패를 해결하지만, 게이팅 설계나 모델 기반의 한계는 해결하지 않습니다; 운영 경계는 작업, 기반, 게이팅 패밀리에 따라 달라질 수 있습니다.
- 동시 감지기(분포 이동 또는 개루프 편향 대상)는 이 테스트에서 제외되었습니다; 반응적 신호(mid-chunk re-query 분기, 고유수용성 추적 편향)의 초기 창 AUROC는 0.45–0.65, 전체 에피소드 AUROC 0.80은 길이 아티팩트이며, 조건화 후 0.26–0.44입니다.
- 결론은 OFT에서 테스트된 트리거에 국한됩니다; CogACT에서 oracle 트리거는 γ=0.90에서 밀집 성공률을 달성하여, 트리거 실패 결론이 기반 특이적임을 시사합니다.

## 공학적 시사점

- **재현 시 먼저 게이팅 출처를 확인**: 모든 토큰 스킵핑 방법의 폐루프 평가는 게이팅 신호가 희소 전방향에서 오는지 밀집 전방향에서 오는지 반드시 보고해야 합니다. 게이팅이 가속 전방향에서 오면, 0.9 skip ratio에서 성공률이 0.98에서 0.68(reuse) 또는 0.31(deletion)로 떨어질 수 있습니다. 이는 가장 쉽게 함정에 빠지는 혼동 지점입니다.
- **새로고침 창의 타이밍 검증**: 실행 간격 새로고침은 약 400ms의 실행 창에 의존합니다. H100에서 경로 외 밀집 전방향 p50은 63.6ms, p99는 79.9ms로 모두 창보다 훨씬 작습니다; 그러나 RTX 4090에서 p50은 122.2ms로, 실행 창이 짧아지거나 하드웨어가 느리면 데드라인을 재검증해야 합니다. 대상 플랫폼의 밀집 전방향 지연과 실행 창의 비율을 먼저 측정할 것을 권장합니다.
- **트리거 기반 새로고침은 불신뢰**: SAFE-Pruner의 트리거율은 Object 작업에서 0.09%에 불과하며(3,222회 인코딩 중 3회 트리거), 해당 작업 성공률은 0.19입니다. 하류 팀이 트리거 기반 새로고침을 채택하려면, 게이팅 신호가 불신뢰할 때 트리거가 조용히 실패할 것으로 예상해야 합니다; 무조건적 새로고침이 더 안정적인 구조적 선택입니다.
- **높은 skip ratio 경계**: 깨끗한 게이팅은 0.97 skip ratio까지 밀집과 통계적으로 구별 불가능하지만, 자체 수확 게이팅은 0.65에서 분리되기 시작합니다. 0.9 이상의 skip ratio에서 작업해야 한다면, 게이팅 출처가 밀집 전방향임을 보장해야 합니다. 그렇지 않으면 성공률이 0.06(VC의 0.97 시점)까지 떨어질 수 있습니다.
