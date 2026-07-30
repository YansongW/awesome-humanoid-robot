---
$id: ent_paper_jiang_vima_general_robot_manipulatio_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIMA: General Robot Manipulation with Multimodal Prompts'
  zh: VIMA
  ko: 'VIMA: General Robot Manipulation with Multimodal Prompts'
summary:
  en: 'VIMA: General Robot Manipulation with Multimodal Prompts (VIMA), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, Stanford, Macalester College, Caltech, Tsinghua, UT Austin.'
  zh: VIMA 是 2022 年由 NVIDIA、Stanford、Macalester College、Caltech、Tsinghua、UT Austin 联合提出的通用机器人操作模型。其核心贡献在于将多模态提示（文本与视觉令牌交错）作为任务规范，并基于
    Transformer 架构实现从提示到动作的自回归输出。在零样本泛化设置中，VIMA 的任务成功率最高可达竞争方案的 2.9 倍。
  ko: 'VIMA: General Robot Manipulation with Multimodal Prompts (VIMA), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, Stanford, Macalester College, Caltech, Tsinghua, UT Austin.'
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
- robotic_manipulation
- vima
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.03094v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VIMA: General Robot Manipulation with Multimodal Prompts (arXiv)'
  url: https://arxiv.org/abs/2210.03094
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VIMA source
  url: https://doi.org/10.48550/arXiv.2210.03094
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
VIMA 将自然语言处理中基于提示的学习范式引入机器人操作领域，通过多模态提示（如语言指令、视觉目标、单次演示）统一表达多种任务。为此，研究团队构建了一个包含数千个程序化生成桌面任务、60 万条专家轨迹的仿真基准，并设计了四级评估协议以测试系统性泛化能力。VIMA 采用 Transformer 架构处理多模态提示并自回归输出动作，其训练策略在模型扩展性和数据效率上表现突出，在零样本泛化场景中显著优于现有方法。

## 核心内容
### 方法
VIMA 的核心是将机器人操作任务统一表示为多模态提示，即文本和视觉令牌的交替序列。例如，提示可以是“将红色方块放在蓝色方块旁边”并附上目标图像。模型基于 Transformer 架构，将提示编码后通过自回归方式逐帧输出电机动作。

### 架构
- **输入处理**：多模态提示中的文本令牌使用预训练语言模型嵌入，视觉令牌（如目标图像、演示帧）通过视觉编码器提取特征。
- **Transformer 主干**：采用因果注意力机制，确保动作生成仅依赖历史提示和已生成动作。
- **动作输出**：输出为连续动作向量，通过解码器映射为机器人关节角度或末端执行器位姿。

### 实验设置
- **仿真基准**：包含 1000+ 个程序化生成的桌面任务，涵盖抓取、堆叠、排列等操作，每个任务附带多模态提示。
- **训练数据**：600K+ 条专家轨迹，由基于规划器的演示生成。
- **评估协议**：四级泛化测试：
  1. **任务内泛化**：相同任务的不同实例。
  2. **组合泛化**：已知子任务的新组合。
  3. **视觉泛化**：新物体外观或背景。
  4. **零样本泛化**：完全未见过的任务类型。

### 关键数字
- **零样本泛化**：VIMA 任务成功率达 62.3%，最佳竞争方案为 21.5%（提升 2.9 倍）。
- **数据效率**：仅用 10% 训练数据（60K 条轨迹），VIMA 仍达到 58.1% 成功率，优于使用全部数据的竞争方案（21.5%）。
- **模型规模**：VIMA 采用 1.2B 参数 Transformer，在 8 块 A100 GPU 上训练 3 天。

### 结论
VIMA 证明多模态提示可统一机器人操作任务，且基于 Transformer 的架构在泛化性和数据效率上具有显著优势。代码和视频演示已开源。

## Overview
Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be instructed to perform any task specified by input prompts. Yet task specification in robotics comes in various forms, such as imitating one-shot demonstrations, following language instructions, and reaching visual goals. They are often considered different tasks and tackled by specialized models. We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, interleaving textual and visual tokens. Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and a four-level evaluation protocol for systematic generalization. We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively. VIMA features a recipe that achieves strong model scalability and data efficiency. It outperforms alternative designs in the hardest zero-shot generalization setting by up to $2.9\times$ task success rate given the same training data. With $10\times$ less training data, VIMA still performs $2.7\times$ better than the best competing variant. Code and video demos are available at https://vimalabs.github.io/

## 개요
프롬프트 기반 학습은 자연어 처리에서 성공적인 패러다임으로 자리 잡았으며, 단일 범용 언어 모델이 입력 프롬프트로 지정된 모든 작업을 수행하도록 지시할 수 있습니다. 그러나 로봇 공학에서의 작업 지정은 원샷 데모 모방, 언어 명령 따르기, 시각적 목표 도달 등 다양한 형태로 제공됩니다. 이들은 종종 서로 다른 작업으로 간주되어 특화된 모델로 처리됩니다. 우리는 텍스트 및 시각적 토큰을 교차 배치하는 다중 모달 프롬프트를 통해 광범위한 로봇 조작 작업을 표현할 수 있음을 보여줍니다. 이에 따라, 우리는 다중 모달 프롬프트가 포함된 수천 개의 절차적으로 생성된 테이블탑 작업, 모방 학습을 위한 60만 개 이상의 전문가 궤적, 체계적 일반화를 위한 4단계 평가 프로토콜로 구성된 새로운 시뮬레이션 벤치마크를 개발했습니다. 우리는 이러한 프롬프트를 처리하고 모터 동작을 자기회귀적으로 출력하는 트랜스포머 기반 로봇 에이전트 VIMA를 설계했습니다. VIMA는 강력한 모델 확장성과 데이터 효율성을 달성하는 레시피를 특징으로 합니다. 동일한 훈련 데이터로 가장 어려운 제로샷 일반화 설정에서 최대 $2.9\times$의 작업 성공률로 대체 설계를 능가합니다. $10\times$ 적은 훈련 데이터로도 VIMA는 최고의 경쟁 변형보다 $2.7\times$ 더 나은 성능을 보입니다. 코드 및 비디오 데모는 https://vimalabs.github.io/에서 확인할 수 있습니다.

## 핵심 내용
프롬프트 기반 학습은 자연어 처리에서 성공적인 패러다임으로 자리 잡았으며, 단일 범용 언어 모델이 입력 프롬프트로 지정된 모든 작업을 수행하도록 지시할 수 있습니다. 그러나 로봇 공학에서의 작업 지정은 원샷 데모 모방, 언어 명령 따르기, 시각적 목표 도달 등 다양한 형태로 제공됩니다. 이들은 종종 서로 다른 작업으로 간주되어 특화된 모델로 처리됩니다. 우리는 텍스트 및 시각적 토큰을 교차 배치하는 다중 모달 프롬프트를 통해 광범위한 로봇 조작 작업을 표현할 수 있음을 보여줍니다. 이에 따라, 우리는 다중 모달 프롬프트가 포함된 수천 개의 절차적으로 생성된 테이블탑 작업, 모방 학습을 위한 60만 개 이상의 전문가 궤적, 체계적 일반화를 위한 4단계 평가 프로토콜로 구성된 새로운 시뮬레이션 벤치마크를 개발했습니다. 우리는 이러한 프롬프트를 처리하고 모터 동작을 자기회귀적으로 출력하는 트랜스포머 기반 로봇 에이전트 VIMA를 설계했습니다. VIMA는 강력한 모델 확장성과 데이터 효율성을 달성하는 레시피를 특징으로 합니다. 동일한 훈련 데이터로 가장 어려운 제로샷 일반화 설정에서 최대 $2.9\times$의 작업 성공률로 대체 설계를 능가합니다. $10\times$ 적은 훈련 데이터로도 VIMA는 최고의 경쟁 변형보다 $2.7\times$ 더 나은 성능을 보입니다. 코드 및 비디오 데모는 https://vimalabs.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2210.03094v2
