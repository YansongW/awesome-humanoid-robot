---
$id: ent_paper_safehumanoid_vlm_rag_driven_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
  zh: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
  ko: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
summary:
  en: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
  zh: SafeHumanoid 是 2025 年提出的人形机器人上身阻抗控制方法，由研究团队开发。其核心贡献在于利用 Vision Language Models (VLMs) 与 Retrieval-Augmented Generation
    (RAG) 技术，根据场景上下文和人类接近程度动态调整机器人的刚度、阻尼与速度参数，实现安全的人机交互。
  ko: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
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
- manipulation
- safehumanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23300v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (923 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2511.23300
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SafeHumanoid 构建了一个以自我为中心视觉处理管线，通过结构化 VLM 提示处理第一人称视角图像，并将嵌入结果与预验证场景数据库进行匹配。系统利用检索增强生成技术将匹配结果映射为关节级阻抗指令，从而在桌面操作任务中实现上下文感知的刚度、阻尼和速度调节。实验涵盖擦拭、物体交接和液体倾倒等场景，结果表明该方法能在保持任务成功率的同时提升安全性，尽管当前推理延迟（最高 1.4 秒）限制了其在高度动态环境中的响应速度。

## 核心内容
### 方法架构
- **视觉处理管线**：采用自我中心视觉（egocentric vision）作为输入，通过结构化 VLM 提示处理第一人称视角图像帧。
- **检索增强生成**：将 VLM 输出的嵌入向量与预验证场景数据库进行匹配，利用 RAG 技术检索最相关的阻抗控制参数。
- **关节级控制**：通过逆运动学将检索到的阻抗参数映射为关节级刚度、阻尼和速度指令，实现上身阻抗的实时调度。

### 实验设置
- **任务场景**：在桌面操作环境中测试，包括擦拭（wiping）、物体交接（object handovers）和液体倾倒（liquid pouring）三类任务。
- **对比条件**：分别在有无人存在的场景下进行实验，评估系统对上下文变化的适应能力。
- **性能指标**：重点考察任务成功率与安全性指标的平衡，同时记录推理延迟对动态响应的影响。

### 关键结果
- **上下文适应能力**：系统能根据人类接近程度和任务类型自动调整阻抗参数，在有人场景下降低刚度与速度以提升安全性。
- **任务成功率**：在保持与基线方法相当的任务完成率的同时，显著减少了意外碰撞风险。
- **延迟限制**：当前推理延迟最高达 1.4 秒，在高度动态交互场景中响应不足，但证明了语义引导阻抗控制（semantic grounding of impedance control）的可行性。

### 结论
SafeHumanoid 展示了将 VLM 与 RAG 结合用于人形机器人阻抗控制的潜力，为符合安全标准的人机协作提供了新路径。未来工作需优化推理速度以支持实时动态交互。

## Overview
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## 参考
- http://arxiv.org/abs/2511.23300v1

## 개요
SafeHumanoid는 자기 중심적 시각 처리 파이프라인을 구축하여 구조화된 VLM 프롬프트를 통해 1인칭 시점 이미지를 처리하고, 임베딩 결과를 사전 검증된 장면 데이터베이스와 매칭합니다. 시스템은 검색 증강 생성 기술을 활용하여 매칭 결과를 관절 수준 임피던스 명령으로 매핑함으로써, 데스크톱 조작 작업에서 상황 인식형 강성, 감쇠, 속도 조절을 구현합니다. 실험은 닦기, 물체 인계, 액체 따르기 등의 시나리오를 포함하며, 해당 방법이 작업 성공률을 유지하면서 안전성을 향상시킬 수 있음을 보여줍니다. 다만 현재 추론 지연 시간(최대 1.4초)이 매우 동적인 환경에서의 응답 속도를 제한합니다.

## 핵심 내용
### 방법 아키텍처
- **시각 처리 파이프라인**: 자기 중심적 시각(egocentric vision)을 입력으로 사용하며, 구조화된 VLM 프롬프트를 통해 1인칭 시점 이미지 프레임을 처리합니다.
- **검색 증강 생성**: VLM 출력의 임베딩 벡터를 사전 검증된 장면 데이터베이스와 매칭하고, RAG 기술을 활용하여 가장 관련성 높은 임피던스 제어 파라미터를 검색합니다.
- **관절 수준 제어**: 역운동학을 통해 검색된 임피던스 파라미터를 관절 수준의 강성, 감쇠, 속도 명령으로 매핑하여 상체 임피던스의 실시간 스케줄링을 구현합니다.

### 실험 설정
- **작업 시나리오**: 데스크톱 조작 환경에서 닦기(wiping), 물체 인계(object handovers), 액체 따르기(liquid pouring)의 세 가지 작업 유형을 테스트합니다.
- **비교 조건**: 사람이 있는 경우와 없는 경우의 시나리오를 각각 실험하여, 시스템의 상황 변화 적응 능력을 평가합니다.
- **성능 지표**: 작업 성공률과 안전성 지표 간의 균형을 중점적으로 살펴보며, 추론 지연 시간이 동적 응답에 미치는 영향도 기록합니다.

### 주요 결과
- **상황 적응 능력**: 시스템은 인간의 접근 정도와 작업 유형에 따라 임피던스 파라미터를 자동으로 조정하며, 사람이 있는 시나리오에서는 강성과 속도를 낮추어 안전성을 향상시킵니다.
- **작업 성공률**: 기준 방법과 유사한 작업 완료율을 유지하면서도, 예상치 못한 충돌 위험을 크게 줄입니다.
- **지연 시간 제한**: 현재 추론 지연 시간은 최대 1.4초로, 매우 동적인 상호작용 시나리오에서는 응답이 부족하지만, 의미 기반 임피던스 제어(semantic grounding of impedance control)의 실현 가능성을 입증합니다.

### 결론
SafeHumanoid는 VLM과 RAG를 결합하여 휴머노이드 로봇의 임피던스 제어에 적용할 수 있는 잠재력을 보여주며, 안전 기준을 충족하는 인간-로봇 협업의 새로운 경로를 제시합니다. 향후 작업은 실시간 동적 상호작용을 지원하기 위해 추론 속도를 최적화해야 합니다.
