---
$id: ent_paper_roller_skating_motions_humanoid_robots_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Roller-Skating Motions of Humanoid Robots Based on Adversarial Motion Priors
  zh: Learning Roller-Skating Motions of Humanoid Robots Based on Adversarial Motion Priors
  ko: Learning Roller-Skating Motions of Humanoid Robots Based on Adversarial Motion Priors
summary:
  en: 'Humanoid roller-skating is difficult because the robot must coordinate whole-body balance, rolling contacts, and velocity-dependent
    posture regulation. This paper presents an adversarial motion prior based reinforcement learning framework for two humanoid
    roller-skating gaits: Pump Glide skating and Push Glide skating. The two gait datasets are collected independently through
    motion capture and.'
  zh: 本文提出基于对抗运动先验（AMP）的强化学习框架，在Booster T1人形机器人上实现了两种被动轮滑步态（Pump Glide和Push Glide）的仿真与真实世界可持续滑行。核心贡献在于将AMP扩展到被动轮滚动接触场景，通过切片圆柱轮碰撞模型和步态特定的课程学习，解决了欠驱动动力学下的风格模仿与任务跟踪的耦合问题。
  ko: 'Humanoid roller-skating is difficult because the robot must coordinate whole-body balance, rolling contacts, and velocity-dependent
    posture regulation. This paper presents an adversarial motion prior based reinforcement learning framework for two humanoid
    roller-skating gaits: Pump Glide skating and Push Glide skating. The two gait datasets are collected independently through
    motion capture and.'
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
- roller
- skating
- motions
- humanoid
- robots
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.10815 Learning Roller-Skating Motions of Humanoid Robots Based on Adversarial Motion P
  url: https://arxiv.org/abs/2607.10815
  date: '2026-07-12'
  accessed_at: '2026-08-05'
---

## 概述

本文提出基于对抗运动先验（AMP）的强化学习框架，在Booster T1人形机器人上实现了两种被动轮滑步态（Pump Glide和Push Glide）的仿真与真实世界可持续滑行。核心贡献在于将AMP扩展到被动轮滚动接触场景，通过切片圆柱轮碰撞模型和步态特定的课程学习，解决了欠驱动动力学下的风格模仿与任务跟踪的耦合问题。

## 它改变了什么

被动轮滑行对人形机器人是本质不同的控制问题：平足支撑被滚动接触取代，推进力完全来自腿部运动与轮地摩擦的耦合，系统欠驱动程度显著增加。现有AMP工作多针对足式运动，其风格先验与滚动接触的兼容性未经验证；而传统手工奖励设计又难以捕捉滑行中重心转移、速度相关姿态调节等微妙动力学。本文真正改变的是将"风格模仿"从足式运动范式扩展到"滚动接触+欠驱动推进"范式，并证明AMP的判别器能够学习到与被动轮约束兼容的运动风格，而非简单叠加奖励项。这一转变使得两种不同推进机制的步态（泵式滑行与推式滑行）能在同一框架下系统训练，突破了以往单一运动形式或手工设计的局限。

## 方法拆解

### 系统架构
- **平台**：Booster T1，23个驱动身体自由度，每脚4个被动轮（共8个被动轮自由度），策略50Hz输出21个非轮关节目标位置，由50Hz PD控制器执行
- **轮建模**：切片圆柱碰撞模型，沿轮宽用9个窄圆柱替代（最大半径0.032m），视觉模型保持STL；轮动力学由切向接触力主导：Iω̇ = (r_c × F_t) · a

### 训练框架
- **AMP-PPO**：两种步态共享框架但独立判别器/策略/任务奖励（因推进机制和接触时序不同）
- **AMP状态**：5帧拼接，z_t^m ∈ ℝ³⁰⁰，包含身体关节状态、手/脚关键点位置、根速度
- **判别器**：Wasserstein形式，η=0.4，λ_gp=10；AMP奖励 r_amp = 2.0·(1 + tanh(0.4·D_ψ(z)))
- **总回报**：Pump Glide为0.40·r_amp + 0.60·r_task；Push Glide为0.45·r_amp + 0.55·r_task

### 关键设计决策
- **数据采集**：动作捕捉+GMR重定向，被动轮关节不作为模仿目标，处理后组织为短状态转移样本
- **课程学习**：Push Glide的轮空时间惩罚从1.25降至0.9（0–22000步）抑制早期跳跃；支撑腿切换奖励5000步前保持0.2，后线性增至1.0（至32000步）
- **指令生成**：Pump Glide用12s速度课程（0.2–0.7 m/s）；Push Glide每12s重采样（前向0–2 m/s，偏航率±0.2 rad/s）
- **速度滤波**：v_t^f = 0.9·v_{t−1}^f + 0.1·v_t^yaw，指数跟踪项 φ_exp(e; σ) = exp(−e²/σ²)
- **随机化**：80%环境从参考运动随机帧初始化；观测噪声、轮地摩擦、质量、质心、PD增益、轮关节阻尼均随机化

## 关键创新

1. **切片圆柱轮碰撞模型**：用9个窄圆柱替代全球体碰撞，将轮宽误差从2.77倍降至可接受范围（体积超出48.2%→接近真实），在滚动稳定性与训练成本间取得折中（吞吐量7.13×10³ steps/s）。这是sim-to-real可行性的关键，全球体模型会导致接触几何严重失真。
2. **AMP与被动轮动力学的系统集成**：首次证明AMP判别器能学习与滚动接触、重心转移兼容的风格，且两种步态需独立判别器——这验证了推进机制差异对风格先验的根本影响，而非简单调参可解决。
3. **步态特定的课程学习**：针对Push Glide的轮空时间惩罚衰减和支撑腿切换奖励渐进增强，有效抑制了早期"跳跃"伪策略，这是被动轮场景特有的训练稳定性问题。

## 实验与结果

### Pump Glide速度扫描（64次评估/指令）
| 指令 (m/s) | 完成率 | 平均持续时间 (s) | 躯干倾斜RMS (rad) |
|-----------|--------|-----------------|------------------|
| 0.10–0.45 | 0.766–0.813 | 15.88–16.25 | 0.104–0.196 |
| 0.50 | 0.531 | - | - |

最大行驶距离14.55m，偏航率误差<0.184 rad/s；100s长时程剖面总距离39.50m，躯干倾斜RMS 0.132 rad。

### Push Glide前向速度响应（MuJoCo，稳定窗口8s起）
| 指令 (m/s) | 实际v_x^f (m/s) | 误差e_v (m/s) | 时间 (s) |
|-----------|----------------|--------------|---------|
| 0.10 | 0.366±0.015 | 0.266 | 20.00 |
| 0.20 | 0.558±0.028 | 0.358 | 20.00 |
| 0.30 | 0.746±0.030 | 0.446 | 20.00 |
| 0.40 | 1.069±0.043 | 0.669 | 20.00 |
| 0.50 | 1.594±0.109 | 1.094 | 20.00 |

所有指令均维持20s，实际速度单调增加但始终高于指令值，误差随指令增大而增大。

### 轮模型对比
全球体碰撞宽度64mm为真实轮宽23.13mm的2.77倍，体积超出48.2%，最低点离开真实轮宽阈值ϕ_edge≈21.2°；9切片方案在滚动稳定性、几何保真度与训练成本间最优。

## 边界与局限

- **评估局限**：当前为任务级评估，缺乏标准化滑行质量基准；横向速度和偏航率指令未在实验中验证（仅前向速度指令）
- **模型近似**：切片圆柱仍是真实轮地接触的近似，支撑高度不连续虽小，但近似模型、部署模型与真实接触的不匹配可能导致速度跟踪误差
- **未做之事**：更精确的轮接触建模、系统辨识、闭环速度控制均留作未来工作；未提及具体GPU型号、演示数据量、训练步数（除课程学习中的22000/32000步）
- **速度跟踪**：Push Glide实际速度系统性高于指令（误差0.266–1.094 m/s），作者未给出补偿机制

## 工程启示

- **先核对轮碰撞模型**：全球体碰撞在被动轮场景不可用，切片数选择需权衡——9切片吞吐量7.13×10³ steps/s，若训练资源紧张可考虑减少切片但需验证滚动稳定性
- **AMP权重敏感**：Pump Glide的AMP权重0.40与Push Glide的0.45差异显著，复现时需按步态单独调参，不可直接迁移
- **课程学习是关键**：Push Glide的轮空时间惩罚衰减（1.25→0.9）和支撑腿切换奖励渐进增强（0.2→1.0）是抑制跳跃伪策略的核心，跳过此步骤可能导致训练失败
- **速度误差预期**：Push Glide实际速度高于指令是系统性的（非随机噪声），下游任务若需精确速度控制需额外设计补偿或闭环
- **数据管线**：GMR重定向后需严格过滤地面穿透/自碰撞/关节突变片段，被动轮关节不作为模仿目标——这是AMP在欠驱动系统应用的关键细节
- **最易踩坑**：80%环境从参考运动随机帧初始化，若比例不当可能导致策略过度依赖初始状态；观测噪声与轮地摩擦随机化范围需与真实平台匹配，否则sim-to-real gap会放大速度跟踪误差

## Overview
Humanoid roller-skating is difficult because the robot must coordinate whole-body balance, rolling contacts, and velocity-dependent posture regulation. This paper presents an adversarial motion prior based reinforcement learning framework for two humanoid roller-skating gaits: Pump Glide skating and Push Glide skating. The two gait datasets are collected independently through motion capture and retargeted to the humanoid robot separately. The retargeted data are then smoothed and resampled into reference motion states for AMP training. The two gaits are learned by independent AMP training pipelines with separate reference datasets, separate policies, and independent reward architectures. Simulation experiments are designed to evaluate gait quality, velocity tracking, turning, and gait-specific reward ablations.

## 参考
- https://arxiv.org/abs/2607.10815

## 개요

본 논문은 적대적 운동 사전(AMP) 기반 강화 학습 프레임워크를 제안하여, Booster T1 휴머노이드 로봇에서 두 가지 수동 바퀴 활강 보행(Pump Glide 및 Push Glide)의 시뮬레이션 및 실제 환경 지속 활강을 구현한다. 핵심 기여는 AMP를 수동 바퀴 구름 접촉 시나리오로 확장하고, 슬라이스 실린더 바퀴 충돌 모델과 보행 특정 커리큘럼 학습을 통해 저추진 동역학에서의 스타일 모방과 작업 추적의 결합 문제를 해결한 것이다.

## 무엇을 바꾸었는가

수동 바퀴 활강은 휴머노이드 로봇에게 본질적으로 다른 제어 문제이다: 평평한 발 지지가 구름 접촉으로 대체되고, 추진력은 전적으로 다리 운동과 바퀴-지면 마찰의 결합에서 발생하며, 시스템의 저추진 정도가 크게 증가한다. 기존 AMP 연구는 주로 보행 운동을 대상으로 하여, 스타일 사전과 구름 접촉의 호환성이 검증되지 않았다; 반면 전통적인 수동 보상 설계는 활강 중 무게 중심 이동, 속도 관련 자세 조절과 같은 미묘한 동역학을 포착하기 어렵다. 본 논문이 실제로 바꾼 것은 "스타일 모방"을 보행 운동 패러다임에서 "구름 접촉 + 저추진 추진" 패러다임으로 확장하고, AMP의 판별기가 수동 바퀴 제약과 호환되는 운동 스타일을 학습할 수 있음을 증명한 것이다—단순히 보상 항목을 추가하는 것이 아니다. 이러한 전환은 두 가지 서로 다른 추진 메커니즘의 보행(펌프 활강과 푸시 활강)이 동일한 프레임워크에서 체계적으로 훈련될 수 있게 하여, 기존의 단일 운동 형태 또는 수동 설계의 한계를 돌파했다.

## 방법 분석

### 시스템 아키텍처
- **플랫폼**: Booster T1, 23개의 구동 신체 자유도, 각 발에 4개의 수동 바퀴(총 8개의 수동 바퀴 자유도), 정책은 50Hz로 21개의 비바퀴 관절 목표 위치를 출력하며, 50Hz PD 컨트롤러가 실행
- **바퀴 모델링**: 슬라이스 실린더 충돌 모델, 바퀴 폭을 따라 9개의 좁은 실린더로 대체(최대 반경 0.032m), 시각 모델은 STL 유지; 바퀴 동역학은 접선 접촉력이 지배: Iω̇ = (r_c × F_t) · a

### 훈련 프레임워크
- **AMP-PPO**: 두 보행이 프레임워크를 공유하지만 판별기/정책/작업 보상은 독립적(추진 메커니즘과 접촉 타이밍이 다르기 때문)
- **AMP 상태**: 5프레임 연결, z_t^m ∈ ℝ³⁰⁰, 신체 관절 상태, 손/발 키포인트 위치, 루트 속도 포함
- **판별기**: Wasserstein 형태, η=0.4, λ_gp=10; AMP 보상 r_amp = 2.0·(1 + tanh(0.4·D_ψ(z)))
- **총 보상**: Pump Glide는 0.40·r_amp + 0.60·r_task; Push Glide는 0.45·r_amp + 0.55·r_task

### 핵심 설계 결정
- **데이터 수집**: 모션 캡처 + GMR 리타게팅, 수동 바퀴 관절은 모방 대상이 아니며, 처리 후 짧은 상태 전이 샘플로 구성
- **커리큘럼 학습**: Push Glide의 바퀴 공중 시간 페널티를 1.25에서 0.9로 감소(0–22000스텝)하여 초기 점프 억제; 지지 다리 전환 보상은 5000스텝 전까지 0.2 유지, 이후 선형적으로 1.0까지 증가(32000스텝까지)
- **명령 생성**: Pump Glide는 12초 속도 커리큘럼(0.2–0.7 m/s); Push Glide는 12초마다 재샘플링(전방 0–2 m/s, 요 레이트 ±0.2 rad/s)
- **속도 필터링**: v_t^f = 0.9·v_{t−1}^f + 0.1·v_t^yaw, 지수 추적 항 φ_exp(e; σ) = exp(−e²/σ²)
- **무작위화**: 80% 환경이 참조 운동의 무작위 프레임에서 초기화; 관측 노이즈, 바퀴-지면 마찰, 질량, 무게 중심, PD 게인, 바퀴 관절 댐핑 모두 무작위화

## 핵심 혁신

1. **슬라이스 실린더 바퀴 충돌 모델**: 전역 볼륨 충돌을 9개의 좁은 실린더로 대체하여 바퀴 폭 오차를 2.77배에서 허용 가능한 범위로 감소(부피 초과 48.2%→실제에 근접), 구름 안정성과 훈련 비용 사이의 절충 달성(처리량 7.13×10³ steps/s). 이는 sim-to-real 실현 가능성의 핵심으로, 전역 볼륨 모델은 접촉 기하학의 심각한 왜곡을 초래한다.
2. **AMP와 수동 바퀴 동역학의 체계적 통합**: AMP 판별기가 구름 접촉, 무게 중심 이동과 호환되는 스타일을 학습할 수 있음을 처음으로 증명했으며, 두 보행은 독립적인 판별기가 필요함—이는 추진 메커니즘 차이가 스타일 사전에 근본적 영향을 미친다는 것을 검증한 것으로, 단순한 파라미터 조정으로 해결할 수 없다.
3. **보행 특정 커리큘럼 학습**: Push Glide의 바퀴 공중 시간 페널티 감쇠와 지지 다리 전환 보상 점진적 강화를 통해 초기 "점프" 의사 정책을 효과적으로 억제하며, 이는 수동 바퀴 시나리오 특유의 훈련 안정성 문제이다.

## 실험 및 결과

### Pump Glide 속도 스캔(명령당 64회 평가)
| 명령 (m/s) | 완료율 | 평균 지속 시간 (s) | 몸통 기울기 RMS (rad) |
|-----------|--------|-----------------|------------------|
| 0.10–0.45 | 0.766–0.813 | 15.88–16.25 | 0.104–0.196 |
| 0.50 | 0.531 | - | - |

최대 주행 거리 14.55m, 요 레이트 오차 <0.184 rad/s; 100초 장시간 프로파일 총 거리 39.50m, 몸통 기울기 RMS 0.132 rad.

### Push Glide 전방 속도 응답(MuJoCo, 안정 창 8초부터)
| 명령 (m/s) | 실제 v_x^f (m/s) | 오차 e_v (m/s) | 시간 (s) |
|-----------|----------------|--------------|---------|
| 0.10 | 0.366±0.015 | 0.266 | 20.00 |
| 0.20 | 0.558±0.028 | 0.358 | 20.00 |
| 0.30 | 0.746±0.030 | 0.446 | 20.00 |
| 0.40 | 1.069±0.043 | 0.669 | 20.00 |
| 0.50 | 1.594±0.109 | 1.094 | 20.00 |

모든 명령이 20초 동안 유지되며, 실제 속도는 단조 증가하지만 항상 명령 값보다 높고, 오차는 명령이 증가함에 따라 커진다.

### 바퀴 모델 비교
전역 볼륨 충돌 폭 64mm는 실제 바퀴 폭 23.13mm의 2.77배, 부피 초과 48.2%, 최저점이 실제 바퀴 폭 임계값 ϕ_edge≈21.2°를 벗어남; 9슬라이스 방식은 구름 안정성, 기하학적 충실도, 훈련 비용 사이에서 최적이다.

## 경계 및 한계

- **평가 한계**: 현재는 작업 수준 평가로, 표준화된 활강 품질 벤치마크가 부족; 횡방향 속도 및 요 레이트 명령은 실험에서 검증되지 않음(전방 속도 명령만)
- **모델 근사**: 슬라이스 실린더는 여전히 실제 바퀴-지면 접촉의 근사이며, 지지 높이 불연속성은 작지만 근사 모델, 배포 모델, 실제 접촉 간의 불일치가 속도 추적 오차를 초래할 수 있음
- **수행하지 않은 것**: 더 정밀한 바퀴 접촉 모델링, 시스템 식별, 폐루프 속도 제어는 모두 향후 작업으로 남김; 구체적인 GPU 모델, 데모 데이터 양, 훈련 스텝 수(커리큘럼 학습의 22000/32000스텝 제외)는 언급되지 않음
- **속도 추적**: Push Glide의 실제 속도는 체계적으로 명령보다 높음(오차 0.266–1.094 m/s), 저자는 보상 메커니즘을 제시하지 않음

## 공학적 시사점

- **먼저 바퀴 충돌 모델 확인**: 전역 볼륨 충돌은 수동 바퀴 시나리오에서 사용 불가, 슬라이스 수 선택은 절충 필요—9슬라이스 처리량 7.13×10³ steps/s, 훈련 자원이 부족하면 슬라이스 수를 줄일 수 있지만 구름 안정성 검증 필요
- **AMP 가중치 민감성**: Pump Glide의 AMP 가중치 0.40과 Push Glide의 0.45 차이가 유의미하므로, 재현 시 보행별로 별도 파라미터 조정 필요, 직접 전이 불가
- **커리큘럼 학습이 핵심**: Push Glide의 바퀴 공중 시간 페널티 감쇠(1.25→0.9)와 지지 다리 전환 보상 점진적 강화(0.2→1.0)는 점프 의사 정책 억제의 핵심이며, 이 단계를 건너뛰면 훈련 실패 가능
- **속도 오차 예상**: Push Glide의 실제 속도가 명령보다 높은 것은 체계적(무작위 노이즈 아님), 하위 작업에서 정밀한 속도 제어가 필요하면 추가 보상 또는 폐루프 설계 필요
- **데이터 파이프라인**: GMR 리타게팅 후 지면 관통/자체 충돌/관절 급변 구간을 엄격히 필터링해야 하며, 수동 바퀴 관절은 모방 대상이 아님—이는 AMP를 저추진 시스템에 적용하는 핵심 세부 사항
- **가장 쉽게 빠지는 함정**: 80% 환경이 참조 운동의 무작위 프레임에서 초기화되는데, 비율이 부적절하면 정책이 초기 상태에 과도하게 의존할 수 있음; 관측 노이즈와 바퀴-지면 마찰 무작위화 범위는 실제 플랫폼과 일치해야 하며, 그렇지 않으면 sim-to-real 격차가 속도 추적 오차를 증폭시킬 수 있음
