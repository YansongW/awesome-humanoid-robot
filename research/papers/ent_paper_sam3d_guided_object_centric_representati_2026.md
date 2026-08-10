---
$id: ent_paper_sam3d_guided_object_centric_representati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models
  zh: SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models
  ko: SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models
summary:
  en: Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models
    rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion,
    pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment
    framework built upon $π_0$, using.
  zh: SAM3D-VLA 是一种基于 π₀ 架构的视觉-语言-动作模型，通过冻结的 SAM3D 教师网络在训练阶段将目标物体中心的 3D 特征对齐到 RGB 视觉骨干中，推理时保持纯 RGB 管线不变。该方法在 LIBERO、CALVIN
    和真实世界任务上显著提升了长时程操作成功率，尤其改善了遮挡场景下的表现。
  ko: Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models
    rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion,
    pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment
    framework built upon $π_0$, using.
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
- sam3d
- guided
- object
- centric
- representati
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.25912 SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action '
  url: https://arxiv.org/abs/2607.25912
  date: '2026-07-28'
  accessed_at: '2026-08-05'
---

## 概述

SAM3D-VLA 是一种基于 π₀ 架构的视觉-语言-动作模型，通过冻结的 SAM3D 教师网络在训练阶段将目标物体中心的 3D 特征对齐到 RGB 视觉骨干中，推理时保持纯 RGB 管线不变。该方法在 LIBERO、CALVIN 和真实世界任务上显著提升了长时程操作成功率，尤其改善了遮挡场景下的表现。

## 它改变了什么

现有 VLA 模型的核心瓶颈在于：2D 视觉骨干缺乏对目标物体的细粒度 3D 理解，导致在遮挡、姿态变化和精确空间交互中失败。此前引入 3D 信息的方法要么需要额外输入（深度图、点云），要么修改输入输出接口，要么仅关注全局场景级表征，均未解决「目标物体中心」这一关键粒度。本文真正改变的是：在不改变推理管线的前提下，将 3D 物体先验注入 RGB 特征空间，使策略在部署时无需任何 3D 传感器或额外模块即可获得物体级空间理解。这一思路将 3D 知识从「输入模态」转变为「训练监督信号」，是 VLA 3D 化路径上的重要转向。

## 方法拆解

### 训练阶段架构
- 骨干：π₀（SigLIP 视觉编码器 + Gemma 语言模型），冻结 SAM3D 作为 3D 教师。
- 物体定位：Grounding DINO / YOLO 开放词汇检测 + SAM2 分割，生成任务相关物体二值掩码。
- 教师特征提取：多视角观测展平为 (B×V)×3×H×W，图像-掩码对输入冻结 SAM3D，取最后一个 transformer 块输出 T_t ∈ R^(BV)×L_T×D_T。
- 空间重采样：教师序列重塑为 2D 特征网格，移除全局 token，双线性插值到学生视觉 token 分辨率，按视角重组为 T̄_t ∈ R^(B)×(V·L_S)×D_T。
- 学生特征：从 Gemma 选定层提取中间视觉特征 S_t = h_t^(m) ∈ R^(B)×(V·L_S)×D_S，经投影头 P_φ 映射到教师空间：T̂_t = P_φ(S_t)。
- 对齐损失：构建 token 级掩码 m_t 仅监督目标物体 token，双方 ℓ₂ 归一化后计算掩码归一化 MSE：
  L_align = MSE(Norm(T̂_t)[M_t], Norm(T̄_t)[M_t])
- 总目标：L = L_action + α·L_align，其中 L_action 沿用 π₀ 的条件流匹配：
  L_action = E[‖v_θ(A_t^τ, τ, o_t) − (A_t − ε)‖₂²]

### 长时程任务处理
高层指令分解为子任务，每个子任务关联对应物体掩码，提供阶段特定的 3D 监督。

### 推理阶段
仅使用 RGB 图像和语言指令，遵循原始 π₀ 管线，无需深度图、点云、掩码或 SAM3D。

### 冻结表征探测
训练后冻结 VLA 骨干，仅训练两层 MLP 探测头 P_ω 预测重采样的 SAM3D 目标，验证 3D 先验的可恢复性。

## 关键创新

1. **物体中心 3D 对齐范式**：首次将 SAM3D 的密集物体中心特征作为监督信号对齐到 VLA 视觉骨干，而非作为输入模态。这使得 3D 知识在训练时注入、推理时零成本，突破了以往 3D-VLA 对额外传感器的依赖。
2. **token 级掩码监督**：仅对目标物体 token 施加对齐损失，避免背景和无关区域干扰，使监督信号精准聚焦于任务相关物体。这一设计比全局特征对齐更高效，也更符合操作任务的需求。
3. **子任务-物体关联**：在长时程任务中按子任务提供阶段特定 3D 监督，使策略在不同操作阶段关注不同物体，解决了单一全局 3D 表征无法覆盖多阶段任务的问题。

## 实验与结果

### LIBERO 基准（成功率 %）
| 方法 | Spatial | Object | Goal | Long | Average |
|---|---|---|---|---|---|
| SAM3D-VLA | 99.2 | 99.7 | 99.1 | 98.4 | 99.1 |
| π₀ | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| Spatial Forcing | 99.4 | 99.6 | 98.8 | 96.0 | 98.5 |
| GeoVLA | 98.4 | 99.0 | 96.6 | 96.6 | 97.7 |

### CALVIN ABC→D（成功率 %）
| 方法 | 1/5 | 2/5 | 3/5 | 4/5 | 5/5 | Avg. Len |
|---|---|---|---|---|---|---|
| SAM3D-VLA | 96.2 | 89.1 | 80.5 | 73.6 | 71.6 | 4.11 |
| ReconVLA | 95.6 | 87.6 | 76.9 | 69.3 | 64.1 | 3.95 |
| UniVLA | 95.5 | 85.8 | 75.4 | 66.9 | 56.5 | 3.80 |

### 真实世界（成功率 %）
| 设置 | π₀ Average | SAM3D-VLA Average |
|---|---|---|
| 标准 (ST) | 50.2 | 65.2 |
| 遮挡 (OC) | 21.3 | 44.3 |

关键结果：LIBERO Long 任务从 π₀ 的 85.2% 提升至 98.4%（由表内数值 85.2→98.4 计算），CALVIN 5/5 从 64.1% 提升至 71.6%（由表内数值 64.1→71.6 计算），真实世界遮挡场景平均成功率提升 23.0 个百分点（由表内数值 21.3→44.3 计算）。遮挡场景的显著提升验证了 3D 物体中心先验对鲁棒性的核心贡献。

## 边界与局限

- 训练管线依赖自动生成的子任务标注和物体掩码，分解、grounding 或分割错误会引入噪声监督，影响对齐质量。
- SAM3D 仅处理单张图像，在严重遮挡、透明物体或较差视角下可靠性受限，可能限制 3D 先验的上限。
- 真实世界评估仅限单一机器人平台（Piper-X）的桌面任务，未验证跨平台、跨场景泛化。
- 框架虽声称不限于 π₀，但本文仅基于 π₀ 构建，其他骨干上的有效性论文未明确。
- 推理频率、训练步数、batch size、学习率、α 具体取值等关键超参数论文未明确。

## 工程启示

复现时优先核对三点：一是物体掩码生成质量，Grounding DINO / YOLO 与 SAM2 的检测分割精度直接决定对齐监督的有效性，建议在目标场景先做掩码质量评估；二是 SAM3D 教师特征的空间重采样细节，双线性插值到学生 token 分辨率时需确保视角顺序与掩码对齐一致，这是最容易出错的地方；三是 α 的取值平衡，过强会干扰动作学习，过弱则 3D 先验注入不足，论文未明确具体值，需自行调参。对下游团队，若任务涉及精确空间交互或遮挡场景，该方法的收益最明显；若任务以全局导航为主，则收益有限。部署时无需额外 3D 模块，但训练阶段需要 8 块 H100 GPU 和完整的检测-分割-教师特征提取管线，计算成本集中在训练而非推理。

## Overview
Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion, pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment framework built upon $π_0$, using SAM3D as a frozen 3D teacher to provide target-object 3D priors during training. Specifically, we localize task-relevant objects with object recognition models, generate corresponding object masks, and use SAM3D to extract dense object-level 3D representations, which are aligned with intermediate visual features of $π_0$. This enables the policy to internalize target-object 3D information while preserving the original RGB-language-to-action inference pipeline without requiring depth, point clouds, masks, SAM3D, or additional 3D modules at test time. Simulation experiments show consistent improvements, achieving 99.1\% on LIBERO and an average length of 4.11 on CALVIN. Real-world experiments further demonstrate that our method is particularly effective in long-horizon manipulation scenarios where the robot must focus on different target objects across multiple subtasks.

## 参考
- https://arxiv.org/abs/2607.25912

## 개요

SAM3D-VLA는 π₀ 아키텍처 기반의 비전-언어-행동 모델로, 훈련 단계에서 동결된 SAM3D 교사 네트워크를 통해 목표 객체 중심의 3D 특징을 RGB 비전 백본에 정렬하고, 추론 시에는 순수 RGB 파이프라인을 유지합니다. 이 방법은 LIBERO, CALVIN 및 실제 세계 작업에서 장기간 조작 성공률을 크게 향상시켰으며, 특히 폐색(가림) 시나리오에서의 성능을 개선했습니다.

## 무엇을 바꾸었는가

기존 VLA 모델의 핵심 병목은 2D 비전 백본이 목표 객체에 대한 세밀한 3D 이해가 부족하여 폐색, 자세 변화 및 정밀한 공간 상호작용에서 실패한다는 점입니다. 이전에 3D 정보를 도입한 방법들은 추가 입력(깊이 맵, 포인트 클라우드)이 필요하거나, 입출력 인터페이스를 수정하거나, 전역 장면 수준의 표현에만 초점을 맞추어 '목표 객체 중심'이라는 핵심 세분성을 해결하지 못했습니다. 이 논문이 실제로 바꾼 것은 추론 파이프라인을 변경하지 않으면서 3D 객체 사전 지식을 RGB 특징 공간에 주입하여, 정책이 배포 시 3D 센서나 추가 모듈 없이 객체 수준의 공간 이해를 얻을 수 있게 한 것입니다. 이 접근 방식은 3D 지식을 '입력 양식'에서 '훈련 감독 신호'로 전환한 것으로, VLA 3D화 경로에서 중요한 방향 전환입니다.

## 방법 분석

### 훈련 단계 아키텍처
- 백본: π₀(SigLIP 비전 인코더 + Gemma 언어 모델), SAM3D를 3D 교사로 동결.
- 객체 위치 파악: Grounding DINO / YOLO 개방 어휘 탐지 + SAM2 분할로 작업 관련 객체 이진 마스크 생성.
- 교사 특징 추출: 다중 시점 관측을 (B×V)×3×H×W로 펼치고, 이미지-마스크 쌍을 동결된 SAM3D에 입력하여 마지막 트랜스포머 블록 출력 T_t ∈ R^(BV)×L_T×D_T를 획득.
- 공간 리샘플링: 교사 시퀀스를 2D 특징 그리드로 재구성하고, 전역 토큰을 제거한 후 학생 비전 토큰 해상도로 쌍선형 보간하고, 시점별로 재구성하여 T̄_t ∈ R^(B)×(V·L_S)×D_T를 생성.
- 학생 특징: Gemma의 선택된 레이어에서 중간 비전 특징 S_t = h_t^(m) ∈ R^(B)×(V·L_S)×D_S를 추출하고, 프로젝션 헤드 P_φ를 통해 교사 공간으로 매핑: T̂_t = P_φ(S_t).
- 정렬 손실: 토큰 수준 마스크 m_t를 구성하여 목표 객체 토큰만 감독하고, 양쪽 ℓ₂ 정규화 후 마스크 정규화 MSE 계산:
  L_align = MSE(Norm(T̂_t)[M_t], Norm(T̄_t)[M_t])
- 총 목표: L = L_action + α·L_align, 여기서 L_action은 π₀의 조건부 흐름 매칭을 따름:
  L_action = E[‖v_θ(A_t^τ, τ, o_t) − (A_t − ε)‖₂²]

### 장기간 작업 처리
상위 수준 지침을 하위 작업으로 분해하고, 각 하위 작업은 해당 객체 마스크와 연결되어 단계별 3D 감독을 제공합니다.

### 추론 단계
RGB 이미지와 언어 지침만 사용하며, 원래 π₀ 파이프라인을 따르고 깊이 맵, 포인트 클라우드, 마스크 또는 SAM3D가 필요 없습니다.

### 동결 표현 탐지
훈련 후 VLA 백본을 동결하고, 2층 MLP 탐지 헤드 P_ω만 훈련하여 리샘플링된 SAM3D 목표를 예측함으로써 3D 사전 지식의 복원 가능성을 검증합니다.

## 핵심 혁신

1. **객체 중심 3D 정렬 패러다임**: SAM3D의 밀집 객체 중심 특징을 입력 양식이 아닌 감독 신호로 VLA 비전 백본에 정렬한 최초의 사례입니다. 이를 통해 3D 지식이 훈련 시 주입되고 추론 시 비용이 들지 않아, 기존 3D-VLA의 추가 센서 의존성을 극복했습니다.
2. **토큰 수준 마스크 감독**: 목표 객체 토큰에만 정렬 손실을 적용하여 배경 및 무관 영역의 간섭을 방지하고, 감독 신호가 작업 관련 객체에 정밀하게 집중되도록 합니다. 이 설계는 전역 특징 정렬보다 효율적이며 조작 작업 요구에 더 부합합니다.
3. **하위 작업-객체 연관**: 장기간 작업에서 하위 작업별로 단계별 3D 감독을 제공하여 정책이 서로 다른 조작 단계에서 서로 다른 객체에 주목하게 하여, 단일 전역 3D 표현이 다단계 작업을 포괄하지 못하는 문제를 해결합니다.

## 실험 및 결과

### LIBERO 벤치마크 (성공률 %)
| 방법 | Spatial | Object | Goal | Long | Average |
|---|---|---|---|---|---|
| SAM3D-VLA | 99.2 | 99.7 | 99.1 | 98.4 | 99.1 |
| π₀ | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| Spatial Forcing | 99.4 | 99.6 | 98.8 | 96.0 | 98.5 |
| GeoVLA | 98.4 | 99.0 | 96.6 | 96.6 | 97.7 |

### CALVIN ABC→D (성공률 %)
| 방법 | 1/5 | 2/5 | 3/5 | 4/5 | 5/5 | Avg. Len |
|---|---|---|---|---|---|---|
| SAM3D-VLA | 96.2 | 89.1 | 80.5 | 73.6 | 71.6 | 4.11 |
| ReconVLA | 95.6 | 87.6 | 76.9 | 69.3 | 64.1 | 3.95 |
| UniVLA | 95.5 | 85.8 | 75.4 | 66.9 | 56.5 | 3.80 |

### 실제 세계 (성공률 %)
| 설정 | π₀ Average | SAM3D-VLA Average |
|---|---|---|
| 표준 (ST) | 50.2 | 65.2 |
| 폐색 (OC) | 21.3 | 44.3 |

핵심 결과: LIBERO Long 작업이 π₀의 85.2%에서 98.4%로 향상(표 내 수치 85.2→98.4로 계산), CALVIN 5/5가 64.1%에서 71.6%로 향상(표 내 수치 64.1→71.6으로 계산), 실제 세계 폐색 시나리오 평균 성공률이 23.0% 포인트 향상(표 내 수치 21.3→44.3으로 계산). 폐색 시나리오의 현저한 개선은 3D 객체 중심 사전 지식이 견고성에 기여하는 핵심 역할을 검증합니다.

## 경계 및 한계

- 훈련 파이프라인은 자동 생성된 하위 작업 주석과 객체 마스크에 의존하며, 분해, grounding 또는 분할 오류는 노이즈 감독을 유발하여 정렬 품질에 영향을 줄 수 있습니다.
- SAM3D는 단일 이미지만 처리하므로 심한 폐색, 투명 객체 또는 열악한 시점에서 신뢰성이 제한되어 3D 사전 지식의 상한을 제한할 수 있습니다.
- 실제 세계 평가는 단일 로봇 플랫폼(Piper-X)의 데스크톱 작업에만 국한되어 있으며, 플랫폼 간, 장면 간 일반화는 검증되지 않았습니다.
- 프레임워크가 π₀에 국한되지 않는다고 주장하지만, 이 논문은 π₀ 기반으로만 구축되었으며 다른 백본에서의 효과는 논문에 명시되지 않았습니다.
- 추론 빈도, 훈련 스텝 수, 배치 크기, 학습률, α의 구체적인 값 등 핵심 하이퍼파라미터는 논문에 명시되지 않았습니다.

## 엔지니어링 시사점

재현 시 세 가지를 우선 확인해야 합니다: 첫째, 객체 마스크 생성 품질 — Grounding DINO / YOLO와 SAM2의 탐지 분할 정밀도가 정렬 감독의 유효성을 직접 결정하므로, 목표 장면에서 먼저 마스크 품질 평가를 권장합니다; 둘째, SAM3D 교사 특징의 공간 리샘플링 세부 사항 — 학생 토큰 해상도로 쌍선형 보간 시 시점 순서와 마스크 정렬이 일치하는지 확인해야 하며, 이것이 가장 오류가 발생하기 쉬운 부분입니다; 셋째, α 값의 균형 — 너무 강하면 행동 학습을 방해하고, 너무 약하면 3D 사전 지식 주입이 부족하며, 논문에 구체적인 값이 명시되지 않아 자체 튜닝이 필요합니다. 하류 팀의 경우, 작업이 정밀한 공간 상호작용이나 폐색 시나리오를 포함하면 이 방법의 이점이 가장 분명합니다; 작업이 주로 전역 내비게이션이라면 이점이 제한적입니다. 배포 시 추가 3D 모듈이 필요 없지만, 훈련 단계에서는 8개의 H100 GPU와 완전한 탐지-분할-교사 특징 추출 파이프라인이 필요하며, 계산 비용은 추론이 아닌 훈련에 집중됩니다.
