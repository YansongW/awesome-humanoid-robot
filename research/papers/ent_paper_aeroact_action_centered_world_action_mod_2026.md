---
$id: ent_paper_aeroact_action_centered_world_action_mod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight'
  zh: 'AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight'
  ko: 'AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight'
summary:
  en: Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences
    of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person
    views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level
    waypoints, or instantaneous.
  zh: AeroAct 是首个在真实世界飞行中实例化的动作中心世界-动作模型（WAM），用于语言条件四旋翼飞行。它基于 Wan2.1-1.3B 视频扩散 Transformer，在部署时不生成未来视频，而是仅解码局部五阶轨迹参数块，未来视觉预测仅作为训练时的密集辅助监督。核心贡献在于将视频中心
    WAM 的推理成本与误差累积问题，通过动作中心设计与块状因果掩码在架构层面化解。
  ko: Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences
    of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person
    views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level
    waypoints, or instantaneous.
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
- aeroact
- action
- centered
- world
- action
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.14997 AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor '
  url: https://arxiv.org/abs/2607.14997
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

AeroAct 是首个在真实世界飞行中实例化的动作中心世界-动作模型（WAM），用于语言条件四旋翼飞行。它基于 Wan2.1-1.3B 视频扩散 Transformer，在部署时不生成未来视频，而是仅解码局部五阶轨迹参数块，未来视觉预测仅作为训练时的密集辅助监督。核心贡献在于将视频中心 WAM 的推理成本与误差累积问题，通过动作中心设计与块状因果掩码在架构层面化解。

## 它改变了什么

空中视觉-语言导航与 VLA 方法长期受困于一个根本矛盾：动作空间要么是离散航点或瞬时速度指令，缺乏对“飞行动作如何改变未来观测”的监督；要么是视频中心 WAM，自回归生成未来视频的推理延迟与视觉误差累积，使其在实时飞行中不可用。AeroAct 真正改变的是这个权衡——它把“预测未来”从部署时的必需计算，降级为训练时的辅助监督信号，从而在保留世界模型语义理解能力的同时，将推理延迟压缩到可飞行的范围。

这个改变不是简单的工程优化，而是对 WAM 设计哲学的修正：世界模型的价值不在于测试时生成视频，而在于训练时迫使模型学习动作与视觉后果的耦合。AeroAct 用块状因果掩码实现这一点——动作流在部署时自回归解码，未来视觉 token 仅在训练时参与梯度传播。这使得 4 步去噪下推理时间从 0.296 s 降至 0.184 s（节省 37.8%），首次让 WAM 在真实四旋翼上以闭环方式执行语言指令。

## 方法拆解

### 问题公式化
- 观测历史 𝒪_t^h = (o_{t-(h-1)Δ}, …, o_t)，h 为参考帧数，Δ 为时间步长
- 预测动作块 a_{t:t+p-1} 长度 p，实现中 Δ=3，p=24
- 统一模型 g_Θ 同时做动作预测与视觉后果建模，每块含 K=8 个未来视觉帧和 24 个低层动作步

### 架构设计
- 视频 VAE 编码片段为时空潜在 token，经 3D RoPE 位置编码后分为参考 token T_o 和未来 token T_f
- 本体感觉与动作块经 MLP 编码为状态 token T_s 和动作 token T_a（隐藏尺寸 128 和 256）
- 指令经预训练文本编码器编码为语言 token T_l，作为交叉注意力上下文
- 非语言 token 拼接为 T_t=[T_s;T_o;T_a;T_f]

### 块状因果掩码
- 状态和参考 token 不能关注预测 token
- 动作 token 只关注状态、参考和动作 token
- 未来视觉 token 关注所有 token
- 推理时省略 T_f，只解码动作流，无需测试时视频生成

### 动作空间
- 每个动作参数化局部轨迹段，每维为五阶多项式 p_μ^l(t)=α_0+α_1 t+α_2 t²+α_3 t³+α_4 t⁴+α_5 t⁵
- 动作 a=[r,θ,ψ,v_end^{l⊤},a_end^{l⊤}]^⊤∈ℝ⁹，指定 T=2 s 局部轨迹段端点
- 本体感觉输入 s=[v^{l⊤},a^{l⊤},u_z^{l⊤}]^⊤∈ℝ⁹（局部速度、加速度、body-z 单位向量）

### 自引导（Self-Guidance）
- 当推理 n+1 在推理 n 的块过期前开始，两块时间重叠
- 去噪时用前一块对应后缀替换新样本前缀速度，只采样剩余后缀
- 不改变模型架构，仅约束采样器使低层控制器获得时间一致的轨迹参考

### 训练目标
L(Θ) = L_act + λ_vis L_vis，其中 L_act 和 L_vis 分别为动作和未来帧潜在 token 的扩散/流匹配噪声或速度场预测的均方误差。

### 数据管线
- DiffAero 提供共享动力学与控制接口，两个渲染分支：Isaac Lab（真实光照/材质但场景多样性受限）与 3DGS（高斯溅射渲染，易扩展场景但近距离几何保真度较低）
- 三类仿真演示：Isaac tracking、Isaac reaching、3DGS reaching
- 真实数据：手持设备（鱼眼相机 + Intel RealSense T265 + 轻量计算机），T265 估计里程计并转换为模拟四旋翼位姿

## 关键创新

1. **动作中心 WAM 设计**：首次将视频扩散 Transformer 适配到空中导航，同时保持部署时无视频生成。这不是简单的“砍掉视频分支”，而是通过块状因果掩码在架构层面保证动作流可自回归解码，未来视觉 token 仅作为训练监督。这解决了视频中心 WAM 推理昂贵与误差累积的根本矛盾。

2. **自引导采样器约束**：当推理块时间重叠时，用前一块的对应后缀替换新样本的前缀速度，只采样剩余后缀。这是一个不改变模型架构的采样器级创新，直接解决低层控制器对轨迹时间一致性的需求，避免了块间不连续导致的抖动。

3. **双分支仿真数据管线**：Isaac Lab 分支提供高保真光照/材质/阴影，3DGS 分支提供场景与物体多样性。这种互补设计在 900 K 仿真片段规模下，同时保证了视觉真实性与语义多样性，是真实世界泛化的关键支撑。

## 实验与结果

### 闭环仿真（Isaac Lab，20 episodes）
| 配置 | Success | Collision |
|---|---|---|
| AeroAct tracking 1帧 | 20.0 | 90.0 |
| AeroAct searching 1帧 | 90.0 | 10.0 |
| AeroAct tracking 9帧 | 100.0 | 0.0 |
| AeroAct searching 9帧 | 100.0 | 0.0 |
| AeroAct-FT tracking 9帧 | 95.0 | 0.0 |
| AeroAct-FT searching 9帧 | 100.0 | 0.0 |

### 未见目标物体搜索（表2）
| 配置 | Avg final dist | Success | Collision |
|---|---|---|---|
| AeroAct 1帧 | 3.819 | 75.0 | 25.0 |
| AeroAct 9帧 | 1.983 | 100.0 | 0.0 |
| AeroAct-FT 9帧 | 1.988 | 100.0 | 0.0 |

### 频率与参考帧消融（表3，跟踪）
| 配置 | View succ | In-view | Centered | Dist | Coll |
|---|---|---|---|---|---|
| 1帧, 1 Hz | 20.0 | 55.6 | 21.8 | 7.902 | 90.0 |
| 9帧, 1 Hz | 100.0 | 100.0 | 64.2 | 3.436 | 0.0 |
| 9帧, 2 Hz | 100.0 | 99.3 | 77.0 | 2.245 | 0.0 |
| 9帧, 5 Hz | 100.0 | 98.7 | 78.7 | 2.375 | 5.0 |

### 真实世界
- 手持设备收集 858 条轨迹、332,429 帧、约 3 小时数据
- 真实飞行平台：OddityRC 35Pro + Intel RealSense D435i + Radxa ROCK 5C，运动捕捉系统做状态测量
- 推理延迟约 0.8 s，ZeroMQ 通信，OM-MPC 轨迹跟踪
- 指令“fly to the yellow foam mat”成功生成可行飞行指令并导航接近目标

关键发现：9 参考帧（2.4 s 视觉上下文）是性能分水岭，1 帧配置在跟踪任务中几乎不可用（Success 20.0，Collision 90.0），而 9 帧配置达到 100.0% Success 与 0.0% Collision。频率从 1 Hz 到 5 Hz 对 9 帧配置影响有限，说明模型对重规划频率不敏感。

## 边界与局限

- 真实实验限于短室内轨迹，时间上下文足以处理单阶段目标到达，但不足以处理需要多个语义子目标、恢复行为或长时程记忆的复杂指令
- 真实部署依赖离板推理（工作站通过 ZeroMQ 通信），因视频扩散骨干的计算成本，机载推理未实现
- 论文未明确在更激进飞行动力学（如高速机动、强风扰动）下的鲁棒性表现
- 真实数据收集采用手持设备而非实际飞行，可能引入与真实飞行不同的视觉-运动耦合分布
- 3DGS 渲染分支在近距离几何和光照保真度上低于 Isaac Lab，可能影响近距离操作性能

## 工程启示

复现或下游使用时，先核对以下关键点：

1. **参考帧数是第一优先级超参数**：1 帧与 9 帧的性能差距是数量级的（跟踪 Success 从 20.0 到 100.0），任何消融实验应首先确认视觉上下文长度是否足够。2.4 s 视觉上下文是当前配置的下限，更复杂任务需要更长上下文。

2. **自引导是部署必需而非可选**：当推理频率高于块过期时间时，必须启用自引导采样器约束，否则低层控制器会收到时间不一致的轨迹参考。实现时注意公式(6a)(6b)的前缀替换逻辑，这是最容易出错的地方。

3. **数据管线是性能瓶颈**：900 K 仿真片段（500 K tracking + 200 K Isaac reaching + 200 K 3DGS reaching）是预训练的基础，但真实数据仅 858 条轨迹。如果下游场景与训练分布差异大，建议优先扩展 3DGS 分支的场景多样性，而非增加 Isaac Lab 数据量。

4. **推理延迟预算**：单张 RTX 5090 上 4 步去噪 + 禁用视频预测为 0.184 s，VRAM 约 4,500 MB。如果目标平台算力更低，先检查视频 VAE 编码是否可裁剪，这是最大的计算热点。

5. **最容易踩坑**：块状因果掩码的实现细节——动作 token 不能关注未来视觉 token，但未来视觉 token 可以关注动作 token。这个不对称性在实现注意力掩码时极易写反，会导致训练时信息泄漏或部署时动作流无法解码。

## Overview
Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level waypoints, or instantaneous velocity commands, which provide limited supervision about how flight actions change future observations. We present AeroAct, an action-centered world-action model (WAM) for quadrotor navigation. To the best of our knowledge, AeroAct is the first WAM instantiated and demonstrated for real-world aerial flight. The model adapts a pretrained video diffusion Transformer to predict local trajectory-action chunks from egocentric visual history, proprioception, and language. Future first-person frames are used during training as dense consequence supervision, while deployment directly decodes actions without generating future video. To obtain aligned visual, state, language, and dynamically feasible action data, we build a DiffAero-based pipeline with complementary Isaac Lab and 3D Gaussian splatting renderers. We further introduce a low-cost handheld collection device that couples camera observations with motion estimates to recreate flight-like egocentric trajectories, and a self-guidance procedure that improves temporal consistency across overlapping trajectory chunks. Closed-loop simulation and real-world experiments show that temporal visual context improves target tracking and object-search performance, and that WAM-based policies can be executed on a physical quadrotor.

## 参考
- https://arxiv.org/abs/2607.14997

## 개요

AeroAct는 실제 비행에서 처음으로 구현된 행동 중심 세계-행동 모델(WAM)로, 언어 조건 쿼드로터 비행을 위한 모델이다. Wan2.1-1.3B 비디오 확산 Transformer를 기반으로 하며, 배포 시 미래 비디오를 생성하지 않고 로컬 5차 궤적 파라미터 블록만 디코딩하며, 미래 시각 예측은 훈련 시의 밀집 보조 감독으로만 사용된다. 핵심 기여는 비디오 중심 WAM의 추론 비용과 오류 누적 문제를 행동 중심 설계와 블록형 인과 마스크를 통해 아키텍처 수준에서 해결한 것이다.

## 무엇을 바꾸었는가

공중 시각-언어 내비게이션과 VLA 방법은 오랫동안 근본적인 모순에 시달려 왔다: 행동 공간이 이산 웨이포인트나 순간 속도 명령으로 제한되어 "비행 행동이 미래 관측을 어떻게 바꾸는지"에 대한 감독이 부족하거나, 비디오 중심 WAM으로서 자기회귀적으로 미래 비디오를 생성하는 추론 지연과 시각 오류 누적으로 실시간 비행에서 사용할 수 없었다. AeroAct가 진정으로 바꾼 것은 이 트레이드오프이다——"미래 예측"을 배포 시 필수 계산에서 훈련 시의 보조 감독 신호로 격하시켜, 세계 모델의 의미 이해 능력을 유지하면서 추론 지연을 비행 가능한 범위로 압축했다.

이 변화는 단순한 엔지니어링 최적화가 아니라 WAM 설계 철학에 대한 수정이다: 세계 모델의 가치는 테스트 시 비디오 생성에 있는 것이 아니라, 훈련 시 모델이 행동과 시각 결과의 결합을 학습하도록 강제하는 데 있다. AeroAct는 블록형 인과 마스크로 이를 구현한다——행동 스트림은 배포 시 자기회귀적으로 디코딩되고, 미래 시각 토큰은 훈련 시에만 그래디언트 전파에 참여한다. 이를 통해 4단계 노이즈 제거에서 추론 시간이 0.296초에서 0.184초로 감소하여(37.8% 절약), 처음으로 WAM이 실제 쿼드로터에서 폐루프 방식으로 언어 명령을 실행할 수 있게 되었다.

## 방법 분해

### 문제 공식화
- 관측 이력 𝒪_t^h = (o_{t-(h-1)Δ}, …, o_t), h는 참조 프레임 수, Δ는 시간 스텝
- 예측 행동 블록 a_{t:t+p-1} 길이 p, 구현에서 Δ=3, p=24
- 통합 모델 g_Θ는 행동 예측과 시각 결과 모델링을 동시에 수행하며, 각 블록은 K=8개의 미래 시각 프레임과 24개의 저수준 행동 스텝을 포함

### 아키텍처 설계
- 비디오 VAE가 클립을 시공간 잠재 토큰으로 인코딩하고, 3D RoPE 위치 인코딩 후 참조 토큰 T_o와 미래 토큰 T_f로 분리
- 고유수용감각과 행동 블록은 MLP를 통해 상태 토큰 T_s와 행동 토큰 T_a로 인코딩(은닉 크기 128 및 256)
- 명령은 사전 훈련된 텍스트 인코더를 통해 언어 토큰 T_l로 인코딩되어 교차 주의 컨텍스트로 사용
- 비언어 토큰은 T_t=[T_s;T_o;T_a;T_f]로 연결

### 블록형 인과 마스크
- 상태 및 참조 토큰은 예측 토큰을 주의할 수 없음
- 행동 토큰은 상태, 참조 및 행동 토큰만 주의
- 미래 시각 토큰은 모든 토큰을 주의
- 추론 시 T_f를 생략하고 행동 스트림만 디코딩하여 테스트 시 비디오 생성 불필요

### 행동 공간
- 각 행동은 로컬 궤적 세그먼트를 파라미터화하며, 각 차원은 5차 다항식 p_μ^l(t)=α_0+α_1 t+α_2 t²+α_3 t³+α_4 t⁴+α_5 t⁵
- 행동 a=[r,θ,ψ,v_end^{l⊤},a_end^{l⊤}]^⊤∈ℝ⁹, T=2초 로컬 궤적 세그먼트 끝점 지정
- 고유수용감각 입력 s=[v^{l⊤},a^{l⊤},u_z^{l⊤}]^⊤∈ℝ⁹(로컬 속도, 가속도, body-z 단위 벡터)

### 자기 유도(Self-Guidance)
- 추론 n+1이 추론 n의 블록 만료 전에 시작되면 두 블록이 시간적으로 겹침
- 노이즈 제거 시 이전 블록의 해당 접미사로 새 샘플의 접두사 속도를 대체하고 나머지 접미사만 샘플링
- 모델 아키텍처를 변경하지 않고 샘플러만 제약하여 저수준 제어기가 시간적으로 일관된 궤적 참조를 얻도록 함

### 훈련 목표
L(Θ) = L_act + λ_vis L_vis, 여기서 L_act와 L_vis는 각각 행동 및 미래 프레임 잠재 토큰의 확산/흐름 매칭 노이즈 또는 속도장 예측의 평균 제곱 오차.

### 데이터 파이프라인
- DiffAero는 공유 동역학 및 제어 인터페이스를 제공하며, 두 가지 렌더링 분기: Isaac Lab(실제 조명/재질이지만 장면 다양성 제한) 및 3DGS(가우시안 스플래팅 렌더링, 장면 확장 용이하지만 근거리 기하학적 충실도 낮음)
- 세 가지 시뮬레이션 데모: Isaac tracking, Isaac reaching, 3DGS reaching
- 실제 데이터: 핸드헬드 장치(어안 카메라 + Intel RealSense T265 + 경량 컴퓨터), T265가 오도메트리를 추정하고 시뮬레이션된 쿼드로터 자세로 변환

## 핵심 혁신

1. **행동 중심 WAM 설계**: 비디오 확산 Transformer를 공중 내비게이션에 최초로 적용하면서 배포 시 비디오 생성 없이 유지. 이는 단순한 "비디오 분기 제거"가 아니라 블록형 인과 마스크를 통해 아키텍처 수준에서 행동 스트림이 자기회귀적으로 디코딩될 수 있도록 보장하고, 미래 시각 토큰은 훈련 감독으로만 사용. 비디오 중심 WAM의 추론 비용과 오류 누적이라는 근본적 모순을 해결.

2. **자기 유도 샘플러 제약**: 추론 블록이 시간적으로 겹칠 때 이전 블록의 해당 접미사로 새 샘플의 접두사 속도를 대체하고 나머지 접미사만 샘플링. 모델 아키텍처를 변경하지 않는 샘플러 수준의 혁신으로, 저수준 제어기의 궤적 시간 일관성 요구를 직접 해결하고 블록 간 불연속으로 인한 떨림을 방지.

3. **이중 분기 시뮬레이션 데이터 파이프라인**: Isaac Lab 분기는 고충실도 조명/재질/그림자를 제공하고, 3DGS 분기는 장면 및 객체 다양성을 제공. 이러한 상보적 설계는 900K 시뮬레이션 클립 규모에서 시각적 현실성과 의미적 다양성을 동시에 보장하며, 실제 세계 일반화의 핵심 지원.

## 실험 및 결과

### 폐루프 시뮬레이션(Isaac Lab, 20 에피소드)
| 구성 | Success | Collision |
|---|---|---|
| AeroAct tracking 1프레임 | 20.0 | 90.0 |
| AeroAct searching 1프레임 | 90.0 | 10.0 |
| AeroAct tracking 9프레임 | 100.0 | 0.0 |
| AeroAct searching 9프레임 | 100.0 | 0.0 |
| AeroAct-FT tracking 9프레임 | 95.0 | 0.0 |
| AeroAct-FT searching 9프레임 | 100.0 | 0.0 |

### 미발견 목표 객체 검색(표2)
| 구성 | Avg final dist | Success | Collision |
|---|---|---|---|
| AeroAct 1프레임 | 3.819 | 75.0 | 25.0 |
| AeroAct 9프레임 | 1.983 | 100.0 | 0.0 |
| AeroAct-FT 9프레임 | 1.988 | 100.0 | 0.0 |

### 주파수 및 참조 프레임 소거(표3, 추적)
| 구성 | View succ | In-view | Centered | Dist | Coll |
|---|---|---|---|---|---|
| 1프레임, 1 Hz | 20.0 | 55.6 | 21.8 | 7.902 | 90.0 |
| 9프레임, 1 Hz | 100.0 | 100.0 | 64.2 | 3.436 | 0.0 |
| 9프레임, 2 Hz | 100.0 | 99.3 | 77.0 | 2.245 | 0.0 |
| 9프레임, 5 Hz | 100.0 | 98.7 | 78.7 | 2.375 | 5.0 |

### 실제 세계
- 핸드헬드 장치로 858개 궤적, 332,429프레임, 약 3시간 데이터 수집
- 실제 비행 플랫폼: OddityRC 35Pro + Intel RealSense D435i + Radxa ROCK 5C, 모션 캡처 시스템으로 상태 측정
- 추론 지연 약 0.8초, ZeroMQ 통신, OM-MPC 궤적 추적
- "fly to the yellow foam mat" 명령이 실행 가능한 비행 명령을 성공적으로 생성하고 목표에 접근

핵심 발견: 9개 참조 프레임(2.4초 시각 컨텍스트)이 성능의 분기점이며, 1프레임 구성은 추적 작업에서 거의 사용 불가능(Success 20.0, Collision 90.0)하지만 9프레임 구성은 100.0% Success와 0.0% Collision 달성. 주파수가 1Hz에서 5Hz로 증가해도 9프레임 구성에 미치는 영향이 제한적이며, 모델이 재계획 주파수에 민감하지 않음을 시사.

## 경계 및 한계

- 실제 실험은 짧은 실내 궤적으로 제한되며, 시간 컨텍스트가 단일 단계 목표 도달을 처리하기에 충분하지만 여러 의미적 하위 목표, 복구 행동 또는 장기 기억이 필요한 복잡한 명령을 처리하기에는 부족
- 실제 배포는 오프보드 추론(워크스테이션이 ZeroMQ로 통신)에 의존하며, 비디오 확산 백본의 계산 비용으로 인해 온보드 추론은 구현되지 않음
- 논문은 더 공격적인 비행 동역학(고속 기동, 강풍 교란 등)에서의 강건성 성능을 명시하지 않음
- 실제 데이터 수집은 실제 비행이 아닌 핸드헬드 장치로 수행되어 실제 비행과 다른 시각-운동 결합 분포를 도입할 수 있음
- 3DGS 렌더링 분기는 근거리 기하학 및 조명 충실도에서 Isaac Lab보다 낮아 근거리 조작 성능에 영향을 줄 수 있음

## 엔지니어링 시사점

재현 또는 다운스트림 사용 시 다음 핵심 사항을 먼저 확인:

1. **참조 프레임 수는 최우선 하이퍼파라미터**: 1프레임과 9프레임의 성능 차이는 규모의 차이(추적 Success 20.0에서 100.0)이며, 모든 소거 실험은 먼저 시각 컨텍스트 길이가 충분한지 확인해야 함. 2.4초 시각 컨텍스트는 현재 구성의 하한이며, 더 복잡한 작업은 더 긴 컨텍스트가 필요.

2. **자기 유도는 배포 필수 사항이지 선택 사항이 아님**: 추론 주파수가 블록 만료 시간보다 높으면 자기 유도 샘플러 제약을 반드시 활성화해야 하며, 그렇지 않으면 저수준 제어기가 시간적으로 일관되지 않은 궤적 참조를 받게 됨. 구현 시 수식(6a)(6b)의 접두사 대체 로직에 주의——가장 오류가 발생하기 쉬운 부분.

3. **데이터 파이프라인이 성능 병목**: 900K 시뮬레이션 클립(500K tracking + 200K Isaac reaching + 200K 3DGS reaching)이 사전 훈련의 기반이지만, 실제 데이터는 858개 궤적에 불과. 다운스트림 장면이 훈련 분포와 크게 다르면 Isaac Lab 데이터 양을 늘리는 대신 3DGS 분기의 장면 다양성을 우선 확장하는 것이 좋음.

4. **추론 지연 예산**: 단일 RTX 5090에서 4단계 노이즈 제거 + 비디오 예측 비활성화 시 0.184초, VRAM 약 4,500MB. 대상 플랫폼의 연산 능력이 더 낮으면 비디오 VAE 인코딩을 잘라낼 수 있는지 먼저 확인——가장 큰 계산 핫스팟.

5. **가장 함정에 빠지기 쉬운 부분**: 블록형 인과 마스크 구현 세부 사항——행동 토큰은 미래 시각 토큰을 주의할 수 없지만, 미래 시각 토큰은 행동 토큰을 주의할 수 있음. 이 비대칭성은 주의 마스크 구현 시 매우 쉽게 반대로 작성되어 훈련 중 정보 누출 또는 배포 시 행동 스트림 디코딩 실패를 초래할 수 있음.
