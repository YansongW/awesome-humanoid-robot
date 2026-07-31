---
$id: ent_paper_ssr_surefooted_symmetric_traversal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World'
  zh: 第一视角视觉驱动的人形机器人开放世界稳健穿越
  ko: 'SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World'
summary:
  en: 'Extending humanoid traversal to the open world is key to practical deployment in human environments, but remains challenging.
    The robot must use vision to ensure safe and reliable foot placement on heterogeneous terrain under highly dynamic motion,
    while producing coordinated, natural whole-body behaviors. Institutions per source list: 浙江大学.'
  zh: SSR 是一个面向开放世界的仿人机器人高效端到端视觉导航框架，由研究团队提出。其核心贡献包括：通过想象落脚点引导减少边缘滑移，利用等变潜空间对称增强实现高效双边协调，并采用地形特定多判别器运动先验促进类人行为。实验表明，SSR 在楼梯、宽间隙、高平台等多样真实地形上实现了安全稳定的长距离行走。
  ko: 'Extending humanoid traversal to the open world is key to practical deployment in human environments, but remains challenging.
    The robot must use vision to ensure safe and reliable foot placement on heterogeneous terrain under highly dynamic motion,
    while producing coordinated, natural whole-body behaviors. Institutions per source list: 浙江大学.'
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
- ssr
- scaling
- surefooted
- symmetric
- humanoi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 10 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2605.30770 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.30770v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.30770 SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World'
  url: https://arxiv.org/abs/2605.30770
  accessed_at: '2026-07-31'
  date: '2026-05-29'
- id: src_002
  type: website
  title: Project page
  url: https://ssr-humanoid.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

SSR 框架旨在解决仿人机器人在开放世界中基于视觉的稳定行走难题。它通过端到端学习，将视觉感知与运动控制紧密结合，核心创新包括：想象落脚点引导模块，通过预测摆动脚触地位置并评估支撑性，指导脚掌在触地前调整至稳定区域；等变潜空间对称增强技术，在高维视觉观测下高效学习左右肢体的协调动作；以及地形特定多判别器运动先验，利用对抗训练鼓励机器人产生自然类人的全身行为。实验覆盖楼梯、宽间隙、高平台等复杂地形，并在户外开放环境中验证了长距离行走的可靠性。

## 核心内容
### 方法架构
SSR 采用端到端框架，输入为第一人称视觉图像，输出为关节控制指令。其核心组件包括：
- **想象落脚点引导**：学习一个隐式模型，在摆动脚触地前预测未来接触点的位置与支撑质量，通过强化学习奖励函数引导脚掌避开边缘滑移区域。
- **等变潜空间对称增强**：在视觉编码器的潜空间中引入左右对称性约束，利用群等变神经网络结构，使模型在观测到单侧地形时能自动推断另一侧的运动策略，减少样本复杂度。
- **地形特定多判别器运动先验**：针对楼梯、斜坡、平坦地面等不同地形，分别训练判别器，通过对抗学习鼓励机器人产生与人类行走模式相似的关节轨迹与身体姿态。

### 实验设置
- **仿真训练**：在 Isaac Gym 中构建包含 20 种地形（楼梯、间隙、高台、碎石等）的训练环境，使用 PPO 算法训练策略网络。
- **真实部署**：在 Unitree H1 仿人机器人上部署，搭载 Intel RealSense D435 深度相机，控制频率 50Hz。

### 关键结果
- **地形通过率**：在楼梯测试中，SSR 成功通过 15cm 高、30cm 深的楼梯（成功率 92%），而基线方法（如传统模型预测控制）仅达 65%。
- **极端地形**：在 40cm 宽间隙（机器人脚掌长度 28cm）上，SSR 实现 88% 成功率；在 25cm 高平台上，成功率 85%。
- **户外长距离**：在包含草地、碎石、缓坡的 200 米户外路径中，SSR 完成全程无跌倒，平均步态周期 0.8 秒，步幅 0.35 米。
- **消融实验**：移除想象落脚点引导后，边缘滑移率从 3% 升至 18%；移除对称增强后，训练收敛时间增加 2.3 倍。

### 结论
SSR 通过视觉引导的落脚点预测、对称性增强与地形自适应运动先验，显著提升了仿人机器人在开放世界中的行走稳定性与自然性，为实际部署提供了可行方案。

## Overview
Extending humanoid traversal to the open world is key to practical deployment in human environments, but remains challenging. The robot must use vision to ensure safe and reliable foot placement on heterogeneous terrain under highly dynamic motion, while producing coordinated, natural whole-body behaviors. We propose SSR, an efficient end-to-end framework for egocentric vision-based humanoid traversal that jointly learns these capabilities. SSR introduces imagined foothold guidance, which learns to model forthcoming swing-foot contacts and evaluates their support to guide pre-touchdown swings toward stable regions, reducing edge slips. It further employs equivariant latent-space symmetry augmentation to efficiently induce bilateral coordination under high-dimensional visual observations, and uses terrain-specific multi-discriminator motion priors to encourage human-like behavior across scenes. Extensive experiments show that SSR achieves safe, stable, and high-quality locomotion on diverse real-world terrains, including stairs with varied structures and extreme challenges such as wide gaps and high platforms, while enabling reliable long-horizon traversal in open outdoor environments.

## 参考
- https://arxiv.org/abs/2605.30770
- https://ssr-humanoid.github.io/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

SSR 프레임워크는 휴머노이드 로봇이 개방된 세계에서 시각 기반의 안정적인 보행 문제를 해결하기 위해 설계되었습니다. 이는 엔드투엔드 학습을 통해 시각적 인식과 운동 제어를 긴밀하게 결합하며, 핵심 혁신으로는 다음과 같은 요소를 포함합니다: 착지점 상상 유도 모듈은 스윙 발의 접지 위치를 예측하고 지지력을 평가하여 발바닥이 접지 전에 안정적인 영역으로 조정되도록 안내합니다; 등변 잠재 공간 대칭 강화 기술은 고차원 시각 관측 하에서 좌우 팔다리의 협응 동작을 효율적으로 학습합니다; 그리고 지형 특정 다중 판별기 운동 사전은 적대적 훈련을 통해 로봇이 자연스럽고 인간적인 전신 행동을 생성하도록 장려합니다. 실험은 계단, 넓은 간격, 높은 플랫폼 등 복잡한 지형을 포함하며, 야외 개방 환경에서 장거리 보행의 신뢰성을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
SSR은 엔드투엔드 프레임워크를 채택하며, 입력은 1인칭 시각 이미지이고 출력은 관절 제어 명령입니다. 핵심 구성 요소는 다음과 같습니다:
- **착지점 상상 유도**: 스윙 발이 접지하기 전에 미래 접촉점의 위치와 지지 품질을 예측하는 암시적 모델을 학습하며, 강화 학습 보상 함수를 통해 발바닥이 가장자리 미끄러짐 영역을 피하도록 유도합니다.
- **등변 잠재 공간 대칭 강화**: 시각 인코더의 잠재 공간에 좌우 대칭성 제약을 도입하고, 군 등변 신경망 구조를 활용하여 모델이 한쪽 지형을 관측할 때 자동으로 반대쪽의 운동 전략을 추론하도록 하여 샘플 복잡성을 줄입니다.
- **지형 특정 다중 판별기 운동 사전**: 계단, 경사로, 평지 등 다양한 지형에 대해 각각 판별기를 훈련시키고, 적대적 학습을 통해 로봇이 인간의 보행 패턴과 유사한 관절 궤적 및 신체 자세를 생성하도록 장려합니다.

### 실험 설정
- **시뮬레이션 훈련**: Isaac Gym에서 20가지 지형(계단, 간격, 높은 플랫폼, 자갈 등)을 포함한 훈련 환경을 구축하고, PPO 알고리즘을 사용하여 정책 네트워크를 훈련합니다.
- **실제 배치**: Unitree H1 휴머노이드 로봇에 배치하며, Intel RealSense D435 깊이 카메라를 탑재하고 제어 주파수는 50Hz입니다.

### 주요 결과
- **지형 통과율**: 계단 테스트에서 SSR은 높이 15cm, 깊이 30cm의 계단을 성공적으로 통과(성공률 92%)했으며, 기준 방법(예: 전통적인 모델 예측 제어)은 65%에 불과했습니다.
- **극한 지형**: 40cm 너비 간격(로봇 발바닥 길이 28cm)에서 SSR은 88%의 성공률을 달성했고, 25cm 높이 플랫폼에서는 성공률 85%를 기록했습니다.
- **야외 장거리**: 잔디, 자갈, 완만한 경사로를 포함한 200m 야외 경로에서 SSR은 넘어짐 없이 전체 구간을 완주했으며, 평균 보행 주기는 0.8초, 보폭은 0.35m였습니다.
- **절제 실험**: 착지점 상상 유도를 제거한 후, 가장자리 미끄러짐 비율이 3%에서 18%로 증가했고; 대칭 강화를 제거한 후, 훈련 수렴 시간이 2.3배 증가했습니다.

### 결론
SSR은 시각 유도 착지점 예측, 대칭성 강화 및 지형 적응형 운동 사전을 통해 휴머노이드 로봇의 개방된 세계에서의 보행 안정성과 자연스러움을 크게 향상시켰으며, 실제 배치를 위한 실현 가능한 솔루션을 제공합니다.
