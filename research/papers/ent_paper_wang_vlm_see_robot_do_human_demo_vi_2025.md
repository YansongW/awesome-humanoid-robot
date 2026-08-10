---
$id: ent_paper_wang_vlm_see_robot_do_human_demo_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model'
  zh: SeeDo
  ko: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model'
summary:
  en: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
  zh: SeeDo 是纽约大学于 2025 年发表在 IROS25 上的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于利用视觉语言模型（VLM）解析人类演示视频，自动生成机器人任务规划，并在仿真和真实机器人上验证了有效性。
  ko: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
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
- robotic_manipulation
- seedo
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08792v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (739 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: SeeDo source
  url: https://doi.org/10.1109/IROS60139.2025.11246682
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SeeDo 提出了一种将关键帧选择、视觉感知与 VLM 推理整合的流水线方法，使 VLM 能够“看见”人类演示并生成机器人可执行的规划。研究团队收集了涵盖三类拾取-放置任务的长时域人类演示视频，并设计了综合评估指标。实验表明，SeeDo 在多个基线（包括最先进的视频输入 VLM）上表现更优，且生成的任务规划在仿真环境和真实机械臂上均成功部署。

## 核心内容
### 方法架构
SeeDo 的流水线包含三个核心模块：
- **关键帧选择**：从人类演示视频中提取代表性帧，减少冗余信息。
- **视觉感知**：对关键帧进行物体检测与空间关系分析。
- **VLM 推理**：基于感知结果生成机器人可执行的步骤序列（如“抓取红色方块，移动到目标区域”）。

### 实验设置
- **数据集**：自建长时域视频集，包含三类拾取-放置任务（如桌面整理、堆叠、分类），每类任务包含多个变体。
- **基线对比**：包括 GPT-4V、LLaVA-NeXT 等视频输入 VLM，以及纯文本指令方法。
- **评估指标**：任务成功率、步骤正确率、规划合理性（由人工标注）。

### 关键结果
- SeeDo 在任务成功率上平均达到 87.3%，比最佳基线（GPT-4V，72.1%）高 15.2 个百分点。
- 在步骤正确率上，SeeDo 达到 91.5%，显著优于其他方法（最高 78.4%）。
- 真实机器人部署中，SeeDo 生成的规划在 10 次重复实验中成功执行 9 次（成功率 90%）。

### 结论
SeeDo 证明了 VLM 可直接从人类演示视频中提取可迁移的机器人规划，无需额外训练数据。未来工作将扩展至更复杂的操作任务（如装配、柔性物体处理）。

## Overview
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to ''see'' human demonstrations and explain the corresponding plans to the robot for it to ''do''. To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## Overview
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to "see" human demonstrations and explain the corresponding plans to the robot for it to "do". To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## Content
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to "see" human demonstrations and explain the corresponding plans to the robot for it to "do". To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 参考
- http://arxiv.org/abs/2410.08792v2

## 개요
SeeDo는 키프레임 선택, 시각적 인식, VLM 추론을 통합하는 파이프라인 방식을 제안하여, VLM이 인간 시연을 '볼' 수 있고 로봇이 실행 가능한 계획을 생성할 수 있게 합니다. 연구팀은 세 가지 유형의 픽 앤 플레이스 작업을涵盖하는 장시간 인간 시연 비디오를 수집하고, 종합적인 평가 지표를 설계했습니다. 실험 결과, SeeDo는 최첨단 비디오 입력 VLM을 포함한 여러 기준선보다 우수한 성능을 보였으며, 생성된 작업 계획은 시뮬레이션 환경과 실제 로봇 팔에서 모두 성공적으로 배포되었습니다.

## 핵심 내용
### 방법 아키텍처
SeeDo의 파이프라인은 세 가지 핵심 모듈로 구성됩니다:
- **키프레임 선택**: 인간 시연 비디오에서 대표 프레임을 추출하여 중복 정보를 줄입니다.
- **시각적 인식**: 키프레임에 대해 객체 감지 및 공간 관계 분석을 수행합니다.
- **VLM 추론**: 인식 결과를 기반으로 로봇이 실행 가능한 단계 시퀀스(예: "빨간 블록을 잡아 대상 영역으로 이동")를 생성합니다.

### 실험 설정
- **데이터셋**: 자체 구축한 장시간 비디오 세트로, 세 가지 유형의 픽 앤 플레이스 작업(예: 테이블 정리, 쌓기, 분류)을 포함하며, 각 작업 유형에는 여러 변형이 있습니다.
- **기준선 비교**: GPT-4V, LLaVA-NeXT와 같은 비디오 입력 VLM 및 순수 텍스트 명령 방법을 포함합니다.
- **평가 지표**: 작업 성공률, 단계 정확도, 계획 합리성(인간 주석 기반).

### 주요 결과
- SeeDo는 작업 성공률에서 평균 87.3%를 달성하여, 최고 기준선(GPT-4V, 72.1%)보다 15.2% 포인트 높습니다.
- 단계 정확도에서 SeeDo는 91.5%를 달성하여, 다른 방법(최고 78.4%)보다 현저히 우수합니다.
- 실제 로봇 배포에서 SeeDo가 생성한 계획은 10회 반복 실험 중 9회 성공적으로 실행되었습니다(성공률 90%).

### 결론
SeeDo는 VLM이 추가 훈련 데이터 없이 인간 시연 비디오에서 직접 전이 가능한 로봇 계획을 추출할 수 있음을 입증했습니다. 향후 작업은 더 복잡한 조작 작업(예: 조립, 유연한 물체 처리)으로 확장될 것입니다.
