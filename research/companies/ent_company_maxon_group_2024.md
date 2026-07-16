---
$id: ent_company_maxon_group_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Maxon Group
  zh: Maxon
  ko: Maxon Group
summary:
  en: Swiss manufacturer of high-precision brushless DC motors, gearheads and controllers for robotics.
  zh: Maxon是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 로보틱스용 고정밀 브러시리스 DC 모터, 기어헤드 및 컨트롤러 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component_manufactur
- component_manufacturer
- controller
- gearhead
- maxon
- motor
- switzerland
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_maxon.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Maxon Group
  url: https://www.maxongroup.com/
  date: '2024'
  accessed_at: '2026-07-01'
---


## 概述
Maxon是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Maxon Motor / Maxon Motor

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Maxon Motor |
| **英文名** | Maxon Motor |
| **总部** | 瑞士 Sachseln |
| **成立时间** | 1961 |
| **官网** | [https://www.maxongroup.com](https://www.maxongroup.com) |
| **供应链环节** | 电机 / 驱动 / 精密运动控制 |
| **企业属性** | 外资品牌、瑞士上市 |
| **母公司/所属集团** | maxon Group |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

### 公司简介

全球领先的精密直流电机与驱动系统供应商，以高扭矩密度、低齿槽转矩的 brushless DC 电机著称。

Maxon Motor 提供 brushed/brushless DC 电机、齿轮箱、编码器和控制器，产品广泛应用于医疗、航天、机器人和工业自动化。其 EC-i 系列铁芯无刷电机因高动态响应和紧凑设计，常被用于协作机器人和人形机器人关节驱动。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| EC-i / EC 无刷电机 | 高扭矩密度伺服电机 | EC-i 40 / EC 40 | 机器人关节、AGV、医疗设备 |
| ECX SPEED / ESK 电机 | 超高速无刷电机 | ECX SPEED 16 | 手术工具、航空作动器 |

### 代表产品

#### EC-i 40 无刷直流电机 / EC-i 40 Brushless DC Motor

> EC-i 40 无刷直流电机：请访问 [官方资料](https://www.maxongroup.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø40 × 52 mm（参考） | maxon 产品页 |
| 重量 | 390 g | maxon 产品页 488607 |
| 额定功率 | 100 W | maxon 产品页 |
| 额定扭矩 | 224 mNm | maxon 产品页 |
| 堵转扭矩 | 2080 mNm | maxon 产品页 |
| 额定转速 | 4390 rpm | maxon 产品页 |
| 最高转速 | 8000 rpm | maxon 产品页 |
| 效率 | 89% | maxon 产品页 |
| 编码器 | Hall 传感器，可配编码器 | maxon 产品页 |

**技术亮点**：铁芯绕组、高扭矩密度、低齿槽转矩，适合机器人关节紧凑集成。

**应用场景**：协作机器人关节、外骨骼、AGV 驱动轮、精密自动化设备。

#### EC 40 无刷直流电机 / EC 40 Brushless DC Motor

> EC 40 无刷直流电机：请访问 [官方资料](https://www.maxongroup.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø40 mm | TraceParts |
| 重量 | 390 g | TraceParts |
| 额定功率 | 120 W | TraceParts 118896 |
| 额定扭矩 | 124 mNm | TraceParts |
| 堵转扭矩 | 1280 mNm | TraceParts |
| 额定转速 | 9280 rpm | TraceParts |
| 最高转速 | 18000 rpm | TraceParts |
| 效率 | 84% | TraceParts |
| 工作温度 | -20 ~ +125 °C | TraceParts |

**技术亮点**：高速型无刷电机，适合需要高转速与小体积的精密传动场景。

**应用场景**：医疗手持工具、光学平台、小型无人机、机器人末端执行器。

### 供应链位置

- **上游关键零部件/材料**：稀土永磁体（钕铁硼）、铜线、硅钢片、轴承、铝外壳
- **下游客户/应用场景**：协作机器人、人形机器人 OEM、医疗器械、航空航天厂商
- **主要竞争对手/对标**：Kollmorgen、汇川技术、禾川科技、鸣志电器

### 知识图谱节点与关系

- 公司实体：`ent_company_maxon`
- 产品实体：`ent_component_maxon_ec_i_40`、`ent_component_maxon_ec_40`
- 关键关系：
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_i_40`
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_40`

### 参考资料

1. [官网](https://www.maxongroup.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Maxon Group](https://www.maxongroup.com/)
- 项目 Wiki：appendix-d/companies/company_maxon.md

## 개요
Maxon은 휴머노이드 로봇 분야의 핵심 부품 제조사입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Maxon Motor |
| **영문명** | Maxon Motor |
| **본사** | 스위스 작셀른(Sachseln) |
| **설립 연도** | 1961 |
| **공식 사이트** | [https://www.maxongroup.com](https://www.maxongroup.com) |
| **공급망 단계** | 모터 / 드라이브 / 정밀 운동 제어 |
| **기업 속성** | 외자 브랜드, 스위스 상장 |
| **모회사/소속 그룹** | maxon Group |
| **데이터 출처** | 공식 사이트, 제품 매뉴얼, 공개 보고서, WAIC 2026 보도 |

### 회사 소개

글로벌 선두의 정밀 DC 모터 및 드라이브 시스템 공급업체로, 높은 토크 밀도와 낮은 코깅 토크의 브러시리스 DC 모터로 유명합니다.

Maxon Motor는 브러시/브러시리스 DC 모터, 기어박스, 엔코더 및 컨트롤러를 제공하며, 의료, 항공우주, 로봇 및 산업 자동화 분야에 널리 사용됩니다. EC-i 시리즈 철심 브러시리스 모터는 높은 동적 응답성과 컴팩트한 설계로 협동 로봇 및 휴머노이드 로봇 관절 구동에 자주 사용됩니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|-----------|----------|-----------|-----------|
| EC-i / EC 브러시리스 모터 | 고토크 밀도 서보 모터 | EC-i 40 / EC 40 | 로봇 관절, AGV, 의료 기기 |
| ECX SPEED / ESK 모터 | 초고속 브러시리스 모터 | ECX SPEED 16 | 수술 도구, 항공 액추에이터 |

### 대표 제품

#### EC-i 40 브러시리스 DC 모터 / EC-i 40 Brushless DC Motor

> EC-i 40 브러시리스 DC 모터: [공식 자료](https://www.maxongroup.com)를 방문하세요.

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 크기 | Ø40 × 52 mm (참고) | maxon 제품 페이지 |
| 무게 | 390 g | maxon 제품 페이지 488607 |
| 정격 출력 | 100 W | maxon 제품 페이지 |
| 정격 토크 | 224 mNm | maxon 제품 페이지 |
| 구속 토크 | 2080 mNm | maxon 제품 페이지 |
| 정격 속도 | 4390 rpm | maxon 제품 페이지 |
| 최대 속도 | 8000 rpm | maxon 제품 페이지 |
| 효율 | 89% | maxon 제품 페이지 |
| 엔코더 | 홀 센서, 엔코더 옵션 가능 | maxon 제품 페이지 |

**기술 하이라이트**: 철심 권선, 높은 토크 밀도, 낮은 코깅 토크로 로봇 관절의 컴팩트한 통합에 적합합니다.

**적용 분야**: 협동 로봇 관절, 외골격, AGV 구동 휠, 정밀 자동화 장비.

#### EC 40 브러시리스 DC 모터 / EC 40 Brushless DC Motor

> EC 40 브러시리스 DC 모터: [공식 자료](https://www.maxongroup.com)를 방문하세요.

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 크기 | Ø40 mm | TraceParts |
| 무게 | 390 g | TraceParts |
| 정격 출력 | 120 W | TraceParts 118896 |
| 정격 토크 | 124 mNm | TraceParts |
| 구속 토크 | 1280 mNm | TraceParts |
| 정격 속도 | 9280 rpm | TraceParts |
| 최대 속도 | 18000 rpm | TraceParts |
| 효율 | 84% | TraceParts |
| 작동 온도 | -20 ~ +125 °C | TraceParts |

**기술 하이라이트**: 고속형 브러시리스 모터로, 높은 회전 속도와 작은 부피가 필요한 정밀 전동 시나리오에 적합합니다.

**적용 분야**: 의료용 핸드헬드 도구, 광학 플랫폼, 소형 드론, 로봇 엔드 이펙터.

### 공급망 위치

- **상류 핵심 부품/소재**: 희토류 영구 자석(네오디뮴 자석), 구리선, 규소 강판, 베어링, 알루미늄 하우징
- **하류 고객/적용 분야**: 협동 로봇, 휴머노이드 로봇 OEM, 의료 기기, 항공우주 제조사
- **주요 경쟁사/비교 대상**: Kollmorgen, 汇川技术(Inovance), 禾川科技(Hcfa), 鸣志电器(Moons')

### 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_maxon`
- 제품 엔티티: `ent_component_maxon_ec_i_40`, `ent_component_maxon_ec_40`
- 주요 관계:
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_i_40`
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_40`

### 참고 자료

1. [공식 사이트](https://www.maxongroup.com)
2. [WAIC 2026 전시 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 보고서](https://www.inovance.com) (실제 제품 모델에 따라 확인 필요)
