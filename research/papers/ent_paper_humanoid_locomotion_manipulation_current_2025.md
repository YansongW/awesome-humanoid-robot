---
$id: ent_paper_humanoid_locomotion_manipulation_current_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning'
  zh: 'Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning'
  ko: 'Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning'
summary:
  en: Humanoid robots hold great potential to perform various human-level skills, involving unified locomotion and manipulation
    in real-world settings. Driven by advances in machine learning and the strength of existing model-based approaches, these
    capabilities have progressed rapidly, but often separately. This survey offers a comprehensive overview of the state-of-the-art
    in humanoid locomotion and.
  zh: 本文是一篇关于人形机器人全身运动与操作（locomotion-manipulation）的权威综述，由佐治亚理工学院、南加州大学、Google DeepMind、NVIDIA 等多机构联合撰写。文章系统梳理了模型基方法（MPC、WBC、接触规划）与学习基方法（RL、IL、基础模型）的现状，指出两者分离是当前核心瓶颈，并提出了融合感知、规划、控制与学习的未来方向。
  ko: Humanoid robots hold great potential to perform various human-level skills, involving unified locomotion and manipulation
    in real-world settings. Driven by advances in machine learning and the strength of existing model-based approaches, these
    capabilities have progressed rapidly, but often separately. This survey offers a comprehensive overview of the state-of-the-art
    in humanoid locomotion and.
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
- humanoid
- locomotion
- manipulation
- current
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): xiaoze_P069. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2501.02116 Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control'
  url: https://arxiv.org/abs/2501.02116
  date: '2025-01-03'
  accessed_at: '2026-08-05'
---

## 概述

本文是一篇关于人形机器人全身运动与操作（locomotion-manipulation）的权威综述，由佐治亚理工学院、南加州大学、Google DeepMind、NVIDIA 等多机构联合撰写。文章系统梳理了模型基方法（MPC、WBC、接触规划）与学习基方法（RL、IL、基础模型）的现状，指出两者分离是当前核心瓶颈，并提出了融合感知、规划、控制与学习的未来方向。

## 它改变了什么

这篇综述真正改变的是对“人形机器人全身操作”这一问题的定义方式。过去，locomotion 和 manipulation 被当作两个独立领域分别研究，模型基与学习基方法各自为战，缺乏统一的理论框架和评价基准。作者明确指出，这种分离导致模型基方法难以处理非结构化环境和动态交互，而纯学习方法又因高自由度、稀疏奖励和 sim-to-real 差距而效率低下。更关键的是，作者将“触觉感知”和“接触推理”提升到与运动规划同等重要的位置，指出动态接触理解（而非静态接触点估计）是连接感知、规划与控制的枢纽——这一视角转变将推动整个领域从“轨迹生成”转向“交互推理”。

## 方法拆解

### 模型基方法：分层控制架构
- **MPC-WBC 层级**：全身 MPC（基于 SRBM、CD 或 WBD 模型）生成质心与末端执行器轨迹，底层 WBC 通过求解 QP 实现瞬时力矩分配。关键公式：WBC 动力学方程 M𝒒̈ − Jᵀ𝝀 − Sᵀ𝝉 = −C𝒒̇ − G，决策变量 X = [𝒒̈, 𝝀, 𝝉]ᵀ 使问题线性化，可实时求解。
- **接触规划三范式**：搜索式（状态扩展探索接触模式，启发式加速）、优化式（CITO 将接触动力学纳入轨迹优化，用平滑最大值函数近似接触冲量）、学习式（RL 预测接触序列，[177] 实现 0.1 秒内生成，较优化方法快 300 倍）。
- **MPC 加速策略**：结构利用（稀疏 NLP 将复杂度从 O(N³) 降至 O(N)）、逐次线性化（形成稀疏 QP）、热启动（用上一迭代解或运动记忆初始化）、采样（MPPI 利用 GPU 并行）。ReLU-QP 将人形平衡 MPC 频率从 65 Hz 提升至 1300 Hz 以上。

### 学习基方法：数据与策略
- **数据来源四类**：策略执行、遥操作、动作捕捉、人类视频。机器人经验数据形态匹配但稀缺；人类数据丰富但存在具身差距（embodiment gap），需重定向（retargeting）解决。
- **混合范式**：教师-学生（特权观测训练教师，部分观测克隆学生）、IL 预训练 + RL 微调、MPC 生成参考轨迹 + RL 运动模仿（轨迹增强）。
- **技能表示**：MOE（专家不平衡问题）、VAE/GAN 潜在空间、Goal-Conditioned Policies、世界模型（TD-MPC2 以 MPC 方式规划想象轨迹）。
- **基础模型**：VLA 模型（RT-2、OpenVLA、π₀）将动作标记化，π₀ 实现 50 Hz 高频控制；分层框架（LLM/VLM 高层决策 + 低层控制策略）是当前主流部署方式。

## 关键创新

1. **统一框架的提出**：首次将触觉感知、接触规划、全身控制、模仿学习与基础模型纳入同一分析框架，明确了“动态接触推理”作为连接各模块的核心纽带。这一视角超越了以往将感知、规划、控制割裂的综述范式。
2. **对“数据扩展”的批判性反思**：作者主张泛化应通过包含被操作物体运动、认知动作和多模态观测实现，而非单纯数据量扩展。这一观点挑战了“大数据 + 大模型”的流行叙事，为数据采集策略提供了新方向。
3. **混合保真度模型与级联架构**：提出近视野用全阶模型、远视野用简化模型的级联保真度策略，以及云端 FM 高层决策 + 机载实时控制的去中心化部署架构，为计算受限的实时系统提供了可行路径。

## 实验与结果

本文为综述性质，未报告原始实验数据，但汇总了关键量化指标：

| 指标 | 数值 | 来源 |
|------|------|------|
| 学习式接触序列生成时间 | <0.1 秒 | [177] |
| 学习式接触规划加速比 | 300 倍（vs 优化方法） | [177] |
| ReLU-QP 提升 MPC 频率 | 65 Hz → >1300 Hz | [210] |
| 稀疏 NLP 复杂度 | O(N³) → O(N) | 直接配点 |
| π₀ 控制频率 | 50 Hz（双臂+轮式底座） | [375] |
| LLaMA 训练资源 | 992×A100-80B GPU，34 天 | [405] |
| SRBM MPC 典型频率 | 20-300 Hz（QP 求解） | 表 II |
| WBD MPC 典型频率 | 100 Hz（DDP 求解） | [190] |

这些数字表明：学习基方法在计算效率上已具优势，但模型基方法在实时性和鲁棒性上仍占主导；基础模型的高频控制能力（50 Hz）尚不足以支撑全身动态操作。

## 边界与局限

作者明确承认的边界包括：动态环境中的腿臂操作“在很大程度上尚未被探索”；可变形物体建模需简化且集成到人形操作中“相对未被充分探索”；CITO 迁移为实时 CI-MPC 尚未实现；基础模型缺乏缩放定律，且推理延迟和互联网延迟可能妨碍去中心化部署。此外，多数运动模仿工作仅实现保守行为，DeepMimic 中的敏捷技能仍仅存在于仿真；遥操作全身体传感需额外设备（IMU 服、外骨骼），成本高且缺乏用户友好性。论文未明确提及具体硬件配置、数据量或训练配置等复现细节。

## 工程启示

对工程团队的启示：**首先核对接触建模假设**——若任务涉及动态物体（如搬运重箱），必须采用统一机器人-物体模型而非外部力旋量近似；若为静态交互，外部力旋量策略可显著简化。**MPC 选型优先级**：SRBM 适合实时平衡（20-300 Hz），CD 适合多接触规划（5-10 Hz），WBD 仅适合离线或热启动场景（100 Hz）。**最易踩坑处**：加权 QP 的权重调参在高维任务中极易不稳定，建议优先采用层次 QP 或约束 RL 替代；域随机化范围需谨慎平衡——过大导致学习失败，过小导致迁移失败。**数据策略**：遥操作仍是收集人形数据最实用途径，但需注意重定向的动态任务（如行走）对演示者动态模型敏感；从人类视频学习时，应优先选择包含物体运动和多模态观测的数据，而非仅关节姿态。**基础模型部署**：当前不宜直接端到端控制，建议采用云端 FM 高层决策 + 机载 WBC 低层执行的层级架构，并关注 π₀ 式标记化动作表示对高自由度系统的效率问题。

## Overview
Humanoid robots hold great potential to perform various human-level skills, involving unified locomotion and manipulation in real-world settings. Driven by advances in machine learning and the strength of existing model-based approaches, these capabilities have progressed rapidly, but often separately. This survey offers a comprehensive overview of the state-of-the-art in humanoid locomotion and manipulation (HLM), with a focus on control, planning, and learning methods. We first review the model-based methods that have been the backbone of humanoid robotics for the past three decades. We discuss contact planning, motion planning, and whole-body control, highlighting the trade-offs between model fidelity and computational efficiency. Then the focus is shifted to examine emerging learning-based methods, with an emphasis on reinforcement and imitation learning that enhance the robustness and versatility of loco-manipulation skills. Furthermore, we assess the potential of integrating foundation models with humanoid embodiments to enable the development of generalist humanoid agents. This survey also highlights the emerging role of tactile sensing, particularly whole-body tactile feedback, as a crucial modality for handling contact-rich interactions. Finally, we compare the strengths and limitations of model-based and learning-based paradigms from multiple perspectives, such as robustness, computational efficiency, versatility, and generalizability, and suggest potential solutions to existing challenges.

## 参考
- https://arxiv.org/abs/2501.02116

## 개요

본 논문은 휴머노이드 로봇의 전신 운동 및 조작(locomotion-manipulation)에 관한 권위 있는 종설로, 조지아 공과대학교, 서던캘리포니아대학교, Google DeepMind, NVIDIA 등 다수 기관이 공동으로 작성했다. 본 논문은 모델 기반 방법(MPC, WBC, 접촉 계획)과 학습 기반 방법(RL, IL, 기초 모델)의 현황을 체계적으로 정리하고, 두 접근법의 분리가 현재의 핵심 병목임을 지적하며, 인지, 계획, 제어 및 학습을 융합하는 미래 방향을 제시한다.

## 무엇을 바꾸었는가

이 종설이 진정으로 바꾼 것은 "휴머노이드 로봇 전신 조작"이라는 문제의 정의 방식이다. 과거에는 locomotion과 manipulation이 독립된 두 분야로 각각 연구되었고, 모델 기반 방법과 학습 기반 방법이 각자 싸우며 통일된 이론적 프레임워크와 평가 기준이 부재했다. 저자들은 이러한 분리가 모델 기반 방법이 비구조화된 환경과 동적 상호작용을 처리하기 어렵게 만들고, 순수 학습 방법은 높은 자유도, 희소 보상, sim-to-real 격차로 인해 비효율적임을 명확히 지적한다. 더욱 중요하게, 저자들은 "촉각 인지"와 "접촉 추론"을 운동 계획과 동등한 중요도로 격상시키며, 동적 접촉 이해(정적 접촉점 추정이 아닌)가 인지, 계획, 제어를 연결하는 중심축임을 지적한다. 이러한 관점의 전환은 전체 분야를 "궤적 생성"에서 "상호작용 추론"으로 이끌 것이다.

## 방법 분해

### 모델 기반 방법: 계층적 제어 아키텍처
- **MPC-WBC 계층**: 전신 MPC(SRBM, CD 또는 WBD 모델 기반)가 질량 중심 및 말단 실행기 궤적을 생성하고, 하위 WBC는 QP를 풀어 순간 토크 분배를 구현한다. 핵심 공식: WBC 동역학 방정식 M𝒒̈ − Jᵀ𝝀 − Sᵀ𝝉 = −C𝒒̇ − G, 결정 변수 X = [𝒒̈, 𝝀, 𝝉]ᵀ로 문제를 선형화하여 실시간으로 풀 수 있다.
- **접촉 계획의 세 가지 패러다임**: 탐색 기반(상태 확장으로 접촉 모드 탐색, 휴리스틱으로 가속), 최적화 기반(CITO가 접촉 동역학을 궤적 최적화에 포함하고, 평활 최대값 함수로 접촉 충격량 근사), 학습 기반(RL이 접촉 시퀀스 예측, [177]은 0.1초 내 생성으로 최적화 방법보다 300배 빠름).
- **MPC 가속 전략**: 구조 활용(희소 NLP로 복잡도를 O(N³)에서 O(N)으로 감소), 순차 선형화(희소 QP 형성), 온난 시작(이전 반복 해 또는 운동 기억으로 초기화), 샘플링(MPPI가 GPU 병렬 처리 활용). ReLU-QP는 휴머노이드 균형 MPC 주파수를 65 Hz에서 1300 Hz 이상으로 향상시켰다.

### 학습 기반 방법: 데이터와 정책
- **네 가지 데이터 소스**: 정책 실행, 원격 조작, 모션 캡처, 인간 비디오. 로봇 경험 데이터는 형태가 일치하지만 희소하고, 인간 데이터는 풍부하지만 구현 격차(embodiment gap)가 존재하며, 리타게팅(retargeting)으로 해결해야 한다.
- **혼합 패러다임**: 교사-학생(특권 관측으로 교사 훈련, 부분 관측으로 학생 클로닝), IL 사전 훈련 + RL 미세 조정, MPC가 참조 궤적 생성 + RL 운동 모방(궤적 증강).
- **스킬 표현**: MOE(전문가 불균형 문제), VAE/GAN 잠재 공간, Goal-Conditioned Policies, 세계 모델(TD-MPC2가 MPC 방식으로 상상 궤적 계획).
- **기초 모델**: VLA 모델(RT-2, OpenVLA, π₀)이 행동을 토큰화하고, π₀는 50 Hz 고주파 제어를 구현한다. 계층적 프레임워크(LLM/VLM 고수준 의사결정 + 저수준 제어 정책)가 현재 주류 배포 방식이다.

## 핵심 혁신

1. **통합 프레임워크 제안**: 촉각 인지, 접촉 계획, 전신 제어, 모방 학습 및 기초 모델을 처음으로 동일한 분석 프레임워크에 포함시키고, "동적 접촉 추론"이 각 모듈을 연결하는 핵심 축임을 명확히 했다. 이 관점은 기존의 인지, 계획, 제어를 분리한 종설 패러다임을 넘어선다.
2. **"데이터 확장"에 대한 비판적 성찰**: 저자들은 일반화가 단순 데이터량 확장이 아닌, 조작 대상 물체의 운동, 인지적 행동, 다중 모달 관측을 포함함으로써 달성되어야 한다고 주장한다. 이 관점은 "빅데이터 + 대형 모델"이라는 유행하는 서사를 도전하며 데이터 수집 전략에 새로운 방향을 제시한다.
3. **혼합 충실도 모델과 캐스케이드 아키텍처**: 근거리 시야는 전차수 모델, 원거리 시야는 단순화된 모델을 사용하는 캐스케이드 충실도 전략과, 클라우드 FM 고수준 의사결정 + 기내 실시간 제어의 분산 배포 아키텍처를 제안하여 계산 제약이 있는 실시간 시스템에 실현 가능한 경로를 제공한다.

## 실험 및 결과

본 논문은 종설 성격으로 원시 실험 데이터를 보고하지 않지만, 핵심 정량 지표를 요약했다:

| 지표 | 값 | 출처 |
|------|------|------|
| 학습 기반 접촉 시퀀스 생성 시간 | <0.1초 | [177] |
| 학습 기반 접촉 계획 가속비 | 300배 (최적화 방법 대비) | [177] |
| ReLU-QP가 향상시킨 MPC 주파수 | 65 Hz → >1300 Hz | [210] |
| 희소 NLP 복잡도 | O(N³) → O(N) | 직접 배치 |
| π₀ 제어 주파수 | 50 Hz (양팔 + 바퀴형 베이스) | [375] |
| LLaMA 훈련 자원 | 992×A100-80B GPU, 34일 | [405] |
| SRBM MPC 일반 주파수 | 20-300 Hz (QP 해석) | 표 II |
| WBD MPC 일반 주파수 | 100 Hz (DDP 해석) | [190] |

이 수치들은 학습 기반 방법이 계산 효율에서 이미 우위를 점했지만, 모델 기반 방법이 실시간성과 견고성에서 여전히 우세함을 보여준다. 기초 모델의 고주파 제어 능력(50 Hz)은 아직 전신 동적 조작을 지원하기에 부족하다.

## 경계와 한계

저자들이 명시적으로 인정한 경계는 다음과 같다: 동적 환경에서의 다리-팔 조작은 "상당 부분 아직 탐구되지 않음"; 변형 가능한 물체 모델링은 단순화가 필요하며 휴머노이드 조작에 통합하는 것은 "상대적으로 충분히 탐구되지 않음"; CITO를 실시간 CI-MPC로 전환하는 것은 아직 미구현; 기초 모델은 스케일링 법칙이 부족하고, 추론 지연 및 인터넷 지연이 분산 배포를 방해할 수 있음. 또한 대부분의 운동 모방 연구는 보수적 행동만 구현했으며, DeepMimic의 민첩한 스킬은 여전히 시뮬레이션에만 존재한다. 원격 조작 전신 센싱은 추가 장비(IMU 슈트, 외골격)가 필요하고 비용이 높으며 사용자 친화적이지 않다. 논문은 구체적인 하드웨어 구성, 데이터량 또는 훈련 설정 등의 재현 세부 사항을 명시하지 않았다.

## 공학적 시사점

공학 팀에 대한 시사점: **먼저 접촉 모델링 가정을 확인하라** — 작업이 동적 물체(예: 무거운 상자 운반)를 포함한다면 외부 힘 스크류 근사가 아닌 통합 로봇-물체 모델을 반드시 사용해야 한다. 정적 상호작용이라면 외부 힘 스크류 전략으로 크게 단순화할 수 있다. **MPC 선택 우선순위**: SRBM은 실시간 균형(20-300 Hz)에 적합하고, CD는 다중 접촉 계획(5-10 Hz)에 적합하며, WBD는 오프라인 또는 온난 시작 시나리오(100 Hz)에만 적합하다. **가장 함정에 빠지기 쉬운 부분**: 가중 QP의 가중치 튜닝은 고차원 작업에서 극도로 불안정해지기 쉬우므로, 계층적 QP 또는 제약 RL로 대체하는 것을 우선 권장한다. 도메인 무작위화 범위는 신중히 균형을 잡아야 한다 — 너무 크면 학습 실패, 너무 작으면 전이 실패. **데이터 전략**: 원격 조작이 여전히 휴머노이드 데이터 수집의 가장 실용적인 경로이지만, 리타게팅된 동적 작업(예: 보행)은 시연자의 동적 모델에 민감하다는 점에 주의해야 한다. 인간 비디오 학습 시 단순 관절 자세가 아닌 물체 운동과 다중 모달 관측을 포함한 데이터를 우선 선택해야 한다. **기초 모델 배포**: 현재는 직접적인 엔드투엔드 제어가 적합하지 않으며, 클라우드 FM 고수준 의사결정 + 기내 WBC 저수준 실행의 계층적 아키텍처를 권장하고, π₀식 토큰화된 행동 표현이 고자유도 시스템에서의 효율성 문제에 주목해야 한다.
