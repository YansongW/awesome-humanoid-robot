---
$id: ent_paper_nai_humanoid_manipulation_interfac_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Manipulation Interface (HuMI): Humanoid Whole-Body Manipulation from
    Robot-Free Demonstrations'
  zh: 人形机器人操作接口（HuMI）：无需机器人演示的全身操作
  ko: '휴머노이드 조작 인터페이스(HuMI): 로봇 없는 시연으로부터의 전신 조작'
summary:
  en: HuMI is a portable, robot-free data-collection and hierarchical-learning framework
    that translates human whole-body manipulation demonstrations into autonomous humanoid
    skills. Using handheld sensorized grippers and wearable trackers, it trains a
    high-level Diffusion Policy to predict keypoint trajectories and a low-level RL
    whole-body controller to execute them, achieving 3× teleoperation throughput and
    70% success in unseen environments on a Unitree G1.
  zh: HuMI 是一种便携式、无需机器人的数据采集与分层学习框架，可将人体全身操作演示转化为自主的人形机器人操作技能。该系统仅使用手持传感夹爪和可穿戴追踪器，训练高层扩散策略预测关键点轨迹，并由低层强化学习全身控制器执行，在
    Unitree G1 上实现了比遥操作高 3 倍的数据采集效率，并在未见环境中达到 70% 成功率。
  ko: HuMI는 휴대용 로봇 불필요 데이터 수집 및 계층적 학습 프레임워크로, 인간의 전신 조작 시연을 자율 휴머노이드 조작 기술로 변환한다.
    손에 든 센서화된 그리퍼와 웨어러블 추적기만으로 고차원 확산 정책이 키포인트 궤적을 예측하고, 저차원 강화학습 전신 제어기가 이를 실행하여
    Unitree G1에서 원격조작 대비 3배의 데이터 수집 처리량과 보지 않은 환경에서 70% 성공률을 달성했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_whole_body_manipulation
- robot_free_demonstration
- diffusion_policy
- whole_body_rl_controller
- adaptive_end_effector_tracking
- variable_speed_augmentation
- loco_manipulation
- bimanual_manipulation
- imitation_learning
- unitree_g1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv HTML full text; requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: 'Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free
    Demonstrations'
  url: https://arxiv.org/abs/2602.06643
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

Humanoid Manipulation Interface (HuMI) addresses the logistical and engineering barriers that limit current humanoid whole-body manipulation. Instead of teleoperation or visual sim-to-real reinforcement learning, HuMI collects robot-free demonstrations with portable handheld sensorized grippers and wearable pose trackers, then converts the captured motions into feasible humanoid skills through a hierarchical learning pipeline. The demonstrator wears five HTC Vive Ultimate Trackers on the grippers, waist, and feet, and uses a real-time inverse-kinematics preview interface to adapt motions to the robot's kinematic limits on the fly. This human-in-the-loop adaptation keeps the collected trajectories both task-compliant and executable without requiring the physical robot during data collection.

The learning pipeline has a high-level manipulation policy and a low-level whole-body controller. The high-level policy uses Diffusion Policy to map onboard camera images and proprioception to action chunks represented as relative keypoint trajectories for the grippers and base (and optionally feet). The low-level controller is a reinforcement-learning whole-body tracker that outputs joint commands at 50 Hz to follow the 5 Hz keypoint targets. To improve manipulation precision, the controller introduces adaptive end-effector tracking that tightens tolerance during slow interactions and a variable-speed augmentation that lets the policy practice slow corrections. The policy interface is also redesigned so that each action chunk is anchored to the previous scheduled target pose rather than the lagging executed pose, avoiding momentum-disrupting reversals, and non-vision-grounded keypoints are tracked relatively within a chunk to avoid open-loop drift.

The authors evaluate HuMI on five real-world tasks: marriage proposal (kneeling and ring grasp), squatting to pick up a bottle from the ground, tossing a toy into a container, unsheathing a sword with bimanual coordination, and walking to clean a table with a lint roller. The tasks span whole-body coordination, precise bimanual manipulation, dynamic motion, and long-range loco-manipulation. Quantitative results include an 85% success rate for marriage proposal and sword unsheathing, 75% for tossing and walking-to-clean, and 70% generalization success across unseen environments and objects in the squat-and-pick task.

## Key Contributions

- First robot-free demonstration system specifically designed for humanoid whole-body manipulation.
- Hierarchical learning framework that transfers human manipulation skills to humanoids by overcoming the embodiment gap via whole-body keypoint tracking and real-time IK preview.
- Manipulation-centric whole-body RL controller with adaptive end-effector tracking and variable-speed augmentation for high-precision execution.
- Redesigned high-/low-level policy interface using target-pose action reference and relative tracking for non-vision-grounded keypoints.
- Real-world validation on five diverse tasks, showing 3× higher data-collection throughput than teleoperation and 70% success in unseen environments.

## Relevance to Humanoid Robotics

HuMI is highly relevant to humanoid robotics because it removes the need for the robot itself during data collection, which is one of the main scalability bottlenecks in learning whole-body manipulation. By enabling portable, in-the-wild demonstration capture and converting those demonstrations into generalizable autonomous policies, the framework lowers both the logistical burden and the expertise required to train humanoid robots. The strong generalization results across environments and objects, together with the broad coverage of whole-body behaviors including kneeling, squatting, dynamic tossing, bimanual manipulation, and loco-manipulation, suggest a path toward more capable and deployable humanoid systems outside tightly controlled labs.
