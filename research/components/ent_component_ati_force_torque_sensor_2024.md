---
$id: ent_component_ati_force_torque_sensor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: ATI Force Torque Sensor
  zh: ATI 力/力矩传感器
  ko: ATI 힘/토크 센서
summary:
  en: Wrist and ankle force/torque sensor for contact control and interaction.
  zh: OnRobot HEX-E QC 六维力/力矩传感器 / OnRobot HEX-E QC 6-Axis Force/Torque Sensor
  ko: 접촉 제어 및 상호작용을 위한 손목 및 발목 힘/토크 센서.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- ankle
- ati
- component
- force_torque
- sensor
- wrist
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_onrobot_hex_e.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: ATI Force Torque Sensor
  url: https://www.ati-ia.com/
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
ATI 力/力矩传感器是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## OnRobot HEX-E QC 六维力/力矩传感器 / OnRobot HEX-E QC 6-Axis Force/Torque Sensor

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [OnRobot（昂乐） / OnRobot](../companies/company_onrobot.md) |
| **产品类别** | 协作机器人六维力/力矩传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [OnRobot HEX-E QC 六维力/力矩传感器 产品/资料页](https://www.onrobot.com/en/products/he-x) |

### 产品概述

HEX-E QC 是 OnRobot 为协作机器人末端设计的六维力/力矩传感器，集成 Quick Changer 快换接口，支持即插即用安装。它可实时测量六维力/力矩数据，帮助机器人完成精密装配、恒力抛光、表面处理和碰撞检测。

### 产品图片

> OnRobot HEX-E QC 六维力/力矩传感器：请访问 [官方资料](https://www.onrobot.com/en/products/he-x) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 六维力/力矩传感器 | 官网 |
| 力测量范围（Fx/Fy/Fz） | ±100 N / ±100 N / ±200 N | 官网/datasheet |
| 力矩测量范围（Mx/My/Mz） | ±10 Nm / ±10 Nm / ±10 Nm | 官网/datasheet |
| 精度 | 未公开 | - |
| 分辨率 | 未公开 | - |
| 采样频率 | 未公开 | - |
| 过载能力 | 约 500% FS | 官网/datasheet |
| 防护等级 | IP67 | 官网/datasheet |
| 通信接口 | TCP/IP、USB、EtherNet/IP、PROFINET | 官网/datasheet |
| 集成接口 | Quick Changer / 机器人法兰 | 官网/datasheet |
| 供电 | 24 V DC | 官网/datasheet |
| 重量 | 约 350 g | 官网/datasheet |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[OnRobot（昂乐） / OnRobot](../companies/company_onrobot.md)
- **核心零部件/技术来源**：自研力觉传感单元、信号处理与通信电路、Quick Changer 机械接口、工业级密封外壳。
- **下游应用/客户**：协作机器人 OEM、汽车与电子制造商、人形机器人整机厂、自动化系统集成商。

### 知识图谱节点与关系

- 产品实体：`ent_product_onrobot_hex_e`
- 零部件实体：`ent_component_onrobot_hex_e_sensor`
- 制造商实体：`ent_company_onrobot`
- 关键关系：
  - `rel_ent_company_onrobot_manufactures_ent_product_onrobot_hex_e`（`ent_company_onrobot` → `manufactures` → `ent_product_onrobot_hex_e`）
  - `rel_ent_company_onrobot_manufactures_ent_component_onrobot_hex_e_sensor`（`ent_company_onrobot` → `manufactures` → `ent_component_onrobot_hex_e_sensor`）
  - `rel_ent_product_onrobot_hex_e_uses_ent_component_onrobot_hex_e_sensor`（`ent_product_onrobot_hex_e` → `uses` → `ent_component_onrobot_hex_e_sensor`）

### 应用场景

- **力控装配**：精密插件、齿轮装配中的柔顺插入与定位。
- **恒力打磨/抛光**：保持恒定接触力，提高表面质量一致性。
- **插拔与测试**：连接器、开关等零部件的力-位移测试。
- **人形机器人手臂**：末端六维力觉用于抓取与交互。

### 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 协作机器人六维力传感器 | ATI Nano25 | Bota Systems SensONE |
| 力范围 | ±100 N / ±200 N | ±250 N / ±1000 N | ±200 N / ±500 N |
| 通信 | TCP/IP/USB/EtherNet/IP | 模拟/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |
| 核心优势 | 快换集成、生态成熟 | 极小尺寸、高过载 | 紧凑高性价比 |

### 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

### 相关词条

- [制造商：OnRobot（昂乐） / OnRobot](../companies/company_onrobot.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

### 参考资料

1. [OnRobot 官网](https://www.onrobot.com)
2. [OnRobot HEX-E QC 六维力/力矩传感器 产品/资料页](https://www.onrobot.com/en/products/he-x)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../index-companies.md)

## 参考
- [ATI Force Torque Sensor](https://www.ati-ia.com/)
- 项目 Wiki：appendix-d/products/product_onrobot_hex_e.md

## Overview
ATI force/torque sensors are important components in the humanoid robotics field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## OnRobot HEX-E QC 6-Axis Force/Torque Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [OnRobot](../companies/company_onrobot.md) |
| **Product Category** | Collaborative robot 6-axis force/torque sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [OnRobot HEX-E QC 6-Axis Force/Torque Sensor Product/Data Page](https://www.onrobot.com/en/products/he-x) |

### Product Overview

The HEX-E QC is a 6-axis force/torque sensor designed by OnRobot for collaborative robot end-effectors, integrating a Quick Changer interface for plug-and-play installation. It measures 6-axis force/torque data in real time, enabling robots to perform precision assembly, constant-force polishing, surface finishing, and collision detection.

### Product Image

> OnRobot HEX-E QC 6-Axis Force/Torque Sensor: Please visit the [official page](https://www.onrobot.com/en/products/he-x) for details.

### Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | 6-axis force/torque sensor | Official website |
| Force measurement range (Fx/Fy/Fz) | ±100 N / ±100 N / ±200 N | Official website/datasheet |
| Torque measurement range (Mx/My/Mz) | ±10 Nm / ±10 Nm / ±10 Nm | Official website/datasheet |
| Accuracy | Not disclosed | - |
| Resolution | Not disclosed | - |
| Sampling frequency | Not disclosed | - |
| Overload capacity | Approx. 500% FS | Official website/datasheet |
| Protection rating | IP67 | Official website/datasheet |
| Communication interface | TCP/IP, USB, EtherNet/IP, PROFINET | Official website/datasheet |
| Integration interface | Quick Changer / Robot flange | Official website/datasheet |
| Power supply | 24 V DC | Official website/datasheet |
| Weight | Approx. 350 g | Official website/datasheet |
| Operating temperature | Not disclosed | - |
| Price | Not disclosed | - |

### Supply Chain Position

- **Manufacturer**: [OnRobot](../companies/company_onrobot.md)
- **Core components/technology source**: Self-developed force sensing unit, signal processing and communication circuit, Quick Changer mechanical interface, industrial-grade sealed housing.
- **Downstream applications/customers**: Collaborative robot OEMs, automotive and electronics manufacturers, humanoid robot integrators, automation system integrators.

### Knowledge Graph Nodes and Relationships

- Product entity: `ent_product_onrobot_hex_e`
- Component entity: `ent_component_onrobot_hex_e_sensor`
- Manufacturer entity: `ent_company_onrobot`
- Key relationships:
  - `rel_ent_company_onrobot_manufactures_ent_product_onrobot_hex_e` (`ent_company_onrobot` → `manufactures` → `ent_product_onrobot_hex_e`)
  - `rel_ent_company_onrobot_manufactures_ent_component_onrobot_hex_e_sensor` (`ent_company_onrobot` → `manufactures` → `ent_component_onrobot_hex_e_sensor`)
  - `rel_ent_product_onrobot_hex_e_uses_ent_component_onrobot_hex_e_sensor` (`ent_product_onrobot_hex_e` → `uses` → `ent_component_onrobot_hex_e_sensor`)

### Application Scenarios

- **Force-controlled assembly**: Compliant insertion and positioning in precision plug-in and gear assembly.
- **Constant-force grinding/polishing**: Maintains constant contact force to improve surface quality consistency.
- **Insertion and testing**: Force-displacement testing of connectors, switches, and other components.
- **Humanoid robot arms**: End-effector 6-axis force sensing for grasping and interaction.

### Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | Collaborative robot 6-axis force sensor | ATI Nano25 | Bota Systems SensONE |
| Force range | ±100 N / ±200 N | ±250 N / ±1000 N | ±200 N / ±500 N |
| Communication | TCP/IP/USB/EtherNet/IP | Analog/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |
| Core advantage | Quick-change integration, mature ecosystem | Extremely compact size, high overload | Compact and cost-effective |

### Selection and Deployment Recommendations

- Choose a specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Before deployment, confirm that the interface, power supply, cooling, mechanical mounting, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

### Related Entries

- [Manufacturer: OnRobot](../companies/company_onrobot.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

### References

1. [OnRobot Official Website](https://www.onrobot.com)
2. [OnRobot HEX-E QC 6-Axis Force/Torque Sensor Product/Data Page](https://www.onrobot.com/en/products/he-x)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)

## 개요
ATI 힘/토크 센서는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 자세한 참고를 위해 제공됩니다.

## 핵심 내용
## OnRobot HEX-E QC 6축 힘/토크 센서 / OnRobot HEX-E QC 6-Axis Force/Torque Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [OnRobot (온로봇) / OnRobot](../companies/company_onrobot.md) |
| **제품 카테고리** | 협동 로봇용 6축 힘/토크 센서 |
| **출시일** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [OnRobot HEX-E QC 6축 힘/토크 센서 제품/자료 페이지](https://www.onrobot.com/en/products/he-x) |

### 제품 개요

HEX-E QC는 OnRobot이 협동 로봇 엔드 이펙터용으로 설계한 6축 힘/토크 센서로, Quick Changer 퀵 체인지 인터페이스가 통합되어 플러그 앤 플레이 설치를 지원합니다. 실시간으로 6축 힘/토크 데이터를 측정하여 로봇이 정밀 조립, 일정 힘 연마, 표면 처리 및 충돌 감지를 수행할 수 있도록 돕습니다.

### 제품 이미지

> OnRobot HEX-E QC 6축 힘/토크 센서: [공식 자료](https://www.onrobot.com/en/products/he-x)를 방문하여 확인하세요.

### 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 6축 힘/토크 센서 | 공식 사이트 |
| 힘 측정 범위 (Fx/Fy/Fz) | ±100 N / ±100 N / ±200 N | 공식 사이트/데이터시트 |
| 토크 측정 범위 (Mx/My/Mz) | ±10 Nm / ±10 Nm / ±10 Nm | 공식 사이트/데이터시트 |
| 정밀도 | 미공개 | - |
| 분해능 | 미공개 | - |
| 샘플링 주파수 | 미공개 | - |
| 과부하 용량 | 약 500% FS | 공식 사이트/데이터시트 |
| 보호 등급 | IP67 | 공식 사이트/데이터시트 |
| 통신 인터페이스 | TCP/IP, USB, EtherNet/IP, PROFINET | 공식 사이트/데이터시트 |
| 통합 인터페이스 | Quick Changer / 로봇 플랜지 | 공식 사이트/데이터시트 |
| 전원 공급 | 24 V DC | 공식 사이트/데이터시트 |
| 무게 | 약 350 g | 공식 사이트/데이터시트 |
| 작동 온도 | 미공개 | - |
| 가격 | 미공개 | - |

### 공급망 위치

- **제조사**: [OnRobot (온로봇) / OnRobot](../companies/company_onrobot.md)
- **핵심 부품/기술 출처**: 자체 개발 힘 감지 유닛, 신호 처리 및 통신 회로, Quick Changer 기계 인터페이스, 산업용 밀봉 케이스.
- **하위 응용/고객**: 협동 로봇 OEM, 자동차 및 전자 제조사, 휴머노이드 로봇 완성체 제조사, 자동화 시스템 통합 업체.

### 지식 그래프 노드 및 관계

- 제품 엔티티: `ent_product_onrobot_hex_e`
- 부품 엔티티: `ent_component_onrobot_hex_e_sensor`
- 제조사 엔티티: `ent_company_onrobot`
- 주요 관계:
  - `rel_ent_company_onrobot_manufactures_ent_product_onrobot_hex_e` (`ent_company_onrobot` → `manufactures` → `ent_product_onrobot_hex_e`)
  - `rel_ent_company_onrobot_manufactures_ent_component_onrobot_hex_e_sensor` (`ent_company_onrobot` → `manufactures` → `ent_component_onrobot_hex_e_sensor`)
  - `rel_ent_product_onrobot_hex_e_uses_ent_component_onrobot_hex_e_sensor` (`ent_product_onrobot_hex_e` → `uses` → `ent_component_onrobot_hex_e_sensor`)

### 응용 시나리오

- **힘 제어 조립**: 정밀 플러그인, 기어 조립 시 유연한 삽입 및 위치 결정.
- **일정 힘 연마/광택**: 일정한 접촉력을 유지하여 표면 품질 일관성 향상.
- **삽입 및 테스트**: 커넥터, 스위치 등 부품의 힘-변위 테스트.
- **휴머노이드 로봇 팔**: 엔드 이펙터의 6축 힘 감지를 통한 파지 및 상호작용.

### 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 협동 로봇용 6축 힘 센서 | ATI Nano25 | Bota Systems SensONE |
| 힘 범위 | ±100 N / ±200 N | ±250 N / ±1000 N | ±200 N / ±500 N |
| 통신 | TCP/IP/USB/EtherNet/IP | 아날로그/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |
| 핵심 장점 | 퀵 체인지 통합, 생태계 성숙 | 초소형 크기, 높은 과부하 | 소형 고성능 가격비 |

### 구매 및 배치 제안

- 목표 응용의 분해능, 측정 범위, 정밀도 또는 연산 요구 사항에 따라 특정 모델을 선택하세요.
- 배치 전 인터페이스, 전원 공급, 방열, 기계 설치 및 환경 온도 범위가 일치하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

### 관련 항목

- [제조사: OnRobot (온로봇) / OnRobot](../companies/company_onrobot.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

### 참고 자료

1. [OnRobot 공식 사이트](https://www.onrobot.com)
2. [OnRobot HEX-E QC 6축 힘/토크 센서 제품/자료 페이지](https://www.onrobot.com/en/products/he-x)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
