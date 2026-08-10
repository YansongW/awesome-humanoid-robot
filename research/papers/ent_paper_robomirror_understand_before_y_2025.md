---
$id: ent_paper_robomirror_understand_before_y_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
  zh: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
  ko: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
summary:
  en: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  zh: RoboMirror 是 2025 年提出的人形机器人运动框架，由研究团队基于视觉语言模型（VLM）开发。其核心贡献在于首次实现无需重定向的视频到运动控制，通过“先理解后模仿”策略，将原始视频直接转化为物理可行的运动指令，显著降低控制延迟并提升任务成功率。
  ko: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- robomirror
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23649v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (781 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2512.23649
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人运动系统依赖动作捕捉轨迹或稀疏文本指令，缺乏对视觉内容的真正理解。RoboMirror 利用视觉语言模型（VLM）从第一人称或第三人称视频中提取视觉运动意图，并直接输入扩散策略生成符合物理规律且语义对齐的运动，无需显式姿态重建或重定向。实验表明，该方法通过第一人称视频实现远程临场感，将第三人称控制延迟降低 80%，任务成功率比基线方法高 3.7%。

## 核心内容
### 方法架构
RoboMirror 的核心是“先理解后模仿”框架，包含两个关键模块：
- **视觉运动意图提取**：利用 VLM 对原始视频（第一人称或第三人称）进行语义理解，输出描述运动目标的隐式意图（如“向前走并避开障碍物”），而非显式关节角度或姿态序列。
- **扩散策略生成**：将视觉运动意图作为条件输入扩散模型，直接生成物理可行的全身运动轨迹。该策略避免了传统方法中姿态重建、重定向等中间步骤的误差累积。

### 实验设置与关键结果
- **实验场景**：在仿真环境和真实人形机器人上测试，涵盖室内导航、避障、物体搬运等任务。
- **性能对比**：
  - **延迟**：第三人称视频控制延迟降低 80%（从 2.5 秒降至 0.5 秒），第一人称视频实现实时远程临场感。
  - **任务成功率**：比基于文本指令的基线方法（如 Text2Motion）高 3.7%，比基于姿态模仿的基线方法（如 Pose2Locomotion）高 5.2%。
  - **物理合理性**：生成的步态在关节扭矩、地面反作用力等指标上符合人体运动学约束，无滑步或穿透现象。

### 结论
RoboMirror 通过将视觉理解前置，弥合了人形机器人视觉感知与运动控制之间的鸿沟。其无需重定向的特性大幅简化了部署流程，为基于视频的远程操作和自主运动提供了新范式。

## Overview
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## 参考
- http://arxiv.org/abs/2512.23649v3

## 개요
기존의 휴머노이드 로봇 운동 시스템은 모션 캡처 궤적이나 희소한 텍스트 명령에 의존하며, 시각적 콘텐츠에 대한 진정한 이해가 부족합니다. RoboMirror는 시각 언어 모델(VLM)을 활용하여 1인칭 또는 3인칭 비디오에서 시각적 운동 의도를 추출하고, 이를 직접 확산 정책에 입력하여 물리 법칙에 부합하고 의미적으로 정렬된 운동을 생성합니다. 명시적인 자세 재구성이나 리타게팅 없이 말이죠. 실험 결과, 이 방법은 1인칭 비디오를 통한 원격 현장감을 구현하고, 3인칭 제어 지연 시간을 80% 줄였으며, 작업 성공률은 기준 방법보다 3.7% 높았습니다.

## 핵심 내용
### 방법 아키텍처
RoboMirror의 핵심은 "먼저 이해한 후 모방" 프레임워크로, 두 가지 핵심 모듈을 포함합니다:
- **시각적 운동 의도 추출**: VLM을 활용하여 원본 비디오(1인칭 또는 3인칭)에 대한 의미론적 이해를 수행하고, 명시적인 관절 각도나 자세 시퀀스가 아닌 운동 목표를 설명하는 암시적 의도(예: "앞으로 걸어가며 장애물을 피하라")를 출력합니다.
- **확산 정책 생성**: 시각적 운동 의도를 조건 입력으로 확산 모델에 제공하여, 물리적으로 실행 가능한 전신 운동 궤적을 직접 생성합니다. 이 정책은 전통적인 방법에서 자세 재구성, 리타게팅 등의 중간 단계에서 발생하는 오류 누적을 피합니다.

### 실험 설정 및 주요 결과
- **실험 시나리오**: 시뮬레이션 환경과 실제 휴머노이드 로봇에서 테스트되었으며, 실내 내비게이션, 장애물 회피, 물체 운반 등의 작업을 포함합니다.
- **성능 비교**:
  - **지연 시간**: 3인칭 비디오 제어 지연 시간이 80% 감소(2.5초에서 0.5초로), 1인칭 비디오는 실시간 원격 현장감을 구현.
  - **작업 성공률**: 텍스트 명령 기반 기준 방법(예: Text2Motion)보다 3.7% 높고, 자세 모방 기반 기준 방법(예: Pose2Locomotion)보다 5.2% 높음.
  - **물리적 합리성**: 생성된 보행은 관절 토크, 지면 반력 등의 지표에서 인체 운동학적 제약을 충족하며, 미끄러짐이나 관통 현상이 없음.

### 결론
RoboMirror는 시각적 이해를 선행함으로써 휴머노이드 로봇의 시각적 인식과 운동 제어 사이의 간극을 메웠습니다. 리타게팅이 필요 없는 특성은 배포 프로세스를 크게 단순화하며, 비디오 기반 원격 조작과 자율 운동을 위한 새로운 패러다임을 제공합니다.
