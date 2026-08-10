---
$id: ent_paper_robot_parkour_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Parkour Learning
  zh: Robot Parkour Learning
  ko: Robot Parkour Learning
summary:
  en: Parkour is a grand challenge for legged locomotion that requires robots to overcome various obstacles rapidly in complex
    environments. Existing methods can generate either diverse but blind locomotion skills or vision-based but specialized
    skills by using reference animal data or complex rewards. However, autonomous parkour requires robots to learn generalizable
    skills that are both vision-based.
  zh: 本文提出一种两阶段强化学习框架，在低成本四足机器人（Unitree A1/Go1）上实现端到端、视觉驱动的单一跑酷策略，涵盖攀爬、跳跃、爬行、侧身和奔跑五种技能。核心贡献在于通过软动力学约束的预训练与硬动力学微调，结合DAgger蒸馏，使机器人仅凭机载深度相机即可在仿真和真实世界中完成高难度障碍穿越。
  ko: Parkour is a grand challenge for legged locomotion that requires robots to overcome various obstacles rapidly in complex
    environments. Existing methods can generate either diverse but blind locomotion skills or vision-based but specialized
    skills by using reference animal data or complex rewards. However, autonomous parkour requires robots to learn generalizable
    skills that are both vision-based.
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
- robot
- parkour
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P130. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2309.05665 Robot Parkour Learning
  url: https://arxiv.org/abs/2309.05665
  date: '2023-09-11'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种两阶段强化学习框架，在低成本四足机器人（Unitree A1/Go1）上实现端到端、视觉驱动的单一跑酷策略，涵盖攀爬、跳跃、爬行、侧身和奔跑五种技能。核心贡献在于通过软动力学约束的预训练与硬动力学微调，结合DAgger蒸馏，使机器人仅凭机载深度相机即可在仿真和真实世界中完成高难度障碍穿越。

## 它改变了什么

足式机器人敏捷运动长期受困于“多样性”与“视觉闭环”的割裂：基于参考运动的方法能生成丰富动作但缺乏环境感知，而视觉策略往往针对单一技能且依赖昂贵硬件或复杂奖励工程。本文改变了这一局面——它证明一个单一策略、仅用低成本硬件和简单奖励，就能同时掌握五种差异极大的跑酷技能，且无需任何动物运动数据或任务特定奖励塑形。这实质上是将“跑酷”从精心设计的专用控制器问题，重新定义为可扩展的通用强化学习问题，为足式机器人在非结构化环境中的自主导航提供了新的可行性基线。

## 方法拆解

### 两阶段训练范式
1. **RL预训练（软动力学）**：允许机器人身体穿透障碍物，奖励函数仅含三项：
   - `r_forward = -α1|v_x - v_x_target| - α2|v_y|² + α3·e^{-|ω_yaw|}`
   - `r_energy = -α4·Σ|τ_j·q̇_j|²`
   - `r_alive = 2`
   另加穿透惩罚 `r_penetrate = -Σ_p(α5·𝟙[p] + α6·d(p))·v_x`，其中`d(p)`为穿透深度，乘以`v_x`防止机器人利用穿透快速冲关。
2. **RL微调（硬动力学）**：移除穿透奖励，在真实碰撞约束下优化预训练策略，仅用`r_skill`。

### 自动课程与技能策略
- 障碍难度由分数`s∈[0,1]`（步长0.05）控制，属性线性插值：`l = (1-s)·l_easy + s·l_hard`，根据穿透奖励自动调整`s`。
- 训练五个专用GRU策略（`π_climb`, `π_leap`, `π_crawl`, `π_tilt`, `π_run`），输入为本体感觉（ℝ²⁹）、上一动作（ℝ¹²）及特权信息（障碍距离/高度/宽度/4维one-hot类别、地形摩擦、质心、电机强度）。

### 蒸馏与部署
- 用DAgger将五个专用策略蒸馏为单一视觉策略`π_parkour`，输入含深度图像潜在嵌入（小型CNN，通道[16,32,32]，核[5,4,3]），蒸馏损失为二元交叉熵。
- 深度图分辨率48×64，刷新率10Hz，异步获取嵌入；策略运行50Hz，输出目标关节位置经PD控制器（Kp=50, Kd=1）转为扭矩，限幅25Nm。

## 关键创新

1. **软动力学穿透训练**：允许预训练阶段穿透障碍物，配合自动课程，解决了稀疏奖励下探索困难的问题。这是唯一能让攀爬和跳跃技能从零学起的方法（对比RND和硬动力学基线均失败）。
2. **简单奖励+特权蒸馏**：仅用三项通用奖励（速度、能量、存活）即可训练五种技能，再通过DAgger将特权信息蒸馏为纯视觉策略，避免了复杂的奖励整形和任务特定设计。
3. **低成本硬件闭环**：在A1/Go1上仅用机载Jetson NX和RealSense D435实现50Hz闭环控制，无需外部动捕或昂贵计算平台，显著降低了敏捷机器人的部署门槛。

## 实验与结果

### 仿真对比（表2，最大距离3.6m，成功率%）
| 方法 | Climb | Leap | Crawl | Tilt | Run |
|------|-------|------|-------|------|-----|
| Blind | 0 | 0 | 13 | 0 | 100 |
| MLP | 0 | 1 | 63 | 43 | 100 |
| No Distill | 0 | 0 | 73 | 0 | 100 |
| RMA | - | - | - | 74 | - |
| **Ours** | **86** | **80** | **100** | **73** | **100** |
| Oracles w/o Soft Dyn | 0 | 0 | 93 | 86 | 100 |
| Oracles | 95 | 82 | 100 | 100 | 100 |

### 真实世界（A1，10次试验）
| 任务 | 尺寸 | 成功率 |
|------|------|--------|
| 攀爬 | 0.40m（1.53倍身高） | 80% |
| 跳跃 | 0.60m（1.5倍身长） | 80% |
| 爬行 | 0.2m（0.76倍身高） | 90% |
| 侧身 | 0.28m（小于身宽） | 通过 |

关键结论：软动力学预训练是攀爬/跳跃成功的必要条件（Oracles w/o Soft Dyn成功率为0）；蒸馏后的视觉策略性能接近特权专家（Oracles），且显著优于无视觉基线。

## 边界与局限

- **环境构建依赖人工**：模拟环境需手动搭建，新技能需新增障碍物类型和外观，自动化程度低，限制了技能扩展速度。
- **视觉模态单一**：仅使用深度图像，未利用RGB语义信息，对透明/反光/低纹理障碍可能失效。
- **障碍物范围有限**：测试尺寸均小于2倍机器人尺度，未验证更大尺度或动态障碍物场景。
- **论文未明确**：策略对地形坡度、软地面、非刚性障碍的泛化能力；长时间运行下的漂移与磨损影响。

## 工程启示

- **复现优先核对**：奖励系数α1-α6（如Climb的α5=1e-2, α6=1e-2）和课程步长0.05对训练稳定性至关重要，建议先复现单技能再扩展多技能。
- **易踩坑点**：深度图像延迟随机化（[0.2, 0.26]s）和相机位姿扰动（位置±0.01m，俯仰[0,5]°）是sim-to-real成功的关键，不可省略；PD增益Kp=50, Kd=1需严格匹配，否则扭矩限幅25Nm会导致动作失真。
- **下游团队建议**：若需部署到新平台，优先调整动作缩放常数（髋0.4，膝0.6）和电机强度采样范围[0.9, 1.1]；蒸馏阶段需保证4台3090的NFS同步，否则策略更新滞后会导致蒸馏发散。
- **计算资源**：单技能预训练12小时+微调6小时（1×3090），蒸馏需4×3090并行，预算有限时建议先验证软动力学收益再投入全流程。

## Overview
Parkour is a grand challenge for legged locomotion that requires robots to overcome various obstacles rapidly in complex environments. Existing methods can generate either diverse but blind locomotion skills or vision-based but specialized skills by using reference animal data or complex rewards. However, autonomous parkour requires robots to learn generalizable skills that are both vision-based and diverse to perceive and react to various scenarios. In this work, we propose a system for learning a single end-to-end vision-based parkour policy of diverse parkour skills using a simple reward without any reference motion data. We develop a reinforcement learning method inspired by direct collocation to generate parkour skills, including climbing over high obstacles, leaping over large gaps, crawling beneath low barriers, squeezing through thin slits, and running. We distill these skills into a single vision-based parkour policy and transfer it to a quadrupedal robot using its egocentric depth camera. We demonstrate that our system can empower two different low-cost robots to autonomously select and execute appropriate parkour skills to traverse challenging real-world environments.

## 参考
- https://arxiv.org/abs/2309.05665

## 개요

본 논문은 저비용 사족 로봇(Unitree A1/Go1)에서 등반, 점프, 기어가기, 옆으로 이동, 달리기의 다섯 가지 기술을 포괄하는 엔드투엔드, 비전 기반 단일 파쿠르 정책을 구현하는 2단계 강화 학습 프레임워크를 제안한다. 핵심 기여는 소프트 동역학 제약을 통한 사전 학습과 하드 동역학 미세 조정, 그리고 DAgger 증류를 결합하여 로봇이 온보드 깊이 카메라만으로 시뮬레이션과 실제 세계에서 고난도 장애물 통과를 수행할 수 있게 한 점이다.

## 무엇이 바뀌었는가

족식 로봇의 민첩한 운동은 오랫동안 "다양성"과 "시각적 폐루프"의 분리 문제에 직면해 왔다. 참조 운동 기반 방법은 풍부한 동작을 생성할 수 있지만 환경 인식이 부족하고, 시각 정책은 종종 단일 기술에 국한되며 고가의 하드웨어나 복잡한 보상 엔지니어링에 의존한다. 본 논문은 이러한 상황을 바꾼다. 단일 정책, 저비용 하드웨어, 단순한 보상만으로도 동물 운동 데이터나 작업별 보상 설계 없이도 다섯 가지 매우 다른 파쿠르 기술을 동시에 습득할 수 있음을 증명한다. 이는 본질적으로 "파쿠르"를 정교하게 설계된 전용 컨트롤러 문제에서 확장 가능한 범용 강화 학습 문제로 재정의하며, 비구조화된 환경에서 족식 로봇의 자율 탐색을 위한 새로운 실현 가능성 기준을 제시한다.

## 방법 분석

### 2단계 훈련 패러다임
1. **RL 사전 학습(소프트 동역학)**: 로봇의 몸체가 장애물을 통과할 수 있도록 허용하며, 보상 함수는 세 가지 항만 포함한다:
   - `r_forward = -α1|v_x - v_x_target| - α2|v_y|² + α3·e^{-|ω_yaw|}`
   - `r_energy = -α4·Σ|τ_j·q̇_j|²`
   - `r_alive = 2`
   추가로 관통 패널티 `r_penetrate = -Σ_p(α5·𝟙[p] + α6·d(p))·v_x`를 포함하며, 여기서 `d(p)`는 관통 깊이이고 `v_x`를 곱해 로봇이 관통을 이용해 빠르게 통과하는 것을 방지한다.
2. **RL 미세 조정(하드 동역학)**: 관통 보상을 제거하고 실제 충돌 제약 하에서 사전 학습된 정책을 `r_skill`만으로 최적화한다.

### 자동 커리큘럼 및 기술 정책
- 장애물 난이도는 점수 `s∈[0,1]`(간격 0.05)로 제어되며, 속성은 선형 보간된다: `l = (1-s)·l_easy + s·l_hard`, 관통 보상에 따라 `s`가 자동 조정된다.
- 다섯 개의 전용 GRU 정책(`π_climb`, `π_leap`, `π_crawl`, `π_tilt`, `π_run`)을 훈련하며, 입력은 고유 감각(ℝ²⁹), 이전 동작(ℝ¹²) 및 특권 정보(장애물 거리/높이/너비/4차원 원-핫 범주, 지면 마찰, 질량 중심, 모터 강도)이다.

### 증류 및 배포
- DAgger를 사용하여 다섯 개의 전용 정책을 단일 시각 정책 `π_parkour`로 증류하며, 입력에는 깊이 이미지 잠재 임베딩(소형 CNN, 채널 [16,32,32], 커널 [5,4,3])이 포함되고 증류 손실은 이진 교차 엔트로피이다.
- 깊이 맵 해상도 48×64, 갱신 주파수 10Hz, 임베딩은 비동기적으로 획득된다. 정책은 50Hz로 실행되며, 출력 목표 관절 위치는 PD 컨트롤러(Kp=50, Kd=1)를 통해 토크로 변환되고 25Nm로 제한된다.

## 핵심 혁신

1. **소프트 동역학 관통 훈련**: 사전 학습 단계에서 장애물 관통을 허용하고 자동 커리큘럼을 결합하여 희소 보상 하에서 탐색의 어려움을 해결한다. 이는 등반과 점프 기술을 처음부터 학습할 수 있는 유일한 방법이다(RND 및 하드 동역학 기준선은 모두 실패).
2. **단순 보상 + 특권 증류**: 세 가지 일반 보상(속도, 에너지, 생존)만으로 다섯 가지 기술을 훈련한 다음 DAgger를 통해 특권 정보를 순수 시각 정책으로 증류하여 복잡한 보상 설계와 작업별 설계를 피한다.
3. **저비용 하드웨어 폐루프**: A1/Go1에서 온보드 Jetson NX와 RealSense D435만으로 50Hz 폐루프 제어를 구현하며, 외부 모션 캡처나 고가의 컴퓨팅 플랫폼 없이도 민첩한 로봇의 배포 장벽을 크게 낮춘다.

## 실험 및 결과

### 시뮬레이션 비교(표 2, 최대 거리 3.6m, 성공률 %)
| 방법 | Climb | Leap | Crawl | Tilt | Run |
|------|-------|------|-------|------|-----|
| Blind | 0 | 0 | 13 | 0 | 100 |
| MLP | 0 | 1 | 63 | 43 | 100 |
| No Distill | 0 | 0 | 73 | 0 | 100 |
| RMA | - | - | - | 74 | - |
| **Ours** | **86** | **80** | **100** | **73** | **100** |
| Oracles w/o Soft Dyn | 0 | 0 | 93 | 86 | 100 |
| Oracles | 95 | 82 | 100 | 100 | 100 |

### 실제 세계(A1, 10회 시도)
| 작업 | 크기 | 성공률 |
|------|------|--------|
| 등반 | 0.40m(신장의 1.53배) | 80% |
| 점프 | 0.60m(몸길이의 1.5배) | 80% |
| 기어가기 | 0.2m(신장의 0.76배) | 90% |
| 옆으로 이동 | 0.28m(몸폭보다 작음) | 통과 |

핵심 결론: 소프트 동역학 사전 학습은 등반/점프 성공의 필수 조건이다(Oracles w/o Soft Dyn 성공률 0). 증류된 시각 정책의 성능은 특권 전문가(Oracles)에 근접하며, 시각 없는 기준선보다 크게 우수하다.

## 경계 및 한계

- **환경 구축의 수동 의존성**: 시뮬레이션 환경은 수동으로 구축해야 하며, 새로운 기술에는 새로운 장애물 유형과 외관이 필요하므로 자동화 수준이 낮아 기술 확장 속도가 제한된다.
- **시각 양식 단일성**: 깊이 이미지만 사용하고 RGB 의미 정보를 활용하지 않으므로 투명/반사/저질감 장애물에는 실패할 수 있다.
- **장애물 범위 제한**: 테스트 크기는 모두 로봇 스케일의 2배 미만이며, 더 큰 스케일이나 동적 장애물 시나리오는 검증되지 않았다.
- **논문에서 명확하지 않음**: 지면 경사, 연약한 지면, 비강성 장애물에 대한 정책의 일반화 능력, 장시간 운영 시 드리프트 및 마모 영향.

## 엔지니어링 시사점

- **재현 시 우선 확인 사항**: 보상 계수 α1-α6(예: Climb의 α5=1e-2, α6=1e-2)와 커리큘럼 간격 0.05는 훈련 안정성에 중요하므로, 단일 기술 재현 후 다중 기술로 확장하는 것을 권장한다.
- **쉽게 빠지는 함정**: 깊이 이미지 지연 무작위화([0.2, 0.26]s)와 카메라 자세 섭동(위치 ±0.01m, 피치 [0,5]°)은 sim-to-real 성공의 핵심이므로 생략할 수 없다. PD 게인 Kp=50, Kd=1은 엄격히 일치해야 하며, 그렇지 않으면 토크 제한 25Nm로 인해 동작이 왜곡된다.
- **하류 팀 권장 사항**: 새 플랫폼에 배포할 경우 동작 스케일링 상수(엉덩이 0.4, 무릎 0.6)와 모터 강도 샘플링 범위 [0.9, 1.1]을 우선 조정하라. 증류 단계에서는 4대의 3090 NFS 동기화가 필요하며, 그렇지 않으면 정책 업데이트 지연으로 증류가 발산할 수 있다.
- **계산 자원**: 단일 기술 사전 학습 12시간 + 미세 조정 6시간(1×3090), 증류는 4×3090 병렬이 필요하므로, 예산이 제한된 경우 먼저 소프트 동역학의 이점을 검증한 후 전체 프로세스에 투자하는 것을 권장한다.
