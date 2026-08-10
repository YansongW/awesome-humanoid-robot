---
$id: ent_paper_robosnap_one_shot_real_sim_scene_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation'
  zh: 'RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation'
  ko: 'RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation'
summary:
  en: Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible
    policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and
    expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready
    scene. The key idea is a.
  zh: RoboSnap 提出从单张 RGB 图像自动生成物理稳定、视觉保真且仿真就绪的分层场景，用于机器人策略训练与评估。该方法由华盛顿大学等机构完成，核心贡献在于将碰撞感知的交互物理层与 3D 高斯泼溅视觉上下文层分离，并通过交替 SDF-物理优化实现仿真就绪精修。基于
    564 个 DROID 场景构建的 DROID-Sim 数据集，验证了其在轨迹重放、数据生成与 sim-real 评估对齐上的有效性。
  ko: Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible
    policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and
    expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready
    scene. The key idea is a.
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
- robosnap
- one
- shot
- real
- sim
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
  title: 'arXiv:2607.06699 RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning'
  url: https://arxiv.org/abs/2607.06699
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

RoboSnap 提出从单张 RGB 图像自动生成物理稳定、视觉保真且仿真就绪的分层场景，用于机器人策略训练与评估。该方法由华盛顿大学等机构完成，核心贡献在于将碰撞感知的交互物理层与 3D 高斯泼溅视觉上下文层分离，并通过交替 SDF-物理优化实现仿真就绪精修。基于 564 个 DROID 场景构建的 DROID-Sim 数据集，验证了其在轨迹重放、数据生成与 sim-real 评估对齐上的有效性。

## 它改变了什么

现有 real-to-sim 管线要么依赖多视角采集与人工精修，要么输出针对窄端点的检索式数字孪生或静态背景，无法普遍恢复可重新渲染、编辑和从新视角复用的持久仿真世界。RoboSnap 真正改变的是将 real-to-sim 从“视觉重建任务”重新定义为“可复用基础设施构建任务”——它不再追求像素级完美，而是优先保证物理交互区域的稳定性与视觉上下文的保真度，使单张图像生成的场景能直接支撑策略微调与闭环评估。

这一转变的关键在于分层设计：物理层只保留与机器人交互直接相关的物体和支持表面，视觉层则用高斯泼溅覆盖背景。这种解耦使得物理精修可以专注于少数关键资产，而视觉层在 novel views 下保持外观一致性，从而在单目输入条件下同时满足物理稳定性与视觉保真度两个原本冲突的目标。

## 方法拆解

### 分层场景重建
- 输入单张 RGB 图像 I ∈ ℝ^{H_0×W_0×3}，输出初始场景 S^(0) 与仿真就绪场景 S^⋆。
- 物理层：VLM 解析交互区域与物体名称 {ℓ_i}，SAM 3 提取实例掩码 {M_i}，SAM 3D 重建带初始姿态的纹理网格 M_i。
- 视觉层：前景掩码后，VLM 引导修复缺失区域，生成式世界模型产出高斯泼溅场景 G_M。

### 姿态估计与规范对齐
- VGGT 预测相机几何与稠密点图 X_V，掩码引导的从粗到细固定尺度 ICP 精修 SAM 3D 初始姿态，拒绝旋转/平移过大的更新。
- RANSAC 拟合支撑平面估计规范系 W（原点为平台质心，−ê_z 为重力方向），物体姿态提升：T_{i→W}^{init} = T_{V→W} T_{i→V}^{init}（式1）。
- 机器人基座：校准数据用 T_{B→W} = T_{V→W} T_{B→V}，未校准数据从支撑平台几何初始化。

### 仿真就绪精修
- 场景图提取：GPT-4V 在 K=5 个随机化 SoM 覆盖上预测物理关系，多数投票定义 Support/Contact 边，仅支撑他人的物体固定为根 R。
- 交替优化：SDF 阶段最小化穿透、支撑、接触与正则化损失（λ_r=5）；物理阶段在 SAPIEN 中仿真，根物体运动学、其余动态，稳定姿态初始化下一轮。
- 姿态参数化：T_{i→W} = ΔT_i T_{i→W}^{init}，ΔT_i = [exp([Δr_i]_×) Δt_i; 0^T 1]（式2）。

### 分层渲染与数据生成
- 查询相机 Q 下，Isaac Sim 渲染物理层 (I_fg, D_fg, α_fg)，高斯泼溅层渲染 (I_bg, D_bg)，深度合成：I_out(u) = m(u) I_fg(u) + (1−m(u)) I_bg(u)，m(u) = 1[α_fg(u) > 0 ∧ D_fg(u) ≤ D_bg(u)]（式3）。
- 抓取中心技能用 AnyGrasp 初始化候选，cuRobo 转换为稠密关节空间动作。

## 关键创新

1. **单图像分层 real-to-sim 范式**：首次将物理关键交互区域与视觉上下文分离处理，使单目输入即可生成可交互、可编辑、可新视角复用的持久仿真场景，突破了此前多视角或人工精修的限制。
2. **交替 SDF-物理优化精修**：通过场景图引导的根物体识别与交替优化，将初始重建姿态收敛到物理稳定构型，显著降低仿真中的掉落与穿透（Falling 从 0.5640 降至 0.1026，Collision 从 0.3590 降至 0.0256）。
3. **大规模真实数据到仿真资产的转化**：构建 DROID-Sim（564 个场景），每个场景链接回原始 DROID 数据标识符，使 76k 演示、350 小时交互数据可追溯地转化为可复用仿真基础设施，支持策略微调与生成式评估代理。

## 实验与结果

### 视觉对齐（10 场景平均）
| 方法 | PSNR | SSIM | LPIPS | SIFT-MR | RGB-EMD | Gabor-L1 |
|---|---|---|---|---|---|---|
| RoLA | 13.40 | 0.4521 | 0.4996 | 0.0664 | 28.5806 | 0.001817 |
| RoboSnap | 13.25 | 0.4907 | 0.4958 | 0.1226 | 11.4795 | 0.000741 |

RoboSnap 在 SSIM、SIFT-MR、RGB-EMD、Gabor-L1 上优于 RoLA，PSNR 略低但差距微小，表明视觉保真度相当且特征匹配更优。

### 仿真稳定性（300 帧 Isaac Sim 步后）
| 方法 | Falling | Collision | Trans MSE | Mean disp. (m) | Quat MSE |
|---|---|---|---|---|---|
| SAM 3D | 0.5640 | 0.3590 | 0.1079 | 0.3284 | 0.1560 |
| SAM 3D + FoundationPose | 0.5900 | 0.1538 | 0.1921 | 0.4383 | 0.1703 |
| RoLA | 0.3810 | 0.3226 | 0.0736 | 0.2713 | 0.1093 |
| RoboSnap w/o refinement | 0.4320 | 0.2982 | 0.0977 | 0.3126 | 0.1255 |
| RoboSnap (ours) | 0.1026 | 0.0256 | 0.0022 | 0.0474 | 0.0178 |

RoboSnap 在全部指标上显著优于基线，精修环节贡献明显（w/o refinement 的 Falling 为 0.4320 vs 0.1026）。

### 轨迹重放（5 场景）
RoboSnap 5/5 成功，RoLA 2/5 成功。重放标准为夹爪抓住目标并移动到目标位置，无穿透或碰撞。

### 真实世界数据生成（π_0.5 平均成功率）
| 数据混合 | Real | R1 | R2 | R3 |
|---|---|---|---|---|
| π_0.5 | 32.7% | 35.7% | 41.7% | 17.3% |
| π_0 | 29.3% | 31.0% | 42.7% | 15.0% |

Ratio 2（0.6 真实 + 0.2 RoboSnap + 0.2 仿真增强）最佳，π_0.5 从 32.7% 提升至 41.7%，π_0 从 29.3% 提升至 42.7%（由表内数值计算）。Ratio 3 在无真实演示下仍实现非零成功率。

### 随机化鲁棒性（30 次试验）
| 条件 | Real-only 平均 | Mix Ratio 2 平均 |
|---|---|---|
| Orig. | 32.7 | 41.7 |
| Obj. | 16.7 | 33.0 |
| BG | 29.0 | 39.0 |
| Lt. | 26.3 | 37.3 |
| Tex. | 25.7 | 35.0 |
| Cam. | 13.3 | 31.7 |
| Arm | 5.66 | 23.3 |

真实-仿真联合训练将平均退化从 13% 降至 8%（跨扰动类型）。

### 生成式评估
Pearson 相关 r = 0.887，MMRV = 0.0066，表明 RoboSnap 生成的仿真场景可作为策略排序的可靠代理。

## 边界与局限

- 输入质量受限：严重遮挡、极端光照、视觉模糊材料会降低重建质量或生成演示可靠性。
- 物体范围有限：仅支持刚体和铰接物体，未处理可变形、颗粒或流体材料。
- 无专用物理参数估计流程：摩擦、质量等参数从 VLM 先验推断，铰接关节参数从标准数据集检索，可能不精确。
- 验证范围有限：仅在本文设置和模型上验证接口，更广泛的框架验证留待未来工作。
- 轨迹重放不优化物体姿态，不使用特权仿真回滚，仅评估静态场景恢复的准确性。

## 工程启示

- 复现时优先核对场景图提取的根物体识别质量——这是精修流程的起点，根物体错误会导致后续所有姿态优化失效。
- 物理精修的超参数（N_round=20, N_sdf=15, N_sim=200, N_damp=100, ε=10⁻⁴）对稳定性影响显著，建议先在小场景上验证收敛行为再扩展。
- 数据混合比例是关键决策：Ratio 2（0.6 真实 + 0.2 RoboSnap + 0.2 仿真增强）效果最佳，但 Ratio 3（无真实演示）仍能提供非零收益，适合真实数据稀缺场景。
- 最容易踩坑的是背景修复质量——高斯泼溅视觉层依赖修复后的图像，修复不佳会直接影响 novel views 的视觉一致性。
- 铰接物体处理依赖点基部件分割与数据集检索的运动学参数，若目标场景含非标准铰接结构，需额外人工标注。

## Overview
Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready scene. The key idea is a layered design that separates the physics-critical interaction area from the surrounding visual context: collision-aware foreground assets are refined for stable robot interaction, while a 3D Gaussian splatting visual layer preserves faithful background appearance under novel views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves reliable trajectory replay in the recovered scenes, supports task-specific synthetic data generation for policy training, and yields meaningful sim-real correlation for policy evaluation. To further support real-to-sim research, we introduce DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes in DROID. Extensive experiments suggest that the value of real-to-sim methods lies not only in high-fidelity visual reconstruction, but in turning real environments into reusable infrastructure for robot learning and evaluation.

## 参考
- https://arxiv.org/abs/2607.06699

## 개요

RoboSnap은 단일 RGB 이미지에서 물리적으로 안정적이고, 시각적 충실도가 높으며, 시뮬레이션에 바로 사용 가능한 계층적 장면을 자동으로 생성하여 로봇 정책 훈련 및 평가에 활용하는 방법을 제안합니다. 이 방법은 워싱턴 대학교 등 기관에서 개발했으며, 핵심 기여는 충돌 인식 상호작용 물리 계층과 3D 가우시안 스플래팅 시각적 컨텍스트 계층을 분리하고, 교대 SDF-물리 최적화를 통해 시뮬레이션 준비 정밀화를 구현한 것입니다. 564개의 DROID 장면으로 구축된 DROID-Sim 데이터셋을 통해 궤적 재생, 데이터 생성 및 sim-real 평가 정렬에서의 효율성을 검증했습니다.

## 그것이 바꾸는 것

기존 real-to-sim 파이프라인은 다중 시점 수집과 수동 정밀화에 의존하거나, 좁은 엔드포인트를 위한 검색 기반 디지털 트윈 또는 정적 배경을 출력하여, 재렌더링, 편집 및 새로운 시점에서 재사용 가능한 지속적 시뮬레이션 세계를 보편적으로 복원하지 못합니다. RoboSnap이 진정으로 바꾸는 것은 real-to-sim을 "시각적 재구성 작업"에서 "재사용 가능한 인프라 구축 작업"으로 재정의한 것입니다. 픽셀 단위 완벽함을 추구하지 않고, 물리적 상호작용 영역의 안정성과 시각적 컨텍스트의 충실도를 우선시하여 단일 이미지로 생성된 장면이 정책 미세 조정과 폐쇄 루프 평가를 직접 지원할 수 있게 합니다.

이 전환의 핵심은 계층적 설계에 있습니다. 물리 계층은 로봇 상호작용과 직접 관련된 객체와 지지 표면만 유지하고, 시각 계층은 가우시안 스플래팅으로 배경을 덮습니다. 이러한 분리를 통해 물리 정밀화가 소수의 핵심 자산에 집중할 수 있고, 시각 계층은 새로운 시점에서 외관 일관성을 유지하여 단안 입력 조건에서 물리적 안정성과 시각적 충실도라는 원래 충돌하는 두 목표를 동시에 충족합니다.

## 방법 분석

### 계층적 장면 재구성
- 단일 RGB 이미지 I ∈ ℝ^{H_0×W_0×3}를 입력으로 받아 초기 장면 S^(0)와 시뮬레이션 준비 장면 S^⋆를 출력합니다.
- 물리 계층: VLM이 상호작용 영역과 객체 이름 {ℓ_i}을 분석하고, SAM 3가 인스턴스 마스크 {M_i}를 추출하며, SAM 3D가 초기 자세를 가진 텍스처 메시 M_i를 재구성합니다.
- 시각 계층: 전경 마스크 후 VLM이 누락 영역 복원을 안내하고, 생성적 세계 모델이 가우시안 스플래팅 장면 G_M을 생성합니다.

### 자세 추정 및 표준 정렬
- VGGT가 카메라 기하학과 밀집 점 지도 X_V를 예측하고, 마스크 안내를 받은 조대정밀 고정 스케일 ICP가 SAM 3D 초기 자세를 정밀화하며, 회전/병진이 과도한 업데이트는 거부합니다.
- RANSAC이 지지 평면을 피팅하여 표준 좌표계 W(원점은 플랫폼 질량 중심, −ê_z는 중력 방향)를 추정하고, 객체 자세를 승격합니다: T_{i→W}^{init} = T_{V→W} T_{i→V}^{init} (식1).
- 로봇 베이스: 보정 데이터는 T_{B→W} = T_{V→W} T_{B→V}를 사용하고, 미보정 데이터는 지지 플랫폼 기하학에서 초기화합니다.

### 시뮬레이션 준비 정밀화
- 장면 그래프 추출: GPT-4V가 K=5개의 무작위화된 SoM 커버리지에서 물리적 관계를 예측하고, 다수결 투표로 Support/Contact 엣지를 정의하며, 다른 객체를 지지하는 객체만 루트 R로 고정합니다.
- 교대 최적화: SDF 단계는 침투, 지지, 접촉 및 정규화 손실(λ_r=5)을 최소화하고, 물리 단계는 SAPIEN에서 시뮬레이션하며, 루트 객체는 운동학적으로, 나머지는 동적으로 처리하고, 안정된 자세로 다음 라운드를 초기화합니다.
- 자세 파라미터화: T_{i→W} = ΔT_i T_{i→W}^{init}, ΔT_i = [exp([Δr_i]_×) Δt_i; 0^T 1] (식2).

### 계층적 렌더링 및 데이터 생성
- 쿼리 카메라 Q에서 Isaac Sim이 물리 계층 (I_fg, D_fg, α_fg)을 렌더링하고, 가우시안 스플래팅 계층이 (I_bg, D_bg)를 렌더링하며, 깊이 합성: I_out(u) = m(u) I_fg(u) + (1−m(u)) I_bg(u), m(u) = 1[α_fg(u) > 0 ∧ D_fg(u) ≤ D_bg(u)] (식3).
- 그리퍼 중심 스킬은 AnyGrasp로 후보를 초기화하고, cuRobo가 조밀한 관절 공간 동작으로 변환합니다.

## 핵심 혁신

1. **단일 이미지 계층적 real-to-sim 패러다임**: 물리적 핵심 상호작용 영역과 시각적 컨텍스트를 처음으로 분리 처리하여, 단안 입력만으로 상호작용 가능하고, 편집 가능하며, 새로운 시점에서 재사용 가능한 지속적 시뮬레이션 장면을 생성할 수 있게 되어, 기존의 다중 시점 또는 수동 정밀화 제한을 돌파했습니다.
2. **교대 SDF-물리 최적화 정밀화**: 장면 그래프 안내를 받은 루트 객체 식별과 교대 최적화를 통해 초기 재구성 자세를 물리적으로 안정적인 구성으로 수렴시켜, 시뮬레이션에서의 낙하 및 침투를 크게 줄였습니다(Falling 0.5640→0.1026, Collision 0.3590→0.0256).
3. **대규모 실제 데이터의 시뮬레이션 자산 변환**: DROID-Sim(564개 장면)을 구축하고, 각 장면을 원본 DROID 데이터 식별자에 연결하여 76k 데모, 350시간 상호작용 데이터를 추적 가능한 재사용 가능한 시뮬레이션 인프라로 변환하여 정책 미세 조정 및 생성적 평가 에이전트를 지원합니다.

## 실험 및 결과

### 시각적 정렬(10개 장면 평균)
| 방법 | PSNR | SSIM | LPIPS | SIFT-MR | RGB-EMD | Gabor-L1 |
|---|---|---|---|---|---|---|
| RoLA | 13.40 | 0.4521 | 0.4996 | 0.0664 | 28.5806 | 0.001817 |
| RoboSnap | 13.25 | 0.4907 | 0.4958 | 0.1226 | 11.4795 | 0.000741 |

RoboSnap은 SSIM, SIFT-MR, RGB-EMD, Gabor-L1에서 RoLA보다 우수하며, PSNR은 약간 낮지만 차이가 미미하여 시각적 충실도는 비슷하고 특징 매칭은 더 우수함을 보여줍니다.

### 시뮬레이션 안정성(300프레임 Isaac Sim 스텝 후)
| 방법 | Falling | Collision | Trans MSE | Mean disp. (m) | Quat MSE |
|---|---|---|---|---|---|
| SAM 3D | 0.5640 | 0.3590 | 0.1079 | 0.3284 | 0.1560 |
| SAM 3D + FoundationPose | 0.5900 | 0.1538 | 0.1921 | 0.4383 | 0.1703 |
| RoLA | 0.3810 | 0.3226 | 0.0736 | 0.2713 | 0.1093 |
| RoboSnap w/o refinement | 0.4320 | 0.2982 | 0.0977 | 0.3126 | 0.1255 |
| RoboSnap (ours) | 0.1026 | 0.0256 | 0.0022 | 0.0474 | 0.0178 |

RoboSnap은 모든 지표에서 기준선보다 크게 우수하며, 정밀화 단계의 기여가 뚜렷합니다(w/o refinement의 Falling 0.4320 vs 0.1026).

### 궤적 재생(5개 장면)
RoboSnap은 5/5 성공, RoLA는 2/5 성공. 재생 기준은 그리퍼가 목표 객체를 잡아 목표 위치로 이동하며, 침투나 충돌이 없어야 합니다.

### 실제 세계 데이터 생성(π_0.5 평균 성공률)
| 데이터 혼합 | Real | R1 | R2 | R3 |
|---|---|---|---|---|
| π_0.5 | 32.7% | 35.7% | 41.7% | 17.3% |
| π_0 | 29.3% | 31.0% | 42.7% | 15.0% |

Ratio 2(0.6 실제 + 0.2 RoboSnap + 0.2 시뮬레이션 증강)가 최적이며, π_0.5는 32.7%에서 41.7%로, π_0는 29.3%에서 42.7%로 향상되었습니다(표 내 값으로 계산). Ratio 3은 실제 데모 없이도 0이 아닌 성공률을 달성합니다.

### 무작위화 강건성(30회 시행)
| 조건 | Real-only 평균 | Mix Ratio 2 평균 |
|---|---|---|
| Orig. | 32.7 | 41.7 |
| Obj. | 16.7 | 33.0 |
| BG | 29.0 | 39.0 |
| Lt. | 26.3 | 37.3 |
| Tex. | 25.7 | 35.0 |
| Cam. | 13.3 | 31.7 |
| Arm | 5.66 | 23.3 |

실제-시뮬레이션 공동 훈련은 평균 성능 저하를 13%에서 8%로 줄였습니다(교란 유형 전체).

### 생성적 평가
Pearson 상관 r = 0.887, MMRV = 0.0066으로, RoboSnap이 생성한 시뮬레이션 장면이 정책 순위를 매기는 신뢰할 수 있는 대리자 역할을 할 수 있음을 보여줍니다.

## 경계 및 한계

- 입력 품질 제한: 심한 폐색, 극단적 조명, 시각적으로 흐릿한 재질은 재구성 품질이나 생성 데모 신뢰성을 저하시킬 수 있습니다.
- 객체 범위 제한: 강체 및 관절 객체만 지원하며, 변형 가능한 객체, 입자 또는 유체 재질은 처리하지 않습니다.
- 전용 물리 파라미터 추정 프로세스 없음: 마찰, 질량 등의 파라미터는 VLM 사전 지식에서 추론하고, 관절 조인트 파라미터는 표준 데이터셋에서 검색하므로 부정확할 수 있습니다.
- 검증 범위 제한: 본 논문의 설정과 모델에서만 인터페이스를 검증했으며, 더 광범위한 프레임워크 검증은 향후 작업으로 남겨둡니다.
- 궤적 재생은 객체 자세를 최적화하지 않고, 특권 시뮬레이션 롤백을 사용하지 않으며, 정적 장면 복원의 정확성만 평가합니다.

## 엔지니어링 시사점

- 재현 시 장면 그래프 추출의 루트 객체 식별 품질을 우선적으로 확인하세요. 이는 정밀화 프로세스의 시작점이며, 루트 객체 오류는 이후 모든 자세 최적화를 무효화합니다.
- 물리 정밀화 하이퍼파라미터(N_round=20, N_sdf=15, N_sim=200, N_damp=100, ε=10⁻⁴)는 안정성에 큰 영향을 미치므로, 작은 장면에서 수렴 동작을 먼저 검증한 후 확장하는 것이 좋습니다.
- 데이터 혼합 비율은 핵심 결정 사항입니다. Ratio 2(0.6 실제 + 0.2 RoboSnap + 0.2 시뮬레이션 증강)가 가장 효과적이지만, Ratio 3(실제 데모 없음)도 0이 아닌 이점을 제공하므로 실제 데이터가 부족한 시나리오에 적합합니다.
- 가장 쉽게 함정에 빠지는 부분은 배경 복원 품질입니다. 가우시안 스플래팅 시각 계층은 복원된 이미지에 의존하며, 복원이 좋지 않으면 새로운 시점의 시각적 일관성에 직접적인 영향을 미칩니다.
- 관절 객체 처리는 점 기반 부품 분할과 데이터셋에서 검색한 운동학 파라미터에 의존하므로, 대상 장면에 비표준 관절 구조가 포함된 경우 추가 수동 주석이 필요합니다.
