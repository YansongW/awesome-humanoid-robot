---
$id: ent_company_mingzhi_appliance_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Mingzhi Appliance
  zh: 鸣志电器
  ko: Mingzhi Appliance
summary:
  en: Chinese manufacturer of hollow-cup motors used in dexterous robot hands.
  zh: 概述 鸣志电器是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 로봇 능숙한 손에 사용되는 홀컵 모터 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- china
- component_manufactur
- component_manufacturer
- dexterous_hand
- hollow_cup_motor
- mingzhi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_moons.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Mingzhi Appliance
  url: http://www.moons.com.cn/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
鸣志电器是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 鸣志电器 / MOONS' Electric

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 鸣志电器 |
| **英文名** | MOONS' Electric |
| **总部** | 中国上海 |
| **成立时间** | 1994 |
| **官网** | [https://www.moons.com.cn](https://www.moons.com.cn) |
| **供应链环节** | 电机 / 驱动 / 运动控制 |
| **企业属性** | 上市公司（SH.603728）、国内品牌 |
| **母公司/所属集团** | 鸣志电器股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

### 公司简介

国内领先的控制电机及其驱动系统供应商，步进电机全球市占率前列。

鸣志电器专注于控制电机及其驱动系统，产品覆盖步进电机、无刷电机、伺服电机、精密减速器与运动控制器。公司在空心杯电机、无槽无刷电机等高端品类具备量产能力，为机器人、医疗、半导体设备提供核心运动部件。其人形机器人相关布局以微型化、高响应电机与一体化关节模组为主。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 步进电机 | 精密开环/闭环步进 | 57/86 系列、NEMA 系列 | 3C、半导体、医疗设备 |
| 无刷电机 | 高速无槽/空心杯电机 | ECU、DCU 系列 | 机器人关节、无人机、医疗 |
| 伺服系统 | 低压伺服与驱动 | M2AC、M3AC 系列 | AGV、协作机器人 |

### 代表产品

#### 空心杯无刷直流电机 / MOONS' Coreless Brushless DC Motor

> 空心杯无刷直流电机：请访问 [官方资料](https://www.moons.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø16–Ø40 mm（系列范围） | 产品手册 |
| 重量 | 20–150 g（依型号） | 产品手册 |
| 额定电压 | 12–48 VDC | 产品手册 |
| 额定转速 | 5,000–15,000 rpm | 产品手册 |
| 额定扭矩 | 3–50 mNm | 产品手册 |
| 效率 | ≥85% | 产品手册 |
| 通信接口 | Hall / 编码器可选 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：无槽空心杯绕组、低惯量、高动态响应，适合机器人手指、灵巧手等狭小空间驱动。

**应用场景**：人形机器人灵巧手、医疗手持器械、精密光学调焦、无人机云台。

#### 步进电机驱动器 / MOONS' Stepper Drive

> 步进电机驱动器：请访问 [官方资料](https://www.moons.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | 产品手册 |
| 重量 | 未公开 | 产品手册 |
| 额定电流 | 0.5–10 A | 产品手册 |
| 供电电压 | 12–80 VDC | 产品手册 |
| 控制方式 | 脉冲 / CANopen / Modbus | 产品手册 |
| 细分模式 | 最高 256 细分 | 产品手册 |
| 保护功能 | 过流、过压、过热 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：闭环步进控制、振动抑制、支持多种总线协议，适合精密定位与低成本自动化。

**应用场景**：3C 设备、半导体封装、医疗仪器、小型机器人关节。

### 供应链位置

- **上游关键零部件/材料**：稀土永磁体、硅钢片、铜线、轴承、驱动 IC、功率器件
- **下游客户/应用场景**：工业机器人、人形机器人、医疗设备、半导体设备、3C 自动化厂商
- **主要竞争对手/对标**：Maxon、Faulhaber、汇川技术、步科股份、禾川科技

### 知识图谱节点与关系

- 公司实体：`ent_company_moons`
- 产品/零部件实体：`ent_component_moons_brushless_motor`, `ent_component_moons_stepper_drive`
- 关键关系：
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_brushless_motor`
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_stepper_drive`

### 参考资料

1. [官网](https://www.moons.com.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Mingzhi Appliance](http://www.moons.com.cn/)
- 项目 Wiki：appendix-d/companies/company_moons.md

## Overview
MOONS' Electric is an important component manufacturer in the humanoid robot sector. The following content is compiled from the project Wiki for in-depth reference.

## Content
## MOONS' Electric

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 鸣志电器 |
| **English Name** | MOONS' Electric |
| **Headquarters** | Shanghai, China |
| **Founded** | 1994 |
| **Website** | [https://www.moons.com.cn](https://www.moons.com.cn) |
| **Supply Chain Role** | Motors / Drives / Motion Control |
| **Enterprise Type** | Listed Company (SH.603728), Domestic Brand |
| **Parent Company/Group** | MOONS' Electric Co., Ltd. |
| **Data Sources** | Official website, annual reports, product manuals, WAIC 2026 reports |

### Company Profile

A leading domestic supplier of control motors and their drive systems, with a top global market share in stepper motors.

MOONS' Electric focuses on control motors and their drive systems, with products covering stepper motors, brushless motors, servo motors, precision reducers, and motion controllers. The company has mass production capabilities for high-end categories such as coreless motors and slotless brushless motors, providing core motion components for robotics, medical, and semiconductor equipment. Its humanoid robot-related layout primarily features miniaturized, high-response motors and integrated joint modules.

### Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Stepper Motors | Precision open-loop/closed-loop stepping | 57/86 Series, NEMA Series | 3C, Semiconductor, Medical Equipment |
| Brushless Motors | High-speed slotless/coreless motors | ECU, DCU Series | Robot Joints, Drones, Medical |
| Servo Systems | Low-voltage servo and drive | M2AC, M3AC Series | AGV, Collaborative Robots |

### Representative Products

#### Coreless Brushless DC Motor / MOONS' Coreless Brushless DC Motor

> Coreless Brushless DC Motor: Please visit [Official Materials](https://www.moons.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Size | Ø16–Ø40 mm (series range) | Product Manual |
| Weight | 20–150 g (depending on model) | Product Manual |
| Rated Voltage | 12–48 VDC | Product Manual |
| Rated Speed | 5,000–15,000 rpm | Product Manual |
| Rated Torque | 3–50 mNm | Product Manual |
| Efficiency | ≥85% | Product Manual |
| Communication Interface | Hall / Encoder optional | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Slotless coreless winding, low inertia, high dynamic response, suitable for driving in confined spaces such as robot fingers and dexterous hands.

**Application Scenarios**: Humanoid robot dexterous hands, medical handheld instruments, precision optical focusing, drone gimbals.

#### Stepper Motor Drive / MOONS' Stepper Drive

> Stepper Motor Drive: Please visit [Official Materials](https://www.moons.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Size | Not disclosed | Product Manual |
| Weight | Not disclosed | Product Manual |
| Rated Current | 0.5–10 A | Product Manual |
| Supply Voltage | 12–80 VDC | Product Manual |
| Control Method | Pulse / CANopen / Modbus | Product Manual |
| Microstep Mode | Up to 256 microsteps | Product Manual |
| Protection Features | Overcurrent, Overvoltage, Overtemperature | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Closed-loop stepper control, vibration suppression, support for multiple bus protocols, suitable for precision positioning and low-cost automation.

**Application Scenarios**: 3C equipment, semiconductor packaging, medical instruments, small robot joints.

### Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, silicon steel sheets, copper wire, bearings, driver ICs, power devices
- **Downstream Customers/Application Scenarios**: Industrial robots, humanoid robots, medical equipment, semiconductor equipment, 3C automation manufacturers
- **Main Competitors/Peers**: Maxon, Faulhaber, Inovance Technology, Buke Shares, Hechuan Technology

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_moons`
- Product/Component Entities: `ent_component_moons_brushless_motor`, `ent_component_moons_stepper_drive`
- Key Relationships:
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_brushless_motor`
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_stepper_drive`

### References

1. [Official Website](https://www.moons.com.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)

## 개요
MOONS' Electric은 휴머노이드 로봇 분야의 핵심 부품 제조사입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 조사 시 참고하시기 바랍니다.

## 핵심 내용
## MOONS' Electric / MOONS' Electric

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시점: 2026-07-01. 모든 파라미터는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 鸣志电器 |
| **영문명** | MOONS' Electric |
| **본사** | 중국 상하이 |
| **설립 연도** | 1994 |
| **공식 홈페이지** | [https://www.moons.com.cn](https://www.moons.com.cn) |
| **공급망 단계** | 모터 / 드라이브 / 모션 컨트롤 |
| **기업 속성** | 상장 기업 (SH.603728), 국내 브랜드 |
| **모회사/소속 그룹** | MOONS' Electric Co., Ltd. |
| **데이터 출처** | 공식 홈페이지, 연례 보고서, 제품 매뉴얼, WAIC 2026 보도 |

### 회사 소개

국내 선도적인 제어 모터 및 그 구동 시스템 공급업체로, 스테핑 모터 글로벌 시장 점유율 상위권.

MOONS' Electric은 제어 모터 및 그 구동 시스템에 주력하며, 제품군은 스테핑 모터, 브러시리스 모터, 서보 모터, 정밀 감속기 및 모션 컨트롤러를 포괄합니다. 코어리스 모터, 슬롯리스 브러시리스 모터 등 고급 품목에서 양산 능력을 갖추고 있으며, 로봇, 의료, 반도체 장비에 핵심 운동 부품을 제공합니다. 휴머노이드 로봇 관련 포트폴리오는 소형화, 고응답 모터 및 일체형 관절 모듈을 중심으로 구성됩니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 스테핑 모터 | 정밀 오픈/클로즈드 루프 스테핑 | 57/86 시리즈, NEMA 시리즈 | 3C, 반도체, 의료 장비 |
| 브러시리스 모터 | 고속 슬롯리스/코어리스 모터 | ECU, DCU 시리즈 | 로봇 관절, 드론, 의료 |
| 서보 시스템 | 저전압 서보 및 드라이브 | M2AC, M3AC 시리즈 | AGV, 협동 로봇 |

### 대표 제품

#### 코어리스 브러시리스 DC 모터 / MOONS' Coreless Brushless DC Motor

> 코어리스 브러시리스 DC 모터: [공식 자료](https://www.moons.com.cn)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | Ø16–Ø40 mm (시리즈 범위) | 제품 매뉴얼 |
| 무게 | 20–150 g (모델에 따라 다름) | 제품 매뉴얼 |
| 정격 전압 | 12–48 VDC | 제품 매뉴얼 |
| 정격 속도 | 5,000–15,000 rpm | 제품 매뉴얼 |
| 정격 토크 | 3–50 mNm | 제품 매뉴얼 |
| 효율 | ≥85% | 제품 매뉴얼 |
| 통신 인터페이스 | Hall / 엔코더 선택 가능 | 제품 매뉴얼 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 슬롯리스 코어리스 권선, 저관성, 고동적 응답으로 로봇 손가락, 정교한 손 등 협소 공간 구동에 적합.

**적용 시나리오**: 휴머노이드 로봇 정교한 손, 의료용 핸드헬드 기기, 정밀 광학 초점 조정, 드론 짐벌.

#### 스테핑 모터 드라이브 / MOONS' Stepper Drive

> 스테핑 모터 드라이브: [공식 자료](https://www.moons.com.cn)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 미공개 | 제품 매뉴얼 |
| 무게 | 미공개 | 제품 매뉴얼 |
| 정격 전류 | 0.5–10 A | 제품 매뉴얼 |
| 공급 전압 | 12–80 VDC | 제품 매뉴얼 |
| 제어 방식 | 펄스 / CANopen / Modbus | 제품 매뉴얼 |
| 미세 스텝 모드 | 최대 256 미세 스텝 | 제품 매뉴얼 |
| 보호 기능 | 과전류, 과전압, 과열 | 제품 매뉴얼 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 클로즈드 루프 스테핑 제어, 진동 억제, 다양한 버스 프로토콜 지원으로 정밀 위치 제어 및 저비용 자동화에 적합.

**적용 시나리오**: 3C 장비, 반도체 패키징, 의료 기기, 소형 로봇 관절.

### 공급망 위치

- **상류 핵심 부품/재료**: 희토류 영구 자석, 규소 강판, 동선, 베어링, 구동 IC, 전력 소자
- **하류 고객/적용 시나리오**: 산업용 로봇, 휴머노이드 로봇, 의료 장비, 반도체 장비, 3C 자동화 업체
- **주요 경쟁사/대상**: Maxon, Faulhaber, 汇川技术, 步科股份, 禾川科技

### 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_moons`
- 제품/부품 엔티티: `ent_component_moons_brushless_motor`, `ent_component_moons_stepper_drive`
- 주요 관계:
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_brushless_motor`
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_stepper_drive`

### 참고 자료

1. [공식 홈페이지](https://www.moons.com.cn)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 연구 보고서](https://www.inovance.com) (실제 제품 모델에 따라 확인 필요)
