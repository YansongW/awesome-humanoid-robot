---
$id: ent_paper_panorama_aware_vla_mobile_manipulation_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation
  zh: Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation
  ko: Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation
summary:
  en: 'Mobile manipulation is a key capability for embodied intelligence, enabling robots to accomplish complex multi-stage
    tasks in open-world environments. However, mobile manipulation poses two key challenges for vision-language-action (VLA)
    policies: At the data level, the efficient collection of high-quality whole-body demonstrations demands the coordinated
    control of both the mobile base and the.'
  zh: 本文提出PanoVLA，一种面向移动操作的全景感知视觉-语言-动作模型，配合基于VR的全身遥操作系统实现野外数据采集。核心贡献在于通过引入全景专家模块和MTPano编码器，将全局空间上下文注入VLA策略，在4个真实移动操作任务上平均成功率从30.0%提升至73.4%。
  ko: 'Mobile manipulation is a key capability for embodied intelligence, enabling robots to accomplish complex multi-stage
    tasks in open-world environments. However, mobile manipulation poses two key challenges for vision-language-action (VLA)
    policies: At the data level, the efficient collection of high-quality whole-body demonstrations demands the coordinated
    control of both the mobile base and the.'
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
- panorama
- aware
- vla
- mobile
- manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2608.02257 Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperatio
  url: https://arxiv.org/abs/2608.02257
  date: '2026-08-03'
  accessed_at: '2026-08-05'
---

## 概述

本文提出PanoVLA，一种面向移动操作的全景感知视觉-语言-动作模型，配合基于VR的全身遥操作系统实现野外数据采集。核心贡献在于通过引入全景专家模块和MTPano编码器，将全局空间上下文注入VLA策略，在4个真实移动操作任务上平均成功率从30.0%提升至73.4%。

## 它改变了什么

移动操作VLA面临的核心矛盾在于：局部相机视野与全局空间推理需求之间的鸿沟。现有π_0.5等模型仅依赖前视和腕部相机，在底盘旋转或机械臂自遮挡时，目标物体和地标频繁脱离视野，导致策略在长时程任务中"迷失"。简单拼接更多图像流（如Stacked Pano）无法建立连贯的以机器人为中心的空间表征，反而引入冗余计算和域偏移。

本文真正改变的是VLA架构中"全局上下文注入"的方式——不再将全景图像作为额外输入token简单拼接，而是设计独立的全景专家模块，通过KV缓存机制与VLM专家交互，在保持局部精细操作能力的同时，显式建模任务相关的全局空间关系。这解决了两个此前被忽视的问题：一是等距柱状投影与预训练视觉编码器（SigLIP）之间的域差距，二是全局信息与局部动作预测之间的融合接口设计。

## 方法拆解

### 遥操作数据采集
- 基于VR的全身遥操作：6-DoF头部追踪、双手控制器、三个身体追踪器（腰+双踝）
- GMR（General Motion Retargeting）框架将稀疏人体运动重定向到轮式双臂机器人
- 机器人配置参数化：q = (x_b, y_b, θ_b, q_L, q_R)，其中底盘位姿在局部遥操作坐标系中表达
- 重定向优化目标：q* = arg min_q [λ_pos·L_pos + λ_rot·L_rot + λ_base·L_base + λ_reg·L_reg]
  - L_pos：手与夹爪位置对齐
  - L_rot：手与末端执行器方向对齐
  - L_base：底盘平面运动与操作员骨盆位移/朝向耦合
  - L_reg：关节极限与配置变化正则化
- 成本驱动模式切换：每控制周期评估自旋、阿克曼转向、对角平移三种模式与期望运动的匹配成本，选最优执行

### PanoVLA架构
- 基于Mixture-of-Transformers（MoT），从π_0.5双专家骨干扩展为三专家：
  - VLM专家：编码局部视图、指令、机器人状态
  - 全景专家：将宽视野观测转换为任务条件空间上下文
  - 动作专家：预测连续动作块
- 融合接口：Transformer KV缓存
  - VLM专家计算缓存C_t^vlm
  - 全景编码器将全景图像转为token Z_t^pano
  - 全景专家与C_t^vlm联合自注意力，产生C_t^pano
  - 动作专家基于组合缓存C_t = [C_t^vlm; C_t^pano]预测动作
- 全景编码器三阶段：
  1. 球面投影：双鱼眼视图重投影到公共球面，栅格化为ERP图像
  2. 特征提取：MTPano基础模型，拼接分割和深度分支中间特征
  3. Token适配：自适应平均池化压缩空间分辨率，轻量MLP映射到专家隐藏维度
- 训练目标：条件流匹配，L = E[||v_θ^act(x_τ, τ|C_t) - u(x_τ|a)||²₂]

### 关键设计决策
- 选择MTPano而非SigLIP：SigLIP在透视图像预训练，对ERP的水平连续性和全局布局捕获差
- 全景专家规模100M：50M容量不足，200M/300M在有限微调数据下无一致改进

## 关键创新

1. **全景专家模块的独立设计**：不同于将全景图像作为额外输入通道的朴素做法，PanoVLA将全局空间推理从VLM中解耦，通过KV缓存实现信息交互。这使得全景信息可以"条件化"VLM的局部推理，而非简单叠加，避免了特征稀释和域偏移问题。

2. **MTPano作为全景编码器**：利用全景基础模型的中间特征（分割+深度分支），而非通用视觉编码器。这一选择直接回应了ERP图像与透视预训练编码器之间的域差距，实验显示SigLIP编码器在Move Pen任务上SR仅40.0%，而MTPano达到86.7%。

3. **全身遥操作与VLA训练的数据闭环**：VR遥操作系统的成本驱动模式切换和GMR重定向，使得在无真实机器人条件下采集高质量全身演示成为可能，为VLA提供了与部署平台一致的训练数据分布。

## 实验与结果

**主要结果（15次闭环试验/任务）**：

| 方法 | Move Pen SR | Move Block SR | Open Curtain SR | Wipe Table SR | 平均SR |
|------|------------|--------------|----------------|--------------|--------|
| π_0.5 | 46.7% | 20.0% | 26.7% | 26.7% | 30.0% |
| π_0.5 w/ Pano | 86.7% | 73.3% | 46.7% | 20.0% | 56.7% |
| π_0.5 w/ Stacked Pano | 60.0% | 40.0% | 13.3% | 40.0% | 38.3% |
| **PanoVLA** | **86.7%** | **93.3%** | **66.7%** | **46.7%** | **73.4%** |

**关键观察**：
- PanoVLA在Move Block任务上提升最显著（20.0%→93.3%），该任务需要跨区域空间推理
- π_0.5 w/ Pano在Wipe Table上SR仅20.0%，尽管SCR达74.4%，说明简单拼接全景图像在长时程任务中导致末端执行精度下降
- PanoVLA在Wipe Table最后阶段完成率73.3%，显著优于π_0.5 w/ Pano的26.7%

**消融实验（Move Pen，15次试验）**：
- 专家规模：50M SR 60.0%，100M SR 86.7%，200M SR 86.7%，300M SR 73.3%
- 全景编码器：SigLIP SR 40.0%，MTPano SR 86.7%

## 边界与局限

论文未明确提及局限性讨论章节。从实验设置可推断：每个策略仅使用对应任务的200条演示独立微调，未验证跨任务泛化能力；未与MoManipVLA、SG-VLA等最新移动操作VLA方法直接对比；未探索超过300M的全景专家规模；未在仿真环境中评估。Wipe Table任务上PanoVLA的SR仅46.7%，说明在需要精细末端操作与全局导航结合的场景中仍有明显不足。

## 工程启示

复现时需优先核对以下环节：
1. **全景编码器选择**：务必使用MTPano而非SigLIP，这是性能差距最大的单一因素（SR 86.7% vs 40.0%）
2. **专家规模**：100M是性价比最优选择，300M反而性能下降，可能与有限微调数据下的过拟合有关
3. **KV缓存融合机制**：需确保VLM缓存和全景缓存的维度匹配，且块级因果掩码M_pano正确实现，否则全局信息可能泄漏到局部推理
4. **数据采集一致性**：遥操作系统的成本驱动模式切换逻辑需与部署时底盘控制策略一致，否则训练-部署分布偏移会显著影响成功率
5. **训练配置**：冻结语言模型和MTPano编码器，仅优化其余模块；30K步、学习率5e-5、批大小64（4×A100）是已验证的配置，RTX 4090可闭环推理

最易踩坑之处在于全景token的球面投影和栅格化参数——若ERP图像分辨率或投影中心设置不当，会直接影响MTPano特征质量，进而导致全局上下文注入失效。

## Overview
Mobile manipulation is a key capability for embodied intelligence, enabling robots to accomplish complex multi-stage tasks in open-world environments. However, mobile manipulation poses two key challenges for vision-language-action (VLA) policies: At the data level, the efficient collection of high-quality whole-body demonstrations demands the coordinated control of both the mobile base and the robotic arms; at the model level, existing VLA models predominantly rely on local camera observations, whose limited field of view hinders global spatial understanding. To address these challenges, we develop a whole-body teleoperation system and a panoramic-aware VLA policy. The system enables coordinated control of a wheeled bimanual robot through a single VR interface and supports the acquisition of a real-world mobile manipulation dataset comprising 5.5 hours of multimodal demonstrations. Building upon this dataset, we propose PanoVLA, a panorama-aware vision-language-action policy for mobile bimanual manipulation. Built upon a Mixture-of-Transformers architecture, PanoVLA introduces global spatial context through dedicated panorama encoding and fusion modules, enabling effective integration of panoramic observations with language instructions and robot states for action generation. Evaluation on four real-world mobile manipulation tasks demonstrates that PanoVLA achieves an average stage completion rate of 91.3\% and an end-to-end success rate of 73.4\%, substantially outperforming local-view baselines. These results demonstrate that incorporating panoramic spatial context improves spatial understanding and closed-loop manipulation performance in mobile robots.

## 参考
- https://arxiv.org/abs/2608.02257

## 개요

본 논문은 모바일 조작을 위한 전방위 인식 비전-언어-행동 모델인 PanoVLA를 제안하며, VR 기반 전신 원격 조작 시스템을 결합하여 야외 데이터 수집을 구현한다. 핵심 기여는 전방위 전문가 모듈과 MTPano 인코더를 도입하여 전역 공간 컨텍스트를 VLA 정책에 주입함으로써, 4가지 실제 모바일 조작 작업에서 평균 성공률을 30.0%에서 73.4%로 향상시킨 것이다.

## 무엇을 변화시켰는가

모바일 조작 VLA가 직면한 핵심 모순은 로컬 카메라 시야와 전역 공간 추론 요구 사이의 격차이다. 기존 π_0.5와 같은 모델은 전방 카메라와 손목 카메라에만 의존하여, 섀시 회전이나 로봇 팔의 자기 폐색 시 대상 물체와 랜드마크가 시야에서 자주 벗어나 정책이 장기 작업에서 "길을 잃는" 문제가 발생한다. 단순히 더 많은 이미지 스트림을 연결하는 방식(예: Stacked Pano)은 로봇 중심의 일관된 공간 표현을 구축하지 못하며, 오히려 중복 계산과 도메인 편향을 초래한다.

본 논문이 실제로 변화시킨 것은 VLA 아키텍처에서 "전역 컨텍스트 주입" 방식이다. 즉, 전방위 이미지를 추가 입력 토큰으로 단순 연결하는 대신, 독립적인 전방위 전문가 모듈을 설계하고 KV 캐시 메커니즘을 통해 VLM 전문가와 상호작용하게 하여, 로컬 정밀 조작 능력을 유지하면서 작업 관련 전역 공간 관계를 명시적으로 모델링한다. 이는 이전에 간과된 두 가지 문제를 해결한다. 첫째는 등장방형 투영과 사전 훈련된 시각 인코더(SigLIP) 간의 도메인 격차, 둘째는 전역 정보와 로컬 행동 예측 간의 융합 인터페이스 설계이다.

## 방법 분석

### 원격 조작 데이터 수집
- VR 기반 전신 원격 조작: 6-DoF 헤드 트래킹, 양손 컨트롤러, 세 개의 신체 트래커(허리 + 양쪽 발목)
- GMR(General Motion Retargeting) 프레임워크가 희소 인체 모션을 바퀴형 이팔 로봇으로 재타겟팅
- 로봇 구성 파라미터화: q = (x_b, y_b, θ_b, q_L, q_R), 여기서 섀시 포즈는 로컬 원격 조작 좌표계에서 표현
- 재타겟팅 최적화 목표: q* = arg min_q [λ_pos·L_pos + λ_rot·L_rot + λ_base·L_base + λ_reg·L_reg]
  - L_pos: 손과 그리퍼 위치 정렬
  - L_rot: 손과 엔드 이펙터 방향 정렬
  - L_base: 섀시 평면 운동과 조작자 골반 변위/방향 커플링
  - L_reg: 관절 한계 및 구성 변화 정규화
- 비용 기반 모드 전환: 각 제어 주기마다 회전, 애커만 조향, 대각 이동 세 가지 모드와 원하는 운동의 매칭 비용을 평가하여 최적 모드 선택

### PanoVLA 아키텍처
- Mixture-of-Transformers(MoT) 기반, π_0.5의 이중 전문가 백본을 삼중 전문가로 확장:
  - VLM 전문가: 로컬 뷰, 명령, 로봇 상태 인코딩
  - 전방위 전문가: 광시야 관측을 작업 조건 공간 컨텍스트로 변환
  - 행동 전문가: 연속 행동 블록 예측
- 융합 인터페이스: Transformer KV 캐시
  - VLM 전문가가 캐시 C_t^vlm 계산
  - 전방위 인코더가 전방위 이미지를 토큰 Z_t^pano로 변환
  - 전방위 전문가가 C_t^vlm과 결합된 자기 주의를 수행하여 C_t^pano 생성
  - 행동 전문가가 결합 캐시 C_t = [C_t^vlm; C_t^pano] 기반으로 행동 예측
- 전방위 인코더 3단계:
  1. 구면 투영: 이중 어안 뷰를 공통 구면에 재투영하고, 격자화하여 ERP 이미지 생성
  2. 특징 추출: MTPano 기반 모델, 분할 및 깊이 분기 중간 특징 연결
  3. 토큰 적응: 적응형 평균 풀링으로 공간 해상도 압축, 경량 MLP로 전문가 숨김 차원 매핑
- 훈련 목표: 조건부 흐름 매칭, L = E[||v_θ^act(x_τ, τ|C_t) - u(x_τ|a)||²₂]

### 핵심 설계 결정
- SigLIP 대신 MTPano 선택: SigLIP은 투시 이미지로 사전 훈련되어 ERP의 수평 연속성과 전역 레이아웃 포착이 부족
- 전방위 전문가 규모 100M: 50M 용량 부족, 200M/300M은 제한된 미세 조정 데이터에서 일관된 개선 없음

## 핵심 혁신

1. **전방위 전문가 모듈의 독립 설계**: 전방위 이미지를 추가 입력 채널로 사용하는 단순한 방식과 달리, PanoVLA는 전역 공간 추론을 VLM에서 분리하고 KV 캐시를 통해 정보 상호작용을 구현한다. 이를 통해 전방위 정보가 VLM의 로컬 추론을 "조건화"할 수 있으며, 단순 중첩이 아닌 방식으로 특징 희석과 도메인 편향 문제를 피한다.

2. **MTPano를 전방위 인코더로 사용**: 일반 시각 인코더 대신 전방위 기반 모델의 중간 특징(분할 + 깊이 분기)을 활용한다. 이 선택은 ERP 이미지와 투시 사전 훈련 인코더 간의 도메인 격차에 직접 대응하며, 실험에서 SigLIP 인코더는 Move Pen 작업에서 SR 40.0%에 불과하지만 MTPano는 86.7%를 달성한다.

3. **전신 원격 조작과 VLA 훈련의 데이터 폐루프**: VR 원격 조작 시스템의 비용 기반 모드 전환과 GMR 재타겟팅은 실제 로봇 없이도 고품질 전신 데모 수집을 가능하게 하여, VLA에 배포 플랫폼과 일치하는 훈련 데이터 분포를 제공한다.

## 실험 및 결과

**주요 결과(작업당 15회 폐루프 시험)**:

| 방법 | Move Pen SR | Move Block SR | Open Curtain SR | Wipe Table SR | 평균 SR |
|------|------------|--------------|----------------|--------------|--------|
| π_0.5 | 46.7% | 20.0% | 26.7% | 26.7% | 30.0% |
| π_0.5 w/ Pano | 86.7% | 73.3% | 46.7% | 20.0% | 56.7% |
| π_0.5 w/ Stacked Pano | 60.0% | 40.0% | 13.3% | 40.0% | 38.3% |
| **PanoVLA** | **86.7%** | **93.3%** | **66.7%** | **46.7%** | **73.4%** |

**핵심 관찰**:
- PanoVLA는 Move Block 작업에서 가장 큰 향상을 보임(20.0%→93.3%), 이 작업은 지역 간 공간 추론이 필요
- π_0.5 w/ Pano는 Wipe Table에서 SR 20.0%에 불과하지만 SCR은 74.4%로, 단순 전방위 이미지 연결이 장기 작업에서 엔드 이펙터 정밀도를 저하시킴을 시사
- PanoVLA는 Wipe Table 마지막 단계에서 완료율 73.3%로 π_0.5 w/ Pano의 26.7%보다 크게 우수

**소거 실험(Move Pen, 15회 시험)**:
- 전문가 규모: 50M SR 60.0%, 100M SR 86.7%, 200M SR 86.7%, 300M SR 73.3%
- 전방위 인코더: SigLIP SR 40.0%, MTPano SR 86.7%

## 경계 및 한계

논문은 한계 논의 섹션을 명시적으로 언급하지 않았다. 실험 설정에서 추론할 수 있는 점: 각 정책은 해당 작업의 200개 데모로만 독립적으로 미세 조정되어 교차 작업 일반화 능력이 검증되지 않음; MoManipVLA, SG-VLA와 같은 최신 모바일 조작 VLA 방법과 직접 비교하지 않음; 300M 이상의 전방위 전문가 규모를 탐색하지 않음; 시뮬레이션 환경에서 평가하지 않음. Wipe Table 작업에서 PanoVLA의 SR은 46.7%에 불과하여, 정밀 엔드 이펙터 조작과 전역 내비게이션 결합이 필요한 시나리오에서 여전히 뚜렷한 부족함이 있음을 보여준다.

## 공학적 시사점

재현 시 다음 단계를 우선적으로 검증해야 한다:
1. **전방위 인코더 선택**: 반드시 SigLIP 대신 MTPano를 사용해야 하며, 이는 성능 차이가 가장 큰 단일 요소(SR 86.7% vs 40.0%)
2. **전문가 규모**: 100M이 비용 대비 최적이며, 300M은 오히려 성능이 저하되는데, 이는 제한된 미세 조정 데이터에서의 과적합과 관련될 수 있음
3. **KV 캐시 융합 메커니즘**: VLM 캐시와 전방위 캐시의 차원 일치를 보장하고, 블록 수준 인과 마스크 M_pano가 올바르게 구현되어야 함. 그렇지 않으면 전역 정보가 로컬 추론에 누출될 수 있음
4. **데이터 수집 일관성**: 원격 조작 시스템의 비용 기반 모드 전환 로직이 배포 시 섀시 제어 정책과 일치해야 하며, 그렇지 않으면 훈련-배포 분포 편향이 성공률에 크게 영향을 미침
5. **훈련 구성**: 언어 모델과 MTPano 인코더를 동결하고 나머지 모듈만 최적화; 30K 스텝, 학습률 5e-5, 배치 크기 64(4×A100)는 검증된 구성이며, RTX 4090에서 폐루프 추론 가능

가장 함정에 빠지기 쉬운 부분은 전방위 토큰의 구면 투영 및 격자화 파라미터이다. ERP 이미지 해상도나 투영 중심 설정이 잘못되면 MTPano 특징 품질에 직접 영향을 미쳐 전역 컨텍스트 주입이 실패할 수 있다.
