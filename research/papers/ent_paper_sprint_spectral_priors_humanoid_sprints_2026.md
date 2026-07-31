---
$id: ent_paper_sprint_spectral_priors_humanoid_sprints_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints'
  zh: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints'
  ko: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints'
summary:
  en: 'The pursuit of humanoid athletic sprints is hindered by a scarcity of humanoid-viable kinematic reference data and
    the inability of existing frameworks to maintain stability during sprints. Institutions per source list: 国防科技大学、湖南大学.'
  zh: SPRINT 是一个面向人形机器人高速冲刺的框架，由研究团队提出，利用频率自适应频谱先验生成运动轨迹。该框架在 Unitree G1 平台上实现了零样本仿真到现实迁移，峰值冲刺速度达 6 m/s，并保持仿生自然性。
  ko: 'The pursuit of humanoid athletic sprints is hindered by a scarcity of humanoid-viable kinematic reference data and
    the inability of existing frameworks to maintain stability during sprints. Institutions per source list: 国防科技大学、湖南大学.'
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
- sprint
- efficient
- spectral
- priors
- humanoi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 791 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.28549v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.28549 SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints'
  url: https://arxiv.org/abs/2605.28549
  accessed_at: '2026-07-31'
  date: '2026-05-27'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

人形机器人运动领域长期面临两个瓶颈：缺乏适合高速冲刺的运动学参考数据，以及现有框架在冲刺中难以维持稳定性。SPRINT 通过构建一个包含五种离散运动序列的参考库，在频域中表征人类运动的基本周期性，从而生成覆盖广泛速度范围的可行关节轨迹。这些预训练先验引导策略在 Unitree G1 平台上实现了零样本仿真到现实迁移，峰值速度达到 6 m/s，并展示了无缝步态转换能力。

## 核心内容
### 核心挑战
人形机器人高速冲刺面临两大障碍：
- **数据稀缺**：缺乏适合人形机器人的高速运动学参考数据
- **稳定性不足**：现有框架在冲刺过程中难以维持平衡

### 方法架构
SPRINT 框架的核心创新在于频率自适应频谱先验：
- **频谱先验生成**：基于五种离散运动序列的参考库，在频域中提取人类运动的基本周期性特征
- **轨迹生成**：利用这些先验生成覆盖广泛速度范围的运动学可行关节轨迹，成功外推至超出参考分布的速度
- **策略学习**：预训练先验引导策略学习，实现零样本迁移

### 实验设置
- **硬件平台**：Unitree G1 人形机器人
- **迁移方式**：零样本仿真到现实迁移（sim-to-real）
- **性能指标**：峰值冲刺速度、步态转换能力、仿生自然性

### 关键结果
- **峰值速度**：达到 6 m/s，显著超越现有参考分布
- **步态转换**：实现无缝步态转换，保持运动连续性
- **仿生性**：运动轨迹保持仿生自然性，避免机械感

### 结论
SPRINT 证明了频率自适应频谱先验作为人形机器人高速冲刺的高效数据基础的有效性。该方法以极低的数据需求实现了高性能冲刺，为未来人形机器人运动控制提供了新范式。

项目页面：https://anonymous.4open.science/w/SPRINT-138A/

## Overview
The pursuit of humanoid athletic sprints is hindered by a scarcity of humanoid-viable kinematic reference data and the inability of existing frameworks to maintain stability during sprints. To overcome these limitations, we introduce SPRINT, a novel framework driven by efficient, frequency-adaptive spectral priors. By characterizing the fundamental periodicity of human locomotion in the frequency domain using a reference library of five discrete motion sequences, these priors generate kinematically feasible joint trajectories across a broad velocity spectrum, successfully extrapolating to speeds that exceed the reference distribution. Guided by these pretrained priors, the SPRINT policy achieves zero-shot sim-to-real transfer in field experiments on the Unitree G1 platform, reaching a peak sprinting velocity of 6 m/s and demonstrating seamless gait transitions while preserving biomimetic naturalness. Ultimately, this work establishes frequency-adaptive spectral priors as a highly data-efficient foundation for humanoid athletic sprints. The project page is available at https://anonymous.4open.science/w/SPRINT-138A/.

## 参考
- https://arxiv.org/abs/2605.28549
- https://github.com/ImChong/Robotics_Notebooks

## 개요

휴머노이드 로봇 운동 분야는 오랫동안 두 가지 병목 현상에 직면해 왔습니다: 고속 질주에 적합한 운동학 참조 데이터의 부족과 기존 프레임워크가 질주 중 안정성을 유지하기 어렵다는 점입니다. SPRINT는 다섯 가지 이산 운동 시퀀스를 포함하는 참조 라이브러리를 구축하여 주파수 영역에서 인간 운동의 기본 주기성을 특성화함으로써 광범위한 속도 범위를 포괄하는 실현 가능한 관절 궤적을 생성합니다. 이러한 사전 훈련된 사전 지식은 Unitree G1 플랫폼에서 제로샷 시뮬레이션-현실 전이를 가능하게 하여 최고 속도 6 m/s를 달성하고 매끄러운 보행 전환 능력을 보여줍니다.

## 핵심 내용
### 핵심 과제
휴머노이드 로봇의 고속 질주는 두 가지 주요 장애물에 직면합니다:
- **데이터 부족**: 휴머노이드 로봇에 적합한 고속 운동학 참조 데이터의 부족
- **안정성 부족**: 기존 프레임워크가 질주 중 균형을 유지하기 어려움

### 방법 아키텍처
SPRINT 프레임워크의 핵심 혁신은 주파수 적응형 스펙트럼 사전 지식입니다:
- **스펙트럼 사전 지식 생성**: 다섯 가지 이산 운동 시퀀스의 참조 라이브러리를 기반으로 주파수 영역에서 인간 운동의 기본 주기성 특징 추출
- **궤적 생성**: 이러한 사전 지식을 활용하여 광범위한 속도 범위를 포괄하는 운동학적으로 실현 가능한 관절 궤적을 생성하고, 참조 분포를 초과하는 속도로 성공적으로 외삽
- **정책 학습**: 사전 훈련된 사전 지식이 정책 학습을 안내하여 제로샷 전이 구현

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇
- **전이 방식**: 제로샷 시뮬레이션-현실 전이 (sim-to-real)
- **성능 지표**: 최고 질주 속도, 보행 전환 능력, 생체 모방 자연스러움

### 주요 결과
- **최고 속도**: 6 m/s 달성, 기존 참조 분포를 크게 초과
- **보행 전환**: 매끄러운 보행 전환 구현, 운동 연속성 유지
- **생체 모방성**: 운동 궤적이 생체 모방 자연스러움을 유지, 기계적 느낌 회피

### 결론
SPRINT는 주파수 적응형 스펙트럼 사전 지식이 휴머노이드 로봇 고속 질주를 위한 효율적인 데이터 기반으로서의 효과성을 입증했습니다. 이 방법은 매우 낮은 데이터 요구 사항으로 고성능 질주를 구현하여 미래 휴머노이드 로봇 운동 제어에 새로운 패러다임을 제공합니다.

프로젝트 페이지: https://anonymous.4open.science/w/SPRINT-138A/
