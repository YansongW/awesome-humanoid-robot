---
$id: ent_paper_lamp_learning_vision_language_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  zh: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  ko: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
summary:
  en: 'arXiv:2603.25399v2 Announce Type: replace-cross Abstract: We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action
    framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress
    actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This
    implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching
    \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion
    Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without
    full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks
    as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and
    SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On
    LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our
    project page is available at https://summerwxk.github.io/lamp-project-page/.'
  zh: 'arXiv:2603.25399v2 Announce Type: replace-cross Abstract: We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action
    framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress
    actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This
    implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching
    \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion
    Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without
    full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks
    as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and
    SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On
    LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our
    project page is available at https://summerwxk.github.io/lamp-project-page/.'
  ko: 'arXiv:2603.25399v2 Announce Type: replace-cross Abstract: We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action
    framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress
    actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This
    implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching
    \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion
    Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without
    full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks
    as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and
    SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On
    LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our
    project page is available at https://summerwxk.github.io/lamp-project-page/.'
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
- lamp
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.25399v2.
sources:
- id: src_001
  type: paper
  title: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  url: https://arxiv.org/abs/2603.25399
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## 核心内容
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## 参考
- http://arxiv.org/abs/2603.25399v2

## Overview
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation. Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly. This implicit learning strategy degrades under unfamiliar spatial dynamics. LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention. Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction. We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments. LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline. Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## Content
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation. Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly. This implicit learning strategy degrades under unfamiliar spatial dynamics. LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention. Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction. We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments. LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline. Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## 개요
우리는 로봇 조작을 위한 잠재적 모션 사전(latent motion prior)으로 밀집 3D 장면 흐름(dense 3D scene flow)을 내장하는 이중 전문가 비전-언어-행동 프레임워크인 \textbf{LaMP}를 소개합니다. 기존 VLA 모델은 2D 의미론적 시각 특징에서 직접 행동을 회귀(regress)하여 복잡한 3D 물리적 상호작용을 암시적으로 학습해야 합니다. 이러한 암시적 학습 전략은 익숙하지 않은 공간 역학에서 성능이 저하됩니다. LaMP는 게이트 교차 주의(gated cross-attention)를 통해 흐름 정합 \emph{모션 전문가}를 정책 예측 \emph{행동 전문가}와 정렬함으로써 이 한계를 해결합니다. 구체적으로, 모션 전문가는 단일 단계 부분 잡음 제거 3D 장면 흐름을 생성하고, 그 은닉 상태는 완전한 다단계 재구성 없이 행동 전문가를 조건화합니다. 우리는 LaMP를 LIBERO, LIBERO-Plus, SimplerEnv-WidowX 시뮬레이션 벤치마크와 실제 실험에서 평가합니다. LaMP는 LIBERO, LIBERO-Plus, SimplerEnv-WidowX 벤치마크에서 평가된 VLA 기준선을 일관되게 능가하며, 동일한 학습 예산 하에서 가장 높은 평균 성공률을 달성합니다. LIBERO-Plus OOD 변동에서 LaMP는 가장 강력한 이전 기준선 대비 평균 9.7% 향상된 견고성을 보여줍니다. 프로젝트 페이지는 https://summerwxk.github.io/lamp-project-page/에서 확인할 수 있습니다.

## 핵심 내용
우리는 로봇 조작을 위한 잠재적 모션 사전(latent motion prior)으로 밀집 3D 장면 흐름(dense 3D scene flow)을 내장하는 이중 전문가 비전-언어-행동 프레임워크인 \textbf{LaMP}를 소개합니다. 기존 VLA 모델은 2D 의미론적 시각 특징에서 직접 행동을 회귀(regress)하여 복잡한 3D 물리적 상호작용을 암시적으로 학습해야 합니다. 이러한 암시적 학습 전략은 익숙하지 않은 공간 역학에서 성능이 저하됩니다. LaMP는 게이트 교차 주의(gated cross-attention)를 통해 흐름 정합 \emph{모션 전문가}를 정책 예측 \emph{행동 전문가}와 정렬함으로써 이 한계를 해결합니다. 구체적으로, 모션 전문가는 단일 단계 부분 잡음 제거 3D 장면 흐름을 생성하고, 그 은닉 상태는 완전한 다단계 재구성 없이 행동 전문가를 조건화합니다. 우리는 LaMP를 LIBERO, LIBERO-Plus, SimplerEnv-WidowX 시뮬레이션 벤치마크와 실제 실험에서 평가합니다. LaMP는 LIBERO, LIBERO-Plus, SimplerEnv-WidowX 벤치마크에서 평가된 VLA 기준선을 일관되게 능가하며, 동일한 학습 예산 하에서 가장 높은 평균 성공률을 달성합니다. LIBERO-Plus OOD 변동에서 LaMP는 가장 강력한 이전 기준선 대비 평균 9.7% 향상된 견고성을 보여줍니다. 프로젝트 페이지는 https://summerwxk.github.io/lamp-project-page/에서 확인할 수 있습니다.
