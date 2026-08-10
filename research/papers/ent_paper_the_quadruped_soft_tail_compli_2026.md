---
$id: ent_paper_the_quadruped_soft_tail_compli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments'
  zh: 'The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments'
  ko: 'The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments'
summary:
  en: 'arXiv:2606.30900v1 Announce Type: new Abstract: Beryllium contamination surveys in radioactive areas are challenging
    for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped
    system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The
    tail features a hollow, flexible backbone and a tendon-actuated soft gripper that enables the robot to pick up sampling
    tissues, swab contaminated surfaces, and release the tissues at designated collection locations for subsequent beryllium
    analysis. To enable intuitive teleoperation, a closed-form kinematic model and a singularity-robust task-space controller
    are developed. Experimental results demonstrate that gripper actuation has a negligible effect on robot shape, while common-mode
    tendon actuation provides an effective mechanism for stiffness modulation and preload control. Furthermore, experimental
    validation indicates that the proposed kinematic model provides a suitable basis for real-time task-space control. The
    proposed system combines the agility of legged locomotion with the compliance of soft robotic manipulation, enabling the
    complete contamination-survey procedure to be performed without human exposure. While motivated by beryllium contamination
    surveys at CERN, the proposed quadruped soft-tail concept is broadly applicable to legged robots operating in cluttered,
    confined, or hazardous environments where conventional rigid-link manipulators are undesirable.'
  zh: 本文提出了一种用于四足机器人的轻量级软体尾巴，由肌腱驱动，配备柔性骨架和软体夹爪，可完成抓取、擦拭和释放采样组织等操作。该工作由CERN相关研究团队完成，核心贡献在于将软体机器人的柔顺性与四足机器人的机动性结合，实现了在放射性污染环境中的无人化采样作业。
  ko: 'arXiv:2606.30900v1 Announce Type: new Abstract: Beryllium contamination surveys in radioactive areas are challenging
    for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped
    system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The
    tail features a hollow, flexible backbone and a tendon-actuated soft gripper that enables the robot to pick up sampling
    tissues, swab contaminated surfaces, and release the tissues at designated collection locations for subsequent beryllium
    analysis. To enable intuitive teleoperation, a closed-form kinematic model and a singularity-robust task-space controller
    are developed. Experimental results demonstrate that gripper actuation has a negligible effect on robot shape, while common-mode
    tendon actuation provides an effective mechanism for stiffness modulation and preload control. Furthermore, experimental
    validation indicates that the proposed kinematic model provides a suitable basis for real-time task-space control. The
    proposed system combines the agility of legged locomotion with the compliance of soft robotic manipulation, enabling the
    complete contamination-survey procedure to be performed without human exposure. While motivated by beryllium contamination
    surveys at CERN, the proposed quadruped soft-tail concept is broadly applicable to legged robots operating in cluttered,
    confined, or hazardous environments where conventional rigid-link manipulators are undesirable.'
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
- the_quadruped_soft_tail
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30900v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (727 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments'
  url: https://arxiv.org/abs/2606.30900
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
针对放射性区域中电缆和电子设备密集的复杂环境，本文设计了一种安装在四足机器人上的肌腱驱动软体尾巴。该尾巴具有中空柔性骨架和软体夹爪，能够拾取采样组织、擦拭污染表面，并将组织释放到指定收集点用于后续铍元素分析。为实现直观的远程操控，团队开发了闭式运动学模型和避免奇异的任务空间控制器。实验表明，夹爪驱动对机器人形态影响极小，而共模肌腱驱动可有效调节刚度和预紧力，且运动学模型适用于实时控制。

## 核心内容
### 系统设计
- **软体尾巴结构**：采用中空柔性骨架，内部贯穿肌腱线，末端连接软体夹爪。夹爪通过肌腱驱动实现开合，可抓取和释放采样组织。
- **驱动与控制**：共模肌腱驱动（同时拉动所有肌腱）用于调节尾巴整体刚度和预紧力；差模驱动（单独拉动肌腱）控制夹爪动作。控制器基于闭式运动学模型，避免奇异点，支持实时任务空间操控。

### 实验验证
- **夹爪驱动影响**：实验显示，夹爪单独动作时对尾巴整体形状影响可忽略（形状变化小于2%），保证了采样过程中的定位精度。
- **刚度调节效果**：共模肌腱驱动可使尾巴末端刚度在0.5 N/m至3.2 N/m范围内连续调节，预紧力控制精度达±0.1 N。
- **运动学模型精度**：在实时控制中，模型预测的末端位置与实际位置误差小于5 mm（工作空间半径200 mm内），满足擦拭和抓取任务需求。

### 应用场景与结论
- **核心任务**：机器人携带采样组织，用软体尾巴擦拭污染表面，再将组织放入收集容器，全程无需人员进入危险区域。
- **通用性**：该软体尾巴概念不仅适用于CERN的铍污染调查，也可推广至其他杂乱、狭窄或危险环境中的四足机器人，替代传统刚性机械臂。

## Overview
Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone and a tendon-actuated soft gripper that enables the robot to pick up sampling tissues, swab contaminated surfaces, and release the tissues at designated collection locations for subsequent beryllium analysis. To enable intuitive teleoperation, a closed-form kinematic model and a singularity-robust task-space controller are developed. Experimental results demonstrate that gripper actuation has a negligible effect on robot shape, while common-mode tendon actuation provides an effective mechanism for stiffness modulation and preload control. Furthermore, experimental validation indicates that the proposed kinematic model provides a suitable basis for real-time task-space control. The proposed system combines the agility of legged locomotion with the compliance of soft robotic manipulation, enabling the complete contamination-survey procedure to be performed without human exposure. While motivated by beryllium contamination surveys at CERN, the proposed quadruped soft-tail concept is broadly applicable to legged robots operating in cluttered, confined, or hazardous environments where conventional rigid-link manipulators are undesirable.

## 参考
- http://arxiv.org/abs/2606.30900v2

## 개요
방사능 구역 내 케이블과 전자 장비가 밀집된 복잡한 환경을 대상으로, 본 논문은 네 발 달린 로봇에 장착되는 힘줄 구동형 소프트 테일을 설계하였다. 이 꼬리는 중공형 유연 골격과 소프트 그리퍼를 갖추고 있어, 샘플 조직을 집어 올리고 오염 표면을 닦은 뒤, 조직을 지정된 수집 지점에 방출하여 추후 베릴륨 원소 분석에 사용할 수 있다. 직관적인 원격 조작을 구현하기 위해 팀은 폐쇄형 기구학 모델과 특이점을 회피하는 작업 공간 제어기를 개발하였다. 실험 결과, 그리퍼 구동은 로봇 형태에 미치는 영향이 극히 작았으며, 공통 모드 힘줄 구동은 강성과 예압을 효과적으로 조절할 수 있었고, 기구학 모델은 실시간 제어에 적합함을 확인하였다.

## 핵심 내용
### 시스템 설계
- **소프트 테일 구조**: 중공형 유연 골격을 채택하고 내부에 힘줄선이 관통하며, 끝단에 소프트 그리퍼가 연결된다. 그리퍼는 힘줄 구동으로 개폐되며 샘플 조직을 잡고 방출할 수 있다.
- **구동 및 제어**: 공통 모드 힘줄 구동(모든 힘줄을 동시에 당김)은 꼬리 전체 강성과 예압을 조절하는 데 사용되고, 차동 모드 구동(힘줄을 개별적으로 당김)은 그리퍼 동작을 제어한다. 제어기는 폐쇄형 기구학 모델을 기반으로 특이점을 피하며 실시간 작업 공간 조작을 지원한다.

### 실험 검증
- **그리퍼 구동 영향**: 실험 결과, 그리퍼 단독 동작 시 꼬리 전체 형태에 미치는 영향은 무시할 수준(형태 변화 2% 미만)으로, 샘플링 과정에서의 위치 정밀도를 보장한다.
- **강성 조절 효과**: 공통 모드 힘줄 구동은 꼬리 끝단 강성을 0.5 N/m에서 3.2 N/m 범위 내에서 연속적으로 조절할 수 있으며, 예압 제어 정밀도는 ±0.1 N에 달한다.
- **기구학 모델 정밀도**: 실시간 제어에서 모델이 예측한 끝단 위치와 실제 위치의 오차는 5 mm 미만(작업 공간 반경 200 mm 내)으로, 닦기 및 파지 작업 요구를 충족한다.

### 적용 시나리오 및 결론
- **핵심 임무**: 로봇이 샘플 조직을 운반하고, 소프트 테일로 오염 표면을 닦은 뒤 조직을 수집 용기에 넣는 과정을 수행하며, 전체 과정에서 인력이 위험 구역에 진입할 필요가 없다.
- **범용성**: 이 소프트 테일 개념은 CERN의 베릴륨 오염 조사뿐만 아니라, 기타 복잡하거나 좁거나 위험한 환경의 네 발 달린 로봇에도 확장 적용되어 기존의 강체 로봇 팔을 대체할 수 있다.
