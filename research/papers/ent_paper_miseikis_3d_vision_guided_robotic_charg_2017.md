---
$id: ent_paper_miseikis_3d_vision_guided_robotic_charg_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid Vehicles
  zh: 面向电动和插电式混合动力汽车的3D视觉引导机器人充电站
  ko: 전기 및 플러그인 하이브리드 차량을 위한 3D 비전 기반 로봇 충전 스테이션
summary:
  en: This 2017 arXiv paper presents an automated robotic charging station that uses a stereo-camera 3D vision system, shape-based
    matching, and a UR10 arm to locate and plug into EV/PHEV charging ports without vehicle modification.
  zh: 本文提出一种基于3D视觉引导的自动机器人充电站，使用立体相机、形状匹配算法和UR10机械臂，无需改装车辆即可定位并插入电动汽车/插电式混合动力汽车充电接口。核心贡献在于通过形状匹配实现充电口位姿精确识别，并利用连接器插头结构完成相机-机器人系统标定。
  ko: 이 2017년 arXiv 논문은 스테레오 카메라 3D 비전 시스템, 형상 기반 매칭 및 UR10 로봇 암을 사용하여 차량을 개조하지 않고도 EV/PHEV 충전 포트를 찾아 연결하는 자동 로봇 충전 스테이션을
    제시한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- robotic_charging
- ev_charging
- 3d_vision
- stereo_vision
- shape_based_matching
- visual_servoing
- hand_eye_calibration
- markerless_calibration
- force_monitored_insertion
- plug_insertion
- ur10
- contact_rich_manipulation
- manipulation_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1703.05381v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (604 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 3D Vision Guided Robotic Charging Station for Electric and Plug-in Hybrid Vehicles
  url: https://arxiv.org/abs/1703.05381
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该2017年arXiv论文针对电动汽车充电不便的问题，设计了一套全自动机器人充电系统。系统由立体相机3D视觉模块、UR10协作机器人和充电站组成，通过形状匹配算法识别充电口并获取精确位姿，无需车辆预装特殊标记。标定过程利用充电插头自身结构完成，避免了额外标定物。机器人采用三步运动规划策略完成插拔动作，实验验证了系统有效性。

## 核心内容
### 系统架构
- 硬件组成：立体相机3D视觉系统 + UR10六轴协作机器人 + 充电站
- 核心流程：视觉定位 → 位姿解算 → 机器人运动规划 → 插拔执行

### 视觉定位方法
- 采用形状匹配（shape-based matching）算法识别充电口
- 通过立体相机获取3D点云数据，计算充电口精确六自由度位姿
- 无需车辆改装或额外标记，仅依赖充电口几何特征

### 标定方案
- 利用充电连接器插头的已知结构完成相机-机器人手眼标定
- 无需棋盘格或标定板，简化部署流程

### 运动规划策略
- 三步插接流程：
  1. 粗定位：基于视觉引导将机械臂移至充电口附近
  2. 精对准：通过力/位混合控制调整末端姿态
  3. 插接执行：沿充电口轴向完成插入动作

### 实验验证
- 在真实充电场景中完成多组插拔测试
- 成功实现自动插拔，未报告具体成功率数值
- 系统响应时间与定位精度受限于立体相机性能（未提供具体参数）

## Overview
Electric vehicles (EVs) and plug-in hybrid vehicles (PHEVs) are rapidly gaining popularity on our roads. Besides a comparatively high purchasing price, the main two problems limiting their use are the short driving range and inconvenient charging process. In this paper we address the following by presenting an automatic robot-based charging station with 3D vision guidance for plugging and unplugging the charger. First of all, the whole system concept consisting of a 3D vision system, an UR10 robot and a charging station is presented. Then we show the shape-based matching methods used to successfully identify and get the exact pose of the charging port. The same approach is used to calibrate the camera-robot system by using just known structure of the connector plug and no additional markers. Finally, a three-step robot motion planning procedure for plug-in is presented and functionality is demonstrated in a series of successful experiments.

## 参考
- http://arxiv.org/abs/1703.05381v1

## 개요
이 2017년 arXiv 논문은 전기차 충전의 불편함을 해결하기 위해 완전 자동 로봇 충전 시스템을 설계했다. 시스템은 스테레오 카메라 3D 비전 모듈, UR10 협동 로봇, 충전 스테이션으로 구성되며, 형상 매칭 알고리즘을 통해 충전 포트를 인식하고 정밀한 자세를 획득하여 차량에 사전 설치된 특수 마커가 필요 없다. 캘리브레이션 과정은 충전 플러그 자체의 구조를 활용하여 추가 캘리브레이션 대상물을 피한다. 로봇은 3단계 운동 계획 전략으로 삽입 및 분리 동작을 수행하며, 실험을 통해 시스템 유효성을 검증했다.

## 핵심 내용
### 시스템 아키텍처
- 하드웨어 구성: 스테레오 카메라 3D 비전 시스템 + UR10 6축 협동 로봇 + 충전 스테이션
- 핵심 프로세스: 비전 위치 확인 → 자세 계산 → 로봇 운동 계획 → 삽입 및 분리 실행

### 비전 위치 확인 방법
- 형상 기반 매칭(shape-based matching) 알고리즘을 사용하여 충전 포트 인식
- 스테레오 카메라로 3D 포인트 클라우드 데이터를 획득하여 충전 포트의 정밀한 6자유도 자세 계산
- 차량 개조나 추가 마커 불필요, 충전 포트의 기하학적 특징에만 의존

### 캘리브레이션 방안
- 충전 커넥터 플러그의 알려진 구조를 활용하여 카메라-로봇 핸드아이 캘리브레이션 완료
- 체커보드나 캘리브레이션 보드 불필요, 배포 프로세스 간소화

### 운동 계획 전략
- 3단계 삽입 프로세스:
  1. 대략적 위치 확인: 비전 유도로 로봇 팔을 충전 포트 근처로 이동
  2. 정밀 정렬: 힘/위치 혼합 제어로 말단 자세 조정
  3. 삽입 실행: 충전 포트 축 방향을 따라 삽입 동작 완료

### 실험 검증
- 실제 충전 시나리오에서 여러 그룹의 삽입 및 분리 테스트 수행
- 자동 삽입 및 분리 성공, 구체적인 성공률 수치는 보고되지 않음
- 시스템 응답 시간과 위치 정밀도는 스테레오 카메라 성능에 제한됨(구체적 파라미터 미제공)
