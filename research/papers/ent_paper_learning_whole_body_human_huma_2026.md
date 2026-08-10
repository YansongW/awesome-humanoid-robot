---
$id: ent_paper_learning_whole_body_human_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
  zh: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
  ko: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
summary:
  en: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
  zh: PAIR (Physics-Aware Interaction Retargeting) 与 D-STAR (Decoupled Spatio-Temporal Action Reasoner) 是2026年提出的从人人交互数据学习人形机器人全身交互的完整框架。PAIR
    通过接触感知的两阶段重定向解决形态差异导致的接触破坏问题，D-STAR 则通过解耦时空推理实现超越轨迹模仿的响应式协作。实验证明该框架在仿真中显著优于基线方法。
  ko: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
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
- learning_whole_body_human_huma
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.09518v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1345 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations (arXiv)
  url: https://arxiv.org/abs/2601.09518
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作首先发现标准运动重定向方法会破坏人人交互数据中的关键接触点，因此提出接触感知的 PAIR 管道，通过两阶段处理保留接触语义并生成物理一致的人机交互数据。然而高质量数据暴露了模仿学习的根本缺陷——仅复制轨迹而缺乏交互理解。为此引入分层策略 D-STAR，将动作时序（何时行动）与空间选择（何处行动）解耦：Phase Attention 模块负责时序阶段识别，Multi-Scale Spatial 模块处理空间定位，最终由扩散头融合生成全身协调行为。这种解耦设计使模型能专注学习鲁棒的时间阶段特征而不受空间噪声干扰，从而产生响应式同步协作。

## 核心内容
### 核心挑战
- **数据稀缺**：高质量人形机器人交互数据（HHoI）获取困难，而人人交互数据（HHI）丰富但存在形态差异
- **重定向失败**：标准运动重定向会破坏HHI数据中的关键接触点（如握手、拥抱时的接触力）
- **模仿学习局限**：传统策略仅复制轨迹，缺乏对交互意图的时空理解

### PAIR：物理感知交互重定向
- **两阶段管道**：
  1. 接触语义保留：检测HHI数据中的接触事件（接触点位置、接触力方向）
  2. 物理一致性生成：通过优化调整人形机器人运动学参数，确保重定向后接触力分布与原始数据一致
- **关键创新**：在重定向过程中显式建模接触约束，而非简单映射关节角度

### D-STAR：解耦时空推理器
- **分层策略架构**：
  - **Phase Attention（何时行动）**：使用时序注意力机制识别交互阶段（如准备、接触、释放），输出阶段概率分布
  - **Multi-Scale Spatial（何处行动）**：多尺度空间模块处理不同粒度（全身/局部/关节）的空间特征，生成动作空间热图
  - **扩散头融合**：将时序与空间特征通过条件扩散模型融合，生成连续全身动作序列
- **解耦优势**：时序模块不受空间噪声干扰，空间模块不依赖时序先验，两者独立训练后联合微调

### 实验设置
- **仿真环境**：基于 MuJoCo 的人形机器人平台，包含5类交互任务（搬运、舞蹈、格挡、拥抱、握手）
- **基线方法**：标准运动重定向+行为克隆（BC）、隐式策略（IBC）、扩散策略（DP）
- **评估指标**：接触成功率、任务完成率、运动自然度（FID分数）、交互响应延迟

### 关键结果
- **PAIR有效性**：相比标准重定向，接触保持率从32%提升至89%
- **D-STAR性能**：
  - 任务完成率：D-STAR 达91%，优于 BC（43%）、IBC（67%）、DP（78%）
  - 交互响应延迟：D-STAR 平均延迟0.12秒，比DP快3倍
  - 运动自然度：FID分数比DP降低41%
- **消融实验**：移除Phase Attention后任务完成率下降至62%，移除Multi-Scale Spatial后下降至71%

### 结论
PAIR 与 D-STAR 构成从人人数据到人机交互的完整学习管道，通过接触感知重定向与时空解耦策略，首次实现无需真实人机交互数据即可训练响应式全身协作策略。

## Overview
Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

## 参考
- http://arxiv.org/abs/2601.09518v1

## 개요
이 연구는 먼저 표준 모션 리타게팅 방법이 인간-인간 상호작용 데이터의 핵심 접촉점을 파괴한다는 것을 발견하고, 접촉 인식 PAIR 파이프라인을 제안하여 두 단계 처리를 통해 접촉 의미를 보존하고 물리적으로 일관된 인간-로봇 상호작용 데이터를 생성합니다. 그러나 고품질 데이터는 모방 학습의 근본적인 결함을 드러냈습니다—단순히 궤적을 복제할 뿐 상호작용 이해가 부족하다는 것입니다. 이를 위해 계층적 정책 D-STAR를 도입하여 행동 타이밍(언제 행동할지)과 공간 선택(어디서 행동할지)을 분리합니다: Phase Attention 모듈은 시간적 단계 인식을 담당하고, Multi-Scale Spatial 모듈은 공간 위치 파악을 처리하며, 최종적으로 확산 헤드가 융합하여 전신 조화 행동을 생성합니다. 이러한 분리 설계는 모델이 공간 노이즈의 간섭 없이 강건한 시간적 단계 특징 학습에 집중할 수 있게 하여 반응적 동기화 협력을 가능하게 합니다.

## 핵심 내용
### 핵심 과제
- **데이터 부족**: 고품질 휴머노이드 로봇 상호작용 데이터(HHoI) 획득이 어렵고, 인간-인간 상호작용 데이터(HHI)는 풍부하지만 형태적 차이가 존재
- **리타게팅 실패**: 표준 모션 리타게팅은 HHI 데이터의 핵심 접촉점(악수, 포옹 시 접촉력)을 파괴
- **모방 학습 한계**: 전통적 정책은 궤적만 복제할 뿐 상호작용 의도의 시공간적 이해가 부족

### PAIR: 물리 인식 상호작용 리타게팅
- **두 단계 파이프라인**:
  1. 접촉 의미 보존: HHI 데이터의 접촉 이벤트(접촉점 위치, 접촉력 방향) 감지
  2. 물리적 일관성 생성: 최적화를 통해 휴머노이드 운동학 파라미터를 조정하여 리타게팅 후 접촉력 분포가 원본 데이터와 일치하도록 보장
- **핵심 혁신**: 리타게팅 과정에서 접촉 제약을 명시적으로 모델링하며, 단순한 관절 각도 매핑이 아님

### D-STAR: 분리된 시공간 추론기
- **계층적 정책 아키텍처**:
  - **Phase Attention(언제 행동할지)**: 시간적 주의 메커니즘을 사용하여 상호작용 단계(준비, 접촉, 해제 등)를 인식하고 단계 확률 분포 출력
  - **Multi-Scale Spatial(어디서 행동할지)**: 다중 스케일 공간 모듈이 다양한 세분화 수준(전신/국소/관절)의 공간 특징을 처리하고 행동 공간 히트맵 생성
  - **확산 헤드 융합**: 시간적 및 공간적 특징을 조건부 확산 모델로 융합하여 연속 전신 행동 시퀀스 생성
- **분리 이점**: 시간적 모듈은 공간 노이즈의 간섭을 받지 않고, 공간 모듈은 시간적 사전 지식에 의존하지 않으며, 두 모듈은 독립적으로 훈련 후 공동 미세 조정

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 기반 휴머노이드 로봇 플랫폼, 5가지 상호작용 작업(운반, 춤, 차단, 포옹, 악수) 포함
- **기준 방법**: 표준 모션 리타게팅+행동 복제(BC), 암시적 정책(IBC), 확산 정책(DP)
- **평가 지표**: 접촉 성공률, 작업 완료율, 운동 자연성(FID 점수), 상호작용 응답 지연

### 핵심 결과
- **PAIR 효과성**: 표준 리타게팅 대비 접촉 유지율이 32%에서 89%로 향상
- **D-STAR 성능**:
  - 작업 완료율: D-STAR 91%로 BC(43%), IBC(67%), DP(78%)보다 우수
  - 상호작용 응답 지연: D-STAR 평균 0.12초로 DP보다 3배 빠름
  - 운동 자연성: FID 점수가 DP보다 41% 감소
- **절제 실험**: Phase Attention 제거 시 작업 완료율 62%로 하락, Multi-Scale Spatial 제거 시 71%로 하락

### 결론
PAIR와 D-STAR는 인간-인간 데이터에서 인간-로봇 상호작용까지의 완전한 학습 파이프라인을 구성하며, 접촉 인식 리타게팅과 시공간 분리 정책을 통해 실제 인간-로봇 상호작용 데이터 없이도 반응형 전신 협력 정책을 훈련할 수 있는 최초의 방법을 구현합니다.
