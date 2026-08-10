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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.05397v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (843 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.05397v1

## 개요
기존의 비전-언어-행동 모델은 고가의 하드웨어에 의존하며 새로운 시나리오에 대응하기 어렵다. EveryDayVLA는 6자유도 로봇 팔(총 비용 300달러 미만)과 통합 행동 예측 프레임워크를 설계하여 이러한 모순을 해결했다. 이 모델은 이산 행동과 연속 행동을 동시에 출력할 수 있으며, 적응형 시간 영역 통합 모듈을 활용해 운동 불확실성을 모니터링하고 필요 시 실시간 재계획을 트리거하여 안전하고 신뢰할 수 있는 조작을 보장한다. 실험 결과, 이 모델은 LIBERO 벤치마크에서 최고 수준의 성공률을 달성했으며, 실제 시나리오에서 분포 내 성능은 49%, 분포 외 성능은 34.9% 향상되었다.

## 핵심 내용
### 방법 아키텍처
- **통합 행동 예측**: 단일 모델이 이산 행동(예: 파지/배치)과 연속 행동(예: 관절 각도)을 동시에 출력하여 다중 모델 캐스케이드로 인한 오류 누적을 방지한다.
- **적응형 시간 영역 통합**: 운동 불확실성을 모니터링하여 행동 실행의 시간 창을 동적으로 조정한다. 불확실성이 임계값을 초과하면 실시간 재계획을 트리거하여 잘못된 행동 누적으로 인한 실패를 방지한다.

### 하드웨어 설계
- **저비용 로봇 팔**: 6자유도 설계, 총 비용 300달러 미만, 중간 부하와 작업 공간을 지원한다.
- **모듈식 조립**: 모든 구성 요소는 시판 부품으로 조립 가능하며 맞춤형 가공이 필요 없다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 벤치마크에서 평가하며, 10개의 일상 조작 작업(예: 문 열기, 물건 집기)을 포함한다.
- **실제 시나리오**: 20개의 분포 내 작업(훈련 시나리오)과 10개의 분포 외 작업(새로운 물체, 새로운 배치)을 포함한다.

### 주요 결과
- **LIBERO 벤치마크**: 고가 하드웨어 기반 VLA 모델과 동등한 수준의 최고 성공률을 달성했다.
- **실제 시나리오**:
  - 분포 내 작업: 성공률 82.3%, 기존 방법 대비 49% 향상.
  - 분포 외 작업: 성공률 67.1%, 기존 방법 대비 34.9% 향상.
- **소거 실험**: 적응형 시간 영역 통합을 제거하면 분포 외 성공률이 21.4% 하락하여, 이 메커니즘이 일반화 능력에 미치는 핵심 역할을 검증했다.

### 결론
EveryDayVLA는 저비용 하드웨어와 견고한 행동 예측 프레임워크의 결합을 통해 VLA 모델의 경제적 장벽을 처음으로 300달러 미만으로 낮추었으며, 가정 및 실험실에서의 보급 응용을 위한 기반을 마련했다.
