---
$id: ent_paper_wang_vla_survey_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines'
  zh: 机器人视觉-语言-动作：数据集、基准与数据引擎综述
  ko: '로보틱스에서의 비전-언어-액션: 데이터셋, 벤치마크 및 데이터 엔진에 대한 서베이'
summary:
  en: A 2026 survey arguing that VLA progress now depends more on data infrastructure and evaluation co-design than on model
    architecture, organized around datasets, benchmarks, and data engines.
  zh: 本文是2026年关于视觉-语言-动作（VLA）模型的综述，指出VLA进展的关键瓶颈已从模型架构转向数据基础设施与评估协同设计。研究围绕数据集、基准测试和数据引擎三大支柱展开系统分析，揭示了数据保真度与成本之间的根本性权衡，以及现有评估协议在组合泛化和长程推理方面的结构性缺陷。
  ko: 2026년 서베이로, VLA의 발전은 모델 아키텍처보다 데이터 인프라와 평가 공동 설계에 더 많이 의존하고 있으며, 데이터셋, 벤치마크, 데이터 엔진 세 축으로 구성됨.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- survey
- datasets
- benchmarks
- data_engines
- sim_to_real
- embodied_ai
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.23001v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py [2026-08-04] body rewritten as full-text
    six-section deep read (.staging/deep_read, DeepSeek deepseek-chat T<=0.3, arXiv HTML full text); en/ko sections regenerated
    by translate pipeline.
sources:
- id: src_paper_wang_vla_survey_2026
  type: paper
  title: 'Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines'
  url: https://arxiv.org/abs/2604.23001
  date: '2026-04-24'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: cites
  description:
    en: The survey cites Open X-Embodiment as a widely used cross-embodiment pretraining dataset.
    zh: 该综述引用 Open X-Embodiment 作为常用的跨具身预训练数据集。
    ko: 해당 서베이는 Open X-Embodiment를 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함.
- id: ent_dataset_droid
  relationship: cites
  description:
    en: The survey cites DROID as a distributed real-world dataset emphasizing visual and environmental variation.
    zh: 该综述引用 DROID 作为强调视觉与环境变化的分布式真实世界数据集。
    ko: 해당 서베이는 DROID를 시각 및 환경 변화를 강조하는 분산 실제 데이터셋으로 인용함.
- id: ent_benchmark_humanoidbench
  relationship: cites
  description:
    en: The survey discusses HumanoidBench as a simulation benchmark for whole-body locomotion and manipulation.
    zh: 该综述讨论 HumanoidBench 作为全身运动与操作的仿真基准。
    ko: 해당 서베이는 HumanoidBench를 전신 로코모션 및 조작을 위한 시뮬레이션 벤치마크로 논의함.
- id: ent_benchmark_libero
  relationship: cites
  description:
    en: The survey cites LIBERO as a representative short-horizon table-top VLA benchmark.
    zh: 该综述引用 LIBERO 作为代表性短程桌面 VLA 基准。
    ko: 해당 서베이는 LIBERO를 대표적인 단기 테이블탑 VLA 벤치마크로 인용함.
- id: ent_tech_mimicgen
  relationship: cites
  description:
    en: The survey discusses MimicGen as a demonstration augmentation method that scales simulator data.
    zh: 该综述讨论 MimicGen 作为扩展仿真器数据的演示增强方法。
    ko: 해당 서베이는 MimicGen을 시뮬레이터 데이터를 확장하는 데모 증강 방법으로 논의함.
- id: ent_tech_robogen
  relationship: cites
  description:
    en: The survey discusses RoboGen as an LLM-driven automatic task-generation framework for simulation.
    zh: 该综述讨论 RoboGen 作为由大语言模型驱动的仿真自动任务生成框架。
    ko: 해당 서베이는 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함.
theoretical_depth:
- system
---

## 概述

这篇来自马里兰大学、犹他大学、东北大学和威斯康星大学麦迪逊分校的综述，首次从数据为中心视角系统梳理了VLA（视觉-语言-动作）机器人学习领域。作者将现有工作组织为数据集、基准和数据引擎三大类，提出统一分类法和基准的二维表征框架，并识别出跨具身对齐、长时程评估可信度、物理真实数据生成三个结构性挑战。核心主张是：VLA的未来进展将更多依赖高保真数据引擎与结构化评估协议的协同设计，而非模型架构本身。

## 它改变了什么

这篇综述真正改变的是VLA研究的讨论重心——它把“数据基础设施”从配角推到了舞台中央。此前VLA领域的默认假设是“模型架构是瓶颈”，各家比拼的是网络结构、预训练策略和参数量；而这篇综述用大量证据表明，真正卡住进展的是数据保真度与可扩展性之间的根本矛盾，以及评估协议缺乏标准化导致的“报告改进无法验证真泛化”的困境。它让“数据引擎”这个此前零散、未被系统化的概念成为独立研究对象，并主张数据集、基准、生成引擎三者必须协同设计——这直接挑战了“先攒数据、再训模型、最后评估”的线性流水线思维。

更关键的是，它揭示了数据生成速度已经超过物理接地和验证速度这一结构性失衡。当Genie能从20万小时互联网视频无监督学习、RoboTwin 2.0能生成10万+专家轨迹时，瓶颈不再是“能不能生成”，而是“生成的数据是否物理可信、能否在真实机器人上闭环”。这个判断将迫使研究社区重新审视：我们缺的不是更多数据，而是能保证数据质量、可验证、可归因失败的数据基础设施。

## 方法拆解

### 形式化框架
- 将VLA问题形式化为顺序决策过程：策略π在每个时间步t接收视觉观测o_t和语言指令l，输出动作a_t = π(o_t, l)
- 动作表示沿两个轴区分：控制目标（末端执行器EEF空间 vs 关节DoF空间）和参数化方式（绝对目标 vs 相对/增量命令，a_t^Δ = a_t^abs − a_{t−1}^abs）
- 成功率定义为SR = (1/|ℰ|) Σ_{e∈ℰ} 𝕀[task completed in e]

### 统一分类法
- 数据集分为真实世界（Open X-Embodiment、RT-1/2、DROID、BridgeData V2、RH20T、Ego4D）和合成（SynGrasp-1B、RoboCasa、RoboGen、MimicGen）
- 数据引擎分为三类：视频到数据引擎（H2R、RoboWheel、Video2Policy、X-Humanoid、GenMimic、UniSim）、硬件辅助收集系统（ALOHA、GELLO、UMI、DexCap、Lucid-XR）、生成式数据引擎（MimicGen、DynaMimicGen、DemoGen、GenSim、RoboGen、RoboTwin 2.0、ROSIE、RoboEngine、EMMA、PointWorld、IRASim、3D-VLA、Genie）
- 基准按任务设置（桌面vs非桌面）、情节时长和任务复杂度组织，引入“任务复杂度×环境结构”二维表征框架

### 数据引擎关键技术路径
- **轨迹复用**：MimicGen将演示分割为以物体为中心的子任务再空间变换，从200条种子生成50k条演示；DynaMimicGen用DMP实现移动物体实时适应；DemoGen完全合成3D点云编辑
- **LLM驱动生成**：GenSim/RoboGen查询LLM生成任务代码和奖励函数；RoboTwin 2.0加入VLM反馈循环监控执行、检测失败、迭代修正
- **生成模型视觉增强**：ROSIE用文本到图像扩散做语义修复；RoboEngine含机器人专用分割模型Robo-SAM；EMMA通过DreamTransfer生成跨视角几何一致视频
- **预测性世界模型**：PointWorld用3D点流实现零样本MPC；IRASim做轨迹到视频扩散；3D-VLA生成多模态目标状态；Genie通过VQ-VAE从互联网视频发现潜在动作

## 关键创新

**第一，首次提出“数据引擎”作为独立研究对象。** 此前视频到数据、硬件采集、生成式数据增强分散在不同子领域，没有统一抽象。这篇综述将它们归入“数据生成过程𝒢”的形式化框架，使研究者能系统比较不同引擎的输入类型（视频、仿真状态、人类演示、语言提示）、人工依赖度和Sim2Real验证情况——这为后续工作提供了可操作的比较维度。

**第二，揭示“接地可靠性”而非“生成能力”是数据引擎的真正瓶颈。** 当Genie能从20万小时视频无监督学习、RoboTwin 2.0能生成10万+轨迹时，生成规模已不是问题。真正的限制在于：视频管线依赖感知保真度，接地/姿态估计失败会引入系统性噪声；LLM驱动引擎在物理理解和奖励规范方面存在缺口。这个判断将研究注意力从“生成更多”转向“生成更可信”。

**第三，提出基准的二维表征框架（任务复杂度×环境结构）。** 现有基准如Meta-World、CALVIN、COLOSSEUM、BEHAVIOR-1K各自覆盖不同难度维度，但缺乏统一坐标系。这个框架使研究者能定位“某个基准到底在测什么”，并识别出任务复杂度和环境结构常同时变化导致失败归因困难的问题——这是对现有评估协议最尖锐的批评之一。

## 实验与结果

| 任务/方法 | 基线/对照 | 关键指标 | 结果 |
|---------|---------|---------|------|
| H2R（视频到数据） | 预训练视觉编码器MAE、R3M | 仿真操作成功率提升 | 1.3–10.2个百分点 |
| H2R（视频到数据） | 预训练视觉编码器MAE、R3M | 真实机器人成功率提升 | 3–23个百分点 |
| Video2Policy | 100+视频 | 仿真成功率 | 88% |
| UniSim | 短演示基线 | 性能提升 | 3–4倍 |
| ALOHA | ACT动作分块 | 成功率 | 80–90% |
| GELLO | VR基线 | 可靠性提升 | 近30% |
| UMI | 标准遥操作 | 采集速度 | 快3倍 |
| UMI | 30个真实地点、12人小时 | 零样本成功率 | 71.7% |
| DexCap | 多指任务 | 成功率 | 72% |
| Lucid-XR | 真实遥操作 | 有效数据量 | 5倍 |
| DemoGen | 单条演示、8个真实任务 | 平均成功率 | 74.6% |
| RoboGen | 69个基准任务 | 平均成功率 | 77.4% |
| ROSIE | 基线 | 整体性能提升 | 超过115% |
| IRASim | 真实仿真评估 | 相关性 | 0.99 |
| IRASim | 规划后Push-T | IoU | 0.637→0.961 |
| MimicGen | 200条种子演示 | 生成演示数 | 50k条 |
| CALVIN | 五个连续指令 | 成功率 | 0.08% |

这些数字揭示了一个关键模式：视频到数据引擎（H2R、Video2Policy、UniSim）和硬件辅助系统（UMI、GELLO）在真实机器人上取得了可验证的改进，而纯生成式引擎（MimicGen、RoboGen）虽能大规模生产数据，但多数缺乏Sim2Real验证。CALVIN上五个连续指令成功率降至0.08%则尖锐暴露了长时程组合任务的评估困境——这直接支撑了作者关于“可信评估”是结构性挑战的判断。

## 边界与局限

作者明确承认未提出新数据集、基准或数据引擎，也未进行任何新实验。综述范围限定于机器人操作（机械臂+夹爪），不涵盖自动驾驶或移动导航。真实世界数据集无法从根本上解决质量-成本权衡；合成数据受渲染质量和物理真实性的根本限制；抓取任务中姿态常通过启发式采样生成，可能不反映稳定策略。视频到数据引擎仍面临重建噪声和最小动作误差挑战。现有基准中任务复杂度和环境结构常纠缠变化，使失败归因困难。接触丰富行为（需力/触觉反馈）在真实环境采集昂贵且代表性不足。论文未提及具体训练配置、GPU型号、训练时间等工程细节。

## 工程启示

对复现和选型，最值得先核对的是**数据引擎的Sim2Real验证状态**——表中大量生成式引擎（MimicGen、GenSim、RoboGen、ROSIE、RoboEngine、EMMA）没有Sim2Real验证，这意味着它们的效果只在仿真内被证实，直接迁移到真实机器人风险极高。如果你的团队目标是真实部署，优先考虑有Sim2Real验证的引擎（H2R、RoboWheel、Video2Policy、UniSim、Lucid-XR、PointWorld、IRASim、3D-VLA）。

最容易踩坑的是**动作参数化的异构性**：Open X-Embodiment混合了EEF和DoF动作、绝对和Delta参数化，跨具身聚合时接口对齐本身就是难题。如果你的下游任务需要跨机器人迁移，务必先统一动作表示（a_t^Δ = a_t^abs − a_{t−1}^abs 这个形式化定义值得作为对齐基准）。另一个坑是**评估协议不标准化**——不同工作使用不同成功标准和数据划分，报告的数字可能不可比。建议采用CALVIN的零样本泛化协议作为强基线，但要注意其长时程任务成功率极低（0.08%），不要用它作为唯一评估手段。

对硬件采集团队，UMI（GoPro夹爪+SLAM，快3倍）和GELLO（300美元3D打印外骨骼，可靠性提升30%）是低成本高性价比方案；ALOHA（2万美元）适合需要高精度双臂操作的任务。对纯算法团队，DemoGen（单条演示74.6%成功率）和IRASim（与真实仿真相关性0.99）值得优先复现——前者证明完全合成数据的可行性，后者可作为仿真评估的可信代理。最后，持续关注作者维护的资源库（github.com/ziyaow1010/vla-datasets-benchmarks），这是目前最系统的VLA数据基础设施索引。

## 参考
- http://arxiv.org/abs/2604.23001v1

## Overview

This survey from the University of Maryland, University of Utah, Northeastern University, and the University of Wisconsin-Madison is the first to systematically organize the field of VLA (Vision-Language-Action) robot learning from a data-centric perspective. The authors organize existing work into three categories—datasets, benchmarks, and data engines—propose a unified taxonomy and a two-dimensional representation framework for benchmarks, and identify three structural challenges: cross-embodiment alignment, long-horizon evaluation credibility, and physically realistic data generation. The core claim is that future progress in VLA will depend more on the co-design of high-fidelity data engines and structured evaluation protocols than on model architecture itself.

## What It Changes

What this survey truly changes is the focus of VLA research discussions—it pushes "data infrastructure" from a supporting role to center stage. Previously, the default assumption in the VLA field was that "model architecture is the bottleneck," with groups competing on network structures, pretraining strategies, and parameter counts. This survey uses extensive evidence to show that what actually constrains progress is the fundamental tension between data fidelity and scalability, along with the dilemma that non-standardized evaluation protocols make "reported improvements unable to verify true generalization." It elevates the "data engine"—previously scattered and unsystematized—into an independent research object, and argues that datasets, benchmarks, and generation engines must be co-designed—directly challenging the linear pipeline mindset of "collect data first, train models next, evaluate last."

More critically, it reveals a structural imbalance: data generation speed has already outpaced physical grounding and verification speed. When Genie can learn unsupervised from 200,000 hours of internet video and RoboTwin 2.0 can generate 100,000+ expert trajectories, the bottleneck is no longer "whether we can generate" but "whether the generated data is physically credible and can be closed-loop tested on real robots." This judgment will force the research community to reconsider: what we lack is not more data, but data infrastructure that guarantees quality, enables verification, and supports failure attribution.

## Method Breakdown

### Formal Framework
- Formalizes the VLA problem as a sequential decision process: policy π receives visual observation o_t and language instruction l at each timestep t, and outputs action a_t = π(o_t, l)
- Action representations are distinguished along two axes: control target (end-effector EEF space vs. joint DoF space) and parameterization (absolute targets vs. relative/incremental commands, a_t^Δ = a_t^abs − a_{t−1}^abs)
- Success rate is defined as SR = (1/|ℰ|) Σ_{e∈ℰ} 𝕀[task completed in e]

### Unified Taxonomy
- Datasets are divided into real-world (Open X-Embodiment, RT-1/2, DROID, BridgeData V2, RH20T, Ego4D) and synthetic (SynGrasp-1B, RoboCasa, RoboGen, MimicGen)
- Data engines are divided into three categories: video-to-data engines (H2R, RoboWheel, Video2Policy, X-Humanoid, GenMimic, UniSim), hardware-assisted collection systems (ALOHA, GELLO, UMI, DexCap, Lucid-XR), and generative data engines (MimicGen, DynaMimicGen, DemoGen, GenSim, RoboGen, RoboTwin 2.0, ROSIE, RoboEngine, EMMA, PointWorld, IRASim, 3D-VLA, Genie)
- Benchmarks are organized by task setting (tabletop vs. non-tabletop), episode length, and task complexity, introducing a two-dimensional representation framework of "task complexity × environment structure"

### Key Technical Paths for Data Engines
- **Trajectory reuse**: MimicGen segments demonstrations into object-centric subtasks and applies spatial transformations, generating 50k demonstrations from 200 seeds; DynaMimicGen uses DMPs for real-time adaptation to moving objects; DemoGen performs fully synthetic 3D point cloud editing
- **LLM-driven generation**: GenSim/RoboGen query LLMs to generate task code and reward functions; RoboTwin 2.0 adds a VLM feedback loop to monitor execution, detect failures, and iteratively correct
- **Generative model visual enhancement**: ROSIE uses text-to-image diffusion for semantic inpainting; RoboEngine includes the robot-specific segmentation model Robo-SAM; EMMA generates cross-view geometrically consistent videos via DreamTransfer
- **Predictive world models**: PointWorld achieves zero-shot MPC with 3D point flows; IRASim performs trajectory-to-video diffusion; 3D-VLA generates multimodal goal states; Genie discovers latent actions from internet video via VQ-VAE

## Key Innovations

**First, proposing the "data engine" as an independent research object.** Previously, video-to-data, hardware collection, and generative data augmentation were scattered across different subfields without a unified abstraction. This survey groups them under the formal framework of the "data generation process 𝒢," enabling researchers to systematically compare different engines along input types (video, simulation state, human demonstrations, language prompts), human dependency levels, and Sim2Real verification status—providing actionable comparison dimensions for subsequent work.

**Second, revealing that "grounding reliability" rather than "generation capability" is the true bottleneck for data engines.** When Genie can learn unsupervised from 200,000 hours of video and RoboTwin 2.0 can generate 100,000+ trajectories, generation scale is no longer the issue. The real constraint lies in: video pipelines depend on perception fidelity, where grounding/pose estimation failures introduce systematic noise; and LLM-driven engines have gaps in physical understanding and reward specification. This judgment shifts research attention from "generating more" to "generating more credibly."

**Third, proposing a two-dimensional representation framework for benchmarks (task complexity × environment structure).** Existing benchmarks such as Meta-World, CALVIN, COLOSSEUM, and BEHAVIOR-1K each cover different difficulty dimensions but lack a unified coordinate system. This framework allows researchers to locate "what a given benchmark is actually measuring" and identifies the problem that task complexity and environment structure often vary simultaneously, making failure attribution difficult—one of the sharpest critiques of existing evaluation protocols.

## Experiments and Results

| Task/Method | Baseline/Control | Key Metric | Result |
|---------|---------|---------|------|
| H2R (video-to-data) | Pretrained visual encoders MAE, R3M | Simulation manipulation success rate improvement | 1.3–10.2 percentage points |
| H2R (video-to-data) | Pretrained visual encoders MAE, R3M | Real robot success rate improvement | 3–23 percentage points |
| Video2Policy | 100+ videos | Simulation success rate | 88% |
| UniSim | Short demonstration baseline | Performance improvement | 3–4× |
| ALOHA | ACT action chunking | Success rate | 80–90% |
| GELLO | VR baseline | Reliability improvement | ~30% |
| UMI | Standard teleoperation | Collection speed | 3× faster |
| UMI | 30 real locations, 12 person-hours | Zero-shot success rate | 71.7% |
| DexCap | Multi-finger tasks | Success rate | 72% |
| Lucid-XR | Real teleoperation | Effective data volume | 5× |
| DemoGen | Single demonstration, 8 real tasks | Average success rate | 74.6% |
| RoboGen | 69 benchmark tasks | Average success rate | 77.4% |
| ROSIE | Baseline | Overall performance improvement | Over 115% |
| IRASim | Real-simulation evaluation | Correlation | 0.99 |
| IRASim | Push-T after planning | IoU | 0.637→0.961 |
| MimicGen | 200 seed demonstrations | Generated demonstrations | 50k |
| CALVIN | Five consecutive instructions | Success rate | 0.08% |

These numbers reveal a key pattern: video-to-data engines (H2R, Video2Policy, UniSim) and hardware-assisted systems (UMI, GELLO) achieve verifiable improvements on real robots, while purely generative engines (MimicGen, RoboGen), though capable of large-scale data production, mostly lack Sim2Real validation. The CALVIN success rate dropping to 0.08% on five consecutive instructions sharply exposes the evaluation dilemma for long-horizon compositional tasks—directly supporting the authors' judgment that "credible evaluation" is a structural challenge.

## Boundaries and Limitations

The authors explicitly acknowledge that they propose no new datasets, benchmarks, or data engines, and conduct no new experiments. The survey scope is limited to robot manipulation (arm + gripper), excluding autonomous driving and mobile navigation. Real-world datasets cannot fundamentally resolve the quality-cost tradeoff; synthetic data is fundamentally limited by rendering quality and physical realism; in grasping tasks, poses are often generated via heuristic sampling and may not reflect stable policies. Video-to-data engines still face challenges from reconstruction noise and minimal action errors. In existing benchmarks, task complexity and environment structure often vary in entangled ways, making failure attribution difficult. Contact-rich behaviors (requiring force/tactile feedback) are expensive to collect in real environments and are underrepresented. The paper does not mention specific training configurations, GPU models, training times, or other engineering details.

## Engineering Implications

For reproduction and method selection, the first thing worth verifying is the **Sim2Real validation status of data engines**—many generative engines in the table (MimicGen, GenSim, RoboGen, ROSIE, RoboEngine, EMMA) lack Sim2Real validation, meaning their effectiveness is only confirmed in simulation and direct transfer to real robots carries high risk. If your team's goal is real-world deployment, prioritize engines with Sim2Real validation (H2R, RoboWheel, Video2Policy, UniSim, Lucid-XR, PointWorld, IRASim, 3D-VLA).

The most common pitfall is **heterogeneity in action parameterization**: Open X-Embodiment mixes EEF and DoF actions, absolute and Delta parameterizations, and interface alignment itself is a challenge when aggregating across embodiments. If your downstream task requires cross-robot transfer, be sure to unify action representations first (the formal definition a_t^Δ = a_t^abs − a_{t−1}^abs is worth using as an alignment baseline). Another pitfall is **non-standardized evaluation protocols**—different works use different success criteria and data splits, so reported numbers may not be comparable. We recommend adopting CALVIN's zero-shot generalization protocol as a strong baseline, but note its extremely low long-horizon task success rate (0.08%)—do not use it as the sole evaluation method.

For hardware collection teams, UMI (GoPro gripper + SLAM, 3× faster) and GELLO ($300 3D-printed exoskeleton, 30% reliability improvement) are low-cost, high-value solutions; ALOHA ($20,000) suits tasks requiring high-precision bimanual manipulation. For pure algorithm teams, DemoGen (74.6% success rate from a single demonstration) and IRASim (0.99 correlation with real simulation) are worth reproducing first—the former demonstrates the feasibility of fully synthetic data, and the latter serves as a credible proxy for simulation evaluation. Finally, keep an eye on the resource repository maintained by the authors (github.com/ziyaow1010/vla-datasets-benchmarks), currently the most systematic index of VLA data infrastructure.

## 개요

메릴랜드 대학교, 유타 대학교, 노스이스턴 대학교, 위스콘신 대학교 매디슨 캠퍼스의 연구자들이 작성한 이 서베이는 데이터 중심 관점에서 VLA(비전-언어-행동) 로봇 학습 분야를 최초로 체계적으로 정리한 논문입니다. 저자들은 기존 연구를 데이터셋, 벤치마크, 데이터 엔진의 세 가지 범주로 구성하고, 통합 분류법과 벤치마크의 2차원 표현 프레임워크를 제안하며, 교차-구현 정렬, 장기 평가 신뢰성, 물리적으로 사실적인 데이터 생성이라는 세 가지 구조적 과제를 식별합니다. 핵심 주장은 VLA의 향후 발전이 모델 아키텍처 자체보다는 고충실도 데이터 엔진과 구조화된 평가 프로토콜의 협력적 설계에 더 크게 의존할 것이라는 점입니다.

## 그것이 바꾸는 것

이 서베이가 실제로 바꾸는 것은 VLA 연구의 논의 중심입니다——"데이터 인프라"를 조연에서 무대 중앙으로 끌어올립니다. 이전 VLA 분야의 암묵적 가정은 "모델 아키텍처가 병목이다"였으며, 각 팀은 네트워크 구조, 사전 학습 전략, 파라미터 수를 겨루었습니다. 그러나 이 서베이는 방대한 증거를 통해 실제로 진행을 막는 것이 데이터 충실도와 확장성 사이의 근본적 모순, 그리고 평가 프로토콜의 표준화 부재로 인한 "보고된 개선이 실제 일반화를 검증하지 못하는" 딜레마임을 보여줍니다. 이는 "데이터 엔진"이라는 이전에는 산발적이고 체계화되지 않았던 개념을 독립적인 연구 대상으로 만들고, 데이터셋, 벤치마크, 생성 엔진이 반드시 협력적으로 설계되어야 한다고 주장합니다——이는 "데이터를 먼저 모으고, 모델을 훈련하고, 마지막으로 평가하는" 선형 파이프라인 사고를 직접적으로 도전합니다.

더 중요하게, 이 논문은 데이터 생성 속도가 이미 물리적 접지 및 검증 속도를 초과했다는 구조적 불균형을 드러냅니다. Genie가 20만 시간의 인터넷 비디오에서 비지도 학습을 할 수 있고, RoboTwin 2.0이 10만 개 이상의 전문가 궤적을 생성할 수 있을 때, 병목은 더 이상 "생성할 수 있는가"가 아니라 "생성된 데이터가 물리적으로 신뢰할 수 있고, 실제 로봇에서 폐루프로 검증될 수 있는가"입니다. 이 판단은 연구 커뮤니티가 재고하도록 강제할 것입니다: 우리에게 부족한 것은 더 많은 데이터가 아니라, 데이터 품질을 보장하고 검증 가능하며 실패를 귀인할 수 있는 데이터 인프라입니다.

## 방법 분해

### 형식적 프레임워크
- VLA 문제를 순차적 의사결정 과정으로 형식화: 정책 π는 각 시간 단계 t에서 시각적 관측 o_t와 언어 명령 l을 수신하고, 행동 a_t = π(o_t, l)을 출력
- 행동 표현은 두 축을 따라 구분: 제어 목표(엔드 이펙터 EEF 공간 vs 관절 DoF 공간) 및 파라미터화 방식(절대 목표 vs 상대/증분 명령, a_t^Δ = a_t^abs − a_{t−1}^abs)
- 성공률은 SR = (1/|ℰ|) Σ_{e∈ℰ} 𝕀[task completed in e]로 정의

### 통합 분류법
- 데이터셋은 실제 세계(Open X-Embodiment, RT-1/2, DROID, BridgeData V2, RH20T, Ego4D)와 합성(SynGrasp-1B, RoboCasa, RoboGen, MimicGen)으로 구분
- 데이터 엔진은 세 가지 범주로 분류: 비디오-데이터 엔진(H2R, RoboWheel, Video2Policy, X-Humanoid, GenMimic, UniSim), 하드웨어 지원 수집 시스템(ALOHA, GELLO, UMI, DexCap, Lucid-XR), 생성적 데이터 엔진(MimicGen, DynaMimicGen, DemoGen, GenSim, RoboGen, RoboTwin 2.0, ROSIE, RoboEngine, EMMA, PointWorld, IRASim, 3D-VLA, Genie)
- 벤치마크는 작업 설정(테이블 위 vs 비테이블), 에피소드 길이, 작업 복잡도에 따라 구성되며, "작업 복잡도 × 환경 구조" 2차원 표현 프레임워크를 도입

### 데이터 엔진 핵심 기술 경로
- **궤적 재사용**: MimicGen은 데모를 객체 중심 하위 작업으로 분할한 후 공간 변환하여 200개의 시드에서 50k개의 데모를 생성; DynaMimicGen은 DMP를 사용하여 이동 객체에 실시간 적응; DemoGen은 3D 포인트 클라우드 편집을 완전히 합성
- **LLM 기반 생성**: GenSim/RoboGen은 LLM에 쿼리하여 작업 코드와 보상 함수를 생성; RoboTwin 2.0은 VLM 피드백 루프를 추가하여 실행을 모니터링하고 실패를 감지하며 반복적으로 수정
- **생성 모델 비주얼 강화**: ROSIE는 텍스트-이미지 확산을 사용한 의미론적 인페인팅; RoboEngine은 로봇 전용 분할 모델 Robo-SAM 포함; EMMA는 DreamTransfer를 통해 교차 시점 기하학적으로 일관된 비디오 생성
- **예측적 세계 모델**: PointWorld는 3D 포인트 플로우로 제로샷 MPC 구현; IRASim은 궤적-비디오 확산; 3D-VLA는 다중 모달 목표 상태 생성; Genie는 VQ-VAE를 통해 인터넷 비디오에서 잠재 행동 발견

## 핵심 혁신

**첫째, "데이터 엔진"을 독립적인 연구 대상으로 최초 제안.** 이전에는 비디오-데이터, 하드웨어 수집, 생성적 데이터 증강이 서로 다른 하위 분야에 흩어져 있었고 통일된 추상화가 없었습니다. 이 서베이는 이를 "데이터 생성 과정 𝒢"의 형식적 프레임워크로 묶어, 연구자들이 서로 다른 엔진의 입력 유형(비디오, 시뮬레이션 상태, 인간 데모, 언어 프롬프트), 인간 의존도, Sim2Real 검증 상태를 체계적으로 비교할 수 있게 합니다——이는 후속 작업에 실행 가능한 비교 차원을 제공합니다.

**둘째, "접지 신뢰성"이 "생성 능력"보다 데이터 엔진의 진정한 병목임을 밝힘.** Genie가 20만 시간의 비디오에서 비지도 학습을 할 수 있고 RoboTwin 2.0이 10만 개 이상의 궤적을 생성할 수 있을 때, 생성 규모는 더 이상 문제가 아닙니다. 진정한 제약은: 비디오 파이프라인이 인식 충실도에 의존하며 접지/자세 추정 실패가 체계적 노이즈를 도입하고, LLM 기반 엔진이 물리적 이해와 보상 사양에 격차가 있다는 점입니다. 이 판단은 연구 관심을 "더 많이 생성"에서 "더 신뢰할 수 있게 생성"으로 전환합니다.

**셋째, 벤치마크의 2차원 표현 프레임워크(작업 복잡도 × 환경 구조) 제안.** 기존 벤치마크인 Meta-World, CALVIN, COLOSSEUM, BEHAVIOR-1K는 각각 다른 난이도 차원을 다루지만 통일된 좌표계가 부족합니다. 이 프레임워크는 연구자들이 "특정 벤치마크가 실제로 무엇을 측정하는지"를 파악할 수 있게 하고, 작업 복잡도와 환경 구조가 종종 동시에 변화하여 실패 귀인이 어려운 문제를 식별합니다——이는 기존 평가 프로토콜에 대한 가장 날카로운 비판 중 하나입니다.

## 실험 및 결과

| 작업/방법 | 기준/대조 | 핵심 지표 | 결과 |
|---------|---------|---------|------|
| H2R(비디오-데이터) | 사전 학습 비주얼 인코더 MAE, R3M | 시뮬레이션 조작 성공률 향상 | 1.3–10.2퍼센트 포인트 |
| H2R(비디오-데이터) | 사전 학습 비주얼 인코더 MAE, R3M | 실제 로봇 성공률 향상 | 3–23퍼센트 포인트 |
| Video2Policy | 100+ 비디오 | 시뮬레이션 성공률 | 88% |
| UniSim | 짧은 데모 기준 | 성능 향상 | 3–4배 |
| ALOHA | ACT 행동 청킹 | 성공률 | 80–90% |
| GELLO | VR 기준 | 신뢰성 향상 | 약 30% |
| UMI | 표준 원격 조작 | 수집 속도 | 3배 빠름 |
| UMI | 30개 실제 위치, 12인-시간 | 제로샷 성공률 | 71.7% |
| DexCap | 다지 작업 | 성공률 | 72% |
| Lucid-XR | 실제 원격 조작 | 유효 데이터량 | 5배 |
| DemoGen | 단일 데모, 8개 실제 작업 | 평균 성공률 | 74.6% |
| RoboGen | 69개 벤치마크 작업 | 평균 성공률 | 77.4% |
| ROSIE | 기준 | 전체 성능 향상 | 115% 초과 |
| IRASim | 실제 시뮬레이션 평가 | 상관관계 | 0.99 |
| IRASim | 계획 후 Push-T | IoU | 0.637→0.961 |
| MimicGen | 200개 시드 데모 | 생성 데모 수 | 50k개 |
| CALVIN | 다섯 개 연속 명령 | 성공률 | 0.08% |

이 숫자들은 핵심 패턴을 드러냅니다: 비디오-데이터 엔진(H2R, Video2Policy, UniSim)과 하드웨어 지원 시스템(UMI, GELLO)은 실제 로봇에서 검증 가능한 개선을 달성한 반면, 순수 생성적 엔진(MimicGen, RoboGen)은 대규모 데이터 생산이 가능하지만 대부분 Sim2Real 검증이 부족합니다. CALVIN에서 다섯 개 연속 명령의 성공률이 0.08%로 떨어진 것은 장기 조합 작업의 평가 딜레마를 날카롭게 드러냅니다——이는 "신뢰할 수 있는 평가"가 구조적 과제라는 저자들의 판단을 직접적으로 뒷받침합니다.

## 경계와 한계

저자들은 새로운 데이터셋, 벤치마크 또는 데이터 엔진을 제안하지 않았으며 새로운 실험도 수행하지 않았음을 명시적으로 인정합니다. 서베이 범위는 로봇 조작(로봇 팔 + 그리퍼)으로 제한되며 자율주행이나 이동 내비게이션은 포함하지 않습니다. 실제 세계 데이터셋은 품질-비용 트레이드오프를 근본적으로 해결할 수 없습니다; 합성 데이터는 렌더링 품질과 물리적 사실성의 근본적 제약을 받습니다; 그리핑 작업에서 자세는 종종 휴리스틱 샘플링으로 생성되어 안정적인 정책을 반영하지 않을 수 있습니다. 비디오-데이터 엔진은 여전히 재구성 노이즈와 최소 행동 오류의 과제에 직면합니다. 기존 벤치마크에서 작업 복잡도와 환경 구조는 종종 얽혀 변화하여 실패 귀인을 어렵게 만듭니다. 접촉이 풍부한 행동(힘/촉각 피드백 필요)은 실제 환경에서 수집 비용이 높고 대표성이 부족합니다. 논문은 구체적인 훈련 구성, GPU 모델, 훈련 시간 등의 엔지니어링 세부 사항을 언급하지 않습니다.

## 엔지니어링 시사점

재현 및 선택 측면에서 가장 먼저 확인해야 할 것은 **데이터 엔진의 Sim2Real 검증 상태**입니다——표의 많은 생성적 엔진(MimicGen, GenSim, RoboGen, ROSIE, RoboEngine, EMMA)은 Sim2Real 검증이 없으며, 이는 그 효과가 시뮬레이션 내에서만 입증되었고 실제 로봇으로 직접 전환할 때 위험이 매우 높다는 것을 의미합니다. 팀의 목표가 실제 배포라면 Sim2Real 검증이 있는 엔진(H2R, RoboWheel, Video2Policy, UniSim, Lucid-XR, PointWorld, IRASim, 3D-VLA)을 우선 고려하십시오.

가장 쉽게 함정에 빠지는 것은 **행동 파라미터화의 이질성**입니다: Open X-Embodiment는 EEF와 DoF 행동, 절대 및 Delta 파라미터화를 혼합하며, 교차-구현 집계 시 인터페이스 정렬 자체가 어려운 문제입니다. 다운스트림 작업이 교차 로봇 전환을 필요로 한다면 반드시 먼저 행동 표현을 통일하십시오(a_t^Δ = a_t^abs − a_{t−1}^abs 형식적 정의가 정렬 기준으로 가치가 있습니다). 또 다른 함정은 **평가 프로토콜의 비표준화**입니다——서로 다른 작업이 서로 다른 성공 기준과 데이터 분할을 사용하므로 보고된 숫자가 비교 불가능할 수 있습니다. CALVIN의 제로샷 일반화 프로토콜을 강력한 기준선으로 채택하는 것을 권장하지만, 장기 작업 성공률이 매우 낮다는 점(0.08%)을 인지하고 유일한 평가 수단으로 사용하지 마십시오.

하드웨어 수집 팀에게 UMI(GoPro 그리퍼 + SLAM, 3배 빠름)와 GELLO(300달러 3D 프린팅 외골격, 신뢰성 30% 향상)는 저비용 고효율 솔루션입니다; ALOHA(2만 달러)는 고정밀 양팔 조작 작업에 적합합니다. 순수 알고리즘 팀에게 DemoGen(단일 데모 74.6% 성공률)과 IRASim(실제 시뮬레이션 상관관계 0.99)은 우선 재현할 가치가 있습니다——전자는 완전 합성 데이터의 실현 가능성을 입증하고, 후자는 시뮬레이션 평가의 신뢰할 수 있는 대리자 역할을 할 수 있습니다. 마지막으로, 저자들이 유지 관리하는 리소스 저장소(github.com/ziyaow1010/vla-datasets-benchmarks)를 지속적으로 주시하십시오——현재 가장 체계적인 VLA 데이터 인프라 인덱스입니다.
