---
$id: ent_robot_fourier_intelligence_gr_1_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Fourier Intelligence GR-1
  zh: 傅利叶智能 GR-1
  ko: Fourier Intelligence GR-1
summary:
  en: Full-size humanoid robot with 44 DoF and self-developed integrated joint actuators.
  zh: 概述 傅利叶智能 GR-1是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。
  ko: 44자유도와 자체 개발 통합 관절 액추에이터를 갖춘 전신 휨로봇.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- fourier_intelligence
- humanoid
- integrated_joint
- robot_system
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_fourier.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Fourier Intelligence GR-1
  url: https://www.fourierintelligence.com/
  date: '2023'
  accessed_at: '2026-07-01'
---

## 概述
傅利叶智能 GR-1是人形机器人领域的重要机器人系统。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 傅利叶智能 / Fourier Intelligence

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 傅利叶智能 |
| **英文名** | Fourier Intelligence |
| **总部** | 中国上海 |
| **成立时间** | 2015 年 |
| **官网** | [https://www.fftai.cn](https://www.fftai.cn) |
| **供应链环节** | 整机 OEM / 康复机器人 + 通用人形机器人 |
| **企业属性** | 康复机器人龙头向通用机器人延伸 |
| **母公司/所属集团** | 无 |
| **数据来源** | 傅利叶官网、IT之家、证券时报、动脉网 |

### 公司简介

傅利叶智能从外骨骼与康复机器人起步，逐步进入通用人形机器人领域，提出“以机器人科技赋能生活”。

2023 年发布 GR-1，被称为国内首批实现量产交付的双足人形机器人之一；2025 年发布 GR-3，定位交互陪伴型 Care-bot，强调柔肤软包与全感交互系统。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 通用人形 | 科研、导览、工业协作 | GR-1 / GR-2 | 科研教育、展厅导览、康复 |
| 陪伴人形 | 康养、陪伴、交互 | GR-3 | 养老、医疗、家庭 |
| 康复机器人 | 肢体康复训练 | ExoMotus / AnkleMotus 等 | 医院、康复中心 |

### 代表产品

#### GR-1

> 傅利叶 GR-1：请访问 [官方资料](https://www.fftai.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 165 cm | 傅利叶官网 |
| 重量 | 55 kg | 傅利叶官网 |
| 自由度 | 44 DOF | 傅利叶官网 |
| 负载/扭矩 | 最大关节扭矩 230 N·m | 傅利叶官网 |
| 速度/转速 | 步态行走 5 km/h | 傅利叶官网 |
| 续航 | 未公开 | - |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：自研 FSA 一体化执行器、6×RGB 摄像头 360° 感知、BEV+Transformer+OCC。

**应用场景**：科研教育、AI 具身本体、迎宾导览、康复辅助。

#### GR-3

> 傅利叶 GR-3：请访问 [官方资料](https://www.fftai.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 165 cm | 科创板日报 / 北京商报 |
| 重量 | 71 kg | 科创板日报 / 北京商报 |
| 自由度 | 55 DOF | 公开报道 |
| 负载/扭矩 | 12 DOF 灵巧手 | 公开报道 |
| 速度/转速 | 未公开 | - |
| 续航 | 约 3 h（双电池热插拔） | 电子发烧友网 |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：全感交互系统（听觉/视觉/触觉 31 组传感器）、柔肤软包、微表情与眼神追踪。

**应用场景**：养老陪护、儿童互动、康复机构、公共空间服务。

### 供应链位置

- **上游关键零部件/材料**：自研 FSA 一体化执行器，外购电机、减速器、传感器、软包材料。
- **下游客户/应用场景**：医院、康复中心、科研机构、康养机构。
- **主要竞争对手/对标**：优必选 Walker、特斯拉 Optimus、日本 Cyberdyne。

### 知识图谱节点与关系

- 公司实体：`ent_company_fourier`
- 产品实体：`ent_product_fourier_gr1`、`ent_product_fourier_gr3`
- 关键关系：
  - `ent_company_fourier` -- `manufactures` --> `ent_product_fourier_gr1`
  - `ent_company_fourier` -- `manufactures` --> `ent_product_fourier_gr3`
  - `ent_product_fourier_gr1` -- `uses` --> `ent_component_fourier_fsa_actuator`

### 参考资料

1. [傅利叶智能官网](https://www.fftai.cn)
2. [傅利叶 GR-1 产品页](https://www.fftai.cn/products-gr1)
3. [IT之家 – 傅利叶 GR-3 发布](https://www.ithome.com/0/810/472.htm)（同类报道）
4. [证券时报 / 科创板日报 – GR-3 报道](https://www.msn.cn/zh-cn/...)
5. [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考
- [Fourier Intelligence GR-1](https://www.fourierintelligence.com/)
- 项目 Wiki：appendix-d/companies/company_fourier.md

## 개요
Fourier Intelligence GR-1은 휴머노이드 로봇 분야의 중요한 로봇 시스템입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## Fourier Intelligence

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 기업 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 傅利叶智能 |
| **영문명** | Fourier Intelligence |
| **본사** | 중국 상하이 |
| **설립 연도** | 2015년 |
| **공식 사이트** | [https://www.fftai.cn](https://www.fftai.cn) |
| **공급망 단계** | 완제품 OEM / 재활 로봇 + 범용 휴머노이드 로봇 |
| **기업 속성** | 재활 로봇 선두 기업이 범용 로봇으로 확장 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Fourier 공식 사이트, IT之家, 증권시보, 동맥망 |

### 기업 소개

Fourier Intelligence는 외골격 및 재활 로봇에서 시작하여 점차 범용 휴머노이드 로봇 분야로 진출하며, "로봇 기술로 생활에 힘을 실어준다"는 비전을 제시했습니다.

2023년 GR-1을 출시하여 국내 최초로 양산 및 납품을 실현한 이족 보행 휴머노이드 로봇 중 하나로 꼽혔습니다. 2025년에는 GR-3를 출시하여 상호작용 및 동반형 Care-bot으로 자리매김하고, 부드러운 외피와 전감각 상호작용 시스템을 강조했습니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| 범용 휴머노이드 | 연구, 안내, 산업 협력 | GR-1 / GR-2 | 연구 교육, 전시 안내, 재활 |
| 동반 휴머노이드 | 건강 관리, 동반, 상호작용 | GR-3 | 요양, 의료, 가정 |
| 재활 로봇 | 사지 재활 훈련 | ExoMotus / AnkleMotus 등 | 병원, 재활 센터 |

### 대표 제품

### 공급망 위치

- **상류 핵심 부품/소재**: 자체 개발 FSA 통합 액추에이터, 외부 조달 모터, 감속기, 센서, 연질 외피 재료.
- **하류 고객/응용 시나리오**: 병원, 재활 센터, 연구 기관, 요양 기관.
- **주요 경쟁사/비교 대상**: UBTECH Walker, Tesla Optimus, 일본 Cyberdyne.

### 지식 그래프 노드 및 관계

- 기업 엔티티: `ent_company_fourier`
- 제품 엔티티: `ent_product_fourier_gr1`, `ent_product_fourier_gr3`
- 주요 관계:
  - `ent_company_fourier` -- `manufactures` --> `ent_product_fourier_gr1`
  - `ent_company_fourier` -- `manufactures` --> `ent_product_fourier_gr3`
  - `ent_product_fourier_gr1` -- `uses` --> `ent_component_fourier_fsa_actuator`

### 참고 자료

1. [Fourier Intelligence 공식 사이트](https://www.fftai.cn)
2. [Fourier GR-1 제품 페이지](https://www.fftai.cn/products-gr1)
3. [IT之家 – Fourier GR-3 출시](https://www.ithome.com/0/810/472.htm) (유사 보도)
4. [증권시보 / 과학창업판 일보 – GR-3 보도](https://www.msn.cn/zh-cn/...)
5. [부록 D.4 주요 제품 Wiki](../index-products.md)
