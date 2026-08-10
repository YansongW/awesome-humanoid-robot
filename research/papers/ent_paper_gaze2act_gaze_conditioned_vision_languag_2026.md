---
$id: ent_paper_gaze2act_gaze_conditioned_vision_languag_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
  zh: 'Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
  ko: 'Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
summary:
  en: 'Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions.
    However, in practice, language alone is often insufficient to precisely convey human intent. Institutions per source list:
    NTU MARS Lab.'
  zh: Gaze2Act 是一种基于人类注视的视觉-语言-动作（VLA）框架，由研究团队提出，用于解决机器人交互操作中语言指令意图表达不精确的问题。其核心贡献在于通过跨视角语义匹配将第一人称注视映射到机器人视角，并结合注视点与物体掩码实现粗到细的目标指定，在
    Unitree G1 人形机器人上的 16 项任务中取得了最优意图准确率和任务成功率。
  ko: 'Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions.
    However, in practice, language alone is often insufficient to precisely convey human intent. Institutions per source list:
    NTU MARS Lab.'
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
- gaze2act
- gaze
- conditioned
- vision
- languag
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 278 (merged duplicate list rows: [358]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: jaccard (score 0.636). Abstract and metadata from arXiv API (2605.30282v1); zh content by DeepSeek
    from the abstract. Institutions as given in the source list, not verified. [2026-08-04] body rewritten as full-text six-section
    deep read (.staging/deep_read batch1, DeepSeek deepseek-chat T<=0.3, arXiv HTML full text); en/ko sections regenerated
    by translate pipeline. 深读+数字白名单复核通过 2026-08-10（批量一）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.30282 Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation'
  url: https://arxiv.org/abs/2605.30282
  accessed_at: '2026-07-31'
  date: '2026-05-28'
- id: src_002
  type: website
  title: Project page
  url: https://zuo-kuangji.github.io/Gaze2Act/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---


## 概述

Gaze2Act 是一个将操作者实时注视作为空间意图信号集成到视觉-语言-动作（VLA）策略中的系统，用于解决语言指令在目标消歧、部件级交互和动态意图更新上的不足。该系统基于 GROOT N1.5 骨干，通过跨视角注视接地、感知级注视提示和动作级注视条件化三个模块，在 Unitree G1 人形机器人上实现了 88.8% 的平均意图准确率和 83.5% 的平均任务成功率，显著超越语言条件基线。核心贡献在于证明了注视不仅是静态目标选择器，还能作为实时意图更新信号，在任务执行中动态切换目标。

## 它改变了什么

这个问题真正改变的是 VLA 策略中“意图信号”的定义和传递方式。现有 VLA 模型将语言作为唯一意图通道，但语言在空间精度和时间连续性上存在固有缺陷——超过 20% 的表达是描述性的（隐式指称），边界框和分割掩码继承语言歧义，且无法表达“执行中目标变化”这类动态意图。Gaze2Act 的动机不是增加一种新的空间表示，而是引入一种“直接且持续更新”的意图信号：注视是连续、即时、空间精确的，且认知研究表明眼睛先于手部运动指向目标（eye-leads-hand coordination）。这改变了 VLA 系统的交互范式——从“一次性语言描述”变为“事件触发的实时意图流”，使得目标选择、部件指定和动态切换不再依赖语言的表达能力，而是依赖操作者的自然视觉行为。

## 方法拆解

### 三阶段流程
1. **跨视角注视接地（Cross-View Gaze Grounding）**：将第一人称注视坐标 g_t ∈ ℝ² 映射到机器人视角，产生目标掩码 m_t 和注视点 p_t。
   - 特征提取：DINOv3 ViT-L/16，从五个均匀采样层（{0, 5, 10, 15, 20}）提取特征，L2 归一化后平均得到特征图 φ(·) ∈ ℝ^{H×W×D}。
   - 粗粒度匹配：SAM3 以注视点为点提示分割参考物体得到 M_ref；SAM3 在机器人观测上自动生成候选掩码集 {M_k}；掩码内 patch 特征平均后选余弦相似度最高的掩码作为 m_t。
   - 细粒度匹配：在参考掩码对应 patch 周围提取 (2R+1)×(2R+1) 邻域特征平均，与机器人观测密集特征计算余弦相似度，argmax 限制在 m_t 内得到 p_t。
   - 部署时注视接地由语音触发，选定目标被 SAM3 持续跟踪直到下一次触发，无需持续注视。

2. **感知级注视提示（Perception-Level Gaze Prompting）**：将 (m_t, p_t) 渲染到机器人观测上。
   - 轮廓叠加：沿 m_t 边界绘制彩色轮廓，不同颜色区分多目标任务中的不同目标；语言指令可类别无关（如"pick up the outlined object"）。
   - 注视热图：将 p_t 转换为二维各向同性高斯热图 ℋ_t(x,y) = exp(−((x−p_t^x)²+(y−p_t^y)²)/(2σ²)) · 1[(x,y)∈m_t]，σ 为高斯核尺度超参数；仅在接触前阶段提供细粒度空间指导。
   - 选择规则：细粒度、部件级交互依赖热图提示；粗粒度物体级动作仅用轮廓提示即可。

3. **动作级注视条件化（Action-Level Gaze Conditioning）**：将掩码和注视点编码为紧凑空间 token，直接注入 DiT 动作头。
   - 注视 token 构建：位置通路用二维正弦编码（p_t∈m_t 时在 p_t 处计算，否则在 m_t 中心），得到 z_t^pos ∈ ℝ^{d_p}；物体通路用冻结的 29M 参数 DINOv3 ViT-S+/16 编码 m_t 边界框裁剪（resized 到 224×224）的 CLS 特征 z_t^obj ∈ ℝ^{d_v}；两者拼接后经线性层 W_fuse 投影得到注视 token c_t^gaze = W_fuse[z_t^pos; z_t^obj] + b_fuse。
   - 解耦交叉注意力：每个 DiT 块中新增独立交叉注意力路径，与原始视觉-语言路径并行；共享相同 Query Q = W_Q h，但 Key/Value 来自不同源（原始路径用预训练权重投影 VLM token，新路径用新增权重投影注视 token）；输出相加：h_xattn = h + Attn(Q,K,V) + Attn(Q,K^gaze,V^gaze)。
   - 稳定化注视注入：注视交叉注意力分支的输出投影零初始化，其他投影标准初始化；新增分支初始为 no-op，影响从操作目标逐步学习；仅增加 4.95% 参数。

### 训练与推理差异
- 训练时视觉提示和注视 token 由离线地面真值掩码和注视点生成；推理时由 Meta Aria 眼镜注视在线生成。
- 眼动追踪硬件仅用于交互式部署，不用于收集训练演示。

## 关键创新

1. **事件触发的注视交互协议**：注视接地由语音关键词触发，选定目标由 SAM3 持续跟踪直到下一次触发。这避免了每帧运行注视选择的计算开销，同时实现了动态意图转向——在长时程任务中切换目标。这是对“注视作为持续信号”的工程化折中，既保留了注视的实时性，又避免了噪声累积。

2. **解耦交叉注意力注入机制**：在 DiT 动作头中新增独立交叉注意力路径，与原始视觉-语言路径并行，共享 Query 但使用不同的 Key/Value。输出投影零初始化使新增分支初始为 no-op，从操作目标逐步学习。这种设计避免了随机初始化导致的训练不稳定（消融中随机初始化使 Pick Bread Place Bowl 从 40 降至 24），且仅增加 4.95% 参数。

3. **感知级与动作级双路径提示**：视觉提示（轮廓+热图）提供直观的空间引导，动作级注视 token 提供精确的条件化信号。消融显示两者互补——Hammer 任务中视觉提示更强（15→28），Pick Bread Place Bowl 中动作级条件化更有效（40 vs 34）。这种双路径设计允许不同任务类型自适应选择信息通路。

## 实验与结果

### 主要结果（表1，每任务 50 次试验，Int. = Intent Accuracy, Suc. = Task Success）

| 任务类别 | Vanilla GROOT (Int./Suc.) | RoboGround (Int./Suc.) | ControlVLA (Int./Suc.) | Gaze2Act (Int./Suc.) |
|---------|--------------------------|------------------------|------------------------|----------------------|
| Ambiguous Obj. Cup | 44/44 | 96/94 | 82/62 | 92/92 |
| Ambiguous Obj. Bread | 28/18 | 36/32 | 40/32 | 98/96 |
| Ambiguous Obj. Fruits | 30/20 | 66/56 | 80/44 | 100/94 |
| Unseen Obj. Cup | 44/36 | 84/74 | 76/62 | 90/88 |
| Unseen Obj. Bread | 38/16 | 44/28 | 82/54 | 96/86 |
| Unseen Obj. Fruits | 48/26 | 76/40 | 90/54 | 94/86 |
| Transparent Obj. Cup | 30/24 | 56/32 | 64/42 | 88/86 |
| Transparent Obj. Bottle | 20/14 | 32/24 | 40/28 | 88/84 |
| Compositional Pick bread place bowl | 30/26 | 38/34 | 42/34 | 96/94 |
| Compositional Pick paper ball place bin | 24/18 | 78/32 | 84/52 | 88/84 |
| Subpart Grasp Hammer (handle) | –/24 | –/26 | –/28 | 80/62 |
| Subpart Grasp Hammer (head) | –/18 | –/22 | –/24 | 76/64 |
| Subpart Grasp Hammer (neck) | –/22 | –/26 | –/24 | 70/68 |
| Part-cond. Act. Cup (handover) | –/22 | –/38 | –/42 | 90/88 |
| Part-cond. Act. Cup (pour) | –/20 | –/36 | –/40 | 86/80 |
| **Object-level Avg.** | 33.6/24.2 | 60.6/44.6 | 68.0/46.4 | **93.0/89.0** |
| **Part-level Avg.** | –/21.2 | –/29.6 | –/31.6 | **80.4/72.4** |
| **Overall Avg.** | 33.6/23.2 | 60.6/39.6 | 68.0/41.5 | **88.8/83.5** |

### 关键发现
- **Dynamic Intent Steering**：长时程目标切换设置中，RoboGround 4/30 成功，ControlVLA 5/30 成功，Gaze2Act 14/30 成功（所有方法均低于一半成功率，说明动态意图转向仍是开放挑战）。
- **消融实验**（表2，每任务 60 次试验，Hammer 每部件 20 次试验）：

| 配置 | Pick Bread Place Bowl | Hammer (handle/head/neck) |
|------|----------------------|---------------------------|
| Baseline | 17/60 | 15/60 |
| Gaze prompting only | 34/60 | 28/60 |
| Gaze conditioning only (random init) | 24/60 | 17/60 |
| Gaze conditioning only (zero init) | 40/60 | 19/60 |
| Gaze2Act (full) | 55/60 | 39/60 |

- 消融显示：Hammer 中视觉提示是更强的单一路径（15→28），动作级条件化单独仅达 19（零初始化）；Pick Bread Place Bowl 中动作级条件化更有效（40 vs 34）；随机初始化使 Pick Bread Place Bowl 从 40 降至 24，验证零初始化的重要性。

## 边界与局限

- 框架依赖可靠的注视估计和跨视角接地，在严重遮挡、快速头部运动或人与机器人视角差异大时可能不稳定。
- 当前系统假设注视反映用户预期操作目标，但实际中人类注视可能偶尔漂移或表现出与期望动作无关的探索行为。
- Dynamic Intent Steering 中所有方法成功率均低于 50%（Gaze2Act 14/30），说明动态目标切换仍是未完全解决的问题。
- 论文未提及多用户/多操作员场景、非英语语言指令、长时间连续操作中的注视疲劳问题、与其他意图模态（如语音、手势）的融合实验。

## 工程启示

- **复现时先核对注视接地模块**：跨视角接地是系统瓶颈，DINOv3 特征层选择（{0, 5, 10, 15, 20}）和 SAM3 掩码生成质量直接影响后续所有模块。建议先单独评估接地精度，再接入策略训练。
- **零初始化是动作级条件化的关键**：消融显示随机初始化导致 Pick Bread Place Bowl 从 40 降至 24，必须严格遵循输出投影零初始化的设计，否则新增分支会破坏预训练 DiT 的稳定性。
- **视觉提示与动作级条件化互补**：不同任务对两条信息通路的依赖不同（Hammer 依赖视觉提示，Pick Bread Place Bowl 依赖动作级条件化），复现时不要省略任一通路，且需根据任务类型调整热图渲染规则（仅当 p_t ∈ m_t 时渲染）。
- **训练数据收集不需要眼动追踪硬件**：注视点和掩码在演示视频上离线标注，这大幅降低了数据收集门槛；但推理时需 Meta Aria 眼镜和在线接地流程，部署成本集中在硬件端。
- **基线比较需注意语言描述协议**：语言条件基线使用最具体的无歧义描述（如"handover the red patterned cup with white lid"），而 Gaze2Act 使用类别级通用模板（如"handover the outlined object"），这种不对称设计是公平比较的关键，复现时需严格遵循。

## 参考
- https://arxiv.org/abs/2605.30282
- https://zuo-kuangji.github.io/Gaze2Act/
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## Overview

Gaze2Act is a system that integrates the operator's real-time gaze as a spatial intent signal into Vision-Language-Action (VLA) policies, addressing the limitations of language instructions in target disambiguation, part-level interaction, and dynamic intent updates. Built on the GROOT N1.5 backbone, the system achieves 88.8% average intent accuracy and 83.5% average task success on the Unitree G1 humanoid robot through three modules—cross-view gaze grounding, perception-level gaze prompting, and action-level gaze conditioning—significantly surpassing language-conditioned baselines. The core contribution lies in demonstrating that gaze is not merely a static target selector but can serve as a real-time intent update signal, dynamically switching targets during task execution.

## What It Changes

What this work truly changes is the definition and transmission of "intent signals" in VLA policies. Existing VLA models treat language as the sole intent channel, but language has inherent deficiencies in spatial precision and temporal continuity—over 20% of expressions are descriptive (implicit references), bounding boxes and segmentation masks inherit language ambiguity, and dynamic intents such as "target changes during execution" cannot be expressed. The motivation of Gaze2Act is not to add a new spatial representation but to introduce a "direct and continuously updated" intent signal: gaze is continuous, instantaneous, spatially precise, and cognitive research shows that eyes lead hand movements toward targets (eye-leads-hand coordination). This changes the interaction paradigm of VLA systems—from "one-shot language descriptions" to "event-triggered real-time intent streams"—making target selection, part specification, and dynamic switching no longer dependent on language expressiveness but on the operator's natural visual behavior.

## Method Breakdown

### Three-Stage Pipeline
1. **Cross-View Gaze Grounding**: Maps first-person gaze coordinates g_t ∈ ℝ² to the robot's viewpoint, producing target mask m_t and gaze point p_t.
   - Feature extraction: DINOv3 ViT-L/16, extracting features from five uniformly sampled layers ({0, 5, 10, 15, 20}), L2-normalized and averaged to obtain feature maps φ(·) ∈ ℝ^{H×W×D}.
   - Coarse-grained matching: SAM3 segments the reference object using the gaze point as a point prompt to obtain M_ref; SAM3 automatically generates a candidate mask set {M_k} on the robot's observation; patch features within masks are averaged, and the mask with the highest cosine similarity is selected as m_t.
   - Fine-grained matching: A (2R+1)×(2R+1) neighborhood around the corresponding patch in the reference mask is extracted and averaged, cosine similarity is computed against dense features from the robot's observation, and argmax constrained within m_t yields p_t.
   - At deployment, gaze grounding is triggered by voice, and the selected target is continuously tracked by SAM3 until the next trigger, requiring no sustained gaze.

2. **Perception-Level Gaze Prompting**: Renders (m_t, p_t) onto the robot's observation.
   - Contour overlay: A colored contour is drawn along the boundary of m_t, with different colors distinguishing different targets in multi-object tasks; language instructions can be category-agnostic (e.g., "pick up the outlined object").
   - Gaze heatmap: p_t is converted into a 2D isotropic Gaussian heatmap ℋ_t(x,y) = exp(−((x−p_t^x)²+(y−p_t^y)²)/(2σ²)) · 1[(x,y)∈m_t], where σ is the Gaussian kernel scale hyperparameter; provided only during the pre-contact phase for fine-grained spatial guidance.
   - Selection rule: Fine-grained, part-level interactions rely on heatmap prompting; coarse-grained object-level actions require only contour prompting.

3. **Action-Level Gaze Conditioning**: Encodes mask and gaze point into compact spatial tokens, directly injected into the DiT action head.
   - Gaze token construction: The position pathway uses 2D sinusoidal encoding (computed at p_t when p_t∈m_t, otherwise at the center of m_t), yielding z_t^pos ∈ ℝ^{d_p}; the object pathway uses a frozen 29M-parameter DINOv3 ViT-S+/16 to encode the bounding-box crop of m_t (resized to 224×224) and extracts the CLS feature z_t^obj ∈ ℝ^{d_v}; both are concatenated and projected via a linear layer W_fuse to obtain the gaze token c_t^gaze = W_fuse[z_t^pos; z_t^obj] + b_fuse.
   - Decoupled cross-attention: Each DiT block adds an independent cross-attention path, running in parallel with the original vision-language path; sharing the same Query Q = W_Q h, but Key/Value come from different sources (the original path uses pretrained weights to project VLM tokens, the new path uses newly added weights to project gaze tokens); outputs are summed: h_xattn = h + Attn(Q,K,V) + Attn(Q,K^gaze,V^gaze).
   - Stabilized gaze injection: The output projection of the gaze cross-attention branch is zero-initialized, while other projections use standard initialization; the new branch is initially a no-op and gradually learns from manipulation objectives; parameter increase is only 4.95%.

### Training vs. Inference Differences
- During training, visual prompts and gaze tokens are generated from offline ground-truth masks and gaze points; during inference, they are generated online from Meta Aria glasses gaze.
- Eye-tracking hardware is used only for interactive deployment, not for collecting training demonstrations.

## Key Innovations

1. **Event-Triggered Gaze Interaction Protocol**: Gaze grounding is triggered by voice keywords, and the selected target is continuously tracked by SAM3 until the next trigger. This avoids the computational overhead of per-frame gaze selection while enabling dynamic intent switching—switching targets in long-horizon tasks. This is an engineering compromise for "gaze as a continuous signal," preserving gaze real-time capability while avoiding noise accumulation.

2. **Decoupled Cross-Attention Injection Mechanism**: An independent cross-attention path is added in the DiT action head, running in parallel with the original vision-language path, sharing the Query but using different Key/Value. Zero-initialized output projections make the new branch initially a no-op, gradually learning from manipulation objectives. This design avoids training instability caused by random initialization (in ablation, random initialization dropped Pick Bread Place Bowl from 40 to 24) and adds only 4.95% parameters.

3. **Dual-Path Prompting at Perception and Action Levels**: Visual prompts (contour + heatmap) provide intuitive spatial guidance, while action-level gaze tokens provide precise conditioning signals. Ablations show they are complementary—in the Hammer task, visual prompts are stronger (15→28), while in Pick Bread Place Bowl, action-level conditioning is more effective (40 vs 34). This dual-path design allows different task types to adaptively select the information pathway.

## Experiments and Results

### Main Results (Table 1, 50 trials per task, Int. = Intent Accuracy, Suc. = Task Success)

| Task Category | Vanilla GROOT (Int./Suc.) | RoboGround (Int./Suc.) | ControlVLA (Int./Suc.) | Gaze2Act (Int./Suc.) |
|---------|--------------------------|------------------------|------------------------|----------------------|
| Ambiguous Obj. Cup | 44/44 | 96/94 | 82/62 | 92/92 |
| Ambiguous Obj. Bread | 28/18 | 36/32 | 40/32 | 98/96 |
| Ambiguous Obj. Fruits | 30/20 | 66/56 | 80/44 | 100/94 |
| Unseen Obj. Cup | 44/36 | 84/74 | 76/62 | 90/88 |
| Unseen Obj. Bread | 38/16 | 44/28 | 82/54 | 96/86 |
| Unseen Obj. Fruits | 48/26 | 76/40 | 90/54 | 94/86 |
| Transparent Obj. Cup | 30/24 | 56/32 | 64/42 | 88/86 |
| Transparent Obj. Bottle | 20/14 | 32/24 | 40/28 | 88/84 |
| Compositional Pick bread place bowl | 30/26 | 38/34 | 42/34 | 96/94 |
| Compositional Pick paper ball place bin | 24/18 | 78/32 | 84/52 | 88/84 |
| Subpart Grasp Hammer (handle) | –/24 | –/26 | –/28 | 80/62 |
| Subpart Grasp Hammer (head) | –/18 | –/22 | –/24 | 76/64 |
| Subpart Grasp Hammer (neck) | –/22 | –/26 | –/24 | 70/68 |
| Part-cond. Act. Cup (handover) | –/22 | –/38 | –/42 | 90/88 |
| Part-cond. Act. Cup (pour) | –/20 | –/36 | –/40 | 86/80 |
| **Object-level Avg.** | 33.6/24.2 | 60.6/44.6 | 68.0/46.4 | **93.0/89.0** |
| **Part-level Avg.** | –/21.2 | –/29.6 | –/31.6 | **80.4/72.4** |
| **Overall Avg.** | 33.6/23.2 | 60.6/39.6 | 68.0/41.5 | **88.8/83.5** |

### Key Findings
- **Dynamic Intent Steering**: In the long-horizon target-switching setting, RoboGround succeeded in 4/30 trials, ControlVLA in 5/30, and Gaze2Act in 14/30 (all methods below 50% success, indicating dynamic intent steering remains an open challenge).
- **Ablation Study** (Table 2, 60 trials per task, 20 trials per Hammer subpart):

| Configuration | Pick Bread Place Bowl | Hammer (handle/head/neck) |
|------|----------------------|---------------------------|
| Baseline | 17/60 | 15/60 |
| Gaze prompting only | 34/60 | 28/60 |
| Gaze conditioning only (random init) | 24/60 | 17/60 |
| Gaze conditioning only (zero init) | 40/60 | 19/60 |
| Gaze2Act (full) | 55/60 | 39/60 |

- Ablations show: In Hammer, visual prompting is the stronger single pathway (15→28), while action-level conditioning alone reaches only 19 (zero init); in Pick Bread Place Bowl, action-level conditioning is more effective (40 vs 34); random initialization drops Pick Bread Place Bowl from 40 to 24, validating the importance of zero initialization.

## Boundaries and Limitations

- The framework relies on reliable gaze estimation and cross-view grounding, which may become unstable under severe occlusion, rapid head motion, or large differences between human and robot viewpoints.
- The current system assumes gaze reflects the user's intended manipulation target, but in practice, human gaze may occasionally drift or exhibit exploratory behavior unrelated to the desired action.
- In Dynamic Intent Steering, all methods achieve success rates below 50% (Gaze2Act 14/30), indicating dynamic target switching remains an incompletely solved problem.
- The paper does not address multi-user/multi-operator scenarios, non-English language instructions, gaze fatigue during prolonged continuous operation, or experiments fusing other intent modalities (e.g., speech, gestures).

## Engineering Insights

- **Verify the gaze grounding module first when reproducing**: Cross-view grounding is the system bottleneck; DINOv3 feature layer selection ({0, 5, 10, 15, 20}) and SAM3 mask generation quality directly affect all downstream modules. It is recommended to evaluate grounding accuracy independently before integrating policy training.
- **Zero initialization is critical for action-level conditioning**: Ablations show random initialization drops Pick Bread Place Bowl from 40 to 24; the zero-initialized output projection design must be strictly followed, otherwise the new branch will disrupt the stability of the pretrained DiT.
- **Visual prompting and action-level conditioning are complementary**: Different tasks rely differently on the two information pathways (Hammer relies on visual prompting, Pick Bread Place Bowl on action-level conditioning); do not omit either pathway during reproduction, and adjust heatmap rendering rules according to task type (render only when p_t ∈ m_t).
- **Training data collection does not require eye-tracking hardware**: Gaze points and masks are annotated offline on demonstration videos, significantly lowering the data collection barrier; however, inference requires Meta Aria glasses and an online grounding pipeline, concentrating deployment costs on the hardware side.
- **Baseline comparisons must follow the language description protocol**: Language-conditioned baselines use the most specific unambiguous descriptions (e.g., "handover the red patterned cup with white lid"), while Gaze2Act uses category-level generic templates (e.g., "handover the outlined object"); this asymmetry is key to fair comparison and must be strictly followed during reproduction.

## 개요

Gaze2Act는 작업자의 실시간 시선을 공간적 의도 신호로 통합하여 비전-언어-행동(VLA) 정책에 적용하는 시스템으로, 언어 명령이 갖는 목표 식별, 부품 수준 상호작용, 동적 의도 업데이트의 한계를 해결합니다. 이 시스템은 GROOT N1.5 백본을 기반으로, 교차 시점 시선 접지, 인식 수준 시선 프롬프팅, 행동 수준 시선 조건화의 세 가지 모듈을 통해 Unitree G1 휴머노이드 로봇에서 평균 의도 정확도 88.8%, 평균 작업 성공률 83.5%를 달성하여 언어 조건 기준선을 크게 능가합니다. 핵심 기여는 시선이 단순한 정적 목표 선택기가 아니라 실시간 의도 업데이트 신호로 작동하여 작업 실행 중 목표를 동적으로 전환할 수 있음을 입증한 것입니다.

## 무엇을 바꾸는가

이 문제가 실제로 바꾸는 것은 VLA 정책에서 '의도 신호'의 정의와 전달 방식입니다. 기존 VLA 모델은 언어를 유일한 의도 채널로 사용하지만, 언어는 공간 정밀도와 시간 연속성에서 본질적인 한계를 가집니다—표현의 20% 이상이 서술적(암시적 지시)이며, 경계 상자와 분할 마스크는 언어의 모호성을 상속받고, '실행 중 목표 변경'과 같은 동적 의도를 표현할 수 없습니다. Gaze2Act의 동기는 새로운 공간 표현을 추가하는 것이 아니라 '직접적이고 지속적으로 업데이트되는' 의도 신호를 도입하는 것입니다: 시선은 연속적이고, 즉각적이며, 공간적으로 정밀하며, 인지 연구에 따르면 눈은 손의 움직임보다 먼저 목표를 가리킵니다(eye-leads-hand coordination). 이는 VLA 시스템의 상호작용 패러다임을 '일회성 언어 설명'에서 '이벤트 트리거 실시간 의도 흐름'으로 변화시켜, 목표 선택, 부품 지정, 동적 전환이 더 이상 언어의 표현 능력에 의존하지 않고 작업자의 자연스러운 시각적 행동에 의존하게 됩니다.

## 방법 분해

### 3단계 프로세스
1. **교차 시점 시선 접지(Cross-View Gaze Grounding)**: 1인칭 시선 좌표 g_t ∈ ℝ²를 로봇 시점으로 매핑하여 목표 마스크 m_t와 시선 지점 p_t를 생성합니다.
   - 특징 추출: DINOv3 ViT-L/16, 5개의 균일 샘플링 레이어({0, 5, 10, 15, 20})에서 특징을 추출하고, L2 정규화 후 평균하여 특징 맵 φ(·) ∈ ℝ^{H×W×D}를 얻습니다.
   - 거친 정합: SAM3가 시선 지점을 포인트 프롬프트로 사용하여 참조 객체를 분할하여 M_ref를 얻습니다; SAM3가 로봇 관측에서 후보 마스크 집합 {M_k}를 자동 생성합니다; 마스크 내 패치 특징을 평균한 후 코사인 유사도가 가장 높은 마스크를 m_t로 선택합니다.
   - 세밀한 정합: 참조 마스크의 해당 패치 주변에서 (2R+1)×(2R+1) 이웃 특징을 추출하여 평균하고, 로봇 관측의 밀집 특징과 코사인 유사도를 계산하며, argmax를 m_t 내로 제한하여 p_t를 얻습니다.
   - 배포 시 시선 접지는 음성으로 트리거되며, 선택된 목표는 다음 트리거까지 SAM3에 의해 지속적으로 추적되므로 지속적인 시선이 필요하지 않습니다.

2. **인식 수준 시선 프롬프팅(Perception-Level Gaze Prompting)**: (m_t, p_t)를 로봇 관측에 렌더링합니다.
   - 윤곽 오버레이: m_t 경계를 따라 색상 윤곽을 그리며, 다중 목표 작업에서 서로 다른 색상으로 서로 다른 목표를 구분합니다; 언어 명령은 범주와 무관할 수 있습니다(예: "outlined object를 집어 올리세요").
   - 시선 히트맵: p_t를 2차원 등방성 가우시안 히트맵 ℋ_t(x,y) = exp(−((x−p_t^x)²+(y−p_t^y)²)/(2σ²)) · 1[(x,y)∈m_t]로 변환하며, σ는 가우시안 커널 스케일 하이퍼파라미터입니다; 접촉 전 단계에서만 세밀한 공간 지침을 제공합니다.
   - 선택 규칙: 세밀한 부품 수준 상호작용은 히트맵 프롬프트에 의존합니다; 대략적인 객체 수준 동작은 윤곽 프롬프트만으로 충분합니다.

3. **행동 수준 시선 조건화(Action-Level Gaze Conditioning)**: 마스크와 시선 지점을 컴팩트한 공간 토큰으로 인코딩하여 DiT 행동 헤드에 직접 주입합니다.
   - 시선 토큰 구성: 위치 경로는 2차원 사인 인코딩을 사용하며(p_t∈m_t일 때 p_t에서 계산, 그렇지 않으면 m_t 중심에서 계산), z_t^pos ∈ ℝ^{d_p}를 얻습니다; 객체 경로는 동결된 29M 파라미터 DINOv3 ViT-S+/16을 사용하여 m_t 경계 상자 크롭(224×224로 리사이즈)의 CLS 특징 z_t^obj ∈ ℝ^{d_v}를 인코딩합니다; 둘을 연결한 후 선형 레이어 W_fuse로 프로젝션하여 시선 토큰 c_t^gaze = W_fuse[z_t^pos; z_t^obj] + b_fuse를 얻습니다.
   - 분리 교차 주의: 각 DiT 블록에 독립적인 교차 주의 경로를 추가하여 원래 비전-언어 경로와 병렬로 실행합니다; 동일한 Query Q = W_Q h를 공유하지만 Key/Value는 서로 다른 소스에서 옵니다(원래 경로는 사전 훈련 가중치로 VLM 토큰을 프로젝션하고, 새 경로는 새 가중치로 시선 토큰을 프로젝션합니다); 출력은 더해집니다: h_xattn = h + Attn(Q,K,V) + Attn(Q,K^gaze,V^gaze).
   - 안정화된 시선 주입: 시선 교차 주의 분기의 출력 프로젝션은 제로 초기화되고, 다른 프로젝션은 표준 초기화됩니다; 새 분기는 초기에는 no-op이며, 조작 목표에서 점진적으로 학습합니다; 파라미터는 4.95%만 증가합니다.

### 훈련 및 추론 차이
- 훈련 시 시각 프롬프트와 시선 토큰은 오프라인 지상 진실 마스크와 시선 지점에서 생성됩니다; 추론 시 Meta Aria 안경 시선에서 온라인으로 생성됩니다.
- 안구 추적 하드웨어는 대화형 배포에만 사용되며 훈련 데모 수집에는 사용되지 않습니다.

## 핵심 혁신

1. **이벤트 트리거 시선 상호작용 프로토콜**: 시선 접지는 음성 키워드로 트리거되고, 선택된 목표는 다음 트리거까지 SAM3에 의해 지속적으로 추적됩니다. 이는 매 프레임 시선 선택을 실행하는 계산 오버헤드를 피하면서 동적 의도 전환—장기 작업에서 목표 전환—을 가능하게 합니다. 이는 '시선을 지속 신호로 사용'하는 것에 대한 공학적 절충으로, 시선의 실시간성을 유지하면서 노이즈 누적을 피합니다.

2. **분리 교차 주의 주입 메커니즘**: DiT 행동 헤드에 독립적인 교차 주의 경로를 추가하여 원래 비전-언어 경로와 병렬로 실행하고, Query를 공유하지만 서로 다른 Key/Value를 사용합니다. 출력 프로젝션 제로 초기화로 새 분기는 초기에는 no-op이며, 조작 목표에서 점진적으로 학습합니다. 이 설계는 무작위 초기화로 인한 훈련 불안정을 피하며(절제에서 무작위 초기화는 Pick Bread Place Bowl을 40에서 24로 감소), 파라미터는 4.95%만 증가합니다.

3. **인식 수준과 행동 수준 이중 경로 프롬프팅**: 시각 프롬프트(윤곽+히트맵)는 직관적인 공간 지침을 제공하고, 행동 수준 시선 토큰은 정밀한 조건화 신호를 제공합니다. 절제는 둘이 상호 보완적임을 보여줍니다—Hammer 작업에서는 시각 프롬프트가 더 강하고(15→28), Pick Bread Place Bowl에서는 행동 수준 조건화가 더 효과적입니다(40 vs 34). 이 이중 경로 설계는 서로 다른 작업 유형이 정보 경로를 적응적으로 선택할 수 있게 합니다.

## 실험 및 결과

### 주요 결과(표1, 작업당 50회 시도, Int. = 의도 정확도, Suc. = 작업 성공률)

| 작업 범주 | Vanilla GROOT (Int./Suc.) | RoboGround (Int./Suc.) | ControlVLA (Int./Suc.) | Gaze2Act (Int./Suc.) |
|---------|--------------------------|------------------------|------------------------|----------------------|
| 모호한 객체 컵 | 44/44 | 96/94 | 82/62 | 92/92 |
| 모호한 객체 빵 | 28/18 | 36/32 | 40/32 | 98/96 |
| 모호한 객체 과일 | 30/20 | 66/56 | 80/44 | 100/94 |
| 미지의 객체 컵 | 44/36 | 84/74 | 76/62 | 90/88 |
| 미지의 객체 빵 | 38/16 | 44/28 | 82/54 | 96/86 |
| 미지의 객체 과일 | 48/26 | 76/40 | 90/54 | 94/86 |
| 투명 객체 컵 | 30/24 | 56/32 | 64/42 | 88/86 |
| 투명 객체 병 | 20/14 | 32/24 | 40/28 | 88/84 |
| 구성적 빵 집기 그릇에 놓기 | 30/26 | 38/34 | 42/34 | 96/94 |
| 구성적 종이공 집기 쓰레기통에 놓기 | 24/18 | 78/32 | 84/52 | 88/84 |
| 하위 부품 망치 잡기(손잡이) | –/24 | –/26 | –/28 | 80/62 |
| 하위 부품 망치 잡기(머리) | –/18 | –/22 | –/24 | 76/64 |
| 하위 부품 망치 잡기(목) | –/22 | –/26 | –/24 | 70/68 |
| 부품 조건 동작 컵(건네기) | –/22 | –/38 | –/42 | 90/88 |
| 부품 조건 동작 컵(따르기) | –/20 | –/36 | –/40 | 86/80 |
| **객체 수준 평균** | 33.6/24.2 | 60.6/44.6 | 68.0/46.4 | **93.0/89.0** |
| **부품 수준 평균** | –/21.2 | –/29.6 | –/31.6 | **80.4/72.4** |
| **전체 평균** | 33.6/23.2 | 60.6/39.6 | 68.0/41.5 | **88.8/83.5** |

### 핵심 발견
- **동적 의도 전환(Dynamic Intent Steering)**: 장기 목표 전환 설정에서 RoboGround 4/30 성공, ControlVLA 5/30 성공, Gaze2Act 14/30 성공(모든 방법이 성공률 절반 미만으로, 동적 의도 전환은 여전히 열린 과제임을 시사).
- **절제 실험**(표2, 작업당 60회 시도, Hammer는 부품당 20회 시도):

| 구성 | Pick Bread Place Bowl | Hammer (손잡이/머리/목) |
|------|----------------------|---------------------------|
| 기준선 | 17/60 | 15/60 |
| 시선 프롬프팅만 | 34/60 | 28/60 |
| 시선 조건화만(무작위 초기화) | 24/60 | 17/60 |
| 시선 조건화만(제로 초기화) | 40/60 | 19/60 |
| Gaze2Act(전체) | 55/60 | 39/60 |

- 절제는 다음을 보여줍니다: Hammer에서 시각 프롬프트가 더 강한 단일 경로이며(15→28), 행동 수준 조건화 단독은 19(제로 초기화)에 불과합니다; Pick Bread Place Bowl에서는 행동 수준 조건화가 더 효과적입니다(40 vs 34); 무작위 초기화는 Pick Bread Place Bowl을 40에서 24로 감소시켜 제로 초기화의 중요성을 검증합니다.

## 경계 및 한계

- 프레임워크는 신뢰할 수 있는 시선 추정과 교차 시점 접지에 의존하며, 심한 가림, 빠른 머리 움직임 또는 사람과 로봇 시점 간 큰 차이가 있을 때 불안정할 수 있습니다.
- 현재 시스템은 시선이 사용자의 의도된 조작 목표를 반영한다고 가정하지만, 실제로 인간의 시선은 때때로 표류하거나 의도된 동작과 무관한 탐색 행동을 보일 수 있습니다.
- 동적 의도 전환에서 모든 방법의 성공률이 50% 미만(Gaze2Act 14/30)으로, 동적 목표 전환은 완전히 해결되지 않은 문제입니다.
- 논문은 다중 사용자/다중 운영자 시나리오, 비영어 언어 명령, 장시간 연속 조작 중 시선 피로 문제, 다른 의도 양식(음성, 제스처 등)과의 융합 실험을 언급하지 않습니다.

## 공학적 시사점

- **재현 시 시선 접지 모듈을 먼저 검증하세요**: 교차 시점 접지는 시스템의 병목이며, DINOv3 특징 레이어 선택({0, 5, 10, 15, 20})과 SAM3 마스크 생성 품질은 이후 모든 모듈에 직접적인 영향을 미칩니다. 접지 정확도를 먼저 단독 평가한 후 정책 훈련에 연결하는 것이 좋습니다.
- **제로 초기화는 행동 수준 조건화의 핵심입니다**: 절제는 무작위 초기화가 Pick Bread Place Bowl을 40에서 24로 감소시킴을 보여주며, 출력 프로젝션 제로 초기화 설계를 엄격히 따라야 합니다. 그렇지 않으면 새 분기가 사전 훈련된 DiT의 안정성을 손상시킵니다.
- **시각 프롬프트와 행동 수준 조건화는 상호 보완적입니다**: 서로 다른 작업이 두 정보 경로에 의존하는 정도가 다릅니다(Hammer는 시각 프롬프트에 의존, Pick Bread Place Bowl은 행동 수준 조건화에 의존). 재현 시 어느 경로도 생략하지 말고, 작업 유형에 따라 히트맵 렌더링 규칙을 조정해야 합니다(p_t ∈ m_t일 때만 렌더링).
- **훈련 데이터 수집에는 안구 추적 하드웨어가 필요하지 않습니다**: 시선 지점과 마스크는 데모 비디오에서 오프라인으로 주석 처리되므로 데이터 수집 장벽이 크게 낮아집니다; 그러나 추론 시 Meta Aria 안경과 온라인 접지 프로세스가 필요하므로 배포 비용은 하드웨어 측에 집중됩니다.
- **기준선 비교 시 언어 설명 프로토콜에 주의하세요**: 언어 조건 기준선은 가장 구체적인 무모호 설명(예: "흰 뚜껑이 있는 빨간 패턴 컵을 건네주세요")을 사용하는 반면, Gaze2Act는 범주 수준의 일반 템플릿(예: "outlined object를 건네주세요")을 사용합니다. 이러한 비대칭 설계는 공정한 비교의 핵심이며, 재현 시 엄격히 따라야 합니다.
