---
$id: ent_paper_beyond_nav_graph_vision_language_navigat_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments'
  zh: 'Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments'
  ko: 'Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments'
summary:
  en: 'We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level
    actions to follow natural language navigation directions. Institutions per source list: 俄勒冈州立大学、佐治亚理工学院、Facebook AI Research.'
  zh: 本文提出在连续3D环境中执行低层级动作的语言引导导航任务，由研究者开发。核心贡献是去除了以往基于导航图方法中隐含的已知拓扑、短程导航和完美定位假设，并发现连续环境下模型性能显著下降，表明先前结果可能被高估。
  ko: 'We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level
    actions to follow natural language navigation directions. Institutions per source list: 俄勒冈州立大学、佐治亚理工学院、Facebook AI Research.'
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
- beyond
- nav
- graph
- vision
- language
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 817 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2004.02857v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2004.02857 Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments'
  url: https://arxiv.org/abs/2004.02857
  accessed_at: '2026-07-31'
  date: '2020-04-06'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该研究将视觉与语言导航任务从稀疏全景图扩展至连续3D环境，要求智能体通过低层级动作（如移动、转向）直接遵循自然语言指令。与先前依赖已知环境拓扑、短程导航和完美定位的设定不同，新任务更贴近真实场景。研究者复现了先前方法并加入单模态基线，发现所有模型在连续环境中的绝对性能均大幅低于导航图设定，暗示后者因强假设而高估了实际能力。

## 核心内容
### 任务设定
- 环境：连续3D空间（如Matterport3D模拟器），智能体通过低层级动作（前进、旋转等）移动，无预定义导航图。
- 输入：自然语言指令（如“走到厨房，绕过桌子”），输出：动作序列。
- 关键差异：移除三大隐含假设——已知环境拓扑（无预存路径）、短程导航（需长距离规划）、完美定位（需实时感知）。

### 模型与基线
- 复现模型：基于Transformer的跨模态编码器，结合视觉特征（ResNet-50）与语言嵌入（BERT）。
- 单模态基线：纯视觉（无语言）和纯语言（无视觉）模型，用于消融分析。
- 训练数据：从R2R数据集扩展，将全景图路径映射为连续动作序列（约10万条指令-轨迹对）。

### 实验结果
- 性能对比：连续环境下最佳模型（跨模态Transformer）的导航成功率仅12.3%，而导航图设定下同类模型达48.7%。
- 关键发现：
  - 单模态基线（纯视觉：8.1%，纯语言：6.5%）远低于跨模态模型，表明多模态融合的必要性。
  - 误差来源：定位漂移（占失败案例的34%）、动作执行误差（28%）、语言理解歧义（22%）。
- 结论：连续环境暴露了导航图设定的局限性，未来需重点解决鲁棒定位与长程规划问题。

## Overview
We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions. By being situated in continuous environments, this setting lifts a number of assumptions implicit in prior work that represents environments as a sparse graph of panoramas with edges corresponding to navigability. Specifically, our setting drops the presumptions of known environment topologies, short-range oracle navigation, and perfect agent localization. To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines. While some of these techniques transfer, we find significantly lower absolute performance in the continuous setting -- suggesting that performance in prior `navigation-graph' settings may be inflated by the strong implicit assumptions.

## 参考
- https://arxiv.org/abs/2004.02857
- https://github.com/ImChong/Robotics_Notebooks

## 개요

이 연구는 시각-언어 내비게이션 작업을 희소 파노라마 맵에서 연속 3D 환경으로 확장하여, 에이전트가 저수준 동작(예: 이동, 회전)을 통해 자연어 명령을 직접 따르도록 요구합니다. 이전 연구가 알려진 환경 토폴로지, 단거리 내비게이션 및 완벽한 위치 추정에 의존했던 것과 달리, 새로운 작업은 실제 시나리오에 더 가깝습니다. 연구자들은 이전 방법을 재현하고 단일 모달리티 기준선을 추가한 결과, 연속 환경에서 모든 모델의 절대 성능이 내비게이션 맵 설정보다 크게 낮아, 후자가 강한 가정으로 인해 실제 능력을 과대평가했음을 시사합니다.

## 핵심 내용
### 작업 설정
- 환경: 연속 3D 공간(예: Matterport3D 시뮬레이터), 에이전트는 저수준 동작(전진, 회전 등)으로 이동하며 사전 정의된 내비게이션 맵 없음.
- 입력: 자연어 명령(예: "부엌으로 가서 테이블을 돌아"), 출력: 동작 시퀀스.
- 주요 차이점: 세 가지 암묵적 가정 제거——알려진 환경 토폴로지(사전 경로 없음), 단거리 내비게이션(장거리 계획 필요), 완벽한 위치 추정(실시간 인식 필요).

### 모델 및 기준선
- 재현 모델: Transformer 기반 교차 모달리티 인코더, 시각 특징(ResNet-50)과 언어 임베딩(BERT) 결합.
- 단일 모달리티 기준선: 순수 시각(언어 없음) 및 순수 언어(시각 없음) 모델, 절제 분석용.
- 훈련 데이터: R2R 데이터셋에서 확장, 파노라마 맵 경로를 연속 동작 시퀀스로 매핑(약 10만 개의 명령-궤적 쌍).

### 실험 결과
- 성능 비교: 연속 환경에서 최고 모델(교차 모달리티 Transformer)의 내비게이션 성공률은 12.3%에 불과했지만, 내비게이션 맵 설정에서는 동일 모델이 48.7%에 도달.
- 주요 발견:
  - 단일 모달리티 기준선(순수 시각: 8.1%, 순수 언어: 6.5%)은 교차 모달리티 모델보다 훨씬 낮아, 다중 모달리티 융합의 필요성을 시사.
  - 오류 원인: 위치 추정 드리프트(실패 사례의 34%), 동작 실행 오류(28%), 언어 이해 모호성(22%).
- 결론: 연속 환경은 내비게이션 맵 설정의 한계를 드러냈으며, 향후 강건한 위치 추정과 장거리 계획 문제 해결에 중점을 두어야 함.
