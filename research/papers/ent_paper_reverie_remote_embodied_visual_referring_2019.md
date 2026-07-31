---
$id: ent_paper_reverie_remote_embodied_visual_referring_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments'
  zh: 'REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments'
  ko: 'REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments'
summary:
  en: 'One of the long-term challenges of robotics is to enable robots to interact with humans in the visual world via natural
    language, as humans are visual animals that communicate through language. Institutions per source list: Yuankai Qi、Qi
    Wu、Peter Anderson、Xin Wang 等.'
  zh: REVERIE 是一个面向真实室内环境的远程具身视觉指代表达数据集，由研究者提出以推动机器人通过自然语言与人类交互。其核心贡献在于要求智能体在未见过的环境中导航并识别物体，现有视觉语言导航和指代表达模型在此任务上表现不佳，而新提出的
    Interactive Navigator-Pointer 模型虽在未见测试集上取得最佳结果，但仍远低于人类水平。
  ko: 'One of the long-term challenges of robotics is to enable robots to interact with humans in the visual world via natural
    language, as humans are visual animals that communicate through language. Institutions per source list: Yuankai Qi、Qi
    Wu、Peter Anderson、Xin Wang 等.'
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
- reverie
- remote
- embodied
- visual
- referring
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 818 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (1904.10151v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:1904.10151 REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments'
  url: https://arxiv.org/abs/1904.10151
  accessed_at: '2026-07-31'
  date: '2019-04-23'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该数据集旨在解决机器人领域长期挑战：使机器人能像人类一样通过自然语言在视觉世界中交互。REVERIE 包含大量真实图像中可见物体的自然语言描述任务，要求智能体根据指令在陌生环境中导航并定位目标物体。测试表明，多个顶尖的视觉语言导航和指代表达模型在此任务上均表现不佳，凸显其难度。研究者提出的 Interactive Navigator-Pointer 模型作为强基线，在未见测试集上达到最优性能，但与人类表现仍有显著差距。

## 核心内容
### 任务定义
REVERIE 任务要求智能体接收自然语言指令后，在先前未探索的真实室内环境中导航，并最终识别出指令所指的物体。这模拟了机器人实际应用中的核心视觉问题。

### 数据集特点
- 基于真实室内环境图像，包含多样化复杂任务
- 指令以自然语言描述，涉及环境中可见物体
- 环境对智能体而言是全新的，需具备泛化能力

### 实验设置
- 测试了多个 state-of-the-art 视觉语言导航模型和指代表达模型
- 所有现有模型均未取得令人满意的结果，表明任务存在根本性差异
- 人类表现作为基准，显示任务仍有巨大提升空间

### 模型与结果
- 提出 Interactive Navigator-Pointer 模型作为强基线
- 该模型在 unseen test split 上达到最佳性能
- 但相比人类表现，仍有 substantial room for improvement

## Overview
One of the long-term challenges of robotics is to enable robots to interact with humans in the visual world via natural language, as humans are visual animals that communicate through language. Overcoming this challenge requires the ability to perform a wide variety of complex tasks in response to multifarious instructions from humans. In the hope that it might drive progress towards more flexible and powerful human interactions with robots, we propose a dataset of varied and complex robot tasks, described in natural language, in terms of objects visible in a large set of real images. Given an instruction, success requires navigating through a previously-unseen environment to identify an object. This represents a practical challenge, but one that closely reflects one of the core visual problems in robotics. Several state-of-the-art vision-and-language navigation, and referring-expression models are tested to verify the difficulty of this new task, but none of them show promising results because there are many fundamental differences between our task and previous ones. A novel Interactive Navigator-Pointer model is also proposed that provides a strong baseline on the task. The proposed model especially achieves the best performance on the unseen test split, but still leaves substantial room for improvement compared to the human performance.

## 参考
- https://arxiv.org/abs/1904.10151
- https://github.com/ImChong/Robotics_Notebooks

## 개요

이 데이터셋은 로봇이 인간처럼 자연어를 통해 시각적 세계에서 상호작용할 수 있도록 하는 로봇 공학의 장기적인 과제를 해결하는 것을 목표로 합니다. REVERIE는 실제 이미지에서 볼 수 있는 객체에 대한 자연어 설명 작업을 대량으로 포함하며, 에이전트가 지시에 따라 익숙하지 않은 환경에서 탐색하고 목표 객체를 찾아내도록 요구합니다. 테스트 결과, 여러 최첨단 시각-언어 내비게이션 및 지시 표현 모델이 이 작업에서 저조한 성능을 보여 그 난이도를 드러냈습니다. 연구자들은 강력한 기준선으로 Interactive Navigator-Pointer 모델을 제안했으며, 이는 보지 못한 테스트 세트에서 최고 성능을 달성했지만 인간의 성능과는 여전히 상당한 차이가 있습니다.

## 핵심 내용
### 작업 정의
REVERIE 작업은 에이전트가 자연어 지시를 받은 후, 이전에 탐색하지 않은 실제 실내 환경에서 탐색하여 최종적으로 지시가 가리키는 객체를 식별하도록 요구합니다. 이는 로봇의 실제 응용에서 핵심적인 시각 문제를 시뮬레이션합니다.

### 데이터셋 특징
- 실제 실내 환경 이미지를 기반으로 하며, 다양하고 복잡한 작업을 포함
- 지시는 자연어로 설명되며, 환경에서 볼 수 있는 객체와 관련
- 환경은 에이전트에게 완전히 새로운 것이므로 일반화 능력이 필요

### 실험 설정
- 여러 최첨단 시각-언어 내비게이션 모델 및 지시 표현 모델을 테스트
- 모든 기존 모델이 만족스러운 결과를 얻지 못해, 작업에 근본적인 차이가 있음을 시사
- 인간의 성능을 기준으로 삼아, 작업에 여전히 큰 개선 여지가 있음을 보여줌

### 모델 및 결과
- 강력한 기준선으로 Interactive Navigator-Pointer 모델을 제안
- 이 모델은 보지 못한 테스트 분할에서 최고 성능을 달성
- 그러나 인간의 성능과 비교하면 여전히 상당한 개선 여지가 있음
