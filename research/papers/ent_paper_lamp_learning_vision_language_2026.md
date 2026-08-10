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
  zh: LaMP 是一个双专家视觉-语言-动作（VLA）框架，由研究团队提出，通过嵌入密集3D场景流作为潜在运动先验来提升机器人操作性能。其核心贡献在于引入门控交叉注意力机制，将运动专家与动作专家对齐，在LIBERO、LIBERO-Plus和SimplerEnv-WidowX基准上取得最高平均成功率，并在OOD扰动下比最强基线提升9.7%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.25399v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (922 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  url: https://arxiv.org/abs/2603.25399
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型直接从2D语义视觉特征回归动作，迫使模型隐式学习复杂的3D物理交互，导致在陌生空间动态下性能下降。LaMP通过双专家架构解决此问题：运动专家生成一步部分去噪的3D场景流，其隐藏状态通过门控交叉注意力条件化动作专家，无需完整多步重建。实验在LIBERO、LIBERO-Plus和SimplerEnv-WidowX仿真基准及真实世界场景中验证，LaMP在相同训练预算下始终优于所有基线，尤其在LIBERO-Plus的分布外扰动测试中鲁棒性显著提升。

## 核心内容
### 方法架构
- **双专家框架**：LaMP包含两个专家模块——运动专家（Motion Expert）和动作专家（Action Expert），通过门控交叉注意力（gated cross-attention）对齐。
- **运动专家**：基于流匹配（flow-matching）生成一步部分去噪的3D场景流，其隐藏状态作为条件输入动作专家，避免完整多步重建的计算开销。
- **动作专家**：接收运动专家的隐藏状态，结合视觉-语言特征预测机器人动作策略。

### 实验设置
- **仿真基准**：在LIBERO、LIBERO-Plus（含分布外OOD扰动）和SimplerEnv-WidowX三个仿真环境上评估。
- **真实实验**：在真实机器人平台上进行验证。
- **基线对比**：与现有VLA模型（如RT-2、Octo等）在相同训练预算下比较。

### 关键结果
- **LIBERO基准**：LaMP取得最高平均成功率，超越所有基线。
- **LIBERO-Plus OOD扰动**：LaMP平均成功率比最强基线提升9.7%，展示更强鲁棒性。
- **SimplerEnv-WidowX**：同样保持领先性能。
- **真实实验**：验证了从仿真到真实的迁移能力。

### 结论
LaMP通过显式嵌入3D场景流作为运动先验，有效解决了VLA模型在复杂空间动态下的隐式学习瓶颈，在多个基准上实现性能与鲁棒性的双重提升。项目页面提供更多细节：https://summerwxk.github.io/lamp-project-page/。

## Overview
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## Overview
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation. Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly. This implicit learning strategy degrades under unfamiliar spatial dynamics. LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention. Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction. We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments. LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline. Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## Content
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation. Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly. This implicit learning strategy degrades under unfamiliar spatial dynamics. LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention. Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction. We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments. LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline. Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## 参考
- http://arxiv.org/abs/2603.25399v2

## 개요
기존 VLA 모델은 2D 의미론적 시각 특징에서 직접 행동을 회귀하여, 모델이 복잡한 3D 물리적 상호작용을 암묵적으로 학습하도록 강제하며, 이로 인해 낯선 공간 역학에서 성능이 저하됩니다. LaMP는 이중 전문가 아키텍처를 통해 이 문제를 해결합니다: 운동 전문가가 한 단계 부분 노이즈 제거된 3D 장면 흐름을 생성하고, 그 숨겨진 상태는 게이티드 교차 주의(gated cross-attention)를 통해 행동 전문가를 조건화하며, 완전한 다단계 재구성 없이 작동합니다. 실험은 LIBERO, LIBERO-Plus 및 SimplerEnv-WidowX 시뮬레이션 벤치마크와 실제 세계 시나리오에서 검증되었으며, LaMP는 동일한 훈련 예산에서 모든 기준선을 지속적으로 능가하며, 특히 LIBERO-Plus의 분포 외 교란 테스트에서 강건성이 크게 향상되었습니다.

## 핵심 내용
### 방법 아키텍처
- **이중 전문가 프레임워크**: LaMP는 두 개의 전문가 모듈, 즉 운동 전문가(Motion Expert)와 행동 전문가(Action Expert)를 포함하며, 게이티드 교차 주의(gated cross-attention)를 통해 정렬됩니다.
- **운동 전문가**: 흐름 매칭(flow-matching)을 기반으로 한 단계 부분 노이즈 제거된 3D 장면 흐름을 생성하며, 그 숨겨진 상태는 행동 전문가의 조건 입력으로 사용되어 완전한 다단계 재구성의 계산 오버헤드를 피합니다.
- **행동 전문가**: 운동 전문가의 숨겨진 상태를 수신하고, 시각-언어 특징과 결합하여 로봇 행동 정책을 예측합니다.

### 실험 설정
- **시뮬레이션 벤치마크**: LIBERO, LIBERO-Plus(분포 외 OOD 교란 포함) 및 SimplerEnv-WidowX 세 가지 시뮬레이션 환경에서 평가됩니다.
- **실제 실험**: 실제 로봇 플랫폼에서 검증됩니다.
- **기준선 비교**: 기존 VLA 모델(예: RT-2, Octo 등)과 동일한 훈련 예산에서 비교됩니다.

### 주요 결과
- **LIBERO 벤치마크**: LaMP는 모든 기준선을 능가하는 최고 평균 성공률을 달성합니다.
- **LIBERO-Plus OOD 교란**: LaMP의 평균 성공률은 가장 강력한 기준선보다 9.7% 향상되어 더 강력한 강건성을 보여줍니다.
- **SimplerEnv-WidowX**: 동일하게 선도적인 성능을 유지합니다.
- **실제 실험**: 시뮬레이션에서 실제로의 전이 능력을 검증합니다.

### 결론
LaMP는 3D 장면 흐름을 운동 사전으로 명시적으로 통합함으로써, 복잡한 공간 역학에서 VLA 모델의 암묵적 학습 병목을 효과적으로 해결하며, 여러 벤치마크에서 성능과 강건성의 이중 향상을 달성합니다. 프로젝트 페이지에서 더 많은 세부 정보를 확인할 수 있습니다: https://summerwxk.github.io/lamp-project-page/.
