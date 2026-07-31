---
$id: ent_paper_omnicontact_chaining_meta_skills_contact_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation'
  zh: 'OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation'
  ko: 'OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation'
summary:
  en: 'Learning long-horizon humanoid loco-manipulation poses a dual challenge: it requires not only the robust execution
    of meta-skills but also their seamless, closed-loop chaining equipped with autonomous recovery. Institutions per source
    list: 诺亦腾机器人（Noitom Robotics）、香港科技大学（HKUST）、武汉大学（WHU）、香港大学（HKU）.'
  zh: OmniContact 是一个面向人形机器人全身移动操作任务的层次化框架，由上海交通大学等机构提出。其核心创新在于引入“接触流（Contact Flow）”这一紧凑表示，包含关键身体轨迹与时间序列二值接触信号，并以此为基础构建了低层技能库（CF-Track）与高层规划器（CF-Gen）。实验表明，该方法在长时序任务中成功率显著优于现有基线，并能与
    VLM 结合实现语义驱动的复杂行为。
  ko: 'Learning long-horizon humanoid loco-manipulation poses a dual challenge: it requires not only the robust execution
    of meta-skills but also their seamless, closed-loop chaining equipped with autonomous recovery. Institutions per source
    list: 诺亦腾机器人（Noitom Robotics）、香港科技大学（HKUST）、武汉大学（WHU）、香港大学（HKU）.'
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
- omnicontact
- chaining
- meta
- skills
- contact
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 727 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.26201 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.26201v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.26201 OmniContact: Chaining Meta-Skills via Contact Flow for Generalizable Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2606.26201
  accessed_at: '2026-07-31'
  date: '2026-06-24'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

人形机器人执行长时序移动操作任务面临双重挑战：既要稳健执行元技能，又要实现闭环链式组合与自主恢复。现有方法中，显式的人-物交互表示虽精确但难以用于高层规划，隐式技能嵌入虽紧凑却缺乏可解释性。OmniContact 框架以接触流（Contact Flow）为核心表示，低层策略 CF-Track 学习统一的移动操作技能库，高层模块 CF-Gen 则启发式地合成未来接触流序列。此外，团队还收集了基于动作捕捉的 OmniContact 数据集，支持该框架的训练与评估。该框架能实现稳健执行、自主故障恢复以及元技能的灵活组合，并自然集成 VLM 进行语义任务分解。

## 核心内容
### 方法架构
OmniContact 是一个层次化框架，核心是**接触流（Contact Flow, CF）**，一种紧凑表示，包含：
- 关键身体轨迹（如双手、双脚的 3D 位置）
- 时间序列二值接触信号（指示身体部位是否与物体或地面接触）

框架由两个主要模块组成：
- **CF-Track（低层策略）**：学习一个统一的移动操作技能库，以接触流为共享接口，实现多种元技能的稳健执行。
- **CF-Gen（高层规划器）**：启发式地合成未来接触流序列，用于任务规划与自主恢复。

### 数据集
团队收集了 **OmniContact 数据集**，这是一个基于动作捕捉（MoCap）的人-物交互（HOI）语料库，专门针对人形机器人移动操作任务设计（详见附录）。

### 实验设置与关键结果
实验在多个长时序任务上进行，关键数字如下：
- **Carry Box 任务**：成功率 **98.7%**
- **Push-Stack Boxes 任务**：成功率 **76.5%**
- 相比先前基线，在元技能执行上平均提升 **40.9%**，在技能链式组合上平均提升 **66.5%**

### 结论与扩展
- 框架能实现稳健执行、自主故障恢复以及元技能的灵活组合。
- 自然集成视觉语言模型（VLM）进行语义任务分解，例如将散落的箱子排列成心形，展示了复杂、语义驱动的移动操作行为。

## Overview
Learning long-horizon humanoid loco-manipulation poses a dual challenge: it requires not only the robust execution of meta-skills but also their seamless, closed-loop chaining equipped with autonomous recovery. Existing approaches remain limited: explicit humanoid-object interaction representations offer precision but are notoriously difficult for high-level planning, whereas implicit skill embeddings are compact but lack the interpretability required for reliable composition. We propose \ours, a hierarchical framework centered on \textbf{contact flow (CF)}, a compact representation consisting of key body trajectories and time-series binary contact signals. Leveraging this shared interface, our low-level policy \textbf{CF-Track} learns a unified library of loco-manipulation skills, while our high-level module \textbf{CF-Gen} heuristically synthesizes future contact-flow sequences. To support this setting, we additionally collect the OmniContact dataset, a MoCap-based HOI corpus for humanoid loco-manipulation (Appendix~\ref{sec:dataset}). Together, they enable robust execution, autonomous failure recovery, and flexible composition of meta-skills for long-horizon tasks. Experiments show that OmniContact achieves \(98.7\%\) success on \textit{Carry Box} and \(76.5\%\) on \textit{Push-Stack Boxes}, outperforming prior baselines by average margins of \(40.9\%\) in meta-skill and \(66.5\%\) in skill chaining. Besides, our framework naturally integrates with VLMs for semantic task decomposition, enabling complex, semantically grounded loco-manipulation behaviors, such as arranging scattered boxes into a heart shape.

## 参考
- https://arxiv.org/abs/2606.26201
- https://github.com/ImChong/Robotics_Notebooks

## 개요

휴머노이드 로봇이 장시간 연속 이동 조작 작업을 수행할 때는 두 가지 도전 과제가 있습니다: 기본 기술을 안정적으로 실행하는 동시에 폐쇄 루프 체인 조합과 자율 복구를 실현해야 합니다. 기존 방법 중 명시적 인간-물체 상호작용 표현은 정확하지만 고수준 계획에 사용하기 어렵고, 암시적 기술 임베딩은 간결하지만 해석 가능성이 부족합니다. OmniContact 프레임워크는 접촉 흐름(Contact Flow)을 핵심 표현으로 사용하며, 저수준 정책 CF-Track은 통합된 이동 조작 기술 라이브러리를 학습하고, 고수준 모듈 CF-Gen은 휴리스틱 방식으로 미래 접촉 흐름 시퀀스를 합성합니다. 또한 팀은 모션 캡처 기반의 OmniContact 데이터셋을 수집하여 이 프레임워크의 훈련과 평가를 지원합니다. 이 프레임워크는 안정적 실행, 자율 장애 복구, 기본 기술의 유연한 조합을 실현하며, VLM을 자연스럽게 통합하여 의미론적 작업 분해를 수행합니다.

## 핵심 내용
### 방법 아키텍처
OmniContact는 계층적 프레임워크로, 핵심은 **접촉 흐름(Contact Flow, CF)**이며, 이는 다음과 같은 간결한 표현을 포함합니다:
- 주요 신체 궤적(예: 양손, 양발의 3D 위치)
- 시계열 이진 접촉 신호(신체 부위가 물체나 지면에 접촉하는지 여부를 나타냄)

프레임워크는 두 가지 주요 모듈로 구성됩니다:
- **CF-Track(저수준 정책)**: 접촉 흐름을 공유 인터페이스로 사용하여 통합된 이동 조작 기술 라이브러리를 학습하며, 다양한 기본 기술의 안정적 실행을 가능하게 합니다.
- **CF-Gen(고수준 계획기)**: 휴리스틱 방식으로 미래 접촉 흐름 시퀀스를 합성하여 작업 계획 및 자율 복구에 사용합니다.

### 데이터셋
팀은 **OmniContact 데이터셋**을 수집했습니다. 이는 모션 캡처(MoCap) 기반의 인간-물체 상호작용(HOI) 코퍼스로, 휴머노이드 로봇의 이동 조작 작업을 위해 특별히 설계되었습니다(자세한 내용은 부록 참조).

### 실험 설정 및 주요 결과
실험은 여러 장시간 연속 작업에서 수행되었으며, 주요 수치는 다음과 같습니다:
- **Carry Box 작업**: 성공률 **98.7%**
- **Push-Stack Boxes 작업**: 성공률 **76.5%**
- 이전 기준선 대비 기본 기술 실행에서 평균 **40.9%** 향상, 기술 체인 조합에서 평균 **66.5%** 향상

### 결론 및 확장
- 프레임워크는 안정적 실행, 자율 장애 복구, 기본 기술의 유연한 조합을 실현합니다.
- 시각 언어 모델(VLM)을 자연스럽게 통합하여 의미론적 작업 분해를 수행합니다. 예를 들어 흩어진 상자를 하트 모양으로 배열하는 등 복잡하고 의미론적으로 구동되는 이동 조작 동작을 보여줍니다.
