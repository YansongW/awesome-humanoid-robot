---
$id: ent_paper_xiaomi_robotics_1_scaling_vision_languag_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories'
  zh: 'Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories'
  ko: 'Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories'
summary:
  en: We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language
    instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently
    adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of
    pre-training and post-training..
  zh: 小米机器人团队提出 Xiaomi-Robotics-1，一个基于超过 10 万小时 UMI 真实世界轨迹预训练、再经跨具身数据后训练的 VLA 基础模型。核心贡献在于构建了可扩展的自动标注流水线与两阶段训练方案，并通过数据与模型缩放实验系统验证了数据规模对泛化性能的主导作用。
  ko: We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language
    instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently
    adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of
    pre-training and post-training..
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
- xiaomi
- robotics
- '1'
- scaling
- vision
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.15330 Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of'
  url: https://arxiv.org/abs/2607.15330
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

小米机器人团队提出 Xiaomi-Robotics-1，一个基于超过 10 万小时 UMI 真实世界轨迹预训练、再经跨具身数据后训练的 VLA 基础模型。核心贡献在于构建了可扩展的自动标注流水线与两阶段训练方案，并通过数据与模型缩放实验系统验证了数据规模对泛化性能的主导作用。

## 它改变了什么

机器人 VLA 领域长期受困于数据瓶颈：遥操作采集缓慢、成本高，且数据高度冗余、集中于狭窄任务与环境范围。此前工作要么依赖人工逐段标注轨迹，要么在有限数据上训练，缺乏对“数据规模如何影响基础模型泛化”的系统性认知。Xiaomi-Robotics-1 真正改变的是将机器人基础模型的训练范式推向“网络规模数据 + 自动标注”的路径——用便携式 UMI 设备绕开物理机器人具身限制，以 10 万小时量级数据逼近语言模型式的缩放规律。

这项工作的深层价值在于证明了机器人领域的“数据缩放定律”确实存在：当数据从 12.5% 增至 100% 时，未见环境任务成功率从 26% 跃升至 75%（由表内数值 26%→75% 计算），且模型规模从 2B 增至 10B 仅带来 61%→79% 的提升（由表内数值 61%→79% 计算），数据量的边际收益显著大于模型容量。这为整个行业指明了资源投入方向——数据采集与标注自动化比堆算力更关键。

## 方法拆解

### 两阶段训练架构
- **预训练阶段**：使用 UMI 手持夹爪采集超过 100,000 小时真实轨迹，覆盖家庭、商业、工业、办公、户外等场景。开发生产者-消费者自动标注流水线：CPU 线程将轨迹切分为等长片段并写入内存文件系统，客户端线程维持数百个在途标注请求，调用 Qwen3.5-27B 描述片段中夹爪与交互物体的状态转换，整个语料库约两周完成标注。
- **后训练阶段**：使用约 10,000 小时跨具身数据（7,200 小时自研移动机械臂与双臂数据、1,000 小时人工标注 UMI 数据、开源数据集 Bridge V2/RT-1/DROID），将状态转换提示转换为祈使指令，并过滤空闲片段。

### 模型架构关键设计
- **Mixture-of-Transformers**：预训练 VLM（Qwen3-VL）编码观测与语言指令，扩散 Transformer（DiT）以本体状态和 VLM 的 KV 缓存为条件，通过流匹配生成动作块。DiT 层数与 VLM 相同但隐藏尺寸更小（如 5B 变体中 VLM 隐藏尺寸 2560、DiT 隐藏尺寸 1024），以加快推理。
- **流匹配损失**：L_Flow = ||v_θ(o_t, l, s_t, ã^τ, τ) − u(ã^τ, a, τ)||²₂，训练时 τ 从 Beta(1.5, 1) 采样，推理时 5 步欧拉积分（步长 Δτ = 0.2）。
- **Choice Policies 辅助监督**：VLM 输出 K 个候选动作块与分数，采用赢家通吃范式，仅最小 L1 损失的候选计入动作损失。
- **注意力排除**：阻止 DiT token 关注动作相关 token，防止 DiT 直接复制 VLM 输出而非基于视觉上下文生成。
- **训练目标**：L = L_Flow + L_Regression + 0.1·L_NTP。

### 数据采样与效率优化
- 预训练中视觉语言数据与 UMI 轨迹按 1:9 采样；后训练中视觉语言、开源机器人、指令标注 UMI、自研机器人数据按 0.5:0.5:0.5:8.5 采样。
- 批内所有视觉语言 token 打包为单序列进行 VLM 前向，每个样本采样 4 个流匹配时间步以摊销计算成本。

## 关键创新

1. **可扩展自动标注流水线**：将轨迹分割为等长片段并用 LLM 描述状态转换，替代人工语义分割与标注。这是首次在 10 万小时规模上实现全自动轨迹标注，两周完成整个语料库，使数据规模化成为可能。
2. **两阶段“预训练+后训练”范式**：预训练阶段学习通用状态转换能力，后训练阶段通过跨具身数据将能力迁移到具体机器人并转换为祈使指令。这种解耦设计让数据采集（UMI 手持设备）与模型部署（移动机械臂）分离，大幅降低数据门槛。
3. **系统缩放实验**：首次在 VLA 领域同时变化数据规模（12.5%→100%）与模型规模（2B→10B），揭示数据量是泛化性能的主要瓶颈，模型容量在数十亿参数后边际收益递减。

## 实验与结果

### 开箱评估（未见环境与物体实例）
| 设置 | 成功率 |
|---|---|
| 无动作预训练基线 | 26% |
| 12.5% 预训练数据 | 53% |
| 100% 预训练数据 | 75% |
| 2B 模型 | 61% |
| 5B 模型 | 75% |
| 10B 模型 | 79% |

### 下游微调（每任务平均 <10 小时数据）
| 方法 | 平均成功率 | 平均进度 |
|---|---|---|
| Xiaomi-Robotics-1 | 75% | 90% |
| π_0.5 | 40% | 66% |

打印机加纸任务从最佳基线 20% 提升至 70%（由表内数值 20%→70% 计算）。

### 模拟基准对比
| 基准 | Xiaomi-Robotics-1 | 最佳基线 |
|---|---|---|
| RoboCasa（24 任务） | 74.5% | 72.6%（World2Act） |
| RoboCasa365（365 任务） | 57.4% | 46.6%（ABot-M0.6） |
| VLABench（100 类别） | 59.1% SR | 53.2%（ERVLA） |
| RoboDojo（42+ 任务） | 20.07 分 | 13.07 分（Hy-Embodied-0.5-VLA） |

RoboDojo 中 Memory 维度得分 7.81 低于 Hy-Embodied-0.5-VLA 的 13.37，因未纳入历史观测。

## 边界与局限

- 预训练缩放实验仅使用约 2 万小时 UMI 数据（非全部 10 万小时），受计算预算限制，完整数据下的缩放行为论文未明确。
- 后训练评估任务在后训练数据集中出现过，仅环境与物体实例未见，无法验证完全新颖任务组合的泛化。
- RoboDojo 基准未纳入历史观测，Memory 维度显著落后于显式建模记忆的基线。
- 真实机器人高效适应任务仅报告进度里程碑定义，未提供定量成功率数据。
- 模型缩放实验中 2B 与 10B 差距（61%→79%）小于数据翻倍差距（50%→100% 数据带来 6 个百分点提升），表明当前数据规模下模型容量已接近饱和。

## 工程启示

- **复现优先级**：先核对自动标注流水线的生产者-消费者实现——CPU 线程与内存文件系统的交互是两周完成 10 万小时标注的关键，若此处吞吐不足，整个预训练数据管线将成为瓶颈。
- **数据采样比例**：后训练中自研机器人数据占比 8.5/10 是刻意设计，直接复现时若自研数据不足，需按比例缩减而非简单替换，否则跨具身迁移效果会显著下降。
- **动作空间统一**：手臂采用相对增量末端执行器位姿并统一坐标系方向，基座与腰部用速度/位置增量表示，缺失维度在损失中掩码。下游团队接入新机器人时，必须先完成这一动作空间对齐，否则模型输出无法直接执行。
- **最易踩坑处**：DiT 对动作 token 的注意力排除机制——若移除该设计，模型会退化为复制 VLM 输出而非基于视觉上下文生成，导致动作精度骤降。复现时务必保留此约束。
- **微调协议**：使用异步训练方案（文献[8]），低数据设置下每任务平均 <10 小时即可达到 75% 成功率，但需注意评估为每任务 10 次试验，方差较大，建议增加试验次数以稳定结论。

## Overview
We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. During pre-training, we imbue the model with broad and generalizable action-generation capabilities by training on over 100k hours of real-world manipulation trajectories collected via UMI devices. Crucially, we develop a scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning. During post-training, we aim to align these capabilities with robot embodiments and imperative instructions that humans naturally use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-Robotics-1 consistently improves with increased data scales and model sizes during pre-training. This scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.4% success rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07). Code and model checkpoints will be released. Project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html

## 参考
- https://arxiv.org/abs/2607.15330

## 개요

샤오미 로봇 팀은 10만 시간 이상의 UMI 실제 세계 궤적 사전 학습 후, 교차-구현 데이터 후속 학습을 거친 VLA 기반 모델인 Xiaomi-Robotics-1을 제안한다. 핵심 기여는 확장 가능한 자동 주석 파이프라인과 2단계 훈련 방식을 구축하고, 데이터 및 모델 스케일링 실험을 통해 데이터 규모가 일반화 성능에 미치는 지배적 역할을 체계적으로 검증한 것이다.

## 무엇을 바꾸었는가

로봇 VLA 분야는 오랫동안 데이터 병목 현상에 시달려 왔다: 원격 조작 수집은 느리고 비용이 높으며, 데이터는 고도로 중복되고 좁은 작업 및 환경 범위에 집중되어 있다. 기존 연구는 수동으로 궤적을 구간별로 주석을 달거나 제한된 데이터로 훈련하는 데 의존했으며, "데이터 규모가 기반 모델 일반화에 어떻게 영향을 미치는지"에 대한 체계적 이해가 부족했다. Xiaomi-Robotics-1이 진정으로 바꾼 것은 로봇 기반 모델의 훈련 패러다임을 "네트워크 규모 데이터 + 자동 주석" 경로로 전환한 것이다—휴대용 UMI 장치로 물리적 로봇 구현의 제약을 우회하고, 10만 시간 규모의 데이터로 언어 모델식 스케일링 법칙에 접근한다.

이 작업의 심층적 가치는 로봇 분야의 "데이터 스케일링 법칙"이 실제로 존재함을 증명한 것이다: 데이터가 12.5%에서 100%로 증가할 때, 미경험 환경 작업 성공률이 26%에서 75%로 도약하며(표 내 수치 26%→75% 계산), 모델 규모가 2B에서 10B로 증가할 때는 61%→79%의 향상만을 가져온다(표 내 수치 61%→79% 계산). 데이터 양의 한계 이익이 모델 용량보다 훨씬 크다. 이는 업계 전체에 자원 투입 방향을 제시한다—데이터 수집 및 주석 자동화가 연산력 투입보다 더 중요하다.

## 방법 분석

### 2단계 훈련 아키텍처
- **사전 학습 단계**: UMI 핸드헬드 그리퍼로 10만 시간 이상의 실제 궤적을 수집하며, 가정, 상업, 산업, 사무실, 실외 등 다양한 환경을 포함한다. 생산자-소비자 자동 주석 파이프라인 개발: CPU 스레드가 궤적을 등장 구간으로 분할하고 메모리 파일 시스템에 기록하며, 클라이언트 스레드가 수백 개의 진행 중 주석 요청을 유지하고 Qwen3.5-27B를 호출하여 구간 내 그리퍼와 상호작용 객체의 상태 전환을 설명한다. 전체 코퍼스는 약 2주 만에 주석 완료.
- **후속 학습 단계**: 약 10,000시간의 교차-구현 데이터(7,200시간 자체 개발 이동 매니퓰레이터 및 이중 팔 데이터, 1,000시간 수동 주석 UMI 데이터, 오픈소스 데이터셋 Bridge V2/RT-1/DROID)를 사용하여 상태 전환 프롬프트를 명령형 지시문으로 변환하고, 유휴 구간을 필터링한다.

### 모델 아키텍처 핵심 설계
- **Mixture-of-Transformers**: 사전 학습 VLM(Qwen3-VL)이 관측과 언어 지시를 인코딩하고, 확산 트랜스포머(DiT)가 본체 상태와 VLM의 KV 캐시를 조건으로 하여 흐름 매칭을 통해 액션 블록을 생성한다. DiT 레이어 수는 VLM과 동일하지만 숨겨진 크기는 더 작아(예: 5B 변형에서 VLM 숨겨진 크기 2560, DiT 숨겨진 크기 1024) 추론 속도를 높인다.
- **흐름 매칭 손실**: L_Flow = ||v_θ(o_t, l, s_t, ã^τ, τ) − u(ã^τ, a, τ)||²₂, 훈련 시 τ는 Beta(1.5, 1)에서 샘플링되고, 추론 시 5단계 오일러 적분(스텝 크기 Δτ = 0.2)을 사용한다.
- **Choice Policies 보조 감독**: VLM이 K개의 후보 액션 블록과 점수를 출력하고, 승자 독식 패러다임을 사용하여 최소 L1 손실의 후보만 액션 손실에 포함한다.
- **어텐션 배제**: DiT 토큰이 액션 관련 토큰에 주의를 기울이는 것을 차단하여, DiT가 시각적 맥락에 기반한 생성 대신 VLM 출력을 직접 복사하는 것을 방지한다.
- **훈련 목표**: L = L_Flow + L_Regression + 0.1·L_NTP.

### 데이터 샘플링 및 효율 최적화
- 사전 학습에서 시각-언어 데이터와 UMI 궤적은 1:9 비율로 샘플링되고, 후속 학습에서 시각-언어, 오픈소스 로봇, 지시 주석 UMI, 자체 개발 로봇 데이터는 0.5:0.5:0.5:8.5 비율로 샘플링된다.
- 배치 내 모든 시각-언어 토큰을 단일 시퀀스로 패킹하여 VLM 순방향을 수행하고, 각 샘플에서 4개의 흐름 매칭 시간 단계를 샘플링하여 계산 비용을 분산한다.

## 핵심 혁신

1. **확장 가능한 자동 주석 파이프라인**: 궤적을 등장 구간으로 분할하고 LLM으로 상태 전환을 설명하여 수동 의미 분할 및 주석을 대체한다. 이는 10만 시간 규모에서 전 자동 궤적 주석을 최초로 구현한 것으로, 약 2주 만에 전체 코퍼스를 완료하여 데이터 규모화를 가능하게 한다.
2. **2단계 "사전 학습+후속 학습" 패러다임**: 사전 학습 단계에서 일반적인 상태 전환 능력을 학습하고, 후속 학습 단계에서 교차-구현 데이터를 통해 능력을 특정 로봇으로 전이하고 명령형 지시문으로 변환한다. 이러한 분리 설계는 데이터 수집(UMI 핸드헬드 장치)과 모델 배포(이동 매니퓰레이터)를 분리하여 데이터 장벽을 크게 낮춘다.
3. **체계적 스케일링 실험**: VLA 분야에서 처음으로 데이터 규모(12.5%→100%)와 모델 규모(2B→10B)를 동시에 변화시켜, 데이터 양이 일반화 성능의 주요 병목이며 모델 용량은 수십억 파라미터 이후 한계 이익이 감소함을 밝힌다.

## 실험 및 결과

### 개봉 평가(미경험 환경 및 객체 인스턴스)
| 설정 | 성공률 |
|---|---|
| 액션 사전 학습 없는 기준선 | 26% |
| 12.5% 사전 학습 데이터 | 53% |
| 100% 사전 학습 데이터 | 75% |
| 2B 모델 | 61% |
| 5B 모델 | 75% |
| 10B 모델 | 79% |

### 하위 작업 미세 조정(작업당 평균 <10시간 데이터)
| 방법 | 평균 성공률 | 평균 진행률 |
|---|---|---|
| Xiaomi-Robotics-1 | 75% | 90% |
| π_0.5 | 40% | 66% |

프린터 용지 추가 작업은 최고 기준선 20%에서 70%로 향상되었다(표 내 수치 20%→70% 계산).

### 시뮬레이션 벤치마크 비교
| 벤치마크 | Xiaomi-Robotics-1 | 최고 기준선 |
|---|---|---|
| RoboCasa(24개 작업) | 74.5% | 72.6%(World2Act) |
| RoboCasa365(365개 작업) | 57.4% | 46.6%(ABot-M0.6) |
| VLABench(100개 카테고리) | 59.1% SR | 53.2%(ERVLA) |
| RoboDojo(42+개 작업) | 20.07점 | 13.07점(Hy-Embodied-0.5-VLA) |

RoboDojo의 Memory 차원 점수 7.81은 Hy-Embodied-0.5-VLA의 13.37보다 낮은데, 이는 역사적 관측을 포함하지 않았기 때문이다.

## 경계 및 한계

- 사전 학습 스케일링 실험은 약 2만 시간의 UMI 데이터만 사용했으며(전체 10만 시간 아님), 계산 예산 제약으로 인해 전체 데이터에서의 스케일링 동작은 논문에 명확히 제시되지 않았다.
- 후속 학습 평가 작업은 후속 학습 데이터셋에 등장했으며, 환경과 객체 인스턴스만 미경험이므로 완전히 새로운 작업 조합의 일반화를 검증할 수 없다.
- RoboDojo 벤치마크는 역사적 관측을 포함하지 않아 Memory 차원에서 명시적 메모리 모델링 기준선보다 크게 뒤처진다.
- 실제 로봇 효율 적응 작업은 진행률 마일스톤 정의만 보고하며 정량적 성공률 데이터를 제공하지 않는다.
- 모델 스케일링 실험에서 2B와 10B의 차이(61%→79%)는 데이터 두 배 증가 차이(50%→100% 데이터가 6% 포인트 향상)보다 작아, 현재 데이터 규모에서 모델 용량이 이미 포화에 가까움을 시사한다.

## 공학적 시사점

- **재현 우선순위**: 자동 주석 파이프라인의 생산자-소비자 구현을 먼저 검증하라—CPU 스레드와 메모리 파일 시스템의 상호작용이 2주 만에 10만 시간 주석을 완료하는 핵심이며, 이 처리량이 부족하면 전체 사전 학습 데이터 파이프라인이 병목이 된다.
- **데이터 샘플링 비율**: 후속 학습에서 자체 개발 로봇 데이터 비율 8.5/10은 의도된 설계이다. 직접 재현 시 자체 개발 데이터가 부족하면 단순 교체가 아닌 비율에 따라 축소해야 하며, 그렇지 않으면 교차-구현 전이 효과가 크게 저하된다.
- **액션 공간 통일**: 팔은 상대 증분 엔드 이펙터 포즈를 사용하고 좌표계 방향을 통일하며, 베이스와 허리는 속도/위치 증분으로 표현하고 누락된 차원은 손실에서 마스킹한다. 하위 팀이 새 로봇을 연결할 때 먼저 이 액션 공간 정렬을 완료해야 하며, 그렇지 않으면 모델 출력을 직접 실행할 수 없다.
- **가장 함정에 빠지기 쉬운 부분**: DiT의 액션 토큰 어텐션 배제 메커니즘—이 설계를 제거하면 모델이 시각적 맥락 기반 생성 대신 VLM 출력 복사로 퇴화하여 액션 정밀도가 급락한다. 재현 시 반드시 이 제약을 유지하라.
- **미세 조정 프로토콜**: 비동기 훈련 방식(문헌[8])을 사용하며, 저데이터 설정에서 작업당 평균 <10시간으로 75% 성공률에 도달할 수 있지만, 평가가 작업당 10회 시도로 분산이 크므로 시도 횟수를 늘려 결론을 안정화하는 것이 좋다.
