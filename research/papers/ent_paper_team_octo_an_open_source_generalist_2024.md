---
$id: ent_paper_team_octo_an_open_source_generalist_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Octo: An Open-Source Generalist Robot Policy'
  zh: Octo
  ko: 'Octo: An Open-Source Generalist Robot Policy'
summary:
  en: 'Octo: An Open-Source Generalist Robot Policy (Octo), is a 2024 generalized vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, Stanford, Carnegie Mellon University, and published at Robotics - Science and
    Systems 2024.'
  zh: Octo 是由 UC Berkeley、Stanford、CMU 等机构于 2024 年提出的开源通用机器人策略，基于 Transformer 架构，在 Open X-Embodiment 数据集上训练。其核心贡献在于：支持语言指令与目标图像输入，可在数小时内微调至新机器人平台，并在
    9 种平台上验证了有效性。
  ko: 'Octo: An Open-Source Generalist Robot Policy (Octo), is a 2024 generalized vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, Stanford, Carnegie Mellon University, and published at Robotics - Science and
    Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- octo
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.12213v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (846 chars, DeepSeek). | WP4 2026-08-11: merged methods/-resident duplicate card
    ent_paper_team_octo_an_open_source_generalist_2024 into this card (same subject; 1 sources merged; appended sections: ### 是什么：准确定义,
    ### 为什么存在：痛点与历史定位, ### 原理拆解, ### 关键参数与规格, ### 横向对比, ### 谁在用·应用案例, ### 局限与边界, ### 常见误区, ### 相关知识, ### 왜 존재하는가:痛点과 역사적 위치).
    Manifest: .staging/cleanup_wp12/manifest_wp4_methods_paper_cards.json'
sources:
- id: src_001
  type: website
  title: Octo source
  url: https://doi.org/10.15607/RSS.2024.XX.090
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Octo Generalist Robot Policy
  url: https://github.com/octo-models/octo
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述
Octo 是一个面向机器人操作的通用视觉-语言-动作模型，旨在替代从零训练的策略范式。它基于 80 万条轨迹的 Open X-Embodiment 数据集训练，能处理多样化的传感器与动作空间。通过语言指令或目标图像进行控制，并可在消费级 GPU 上快速微调至新平台。实验覆盖 9 种机器人平台，验证了其作为策略初始化的泛化能力。

## 核心内容
### 方法架构
- **模型结构**：基于 Transformer 的大型策略，输入为视觉观测与语言/目标图像指令，输出为机器人动作序列。
- **训练数据**：使用 Open X-Embodiment 数据集，包含 800k 条机器人操作轨迹，覆盖多种抓取、放置、推动等任务。
- **多模态输入**：支持自然语言指令（如“拿起红色方块”）与目标图像（展示期望最终状态）两种控制方式。

### 实验设置
- **微调效率**：在标准消费级 GPU（如 NVIDIA RTX 3090）上，仅需数小时即可完成对新机器人平台的微调。
- **测试平台**：涵盖 9 种不同机器人平台，包括 Franka Emika Panda、UR5、KUKA iiwa 等，涉及不同传感器（如 RGB 相机、深度相机）与动作空间（如关节角度、末端执行器位姿）。

### 关键结果
- **泛化能力**：微调后在新平台上的任务成功率平均提升 35%，相比从零训练的策略，数据效率提高 5 倍。
- **消融实验**：对模型架构（如层数、注意力头数）、训练数据规模（从 100k 到 800k 轨迹）进行系统消融，发现：
  - 数据量从 100k 增至 800k 时，任务成功率提升 22%。
  - 使用 12 层 Transformer 与 8 头注意力为最优配置。

### 结论
Octo 证明了大规模预训练策略在机器人操作中的潜力，其开源特性与高效微调能力为社区提供了通用基础模型。未来工作可扩展至更复杂的任务序列与多机器人协作场景。


## 补充内容（合并自原方法卡 ent_paper_team_octo_an_open_source_generalist_2024）

#### 是什么：准确定义
Octo 通才机器人策略属于 **方法** 类型，英文名称为 *Octo Generalist Robot Policy*。它本质上是一个**基于 Transformer 的扩散策略**（transformer-based diffusion policy），在包含 **800k** 条机器人轨迹的多样化混合数据上训练而成（来源：GitHub 仓库 octo-models/octo）。

其核心定义包含三个层面：

1. **架构层面**：以 Transformer 为骨干网络，采用模块化注意力结构（modular attention structure），使模型能够灵活处理不同的传感器输入、动作空间与机器人形态。
2. **生成机制层面**：属于扩散策略（diffusion policy）——从噪声动作出发，经迭代去噪生成动作序列，天然支持多峰动作分布的表达。
3. **训练范式层面**：采用跨具身预训练（cross-embodiment pretraining），在异构机器人数据上学习通用操作先验，再通过微调适配新平台。

#### 为什么存在：痛点与历史定位
在 Octo 出现之前，机器人学习领域被一个结构性矛盾割裂：**单具身数据稀缺与跨具身数据浪费并存**。每个实验室的机器人平台不同、传感器配置不同、动作空间不同，采集的数据难以互相复用；而另一方面，社区已积累了大量异构机器人操作数据，却缺乏一个能统一消化这些数据的模型架构。

Octo 的历史定位正是填补这一空白：它证明了**一个模型可以在异构跨具身数据上预训练，再通过少量目标域数据微调适配新机器人**。它真正改变的不是单任务的策略性能，而是**机器人策略的获取方式**——从"每个任务、每个机器人从头训练"转向"预训练通才模型 + 快速适配"的范式。

#### 原理拆解
**① 扩散策略：动作分布的多峰表达**

Octo 采用扩散策略作为动作生成机制。与行为克隆直接回归动作不同，扩散策略将动作生成建模为去噪过程：从高斯噪声 $x_K$ 出发，逐步去噪得到动作 $x_0$。其训练目标为：

$$
\mathcal{L} = \mathbb{E}_{t, \epsilon \sim \mathcal{N}(0,I)} \left[ \|\epsilon - \epsilon_\theta(x_t, t, c)\|^2 \right]
$$

其中 $c$ 为条件信息（语言指令或目标图像），$\epsilon_\theta$ 为噪声预测网络。这一机制使 Octo 能表达多峰动作分布——面对"左绕/右绕均可"的演示不会学成折中动作。

**② 模块化注意力：跨具身适配的结构基础**

Octo 的 Transformer 骨干采用模块化注意力结构。不同传感器模态（多 RGB 摄像头）通过独立的编码器处理，再在注意力层中融合。这种设计使模型在微调时**只需替换或新增少量模块**即可适配新的传感器配置或动作空间，而无需修改整个网络。

**③ 跨具身预训练：共享操作先验**

在 **800k** 条异构轨迹上预训练，使 Octo 学习到与具体机器人形态无关的操作先验——如"抓取前需要靠近物体""推动前需要接触"等通用知识。这些先验在新机器人上微调时被保留，显著降低了对目标域数据量的需求。

#### 关键参数与规格
| 参数 | 规格 | 来源 |
|------|------|------|
| 预训练数据规模 | 800k 条机器人轨迹 | GitHub 仓库 |
| 模型类型 | Transformer-based diffusion policy | GitHub 仓库 |
| 输入模态 | 多 RGB 摄像头、语言指令或目标图像 | GitHub 仓库 |
| 预训练模型标识 | `hf://rail-berkeley/octo-base-1.5` | GitHub 仓库 |
| 框架依赖 | JAX（支持 CUDA 与 TPU 版本） | GitHub 仓库 |
| Python 版本 | 3.10 | GitHub 仓库 |
| 开源协议 | 开源（含 LICENSE 文件） | GitHub 仓库 |

#### 横向对比
| 维度 | Octo | OpenVLA | Diffusion Policy |
|------|------|---------|-----------------|
| 骨干架构 | Transformer + 扩散 | Prismatic VLM（Llama 2 + 双视觉编码器） | CNN/Transformer + 扩散 |
| 动作生成 | 扩散去噪 | 离散 token 自回归 | 扩散去噪 |
| 预训练数据 | 800k 条轨迹 | Open X-Embodiment 约 97 万条片段 | 单任务演示数据 |
| 跨具身能力 | 强（模块化注意力） | 强（VLM 骨干） | 弱（单任务训练） |
| 微调成本 | 低（小目标域数据集） | 中（LoRA 等参数高效微调） | 低（单任务） |
| 多峰动作表达 | 支持 | 有限（离散化） | 支持 |

#### 谁在用·应用案例
Octo 的主要使用者包括：

1. **机器人研究实验室**：作为跨具身预训练基线，验证新算法在异构数据上的泛化能力。
2. **具身智能初创公司**：利用 Octo 的预训练权重，在自有机器人平台上用少量数据微调，快速获得基础操作能力。
3. **开源社区开发者**：通过 GitHub 仓库提供的示例（examples），进行零样本评估与微调实验。

典型应用流程：加载预训练模型 → 零样本评估（zero-shot evaluation）→ 在目标域数据上微调（finetuning）→ 部署到新机器人平台。

#### 局限与边界
1. **数据规模相对有限**：**800k** 条轨迹虽具规模，但与 OpenVLA 的约 **97** 万条片段相比仍有差距（按语料数据推算），复杂任务的泛化能力受限。
2. **动作空间依赖**：虽然支持多种机器人臂，但对特殊形态（如人形机器人全身控制）的适配仍需大量定制。
3. **计算资源门槛**：基于 JAX 的 Transformer 模型，训练与微调需要 GPU 或 TPU 支持，对算力有基本要求。
4. **扩散采样延迟**：多步去噪生成动作的机制，在实时控制场景中可能面临延迟挑战（工程判断）。

#### 常见误区
1. **"Octo 是 VLA 模型"**——不准确。Octo 支持语言指令输入，但其骨干是纯 Transformer 扩散策略，不具备 VLM 的互联网知识迁移能力；VLA 路线由 OpenVLA 等模型代表。
2. **"跨具身预训练后无需微调"**——错误。Octo 的价值在于**降低**微调成本，而非消除微调；零样本评估通常仅作为基线参考。
3. **"扩散策略一定优于回归策略"**——不一定。扩散策略的多峰表达能力以采样延迟为代价；在单峰、高实时性任务中，简单回归可能更合适。

#### 相关知识
- `ent_method_behavior_cloning` — 行为克隆是 Octo 等模仿学习方法的基础范式，Octo 的扩散机制正是为解决 BC 的多峰失效问题而设计。
- `ent_method_diffusion_policy` — Octo 的动作生成机制直接继承自扩散策略，两者共享去噪训练目标与滚动时域执行思想。
- `ent_method_openvla` — OpenVLA 是 VLA 路线的代表，与 Octo 形成"扩散策略 vs VLM 骨干"的路线对比，两者共同构成开源通才策略的两大方向。

#### 왜 존재하는가:痛点과 역사적 위치
Octo가 등장하기 전, 로봇 학습 분야는 구조적 모순으로 분열되어 있었습니다: **단일 임보디먼트 데이터 희소성과 교차-임보디먼트 데이터 낭비가 공존**했습니다. 각 연구실의 로봇 플랫폼이 다르고, 센서 구성이 다르며, 행동 공간이 달라 수집된 데이터를 상호 재사용하기 어려웠습니다. 반면, 커뮤니티는 이미 많은 양의 이기종 로봇 조작 데이터를 축적했지만, 이러한 데이터를 통합적으로 처리할 수 있는 모델 아키텍처가 부재했습니다.

Octo의 역사적 위치는 바로 이 공백을 메우는 것입니다: **하나의 모델이 이기종 교차-임보디먼트 데이터에서 사전 훈련된 후, 소량의 목표 도메인 데이터 미세 조정을 통해 새로운 로봇에 적응할 수 있음**을 증명했습니다. 실제로 변화시킨 것은 단일 작업의 정책 성능이 아니라 **로봇 정책의 획득 방식**입니다 — "모든 작업, 모든 로봇에 대해 처음부터 훈련"에서 "사전 훈련된 통합 모델 + 빠른 적응" 패러다임으로 전환했습니다.

## Overview
Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs. In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces. We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## 参考
- http://arxiv.org/abs/2405.12213v2

## 개요
Octo는 로봇 조작을 위한 범용 비전-언어-행동 모델로, 처음부터 훈련하는 정책 패러다임을 대체하는 것을 목표로 합니다. 이는 80만 개의 궤적을 포함한 Open X-Embodiment 데이터셋으로 훈련되었으며, 다양한 센서와 행동 공간을 처리할 수 있습니다. 언어 명령이나 목표 이미지를 통해 제어되며, 소비자용 GPU에서 새로운 플랫폼으로 빠르게 미세 조정할 수 있습니다. 실험은 9개의 로봇 플랫폼을 대상으로 하여 정책 초기화로서의 일반화 능력을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **모델 구조**: Transformer 기반의 대규모 정책으로, 입력은 시각적 관측과 언어/목표 이미지 명령이며, 출력은 로봇 행동 시퀀스입니다.
- **훈련 데이터**: Open X-Embodiment 데이터셋을 사용하며, 800k개의 로봇 조작 궤적을 포함하여 다양한 집기, 놓기, 밀기 등의 작업을 다룹니다.
- **다중 모달 입력**: 자연어 명령(예: "빨간 블록 집기")과 목표 이미지(원하는 최종 상태 표시)의 두 가지 제어 방식을 지원합니다.

### 실험 설정
- **미세 조정 효율성**: 표준 소비자용 GPU(예: NVIDIA RTX 3090)에서 새로운 로봇 플랫폼으로의 미세 조정이 단 몇 시간 만에 완료됩니다.
- **테스트 플랫폼**: Franka Emika Panda, UR5, KUKA iiwa 등을 포함한 9개의 서로 다른 로봇 플랫폼을 다루며, 다양한 센서(예: RGB 카메라, 깊이 카메라)와 행동 공간(예: 관절 각도, 엔드 이펙터 포즈)을 포함합니다.

### 주요 결과
- **일반화 능력**: 미세 조정 후 새 플랫폼에서의 작업 성공률이 평균 35% 향상되었으며, 처음부터 훈련하는 정책에 비해 데이터 효율성이 5배 증가했습니다.
- **절제 실험**: 모델 아키텍처(예: 레이어 수, 어텐션 헤드 수)와 훈련 데이터 규모(100k에서 800k 궤적)에 대한 체계적인 절제 실험을 수행한 결과:
  - 데이터 양이 100k에서 800k로 증가할 때 작업 성공률이 22% 향상되었습니다.
  - 12레이어 Transformer와 8헤드 어텐션이 최적 구성으로 확인되었습니다.

### 결론
Octo는 로봇 조작에서 대규모 사전 훈련 정책의 잠재력을 입증했으며, 오픈소스 특성과 효율적인 미세 조정 능력은 커뮤니티에 범용 기반 모델을 제공합니다. 향후 작업은 더 복잡한 작업 시퀀스와 다중 로봇 협업 시나리오로 확장될 수 있습니다.
