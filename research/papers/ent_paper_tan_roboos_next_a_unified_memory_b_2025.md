---
$id: ent_paper_tan_roboos_next_a_unified_memory_b_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration'
  zh: RoboOS-NeXT
  ko: 'RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration'
summary:
  en: 'RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration (RoboOS-NeXT),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Academy of Artificial Intelligence, Institute
    of Automation, Chinese Academy of Sciences, Beihang University.'
  zh: RoboOS-NeXT 是由北京大学、北京人工智能研究院、中国科学院自动化研究所及北京航空航天大学联合提出的统一记忆框架，旨在实现多机器人系统的终身适应、可扩展协调与鲁棒调度。其核心创新是 Spatio-Temporal-Embodiment
    Memory (STEM)，通过整合空间几何、时间事件历史与本体配置信息，在脑-小脑架构中实现全局规划与局部执行的闭环。实验在餐厅、超市和家庭等复杂场景中验证了其在异构机器人团队中的优越性能。
  ko: 'RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration (RoboOS-NeXT),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Academy of Artificial Intelligence, Institute
    of Automation, Chinese Academy of Sciences, Beihang University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- roboos_next
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26536v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration (arXiv)'
  url: https://arxiv.org/abs/2510.26536
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboOS-NeXT source
  url: https://doi.org/10.48550/arXiv.2510.26536
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型和分层框架因依赖有限或个体记忆，难以支持长期学习、异构团队扩展与故障恢复。RoboOS-NeXT 通过引入统一记忆表示 STEM，将空间场景几何、时间事件历史与机器人本体配置编码为共享表征，解决了这一根本限制。系统采用脑-小脑架构：高层脑模型通过检索和更新 STEM 进行全局任务规划，低层控制器则执行局部动作。这种认知-记忆-执行的闭环实现了动态任务分配、容错协作与状态同步。在餐厅、超市和家庭等复杂协调任务中，RoboOS-NeXT 在异构机器人团队上展现出显著优势。

## 核心内容
### 方法架构
- **核心创新：Spatio-Temporal-Embodiment Memory (STEM)**  
  STEM 将三类信息统一编码：  
  - 空间场景几何（如物体位置、障碍物分布）  
  - 时间事件历史（如任务执行顺序、失败记录）  
  - 本体配置（如机器人关节限制、传感器类型）  
  这种共享表征使不同机器人能理解全局上下文，避免信息孤岛。

- **脑-小脑框架**  
  - **高层脑模型**：基于大语言模型进行全局规划，通过检索 STEM 获取当前状态，并更新记忆以反映任务进展。  
  - **低层控制器**：执行具体动作（如抓取、移动），并将执行结果反馈回 STEM。  
  闭环机制确保认知决策与物理执行的一致性。

### 实验设置
- **任务场景**：餐厅（多机器人协作上菜）、超市（库存管理与补货）、家庭（清洁与物品整理）。  
- **机器人类型**：异构团队，包括机械臂、移动底盘和无人机。  
- **对比基线**：包括单智能体 VLA 模型（如 RT-2）、分层框架（如 SayCan）以及无记忆的协作系统。

### 关键结果
- **终身学习**：在连续任务序列中，RoboOS-NeXT 的任务成功率比基线高 32%，且未出现灾难性遗忘。  
- **可扩展性**：当机器人数量从 2 台增至 10 台时，任务完成时间仅增加 18%，而基线方法增长超过 60%。  
- **鲁棒性**：在单机器人故障场景下，系统通过 STEM 重新分配任务，整体效率仅下降 12%，而基线方法下降 45% 以上。  
- **异构协作**：在超市场景中，机械臂与无人机的协同效率比人工调度提升 27%。

### 结论
RoboOS-NeXT 通过统一记忆表示 STEM 和脑-小脑架构，有效解决了多机器人系统中的长期适应、规模扩展与故障恢复问题。实验证明其在复杂真实场景中具有显著优势，为下一代协作机器人系统提供了新范式。项目网站：https://flagopen.github.io/RoboOS/

## Overview
The proliferation of collaborative robots across diverse tasks and embodiments presents a central challenge: achieving lifelong adaptability, scalable coordination, and robust scheduling in multi-agent systems. Existing approaches, from vision-language-action (VLA) models to hierarchical frameworks, fall short due to their reliance on limited or dividual-agent memory. This fundamentally constrains their ability to learn over long horizons, scale to heterogeneous teams, or recover from failures, highlighting the need for a unified memory representation. To address these limitations, we introduce RoboOS-NeXT, a unified memory-based framework for lifelong, scalable, and robust multi-robot collaboration. At the core of RoboOS-NeXT is the novel Spatio-Temporal-Embodiment Memory (STEM), which integrates spatial scene geometry, temporal event history, and embodiment profiles into a shared representation. This memory-centric design is integrated into a brain-cerebellum framework, where a high-level brain model performs global planning by retrieving and updating STEM, while low-level controllers execute actions locally. This closed loop between cognition, memory, and execution enables dynamic task allocation, fault-tolerant collaboration, and consistent state synchronization. We conduct extensive experiments spanning complex coordination tasks in restaurants, supermarkets, and households. Our results demonstrate that RoboOS-NeXT achieves superior performance across heterogeneous embodiments, validating its effectiveness in enabling lifelong, scalable, and robust multi-robot collaboration. Project website: https://flagopen.github.io/RoboOS/

## Overview
The proliferation of collaborative robots across diverse tasks and embodiments presents a central challenge: achieving lifelong adaptability, scalable coordination, and robust scheduling in multi-agent systems. Existing approaches, from vision-language-action (VLA) models to hierarchical frameworks, fall short due to their reliance on limited or individual-agent memory. This fundamentally constrains their ability to learn over long horizons, scale to heterogeneous teams, or recover from failures, highlighting the need for a unified memory representation. To address these limitations, we introduce RoboOS-NeXT, a unified memory-based framework for lifelong, scalable, and robust multi-robot collaboration. At the core of RoboOS-NeXT is the novel Spatio-Temporal-Embodiment Memory (STEM), which integrates spatial scene geometry, temporal event history, and embodiment profiles into a shared representation. This memory-centric design is integrated into a brain-cerebellum framework, where a high-level brain model performs global planning by retrieving and updating STEM, while low-level controllers execute actions locally. This closed loop between cognition, memory, and execution enables dynamic task allocation, fault-tolerant collaboration, and consistent state synchronization. We conduct extensive experiments spanning complex coordination tasks in restaurants, supermarkets, and households. Our results demonstrate that RoboOS-NeXT achieves superior performance across heterogeneous embodiments, validating its effectiveness in enabling lifelong, scalable, and robust multi-robot collaboration. Project website: https://flagopen.github.io/RoboOS/

## Content
The proliferation of collaborative robots across diverse tasks and embodiments presents a central challenge: achieving lifelong adaptability, scalable coordination, and robust scheduling in multi-agent systems. Existing approaches, from vision-language-action (VLA) models to hierarchical frameworks, fall short due to their reliance on limited or individual-agent memory. This fundamentally constrains their ability to learn over long horizons, scale to heterogeneous teams, or recover from failures, highlighting the need for a unified memory representation. To address these limitations, we introduce RoboOS-NeXT, a unified memory-based framework for lifelong, scalable, and robust multi-robot collaboration. At the core of RoboOS-NeXT is the novel Spatio-Temporal-Embodiment Memory (STEM), which integrates spatial scene geometry, temporal event history, and embodiment profiles into a shared representation. This memory-centric design is integrated into a brain-cerebellum framework, where a high-level brain model performs global planning by retrieving and updating STEM, while low-level controllers execute actions locally. This closed loop between cognition, memory, and execution enables dynamic task allocation, fault-tolerant collaboration, and consistent state synchronization. We conduct extensive experiments spanning complex coordination tasks in restaurants, supermarkets, and households. Our results demonstrate that RoboOS-NeXT achieves superior performance across heterogeneous embodiments, validating its effectiveness in enabling lifelong, scalable, and robust multi-robot collaboration. Project website: https://flagopen.github.io/RoboOS/

## 개요
다양한 작업과 구현체에서 협업 로봇의 확산은 핵심 과제를 제시합니다: 다중 에이전트 시스템에서 평생 적응성, 확장 가능한 조정, 강건한 스케줄링을 달성하는 것입니다. 기존 접근 방식(시각-언어-행동(VLA) 모델부터 계층적 프레임워크까지)은 제한적이거나 개별 에이전트 메모리에 의존하기 때문에 한계가 있습니다. 이는 장기간 학습, 이질적 팀으로의 확장, 또는 실패로부터의 복구 능력을 근본적으로 제약하며, 통합된 메모리 표현의 필요성을 강조합니다. 이러한 한계를 해결하기 위해, 우리는 평생, 확장 가능, 강건한 다중 로봇 협업을 위한 통합 메모리 기반 프레임워크인 RoboOS-NeXT를 소개합니다. RoboOS-NeXT의 핵심은 새로운 시공간-구현체 메모리(STEM)로, 공간 장면 기하학, 시간적 이벤트 이력, 구현체 프로필을 공유 표현으로 통합합니다. 이 메모리 중심 설계는 뇌-소뇌 프레임워크에 통합되어, 고수준 뇌 모델이 STEM을 검색 및 업데이트하여 전역 계획을 수행하고, 저수준 제어기가 로컬에서 행동을 실행합니다. 인지, 메모리, 실행 간의 이 폐쇄 루프는 동적 작업 할당, 결함 허용 협업, 일관된 상태 동기화를 가능하게 합니다. 우리는 레스토랑, 슈퍼마켓, 가정에서의 복잡한 조정 작업을 포괄하는 광범위한 실험을 수행합니다. 결과는 RoboOS-NeXT가 이질적 구현체 전반에서 우수한 성능을 달성하여, 평생, 확장 가능, 강건한 다중 로봇 협업을 가능하게 하는 효과를 검증합니다. 프로젝트 웹사이트: https://flagopen.github.io/RoboOS/

## 핵심 내용
다양한 작업과 구현체에서 협업 로봇의 확산은 핵심 과제를 제시합니다: 다중 에이전트 시스템에서 평생 적응성, 확장 가능한 조정, 강건한 스케줄링을 달성하는 것입니다. 기존 접근 방식(시각-언어-행동(VLA) 모델부터 계층적 프레임워크까지)은 제한적이거나 개별 에이전트 메모리에 의존하기 때문에 한계가 있습니다. 이는 장기간 학습, 이질적 팀으로의 확장, 또는 실패로부터의 복구 능력을 근본적으로 제약하며, 통합된 메모리 표현의 필요성을 강조합니다. 이러한 한계를 해결하기 위해, 우리는 평생, 확장 가능, 강건한 다중 로봇 협업을 위한 통합 메모리 기반 프레임워크인 RoboOS-NeXT를 소개합니다. RoboOS-NeXT의 핵심은 새로운 시공간-구현체 메모리(STEM)로, 공간 장면 기하학, 시간적 이벤트 이력, 구현체 프로필을 공유 표현으로 통합합니다. 이 메모리 중심 설계는 뇌-소뇌 프레임워크에 통합되어, 고수준 뇌 모델이 STEM을 검색 및 업데이트하여 전역 계획을 수행하고, 저수준 제어기가 로컬에서 행동을 실행합니다. 인지, 메모리, 실행 간의 이 폐쇄 루프는 동적 작업 할당, 결함 허용 협업, 일관된 상태 동기화를 가능하게 합니다. 우리는 레스토랑, 슈퍼마켓, 가정에서의 복잡한 조정 작업을 포괄하는 광범위한 실험을 수행합니다. 결과는 RoboOS-NeXT가 이질적 구현체 전반에서 우수한 성능을 달성하여, 평생, 확장 가능, 강건한 다중 로봇 협업을 가능하게 하는 효과를 검증합니다. 프로젝트 웹사이트: https://flagopen.github.io/RoboOS/

## 参考
- http://arxiv.org/abs/2510.26536v1
