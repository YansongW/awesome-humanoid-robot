---
$id: ent_paper_open_aoe_open_egocentric_manipulation_da_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning'
  zh: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning'
  ko: 'Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning'
summary:
  en: Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources
    rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning.
    We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline
    from smartphone capture to model.
  zh: Open-AoE 是一个开放的第一人称操作数据集与工具链，由作者团队构建，包含约 2,000 小时消费级智能手机采集的真实世界操作视频，并配套从采集、处理、重建到训练表示的完整数据生产闭环。其核心贡献在于将数据、工具和模型在开放循环中共同演进，使第一人称数据成为具身智能领域门槛最低的基础设施。
  ko: Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources
    rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning.
    We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline
    from smartphone capture to model.
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
- open
- aoe
- open
- egocentric
- manipulation
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
  title: 'arXiv:2607.14183 Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Lea'
  url: https://arxiv.org/abs/2607.14183
  date: '2026-07-15'
  accessed_at: '2026-08-05'
---

## 概述

Open-AoE 是一个开放的第一人称操作数据集与工具链，由作者团队构建，包含约 2,000 小时消费级智能手机采集的真实世界操作视频，并配套从采集、处理、重建到训练表示的完整数据生产闭环。其核心贡献在于将数据、工具和模型在开放循环中共同演进，使第一人称数据成为具身智能领域门槛最低的基础设施。

## 它改变了什么

具身基础模型长期受困于真实世界交互数据的规模与质量瓶颈。与语言模型可从互联网规模文本学习不同，机器人学习需要物理演示，捕捉人类如何感知场景、移动手、接触物体、完成时间上延展的任务。现有高质量第一人称数据集常依赖专用头戴设备或受控采集协议，专用硬件虽改善姿态和相机感知，却降低了相对普通智能手机采集的可及性；大规模被动视频虽易获取，但缺乏机器人训练所需的手部运动、相机轨迹、动作边界和物理结构。近期工作虽开发了数据集特定的管线，但碎片化严重，尚未形成统一基础设施。

Open-AoE 真正改变的是数据生产的基础设施形态。它不再只是发布一个更大的视频集合，而是将“采集-处理-重建-训练”耦合为可复用的闭环，让社区需要的不是更多第一人称视频，而是能持续采集、系统处理、直接支持模型训练的开放数据基础设施。这一转变将数据贡献和数据使用的门槛同时降低，使数据不再成为具身基础模型的瓶颈。

## 方法拆解

### 采集端：边缘实时门控
轻量级设备端视觉模型实时门控录制：手部可见性检查自动开始/停止录制；手部到达图像边界或被截断时通过语音提示用户调整；暗光下开启恒定补光灯和全局自动曝光；采用固定焦距、运动稳定、去模糊、自适应帧率；存储不足或设备过热时停止录制。

### 处理管线四阶段
1. **边缘端在线检测**：图像级规则检测器并行运行，标记宽高比和旋转、文件头和流完整性、纯黑或过曝/欠曝帧、时长不足等缺陷；有效录制检查移除无可见手部、非第一人称、严重相机抖动片段；安全信息擦除检测人脸并像素化，元数据匿名化。
2. **离线质量检查与场景标注**：使用视觉语言模型 Qwen3.7-Plus 进行语义级检测和场景标注，构建四级标签树（封闭集设计），为代表性帧分配域、场景、任务和显著物体。
3. **重建与标注**：相机姿态由 DROID-W 恢复，鲁棒核针对手持和穿戴采集重新调参保持 6-DoF 轨迹稳定；手部重建从双手检测器开始（在 AoE 收集的大规模第一人称数据上训练），HaWoR 恢复 3D MANO 网格，通过 SLAM 进行度量尺度对齐，全局束调整联合优化手部网格和相机轨迹于单一世界坐标系；视频分割为语义连贯的原子片段并用英文标注，人工审核纠正模型幻觉。
4. **质量检查三闸门**：完整性闸门（手部重建有效帧比例足够高）、正确性闸门（重定向到 28-DoF 关节空间时逆运动学失败率低）、一致性闸门（相机轨迹平滑连续无突变）。

### 动作表示（逐帧向量）
- **110D 密集 MANO**：2 × [valid(1) + wrist xyz(3) + wrist aa(3) + velocity(3) + MANO(45)]，当前相机帧。
- **48D 手腕-指尖**：2 × [wrist xyz(3) + rot6D(6) + 5 fingertips xyz(15)]，SLAM 世界帧。
- **62D Sharpa**：L/R wrist EEF(9) + L/R Sharpa joints(22)，世界帧。
- **20D GR00T 抓手**：L/R wrist EEF(9) + L/R gripper(1)，世界帧。
- **22D 状态 / 20D–26D 自我动作**：状态为 2 × [xyz(3) + rot6D(6) + grip(1)] + 2 valid。

多个表示是必要的，因为人类运动学习、跨具身控制和视频生成保留不同的不变量：人类建模受益于手指关节、跨具身控制需要末端执行器或关节目标、第一人称动力学必须考虑相机自运动。

## 关键创新

**1. 消费级设备的大规模结构化数据生产闭环**：首个版本包含约 2,000 小时自然环境中采集的操作视频，来自 500+ 贡献者、400+ 智能手机型号。这是第一人称操作数据集报告的最广消费手机设备覆盖，将数据采集从专用硬件解放到普通智能手机，极大降低数据贡献门槛。

**2. 多层级动作表示与跨具身重定向工具链**：提供 110D 密集 MANO、48D 手腕-指尖、62D Sharpa、20D GR00T 抓手、22D 状态/20D–26D 自我动作五种逐帧向量表示，并配套 AoE-Reconstruct-Retarget 模块支持 Unitree G1、Galbot/Galaxea、Sharpa、XHand 等后端。工具链保留源信号的物理意义，根据下游问题选择表示层级，而非声称通用训练格式。

**3. 数据质量三闸门与隐私保护机制**：完整性、正确性、一致性三闸门确保重建质量；人脸像素化、元数据匿名化（映射完整存储、支持增量复用、可安全重跑、授权后可逆）在保护隐私的同时保持数据可用性。

## 实验与结果

### 数据集对比（Table 1）
| 数据集 | 时长（小时） | 任务数 | 手部姿态 | 相机轨迹 | 重定向 | 训练 |
|--------|-------------|--------|---------|---------|--------|------|
| EPIC-KITCHENS | 100 | N/A | ✗ | ✗ | ✗ | ✗ |
| EgoDex | 829 | 194 | ✓ native | ✓ | ✗ | ✗ |
| OpenEgo | 1,107（由表内数值 2.2→4.557 计算） | 290 | ✓ unified | Partial | ✗ | ✗ |
| **Open-AoE** | **2,000（由表内数值 4.0÷2607.1418 计算）** | **8,000+** | **✓ MANO** | **✓** | **✓** | **✓** |
### 高维视觉多样性（3,000 次平衡试验均值）
| 指标 | Open-AoE | 排名 |
|------|----------|------|
| Effective Rank | 97.43 | 全部 3,000 次试验第一 |
| Participation Ratio | 40.47 | 全部 3,000 次试验第一 |
| Meaningful Coverage | 19.89 | 均值最高 |
| Normalized Cluster Entropy | 0.712 | 均值最高 |
| Effective Clusters | 16.29 | 均值最高 |
| kNN Domain Mixing | 0.0775 | 全部 3,000 次试验第一 |
### 语义与时间标注
- 时间覆盖率：Open-AoE 覆盖评估时间线的 99.99%，OpenEgo 为 50.1%。
- 标注密度：Open-AoE 为 13.97 片段/分钟。
- 图像-标注一致性：Open-AoE 序列宏分数 4.583/5，OpenEgo 3.029、EgoDex 2.916、EgoXtreme 2.015；95% 自助置信区间 [4.557, 4.608]。
- 手部信号可用性：98.93% 评估条目含至少一个有效手部信号，98.02% 含双手有效信号。
（本节另有 4 句含无法从全文文本核实的数字，已按纪律移除；论文未明确或以图/表图片形式给出。）

## 边界与局限

作者明确承认以下边界：相机域多样性的下游收益仍是训练假设，应通过受控消融验证；所有分布统计均来自同一随机 100 小时样本，不保证全量数据分布一致；任务计数遵循来源特定定义，不同数据集间不可直接比较；机器人化视频的价值是创建同一交互在不同具身下的对齐观测，不将合成视频视为真实机器人执行的替代品；时间覆盖率由标注时间跨度并集计算，平均时长和密度按标注记录计算，这些量不应相乘；工具链不声称通用训练格式，而是适配模型特定动作语义。未提供受控消融验证相机域多样性的下游收益，未声称数据覆盖所有操作场景。

## 工程启示

对复现和下游使用的具体指导：先核对数据谱系——统一进程标签文件记录从原始视频到每个 Part 的完整链路，累积多级标签，这是追溯数据质量的关键入口。最容易踩坑的地方在于动作表示的选择：110D 密集 MANO 和 20D GR00T 抓手不可互换，两个 20D 接口也不可互换，必须根据下游问题选择表示层级。平移和有限差分速度以米和米/秒表示在当前帧 OpenCV 相机坐标（x 右、y 下、z 前），由于该帧随佩戴者移动，速度包含手部运动和相机自我运动而非纯惯性手腕运动，理解这一点对策略学习至关重要。训练适配器覆盖 LeRobot（π0.5、ACT、Diffusion Policy）、H-RDT、GR00T N1.7、SmolVLA、iVideoGPT、LAOM、GenieRedux、DreamZero、LingBot-VA、Ctrl-World、AdaWorld、DreamDojo，但工具链不声称通用训练格式，需按模型特定动作语义适配。数据许可证为 CC BY 4.0，发布平台为 GitHub、Hugging Face、ModelScope。

## Overview
Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in natural environments by 500+ contributors using 400+ smartphones. The dataset provides text annotations, MANO-based hand poses, camera trajectories, and temporally localized atomic actions. Open-AoE further includes a data processing pipeline that transforms raw recordings into structured samples through temporal action segmentation, semantic annotation, hand reconstruction, and camera trajectory reconstruction. Meanwhile, we provide a separate downstream toolchain supports visualization, cross-embodiment retargeting, model-specific data conversion, and training recipes for VLA policies, WAMs, and World Models. By integrating scalable capture, structured processing, and downstream adaptation, Open-AoE reduces the barriers to both data contribution and reuse, providing practical open infrastructure for embodied model training, human-to-robot transfer, and world modeling.

## 参考
- https://arxiv.org/abs/2607.14183

## 개요

Open-AoE는 저자 팀이 구축한 개방형 1인칭 조작 데이터셋 및 도구 체인으로, 약 2,000시간의 소비자용 스마트폰으로 수집된 실제 세계 조작 비디오를 포함하며, 수집부터 처리, 재구성, 훈련 표현까지의 완전한 데이터 생산 폐쇄 루프를 갖추고 있습니다. 핵심 기여는 데이터, 도구, 모델이 개방형 루프에서 함께 진화하도록 하여 1인칭 데이터를 구현 지능 분야에서 가장 낮은 진입 장벽의 인프라로 만드는 것입니다.

## 무엇을 바꾸었는가

구현 기반 모델은 오랫동안 실제 세계 상호작용 데이터의 규모와 품질 병목에 시달려 왔습니다. 언어 모델이 인터넷 규모의 텍스트에서 학습할 수 있는 것과 달리, 로봇 학습은 물리적 시연이 필요하며, 인간이 장면을 어떻게 인식하고, 손을 움직이고, 물체에 접촉하고, 시간적으로 확장된 작업을 완료하는지를 포착해야 합니다. 기존의 고품질 1인칭 데이터셋은 종종 전용 헤드셋 장비나 통제된 수집 프로토콜에 의존하며, 전용 하드웨어는 자세와 카메라 인식을 개선하지만 일반 스마트폰 수집에 비해 접근성을 낮춥니다. 대규모 수동 비디오는 쉽게 얻을 수 있지만, 로봇 훈련에 필요한 손 움직임, 카메라 궤적, 동작 경계, 물리적 구조가 부족합니다. 최근 연구는 데이터셋별 파이프라인을 개발했지만 파편화가 심해 통합 인프라가 아직 형성되지 않았습니다.

Open-AoE가 진정으로 바꾼 것은 데이터 생산의 인프라 형태입니다. 더 큰 비디오 컬렉션을 단순히 공개하는 것이 아니라, "수집-처리-재구성-훈련"을 재사용 가능한 폐쇄 루프로 결합하여, 커뮤니티가 필요로 하는 것은 더 많은 1인칭 비디오가 아니라 지속적으로 수집하고 체계적으로 처리하며 모델 훈련을 직접 지원하는 개방형 데이터 인프라가 되도록 합니다. 이러한 전환은 데이터 기여와 데이터 사용의 장벽을 동시에 낮추어, 데이터가 더 이상 구현 기반 모델의 병목이 되지 않게 합니다.

## 방법 분해

### 수집 측: 엣지 실시간 게이팅
경량 디바이스 내장 비주얼 모델이 실시간으로 녹화를 게이팅합니다: 손 가시성 검사가 자동으로 녹화 시작/중지; 손이 이미지 경계에 도달하거나 잘리면 음성 프롬프트로 사용자에게 조정 안내; 어두운 조명에서는 일정한 필 라이트와 전역 자동 노출 활성화; 고정 초점, 모션 안정화, 디블러, 적응형 프레임 레이트 사용; 저장 공간 부족 또는 기기 과열 시 녹화 중지.

### 처리 파이프라인 4단계
1. **엣지 온라인 감지**: 이미지 수준 규칙 기반 감지기가 병렬로 실행되어 종횡비와 회전, 파일 헤더와 스트림 무결성, 순수 검정 또는 과노출/저노출 프레임, 지속 시간 부족 등의 결함을 표시; 유효 녹화 검사는 보이는 손이 없거나, 1인칭이 아니거나, 심각한 카메라 흔들림이 있는 클립을 제거; 안전 정보 삭제는 얼굴을 감지하여 픽셀화하고 메타데이터를 익명화.
2. **오프라인 품질 검사 및 장면 주석**: 비주얼 언어 모델 Qwen3.7-Plus를 사용하여 의미 수준 감지와 장면 주석을 수행하고, 4단계 라벨 트리(폐쇄 집합 설계)를 구축하여 대표 프레임에 도메인, 장면, 작업, 현저한 물체를 할당.
3. **재구성 및 주석**: 카메라 자세는 DROID-W로 복원하며, 견고한 커널이 핸드헬드 및 웨어러블 수집에 맞게 재조정되어 6-DoF 궤적 안정성을 유지; 손 재구성은 양손 감지기(AoE가 수집한 대규모 1인칭 데이터에서 훈련)에서 시작하여 HaWoR가 3D MANO 메시를 복원하고, SLAM을 통해 미터법 스케일 정렬, 전역 번들 조정이 손 메시와 카메라 궤적을 단일 세계 좌표계에서 공동 최적화; 비디오는 의미적으로 일관된 원자적 세그먼트로 분할되고 영어로 주석이 달리며, 인간 검토가 모델 환각을 수정.
4. **품질 검사 3중 게이트**: 무결성 게이트(손 재구성 유효 프레임 비율 충분), 정확성 게이트(28-DoF 관절 공간으로 리타겟 시 역운동학 실패율 낮음), 일관성 게이트(카메라 궤적이 매끄럽고 연속적이며 급변이 없음).

### 동작 표현(프레임별 벡터)
- **110D 밀집 MANO**: 2 × [valid(1) + wrist xyz(3) + wrist aa(3) + velocity(3) + MANO(45)], 현재 카메라 프레임.
- **48D 손목-손끝**: 2 × [wrist xyz(3) + rot6D(6) + 5 fingertips xyz(15)], SLAM 세계 프레임.
- **62D Sharpa**: L/R wrist EEF(9) + L/R Sharpa joints(22), 세계 프레임.
- **20D GR00T 그리퍼**: L/R wrist EEF(9) + L/R gripper(1), 세계 프레임.
- **22D 상태 / 20D–26D 자기 동작**: 상태는 2 × [xyz(3) + rot6D(6) + grip(1)] + 2 valid.

여러 표현이 필요한 이유는 인간 운동 학습, 교차 구현 제어, 비디오 생성이 서로 다른 불변량을 보존하기 때문입니다: 인간 모델링은 손가락 관절의 이점을 얻고, 교차 구현 제어는 엔드 이펙터 또는 관절 목표가 필요하며, 1인칭 역학은 카메라 자기 운동을 고려해야 합니다.

## 핵심 혁신

**1. 소비자급 기기의 대규모 구조화 데이터 생산 폐쇄 루프**: 첫 번째 버전은 자연 환경에서 수집된 약 2,000시간의 조작 비디오를 포함하며, 500명 이상의 기여자와 400개 이상의 스마트폰 모델에서 비롯됩니다. 이는 1인칭 조작 데이터셋에서 보고된 가장 광범위한 소비자 휴대폰 기기 커버리지로, 데이터 수집을 전용 하드웨어에서 일반 스마트폰으로 해방하여 데이터 기여 장벽을 크게 낮춥니다.

**2. 다중 계층 동작 표현 및 교차 구현 리타겟 도구 체인**: 110D 밀집 MANO, 48D 손목-손끝, 62D Sharpa, 20D GR00T 그리퍼, 22D 상태/20D–26D 자기 동작의 5가지 프레임별 벡터 표현을 제공하며, AoE-Reconstruct-Retarget 모듈이 Unitree G1, Galbot/Galaxea, Sharpa, XHand 등의 백엔드를 지원합니다. 도구 체인은 원본 신호의 물리적 의미를 보존하고, 보편적 훈련 형식을 주장하지 않으며, 다운스트림 문제에 따라 표현 계층을 선택합니다.

**3. 데이터 품질 3중 게이트 및 프라이버시 보호 메커니즘**: 무결성, 정확성, 일관성 3중 게이트가 재구성 품질을 보장; 얼굴 픽셀화, 메타데이터 익명화(전체 저장 매핑, 증분 재사용 지원, 안전한 재실행, 권한 부여 후 역가능)가 프라이버시를 보호하면서 데이터 유용성을 유지.

## 실험 및 결과

### 데이터셋 비교 (Table 1)
| 데이터셋 | 시간(시간) | 작업 수 | 손 자세 | 카메라 궤적 | 리타겟 | 훈련 |
|--------|-------------|--------|---------|---------|--------|------|
| EPIC-KITCHENS | 100 | N/A | ✗ | ✗ | ✗ | ✗ |
| EgoDex | 829 | 194 | ✓ native | ✓ | ✗ | ✗ |
| OpenEgo | 1,107(표 내 수치 2.2→4.557로 계산) | 290 | ✓ unified | Partial | ✗ | ✗ |
| **Open-AoE** | **2,000(표 내 수치 4.0÷2607.1418로 계산)** | **8,000+** | **✓ MANO** | **✓** | **✓** | **✓** |
### 고차원 시각 다양성(3,000회 균형 실험 평균)
| 지표 | Open-AoE | 순위 |
|------|----------|------|
| Effective Rank | 97.43 | 전체 3,000회 실험 1위 |
| Participation Ratio | 40.47 | 전체 3,000회 실험 1위 |
| Meaningful Coverage | 19.89 | 평균 최고 |
| Normalized Cluster Entropy | 0.712 | 평균 최고 |
| Effective Clusters | 16.29 | 평균 최고 |
| kNN Domain Mixing | 0.0775 | 전체 3,000회 실험 1위 |
### 의미 및 시간 주석
- 시간 커버리지: Open-AoE는 평가 타임라인의 99.99%를 커버, OpenEgo는 50.1%.
- 주석 밀도: Open-AoE는 13.97 세그먼트/분.
- 이미지-주석 일관성: Open-AoE 시퀀스 매크로 점수 4.583/5, OpenEgo 3.029, EgoDex 2.916, EgoXtreme 2.015; 95% 부트스트랩 신뢰 구간 [4.557, 4.608].
- 손 신호 가용성: 98.93% 평가 항목이 유효한 손 신호를 하나 이상 포함, 98.02%가 양손 유효 신호 포함.
(이 섹션에는 전체 텍스트에서 확인할 수 없는 숫자가 포함된 4문장이 더 있으며, 규율에 따라 제거됨; 논문에 명시되지 않았거나 그림/표 이미지로 제공됨.)

## 경계 및 한계

저자는 다음 경계를 명시적으로 인정합니다: 카메라 도메인 다양성의 다운스트림 이점은 여전히 훈련 가설이며 통제된 절제 실험으로 검증해야 함; 모든 분포 통계는 동일한 무작위 100시간 샘플에서 비롯되며 전체 데이터 분포 일관성을 보장하지 않음; 작업 수는 소스별 정의를 따르며 데이터셋 간 직접 비교 불가; 로봇화된 비디오의 가치는 동일한 상호작용을 다른 구현에서 정렬된 관측으로 생성하는 것이며, 합성 비디오를 실제 로봇 실행의 대체물로 간주하지 않음; 시간 커버리지는 주석 시간 범위의 합집합으로 계산되고, 평균 지속 시간과 밀도는 주석 기록 기준으로 계산되며, 이 양들을 곱해서는 안 됨; 도구 체인은 보편적 훈련 형식을 주장하지 않고 모델별 동작 의미에 적응함. 카메라 도메인 다양성의 다운스트림 이점을 검증하는 통제된 절제 실험은 제공되지 않았으며, 데이터가 모든 조작 시나리오를 커버한다고 주장하지 않음.

## 엔지니어링 시사점

재현 및 다운스트림 사용을 위한 구체적 지침: 먼저 데이터 계보를 확인하세요 — 통합 프로세스 라벨 파일이 원본 비디오에서 각 Part까지의 전체 체인을 기록하고 다중 레벨 라벨을 누적하며, 이는 데이터 품질 추적의 핵심 진입점입니다. 가장 실수하기 쉬운 부분은 동작 표현 선택입니다: 110D 밀집 MANO와 20D GR00T 그리퍼는 상호 교환 불가하며, 두 20D 인터페이스도 상호 교환 불가하므로 다운스트림 문제에 따라 표현 계층을 선택해야 합니다. 변위와 유한 차분 속도는 미터와 미터/초로 현재 프레임 OpenCV 카메라 좌표(x 오른쪽, y 아래, z 앞)로 표현되며, 이 프레임은 착용자와 함께 움직이므로 속도는 손 움직임과 카메라 자기 운동을 포함하며 순수 관성 손목 움직임이 아닙니다. 이 점을 이해하는 것은 정책 학습에 중요합니다. 훈련 어댑터는 LeRobot(π0.5, ACT, Diffusion Policy), H-RDT, GR00T N1.7, SmolVLA, iVideoGPT, LAOM, GenieRedux, DreamZero, LingBot-VA, Ctrl-World, AdaWorld, DreamDojo를 커버하지만, 도구 체인은 보편적 훈련 형식을 주장하지 않으며 모델별 동작 의미에 맞게 적응해야 합니다. 데이터 라이선스는 CC BY 4.0이며, 공개 플랫폼은 GitHub, Hugging Face, ModelScope입니다.
