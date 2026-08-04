---
$id: ent_paper_ye_ego2robot_scalable_robot_data_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data'
  zh: Ego2Robot：从第一视角人类数据规模化合成机器人训练数据
  ko: 'Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data'
summary:
  en: Ego2Robot is a 2026 pipeline from Renmin University (Jin Qin group), Alibaba Qwen, ShanghaiTech, BIGAI, and Beihang
    that converts egocentric human videos into robot training data via action alignment, visual alignment, and quality curation,
    producing 18,561 hours across 15 robot morphologies from ~1,940 hours of ego video; it improves EBench averages (62.2->68.1
    Clean, 50.9->53.5 Rand) and real-robot long-horizon tasks on an ARX ACone platform.
  zh: Ego2Robot 提出了一条从大规模第一人称人类操作视频到多形态机器人合成数据的自动化管线，通过动作对齐、视觉对齐和质量筛选三个环节，将约 1,940 小时 ego 数据转化为 18,561 小时、覆盖 15 种机器人形态的训练数据。作者验证了该合成数据作为
    VLA 模型预训练源的有效性，在 RoboTwin 2.0 和 EBench 基准上显著提升分布外泛化，并在真实机器人上展示了长时程任务收益。
  ko: Ego2Robot is a 2026 pipeline that converts egocentric human videos into robot training data, producing 18,561 hours
    across 15 robot morphologies.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- ego2robot
- egocentric_video
- data_synthesis
- retargeting
- cross_embodiment
- robot_pretraining_data
- human_video_to_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: New card from deep-read task (.staging/deep_read). Full text from arXiv HTML (2608.02580v1); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails; key numbers verified against the full text (1,940h->18,561h,
    15 morphologies, 62.2->68.1, 50.9->53.5, Franka<7%, +14/+13 real-robot gains).
sources:
- id: src_001
  type: paper
  title: arXiv:2608.02580 Ego2Robot
  url: https://arxiv.org/abs/2608.02580
  date: '2026-08-03'
  accessed_at: '2026-08-05'
- id: src_002
  type: website
  title: Ego2Robot project page
  url: https://www-ye.github.io/ego2robot_blog/
  accessed_at: '2026-08-05'
---

## 概述

Ego2Robot 提出了一条从大规模第一人称人类操作视频到多形态机器人合成数据的自动化管线，通过动作对齐、视觉对齐和质量筛选三个环节，将约 1,940 小时 ego 数据转化为 18,561 小时、覆盖 15 种机器人形态的训练数据。作者验证了该合成数据作为 VLA 模型预训练源的有效性，在 RoboTwin 2.0 和 EBench 基准上显著提升分布外泛化，并在真实机器人上展示了长时程任务收益。

## 它改变了什么

这项工作真正改变的是机器人策略预训练的数据供给逻辑。此前，VLA 模型的预训练几乎完全依赖真实机器人遥操作数据（如 DROID、AgibotWorld），其规模受硬件、人力和场景多样性三重约束，难以突破。Ego2Robot 证明了一个此前未被验证的假设：人类第一人称操作视频——一种互联网上近乎无限、且天然包含丰富任务语义和交互多样性的数据源——经过系统化的重定向和渲染，可以成为 VLA 预训练的有效补充，甚至在任务语义泛化（+7.9%）和跨形态迁移（+4.4%）上带来纯机器人数据无法提供的增益。

更关键的是，它推翻了"合成数据只能锦上添花、不能雪中送炭"的默认预期。在 1:1 混合比例下，Ego2R 数据不仅没有稀释机器人数据的质量，反而在 Clean 设置上提升了 5.9 个百分点，在视觉外观扰动上提升 5.9 个百分点。这意味着合成数据不再是"凑数"的替代品，而是可以主动扩展策略泛化边界的正资产。同时，作者将 RoboTwin 2.0 的聚合 OOD 指标拆解为 11 个独立扰动维度，使得"合成数据到底提升了什么"第一次可以被归因到具体能力维度——这改变了该领域评估泛化增益的方式。

## 方法拆解

### 整体流程
Ego2Robot 管道分为三个阶段：动作对齐（action alignment）、视觉对齐（visual alignment）、质量筛选（quality curation）。两条输入路径：Path A 直接接受带手部姿态标注的 ego 数据集；Path B 处理无标注视频，先用 WiLoR 逐帧重建 MANO 参数，再用 DynHaMR 做时间优化。

### 手到夹爪重定向
- 虚拟指尖定义为食指与中指指尖的加权混合：p_vf = 0.7·p_index + 0.3·p_middle
- TCP 位置为拇指与虚拟指尖中点，夹爪开度为两者距离
- 抓取姿态为右手系正交框架：z 轴沿夹爪线，y 轴为夹爪法线，x 轴为接近方向；s=+1 右手，s=-1 左手
- 时间平滑：位置和宽度用 Savitzky-Golay 滤波（窗口 min(21, n)），姿态用高斯加权 SLERP（σ=10 帧）
- 动作速度对齐：按数据源降采样——ANT/EgoDex 降至 60%，EgoVerse 降至 45%，ViTRA 降至 25%

### 视觉对齐
- SAM 3 分割手臂区域（文本提示 "person"，400 帧块处理，50 帧重叠）
- ProPainter 时间一致视频修复移除手臂（fp16，neighbor_length=10，ref_stride=10）
- 基座位姿搜索：SE(3) 网格搜索，候选受每形态最大可达距离 r_max 约束；评分 S = FR(T_base) − 5.0·|ρ̄ − 0.65|，其中 FR 为 IK 可行率，ρ̄ 为归一化平均末端距离（目标 0.65 保留运动余量）
- 深度感知合成：机器人深度小于场景深度且掩码为 1 时用机器人像素，否则用修复后的场景像素

### 质量筛选
- L1（管道内部）：标记 IK 失败、自碰撞、动作异常值、工作空间覆盖不足
- L2（统计）：Q1/Q99 滤波 + 突变滤波，总无效帧比例 >60% 的片段丢弃
- L3（VLM 一致性）：Qwen3.5 以 4 fps 采样视频，审计语义一致性

### 动作表示
相机坐标系相对末端执行器动作（7 维：3D 位置增量、3D 旋转增量、1D 夹爪），通过 T_ce = T_wc⁻¹·T_we 变换，避免不同相机设置和机器人形态间的动作空间不兼容。

### 模型架构
Qwen3.5-4B 视觉语言骨干 + Diffusion Transformer（DiT）动作头，预测 32 步动作块，8 步扩散训练 / 4 步 Euler 推理。相机内参和外参通过 mRoPE 位置编码注入。

## 关键创新

**1. 大规模 ego-to-robot 数据管线的完整闭环**：此前 retarget-and-render 方法仅在有限规模或单任务上验证，Ego2Robot 首次将这一思路扩展到 1,940 小时原始数据、15 种机器人形态、18,561 小时合成数据的规模，并系统解决了手部姿态估计、长视频分割、基座搜索、深度感知合成、三级质量筛选等工程问题。这不是单点创新，而是把整个流程做成了可复现、可扩展的工业级管道。

**2. 相机坐标系相对末端执行器的动作表示**：这一设计选择看似简单，实则解决了多形态、多相机设置下数据混合的根本障碍。通过将动作从基座坐标系变换到相机坐标系，不同机器人形态的数据可以在同一动作空间内训练，无需显式外参标定。这是 Ego2R 数据能与 DROID、AgibotWorld 等异构机器人数据混合训练的前提。

**3. 逐扰动评估框架**：将 RoboTwin 2.0 的聚合 OOD 指标拆解为 11 个独立扰动维度（背景、光照、颜色、高度、杂乱、相机偏移、跨形态、未见物体、改写指令），并新增 EBench 桌面任务集。这使得"合成数据提升了什么"第一次可以被精确归因——例如 1:1 混合下任务语义泛化提升 7.9%，而跨形态迁移中 Franka 仅提升 -1.7%，说明合成数据对某些泛化维度的贡献是不均匀的。

## 实验与结果

### 主要结果（RoboTwin 50 任务 + EBench 7 任务，成功率 %）

| 任务/设置 | Robot-only | Ego2R+Robot (1:3) | Ego2R+Robot (3:1) | Ego2R+Robot (1:1) |
|---|---|---|---|---|
| Clean | 62.2 | 61.4 (-0.8) | 64.1 (+1.9) | **68.1 (+5.9)** |
| Rand | 50.9 | 51.0 (+0.1) | 49.2 (-1.7) | **53.5 (+2.6)** |
| Visual | 61.4 | 61.2 (-0.2) | 62.7 (+1.3) | **67.3 (+5.9)** |
| Scene | 52.9 | 52.5 (-0.4) | 54.3 (+1.4) | **56.9 (+4.0)** |
| Embody | 23.8 | 21.9 (-1.9) | **28.2 (+4.4)** | 27.2 (+3.4) |
| Task | 46.2 | 49.5 (+3.3) | 51.6 (+5.4) | **54.1 (+7.9)** |
| EBench | 39.6 | 47.4 (+7.8) | **51.7 (+12.1)** | 49.8 (+10.2) |

### 逐扰动分解（关键维度，成功率 %）

| 扰动 | Robot-only | Ego2R (1:3) | Ego2R (3:1) | Ego2R (1:1) |
|---|---|---|---|---|
| UR5 跨形态 | 20.2 | 17.6 (-2.6) | **31.4 (+11.2)** | 25.0 (+4.8) |
| 未见物体 | 29.3 | 36.8 (+7.5) | **40.0 (+10.7)** | 39.6 (+10.3) |
| 光照 | 58.2 | 58.3 (+0.1) | 60.9 (+2.7) | **65.8 (+7.6)** |
| 相机偏移 | 50.4 | 49.6 (-0.8) | 51.6 (+1.2) | **56.3 (+5.9)** |

### 消融实验（RoboTwin Randomized 成功率 %）
- 原始 ego 协同训练：28.1%
- 经管道处理（单形态）：31.7%（+3.6）
- 1→15 形态逐步提升：31.7 → 33.5
- 15 形态 Ego2R + 原始 ego：37.3%

### 真实机器人（ARX ACone，5 任务，100 分制）
Mix + Ego2R Play 在所有 5 个任务上最佳，最大增益为 Put Blocks（+14）和 Insert Screw（+13）。

### 与 Pi0.5 对比
Pi0.5：Clean 54.9，Rand 27.7；Robot-only：Clean 62.2，Rand 50.9；Ego2R (1:1)：Clean 68.1，Rand 53.5。

## 边界与局限

作者承认的局限包括：重定向将手部姿态映射到平行夹爪，丢弃了细粒度手指关节运动，限制了灵巧操作技能的迁移；视觉对齐依赖修复和深度感知合成，在严重遮挡或复杂光照下可能引入伪影。此外，评估限于 RoboTwin 2.0 任务范围，未覆盖非抓取类操作（如工具使用时的精细力控）、动态场景（移动物体、人类在场）和多智能体协作。跨具身迁移仅在仿真中验证，未在真实机器人上测试。论文未明确报告推理延迟和 Sim2Real 域差距的量化指标。

## 工程启示

复现时最需要优先核对的是**动作速度对齐的降采样比例**——不同数据源（ANT/EgoDex 60%、EgoVerse 45%、ViTRA 25%）的帧率差异直接决定了合成数据的动作节奏，如果忽略这一点，混合训练时模型会学到不一致的速度分布。其次是**基座位姿搜索的评分函数**：S = FR(T_base) − 5.0·|ρ̄ − 0.65| 中的 ρ̄ 目标值 0.65 是关键超参，它平衡了 IK 可行率与运动余量，直接决定合成轨迹的质量；建议在迁移到新机器人形态时重新标定该值。**相机坐标系相对 EEF 的动作表示**是数据混合的前提，如果下游团队使用基座坐标系动作，Ego2R 数据无法直接与 DROID 等数据混合。质量筛选的 L3 VLM 审计环节依赖 Qwen3.5 的语义判断，建议保留原始 ego 视频作为对照，避免过度过滤导致数据多样性损失。最后，1:1 混合比例在多数维度上最优，但 3:1 在跨形态（UR5 +11.2）和 EBench（+12.1）上更强，实际选型时应根据目标泛化维度调整比例。

## Overview
Learning generalizable robot manipulation policies requires large-scale and diverse demonstration data. Egocentric human manipulation videos offer rich scene and task diversity, and prior work has shown that retargeting and rendering such videos into robot-format data can yield effective per-task policies at small scale. However, whether this approach can provide pretraining benefits for vision-language-action models at scale remains unexplored. We present Ego2Robot , a scalable pipeline that converts egocentric human manipulation videos into robot training data through action retargeting, robot-arm visual synthesis, and multi-level quality curation. Ego2Robot supports both curated datasets and in-the-wild videos, producing 18,561 hours of robot training data spanning 15 robot morphologies, making it the largest ego-to-robot dataset to date. To evaluate generalization, we extend RoboTwin2.0 with disentangled perturbation axes covering visual appearance, scene layout, embodiment morphology, and task semantics. Experiments show that joint pretraining on Ego2Robot-synthesized and robot data consistently improves out-of-distribution generalization across multiple perturbation types, with benefits validated on real-robot deployment. Project page: https://www-ye.github.io/ego2robot_blog/ Keywords: Robot Data Synthesis, Egocentric Data, Generalization Evaluation

## 参考
- https://arxiv.org/abs/2608.02580
- https://www-ye.github.io/ego2robot_blog/

## 개요

Ego2Robot은 대규모 1인칭 인간 조작 비디오에서 다형태 로봇 합성 데이터로의 자동화 파이프라인을 제안하며, 동작 정렬, 시각 정렬, 품질 선별의 세 단계를 통해 약 1,940시간의 ego 데이터를 18,561시간, 15가지 로봇 형태를 포괄하는 훈련 데이터로 변환합니다. 저자들은 이 합성 데이터가 VLA 모델 사전 훈련 소스로서의 유효성을 검증했으며, RoboTwin 2.0 및 EBench 벤치마크에서 분포 외 일반화를 크게 향상시키고, 실제 로봇에서 장기 작업 이점을 입증했습니다.

## 그것이 바꾼 것

이 작업이 진정으로 바꾼 것은 로봇 정책 사전 훈련의 데이터 공급 논리입니다. 이전에는 VLA 모델의 사전 훈련이 거의 전적으로 실제 로봇 원격 조작 데이터(예: DROID, AgibotWorld)에 의존했으며, 그 규모는 하드웨어, 인력, 장면 다양성의三重 제약을 받아 돌파하기 어려웠습니다. Ego2Robot은 이전에 검증되지 않았던 가설을 증명했습니다: 인간 1인칭 조작 비디오——인터넷상에서 거의 무한하고 자연스럽게 풍부한 작업 의미론과 상호작용 다양성을 포함하는 데이터 소스——가 체계적인 리타겟팅과 렌더링을 통해 VLA 사전 훈련의 효과적인 보완이 될 수 있으며, 작업 의미론 일반화(+7.9%) 및 교차 형태 전이(+4.4%)에서 순수 로봇 데이터가 제공할 수 없는 이점을 제공합니다.

더 중요하게는, "합성 데이터는 장식일 뿐, 구원자는 될 수 없다"는 기본 기대를 뒤집었습니다. 1:1 혼합 비율에서 Ego2R 데이터는 로봇 데이터의 품질을 희석시키지 않았을 뿐만 아니라, Clean 설정에서 5.9% 포인트, 시각 외관 교란에서 5.9% 포인트를 향상시켰습니다. 이는 합성 데이터가 더 이상 "숫자 채우기" 대체재가 아니라 정책 일반화 경계를 능동적으로 확장할 수 있는 긍정 자산임을 의미합니다. 동시에 저자들은 RoboTwin 2.0의 집계 OOD 지표를 11개의 독립 교란 차원으로 분해하여 "합성 데이터가 정확히 무엇을 향상시켰는지"가 처음으로 특정 능력 차원에 귀속될 수 있게 했습니다——이것은 이 분야의 일반화 이득 평가 방식을 바꿉니다.

## 방법 분해

### 전체 흐름
Ego2Robot 파이프라인은 세 단계로 구성됩니다: 동작 정렬(action alignment), 시각 정렬(visual alignment), 품질 선별(quality curation). 두 가지 입력 경로: Path A는 손 자세 주석이 있는 ego 데이터셋을 직접 수용; Path B는 주석 없는 비디오를 처리하며, 먼저 WiLoR로 프레임별 MANO 파라미터를 재구성한 다음 DynHaMR로 시간 최적화를 수행합니다.

### 손에서 그리퍼로의 리타겟팅
- 가상 손끝은 검지와 중지 손끝의 가중 혼합으로 정의: p_vf = 0.7·p_index + 0.3·p_middle
- TCP 위치는 엄지와 가상 손끝의 중점, 그리퍼 개방도는 두 점 사이의 거리
- 파지 자세는 오른손 좌표계 직교 프레임: z축은 그리퍼 라인, y축은 그리퍼 법선, x축은 접근 방향; s=+1 오른손, s=-1 왼손
- 시간 평활화: 위치와 폭은 Savitzky-Golay 필터(창 min(21, n)), 자세는 가우시안 가중 SLERP(σ=10 프레임)
- 동작 속도 정렬: 데이터 소스별 다운샘플링——ANT/EgoDex는 60%, EgoVerse는 45%, ViTRA는 25%로 감소

### 시각 정렬
- SAM 3로 팔 영역 분할(텍스트 프롬프트 "person", 400프레임 블록 처리, 50프레임 중첩)
- ProPainter 시간 일관 비디오 인페인팅으로 팔 제거(fp16, neighbor_length=10, ref_stride=10)
- 베이스 포즈 검색: SE(3) 그리드 검색, 후보는 각 형태의 최대 도달 거리 r_max로 제약; 점수 S = FR(T_base) − 5.0·|ρ̄ − 0.65|, 여기서 FR은 IK 성공률, ρ̄는 정규화된 평균 말단 거리(목표 0.65는 운동 여유 유지)
- 깊이 인식 합성: 로봇 깊이가 장면 깊이보다 작고 마스크가 1이면 로봇 픽셀 사용, 그렇지 않으면 인페인팅된 장면 픽셀 사용

### 품질 선별
- L1(파이프라인 내부): IK 실패, 자체 충돌, 동작 이상치, 작업 공간 커버리지 부족 표시
- L2(통계): Q1/Q99 필터 + 급변 필터, 총 무효 프레임 비율 >60%인 세그먼트 폐기
- L3(VLM 일관성): Qwen3.5가 4fps로 비디오 샘플링, 의미론적 일관성 감사

### 동작 표현
카메라 좌표계 상대 말단 실행기 동작(7차원: 3D 위치 증분, 3D 회전 증분, 1D 그리퍼), T_ce = T_wc⁻¹·T_we 변환을 통해 서로 다른 카메라 설정과 로봇 형태 간 동작 공간 비호환성 방지.

### 모델 아키텍처
Qwen3.5-4B 비전 언어 백본 + Diffusion Transformer(DiT) 동작 헤드, 32단계 동작 블록 예측, 8단계 확산 훈련 / 4단계 Euler 추론. 카메라 내부 및 외부 파라미터는 mRoPE 위치 인코딩으로 주입.

## 핵심 혁신

**1. 대규모 ego-to-robot 데이터 파이프라인의 완전한 폐루프**: 이전의 retarget-and-render 방법은 제한된 규모 또는 단일 작업에서만 검증되었지만, Ego2Robot은 이 접근 방식을 처음으로 1,940시간 원본 데이터, 15가지 로봇 형태, 18,561시간 합성 데이터 규모로 확장하고, 손 자세 추정, 장시간 비디오 분할, 베이스 검색, 깊이 인식 합성, 3단계 품질 선별 등의 엔지니어링 문제를 체계적으로 해결했습니다. 이것은 단일 혁신이 아니라 전체 프로세스를 재현 가능하고 확장 가능한 산업급 파이프라인으로 만든 것입니다.

**2. 카메라 좌표계 상대 말단 실행기 동작 표현**: 이 설계 선택은 단순해 보이지만, 다형태, 다중 카메라 설정에서 데이터 혼합의 근본 장벽을 해결합니다. 동작을 베이스 좌표계에서 카메라 좌표계로 변환함으로써, 서로 다른 로봇 형태의 데이터가 동일한 동작 공간에서 훈련될 수 있으며, 명시적 외부 파라미터 보정이 필요 없습니다. 이것은 Ego2R 데이터가 DROID, AgibotWorld 등 이종 로봇 데이터와 혼합 훈련될 수 있는 전제 조건입니다.

**3. 교란별 평가 프레임워크**: RoboTwin 2.0의 집계 OOD 지표를 11개의 독립 교란 차원(배경, 조명, 색상, 높이, 어수선함, 카메라 오프셋, 교차 형태, 미지 물체, 재작성 명령)으로 분해하고, EBench 데스크톱 작업 세트를 추가했습니다. 이로써 "합성 데이터가 무엇을 향상시켰는지"가 처음으로 정확히 귀속될 수 있습니다——예를 들어 1:1 혼합에서 작업 의미론 일반화가 7.9% 향상된 반면, 교차 형태 전이에서 Franka는 -1.7%만 향상되어 합성 데이터가 특정 일반화 차원에 불균등하게 기여함을 보여줍니다.

## 실험 및 결과

### 주요 결과(RoboTwin 50개 작업 + EBench 7개 작업, 성공률 %)

| 작업/설정 | Robot-only | Ego2R+Robot (1:3) | Ego2R+Robot (3:1) | Ego2R+Robot (1:1) |
|---|---|---|---|---|
| Clean | 62.2 | 61.4 (-0.8) | 64.1 (+1.9) | **68.1 (+5.9)** |
| Rand | 50.9 | 51.0 (+0.1) | 49.2 (-1.7) | **53.5 (+2.6)** |
| Visual | 61.4 | 61.2 (-0.2) | 62.7 (+1.3) | **67.3 (+5.9)** |
| Scene | 52.9 | 52.5 (-0.4) | 54.3 (+1.4) | **56.9 (+4.0)** |
| Embody | 23.8 | 21.9 (-1.9) | **28.2 (+4.4)** | 27.2 (+3.4) |
| Task | 46.2 | 49.5 (+3.3) | 51.6 (+5.4) | **54.1 (+7.9)** |
| EBench | 39.6 | 47.4 (+7.8) | **51.7 (+12.1)** | 49.8 (+10.2) |

### 교란별 분해(핵심 차원, 성공률 %)

| 교란 | Robot-only | Ego2R (1:3) | Ego2R (3:1) | Ego2R (1:1) |
|---|---|---|---|---|
| UR5 교차 형태 | 20.2 | 17.6 (-2.6) | **31.4 (+11.2)** | 25.0 (+4.8) |
| 미지 물체 | 29.3 | 36.8 (+7.5) | **40.0 (+10.7)** | 39.6 (+10.3) |
| 조명 | 58.2 | 58.3 (+0.1) | 60.9 (+2.7) | **65.8 (+7.6)** |
| 카메라 오프셋 | 50.4 | 49.6 (-0.8) | 51.6 (+1.2) | **56.3 (+5.9)** |

### 소거 실험(RoboTwin Randomized 성공률 %)
- 원본 ego 공동 훈련: 28.1%
- 파이프라인 처리(단일 형태): 31.7%(+3.6)
- 1→15 형태 점진적 향상: 31.7 → 33.5
- 15 형태 Ego2R + 원본 ego: 37.3%

### 실제 로봇(ARX ACone, 5개 작업, 100점 만점)
Mix + Ego2R Play가 모든 5개 작업에서 최고, 최대 이득은 Put Blocks(+14) 및 Insert Screw(+13).

### Pi0.5와 비교
Pi0.5: Clean 54.9, Rand 27.7; Robot-only: Clean 62.2, Rand 50.9; Ego2R (1:1): Clean 68.1, Rand 53.5.

## 경계와 한계

저자들이 인정한 한계는 다음과 같습니다: 리타겟팅이 손 자세를 평행 그리퍼에 매핑하여 세밀한 손가락 관절 운동을 버리므로, 정밀 조작 기술 전이를 제한합니다; 시각 정렬은 인페인팅과 깊이 인식 합성에 의존하므로, 심한 폐색이나 복잡한 조명에서 아티팩트를 유발할 수 있습니다. 또한 평가는 RoboTwin 2.0 작업 범위로 제한되어, 비파지 조작(예: 도구 사용 시 정밀 힘 제어), 동적 장면(이동 물체, 인간 존재), 다중 에이전트 협력을 다루지 않습니다. 교차 구현 전이는 시뮬레이션에서만 검증되었고 실제 로봇에서는 테스트되지 않았습니다. 논문은 추론 지연 시간과 Sim2Real 도메인 격차의 정량적 지표를 명시적으로 보고하지 않았습니다.

## 엔지니어링 시사점

재현 시 가장 우선적으로 확인해야 할 것은 **동작 속도 정렬의 다운샘플링 비율**입니다——서로 다른 데이터 소스(ANT/EgoDex 60%, EgoVerse 45%, ViTRA 25%)의 프레임 속도 차이가 합성 데이터의 동작 리듬을 직접 결정하며, 이를 무시하면 혼합 훈련 시 모델이 일관되지 않은 속도 분포를 학습하게 됩니다. 다음은 **베이스 포즈 검색의 점수 함수**입니다: S = FR(T_base) − 5.0·|ρ̄ − 0.65|에서 ρ̄ 목표 값 0.65는 핵심 하이퍼파라미터로, IK 성공률과 운동 여유를 균형 있게 조정하며 합성 궤적 품질을 직접 결정합니다; 새 로봇 형태로 전이할 때 이 값을 재보정할 것을 권장합니다. **카메라 좌표계 상대 EEF 동작 표현**은 데이터 혼합의 전제 조건이며, 하류 팀이 베이스 좌표계 동작을 사용한다면 Ego2R 데이터는 DROID 등 데이터와 직접 혼합할 수 없습니다. 품질 선별의 L3 VLM 감사 단계는 Qwen3.5의 의미론적 판단에 의존하므로, 원본 ego 비디오를 대조군으로 유지하여 과도한 필터링으로 인한 데이터 다양성 손실을 방지할 것을 권장합니다. 마지막으로, 1:1 혼합 비율이 대부분의 차원에서 최적이지만, 3:1은 교차 형태(UR5 +11.2) 및 EBench(+12.1)에서 더 강하므로, 실제 선택 시 목표 일반화 차원에 따라 비율을 조정해야 합니다.
