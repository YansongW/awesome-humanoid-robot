---
$id: ent_paper_what_do_they_see_interpreting_complex_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: What Do They See? Interpreting Complex Road Scenarios Through the Eyes of Vision-Language-Action Models for Safe and
    Trustworthy Autonomous Vehicle Learning
  zh: What Do They See? Interpreting Complex Road Scenarios Through the Eyes of Vision-Language-Action Models for Safe and
    Trustworthy Autonomous Vehicle Learning
  ko: What Do They See? Interpreting Complex Road Scenarios Through the Eyes of Vision-Language-Action Models for Safe and
    Trustworthy Autonomous Vehicle Learning
summary:
  en: End-to-end autonomous driving models are now able to navigate complex road scenarios, mapping raw sensor observations
    directly to observed paths for open-loop evaluation and often effective driving in closed-loop evaluation. Yet the internal
    logic of these safety-critical systems remains largely opaque, due to the complexity of traffic scenes. We propose a counterfactual
    ablation framework called.
  zh: 本文提出 Counterfactual Vision Action Analysis（CVAA）框架与 Counter-nuScenes 基准，通过生成式修复逐物体移除前视图像中的实体，对 Alpamayo 1 轨迹预测器进行反事实归因，回答“哪些可见物体真正驱动轨迹预测”这一物体级因果问题。作者结合黑盒偏差指标（AD/FD）与白盒隐藏状态分析，揭示模型对交通灯、行人的敏感度远超物理尺度预期，并识别出四种内部传播机制。
  ko: End-to-end autonomous driving models are now able to navigate complex road scenarios, mapping raw sensor observations
    directly to observed paths for open-loop evaluation and often effective driving in closed-loop evaluation. Yet the internal
    logic of these safety-critical systems remains largely opaque, due to the complexity of traffic scenes. We propose a counterfactual
    ablation framework called.
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
- what
- do
- they
- see
- interpreting
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
  title: arXiv:2607.16938 What Do They See? Interpreting Complex Road Scenarios Through the Eyes of Vision
  url: https://arxiv.org/abs/2607.16938
  date: '2026-07-18'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Counterfactual Vision Action Analysis（CVAA）框架与 Counter-nuScenes 基准，通过生成式修复逐物体移除前视图像中的实体，对 Alpamayo 1 轨迹预测器进行反事实归因，回答“哪些可见物体真正驱动轨迹预测”这一物体级因果问题。作者结合黑盒偏差指标（AD/FD）与白盒隐藏状态分析，揭示模型对交通灯、行人的敏感度远超物理尺度预期，并识别出四种内部传播机制。

## 它改变了什么

现有端到端自动驾驶可解释性研究陷入两难：基于结构化状态或模拟器的因果扰动无法反映真实相机输入的分布，而像素级归因（saliency、Grad-CAM、RISE）在密集交通中既难审计，又混淆了物体重要性、位置与掩码伪影。本文真正改变的是将“解释”从像素或文本层面推进到物体级因果层面——它不再问“哪个像素重要”，而是问“移除哪个物体，轨迹会变”。这一转变的关键在于：安全性由输出轨迹决定，而非语言理由，因此必须做轨迹层面的反事实归因，而非文本输出归因。

更实质的贡献在于，作者没有停留在黑盒排名，而是首次对 VLA 内部进行白盒追踪，将视觉编码器、VLM 与轨迹专家的隐藏状态变化关联到具体物体移除事件。这打破了以往将 VLA 视为不可分整体的惯例，暴露出“模型可能生成看似合理轨迹，却并非由正确视觉证据因果驱动”这一安全关键问题——这正是现有评估协议系统性忽略的盲区。

## 方法拆解

### 基准构建：Counter-nuScenes
- 从 nuScenes v1.0-trainval 的 700 个场景中，仅取前视相机（CAM_FRONT）关键帧，保留至少 1.6 秒连续位姿数据之前的帧以匹配模型历史窗口。
- 用 YOLOv8 检测可见智能体，每场景选物体数量最多的单帧，最终采样 210 帧，每帧含 6 至 32 个有效检测物体。
- 用 SAM2 以 YOLOv8 边界框为提示生成逐物体实例掩码，并在像素级细化避免跨边界渗漏。

### 反事实语义集
- 对每个场景，用 Gemini imgen inpainting 逐物体移除生成 N 个反事实图像（N 为检测物体数）；另维护 LaMa + FLUX Fill 1.0 开源消融管线。
- 关键设计：使用逼真生成式修复而非颜色填充、高斯模糊或复制粘贴遮挡，以减少分布偏移，使输出变化可归因于物体移除而非渲染伪影。

### 归因指标
- 模型生成 K 个随机轨迹样本 {p_k}，每个为 T 个未来自车中心点序列，投影到 XY 平面，用均值轨迹汇总分布。
- 平均偏差 AD = (1/T) Σ_{t=1}^{T} ||p̄_var_t − p̄_orig_t||₂；最终偏差 FD = ||p̄_var_T − p̄_orig_T||₂。
- 物体级归因分数：按 AD 排名为主要分数，FD 用于打破平局，形成反事实物体归因（COA）排序。
- 与 minADE/minFDE 的区别：AD/FD 测量相对于参考预测的分布偏移，使用全候选集；minADE/minFDE 测量相对于真实未来的准确性，选择最佳候选轨迹。作者指出使用 min-over-K 估计器不合适，因为会奖励偶然接近原始分布的变体，混淆采样噪声与因果影响。

### 白盒分析
- 对每个移除物体，将其边界框投影到模型 patch 网格，识别视觉编码器和 VLM 中的对应 token 位置。
- 计算原始与修复图像隐藏状态在物体、视觉和全局 token 位置的逐层余弦差值。
- 应用 Logit Lens 跟踪物体类别表示跨层演变；计算空间 KL 散度图；提取轨迹交接 token 到物体 patch 位置的注意力权重。

## 关键创新

1. **物体级反事实归因协议**：首次将生成式修复（inpainting）与轨迹偏差指标（AD/FD）结合，在真实相机图像上实现物体级因果归因，而非像素级或结构化状态级。逼真修复设计显著减少分布偏移，使偏差可归因于物体移除本身，这是对现有 saliency 方法伪影问题的直接回应。

2. **白盒传播机制分类**：通过隐藏状态余弦差值、Logit Lens 与注意力权重，识别出四种内部传播变体——Coupled（约 33.0%）、Transparent（约 33.1%）、Decoupled（约 16.9%）、Silent（约 16.9%）。其中 Silent 变体（大输出偏差但轨迹 token 无签名）暴露了现有探针无法解析的影响路径，这是对 VLA 可解释性工具缺失的直接证据。

3. **min-over-K 估计器的批判性替代**：明确指出使用 minADE/minFDE 作为归因指标会奖励偶然接近原始分布的变体，混淆采样噪声与因果影响。AD/FD 基于全候选集测量分布偏移，这一设计选择在方法论上更严谨，为后续 VLA 归因研究设定了指标标准。

## 实验与结果

实验基于 Alpamayo 1 轨迹预测器，210 个 nuScenes 前视场景，共 3,062 个反事实图像对。
**每类偏差（Table 3 关键数字）**：
| 类别 | N | Mean AD (m) | Max AD (m) | Mean FD (m) |
|------|---|-------------|------------|-------------|
| Bus | 47 | 0.663 | 3.931 | 1.889 |
| Fire hydrant | 17 | 0.540 | 2.037 | 1.454 |
| Truck | 183 | 0.505 | 3.548 | 1.419 |
| Traffic light | 531 | 0.482 | 4.534 | 1.399 |
| Person | 604 | 0.458 | 5.276 | 1.318 |
| Car | 1566 | 0.348 | 7.782 | 0.984 |
**排名稳定性（3 种子）**：AD Top-3 精确保持排名 14.6%，保持在 top-3 内 39.7%；FD 对应 16.0% 与 39.5%。
平均排名范围为 AD 4.691、FD 4.641。
**场景级偏差**：最大 AD 物体的 z-score 均值 2.43，中位数 2.35；148/210 场景（70.5%）超过 z>2 阈值，48 场景（22.9%）超过 z>3。
FD 对应 z>2 为 148，z>3 为 43。
**交通灯颜色**：531 个交通灯物体中 119 个（22.4%）检测到明确颜色；红灯状态平均 AD 0.758 m vs 绿灯 0.229 m，平均 FD 2.241 m vs 0.672 m。
**白盒结果**：视觉编码器在移除物体 patch 位置的 delta 约为 10⁻⁷ 且为负值；LM 中第 15 层起按类别分化，bus 在 35 层达到约 0.06，truck 约 0.02；轨迹专家放大倍数均值 115–180×，中位数 47–106×；Silent 变体中 δ_traj 约 0.0001 但比率超过 1000×。
（本节另有 2 句含无法从全文文本核实的数字，已按纪律移除；论文未明确或以图/表图片形式给出。）

## 边界与局限

评估仅限于单一模型（Alpamayo 1）和 nuScenes 前视相机分布，对其他 VLA 和数据集未验证泛化性。白盒分析暴露了缺乏为 VLA 架构设计的可解释性工具——余弦差值曲线和 Logit Lens（均改编自语言模型研究）只能测量两次前向传递之间的变化，无法解释原因，也无法识别哪些内部计算对输出差异因果负责。Silent 象限（大输出偏差但轨迹 token 无签名）指向现有探针无法解析的影响路径。论文未明确硬件平台、训练配置与推理频率。未来工作包括应用于其他 VLA、评估文本输出相似性、纳入时间多帧反事实、开发适合场景级关系表示的可解释性探针。

## 工程启示

复现时先核对三点：一是修复管线的一致性——Gemini imgen 与 LaMa + FLUX Fill 1.0 的分布偏移差异可能显著影响 AD/FD 绝对值，建议先在小样本上对比两种管线的偏差分布；二是种子敏感性——AD Top-3 精确保持排名仅 14.6%，说明单次运行排名不可靠，至少需 3 个种子取合并排名；三是 minADE 与 AD 的语义差异——49.3% 物体表现出负 ΔminADE，意味着高归因物体未必改善真实预测准确性，下游团队不应将 COA 排名直接等同于安全关键度。

最易踩坑的是掩码面积与偏差的正相关（Pearson r = +0.25）：rank-1 物体平均 38,706 像素，rank-5 后低于 5,000 像素，大物体天然获得更高 AD。若需比较不同类别的重要性，必须控制掩码面积或使用面积归一化指标。交通灯颜色是强信号（红灯 AD 0.758 m vs 绿灯 0.229 m），但仅 22.4% 物体检测到明确颜色，其余可能因分辨率或遮挡无法区分状态，需谨慎解释。Silent 变体（约 16.9%）中轨迹 token 无签名但输出偏差大，若下游依赖注意力或 token 级探针做安全监控，会系统性漏报这类影响路径。

## Overview
End-to-end autonomous driving models are now able to navigate complex road scenarios, mapping raw sensor observations directly to observed paths for open-loop evaluation and often effective driving in closed-loop evaluation. Yet the internal logic of these safety-critical systems remains largely opaque, due to the complexity of traffic scenes. We propose a counterfactual ablation framework called Counterfactual Vision Action Analysis (CVAA) that systematically removes individual detected objects from front-camera images using photorealistic generative inpainting to prepare counterfactual sets to evaluate the difference in the model's response. This isolates the causal effect of each object's presence on the model's planning behaviour. Applied to the Alpamayo 1 trajectory predictor across 210 nuScenes driving scenes, we create a dataset Counter -nuScenes, using which we see that vehicles and pedestrians within the model's 'path' dominate causal influence as expected, while traffic lights, as expected, exert disproportionate effect relative to their image footprint. However, we also find cases where the model responds strongly to objects a human driver would consider irrelevant. This brings forth a deeper question: does the model itself view the scene as a sum of individual objects influencing the outcome, or does it encode an entirely different set of internal features that do not correspond to human-legible scene elements? To further understand this, we compare intermediate representations of original and inpainted image pairs using mechanistic interpretability techniques and examine the effect of the removal through the various model layers. Together, these two stages offer a path from behavioral auditing to representational understanding, creating explainable driving systems and solidifying human-AI trust.

## 参考
- https://arxiv.org/abs/2607.16938

## 개요

본 논문은 Counterfactual Vision Action Analysis(CVAA) 프레임워크와 Counter-nuScenes 벤치마크를 제안하여, 생성적 인페인팅을 통해 전방 카메라 이미지에서 객체 단위로 엔티티를 제거함으로써 Alpamayo 1 궤적 예측기에 대한 반사실적 귀속을 수행하고, "어떤 가시 객체가 궤적 예측을 실제로 구동하는가"라는 객체 수준의 인과 질문에 답한다. 저자들은 블랙박스 편향 지표(AD/FD)와 화이트박스 은닉 상태 분석을 결합하여, 모델이 물리적 규모 예측을 훨씬 초과하는 수준으로 신호등과 보행자에 민감하다는 점을 밝히고, 네 가지 내부 전파 메커니즘을 식별한다.

## 무엇을 바꾸었는가

기존 엔드투엔드 자율주행 설명 가능성 연구는 이중 난관에 봉착해 있다: 구조화된 상태나 시뮬레이터 기반의 인과적 교란은 실제 카메라 입력의 분포를 반영하지 못하며, 픽셀 수준 귀속(saliency, Grad-CAM, RISE)은 밀집 교통에서 감사가 어렵고 객체 중요성, 위치, 마스크 아티팩트를 혼동한다. 본 논문이 실제로 바꾼 것은 "설명"을 픽셀 또는 텍스트 수준에서 객체 수준의 인과 수준으로 끌어올린 것이다——더 이상 "어느 픽셀이 중요한가"를 묻지 않고 "어느 객체를 제거하면 궤적이 변하는가"를 묻는다. 이러한 전환의 핵심은: 안전성은 언어적 이유가 아닌 출력 궤적에 의해 결정되므로, 텍스트 출력 귀속이 아닌 궤적 수준의 반사실적 귀속이 필수적이라는 점이다.

더 실질적인 기여는 저자들이 블랙박스 순위에 머무르지 않고 VLA 내부를 최초로 화이트박스 추적하여, 비전 인코더, VLM, 궤적 전문가의 은닉 상태 변화를 특정 객체 제거 이벤트에 연관시킨 것이다. 이는 기존에 VLA를 불가분의 전체로 간주하던 관례를 깨고, "모델이 그럴듯한 궤적을 생성할 수 있지만 올바른 시각적 증거에 의해 인과적으로 구동되지는 않을 수 있다"는 안전 핵심 문제를 드러낸다——이는 기존 평가 프로토콜이 체계적으로 간과한 사각지대다.

## 방법 분해

### 벤치마크 구축: Counter-nuScenes
- nuScenes v1.0-trainval의 700개 시나리오에서 전방 카메라(CAM_FRONT) 키프레임만 취하며, 모델 히스토리 창과 일치하도록 최소 1.6초 연속 포즈 데이터 이전의 프레임을 유지한다.
- YOLOv8로 가시 에이전트를 감지하고, 각 시나리오에서 객체 수가 가장 많은 단일 프레임을 선택하여 최종적으로 210개 프레임을 샘플링하며, 각 프레임은 6~32개의 유효 감지 객체를 포함한다.
- SAM2를 YOLOv8 경계 상자를 프롬프트로 사용하여 객체별 인스턴스 마스크를 생성하고, 픽셀 수준 정제를 통해 경계 간 누출을 방지한다.

### 반사실적 의미 집합
- 각 시나리오에 대해 Gemini imgen 인페인팅으로 객체별 제거를 수행하여 N개의 반사실적 이미지를 생성한다(N은 감지 객체 수). 또한 LaMa + FLUX Fill 1.0 오픈소스 절제 파이프라인을 유지한다.
- 핵심 설계: 색상 채우기, 가우시안 블러, 복사-붙여넣기 가림 대신 사실적인 생성적 인페인팅을 사용하여 분포 이동을 줄이고, 출력 변화가 렌더링 아티팩트가 아닌 객체 제거에 귀속될 수 있도록 한다.

### 귀속 지표
- 모델은 K개의 무작위 궤적 샘플 {p_k}을 생성하며, 각각은 T개의 미래 자차 중심점 시퀀스로 XY 평면에 투영되고, 평균 궤적으로 분포를 요약한다.
- 평균 편차 AD = (1/T) Σ_{t=1}^{T} ||p̄_var_t − p̄_orig_t||₂; 최종 편차 FD = ||p̄_var_T − p̄_orig_T||₂.
- 객체 수준 귀속 점수: AD 순위를 주요 점수로, FD를 동점 해소에 사용하여 반사실적 객체 귀속(COA) 순위를 형성한다.
- minADE/minFDE와의 차이: AD/FD는 전체 후보 집합을 사용하여 참조 예측 대비 분포 편차를 측정한다. minADE/minFDE는 실제 미래 대비 정확도를 측정하며 최적 후보 궤적을 선택한다. 저자들은 min-over-K 추정기를 사용하는 것이 부적절하다고 지적하는데, 이는 원래 분포에 우연히 근접한 변형을 보상하여 샘플링 노이즈와 인과 영향을 혼동하기 때문이다.

### 화이트박스 분석
- 각 제거 객체에 대해 경계 상자를 모델 패치 그리드에 투영하여 비전 인코더와 VLM의 해당 토큰 위치를 식별한다.
- 원본과 복원 이미지의 은닉 상태를 객체, 비전, 전역 토큰 위치에서 레이어별 코사인 차이로 계산한다.
- Logit Lens를 적용하여 객체 클래스 표현의 레이어 간 진화를 추적하고, 공간 KL 발산 맵을 계산하며, 궤적 핸드오프 토큰에서 객체 패치 위치로의 어텐션 가중치를 추출한다.

## 핵심 혁신

1. **객체 수준 반사실적 귀속 프로토콜**: 생성적 인페인팅과 궤적 편차 지표(AD/FD)를 최초로 결합하여, 실제 카메라 이미지에서 픽셀 수준이나 구조화된 상태 수준이 아닌 객체 수준의 인과 귀속을 구현한다. 사실적 복원 설계는 분포 이동을 크게 줄여 편차가 객체 제거 자체에 귀속될 수 있게 하며, 이는 기존 saliency 방법의 아티팩트 문제에 대한 직접적인 대응이다.

2. **화이트박스 전파 메커니즘 분류**: 은닉 상태 코사인 차이, Logit Lens, 어텐션 가중치를 통해 네 가지 내부 전파 변형을 식별한다——Coupled(약 33.0%), Transparent(약 33.1%), Decoupled(약 16.9%), Silent(약 16.9%). Silent 변형(큰 출력 편차지만 궤적 토큰에 시그니처 없음)은 기존 프로브가 해석할 수 없는 영향 경로를 드러내며, 이는 VLA 설명 가능성 도구 부재에 대한 직접적 증거다.

3. **min-over-K 추정기에 대한 비판적 대안**: minADE/minFDE를 귀속 지표로 사용하면 원래 분포에 우연히 근접한 변형을 보상하여 샘플링 노이즈와 인과 영향을 혼동한다는 점을 명확히 지적한다. AD/FD는 전체 후보 집합을 기반으로 분포 편차를 측정하며, 이 설계 선택은 방법론적으로 더 엄격하고 후속 VLA 귀속 연구를 위한 지표 표준을 설정한다.

## 실험 및 결과

실험은 Alpamayo 1 궤적 예측기를 기반으로, 210개의 nuScenes 전방 시나리오에서 총 3,062개의 반사실적 이미지 쌍을 사용한다.
**클래스별 편차(Table 3 핵심 수치)**:
| 클래스 | N | 평균 AD (m) | 최대 AD (m) | 평균 FD (m) |
|------|---|-------------|------------|-------------|
| 버스 | 47 | 0.663 | 3.931 | 1.889 |
| 소화전 | 17 | 0.540 | 2.037 | 1.454 |
| 트럭 | 183 | 0.505 | 3.548 | 1.419 |
| 신호등 | 531 | 0.482 | 4.534 | 1.399 |
| 보행자 | 604 | 0.458 | 5.276 | 1.318 |
| 자동차 | 1566 | 0.348 | 7.782 | 0.984 |
**순위 안정성(3개 시드)**: AD Top-3 정확 순위 유지 14.6%, top-3 내 유지 39.7%; FD는 각각 16.0%와 39.5%.
평균 순위 범위는 AD 4.691, FD 4.641.
**시나리오 수준 편차**: 최대 AD 객체의 z-score 평균 2.43, 중앙값 2.35; 148/210 시나리오(70.5%)가 z>2 임계값 초과, 48개 시나리오(22.9%)가 z>3 초과.
FD는 z>2에서 148, z>3에서 43.
**신호등 색상**: 531개 신호등 객체 중 119개(22.4%)가 명확한 색상 감지; 빨간불 상태 평균 AD 0.758 m vs 초록불 0.229 m, 평균 FD 2.241 m vs 0.672 m.
**화이트박스 결과**: 비전 인코더의 제거 객체 패치 위치 델타는 약 10⁻⁷ 수준이며 음수; LM에서 15번째 레이어부터 클래스별로 분화되어 버스는 35번째 레이어에서 약 0.06, 트럭은 약 0.02; 궤적 전문가 증폭 배수 평균 115–180×, 중앙값 47–106×; Silent 변형에서 δ_traj 약 0.0001이지만 비율은 1000× 초과.
(이 섹션에는 전체 텍스트에서 확인할 수 없는 숫자를 포함한 문장 2개가 더 있었으나, 규율에 따라 제거됨; 논문에 명시되지 않았거나 그림/표 이미지로 제공됨.)

## 경계 및 한계

평가는 단일 모델(Alpamayo 1)과 nuScenes 전방 카메라 분포에 국한되며, 다른 VLA 및 데이터셋에 대한 일반화는 검증되지 않았다. 화이트박스 분석은 VLA 아키텍처를 위해 설계된 설명 가능성 도구의 부재를 드러낸다——코사인 차이 곡선과 Logit Lens(둘 다 언어 모델 연구에서 차용)는 두 번의 순방향 전달 간 변화만 측정할 수 있을 뿐, 원인을 설명하거나 출력 차이에 인과적으로 책임이 있는 내부 계산을 식별할 수 없다. Silent 사분면(큰 출력 편차지만 궤적 토큰에 시그니처 없음)은 기존 프로브가 해석할 수 없는 영향 경로를 가리킨다. 논문은 하드웨어 플랫폼, 훈련 구성, 추론 빈도를 명시하지 않았다. 향후 작업으로는 다른 VLA 적용, 텍스트 출력 유사성 평가, 시간적 다중 프레임 반사실적 통합, 시나리오 수준 관계 표현에 적합한 설명 가능성 프로브 개발이 포함된다.

## 공학적 시사점

재현 시 세 가지를 먼저 확인해야 한다: 첫째, 인페인팅 파이프라인의 일관성——Gemini imgen과 LaMa + FLUX Fill 1.0의 분포 이동 차이는 AD/FD 절대값에 크게 영향을 미칠 수 있으므로, 소규모 샘플에서 두 파이프라인의 편차 분포를 먼저 비교해야 한다. 둘째, 시드 민감성——AD Top-3 정확 순위 유지가 14.6%에 불과하므로 단일 실행 순위는 신뢰할 수 없으며, 최소 3개 시드의 병합 순위가 필요하다. 셋째, minADE와 AD의 의미적 차이——49.3%의 객체가 음의 ΔminADE를 보이므로, 높은 귀속 객체가 실제 예측 정확도를 반드시 개선하지는 않으며, 다운스트림 팀은 COA 순위를 안전 중요도와 직접 동일시해서는 안 된다.

가장 빠지기 쉬운 함정은 마스크 면적과 편차의 양의 상관관계(Pearson r = +0.25)다: rank-1 객체는 평균 38,706픽셀, rank-5 이후는 5,000픽셀 미만으로, 큰 객체는 자연스럽게 더 높은 AD를 얻는다. 서로 다른 클래스의 중요성을 비교해야 한다면 마스크 면적을 통제하거나 면적 정규화 지표를 사용해야 한다. 신호등 색상은 강한 신호(빨간불 AD 0.758 m vs 초록불 0.229 m)지만, 22.4%의 객체만 명확한 색상이 감지되며 나머지는 해상도나 가림으로 상태를 구분하지 못할 수 있으므로 신중히 해석해야 한다. Silent 변형(약 16.9%)에서는 궤적 토큰에 시그니처가 없지만 출력 편차가 크므로, 다운스트림이 어텐션이나 토큰 수준 프로브에 의존하여 안전 모니터링을 수행한다면 이러한 영향 경로를 체계적으로 놓치게 된다.
