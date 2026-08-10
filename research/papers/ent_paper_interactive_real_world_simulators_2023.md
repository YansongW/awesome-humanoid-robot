---
$id: ent_paper_interactive_real_world_simulators_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Interactive Real-World Simulators
  zh: Learning Interactive Real-World Simulators
  ko: Learning Interactive Real-World Simulators
summary:
  en: Generative models trained on internet data have revolutionized how text, image, and video content can be created. Perhaps
    the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots,
    and other interactive agents. Applications of a real-world simulator range from controllable content creation in games
    and movies, to training embodied.
  zh: 本文提出 UniSim，一个 5.6B 参数的通用真实世界模拟器，将视频生成建模为动力学问题，通过统一动作-视频接口整合互联网图像、人类活动、机器人操作等多源数据。核心贡献在于证明大规模条件视频生成模型可作为交互式环境，用于训练长时程
    VLM 策略和 RL 策略，并显著提升下游任务性能。
  ko: Generative models trained on internet data have revolutionized how text, image, and video content can be created. Perhaps
    the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots,
    and other interactive agents. Applications of a real-world simulator range from controllable content creation in games
    and movies, to training embodied.
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
- interactive
- real
- world
- simulators
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P066. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2310.06114 Learning Interactive Real-World Simulators
  url: https://arxiv.org/abs/2310.06114
  date: '2023-10-09'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 UniSim，一个 5.6B 参数的通用真实世界模拟器，将视频生成建模为动力学问题，通过统一动作-视频接口整合互联网图像、人类活动、机器人操作等多源数据。核心贡献在于证明大规模条件视频生成模型可作为交互式环境，用于训练长时程 VLM 策略和 RL 策略，并显著提升下游任务性能。

## 它改变了什么

生成模型的下一个里程碑不是生成更逼真的静态媒体，而是模拟真实世界体验以响应交互智能体的动作。现有世界模型要么在低维状态空间或游戏域中学习单一系统动力学，要么缺乏对生成视频的控制能力，无法作为通用环境训练具身智能体。策略学习的主要瓶颈在于对真实世界环境的有限访问，而 UniSim 试图提供现实且无限的环境访问。

真正改变的是将“视频生成”从内容创作工具重新定位为“动力学建模”工具。作者没有为每个任务训练专用模拟器，而是构建一个跨任务保持不变的通用模拟器，可与任何单独学习的奖励函数结合。这意味着下游策略学习可以完全在仿真中进行，并直接部署到真实世界，绕开真实环境采样的瓶颈。

## 方法拆解

### 统一动作空间
- 文本令牌经 T5 语言模型嵌入转换为连续表示
- 低层控制动作（如机器人关节运动）归一化后离散化为 4096 个 bin，与语言嵌入拼接
- 数据集标识符可附加于动作，但仅在测试域在训练域分布内时使用

### 数据集编排
- **模拟执行**：Habitat 对象导航（HM3D，710 示例）和 Language Table sim（160k 示例）
- **真实机器人**：Bridge Data（2k）、RT-1/RT-2（70k）、Language Table real（440k）
- **人类活动**：Ego4D（3.5M）、EPIC-KITCHENS（25k）、Something-Something V2（160k）
- **全景扫描**：Matterport3D（3.5M），通过截断全景扫描构造“左转”等动作
- **互联网数据**：LAION-400M 和 ALIGN 各 400M，单张图像视为单帧视频

### 观测预测模型
学习模型 p(o_t|h_{t-1}, a_{t-1})，其中 h_{t-1} 为历史帧集合，a_{t-1} 为时间扩展动作。关键设计决策是仅用最近交互的有限帧（如 4 帧）作为条件，而非条件化所有过去信息，大幅简化建模问题。

### 扩散模型参数化
- 去噪模型 ε_θ(o_t^(k), k|h_{t-1}, a_{t-1})，通过 K 步去噪生成下一观测
- 训练损失为 MSE：L_MSE = ||ε - ε_θ(√(1-β^(k))o_t + √(β^(k))ε, k|h_{t-1}, a_{t-1})||²
- 采样过程：o_t^(k-1) = α^(k)(o_t^(k) - γ^(k)ε_θ(o_t^(k), k|h_{t-1}, a_{t-1})) + ξ
- 动作条件化采用无分类器引导：ε_θ = (1+η)ε_θ(·|h, a) - ηε_θ(·|h)

### 架构
视频 U-Net，交错时间和空间注意力及卷积层。基础模型在 [16, 24, 40] 分辨率运行，两个超分辨率模型分别提升至 [48, 80] 和 [192, 320]。历史条件帧复制到所有未来帧索引，与噪声样本拼接。

## 关键创新

1. **统一动作-视频接口**：将文本、低层控制、图像字幕统一为动作空间，使同一模拟器可响应不同模态的交互。这是首个将互联网规模数据（LAION、ALIGN 各 400M）与机器人、人类活动数据联合训练的视频生成模拟器。

2. **仅条件化最近帧的设计**：发现仅用 4 帧历史即可有效建模，而非条件化所有过去信息。这一简化使长时程自回归滚动成为可能，且消融实验证明 4 帧优于 1 帧（FVD 从 315.69 降至 211.3），近期历史优于远期历史。

3. **模拟器作为通用训练环境**：同一模拟器可与任何奖励函数结合，支持长时程 VLM 策略和 RL 策略训练。实验证明模拟数据微调的视频字幕模型在 MSR-VTT、VATEX、SMIT 上迁移优于真实数据微调。

## 实验与结果

### 帧条件消融（Ego4D 验证集）
| 条件 | FID | FVD | IS | CLIP |
|------|-----|-----|-----|------|
| 1 frame | 59.47 | 315.69 | 3.03 | 22.55 |
| 4 distant | 34.89 | 237 | 3.43 | 22.62 |
| 4 recent | 34.63 | 211.3 | 3.52 | 22.63 |

### 长时程 VLM 策略（Language Table）
| 方法 | RDG (moved) | RDG (all) |
|------|-------------|-----------|
| VLM-BC | 0.11 ± 0.13 | 0.07 ± 0.11 |
| Simulator-Hindsight | 0.34 ± 0.13 | 0.34 ± 0.13 |

模拟长时程生成数据比原始数据好 3-4 倍。

### RL 策略（Language Table，48 任务）
| 方法 | Succ. rate (all) | Succ. rate (pointing) |
|------|-------------------|----------------------|
| VLA-BC | 0.58 | 0.12 |
| Simulator-RL | 0.81 | 0.71 |

### 视频字幕（PaLI-X 55B 微调）
| 方法 | Activity | MSR-VTT | VATEX | SMIT |
|------|----------|---------|-------|------|
| No finetune | 15.2 | 21.91 | 13.31 | 9.22 |
| Activity（真实） | 54.90 | 24.88 | 36.01 | 16.91 |
| Simulator（模拟） | 46.23 | 27.63 | 40.03 | 20.58 |

纯模拟数据微调将 ActivityNet 从 15.2 提升至 46.23，达到真实数据微调的 84%（由表内数值 46.23/54.90 计算），且在三个迁移数据集上优于真实数据微调。

### 数据集与模型规模消融（1024 测试样本）
| 配置 | FVD | CLIP |
|------|-----|------|
| Internet only | 219.62 | 22.27 |
| Without internet | 307.80 | 21.99 |
| Universal simulator | 211.30 | 22.63 |
| 500M | 277.85 | 22.08 |
| 1.6B | 224.61 | 22.27 |
| 5.6B | 211.30 | 22.63 |

## 边界与局限

- **幻觉**：当动作对场景不现实时（如对桌面机器人给出“洗手”），会观察到桌子变成水槽等不现实结果；理想情况下应检测不可模拟动作
- **有限记忆**：仅基于少量最近帧的条件无法捕捉长期记忆（如抽屉中的苹果在打开抽屉时可能消失）
- **有限的域外泛化**：主要训练于 4 种机器人形态，对未见机器人泛化能力有限
- **仅视觉模拟**：不适用于动作不引起视觉变化的环境（如抓取静态杯子时的不同力）；声音不在模拟范围内
- **扩展收益平台期**：模型从 1.6B 增至 5.6B 时 FVD 改善幅度趋于平台期（由表内数值 224.61→211.30 计算），作者认为略显失望

## 工程启示

- **复现优先级**：先核对数据混合权重（0.1 或 0.05）和 4 帧历史条件化，这是性能的关键；训练需 512 TPU-v3 和 20 天，小规模复现可先尝试 500M 模型验证流程
- **最易踩坑**：域特定标识符会损害跨域泛化，仅在测试域在训练域分布内时使用；仅训练于窄域数据（如仅 SSV2 或仅互联网数据）会导致环境模拟失败
- **下游集成**：模拟器通过远程过程调用封装在 DM Env API 的 step 函数中，可直接替换真实环境；RL 训练使用 REINFORCE 时，奖励定义为 r = -[d(o_{t+1}, g) - d(o_t, g)] · C，其中 C = 5e-2
- **数据选择**：互联网数据至关重要，移除后 FVD 从 211.30 恶化至 307.80；低数据域（如 HM3D 仅 700 示例）可通过联合训练受益

## Overview
Generative models trained on internet data have revolutionized how text, image, and video content can be created. Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents. Applications of a real-world simulator range from controllable content creation in games and movies, to training embodied agents purely in simulation that can be directly deployed in the real world. We explore the possibility of learning a universal simulator (UniSim) of real-world interaction through generative modeling. We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in image data, densely sampled actions in robotics data, and diverse movements in navigation data). With careful orchestration of diverse datasets, each providing a different aspect of the overall experience, we can simulate the visual outcome of both high-level instructions such as "open the drawer" and low-level controls from otherwise static scenes and objects. We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world in zero shot after training purely in simulation. We also show that other types of intelligence such as video captioning models can benefit from training with simulated experience, opening up even wider applications. Video demos can be found at https://universal-simulator.github.io.

## 参考
- https://arxiv.org/abs/2310.06114

## 개요

본 논문은 UniSim, 5.6B 파라미터의 범용 실제 세계 시뮬레이터를 제안하며, 비디오 생성을 역학 문제로 모델링하고 통합된 행동-비디오 인터페이스를 통해 인터넷 이미지, 인간 활동, 로봇 조작 등 다양한 소스의 데이터를 통합합니다. 핵심 기여는 대규모 조건부 비디오 생성 모델이 장기간 VLM 정책 및 RL 정책을 훈련하기 위한 상호작용 환경으로 사용될 수 있음을 증명하고, 다운스트림 작업 성능을 크게 향상시키는 것입니다.

## 무엇을 바꾸었는가

생성 모델의 다음 이정표는 더 사실적인 정적 미디어를 생성하는 것이 아니라, 상호작용 에이전트의 행동에 반응하여 실제 세계 경험을 시뮬레이션하는 것입니다. 기존 세계 모델은 저차원 상태 공간이나 게임 도메인에서 단일 시스템 역학을 학습하거나, 생성된 비디오에 대한 제어 능력이 부족하여 구현 에이전트를 훈련하기 위한 범용 환경으로 사용할 수 없습니다. 정책 학습의 주요 병목은 실제 세계 환경에 대한 제한된 접근이며, UniSim은 현실적이고 무한한 환경 접근을 제공하려고 합니다.

진정으로 바뀐 것은 "비디오 생성"을 콘텐츠 생성 도구에서 "역학 모델링" 도구로 재정의한 것입니다. 저자는 각 작업에 대해 전용 시뮬레이터를 훈련하는 대신, 작업 간에 일관되게 유지되는 범용 시뮬레이터를 구축하여 개별적으로 학습된 보상 함수와 결합할 수 있게 했습니다. 이는 다운스트림 정책 학습이 완전히 시뮬레이션에서 수행되고 실제 세계에 직접 배포될 수 있음을 의미하며, 실제 환경 샘플링의 병목을 우회합니다.

## 방법 분해

### 통합 행동 공간
- 텍스트 토큰은 T5 언어 모델 임베딩을 통해 연속 표현으로 변환됩니다
- 저수준 제어 행동(예: 로봇 관절 운동)은 정규화 후 4096개의 bin으로 이산화되어 언어 임베딩과 연결됩니다
- 데이터셋 식별자는 행동에 추가될 수 있지만, 테스트 도메인이 훈련 도메인 분포 내에 있을 때만 사용됩니다

### 데이터셋 구성
- **시뮬레이션 실행**: Habitat 객체 내비게이션(HM3D, 710개 예시) 및 Language Table sim(160k개 예시)
- **실제 로봇**: Bridge Data(2k), RT-1/RT-2(70k), Language Table real(440k)
- **인간 활동**: Ego4D(3.5M), EPIC-KITCHENS(25k), Something-Something V2(160k)
- **파노라마 스캔**: Matterport3D(3.5M), 파노라마 스캔을 잘라 "좌회전" 등의 행동 구성
- **인터넷 데이터**: LAION-400M 및 ALIGN 각 400M, 단일 이미지를 단일 프레임 비디오로 간주

### 관측 예측 모델
모델 p(o_t|h_{t-1}, a_{t-1})을 학습하며, 여기서 h_{t-1}은 과거 프레임 집합, a_{t-1}은 시간 확장 행동입니다. 핵심 설계 결정은 모든 과거 정보를 조건화하는 대신 최근 상호작용의 제한된 프레임(예: 4프레임)만 조건으로 사용하여 모델링 문제를 크게 단순화하는 것입니다.

### 확산 모델 파라미터화
- 노이즈 제거 모델 ε_θ(o_t^(k), k|h_{t-1}, a_{t-1})은 K단계 노이즈 제거를 통해 다음 관측을 생성합니다
- 훈련 손실은 MSE: L_MSE = ||ε - ε_θ(√(1-β^(k))o_t + √(β^(k))ε, k|h_{t-1}, a_{t-1})||²
- 샘플링 과정: o_t^(k-1) = α^(k)(o_t^(k) - γ^(k)ε_θ(o_t^(k), k|h_{t-1}, a_{t-1})) + ξ
- 행동 조건화는 분류기 없는 안내를 사용: ε_θ = (1+η)ε_θ(·|h, a) - ηε_θ(·|h)

### 아키텍처
비디오 U-Net, 교차된 시간 및 공간 주의 메커니즘과 컨볼루션 레이어. 기본 모델은 [16, 24, 40] 해상도에서 실행되며, 두 개의 초해상도 모델이 각각 [48, 80] 및 [192, 320]으로 향상시킵니다. 과거 조건 프레임은 모든 미래 프레임 인덱스에 복사되어 노이즈 샘플과 연결됩니다.

## 핵심 혁신

1. **통합 행동-비디오 인터페이스**: 텍스트, 저수준 제어, 이미지 캡션을 행동 공간으로 통합하여 동일한 시뮬레이터가 다른 양식의 상호작용에 응답할 수 있게 합니다. 이는 인터넷 규모 데이터(LAION, ALIGN 각 400M)를 로봇 및 인간 활동 데이터와 공동 훈련한 최초의 비디오 생성 시뮬레이터입니다.

2. **최근 프레임만 조건화하는 설계**: 모든 과거 정보를 조건화하는 대신 4프레임의 히스토리만으로 효과적으로 모델링할 수 있음을 발견했습니다. 이 단순화는 장기간 자기회귀 롤아웃을 가능하게 하며, 절제 실험은 4프레임이 1프레임보다 우수함(FVD 315.69에서 211.3으로 감소)을 증명하고, 먼 과거보다 최근 과거가 더 우수함을 보여줍니다.

3. **시뮬레이터로서의 범용 훈련 환경**: 동일한 시뮬레이터가 모든 보상 함수와 결합될 수 있어 장기간 VLM 정책 및 RL 정책 훈련을 지원합니다. 실험은 시뮬레이션 데이터로 미세 조정된 비디오 캡션 모델이 MSR-VTT, VATEX, SMIT에서 실제 데이터 미세 조정보다 우수한 전이 성능을 보임을 증명합니다.

## 실험 및 결과

### 프레임 조건 절제(Ego4D 검증 세트)
| 조건 | FID | FVD | IS | CLIP |
|------|-----|-----|-----|------|
| 1프레임 | 59.47 | 315.69 | 3.03 | 22.55 |
| 4개 먼 프레임 | 34.89 | 237 | 3.43 | 22.62 |
| 4개 최근 프레임 | 34.63 | 211.3 | 3.52 | 22.63 |

### 장기간 VLM 정책(Language Table)
| 방법 | RDG (이동) | RDG (전체) |
|------|-------------|-----------|
| VLM-BC | 0.11 ± 0.13 | 0.07 ± 0.11 |
| 시뮬레이터-회고 | 0.34 ± 0.13 | 0.34 ± 0.13 |

시뮬레이션 장기간 생성 데이터가 원본 데이터보다 3-4배 우수합니다.

### RL 정책(Language Table, 48개 작업)
| 방법 | 성공률 (전체) | 성공률 (포인팅) |
|------|-------------------|----------------------|
| VLA-BC | 0.58 | 0.12 |
| 시뮬레이터-RL | 0.81 | 0.71 |

### 비디오 캡션(PaLI-X 55B 미세 조정)
| 방법 | Activity | MSR-VTT | VATEX | SMIT |
|------|----------|---------|-------|------|
| 미세 조정 없음 | 15.2 | 21.91 | 13.31 | 9.22 |
| Activity (실제) | 54.90 | 24.88 | 36.01 | 16.91 |
| 시뮬레이터 (시뮬레이션) | 46.23 | 27.63 | 40.03 | 20.58 |

순수 시뮬레이션 데이터 미세 조정은 ActivityNet을 15.2에서 46.23으로 향상시켜 실제 데이터 미세 조정의 84%에 도달하며(표 내 값 46.23/54.90으로 계산), 세 가지 전이 데이터셋에서 실제 데이터 미세 조정보다 우수합니다.

### 데이터셋 및 모델 규모 절제(1024개 테스트 샘플)
| 구성 | FVD | CLIP |
|------|-----|------|
| 인터넷만 | 219.62 | 22.27 |
| 인터넷 없음 | 307.80 | 21.99 |
| 범용 시뮬레이터 | 211.30 | 22.63 |
| 500M | 277.85 | 22.08 |
| 1.6B | 224.61 | 22.27 |
| 5.6B | 211.30 | 22.63 |

## 경계 및 한계

- **환각**: 행동이 장면에 비현실적일 때(예: 데스크톱 로봇에게 "손 씻기" 지시), 테이블이 싱크대로 변하는 등의 비현실적인 결과가 관찰됩니다; 이상적으로는 시뮬레이션 불가능한 행동을 감지해야 합니다
- **제한된 기억**: 소수의 최근 프레임만 기반으로 한 조건화는 장기 기억을 포착할 수 없습니다(예: 서랍 속 사과가 서랍을 열 때 사라질 수 있음)
- **제한된 도메인 외 일반화**: 주로 4가지 로봇 형태로 훈련되어, 보지 못한 로봇에 대한 일반화 능력이 제한적입니다
- **시각적 시뮬레이션만 가능**: 행동이 시각적 변화를 일으키지 않는 환경(예: 정적 컵을 잡을 때 다른 힘)에는 적용할 수 없습니다; 소리는 시뮬레이션 범위에 포함되지 않습니다
- **확장 이득 정체**: 모델이 1.6B에서 5.6B로 증가할 때 FVD 개선 폭이 정체되는 경향(표 내 값 224.61→211.30으로 계산)을 보이며, 저자는 다소 실망스럽다고 언급합니다

## 엔지니어링 시사점

- **재현 우선순위**: 데이터 혼합 가중치(0.1 또는 0.05)와 4프레임 히스토리 조건화를 먼저 확인하세요. 이것이 성능의 핵심입니다; 훈련에는 512 TPU-v3와 20일이 필요하며, 소규모 재현은 먼저 500M 모델로 프로세스를 검증할 수 있습니다
- **가장 흔한 함정**: 도메인 특정 식별자는 교차 도메인 일반화를 저해하므로, 테스트 도메인이 훈련 도메인 분포 내에 있을 때만 사용하세요; 좁은 도메인 데이터(예: SSV2만 또는 인터넷 데이터만)로만 훈련하면 환경 시뮬레이션이 실패합니다
- **다운스트림 통합**: 시뮬레이터는 DM Env API의 step 함수에 원격 프로시저 호출로 캡슐화되어 실제 환경을 직접 대체할 수 있습니다; RL 훈련에서 REINFORCE를 사용할 때 보상은 r = -[d(o_{t+1}, g) - d(o_t, g)] · C로 정의되며, 여기서 C = 5e-2입니다
- **데이터 선택**: 인터넷 데이터는 매우 중요하며, 제거 시 FVD가 211.30에서 307.80으로 악화됩니다; 저데이터 도메인(예: HM3D 700개 예시)은 공동 훈련을 통해 이점을 얻을 수 있습니다
