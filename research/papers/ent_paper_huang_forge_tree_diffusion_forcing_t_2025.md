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
  zh: FORGE-Tree 是卡尔斯鲁厄理工学院于 2025 年提出的一种用于长时域机器人操控的大规模视觉-语言-动作模型。其核心贡献在于通过阶段对齐的扩散强制头与蒙特卡洛树扩散机制，在测试时动态分配计算资源，有效缓解了轨迹漂移与曝光偏差问题。在
    LIBERO 基准上，该方法相比原生 VLA 基线（OpenVLA 与 Octo-Base）将成功率提升了 13.4 至 17.2 个百分点。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.21744v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1009 chars, DeepSeek).'
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
长时域机器人操控任务对视觉-语言-动作（VLA）策略而言仍具挑战，主要源于轨迹漂移与曝光偏差——模型以固定超参数对整个轨迹进行去噪，导致微小几何误差在阶段间累积，且缺乏在狭窄间隙处分配额外测试时计算资源的机制。FORGE-Tree 作为可插拔控制层，将阶段对齐的 Diffusion Forcing（DF）头与测试时蒙特卡洛树扩散（MCTD）相结合。在冻结 VLA 编码器的情况下，DF 将时间步与子任务阶段对齐；推理时仅对目标片段进行部分去噪，同时冻结其他 token，将轨迹优化转化为一系列局部编辑。随后通过 MCTD 选择下一个待优化的片段，场景图提供扩展先验与几何关系感知评分，形成树状去噪结构，其性能随搜索预算增加而提升，同时保留已执行的前缀。

## 核心内容
### 方法架构
- **阶段对齐的 Diffusion Forcing（DF）头**：在冻结 VLA 编码器的基础上，DF 将去噪时间步与子任务阶段对齐。推理时仅对目标片段进行部分去噪，其余 token 保持冻结状态，从而将轨迹优化分解为一系列局部编辑。
- **蒙特卡洛树扩散（MCTD）**：通过树搜索选择下一个待优化的片段。场景图为扩展提供先验知识，并在 rollout 阶段进行几何关系感知评分，形成树状去噪结构。该机制允许性能随搜索预算（如计算时间）增加而提升，同时保留已执行的前缀轨迹。

### 实验设置
- **基准测试**：在 LIBERO 基准上进行评估，涵盖多种长时域操控任务。
- **基线模型**：对比原生 VLA 策略 OpenVLA 与 Octo-Base。
- **计算预算**：在可比计算预算下验证性能一致性，尤其关注长时域变体任务。

### 关键结果
- **成功率提升**：FORGE-Tree 在 LIBERO 上相比原生 VLA 基线将成功率提升 13.4 至 17.2 个百分点。
- **计算效率**：在可比计算预算下，性能增益保持稳定，长时域变体任务中优势更为显著。
- **视频演示**：详见项目页面 https://taco-group.github.io/FORGE-Tree/。

### 结论
FORGE-Tree 通过可插拔控制层解决了长时域操控中的轨迹漂移与曝光偏差问题，其树状去噪结构在测试时动态分配计算资源，显著提升了 VLA 策略在复杂任务中的成功率与鲁棒性。

## Overview
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## 参考
- http://arxiv.org/abs/2510.21744v1

## 개요
장시간 영역 로봇 조작 작업은 비전-언어-행동(VLA) 정책에 여전히 도전적이며, 주로 궤적 드리프트와 노출 편향에서 비롯됩니다——모델이 고정 하이퍼파라미터로 전체 궤적을 노이즈 제거하여 미세한 기하학적 오류가 단계 간에 누적되고, 좁은 간격에서 추가 테스트 시간 계산 자원을 할당하는 메커니즘이 부족합니다. FORGE-Tree는 플러그 가능한 제어 계층으로, 단계 정렬 Diffusion Forcing(DF) 헤드와 테스트 시간 몬테카를로 트리 확산(MCTD)을 결합합니다. 고정 VLA 인코더에서 DF는 시간 단계를 하위 작업 단계와 정렬합니다. 추론 시 목표 세그먼트만 부분적으로 노이즈 제거하고 다른 토큰은 동결하여 궤적 최적화를 일련의 로컬 편집으로 변환합니다. 이후 MCTD를 통해 다음 최적화할 세그먼트를 선택하고, 장면 그래프가 확장 사전 정보와 기하학적 관계 인식 점수를 제공하여 트리형 노이즈 제거 구조를 형성하며, 성능은 검색 예산이 증가함에 따라 향상되고 실행된 접두사를 유지합니다.

## 핵심 내용
### 방법 아키텍처
- **단계 정렬 Diffusion Forcing(DF) 헤드**: 고정 VLA 인코더를 기반으로 DF는 노이즈 제거 시간 단계를 하위 작업 단계와 정렬합니다. 추론 시 목표 세그먼트만 부분적으로 노이즈 제거하고 나머지 토큰은 동결 상태를 유지하여 궤적 최적화를 일련의 로컬 편집으로 분해합니다.
- **몬테카를로 트리 확산(MCTD)**: 트리 검색을 통해 다음 최적화할 세그먼트를 선택합니다. 장면 그래프는 확장에 사전 지식을 제공하고 rollout 단계에서 기하학적 관계 인식 점수를 수행하여 트리형 노이즈 제거 구조를 형성합니다. 이 메커니즘은 성능이 검색 예산(예: 계산 시간)이 증가함에 따라 향상되도록 허용하면서 실행된 접두사 궤적을 유지합니다.

### 실험 설정
- **벤치마크**: LIBERO 벤치마크에서 평가하며, 다양한 장시간 영역 조작 작업을 포함합니다.
- **기준 모델**: 원시 VLA 정책 OpenVLA 및 Octo-Base와 비교합니다.
- **계산 예산**: 비교 가능한 계산 예산에서 성능 일관성을 검증하며, 특히 장시간 영역 변형 작업에 중점을 둡니다.

### 주요 결과
- **성공률 향상**: FORGE-Tree는 LIBERO에서 원시 VLA 기준선 대비 성공률을 13.4~17.2퍼센트 포인트 향상시킵니다.
- **계산 효율성**: 비교 가능한 계산 예산에서 성능 이득이 안정적으로 유지되며, 장시간 영역 변형 작업에서 우위가 더 두드러집니다.
- **비디오 데모**: 프로젝트 페이지 https://taco-group.github.io/FORGE-Tree/ 참조.

### 결론
FORGE-Tree는 플러그 가능한 제어 계층을 통해 장시간 영역 조작에서 궤적 드리프트와 노출 편향 문제를 해결하며, 트리형 노이즈 제거 구조가 테스트 시간에 계산 자원을 동적으로 할당하여 복잡한 작업에서 VLA 정책의 성공률과 견고성을 크게 향상시킵니다.
