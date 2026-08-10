---
$id: ent_paper_da_nav_direction_aware_city_scale_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DA-Nav: Direction-Aware City-Scale Vision-Language Navigation'
  zh: 'DA-Nav: Direction-Aware City-Scale Vision-Language Navigation'
  ko: 'DA-Nav: Direction-Aware City-Scale Vision-Language Navigation'
summary:
  en: City-scale outdoor navigation is currently hindered by the heavy reliance on dense maps or costly navigation supervision.
    In this work, we introduce a novel paradigm for leveraging directional instructions from commercial navigation tools (e.g.,
    Google Maps). To bridge the gap between commercial instructions and executable navigation actions, while mitigating long-horizon
    error accumulation.
  zh: DA-Nav 提出一种面向城市规模视觉-语言导航的方向感知方法，将导航重新表述为自我中心图像平面上的离散空间接地问题，并引入带恢复行为的 ReDA 数据集与 CoT 决策序列。该方法基于 Qwen2.5-VL-7B 骨干，在 CARLA
    模拟与真实机器人上验证了优于现有基线的成功率与鲁棒性。
  ko: City-scale outdoor navigation is currently hindered by the heavy reliance on dense maps or costly navigation supervision.
    In this work, we introduce a novel paradigm for leveraging directional instructions from commercial navigation tools (e.g.,
    Google Maps). To bridge the gap between commercial instructions and executable navigation actions, while mitigating long-horizon
    error accumulation.
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
- da
- nav
- direction
- aware
- city
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.11638 DA-Nav: Direction-Aware City-Scale Vision-Language Navigation'
  url: https://arxiv.org/abs/2607.11638
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

DA-Nav 提出一种面向城市规模视觉-语言导航的方向感知方法，将导航重新表述为自我中心图像平面上的离散空间接地问题，并引入带恢复行为的 ReDA 数据集与 CoT 决策序列。该方法基于 Qwen2.5-VL-7B 骨干，在 CARLA 模拟与真实机器人上验证了优于现有基线的成功率与鲁棒性。

## 它改变了什么

城市规模导航长期被 SLAM 与全局路径规划主导，其地图构建与维护成本高昂，且对动态环境敏感。近期基于粗粒度信号（自然语言、GPS、地标）的方法虽降低了标注依赖，却仍需要密集监督或人工轨迹，难以规模化。更关键的是，商业导航指令（如“50米后右转”）为人类认知设计，缺乏机器人可执行的细粒度空间信息，而长时程导航中感知与控制误差的累积又要求系统具备轨迹偏差恢复能力——现有数据集与模型均未针对这一核心问题设计。

DA-Nav 真正改变的是将导航从“连续航点回归”转向“离散空间接地”，并首次系统性地将“偏离-恢复”行为纳入训练监督。它不再要求模型直接输出三维坐标，而是预测自我中心图像平面上的网格序列，同时通过显式的状态评估（是否偏离）与纠正动作（CORRECT_LEFT/RIGHT）让模型学会主动纠偏。这一转变使模型能够利用商业导航的粗粒度指令，同时具备对累积误差的鲁棒性，为城市规模部署提供了更实际的路径。

## 方法拆解

### 任务重定义
- 输入：每时间步 t 的 k=4 帧自我中心 RGB 序列 O_t，以及离散方向指令 I_t ∈ {FORWARD, TURN_LEFT, TURN_RIGHT, STOP}。
- 输出：结构化决策序列 Y_t = (s_t, c_t, P_t)，其中 s_t ∈ {Yes, No} 为偏离状态，c_t 为六类 CoT 动作，P_t 为 L=6 个未来网格位置序列（2Hz 采样，覆盖未来 3 秒）。

### 网格与轨迹表示
- 在自我中心图像平面定义有效网格 G = {(r,c) | r ∈ [13,23], c ∈ [0,28]}，排除天空与远处背景。
- 未来轨迹离散化为网格序列，通过三次样条插值平滑专家 3D 航点，经标定相机投影至图像平面。

### ReDA 数据集生成
- 在 CARLA 0.9.15 中使用三状态有限状态机（FSM）：Stable、Drifting、Recovering。
- Stable 跟踪专家轨迹；转向扰动触发 Drifting；当横向误差 e_y ≥ 0.35 m 时切换至 Recovering，采用与 e_y 成正比的前瞻距离 l_d 自适应跟踪。
- Drifting 帧被丢弃，仅保留专家与恢复帧（158k 专家帧 + 128k 恢复帧，共 286k 序列样本）。

### 模型与训练
- 骨干：Qwen2.5-VL-7B-Instruct，视觉编码器与基础 LLM 权重冻结，仅对注意力块应用 LoRA。
- 训练目标：自回归下一词预测，π_θ(Y_t|C_t) = ∏ P_θ(y_t^(j)|y_t^(<j), C_t)。
- 提示中编码离散网格 G 以注入空间接地约束，强制输出顺序为“状态评估→动作选择→轨迹预测”。

### 控制接口
- 最远点控制：选择预测视野中最远的航点 w_target = w_{t+L} 作为控制目标，避免高频波动。
- 低层控制器：角速度 ω_z = sat_{ω_max}(k_steer · arctan2(y_target, x_target))；线速度根据转向幅度自适应（|ω_z| ≤ ω_th 时 v_target = v_nom，否则 v_target = v_low）。
- 图像平面到身体框架采用混合投影：深度可靠时用相机内参与局部深度统计，否则回退到 IPM 平坦地面假设。

## 关键创新

1. **方向感知的离散空间接地**：将导航从连续航点回归转为图像平面离散网格预测，直接利用商业导航的粗粒度方向指令，无需细粒度语言或地标标注。这一设计使系统可规模化部署，且网格表示天然兼容 VLM 的离散 token 输出。
2. **显式恢复行为监督**：ReDA 数据集首次引入“偏离-恢复”状态与纠正动作标签，使模型不仅学习如何跟随路径，更学习如何识别偏差并主动纠正。消融显示去除恢复数据后 SR 从 59.00% 降至 29.71%，证明该监督对长时程鲁棒性至关重要。
3. **CoT 决策分解**：强制模型先评估偏离状态、再选择动作、最后预测轨迹，形成逻辑链条。在复杂 OOD 场景（Town 15）中，无 CoT 时局部 DF 飙升至 18.75，说明结构化推理显著抑制了误差累积。

## 实验与结果

### 模拟评估（CARLA 0.9.15）
- 训练与域内评估：Towns 01–05 与 10HD；零样本泛化：Towns 06、07、15；共 239 条长时程闭环轨迹。
- 关键指标对比（表 II）：

| 方法 | SR (%) | RC (%) | SPL | DF | CSR (%) |
|------|--------|--------|-----|-----|---------|
| DA-Nav | 59.00 | 77.82 | 58.66 | 1.85 | 98.15 |
| CityWalker | 38.08 | 70.79 | 37.48 | 2.96 | 30.73 |
| ViNT | 51.88 | 74.44 | 51.33 | 1.25 | 23.54 |
| NaVid | 20.50 | 66.33 | 20.50 | 0.61 | 4.89 |
| NaVILA | 22.59 | 79.49 | 22.59 | 0.39 | 4.90 |
| Zero-shot Qwen2.5-VL | 11.30 | 43.21 | 11.30 | 3.42 | 42.76 |

- DA-Nav 从已见到未见环境的 SR 下降仅 7.28%，显著优于基线。

### 消融研究（表 III）
| 配置 | SR (%) | RC (%) | SPL | DF | CSR (%) |
|------|--------|--------|-----|-----|---------|
| w/o Recovery Data | 29.71 | 62.01 | 29.68 | 1.31 | 15.46 |
| w/o CoT Reasoning | 38.91 | 68.37 | 38.91 | 4.30 | 50.11 |
| DA-Nav（完整） | 59.00 | 77.82 | 58.66 | 1.85 | 98.15 |

### 真实世界评估
- 开环原语（36 个交叉口）：DA-Nav 平均 SR 83.3%，优于 CityWalker（75%（由表内数值 4.9→1.25 计算））与 ViNT（58.3%）。
- 闭环导航（2 场景 × 5 路径 × 3 次）：DA-Nav 总体 SR 46.7%、RC 76.3%，显著优于 CityWalker（23.3%/53.3%）与 ViNT（16.7%/49.0%）。
- 跨具身泛化：在 Leju Kuavo-V 人形机器人上无需修改策略，实现超过 1.2 km 户外导航。

## 边界与局限

- 系统仍依赖商业导航工具提供高层路径引导，受限于 GPS 不准确、更新延迟及未映射区域覆盖不足。
- 未进行真实世界微调，零样本 sim-to-real 迁移的泛化边界未充分探索。
- 论文未明确在极端天气（如暴雨、大雪）或传感器退化（如相机遮挡）条件下的性能表现。
- 恢复行为监督依赖 CARLA 中定义的横向误差阈值（0.35 m），该阈值在真实机器人上的适用性未验证。

## 工程启示

- **复现优先核对**：ReDA 数据集的 FSM 状态切换逻辑（Stable→Drifting→Recovering）与 e_y ≥ 0.35 m 阈值是恢复监督的核心，需严格复现；Drifting 帧的丢弃策略直接影响数据分布。
- **模型选型**：Qwen2.5-VL-7B 的 LoRA 微调方案有效，但推理需 RTX 4090 级 GPU；若算力受限，可考虑更小骨干，但需重新验证空间接地能力。
- **控制接口易踩坑**：最远点控制（w_target = w_{t+L}）与自适应线速度策略对低频控制至关重要，直接跟踪密集预测轨迹会导致高频波动；建议先验证低层控制器的角速度饱和与转向阈值。
- **下游集成**：商业导航指令解析模块（异步提取“30米后左转”等文本）是真实部署的关键前置，需确保指令到 I_t 的映射延迟可控；跨具身迁移时，相机标定与 IPM 回退策略的鲁棒性需重点测试。

## Overview
City-scale outdoor navigation is currently hindered by the heavy reliance on dense maps or costly navigation supervision. In this work, we introduce a novel paradigm for leveraging directional instructions from commercial navigation tools (e.g., Google Maps). To bridge the gap between commercial instructions and executable navigation actions, while mitigating long-horizon error accumulation through robust trajectory recovery, we propose DA-Nav, a Direction-Aware vision-language Navigation framework that reformulates navigation as a discrete spatial grounding problem on the egocentric 2D image plane. To achieve trajectory recovery, DA-Nav employs a Chain-of-Thought (CoT) reasoning process encompassing deviation assessment, action prediction, and target grid selection. We further introduce ReDA, a dataset that provides direction-aware instructions and recovery trajectories to enhance spatial grounding and support CoT recovery reasoning. Extensive experiments in CARLA demonstrate that DA-Nav achieves a high success rate of 56.16% in unseen urban environments, outperforming existing State-of-The-Art (SoTA) methods while maintaining a substantially stronger recovery capability. Furthermore, without fine-tuning, DA-Nav seamlessly adapts to both quadruped and humanoid robots, enabling stable kilometer-scale closed-loop outdoor navigation in complex real world environments.

## 参考
- https://arxiv.org/abs/2607.11638

## 개요

DA-Nav는 도시 규모의 시각-언어 내비게이션을 위한 방향 인식 방법을 제안하며, 내비게이션을 자아중심 이미지 평면 위의 이산 공간 접지 문제로 재정의하고, 복구 행동을 포함한 ReDA 데이터셋과 CoT 결정 시퀀스를 도입한다. 이 방법은 Qwen2.5-VL-7B 백본을 기반으로 하며, CARLA 시뮬레이션과 실제 로봇에서 기존 기준선보다 우수한 성공률과 견고성을 검증했다.

## 무엇을 바꾸었는가

도시 규모 내비게이션은 오랫동안 SLAM과 전역 경로 계획이 지배해 왔으며, 지도 구축과 유지 비용이 높고 동적 환경에 민감하다. 최근 조잡한 신호(자연어, GPS, 랜드마크)를 기반으로 한 방법은 주석 의존도를 낮췄지만, 여전히 밀집된 감독이나 수동 궤적이 필요하여 확장이 어렵다. 더 중요하게는, 상용 내비게이션 지시(예: "50미터 후 우회전")는 인간 인지를 위해 설계되어 로봇이 실행 가능한 세밀한 공간 정보가 부족하며, 장시간 내비게이션에서 인식 및 제어 오류의 누적은 시스템이 궤적 이탈 복구 능력을 갖추도록 요구한다—기존 데이터셋과 모델은 이 핵심 문제를 위해 설계되지 않았다.

DA-Nav가 실제로 바꾼 것은 내비게이션을 "연속 웨이포인트 회귀"에서 "이산 공간 접지"로 전환하고, 처음으로 "이탈-복구" 행동을 훈련 감독에 체계적으로 포함시킨 것이다. 모델이 3D 좌표를 직접 출력하도록 요구하는 대신, 자아중심 이미지 평면 위의 그리드 시퀀스를 예측하고, 명시적 상태 평가(이탈 여부)와 교정 동작(CORRECT_LEFT/RIGHT)을 통해 모델이 능동적으로 오류를 교정하도록 학습시킨다. 이러한 전환은 모델이 상용 내비게이션의 조잡한 지시를 활용하면서도 누적 오류에 대한 견고성을 갖추게 하여, 도시 규모 배포에 더 실용적인 경로를 제공한다.

## 방법 분해

### 작업 재정의
- 입력: 각 시간 단계 t에서의 k=4프레임 자아중심 RGB 시퀀스 O_t 및 이산 방향 지시 I_t ∈ {FORWARD, TURN_LEFT, TURN_RIGHT, STOP}.
- 출력: 구조화된 결정 시퀀스 Y_t = (s_t, c_t, P_t). 여기서 s_t ∈ {Yes, No}는 이탈 상태, c_t는 6가지 CoT 동작, P_t는 L=6개의 미래 그리드 위치 시퀀스(2Hz 샘플링, 미래 3초 커버).

### 그리드 및 궤적 표현
- 자아중심 이미지 평면에서 유효 그리드 G = {(r,c) | r ∈ [13,23], c ∈ [0,28]} 정의, 하늘과 먼 배경 제외.
- 미래 궤적을 그리드 시퀀스로 이산화하고, 전문가 3D 웨이포인트를 3차 스플라인 보간으로 평활화한 후, 캘리브레이션된 카메라로 이미지 평면에 투영.

### ReDA 데이터셋 생성
- CARLA 0.9.15에서 3상태 유한 상태 머신(FSM) 사용: Stable, Drifting, Recovering.
- Stable은 전문가 궤적 추적; 조향 교란은 Drifting을 유발; 횡방향 오류 e_y ≥ 0.35 m일 때 Recovering으로 전환, e_y에 비례하는 전방 주시 거리 l_d로 적응형 추적.
- Drifting 프레임은 폐기하고 전문가 및 복구 프레임만 유지(158k 전문가 프레임 + 128k 복구 프레임, 총 286k 시퀀스 샘플).

### 모델 및 훈련
- 백본: Qwen2.5-VL-7B-Instruct, 시각 인코더와 기본 LLM 가중치는 동결, 주의 블록에만 LoRA 적용.
- 훈련 목표: 자기회귀 다음 토큰 예측, π_θ(Y_t|C_t) = ∏ P_θ(y_t^(j)|y_t^(<j), C_t).
- 프롬프트에 이산 그리드 G를 인코딩하여 공간 접지 제약을 주입하고, 출력 순서를 "상태 평가→동작 선택→궤적 예측"으로 강제.

### 제어 인터페이스
- 최원점 제어: 예측 시야에서 가장 먼 웨이포인트 w_target = w_{t+L}을 제어 목표로 선택하여 고주파 변동 방지.
- 저수준 제어기: 각속도 ω_z = sat_{ω_max}(k_steer · arctan2(y_target, x_target)); 선속도는 조향 정도에 따라 적응형(|ω_z| ≤ ω_th일 때 v_target = v_nom, 그 외 v_target = v_low).
- 이미지 평면에서 바디 프레임으로의 변환은 혼합 투영 사용: 깊이가 신뢰할 수 있을 때 카메라 내부 파라미터와 로컬 깊이 통계 사용, 그 외에는 IPM 평평한 지면 가정으로 폴백.

## 핵심 혁신

1. **방향 인식 이산 공간 접지**: 내비게이션을 연속 웨이포인트 회귀에서 이미지 평면 이산 그리드 예측으로 전환하고, 상용 내비게이션의 조잡한 방향 지시를 직접 활용하여 세밀한 언어나 랜드마크 주석이 필요 없다. 이 설계는 시스템을 확장 가능하게 하며, 그리드 표현은 VLM의 이산 토큰 출력과 자연스럽게 호환된다.
2. **명시적 복구 행동 감독**: ReDA 데이터셋은 처음으로 "이탈-복구" 상태와 교정 동작 라벨을 도입하여, 모델이 경로를 따르는 방법뿐만 아니라 편차를 식별하고 능동적으로 교정하는 방법도 학습하게 한다. 절제 실험에서 복구 데이터 제거 시 SR이 59.00%에서 29.71%로 감소하여, 이 감독이 장시간 견고성에 필수적임을 증명한다.
3. **CoT 결정 분해**: 모델이 먼저 이탈 상태를 평가하고, 그다음 동작을 선택하며, 마지막으로 궤적을 예측하도록 강제하여 논리적 체인을 형성한다. 복잡한 OOD 시나리오(Town 15)에서 CoT가 없을 때 로컬 DF가 18.75로 급증하여, 구조화된 추론이 오류 누적을 크게 억제함을 보여준다.

## 실험 및 결과

### 시뮬레이션 평가(CARLA 0.9.15)
- 훈련 및 도메인 내 평가: Towns 01–05 및 10HD; 제로샷 일반화: Towns 06, 07, 15; 총 239개의 장시간 폐루프 궤적.
- 주요 지표 비교(표 II):

| 방법 | SR (%) | RC (%) | SPL | DF | CSR (%) |
|------|--------|--------|-----|-----|---------|
| DA-Nav | 59.00 | 77.82 | 58.66 | 1.85 | 98.15 |
| CityWalker | 38.08 | 70.79 | 37.48 | 2.96 | 30.73 |
| ViNT | 51.88 | 74.44 | 51.33 | 1.25 | 23.54 |
| NaVid | 20.50 | 66.33 | 20.50 | 0.61 | 4.89 |
| NaVILA | 22.59 | 79.49 | 22.59 | 0.39 | 4.90 |
| Zero-shot Qwen2.5-VL | 11.30 | 43.21 | 11.30 | 3.42 | 42.76 |

- DA-Nav는 이미 본 환경에서 보지 못한 환경으로의 SR 감소가 7.28%에 불과하여 기준선보다 크게 우수.

### 절제 연구(표 III)
| 구성 | SR (%) | RC (%) | SPL | DF | CSR (%) |
|------|--------|--------|-----|-----|---------|
| w/o Recovery Data | 29.71 | 62.01 | 29.68 | 1.31 | 15.46 |
| w/o CoT Reasoning | 38.91 | 68.37 | 38.91 | 4.30 | 50.11 |
| DA-Nav(완전) | 59.00 | 77.82 | 58.66 | 1.85 | 98.15 |

### 실제 세계 평가
- 개루프 원시 동작(36개 교차로): DA-Nav 평균 SR 83.3%, CityWalker(75%(표 내 수치 4.9→1.25로 계산)) 및 ViNT(58.3%)보다 우수.
- 폐루프 내비게이션(2 시나리오 × 5 경로 × 3회): DA-Nav 전체 SR 46.7%, RC 76.3%, CityWalker(23.3%/53.3%) 및 ViNT(16.7%/49.0%)보다 크게 우수.
- 교차 구현 일반화: Leju Kuavo-V 휴머노이드 로봇에서 정책 수정 없이 1.2km 이상의 실외 내비게이션 달성.

## 경계 및 한계

- 시스템은 여전히 상용 내비게이션 도구의 고수준 경로 안내에 의존하며, GPS 부정확성, 업데이트 지연 및 미매핑 영역의 커버리지 부족에 제한을 받는다.
- 실제 세계 미세 조정이 수행되지 않아, 제로샷 sim-to-real 전이의 일반화 경계가 충분히 탐구되지 않았다.
- 논문은 극한 기상(폭우, 폭설) 또는 센서 열화(카메라 가림) 조건에서의 성능을 명시하지 않았다.
- 복구 행동 감독은 CARLA에서 정의된 횡방향 오류 임계값(0.35 m)에 의존하며, 이 임계값의 실제 로봇 적용 가능성은 검증되지 않았다.

## 엔지니어링 시사점

- **재현 시 우선 확인 사항**: ReDA 데이터셋의 FSM 상태 전환 로직(Stable→Drifting→Recovering)과 e_y ≥ 0.35 m 임계값은 복구 감독의 핵심이므로 엄격히 재현해야 함; Drifting 프레임 폐기 전략은 데이터 분포에 직접 영향을 미친다.
- **모델 선택**: Qwen2.5-VL-7B의 LoRA 미세 조정 방식은 효과적이지만, 추론에는 RTX 4090급 GPU가 필요; 연산 자원이 제한된 경우 더 작은 백본을 고려할 수 있지만, 공간 접지 능력을 재검증해야 한다.
- **제어 인터페이스 주의점**: 최원점 제어(w_target = w_{t+L})와 적응형 선속도 전략은 저주파 제어에 필수적이며, 밀집 예측 궤적을 직접 추적하면 고주파 변동이 발생; 저수준 제어기의 각속도 포화 및 조향 임계값을 먼저 검증할 것.
- **하위 통합**: 상용 내비게이션 지시 파싱 모듈(비동기적으로 "30미터 후 좌회전" 등의 텍스트 추출)은 실제 배포의 핵심 전제 조건이며, 지시에서 I_t로의 매핑 지연이 제어 가능해야 함; 교차 구현 전이 시 카메라 캘리브레이션과 IPM 폴백 전략의 견고성을 중점적으로 테스트할 것.
