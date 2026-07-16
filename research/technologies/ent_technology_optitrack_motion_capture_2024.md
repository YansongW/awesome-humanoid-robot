---
$id: ent_technology_optitrack_motion_capture_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: OptiTrack Motion Capture
  zh: OptiTrack 动作捕捉
  ko: OptiTrack 모션 캡처
summary:
  en: Optical marker-based motion-capture system for high-precision 3-D body tracking and robot retargeting.
  zh: 概述 OptiTrack 动作捕捉是人形机器人领域的重要technology。以下内容整理自项目 Wiki，供深入查阅。
  ko: 고정밀 3차원 신체 추적 및 로봇 리타게팅을 위한 광학 마커 기반 모션 캡처 시스템.
domains:
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- motion_capture
- optical
- optitrack
- retargeting
- technology
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_optitrack_motive_system.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: OptiTrack Motion Capture
  url: https://www.optitrack.com/
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
OptiTrack 动作捕捉是人形机器人领域的重要技术。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## OptiTrack 运动捕捉系统 / OptiTrack Motion Capture System

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [OptiTrack](../companies/company_optitrack.md) |
| **产品类别** | 光学动作捕捉系统 |
| **发布时间** | PrimeX 系列持续在售；Motive 3 现行 |
| **状态** | 量产/商用 |
| **官网/来源** | [OptiTrack 相机产品页](https://optitrack.com/cameras/) |

### 产品概述

OptiTrack 运动捕捉系统由 PrimeX 系列红外相机、Motive 追踪软件与主动/被动标记点组成，可在室内环境下实现亚毫米级、低延迟的 6DoF 位姿追踪。该系统广泛应用于人形机器人运动验证、遥操作训练、步态分析、无人机/AGV 定位标定以及影视动画制作。

### 产品图片

> OptiTrack 运动捕捉系统：请访问 [官方资料](https://optitrack.com/cameras/) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系统组成 | PrimeX 相机 + Motive 软件 + 标记点 | 官网 |
| 代表相机 | PrimeX 13（1.3 MP）、PrimeX 41（2048×2048） | 产品页 |
| 追踪精度 | 亚毫米级（未公开精确值） | 公开资料 |
| 延迟 | 低至数毫秒级 | 产品页 |
| 最大帧率 | PrimeX 13：240 fps；PrimeX 41：180 fps | 产品页 |
| 视场角 | 未公开 | 产品页 |
| 同步方式 | eSync / 以太网 | 产品页 |
| 软件接口 | Motive 3、C/C++ SDK、Python、ROS、VRPN | 官网 |
| 工作距离 | 未公开 | 产品页 |
| 价格 | 未公开 | 商务报价 |

### 供应链位置

- **制造商**：[OptiTrack](../companies/company_optitrack.md)
- **核心零部件/技术来源**：红外图像传感器、光学镜头、FPGA/处理芯片、红外照明、校准算法、网络同步与 3D 解算软件
- **下游应用/客户**：影视动画公司、机器人/无人机研发团队、高校与科研院所、体育/康复机构

### 知识图谱节点与关系

- 产品实体：`ent_product_optitrack_motive_system`
- 零部件实体：`ent_component_optitrack_motive_system_core`
- 制造商实体：`ent_company_optitrack`
- 关键关系：
  - `rel_ent_company_optitrack_manufactures_ent_product_optitrack_motive_system`（`ent_company_optitrack` → `manufactures` → `ent_product_optitrack_motive_system`）
  - `rel_ent_company_optitrack_manufactures_ent_component_optitrack_motive_system_core`（`ent_company_optitrack` → `manufactures` → `ent_component_optitrack_motive_system_core`）
  - `rel_ent_product_optitrack_motive_system_uses_ent_component_optitrack_motive_system_core`（`ent_product_optitrack_motive_system` → `uses` → `ent_component_optitrack_motive_system_core`）

### 应用场景

- **人形机器人运动标定**：捕捉全身关节轨迹，验证运动规划与控制算法。
- **遥操作训练**：记录操作员手部/身体动作，用于训练遥操作策略。
- **无人机/AGV 定位验证**：提供高精度 ground truth，评估 SLAM 与定位算法。
- **影视动画与游戏**：角色动作采集与实时虚拟制作。

### 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 光学红外动作捕捉 | Vicon Vero/Vantage | Qualisys Miqus/Arqus |
| 精度 | 亚毫米级 | 亚毫米级 | 亚毫米级 |
| 延迟 | 低延迟 | 低延迟 | 低延迟 |
| 价格 | 未公开 | 高端 | 高端 |

### 选购与部署建议

- 根据捕捉空间大小与精度需求选择相机数量与型号。
- 确保场地具备可控的红外反射条件，避免阳光与强红外干扰。
- 部署前进行系统校准，并验证 SDK 与目标软件栈的接口兼容性。

### 相关词条

- [制造商：OptiTrack](../companies/company_optitrack.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

### 参考资料

1. [OptiTrack 官网](https://optitrack.com)
2. [OptiTrack 相机产品页](https://optitrack.com/cameras/)
3. Motive 软件文档与公开技术资料
4. [附录 D 企业目录](../index-companies.md)

## 参考
- [OptiTrack Motion Capture](https://www.optitrack.com/)
- 项目 Wiki：appendix-d/products/product_optitrack_motive_system.md

## Overview
OptiTrack motion capture is a key technology in the humanoid robotics field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## OptiTrack Motion Capture System

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [OptiTrack](../companies/company_optitrack.md) |
| **Product Category** | Optical Motion Capture System |
| **Release Date** | PrimeX series continuously available; Motive 3 current |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [OptiTrack Camera Product Page](https://optitrack.com/cameras/) |

### Product Overview

The OptiTrack motion capture system consists of PrimeX series infrared cameras, Motive tracking software, and active/passive markers, enabling sub-millimeter, low-latency 6DoF pose tracking in indoor environments. This system is widely used in humanoid robot motion validation, teleoperation training, gait analysis, drone/AGV positioning calibration, and film/animation production.

### Product Image

> OptiTrack Motion Capture System: Please visit the [official page](https://optitrack.com/cameras/) for details.

### Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| System Composition | PrimeX cameras + Motive software + markers | Official website |
| Representative Camera | PrimeX 13 (1.3 MP), PrimeX 41 (2048×2048) | Product page |
| Tracking Accuracy | Sub-millimeter (exact value not disclosed) | Public information |
| Latency | As low as a few milliseconds | Product page |
| Maximum Frame Rate | PrimeX 13: 240 fps; PrimeX 41: 180 fps | Product page |
| Field of View | Not disclosed | Product page |
| Synchronization Method | eSync / Ethernet | Product page |
| Software Interface | Motive 3, C/C++ SDK, Python, ROS, VRPN | Official website |
| Working Distance | Not disclosed | Product page |
| Price | Not disclosed | Business quotation |

### Supply Chain Position

- **Manufacturer**: [OptiTrack](../companies/company_optitrack.md)
- **Core Components/Technology Sources**: Infrared image sensors, optical lenses, FPGA/processing chips, infrared illumination, calibration algorithms, network synchronization, and 3D solving software
- **Downstream Applications/Customers**: Film/animation companies, robotics/drone R&D teams, universities and research institutes, sports/rehabilitation institutions

### Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_optitrack_motive_system`
- Component Entity: `ent_component_optitrack_motive_system_core`
- Manufacturer Entity: `ent_company_optitrack`
- Key Relationships:
  - `rel_ent_company_optitrack_manufactures_ent_product_optitrack_motive_system` (`ent_company_optitrack` → `manufactures` → `ent_product_optitrack_motive_system`)
  - `rel_ent_company_optitrack_manufactures_ent_component_optitrack_motive_system_core` (`ent_company_optitrack` → `manufactures` → `ent_component_optitrack_motive_system_core`)
  - `rel_ent_product_optitrack_motive_system_uses_ent_component_optitrack_motive_system_core` (`ent_product_optitrack_motive_system` → `uses` → `ent_component_optitrack_motive_system_core`)

### Application Scenarios

- **Humanoid Robot Motion Calibration**: Capture full-body joint trajectories to validate motion planning and control algorithms.
- **Teleoperation Training**: Record operator hand/body movements for training teleoperation strategies.
- **Drone/AGV Positioning Validation**: Provide high-precision ground truth to evaluate SLAM and positioning algorithms.
- **Film/Animation and Gaming**: Character motion capture and real-time virtual production.

### Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | Optical infrared motion capture | Vicon Vero/Vantage | Qualisys Miqus/Arqus |
| Accuracy | Sub-millimeter | Sub-millimeter | Sub-millimeter |
| Latency | Low latency | Low latency | Low latency |
| Price | Not disclosed | High-end | High-end |

### Selection and Deployment Recommendations

- Choose the number and model of cameras based on capture space size and accuracy requirements.
- Ensure the venue has controllable infrared reflection conditions, avoiding sunlight and strong infrared interference.
- Perform system calibration before deployment and verify interface compatibility between the SDK and the target software stack.

### Related Entries

- [Manufacturer: OptiTrack](../companies/company_optitrack.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

### References

1. [OptiTrack Official Website](https://optitrack.com)
2. [OptiTrack Camera Product Page](https://optitrack.com/cameras/)
3. Motive software documentation and public technical materials
4. [Appendix D Company Directory](../index-companies.md)

## 개요
OptiTrack 모션 캡처는 휴머노이드 로봇 분야의 중요한 기술입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## OptiTrack 모션 캡처 시스템 / OptiTrack Motion Capture System

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [OptiTrack](../companies/company_optitrack.md) |
| **제품 카테고리** | 광학 모션 캡처 시스템 |
| **출시일** | PrimeX 시리즈 지속 판매 중; Motive 3 현재 버전 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [OptiTrack 카메라 제품 페이지](https://optitrack.com/cameras/) |

### 제품 개요

OptiTrack 모션 캡처 시스템은 PrimeX 시리즈 적외선 카메라, Motive 추적 소프트웨어 및 능동/수동 마커 포인트로 구성되어 실내 환경에서 서브밀리미터급, 저지연 6DoF 자세 추적을 구현합니다. 이 시스템은 휴머노이드 로봇 동작 검증, 원격 조작 훈련, 보행 분석, 드론/AGV 위치 보정 및 영화/애니메이션 제작에 널리 사용됩니다.

### 제품 이미지

> OptiTrack 모션 캡처 시스템: [공식 자료](https://optitrack.com/cameras/)를 방문하여 확인하세요.

### 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 시스템 구성 | PrimeX 카메라 + Motive 소프트웨어 + 마커 포인트 | 공식 사이트 |
| 대표 카메라 | PrimeX 13 (1.3 MP), PrimeX 41 (2048×2048) | 제품 페이지 |
| 추적 정밀도 | 서브밀리미터급 (정확한 값 미공개) | 공개 자료 |
| 지연 시간 | 수 밀리초 수준 | 제품 페이지 |
| 최대 프레임 속도 | PrimeX 13: 240 fps; PrimeX 41: 180 fps | 제품 페이지 |
| 시야각 | 미공개 | 제품 페이지 |
| 동기화 방식 | eSync / 이더넷 | 제품 페이지 |
| 소프트웨어 인터페이스 | Motive 3, C/C++ SDK, Python, ROS, VRPN | 공식 사이트 |
| 작업 거리 | 미공개 | 제품 페이지 |
| 가격 | 미공개 | 비즈니스 견적 |

### 공급망 위치

- **제조사**: [OptiTrack](../companies/company_optitrack.md)
- **핵심 부품/기술 출처**: 적외선 이미지 센서, 광학 렌즈, FPGA/처리 칩, 적외선 조명, 보정 알고리즘, 네트워크 동기화 및 3D 해석 소프트웨어
- **하류 응용/고객**: 영화/애니메이션 회사, 로봇/드론 연구팀, 대학 및 연구 기관, 스포츠/재활 기관

### 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_optitrack_motive_system`
- 부품 엔터티: `ent_component_optitrack_motive_system_core`
- 제조사 엔터티: `ent_company_optitrack`
- 주요 관계:
  - `rel_ent_company_optitrack_manufactures_ent_product_optitrack_motive_system` (`ent_company_optitrack` → `manufactures` → `ent_product_optitrack_motive_system`)
  - `rel_ent_company_optitrack_manufactures_ent_component_optitrack_motive_system_core` (`ent_company_optitrack` → `manufactures` → `ent_component_optitrack_motive_system_core`)
  - `rel_ent_product_optitrack_motive_system_uses_ent_component_optitrack_motive_system_core` (`ent_product_optitrack_motive_system` → `uses` → `ent_component_optitrack_motive_system_core`)

### 응용 시나리오

- **휴머노이드 로봇 동작 보정**: 전신 관절 궤적을 캡처하여 동작 계획 및 제어 알고리즘 검증.
- **원격 조작 훈련**: 운영자의 손/신체 동작을 기록하여 원격 조작 전략 훈련.
- **드론/AGV 위치 검증**: 고정밀 ground truth 제공, SLAM 및 위치 알고리즘 평가.
- **영화/애니메이션 및 게임**: 캐릭터 동작 캡처 및 실시간 가상 제작.

### 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 광학 적외선 모션 캡처 | Vicon Vero/Vantage | Qualisys Miqus/Arqus |
| 정밀도 | 서브밀리미터급 | 서브밀리미터급 | 서브밀리미터급 |
| 지연 시간 | 저지연 | 저지연 | 저지연 |
| 가격 | 미공개 | 고급형 | 고급형 |

### 구매 및 배포 권장 사항

- 캡처 공간 크기와 정밀도 요구 사항에 따라 카메라 수와 모델을 선택하세요.
- 현장에 통제 가능한 적외선 반사 조건을 확보하고, 햇빛과 강한 적외선 간섭을 피하세요.
- 배포 전 시스템 보정을 수행하고 SDK와 대상 소프트웨어 스택의 인터페이스 호환성을 확인하세요.

### 관련 항목

- [제조사: OptiTrack](../companies/company_optitrack.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

### 참고 자료

1. [OptiTrack 공식 사이트](https://optitrack.com)
2. [OptiTrack 카메라 제품 페이지](https://optitrack.com/cameras/)
3. Motive 소프트웨어 문서 및 공개 기술 자료
4. [부록 D 기업 목록](../index-companies.md)
