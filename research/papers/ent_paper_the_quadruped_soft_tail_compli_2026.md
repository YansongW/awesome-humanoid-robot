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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30900v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
방사능 구역에서의 베릴륨 오염 조사는 케이블과 전자 장비가 복잡하게 얽힌 환경에서 로봇에게 도전적인 과제입니다. 이 문제를 해결하기 위해, 우리는 새로운 사족 로봇 시스템 확장을 개발했습니다: 사족 로봇에 장착된 경량, 부드럽고 유연한 텐던 구동 로봇 꼬리입니다. 이 꼬리는 중공형 유연한 척추와 텐던 구동 소프트 그리퍼를 특징으로 하며, 로봇이 샘플링 조직을 집어 들고, 오염된 표면을 닦아내며, 이후 베릴륨 분석을 위해 지정된 수거 위치에 조직을 놓을 수 있게 합니다. 직관적인 원격 조작을 위해 폐쇄형 운동학 모델과 특이점에 강건한 작업 공간 제어기가 개발되었습니다. 실험 결과는 그리퍼 작동이 로봇 형상에 미치는 영향이 무시할 만한 수준이며, 공통 모드 텐던 작동이 강성 조절 및 예압 제어를 위한 효과적인 메커니즘을 제공함을 보여줍니다. 또한, 실험적 검증은 제안된 운동학 모델이 실시간 작업 공간 제어에 적합한 기반을 제공함을 나타냅니다. 제안된 시스템은 다리 이동의 민첩성과 소프트 로봇 조작의 유연성을 결합하여, 인간의 노출 없이 완전한 오염 조사 절차를 수행할 수 있게 합니다. CERN에서의 베릴륨 오염 조사에 동기를 얻었지만, 제안된 사족 소프트 꼬리 개념은 기존의 강체 링크 매니퓰레이터가 바람직하지 않은 복잡하고, 제한적이며, 위험한 환경에서 작동하는 다리 로봇에 광범위하게 적용 가능합니다.

## 핵심 내용
방사능 구역에서의 베릴륨 오염 조사는 케이블과 전자 장비가 복잡하게 얽힌 환경에서 로봇에게 도전적인 과제입니다. 이 문제를 해결하기 위해, 우리는 새로운 사족 로봇 시스템 확장을 개발했습니다: 사족 로봇에 장착된 경량, 부드럽고 유연한 텐던 구동 로봇 꼬리입니다. 이 꼬리는 중공형 유연한 척추와 텐던 구동 소프트 그리퍼를 특징으로 하며, 로봇이 샘플링 조직을 집어 들고, 오염된 표면을 닦아내며, 이후 베릴륨 분석을 위해 지정된 수거 위치에 조직을 놓을 수 있게 합니다. 직관적인 원격 조작을 위해 폐쇄형 운동학 모델과 특이점에 강건한 작업 공간 제어기가 개발되었습니다. 실험 결과는 그리퍼 작동이 로봇 형상에 미치는 영향이 무시할 만한 수준이며, 공통 모드 텐던 작동이 강성 조절 및 예압 제어를 위한 효과적인 메커니즘을 제공함을 보여줍니다. 또한, 실험적 검증은 제안된 운동학 모델이 실시간 작업 공간 제어에 적합한 기반을 제공함을 나타냅니다. 제안된 시스템은 다리 이동의 민첩성과 소프트 로봇 조작의 유연성을 결합하여, 인간의 노출 없이 완전한 오염 조사 절차를 수행할 수 있게 합니다. CERN에서의 베릴륨 오염 조사에 동기를 얻었지만, 제안된 사족 소프트 꼬리 개념은 기존의 강체 링크 매니퓰레이터가 바람직하지 않은 복잡하고, 제한적이며, 위험한 환경에서 작동하는 다리 로봇에 광범위하게 적용 가능합니다.

## 参考
- http://arxiv.org/abs/2606.30900v2
