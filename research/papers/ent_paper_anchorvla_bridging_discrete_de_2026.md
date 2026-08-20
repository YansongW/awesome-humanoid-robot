---
$id: ent_paper_anchorvla_bridging_discrete_de_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
  zh: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
  ko: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
summary:
  en: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
  zh: AnchorVLA 是一个由研究者提出的分层决策锚定视觉-语言-动作规划框架，旨在解决现有 VLA 规划器在连续轨迹生成中语义-动作对齐困难与推理效率低下的问题。其核心贡献在于引入轨迹模式锚点作为高层推理与连续执行之间的显式接口，并在
    Bench2Drive 闭环基准上取得了 77.28 的成功率与 89.92 的驾驶分数。
  ko: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
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
- robotics
- anchorvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03182v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (895 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning (arXiv)'
  url: https://arxiv.org/abs/2607.03182
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述

AnchorVLA由研究者提出，旨在弥合高层语言推理与低层连续轨迹执行间的“抽象鸿沟”。其核心创新是将动作表示从低层坐标token提升为高层轨迹模式锚点（trajectory-pattern anchors），通过k-means构建含100个锚点的码本，将轨迹分解为离散锚点决策与连续残差两部分。框架包含两个关键模块：Decision-as-Anchor Representation（DAAR）支持查询式和自回归两种锚点决策建模，Decision-Anchored Residual Flow（DARF）则在锚点定义的残差空间中用流匹配生成连续轨迹。在Bench2Drive闭环基准上，AnchorVLA取得DS 89.92、SR 77.28的成绩，显著优于SimLingo（DS 85.07, SR 67.27）等基线，且自回归锚点决策仅增加64ms延迟。消融实验证实锚点决策与残差流设计均有效，但作者承认Comfort分数（28.94）低于部分基线，且未实现反射机制来纠正潜在错误锚点预测。

## 它改变了什么

AnchorVLA 真正改变的，是 VLA 规划器对“动作”这一基本语义单元的定义方式。长期以来，VLA 领域存在一条隐形的断层线：基于规划头的方法把连续轨迹当作回归问题，语言推理与几何输出之间缺乏结构化的中间表征，导致高层决策（“我要让行”）与低层执行（“方向盘转 3 度”）在梯度流中几乎解耦；而自回归方法把轨迹压成坐标级 token，虽然形式上统一了模态，却把语义信息稀释在数百个几何点里，序列越长，离散化误差越积越深，推理延迟也随序列长度线性恶化。AnchorVLA 的切入点不是换一个更大的 VLM 或更快的解码器，而是重新发明了动作的“粒度”——它把轨迹分解为“行为级锚点 + 残差”，让离散决策与连续执行在表征层面就完成对齐，而非在损失函数里强行拉近。

这个改变的实质，是把“决策”从隐空间中的隐变量提升为显式的、可监督的、可解释的轨迹模式锚点。码本中的每个锚点（如车道保持、制动、让行）不再是抽象的高层意图，而是轨迹空间中的聚类中心，天然携带几何信息。于是，语言推理与轨迹生成之间第一次有了一个“中间层”：VLM 先选锚点（离散决策），再在锚点定义的残差空间里做流匹配（连续细化）。这个两阶段分解在数学上等价于把全局轨迹分布 \(p(\tau|x)\) 因式分解为 \(p(a_k|x) \cdot p(r_k|x,a_k)\)，但工程意义远大于形式——残差目标的分布比完整轨迹紧凑得多，流匹配的传输路径被大幅缩短，因此仅用 2 步欧拉积分就能逼近高质量轨迹，而无需像 DiffusionDrive 那样在完整轨迹空间里做多步去噪。表 3 中 Query Based 变体（DS 88.67）与 None 变体（DS 87.49）的对比也印证了这一点：即使去掉自回归 token，仅靠锚点决策 + 残差流，性能已显著超越无锚点的纯流匹配基线。

更值得注意的，是 AnchorVLA 对“决策”本身的可控性。自回归变体在 LLM 词汇表中引入锚点 token，意味着驾驶行为可以被语言模型“说出来”——这不仅是表征上的统一，更打开了推理时干预的窗口：你可以通过 prompt 约束行为模式，也可以在锚点预测错误时（作者承认的局限）介入修正。相比之下，LinkVLA 虽然 DS 略高（91.01 vs 89.92），但 SR 落后近 3 个百分点（74.55 vs 77.28），且额外延迟高达 361 ms，说明其“全轨迹自回归”的代价是实时性。AnchorVLA 用 64 ms 的额外延迟换来了 SR 的显著提升，这个权衡在闭环驾驶中是有意义的——成功率比绝对分数更接近“安全”的定义。当然，Comfort 28.94 的短板也暴露了生成式细化的代价：灵活性与平滑度之间存在真实张力，作者对此的坦诚值得肯定。

## 方法拆解

AnchorVLA 的核心是把“决策”从语言空间下沉为轨迹空间中的离散锚点，再在锚点定义的残差空间里做连续生成。整个方法拆成三个模块：轨迹模式码本、决策锚点表示（DAAR）、以及决策锚定残差流（DARF）。

### 轨迹模式码本：行为先验的离散化
- 用 k-means 对训练集轨迹聚类，得到 \(K=100\) 个锚点 \(\mathcal{A}=\{a_k\}_{k=1}^{K}\)，每个 \(a_k\in\mathbb{R}^{T\times 2}\) 代表一个完整的局部运动模式（车道保持、制动、让行、转弯、超车等）。
- 轨迹与锚点的距离定义为平均 L2 距离：\(d(\tau_{\mathrm{gt}},a_k)=\frac{1}{T}\sum_{t=1}^{T}\|\tau_{\mathrm{gt}}^t-a_k^t\|_2\)。
- 关键设计：锚点不是坐标 token，而是“行为级”的轨迹原型。这直接回应了自回归方法中每个 token 仅含低层几何点、语义信息稀薄的问题——锚点把语义和几何绑定在一起。

### DAAR：两种决策建模方式
- **软锚点目标**：对真实轨迹 \(\tau_{\mathrm{gt}}\)，取 top-\(N\) 最近锚点集 \(\mathcal{N}\)，计算软标签 \(q_k=\frac{\mathbb{I}[k\in\mathcal{N}]\exp(-d(\tau_{\mathrm{gt}},a_k)/\gamma)}{\sum_{j\in\mathcal{N}}\exp(-d(\tau_{\mathrm{gt}},a_j)/\gamma)}\)，\(\gamma\) 为温度。软目标而非硬 one-hot，是为了保留锚点间的相似性结构，避免聚类边界处的硬截断。
- **查询式建模（Query Based）**：用可学习查询作为特征锚点分类器，MLP 头输出 logits，损失 \(\mathcal{L}_{\mathrm{qry}}=-\sum_{k=1}^{K}q_k\log p_{\theta}^{\mathrm{qry}}(a_k|x)\)。该模式额外延迟仅 33 ms。
- **自回归建模（Autoregressive）**：在 LLM 词汇表中插入 \(K\) 个特殊 token \(\{y_k\}_{k=1}^{K}\)，与锚点一一映射。训练时插入控制 token 和最近锚点 token，从控制 token 位置的 logits 提取锚点子集分布，损失 \(\mathcal{L}_{\mathrm{ar}}=-\sum_{k=1}^{K}q_k\log p_{\theta}^{\mathrm{ar}}(a_k|x)\)。额外延迟 64 ms。
- 消融显示自回归优于查询式（SR 77.28 vs 73.81），作者归因于自回归让 LLM 在生成锚点时能利用上下文注意力中的序列依赖，而查询式是独立分类、缺乏这种交互。

### DARF：残差空间中的流匹配
- 对 top-\(M\) 候选锚点（\(M=6\)），每个候选轨迹 \(\tau_k=a_k+r_k\)，目标残差 \(r_{\mathrm{gt}}^k=\tau_{\mathrm{gt}}-a_k\)。
- **流匹配路径**：\(z_t^k=(1-t)\epsilon+t r_{\mathrm{gt}}^k\)，\(\epsilon\sim\mathcal{N}(0,I)\)，目标速度 \(v_k^*=r_{\mathrm{gt}}^k-\epsilon\)。选择最接近真实轨迹的锚点 \(k^{\dagger}=\arg\min_{k\in\mathcal{I}_M}d(\tau_{\mathrm{gt}},a_k)\)，损失 \(\mathcal{L}_{\mathrm{flow}}=\|\hat{v}_{k^{\dagger}}-v_{k^{\dagger}}^*\|_1\)。
- **双分支解码器**：
  - 速度分支：输入噪声残差 \(z_t^k\)、时间步 \(t\)、锚点 \(a_k\)、多模态上下文 \(H_x\)。每个航点加 2D 正弦-余弦位置嵌入，经 MLP 编码为 \(h_z^k\)；锚点经两个独立 MLP 编码为 \(h_{a,k}^{pos}\)（速度分支）和 \(h_{a,k}^{conf}\)（置信度分支）。每层先做特征仿射调制 \(\mathrm{Mod}(h,c)=h\odot(1+s(c))+b(c)\) 融合时间特征，再将锚点位置特征作为查询偏置 \(q_l^k=h_l^k+h_{a,k}^{pos}\)，通过交叉注意力关注 \(H_x\)，残差头预测速度场 \(\hat{v}_l^k\in\mathbb{R}^{T\times 2}\)。
  - 置信度分支：不使用 \(z_t^k\) 和 \(t\)，仅以锚点特征 \(h_{a,k}^{conf}\) 为查询关注 \(H_x\)，输出标量分数 \(s_l^k\)，损失 \(\mathcal{L}_{\mathrm{conf}}=-\log\frac{\exp(s_{k^{\dagger}})}{\sum_{k\in\mathcal{I}_M}\exp(s_k)}\)。
- **推理**：少量欧拉步积分速度场，最终轨迹 \(\hat{\tau}=\hat{\tau}_{\arg\max_{k\in\mathcal{I}_M}s_k}\)。主实验 Flow Step 2，确定性变体 Step 1。
- 关键设计理由：锚点提供粗略轨迹参考，使残差目标比完整轨迹目标更紧凑，缩短流匹配的传输路径，让有限步生成更容易；流匹配建模残差分布以处理多模态细化，优于确定性残差回归（消融中 DARF SR 77.28 vs Deterministic 70.45）。

### 训练配置
两阶段：第一阶段训练 DAAR（15 epoch，8×A100，batch 16）；第二阶段冻结 VLA 骨干，训练 DARF（15 epoch，4×A100，batch 32）。VLA 骨干为 InternVL2-1B（InternViT-300M 视觉 + Qwen2-0.5B-Instruct 文本），GPS 目标点经 MLP 投影为 token 嵌入。

## 关键创新

AnchorVLA的核心创新在于将VLA的动作表示从“低层坐标token”提升到“高层轨迹模式锚点”，以此弥合语言推理与连续执行之间的抽象鸿沟。这一设计包含三个关键突破：

**其一，Decision-as-Anchor Representation（DAAR）将离散决策与连续轨迹在表示层面统一。** 通过k-means聚类构建K=100个轨迹模式码本，每个锚点对应一个完整局部运动模式（如车道保持、制动、让行）。轨迹被分解为τ = a_k + r_k，全局分布随之分解为p(τ|x) = Σ p(a_k|x)p(r_k|x,a_k)。这一分解的深刻之处在于：锚点选择是离散决策（对应语言指令的语义粒度），而残差生成是连续执行（对应几何精度），两者在数学上严格互补，而非简单拼接。相比自回归方法将轨迹离散化为坐标token（每个token仅含几何信息、序列长且误差累积），锚点token携带完整行为语义，显著压缩序列长度并缓解离散化误差。

**其二，双路径锚点决策建模兼顾效率与语义对齐。** 作者同时实现查询式（query-based）和自回归式两种锚点预测头，共享相同的软锚点目标q_k（基于top-N最近锚点的温度软化分布）。消融显示自回归式（DS 89.92, SR 77.28）优于查询式（DS 88.67, SR 73.81），且额外延迟仅64ms——远低于LinkVLA-AR的361ms。这证明在LLM词汇表中引入K个特殊token（每个映射一个锚点）能以极小代价将高层语言推理与行为决策对齐，而查询式则提供更轻量的替代方案。

**其三，Decision-Anchored Residual Flow（DARF）在锚点约束的残差空间中执行连续生成。** 这是对“抽象鸿沟”最直接的回应：流匹配不再在完整轨迹空间（高维、多模态、传输路径长）中运行，而是在锚点定义的残差空间（更紧凑、单模态、传输路径短）中预测速度场。消融显示DARF（DS 89.92, SR 77.28）显著优于确定性残差回归（DS 86.74, SR 70.45）和全轨迹流匹配（DS 88.34, SR 72.73），且仅增加18ms延迟。其解耦双分支设计——速度分支（受锚点位置特征调制）与置信度分支（独立评估锚点-上下文兼容性）——使最终轨迹选择既尊重高层行为意图，又保留细粒度几何调整能力。这一设计将“决策”从隐式潜变量变为显式可监督、可解释的结构化中间层，是VLA规划从“黑盒生成”走向“结构化决策”的关键一步。

## 实验与结果

AnchorVLA 在 Bench2Drive 闭环基准（CARLA）上的主结果（表1）显示，其 DS 89.92 / SR 77.28 显著领先于所有对比方法，但这一领先并非全面碾压：LinkVLA 的 DS 91.01 更高，Comfort 34.62 也优于 AnchorVLA 的 28.94。SR 优势（77.28 vs 74.55）是 AnchorVLA 的核心竞争力，说明其决策锚定机制在“完成驾驶任务”这一硬指标上更可靠。Efficiency 251.14 处于中游，低于 SimLingo（259.23）和 LinkVLA（255.84），但远高于 AutoVLA（146.93）和 TCP-traj（76.54），表明轨迹质量与平滑性之间存在权衡。

| 方法 | DS | SR | Efficiency | Comfort |
|---|---|---|---|---|
| AnchorVLA | 89.92 | 77.28 | 251.14 | 28.94 |
| LinkVLA | 91.01 | 74.55 | 255.84 | 34.62 |
| BridgeDrive | 87.99 | 74.99 | 236.49 | 20.98 |
| SimLingo | 85.07 | 67.27 | 259.23 | 33.67 |
| DiffusionDrive | 80.79 | 58.18 | 248.18 | 24.56 |
| AutoVLA | 78.84 | 57.73 | 146.93 | 39.33 |

多能力评估（表2）进一步揭示 AnchorVLA 的行为级优势：Overtake 81.11 和 Brake 90.00 均为最高，Merging 65.00 仅次于 BridgeDrive（69.92），Mean 74.22 领先 LinkVLA（73.40）和 BridgeDrive（73.15）。但 Give-Way 仅 50.00，与多数基线持平，说明在“让行”这类需要精细速度控制的场景中，锚点决策的粗粒度约束可能限制了残差细化的空间。

| 方法 | Merging | Overtake | Brake | Give-Way | Traffic-Sign | Mean |
|---|---|---|---|---|---|---|
| AnchorVLA | 65.00 | 81.11 | 90.00 | 50.00 | 85.00 | 74.22 |
| LinkVLA | 60.00 | 80.00 | 93.33 | 50.00 | 83.68 | 73.40 |
| BridgeDrive | 69.92 | 66.67 | 90.00 | 50.00 | 89.47 | 73.15 |
| SimLingo | 53.75 | 68.89 | 81.67 | 50.00 | 82.11 | 67.28 |

消融研究（表3）验证了锚点决策的必要性：无锚点（None）DS 87.49 / SR 70.91，Query Based 提升至 88.67 / 73.81，Autoregressive 达到 89.92 / 77.28。自回归建模额外延迟仅 64 ms，远低于 LinkVLA-AR 的 361 ms，说明将锚点作为 LLM 词汇表 token 的代价可控。表4 中 DARF（Flow Step 2，额外延迟 18 ms）相比 Deterministic（Flow Step 1，8 ms）DS 提升 3.18（由表内数值 4.0−0.8 计算）、SR 提升 6.83（由表内数值 64.22→59.9 计算），证明流匹配对残差多模态分布的建模优于确定性回归。导航模态消融（表5）显示 GPS 目标点与导航命令在 DS 上几乎持平（89.92 vs 90.26），但 GPS 在 Merging（65.00 vs 61.25）和 Overtake（81.11 vs 80.00）上更优，说明连续目标点提供了更丰富的空间线索。

综合来看，AnchorVLA 的核心贡献在于用 100 个轨迹模式锚点（k-means 聚类，top-M=6 候选）将高层决策与低层轨迹解耦，以 64 ms 锚点延迟 + 18 ms 残差延迟的代价换取了 SR 上的显著提升。但 Comfort 28.94 低于 LinkVLA（34.62）和 SimLingo（33.67），印证了作者承认的“生成式灵活细化与轨迹平滑度之间的权衡”——残差流在追求任务完成度时牺牲了乘坐舒适性，这可能是后续引入平滑感知目标或舒适度约束的切入点。

## 边界与局限

AnchorVLA的边界与局限首先体现在其核心假设上：轨迹模式码本（K=100）能否覆盖真实驾驶中的长尾行为。k-means聚类得到的锚点本质上是训练数据分布的统计中心，对分布外场景（如极端天气、非常规交通规则、罕见交互）的泛化能力论文未明确。作者承认的错误传播问题尤为关键——当锚点预测与语言指令或导航意图不一致时，DARF只在锚点定义的残差空间内细化，无法覆盖或纠正锚点本身的偏差，这意味着高层决策错误会直接传导至低层轨迹，且无反射机制（reflection mechanism）在生成前重新校验锚点与上下文的一致性。

其次，实验全部基于Bench2Drive/CARLA仿真，未提及真实车辆或更复杂开放场景验证。仿真环境的感知噪声、动力学模型与真实世界存在显著差异，锚点码本在真实数据上的有效性存疑。Comfort分数28.94低于LinkVLA（34.62）和SimLingo（33.67），表明生成式灵活细化与轨迹平滑度之间存在明确权衡，作者也承认未集成平滑感知目标或舒适度约束。此外，消融显示自回归锚点决策（64ms额外延迟）优于查询式（33ms），但代价是推理延迟翻倍，实时性边界未在更严苛硬件或更高帧率需求下验证。

DARF的流匹配仅用2步欧拉积分，虽在仿真中有效，但残差分布的传输路径缩短依赖锚点质量——若锚点远离真实轨迹，残差目标仍可能较大，有限步生成的精度保证缺乏理论分析。最后，导航模态消融中GPS目标点与导航命令的DS差异仅0.34，但Merging能力差异达3.75，说明不同导航信息对特定行为的影响未被深入解耦分析。

## 工程启示

复现AnchorVLA，第一优先级是核对码本构建与软锚点目标的一致性。论文用k-means在训练轨迹上聚类出K=100个锚点，距离度量是逐帧平均L2；软标签q_k依赖top-N近邻和温度γ，这两处超参直接决定DAAR训练信号质量，建议先固定N和γ做小规模敏感性测试，再上全量。最容易踩坑的是两阶段训练的解耦：第一阶段训DAAR时VLM骨干冻结，第二阶段训DARF时又冻结骨干只训残差流，若误将骨干梯度放开，会导致锚点分布漂移，复现出的DS/SR会明显低于报告的89.92/77.28。

DARF的工程细节值得注意：速度分支和置信度分支是解耦的，置信度分支不接收噪声残差z_t^k和时间步t，只以锚特征为查询去关注多模态上下文。若在实现中误把速度分支的隐藏状态共享给置信度分支，会破坏候选锚选择机制，导致表4中DARF相对Full Flow的SR增益（77.28 vs 72.73）消失。推理时流匹配仅用2步欧拉积分，额外延迟18ms，这是性能与实时性的关键平衡点；若为省算力降到1步，会退化为确定性回归，SR掉到70.45。下游团队若想换骨干，需注意锚点码本是在SimLingo骨干的轨迹分布上聚类的，换VLM后必须重新聚类，否则锚点与残差空间的语义对齐会失效。最后，Comfort分数28.94低于多个基线，这是生成式细化的固有代价，若产品对平顺性敏感，需在DARF损失中主动加入平滑约束，论文未做此优化。

## 参考
- http://arxiv.org/abs/2607.03182v1

## 개요
기존 VLA 플래너는 주로 플래닝 헤드 기반의 궤적 예측 또는 전체 궤적 자기회귀 생성에 의존하는데, 전자는 연속 궤적에 대한 제약이 약하고, 후자는 정보 밀도가 낮은 좌표 토큰의 긴 시퀀스를 사용하여 이산화 오류와 추론 효율 저하를 초래합니다. AnchorVLA는 결정을 앵커 표현으로 인코딩하여 행동 수준의 운전 결정을 앵커 토큰으로 표현하며, 각 토큰은 단일 좌표점이 아닌 완전한 국소 운동 패턴을 나타냅니다. 이후 결정 앵커링 잔차 흐름을 통해 선택된 앵커가 정의하는 잔차 공간에서 정밀한 연속 궤적을 생성합니다. 이러한 설계는 LLM 기반의 결정 능력을 유지하면서 추론 효율과 의미-행동 정렬 효과를 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
AnchorVLA는 계층적 결정 앵커링 프레임워크를 채택하며, 두 가지 핵심 모듈로 구성됩니다:
- **Decision-as-Anchor Representation**: 고수준 운전 결정(예: 차선 변경, 감속)을 컴팩트한 앵커 토큰으로 표현하며, 각 토큰은 전통적인 방법의 단일 좌표점이 아닌 완전한 국소 운동 패턴을 인코딩합니다. 이를 통해 모델은 비효율적인 웨이포인트 시퀀스를 자기회귀적으로 생성하는 대신 의미적으로 풍부한 앵커를 기반으로 추론할 수 있습니다.
- **Decision-Anchored Residual Flow**: 선택된 앵커가 정의하는 잔차 공간에서 정밀한 연속 궤적을 생성하여 고수준 결정 이후의 다중 모드 실행 세부화를 포착합니다. 이 모듈은 잔차 흐름 메커니즘을 통해 연속 궤적의 유연한 생성을 가능하게 하여 이산화 오류를 방지합니다.

### 실험 설정 및 주요 결과
- **벤치마크**: Bench2Drive 폐루프 시뮬레이션 벤치마크에서 평가되었으며, 다양한 운전 시나리오와 언어 명령을 포함합니다.
- **성능 지표**: AnchorVLA는 77.28의 성공률(state-of-the-art)과 89.92의 운전 점수를 달성하여 의미-행동 정렬 및 추론 효율에서 기존 VLA 플래너를 크게 능가합니다.
- **비교 우위**: 플래닝 헤드 기반 방법과 비교하여 AnchorVLA는 앵커를 통해 궤적 생성을 명시적으로 제약하며, 전체 궤적 자기회귀 방법과 비교하여 추론 속도가 빠르고 정보 밀도가 낮은 좌표 토큰으로 인한 문제를 피합니다.

### 결론
AnchorVLA는 궤적 패턴 앵커를 고수준 추론과 연속 실행 사이의 명시적 인터페이스로 도입하여 기존 VLA 플래너의 의미-행동 정렬 어려움과 추론 효율 저하 문제를 효과적으로 해결합니다. 실험을 통해 폐루프 운전 작업에서 선도적인 성능을 달성함을 입증했으며, 자율주행 계획에서의 시각-언어-행동 모델에 새로운 설계 패러다임을 제공합니다.
