---
$id: ent_robot_system_bruce
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
  zh: BRUCE 儿童尺寸人形机器人
  ko: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
summary:
  en: A 70 cm, 4.8 kg child-size bipedal humanoid platform co-developed by Westwood Robotics and UCLA RoMeLa, with 16 degrees
    of freedom, proprioceptive quasi-direct-drive Koala BEAR actuators with liquid cooling on key joints, and a variable-frequency
    MPC stack for highly dynamic walking, running and jumping.
  zh: BRUCE（Bipedal Robot Unit with Compliance Enhanced）是 Westwood Robotics（西木科技）与 UCLA RoMeLa 联合开发的 70 cm / 4.8 kg 儿童尺寸双足人形平台，16
    个自由度，搭载本体感知准直驱 Koala BEAR 执行器（关键关节液态冷却），采用可变周期 MPC 运控算法支持行走/跑步/跳跃等高动态行为，整机以商务采购渠道获取。
  ko: A 70 cm, 4.8 kg child-size bipedal humanoid platform co-developed by Westwood Robotics and UCLA RoMeLa, with 16 degrees
    of freedom, proprioceptive quasi-direct-drive Koala BEAR actuators with liquid cooling on key joints, and a variable-frequency
    MPC stack for highly dynamic walking, running and jumping.
domains:
- 02_components
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- system
- knowledge
tags:
- open_source
- humanoid_robot
- bruce
- westwood_robotics
- ucla_romela
- quasi_direct_drive
- liquid_cooling
- mpc
- high_dynamic_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/bruce-westwood.md（访问日期 2026-07-01）。官方宣称开源软件与模型，但整机控制框架的公开仓库在检索中未找到，整机开源程度存疑；价格约
    $6.5K 来自第三方论文对比表（ToddlerBot, arXiv:2502.00893 Table I），官方为询价制。 | WP4 trilingual backfill 2026-08-10: en body retranslated
    from zh deep-read (1566 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Westwood-Robotics GitHub Organization
  url: https://github.com/Westwood-Robotics
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BRUCE at World Robot Conference
  url: https://www.worldrobotconference.com/ex/product/244.html
  accessed_at: '2026-07-01'
- id: src_003
  type: website
  title: BRUCE on aparobot.com
  url: https://www.aparobot.com/robots/bruce
  accessed_at: '2026-07-01'
---
## 概述

BRUCE（Bipedal Robot Unit with Compliance Enhanced）是 Westwood Robotics（西木科技，2018 年由 UCLA RoMeLa 前核心成员创立）与 UCLA RoMeLa 联合开发的儿童尺寸双足人形平台，设计论文为 Liu et al., ICRA 2022。整机高 70 cm、重 4.8 kg，16 个自由度（每条腿 5、每条臂 3），是"能跑能跳"的少数派小型高动态双足平台（来源：调研档案 bruce-westwood.md，下同）。

开源情况需要说清楚：官方定位为"开放平台（open platform）"，宣称开源软件与模型，但整机控制框架的公开仓库在 GitHub 检索中未找到（截至 2026-07-01，未能直接验证其许可证条款）；组件级仓库（PyBEAR、BRUCE_SENSE、Wireless_ESTOP 等）开源于 `Westwood-Robotics` 组织。硬件成本方面，第三方论文对比表（ToddlerBot, arXiv:2502.00893 Table I）列为约 $6.5K 量级；官方页面为询价制，未公开标价，获取渠道为商务采购而非自助复刻。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 70 cm / 4.8 kg | WRC 展品页 / 第三方论文 |
| 自由度 | 16（腿 5×2、臂 3×2） | WRC 展品页 |
| 硬件成本 | 约 $6.5K 量级（第三方论文对比表）；官方询价制 | ToddlerBot 论文 Table I |
| 主控 | 算力 6 TOPS、8GB 内存、32GB 存储，支持主流深度学习框架 | 展品页口径 |
| 传感器 | 4 个足底接触传感器；6 轴 IMU，通信/采样速率 2 kHz | aparobot.com |
| 电池 | 3000 mAh，连续动态运行约 20 分钟；独立无线急停装置 | aparobot.com |
| 新手友好度 | 2 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- 自研 Koala BEAR 本体感知（proprioceptive）准直驱执行器：单台仅 250 g，峰值扭矩 10.5 N·m（腿部关节口径）；关键关节（膝等）采用液态冷却以支撑爆发力矩与持续高动态输出。
- 碳纤维复合材料骨架，拓扑优化，高度模块化，便于维修更换——技术血统与 UCLA ARTEMIS 的 BEAR 系列执行器一致（半直驱/QDD 路线）。

### 软件栈

- 可变周期（variable-frequency）MPC 运控算法，支持行走/跑步/跳跃等高动态行为；模型库与仿真环境被多篇第三方论文用作 benchmark（如 arXiv:2511.00840 的步态规划对比研究）。
- 官方宣称"开源软件和模型""积极迭代 GitHub Repo 和 Wiki"；实际公开内容以执行器（PyBEAR）、传感（BRUCE_SENSE）、无线急停等组件级仓库为主；无 ROS/ROS2 官方栈的公开证据。

### 适合人群

- 适合：高校实验室做高动态双足运控研究——70 cm / 4.8 kg 小体型 + 准直驱 + 液冷，BEAR 执行器与 MPC 栈对研究高动态运控的人很有价值；被多所欧美大学与研究公司采用（如 UCL）。
- 门槛：整机开源程度存疑（公开仓库只见组件级），个人无法自助复刻，只能商务采购；文档面向专业用户；不建议作为 0→1 首台机器人，新手可关注其开源组件（PyBEAR 等）学习准直驱执行器。

## 参考

- [Westwood-Robotics GitHub 组织（组件级开源仓库）](https://github.com/Westwood-Robotics)
- [WRC 展品页](https://www.worldrobotconference.com/ex/product/244.html)
- [aparobot.com 产品页](https://www.aparobot.com/robots/bruce)

## 개요

BRUCE(Bipedal Robot Unit with Compliance Enhanced)는 Westwood Robotics(서목과학기술, 2018년 UCLA RoMeLa 전 핵심 멤버들이 창립)와 UCLA RoMeLa가 공동 개발한 아동 사이즈 이족 보행 휴머노이드 플랫폼으로, 설계 논문은 Liu et al., ICRA 2022입니다. 전체 높이 70cm, 무게 4.8kg, 16자유도(다리 각 5, 팔 각 3)로, "달리고 점프할 수 있는" 소수 소형 고동적 이족 보행 플랫폼입니다(출처: 조사 파일 bruce-westwood.md, 이하 동일).

오픈소스 현황을 명확히 설명하자면: 공식적으로 "오픈 플랫폼(open platform)"으로定位되며, 소프트웨어와 모델을 오픈소스로 공개한다고 주장하지만, 전체 제어 프레임워크의 공개 저장소는 GitHub 검색에서 찾을 수 없습니다(2026-07-01 기준, 라이선스 조건을 직접 확인할 수 없음); 컴포넌트 수준 저장소(PyBEAR, BRUCE_SENSE, Wireless_ESTOP 등)는 `Westwood-Robotics` 조직 아래 오픈소스로 제공됩니다. 하드웨어 비용은 제3자 논문 비교표(ToddlerBot, arXiv:2502.00893 Table I)에서 약 $6.5K 수준으로 기재되어 있으며, 공식 페이지는 견적 문의 방식으로 공개 가격이 없으며, 획득 경로는 상업 구매이며 자체 복제가 아닙니다.

## 핵심 내용

### 주요 파라미터

| 항목 | 수치 | 출처 |
|---|---|---|
| 신장 / 무게 | 70 cm / 4.8 kg | WRC 전시품 페이지 / 제3자 논문 |
| 자유도 | 16(다리 5×2, 팔 3×2) | WRC 전시품 페이지 |
| 하드웨어 비용 | 약 $6.5K 수준(제3자 논문 비교표); 공식 견적 문의 방식 | ToddlerBot 논문 Table I |
| 메인 컨트롤러 | 연산 성능 6 TOPS, 8GB 메모리, 32GB 저장 공간, 주요 딥러닝 프레임워크 지원 | 전시품 페이지 기준 |
| 센서 | 발바닥 접촉 센서 4개; 6축 IMU, 통신/샘플링 속도 2 kHz | aparobot.com |
| 배터리 | 3000 mAh, 연속 동적 운행 약 20분; 독립 무선 긴급 정지 장치 | aparobot.com |
| 초보자 친화도 | 2 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 솔루션

- 자체 개발 Koala BEAR 고유 감각(proprioceptive) 준직구동 액추에이터: 단일 250g, 최대 토크 10.5 N·m(다리 관절 기준); 주요 관절(무릎 등)은 액체 냉각을 사용하여 폭발적인 토크와 지속적인 고동적 출력을 지원합니다.
- 탄소 섬유 복합 재료 프레임, 위상 최적화, 고도로 모듈화되어 유지보수 및 교체가 용이함——기술적 계보는 UCLA ARTEMIS의 BEAR 시리즈 액추에이터와 일치합니다(반직구동/QDD 경로).

### 소프트웨어 스택

- 가변 주기(variable-frequency) MPC 운동 제어 알고리즘, 보행/달리기/점프 등 고동적 행동 지원; 모델 라이브러리와 시뮬레이션 환경은 여러 제3자 논문에서 벤치마크로 사용됩니다(예: arXiv:2511.00840의 보행 계획 비교 연구).
- 공식적으로 "오픈소스 소프트웨어 및 모델", "GitHub Repo 및 Wiki 적극적 업데이트"를 주장하지만, 실제 공개 내용은 액추에이터(PyBEAR), 센싱(BRUCE_SENSE), 무선 긴급 정지 등 컴포넌트 수준 저장소가 주를 이룹니다; ROS/ROS2 공식 스택의 공개 증거는 없습니다.

### 적합한 대상

- 적합: 대학 연구실에서 고동적 이족 보행 운동 제어 연구——70cm / 4.8kg 소형 + 준직구동 + 액체 냉각, BEAR 액추에이터와 MPC 스택은 고동적 운동 제어 연구자에게 매우 가치 있음; 여러 유럽 및 미국 대학과 연구 회사에서 채택(예: UCL).
- 진입 장벽: 전체 기계의 오픈소스 정도가 의문(공개 저장소는 컴포넌트 수준만), 개인이 자체 복제 불가능, 상업 구매만 가능; 문서는 전문 사용자 대상; 0→1 첫 번째 로봇으로 권장되지 않으며, 초보자는 오픈소스 컴포넌트(PyBEAR 등)를 통해 준직구동 액추에이터를 학습할 수 있음.

## Overview

BRUCE (Bipedal Robot Unit with Compliance Enhanced) is a child-sized bipedal humanoid platform jointly developed by Westwood Robotics (founded in 2018 by former core members of UCLA RoMeLa) and UCLA RoMeLa, with the design paper by Liu et al., ICRA 2022. The robot stands 70 cm tall, weighs 4.8 kg, and has 16 degrees of freedom (5 per leg, 3 per arm), making it one of the few small-scale high-dynamic bipedal platforms capable of running and jumping (source: research archive bruce-westwood.md, same below).

The open-source status needs to be clarified: it is officially positioned as an "open platform," claiming open-source software and models, but the public repository for the full-robot control framework was not found in GitHub searches (as of 2026-07-01, its license terms could not be directly verified); component-level repositories (PyBEAR, BRUCE_SENSE, Wireless_ESTOP, etc.) are open-sourced under the `Westwood-Robotics` organization. Regarding hardware cost, a third-party paper comparison table (ToddlerBot, arXiv:2502.00893 Table I) lists it at approximately $6.5K; the official page uses an inquiry-based pricing model without public pricing, and the acquisition channel is commercial procurement rather than self-replication.

## Content

### Key Parameters

| Item | Value | Source |
|---|---|---|
| Height / Weight | 70 cm / 4.8 kg | WRC exhibit page / third-party paper |
| Degrees of Freedom | 16 (legs 5×2, arms 3×2) | WRC exhibit page |
| Hardware Cost | Approximately $6.5K (third-party paper comparison table); official inquiry-based pricing | ToddlerBot paper Table I |
| Main Controller | 6 TOPS compute, 8GB RAM, 32GB storage, supports mainstream deep learning frameworks | Exhibit page description |
| Sensors | 4 foot contact sensors; 6-axis IMU, communication/sampling rate 2 kHz | aparobot.com |
| Battery | 3000 mAh, approximately 20 minutes of continuous dynamic operation; independent wireless emergency stop device | aparobot.com |
| Beginner Friendliness | 2 / 5 (research archive assessment) | Research archive |

### Actuator Solution

- Self-developed Koala BEAR proprioceptive quasi-direct-drive actuators: only 250 g per unit, peak torque 10.5 N·m (leg joint specification); critical joints (such as knees) use liquid cooling to support burst torque and sustained high-dynamic output.
- Carbon fiber composite frame, topology-optimized, highly modular, easy to maintain and replace—technical lineage consistent with UCLA ARTEMIS's BEAR series actuators (semi-direct-drive/QDD approach).

### Software Stack

- Variable-frequency MPC motion control algorithm supporting high-dynamic behaviors such as walking, running, and jumping; the model library and simulation environment are used as benchmarks in multiple third-party papers (e.g., gait planning comparison study in arXiv:2511.00840).
- Officially claims "open-source software and models" and "actively iterating GitHub Repo and Wiki"; actual public content mainly consists of component-level repositories such as actuators (PyBEAR), sensing (BRUCE_SENSE), and wireless emergency stop; no public evidence of an official ROS/ROS2 stack.

### Suitable Audience

- Suitable for: university laboratories conducting high-dynamic bipedal motion control research—70 cm / 4.8 kg compact size + quasi-direct-drive + liquid cooling, with BEAR actuators and MPC stack being highly valuable for those researching high-dynamic motion control; adopted by multiple European and American universities and research companies (e.g., UCL).
- Barrier: the degree of full-robot open-sourcing is questionable (only component-level public repositories are visible), individuals cannot self-replicate and must procure commercially; documentation targets professional users; not recommended as a first 0→1 robot, but beginners can learn about quasi-direct-drive actuators from its open-source components (PyBEAR, etc.).
