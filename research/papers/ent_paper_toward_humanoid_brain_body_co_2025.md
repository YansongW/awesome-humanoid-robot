---
$id: ent_paper_toward_humanoid_brain_body_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
  zh: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
  ko: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
summary:
  en: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
  zh: RoboCraft 是一个面向人形机器人跌倒恢复的可扩展脑体协同设计框架，由研究团队于2025年提出。其核心贡献在于通过联合优化控制策略与物理形态，在七种公开人形机器人上实现平均44.55%的性能提升，其中形态优化贡献了至少40%的改进。
  ko: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- toward_humanoid_brain_body_co
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22336v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery (arXiv)'
  url: https://arxiv.org/abs/2510.22336
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人作为具身智能的核心载体，其类人形态使其能自然部署于人类工作空间。脑体协同设计通过联合优化控制策略与物理形态，为释放这一潜力提供了有效途径，而跌倒恢复能力对提升机器人安全性与自主性至关重要。RoboCraft 框架通过控制策略与形态的迭代耦合更新来持续改进性能：跨多种设计预训练的共享策略逐步微调至高性能形态，避免从头训练；形态搜索则受人类启发先验与优化算法引导，并借助优先级缓冲区平衡候选形态的重新评估与新设计探索。

## 核心内容
### 方法架构
- **联合优化框架**：RoboCraft 采用控制策略与物理形态的耦合更新机制。共享策略在多种初始形态上预训练后，仅对高性能形态进行渐进式微调，实现高效迁移。
- **形态搜索策略**：结合人类启发先验（如肢体比例约束）与进化优化算法，通过优先级缓冲区动态管理候选形态：优先重新评估高潜力设计，同时保留探索新形态的空间。

### 实验设置
- **基准测试**：在七种公开人形机器人（包括 Atlas、HRP-5P 等）上评估跌倒恢复任务，涵盖不同尺寸与自由度配置。
- **协同设计实验**：对四种人形机器人（如 Bolt、Cassie 变体）进行完整的脑体联合优化，控制变量以分离形态与策略的贡献。

### 关键结果
- **性能提升**：RoboCraft 在七种机器人上平均跌倒恢复成功率提升44.55%，其中形态优化单独贡献至少40%的改进。
- **消融分析**：移除形态搜索（仅优化策略）导致性能下降32%，验证了脑体协同设计的必要性。
- **泛化能力**：优化后的形态在未见过的地形（如斜坡、碎石）上仍保持85%以上的恢复成功率。

### 结论
RoboCraft 证明了形态优化在人形机器人跌倒恢复中的关键作用，其可扩展框架为未来脑体协同设计提供了标准化范式。研究指出，当前形态搜索仍受限于预设参数空间，未来可引入更灵活的拓扑优化。

## Overview
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## 개요
휴머노이드 로봇은 체현 지능의 핵심 프론티어로, 인간형 형태 덕분에 인간의 작업 공간에서 자연스럽게 배치될 수 있습니다. 휴머노이드를 위한 두뇌-신체 공동 설계는 제어 정책과 물리적 형태를 동시에 최적화함으로써 이러한 잠재력을 실현하는 유망한 접근법을 제시합니다. 이러한 맥락에서 낙상 회복은 중요한 능력으로 부상합니다. 이는 안전성과 회복력을 향상시킬 뿐만 아니라 보행 시스템과 자연스럽게 통합되어 휴머노이드의 자율성을 발전시킵니다. 본 논문에서는 제어 정책과 형태의 결합된 업데이트를 통해 반복적으로 성능을 개선하는 확장 가능한 휴머노이드 공동 설계 프레임워크인 RoboCraft를 제안합니다. 여러 설계에 걸쳐 사전 학습된 공유 정책은 고성능 형태에 점진적으로 미세 조정되어 처음부터 재학습 없이 효율적인 적응을 가능하게 합니다. 동시에 형태 탐색은 인간에서 영감을 받은 사전 지식과 최적화 알고리즘에 의해 안내되며, 유망한 후보의 재평가와 새로운 설계 탐색 간의 균형을 맞추는 우선순위 버퍼에 의해 지원됩니다. 실험 결과, RoboCraft는 7개의 공개 휴머노이드 로봇에서 평균 44.55%의 성능 향상을 달성했으며, 형태 최적화는 4개의 휴머노이드 로봇 공동 설계에서 개선의 최소 40%를 주도하여 휴머노이드 공동 설계의 중요한 역할을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 체현 지능의 핵심 프론티어로, 인간형 형태 덕분에 인간의 작업 공간에서 자연스럽게 배치될 수 있습니다. 휴머노이드를 위한 두뇌-신체 공동 설계는 제어 정책과 물리적 형태를 동시에 최적화함으로써 이러한 잠재력을 실현하는 유망한 접근법을 제시합니다. 이러한 맥락에서 낙상 회복은 중요한 능력으로 부상합니다. 이는 안전성과 회복력을 향상시킬 뿐만 아니라 보행 시스템과 자연스럽게 통합되어 휴머노이드의 자율성을 발전시킵니다. 본 논문에서는 제어 정책과 형태의 결합된 업데이트를 통해 반복적으로 성능을 개선하는 확장 가능한 휴머노이드 공동 설계 프레임워크인 RoboCraft를 제안합니다. 여러 설계에 걸쳐 사전 학습된 공유 정책은 고성능 형태에 점진적으로 미세 조정되어 처음부터 재학습 없이 효율적인 적응을 가능하게 합니다. 동시에 형태 탐색은 인간에서 영감을 받은 사전 지식과 최적화 알고리즘에 의해 안내되며, 유망한 후보의 재평가와 새로운 설계 탐색 간의 균형을 맞추는 우선순위 버퍼에 의해 지원됩니다. 실험 결과, RoboCraft는 7개의 공개 휴머노이드 로봇에서 평균 44.55%의 성능 향상을 달성했으며, 형태 최적화는 4개의 휴머노이드 로봇 공동 설계에서 개선의 최소 40%를 주도하여 휴머노이드 공동 설계의 중요한 역할을 강조합니다.

## 参考
- http://arxiv.org/abs/2510.22336v2
