---
$id: ent_oem_unitree_robotics
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: oem
names:
  en: Unitree Robotics
  zh: 宇树科技
  ko: 유닛리 로보틱스
summary:
  en: Chinese robotics company developing quadruped and humanoid robots, including the Unitree H1 and G1 platforms, with a
    focus on high-torque actuators and cost-conscious design.
  zh: '> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。 > 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。'
  ko: 중국 로봇 기업으로, 고토크 액추에이터와 비용 중심 설계에 초점을 맞춘 Unitree H1 및 G1 휴인oid 플랫폼을 개발하고 있습니다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- upstream
- midstream
- validation_markets
functional_roles:
- organization
- system
tags:
- unitree
- humanoid
- oem
- quadruped
- actuator
- h1
- g1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_unitree.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Unitree H1 Humanoid Robot — Product Specifications
  url: https://unitreerobotics.us/products/unitree-h1-humanoid-robot
  date: '2025'
  accessed_at: '2026-06-24'
- id: src_002
  type: report
  title: IDTechEx Humanoid Robots 2025-2035
  url: https://www.idtechex.com/en/research-report/humanoid-robots/1093
  date: '2025'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---

## 概述
宇树科技是人形机器人领域的重要整机厂商。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 宇树科技 / Unitree Robotics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 宇树科技 |
| **英文名** | Unitree Robotics |
| **总部** | 中国杭州 |
| **成立时间** | 2016 年 |
| **官网** | [https://www.unitree.com](https://www.unitree.com) |
| **供应链环节** | 整机 OEM / 四足+人形机器人、自研关节电机 |
| **企业属性** | 独角兽、四足机器人全球销量领先 |
| **母公司/所属集团** | 无 |
| **数据来源** | Unitree 官网、IT之家、Robozaps、第三方产品数据库 |

### 公司简介

宇树科技以高性价比四足机器人（机器犬）切入市场，2023 年发布首款全尺寸人形机器人 H1，2024 年推出紧凑型人形 G1。

公司坚持核心零部件垂直整合，自研 M107 永磁同步电机、驱动器与整机运控算法，并通过 ROS2 兼容生态与激进定价策略，成为科研机构和开发者社区中最具出货量的人形平台之一。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 全尺寸人形 | 高动态运动、科研原型 | H1 / H1-2 | 科研教育、AI 具身智能研究 |
| 紧凑人形 | 低成本开发平台 | G1 / G1-Comp | 教育、开发者、轻工业 |
| 四足机器人 | 巡检、运输、科研 | Go2 / B2 / B2-W | 电力巡检、应急救援、科研 |

### 代表产品

#### Unitree H1

> Unitree H1：请访问 [官方资料](https://www.unitree.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 180 cm | Unitree 公开资料 / Robozaps |
| 重量 | 47 kg | 公开规格 |
| 自由度 | 26 DOF（基础版） | Robozaps 汇总 |
| 负载/扭矩 | 膝关节峰值扭矩 360 N·m | 公开规格 |
| 速度/转速 | 行走约 1.5 m/s；跑步 3.3 m/s | Unitree 宣称世界纪录 |
| 续航 | 约 1.5–2 h（864 Wh 电池） | 公开规格 |
| 接口/通信 | Wi-Fi、蓝牙、ROS2 / Unitree SDK | 公开规格 |
| 价格 | 约 9 万美元 / 国内约 65 万元 | 经销商与媒体报道 |

**技术亮点**：M107 高扭矩密度电机（189 N·m/kg）、强化学习-based 步态、可热插拔电池、OTA 持续升级。

**应用场景**：双足运动研究、具身智能算法验证、高校实验室。

#### Unitree G1

> Unitree G1：请访问 [官方资料](https://www.unitree.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 127 cm | 公开规格 |
| 重量 | 约 35 kg | 公开规格 |
| 自由度 | 23–43 DOF（含灵巧手配置） | Unitree 配置差异 |
| 负载/扭矩 | 负载约 2 kg | Humanoid.Guide |
| 速度/转速 | 约 2 m/s | 公开规格 |
| 续航 | 约 2 h | 公开规格 |
| 接口/通信 | Wi-Fi、蓝牙、ROS2 | 公开规格 |
| 价格 | 约 1.6 万美元 / 国内 9.9 万元起 | 媒体报道 |

**技术亮点**：三指力控灵巧手、Intel RealSense / LIVOX 传感器、低成本高可及性。

**应用场景**：教育演示、AI 研究、轻量物流与商用展示。

### 供应链位置

- **上游关键零部件/材料**：自研 M107 电机与驱动器，外购减速器、轴承、电池、视觉传感器（参见 [第 4 章 执行器](../../../chapters/chapter-04.md)）。
- **下游客户/应用场景**：高校、科研院所、开发者、物流与安防客户。
- **主要竞争对手/对标**：优必选 Walker、傅利叶 GR-1、特斯拉 Optimus。

### 知识图谱节点与关系

- 公司实体：`ent_company_unitree`
- 产品实体：`ent_product_unitree_h1`、`ent_product_unitree_g1`
- 关键关系：
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_h1`
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_g1`
  - `ent_product_unitree_h1` -- `uses` --> `ent_component_unitree_m107_motor`

### 参考资料

1. [Unitree 官网](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [IT之家 – Unitree 人形机器人报道](https://www.ithome.com)
5. [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考
- [Unitree H1 Humanoid Robot — Product Specifications](https://unitreerobotics.us/products/unitree-h1-humanoid-robot)
- [IDTechEx Humanoid Robots 2025-2035](https://www.idtechex.com/en/research-report/humanoid-robots/1093)
- 项目 Wiki：appendix-d/companies/company_unitree.md

## 개요
우슈 테크놀로지는 휴머노이드 로봇 분야의 중요한 완제품 제조사입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## 우슈 테크놀로지 / Unitree Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 우슈 테크놀로지 |
| **영문명** | Unitree Robotics |
| **본사** | 중국 항저우 |
| **설립 연도** | 2016년 |
| **공식 사이트** | [https://www.unitree.com](https://www.unitree.com) |
| **공급망 단계** | 완제품 OEM / 사족+휴머노이드 로봇, 자체 개발 관절 모터 |
| **기업 속성** | 유니콘, 사족 로봇 글로벌 판매량 선두 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Unitree 공식 사이트, IT之家, Robozaps, 제3자 제품 데이터베이스 |

### 회사 소개

우슈 테크놀로지는 높은 가성비의 사족 로봇(로봇 개)으로 시장에 진입했으며, 2023년 첫 번째 풀사이즈 휴머노이드 로봇 H1을 발표하고, 2024년에는 소형 휴머노이드 G1을 출시했습니다.

회사는 핵심 부품의 수직 통합을 고수하며, 자체 개발한 M107 영구자석 동기 모터, 드라이버 및 완제품 운동 제어 알고리즘을 보유하고 있으며, ROS2 호환 생태계와 공격적인 가격 책정 전략을 통해 연구 기관과 개발자 커뮤니티에서 가장 많은 출하량을 기록한 휴머노이드 플랫폼 중 하나가 되었습니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| 풀사이즈 휴머노이드 | 고동적 운동, 연구 프로토타입 | H1 / H1-2 | 연구 교육, AI 구현 지능 연구 |
| 소형 휴머노이드 | 저비용 개발 플랫폼 | G1 / G1-Comp | 교육, 개발자, 경공업 |
| 사족 로봇 | 순찰, 운송, 연구 | Go2 / B2 / B2-W | 전력 순찰, 긴급 구조, 연구 |

### 대표 제품

### 공급망 위치

- **상류 핵심 부품/재료**: 자체 개발 M107 모터 및 드라이버, 외부 구매 감속기, 베어링, 배터리, 시각 센서 ([제4장 액추에이터](../../../chapters/chapter-04.md) 참조).
- **하류 고객/응용 시나리오**: 대학, 연구 기관, 개발자, 물류 및 보안 고객.
- **주요 경쟁사/대상**: 유비테크 Walker, Fourier GR-1, Tesla Optimus.

### 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_unitree`
- 제품 엔티티: `ent_product_unitree_h1`, `ent_product_unitree_g1`
- 주요 관계:
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_h1`
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_g1`
  - `ent_product_unitree_h1` -- `uses` --> `ent_component_unitree_m107_motor`

### 참고 자료

1. [Unitree 공식 사이트](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [IT之家 – Unitree 휴머노이드 로봇 보도](https://www.ithome.com)
5. [부록 D.4 주요 제품 Wiki](../index-products.md)
