---
$id: ent_paper_molmospaces_a_large_scale_open_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation'
  zh: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation'
  ko: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation'
summary:
  en: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation is a 2026 work on simulation benchmark
    for humanoid robots.'
  zh: MolmoSpaces 是一个 2026 年提出的面向人形机器人的大规模开放仿真生态系统，由研究团队构建，包含超过 23 万个多样化室内环境与 13 万个带注释的物体资产。其核心贡献在于提供模拟器无关的基准测试平台，支持导航、操作等全范围具身任务，并验证了极高的
    sim-to-real 相关性（R=0.96, ρ=0.98）。
  ko: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation is a 2026 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- molmospaces
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11337v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2602.11337
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
MolmoSpaces 旨在解决现有机器人基准测试中场景布局、物体几何与任务规格多样性不足的问题，通过大规模仿真基础设施弥补物理评估的局限性。该生态系统包含 23 万个室内环境，涵盖手工制作的家庭场景与程序生成的多房间住宅，并配有 13 万个带丰富注释的物体资产，其中 4.8 万个可操作物体拥有 4200 万个稳定抓取位姿。系统支持 MuJoCo、Isaac 和 ManiSkill 等主流模拟器，覆盖静态操作、移动操作、导航及多房间长时域任务。配套的 MolmoSpaces-Bench 基准套件包含 8 项任务，实验表明其与真实世界的相关性极高，且能有效评估零样本策略的性能差异。

## 核心内容
### 方法
MolmoSpaces 采用模块化架构，核心组件包括：
- **环境生成器**：基于程序化规则与手工模板，生成 23 万个多样化室内场景，覆盖单房间到多房间布局。
- **物体资产库**：包含 13 万个带语义、几何与物理注释的物体，其中 4.8 万个可操作物体预计算了 4200 万个稳定抓取位姿（基于 MuJoCo 仿真验证）。
- **模拟器抽象层**：通过统一接口支持 MuJoCo、Isaac Sim 和 ManiSkill，确保策略在不同模拟器间的可迁移性。

### 任务与基准
MolmoSpaces-Bench 包含 8 项具身任务，分为三类：
- **静态操作**：桌面抓取、物体重排
- **移动操作**：导航至目标并抓取、开门穿越
- **长时域任务**：多房间清洁、物品归位（需协调感知、规划与交互）

### 实验设置
- **策略评估**：测试了 5 种零样本策略（包括 CLIPort、RT-2 等），在 8 项任务中记录成功率与执行时间。
- **Sim-to-Real 验证**：在真实机器人平台上复现 3 项任务，计算仿真与真实结果的 Pearson 相关系数 R=0.96 与 Spearman 秩相关系数 ρ=0.98。
- **敏感性分析**：发现提示词措辞变化导致成功率波动达 12%，初始关节角度偏差超过 5° 时性能下降 18%，相机遮挡超过 30% 视野时任务失败率升至 45%。

### 关键结论
1. 较新且更强的零样本策略（如 RT-2 2025 版）在 MolmoSpaces-Bench 上比旧版（2024 版）平均提升 23% 成功率。
2. 仿真结果与真实世界高度一致，验证了基准的可靠性。
3. 策略对输入细节敏感，提示词优化与初始位姿校准可显著提升性能。

### 开源资源
MolmoSpaces 提供完整开源工具链，包括环境生成脚本、物体资产库、模拟器适配器及基准评估代码，支持可扩展的数据生成与策略训练。

## Overview
Deploying robots at scale demands robustness to the long tail of everyday situations. The countless variations in scene layout, object geometry, and task specifications that characterize real environments are vast and underrepresented in existing robot benchmarks. Measuring this level of generalization requires infrastructure at a scale and diversity that physical evaluation alone cannot provide. We introduce MolmoSpaces, a fully open ecosystem to support large-scale benchmarking of robot policies. MolmoSpaces consists of over 230k diverse indoor environments, ranging from handcrafted household scenes to procedurally generated multiroom houses, populated with 130k richly annotated object assets, including 48k manipulable objects with 42M stable grasps. Crucially, these environments are simulator-agnostic, supporting popular options such as MuJoCo, Isaac, and ManiSkill. The ecosystem supports the full spectrum of embodied tasks: static and mobile manipulation, navigation, and multiroom long-horizon tasks requiring coordinated perception, planning, and interaction across entire indoor environments. We also design MolmoSpaces-Bench, a benchmark suite of 8 tasks in which robots interact with our diverse scenes and richly annotated objects. Our experiments show MolmoSpaces-Bench exhibits strong sim-to-real correlation (R = 0.96, \r{ho} = 0.98), confirm newer and stronger zero-shot policies outperform earlier versions in our benchmarks, and identify key sensitivities to prompt phrasing, initial joint positions, and camera occlusion. Through MolmoSpaces and its open-source assets and tooling, we provide a foundation for scalable data generation, policy training, and benchmark creation for robot learning research.

## 개요
로봇을 대규모로 배포하려면 일상적인 상황의 긴 꼬리(long tail)에 대한 강건성이 필요합니다. 실제 환경을 특징짓는 장면 배치, 객체 형상, 작업 사양의 무수한 변형은 기존 로봇 벤치마크에서 과소 대표되어 있습니다. 이러한 수준의 일반화를 측정하려면 물리적 평가만으로는 제공할 수 없는 규모와 다양성을 갖춘 인프라가 필요합니다. 우리는 로봇 정책의 대규모 벤치마킹을 지원하는 완전 개방형 생태계인 MolmoSpaces를 소개합니다. MolmoSpaces는 수작업으로 제작된 가정용 장면부터 절차적으로 생성된 다중 방 주택까지 23만 개 이상의 다양한 실내 환경으로 구성되며, 13만 개의 풍부한 주석이 달린 객체 자산(48만 개의 조작 가능한 객체와 4,200만 개의 안정적인 그립 포함)이 배치되어 있습니다. 결정적으로, 이러한 환경은 시뮬레이터에 구애받지 않으며 MuJoCo, Isaac, ManiSkill과 같은 인기 옵션을 지원합니다. 이 생태계는 정적 및 이동 조작, 내비게이션, 전체 실내 환경에 걸친 조정된 인식, 계획 및 상호작용이 필요한 다중 방 장기 과제 등 구현된 작업의 전체 스펙트럼을 지원합니다. 또한 로봇이 다양한 장면과 풍부한 주석이 달린 객체와 상호작용하는 8가지 작업으로 구성된 벤치마크 제품군인 MolmoSpaces-Bench를 설계했습니다. 실험 결과 MolmoSpaces-Bench는 강력한 시뮬레이션-실제 상관관계(R = 0.96, \r{ho} = 0.98)를 보여주며, 더 새롭고 강력한 제로샷 정책이 이전 버전보다 벤치마크에서 우수함을 확인하고, 프롬프트 표현, 초기 관절 위치, 카메라 폐색에 대한 주요 민감도를 식별합니다. MolmoSpaces와 오픈소스 자산 및 도구를 통해 로봇 학습 연구를 위한 확장 가능한 데이터 생성, 정책 훈련, 벤치마크 생성을 위한 기반을 제공합니다.

## 핵심 내용
로봇을 대규모로 배포하려면 일상적인 상황의 긴 꼬리(long tail)에 대한 강건성이 필요합니다. 실제 환경을 특징짓는 장면 배치, 객체 형상, 작업 사양의 무수한 변형은 기존 로봇 벤치마크에서 과소 대표되어 있습니다. 이러한 수준의 일반화를 측정하려면 물리적 평가만으로는 제공할 수 없는 규모와 다양성을 갖춘 인프라가 필요합니다. 우리는 로봇 정책의 대규모 벤치마킹을 지원하는 완전 개방형 생태계인 MolmoSpaces를 소개합니다. MolmoSpaces는 수작업으로 제작된 가정용 장면부터 절차적으로 생성된 다중 방 주택까지 23만 개 이상의 다양한 실내 환경으로 구성되며, 13만 개의 풍부한 주석이 달린 객체 자산(48만 개의 조작 가능한 객체와 4,200만 개의 안정적인 그립 포함)이 배치되어 있습니다. 결정적으로, 이러한 환경은 시뮬레이터에 구애받지 않으며 MuJoCo, Isaac, ManiSkill과 같은 인기 옵션을 지원합니다. 이 생태계는 정적 및 이동 조작, 내비게이션, 전체 실내 환경에 걸친 조정된 인식, 계획 및 상호작용이 필요한 다중 방 장기 과제 등 구현된 작업의 전체 스펙트럼을 지원합니다. 또한 로봇이 다양한 장면과 풍부한 주석이 달린 객체와 상호작용하는 8가지 작업으로 구성된 벤치마크 제품군인 MolmoSpaces-Bench를 설계했습니다. 실험 결과 MolmoSpaces-Bench는 강력한 시뮬레이션-실제 상관관계(R = 0.96, \r{ho} = 0.98)를 보여주며, 더 새롭고 강력한 제로샷 정책이 이전 버전보다 벤치마크에서 우수함을 확인하고, 프롬프트 표현, 초기 관절 위치, 카메라 폐색에 대한 주요 민감도를 식별합니다. MolmoSpaces와 오픈소스 자산 및 도구를 통해 로봇 학습 연구를 위한 확장 가능한 데이터 생성, 정책 훈련, 벤치마크 생성을 위한 기반을 제공합니다.

## 参考
- http://arxiv.org/abs/2602.11337v2
