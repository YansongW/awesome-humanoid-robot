---
$id: ent_paper_huang_forge_tree_diffusion_forcing_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation'
  zh: FORGE-Tree
  ko: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation'
summary:
  en: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (FORGE-Tree), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology.'
  zh: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (FORGE-Tree), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology.'
  ko: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (FORGE-Tree), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- forge_tree
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.21744v1.
sources:
- id: src_001
  type: paper
  title: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.21744
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FORGE-Tree source
  url: https://doi.org/10.48550/arXiv.2510.21744
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## 核心内容
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## 参考
- http://arxiv.org/abs/2510.21744v1

## Overview
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## Content
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## 개요
장기간 로봇 조작 작업은 드리프트와 노출 편향으로 인해 Vision-Language-Action(VLA) 정책에 여전히 어려움을 겪고 있으며, 고정된 하이퍼파라미터로 전체 궤적을 노이즈 제거하는 경우가 많아 작은 기하학적 오류가 단계별로 누적되고, 간격이 좁은 곳에서 추가 테스트 시간 연산을 할당할 메커니즘이 제공되지 않습니다. 이러한 문제를 해결하기 위해, 우리는 단계 정렬 Diffusion Forcing(DF) 헤드와 테스트 시간 Monte Carlo Tree Diffusion(MCTD)을 결합한 플러그인 제어 계층인 FORGE-Tree를 소개합니다. 고정된 VLA 인코더를 사용하여 DF는 타임스텝을 하위 작업 단계에 정렬합니다. 추론 중에는 다른 토큰을 고정한 상태에서 대상 세그먼트만 부분적으로 노이즈 제거하여 궤적 개선을 일련의 로컬 편집으로 전환합니다. 그런 다음 Monte Carlo Tree Diffusion을 적용하여 개선할 다음 세그먼트를 선택합니다. 장면 그래프는 확장을 위한 사전 정보와 롤아웃을 위한 기하학적 관계 인식 점수를 제공하여, 실행된 접두사를 유지하면서 검색 예산에 따라 성능이 확장되는 트리 구조의 노이즈 제거를 생성합니다. LIBERO에서의 평가 결과, FORGE-Tree는 OpenVLA와 Octo-Base 모두에서 기본 VLA 기준선 대비 성공률을 13.4~17.2% 포인트 향상시킵니다. 이러한 개선은 비슷한 연산 예산 하에서도 일관되게 유지되며, 특히 장기간 변형에서 두드러집니다. 동영상은 다음에서 확인할 수 있습니다: https://taco-group.github.io/FORGE-Tree/

## 핵심 내용
장기간 로봇 조작 작업은 드리프트와 노출 편향으로 인해 Vision-Language-Action(VLA) 정책에 여전히 어려움을 겪고 있으며, 고정된 하이퍼파라미터로 전체 궤적을 노이즈 제거하는 경우가 많아 작은 기하학적 오류가 단계별로 누적되고, 간격이 좁은 곳에서 추가 테스트 시간 연산을 할당할 메커니즘이 제공되지 않습니다. 이러한 문제를 해결하기 위해, 우리는 단계 정렬 Diffusion Forcing(DF) 헤드와 테스트 시간 Monte Carlo Tree Diffusion(MCTD)을 결합한 플러그인 제어 계층인 FORGE-Tree를 소개합니다. 고정된 VLA 인코더를 사용하여 DF는 타임스텝을 하위 작업 단계에 정렬합니다. 추론 중에는 다른 토큰을 고정한 상태에서 대상 세그먼트만 부분적으로 노이즈 제거하여 궤적 개선을 일련의 로컬 편집으로 전환합니다. 그런 다음 Monte Carlo Tree Diffusion을 적용하여 개선할 다음 세그먼트를 선택합니다. 장면 그래프는 확장을 위한 사전 정보와 롤아웃을 위한 기하학적 관계 인식 점수를 제공하여, 실행된 접두사를 유지하면서 검색 예산에 따라 성능이 확장되는 트리 구조의 노이즈 제거를 생성합니다. LIBERO에서의 평가 결과, FORGE-Tree는 OpenVLA와 Octo-Base 모두에서 기본 VLA 기준선 대비 성공률을 13.4~17.2% 포인트 향상시킵니다. 이러한 개선은 비슷한 연산 예산 하에서도 일관되게 유지되며, 특히 장기간 변형에서 두드러집니다. 동영상은 다음에서 확인할 수 있습니다: https://taco-group.github.io/FORGE-Tree/
