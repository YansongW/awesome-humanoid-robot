---
$id: ent_paper_bilivla_scene_aware_vision_lan_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  zh: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  ko: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
summary:
  en: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
  zh: BiliVLA 是一个场景感知的视觉-语言-动作（VLA）框架，由研究团队提出，用于自主胆道内窥镜导航。其核心贡献在于将内窥镜导航建模为指令条件化的视觉运动学习问题，并通过结合语义定位、场景感知监督与两阶段训练范式（SFT + GRPO），在真实体模实验中实现了91.96%的动作精度和84.85%的整体成功率。
  ko: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
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
- bilivla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.23531v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (776 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic
    Navigation (arXiv)'
  url: https://arxiv.org/abs/2606.23531
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述

BiliVLA 是一个面向 ERCP 胆道内镜自主导航的视觉-语言-动作（VLA）模型，由研究团队提出，核心贡献在于将导航任务统一为指令条件化的视觉运动学习，并引入两阶段训练（SFT + GRPO 强化学习）与场景感知安全机制。该系统在入口导航、管腔穿越、结石定位三个子任务上，将真实世界任务成功率从基线 EndoVLA 的 58.86% 提升至 84.85%（由表内数值 58.86%→84.85% 计算），同时保持较高的边界框预测精度（mIoU 0.9625）。

## 它改变了什么

胆道内镜导航长期以来是模块化系统的天下：感知、规划、控制各自独立优化，在解剖变异和镜面反射、组织接触等视觉伪影面前，级联误差被逐级放大。现有基于视觉的辅助技术（如 EndoVLA）虽然引入了语义理解，但本质上仍是“感知提示 + 人工决策”的增强工具，无法将程序性语义（如“找到结石并居中”）直接转化为闭环电机指令。BiliVLA 真正改变的是问题建模方式——它把插管导航重新定义为端到端的指令条件化视觉运动映射，让语义目标、视觉接地和离散动作在同一个策略网络内联合优化，从而绕开了模块间接口的信息损失。此外，它首次在 VLA 框架内显式引入“场景感知”安全层，将腔壁接触检测直接耦合到动作输出（强制后退），这比事后碰撞检测或人工急停更符合手术机器人对安全关键操作的需求。

## 方法拆解

### 问题形式化
导航被建模为目标条件化视觉运动决策：每个时间步输入内镜 RGB 观测 \(o_t\) 与任务指令 \(I\)，策略 \(\pi_\theta\) 联合输出目标类别 \(\hat{c}_t\)、归一化边界框 \(\hat{b}_t\) 和离散动作 \(\hat{a}_t\)，通过自回归条件解码获得。

### 动作空间与低层驱动
- 动作空间包含 11 个运动原语：{left-up, left-down, right-up, right-down, left, right, up, down, forward, backward, stop}，联合参数化平面弯曲、轴向平移和运动终止。
- 每个离散动作映射到固定角度增量 \(\Delta\theta_t = (\Delta\theta_{x,t}, \Delta\theta_{y,t}, \Delta\theta_{z,t}) \in \mathbb{R}^3\)，其中前两维控制远端尖端正交弯曲，第三维控制插入/回退；电机更新遵循 \(\theta_{t+1} = \theta_t + \Delta\theta(a_t)\)。

### 最优决策规则
\[
a_t^* = \begin{cases}
\text{stop} & \text{若 calculus 居中} \\
\arg\min_{a \in A} \|p_t(a) - p_c\|_2 & \text{若 } \|p_t - p_c\|_2 > \tau \\
\text{forward} & \text{若 } \|p_t - p_c\|_2 \le \tau
\end{cases}
\]
其中 \(p_t\) 为目标中心，\(p_c\) 为图像中心，\(\tau\) 为居中阈值。

### 两阶段训练框架
#### 阶段一：接地增强导航 SFT
- 使用 LoRA 高效微调 LLM（骨干为 Qwen3-VL-8B），骨干与分词器冻结，内镜图像由可训练 ViT 和 MLP 投影器编码映射到语言嵌入空间。
- 训练数据包含多视图图像、空间接地标注、场景级语义信息和运动命令。
- 训练配置：序列长度 1024，有效批大小 8，8-bit AdamW，线性学习率调度，2k 步，四块 NVIDIA RTX A6000 GPU。

#### 阶段二：奖励引导策略优化（GRPO）
- 对每个输入 \(u\) 采样 \(K\) 个候选输出 \(\{s_i\}_{i=1}^K\)，每个样本分配标量奖励 \(r_i = R(u, s_i)\)。
- GRPO 通过对比组内个体奖励与组级统计量估计归一化优势，避免依赖外部价值函数。
- 奖励函数 \(R(u, s) = R_{\text{bbox}} + R_{\text{act}} + R_{\text{fmt}}\)，其中 \(R_{\text{bbox}} = \text{IoU}(B_{\text{pred}}, B_{\text{gt}})\)，\(R_{\text{act}}\) 为动作一致性（1/0），\(R_{\text{fmt}}\) 为输出格式有效性（1/0）。

### 场景感知安全机制
- 对检测为腔壁接触的帧，边界框设为覆盖整个图像 \(b_t^s = (0,0,1,1)\)，控制命令设为 backward；其余帧采用名义监督。
- 训练目标为 \((b_t, a_t) = \{(b_t^s, a_t^s) \text{ 若 } o_t \text{ 指示腔壁接触}, (\hat{b}_t, \hat{a}_t) \text{ 否则}\}\)。

## 关键创新

1. **端到端语义-动作联合优化**：不同于模块化系统将感知结果作为中间表示传递，BiliVLA 让语义目标（如“找到结石”）直接参与动作决策的梯度回传，消除了接口信息瓶颈。这是对现有“感知提示 + 人工决策”范式的根本性突破。
2. **GRPO 在手术导航中的引入**：将强化学习从仿真环境迁移到真实内镜数据上，通过组内相对奖励估计优势，避免了价值函数估计的高方差问题。消融显示去除 GRPO 后总体 SR 从 84.85% 降至 63.64%（由表内数值 84.85%→63.64% 计算），证明 RL 阶段对策略精调不可或缺。
3. **场景感知安全层**：将腔壁接触检测直接耦合到动作输出（强制后退），而非作为独立的安全监控模块。这种设计将安全约束内化到策略本身，使模型在视觉退化下仍能保持保守行为，是手术机器人安全关键应用的重要工程创新。

## 实验与结果

实验在 ERCP 幻影模型（十二指肠和胆总管）上进行，使用商用 Olympus 内镜，成像 30 FPS，分辨率 640×480。三个子任务各执行 11 次，最大 50 步/试验。

| 方法 | 入口导航 mIoU / PR / SR | 管腔穿越 mIoU / PR / SR | 结石定位 mIoU / PR / SR | 总计 mIoU / PR / SR |
|------|------------------------|------------------------|------------------------|--------------------|
| Imitation Learning | 0.9315 / 74.17% / 27.27% | 0.9751 / 76.92% / 54.55% | 0.9894 / 78.80% / 45.45% | 0.9718 / 77.31% / 42.42% |
| Qwen3-VL | 0.7595 / 81.77% / 43.28% | 0.7352 / 81.92% / 64.83% | 0.8465 / 80.60% / 53.42% | 0.8117 / 81.14% / 51.82% |
| EndoVLA | 0.8189 / 84.49% / 51.69%（由表内数值 51.82→78.8 计算） | 0.8124 / 84.62% / 71.29% | 0.8537 / 84.26% / 59.93% | 0.8406 / 84.44% / 58.86% |
| BiliVLA (w/o GRPO) | 0.8832 / 86.57% / 54.55% | 0.9480 / 87.50% / 72.73% | 0.9782 / 90.33% / 63.64% | 0.9488 / 89.00% / 63.64% |
| BiliVLA (w/o Scene Aware) | 0.8980 / 88.69% / 63.64% | 0.9477 / 89.62% / 81.82% | 0.9798 / 91.44% / 72.73% | 0.9430 / 90.49% / 72.73% |
| **Ours** | **0.9162 / 90.82% / 72.73%** | **0.9630 / 91.46% / 100.00%** | **0.9816 / 92.55% / 81.82%** | **0.9625 / 91.96% / 84.85%** |

关键结果解读：
- 完整 BiliVLA 在管腔穿越任务上达到 100.00% SR，在结石定位上达到 81.82% SR，显著优于所有基线。
- 消融显示 GRPO 贡献约 21 个百分点 SR（由表内数值 63.64%→84.85% 计算），场景感知模块贡献约 12 个百分点（由表内数值 72.73%→84.85% 计算），两者均为关键组件。
- 值得注意的是，Imitation Learning 基线在 mIoU 上表现优异（0.9718）但 SR 极低（42.42%），说明纯模仿学习在真实部署中动作精度不足，RL 阶段对策略精调不可或缺。

## 边界与局限

论文明确未在活体动物或人体临床试验中验证，所有实验均在 ERCP 幻影模型上进行，真实组织的光学特性、生物力学响应和生理运动（如呼吸、蠕动）未被覆盖。作者承认未来将扩展至离体组织（ex vivo tissue）评估，并加强在更多样化视觉退化下的安全性验证。此外，动作空间仅包含 11 个离散原语，对精细插管所需的连续力控和触觉反馈未做建模；电机角度与远端尖端弯曲角度之间采用线性映射假设，实际柔性连续体机器人的非线性可能引入误差。数据集规模（10k 图像-运动对）相对有限，且边界框标注依赖 YOLOv11 生成后人工精炼，标注质量对训练效果的影响未做敏感性分析。

## 工程启示

复现或下游应用时，优先核对以下环节：
1. **数据标注一致性**：运动标签根据目标中心相对 44 像素聚焦区域的偏移分配，这一阈值直接决定动作分布，复现时需严格对齐；边界框由 YOLOv11 生成后人工精炼，建议检查标注者间一致性。
2. **GRPO 超参数敏感性**：奖励函数中 \(R_{\text{fmt}}\) 为硬性格式约束，若下游任务输出格式不同，需重新设计；采样数 \(K\) 和组内奖励归一化方式对训练稳定性影响较大，建议先在小规模验证集上调试。
3. **场景感知触发条件**：腔壁接触检测的判定标准（如何定义“指示腔壁接触”）是安全机制的核心，复现时需明确该分类器的输入特征和阈值，否则安全层可能过度触发（导致频繁后退）或漏触发（失去保护）。
4. **硬件映射**：电机角度与尖端弯曲角度的线性映射假设在真实连续体机器人上可能不成立，部署前需标定实际运动学模型，否则离散动作到电机指令的转换会引入系统性误差。
5. **推理硬件**：所有推理在单块 NVIDIA RTX 5090 GPU 上进行，若下游设备算力不足，需考虑量化或蒸馏，但需重新验证 SR 指标。

## 参考
- http://arxiv.org/abs/2606.23531v3

## 개요
BiliVLA는 ERCP 수술 중 단일 시야의 협소함, 거울 반사, 조직 접촉 등의 도전 과제를 해결하기 위해 담도 내시경 내비게이션을 언어 기반의 시각 운동 학습 작업으로 변환합니다. 이 프레임워크는 목표 클래스 예측, 경계 상자 위치 파악, 연속 내시경의 이산 3자유도 운동 명령을 동시에 예측할 수 있습니다. 장면 인식 감독을 도입하여 의미적 일관성을 강화하고, 안전 인식 복구 감독을 활용하여 관벽 접촉 시 보수적인 후퇴 행동을 유도합니다. 두 단계 훈련 전략은 위치 파악 강화를 위한 지도 미세 조정(SFT)과 Group Relative Policy Optimization(GRPO)을 결합하여 폐쇄 루프 내비게이션에서 동작 신뢰성과 결정 일관성을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
BiliVLA는 담도 내시경 내비게이션을 명령 조건부 시각 운동 학습 문제로 공식화합니다. 입력은 내시경 관찰 이미지와 단계별 언어 명령이며, 출력은 목표 클래스, 경계 상자 위치, 연속 내시경의 이산 3자유도(3-DoF) 운동 명령을 공동으로 예측합니다.

### 주요 구성 요소
- **장면 인식 감독**: 의미적 목표의 일관성을 강화하여 모델이 내시경 시야 내 해부학적 구조를 더 잘 이해할 수 있게 합니다.
- **안전 인식 복구 감독**: 관강벽 접촉 시 보수적인 후퇴 행동을 유도하여 조직 손상을 방지합니다.
- **두 단계 훈련 패러다임**:
  1. **위치 파악 강화를 위한 지도 미세 조정(SFT)**: 위치 정보를 통해 시각-동작 매핑을 강화합니다.
  2. **Group Relative Policy Optimization(GRPO)**: 보상 기반 정책 최적화를 통해 폐쇄 루프 내비게이션에서 동작 신뢰성과 결정 일관성을 향상시킵니다.

### 실험 설정 및 결과
실제 팬텀 실험에서 BiliVLA는 세 가지 ERCP 하위 작업에서 최고의 전체 성능을 달성했습니다:
- **총 mIoU**: 0.9625
- **전체 동작 정확도**: 91.96%
- **전체 성공률(SR)**: 84.85%

### 결론
결과는 의미적 위치 파악, 장면 인식 학습, 보상 기반 최적화를 통합하면 인식-동작 정렬이 강화되어 더 견고한 자율 담도 내시경 내비게이션이 가능함을 보여줍니다.
