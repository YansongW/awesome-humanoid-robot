---
$id: ent_paper_refertrack_referring_then_tracking_embod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
  zh: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
  ko: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
summary:
  en: Embodied visual tracking (EVT) requires a mobile agent to continuously follow a specific target described in natural
    language using only onboard vision. While recent vision-language-action (VLA) policies unify target identification and
    trajectory planning, their chain-of-thought (CoT) reasoning often operates in abstract spatial latents that are difficult
    to supervise and weakly aligned with.
  zh: ReferTrack 提出“先指代后跟踪”（referring then tracking）范式，将具身视觉跟踪（EVT）中的目标识别显式化为图像空间边界框索引选择，而非抽象潜变量推理。作者基于 Qwen3-4B 构建双分支 VLA，通过
    Refer-CoT token 与 TVBI 历史注入，在单前视相机、无 RL 的 SFT 设置下，于 EVT-Bench 上显著超越最强单视图基线 TrackVLA++，尤其在歧义跟踪（AT）任务上 SR 提升 22.9 个点。
  ko: Embodied visual tracking (EVT) requires a mobile agent to continuously follow a specific target described in natural
    language using only onboard vision. While recent vision-language-action (VLA) policies unify target identification and
    trajectory planning, their chain-of-thought (CoT) reasoning often operates in abstract spatial latents that are difficult
    to supervise and weakly aligned with.
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
- refertrack
- referring
- then
- tracking
- embod
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
  title: 'arXiv:2607.20061 ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
  url: https://arxiv.org/abs/2607.20061
  date: '2026-07-22'
  accessed_at: '2026-08-05'
---

## 概述

ReferTrack 提出“先指代后跟踪”（referring then tracking）范式，将具身视觉跟踪（EVT）中的目标识别显式化为图像空间边界框索引选择，而非抽象潜变量推理。作者基于 Qwen3-4B 构建双分支 VLA，通过 Refer-CoT token 与 TVBI 历史注入，在单前视相机、无 RL 的 SFT 设置下，于 EVT-Bench 上显著超越最强单视图基线 TrackVLA++，尤其在歧义跟踪（AT）任务上 SR 提升 22.9 个点。

## 它改变了什么

现有 VLA 策略将目标识别与轨迹规划统一在链式推理（CoT）中，但该推理常在抽象空间潜变量中运行，难以监督且与显式图像空间检测对齐弱。早期模块化流水线虽分离识别与规划，但识别错误会累积并传播至规划模块。ReferTrack 真正改变的是将“目标是谁”这一决策从隐式潜空间拉回显式图像空间，通过从检测器生成的边界框候选目录中选择索引，使识别过程可监督、可解释，并减少对昂贵 RL 策略优化的依赖。这一转变意味着跟踪失败模式从“模型幻觉目标”变为“检测器漏检或索引误选”，后者更易诊断与修正。

## 方法拆解

### 两阶段推理
- 第一阶段生成 Refer-CoT token：`E_T^refer = LLM(ℒ, C_T, E_{1:T}^V)`，从候选目录 `{⟨ped_1⟩, ..., ⟨ped_K⟩, ⟨NO_EXIST⟩}` 中选择索引。
- 第二阶段以 Refer-CoT 为条件前缀生成动作 token：`E_T^A = LLM(ℒ, C_T, E_{1:T}^V, E_T^refer)`，动作头解码 M 个航点 `w_i = (x, y, θ) ∈ ℝ³`。

### 观测编码
- 双编码器：SigLIP + DINOv2，网格池化生成细粒度 token `V^fine ∈ ℝ^{64×C}`（当前帧）与粗粒度 token `V^coarse ∈ ℝ^{4×C}`（历史帧）。
- 滑动窗口保留最近 H 帧，视觉流为 `V_T = {V_{T-H}^coarse, ..., V_{T-1}^coarse, V_T^fine}`，经两层 MLP 投影器 `P_vision` 映射至 LLM 潜空间。

### TVBI token 注入
- `E_TVBI(t) = E_TVI(t) + P_bbox(b_t)`，将目标 bbox 几何特征注入历史视觉 token；目标未观测时 `b_t = [0,0,0,0]` 作为确定性缺失哨兵。
- 关键设计：当前帧细粒度 token 仅用 TVI 指示器，不注入显式 bbox；历史帧 TVBI 流由目标 bbox 队列条件化，迫使模型仅依赖历史线索与原始视觉特征进行时空定位。

### 候选目录与训练
- 使用 YOLO11 实时检测行人，按 bbox 面积 top-K 排序，固定虚拟索引 `⟨NO_EXIST⟩` 处理目标不在视野情况。
- 目标 bbox 队列为 FIFO，容量 H−1；训练时用 GT 标注填充并随机注入错误索引模拟历史误差，推理时用 Refer-CoT 选定 bbox 自回归更新。
- 训练目标 `L = α·L_traj + L_refer + L_text`，α=10；`L_traj` 为航点 MSE，`L_refer` 为索引交叉熵，`L_text` 为 Refer-QA 文本交叉熵（刻意绕过动作头）。
- 两阶段 SFT：Stage 1 用通用多模态 QA 数据对齐视觉投影器；Stage 2 导航与 Refer-QA 数据 1:1 联合全微调（视觉编码器冻结）。

## 关键创新

1. **显式图像空间指代**：将目标识别从抽象潜变量 CoT 转为边界框索引选择，使识别过程可监督、可解释，且与检测器输出直接对齐，这是与现有 VLA 策略的本质区别。
2. **TVBI 历史注入机制**：通过将目标 bbox 几何特征注入历史视觉 token（而非当前帧），迫使模型利用时间上下文进行定位，同时保留当前帧原始视觉特征，避免信息冗余与过拟合。
3. **无 RL 的强性能**：在纯 SFT 设置下，单视图 4B 模型在 AT 任务上 SR 达 74.1%，超越需 RL 的 CoMaTrack（3B）与 TrackVLA++（7B）多相机参考，证明显式指代可替代部分策略优化成本。

## 实验与结果

主评估为 EVT-Bench 单前视相机协议，指标为成功率（SR↑）、跟踪率（TR↑）、碰撞率（CR↓）。ReferTrack（4B，SFT 无 RL）在 STT/DT/AT 上分别取得 89.4/92.5/1.6、73.3/81.8/7.6、74.1/85.7/7.7。对比最强单视图基线 TrackVLA++（7B），DT 上 SR 提升 6.8、TR 提升 13.0；AT 上 SR 提升 22.9、TR 提升 22.3（由表内数值 51.2→74.1、63.4→85.7 计算）。多相机参考中，CoMaTrack（3B，RL）在 DT 上 SR 74.2 略高，但 AT 上仅 57.5，显著低于 ReferTrack。

| 任务 | ReferTrack SR/TR/CR | TrackVLA++ SR/TR/CR | CoMaTrack SR/TR/CR |
|------|---------------------|---------------------|-------------------|
| STT  | 89.4/92.5/1.6       | 86.0/81.0/2.10      | 92.1/90.3/0.9     |
| DT   | 73.3/81.8/7.6       | 66.5/68.8/4.71      | 74.2/80.5/2.1     |
| AT   | 74.1/85.7/7.7       | 51.2/63.4/15.9      | 57.5/73.4/12.0    |

消融（DT split）：去除 Refer-CoT 与 TVBI 后 SR 降至 55.7（−17.6）；仅去除 TVBI 则 SR 70.4（−2.9）；使用 GT bbox 的 oracle 版本 SR 81.5（+8.2），接近专家策略的 85.1%，表明检测器误差是主要性能瓶颈。

## 边界与局限

论文未明确列出局限性章节。从内容推断：未使用 RL 训练，未采用多相机设置，未在真实世界进行定量评估（仅定性展示）。未消融候选目录大小 K、滑动窗口长度 H 及不同检测器（如 GroundingDINO vs YOLO11）的影响。未报告推理延迟详细分解（除检测 12ms 与整体 10.6Hz 外），未报告训练时长与 GPU 数量等成本细节。性能高度依赖 YOLO11 检测质量，在遮挡密集或小目标场景下可能退化。

## 工程启示

复现时先核对检测器与跟踪器（YOLO11 + ByteTrack）的实时性与召回率，因为消融显示 oracle bbox 可带来 +8.2 SR，检测误差是最大瓶颈。训练数据配比（导航:Refer-QA = 1:1）与两阶段 SFT 策略（Stage 1 仅训投影器，Stage 2 全微调）需严格遵循，α=10 的损失权重对轨迹与指代平衡敏感。部署时注意：推理管线中 DINO 与 SigLIP 特征在独立 CUDA 流并行计算，torch.compile 与预热步骤对达到 10.6 Hz 至关重要；网络抖动时仅保留最新帧并丢弃过期请求。最易踩坑处为 TVBI 队列的时序一致性——训练时随机注入错误索引模拟历史误差，推理时若队列更新滞后会导致误差累积，需确保 Refer-CoT 选定的 bbox 严格按帧序入队。

## Overview
Embodied visual tracking (EVT) requires a mobile agent to continuously follow a specific target described in natural language using only onboard vision. While recent vision-language-action (VLA) policies unify target identification and trajectory planning, their chain-of-thought (CoT) reasoning often operates in abstract spatial latents that are difficult to supervise and weakly aligned with explicit image-space detections. To address this, we introduce ReferTrack, a referring-then-tracking paradigm that grounds EVT using a single forward-facing camera. Our model first selects the target from an indexed set of bounding boxes, then decodes tracking waypoints conditioned on this image-grounded decision. To preserve target motion cues over time, ReferTrack maintains a sliding-window queue of previously selected bounding boxes, injecting their geometric features into the visual history via temporal-viewpoint-bbox indicator (TVBI) tokens. We further enhance target identification by co-training on a custom Refer-QA dataset. On EVT-Bench, ReferTrack achieves state-of-the-art single-view performance with success rates of 89.4%, 73.3%, and 74.1% on the single-target, distracted, and ambiguity tracking splits, respectively -- matching or even surpassing several multi-camera baselines on identification-heavy tasks. Finally, real-world deployments on legged and humanoid robots validate its robust sim-to-real transfer capabilities. Code is available at https://github.com/MedlarTea/referTrack.

## 参考
- https://arxiv.org/abs/2607.20061

## 개요

ReferTrack은 "먼저 지시한 후 추적"(referring then tracking) 패러다임을 제안하여, 구현적 시각 추적(EVT)에서의 대상 인식을 추상적 잠재 변수 추론이 아닌 이미지 공간 경계 상자 인덱스 선택으로 명시화한다. 저자는 Qwen3-4B 기반의 이중 분기 VLA를 구축하고, Refer-CoT 토큰과 TVBI 히스토리 주입을 통해 단일 전방 카메라, RL 없는 SFT 설정에서 EVT-Bench의 가장 강력한 단일 뷰 기준선인 TrackVLA++를 크게 능가하며, 특히 모호한 추적(AT) 작업에서 SR이 22.9포인트 향상되었다.

## 무엇이 바뀌었는가

기존 VLA 전략은 대상 인식과 궤적 계획을 체인 추론(CoT)으로 통합하지만, 이 추론은 종종 추상적 공간 잠재 변수에서 작동하여 감독이 어렵고 명시적 이미지 공간 검출과의 정렬이 약하다. 초기 모듈식 파이프라인은 인식과 계획을 분리했지만, 인식 오류가 누적되어 계획 모듈로 전파된다. ReferTrack이 진정으로 바꾼 것은 "대상이 누구인가"라는 결정을 암시적 잠재 공간에서 명시적 이미지 공간으로 끌어내어, 검출기에서 생성된 경계 상자 후보 카탈로그에서 인덱스를 선택하도록 함으로써 인식 과정을 감독 가능하고 해석 가능하게 만들고, 값비싼 RL 정책 최적화에 대한 의존도를 줄인다. 이러한 전환은 추적 실패 모드가 "모델이 대상을 환각하는 것"에서 "검출기 누락 또는 인덱스 오선택"으로 바뀌며, 후자가 진단과 수정이 더 쉽다.

## 방법 분해

### 2단계 추론
- 1단계에서 Refer-CoT 토큰 생성: `E_T^refer = LLM(ℒ, C_T, E_{1:T}^V)`, 후보 카탈로그 `{⟨ped_1⟩, ..., ⟨ped_K⟩, ⟨NO_EXIST⟩}`에서 인덱스 선택.
- 2단계에서 Refer-CoT를 조건부 접두사로 사용하여 액션 토큰 생성: `E_T^A = LLM(ℒ, C_T, E_{1:T}^V, E_T^refer)`, 액션 헤드가 M개의 웨이포인트 `w_i = (x, y, θ) ∈ ℝ³`를 디코딩.

### 관측 인코딩
- 이중 인코더: SigLIP + DINOv2, 그리드 풀링으로 세밀한 토큰 `V^fine ∈ ℝ^{64×C}`(현재 프레임)과 거친 토큰 `V^coarse ∈ ℝ^{4×C}`(히스토리 프레임) 생성.
- 슬라이딩 윈도우로 최근 H 프레임 유지, 시각 흐름은 `V_T = {V_{T-H}^coarse, ..., V_{T-1}^coarse, V_T^fine}`, 2계층 MLP 프로젝터 `P_vision`을 통해 LLM 잠재 공간으로 매핑.

### TVBI 토큰 주입
- `E_TVBI(t) = E_TVI(t) + P_bbox(b_t)`, 대상 bbox 기하 특징을 히스토리 시각 토큰에 주입; 대상이 관측되지 않으면 `b_t = [0,0,0,0]`을 결정적 누락 센티널로 사용.
- 핵심 설계: 현재 프레임 세밀한 토큰에는 TVI 표시기만 사용하고 명시적 bbox를 주입하지 않음; 히스토리 프레임 TVBI 흐름은 대상 bbox 큐에 의해 조건화되어, 모델이 히스토리 단서와 원시 시각 특징만으로 시공간 위치 파악을 수행하도록 강제.

### 후보 카탈로그 및 훈련
- YOLO11로 보행자를 실시간 검출, bbox 면적 기준 top-K 정렬, 고정 가상 인덱스 `⟨NO_EXIST⟩`로 대상이 시야에 없는 경우 처리.
- 대상 bbox 큐는 FIFO, 용량 H−1; 훈련 시 GT 주석으로 채우고 무작위로 잘못된 인덱스를 주입하여 히스토리 오류를 시뮬레이션, 추론 시 Refer-CoT로 선택된 bbox를 자동 회귀적으로 업데이트.
- 훈련 목표 `L = α·L_traj + L_refer + L_text`, α=10; `L_traj`는 웨이포인트 MSE, `L_refer`는 인덱스 교차 엔트로피, `L_text`는 Refer-QA 텍스트 교차 엔트로피(의도적으로 액션 헤드 우회).
- 2단계 SFT: Stage 1은 일반 다중 모달 QA 데이터로 시각 프로젝터 정렬; Stage 2는 내비게이션과 Refer-QA 데이터를 1:1로 결합하여 전체 미세 조정(시각 인코더 동결).

## 핵심 혁신

1. **명시적 이미지 공간 지시**: 대상 인식을 추상적 잠재 변수 CoT에서 경계 상자 인덱스 선택으로 전환하여 인식 과정을 감독 가능하고 해석 가능하게 만들고 검출기 출력과 직접 정렬한다. 이는 기존 VLA 전략과의 본질적 차이다.
2. **TVBI 히스토리 주입 메커니즘**: 대상 bbox 기하 특징을 현재 프레임이 아닌 히스토리 시각 토큰에 주입하여 모델이 시간적 맥락을 활용한 위치 파악을 수행하도록 강제하면서, 현재 프레임의 원시 시각 특징을 보존하여 정보 중복과 과적합을 방지한다.
3. **RL 없는 강력한 성능**: 순수 SFT 설정에서 단일 뷰 4B 모델이 AT 작업에서 SR 74.1%를 달성하여, RL이 필요한 CoMaTrack(3B)과 TrackVLA++(7B) 다중 카메라 참조를 능가한다. 이는 명시적 지시가 일부 정책 최적화 비용을 대체할 수 있음을 증명한다.

## 실험 및 결과

주 평가는 EVT-Bench 단일 전방 카메라 프로토콜이며, 지표는 성공률(SR↑), 추적률(TR↑), 충돌률(CR↓)이다. ReferTrack(4B, SFT, RL 없음)은 STT/DT/AT에서 각각 89.4/92.5/1.6, 73.3/81.8/7.6, 74.1/85.7/7.7을 기록했다. 가장 강력한 단일 뷰 기준선 TrackVLA++(7B)와 비교하면, DT에서 SR 6.8, TR 13.0 향상; AT에서 SR 22.9, TR 22.3 향상(표 내 값 51.2→74.1, 63.4→85.7로 계산). 다중 카메라 참조에서 CoMaTrack(3B, RL)은 DT에서 SR 74.2로 약간 높지만, AT에서는 57.5에 불과하여 ReferTrack보다 현저히 낮다.

| 작업 | ReferTrack SR/TR/CR | TrackVLA++ SR/TR/CR | CoMaTrack SR/TR/CR |
|------|---------------------|---------------------|-------------------|
| STT  | 89.4/92.5/1.6       | 86.0/81.0/2.10      | 92.1/90.3/0.9     |
| DT   | 73.3/81.8/7.6       | 66.5/68.8/4.71      | 74.2/80.5/2.1     |
| AT   | 74.1/85.7/7.7       | 51.2/63.4/15.9      | 57.5/73.4/12.0    |

소거(DT split): Refer-CoT와 TVBI를 제거하면 SR이 55.7(−17.6)로 하락; TVBI만 제거하면 SR 70.4(−2.9); GT bbox를 사용하는 oracle 버전은 SR 81.5(+8.2)로 전문가 정책의 85.1%에 근접하여, 검출기 오류가 주요 성능 병목임을 시사한다.

## 경계 및 한계

논문은 한계 섹션을 명시적으로 나열하지 않았다. 내용에서 추론: RL 훈련을 사용하지 않았고, 다중 카메라 설정을 채택하지 않았으며, 실제 세계에서 정량적 평가를 수행하지 않았다(정성적 시연만). 후보 카탈로그 크기 K, 슬라이딩 윈도우 길이 H, 다양한 검출기(예: GroundingDINO vs YOLO11)의 영향을 소거하지 않았다. 추론 지연 시간 상세 분해(검출 12ms 및 전체 10.6Hz 외)를 보고하지 않았고, 훈련 시간과 GPU 수 등의 비용 세부 사항도 보고하지 않았다. 성능은 YOLO11 검출 품질에 크게 의존하며, 폐색이 밀집되거나 소형 대상 시나리오에서 저하될 수 있다.

## 엔지니어링 시사점

재현 시 먼저 검출기와 추적기(YOLO11 + ByteTrack)의 실시간성과 재현율을 확인하라. 소거 결과 oracle bbox가 +8.2 SR을 제공하므로 검출 오류가 가장 큰 병목이다. 훈련 데이터 비율(내비게이션:Refer-QA = 1:1)과 2단계 SFT 전략(Stage 1은 프로젝터만 훈련, Stage 2는 전체 미세 조정)을 엄격히 따르고, α=10의 손실 가중치는 궤적과 지시 균형에 민감하다. 배포 시 주의: 추론 파이프라인에서 DINO와 SigLIP 특징을 별도 CUDA 스트림에서 병렬 계산하며, torch.compile과 워밍업 단계가 10.6Hz 달성에 중요하다; 네트워크 지터 시 최신 프레임만 유지하고 만료된 요청을 폐기한다. 가장 함정에 빠지기 쉬운 곳은 TVBI 큐의 시간적 일관성이다 — 훈련 시 무작위로 잘못된 인덱스를 주입하여 히스토리 오류를 시뮬레이션하고, 추론 시 큐 업데이트가 지연되면 오류가 누적될 수 있으므로 Refer-CoT로 선택된 bbox가 프레임 순서대로 엄격히 큐에 들어가도록 보장해야 한다.
