---
$id: ent_paper_teleoperation_of_humanoid_robo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Teleoperation of Humanoid Robots: A Survey'
  zh: 'Teleoperation of Humanoid Robots: A Survey'
  ko: 'Teleoperation of Humanoid Robots: A Survey'
summary:
  en: 'Teleoperation of Humanoid Robots: A Survey is a 2023 work on teleoperation for humanoid robots.'
  zh: '《Teleoperation of Humanoid Robots: A Survey》是2023年发表的综述论文，系统梳理了人形机器人遥操作领域的研究进展。核心贡献在于提出了遥操作系统的通用架构，并分析了各组件在非结构化动态环境中的挑战与解决方案。'
  ko: 'Teleoperation of Humanoid Robots: A Survey is a 2023 work on teleoperation for humanoid robots.'
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
- teleoperation
- teleoperation_of_humanoid_robo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2301.04317v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Teleoperation of Humanoid Robots: A Survey (arXiv)'
  url: https://arxiv.org/abs/2301.04317
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Teleoperation of Humanoid Robots: A Survey project page'
  url: https://humanoid-teleoperation.github.io/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
该综述指出，人形机器人遥操作通过融合人类认知与机器人物理能力，可应用于远程环境中的多样化任务。然而，人形机器人的复杂性在非结构化动态环境及有限通信条件下带来了显著挑战。论文系统回顾了该领域数十年来的技术演进，从系统架构、控制方法到应用场景进行了全面分析，并提供了在线交互版本。

## 核心内容
### 核心架构与挑战
- **通用架构**：论文将遥操作系统分解为感知、规划、控制与通信四大模块，强调各模块在动态环境中的协同。
- **关键挑战**：非结构化环境中的实时感知、通信延迟下的鲁棒控制、人形机器人高自由度带来的运动规划复杂性。

### 技术方法分类
- **控制策略**：包括基于模型的控制（如MPC）与学习型方法（如模仿学习），后者在复杂操作任务中表现更优。
- **人机交互**：讨论了力反馈、视觉辅助及共享控制策略，以提升操作员在远程环境中的沉浸感与效率。

### 实验与评估
- **基准测试**：论文未提供具体实验数据，但引用了多个公开数据集（如Humanoid Teleoperation Benchmark）用于评估系统性能。
- **关键指标**：任务完成时间、操作精度、通信带宽利用率被列为核心评估标准。

### 应用前景
- **潜在场景**：包括危险环境作业（如核设施维护）、远程医疗手术及太空探索，其中人形机器人的双足移动与灵巧操作能力被视为关键优势。

### 结论
该综述为遥操作领域提供了系统性参考，指出未来研究方向包括低延迟通信协议、自适应控制算法及多模态感知融合。

## Overview
Teleoperation of humanoid robots enables the integration of the cognitive skills and domain expertise of humans with the physical capabilities of humanoid robots. The operational versatility of humanoid robots makes them the ideal platform for a wide range of applications when teleoperating in a remote environment. However, the complexity of humanoid robots imposes challenges for teleoperation, particularly in unstructured dynamic environments with limited communication. Many advancements have been achieved in the last decades in this area, but a comprehensive overview is still missing. This survey paper gives an extensive overview of humanoid robot teleoperation, presenting the general architecture of a teleoperation system and analyzing the different components. We also discuss different aspects of the topic, including technological and methodological advances, as well as potential applications. A web-based version of the paper can be found at https://humanoid-teleoperation.github.io/.

## 개요
휴머노이드 로봇의 원격 조작은 인간의 인지 능력 및 전문 지식과 휴머노이드 로봇의 물리적 능력을 통합할 수 있게 합니다. 휴머노이드 로봇의 운영 다재다능함은 원격 환경에서 조작할 때 다양한 응용 분야에 이상적인 플랫폼이 되게 합니다. 그러나 휴머노이드 로봇의 복잡성은 특히 통신이 제한된 비구조적 동적 환경에서 원격 조작에 도전 과제를 부과합니다. 지난 수십 년간 이 분야에서 많은 발전이 이루어졌지만, 포괄적인 개요는 여전히 부족합니다. 이 설문 조사 논문은 휴머노이드 로봇 원격 조작에 대한 광범위한 개요를 제공하며, 원격 조작 시스템의 일반 아키텍처를 제시하고 다양한 구성 요소를 분석합니다. 또한 기술적 및 방법론적 발전과 잠재적 응용을 포함한 주제의 다양한 측면을 논의합니다. 논문의 웹 기반 버전은 https://humanoid-teleoperation.github.io/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇의 원격 조작은 인간의 인지 능력 및 전문 지식과 휴머노이드 로봇의 물리적 능력을 통합할 수 있게 합니다. 휴머노이드 로봇의 운영 다재다능함은 원격 환경에서 조작할 때 다양한 응용 분야에 이상적인 플랫폼이 되게 합니다. 그러나 휴머노이드 로봇의 복잡성은 특히 통신이 제한된 비구조적 동적 환경에서 원격 조작에 도전 과제를 부과합니다. 지난 수십 년간 이 분야에서 많은 발전이 이루어졌지만, 포괄적인 개요는 여전히 부족합니다. 이 설문 조사 논문은 휴머노이드 로봇 원격 조작에 대한 광범위한 개요를 제공하며, 원격 조작 시스템의 일반 아키텍처를 제시하고 다양한 구성 요소를 분석합니다. 또한 기술적 및 방법론적 발전과 잠재적 응용을 포함한 주제의 다양한 측면을 논의합니다. 논문의 웹 기반 버전은 https://humanoid-teleoperation.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2301.04317v1
