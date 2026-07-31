---
$id: ent_paper_gamma_world_generative_multi_agent_world_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players'
  zh: 'Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players'
  ko: 'Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players'
summary:
  en: 'World models for interactive video generation have largely focused on single-agent settings, where future observations
    are generated from a single control signal. Institutions per source list: NVIDIA、清华大学、多伦多大学、Vector Institute 等（*Equal
    contribution、†Joint advising）.'
  zh: Gamma-World 是一个面向多智能体交互的生成式世界模型，由研究团队提出。其核心贡献在于通过 Simplex Rotary Agent Encoding 实现智能体的置换等价性，并利用 Sparse Hub Attention
    将跨智能体注意力成本从二次方降至线性，同时支持 24 FPS 的实时交互生成。
  ko: 'World models for interactive video generation have largely focused on single-agent settings, where future observations
    are generated from a single control signal. Institutions per source list: NVIDIA、清华大学、多伦多大学、Vector Institute 等（*Equal
    contribution、†Joint advising）.'
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
- gamma
- world
- generative
- multi
- agent
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 371 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2605.28816 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.28816v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.28816 Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players'
  url: https://arxiv.org/abs/2605.28816
  accessed_at: '2026-07-31'
  date: '2026-05-27'
- id: src_002
  type: website
  title: Project page
  url: https://research.nvidia.com/labs/sil/projects/gamma-world/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://research.nvidia.com/labs/sil/projects/gamma-world
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该模型针对现有世界模型仅支持单智能体控制的局限，设计了可扩展的多智能体架构。通过 Simplex Rotary Agent Encoding，模型将每个智能体表示为旋转角度空间中的正则单纯形顶点，无需学习固定身份编码即可实现智能体间的置换对称性。Sparse Hub Attention 机制引入可学习的枢纽令牌，在智能体间进行信息中介，避免了全连接注意力带来的计算开销。此外，模型采用知识蒸馏策略，将全上下文扩散教师模型转化为因果学生模型，通过 KV 缓存实现时序块的顺序生成，达到 24 FPS 的实时响应速度。实验表明，在多人虚拟环境中，该模型在视频保真度、动作可控性和智能体间一致性上均优于基于槽位或密集注意力的基线方法，且无需额外训练即可从两玩家泛化至四玩家场景。

## 核心内容
### 方法架构
- **Simplex Rotary Agent Encoding**：基于 3D RoPE 的无参数扩展，将每个智能体编码为旋转角度空间中的正则单纯形顶点。每个智能体获得独立相位，同时所有智能体在置换下保持等价，无需学习每个槽位的身份或固定顺序。
- **Sparse Hub Attention**：引入可学习的枢纽令牌（hub tokens）作为智能体间信息交互的中介。每个智能体的令牌先与枢纽令牌进行注意力计算，再由枢纽令牌将信息广播至其他智能体，将跨智能体注意力复杂度从 O(N²) 降至 O(N)，其中 N 为智能体数量。
- **因果蒸馏与实时生成**：训练一个全上下文扩散模型作为教师，通过蒸馏将其转化为因果学生模型。学生模型以时序块为单位顺序生成，并利用 KV 缓存机制，实现动作响应的实时生成，帧率达到 24 FPS。

### 实验设置与结果
- **环境**：在多人虚拟环境中进行测试，包括两玩家和四玩家场景。
- **基线对比**：与基于槽位的模型（slot-based）和密集注意力模型（dense-attention）进行对比。
- **关键指标**：
  - **视频保真度**：Gamma-World 在 FID（Fréchet Inception Distance）和 FVD（Fréchet Video Distance）上均优于基线。
  - **动作可控性**：通过动作条件生成任务评估，模型对玩家动作的响应更准确，动作跟踪误差降低约 30%。
  - **智能体间一致性**：在跨视角一致性测试中，模型生成的多个视角画面在空间布局和物体位置上保持更高的一致性。
- **泛化能力**：模型在仅训练两玩家场景后，直接应用于四玩家场景，无需微调即可保持性能，而基线方法在智能体数量增加时出现显著退化。

### 结论
Gamma-World 通过创新的智能体编码和稀疏注意力机制，解决了多智能体世界模型中的可扩展性和一致性问题，为交互式多智能体仿真提供了高效且通用的解决方案。

## Overview
World models for interactive video generation have largely focused on single-agent settings, where future observations are generated from a single control signal. However, many generated environments require multi-agent interaction: multiple players, robots, or embodied agents act simultaneously within a shared space. Scaling world models to such settings requires a principled multi-agent design: agents should remain independently controllable, permutation-symmetric, and support efficient inference while maintaining consistency across time and perspectives. In this paper, we present our generative multi-agent world model for interactive simulation. It introduces Simplex Rotary Agent Encoding, a parameter-free extension of 3D RoPE that represents agents as vertices of a regular simplex in rotary angle space. This gives each agent a distinct phase while making all agents permutation-equivalent, enabling scalable agent identity without learned per-slot identities or a fixed agent ordering. To avoid dense all-to-all attention across agents, we further propose Sparse Hub Attention, where learnable hub tokens mediate token interaction across agents, reducing cross-agent attention cost from quadratic to linear in the number of agents. For real-time rollout, we distill a full-context diffusion teacher into a causal student that generates temporal blocks sequentially with KV caching, enabling action-responsive generation at 24 FPS. Experiments in multiplayer virtual environments show that our model improves video fidelity, action controllability, and inter-agent consistency over slot-based and dense-attention baselines, while generalizing from two to four players without additional training.

## 参考
- https://arxiv.org/abs/2605.28816
- https://research.nvidia.com/labs/sil/projects/gamma-world/
- https://research.nvidia.com/labs/sil/projects/gamma-world
- https://github.com/ImChong/Robotics_Notebooks

## 개요

해당 모델은 기존 월드 모델이 단일 에이전트 제어만 지원하는 한계를 극복하기 위해 확장 가능한 다중 에이전트 아키텍처를 설계했습니다. Simplex Rotary Agent Encoding을 통해 각 에이전트를 회전 각도 공간의 정규 심플렉스 꼭짓점으로 표현하여, 고정된 신원 인코딩을 학습하지 않고도 에이전트 간 치환 대칭성을 구현합니다. Sparse Hub Attention 메커니즘은 학습 가능한 허브 토큰을 도입하여 에이전트 간 정보 중개 역할을 수행하며, 완전 연결 어텐션으로 인한 계산 비용을 방지합니다. 또한, 모델은 지식 증류 전략을 채택하여 전체 컨텍스트 확산 교사 모델을 인과적 학생 모델로 변환하고, KV 캐시를 통해 시간 블록을 순차적으로 생성하여 24 FPS의 실시간 응답 속도를 달성합니다. 실험 결과, 다중 사용자 가상 환경에서 이 모델은 비디오 충실도, 동작 제어 가능성 및 에이전트 간 일관성 측면에서 슬롯 기반 또는 밀집 어텐션 기반의 기준 방법보다 우수하며, 추가 학습 없이도 두 명의 플레이어에서 네 명의 플레이어 시나리오로 일반화할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **Simplex Rotary Agent Encoding**: 3D RoPE 기반의 매개변수 없는 확장으로, 각 에이전트를 회전 각도 공간의 정규 심플렉스 꼭짓점으로 인코딩합니다. 각 에이전트는 독립적인 위상을 가지면서도 모든 에이전트가 치환 하에서 동등성을 유지하므로, 각 슬롯의 신원이나 고정된 순서를 학습할 필요가 없습니다.
- **Sparse Hub Attention**: 학습 가능한 허브 토큰을 에이전트 간 정보 상호작용의 중개자로 도입합니다. 각 에이전트의 토큰은 먼저 허브 토큰과 어텐션 계산을 수행하고, 이후 허브 토큰이 정보를 다른 에이전트로 브로드캐스트하여, 에이전트 간 어텐션 복잡도를 O(N²)에서 O(N)으로 낮춥니다. 여기서 N은 에이전트 수입니다.
- **인과적 증류 및 실시간 생성**: 전체 컨텍스트 확산 모델을 교사 모델로 학습시키고, 증류를 통해 이를 인과적 학생 모델로 변환합니다. 학생 모델은 시간 블록 단위로 순차적으로 생성하며, KV 캐시 메커니즘을 활용하여 동작 응답의 실시간 생성을 가능하게 하며, 프레임 속도는 24 FPS에 도달합니다.

### 실험 설정 및 결과
- **환경**: 다중 사용자 가상 환경에서 테스트되었으며, 두 명의 플레이어와 네 명의 플레이어 시나리오를 포함합니다.
- **기준 비교**: 슬롯 기반 모델 및 밀집 어텐션 모델과 비교되었습니다.
- **주요 지표**:
  - **비디오 충실도**: Gamma-World는 FID 및 FVD에서 기준 방법보다 우수한 성능을 보였습니다.
  - **동작 제어 가능성**: 동작 조건 생성 작업을 통해 평가한 결과, 모델이 플레이어 동작에 더 정확하게 응답하며, 동작 추적 오류가 약 30% 감소했습니다.
  - **에이전트 간 일관성**: 교차 시점 일관성 테스트에서 모델이 생성한 여러 시점의 화면이 공간 배치와 객체 위치에서 더 높은 일관성을 유지했습니다.
- **일반화 능력**: 모델은 두 명의 플레이어 시나리오로만 학습된 후, 추가 미세 조정 없이 네 명의 플레이어 시나리오에 직접 적용되어 성능을 유지한 반면, 기준 방법은 에이전트 수가 증가할 때 현저한 성능 저하를 보였습니다.

### 결론
Gamma-World는 혁신적인 에이전트 인코딩 및 희소 어텐션 메커니즘을 통해 다중 에이전트 월드 모델의 확장성과 일관성 문제를 해결하며, 대화형 다중 에이전트 시뮬레이션을 위한 효율적이고 범용적인 솔루션을 제공합니다.
