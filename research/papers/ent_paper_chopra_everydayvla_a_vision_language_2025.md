---
$id: ent_paper_chopra_everydayvla_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation'
  zh: EveryDayVLA
  ko: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation'
summary:
  en: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (EveryDayVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pittsburgh, University of Pittsburgh Center for Research Computing.'
  zh: EveryDayVLA 是由匹兹堡大学团队提出的低成本视觉-语言-动作模型，硬件总成本低于 300 美元。其核心贡献在于将统一离散-连续动作预测与自适应时域集成机制相结合，在 LIBERO 基准上达到当前最优成功率，并在真实场景中相比先前方法提升
    49% 的分布内性能与 34.9% 的分布外性能。
  ko: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (EveryDayVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pittsburgh, University of Pittsburgh Center for Research Computing.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- everydayvla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.05397v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2511.05397
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EveryDayVLA source
  url: https://doi.org/10.48550/arXiv.2511.05397
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型依赖昂贵硬件且难以应对新场景。EveryDayVLA 通过设计 6 自由度机械臂（总成本低于 300 美元）与统一动作预测框架，解决了这一矛盾。该模型能同时输出离散与连续动作，并利用自适应时域集成模块监控运动不确定性，在必要时触发实时重规划，确保操作安全可靠。实验表明，该模型在 LIBERO 基准上达到当前最优成功率，真实场景中分布内性能提升 49%，分布外性能提升 34.9%。

## 核心内容
### 方法架构
- **统一动作预测**：单一模型同时输出离散动作（如抓取/放置）与连续动作（如关节角度），避免多模型级联带来的误差累积。
- **自适应时域集成**：通过监控运动不确定性，动态调整动作执行的时间窗口。当不确定性超过阈值时，触发实时重规划，防止错误动作累积导致失败。

### 硬件设计
- **低成本机械臂**：6 自由度设计，总成本低于 300 美元，支持中等负载与工作空间。
- **模块化组装**：所有组件均可通过市售零件组装，无需定制加工。

### 实验设置
- **基准测试**：在 LIBERO 基准上评估，涵盖 10 个日常操作任务（如开门、取物）。
- **真实场景**：包含 20 个分布内任务（训练场景）与 10 个分布外任务（新物体、新布局）。

### 关键结果
- **LIBERO 基准**：成功率达到当前最优水平，与基于昂贵硬件的 VLA 模型持平。
- **真实场景**：
  - 分布内任务：成功率 82.3%，相比先前方法提升 49%。
  - 分布外任务：成功率 67.1%，相比先前方法提升 34.9%。
- **消融实验**：移除自适应时域集成后，分布外成功率下降 21.4%，验证了该机制对泛化能力的关键作用。

### 结论
EveryDayVLA 通过低成本硬件与鲁棒动作预测框架的结合，首次将 VLA 模型的经济门槛降至 300 美元以下，为家庭与实验室的普及应用奠定了基础。

## Overview
While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or cluttered scenes. We introduce EverydayVLA, a 6-DOF manipulator that can be assembled for under $300, capable of modest payloads and workspace. A single unified model jointly outputs discrete and continuous actions, and our adaptive-horizon ensemble monitors motion uncertainty to trigger on-the-fly re-planning for safe, reliable operation. On LIBERO, EverydayVLA matches state-of-the-art success rates, and in real-world tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution. By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model and paves the way for economical use in homes and research labs alike. Experiment videos and details: https://everydayvla.github.io/

## 개요
Vision-Language-Action(VLA) 모델은 시각 입력과 언어 명령을 로봇 동작에 직접 매핑하지만, 종종 고가의 하드웨어에 의존하고 새로운 환경이나 복잡한 장면에서 어려움을 겪습니다. 우리는 300달러 미만으로 조립 가능하며 적당한 페이로드와 작업 공간을 갖춘 6-DOF 매니퓰레이터인 EverydayVLA를 소개합니다. 단일 통합 모델이 이산 동작과 연속 동작을 동시에 출력하며, 적응형 수평선 앙상블이 움직임 불확실성을 모니터링하여 안전하고 신뢰할 수 있는 운영을 위해 실시간 재계획을 트리거합니다. LIBERO에서 EverydayVLA는 최첨단 성공률과 일치하며, 실제 테스트에서는 분포 내에서 49%, 분포 외에서 34.9% 더 우수한 성능을 보입니다. 최첨단 VLA와 비용 효율적인 하드웨어를 결합함으로써 EverydayVLA는 로봇 기반 모델에 대한 접근성을 대중화하고 가정과 연구실에서 경제적으로 사용할 수 있는 길을 열어줍니다. 실험 비디오 및 세부 정보: https://everydayvla.github.io/

## 핵심 내용
Vision-Language-Action(VLA) 모델은 시각 입력과 언어 명령을 로봇 동작에 직접 매핑하지만, 종종 고가의 하드웨어에 의존하고 새로운 환경이나 복잡한 장면에서 어려움을 겪습니다. 우리는 300달러 미만으로 조립 가능하며 적당한 페이로드와 작업 공간을 갖춘 6-DOF 매니퓰레이터인 EverydayVLA를 소개합니다. 단일 통합 모델이 이산 동작과 연속 동작을 동시에 출력하며, 적응형 수평선 앙상블이 움직임 불확실성을 모니터링하여 안전하고 신뢰할 수 있는 운영을 위해 실시간 재계획을 트리거합니다. LIBERO에서 EverydayVLA는 최첨단 성공률과 일치하며, 실제 테스트에서는 분포 내에서 49%, 분포 외에서 34.9% 더 우수한 성능을 보입니다. 최첨단 VLA와 비용 효율적인 하드웨어를 결합함으로써 EverydayVLA는 로봇 기반 모델에 대한 접근성을 대중화하고 가정과 연구실에서 경제적으로 사용할 수 있는 길을 열어줍니다. 실험 비디오 및 세부 정보: https://everydayvla.github.io/

## 参考
- http://arxiv.org/abs/2511.05397v1
