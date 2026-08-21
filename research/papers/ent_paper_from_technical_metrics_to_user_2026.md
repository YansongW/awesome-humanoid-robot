---
$id: ent_paper_from_technical_metrics_to_user_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection
    and Grasping'
  zh: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection
    and Grasping'
  ko: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection
    and Grasping'
summary:
  en: 'arXiv:2607.00530v1 Announce Type: new Abstract: Improvements in the technical performance of human--robot interaction
    (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This
    paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system
    to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and
    measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for
    open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion
    execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen
    3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both
    systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived
    speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants
    (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs
    were rated significantly higher for the improved configuration after Holm correction, with large to very large effect
    sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct
    interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing
    robotic manipulation pipelines.'
  zh: 本文研究多模态人机交互系统中技术性能提升是否可被用户感知。作者通过24人用户实验，对比基线系统（Whisper+Florence-2+LLaMA 3.1）与改进系统（Grounding DINO+SAM+Qwen 3.5 9B）在桌面抓取任务中的表现。结果显示70.83%用户偏好改进系统，且感知速度、可靠性、流畅性评分均显著提升（p<0.001），证实15%的任务成功率提升可被用户察觉。
  ko: 'arXiv:2607.00530v1 Announce Type: new Abstract: Improvements in the technical performance of human--robot interaction
    (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This
    paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system
    to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and
    measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for
    open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion
    execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen
    3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both
    systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived
    speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants
    (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs
    were rated significantly higher for the improved configuration after Holm correction, with large to very large effect
    sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct
    interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing
    robotic manipulation pipelines.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- from_technical_metrics_to_user
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00530v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (870 chars, DeepSeek). [2026-08-21] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object
    Detection and Grasping (arXiv)'
  url: https://arxiv.org/abs/2607.00530
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述

本文通过一项受控用户研究（24名参与者），系统验证了多模态人机交互系统在技术指标提升（端到端成功率从75%到90%）后，用户感知层面是否出现一致且可测量的差异。研究采用被试内设计，对比基线系统与改进系统在感知速度、可靠性和能力流畅性三个构念上的主观评分，发现改进系统在全部构念上均显著优于基线，且70.83%的参与者明确偏好改进系统。核心贡献在于将评估范式从模块级技术基准转向用户感知验证，并提供了技术指标与主观体验对齐的经验证据。

## 它改变了什么

这项工作的真正价值不在于提出新的算法或架构，而在于它挑战了HRI领域一个长期被默认的假设：技术指标的提升会自动转化为用户可感知的体验改善。作者敏锐地指出，当任务短、场景受限、两种条件下的机器人行为都已相对稳定时，模块级基准测试的改进（如成功率提升15个百分点）可能在实际交互中被用户完全忽略。这种“指标-感知”脱节是HRI系统从实验室走向部署时最隐蔽的风险——工程师看到的是数字变好，用户感受到的却可能是“差不多”甚至“更差”。

它改变了评估的参照系。传统消融研究或基准比较只回答“哪个模块更强”，而本文追问“更强的模块是否让用户觉得更好”。这种转向意味着，未来的系统改进验证不能止步于技术指标，必须纳入用户层面的感知评估作为常规步骤。作者用实证数据表明，主观评分与客观性能确实可以对齐，但前提是评估设计足够精细——包括被试内设计、中性系统命名、随机化顺序以及多构念问卷。这为HRI社区提供了一套可复用的方法论模板，而非仅仅是一个结论。

## 方法拆解

### 系统架构与模块替换
两种配置共享同一多模态管线：语音命令捕获→语音转文本→结构化动作提取→视觉场景定位→机器人控制器执行。基线与改进系统的差异集中在两个模块：
- **动作提取**：基线用LLaMA 3.1 7B，改进用Qwen 3.5 9B（因消融研究中语言阶段结果最强）。
- **视觉定位**：基线用Florence-2（开放词汇模式），改进用Grounding DINO + SAM（测试的感知管线中最强）。
- **运动控制**：两者均保留区间Type-2模糊逻辑控制器（IT2FLS），因消融研究确认其仍是最佳控制器选择。

### 实验设计
- **被试内设计**：每位参与者对两个系统各完成2次实时抓取任务运行（共4次），系统呈现顺序随机化以减少学习、疲劳和期望效应。
- **中性命名**：系统在会话中标记为“系统A”和“系统B”，参与者不知晓对应关系；最终偏好问题仅在两个系统均体验后收集。
- **问卷构念**：感知速度、感知可靠性、整体能力与流畅性，每个构念含2个陈述，采用7点Likert量表（1=强烈不同意，7=强烈同意）。

### 统计分析
- 构念得分为两个条目得分的平均值；配对差异分数用Shapiro–Wilk检验评估正态性（所有W > 0.93，p > 0.05）。
- 默认推断检验为Wilcoxon符号秩检验；因近似正态，报告配对双尾t检验作为敏感性分析。
- 效应量：配对t检验用Cohen's d_z，非参数比较用秩双列相关或标准化Wilcoxon效应量。
- 最终偏好问题用精确二项检验（零假设比例为0.5），多构念比较应用Holm校正，显著性阈值α = 0.05。

### 硬件与复现条件
- 机器人：Dobot Magician机械臂（吸盘式末端执行器）；视觉：Intel RealSense D435i RGB-D相机；音频：Samsung Buds2无线耳机。
- 计算：Intel Core i9-14900HX + NVIDIA RTX 4070 GPU，所有推理和控制本地运行。
- 工作空间、相机视角、机器人基座位姿、桌面几何、光照和标定流程在两种配置间保持不变；使用印刷水果图片而非实体水果以保证一致性。

## 关键创新

1. **将用户感知作为技术改进的验证终点**：这是对HRI评估范式的实质性补充。以往消融研究止步于技术指标，本文首次系统性地证明，技术改进（成功率75%→90%）在用户感知层面产生了显著且一致的效果——三个构念的效应量（d_z = 1.54至2.03）均达到“极大”水平，远超常规心理学研究的阈值。这种“指标-感知”对齐的实证证据，为后续研究提供了方法论参照。

2. **精细化的实验控制设计**：被试内设计、中性系统命名、随机化顺序、多构念问卷以及Holm校正的组合，有效隔离了学习效应、期望效应和多重比较风险。特别是最终偏好问题仅在两个系统均体验后收集，避免了早期判断对后续评估的污染。这种设计严谨性在HRI用户研究中并不常见，其价值在于让结论具有可辩护的统计效力。

3. **识别视觉接地为端到端性能的主要决定因素**：消融研究明确指向视觉定位组件（Grounding DINO + SAM）是成功率提升的关键，而语言模型升级（Qwen 3.5 9B）和控制器保留（IT2FLS）的贡献相对次要。这一发现为系统优化提供了明确的优先级指引——在资源受限时，应优先投入视觉感知而非语言理解。

## 实验与结果

### 关键结果汇总

| 指标 | 基线 | 改进 | 差异/统计量 |
|------|------|------|-------------|
| 端到端成功率 | 75% | 90% | +15个百分点（技术指标） |
| 感知速度（H1） | M=4.61, SD=0.55 | M=5.69, SD=0.61 | Δ=1.08, 95% CI [0.83, 1.33], d_z=1.85, t(23)=9.09, p_adj<0.001 |
| 感知可靠性（H2） | M=3.95, SD=0.63 | M=4.89, SD=0.59 | Δ=0.94, 95% CI [0.68, 1.20], d_z=1.54, t(23)=7.54, p_adj<0.001 |
| 感知能力与流畅性（H3） | M=3.76, SD=0.59 | M=5.01, SD=0.64 | Δ=1.25, 95% CI [0.99, 1.51], d_z=2.03, t(23)=9.93, p_adj<0.001 |
| 最终偏好 | — | 17/24（70.83%） | 精确二项检验p=0.043, 95% CI [0.49, 0.87], Cohen's h=0.43 |

### 结果解读
- 三个构念的改进均达到统计显著且效应量极大（d_z > 1.5（由表内数值 0.49→0.5 计算）），说明技术改进在用户主观体验上产生了“压倒性”的可感知差异。
- 偏好检验p=0.043恰好低于0.05阈值，但效应量h=0.43为中等，且95%置信区间下界为0.49（接近0.5的零假设），提示偏好差异虽真实存在但强度有限。
- 改进系统的可靠性均分4.89仍接近量表中点（4.0），基线均分3.95低于中点，说明用户平均认为原系统“略不可靠”，改进系统也远未达到“完全可信赖”水平。

## 边界与局限

- **样本量与生态效度**：24名参与者规模较小，且研究在受控实验室进行，使用印刷水果图片、受限物体词汇和简短分条件协议。结论应被解释为特定任务和设置内可感知性的证据，而非对更丰富或更自然环境中用户响应的普遍描述。
- **未覆盖的评估维度**：未采用信任、感知安全、认知工作负载、长期接受度等更广泛的评估框架；未进行纵向设计以检验感知优势在新奇效应消退后是否保持。
- **任务与场景局限**：未将任务扩展到更长会话、更复杂指令集（包括多物体操作和动态场景变化）；未用物理多样化的真实物体替换印刷水果图像，视觉接地组件的鲁棒性未在更严苛条件下测试。
- **偏好效应量中等**：尽管统计显著，但偏好差异的效应量（h=0.43）和置信区间宽度表明，感知差异主要源于失败率降低，在每次单独试验中可能并不显著。
- **绝对可靠性不足**：改进系统可靠性均分4.89仍接近中点，且最佳配置仍偶尔出现任务失败，说明控制器虽更稳健但未完全消除执行错误，未达到非受控真实环境所需的无缝性。

## 工程启示

- **复现时先核对实验控制**：确保两个系统共享完全相同的硬件、工作空间、光照和标定流程，使用印刷刺激物以保证物体一致性。系统命名必须中性（如“系统A/B”），顺序随机化，且最终偏好问题仅在两个系统均体验后收集——任何一步缺失都可能污染结果。
- **统计方法选择有讲究**：先做Shapiro–Wilk检验判断正态性（本文所有W > 0.93，p > 0.05），再决定用t检验还是Wilcoxon。多构念比较务必应用Holm校正，否则多重比较风险会虚增显著性。效应量报告（d_z）比单纯p值更有信息量。
- **最容易踩坑的是“指标-感知”脱节**：技术成功率提升15个百分点（75%→90%）在用户感知上产生了极大效应（d_z > 1.5），但这不代表所有技术改进都能如此。如果任务更长、场景更复杂或基线行为更不稳定，用户可能完全感知不到差异。建议在消融研究后增加用户感知验证作为常规步骤，而非默认技术指标即用户体验。
- **视觉接地是优先优化方向**：消融研究明确指向视觉定位组件是端到端性能的主要决定因素。若资源有限，优先升级视觉感知（如Grounding DINO + SAM）比升级语言模型（Qwen 3.5 9B）更有效。但注意，改进系统的可靠性均分仍接近中点，说明视觉接地虽提升明显，尚未达到部署级鲁棒性。

## 参考
- http://arxiv.org/abs/2607.00530v1

## 개요
본 연구는 인간-로봇 상호작용 시스템의 기술적 지표 향상과 사용자 실제 경험 사이의 간극을 다룬다. 기준 시스템은 Whisper 음성 인식, Florence-2 개방형 어휘 검출, LLaMA 3.1 동작 추출 및 구간 2형 퍼지 논리 제어기를 사용한다. 개선 시스템은 지각 모듈을 Grounding DINO+SAM으로, 언어 모듈을 Qwen 3.5 9B로 교체한다. 24명의 피험자가 테이블 위 물체 잡기 과제에서 두 구성을 순차적으로 경험하며, 7점 리커트 척도로 지각 속도, 신뢰성, 전반적 능력 및 유창성을 평가한다. 통계 결과, 개선 시스템은 세 가지 지각 차원 모두에서 유의미하게 높은 점수를 얻었으며(효과 크기 큼~매우 큼), 선호 비율은 70.83%에 달했다(정확 이항 검정 p=0.043).

## 핵심 내용
### 연구 동기
- 기술적 성능 향상(예: 작업 성공률 75%에서 90%로 상승)이 반드시 사용자가 인지 가능한 상호작용 경험 차이로 이어지지는 않음
- 벤치마크 개선의 실제 인지 가능성을 사용자 연구를 통해 검증할 필요가 있음

### 시스템 아키텍처
- **기준 시스템**: Whisper(음성 인식) + Florence-2(개방형 어휘 검출) + LLaMA 3.1(동작 추출) + 구간 2형 퍼지 논리 제어기(운동 실행)
- **개선 시스템**: Grounding DINO + SAM(지각 모듈) + Qwen 3.5 9B(언어 모듈), 동일한 제어기 유지

### 실험 설계
- **피험자**: 24명의 참가자(피험자 내 설계)
- **과제**: 테이블 위 물체 잡기
- **평가 지표**: 7점 리커트 척도(1=매우 동의하지 않음, 7=매우 동의함), 지각 속도, 신뢰성, 전반적 능력 및 유창성 측정
- **통계 방법**: 정확 이항 검정(선호 데이터), Holm 보정(지각 점수)

### 주요 결과
- **선호 데이터**: 17/24(70.83%)가 개선 시스템을 선호함(p=0.043, 효과 크기 h=0.43)
- **지각 점수**: 개선 시스템은 세 가지 차원 모두에서 유의미하게 높음(p<0.001), 효과 크기 큼~매우 큼
- **결론**: 15%의 작업 성공률 향상은 사용자가 안정적으로 인지할 수 있으며, 기술 개선의 실제 가치를 검증함

### 연구 의의
- 로봇 조작 파이프라인 평가에서 벤치마크 테스트와 사용자 중심 증거를 결합해야 함을 강조
- 다중 모달 HRI 시스템의 사용자 지각 연구를 위한 정량적 방법론 참조를 제공함
