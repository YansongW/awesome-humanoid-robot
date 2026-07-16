---
$id: ent_material_rare_earth_supply
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: material
names:
  en: Rare-Earth Supply Chain
  zh: 稀土元素供应链
  ko: 희토류 공급망
summary:
  en: The upstream supply chain of rare-earth elements—especially neodymium, dysprosium, and terbium—used in high-performance
    permanent magnets for actuators.
  zh: '> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。 > 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。'
  ko: 액추에이터용 고성능 영구자석에 사용되는 네오디뮴·디스프로슘·터븀 등 희토류의 상류 공급망.
domains:
- 01_raw_materials
layers:
- upstream
functional_roles:
- knowledge
tags:
- material
- chapter_3
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from appendix-d/companies/company_china_northern_rare_earth.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
稀土元素供应链是人形机器人领域的重要材料。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 北方稀土 / China Northern Rare Earth

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 中国北方稀土（集团）高科技股份有限公司 |
| **英文名** | China Northern Rare Earth (Group) High-Tech Co., Ltd. |
| **总部** | 中国内蒙古包头市 |
| **成立时间** | 1997 年（前身始建于 1961 年） |
| **官网** | [http://www.cnre.com.cn](http://www.cnre.com.cn) |
| **供应链环节** | 稀土精矿、稀土氧化物、稀土金属、磁材合金 |
| **企业属性** | 上市公司（上交所：600111） |
| **母公司/所属集团** | 中国北方稀土集团 |
| **数据来源** | 公司年报/可持续发展报告、上交所公告 |

### 公司简介

北方稀土是全球最大的轻稀土供应商之一，依托包头白云鄂博稀土资源优势，构建了从稀土精矿、冶炼分离到功能材料的全产业链布局。

公司主要产品包括稀土精矿、稀土氧化物、稀土金属及钕铁硼速凝薄带合金等磁材原料。高性能钕铁硼永磁体是人形机器人伺服电机和无框力矩电机的关键材料，北方稀土在上游原材料端具有重要战略地位。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 稀土原料 | 轻稀土精矿与氧化物 | 氧化镨钕、碳酸稀土 | 永磁、催化、储氢 |
| 稀土金属 | 冶炼分离产品 | 镨钕金属 | 磁材合金 |
| 磁材合金 | 钕铁硼速凝薄带合金 | NdFeB 甩带片 | 永磁电机、磁组件 |

### 代表产品/材料

#### 钕铁硼速凝薄带合金（NdFeB Strip-Casting Alloy）

![稀土合金](http://www.cnre.com.cn)

> 图片来源：北方稀土官网。若链接失效或缺失，请替换为官方公开图片 URL。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 主要成分 | Nd-Fe-B（镨钕-铁-硼） | 公开资料 |
| 稀土含量 | 约 30–32 wt% | 学术论文 / 行业资料 |
| 形态 | 薄带 / 鳞片 | 公司公告 |
| 矫顽力（对应磁体） | 依牌号而定，N52 约 11 kOe | 行业标准 |
| 最大磁能积（对应磁体） | N52 约 50–53 MGOe | 行业标准 |
| 工作温度（对应磁体） | N52 ≤ 80 °C | 行业标准 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：速凝薄带工艺可细化晶粒、提高磁性能一致性，是高性能烧结钕铁硼的前驱材料。

**应用场景**：新能源汽车驱动电机、风力发电机、人形机器人关节电机磁钢。

### 与人形机器人的关联

- 电池、功率半导体与先进材料是人形机器人实现长续航、高动态与轻量化的共性基础。
- 工业机器人与自动化产线为人形机器人整机装配、测试与量产提供可复用的制造能力。

### 供应链位置

- **上游关键零部件/材料**：稀土精矿、白云鄂博矿资源、能源。
- **下游客户/应用场景**：钕铁硼磁材厂（如金力永磁）、新能源汽车电机厂、风电整机厂。
- **主要竞争对手/对标**：中国稀土集团、Lynas Rare Earths、MP Materials。

### 知识图谱节点与关系

- 公司实体：`ent_company_china_northern_rare_earth`
- 材料实体：`ent_material_cnre_ndfeb_alloy`
- 关键关系：
  - `ent_company_china_northern_rare_earth` -- `produces` --> `ent_material_cnre_ndfeb_alloy`

### 参考资料

1. [北方稀土官网](http://www.cnre.com.cn)
2. [北方稀土 2025 年度可持续发展报告](https://www.cnfin.com/announ/detail/index.html?id=835475261499&code=600111)
3. [中国北方稀土上交所公告](http://static.sse.com.cn)

## 参考
- Wiki extraction
- 项目 Wiki：appendix-d/companies/company_china_northern_rare_earth.md

## Overview
Rare earth element supply chains are crucial materials for the humanoid robotics sector. The following content is compiled from the project Wiki for in-depth reference.

## Content
## China Northern Rare Earth

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 中国北方稀土（集团）高科技股份有限公司 |
| **English Name** | China Northern Rare Earth (Group) High-Tech Co., Ltd. |
| **Headquarters** | Baotou, Inner Mongolia, China |
| **Established** | 1997 (predecessor founded in 1961) |
| **Website** | [http://www.cnre.com.cn](http://www.cnre.com.cn) |
| **Supply Chain Role** | Rare earth concentrates, rare earth oxides, rare earth metals, magnetic material alloys |
| **Company Type** | Listed company (Shanghai Stock Exchange: 600111) |
| **Parent/Group** | China Northern Rare Earth Group |
| **Data Source** | Company annual reports/sustainability reports, SSE announcements |

### Company Overview

China Northern Rare Earth is one of the world's largest suppliers of light rare earths. Leveraging the rare earth resources of the Bayan Obo deposit in Baotou, it has built a full industry chain from rare earth concentrates and smelting/separation to functional materials.

The company's main products include rare earth concentrates, rare earth oxides, rare earth metals, and magnetic material precursors such as NdFeB strip-casting alloys. High-performance NdFeB permanent magnets are critical materials for servo motors and frameless torque motors in humanoid robots, and China Northern Rare Earth holds a strategically important position in upstream raw materials.

### Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Rare Earth Raw Materials | Light rare earth concentrates and oxides | Praseodymium neodymium oxide, rare earth carbonates | Permanent magnets, catalysis, hydrogen storage |
| Rare Earth Metals | Smelting and separation products | Praseodymium neodymium metal | Magnetic material alloys |
| Magnetic Material Alloys | NdFeB strip-casting alloys | NdFeB flake castings | Permanent magnet motors, magnetic assemblies |

### Representative Product/Material

#### NdFeB Strip-Casting Alloy

![Rare Earth Alloy](http://www.cnre.com.cn)

> Image source: China Northern Rare Earth official website. If the link is invalid or missing, please replace with an official public image URL.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Main Composition | Nd-Fe-B (PrNd-Fe-B) | Public information |
| Rare Earth Content | Approx. 30–32 wt% | Academic papers/industry data |
| Form | Strip/Flake | Company announcements |
| Coercivity (corresponding magnet) | Varies by grade, N52 approx. 11 kOe | Industry standards |
| Maximum Energy Product (corresponding magnet) | N52 approx. 50–53 MGOe | Industry standards |
| Operating Temperature (corresponding magnet) | N52 ≤ 80 °C | Industry standards |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: The strip-casting process refines grain size and improves magnetic performance consistency, serving as a precursor material for high-performance sintered NdFeB.

**Application Scenarios**: Drive motors for new energy vehicles, wind turbine generators, and magnetic steel for humanoid robot joint motors.

### Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations enabling long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for assembly, testing, and mass production of humanoid robots.

### Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth concentrates, Bayan Obo mineral resources, energy.
- **Downstream Customers/Applications**: NdFeB magnet manufacturers (e.g., JL Mag), new energy vehicle motor manufacturers, wind turbine OEMs.
- **Main Competitors/Peers**: China Rare Earth Group, Lynas Rare Earths, MP Materials.

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_china_northern_rare_earth`
- Material Entity: `ent_material_cnre_ndfeb_alloy`
- Key Relationship:
  - `ent_company_china_northern_rare_earth` -- `produces` --> `ent_material_cnre_ndfeb_alloy`

### References

1. [China Northern Rare Earth Official Website](http://www.cnre.com.cn)
2. [China Northern Rare Earth 2025 Sustainability Report](https://www.cnfin.com/announ/detail/index.html?id=835475261499&code=600111)
3. [China Northern Rare Earth SSE Announcements](http://static.sse.com.cn)

## 개요
희토류 원소 공급망은 휴머노이드 로봇 분야의 중요한 소재입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## 북방희토 / China Northern Rare Earth

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 기업 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 중국 북방희토(그룹) 하이테크 주식회사 |
| **영문명** | China Northern Rare Earth (Group) High-Tech Co., Ltd. |
| **본사** | 중국 내몽골 바오터우시 |
| **설립일** | 1997년 (전신은 1961년 설립) |
| **공식 사이트** | [http://www.cnre.com.cn](http://www.cnre.com.cn) |
| **공급망 단계** | 희토류 정광, 희토류 산화물, 희토류 금속, 자성재 합금 |
| **기업 속성** | 상장 기업 (상하이 증권거래소: 600111) |
| **모회사/소속 그룹** | 중국 북방희토 그룹 |
| **데이터 출처** | 회사 연차 보고서/지속 가능성 보고서, 상하이 증권거래소 공시 |

### 기업 개요

북방희토는 세계 최대의 경희토류 공급업체 중 하나로, 바오터우 바이윤어보 희토류 자원의 이점을 바탕으로 희토류 정광, 제련 분리부터 기능성 소재까지 전 산업 체인을 구축했습니다.

주요 제품으로는 희토류 정광, 희토류 산화물, 희토류 금속 및 네오디뮴 철 붕소 급속 응고 박대 합금 등의 자성재 원료가 있습니다. 고성능 네오디뮴 철 붕소 영구 자석은 휴머노이드 로봇의 서보 모터 및 프레임리스 토크 모터의 핵심 소재이며, 북방희토는 상류 원료 측면에서 중요한 전략적 위치를 차지합니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| 희토류 원료 | 경희토류 정광 및 산화물 | 산화 프라세오디뮴 네오디뮴, 탄산 희토류 | 영구 자석, 촉매, 수소 저장 |
| 희토류 금속 | 제련 분리 제품 | 프라세오디뮴 네오디뮴 금속 | 자성재 합금 |
| 자성재 합금 | 네오디뮴 철 붕소 급속 응고 박대 합금 | NdFeB 스트립 캐스팅 시트 | 영구 자석 모터, 자기 부품 |

### 대표 제품/소재

#### 네오디뮴 철 붕소 급속 응고 박대 합금 (NdFeB Strip-Casting Alloy)

![희토류 합금](http://www.cnre.com.cn)

> 이미지 출처: 북방희토 공식 사이트. 링크가 유효하지 않거나 누락된 경우, 공식 공개 이미지 URL로 대체하십시오.

| 규격 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 주요 성분 | Nd-Fe-B (프라세오디뮴 네오디뮴-철-붕소) | 공개 자료 |
| 희토류 함량 | 약 30–32 wt% | 학술 논문 / 업계 자료 |
| 형태 | 박대 / 인편 | 회사 공시 |
| 보자력 (해당 자석 기준) | 등급에 따라 다름, N52 약 11 kOe | 업계 표준 |
| 최대 자기 에너지 곱 (해당 자석 기준) | N52 약 50–53 MGOe | 업계 표준 |
| 작동 온도 (해당 자석 기준) | N52 ≤ 80 °C | 업계 표준 |
| 가격 | 미공개 | 미공개 |

**기술적 특징**: 급속 응고 박대 공정은 결정립을 미세화하고 자기 성능 일관성을 향상시켜, 고성능 소결 네오디뮴 철 붕소의 전구체 소재입니다.

**응용 시나리오**: 신에너지 자동차 구동 모터, 풍력 발전기, 휴머노이드 로봇 관절 모터 자석.

### 휴머노이드 로봇과의 연관성

- 배터리, 전력 반도체 및 첨단 소재는 휴머노이드 로봇의 장시간 구동, 고역학 성능 및 경량화를 위한 공통 기반입니다.
- 산업용 로봇 및 자동화 생산 라인은 휴머노이드 로봇의 완제품 조립, 테스트 및 양산에 재사용 가능한 제조 역량을 제공합니다.

### 공급망 위치

- **상류 핵심 부품/소재**: 희토류 정광, 바이윤어보 광산 자원, 에너지.
- **하류 고객/응용 시나리오**: 네오디뮴 철 붕소 자석재 공장 (예: 진리영구자석), 신에너지 자동차 모터 공장, 풍력 터빈 완제품 공장.
- **주요 경쟁사/벤치마크**: 중국 희토류 그룹, Lynas Rare Earths, MP Materials.

### 지식 그래프 노드 및 관계

- 기업 엔티티: `ent_company_china_northern_rare_earth`
- 소재 엔티티: `ent_material_cnre_ndfeb_alloy`
- 주요 관계:
  - `ent_company_china_northern_rare_earth` -- `produces` --> `ent_material_cnre_ndfeb_alloy`

### 참고 자료

1. [북방희토 공식 사이트](http://www.cnre.com.cn)
2. [북방희토 2025년 지속 가능성 보고서](https://www.cnfin.com/announ/detail/index.html?id=835475261499&code=600111)
3. [중국 북방희토 상하이 증권거래소 공시](http://static.sse.com.cn)
