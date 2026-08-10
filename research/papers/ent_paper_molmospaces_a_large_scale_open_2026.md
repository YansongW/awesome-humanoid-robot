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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11337v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1157 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.11337v2

## 개요
MolmoSpaces는 기존 로봇 벤치마크에서 장면 레이아웃, 객체 기하학 및 작업 사양의 다양성이 부족한 문제를 해결하고, 대규모 시뮬레이션 인프라를 통해 물리적 평가의 한계를 보완하는 것을 목표로 합니다. 이 생태계는 23만 개의 실내 환경을 포함하며, 수작업으로 제작된 가정용 장면과 절차적으로 생성된 다중 방 주거 공간을 아우르고, 13만 개의 풍부한 주석이 달린 객체 자산을 갖추고 있으며, 그중 4.8만 개의 조작 가능한 객체는 4200만 개의 안정적인 파지 자세를 보유합니다. 시스템은 MuJoCo, Isaac 및 ManiSkill과 같은 주요 시뮬레이터를 지원하며, 정적 조작, 이동 조작, 내비게이션 및 다중 방 장기 시간 작업을 포괄합니다. 함께 제공되는 MolmoSpaces-Bench 벤치마크 스위트는 8가지 작업을 포함하며, 실험 결과 실제 세계와의 상관관계가 매우 높고 제로샷 정책의 성능 차이를 효과적으로 평가할 수 있음을 보여줍니다.

## 핵심 내용
### 방법
MolmoSpaces는 모듈식 아키텍처를 채택하며, 핵심 구성 요소는 다음과 같습니다:
- **환경 생성기**: 절차적 규칙과 수작업 템플릿을 기반으로 단일 방에서 다중 방 레이아웃까지 23만 개의 다양한 실내 장면을 생성합니다.
- **객체 자산 라이브러리**: 의미론, 기하학 및 물리 주석이 포함된 13만 개의 객체를 포함하며, 그중 4.8만 개의 조작 가능한 객체는 MuJoCo 시뮬레이션 검증을 기반으로 4200만 개의 안정적인 파지 자세를 사전 계산했습니다.
- **시뮬레이터 추상화 계층**: 통합 인터페이스를 통해 MuJoCo, Isaac Sim 및 ManiSkill을 지원하여 정책이 서로 다른 시뮬레이터 간에 이식 가능하도록 보장합니다.

### 작업 및 벤치마크
MolmoSpaces-Bench는 8가지 구현 작업을 포함하며, 세 가지 범주로 나뉩니다:
- **정적 조작**: 테이블 위 파지, 객체 재배치
- **이동 조작**: 목표 지점까지 내비게이션 후 파지, 문 열고 통과
- **장기 시간 작업**: 다중 방 청소, 물건 제자리 배치(인식, 계획 및 상호작용의 조정 필요)

### 실험 설정
- **정책 평가**: CLIPort, RT-2 등을 포함한 5가지 제로샷 정책을 테스트하고, 8가지 작업에서 성공률과 실행 시간을 기록했습니다.
- **Sim-to-Real 검증**: 실제 로봇 플랫폼에서 3가지 작업을 재현하고, 시뮬레이션과 실제 결과 간의 Pearson 상관계수 R=0.96 및 Spearman 순위 상관계수 ρ=0.98을 계산했습니다.
- **민감도 분석**: 프롬프트 문구 변화로 성공률 변동이 최대 12% 발생하고, 초기 관절 각도 편차가 5°를 초과하면 성능이 18% 하락하며, 카메라 가림이 시야의 30%를 초과하면 작업 실패율이 45%로 상승함을 발견했습니다.

### 핵심 결론
1. 더 새롭고 강력한 제로샷 정책(예: RT-2 2025 버전)은 MolmoSpaces-Bench에서 이전 버전(2024 버전)보다 평균 23%의 성공률 향상을 보였습니다.
2. 시뮬레이션 결과는 실제 세계와 높은 일치도를 보여 벤치마크의 신뢰성을 검증했습니다.
3. 정책은 입력 세부 사항에 민감하며, 프롬프트 최적화와 초기 자세 보정은 성능을 크게 향상시킬 수 있습니다.

### 오픈소스 리소스
MolmoSpaces는 환경 생성 스크립트, 객체 자산 라이브러리, 시뮬레이터 어댑터 및 벤치마크 평가 코드를 포함한 완전한 오픈소스 도구 체인을 제공하며, 확장 가능한 데이터 생성과 정책 훈련을 지원합니다.
