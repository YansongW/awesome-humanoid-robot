---
$id: ent_paper_lights_camera_malfunction_when_illuminat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color'
  zh: 'Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color'
  ko: 'Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color'
summary:
  en: Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however,
    their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE,
    an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping
    baseline task success rates to.
  zh: 本文由机器人鲁棒性研究团队提出，针对 VLA 模型在真实世界部署中对光照扰动的脆弱性，构建了 FLARE 物理聚光灯攻击框架与 ChromaGuard 色调保持对抗训练防御。核心贡献在于揭示朴素数据增强会让模型丢弃颜色信息、退化为形状偏置处理器，并提出在保留色度完整性的前提下实现光照鲁棒性的可行方案。
  ko: Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however,
    their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE,
    an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping
    baseline task success rates to.
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
- lights
- camera
- malfunction
- when
- illuminat
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
  title: 'arXiv:2607.14698 Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blin'
  url: https://arxiv.org/abs/2607.14698
  date: '2026-07-16'
  accessed_at: '2026-08-05'
---

## 概述

本文由机器人鲁棒性研究团队提出，针对 VLA 模型在真实世界部署中对光照扰动的脆弱性，构建了 FLARE 物理聚光灯攻击框架与 ChromaGuard 色调保持对抗训练防御。核心贡献在于揭示朴素数据增强会让模型丢弃颜色信息、退化为形状偏置处理器，并提出在保留色度完整性的前提下实现光照鲁棒性的可行方案。

## 它改变了什么

现有 VLA 鲁棒性研究几乎都聚焦于高级攻击——物理传感器欺骗、对抗样本、训练时后门注入，这些都需要攻击者具备特定知识或控制能力。但本文指出一个更根本、也更隐蔽的问题：模型在从仿真到真实、从实验室到部署时，对微小环境扰动（如光照角度或色温的轻微偏移）的失败，本质上源于泛化能力不足，而非安全漏洞被利用。这一判断将问题从“如何防御恶意攻击”重新定义为“如何提升对自然扰动的鲁棒性”，改变了讨论的框架。

更值得警惕的是作者发现的防御陷阱：朴素 HSV 数据增强（色调 ±180° 随机扰动）虽然能提升光照鲁棒性，却让模型把颜色当作可丢弃的噪声。灰度诊断实验显示，Naive-Aug 模型在灰度输入下成功率几乎不变（LIBERO-Object 上 90.5% vs. 89.8%），而 Baseline 则从 89.4% 跌至 10%。这意味着增强训练教会了模型“不要依赖颜色”，但对于颜色本身就是任务关键信息的场景（如按颜色抓取物体），这种鲁棒性是灾难性的——Naive-Aug 在颜色依赖任务上良性光照下成功率从 77.5% 跌至 47.5%，且 85.7% 的失败源于抓错颜色。这改变了“数据增强总是有益”的朴素认知。

## 方法拆解

### FLARE 攻击框架
- **威胁模型**：严格黑盒，攻击者无法访问模型架构、权重、梯度或训练数据；可在工作空间部署物理照明设备，控制位置、强度、色度，但部署后参数固定。
- **参数化**（公式 1）：θ = [h_light, s_light, v_light, I, z_light, α_cutoff]，涵盖色调、饱和度、明度、强度、空间高度与截止角。
- **目标函数**（公式 2）：L_i(θ) = (1/S) Σ_{t=1}^{S} ‖P_t^(i) − P_t'^(i)‖₂ + λ₁‖P_T^(i) − P_T'^(i)‖₂ + λ₂·𝕀_f^(i)，同时惩罚轨迹偏差与任务失败。
- **优化器**：选择 Optuna 的 TPE 采样器而非 GP-BO，理由是高维连续空间下 GP-BO 的计算开销随试验次数显著增长，在需要数百次高成本机器人 rollout 的场景成为瓶颈。
- **任务评估**：将 10 个 LIBERO 任务划分为两个各含 5 个任务的子集交替评估，防止优化过拟合到特定场景。

### ChromaGuard 防御
- **朴素增强基线**：参数 φ = [h, s, v, c, γ]ᵀ，从均匀分布采样，色调扰动范围 ±180°。
- **核心设计**：将增强参数空间限制为 Φ_CG，允许饱和度 [0.0, 4.0]、明度 [0.2, 3.0]、对比度 [0.8, 1.2]、锐度 [0.5, 1.5] 的有界扰动，但显式固定色调扰动为零（h = 0）。
- **对抗训练目标**：min_w 𝔼_{x,y}[max_{φ∈Φ_CG} L(f_w(T(x;φ)), y)]，在色调受限空间内优化最坏情况光照。

### 实验设置
- 仿真：LeRobot + LIBERO + MuJoCo，SmolVLA 训练 200,000 步，每套件 500 个评估回合。
- 真实世界：6-DoF SO-101 Arm Pro，双摄像头，外部可编程 RGB 聚光灯；SmolVLA 与 π_0.5 各微调 100,000 步；颜色不变任务 50 回合数据、20 次试验，颜色依赖任务 240 回合数据、40 次试验。

## 关键创新

1. **将“泛化失败”与“安全攻击”明确区分**：作者用 FLARE 证明，无需任何模型内部知识，仅通过物理光照调整就能将 Baseline 成功率降至 0.0%，最大轨迹误差达 115.5 cm。这比高级攻击更易实施、更难防御，因为它利用的是模型本身的泛化缺陷而非安全漏洞。

2. **揭示“鲁棒性-色觉”权衡**：灰度诊断实验首次量化了朴素增强的代价——模型在丢弃颜色噪声的同时也丢弃了颜色语义。这一发现对依赖颜色线索的机器人任务（分拣、装配）具有直接警示意义，此前文献未系统讨论过这一副作用。

3. **ChromaGuard 的“定向鲁棒”思路**：不是无差别增强，而是将扰动空间限制在保留色度完整性的子空间内。真实世界实验中，SmolVLA 在颜色依赖任务上良性条件达 97.5%、攻击下达 92.5%，而 Naive-Aug 分别仅为 47.5% 和 40.0%，且失败主因是抓错颜色（85.7% vs. ChromaGuard 的 0%）。

## 实验与结果

### 仿真攻击评估（表 1 关键数据）

| 任务套件 | 模型 | 攻击 | SR (%) | TE-Avg (cm) | TE-Max (cm) |
|---|---|---|---|---|---|
| LIBERO-Spatial | Baseline | Optimized | 0.0 | 22.3 | 67.6 |
| | Naive-Aug | Optimized | 78.8 | 4.23 | 40.3 |
| LIBERO-Object | Baseline | Optimized | 0 | 29.1 | 88.3 |
| | Naive-Aug | Optimized | 93.2 | 4.99 | 41.8 |
| LIBERO-10 | Baseline | Optimized | 0.0 | 36.3 | 115.5 |
| | Naive-Aug | Optimized | 47.2 | 9.0 | 64.0 |

优化攻击将 Baseline 成功率全部降至 0.0%，而 Naive-Aug 保持较高成功率，说明朴素增强确实提升了光照鲁棒性。

### 灰度诊断（表 2 关键数据）

| 任务套件 | 模型 | Benign (RGB) SR (%) | Grayscale SR (%) |
|---|---|---|---|
| LIBERO-Spatial | Baseline | 81.2 | 0 |
| | Naive-Aug | 79.4 | 80.1 |
| LIBERO-Object | Baseline | 89.4 | 10 |
| | Naive-Aug | 89.8 | 90.5 |
| LIBERO-10 | Baseline | 58.4 | 0 |
| | Naive-Aug | 50.2 | 47.8 |

Naive-Aug 在灰度下性能几乎不变，Baseline 则崩溃，证实朴素增强导致颜色信息被丢弃。

### 真实世界实验（表 3 关键数据）

| 基础模型 | 模型 | 颜色不变 Attack SR (%) | 颜色依赖 Benign SR (%) | 颜色依赖 Attack SR (%) |
|---|---|---|---|---|
| SmolVLA | Baseline | 0.0 | 77.5 | 27.5 |
| | Naive-Aug | 70.0 | 47.5 | 40.0 |
| | ChromaGuard | 70.0 | 97.5 | 92.5 |
| π_0.5 | Baseline | 30.0 | 47.5 | 12.5 |
| | Naive-Aug | 75.0 | 40.0 | 47.5 |
| | ChromaGuard | 75.0 | 55.0 | 70.0 |

ChromaGuard 在 SmolVLA 上显著优于 Naive-Aug，颜色依赖任务良性条件提升 50 个百分点（由表内 47.5%→97.5% 计算）。π_0.5 提升有限，作者归因于其预训练模型本身在良性场景就有 66.7% 的失败源于抓错颜色，是 SmolVLA 对应比例（11.1%）的六倍。

## 边界与局限

作者明确声明 FLARE 与 ChromaGuard 是分析工具而非最终攻防方案，未探索时间动态光照或闭环自适应攻击。真实世界实验仅覆盖两种模型、两个任务类型，π_0.5 的较差表现提示防御效果可能受基础模型预训练质量制约。仿真到真实的迁移依赖先仿真优化再选真实攻击的两阶段流程，未验证端到端迁移的可靠性。灰度诊断仅作为间接证据，未直接测量模型内部表征的颜色编码强度。论文未明确讨论 ChromaGuard 在颜色本身是唯一区分特征（如形状完全相同）时的极限，也未给出训练成本对比。

## 工程启示

复现时最先核对的是增强参数范围：Naive-Aug 的色调扰动 ±180° 是导致颜色丢弃的直接原因，ChromaGuard 将其固定为零是全部改进的来源。最容易踩坑的地方是任务评估策略——如果不在每次优化迭代中交替评估任务子集，FLARE 会过拟合到少数场景，导致真实世界攻击效果虚高。对于下游团队，若任务依赖颜色线索，务必用灰度输入做一次诊断测试：若模型在灰度下性能不降，说明颜色信息已被丢弃，需要检查增强配置。π_0.5 的结果提醒我们，防御策略的效果上限受基础模型预训练质量约束，选择基础模型时需评估其颜色敏感度。真实世界攻击生成依赖仿真候选，建议先在小规模仿真中验证攻击参数的可迁移性，再投入真实硬件实验。

## Overview
Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals. While adversarial training is the standard countermeasure, we identify a critical and previously underestimated defensive pitfall: naive data augmentations incorrectly condition VLA models to discard color as noise, collapsing their visual perception into a purely shape-biased processor. We expose this degradation through a diagnostic grayscale evaluation, in which the defended model maintains high success rates on grayscale inputs, while its success rate on benign, color-dependent real-world tasks drops to at most 47.5%, well below the undefended baseline. To address this, we propose ChromaGuard, a chroma-preserving adversarial training method. On a physical 6-DoF robotic platform, we demonstrate that ChromaGuard achieves 97.5% and 92.5% success rates in benign and attacked color-dependent tasks, respectively.

## 参考
- https://arxiv.org/abs/2607.14698

## 개요

본 논문은 로봇 견고성 연구팀이 제안한 것으로, VLA 모델이 실제 환경 배포 시 조명 교란에 취약하다는 점을 겨냥하여 FLARE 물리적 스포트라이트 공격 프레임워크와 ChromaGuard 색조 유지 적대적 훈련 방어를 구축했습니다. 핵심 기여는 단순 데이터 증강이 모델이 색상 정보를 버리고 형태 편향 처리기로 퇴화하게 만든다는 점을 밝히고, 색도 완전성을 유지하면서 조명 견고성을 달성하는 실행 가능한 방안을 제시한 것입니다.

## 그것이 바꾼 것

기존 VLA 견고성 연구는 거의 모두 고급 공격(물리적 센서 속임, 적대적 샘플, 훈련 시 백도어 주입)에 초점을 맞추었으며, 이러한 공격은 공격자가 특정 지식이나 제어 능력을 보유해야 합니다. 그러나 본 논문은 더 근본적이고 더 은밀한 문제를 지적합니다. 모델이 시뮬레이션에서 실제로, 실험실에서 배포로 전환될 때 미세한 환경 교란(예: 조명 각도나 색온도의 약간의 변화)에 실패하는 것은 본질적으로 보안 취약점이 악용된 것이 아니라 일반화 능력 부족에서 비롯된다는 것입니다. 이러한 판단은 문제를 "악의적 공격을 어떻게 방어할 것인가"에서 "자연적 교란에 대한 견고성을 어떻게 향상시킬 것인가"로 재정의하여 논의 프레임워크를 바꿉니다.

더욱 경계해야 할 점은 저자가 발견한 방어 함정입니다. 단순 HSV 데이터 증강(색조 ±180° 무작위 교란)은 조명 견고성을 향상시킬 수 있지만, 모델이 색상을 버릴 수 있는 노이즈로 취급하게 만듭니다. 그레이스케일 진단 실험에 따르면 Naive-Aug 모델은 그레이스케일 입력에서 성공률이 거의 변하지 않았으며(LIBERO-Object에서 90.5% vs. 89.8%), Baseline은 89.4%에서 10%로 급락했습니다. 이는 증강 훈련이 모델에게 "색상에 의존하지 말라"고 가르쳤음을 의미하지만, 색상 자체가 작업의 핵심 정보인 시나리오(예: 색상별 물체 집기)에서는 이러한 견고성이 치명적입니다. Naive-Aug는 색상 의존 작업에서 양호한 조명 하 성공률이 77.5%에서 47.5%로 떨어졌고, 실패의 85.7%가 잘못된 색상을 집는 데서 비롯되었습니다. 이는 "데이터 증강은 항상 유익하다"는 단순한 인식을 바꿉니다.

## 방법 분석

### FLARE 공격 프레임워크
- **위협 모델**: 엄격한 블랙박스로, 공격자는 모델 아키텍처, 가중치, 그래디언트 또는 훈련 데이터에 접근할 수 없습니다. 작업 공간에 물리적 조명 장치를 배치하여 위치, 강도, 색도를 제어할 수 있지만 배포 후 매개변수는 고정됩니다.
- **매개변수화**(수식 1): θ = [h_light, s_light, v_light, I, z_light, α_cutoff], 색조, 채도, 명도, 강도, 공간 높이 및 차단 각도를 포함합니다.
- **목적 함수**(수식 2): L_i(θ) = (1/S) Σ_{t=1}^{S} ‖P_t^(i) − P_t'^(i)‖₂ + λ₁‖P_T^(i) − P_T'^(i)‖₂ + λ₂·𝕀_f^(i), 궤적 편차와 작업 실패를 동시에 페널티합니다.
- **최적화 도구**: GP-BO 대신 Optuna의 TPE 샘플러를 선택한 이유는 고차원 연속 공간에서 GP-BO의 계산 비용이 실험 횟수에 따라 크게 증가하여 수백 회의 고비용 로봇 rollout이 필요한 시나리오에서 병목이 되기 때문입니다.
- **작업 평가**: 10개의 LIBERO 작업을 각각 5개 작업으로 구성된 두 하위 집합으로 나누어 교대로 평가하여 최적화가 특정 시나리오에 과적합되는 것을 방지합니다.

### ChromaGuard 방어
- **단순 증강 기준선**: 매개변수 φ = [h, s, v, c, γ]ᵀ, 균등 분포에서 샘플링, 색조 교란 범위 ±180°.
- **핵심 설계**: 증강 매개변수 공간을 Φ_CG로 제한하여 채도 [0.0, 4.0], 명도 [0.2, 3.0], 대비 [0.8, 1.2], 선명도 [0.5, 1.5]의 유계 교란을 허용하지만 색조 교란은 명시적으로 0으로 고정합니다(h = 0).
- **적대적 훈련 목표**: min_w 𝔼_{x,y}[max_{φ∈Φ_CG} L(f_w(T(x;φ)), y)], 색조 제한 공간 내에서 최악의 경우 조명을 최적화합니다.

### 실험 설정
- 시뮬레이션: LeRobot + LIBERO + MuJoCo, SmolVLA 200,000 스텝 훈련, 각 스위트당 500회 평가 에피소드.
- 실제 세계: 6-DoF SO-101 Arm Pro, 이중 카메라, 외부 프로그래밍 가능 RGB 스포트라이트; SmolVLA와 π_0.5 각각 100,000 스텝 미세 조정; 색상 불변 작업 50 에피소드 데이터, 20회 시도, 색상 의존 작업 240 에피소드 데이터, 40회 시도.

## 핵심 혁신

1. **"일반화 실패"와 "보안 공격"을 명확히 구분**: 저자는 FLARE를 통해 모델 내부 지식 없이도 물리적 조명 조정만으로 Baseline 성공률을 0.0%로 낮출 수 있고 최대 궤적 오차가 115.5cm에 달함을 증명했습니다. 이는 고급 공격보다 실행이 쉽고 방어가 더 어렵습니다. 보안 취약점이 아닌 모델 자체의 일반화 결함을 활용하기 때문입니다.

2. **"견고성-색각" 트레이드오프 규명**: 그레이스케일 진단 실험은 단순 증강의 대가를 처음으로 정량화했습니다. 모델이 색상 노이즈를 버리는 동시에 색상 의미론도 버린다는 것입니다. 이 발견은 색상 단서에 의존하는 로봇 작업(분류, 조립)에 직접적인 경고 의미를 가지며, 기존 문헌에서는 이 부작용을 체계적으로 논의하지 않았습니다.

3. **ChromaGuard의 "방향성 견고성" 접근**: 무차별 증강이 아니라 교란 공간을 색도 완전성을 보존하는 부분 공간으로 제한합니다. 실제 세계 실험에서 SmolVLA는 색상 의존 작업에서 양호 조건 97.5%, 공격 조건 92.5%를 달성한 반면 Naive-Aug는 각각 47.5%와 40.0%에 불과했으며, 실패의 주요 원인은 잘못된 색상 집기였습니다(85.7% vs. ChromaGuard의 0%).

## 실험 및 결과

### 시뮬레이션 공격 평가(표 1 핵심 데이터)

| 작업 스위트 | 모델 | 공격 | SR (%) | TE-Avg (cm) | TE-Max (cm) |
|---|---|---|---|---|---|
| LIBERO-Spatial | Baseline | Optimized | 0.0 | 22.3 | 67.6 |
| | Naive-Aug | Optimized | 78.8 | 4.23 | 40.3 |
| LIBERO-Object | Baseline | Optimized | 0 | 29.1 | 88.3 |
| | Naive-Aug | Optimized | 93.2 | 4.99 | 41.8 |
| LIBERO-10 | Baseline | Optimized | 0.0 | 36.3 | 115.5 |
| | Naive-Aug | Optimized | 47.2 | 9.0 | 64.0 |

최적화 공격은 Baseline 성공률을 모두 0.0%로 낮췄지만 Naive-Aug는 높은 성공률을 유지하여 단순 증강이 실제로 조명 견고성을 향상시켰음을 보여줍니다.

### 그레이스케일 진단(표 2 핵심 데이터)

| 작업 스위트 | 모델 | Benign (RGB) SR (%) | Grayscale SR (%) |
|---|---|---|---|
| LIBERO-Spatial | Baseline | 81.2 | 0 |
| | Naive-Aug | 79.4 | 80.1 |
| LIBERO-Object | Baseline | 89.4 | 10 |
| | Naive-Aug | 89.8 | 90.5 |
| LIBERO-10 | Baseline | 58.4 | 0 |
| | Naive-Aug | 50.2 | 47.8 |

Naive-Aug는 그레이스케일에서 성능이 거의 변하지 않았고 Baseline은 붕괴하여 단순 증강이 색상 정보 폐기를 초래함을 확인했습니다.

### 실제 세계 실험(표 3 핵심 데이터)

| 기본 모델 | 모델 | 색상 불변 Attack SR (%) | 색상 의존 Benign SR (%) | 색상 의존 Attack SR (%) |
|---|---|---|---|---|
| SmolVLA | Baseline | 0.0 | 77.5 | 27.5 |
| | Naive-Aug | 70.0 | 47.5 | 40.0 |
| | ChromaGuard | 70.0 | 97.5 | 92.5 |
| π_0.5 | Baseline | 30.0 | 47.5 | 12.5 |
| | Naive-Aug | 75.0 | 40.0 | 47.5 |
| | ChromaGuard | 75.0 | 55.0 | 70.0 |

ChromaGuard는 SmolVLA에서 Naive-Aug보다 현저히 우수하며, 색상 의존 작업 양호 조건에서 50퍼센트 포인트 향상(표 내 47.5%→97.5% 계산)을 보였습니다. π_0.5의 향상은 제한적이며, 저자는 사전 훈련 모델 자체가 양호 시나리오에서도 실패의 66.7%가 잘못된 색상 집기에서 비롯되었고, 이는 SmolVLA의 해당 비율(11.1%)의 6배이기 때문이라고 설명합니다.

## 경계 및 한계

저자는 FLARE와 ChromaGuard가 최종 공격/방어 솔루션이 아닌 분석 도구임을 명시적으로 선언했으며, 시간적 동적 조명이나 폐루프 적응형 공격을 탐구하지 않았습니다. 실제 세계 실험은 두 모델, 두 작업 유형만을 다루었으며, π_0.5의 저조한 성능은 방어 효과가 기본 모델의 사전 훈련 품질에 의해 제약될 수 있음을 시사합니다. 시뮬레이션-실제 전이는 먼저 시뮬레이션에서 최적화한 후 실제 공격을 선택하는 2단계 프로세스에 의존하며, 엔드투엔드 전이의 신뢰성은 검증되지 않았습니다. 그레이스케일 진단은 간접 증거일 뿐 모델 내부 표현의 색상 인코딩 강도를 직접 측정하지 않았습니다. 논문은 색상 자체가 유일한 구별 특징(예: 형태가 완전히 동일한 경우)일 때 ChromaGuard의 한계를 명시적으로 논의하지 않았으며 훈련 비용 비교도 제공하지 않았습니다.

## 공학적 시사점

재현 시 가장 먼저 확인해야 할 것은 증강 매개변수 범위입니다. Naive-Aug의 색조 교란 ±180°는 색상 폐기의 직접적 원인이며, ChromaGuard가 이를 0으로 고정한 것이 모든 개선의 원천입니다. 가장 함정에 빠지기 쉬운 곳은 작업 평가 전략입니다. 각 최적화 반복에서 작업 하위 집합을 교대로 평가하지 않으면 FLARE가 소수 시나리오에 과적합되어 실제 세계 공격 효과가 부풀려질 수 있습니다. 하류 팀의 경우 작업이 색상 단서에 의존한다면 반드시 그레이스케일 입력으로 진단 테스트를 수행해야 합니다. 모델이 그레이스케일에서 성능이 떨어지지 않으면 색상 정보가 이미 폐기된 것이므로 증강 구성을 점검해야 합니다. π_0.5의 결과는 방어 전략의 효과 상한이 기본 모델의 사전 훈련 품질에 의해 제약된다는 점을 상기시키며, 기본 모델 선택 시 색상 민감도를 평가해야 합니다. 실제 세계 공격 생성은 시뮬레이션 후보에 의존하므로 먼저 소규모 시뮬레이션에서 공격 매개변수의 전이 가능성을 검증한 후 실제 하드웨어 실험에 투자하는 것이 좋습니다.
