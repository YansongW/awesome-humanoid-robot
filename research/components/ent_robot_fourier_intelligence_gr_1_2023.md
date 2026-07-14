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
  zh: 全尺寸人形机器人，44自由度，自研一体化关节执行器。
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
傅利叶智能 GR-1是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

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

