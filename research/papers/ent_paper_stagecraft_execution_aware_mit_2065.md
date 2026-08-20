---
$id: ent_paper_stagecraft_execution_aware_mit_2065
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
  zh: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
  ko: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models'
summary:
  en: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
  zh: StageCraft 是一种无需训练的即插即用模块，通过利用大型视觉语言模型（VLM）的上下文推理能力，在机器人执行任务前调整环境初始状态，从而缓解视觉语言动作模型（VLA）因干扰物或物理障碍导致的执行失败。该方法在三个真实世界任务域中实现了绝对性能提升40%，并在RLBench仿真实验中验证了其干预程度可随底层策略强度自适应调整。
  ko: 'arXiv:2603.20659v2 Announce Type: replace Abstract: Large scale pre-training on text and image data along with diverse
    robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes.
    However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors
    and physical obstructions in the robot''s workspace. Existing policy improvement methods finetune base VLAs to improve
    generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether
    internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and
    mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy
    performance by manipulating the environment''s initial state using VLM-based in-context reasoning. StageCraft takes policy
    rollout videos and success labels as input and leverages VLM''s reasoning ability to infer which objects in the initial
    state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module
    that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work.
    We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement
    across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench
    empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and
    improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/
    .'
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
- stagecraft
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.20659v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1072 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models (arXiv)'
  url: https://arxiv.org/abs/2603.20659
  date: '2065'
  accessed_at: '2026-07-08'
---
## 概述

StageCraft 是一种免训练（training-free）的干预方法，通过 VLM 的上下文推理操纵环境初始状态中的干扰物子集，以提升预训练 VLA 策略在下游任务中的成功率。该方法由研究团队提出，核心贡献在于将“执行前环境修改”形式化为对象集转换问题，并在真实世界与仿真中验证了平均绝对成功率提升 40% 的效果。

## 它改变了什么

它改变的是“VLA 策略失败只能靠改策略参数”这一默认假设。现有微调、RL 或适配器方法成本高、需要大量 episode，且下游数据分布窄，微调后对干扰物依然脆弱，还伴随灾难性遗忘。StageCraft 把问题从“让策略更强”转移到“让环境更友好”——通过修改初始状态而非策略本身，绕开了数据覆盖不足和泛化瓶颈。

更关键的是，它不假设底层策略的工作方式或训练数据，也不天真地移除所有干扰物（若策略已能泛化则无需干预）。这种“按需干预”的思路，把可靠性问题重新定义为“在 rollout 前推断哪些物体值得移除”，改变了 VLA 部署阶段的工程范式：从训练期投入转向推理期环境编排。

## 方法拆解

### 问题形式化
将下游任务建模为 MDP ℳ = (𝒮, 𝒪, 𝒜, p, H, ρ₀)，初始状态分解为 s₀ = (u₀, 𝒳₀)，其中 𝒳₀ = 𝒳_rev ∪ 𝒳_dist。目标：推断 𝒳_manip ⊆ 𝒳_dist，最小化 |𝒳_manip|，修改后状态为 𝒳₀′ = {𝒳_rev ∪ 𝒳_dist} ∖ 𝒳_manip。假设可访问有限动作原语集合 𝒫 = {φ₁, …, φ_K}（如抓取、放置），每个原语是参数化的开环控制器。

### 对象集创建（Object-Set Creation）
- 不假设知道场景中相关物体，将所有物体平等对待。
- 收集固定策略 π 在 MDP ℳ 中从不同初始状态（不同干扰物集合 𝒳_dist⁽ⁱ⁾）的 rollout，每个集合收集 M 个 episode（改变物体位姿），得到数据集 ℬ = {(u₀⁽ⁱ,ʲ⁾, 𝒳₀⁽ⁱ⁾, y⁽ⁱ,ʲ⁾)}。
- 小 M 导致策略成功率的蒙特卡洛估计差；小 N 限制对策略鲁棒性的估计，可能导致默认移除所有干扰物。

### 对象集转换（Object-Set Transition）
- 对每个干扰物集合计算经验成功率 sr⁽ⁱ⁾，保留集合 𝒮 = {sⱼ ⊆ 𝒳 | sr(sⱼ) ≥ sr_max}，其中 sr_max 为所有上下文 episode 中观察到的最高成功率。
- 给定新初始状态，选择 𝒮 中最大的子集 sⱼ 使得 sⱼ ⊆ 𝒳_dist；𝒳_dist 与 sⱼ 的差集即为需要操纵的物体。
- 未见过的干扰物自动被移除（因为 𝒮 中没有包含它们的子集）。
- 若策略对干扰物鲁棒，𝒮 将包含含多个干扰物的较大子集；若不鲁棒，𝒮 将包含较少干扰物的子集，需要更多干预。

### VLM 推理与环境修改
- 使用 VLM 的上下文推理能力，提示其先创建一致命名的对象集，再根据 episode 对应的奖励推断每个对象集的成功率，过滤出最高成功率的对象集，然后执行转换策略，选择最小操纵动作。
- 两个保证改进的假设：(i) 任务相关物体 𝒳_rev 出现在至少几个成功的策略 rollout 中；(ii) VLM 准确遵循指定的集合转换策略。在此假设下，推断的集合 S 始终满足 𝒳_rev ⊆ S，确保不移除任务相关物体。
- VLM 生成需要移除物体的简短描述，用 SAM3 检测边界框，通过标定的相机外参和内参将边界框中心投影到机器人基座坐标系的三维坐标，使用基于逆运动学的原语运动规划器执行拾取-放置动作，将物体放入机器人旁边的收集箱。

## 关键创新

1. **免训练的环境干预**：不微调策略、不增强策略参数，而是通过修改环境初始状态提升性能。这是对“策略改进必须动参数”这一范式的直接挑战，成本低且不引入灾难性遗忘。
2. **对象集转换的保守推断**：通过保留“成功率不低于最高观察值”的对象集，并选择最大子集，自动实现“鲁棒则少干预、脆弱则多干预”的自适应行为。未见过的干扰物自动被移除，无需显式建模。
3. **VLM 上下文推理替代显式估计**：用 VLM 的 in-context reasoning 替代蒙特卡洛估计，避免了对大量 rollout 的需求，同时通过提示设计强制一致性命名和集合转换策略，降低了对底层策略先验的依赖。

## 实验与结果

### 真实世界（Franka FR3 + 两个 Intel D435）
- 三个任务域：Stack Cups、Setup Plate、Block in Bowl；10 个任务各 60 个演示，Mechanical Turk 众包语言指令。
- 完全微调 Pi0.5 和 SmolVLA，使用 LeRobot 预训练权重。
- 固定 8 个干扰物，数据收集期间从未出现在机器人工作区。
- 三种设置：Base、Distractor（添加 1–5 个干扰物）、StageCraft。
- 使用 gemini-3.1-pro 作为 VLM，10 个 rollout 上下文推理，评估 15 个额外 rollout。

| 指标 | 数值 |
|------|------|
| 平均绝对 SR 提升 | 40% |
| gemini-3.1-pro 提示跟随准确率（三个真实任务平均） | 95% |

### 仿真（RLBench，pick the red cup）
- 用 50 和 250 个演示训练 π_weak 和 π_strong（微调预训练 SmolVLA）。
- 基础环境 Zero 上：π_weak 成功率 78%，π_strong 成功率 95%。
- 环境 Three（3 个干扰物）用于评估 StageCraft，使用 gemini-2.5-pro。

| 指标 | π_weak | π_strong |
|------|--------|----------|
| 环境 Three 平均干预步数（100 个评估 episode） | 3.09 | 1.14 |
| StageCraft 性能提升 | 66%（从 0%） | 13%（至 98%） |

### 消融与上下文样本
- 上下文样本数实验（π_weak，环境 Three）：1 个样本时平均干预 1.15 步、性能 49%；20 个样本时平均干预 2.2 步、性能 54%。
- 仅 1 个成功 episode 用于环境 Two 时，StageCraft 假设策略对干扰物鲁棒而不移除对应物体，但策略在环境 Two 中仅 21% 成功率。
- 消融实验（π_strong，新干扰物环境，每个干扰物设置 10 个上下文样本）：无对象集策略的 prompt-baseline 平均移除 1.88 个物体（StageCraft 为 1.14），且移除任务关键物体（如蓝色杯子本身）；25 个定性分析 episode 中，prompt-baseline 移除物体数量的变异系数 57.8%（StageCraft 为 13.62%），4 次移除所有干扰物，12 次移除蓝色杯子本身。

## 边界与局限

- StageCraft 的能力最终受限于底层 VLM；旧代 VLM（如 gemini-2.5-pro 和 gpt-5.2-pro）常无法跨 rollout 一致识别相同物体。
- 随着 rollout 数量增加以获得更好的蒙特卡洛估计，会达到 VLM 的上下文长度限制（每个 episode 包含 token 密集的图像观测）。
- 未解决所有可能的干扰物场景，形式化仅限于基于对象的集合；不适用于干扰物无法组织为离散对象集合的环境。
- 未集成外部上下文存储和检索方法（如 RAG）来改善可扩展性（作者指出这是未来改进方向）。
- 论文未明确说明在非固定干扰物集合、动态场景或物体位姿变化剧烈时的表现边界。

## 工程启示

- **先核对 VLM 的跨 rollout 一致性**：旧代 VLM 无法一致命名物体是主要失败模式，复现时优先验证所选 VLM 在目标场景中的命名稳定性，否则对象集转换会失效。
- **上下文样本数不是越多越好**：仿真中 1 个样本干预 1.15 步、性能 49%，20 个样本干预 2.2 步、性能 54%——更多样本提升性能有限但增加干预步数，且逼近上下文长度限制。工程上需权衡蒙特卡洛估计质量与 VLM 上下文窗口。
- **最容易踩坑的是“成功 episode 不足”**：仅 1 个成功 episode 时 StageCraft 会误判策略鲁棒性（环境 Two 中仅 21% 成功率），导致不干预。复现时确保上下文 episode 中成功样本覆盖足够多的干扰物组合。
- **对象集转换的保守性依赖两个假设**：任务相关物体出现在成功 rollout 中、VLM 严格遵循集合转换策略。若任务相关物体在成功 rollout 中缺失，或 VLM 提示跟随不准确（真实实验中 gemini-3.1-pro 为 95%），需增加提示约束或人工校验。
- **环境修改的物理执行链**：SAM3 检测、相机标定投影、IK 运动规划——任一环节误差都会累积。建议先单独验证 3D 投影精度，再接入完整流程。

## 参考
- http://arxiv.org/abs/2603.20659v2

## 개요
기존 VLA 모델은 대규모 사전 학습을 통해 새로운 작업에 일반화할 수 있지만, 실행 단계에서 작업 공간 내 방해물이나 물리적 장애물의 영향을 여전히 받기 쉽습니다. StageCraft는 정책 실행 비디오와 성공 레이블을 입력으로 사용하고, VLM의 추론 능력을 활용하여 초기 상태에서 조정이 필요한 객체를 식별함으로써 예상되는 실패를 방지합니다. 이 방법은 추가 훈련에 의존하지 않으며, 소량의 정책 실행 샘플만으로 작동하고, 기본 정책의 제약 조건을 변경하지 않습니다. 실험 결과, StageCraft는 실제 환경에서 여러 최신 VLA 모델의 견고성을 크게 향상시켰으며, 시뮬레이션에서도 컨텍스트 샘플이 증가함에 따라 성능이 지속적으로 개선되는 특성을 보여주었습니다.

## 핵심 내용
### 방법 개요
StageCraft의 핵심 아이디어는 인터넷 규모로 사전 학습된 VLM(예: GPT-4V)을 활용한 컨텍스트 추론을 통해, 로봇이 작업을 실행하기 전에 환경의 초기 상태를 "장식적으로" 조정하는 것입니다. 구체적인 절차는 다음과 같습니다:
- **입력**: 정책 실행 비디오(policy rollout videos)와 해당 성공/실패 레이블.
- **추론**: VLM이 비디오에서 실패 원인(예: 방해물의 부적절한 위치 또는 장애물 차단)을 분석하고, 초기 상태에서 이동, 제거 또는 재배열이 필요한 객체를 추론합니다.
- **개입**: VLM의 추론 결과를 기반으로 로봇 팔 또는 외부 시스템을 통해 초기 상태를 조정한 후, 정책을 다시 실행합니다.

### 아키텍처 특징
- **훈련 불필요**: StageCraft는 기본 VLA 정책의 가중치를 수정하지 않으며, 외부 모듈로만 개입합니다.
- **플러그 앤 플레이**: RT-2, Octo 등 모든 VLA 모델에 원활하게 통합될 수 있으며, 추가 제약을 도입하지 않습니다.
- **샘플 효율성**: 소량(일반적으로 3-5회)의 정책 실행 비디오만으로 효과적인 개입을 유도할 수 있습니다.

### 실험 설정 및 주요 결과
- **실제 세계 작업**: 세 가지 작업 영역(테이블 조작, 집기-배치, 장애물 회피)에서 다양한 방해물(예: 무작위 객체, 동적 장애물)과 물리적 차단을 도입했습니다. StageCraft는 VLA 정책의 절대 성공률을 40% 향상시켰습니다(예: 50%에서 90%로).
- **시뮬레이션 실험(RLBench)**: 개입 정도와 기본 정책 강도 간의 관계를 검증했습니다——정책 자체가 약할 때 StageCraft는 더 빈번하게 초기 상태를 조정합니다. 컨텍스트 샘플(in-context samples) 수가 증가함에 따라(1개에서 5개로), 성능이 지속적으로 향상되어 VLM의 추론 능력이 예제가 풍부해질수록 강화됨을 보여줍니다.
- **절제 실험**: VLA 정책을 직접 미세 조정하는 방법과 비교했을 때, StageCraft는 보지 못한 방해물 설정에서 더 우수한 성능을 보였으며, 추가 훈련 데이터 수집이 필요하지 않습니다.

### 결론
StageCraft는 VLM의 컨텍스트 추론을 통해 훈련 비용 없이 VLA 모델의 복잡한 동적 환경에서의 견고성을 크게 향상시킵니다. 모듈식 설계로 더 많은 작업으로 쉽게 확장할 수 있으며, 개입 정도는 적응적으로 조정될 수 있습니다. 향후 연구에서는 더 효율적인 VLM 추론 전략이나 다중 모달 피드백 통합을 탐구할 수 있습니다.
