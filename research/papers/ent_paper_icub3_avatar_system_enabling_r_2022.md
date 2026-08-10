---
$id: ent_paper_icub3_avatar_system_enabling_r_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots'
  zh: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots'
  ko: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots'
summary:
  en: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots is a 2022 work on teleoperation
    for humanoid robots, with open-source code available.'
  zh: iCub3 Avatar System 是意大利技术研究院（IIT）于2022年提出的远程全沉浸式人形机器人具身系统。该系统通过集成视觉、听觉、触觉等多模态反馈，使操作者能够远程控制iCub3机器人完成行走、操作、语音和面部表情等复杂交互。核心贡献在于实现了290公里外的威尼斯艺术展远程参观和300公里外舞台协作等真实场景验证。
  ko: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots is a 2022 work on teleoperation
    for humanoid robots, with open-source code available.'
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
- icub3_avatar_system
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.06972v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (837 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2203.06972
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots project page'
  url: https://www.science.org/doi/10.1126/scirobotics.adh3834
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
该系统基于iCub系列十五年的技术积累，构建了支持全身运动控制与多模态感知反馈的通用化具身架构。操作者可通过头戴显示器、力反馈手套等设备获得视觉、听觉、触觉、重量感和触摸感等全方位反馈，同时远程控制机器人完成行走、抓取、语音对话和面部表情同步。系统在三个真实场景中完成验证：威尼斯双年展的远程艺术展参观（操作者在热那亚，距离290公里）、We Make Future数字创新节的舞台协作（操作者在热那亚，距离300公里，与2000名观众互动），以及ANA Avatar XPrize竞赛的参赛架构。

## 核心内容
### 系统架构
- **机器人平台**：iCub3 是IIT开发的第三代iCub人形机器人，集成了约15年的技术迭代成果
- **操作端**：操作者佩戴VR头显、力反馈手套和全身运动追踪设备
- **反馈模态**：视觉（立体摄像头）、听觉（双耳麦克风）、触觉（指尖压力传感器）、重量感（关节力矩反馈）、触摸感（全身皮肤传感器）
- **控制通道**：支持行走、抓取、语音合成/识别、面部表情同步

### 实验验证
1. **威尼斯双年展远程参观**（2022年）
   - 操作者位于热那亚，机器人位于威尼斯，距离约290公里
   - 实现远程艺术展览的语音讲解、手势交流和非语言互动
   - 网络延迟控制在可接受范围内

2. **We Make Future 舞台协作**（2022年）
   - 操作者在热那亚，机器人在里米尼，距离约300公里
   - 机器人接收观众委托的载荷并搬运至舞台指定位置
   - 现场约2000名观众观看实时交互演示

3. **ANA Avatar XPrize 竞赛架构**
   - 由iCub团队专门优化的参赛版本
   - 侧重远程操作精度和任务完成效率

### 关键参数
- 远程操作距离：290-300公里
- 交互类型：言语交流、非语言手势、物理协作
- 公开代码：项目代码已开源

## Overview
We present an avatar system designed to facilitate the embodiment of humanoid robots by human operators, validated through iCub3, a humanoid developed at the Istituto Italiano di Tecnologia (IIT). More precisely, the contribution of the paper is twofold: first, we present the humanoid iCub3 as a robotic avatar which integrates the latest significant improvements after about fifteen years of development of the iCub series; second, we present a versatile avatar system enabling humans to embody humanoid robots encompassing aspects such as locomotion, manipulation, voice, and face expressions with comprehensive sensory feedback including visual, auditory, haptic, weight, and touch modalities. We validate the system by implementing several avatar architecture instances, each tailored to specific requirements. First, we evaluated the optimized architecture for verbal, non-verbal, and physical interactions with a remote recipient. This testing involved the operator in Genoa and the avatar in the Biennale di Venezia, Venice - about 290 Km away - thus allowing the operator to visit remotely the Italian art exhibition. Second, we evaluated the optimised architecture for recipient physical collaboration and public engagement on-stage, live, at the We Make Future show, a prominent world digital innovation festival. In this instance, the operator was situated in Genoa while the avatar operates in Rimini - about 300 Km away - interacting with a recipient who entrusted the avatar a payload to carry on stage before an audience of approximately 2000 spectators. Third, we present the architecture implemented by the iCub Team for the ANA Avatar XPrize competition.

## 参考
- http://arxiv.org/abs/2203.06972v2

## 개요
이 시스템은 iCub 시리즈의 15년 기술 축적을 기반으로, 전신 운동 제어와 다중 감각 피드백을 지원하는 범용적 구현 아키텍처를 구축했습니다. 조작자는 헤드 마운트 디스플레이, 힘 피드백 장갑 등의 장치를 통해 시각, 청각, 촉각, 무게감, 접촉감 등 전방위 피드백을 얻을 수 있으며, 동시에 원격으로 로봇을 제어하여 보행, 파지, 음성 대화, 표정 동기화를 완료할 수 있습니다. 시스템은 세 가지 실제 시나리오에서 검증을 완료했습니다: 베네치아 비엔날레의 원격 예술 전시 관람(조작자는 제노바, 거리 290km), We Make Future 디지털 혁신 페스티벌의 무대 협업(조작자는 제노바, 거리 300km, 2000명의 관객과 상호작용), 그리고 ANA Avatar XPrize 대회의 참가 아키텍처입니다.

## 핵심 내용
### 시스템 아키텍처
- **로봇 플랫폼**: iCub3는 IIT가 개발한 3세대 iCub 휴머노이드 로봇으로, 약 15년간의 기술 반복 성과를 통합했습니다
- **조작 단말**: 조작자는 VR 헤드셋, 힘 피드백 장갑, 전신 모션 추적 장치를 착용합니다
- **피드백 모달리티**: 시각(스테레오 카메라), 청각(바이노럴 마이크), 촉각(손끝 압력 센서), 무게감(관절 토크 피드백), 접촉감(전신 피부 센서)
- **제어 채널**: 보행, 파지, 음성 합성/인식, 표정 동기화 지원

### 실험 검증
1. **베네치아 비엔날레 원격 관람** (2022년)
   - 조작자는 제노바에, 로봇은 베네치아에 위치, 거리 약 290km
   - 원격 예술 전시의 음성 설명, 제스처 소통, 비언어적 상호작용 구현
   - 네트워크 지연은 허용 가능한 범위 내로 제어

2. **We Make Future 무대 협업** (2022년)
   - 조작자는 제노바에, 로봇은 리미니에 위치, 거리 약 300km
   - 로봇이 관객이 위탁한 하중을 받아 무대 지정 위치로 운반
   - 현장 약 2000명의 관객이 실시간 상호작용 시연 관람

3. **ANA Avatar XPrize 대회 아키텍처**
   - iCub 팀이 특별히 최적화한 참가 버전
   - 원격 조작 정밀도와 작업 완료 효율성에 중점

### 핵심 매개변수
- 원격 조작 거리: 290-300km
- 상호작용 유형: 언어적 소통, 비언어적 제스처, 물리적 협업
- 공개 코드: 프로젝트 코드는 오픈소스로 공개됨
