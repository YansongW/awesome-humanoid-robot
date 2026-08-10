---
$id: ent_paper_look_where_it_matters_adaptive_visual_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Models'
  zh: 'Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Models'
  ko: 'Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Models'
summary:
  en: Visual representations of VLA models remain unreliable for spatially precise robotic manipulation. We uncover that vision
    encoders in VLAs also exhibit attention artifacts previously documented in generic Vision Transformers, and further show
    that, in embodied policies, these artifacts are closely associated with spatial perception capabilities acquired during
    post-training. As the encoder learns.
  zh: 本文提出 AtVLA（Attention-guided Vision-Language-Action）模型，通过寄存器增强视觉编码与不确定性门控的注意力引导裁剪机制，解决 VLA 模型在精细操作中因全局视觉编码不足导致的定位不精确问题。该方法在预训练
    π₀ 模型基础上分三阶段后训练，在 LIBERO 基准上将平均成功率从 94.2% 提升至 98.4%，真实世界成功率从 46.5% 提升至 69.0%，总计算量仅为 π₀ 的 1.4–1.6 倍。
  ko: Visual representations of VLA models remain unreliable for spatially precise robotic manipulation. We uncover that vision
    encoders in VLAs also exhibit attention artifacts previously documented in generic Vision Transformers, and further show
    that, in embodied policies, these artifacts are closely associated with spatial perception capabilities acquired during
    post-training. As the encoder learns.
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
- look
- where
- it
- matters
- adaptive
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. [2026-08-05] experiments section regenerated under programmatic
    number whitelist (guardrail fix: previous numbers unverifiable against full text); en/ko regenerated. 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.02197 Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Mod'
  url: https://arxiv.org/abs/2608.02197
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---



## 概述

本文提出 AtVLA（Attention-guided Vision-Language-Action）模型，通过寄存器增强视觉编码与不确定性门控的注意力引导裁剪机制，解决 VLA 模型在精细操作中因全局视觉编码不足导致的定位不精确问题。该方法在预训练 π₀ 模型基础上分三阶段后训练，在 LIBERO 基准上将平均成功率从 94.2% 提升至 98.4%，真实世界成功率从 46.5% 提升至 69.0%，总计算量仅为 π₀ 的 1.4–1.6 倍。

## 它改变了什么

这项工作的真正价值在于它改变了 VLA 模型处理视觉信息的基本范式。此前，VLA 模型要么依赖固定分辨率的全局视觉编码，要么引入显式视觉专家或 3D 表示——前者在精细操作中因局部几何细节不足而失败，后者则带来额外的传感、标定和建模开销。AtVLA 的核心判断是：模型不需要在所有时刻都看到高分辨率图像，只需要在"不确定"的时候，基于自身动作条件注意力动态选择任务相关区域进行局部细化。

这种"按需细化"的思路打破了两个隐含假设：一是视觉编码必须全程一致，二是细化必须依赖外部信号（如 VLM 或标注）。作者证明，动作专家自身的注意力分布已经包含了足够的空间定位信息，可以作为裁剪的信号源。同时，他们发现视觉编码器中的注意力伪影（高范数伪影）并非纯粹噪声，而是与后训练获得的空间感知能力密切相关——这促使他们用寄存器 token 来吸收这些伪影，而非简单地抑制它们。这一发现本身就对 VLA 视觉表征的理解有独立贡献。

## 方法拆解

### 三阶段后训练流程
- **Stage 0（寄存器适应，20K 步）**：前 4K 步仅更新 4 个寄存器嵌入（θ_reg），学习率 1×10⁻⁴；后 16K 步额外解冻 SigLIP 最后 4 个 transformer 块（θ_vis^last），学习率 2×10⁻⁵。PaliGemma 骨干、视觉投影器和动作专家保持冻结。
- **Stage 1（真值裁剪对齐，10K 步）**：仅使用标注任务相关区域的真值裁剪，禁用裁剪丢弃。优化裁剪位置编码器和 rank-32 LoRA 适配器（插入语言和动作组件），学习率 1×10⁻⁴。SigLIP 编码器、寄存器嵌入、视觉投影器和预训练骨干权重全部冻结。
- **Stage 2（联合细化与推理对齐，40K 步）**：联合优化完整 AtVLA 策略，SigLIP、Gemma 和动作专家的基础权重冻结，三者的 rank-32 LoRA 适配器可训练，寄存器嵌入、视觉投影器和裁剪位置编码器直接优化。使用 AdamW，batch size 4，恒定学习率 1×10⁻⁴。

### 联合目标函数
ℒ_joint = ℒ_π₀ + λ_ag·ℒ_ag，其中 λ_ag = 1.0。ℒ_ag = −log( (Σ_{p∈Ω(b^gt)} A_p + ε) / (Σ_p A_p + ε) )，A_p 为近端动作 token 对基础图像 patch p 的聚合注意力，Ω(b^gt) 为标注任务相关区域内 patch 中心的集合。

### 不确定性门控细化
- 每个动作块重规划步骤，基础视觉和语言前缀计算一次并存储在可复用键值缓存中。
- 动作专家从独立高斯初始化生成 K = 4 个动作块，使用十步 Euler 求解器。
- 不确定性 U_t 基于前 h 个动作的平移维度（Δx, Δy, Δz）计算：U_t = (1/(h|D_tr|)) Σ_{j=1}^{h} Σ_{d∈D_tr} sqrt( (1/(K−1)) Σ_{k=1}^{K} (A_{j,d}^{(k)} − Ā_{j,d})² )
- 当 U_t ≤ τ 时直接执行均值动作块；U_t > τ 时尝试注意力引导裁剪细化（仅一次额外裁剪编码和一次额外动作生成）。

### 注意力 rollout 聚合
从动作专家全部 18 个联合注意力层收集动作到前缀注意力，在头部和 Euler 去噪步骤 {3, 6, 9} 上平均。逐层传播：M_roll = M̃_L · M̃_{L−1} · … · M̃_1，其中 M̃_l = RowNorm(I + (1/(|H||Q|)) Σ_{m∈H} Σ_{q∈Q} M_{l,m,q})。将前 h 个动作 token 行到 256 个基础图像 patch 列的 rollout 条目平均，重塑为 16×16 显著性图，双线性上采样到原始图像分辨率。寄存器 token 列被排除。

### 对比窗口搜索
候选窗口边长 S = {84, 112, 140} 像素，在 224×224 输入图像上以 14 像素步长搜索。选择最大化内部注意力均值与上下文环（边长扩展 1.25 倍）注意力均值之差的窗口。选定框每侧填充 10%，裁剪并调整至 224×224。归一化坐标通过两层裁剪位置 MLP（4→256→d_LLM，GELU 激活）映射，位置嵌入加到每个投影裁剪 patch token。

### 裁剪课程
在 40K 步联合训练中：前 40% α = 0，p_drop = 0，所有裁剪来自真值区域；40%–90% α 从 0 线性增至 1，裁剪丢弃概率从 0 线性增至 0.3，无效 rollout 不回退到真值裁剪，而是跳过裁剪细化；最后 10% α = 1，p_drop = 0.3，所有有效非丢弃裁剪来自注意力 rollout。

## 关键创新

1. **寄存器 token 的具身化训练**：与通用 ViT 中寄存器仅作为内部工作空间不同，AtVLA 保留寄存器输出并通过视觉投影器送入语言骨干，且完全用具身数据和动作监督训练。作者发现混合 ImageNet 和 CC3M 数据会破坏机器人演示获得的能力，因此放弃通用视觉预训练——这一决策挑战了"视觉编码器应先通用预训练再具身微调"的常见假设。

2. **不确定性门控的按需细化**：用动作采样的样本间标准差作为空间不确定性的代理指标，仅在必要时触发裁剪。这种设计将计算开销从"总是细化"降为"按需细化"，总计算量仅为 π₀ 的 1.4–1.6 倍，同时保持约 30% 的触发率。门控在每个动作块重规划步骤评估而非每个低级控制步骤，进一步控制开销。

3. **注意力 rollout 作为裁剪信号源**：从动作专家的联合注意力层逐层传播，生成 16×16 显著性图，用对比窗口搜索（内部 vs 上下文环）选择裁剪区域。这一设计避免了外部 VLM 或标注依赖，且对比准则同时避免全图裁剪和孤立注意力峰的小窗口——这是对"注意力图直接 argmax"朴素方法的实质性改进。

## 实验与结果


## 实验与结果

**对照设置。** 我们在 LIBERO 四个标准套件（Spatial、Object、Goal、Long-10）、SimplerEnv Google Robot 套件以及 Franka Research 3 机器人上的真实世界基准（Kitchen 与 Building Blocks）中，将 AtVLA 与预训练 π₀ 基线、π₀.₅、SpatialVLA、CoT-VLA、OFT、VLANeXt、RT-1-X、RT-2-X、RoboVLM、TraceVLA 等公开基线，以及两个受控变体（π₀ + Registers、π₀ + Cropping）进行对比。所有 AtVLA 变体从同一预训练 π₀ 检查点初始化，训练分布在 8 张 NVIDIA RTX 6000 Ada GPU 上，真实世界部署使用 NVIDIA RTX 4090 GPU 与 Franka Research 3 机器人。训练采用三阶段课程：寄存器适配 20K 步、裁剪对齐 10K 步、联合精炼 40K 步，联合目标权重 λ_ag = 1.0，LoRA 秩为 32，批大小为 4（Stage 2），输入分辨率统一为 224×224。不确定性门控在每次动作块重规划步评估一次，裁剪触发率约为 30% 的重规划步。

| 基准 | π₀ 基线 | π₀ + Registers | π₀ + Cropping | AtVLA (Full) |
|---|---|---|---|---|
| LIBERO Spatial | 96.8 ± 1.3 | 98.8 ± 0.6 | 96.5 ± 1.3 | 99.3 ± 0.7 |
| LIBERO Object | 98.8 ± 1.2 | 99.0 ± 0.8 | 98.2 ± 1.2 | 99.4 ± 0.8 |
| LIBERO Goal | 95.8 ± 1.5 | 98.0 ± 0.9 | 96.7 ± 1.5 | 98.3 ± 1.2 |
| LIBERO Long-10 | 85.2 ± 1.0 | 93.1 ± 1.7 | 93.3 ± 2.1 | 96.5 ± 2.6 |
| SimplerEnv PCC | 88.0 | 88.2 | 90.0 | 91.3 |
| SimplerEnv MN | 80.3 | 80.5 | 79.2 | 81.6 |
| SimplerEnv O/C | 56.0 | 56.0 | 56.9 | 57.5 |
| 真实世界（平均） | 46.5 | 论文未明确 | 论文未明确 | 69.0 |

**结果含义。** 以下几点值得强调：

- **分阶段训练与注意力接地目标共同带来一致增益。** AtVLA 在 LIBERO 平均成功率从 π₀ 基线的 94.2% 提升至 98.4%，真实世界平均成功率从 46.5% 提升至 69.0%。在 Long-10 套件上，AtVLA 达到 96.5 ± 2.6，显著高于 π₀ 的 85.2 ± 1.0，也高于仅加寄存器（93.1 ± 1.7）和仅加裁剪（93.3 ± 2.1）的变体，说明两个组件互补而非冗余。寄存器 token 的消融（w/o REGs）在 LIBERO 各套件上平均下降 4.45 个百分点，证实寄存器不仅抑制注意力伪影，还保留任务相关的具身空间信息——线性探针在物体定位、深度、表面法线三项上均超过 0.70。

- **裁剪课程与不确定性门控控制计算开销。** 裁剪触发率约为 30% 的重规划步，且精炼路径仅执行一次额外裁剪编码和一次额外动作生成，而非重复全部 K 次采样（K = 4）。总计算量为 π₀ 的 1.4–1.6×。在 SimplerEnv 的 Open/Close Drawer 场景中，裁剪几乎保留整图而非解析把手或接触点，导致 AtVLA 在该任务上（57.5）仅略高于 π₀（56.0），论文将此归因于橱柜占据大部分画面时裁剪难以隔离关键区域。

- **真实世界长时程任务增益最为明显。** 在 Kitchen 套件中，AtVLA 的 Move 达到 80 ± 10、Grab 达到 65 ± 5、Pick 达到 80 ± 5、Long 达到 40 ± 5；在 Building Blocks 套件中，Stack 达到 80 ± 5、Edge 达到 50 ± 10、Grab 达到 70 ± 10。相比之下，π₀ 基线在 Kitchen Long 仅为 15 ± 5、Building Blocks Edge 仅为 25 ± 5。增益在物体中心任务（Kitchen Grab/Pick）和空间要求高的任务（Building Blocks Spatial/Grab）上尤为突出，与注意力接地目标将视觉容量集中于交互区域的机制一致。

## 边界与局限

论文未明确列出作者承认的局限，但可从实验细节推断若干边界。SimplerEnv Open/Close Drawer 场景中裁剪效果次优，因为场景大部分被柜子占据，裁剪几乎保留整个原始图像而非解决把手或接触点——这说明对比窗口搜索在"目标区域占图像大部分"时失效。π_0 + Cropping 的裁剪由外部 VLM 生成（无具身后训练），性能略低于完整 AtVLA，表明裁剪质量对最终性能有显著影响。不准确的裁剪会扭曲策略输入、降低决策精度、增加动作不确定性。

论文未提及多视角融合策略的详细消融、不同机器人平台泛化、训练数据规模细节、推理延迟的具体毫秒数。真实世界实验仅覆盖 Franka Research 3 和 Google Robot 两种具身，且未报告 Google Robot 的具体训练数据量。省略 SimplerEnv WidowX 套件，因需 BridgeData 特定训练和具身适应，会混淆视觉改进与具身迁移——这意味着跨具身泛化结论的适用范围有限。

## 工程启示

复现 AtVLA 时，最值得先核对的是三阶段训练的顺序和冻结策略。Stage 0 的寄存器适应是后续一切的基础——作者明确发现混合 ImageNet 和 CC3M 数据会破坏机器人演示获得的能力，因此寄存器必须完全用具身数据训练。如果跳过或缩短 Stage 0，后续的注意力 rollout 质量可能直接崩溃，因为寄存器未充分吸收注意力伪影。

最容易踩坑的地方是裁剪课程的设计。Stage 2 中前 40% 步必须完全使用真值裁剪（α = 0），40%–90% 逐步过渡到注意力 rollout，且无效 rollout 不回退到真值裁剪而是跳过细化。如果过早引入模型自身生成的裁剪，策略可能学到对噪声注意力信号的错误依赖。另一个关键细节是无效 rollout 的判定规则（非有限值、注意力质量 < ε = 10⁻⁶、窗口搜索无有限候选分数、裁剪边长 < 56 像素）必须在训练和部署时完全一致，否则会产生训练-测试差异。

对于下游团队，建议先在小规模数据上验证寄存器适应是否显著改善注意力图质量（可用线性探针检查寄存器特征在物体定位上的分数是否超过 0.70），再投入完整的三阶段训练。不确定性阈值 τ 需要按具身分别校准，LIBERO 四个套件共享同一阈值，但 Google Robot 和 Franka 需独立校准——初始值设为验证不确定性分布的第 70 百分位，目标触发率约 30%。计算成本方面，K = 4 动作采样和十步 Euler 求解器是主要开销，裁剪细化约占 20–25% 总成本，如果硬件资源紧张，可考虑先降低 K 或减少 rollout 去噪步骤数。

## 参考
- https://arxiv.org/abs/2608.02197

## Overview

This paper proposes the AtVLA (Attention-guided Vision-Language-Action) model, which addresses the issue of imprecise localization in VLA models during fine manipulation tasks caused by insufficient global visual encoding, through register-enhanced visual encoding and uncertainty-gated attention-guided cropping mechanisms. The method employs a three-stage post-training approach on the pretrained π₀ model, improving average success rates from 94.2% to 98.4% on the LIBERO benchmark and from 46.5% to 69.0% in real-world settings, with total computation only 1.4–1.6 times that of π₀.

## What It Changes

The true value of this work lies in how it changes the fundamental paradigm of visual information processing in VLA models. Previously, VLA models either relied on fixed-resolution global visual encoding or introduced explicit vision experts or 3D representations—the former fails in fine manipulation due to insufficient local geometric detail, while the latter introduces additional sensing, calibration, and modeling overhead. AtVLA's core insight is that the model does not need to see high-resolution images at all times; it only needs to dynamically select task-relevant regions for local refinement based on its own action-conditioned attention when "uncertain."

This "on-demand refinement" approach breaks two implicit assumptions: first, that visual encoding must remain consistent throughout, and second, that refinement must rely on external signals (such as VLMs or annotations). The authors demonstrate that the action expert's own attention distribution already contains sufficient spatial localization information to serve as a signal source for cropping. Additionally, they discover that attention artifacts (high-norm artifacts) in the vision encoder are not pure noise but are closely related to spatial awareness capabilities acquired during post-training—this motivates them to use register tokens to absorb these artifacts rather than simply suppress them. This finding itself constitutes an independent contribution to the understanding of VLA visual representations.

## Method Breakdown

### Three-Stage Post-Training Pipeline
- **Stage 0 (Register Adaptation, 20K steps)**: The first 4K steps update only the 4 register embeddings (θ_reg) with a learning rate of 1×10⁻⁴; the subsequent 16K steps additionally unfreeze the last 4 transformer blocks of SigLIP (θ_vis^last) with a learning rate of 2×10⁻⁵. The PaliGemma backbone, vision projector, and action expert remain frozen.
- **Stage 1 (Ground-Truth Cropping Alignment, 10K steps)**: Uses only ground-truth crops of annotated task-relevant regions, with crop dropping disabled. Optimizes the cropping position encoder and rank-32 LoRA adapters (inserted into language and action components) with a learning rate of 1×10⁻⁴. The SigLIP encoder, register embeddings, vision projector, and pretrained backbone weights are all frozen.
- **Stage 2 (Joint Refinement and Inference Alignment, 40K steps)**: Jointly optimizes the full AtVLA policy. The base weights of SigLIP, Gemma, and the action expert are frozen, while their rank-32 LoRA adapters are trainable. Register embeddings, vision projector, and cropping position encoder are directly optimized. Uses AdamW, batch size 4, and a constant learning rate of 1×10⁻⁴.

### Joint Objective Function
ℒ_joint = ℒ_π₀ + λ_ag·ℒ_ag, where λ_ag = 1.0. ℒ_ag = −log( (Σ_{p∈Ω(b^gt)} A_p + ε) / (Σ_p A_p + ε) ), where A_p is the aggregated attention from proximal action tokens to base image patch p, and Ω(b^gt) is the set of patch centers within the annotated task-relevant region.

### Uncertainty-Gated Refinement
- At each action chunk replanning step, base vision and language prefixes are computed once and stored in a reusable key-value cache.
- The action expert generates K = 4 action chunks from independent Gaussian initializations using a ten-step Euler solver.
- Uncertainty U_t is computed based on the translation dimensions (Δx, Δy, Δz) of the first h actions: U_t = (1/(h|D_tr|)) Σ_{j=1}^{h} Σ_{d∈D_tr} sqrt( (1/(K−1)) Σ_{k=1}^{K} (A_{j,d}^{(k)} − Ā_{j,d})² )
- When U_t ≤ τ, the mean action chunk is executed directly; when U_t > τ, attention-guided cropping refinement is attempted (only one additional crop encoding and one additional action generation).

### Attention Rollout Aggregation
Action-to-prefix attention is collected from all 18 joint attention layers of the action expert, averaged over heads and Euler denoising steps {3, 6, 9}. Layer-wise propagation: M_roll = M̃_L · M̃_{L−1} · … · M̃_1, where M̃_l = RowNorm(I + (1/(|H||Q|)) Σ_{m∈H} Σ_{q∈Q} M_{l,m,q}). The rollout entries from the first h action token rows to the 256 base image patch columns are averaged, reshaped into a 16×16 saliency map, and bilinearly upsampled to the original image resolution. Register token columns are excluded.

### Contrastive Window Search
Candidate window side lengths S = {84, 112, 140} pixels are searched on the 224×224 input image with a 14-pixel stride. The window maximizing the difference between internal attention mean and context ring (side length expanded by 1.25×) attention mean is selected. The chosen box is padded by 10% on each side, cropped, and resized to 224×224. Normalized coordinates are mapped through a two-layer cropping position MLP (4→256→d_LLM, GELU activation), and position embeddings are added to each projected crop patch token.

### Cropping Curriculum
During the 40K-step joint training: for the first 40%, α = 0, p_drop = 0, and all crops come from ground-truth regions; from 40%–90%, α increases linearly from 0 to 1, crop dropping probability increases linearly from 0 to 0.3, and invalid rollouts do not fall back to ground-truth crops but instead skip crop refinement; for the final 10%, α = 1, p_drop = 0.3, and all valid non-dropped crops come from attention rollouts.

## Key Innovations

1. **Embodied Training of Register Tokens**: Unlike general ViTs where registers serve only as internal working space, AtVLA retains register outputs and feeds them through the vision projector into the language backbone, trained entirely with embodied data and action supervision. The authors find that mixing ImageNet and CC3M data destroys capabilities acquired from robot demonstrations, so they abandon general visual pretraining—a decision that challenges the common assumption that "vision encoders should first undergo general pretraining before embodied fine-tuning."

2. **Uncertainty-Gated On-Demand Refinement**: Uses the inter-sample standard deviation of action sampling as a proxy indicator for spatial uncertainty, triggering refinement only when necessary. This design reduces computational overhead from "always refine" to "refine on demand," keeping total computation at only 1.4–1.6 times that of π₀ while maintaining approximately 30% trigger rate. The gate is evaluated at each action chunk replanning step rather than each low-level control step, further controlling overhead.

3. **Attention Rollout as Cropping Signal Source**: Propagates layer by layer through the action expert's joint attention layers to generate a 16×16 saliency map, using contrastive window search (internal vs. context ring) to select the cropping region. This design avoids dependence on external VLMs or annotations, and the contrastive criterion simultaneously avoids full-image cropping and small windows around isolated attention peaks—a substantial improvement over the naive "direct argmax of attention map" approach.

## Experiments and Results

**Comparison Setup.** We compare AtVLA against the pretrained π₀ baseline, π₀.₅, SpatialVLA, CoT-VLA, OFT, VLANeXt, RT-1-X, RT-2-X, RoboVLM, TraceVLA, and other public baselines, as well as two controlled variants (π₀ + Registers, π₀ + Cropping), across the four standard LIBERO suites (Spatial, Object, Goal, Long-10), the SimplerEnv Google Robot suite, and real-world benchmarks on the Franka Research 3 robot (Kitchen and Building Blocks). All AtVLA variants are initialized from the same pretrained π₀ checkpoint, with training distributed across 8 NVIDIA RTX 6000 Ada GPUs, and real-world deployment using NVIDIA RTX 4090 GPUs with the Franka Research 3 robot. Training follows a three-stage curriculum: register adaptation for 20K steps, cropping alignment for 10K steps, and joint refinement for 40K steps, with joint objective weight λ_ag = 1.0, LoRA rank 32, batch size 4 (Stage 2), and unified input resolution of 224×224. The uncertainty gate is evaluated once per action chunk replanning step, with a crop trigger rate of approximately 30% of replanning steps.

| Benchmark | π₀ Baseline | π₀ + Registers | π₀ + Cropping | AtVLA (Full) |
|---|---|---|---|---|
| LIBERO Spatial | 96.8 ± 1.3 | 98.8 ± 0.6 | 96.5 ± 1.3 | 99.3 ± 0.7 |
| LIBERO Object | 98.8 ± 1.2 | 99.0 ± 0.8 | 98.2 ± 1.2 | 99.4 ± 0.8 |
| LIBERO Goal | 95.8 ± 1.5 | 98.0 ± 0.9 | 96.7 ± 1.5 | 98.3 ± 1.2 |
| LIBERO Long-10 | 85.2 ± 1.0 | 93.1 ± 1.7 | 93.3 ± 2.1 | 96.5 ± 2.6 |
| SimplerEnv PCC | 88.0 | 88.2 | 90.0 | 91.3 |
| SimplerEnv MN | 80.3 | 80.5 | 79.2 | 81.6 |
| SimplerEnv O/C | 56.0 | 56.0 | 56.9 | 57.5 |
| Real-World (Average) | 46.5 | Not specified in paper | Not specified in paper | 69.0 |

**Implications of Results.** The following points deserve emphasis:

- **Staged training combined with the attention grounding objective yields consistent gains.** AtVLA improves the average LIBERO success rate from 94.2% for the π₀ baseline to 98.4%, and the average real-world success rate from 46.5% to 69.0%. On the Long-10 suite, AtVLA achieves 96.5 ± 2.6, significantly higher than π₀'s 85.2 ± 1.0, and also higher than the register-only (93.1 ± 1.7) and cropping-only (93.3 ± 2.1) variants, indicating that the two components are complementary rather than redundant. Ablation of register tokens (w/o REGs) results in an average drop of 4.45 percentage points across LIBERO suites, confirming that registers not only suppress attention artifacts but also preserve task-relevant embodied spatial information—linear probes exceed 0.70 on all three tasks of object localization, depth, and surface normals.

- **The cropping curriculum and uncertainty gate control computational overhead.** The crop trigger rate is approximately 30% of replanning steps, and the refinement path performs only one additional crop encoding and one additional action generation, rather than repeating all K samples (K = 4). Total computation is 1.4–1.6× that of π₀. In the SimplerEnv Open/Close Drawer scenario, cropping preserves nearly the entire image rather than resolving the handle or contact point, causing AtVLA to achieve only marginal improvement (57.5) over π₀ (56.0) on this task; the paper attributes this to the difficulty of isolating key regions when the cabinet occupies most of the frame.

- **Real-world long-horizon tasks show the most significant gains.** In the Kitchen suite, AtVLA achieves Move at 80 ± 10, Grab at 65 ± 5, Pick at 80 ± 5, and Long at 40 ± 5; in the Building Blocks suite, Stack reaches 80 ± 5, Edge reaches 50 ± 10, and Grab reaches 70 ± 10. In contrast, the π₀ baseline achieves only 15 ± 5 on Kitchen Long and 25 ± 5 on Building Blocks Edge. Gains are particularly pronounced on object-centric tasks (Kitchen Grab/Pick) and spatially demanding tasks (Building Blocks Spatial/Grab), consistent with the mechanism by which the attention grounding objective concentrates visual capacity on interaction regions.

## Boundaries and Limitations

The paper does not explicitly list limitations acknowledged by the authors, but several boundaries can be inferred from experimental details. In the SimplerEnv Open/Close Drawer scenario, cropping is suboptimal because the scene is largely occupied by the cabinet, causing cropping to preserve nearly the entire original image rather than resolving the handle or contact point—indicating that the contrastive window search fails when the target region occupies most of the image. The π₀ + Cropping variant, whose crops are generated by an external VLM (without embodied post-training), performs slightly worse than the full AtVLA, suggesting that crop quality significantly impacts final performance. Inaccurate crops distort policy inputs, reduce decision precision, and increase action uncertainty.

The paper does not mention detailed ablations of multi-view fusion strategies, generalization across different robot platforms, training data scale details, or specific inference latency in milliseconds. Real-world experiments cover only two embodiments—Franka Research 3 and Google Robot—and the specific training data volume for Google Robot is not reported. The SimplerEnv WidowX suite is omitted because it requires BridgeData-specific training and embodiment adaptation, which would confound visual improvements with embodiment transfer—this implies that the applicability of cross-embodiment generalization conclusions is limited.

## Engineering Insights

When reproducing AtVLA, the most critical aspects to verify first are the ordering of the three-stage training and the freezing strategy. Stage 0's register adaptation is the foundation for everything that follows—the authors explicitly find that mixing ImageNet and CC3M data destroys capabilities acquired from robot demonstrations, so registers must be trained entirely with embodied data. If Stage 0 is skipped or shortened, the quality of subsequent attention rollouts may collapse directly, because registers have not sufficiently absorbed attention artifacts.

The most likely pitfall lies in the design of the cropping curriculum. In Stage 2, the first 40% of steps must use ground-truth crops exclusively (α = 0), with a gradual transition to attention rollouts from 40%–90%, and invalid rollouts do not fall back to ground-truth crops but instead skip refinement. If model-generated crops are introduced too early, the policy may learn a spurious dependence on noisy attention signals. Another critical detail is that the invalidity determination rules for rollouts (non-finite values, attention quality < ε = 10⁻⁶, no finite candidate scores in window search, crop side length < 56 pixels) must be completely consistent between training and deployment; otherwise, a train-test discrepancy will arise.

For downstream teams, it is recommended to first validate on small-scale data whether register adaptation significantly improves attention map quality (using linear probes to check whether register features exceed 0.70 on object localization scores) before committing to the full three-stage training. The uncertainty threshold τ needs to be calibrated separately per embodiment; the four LIBERO suites share the same threshold, but Google Robot and Franka require independent calibration—set the initial value to the 70th percentile of the validation uncertainty distribution, targeting a trigger rate of approximately 30%. In terms of computational cost, K = 4 action sampling and the ten-step Euler solver are the primary overhead, with crop refinement accounting for approximately 20–25% of total cost; if hardware resources are constrained, consider first reducing K or decreasing the number of rollout denoising steps.

## 개요

본 논문은 AtVLA(Attention-guided Vision-Language-Action) 모델을 제안하며, 레지스터 강화 시각 인코딩과 불확실성 게이팅 기반의 어텐션 유도 크롭 메커니즘을 통해 VLA 모델이 정밀 조작에서 전역 시각 인코딩 부족으로 인해 발생하는 위치 파악 부정확성 문제를 해결합니다. 이 방법은 사전 훈련된 π₀ 모델을 기반으로 3단계 후속 훈련을 수행하며, LIBERO 벤치마크에서 평균 성공률을 94.2%에서 98.4%로, 실제 세계 성공률을 46.5%에서 69.0%로 향상시키고, 총 계산량은 π₀의 1.4–1.6배에 불과합니다.

## 무엇을 변화시키는가

이 작업의 진정한 가치는 VLA 모델이 시각 정보를 처리하는 기본 패러다임을 변화시킨다는 점입니다. 이전에는 VLA 모델이 고정 해상도의 전역 시각 인코딩에 의존하거나 명시적 시각 전문가 또는 3D 표현을 도입했습니다. 전자는 정밀 조작에서 국소 기하학적 세부 정보 부족으로 실패하고, 후자는 추가적인 센싱, 캘리브레이션 및 모델링 비용을 초래합니다. AtVLA의 핵심 판단은 모델이 모든 시점에서 고해상도 이미지를 볼 필요가 없으며, "불확실한" 시점에만 자체 동작 조건부 어텐션을 기반으로 작업 관련 영역을 동적으로 선택하여 국소 정밀화를 수행하면 된다는 것입니다.

이러한 "요구 기반 정밀화" 접근 방식은 두 가지 암묵적 가정을 깨뜨립니다. 첫째, 시각 인코딩이 전체 과정에서 일관되어야 한다는 가정, 둘째, 정밀화가 외부 신호(예: VLM 또는 주석)에 의존해야 한다는 가정입니다. 저자들은 동작 전문가 자체의 어텐션 분포가 이미 충분한 공간 위치 정보를 포함하고 있어 크롭 신호 소스로 사용될 수 있음을 증명합니다. 동시에, 그들은 시각 인코더의 어텐션 아티팩트(고노름 아티팩트)가 순수한 노이즈가 아니라 후속 훈련에서 획득한 공간 인식 능력과 밀접하게 관련되어 있음을 발견합니다. 이는 이러한 아티팩트를 단순히 억제하는 대신 레지스터 토큰으로 흡수하도록 유도합니다. 이 발견 자체는 VLA 시각 표현 이해에 독립적인 기여를 합니다.

## 방법 분해

### 3단계 후속 훈련 프로세스
- **Stage 0 (레지스터 적응, 20K 스텝)**: 처음 4K 스텝에서는 4개의 레지스터 임베딩(θ_reg)만 업데이트하며 학습률은 1×10⁻⁴입니다. 이후 16K 스텝에서는 SigLIP의 마지막 4개 transformer 블록(θ_vis^last)을 추가로 해제하며 학습률은 2×10⁻⁵입니다. PaliGemma 백본, 시각 프로젝터 및 동작 전문가는 동결 상태를 유지합니다.
- **Stage 1 (정답 크롭 정렬, 10K 스텝)**: 주석이 달린 작업 관련 영역의 정답 크롭만 사용하며 크롭 드롭아웃을 비활성화합니다. 크롭 위치 인코더와 rank-32 LoRA 어댑터(언어 및 동작 컴포넌트에 삽입)를 최적화하며 학습률은 1×10⁻⁴입니다. SigLIP 인코더, 레지스터 임베딩, 시각 프로젝터 및 사전 훈련된 백본 가중치는 모두 동결됩니다.
- **Stage 2 (결합 정밀화 및 추론 정렬, 40K 스텝)**: 완전한 AtVLA 정책을 결합 최적화하며, SigLIP, Gemma 및 동작 전문가의 기본 가중치는 동결되고 세 가지의 rank-32 LoRA 어댑터는 훈련 가능하며, 레지스터 임베딩, 시각 프로젝터 및 크롭 위치 인코더는 직접 최적화됩니다. AdamW, batch size 4, 일정 학습률 1×10⁻⁴을 사용합니다.

### 결합 목적 함수
ℒ_joint = ℒ_π₀ + λ_ag·ℒ_ag, 여기서 λ_ag = 1.0입니다. ℒ_ag = −log( (Σ_{p∈Ω(b^gt)} A_p + ε) / (Σ_p A_p + ε) ), A_p는 근위 동작 토큰의 기본 이미지 패치 p에 대한 집계 어텐션이며, Ω(b^gt)는 주석이 달린 작업 관련 영역 내 패치 중심의 집합입니다.

### 불확실성 게이팅 정밀화
- 각 동작 블록 재계획 단계에서 기본 시각 및 언어 프리픽스는 한 번 계산되어 재사용 가능한 키-값 캐시에 저장됩니다.
- 동작 전문가는 독립적인 가우시안 초기화에서 K = 4개의 동작 블록을 생성하며 10단계 Euler 솔버를 사용합니다.
- 불확실성 U_t는 처음 h개 동작의 병진 차원(Δx, Δy, Δz)을 기반으로 계산됩니다: U_t = (1/(h|D_tr|)) Σ_{j=1}^{h} Σ_{d∈D_tr} sqrt( (1/(K−1)) Σ_{k=1}^{K} (A_{j,d}^{(k)} − Ā_{j,d})² )
- U_t ≤ τ일 때 평균 동작 블록을 직접 실행합니다. U_t > τ일 때 어텐션 유도 크롭 정밀화를 시도합니다(추가 크롭 인코딩 1회 및 추가 동작 생성 1회만 수행).

### 어텐션 롤아웃 집계
동작 전문가의 전체 18개 결합 어텐션 레이어에서 동작-프리픽스 어텐션을 수집하고, 헤드 및 Euler 디노이징 스텝 {3, 6, 9}에서 평균을 냅니다. 레이어별 전파: M_roll = M̃_L · M̃_{L−1} · … · M̃_1, 여기서 M̃_l = RowNorm(I + (1/(|H||Q|)) Σ_{m∈H} Σ_{q∈Q} M_{l,m,q})입니다. 처음 h개 동작 토큰 행에서 256개 기본 이미지 패치 열로의 롤아웃 항목을 평균하여 16×16 유의성 맵으로 재구성하고, 이중선형 업샘플링으로 원본 이미지 해상도로 확대합니다. 레지스터 토큰 열은 제외됩니다.

### 대비 창 검색
후보 창 변 길이 S = {84, 112, 140} 픽셀로, 224×224 입력 이미지에서 14픽셀 스텝으로 검색합니다. 내부 어텐션 평균과 컨텍스트 링(변 길이 1.25배 확장) 어텐션 평균 간의 차이를 최대화하는 창을 선택합니다. 선택된 박스의 각 측면에 10% 패딩을 추가하고, 크롭하여 224×224로 조정합니다. 정규화된 좌표는 2계층 크롭 위치 MLP(4→256→d_LLM, GELU 활성화)를 통해 매핑되며, 위치 임베딩은 각 프로젝션된 크롭 패치 토큰에 추가됩니다.

### 크롭 커리큘럼
40K 스텝 결합 훈련에서: 처음 40%는 α = 0, p_drop = 0이며 모든 크롭은 정답 영역에서 옵니다. 40%–90%는 α가 0에서 1로 선형 증가하고, 크롭 드롭아웃 확률은 0에서 0.3으로 선형 증가하며, 무효 롤아웃은 정답 크롭으로 폴백하지 않고 크롭 정밀화를 건너뜁니다. 마지막 10%는 α = 1, p_drop = 0.3이며 모든 유효한 비드롭 크롭은 어텐션 롤아웃에서 옵니다.

## 핵심 혁신

1. **레지스터 토큰의 구현화 훈련**: 일반 ViT에서 레지스터가 내부 작업 공간으로만 사용되는 것과 달리, AtVLA는 레지스터 출력을 유지하고 시각 프로젝터를 통해 언어 백본으로 전달하며, 완전히 구현 데이터와 동작 감독으로 훈련합니다. 저자들은 ImageNet과 CC3M 데이터를 혼합하면 로봇 시연에서 얻은 능력이 손상된다는 것을 발견하고 일반 시각 사전 훈련을 포기합니다. 이 결정은 "시각 인코더는 먼저 일반 사전 훈련 후 구현 미세 조정"이라는 일반적인 가정에 도전합니다.

2. **불확실성 게이팅 기반 요구형 정밀화**: 동작 샘플링의 샘플 간 표준 편차를 공간 불확실성의 대리 지표로 사용하여 필요한 경우에만 크롭을 트리거합니다. 이 설계는 계산 비용을 "항상 정밀화"에서 "요구 기반 정밀화"로 낮추어 총 계산량을 π₀의 1.4–1.6배로 유지하면서 약 30%의 트리거율을 유지합니다. 게이팅은 각 동작 블록 재계획 단계에서 평가되며, 각 저수준 제어 스텝이 아닌 단위로 평가되어 추가 비용을 제어합니다.

3. **어텐션 롤아웃을 크롭 신호 소스로 사용**: 동작 전문가의 결합 어텐션 레이어에서 레이어별 전파를 통해 16×16 유의성 맵을 생성하고, 대비 창 검색(내부 vs 컨텍스트 링)을 통해 크롭 영역을 선택합니다. 이 설계는 외부 VLM 또는 주석 의존성을 피하며, 대비 기준은 전체 이미지 크롭과 고립된 어텐션 피크의 작은 창을 동시에 피합니다. 이는 "어텐션 맵 직접 argmax"의 단순한 방법에 대한 실질적인 개선입니다.

## 실험 및 결과

**대조 설정.** 우리는 LIBERO 4개 표준 스위트(Spatial, Object, Goal, Long-10), SimplerEnv Google Robot 스위트, Franka Research 3 로봇의 실제 세계 벤치마크(Kitchen 및 Building Blocks)에서 AtVLA를 사전 훈련된 π₀ 베이스라인, π₀.₅, SpatialVLA, CoT-VLA, OFT, VLANeXt, RT-1-X, RT-2-X, RoboVLM, TraceVLA 등의 공개 베이스라인, 그리고 두 개의 통제 변형(π₀ + Registers, π₀ + Cropping)과 비교합니다. 모든 AtVLA 변형은 동일한 사전 훈련된 π₀ 체크포인트에서 초기화되며, 훈련 분포는 8장의 NVIDIA RTX 6000 Ada GPU에서, 실제 세계 배포는 NVIDIA RTX 4090 GPU와 Franka Research 3 로봇에서 수행됩니다. 훈련은 3단계 커리큘럼을 사용합니다: 레지스터 적응 20K 스텝, 크롭 정렬 10K 스텝, 결합 정밀화 40K 스텝, 결합 목표 가중치 λ_ag = 1.0, LoRA 랭크 32, 배치 크기 4(Stage 2), 입력 해상도는 224×224로 통일됩니다. 불확실성 게이팅은 각 동작 블록 재계획 단계에서 한 번 평가되며, 크롭 트리거율은 재계획 단계의 약 30%입니다.

| 벤치마크 | π₀ 베이스라인 | π₀ + Registers | π₀ + Cropping | AtVLA (Full) |
|---|---|---|---|---|
| LIBERO Spatial | 96.8 ± 1.3 | 98.8 ± 0.6 | 96.5 ± 1.3 | 99.3 ± 0.7 |
| LIBERO Object | 98.8 ± 1.2 | 99.0 ± 0.8 | 98.2 ± 1.2 | 99.4 ± 0.8 |
| LIBERO Goal | 95.8 ± 1.5 | 98.0 ± 0.9 | 96.7 ± 1.5 | 98.3 ± 1.2 |
| LIBERO Long-10 | 85.2 ± 1.0 | 93.1 ± 1.7 | 93.3 ± 2.1 | 96.5 ± 2.6 |
| SimplerEnv PCC | 88.0 | 88.2 | 90.0 | 91.3 |
| SimplerEnv MN | 80.3 | 80.5 | 79.2 | 81.6 |
| SimplerEnv O/C | 56.0 | 56.0 | 56.9 | 57.5 |
| 실제 세계 (평균) | 46.5 | 논문 미명시 | 논문 미명시 | 69.0 |

**결과 의미.** 다음 사항을 강조할 가치가 있습니다:

- **단계적 훈련과 어텐션 접지 목표가 함께 일관된 이득을 가져옵니다.** AtVLA는 LIBERO 평균 성공률을 π₀ 베이스라인의 94.2%에서 98.4%로, 실제 세계 평균 성공률을 46.5%에서 69.0%로 향상시킵니다. Long-10 스위트에서 AtVLA는 96.5 ± 2.6에 도달하여 π₀의 85.2 ± 1.0보다 현저히 높고, 레지스터만 추가한 변형(93.1 ± 1.7)과 크롭만 추가한 변형(93.3 ± 2.1)보다도 높아 두 컴포넌트가 중복이 아닌 상호 보완적임을 보여줍니다. 레지스터 토큰의 제거(w/o REGs)는 LIBERO 각 스위트에서 평균 4.45퍼센트 포인트 하락하여, 레지스터가 어텐션 아티팩트를 억제할 뿐만 아니라 작업 관련 구현 공간 정보를 유지함을 확인합니다. 선형 프로브는 객체 위치 파악, 깊이, 표면 법선 세 항목 모두에서 0.70을 초과합니다.

- **크롭 커리큘럼과 불확실성 게이팅이 계산 비용을 제어합니다.** 크롭 트리거율은 재계획 단계의 약 30%이며, 정밀화 경로는 K = 4 전체 샘플링을 반복하지 않고 추가 크롭 인코딩 1회와 추가 동작 생성 1회만 수행합니다. 총 계산량은 π₀의 1.4–1.6배입니다. SimplerEnv의 Open/Close Drawer 시나리오에서 크롭은 핸들이나 접촉점을 분석하는 대신 거의 전체 이미지를 유지하여, AtVLA가 해당 작업(57.5)에서 π₀(56.0)보다 약간만 높습니다. 논문은 캐비닛이 화면의 대부분을 차지할 때 크롭이 핵심 영역을 분리하기 어렵기 때문이라고 설명합니다.

- **실제 세계 장기간 작업에서 이득이 가장 두드러집니다.** Kitchen 스위트에서 AtVLA의 Move는 80 ± 10, Grab은 65 ± 5, Pick은 80 ± 5, Long은 40 ± 5에 도달합니다. Building Blocks 스위트에서 Stack은 80 ± 5, Edge는 50 ± 10, Grab은 70 ± 10에 도달합니다. 반면 π₀ 베이스라인은 Kitchen Long에서 15 ± 5, Building Blocks Edge에서 25 ± 5에 불과합니다. 이득은 객체 중심 작업(Kitchen Grab/Pick)과 공간 요구가 높은 작업(Building Blocks Spatial/Grab)에서 특히 두드러지며, 이는 어텐션 접지 목표가 시각 용량을 상호작용 영역에 집중시키는 메커니즘과 일치합니다.

## 경계 및 한계

논문은 저자가 인정한 한계를 명시적으로 나열하지 않았지만, 실험 세부 사항에서 몇 가지 경계를 추론할 수 있습니다. SimplerEnv Open/Close Drawer 시나리오에서 크롭 효과가 차선인 이유는 장면의 대부분이 캐비닛으로 채워져 크롭이 핸들이나 접촉점을 해결하는 대신 거의 전체 원본 이미지를 유지하기 때문입니다. 이는 "목표 영역이 이미지의 대부분을 차지할 때" 대비 창 검색이 실패함을 보여줍니다. π_0 + Cropping의 크롭은 외부 VLM에 의해 생성되며(구현 후속 훈련 없음), 성능이 완전한 AtVLA보다 약간 낮아 크롭 품질이 최종 성능에 상당한 영향을 미친다는 것을 보여줍니다. 부정확한 크롭은 정책 입력을 왜곡하고, 결정 정밀도를 낮추며, 동작 불확실성을 증가시킵니다.

논문은 다중 뷰 융합 전략의 상세한 제거, 다른 로봇 플랫폼 일반화, 훈련 데이터 규모 세부 사항, 추론 지연 시간의 구체적인 밀리초 수치를 언급하지 않습니다. 실제 세계 실험은 Franka Research 3 및 Google Robot 두 가지 구현만 다루며, Google Robot의 구체적인 훈련 데이터 양도 보고하지 않습니다. SimplerEnv WidowX 스위트는 BridgeData 특정 훈련과 구현 적응이 필요하여 시각 개선과 구현 전이를 혼동할 수 있으므로 생략되었습니다. 이는 교차 구현 일반화 결론의 적용 범위가 제한적임을 의미합니다.

## 엔지니어링 시사점

AtVLA를 재현할 때 가장 먼저 확인해야 할 것은 3단계 훈련의 순서와 동결 전략입니다. Stage 0의 레지스터 적응은 이후 모든 것의 기초입니다. 저자들은 ImageNet과 CC3M 데이터를 혼합하면 로봇 시연에서 얻은 능력이 손상된다는 것을 명확히 발견했으므로, 레지스터는 완전히 구현 데이터로 훈련해야 합니다. Stage 0을 건너뛰거나 단축하면 레지스터가 어텐션 아티팩트를 충분히 흡수하지 못해 이후 어텐션 롤아웃 품질이 직접적으로 붕괴될 수 있습니다.

가장 함정에 빠지기 쉬운 곳은 크롭 커리큘럼 설계입니다. Stage 2에서 처음 40% 스텝은 완전히 정답 크롭을 사용해야 하며(α = 0), 40%–90%는 어텐션 롤아웃으로 점진적으로 전환하고, 무효 롤아웃은 정답 크롭으로 폴백하지 않고 정밀화를 건너뜁니다. 모델 자체가 생성한 크롭을 너무 일찍 도입하면 정책이 노이즈 어텐션 신호에 대한 잘못된 의존성을 학습할 수 있습니다. 또 다른 핵심 세부 사항은 무효 롤아웃 판정 규칙(비유한 값, 어텐션 품질 < ε = 10⁻⁶, 창 검색에 유한 후보 점수 없음, 크롭 변 길이 < 56 픽셀)이 훈련과 배포 시 완전히 일치해야 한다는 것입니다. 그렇지 않으면 훈련-테스트 차이가 발생합니다.

하위 팀에게는 먼저 소규모 데이터에서 레지스터 적응이 어텐션 맵 품질을 현저히 개선하는지 확인하는 것이 좋습니다(선형 프로브로 레지스터 특징의 객체 위치 파악 점수가 0.70을 초과하는지 확인). 그 후에 완전한 3단계 훈련에 투자하십시오. 불확실성 임계값 τ는 구현별로 별도로 캘리브레이션해야 합니다. LIBERO 4개 스위트는 동일한 임계값을 공유하지만, Google Robot과 Franka는 독립적으로 캘리브레이션해야 합니다. 초기 값은 검증 불확실성 분포의 70번째 백분위수로 설정하고 목표 트리거율은 약 30%입니다. 계산 비용 측면에서 K = 4 동작 샘플링과 10단계 Euler 솔버가 주요 비용이며, 크롭 정밀화는 총 비용의 약 20–25%를 차지합니다. 하드웨어 리소스가 부족하면 K를 낮추거나 롤아웃 디노이징 스텝 수를 줄이는 것을 고려할 수 있습니다.
