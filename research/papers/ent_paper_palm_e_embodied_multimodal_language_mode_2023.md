---
$id: ent_paper_palm_e_embodied_multimodal_language_mode_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PaLM-E: An Embodied Multimodal Language Model'
  zh: 'PaLM-E: An Embodied Multimodal Language Model'
  ko: 'PaLM-E: An Embodied Multimodal Language Model'
summary:
  en: Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world,
    e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate
    real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
    Input to our embodied language model.
  zh: PaLM-E 是 Google 等机构提出的具身多模态语言模型，将连续传感器观测（图像、状态向量）直接注入预训练语言模型的嵌入空间，实现单一模型同时处理机器人规划、视觉问答和通用语言任务。核心贡献在于证明通过混合少量具身数据（<10%）与大规模互联网数据训练，可让语言模型获得接地（grounding）能力，并在
    562B 参数规模下达到通用 VQA 最先进水平。
  ko: Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world,
    e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate
    real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
    Input to our embodied language model.
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
- palm
- e
- embodied
- multimodal
- language
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P053. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2303.03378 PaLM-E: An Embodied Multimodal Language Model'
  url: https://arxiv.org/abs/2303.03378
  date: '2023-03-06'
  accessed_at: '2026-08-05'
---

## 概述

PaLM-E 是 Google 等机构提出的具身多模态语言模型，将连续传感器观测（图像、状态向量）直接注入预训练语言模型的嵌入空间，实现单一模型同时处理机器人规划、视觉问答和通用语言任务。核心贡献在于证明通过混合少量具身数据（<10%）与大规模互联网数据训练，可让语言模型获得接地（grounding）能力，并在 562B 参数规模下达到通用 VQA 最先进水平。

## 它改变了什么

此前工作（如 SayCan）将 LLM 作为文本接口，输出仅通过 affordance 函数与低层策略耦合，LLM 本身无法感知场景几何或对象状态；而现成 VLM（如 PaLI）虽能处理图像，但零样本下在具身推理任务上完全失效（成功率 0.0）。PaLM-E 真正改变的是：将感知模态从“外部工具”变为“语言模型的内在输入”，使 LLM 的推理能力直接作用于连续观测，而非经过离散化或语义摘要。

这一转变的意义在于，它重新定义了具身智能体的训练范式——不再为每个机器人任务单独训练感知-控制闭环，而是将机器人数据作为多模态训练混合的一部分，让模型同时学习语言先验与物理世界关联。作者用实验证明，这种混合训练不仅不损害通用能力（562B 模型在 NLU 上甚至超过纯文本 PaLM），反而在数据效率上大幅超越从零训练的专用模型。

## 方法拆解

### 架构核心
- 连续观测编码为与语言 token 嵌入同维的向量序列，动态插入文本 token 之间（非固定位置），形成“多模态句子”前缀。
- 公式 (3)：`x_i = γ(w_i)`（文本）或 `φ_j(O_j)_i`（观测），观测可编码为多个嵌入向量。

### 输入编码器变体
- **状态向量**：MLP `φ_state` 将 `s ∈ ℝ^S` 映射到嵌入空间。
- **ViT**：ViT-4B（4B 参数）或 ViT-22B（22B 参数），预训练于图像分类；通过仿射变换 `ψ` 投影。可选对象中心表示（利用掩码 `M_j` 分解 ViT 特征）。
- **OSRT**：基于 SRT 的 3D 神经场景表示，对象槽 `o_j = φ̄_OSRT(I_{1:v})_j`，经 MLP 投影；冻结槽表示，仅训练投影器 `ψ`。

### 训练与推理
- 损失：前缀后 token 的交叉熵（公式 2）。
- 数据混合：Webli 52.4%、VQ2A 13.1%、CC3M 13.1%、机器人数据合计 8.9%（TAMP 1.6%、Language-Table 4.2%、移动操作 3.1%）。
- 推理循环：PaLM-E 以 1 Hz 输出语言子目标，低层策略（RT-1 或 Interactive Language）以 5 Hz 执行动作；每 40 步（10 Hz 持续 4 秒）请求新指令。
- 实体引用：对难以语言标识的对象，在提示中标注“Object 1 is <obj_1>”，使模型可通过特殊 token 引用。

### 模型变体
- PaLM-E-12B（8B LLM + 4B ViT）、PaLM-E-84B（62B + 22B）、PaLM-E-562B（540B + 22B）。
- 冻结 LLM 仅训练编码器，或端到端微调；增大模型规模可显著减少灾难性遗忘。

## 关键创新

1. **观测动态注入而非固定位置**：与 Chen et al. (2022) 等 VLM 不同，观测嵌入可放在文本中任意位置（如“Q: What happened between <img_1> and <img_2>?”），使模型能灵活处理多图像、多时间步的推理，这是后续多模态 LLM 的通用设计。
2. **OSRT 神经场景表示注入**：将 3D 对象槽直接作为 token 输入，无需大规模数据即可在 TAMP 任务上达到 82.5% 规划成功率（1% 数据），证明几何结构化表示与语言模型的结合是数据高效的关键。
3. **规模缓解灾难性遗忘**：562B 模型在 NLG 上仅退化 3.9%（由表内数值 87.3%→3.9% 计算），而 12B 模型退化 87.3%，首次系统证明超大模型可在多模态混合训练中保持语言能力。

## 实验与结果

### TAMP 环境（1% 数据，p1/p2 规划成功率）
| 方法 | p1 | p2 |
|---|---|---|
| SayCan (oracle afford.) | 38.7 | 33.3 |
| PaLI (zero-shot) | 0.0 | 0.0 |
| PaLM-E w/ State (预训练) | 55.9 | 49.7 |
| PaLM-E w/ ViT-4B full mixture | 74.1 | 74.6 |
| PaLM-E w/ OSRT | 82.5 | 76.2 |

### 移动操作（F1 分数）
| 任务 | PaLI | CLIP-FT-hindsight | PaLM-E-12B (full, unfrozen) |
|---|---|---|---|
| 失败检测 | 0.73 | 0.89 | 0.77 |
| Affordance 预测 | 0.62 | - | 0.91 |

### 通用 VQA（VQAv2 test-dev / OK-VQA val）
| 模型 | VQAv2 | OK-VQA |
|---|---|---|
| PaLM-E-12B | 76.2 | 55.5 |
| PaLM-E-562B | 80.0 | 66.1 |
| Flamingo | 82.0 | 57.8 |
| PaLI | 84.3 | 64.5 |

### 数据效率（任务 1，40 demos）
| 配置 | 成功率 |
|---|---|
| Single robot, 从零训练 | 50.0 |
| Full mixture, LLM 冻结 | 20.0 |
| Full mixture, LLM 不冻结 | 80.0 |

关键结论：全混合训练 + 不冻结 LLM 在 40 demos 下将成功率从 50.0 提升至 80.0；OSRT 在 1% 数据下超越 ViT-4B 全混合（82.5 vs 74.1）；562B 模型在 OK-VQA 上超过专门微调的 PaLI（66.1 vs 64.5）。

## 边界与局限

- 冻结 LLM 的方法在 Language-Table 任务上表现不稳定（论文未明确具体数字）。
- 非对象中心 ViT-4B 变体无法处理涉及对象身份的任务（q1），因依赖颜色引用。
- 低层策略（RT-1 等）无法处理长时程任务或复杂指令，PaLM-E 必须自行确定可用技能，无外部约束过滤输出。
- 通用视觉-语言任务并非工作重点，作者未做专门优化；OK-VQA 等结果仅作为附带报告。
- 论文未明确硬件配置、训练时间等工程细节。

## 工程启示

- **先核对数据混合比例**：机器人数据仅占 8.9%，但效果显著；若下游任务数据稀缺，优先考虑混合互联网规模数据而非从零训练。
- **最容易踩坑：LLM 冻结策略**：冻结 LLM 在部分任务（如 Language-Table）上失败，但在移动操作上 F1 达 0.91；复现时应根据任务类型选择是否微调，并优先尝试 84B 以上规模以缓解遗忘。
- **OSRT 是数据高效的关键**：若场景有明确对象几何结构，优先采用 OSRT 而非全局 ViT；其冻结槽表示 + 仅训练投影器的策略可大幅降低计算成本。
- **推理频率匹配**：PaLM-E 1 Hz 输出与低层 5 Hz 控制需严格同步；实际部署时注意延迟预算，避免子目标过期。
- **实体引用机制**：对难以语言描述的对象，务必在提示中显式标注“Object 1 is <obj_1>”，否则模型无法引用，TAMP 中无实体引用时 p1 从 97.7 降至 94.6（6 物体场景）。

## Overview
Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world, e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings. We train these encodings end-to-end, in conjunction with a pre-trained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, and captioning. Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, and further, exhibits positive transfer: the model benefits from diverse joint training across internet-scale language, vision, and visual-language domains. Our largest model, PaLM-E-562B with 562B parameters, in addition to being trained on robotics tasks, is a visual-language generalist with state-of-the-art performance on OK-VQA, and retains generalist language capabilities with increasing scale.

## 参考
- https://arxiv.org/abs/2303.03378

## 개요

PaLM-E는 Google 등 기관이 제안한 구현적(具身) 멀티모달 언어 모델로, 연속 센서 관측(이미지, 상태 벡터)을 사전 학습된 언어 모델의 임베딩 공간에 직접 주입하여 단일 모델로 로봇 계획, 시각 질의응답, 일반 언어 작업을 동시에 처리한다. 핵심 기여는 소량의 구현 데이터(<10%)와 대규모 인터넷 데이터를 혼합 학습함으로써 언어 모델이 접지(grounding) 능력을 획득할 수 있음을 증명하고, 562B 파라미터 규모에서 일반 VQA 최첨단 수준에 도달했다는 점이다.

## 무엇을 바꾸었는가

이전 연구(예: SayCan)는 LLM을 텍스트 인터페이스로 사용하여 출력이 affordance 함수를 통해서만 저수준 정책과 결합되었고, LLM 자체는 장면 기하학이나 객체 상태를 인식할 수 없었다. 반면 기성 VLM(예: PaLI)은 이미지를 처리할 수 있지만, 제로샷에서 구현 추론 작업에 완전히 실패했다(성공률 0.0). PaLM-E가 실제로 바꾼 것은 인식 모달리티를 "외부 도구"에서 "언어 모델의 내재적 입력"으로 전환하여, LLM의 추론 능력이 이산화나 의미 요약을 거치지 않고 연속 관측에 직접 작용하도록 한 것이다.

이 전환의 의미는 구현 에이전트의 훈련 패러다임을 재정의했다는 점이다. 즉, 각 로봇 작업마다 인식-제어 루프를 별도로 훈련하는 대신, 로봇 데이터를 멀티모달 훈련 혼합의 일부로 포함시켜 모델이 언어 사전 지식과 물리 세계 연관성을 동시에 학습하게 한다. 저자들은 실험을 통해 이러한 혼합 훈련이 일반 능력을 손상시키지 않을 뿐만 아니라(562B 모델은 NLU에서 순수 텍스트 PaLM을 오히려 능가), 데이터 효율성에서도 처음부터 훈련한 전용 모델을 크게 능가함을 증명했다.

## 방법 분해

### 아키텍처 핵심
- 연속 관측은 언어 토큰 임베딩과 동일한 차원의 벡터 시퀀스로 인코딩되어 텍스트 토큰 사이에 동적으로 삽입된다(고정 위치가 아님). 이로써 "멀티모달 문장" 접두사가 형성된다.
- 수식 (3): `x_i = γ(w_i)`(텍스트) 또는 `φ_j(O_j)_i`(관측). 관측은 여러 임베딩 벡터로 인코딩될 수 있다.

### 입력 인코더 변형
- **상태 벡터**: MLP `φ_state`가 `s ∈ ℝ^S`를 임베딩 공간으로 매핑한다.
- **ViT**: ViT-4B(4B 파라미터) 또는 ViT-22B(22B 파라미터)로, 이미지 분류로 사전 학습됨. 아핀 변환 `ψ`를 통해 투영된다. 선택적으로 객체 중심 표현(마스크 `M_j`를 이용해 ViT 특징 분해)을 사용할 수 있다.
- **OSRT**: SRT 기반 3D 신경 장면 표현으로, 객체 슬롯 `o_j = φ̄_OSRT(I_{1:v})_j`를 MLP로 투영한다. 슬롯 표현은 고정하고 투영기 `ψ`만 훈련한다.

### 훈련 및 추론
- 손실: 접두사 이후 토큰의 교차 엔트로피(수식 2).
- 데이터 혼합: Webli 52.4%, VQ2A 13.1%, CC3M 13.1%, 로봇 데이터 합계 8.9%(TAMP 1.6%, Language-Table 4.2%, 이동 조작 3.1%).
- 추론 루프: PaLM-E는 1 Hz로 언어 하위 목표를 출력하고, 저수준 정책(RT-1 또는 Interactive Language)은 5 Hz로 동작을 실행한다. 40스텝마다(10 Hz로 4초 지속) 새 지시를 요청한다.
- 엔티티 참조: 언어로 식별하기 어려운 객체는 프롬프트에 "Object 1 is <obj_1>"로 표기하여 모델이 특수 토큰으로 참조할 수 있게 한다.

### 모델 변형
- PaLM-E-12B(8B LLM + 4B ViT), PaLM-E-84B(62B + 22B), PaLM-E-562B(540B + 22B).
- LLM을 고정하고 인코더만 훈련하거나, 엔드투엔드로 미세 조정한다. 모델 규모를 키우면 파괴적 망각을 크게 줄일 수 있다.

## 핵심 혁신

1. **고정 위치가 아닌 동적 관측 주입**: Chen et al. (2022) 등의 VLM과 달리, 관측 임베딩은 텍스트의 임의 위치에 배치될 수 있다(예: "Q: What happened between <img_1> and <img_2>?"). 이를 통해 모델이 다중 이미지, 다중 시간 스텝 추론을 유연하게 처리할 수 있으며, 이는 이후 멀티모달 LLM의 일반적인 설계가 되었다.
2. **OSRT 신경 장면 표현 주입**: 3D 객체 슬롯을 직접 토큰으로 입력하여 대규모 데이터 없이 TAMP 작업에서 82.5%의 계획 성공률(1% 데이터)을 달성했다. 이는 기하학적 구조화 표현과 언어 모델의 결합이 데이터 효율성의 핵심임을 증명한다.
3. **규모를 통한 파괴적 망각 완화**: 562B 모델은 NLG에서 3.9%만 성능이 저하된 반면(표 내 수치 87.3%→3.9%로 계산), 12B 모델은 87.3% 저하되었다. 이는 초대형 모델이 멀티모달 혼합 훈련에서 언어 능력을 유지할 수 있음을 최초로 체계적으로 증명한 것이다.

## 실험 및 결과

### TAMP 환경(1% 데이터, p1/p2 계획 성공률)
| 방법 | p1 | p2 |
|---|---|---|
| SayCan (oracle afford.) | 38.7 | 33.3 |
| PaLI (제로샷) | 0.0 | 0.0 |
| PaLM-E w/ State (사전 학습) | 55.9 | 49.7 |
| PaLM-E w/ ViT-4B full mixture | 74.1 | 74.6 |
| PaLM-E w/ OSRT | 82.5 | 76.2 |

### 이동 조작(F1 점수)
| 작업 | PaLI | CLIP-FT-hindsight | PaLM-E-12B (full, unfrozen) |
|---|---|---|---|
| 실패 감지 | 0.73 | 0.89 | 0.77 |
| Affordance 예측 | 0.62 | - | 0.91 |

### 일반 VQA(VQAv2 test-dev / OK-VQA val)
| 모델 | VQAv2 | OK-VQA |
|---|---|---|
| PaLM-E-12B | 76.2 | 55.5 |
| PaLM-E-562B | 80.0 | 66.1 |
| Flamingo | 82.0 | 57.8 |
| PaLI | 84.3 | 64.5 |

### 데이터 효율성(작업 1, 40 demos)
| 구성 | 성공률 |
|---|---|
| 단일 로봇, 처음부터 훈련 | 50.0 |
| Full mixture, LLM 고정 | 20.0 |
| Full mixture, LLM 비고정 | 80.0 |

핵심 결론: 전체 혼합 훈련 + LLM 비고정은 40 demos에서 성공률을 50.0에서 80.0으로 향상시켰다. OSRT는 1% 데이터에서 ViT-4B 전체 혼합을 능가했다(82.5 vs 74.1). 562B 모델은 OK-VQA에서 전용 미세 조정된 PaLI를 능가했다(66.1 vs 64.5).

## 경계 및 한계

- LLM 고정 방법은 Language-Table 작업에서 불안정한 성능을 보였다(논문에 구체적 수치 미명시).
- 비객체 중심 ViT-4B 변형은 색상 참조에 의존하므로 객체 정체성과 관련된 작업(q1)을 처리할 수 없다.
- 저수준 정책(RT-1 등)은 장기 작업이나 복잡한 지시를 처리할 수 없으며, PaLM-E는 외부 제약 없이 사용 가능한 기술을 스스로 결정해야 한다.
- 일반 시각-언어 작업은 연구의 초점이 아니며, 저자들은 별도 최적화를 수행하지 않았다. OK-VQA 등의 결과는 부수적으로 보고된 것이다.
- 논문은 하드웨어 구성, 훈련 시간 등 엔지니어링 세부 사항을 명시하지 않았다.

## 엔지니어링 시사점

- **먼저 데이터 혼합 비율을 확인하라**: 로봇 데이터는 8.9%에 불과하지만 효과는 크다. 다운스트림 작업 데이터가 부족하다면 처음부터 훈련하는 대신 인터넷 규모 데이터 혼합을 우선 고려하라.
- **가장 흔한 함정: LLM 고정 전략**: LLM 고정은 일부 작업(예: Language-Table)에서 실패하지만, 이동 조작에서는 F1 0.91을 달성했다. 재현 시 작업 유형에 따라 미세 조정 여부를 선택하고, 망각 완화를 위해 84B 이상 규모를 우선 시도하라.
- **OSRT는 데이터 효율성의 핵심**: 장면에 명확한 객체 기하 구조가 있다면 전역 ViT보다 OSRT를 우선 사용하라. 고정 슬롯 표현 + 투영기만 훈련하는 전략은 계산 비용을 크게 줄일 수 있다.
- **추론 빈도 매칭**: PaLM-E의 1 Hz 출력과 저수준 5 Hz 제어는 엄격히 동기화되어야 한다. 실제 배포 시 지연 예산을 고려하여 하위 목표가 만료되지 않도록 주의하라.
- **엔티티 참조 메커니즘**: 언어로 설명하기 어려운 객체는 반드시 프롬프트에 "Object 1 is <obj_1>"로 명시적으로 표기해야 한다. 그렇지 않으면 모델이 참조할 수 없으며, TAMP에서 엔티티 참조가 없을 때 p1이 97.7에서 94.6으로 감소한다(6개 객체 장면).
