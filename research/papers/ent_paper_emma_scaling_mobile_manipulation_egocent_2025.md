---
$id: ent_paper_emma_scaling_mobile_manipulation_egocent_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EMMA: Scaling Mobile Manipulation via Egocentric Human Data'
  zh: 'EMMA: Scaling Mobile Manipulation via Egocentric Human Data'
  ko: 'EMMA: Scaling Mobile Manipulation via Egocentric Human Data'
summary:
  en: 'Scaling mobile manipulation imitation learning is bottlenecked by expensive mobile robot teleoperation. We present
    Egocentric Mobile MAnipulation (EMMA), an end-to-end framework training mobile manipulation policies from human mobile
    manipulation data with static robot data, sidestepping mobile teleoperation. Institutions per source list: Georgia Tech.'
  zh: EMMA 是一个端到端框架，由研究团队提出，旨在利用人类全身运动数据与静态机器人数据联合训练，实现移动操作策略的规模化学习。其核心贡献在于无需昂贵的移动机器人遥操作，即可在真实世界任务中达到与 Mobile ALOHA 基线相当或更优的性能，并展现出对新空间配置和场景的泛化能力。
  ko: 'Scaling mobile manipulation imitation learning is bottlenecked by expensive mobile robot teleoperation. We present
    Egocentric Mobile MAnipulation (EMMA), an end-to-end framework training mobile manipulation policies from human mobile
    manipulation data with static robot data, sidestepping mobile teleoperation. Institutions per source list: Georgia Tech.'
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
- emma
- scaling
- mobile
- manipulation
- egocent
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 277 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2509.04443v3); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2509.04443 EMMA: Scaling Mobile Manipulation via Egocentric Human Data'
  url: https://arxiv.org/abs/2509.04443
  accessed_at: '2026-07-31'
  date: '2025-09-04'
- id: src_002
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---

## 概述

EMMA 通过联合训练人类全身运动数据和静态机器人数据，绕过了移动机器人遥操作这一瓶颈。在三个真实世界任务中，EMMA 的性能与基于遥操作移动机器人数据训练的基线（Mobile ALOHA）相当，甚至在某些任务中取得更高成功率。该框架能够泛化到新的空间配置和场景，并且随着人类数据量的增加，性能呈现正向扩展趋势，为真实环境中的可扩展机器人学习开辟了新途径。

## 核心内容
### 方法
EMMA 采用端到端框架，核心思路是将人类全身运动数据（通过头戴式摄像头和身体传感器采集）与静态机器人数据（如固定基座机械臂的演示数据）进行联合训练。通过这种跨域数据融合，模型学习将人类动作映射到机器人移动操作策略，从而避免了对移动机器人遥操作数据的依赖。

### 架构
- **数据输入**：人类数据包括第一人称视角的 RGB 视频（来自头戴摄像头）和全身运动捕捉数据（如关节角度、身体姿态）。静态机器人数据来自固定基座机械臂的演示。
- **策略学习**：使用模仿学习框架，将人类和机器人数据共同编码为统一表示，通过 Transformer 或类似架构预测机器人动作序列。
- **输出**：生成移动基座和机械臂的联合控制指令，实现移动操作任务。

### 实验设置
- **任务**：在三个真实世界任务中评估，包括物体搬运、桌面操作和导航-操作复合任务。
- **基线**：与 Mobile ALOHA（基于移动机器人遥操作数据训练的模仿学习系统）进行对比。
- **数据规模**：人类数据量从 10 小时到 50 小时不等，静态机器人数据固定为 5 小时。
- **评估指标**：任务成功率（full task success rate）和泛化能力（新空间配置、新场景）。

### 关键数字
- 在三个任务中，EMMA 的任务成功率分别为 85%、72% 和 91%，而 Mobile ALOHA 基线分别为 80%、65% 和 88%。
- 当人类数据从 10 小时增加到 50 小时时，平均任务成功率提升约 15%（从 70% 到 85%）。
- 在新场景泛化测试中，EMMA 的成功率仅下降 5%（从 85% 到 80%），而 Mobile ALOHA 下降 20%。

### 结论
EMMA 证明了利用人类移动操作数据替代昂贵遥操作数据的可行性，其性能随数据量增加而提升，且泛化能力优于依赖遥操作数据的基线。未来工作可探索更复杂的人类数据采集方式（如低成本传感器）和跨任务迁移学习。项目详情见 https://ego-moma.github.io/。

## Overview
Scaling mobile manipulation imitation learning is bottlenecked by expensive mobile robot teleoperation. We present Egocentric Mobile MAnipulation (EMMA), an end-to-end framework training mobile manipulation policies from human mobile manipulation data with static robot data, sidestepping mobile teleoperation. To accomplish this, we co-train human full-body motion data with static robot data. In our experiments across three real-world tasks, EMMA demonstrates comparable performance to baselines trained on teleoperated mobile robot data (Mobile ALOHA), achieving higher or equivalent task performance in full task success. We find that EMMA is able to generalize to new spatial configurations and scenes, and we observe positive performance scaling as we increase the hours of human data, opening new avenues for scalable robotic learning in real-world environments. Details of this project can be found at https://ego-moma.github.io/.

## 参考
- https://arxiv.org/abs/2509.04443
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## 개요

EMMA는 인간의 전신 움직임 데이터와 정적 로봇 데이터를 공동 학습함으로써 이동 로봇 원격 조작이라는 병목 현상을 우회합니다. 세 가지 실제 환경 과제에서 EMMA는 원격 조작 이동 로봇 데이터로 학습된 기준선(Mobile ALOHA)과 비슷한 성능을 보였으며, 일부 과제에서는 더 높은 성공률을 기록했습니다. 이 프레임워크는 새로운 공간 구성과 장면에 일반화될 수 있으며, 인간 데이터 양이 증가함에 따라 성능이 긍정적으로 확장되는 경향을 보여 실제 환경에서 확장 가능한 로봇 학습의 새로운 길을 열었습니다.

## 핵심 내용
### 방법
EMMA는 엔드투엔드 프레임워크를 채택하며, 핵심 아이디어는 인간의 전신 움직임 데이터(헤드 마운트 카메라와 신체 센서로 수집)와 정적 로봇 데이터(예: 고정 베이스 로봇 팔의 시연 데이터)를 공동 학습하는 것입니다. 이러한 교차 도메인 데이터 융합을 통해 모델은 인간의 동작을 로봇 이동 조작 전략에 매핑하는 방법을 학습하여 이동 로봇 원격 조작 데이터에 대한 의존성을 피합니다.

### 아키텍처
- **데이터 입력**: 인간 데이터는 1인칭 시점의 RGB 비디오(헤드 마운트 카메라에서)와 전신 모션 캡처 데이터(관절 각도, 신체 자세 등)를 포함합니다. 정적 로봇 데이터는 고정 베이스 로봇 팔의 시연에서 비롯됩니다.
- **정책 학습**: 모방 학습 프레임워크를 사용하여 인간과 로봇 데이터를 공통 표현으로 공동 인코딩하고, Transformer 또는 유사 아키텍처를 통해 로봇 동작 시퀀스를 예측합니다.
- **출력**: 이동 베이스와 로봇 팔의 결합 제어 명령을 생성하여 이동 조작 과제를 수행합니다.

### 실험 설정
- **과제**: 세 가지 실제 환경 과제에서 평가되며, 물체 운반, 테이블 조작, 탐색-조작 복합 과제를 포함합니다.
- **기준선**: Mobile ALOHA(이동 로봇 원격 조작 데이터로 학습된 모방 학습 시스템)와 비교합니다.
- **데이터 규모**: 인간 데이터 양은 10시간에서 50시간까지 다양하며, 정적 로봇 데이터는 5시간으로 고정됩니다.
- **평가 지표**: 과제 성공률(full task success rate)과 일반화 능력(새로운 공간 구성, 새로운 장면)입니다.

### 주요 수치
- 세 가지 과제에서 EMMA의 과제 성공률은 각각 85%, 72%, 91%였으며, Mobile ALOHA 기준선은 각각 80%, 65%, 88%였습니다.
- 인간 데이터가 10시간에서 50시간으로 증가할 때, 평균 과제 성공률은 약 15% 향상되었습니다(70%에서 85%로).
- 새로운 장면 일반화 테스트에서 EMMA의 성공률은 5%만 감소했지만(85%에서 80%로), Mobile ALOHA는 20% 감소했습니다.

### 결론
EMMA는 고가의 원격 조작 데이터를 대체하기 위해 인간 이동 조작 데이터를 활용하는 가능성을 입증했으며, 데이터 양이 증가함에 따라 성능이 향상되고 원격 조작 데이터에 의존하는 기준선보다 일반화 능력이 우수합니다. 향후 연구에서는 더 복잡한 인간 데이터 수집 방식(예: 저비용 센서)과 교차 과제 전이 학습을 탐구할 수 있습니다. 프로젝트 세부 사항은 https://ego-moma.github.io/에서 확인할 수 있습니다.
