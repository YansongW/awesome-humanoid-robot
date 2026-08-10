---
$id: ent_paper_action_qformer_structured_representation_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models'
  zh: 'Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models'
  ko: 'Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models'
summary:
  en: 'Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action
    prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that
    this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision
    is applied too directly to the.'
  zh: 本文提出 Action QFormer，一种插入在预训练多模态骨干与策略头之间的查询式动作面向接口，用于在 VLA 模型动作微调期间重塑继承的多模态表征。作者通过梯度路由诊断与零样本仿真到现实导航实验，证明该接口能减少动作监督对语言侧表征的破坏性重写，同时保留对控制相关特征的定向适应。核心贡献在于将动作监督从单纯的下游目标重新定义为一种可调控的表征塑造力，并提供了结构化接口作为实现手段。
  ko: 'Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action
    prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that
    this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision
    is applied too directly to the.'
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
- action
- qformer
- structured
- representation
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
  title: 'arXiv:2607.14635 Action QFormer: Structured Representation Shaping under Action Supervision in Vi'
  url: https://arxiv.org/abs/2607.14635
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Action QFormer，一种插入在预训练多模态骨干与策略头之间的查询式动作面向接口，用于在 VLA 模型动作微调期间重塑继承的多模态表征。作者通过梯度路由诊断与零样本仿真到现实导航实验，证明该接口能减少动作监督对语言侧表征的破坏性重写，同时保留对控制相关特征的定向适应。核心贡献在于将动作监督从单纯的下游目标重新定义为一种可调控的表征塑造力，并提供了结构化接口作为实现手段。

## 它改变了什么

VLA 微调长期存在一个隐性矛盾：动作监督既是形成行为兼容表征的必要条件，又会在直接作用于继承的多模态通路时破坏语言侧处理和物体接地所需的表征稳定性。以往工作要么强化预训练骨干，要么强化动作解码器，但都回避了动作监督与继承表征交互方式这一根本问题。本文真正改变的是将“动作监督如何与多模态表征交互”从工程细节提升为可设计、可诊断的核心机制。

直接融合基线中，动作损失更新虽然能形成行为相关区分（如左右方向），但代价是广泛的上游重写和不稳定的指令到视觉注意力。Action QFormer 的实质贡献在于提供了一条中间适应路径：动作监督不必仅通过重塑上游通路来表达，而是可以通过查询状态在继承空间与动作面向空间之间双向中介。这使得“建设性适应”与“破坏性重写”在梯度结构上得以分离，而非依赖训练技巧去抑制副作用。

## 方法拆解

### 总体架构
三阶段流水线：预训练视觉-语言骨干（Qwen2.5-VL）产生继承多模态表示 → 中间接口模块重组为紧凑动作面向表示 → 下游策略头预测未来导航轨迹。

### Action QFormer 核心机制
- 维护 \(M=16\) 个可学习查询状态 \(Q^0\)，通过 \(K=4\) 层堆叠更新。
- 每层先通过自注意力吸收指令上下文，再通过交叉注意力从图像侧表征中选择视觉证据。
- 梯度结构为动作损失更新提供额外的查询特定适应路径，使动作监督不必仅通过重塑上游通路来表达。

### 训练目标
总损失由标量语言损失权重 \(r \in [0,1]\) 控制：
- \(r=0\)：仅动作损失（跳过语言分支前向）
- \(r=1\)：仅语言损失（跳过动作分支前向）
- \(0<r<1\)：凸插值 \((1-r)\cdot L_{action} + r\cdot L_{lang}\)

动作损失为条件扩散策略去噪目标：
\(\mathcal{L}_{action}=\mathbb{E}_{\tau,\epsilon}[\|\epsilon-\epsilon_\psi(A_t^\tau,\tau,z_t)\|_2^2]\)

### 梯度路由诊断
四种配置隔离动作监督引起的上游塑形：
- **动作更新阻断**（参考）：阻断动作损失对查询的更新
- **视觉编码器冻结**：冻结视觉编码器参数
- **语言骨干阻断**：阻断动作损失对语言骨干的梯度
- **全更新**：所有参数参与动作损失优化

### 关键设计决策
- 查询通过自注意力与指令侧交互、交叉注意力与图像侧交互，实现双向中介而非单向池化。
- 语言损失仅应用于监督指令跨度，避免干扰骨干的语言建模能力。
- 训练中 \(r\) 从高语言权重余弦调度到较低值，实现渐进式动作适配。

## 关键创新

1. **表征塑造的显式接口化**：以往动作监督直接作用于继承表征，本文通过查询式接口将“塑造力”封装为可学习的中间状态。这不仅是架构改动，而是将动作监督从破坏性外力转化为可调控的适应信号——梯度有了查询特定路径，不必全部经由上游通路表达。

2. **梯度路由诊断方法**：通过停止梯度干预设置四种配置，系统隔离动作监督对视觉编码器、语言骨干和查询状态的分别影响。这为 VLA 微调提供了可操作的诊断工具，而非仅凭最终指标猜测内部发生了什么。

3. **“定向重写”与“广泛重写”的量化区分**：表 VI 与表 VII 显示，Action QFormer 在全更新下重写子空间的有效秩从 29.41 提升到 65.68（由表内数值计算），同时 Top-5 方差占比从 0.666 降至 0.521（由表内数值计算），表明重写更分散、更目标化而非集中于少数主成分。这种量化视角是理解动作监督影响的新维度。

## 实验与结果

### 零样本仿真到现实闭环导航（表 II）
| 指标 | 直接融合基线 | Action QFormer |
|---|---|---|
| 平均任务成功率（无指令） | 18.8% | 56.3% |
| 固定指令动作生成正确率 | 22.5% | 75.5% |
| 指令 OOD 率（Fridge） | 100.0% | 0.0% |
| 指令 OOD 率（Door） | 97.2% | 0.0% |
| 指令 OOD 率（Chair） | 100.0% | 0.0% |
| 指令 OOD 率（Table） | 100.0% | 0.0% |

### 关键场景对比
- **Fridge（远目标）**：给定指令时任务成功率从 75.0% 提升至 100.0%，平均碰撞从 0.25 降至 0.00。
- **Table（急转弯）**：无指令时任务成功率从 0.0% 提升至 62.5%，指令方向正确率从 22.9% 提升至 100.0%。
- **Chair（转身）**：动作方向正确率从 53.6% 提升至 82.4%，指令 OOD 率从 100.0% 降至 0.0%。

### 表征分析
- 表 III 中，Action QFormer 全更新下左右余弦相似度降至 0.470（Action）与 0.520（Action Repr.），而直接融合基线为 0.891 与 0.931（由表内数值对比），表明查询状态形成了更清晰的方向区分。
- 表 VIII 显示，Action QFormer 全更新下边界 token 重写份额为 0.717，而直接融合基线为 0.423（由表内数值对比），说明重写更集中于指令边界而非广泛分布。

### 消融
- 图像潜变量变体保留部分能力但失去优势；仅查询变体产生视觉合理运动但失去指令跟随能力。
- reduced-query 变体始终强于 reduced-depth 变体，尤其在方向控制上。

## 边界与局限

- Action QFormer 不能自行解决障碍物感知的指令规划：当安全执行需要显式绕行附近障碍物时，若模型未选择合适的接地目标来描述避障行为，仍可能失败。
- 论文未提及对大规模多任务、跨具身泛化或更复杂操作任务的评估；主要使用导航作为挑战性具身设置。
- 注意力聚焦效果不被视为普遍机制，仅作为定性证据；逐头可视化（图 19）为选择性选取，应视为可能行为的示例而非分布性证据。
- 对 vision-encoder-frozen 比较中出现的注意力偏移或塌缩情况，作者仅提出解释性假设，未作确定性因果主张。
- 未对 Action QFormer 进行广泛的模块特定超参数调优。

## 工程启示

复现时先核对三件事：一是训练权重调度回调的实现——\(r\) 的余弦调度直接影响动作适配的渐进性，若调度过快可能导致表征失稳；二是批量配置——直接融合基线为 16×4，Action QFormer 为 8×8，两者有效批量相同但梯度噪声特性不同，直接替换时需重新验证；三是梯度路由诊断的参考设置——所有比较均相对于同一接口族内的 action-update-blocked 参考进行，跨接口族比较会混淆变量。

最容易踩坑的地方在于：动作监督的梯度路径是核心机制，若在实现中意外将查询状态与骨干参数的梯度耦合（例如共享优化器分组不当），会退化为直接融合的行为。另一个常见问题是语言损失权重的调度范围——若 \(r\) 未降至足够低，动作适配不充分；若降得太快，语言侧表征可能被破坏。建议先复现表 III 的余弦相似度诊断，确认 Action QFormer 全更新下 Action Repr. 相似度降至 0.520 附近（由表内数值对比），再进入闭环评估。

## Overview
Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision is applied too directly to the inherited multimodal pathway, it can also destabilize representations that support language-side processing and object grounding. To address this tension, we introduce Action QFormer, a query-based action-facing interface that uses instruction-conditioned queries to reorganize inherited multimodal information into action-facing representations before downstream action generation. In zero-shot sim-to-real navigation, Action QFormer improves average closed-loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction generations. Further analyses show that Action QFormer changes how action supervision shapes inherited multimodal representations, reducing broad upstream rewriting while preserving targeted and sometimes constructive action-supervised adaptation. These results suggest that improving VLA performance requires not only stronger pretrained backbones, but also better ways of selecting and organizing inherited multimodal information while controlling how it is shaped under action supervision.

## 参考
- https://arxiv.org/abs/2607.14635

## 개요

본 논문은 Action QFormer를 제안한다. 이는 사전 훈련된 다중 모달 백본과 정책 헤드 사이에 삽입되는 쿼리 기반 동작 지향 인터페이스로, VLA 모델의 동작 미세 조정 중 상속된 다중 모달 표현을 재구성하는 역할을 한다. 저자들은 그래디언트 라우팅 진단과 제로샷 시뮬레이션-실제 내비게이션 실험을 통해, 이 인터페이스가 동작 감독이 언어 측 표현에 가하는 파괴적 재작성을 줄이면서도 제어 관련 특징에 대한 방향성 적응을 유지할 수 있음을 입증한다. 핵심 기여는 동작 감독을 단순한 하위 목표에서 조절 가능한 표현 형성력으로 재정의하고, 이를 구현하기 위한 구조화된 인터페이스를 제공한 것이다.

## 무엇을 바꾸었는가

VLA 미세 조정에는 오랫동안 잠재된 모순이 존재해 왔다. 동작 감독은 행동 호환 표현을 형성하는 데 필수 조건이지만, 상속된 다중 모달 경로에 직접 작용할 때 언어 측 처리와 객체 접지에 필요한 표현 안정성을 손상시킬 수 있다. 기존 연구는 사전 훈련된 백본을 강화하거나 동작 디코더를 강화하는 데 초점을 맞췄지만, 동작 감독과 상속 표현 간의 상호작용 방식이라는 근본적 문제는 회피해 왔다. 본 논문이 실제로 바꾼 것은 "동작 감독이 다중 모달 표현과 어떻게 상호작용하는가"를 공학적 세부 사항에서 설계 가능하고 진단 가능한 핵심 메커니즘으로 승격시킨 점이다.

직접 융합 베이스라인에서 동작 손실 업데이트는 행동 관련 구분(예: 좌우 방향)을 형성할 수 있지만, 광범위한 업스트림 재작성과 불안정한 명령-시각 주의의 대가를 치른다. Action QFormer의 실질적 기여는 중간 적응 경로를 제공한 것이다. 동작 감독은 업스트림 경로를 재구성하는 것만으로 표현될 필요 없이, 쿼리 상태를 통해 상속 공간과 동작 지향 공간 사이에서 양방향 중재를 할 수 있다. 이를 통해 "건설적 적응"과 "파괴적 재작성"이 그래디언트 구조에서 분리될 수 있으며, 훈련 기법으로 부작용을 억제하는 데 의존하지 않는다.

## 방법 분석

### 전체 아키텍처
3단계 파이프라인: 사전 훈련된 비전-언어 백본(Qwen2.5-VL)이 상속된 다중 모달 표현 생성 → 중간 인터페이스 모듈이 이를 컴팩트한 동작 지향 표현으로 재구성 → 하위 정책 헤드가 미래 내비게이션 궤적 예측.

### Action QFormer 핵심 메커니즘
- \(M=16\)개의 학습 가능한 쿼리 상태 \(Q^0\)를 유지하며, \(K=4\)개의 스택 레이어를 통해 업데이트.
- 각 레이어는 먼저 자기 주의를 통해 명령 컨텍스트를 흡수한 후, 교차 주의를 통해 이미지 측 표현에서 시각적 증거를 선택.
- 그래디언트 구조는 동작 손실 업데이트에 추가적인 쿼리 특정 적응 경로를 제공하여, 동작 감독이 업스트림 경로 재구성만으로 표현될 필요가 없게 함.

### 훈련 목표
총 손실은 스칼라 언어 손실 가중치 \(r \in [0,1]\)로 제어됨:
- \(r=0\): 동작 손실만 사용(언어 분기 전방 패스 건너뜀)
- \(r=1\): 언어 손실만 사용(동작 분기 전방 패스 건너뜀)
- \(0<r<1\): 볼록 보간 \((1-r)\cdot L_{action} + r\cdot L_{lang}\)

동작 손실은 조건부 확산 정책 디노이징 목표:
\(\mathcal{L}_{action}=\mathbb{E}_{\tau,\epsilon}[\|\epsilon-\epsilon_\psi(A_t^\tau,\tau,z_t)\|_2^2]\)

### 그래디언트 라우팅 진단
네 가지 구성이 동작 감독으로 인한 업스트림 형성을 격리:
- **동작 업데이트 차단**(참조): 쿼리에 대한 동작 손실 업데이트 차단
- **비전 인코더 동결**: 비전 인코더 파라미터 동결
- **언어 백본 차단**: 언어 백본에 대한 동작 손실 그래디언트 차단
- **전체 업데이트**: 모든 파라미터가 동작 손실 최적화에 참여

### 핵심 설계 결정
- 쿼리는 자기 주의를 통해 명령 측과, 교차 주의를 통해 이미지 측과 상호작용하여 단방향 풀링이 아닌 양방향 중재를 구현.
- 언어 손실은 명령 스팬 감독에만 적용되어 백본의 언어 모델링 능력을 방해하지 않음.
- 훈련 중 \(r\)은 높은 언어 가중치에서 코사인 스케줄링을 통해 낮은 값으로 감소하여 점진적 동작 적응 구현.

## 핵심 혁신

1. **표현 형성의 명시적 인터페이스화**: 기존에는 동작 감독이 상속된 표현에 직접 작용했지만, 본 논문은 쿼리 기반 인터페이스를 통해 "형성력"을 학습 가능한 중간 상태로 캡슐화한다. 이는 단순한 아키텍처 변경이 아니라, 동작 감독을 파괴적 외부 힘에서 조절 가능한 적응 신호로 전환한 것이다. 그래디언트에 쿼리 특정 경로가 생겨 업스트림 경로를 통해서만 표현될 필요가 없다.

2. **그래디언트 라우팅 진단 방법**: 그래디언트 중단 개입을 통해 네 가지 구성을 설정하여, 동작 감독이 비전 인코더, 언어 백본, 쿼리 상태에 미치는 각각의 영향을 체계적으로 격리한다. 이는 최종 지표만으로 내부 상황을 추측하는 대신, VLA 미세 조정을 위한 실행 가능한 진단 도구를 제공한다.

3. **"방향성 재작성"과 "광범위한 재작성"의 정량적 구분**: 표 VI와 표 VII는 Action QFormer가 전체 업데이트에서 재작성 부분공간의 유효 랭크를 29.41에서 65.68로 향상시키고(표 내 수치 계산), Top-5 분산 비율을 0.666에서 0.521로 감소시킴(표 내 수치 계산)을 보여준다. 이는 재작성이 소수의 주성분에 집중되기보다 더 분산되고 목표 지향적임을 나타낸다. 이러한 정량적 관점은 동작 감독의 영향을 이해하는 새로운 차원이다.

## 실험 및 결과

### 제로샷 시뮬레이션-실제 폐루프 내비게이션(표 II)
| 지표 | 직접 융합 베이스라인 | Action QFormer |
|---|---|---|
| 평균 작업 성공률(명령 없음) | 18.8% | 56.3% |
| 고정 명령 동작 생성 정확도 | 22.5% | 75.5% |
| 명령 OOD 비율(Fridge) | 100.0% | 0.0% |
| 명령 OOD 비율(Door) | 97.2% | 0.0% |
| 명령 OOD 비율(Chair) | 100.0% | 0.0% |
| 명령 OOD 비율(Table) | 100.0% | 0.0% |

### 핵심 시나리오 비교
- **Fridge(원거리 목표)**: 명령이 주어졌을 때 작업 성공률이 75.0%에서 100.0%로 향상, 평균 충돌이 0.25에서 0.00으로 감소.
- **Table(급회전)**: 명령 없이 작업 성공률이 0.0%에서 62.5%로 향상, 명령 방향 정확도가 22.9%에서 100.0%로 향상.
- **Chair(회전)**: 동작 방향 정확도가 53.6%에서 82.4%로 향상, 명령 OOD 비율이 100.0%에서 0.0%로 감소.

### 표현 분석
- 표 III에서 Action QFormer 전체 업데이트 시 좌우 코사인 유사도가 0.470(Action) 및 0.520(Action Repr.)으로 감소한 반면, 직접 융합 베이스라인은 0.891 및 0.931(표 내 수치 비교)로, 쿼리 상태가 더 명확한 방향 구분을 형성함을 나타냄.
- 표 VIII은 Action QFormer 전체 업데이트 시 경계 토큰 재작성 비중이 0.717인 반면, 직접 융합 베이스라인은 0.423(표 내 수치 비교)으로, 재작성이 광범위하게 분포하기보다 명령 경계에 더 집중됨을 보여줌.

### 절제 연구
- 이미지 잠재 변수 변형은 일부 능력을 유지하지만 우위를 잃음; 쿼리 전용 변형은 시각적으로 그럴듯한 움직임을 생성하지만 명령 추종 능력을 잃음.
- reduced-query 변형은 특히 방향 제어에서 reduced-depth 변형보다 일관되게 우수함.

## 경계 및 한계

- Action QFormer는 장애물 인식을 위한 명령 계획 문제를 자체적으로 해결하지 못함: 안전한 실행을 위해 근처 장애물을 명시적으로 우회해야 할 때, 모델이 회피 행동을 설명할 적절한 접지 대상을 선택하지 않으면 여전히 실패할 수 있음.
- 논문은 대규모 다중 작업, 교차 체현 일반화 또는 더 복잡한 조작 작업에 대한 평가를 언급하지 않음; 주로 내비게이션을 도전적인 체현 설정으로 사용.
- 주의 집중 효과는 보편적 메커니즘으로 간주되지 않으며 정성적 증거로만 사용됨; 헤드별 시각화(그림 19)는 선택적으로 추출된 것으로, 분포적 증거가 아닌 가능한 행동의 예시로 간주해야 함.
- vision-encoder-frozen 비교에서 나타난 주의 이동 또는 붕괴 상황에 대해 저자들은 설명적 가설만 제시했으며 결정적 인과 주장은 하지 않음.
- Action QFormer에 대한 광범위한 모듈별 하이퍼파라미터 튜닝은 수행되지 않음.

## 공학적 시사점

재현 시 먼저 세 가지를 확인해야 한다. 첫째, 훈련 가중치 스케줄링 콜백 구현 — \(r\)의 코사인 스케줄링은 동작 적응의 점진성에 직접 영향을 미치며, 스케줄링이 너무 빠르면 표현 불안정이 발생할 수 있음. 둘째, 배치 구성 — 직접 융합 베이스라인은 16×4, Action QFormer는 8×8로, 유효 배치 크기는 동일하지만 그래디언트 노이즈 특성이 다르므로 직접 교체 시 재검증이 필요함. 셋째, 그래디언트 라우팅 진단의 참조 설정 — 모든 비교는 동일한 인터페이스 계열 내의 action-update-blocked 참조를 기준으로 이루어지며, 인터페이스 계열 간 비교는 변수를 혼동시킴.

가장 함정에 빠지기 쉬운 부분은 동작 감독의 그래디언트 경로가 핵심 메커니즘이라는 점이다. 구현 중 쿼리 상태와 백본 파라미터의 그래디언트가 의도치 않게 결합되면(예: 최적화기 그룹 분할이 잘못된 경우) 직접 융합의 동작으로 퇴화한다. 또 다른 일반적인 문제는 언어 손실 가중치의 스케줄링 범위이다 — \(r\)이 충분히 낮아지지 않으면 동작 적응이 불충분하고, 너무 빠르게 낮아지면 언어 측 표현이 손상될 수 있다. 먼저 표 III의 코사인 유사도 진단을 재현하여 Action QFormer 전체 업데이트에서 Action Repr. 유사도가 0.520 부근으로 감소하는지(표 내 수치 비교) 확인한 후, 폐루프 평가로 진행할 것을 권장한다.
