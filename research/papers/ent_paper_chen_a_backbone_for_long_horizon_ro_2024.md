---
$id: ent_paper_chen_a_backbone_for_long_horizon_ro_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Backbone for Long-Horizon Robot Task Understanding
  zh: 面向长程机器人任务理解的骨干框架
  ko: 장기적 로봇 작업 이해를 위한 백본
summary:
  en: This paper proposes the Therblig-Based Backbone Framework (TBBF), which decomposes long-horizon robot manipulation tasks
    into elemental therblig units offline and transfers trajectories to novel scenes online via Action Registration and LLM-guided
    visual correction.
  zh: 本文提出了一种名为 Therblig-Based Backbone Framework (TBBF) 的框架，用于提升机器人长时域操作任务的可解释性与泛化能力。该框架由北京理工大学等机构的研究者开发，核心贡献在于将复杂任务分解为基本动作单元（therblig），并通过
    Action Registration 与 LLM 引导的视觉校正实现轨迹迁移，在真实场景测试中取得了 94.4% 和 80% 的成功率。
  ko: 본 논문은 장기 로봇 조작 작업을 기본 동작 단위(therblig)로 오프라인 분해하고, 액션 등록 및 LLM 기반 시각 교정을 통해 온라인으로 새로운 장면에 궤적을 전이하는 TBBF를 제안한다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- long_horizon_manipulation
- therblig_decomposition
- one_shot_learning
- task_understanding
- action_object_mapping
- imitation_learning
- robot_learning
- sam
- llm_alignment
- trajectory_transfer
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.01334v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1274 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Backbone for Long-Horizon Robot Task Understanding
  url: https://arxiv.org/abs/2408.01334
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
TBBF 框架通过将长时域机器人操作任务离线分解为基本动作单元（therblig），并在在线阶段利用 Action Registration 与 LLM 引导的视觉校正实现轨迹迁移，从而解决了端到端学习在长时域任务中泛化性差的问题。该框架包含离线训练与在线测试两个阶段：离线阶段使用 Meta-RGate SynerFusion (MGSF) 网络进行精确的 therblig 分割；在线阶段则通过一次演示提取高层知识，并借助 LLM 确保动作注册的准确性。实验结果表明，该框架在 therblig 分割任务中召回率达到 94.37%，在真实机器人测试中，简单场景成功率为 94.4%，复杂场景成功率为 80%。

## 核心内容
### 方法概述
TBBF 框架旨在解决端到端机器人学习在长时域任务中表现不可预测且泛化能力差的问题。其核心思想是将复杂任务分解为可解释的基本动作单元（therblig），并实现从演示到新场景的轨迹迁移。

### 架构与流程
#### 离线训练阶段
- **Meta-RGate SynerFusion (MGSF) 网络**：该网络被开发用于跨多种任务进行精确的 therblig 分割。它通过融合多模态特征，能够从专家演示中识别出不同的动作单元。
- **任务分解**：利用 MGSF 网络，将长时域操作任务离线分解为一系列 therblig 单元，每个单元对应一个基本动作（如抓取、移动、放置等）。这种分解方式增强了任务的可解释性。

#### 在线测试阶段
- **一次演示**：对于新任务，仅需收集一次演示数据。
- **高层知识提取**：MGSF 网络从演示中提取高层知识，即任务对应的 therblig 序列。
- **Action Registration (ActionREG)**：将提取的高层知识编码到当前场景的图像中，实现动作与场景的对应。
- **LLM-Alignment Policy for Visual Correction (LAP-VC)**：利用大语言模型 (LLM) 对 ActionREG 进行视觉校正，确保动作注册的精确性，从而在新场景中生成自适应轨迹。

### 实验设置与结果
- **Therblig 分割性能**：在多种任务上，MGSF 网络实现了 94.37% 的召回率，表明其能够准确识别基本动作单元。
- **真实机器人测试**：
  - **简单场景**：成功率达到 94.4%。
  - **复杂场景**：成功率达到 80%。
- **补充材料**：更多细节和演示视频可在项目网站获取：https://sites.google.com/view/therbligsbasedbackbone/home

### 结论
TBBF 框架通过 therblig 级任务分解与 LLM 辅助的视觉校正，显著提升了机器人长时域操作任务的可解释性、数据效率和泛化能力。实验验证了其在真实场景中的有效性，为复杂机器人任务的理解与执行提供了新的基础结构。

## Overview
End-to-end robot learning, particularly for long-horizon tasks, often results in unpredictable outcomes and poor generalization. To address these challenges, we propose a novel Therblig-Based Backbone Framework (TBBF) as a fundamental structure to enhance interpretability, data efficiency, and generalization in robotic systems. TBBF utilizes expert demonstrations to enable therblig-level task decomposition, facilitate efficient action-object mapping, and generate adaptive trajectories for new scenarios. The approach consists of two stages: offline training and online testing. During the offline training stage, we developed the Meta-RGate SynerFusion (MGSF) network for accurate therblig segmentation across various tasks. In the online testing stage, after a one-shot demonstration of a new task is collected, our MGSF network extracts high-level knowledge, which is then encoded into the image using Action Registration (ActionREG). Additionally, Large Language Model (LLM)-Alignment Policy for Visual Correction (LAP-VC) is employed to ensure precise action registration, facilitating trajectory transfer in novel robot scenarios. Experimental results validate these methods, achieving 94.37% recall in therblig segmentation and success rates of 94.4% and 80% in real-world online robot testing for simple and complex scenarios, respectively. Supplementary material is available at: https://sites.google.com/view/therbligsbasedbackbone/home

## 参考
- http://arxiv.org/abs/2408.01334v3

## 개요
TBBF 프레임워크는 장시간 로봇 조작 작업을 오프라인에서 기본 동작 단위(therblig)로 분해하고, 온라인 단계에서 Action Registration과 LLM 기반 시각 보정을 활용하여 궤적 전이를 구현함으로써, 엔드투엔드 학습이 장시간 작업에서 일반화 성능이 낮은 문제를 해결합니다. 이 프레임워크는 오프라인 훈련과 온라인 테스트 두 단계로 구성됩니다: 오프라인 단계에서는 Meta-RGate SynerFusion (MGSF) 네트워크를 사용하여 정밀한 therblig 분할을 수행하고, 온라인 단계에서는 단일 시연을 통해 고수준 지식을 추출하며 LLM을 활용하여 동작 등록의 정확성을 보장합니다. 실험 결과, 이 프레임워크는 therblig 분할 작업에서 재현율 94.37%를 달성했으며, 실제 로봇 테스트에서 단순 시나리오 성공률은 94.4%, 복잡한 시나리오 성공률은 80%를 기록했습니다.

## 핵심 내용
### 방법 개요
TBBF 프레임워크는 엔드투엔드 로봇 학습이 장시간 작업에서 예측 불가능한 성능과 낮은 일반화 능력을 보이는 문제를 해결하는 것을 목표로 합니다. 핵심 아이디어는 복잡한 작업을 해석 가능한 기본 동작 단위(therblig)로 분해하고, 시연에서 새로운 시나리오로의 궤적 전이를 구현하는 것입니다.

### 아키텍처 및 프로세스
#### 오프라인 훈련 단계
- **Meta-RGate SynerFusion (MGSF) 네트워크**: 이 네트워크는 다양한 작업에 걸쳐 정밀한 therblig 분할을 수행하기 위해 개발되었습니다. 다중 모달 특징을 융합하여 전문가 시연에서 다양한 동작 단위를 식별할 수 있습니다.
- **작업 분해**: MGSF 네트워크를 활용하여 장시간 조작 작업을 오프라인에서 일련의 therblig 단위로 분해하며, 각 단위는 기본 동작(예: 파지, 이동, 배치 등)에 해당합니다. 이러한 분해 방식은 작업의 해석 가능성을 향상시킵니다.

#### 온라인 테스트 단계
- **단일 시연**: 새로운 작업에 대해 단 한 번의 시연 데이터만 수집하면 됩니다.
- **고수준 지식 추출**: MGSF 네트워크가 시연에서 고수준 지식, 즉 작업에 해당하는 therblig 시퀀스를 추출합니다.
- **Action Registration (ActionREG)**: 추출된 고수준 지식을 현재 시나리오의 이미지에 인코딩하여 동작과 시나리오의 대응을 구현합니다.
- **LLM-Alignment Policy for Visual Correction (LAP-VC)**: 대규모 언어 모델(LLM)을 활용하여 ActionREG에 대한 시각 보정을 수행하고, 동작 등록의 정확성을 보장하여 새로운 시나리오에서 적응형 궤적을 생성합니다.

### 실험 설정 및 결과
- **Therblig 분할 성능**: 다양한 작업에서 MGSF 네트워크는 94.37%의 재현율을 달성하여 기본 동작 단위를 정확히 식별할 수 있음을 보여줍니다.
- **실제 로봇 테스트**:
  - **단순 시나리오**: 성공률 94.4% 달성.
  - **복잡한 시나리오**: 성공률 80% 달성.
- **추가 자료**: 더 많은 세부 사항과 시연 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다: https://sites.google.com/view/therbligsbasedbackbone/home

### 결론
TBBF 프레임워크는 therblig 수준의 작업 분해와 LLM 보조 시각 보정을 통해 로봇 장시간 조작 작업의 해석 가능성, 데이터 효율성 및 일반화 능력을 크게 향상시켰습니다. 실험은 실제 시나리오에서의 효과를 검증했으며, 복잡한 로봇 작업의 이해와 실행을 위한 새로운 기본 구조를 제공합니다.
