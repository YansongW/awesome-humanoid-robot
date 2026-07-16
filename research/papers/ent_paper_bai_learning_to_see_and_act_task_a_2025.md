---
$id: ent_paper_bai_learning_to_see_and_act_task_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation'
  zh: TVVE
  ko: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation'
summary:
  en: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University, Pengcheng Laboratory, Nanyang Technological University,
    Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, X-Era AI Lab.'
  zh: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University, Pengcheng Laboratory, Nanyang Technological University,
    Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, X-Era AI Lab.'
  ko: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University, Pengcheng Laboratory, Nanyang Technological University,
    Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, X-Era AI Lab.'
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
- tvve
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.05186v5.
sources:
- id: src_001
  type: paper
  title: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.05186
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: https://hcplab-sysu.github.io/TAVP.

## 核心内容
Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: https://hcplab-sysu.github.io/TAVP.

## 参考
- http://arxiv.org/abs/2508.05186v5

## Overview
Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: https://hcplab-sysu.github.io/TAVP.

## Content
Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: https://hcplab-sysu.github.io/TAVP.

## 개요
최근 다중 작업 로봇 조작을 위한 VLA(Vision-Language-Action) 모델은 고정된 카메라 설정과 공유 시각 인코더에 의존하는 경우가 많아, 폐색 상황 및 교차 작업 전이 시 성능이 제한됩니다. 이러한 문제를 해결하기 위해, 우리는 작업 관련 가상 카메라 시점을 선택하고, 선택된 시점을 사용하여 재구성된 장면 표현에서 관측치를 동적으로 다시 렌더링하는 방법을 학습하는 TVVE(Task-aware Virtual View Exploration) 프레임워크를 제안합니다. 효율적인 시점 선택을 위해, 우리는 가상 환경에서 탐색 정책을 훈련합니다. 또한, 시각적 특징을 작업별 전문가에게 라우팅하여 다중 작업 학습에서의 간섭을 완화하는 TaskMoE(Task-aware Mixture-of-Experts) 시각 인코더를 도입합니다. 분포 변화 하에서의 강건성을 평가하기 위해, 시각적 교란 및 카메라 포즈 변형이 포함된 OOD(Out-of-Distribution) 벤치마크인 RLBench-OG를 구축했습니다. RLBench 및 RLBench-OG 실험은 TVVE가 강력한 기준선보다 높은 성공률을 달성함을 보여주며, 실제 로봇 실험은 시각적 교란 및 보지 못한 명령에 대한 강건성을 추가로 확인합니다. 코드 및 시각화 자료는 다음에서 확인할 수 있습니다: https://hcplab-sysu.github.io/TAVP.

## 핵심 내용
최근 다중 작업 로봇 조작을 위한 VLA(Vision-Language-Action) 모델은 고정된 카메라 설정과 공유 시각 인코더에 의존하는 경우가 많아, 폐색 상황 및 교차 작업 전이 시 성능이 제한됩니다. 이러한 문제를 해결하기 위해, 우리는 작업 관련 가상 카메라 시점을 선택하고, 선택된 시점을 사용하여 재구성된 장면 표현에서 관측치를 동적으로 다시 렌더링하는 방법을 학습하는 TVVE(Task-aware Virtual View Exploration) 프레임워크를 제안합니다. 효율적인 시점 선택을 위해, 우리는 가상 환경에서 탐색 정책을 훈련합니다. 또한, 시각적 특징을 작업별 전문가에게 라우팅하여 다중 작업 학습에서의 간섭을 완화하는 TaskMoE(Task-aware Mixture-of-Experts) 시각 인코더를 도입합니다. 분포 변화 하에서의 강건성을 평가하기 위해, 시각적 교란 및 카메라 포즈 변형이 포함된 OOD(Out-of-Distribution) 벤치마크인 RLBench-OG를 구축했습니다. RLBench 및 RLBench-OG 실험은 TVVE가 강력한 기준선보다 높은 성공률을 달성함을 보여주며, 실제 로봇 실험은 시각적 교란 및 보지 못한 명령에 대한 강건성을 추가로 확인합니다. 코드 및 시각화 자료는 다음에서 확인할 수 있습니다: https://hcplab-sysu.github.io/TAVP.
