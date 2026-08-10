---
$id: ent_paper_turbovla_real_time_vision_language_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM'
  zh: 'TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM'
  ko: 'TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM'
summary:
  en: Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations
    are projected into the representation space of a large language model before being decoded into robot actions. Although
    effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we
    introduce TurboVLA, a new VLA paradigm that.
  zh: TurboVLA 提出一种直接 V+L→A 的视觉-语言-动作执行范式，用 DINOv3 视觉编码器与 BERT 文本编码器替代 LLM 中心接口，通过双向交叉注意力交互后由 ACT 风格解码器并行输出动作块。在 RTX 4090
    上实现 31.2ms 延迟、0.9GB VRAM，LIBERO 平均成功率 97.7%，RoboTwin 2.0 平均成功率 60.2%。
  ko: Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations
    are projected into the representation space of a large language model before being decoded into robot actions. Although
    effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we
    introduce TurboVLA, a new VLA paradigm that.
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
- turbovla
- real
- time
- vision
- language
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
  title: 'arXiv:2607.27205 TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1'
  url: https://arxiv.org/abs/2607.27205
  date: '2026-07-29'
  accessed_at: '2026-08-05'
---

## 概述

TurboVLA 提出一种直接 V+L→A 的视觉-语言-动作执行范式，用 DINOv3 视觉编码器与 BERT 文本编码器替代 LLM 中心接口，通过双向交叉注意力交互后由 ACT 风格解码器并行输出动作块。在 RTX 4090 上实现 31.2ms 延迟、0.9GB VRAM，LIBERO 平均成功率 97.7%，RoboTwin 2.0 平均成功率 60.2%。

## 它改变了什么

现有 VLA 几乎全部押注在 LLM 中心化路径上：视觉 token 投影进 LLM 表示空间，再自回归解码出动作。这个设计在每次策略调用时都要过一遍大模型的前向，计算和显存开销被 LLM 参数规模锁死，控制频率上不去，边缘设备根本跑不动。作者直接质疑这个前提——执行级控制真的需要开放式语言生成吗？指令条件化操作是必要的，但任务分解和自由文本生成对底层闭环控制是冗余的。

TurboVLA 真正改变的是把 VLA 从"语言模型附带动作头"重构为"感知-交互-动作"的专用流水线。它证明了执行级策略可以完全绕开 LLM 的推理能力，用轻量编码器加双向交互就能达到甚至超过 LLM 中心模型的成功率。这个结论动摇了当前 VLA 设计的基本假设：不是所有机器人控制问题都需要大模型，专用小模型在受限平台上可能更合适。

## 方法拆解

TurboVLA 的架构分为四条并行支路，最后汇入动作解码器：

### 视觉编码
- 骨干：DINOv3（LIBERO 用 ViT-B，RoboTwin 2.0 用 ViT-L）
- 视觉特征投影到共享维度 d=256，添加位置嵌入与相机视角嵌入
- 多相机流（K 个）拼接保留互补线索

### 语言编码
- 轻量级 BERT 作为文本编码器，保留完整指令 token 序列而非池化嵌入
- 关键决策：保留 token 级信息以保留对象、属性和空间关系的细粒度条件化信号

### 双向视觉-语言交互
- N=6 层双向交叉注意力，受 Grounding DINO 启发
- 每层包含：层归一化、双向交叉注意力、模态特定前馈网络、残差连接
- 视觉到指令注意力注入场景上下文；指令到视觉注意力条件化视觉特征
- 初始化自 grounding 预训练特征增强权重

### 动作解码
- ACT 风格 transformer 解码器，H=12 个可学习动作查询
- 并行解码连续动作块，无需动作标记化或自回归生成
- 机器人状态通过轻量级投影网络单独编码，直接引入解码器

### 训练
- 行为克隆 ℓ1 损失，无辅助语言建模目标
- 学习率 5×10⁻⁵，四块 RTX 4090 训练
- LIBERO：80k 步，10k 预热，有效批大小 256，预测 12 步 7-DoF 动作块
- RoboTwin 2.0：55k 步，1k 预热，有效批大小 192，预测 50 步 14 维绝对关节位置

## 关键创新

第一，范式级简化。V+L→A 直接路径取代 V→L→A，把 LLM 从执行链路中完全移除。这不是增量优化，而是架构层面的重新定位——执行级控制不需要开放式语言生成，这个判断如果成立，整个 VLA 的算力需求曲线都会下移。

第二，双向交互而非单向条件化。消融显示无交互时平均成功率 95.2%，单向交叉注意力提升到 96.1% 和 96.5%，双向交互达到 97.7%。场景感知的指令特征与指令条件化的视觉特征为动作预测提供互补信息，这个设计决策有明确的实验支撑。

第三，保留完整指令 token 序列而非池化嵌入。语言消融中，用任务 ID 嵌入替代语义指令后平均成功率从 97.7% 降至 95.4%，LIBERO-Goal 从 97.4% 降至 95.8%，证明自然语言提供的细粒度信息超出闭集任务身份，轻量编码器足以承载这些信息。

## 实验与结果

LIBERO 基准上 TurboVLA 以 0.2B 参数、0.9GB VRAM、31.2ms 延迟达到 97.7% 平均成功率，全面超越所有对比方法。效率优势尤其突出：OpenVLA 需要 7.5B 参数、14.9GB VRAM、202.9ms 延迟才达到 76.5% 成功率；π₀.₅ 以 3.4B 参数、12.8GB VRAM、93.6ms 延迟达到 96.9%。TurboVLA 在成功率领先的同时，延迟降低约 3 倍（由表内数值 93.6→31.2 计算），VRAM 降低约 14 倍（由表内数值 12.8→0.9 计算）。

| 指标 | TurboVLA | π₀.₅ | OpenVLA | Diffusion Policy |
|---|---|---|---|---|
| 参数 (B) | 0.2 | 3.4 | 7.5 | 0.3 |
| VRAM (GB) | 0.9 | 12.8 | 14.9 | 1.1 |
| 延迟 (ms) | 31.2 | 93.6 | 202.9 | 924.8 |
| LIBERO 平均成功率 | 97.7% | 96.9% | 76.5% | 72.4% |

RoboTwin 2.0 上 TurboVLA 以 0.4B 参数、43.4ms 延迟达到 60.2% 平均成功率，超过 π₀.₅ 的 57.0% 和 DP3 的 55.2%。真实世界 AgileX Piper 平台四个任务成功率分别为 92.5%、80%、90%、87.5%，均优于 π₀.₅。

消融实验的关键发现：移除语言后平均成功率从 97.7% 降至 70.8%，LIBERO-Goal 从 97.4% 骤降至 11.6%，证明策略不能仅依赖视觉先验；交互深度 N=6 最优，N=8 略降至 96.6%；动作视界 H=12 最优，H=15 降至 95.6%。

## 边界与局限

RoboTwin 2.0 实验仅使用官方干净演示数据，未包含随机场景数据，原因是计算预算限制；也未引入 VLA-Adapter 或 StarVLA 框架之外的增强技术。真实世界评估仅覆盖四个代表性任务，未扩展到更广泛场景。TurboVLA 主要面向具体执行级指令，不具备高层任务规划所需的复杂语义理解与推理能力，开放式语言生成和任务级规划不在其能力范围内。论文未明确在更复杂长程任务或非结构化环境中的表现边界。

## 工程启示

复现时先核对三个关键点：一是交互模块初始化权重必须来自 Grounding DINO 预训练特征增强权重，直接随机初始化可能达不到报告的双向交互增益；二是保留完整指令 token 序列而非池化嵌入，这是语言信息有效性的关键，消融显示任务 ID 嵌入会损失 2.3% 平均成功率；三是动作视界 H=12 和交互深度 N=6 是容量与效率的平衡点，H=15 或 N=8 反而会掉点。

最容易踩坑的地方是 RoboTwin 2.0 的数据配置——论文明确只用官方干净演示，不含随机场景数据，如果混入随机场景数据，训练分布会偏移，成功率可能无法复现。推理时注意延迟测量是从多模态输入到产生动作块的时间，批大小 1，如果按自回归 token 生成方式测量会得到不同数值。真实世界微调从 LIBERO 预训练检查点初始化，4×65 遥操作演示、12.5k 步，这个迁移路径值得参考。

## Overview
Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that reformulates the conventional $V \to L \to A$ pathway as a direct $V + L \to A$ mapping. Instead of using a large language model as the central interface between perception and action, TurboVLA independently encodes visual observations and language instructions, directly exchanges information between them through lightweight bidirectional vision-language interaction, and predicts continuous action chunks with a compact decoder. This simple design constructs task-conditioned representations directly from visual and linguistic features, significantly reducing the computational and memory costs of VLA inference. On LIBERO, TurboVLA achieves 97.7% average success with only 0.2B parameters, 31.2 ms inference latency, and 0.9 GB inference VRAM on a consumer-grade RTX 4090, matching or outperforming substantially larger VLA policies. These results establish TurboVLA as a simple and effective alternative to the prevailing LLM-centric VLA paradigm, offering a new perspective on how vision, language, and action can be connected for efficient robotic manipulation. Code is available at https://github.com/H-EmbodVis/TurboVLA.

## 参考
- https://arxiv.org/abs/2607.27205

## 개요

TurboVLA는 LLM 중심 인터페이스를 대체하는 직접적인 V+L→A 시각-언어-동작 실행 패러다임을 제안하며, DINOv3 시각 인코더와 BERT 텍스트 인코더를 사용하고, 양방향 교차 어텐션 상호작용 후 ACT 스타일 디코더가 동작 블록을 병렬로 출력합니다. RTX 4090에서 31.2ms 지연 시간, 0.9GB VRAM을 달성하고, LIBERO 평균 성공률 97.7%, RoboTwin 2.0 평균 성공률 60.2%를 기록합니다.

## 무엇을 바꾸었는가

기존 VLA는 거의 모두 LLM 중앙 집중식 경로에 의존합니다: 시각 토큰을 LLM 표현 공간에 투영한 후 자기회귀적으로 동작을 디코딩합니다. 이 설계는 정책 호출마다 대형 모델의 순전파를 거쳐야 하므로, 계산 및 메모리 오버헤드가 LLM 파라미터 규모에 고정되어 제어 주파수를 높일 수 없고 엣지 디바이스에서는 실행이 불가능합니다. 저자는 이 전제를 직접 의문시합니다—실행 수준 제어에 정말 개방형 언어 생성이 필요한가? 명령 조건화 조작은 필요하지만, 작업 분해와 자유 텍스트 생성은 하위 수준 폐루프 제어에 중복됩니다.

TurboVLA가 실제로 바꾼 것은 VLA를 "언어 모델에 동작 헤드가 부착된 형태"에서 "지각-상호작용-동작" 전용 파이프라인으로 재구성한 것입니다. 실행 수준 정책이 LLM의 추론 능력을 완전히 우회할 수 있고, 경량 인코더와 양방향 상호작용만으로도 LLM 중심 모델의 성공률에 도달하거나 능가할 수 있음을 증명했습니다. 이 결론은 현재 VLA 설계의 기본 가정을 흔듭니다: 모든 로봇 제어 문제에 대형 모델이 필요한 것은 아니며, 제한된 플랫폼에서는 전용 소형 모델이 더 적합할 수 있습니다.

## 방법 분석

TurboVLA의 아키텍처는 네 개의 병렬 분기로 구성되며, 마지막에 동작 디코더로 수렴합니다:

### 시각 인코딩
- 백본: DINOv3 (LIBERO는 ViT-B, RoboTwin 2.0은 ViT-L 사용)
- 시각 특징을 공유 차원 d=256으로 투영하고, 위치 임베딩과 카메라 시점 임베딩 추가
- 다중 카메라 스트림(K개)을 연결하여 상호 보완적 단서 유지

### 언어 인코딩
- 경량 BERT를 텍스트 인코더로 사용하며, 풀링 임베딩이 아닌 전체 명령 토큰 시퀀스 유지
- 핵심 결정: 객체, 속성, 공간 관계의 세밀한 조건화 신호를 유지하기 위해 토큰 수준 정보 보존

### 양방향 시각-언어 상호작용
- Grounding DINO에서 영감을 받은 N=6층 양방향 교차 어텐션
- 각 층은 층 정규화, 양방향 교차 어텐션, 모달별 피드포워드 네트워크, 잔차 연결 포함
- 시각→명령 어텐션은 장면 컨텍스트를 주입하고, 명령→시각 어텐션은 시각 특징을 조건화
- 그라운딩 사전 훈련 특징 강화 가중치로 초기화

### 동작 디코딩
- ACT 스타일 트랜스포머 디코더, H=12개의 학습 가능한 동작 쿼리
- 동작 토큰화나 자기회귀 생성 없이 연속 동작 블록을 병렬 디코딩
- 로봇 상태는 경량 투영 네트워크로 별도 인코딩되어 디코더에 직접 주입

### 훈련
- 보조 언어 모델링 목표 없이 행동 클로닝 ℓ1 손실
- 학습률 5×10⁻⁵, RTX 4090 4개로 훈련
- LIBERO: 80k 스텝, 10k 워밍업, 유효 배치 크기 256, 12스텝 7-DoF 동작 블록 예측
- RoboTwin 2.0: 55k 스텝, 1k 워밍업, 유효 배치 크기 192, 50스텝 14차원 절대 관절 위치 예측

## 핵심 혁신

첫째, 패러다임 수준의 단순화. V+L→A 직접 경로가 V→L→A를 대체하여 LLM을 실행 체인에서 완전히 제거합니다. 이는 점진적 최적화가 아니라 아키텍처 차원의 재정의입니다—실행 수준 제어에 개방형 언어 생성이 필요하지 않다는 판단이 성립한다면, VLA 전체의 연산 요구 곡선이 하향 이동합니다.

둘째, 단방향 조건화가 아닌 양방향 상호작용. 절제 실험에서 상호작용이 없을 때 평균 성공률 95.2%, 단방향 교차 어텐션은 96.1%와 96.5%로 향상, 양방향 상호작용은 97.7%에 도달합니다. 장면 인식 명령 특징과 명령 조건화 시각 특징이 동작 예측에 상호 보완적 정보를 제공하며, 이 설계 결정은 명확한 실험적 근거를 가집니다.

셋째, 풀링 임베딩이 아닌 전체 명령 토큰 시퀀스 유지. 언어 절제 실험에서 의미 명령을 작업 ID 임베딩으로 대체하면 평균 성공률이 97.7%에서 95.4%로, LIBERO-Goal은 97.4%에서 95.8%로 하락하여, 자연어가 제공하는 세밀한 정보가 폐집합 작업 정체성을 초과하며 경량 인코더가 이러한 정보를 충분히 담을 수 있음을 증명합니다.

## 실험 및 결과

LIBERO 벤치마크에서 TurboVLA는 0.2B 파라미터, 0.9GB VRAM, 31.2ms 지연 시간으로 97.7% 평균 성공률을 달성하여 모든 비교 방법을 능가합니다. 효율성 우위가 특히 두드러집니다: OpenVLA는 7.5B 파라미터, 14.9GB VRAM, 202.9ms 지연 시간으로 76.5% 성공률에 그칩니다; π₀.₅는 3.4B 파라미터, 12.8GB VRAM, 93.6ms 지연 시간으로 96.9%를 달성합니다. TurboVLA는 성공률에서 앞서면서도 지연 시간은 약 3배 감소(표 내 수치 93.6→31.2 기준), VRAM은 약 14배 감소(표 내 수치 12.8→0.9 기준)합니다.

| 지표 | TurboVLA | π₀.₅ | OpenVLA | Diffusion Policy |
|---|---|---|---|---|
| 파라미터 (B) | 0.2 | 3.4 | 7.5 | 0.3 |
| VRAM (GB) | 0.9 | 12.8 | 14.9 | 1.1 |
| 지연 시간 (ms) | 31.2 | 93.6 | 202.9 | 924.8 |
| LIBERO 평균 성공률 | 97.7% | 96.9% | 76.5% | 72.4% |

RoboTwin 2.0에서 TurboVLA는 0.4B 파라미터, 43.4ms 지연 시간으로 60.2% 평균 성공률을 달성하여 π₀.₅의 57.0%와 DP3의 55.2%를 능가합니다. 실제 세계 AgileX Piper 플랫폼의 네 가지 작업 성공률은 각각 92.5%, 80%, 90%, 87.5%로 모두 π₀.₅보다 우수합니다.

절제 실험의 핵심 발견: 언어를 제거하면 평균 성공률이 97.7%에서 70.8%로, LIBERO-Goal은 97.4%에서 11.6%로 급락하여 정책이 시각적 사전 지식만으로는 작동할 수 없음을 증명합니다; 상호작용 깊이 N=6이 최적이며, N=8은 96.6%로 약간 하락합니다; 동작 시야 H=12가 최적이며, H=15는 95.6%로 하락합니다.

## 경계 및 한계

RoboTwin 2.0 실험은 계산 예산 제한으로 공식 클린 데모 데이터만 사용하고 무작위 장면 데이터는 포함하지 않았습니다; 또한 VLA-Adapter나 StarVLA 프레임워크 외의 강화 기술도 도입하지 않았습니다. 실제 세계 평가는 네 가지 대표 작업만 다루며 더 넓은 시나리오로 확장되지 않았습니다. TurboVLA는 주로 구체적인 실행 수준 명령을 대상으로 하며, 고수준 작업 계획에 필요한 복잡한 의미 이해와 추론 능력을 갖추지 못했고, 개방형 언어 생성과 작업 수준 계획은 그 능력 범위에 포함되지 않습니다. 논문은 더 복잡한 장기 작업이나 비구조화 환경에서의 성능 경계를 명확히 제시하지 않습니다.

## 엔지니어링 시사점

재현 시 세 가지 핵심 사항을 먼저 확인해야 합니다: 첫째, 상호작용 모듈 초기화 가중치는 반드시 Grounding DINO 사전 훈련 특징 강화 가중치에서 가져와야 하며, 직접 무작위 초기화하면 보고된 양방향 상호작용 이득을 얻지 못할 수 있습니다; 둘째, 풀링 임베딩이 아닌 전체 명령 토큰 시퀀스를 유지해야 하며, 이는 언어 정보 유효성의 핵심으로, 절제 실험에서 작업 ID 임베딩은 평균 성공률 2.3% 손실을 초래합니다; 셋째, 동작 시야 H=12와 상호작용 깊이 N=6은 용량과 효율의 균형점이며, H=15나 N=8은 오히려 성능이 하락합니다.

가장 함정에 빠지기 쉬운 부분은 RoboTwin 2.0의 데이터 구성입니다—논문은 공식 클린 데모만 사용하고 무작위 장면 데이터를 포함하지 않는다고 명시했으며, 무작위 장면 데이터를 혼합하면 훈련 분포가 이동하여 성공률을 재현하지 못할 수 있습니다. 추론 시 지연 시간 측정은 멀티모달 입력에서 동작 블록 생성까지의 시간이며, 배치 크기 1 기준입니다. 자기회귀 토큰 생성 방식으로 측정하면 다른 수치가 나옵니다. 실제 세계 미세 조정은 LIBERO 사전 훈련 체크포인트에서 초기화하며, 4×65 원격 조작 데모, 12.5k 스텝으로 진행되며, 이 전이 경로는 참고할 가치가 있습니다.
