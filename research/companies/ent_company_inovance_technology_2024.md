---
$id: ent_company_inovance_technology_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Inovance Technology
  zh: 汇川技术
  ko: Inovance Technology
summary:
  en: Chinese industrial automation supplier of servo drives and frameless torque motors for robot joints.
  zh: 概述 汇川技术是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 로봇 관절용 서보 드라이브 및 프레임리스 토크 모터를 공급하는 중국 산업 자동화 업체.
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
- frameless_torque_motor
- inovance
- servo_drive
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_inovance.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Inovance Technology
  url: https://www.inovance.com/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
汇川技术是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 汇川技术 / Inovance Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 汇川技术 |
| **英文名** | Inovance Technology |
| **总部** | 中国深圳 |
| **成立时间** | 2003 |
| **官网** | [https://www.inovance.com](https://www.inovance.com) |
| **供应链环节** | 伺服系统 / 电机 / 驱动器 / 变频器 |
| **企业属性** | 国产品牌、上市公司（300124.SZ） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

### 公司简介

中国工业自动化龙头，提供伺服电机、驱动器、PLC 和机器人核心部件。

汇川技术的 MS1 系列伺服电机搭配 SV680 系列高性能伺服驱动，覆盖 50 W–7.5 kW 功率段，支持 23/26 位绝对值编码器，广泛应用于工业机器人、人形机器人和新能源装备。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| MS1 伺服电机 | 高响应伺服电机 | MS1H2 / MS1H3 / MS1H4 | 机器人、机床、锂电 |
| SV680 伺服驱动 | 高端单轴伺服驱动 | SV680P / SV680-INT | 半导体、机器人 |

### 代表产品

#### MS1H4-40B30CB 伺服电机 / MS1H4-40B30CB Servo Motor

> MS1H4-40B30CB 伺服电机：请访问 [官方资料](https://www.inovance.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 机座号 | 40 mm | 汇川 SV630P 手册 |
| 额定功率 | 400 W | 汇川 SV630P 手册 |
| 额定转速 | 3000 rpm | 汇川手册 |
| 最高转速 | 6000 rpm | 汇川官网 |
| 额定扭矩 | 未公开 | - |
| 最大扭矩 | 约 3.5 倍额定扭矩 | 汇川手册（H4 机型） |
| 转子惯量 | 0.43 kg·cm² | 汇川手册 |
| 编码器 | 18 位多圈绝对值（T3） | 汇川手册 |
| 防护等级 | IP67 | 汇川手册 |

**技术亮点**：小惯量、小容量设计，高过载能力，适配机器人小关节和高速定位应用。

**应用场景**：SCARA、协作机器人关节、人形机器人手臂、3C 自动化。

#### SV680P 伺服驱动器 / SV680P Servo Drive

> SV680P 伺服驱动器：请访问 [官方资料](https://www.inovance.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 功率范围 | 50 W – 7.5 kW | Inovance 官网 |
| 通信协议 | CANopen / EtherCAT / Pulse | Inovance 官网 |
| 速度环带宽 | 3.5 kHz | Inovance 欧洲官网 |
| 电流环频率 | 625 kHz | Inovance 欧洲官网 |
| 编码器支持 | 23/26 位绝对值、BiSS-C、EnDat 2.2 | Inovance 欧洲官网 |
| 安全功能 | STO / SS1 / SLS 等 SIL3/PL e | Inovance 欧洲官网 |
| 认证 | CE / UL / KC / UKCA / SEMI F47 | Inovance 官网 |

**技术亮点**：高响应、功能安全齐全，适合人形机器人对动态性能和安全性的要求。

**应用场景**：工业机器人、半导体设备、人形机器人关节驱动。

### 供应链位置

- **上游关键零部件/材料**：稀土磁材、IGBT、PCB、铜线、铝壳、编码器芯片
- **下游客户/应用场景**：工业机器人、人形机器人、新能源汽车、光伏/锂电设备厂商
- **主要竞争对手/对标**：禾川科技、雷赛智能、安川、三菱

### 知识图谱节点与关系

- 公司实体：`ent_company_inovance`
- 产品实体：`ent_component_inovance_ms1h4_40b`、`ent_component_inovance_sv680p`
- 关键关系：
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_ms1h4_40b`
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_sv680p`

### 参考资料

1. [官网](https://www.inovance.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Inovance Technology](https://www.inovance.com/)
- 项目 Wiki：appendix-d/companies/company_inovance.md

## Overview
Inovance Technology is a key component manufacturer in the humanoid robot sector. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Inovance Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 汇川技术 |
| **English Name** | Inovance Technology |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2003 |
| **Website** | [https://www.inovance.com](https://www.inovance.com) |
| **Supply Chain Role** | Servo Systems / Motors / Drives / Inverters |
| **Enterprise Type** | Domestic brand, listed company (300124.SZ) |
| **Parent Company/Group** | None (independently listed) |
| **Data Sources** | Official website, product manuals, public research reports, WAIC 2026 coverage |

### Company Profile

China's leading industrial automation company, providing servo motors, drives, PLCs, and robot core components.

Inovance Technology's MS1 series servo motors, paired with the SV680 series high-performance servo drives, cover a power range of 50 W–7.5 kW and support 23/26-bit absolute encoders. They are widely used in industrial robots, humanoid robots, and new energy equipment.

### Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| MS1 Servo Motors | High-response servo motors | MS1H2 / MS1H3 / MS1H4 | Robotics, machine tools, lithium batteries |
| SV680 Servo Drives | High-end single-axis servo drives | SV680P / SV680-INT | Semiconductors, robotics |

### Representative Products

#### MS1H4-40B30CB Servo Motor

> MS1H4-40B30CB Servo Motor: Please visit [official materials](https://www.inovance.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Frame Size | 40 mm | Inovance SV630P manual |
| Rated Power | 400 W | Inovance SV630P manual |
| Rated Speed | 3000 rpm | Inovance manual |
| Maximum Speed | 6000 rpm | Inovance official website |
| Rated Torque | Not disclosed | - |
| Maximum Torque | Approx. 3.5x rated torque | Inovance manual (H4 model) |
| Rotor Inertia | 0.43 kg·cm² | Inovance manual |
| Encoder | 18-bit multi-turn absolute (T3) | Inovance manual |
| Protection Rating | IP67 | Inovance manual |

**Technical Highlights**: Low inertia, small capacity design, high overload capacity, suitable for small robot joints and high-speed positioning applications.

**Application Scenarios**: SCARA, collaborative robot joints, humanoid robot arms, 3C automation.

#### SV680P Servo Drive

> SV680P Servo Drive: Please visit [official materials](https://www.inovance.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Power Range | 50 W – 7.5 kW | Inovance official website |
| Communication Protocols | CANopen / EtherCAT / Pulse | Inovance official website |
| Speed Loop Bandwidth | 3.5 kHz | Inovance Europe website |
| Current Loop Frequency | 625 kHz | Inovance Europe website |
| Encoder Support | 23/26-bit absolute, BiSS-C, EnDat 2.2 | Inovance Europe website |
| Safety Functions | STO / SS1 / SLS etc. SIL3/PL e | Inovance Europe website |
| Certifications | CE / UL / KC / UKCA / SEMI F47 | Inovance official website |

**Technical Highlights**: High response, comprehensive functional safety, meeting the dynamic performance and safety requirements of humanoid robots.

**Application Scenarios**: Industrial robots, semiconductor equipment, humanoid robot joint drives.

### Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, IGBT, PCB, copper wire, aluminum housing, encoder chips
- **Downstream Customers/Application Scenarios**: Industrial robot, humanoid robot, new energy vehicle, photovoltaic/lithium battery equipment manufacturers
- **Main Competitors/Benchmarks**: Hechuan Technology, Leadshine, Yaskawa, Mitsubishi

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_inovance`
- Product Entities: `ent_component_inovance_ms1h4_40b`, `ent_component_inovance_sv680p`
- Key Relationships:
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_ms1h4_40b`
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_sv680p`

### References

1. [Official Website](https://www.inovance.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)

## 개요
Inovance Technology는 휴머노이드 로봇 분야의 핵심 부품 제조사입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## Inovance Technology

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 파라미터는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 기업 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 汇川技术 |
| **영문명** | Inovance Technology |
| **본사** | 중국 선전 |
| **설립 연도** | 2003 |
| **공식 사이트** | [https://www.inovance.com](https://www.inovance.com) |
| **공급망 단계** | 서보 시스템 / 모터 / 드라이버 / 인버터 |
| **기업 속성** | 국산 브랜드, 상장 기업 (300124.SZ) |
| **모회사/소속 그룹** | 없음 (독립 상장) |
| **데이터 출처** | 공식 사이트, 제품 매뉴얼, 공개 연구 보고서, WAIC 2026 보도 |

### 기업 소개

중국 산업 자동화 선두 기업으로, 서보 모터, 드라이버, PLC 및 로봇 핵심 부품을 제공합니다.

Inovance Technology의 MS1 시리즈 서보 모터는 SV680 시리즈 고성능 서보 드라이브와 함께 50W~7.5kW 출력 범위를 지원하며, 23/26비트 절대값 엔코더를 지원하여 산업용 로봇, 휴머노이드 로봇 및 신에너지 장비에 널리 사용됩니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| MS1 서보 모터 | 고응답 서보 모터 | MS1H2 / MS1H3 / MS1H4 | 로봇, 공작 기계, 리튬 배터리 |
| SV680 서보 드라이브 | 고급 단축 서보 드라이브 | SV680P / SV680-INT | 반도체, 로봇 |

### 대표 제품

#### MS1H4-40B30CB 서보 모터

> MS1H4-40B30CB 서보 모터: [공식 자료](https://www.inovance.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 프레임 사이즈 | 40 mm | Inovance SV630P 매뉴얼 |
| 정격 출력 | 400 W | Inovance SV630P 매뉴얼 |
| 정격 속도 | 3000 rpm | Inovance 매뉴얼 |
| 최대 속도 | 6000 rpm | Inovance 공식 사이트 |
| 정격 토크 | 미공개 | - |
| 최대 토크 | 약 정격 토크의 3.5배 | Inovance 매뉴얼 (H4 모델) |
| 로터 관성 | 0.43 kg·cm² | Inovance 매뉴얼 |
| 엔코더 | 18비트 멀티턴 절대값 (T3) | Inovance 매뉴얼 |
| 보호 등급 | IP67 | Inovance 매뉴얼 |

**기술적 특징**: 소형 관성, 소형 용량 설계, 높은 과부하 용량으로 로봇 소형 관절 및 고속 위치 결정 애플리케이션에 적합합니다.

**적용 분야**: SCARA, 협동 로봇 관절, 휴머노이드 로봇 팔, 3C 자동화.

#### SV680P 서보 드라이브

> SV680P 서보 드라이브: [공식 자료](https://www.inovance.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 출력 범위 | 50W – 7.5kW | Inovance 공식 사이트 |
| 통신 프로토콜 | CANopen / EtherCAT / Pulse | Inovance 공식 사이트 |
| 속도 루프 대역폭 | 3.5 kHz | Inovance 유럽 공식 사이트 |
| 전류 루프 주파수 | 625 kHz | Inovance 유럽 공식 사이트 |
| 엔코더 지원 | 23/26비트 절대값, BiSS-C, EnDat 2.2 | Inovance 유럽 공식 사이트 |
| 안전 기능 | STO / SS1 / SLS 등 SIL3/PL e | Inovance 유럽 공식 사이트 |
| 인증 | CE / UL / KC / UKCA / SEMI F47 | Inovance 공식 사이트 |

**기술적 특징**: 높은 응답성, 포괄적인 기능 안전으로 휴머노이드 로봇의 동적 성능 및 안전 요구 사항에 적합합니다.

**적용 분야**: 산업용 로봇, 반도체 장비, 휴머노이드 로봇 관절 구동.

### 공급망 위치

- **상류 핵심 부품/소재**: 희토류 자석, IGBT, PCB, 구리선, 알루미늄 케이스, 엔코더 칩
- **하류 고객/적용 분야**: 산업용 로봇, 휴머노이드 로봇, 신에너지 자동차, 태양광/리튬 배터리 장비 제조사
- **주요 경쟁사/대상**: Hechuan Technology, Leadshine, Yaskawa, Mitsubishi

### 지식 그래프 노드 및 관계

- 기업 엔터티: `ent_company_inovance`
- 제품 엔터티: `ent_component_inovance_ms1h4_40b`, `ent_component_inovance_sv680p`
- 주요 관계:
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_ms1h4_40b`
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_sv680p`

### 참고 자료

1. [공식 사이트](https://www.inovance.com)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 연구 보고서](https://www.inovance.com) (실제 제품 모델에 따라 확인 필요)
