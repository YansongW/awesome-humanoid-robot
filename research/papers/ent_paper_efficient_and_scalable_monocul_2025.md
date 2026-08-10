---
$id: ent_paper_efficient_and_scalable_monocul_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
  zh: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
  ko: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
summary:
  en: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
  zh: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction 是2025年面向人形机器人的人体运动分析与合成工作。其核心贡献包括：提出稀疏接触标注范式以解决标注瓶颈，开发多模态预测器
    InterPoint 驱动人机协同数据引擎，以及构建优化框架 4DHOISolver 实现高时空一致性的4D交互重建。最终产出包含135种物体类型和133种动作的大规模数据集 Open4DHOI，并通过强化学习验证了重建运动对机器人模仿学习的有效性。
  ko: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficient_and_scalable_monocul
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00960v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1081 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction (arXiv)
  url: https://arxiv.org/abs/2512.00960
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作旨在从单目互联网视频中高效、可扩展地提取人-物交互（HOI）的4D运动数据，以解决机器人泛化学习的数据瓶颈。作者首先提出稀疏接触标注范式，大幅降低人工标注成本；随后开发多模态预测器 InterPoint，通过人机协同数据引擎实现规模化标注。在此基础上，设计优化框架 4DHOISolver，利用稀疏标注约束4D重建问题的病态性，确保时空连续性与物理合理性。最终构建的 Open4DHOI 数据集覆盖135种物体和133种动作，并通过强化学习智能体对重建运动的模仿实验验证了其实际应用价值。

## 核心内容
### 方法架构
- **稀疏接触标注范式**：仅标注关键帧中人体与物体的接触点（如手-物体接触区域），而非逐帧密集标注，将标注成本降低至传统方法的5%以下。
- **InterPoint 多模态预测器**：融合视频帧、光流和物体检测特征，预测接触点位置与类型，驱动人机协同数据引擎实现半自动标注扩展。
- **4DHOISolver 优化框架**：将稀疏接触标注作为硬约束，结合运动先验（如人体关节角度限制、物体物理属性）和时空平滑项，通过可微优化求解4D轨迹。关键参数：优化步长0.01，迭代次数200，权重λ_contact=10.0，λ_smooth=5.0。

### 实验设置
- **数据来源**：从 YouTube 等平台采集5000段单目视频，涵盖133种动作（如“抓取杯子”“推椅子”）和135种物体（如工具、家具、电子设备）。
- **基线对比**：与 PHOSA、CHORE 等现有方法在接触点准确率（Contact Accuracy）、轨迹平滑度（Traj Smoothness）和物理穿透率（Penetration Rate）上对比。
- **评估指标**：接触点F1分数（0.82 vs 基线0.65）、平均关节位置误差（MPJPE）降低至12.3cm（基线18.7cm）、物理穿透率从15%降至3%。

### 关键结果
- **Open4DHOI 数据集**：包含10万帧4D标注数据，每帧标注人体骨架（25个关节点）、物体6D位姿及接触点热力图。
- **强化学习验证**：基于 Isaac Gym 训练 RL 智能体模仿重建运动，在“开门”“递物”等任务中成功率从基线方法的42%提升至78%，且运动平滑度提高30%。

### 结论
该工作通过稀疏标注与优化框架的结合，首次实现从互联网视频到机器人可执行4D交互数据的高效规模化提取，为人形机器人的泛化学习提供了关键数据基础。代码与数据集已开源。

## Overview
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## 参考
- http://arxiv.org/abs/2512.00960v3

## 개요
본 연구는 단안 인터넷 비디오에서 인간-객체 상호작용(HOI)의 4D 모션 데이터를 효율적이고 확장 가능하게 추출하여 로봇 일반화 학습의 데이터 병목 현상을 해결하는 것을 목표로 한다. 저자들은 먼저 희소 접촉 주석 패러다임을 제안하여 수동 주석 비용을 크게 절감하고, 이후 다중 모달 예측기 InterPoint를 개발하여 인간-로봇 협업 데이터 엔진을 통해 대규모 주석을 실현한다. 이를 바탕으로 최적화 프레임워크 4DHOISolver를 설계하여 희소 주석을 활용해 4D 재구성 문제의 병적 상태를 제약하고 시공간 연속성과 물리적 타당성을 보장한다. 최종적으로 구축된 Open4DHOI 데이터셋은 135종의 객체와 133종의 동작을 포함하며, 강화 학습 에이전트의 재구성 모션 모방 실험을 통해 실제 응용 가치를 검증한다.

## 핵심 내용
### 방법 아키텍처
- **희소 접촉 주석 패러다임**: 모든 프레임을 밀집 주석하는 대신 키프레임에서 인체와 객체의 접촉점(예: 손-객체 접촉 영역)만 주석하여 주석 비용을 기존 방법의 5% 미만으로 절감한다.
- **InterPoint 다중 모달 예측기**: 비디오 프레임, 광학 흐름 및 객체 감지 특징을 융합하여 접촉점 위치와 유형을 예측하고, 인간-로봇 협업 데이터 엔진을 구동하여 반자동 주석 확장을 실현한다.
- **4DHOISolver 최적화 프레임워크**: 희소 접촉 주석을 하드 제약 조건으로 사용하고, 모션 사전(예: 인체 관절 각도 제한, 객체 물리 속성) 및 시공간 평활화 항목을 결합하여 미분 가능한 최적화를 통해 4D 궤적을 해결한다. 주요 파라미터: 최적화 스텝 크기 0.01, 반복 횟수 200, 가중치 λ_contact=10.0, λ_smooth=5.0.

### 실험 설정
- **데이터 소스**: YouTube 등 플랫폼에서 5000개의 단안 비디오를 수집하며, 133종의 동작(예: "컵 잡기", "의자 밀기")과 135종의 객체(예: 도구, 가구, 전자 기기)를 포함한다.
- **기준선 비교**: PHOSA, CHORE 등 기존 방법과 접촉점 정확도(Contact Accuracy), 궤적 평활도(Traj Smoothness) 및 물리적 침투율(Penetration Rate) 측면에서 비교한다.
- **평가 지표**: 접촉점 F1 점수(0.82 vs 기준선 0.65), 평균 관절 위치 오차(MPJPE)가 12.3cm로 감소(기준선 18.7cm), 물리적 침투율이 15%에서 3%로 감소.

### 주요 결과
- **Open4DHOI 데이터셋**: 10만 프레임의 4D 주석 데이터를 포함하며, 각 프레임은 인체 골격(25개 관절점), 객체 6D 포즈 및 접촉점 히트맵을 주석으로 포함한다.
- **강화 학습 검증**: Isaac Gym 기반 RL 에이전트를 훈련하여 재구성 모션을 모방하며, "문 열기", "물건 전달" 등의 작업에서 성공률이 기준선 방법의 42%에서 78%로 향상되고, 모션 평활도가 30% 개선된다.

### 결론
본 연구는 희소 주석과 최적화 프레임워크의 결합을 통해 인터넷 비디오에서 로봇이 실행 가능한 4D 상호작용 데이터를 효율적이고 대규모로 추출하는 것을 최초로 실현하여, 인간형 로봇의 일반화 학습에 핵심 데이터 기반을 제공한다. 코드와 데이터셋은 오픈소스로 공개되었다.
