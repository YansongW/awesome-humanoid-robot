---
$id: ent_company_bonfiglioli_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Bonfiglioli
  zh: 邦飞利
  ko: Bonfiglioli
summary:
  en: Italian manufacturer of gearboxes and drive systems used in industrial and mobile robotics.
  zh: 概述 邦飞利是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 산업 및 모바일 로보틱스에 사용되는 기어박스 및 드라이브 시스템 이탈리아 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- bonfiglioli
- component_manufactur
- component_manufacturer
- drive_system
- gearbox
- italy
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_bonfiglioli.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Bonfiglioli
  url: https://www.bonfiglioli.com/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
邦飞利是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Bonfiglioli / 邦飞利

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 邦飞利 |
| **英文名** | Bonfiglioli |
| **总部** | 意大利博洛尼亚（Bologna） |
| **成立时间** | 1956 |
| **官网** | [https://www.bonfiglioli.com](https://www.bonfiglioli.com) |
| **供应链环节** | 减速机 / 驱动系统 / 移动机械 |
| **企业属性** | 家族企业、国际工业传动品牌 |
| **母公司/所属集团** | Bonfiglioli 家族（独立） |
| **数据来源** | 官网、产品样本、WAIC 2026 报道 |

### 公司简介

Bonfiglioli 是意大利知名的工业传动与驱动技术供应商，产品涵盖行星减速机、斜齿/伞齿减速电机、变频器及移动机械驱动方案。其 300M 系列行星减速机以高扭矩密度和模块化著称。

公司产品广泛应用于风力发电、物料搬运、工程机械、食品与饮料以及机器人领域，通过全球分销网络提供本地化支持。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 行星减速机 | 重载/高扭矩密度 | 300M 系列 | 风电、矿山、机器人 |
| 斜齿/伞齿减速电机 | 工业齿轮电机 | F / K / A 系列 | 自动化、输送 |
| 变频器与电机 | 运动控制/高效电机 | Active Cube 8 / BN-BE | 产线、物流 |

### 代表产品

#### 300M 系列行星减速机

> 300M 系列行星减速机：请访问 [官方资料](https://www.bonfiglioli.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3.4:1 – 5,000:1 | 产品手册 |
| 输出扭矩 | 1,000 – 450,000 N·m（系列范围） | 产品手册 |
| 框号尺寸 | 20 种 finely spaced 尺寸 | 产品手册 |
| 安装型式 | 底脚 / 法兰 / 空心轴 / 实心键轴 | 产品手册 |
| 输入方式 | IEC/NEMA 电机适配、液压马达、实心轴 | 产品手册 |
| 防护/选项 | IP65、ATEX、独立冷却、Taconite 密封 | 产品手册 |
| 传动级数 | 1–4 级（含直角/组合） | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：模块化设计、高扭矩密度、直角与同轴版本可选、内置冷却与多重密封、适配多种电机。

**应用场景**：风电变桨、矿山机械、工业机器人底座、人形机器人躯干关节、输送与起重设备。

#### 其他代表产品

F 系列斜齿减速电机扭矩可达数万 N·m；Active Cube 8 变频器支持多轴伺服控制；移动机械轮边驱动用于 AGV/叉车。

### 供应链位置

- **上游关键零部件/材料**：球墨铸铁箱体、合金钢齿轮、轴承、密封件、电机、制动器、冷却系统
- **下游客户/应用场景**：风电主机厂、工程机械、机器人 OEM、物料搬运、食品包装
- **主要竞争对手/对标**：SEW-Eurodrive、Lenze、Siemens、STOBER

### 知识图谱节点与关系

- 公司实体：`ent_company_bonfiglioli`
- 零部件实体：`ent_component_bonfiglioli_300m`
- 关键关系：
  - `ent_company_bonfiglioli` -- `manufactures` --> `ent_component_bonfiglioli_300m`

### 参考资料

1. [邦飞利 官网](https://www.bonfiglioli.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [Bonfiglioli 300M 技术概览](https://www.bonfiglioli.com/en/products/gear-motors-and-gear-units)

## 参考
- [Bonfiglioli](https://www.bonfiglioli.com/)
- 项目 Wiki：appendix-d/companies/company_bonfiglioli.md

## Overview
Bonfiglioli is an important component manufacturer in the humanoid robotics field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Bonfiglioli

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 邦飞利 |
| **English Name** | Bonfiglioli |
| **Headquarters** | Bologna, Italy |
| **Founded** | 1956 |
| **Website** | [https://www.bonfiglioli.com](https://www.bonfiglioli.com) |
| **Supply Chain Role** | Gearboxes / Drive Systems / Mobile Machinery |
| **Enterprise Type** | Family-owned, international industrial drive brand |
| **Parent/Group** | Bonfiglioli family (independent) |
| **Data Source** | Official website, product catalogs, WAIC 2026 reports |

### Company Profile

Bonfiglioli is a renowned Italian supplier of industrial transmission and drive technology, offering products including planetary gearboxes, helical/bevel gear motors, inverters, and mobile machinery drive solutions. Its 300M series planetary gearboxes are known for high torque density and modularity.

The company's products are widely used in wind power, material handling, construction machinery, food and beverage, and robotics, with local support provided through a global distribution network.

### Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Planetary Gearboxes | Heavy-duty / High torque density | 300M Series | Wind power, mining, robotics |
| Helical/Bevel Gear Motors | Industrial gear motors | F / K / A Series | Automation, conveying |
| Inverters and Motors | Motion control / High-efficiency motors | Active Cube 8 / BN-BE | Production lines, logistics |

### Representative Products

#### 300M Series Planetary Gearboxes

> 300M Series Planetary Gearboxes: Please visit [Official Documentation](https://www.bonfiglioli.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Reduction Ratio | 3.4:1 – 5,000:1 | Product catalog |
| Output Torque | 1,000 – 450,000 N·m (series range) | Product catalog |
| Frame Sizes | 20 finely spaced sizes | Product catalog |
| Mounting Types | Foot / Flange / Hollow shaft / Solid keyed shaft | Product catalog |
| Input Options | IEC/NEMA motor adapter, hydraulic motor, solid shaft | Product catalog |
| Protection/Options | IP65, ATEX, independent cooling, Taconite seals | Product catalog |
| Stages | 1–4 (including right-angle/combination) | Product catalog |
| Price | Not disclosed | - |

**Technical Highlights**: Modular design, high torque density, right-angle and coaxial versions available, built-in cooling and multiple seals, compatible with various motors.

**Application Scenarios**: Wind turbine pitch control, mining machinery, industrial robot bases, humanoid robot torso joints, conveying and lifting equipment.

#### Other Representative Products

The F series helical gear motors offer torque up to tens of thousands of N·m; the Active Cube 8 inverter supports multi-axis servo control; mobile machinery wheel drives are used in AGVs/forklifts.

### Supply Chain Position

- **Upstream Key Components/Materials**: Ductile iron housings, alloy steel gears, bearings, seals, motors, brakes, cooling systems
- **Downstream Customers/Applications**: Wind turbine OEMs, construction machinery, robot OEMs, material handling, food packaging
- **Main Competitors/Peers**: SEW-Eurodrive, Lenze, Siemens, STOBER

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_bonfiglioli`
- Component Entity: `ent_component_bonfiglioli_300m`
- Key Relationship:
  - `ent_company_bonfiglioli` -- `manufactures` --> `ent_component_bonfiglioli_300m`

### References

1. [Bonfiglioli Official Website](https://www.bonfiglioli.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Bonfiglioli 300M Technical Overview](https://www.bonfiglioli.com/en/products/gear-motors-and-gear-units)

## 개요
Bonfiglioli는 휴머노이드 로봇 분야의 핵심 부품 제조사입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## Bonfiglioli / 본피글리올리

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 본피글리올리 |
| **영문명** | Bonfiglioli |
| **본사** | 이탈리아 볼로냐 (Bologna) |
| **설립 연도** | 1956 |
| **공식 홈페이지** | [https://www.bonfiglioli.com](https://www.bonfiglioli.com) |
| **공급망 단계** | 감속기 / 구동 시스템 / 이동 기계 |
| **기업 속성** | 가족 기업, 국제 산업용 동력 전달 브랜드 |
| **모회사/소속 그룹** | Bonfiglioli 가문 (독립) |
| **데이터 출처** | 공식 홈페이지, 제품 샘플, WAIC 2026 보도 |

### 회사 소개

Bonfiglioli는 이탈리아의 유명한 산업용 동력 전달 및 구동 기술 공급업체로, 제품군에는 유성 감속기, 헬리컬/베벨 기어 감속 모터, 인버터 및 이동 기계 구동 솔루션이 포함됩니다. 300M 시리즈 유성 감속기는 높은 토크 밀도와 모듈식 설계로 유명합니다.

회사 제품은 풍력 발전, 자재 운반, 건설 기계, 식음료 및 로봇 분야에 널리 사용되며, 글로벌 유통 네트워크를 통해 현지화된 지원을 제공합니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 유성 감속기 | 중하중/고토크 밀도 | 300M 시리즈 | 풍력, 광산, 로봇 |
| 헬리컬/베벨 기어 감속 모터 | 산업용 기어 모터 | F / K / A 시리즈 | 자동화, 컨베이어 |
| 인버터 및 모터 | 모션 제어/고효율 모터 | Active Cube 8 / BN-BE | 생산 라인, 물류 |

### 대표 제품

#### 300M 시리즈 유성 감속기

> 300M 시리즈 유성 감속기: [공식 자료](https://www.bonfiglioli.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3.4:1 – 5,000:1 | 제품 매뉴얼 |
| 출력 토크 | 1,000 – 450,000 N·m (시리즈 범위) | 제품 매뉴얼 |
| 프레임 크기 | 20종의 세밀한 간격 크기 | 제품 매뉴얼 |
| 설치 방식 | 풋 / 플랜지 / 중공축 / 실린더 키축 | 제품 매뉴얼 |
| 입력 방식 | IEC/NEMA 모터 어댑터, 유압 모터, 실린더축 | 제품 매뉴얼 |
| 보호/옵션 | IP65, ATEX, 독립 냉각, Taconite 씰 | 제품 매뉴얼 |
| 전달 단수 | 1–4단 (직각/조합 포함) | 제품 매뉴얼 |
| 가격 | 미공개 | - |

**기술적 특징**: 모듈식 설계, 높은 토크 밀도, 직각 및 동축 버전 선택 가능, 내장 냉각 및 다중 씰, 다양한 모터 호환.

**적용 분야**: 풍력 피치 제어, 광산 기계, 산업용 로봇 베이스, 휴머노이드 로봇 몸통 관절, 컨베이어 및 크레인 장비.

#### 기타 대표 제품

F 시리즈 헬리컬 기어 감속 모터는 수만 N·m의 토크를 제공하며, Active Cube 8 인버터는 다축 서보 제어를 지원하고, 이동 기계 휠 구동은 AGV/지게차에 사용됩니다.

### 공급망 위치

- **상류 핵심 부품/재료**: 구상흑연 주철 하우징, 합금강 기어, 베어링, 씰, 모터, 브레이크, 냉각 시스템
- **하류 고객/적용 분야**: 풍력 터빈 제조사, 건설 기계, 로봇 OEM, 자재 운반, 식품 포장
- **주요 경쟁사/대응 기업**: SEW-Eurodrive, Lenze, Siemens, STOBER

### 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_bonfiglioli`
- 부품 엔티티: `ent_component_bonfiglioli_300m`
- 주요 관계:
  - `ent_company_bonfiglioli` -- `manufactures` --> `ent_component_bonfiglioli_300m`

### 참고 자료

1. [본피글리올리 공식 홈페이지](https://www.bonfiglioli.com)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [Bonfiglioli 300M 기술 개요](https://www.bonfiglioli.com/en/products/gear-motors-and-gear-units)
