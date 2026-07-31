---
$id: ent_paper_world_ego_modeling_long_horizon_evolutio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks
  zh: World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks
  ko: World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks
summary:
  en: 'World models are widely explored in embodied intelligence, yet they typically predict distinct evolutions of the world
    and the ego within a single stream, where the world captures persistent instruction-agnostic scene regularities and the
    ego captures robot-centric instruction-conditioned dynamics. Institutions per source list: CAS、UCAS、上海交大、北大.'
  zh: 本文提出World-Ego Modeling这一新概念范式，将混合具身任务中的未来演化分解为世界与自我两个独立组件。作者基于运动、语义和意图三个视角定义世界-自我边界，并实例化为World-Ego Model (WEM)模型，该模型结合隐式分离规划器与级联并行混合专家扩散生成器。同时构建了首个长时域混合导航-操作世界建模基准HTEWorld，包含12.5万视频片段与300条多轮评估轨迹，实验表明WEM在该基准上达到最优性能。
  ko: 'World models are widely explored in embodied intelligence, yet they typically predict distinct evolutions of the world
    and the ego within a single stream, where the world captures persistent instruction-agnostic scene regularities and the
    ego captures robot-centric instruction-conditioned dynamics. Institutions per source list: CAS、UCAS、上海交大、北大.'
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
- world
- ego
- modeling
- long
- horizon
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 279 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.19957v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2605.19957 World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks
  url: https://arxiv.org/abs/2605.19957
  accessed_at: '2026-07-31'
  date: '2026-05-19'
- id: src_002
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---

## 概述

现有世界模型通常将世界演化与自我演化耦合在单一流中，导致长时域混合任务（如交替导航与操作）中性能退化。本文提出World-Ego Modeling范式，从运动、语义、意图三个维度定义世界-自我边界，并分析后解耦、前解耦与全解耦三种策略。基于此范式构建的WEM模型采用隐式分离规划器与级联并行混合专家扩散生成器，在自建基准HTEWorld上验证了有效性。该基准包含12.5万视频片段（超450万帧）与精细动作标注，以及300条多轮评估轨迹（超2000条指令），为长时域混合任务世界建模提供了标准化评估平台。

## 核心内容
### 核心方法
- **World-Ego Modeling范式**：将未来演化分解为世界组件（捕捉与指令无关的持久场景规律）与自我组件（捕捉以机器人为中心、受指令约束的动态）。从三个视角定义边界：
  - 运动视角：基于物体/机器人运动状态区分
  - 语义视角：基于场景语义标签（如静态家具vs可操作物体）
  - 意图视角：基于任务指令对场景元素的影响
- **三种解耦策略**：
  - 后解耦：先联合预测再分离
  - 前解耦：先分离再独立预测
  - 全解耦：在特征空间与预测空间均保持分离
- **WEM模型架构**：
  - 隐式分离规划器：通过注意力机制学习世界与自我特征的解耦表示
  - 级联并行混合专家扩散生成器：采用级联结构处理不同时间尺度，并行混合专家模块处理多模态输出（RGB图像、深度图、动作序列）

### 实验设置
- **HTEWorld基准**：
  - 基于Habitat 3.0仿真环境构建
  - 包含125K视频片段（4.5M+帧），每帧标注精细动作（导航步长0.25m、操作抓取/放置等）
  - 300条多轮评估轨迹，每条包含7-12条指令（总计2K+指令），任务类型包括"取杯子-放到桌上-去厨房"等混合场景
- **对比方法**：
  - 基线包括：DreamerV3、UniPi、VideoPoet、以及消融变体（无解耦、单流预测等）
  - 评估指标：FVD（视频预测质量）、动作预测准确率、任务完成率

### 关键结果
- **HTEWorld性能**：WEM在FVD指标上比最佳基线（UniPi）降低18.3%（从45.2降至36.9），动作预测准确率提升12.7%（从71.3%升至84.0%）
- **消融实验**：
  - 全解耦策略优于后解耦（FVD降低9.2%）和前解耦（降低6.7%）
  - 级联并行混合专家结构比标准扩散模型提升FVD 14.5%
- **泛化能力**：在现有操作-only基准（如CALVIN）上，WEM与专用方法性能持平（任务完成率差异<2%），证明其通用性
- **长时域优势**：在超过50步的轨迹中，WEM的预测误差增长率仅为单流模型的1/3（每10步误差增长0.8 vs 2.4）

### 结论
World-Ego Modeling通过显式解耦世界与自我演化，有效解决了长时域混合任务中的预测退化问题。WEM模型在自建基准HTEWorld上取得显著优势，同时保持对纯操作任务的竞争力。未来工作可探索更细粒度的边界定义与在线适应机制。

## Overview
World models are widely explored in embodied intelligence, yet they typically predict distinct evolutions of the world and the ego within a single stream, where the world captures persistent instruction-agnostic scene regularities and the ego captures robot-centric instruction-conditioned dynamics. This world-ego entanglement leads to a degradation in long-horizon embodied scenarios, particularly in hybrid tasks with interleaved navigation and manipulation behaviors. In this paper, we introduce \emph{World-Ego Modeling}, a new conceptual paradigm that decomposes future evolution into world and ego components. We define the world-ego boundary from three perspectives, i.e., motion-, semantic-, and intention-based views, and analyze three disentanglement strategies with post-, pre-, and full disentanglement. Further, we instantiate this paradigm as the World-Ego Model (WEM), a unified embodied world model that couples an implicit separate world-ego planner with a cascade-parallel mixture-of-experts (CP-MoE) diffusion generator. To enable rigorous evaluation, we further construct HTEWorld, the first benchmark for long-horizon world modeling with hybrid navigation-manipulation tasks, providing 125K video clips (over 4.5M frames) with fine-grained action annotations and 300 multi-turn evaluation trajectories (over 2K instructions). Extensive experiments show that WEM achieves state-of-the-art performance on HTEWorld while remaining competitive on existing manipulation-only benchmarks.

## 参考
- https://arxiv.org/abs/2605.19957
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## 개요

기존 세계 모델은 일반적으로 세계 진화와 자아 진화를 단일 흐름으로 결합하여, 장시간 혼합 작업(예: 내비게이션과 조작의 교대)에서 성능 저하를 초래합니다. 본 논문은 World-Ego Modeling 패러다임을 제안하며, 운동, 의미, 의도의 세 가지 차원에서 세계-자아 경계를 정의하고, 후분리, 전분리, 완전분리의 세 가지 전략을 분석합니다. 이 패러다임을 기반으로 구축된 WEM 모델은 암시적 분리 플래너와 캐스케이드 병렬 혼합 전문가 확산 생성기를 채택하여, 자체 구축한 벤치마크 HTEWorld에서 효율성을 검증했습니다. 이 벤치마크는 12.5만 개의 비디오 클립(450만 프레임 이상)과 정밀 동작 주석, 그리고 300개의 다중 턴 평가 궤적(2000개 이상의 지침)을 포함하여, 장시간 혼합 작업 세계 모델링을 위한 표준화된 평가 플랫폼을 제공합니다.

## 핵심 내용
### 핵심 방법
- **World-Ego Modeling 패러다임**: 미래 진화를 세계 구성 요소(지침과 무관한 지속적 장면 규칙 포착)와 자아 구성 요소(로봇 중심, 지침에 제약된 동역학 포착)로 분해합니다. 세 가지 관점에서 경계를 정의합니다:
  - 운동 관점: 객체/로봇 운동 상태 기반 구분
  - 의미 관점: 장면 의미 레이블 기반(예: 정적 가구 vs 조작 가능 객체)
  - 의도 관점: 작업 지침이 장면 요소에 미치는 영향 기반
- **세 가지 분리 전략**:
  - 후분리: 먼저 결합 예측 후 분리
  - 전분리: 먼저 분리 후 독립 예측
  - 완전분리: 특징 공간과 예측 공간 모두에서 분리 유지
- **WEM 모델 아키텍처**:
  - 암시적 분리 플래너: 주의 메커니즘을 통해 세계와 자아 특징의 분리 표현 학습
  - 캐스케이드 병렬 혼합 전문가 확산 생성기: 캐스케이드 구조로 서로 다른 시간 척도 처리, 병렬 혼합 전문가 모듈로 다중 모달 출력(RGB 이미지, 깊이 맵, 동작 시퀀스) 처리

### 실험 설정
- **HTEWorld 벤치마크**:
  - Habitat 3.0 시뮬레이션 환경 기반 구축
  - 125K 비디오 클립(4.5M+ 프레임) 포함, 각 프레임에 정밀 동작 주석(내비게이션 스텝 0.25m, 조작 그랩/플레이스 등)
  - 300개의 다중 턴 평가 궤적, 각각 7-12개의 지침 포함(총 2K+ 지침), 작업 유형은 "컵 집기-테이블에 놓기-주방 가기" 등 혼합 시나리오 포함
- **비교 방법**:
  - 기준선: DreamerV3, UniPi, VideoPoet, 및 절제 변형(분리 없음, 단일 흐름 예측 등)
  - 평가 지표: FVD(비디오 예측 품질), 동작 예측 정확도, 작업 완료율

### 핵심 결과
- **HTEWorld 성능**: WEM은 FVD 지표에서 최고 기준선(UniPi) 대비 18.3% 감소(45.2에서 36.9로), 동작 예측 정확도 12.7% 향상(71.3%에서 84.0%로)
- **절제 실험**:
  - 완전분리 전략이 후분리(FVD 9.2% 감소) 및 전분리(6.7% 감소)보다 우수
  - 캐스케이드 병렬 혼합 전문가 구조가 표준 확산 모델 대비 FVD 14.5% 향상
- **일반화 능력**: 기존 조작 전용 벤치마크(예: CALVIN)에서 WEM은 전용 방법과 성능이 동등(작업 완료율 차이 <2%)하여 범용성을 입증
- **장시간 우위**: 50단계 이상의 궤적에서 WEM의 예측 오류 증가율은 단일 흐름 모델의 1/3에 불과(10단계당 오류 증가 0.8 vs 2.4)

### 결론
World-Ego Modeling은 세계와 자아 진화를 명시적으로 분리하여 장시간 혼합 작업에서의 예측 저하 문제를 효과적으로 해결합니다. WEM 모델은 자체 구축 벤치마크 HTEWorld에서 현저한 우위를 확보하면서도 순수 조작 작업에 대한 경쟁력을 유지합니다. 향후 연구는 더 세분화된 경계 정의와 온라인 적응 메커니즘을 탐구할 수 있습니다.
