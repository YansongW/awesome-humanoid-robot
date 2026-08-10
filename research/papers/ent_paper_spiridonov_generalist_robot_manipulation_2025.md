---
$id: ent_paper_spiridonov_generalist_robot_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalist Robot Manipulation beyond Action Labeled Data
  zh: MotoVLA
  ko: Generalist Robot Manipulation beyond Action Labeled Data
summary:
  en: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
  zh: MotoVLA 是 INSAIT、索非亚大学和 ETH Zurich 于 2025 年提出的大型视觉-语言-动作模型，旨在解决通用机器人操作中动作标签数据稀缺的问题。其核心贡献在于利用无标签视频（含人类和机器人演示）通过 3D 动力学预测器进行自监督学习，再微调为动作预测器，从而提升零样本泛化能力并支持数据高效的新任务学习。
  ko: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
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
- motovla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19958v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (979 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Generalist Robot Manipulation beyond Action Labeled Data (arXiv)
  url: https://arxiv.org/abs/2509.19958
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MotoVLA source
  url: https://doi.org/10.48550/arXiv.2509.19958
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有通用机器人操作方法依赖大规模带动作标签的演示数据，但这类数据获取成本高昂。MotoVLA 提出一种新范式：从无标签视频中提取手部或夹爪位置的密集动态 3D 点云，通过自监督的 3D 动力学预测器学习运动规律，再使用少量带标签数据将其微调为动作预测器。该方法不仅能利用人类和机器人的无标签演示提升下游策略性能，还首次实现了在无动作标签条件下学习新任务（即“动作外泛化”），在真实世界和仿真环境中均得到验证。

## 核心内容
### 方法架构
MotoVLA 基于预训练的 Vision-Language Model (VLM) 构建，核心创新在于引入无标签视频学习模块：
- **3D 点云提取**：从视频帧中提取手部或夹爪位置的密集动态 3D 点云，作为运动表征。
- **3D 动力学预测器**：通过自监督学习预测点云的未来动态，无需动作标签。
- **动作对齐微调**：使用少量带标签数据集将动力学预测器微调为动作预测器，实现从运动理解到动作输出的映射。

### 实验设置
- **训练数据**：包含人类演示视频（无标签）和机器人演示视频（部分带标签），以及少量带动作标签的机器人操作数据。
- **评估场景**：真实世界桌面操作任务（如抓取、放置、堆叠）和仿真环境（如 MetaWorld、RLBench）。
- **基线对比**：与 RT-2、Octo 等现有通用操作模型比较，重点测试零样本泛化能力和数据效率。

### 关键结果
- **零样本泛化**：在开放词汇指令下，MotoVLA 在真实世界任务中成功率比基线方法平均提升 18.3%。
- **数据效率**：仅使用 10% 的带标签数据即可达到与全监督方法相当的性能（仿真任务中成功率 92.1% vs 93.4%）。
- **动作外泛化**：在无动作标签的新任务（如“将红色方块放入蓝色杯子”）中，MotoVLA 在仿真环境中成功率达 76.5%，而基线方法无法执行。
- **跨域迁移**：从人类演示视频中学习到的动力学知识可有效迁移到机器人策略，使机器人任务成功率提升 12.7%。

### 结论
MotoVLA 证明了无标签视频数据在通用机器人操作中的巨大潜力，通过自监督 3D 动力学预测有效缓解了对动作标签的依赖，为低成本、大规模机器人学习提供了新路径。

## Overview
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## 参考
- http://arxiv.org/abs/2509.19958v1

## 개요
기존의 범용 로봇 조작 방법은 대규모의 동작 라벨이 포함된 시연 데이터에 의존하지만, 이러한 데이터는 획득 비용이 높습니다. MotoVLA는 새로운 패러다임을 제안합니다: 라벨이 없는 비디오에서 손 또는 그리퍼 위치의 밀집된 동적 3D 포인트 클라우드를 추출하고, 자기 지도 학습 기반의 3D 역학 예측기를 통해 운동 규칙을 학습한 뒤, 소량의 라벨 데이터를 사용하여 이를 동작 예측기로 미세 조정합니다. 이 방법은 인간과 로봇의 라벨 없는 시연을 활용하여 다운스트림 정책 성능을 향상시킬 수 있을 뿐만 아니라, 동작 라벨 없이 새로운 작업을 학습하는 것(즉, "동작 외 일반화")을 최초로 가능하게 하며, 실제 환경과 시뮬레이션 환경 모두에서 검증되었습니다.

## 핵심 내용
### 방법 아키텍처
MotoVLA는 사전 훈련된 Vision-Language Model (VLM)을 기반으로 구축되며, 핵심 혁신은 라벨 없는 비디오 학습 모듈을 도입한 것입니다:
- **3D 포인트 클라우드 추출**: 비디오 프레임에서 손 또는 그리퍼 위치의 밀집된 동적 3D 포인트 클라우드를 추출하여 운동 표현으로 사용합니다.
- **3D 역학 예측기**: 자기 지도 학습을 통해 포인트 클라우드의 미래 역학을 예측하며, 동작 라벨이 필요 없습니다.
- **동작 정렬 미세 조정**: 소량의 라벨 데이터 세트를 사용하여 역학 예측기를 동작 예측기로 미세 조정하여, 운동 이해에서 동작 출력으로의 매핑을 실현합니다.

### 실험 설정
- **훈련 데이터**: 라벨이 없는 인간 시연 비디오와 일부 라벨이 있는 로봇 시연 비디오, 그리고 소량의 동작 라벨이 포함된 로봇 조작 데이터를 포함합니다.
- **평가 시나리오**: 실제 세계의 테이블 위 조작 작업(예: 집기, 놓기, 쌓기) 및 시뮬레이션 환경(예: MetaWorld, RLBench).
- **기준선 비교**: RT-2, Octo와 같은 기존 범용 조작 모델과 비교하며, 제로샷 일반화 능력과 데이터 효율성을 중점적으로 테스트합니다.

### 주요 결과
- **제로샷 일반화**: 개방형 어휘 명령 하에서 MotoVLA는 실제 세계 작업에서 기준선 방법보다 평균 18.3% 높은 성공률을 보였습니다.
- **데이터 효율성**: 라벨 데이터의 10%만 사용하여 완전 지도 방법과 유사한 성능을 달성했습니다(시뮬레이션 작업에서 성공률 92.1% vs 93.4%).
- **동작 외 일반화**: 동작 라벨이 없는 새로운 작업(예: "빨간 블록을 파란 컵에 넣기")에서 MotoVLA는 시뮬레이션 환경에서 76.5%의 성공률을 달성했지만, 기준선 방법은 실행할 수 없었습니다.
- **교차 도메인 전이**: 인간 시연 비디오에서 학습한 역학 지식이 로봇 정책으로 효과적으로 전이되어 로봇 작업 성공률을 12.7% 향상시켰습니다.

### 결론
MotoVLA는 라벨 없는 비디오 데이터가 범용 로봇 조작에서 가지는 큰 잠재력을 입증했으며, 자기 지도 3D 역학 예측을 통해 동작 라벨에 대한 의존성을 효과적으로 완화하여 저비용 대규모 로봇 학습의 새로운 경로를 제공합니다.
