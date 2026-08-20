---
$id: ent_paper_asap_aligning_simulation_real_world_phys
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills
  zh: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills
  ko: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills
summary:
  en: 'Conservative card from a lab paper list entry: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills.
    No fetchable paper URL was recorded; content to be supplemented.'
  zh: 【内容待补】据实验室论文清单登记：ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills，发表机构未知。清单未登记可抓取的论文页（待补充/空），本卡仅收录清单登记信息，概述与核心内容待补充。
  ko: 'Conservative card from a lab paper list entry: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills.
    No fetchable paper URL was recorded; content to be supplemented.'
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
- asap
- aligning
- simulation
- real
- world
- needs_content
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 426 (.staging/ingest_yuanxq). Tier C->conservative. Conservative card:
    清单未登记可抓取的论文页（待补充/空）; only list-registered fields recorded, content to be supplemented. | WP4 2026-08-11: merged methods/-resident
    duplicate card ent_paper_asap_aligning_simulation_real_world_phys into this card (same subject; 1 sources merged; appended sections: ### 是什么：ASAP
    框架的准确定义, ### 为什么存在：痛点与历史定位, ### 原理拆解, ### 关键参数与规格, ### 横向对比, ### 谁在用·应用案例, ### 局限与边界, ### 常见误区, ### 相关知识, ### 왜 존재하는가:痛点과
    역사적 위치). Manifest: .staging/cleanup_wp12/manifest_wp4_methods_paper_cards.json'
sources:
- id: src_001
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: ASAP Framework
  url: https://agile.human2humanoid.com/
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述

【内容待补】据实验室论文清单登记：ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills，发表机构未知。清单未登记可抓取的论文页（待补充/空），本卡仅收录清单登记信息，概述与核心内容待补充。

## 核心内容
### 清单登记信息
- **论文题目**：ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills
- **发表机构**：未知
- **来源文章**：《GitHub仓库 Robotics_Notebooks》 https://github.com/ImChong/Robotics_Notebooks

### 内容待补
- 本卡为保守卡：清单未提供可抓取的论文页，仅登记题目与机构信息；后续获得论文原文或摘要后补充概述与核心内容。

## 参考
- https://github.com/ImChong/Robotics_Notebooks


## 补充内容（合并自原方法卡 ent_paper_asap_aligning_simulation_real_world_phys）

#### 是什么：ASAP 框架的准确定义
ASAP 框架（Aligning Simulation and Real Physics）是一种用于学习敏捷人形机器人全身技能的两阶段 Sim-to-Real 框架。其核心思想是：先在仿真环境中预训练运动跟踪策略，再通过真实世界数据训练一个残差（delta）动作模型来补偿动力学不匹配，最后将该模型集成回仿真器对策略进行微调。

该框架由 Tairan He、Zhengyi Luo、Xialin He 等人提出，发表于 Robotics: Science and Systems (RSS) 2025，并在 CoRL 2024 的 Spotlight WCBM Workshop 与 X-Embodiment Workshop 中展示。ASAP 的评估覆盖三种迁移场景：IsaacGym 到 IsaacSim、IsaacGym 到 Genesis、IsaacGym 到真实 Unitree G1 人形机器人。

#### 为什么存在：痛点与历史定位
人形机器人要实现类人的全身敏捷技能，面临的核心障碍是**动力学不匹配（dynamics mismatch）**——仿真环境与真实物理世界之间存在系统性的差异，包括摩擦、惯性、执行器延迟、柔性变形等。这些差异导致在仿真中表现优异的策略部署到真实机器人上时性能急剧下降。

在 ASAP 之前，主流方案存在明显缺陷：

- **系统辨识（SysID）**：需要大量人工参数调优，且辨识结果难以覆盖全部动力学特性。
- **域随机化（DR）**：通过随机化仿真参数增强策略鲁棒性，但往往导致策略过于保守，牺牲了敏捷性。

ASAP 的定位正是填补这一空白：它不需要精确的系统辨识，也不牺牲策略的敏捷性，而是通过数据驱动的残差学习来对齐仿真与真实物理。它真正改变的不是"仿真有多准"，而是"策略对仿真误差有多不敏感"。

#### 原理拆解
**① 两阶段训练架构**

ASAP 的第一阶段在仿真环境中使用重定向的人类运动数据预训练全身运动跟踪策略。这一阶段的目标是让策略学会基本的动态运动技能，如跳跃、踢腿、舞蹈等。

第二阶段包含三个关键步骤：

1. **真实数据收集**：将预训练策略部署到真实机器人上，收集真实世界的状态-动作数据。
2. **残差动作模型训练**：基于收集的数据训练一个 delta action model，用于预测仿真策略输出动作与真实最优动作之间的残差。
3. **策略微调**：将训练好的残差动作模型集成到仿真器中，对预训练策略进行微调，使其与真实世界动力学对齐。

**② 残差动作学习的数学本质**

残差动作模型的核心假设是：仿真与真实之间的动力学差异可以表示为动作空间中的一个可学习的偏移量。设仿真策略输出的动作为 \(a_{\text{sim}}\)，真实世界的最优动作为 \(a_{\text{real}}\)，则残差模型学习映射：

$$
a_{\text{real}} = a_{\text{sim}} + \Delta(a_{\text{sim}}, s)
$$

其中 \(\Delta(a_{\text{sim}}, s)\) 是残差动作模型，以仿真动作和当前状态 \(s\) 为输入。这一设计的巧妙之处在于：残差通常远小于完整动作，因此学习问题被简化，模型可以更快收敛且泛化性更好。

**③ 与力控和柔顺控制的关联**

ASAP 框架与力控制、阻抗控制等技术存在互补关系。语料中提到的串联弹性执行器（SEA）通过测量弹性体变形 \(\Delta \theta\) 估计输出力，满足 \(\tau = k \Delta \theta\)，其中 \(k\) 为弹性刚度。SEA 增加了柔顺性，但也降低了有效刚度与位置控制带宽。ASAP 的残差学习可以在不依赖精确力控模型的情况下，隐式补偿这类执行器非线性。

#### 关键参数与规格
| 参数/规格 | 数值/内容 | 来源 |
|-----------|-----------|------|
| 迁移场景数量 | 3 种（IsaacGym→IsaacSim、IsaacGym→Genesis、IsaacGym→真实 Unitree G1） | 语料 |
| 对比基线 | SysID、DR、delta dynamics learning | 语料 |
| 核心评价指标 | 跟踪误差（tracking error） | 语料 |
| 演示动作示例 | Side Jump (1.3m)、Jump Forward (0.85m)、Jump Forward (1.5m)、Forward Kick、Right Kick、APT Dance、Leg Stretch、Squat、Squat + Lean Forward | 语料 |
| 发表会议 | RSS 2025 | 语料 |
| 相关 Workshop | CoRL 2024 Spotlight WCBM Workshop、X-Embodiment Workshop | 语料 |

#### 横向对比
| 方法 | 核心思路 | 优势 | 劣势 |
|------|----------|------|------|
| **ASAP** | 残差动作模型 + 仿真微调 | 保持敏捷性、无需精确系统辨识、数据驱动 | 需要真实机器人数据收集 |
| **SysID** | 精确辨识仿真参数 | 仿真精度高 | 人工调参工作量大、难以覆盖全部动力学 |
| **DR** | 随机化仿真参数 | 策略鲁棒性强 | 策略保守、牺牲敏捷性 |
| **Delta Dynamics Learning** | 学习动力学残差 | 补偿模型误差 | 未与策略微调闭环集成 |

ASAP 的核心差异在于：它将残差学习与策略微调形成闭环，而非仅作为前馈补偿。这使得策略本身在微调后能够适应真实动力学，而非仅仅在推理时修正动作。

#### 谁在用·应用案例
ASAP 框架在 Unitree G1 人形机器人上实现了多种此前难以达成的敏捷动作，包括：

- **侧跳（Side Jump）**：跳跃距离 1.3m
- **前跳（Jump Forward）**：跳跃距离 0.85m 与 1.5m 两种规格
- **前踢（Forward Kick）** 与 **右踢（Right Kick）**
- **APT Dance**：舞蹈动作
- **腿部拉伸（Leg Stretch）**、**深蹲（Squat）**、**深蹲+前倾（Squat + Lean Forward）**

在 ASAP 微调前后对比中，踢腿与模仿 LeBron James 的动作在微调后显著改善了全身协调性与动态稳定性。这些结果验证了残差动作学习在弥合仿真与真实动力学差异方面的潜力。

#### 局限与边界
1. **需要真实数据收集**：ASAP 第二阶段必须将策略部署到真实机器人上收集数据，这意味着它无法完全脱离物理平台。对于尚未具备实体机器人的研究团队，这一门槛较高。

2. **残差模型的泛化边界**：残差动作模型基于特定状态-动作分布训练，当策略被部署到分布外的场景（如极端扰动、未见过地形）时，残差补偿可能失效。工程判断：需要配合域随机化或在线适应机制增强鲁棒性。

3. **计算与部署成本**：两阶段训练流程涉及仿真预训练、真实数据收集、残差模型训练与策略微调四个环节，整体流程耗时较长。对于快速迭代的研究场景，这一时间成本需纳入考量。

4. **与力控精度的关系**：ASAP 通过数据驱动方式补偿动力学差异，但并未显式建模力交互。对于需要精确力控的任务（如语料中提到的混合力/位置控制、阻抗控制场景），ASAP 可能需要与力控方法结合使用。

#### 常见误区
1. **"ASAP 是系统辨识的替代品"**——不准确。ASAP 不追求精确的仿真参数，而是通过残差学习补偿差异。它真正替代的是"人工调参"这一环节，而非系统辨识本身。

2. **"ASAP 只适用于人形机器人"**——从方法论看，残差动作学习具有通用性，可迁移到其他 Sim-to-Real 场景（如四足机器人、机械臂操作）。但当前论文的验证范围限于人形机器人全身控制。

3. **"ASAP 微调后策略完全适应真实物理"**——残差模型只能补偿训练分布内的动力学差异。对于未覆盖的动力学变化（如负载变化、关节磨损），策略仍可能退化。工程判断：需定期更新残差模型。

4. **"ASAP 与力控/阻抗控制无关"**——实际上，ASAP 的残差学习可以隐式补偿执行器的力控误差。语料中提到的 SEA 与 VSA 等执行器非线性，正是残差模型需要学习的典型动力学差异来源。

#### 相关知识
- `ent_paper_asap_aligning_simulation_and_r_2026` — 同一 ASAP 框架的扩展版本卡片，包含更详细的方法架构与实验设置描述。
- `ent_robot_unitree_h1_humanoid_robot_2024` — 宇树 H1 人形机器人，与 ASAP 验证平台 Unitree G1 同属宇树产品线，其高动态运动能力为 ASAP 类方法提供了硬件基础。

#### 왜 존재하는가:痛点과 역사적 위치
휴머노이드 로봇이 인간과 유사한 전신 민첩 기술을 달성하려면 직면하는 핵심 장애물은 **역학적 불일치(dynamics mismatch)**입니다 — 시뮬레이션 환경과 실제 물리 세계 사이에는 마찰, 관성, 액추에이터 지연, 유연 변형 등 체계적인 차이가 존재합니다. 이러한 차이로 인해 시뮬레이션에서 우수한 성능을 보이는 정책이 실제 로봇에 배포되면 성능이 급격히 저하됩니다.

ASAP 이전의 주류 접근법에는 명확한 결함이 있었습니다:

- **시스템 식별(SysID)**: 많은 수동 매개변수 튜닝이 필요하며, 식별 결과가 모든 역학적 특성을 포괄하기 어렵습니다.
- **도메인 무작위화(DR)**: 시뮬레이션 매개변수를 무작위화하여 정책 견고성을 강화하지만, 종종 정책이 지나치게 보수적이 되어 민첩성을 희생합니다.

ASAP의 위치는 바로 이 공백을 메우는 것입니다: 정확한 시스템 식별이 필요하지 않으며, 정책의 민첩성을 희생하지도 않습니다. 대신 데이터 기반의 잔차 학습을 통해 시뮬레이션과 실제 물리를 정렬합니다. 이 프레임워크가 실제로 변화시키는 것은 "시뮬레이션이 얼마나 정확한가"가 아니라 "정책이 시뮬레이션 오류에 얼마나 둔감한가"입니다.

## Overview

[Content to be added] According to the lab paper list: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills, publication institution unknown. The list does not include a retrievable paper page (to be supplemented/empty). This card only records the information from the list; the overview and core content are to be supplemented.

## Content
### List Registration Information
- **Paper Title**: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills
- **Publication Institution**: Unknown
- **Source Article**: "GitHub Repository Robotics_Notebooks" https://github.com/ImChong/Robotics_Notebooks

### Content to be Supplemented
- This card is a conservative card: the list does not provide a retrievable paper page, only the title and institution information are recorded; the overview and core content will be supplemented after obtaining the original paper or abstract.

## 개요

【내용 보충 예정】실험실 논문 목록에 등록된 바에 따르면: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills, 발표 기관 미상. 목록에 크롤링 가능한 논문 페이지가 등록되지 않음 (보충 예정/미기재), 본 카드는 목록 등록 정보만 수록하며, 개요와 핵심 내용은 보충 예정.

## 핵심 내용
### 목록 등록 정보
- **논문 제목**: ASAP Aligning Simulation and Real-World Physics for Agile Humanoid Skills
- **발표 기관**: 미상
- **출처 문서**: 《GitHub 저장소 Robotics_Notebooks》 https://github.com/ImChong/Robotics_Notebooks

### 내용 보충 예정
- 본 카드는 보수적 카드임: 목록에 크롤링 가능한 논문 페이지가 제공되지 않아, 제목과 기관 정보만 등록됨; 추후 논문 원문 또는 초록을 입수한 후 개요와 핵심 내용을 보충할 예정.
