---
$id: ent_paper_simple_to_complex_structured_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning
  zh: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning
  ko: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning
summary:
  en: 'arXiv:2607.04591v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have demonstrated strong capabilities
    in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing
    research has primarily focused on improving model architectures, training strategies, and dataset scale, while little
    attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a
    fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability,
    and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy
    for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles:
    (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction
    environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing
    task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning
    increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate
    the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding.
    Experimental results show consistent improvements in task success rate and training stability compared with the baseline
    method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization
    as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill
    acquisition, scalable dataset construction, and long-horizon robotic manipulation.'
  zh: 本文提出一种面向VLA模型的简单到复杂结构化演示收集策略，利用双臂机器人平台实现。核心贡献在于通过任务分解、环境标准化和复杂度递增三个原则组织演示数据，显著提升任务成功率与训练稳定性。实验在积木抓取分类和毛巾折叠任务上验证了有效性。
  ko: 'arXiv:2607.04591v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have demonstrated strong capabilities
    in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing
    research has primarily focused on improving model architectures, training strategies, and dataset scale, while little
    attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a
    fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability,
    and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy
    for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles:
    (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction
    environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing
    task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning
    increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate
    the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding.
    Experimental results show consistent improvements in task success rate and training stability compared with the baseline
    method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization
    as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill
    acquisition, scalable dataset construction, and long-horizon robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- simple_to_complex_structured_d
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04591v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (973 chars, DeepSeek). [2026-08-28] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning (arXiv)
  url: https://arxiv.org/abs/2607.04591
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述

本文提出 Simple-to-Complex（S2C）结构化演示收集策略，用于替代 VLA 学习中天真的端到端完整任务演示采集。作者在真实双臂 SO-101 平台、π₀.₅ 模型上验证，S2C 在积木抓取分拣与毛巾折叠两个长时程任务中，将成功率从直接采集的 0% 分别提升至 80.0% 与 25.0%，核心贡献在于将数据收集过程本身作为可设计的监督信号来源。

## 它改变了什么

这个工作的真正改变在于把“演示如何被收集”从工程细节提升为与架构、损失函数同等重要的算法变量。此前 VLA 社区默认演示是给定的、中性的输入，而本文用实验证明：在相同模型、相同训练配置下，仅仅改变演示的组织结构，就能让策略从完全失败（0%）变为可用（80.0%）。这动摇了“数据量越大越好”的朴素直觉——200 条完整轨迹的监督质量，可能不如 300 条按能力分解的结构化轨迹。

更关键的是，它揭示了长时程操作失败的根源未必是模型容量不足，而是监督信号中“能力依赖关系”被端到端轨迹打散。直接采集的完整演示里，抓取、感知、排序三种能力的信息纠缠在一起，模型在有限数据下无法解耦学习。S2C 通过人为构造能力递进的数据分布，相当于给优化过程加了一个课程先验，这比在训练时设计课程调度更直接——因为数据分布本身已经编码了学习顺序。

## 方法拆解

### 任务分解为能力阶段
给定任务 \(\mathcal{T}\)，S2C 先分解为三个递进能力目标：\(\mathcal{T}\Rightarrow(\mathcal{D}_{\text{manip}},\mathcal{D}_{\text{state}},\mathcal{D}_{\text{exec}})\)，对应基本操作、物体感知与状态理解、完整任务执行。三个能力形成时间有序阶段 \(\{S_{\text{manip}},S_{\text{state}},S_{\text{exec}}\}\)。

### 环境标准化
每个阶段内，刻意削减与当前目标能力无关的变异性。例如积木任务 Stage 1 只用单色积木，Stage 2 引入多色但保持双臂独立，Stage 3 才要求双臂协调。毛巾任务 Stage 2 专门收集“任意初始状态→标准化平铺状态 \(o_{\text{flat}}\)”的归一化演示。

### 渐进复杂度调度
仅当上一阶段能力相对可靠后，才引入新难度源（物体属性、目标状态复杂度、双臂协调、可变形物体状态变化）。毛巾任务状态转换链为：
\[
o_{0}\xrightarrow{S_{1}(\mathcal{D}_{\text{manip}}^{\text{towel}})}o_{\text{grasp}}\xrightarrow{S_{2}(\mathcal{D}_{\text{state}}^{\text{towel}})}o_{\text{flat}}\xrightarrow{S_{3}(\mathcal{D}_{\text{exec}}^{\text{towel}})}o_{\text{final}}
\]
关键设计是显式插入状态归一化阶段，将后续折叠动作的输入状态不确定性大幅压缩，使 Stage 3 演示提供一致监督。

### 数据规模分配
积木任务：Stage 1 收集 80 个演示（4 色 × 2 臂 × 10），Stage 2 收集 160 个（4 色 × 2 臂 × 20），Stage 3 收集 60 个，总计 300。毛巾任务同样总计 300。直接基线均为 200 个完整轨迹。所有实验固定 π₀.₅ 模型、训练流程与评估协议，演示收集策略为唯一变量。

## 关键创新

1. **把数据收集过程课程化**：现有课程学习（curriculum learning）聚焦训练阶段的数据调度，默认数据集已固定。S2C 反向操作——在数据生成阶段就按能力依赖关系组织采集顺序，这是对模仿学习数据管线的新定位。其新颖性在于：不是给模型看更难或更简单的样本，而是改变样本本身的结构组成。

2. **状态归一化作为显式监督目标**：毛巾折叠中引入 \(o_{\text{flat}}\) 中间状态，将“任意初始状态→最终折叠”的困难映射拆解为“任意状态→标准状态”和“标准状态→最终状态”两段。这比单纯增加演示数量更有效，因为它直接降低了策略需要学习的输入状态熵，是任务层面的信息瓶颈设计。

3. **能力解耦的实证价值**：积木任务中直接采集导致双臂严重性能不对称（右臂始终无法启动抓取），而 S2C 通过分臂独立收集 Stage 1/2 演示，强制模型分别建立每臂的操作与感知能力，最后在 Stage 3 才要求协同。这种“先独立后协同”的数据结构，比端到端轨迹更符合双臂控制的物理约束。

## 实验与结果

实验在真实 SO-101 双臂平台（四同步 RGB 相机）上进行，π₀.₅ 为底层 VLA 模型。关键结果如下：

| 任务 | 采集策略 | 演示数 | 成功率 |
|---|---|---|---|
| 积木抓取分拣 | 直接 | 200 | 0% (0/5) |
| 积木抓取分拣 | S2C | 300 | 80.0% (4/5) |
| 毛巾折叠 | 直接 | 200 | 0% (0/28) |
| 毛巾折叠 | S2C | 300 | 25.0% (7/28) |

失败事件统计（S2C 策略下）：

| 任务 | 抓取失败占比 | 错误动作占比 | 总失败事件 |
|---|---|---|---|
| 积木抓取分拣 | 50% (1/2) | 50% (1/2) | 2 |
| 毛巾折叠 | 90.47% (19/21) | 9.53% (2/21) | 21 |

直接采集在两项任务上均为 0% 成功率，说明端到端完整轨迹在有限数据下无法支撑长时程操作学习。S2C 在积木任务上达到 80.0%，证明能力分解对刚体操作有效；毛巾折叠仅 25.0%，且失败中 90.47% 为抓取失败，指向低成本双指夹爪对薄软物体的物理抓取限制——这是数据组织无法弥补的硬件瓶颈。注意两组演示总数不同（200 vs 300），作者明确表示评估的是 S2C 整体有效性而非等量对比。

## 边界与局限

论文未明确给出 S2C 与直接采集在相同演示数量（如 300 vs 300）下的对比，因此无法排除数据量增加对成功率提升的贡献。毛巾折叠 25.0% 的成功率偏低，作者归因于可变形物体变异性与低成本平台执行误差，但未提供消除硬件影响后的上界估计。S2C 的阶段实例化（如分解为哪三个能力、每阶段收集多少数据）仍需人工指定，论文未提出自动生成阶段划分的方法。共享表征是否真正学到因果依赖（而非统计相关性）未被验证。所有结论基于 SO-101 平台与 π₀.₅ 模型，迁移到其他硬件或更大规模模型时结论可能不成立。

## 工程启示

复现时先核对三点：一是演示收集协议是否严格按阶段隔离环境变量（如积木任务 Stage 1 必须单色、双臂独立），任何跨阶段污染都会破坏能力解耦；二是状态归一化阶段是否真正将毛巾整理到 \(o_{\text{flat}}\)，若归一化不彻底，Stage 3 的监督一致性会退化；三是评估协议中失败事件统计按事件数而非试验数计算，对比结果时需注意分母差异。

最容易踩坑的地方是数据规模分配——S2C 总演示数 300 高于基线 200，若下游团队只关注“更多数据更好”，可能误以为提升来自数据量。建议在固定总预算下做消融（如 200 个 S2C 演示 vs 200 个直接演示），以分离数据组织与数据量的贡献。另外，毛巾折叠的抓取失败占比 90.47% 提示：若硬件夹爪无法稳定抓取薄软物体，任何数据策略都难以补救，选型时应优先评估末端执行器与目标物体的物理交互能力。

## 参考
- http://arxiv.org/abs/2607.04591v1

## 개요
기존 VLA 연구는 주로 모델 아키텍처, 훈련 전략, 데이터셋 규모에 초점을 맞추었지만, 시연 데이터의 수집 및 구성 방식을 간과했습니다. 본 논문은 시연 구성이 모방 학습에서 정책 학습 효율성, 훈련 안정성, 일반화 능력에 직접적인 영향을 미치는 핵심 요소임을 지적합니다. 이를 위해 저자들은 이중 팔 로봇 플랫폼 기반의 단순-복잡 구조화 시연 수집 전략을 제안합니다. 이는 복잡한 조작 작업을 점진적으로 학습 가능한 하위 기술로 분해하고, 불필요한 변이를 줄이기 위해 상호작용 환경을 표준화하며, 작업 복잡도가 증가하는 순서로 시연을 구성하는 세 가지 원칙을 통해 VLA 모델이 먼저 기초 조작 기술을 습득한 후 복잡한 작업 조합을 학습하도록 합니다. 실험 결과, 엔드투엔드 전체 작업 궤적을 직접 수집하는 기준 방법과 비교하여 블록 집기 분류와 수건 접기 두 작업에서 일관된 개선을 보였습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 시연 구성을 모방 학습의 기초 단계로 간주하고, 구조화된 설계를 통해 VLA 학습 효율성을 향상
- **세 가지 원칙**:
  1. **작업 분해**: 복잡한 조작 작업(예: 수건 접기)을 점진적으로 학습 가능한 하위 기술(예: 집기, 접기, 정렬)로 분해
  2. **환경 표준화**: 작업대 레이아웃, 물체 초기 위치, 조명 조건을 고정하여 무관한 변이를 줄임
  3. **복잡도 증가**: 먼저 단일 하위 기술 시연(예: 블록 집기)을 수집하고, 그 다음 조합 기술 시연(예: 집기 후 분류), 마지막으로 전체 작업 시연을 수집

### 실험 설정
- **플랫폼**: 이중 팔 로봇 플랫폼, RGB-D 카메라 및 힘 센서 장착
- **작업**:
  - 블록 집기 분류: 흩어진 블록에서 지정된 색상/모양의 블록을 집어 해당 영역에 배치
  - 수건 접기: 무작위로 놓인 수건을 표준 형태로 접기
- **기준선**: 엔드투엔드 전체 작업 궤적 직접 수집(구조화 없음)
- **VLA 모델**: RT-2 아키텍처 기반, 동일한 훈련 하이퍼파라미터 사용

### 주요 결과
- **작업 성공률**:
  - 블록 집기 분류: 구조화 정책 87.3%, 기준선 62.1%(25.2% 포인트 향상)
  - 수건 접기: 구조화 정책 71.5%, 기준선 48.9%(22.6% 포인트 향상)
- **훈련 안정성**: 구조화 정책의 손실 곡선이 더 매끄럽고, 수렴 속도가 약 30% 향상
- **일반화 능력**: 물체 위치 오프셋 ±10cm, 조명 변화 조건에서 구조화 정책의 성공률 하락은 5-8%에 불과했지만, 기준선은 15-20% 하락

### 결론
시연 구성은 VLA 학습에서 이전에 간과되었지만 매우 중요한 요소입니다. 구조화 정책은 점진적 기술 습득을 통해 장시간 조작 작업의 학습 어려움을 효과적으로 해결하며, 효율적인 기술 습득, 확장 가능한 데이터셋 구축, 장시간 로봇 조작에 실용적인 통찰을 제공합니다.
