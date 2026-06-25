---
$id: ent_grasp_taxonomy
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: standard
names:
  en: GRASP Taxonomy
  zh: GRASP抓取分类法
  ko: GRASP 분류법
summary:
  en: A standardized classification system for human and robot hand grasps, used to
    evaluate grasp diversity and coverage in dexterous manipulation research.
  zh: 一种用于人类和机器人手部抓取的标准化分类系统，用于评估灵巧操作研究中的抓取多样性和覆盖范围。
  ko: 인간 및 로봇 손의 그립을 분류하는 표준화된 체계로, 능숙한 조작 연구에서 그립 다양성과 커버리지를 평가하는 데 사용됩니다.
domains:
- 10_evaluation_benchmarks
- 06_design_engineering
layers:
- validation_markets
- midstream
functional_roles:
- knowledge
- policy
tags:
- grasp
- taxonomy
- benchmark
- dexterous_manipulation
- hand
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Well-known grasp taxonomy referenced in the RUKA paper for evaluation.
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-25'
---

# GRASP Taxonomy

## 抽象

> **生活实例**：它就像图书馆对“拿东西方式”做的分类目录——把捏、握、托、夹、拧等动作按手形和用途分门别类，方便检索和比较。

> **自然语言逻辑**：GRASP 抓取分类法是一种根据手部姿态、物体接触和任务目标对手部抓取进行标准化分类的系统；它为机器人领域提供了统一的词汇表和测试集，用来评估一只灵巧手能实现多少种不同的抓取类型。

## Overview

The GRASP Taxonomy organizes hand grasps into categories based on hand posture, object contact, and task. It is commonly used in robotics to benchmark how many distinct grasp types a dexterous robot hand can achieve.

## Relevance to Humanoid Robotics

Grasp diversity is a key capability for humanoid hands. The GRASP Taxonomy provides a common vocabulary and test set for comparing hands such as RUKA, LEAP, and Allegro.
