---
$id: ent_oem_figure_ai
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: oem
names:
  en: Figure AI
  zh: Figure AI
  ko: 피규어 AI
summary:
  en: American humanoid robotics startup developing the Figure humanoid robot for logistics and manufacturing, with partnerships
    in automotive and retail.
  zh: '> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。 > 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。'
  ko: 물류 및 제조업용 Figure 휴인oid 로봇을 개발하는 미국 휴인oid 로봇 스타트업으로, 자동차 및 유통 분야와 파트너십을 맺고 있습니다.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- organization
- system
tags:
- figure
- figure_02
- humanoid
- oem
- logistics
- manufacturing
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_figure_ai.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Figure AI Official Website
  url: https://www.figure.ai/
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: website
  title: Built In — What Is Figure AI Building?
  url: https://builtin.com/articles/figure-ai
  date: '2024'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---

## 概述
Figure AI是人形机器人领域的重要整机厂商。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Figure AI / Figure AI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Figure AI |
| **英文名** | Figure AI |
| **总部** | 美国加利福尼亚州森尼韦尔 |
| **成立时间** | 2022 |
| **官网** | [https://www.figure.ai](https://www.figure.ai) |
| **供应链环节** | 人形机器人整机厂、具身智能 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | Figure AI 官网、公开融资与部署报道、第三方规格汇编 |

### 公司简介

Figure AI 是专注于通用人形机器人的初创公司，主打工业制造场景，Figure 02 已在宝马斯帕坦堡工厂进行试点。

Figure AI 自研 Helix 多模态 AI 模型，使机器人可通过自然语言指令和视觉演示学习新任务。Figure 02 拥有更高的计算与感知能力，目标是替代重复性、危险性的人工劳动。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Figure 02 人形机器人 | 工业人形 | Figure 02 | 汽车制造、物流、仓储 |
| Figure 03 人形机器人 | 新一代通用/家庭 | Figure 03 | 工业、未来家庭服务 |

### 代表产品

#### Figure 02

> Figure 02：请访问 [官方资料](https://www.figure.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 168 cm（高） | 公开资料 |
| 重量 | 约 70 kg | 公开资料 |
| 自由度 | 全身 28；手部未单独披露 | Humanoid.guide 等 |
| 负载/扭矩 | 搬运约 20–25 kg | 公开资料 |
| 速度/转速 | 约 1.2 m/s（4.32 km/h） | 公开资料 |
| 续航 | 约 5 小时 | 公开资料 |
| 接口/通信 | 双 NVIDIA GPU 计算、6×RGB 相机、语音交互 | 公开资料 |
| 价格 | 未公开（试点项目约 130,000 USD 估算） | 第三方估计 |

**技术亮点**：Helix 多模态 AI、宝马工厂部署验证、躯干集成电池、6×RGB 相机与语音交互、3 倍于 Figure 01 的算力。

**应用场景**：汽车装配线 kitting、物料搬运、仓储分拣。


#### Figure 03

> Figure 03：请访问 [官方资料](https://www.figure.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 170 cm（高） | 公开报道 |
| 重量 | 约 60–70 kg | 公开报道 |
| 自由度 | 40+；手部 16×2 | 公开报道 |
| 负载/扭矩 | 约 25 kg | 公开报道 |
| 速度/转速 | 约 1.2 m/s | 公开报道 |
| 续航 | 约 5+ 小时（2.25 kWh） | 公开报道 |
| 接口/通信 | Helix VLA 模型、语音交互 | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：更高自由度手部、面向家庭与工业的通用设计、Helix VLA 端到端推理。

**应用场景**：工业制造、未来家庭协助、零售服务。


### 供应链位置

- **上游关键零部件/材料**：NVIDIA GPU 计算、电机/减速器、传感器与电池包外购或定制。
- **下游客户/应用场景**：BMW 斯帕坦堡工厂、物流与制造企业。
- **主要竞争对手/对标**：Tesla Optimus、Boston Dynamics Atlas、Agility Robotics Digit、Apptronik Apollo。

### 知识图谱节点与关系

- 公司实体：`ent_company_figure_ai`
- 产品/平台实体：`ent_product_figure_ai_figure_02`、`ent_product_figure_ai_figure_03`
- 关键关系：
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02`（`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`）
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_03`（`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_03`）

### 参考资料

1. [Figure AI 官网](https://www.figure.ai)
2. [Humanoid.guide Figure 02 规格](https://humanoid.guide/product/figure-02/)
3. [The Robot Report 对 Figure 02 的报道](https://www.therobotreport.com/figure-02-advances-humanoid-robotics-frontier)

## 参考
- [Figure AI Official Website](https://www.figure.ai/)
- [Built In — What Is Figure AI Building?](https://builtin.com/articles/figure-ai)
- 项目 Wiki：appendix-d/companies/company_figure_ai.md

## 개요
Figure AI는 휴머노이드 로봇 분야의 주요 완성체 제조사입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Figure AI |
| **영문명** | Figure AI |
| **본사** | 미국 캘리포니아주 서니베일 |
| **설립 연도** | 2022 |
| **공식 웹사이트** | [https://www.figure.ai](https://www.figure.ai) |
| **공급망 단계** | 휴머노이드 로봇 완성체 제조사, 임베디드 인텔리전스 |
| **기업 성격** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Figure AI 공식 웹사이트, 공개된 자금 조달 및 배치 관련 보도, 제3자 사양 종합 |

### 회사 소개

Figure AI는 범용 휴머노이드 로봇에 특화된 스타트업으로, 주로 산업 제조 현장을 겨냥하고 있습니다. Figure 02는 BMW 스파르탄버그 공장에서 시범 운영 중입니다.

Figure AI는 자체 개발한 Helix 멀티모달 AI 모델을 통해 로봇이 자연어 명령과 시각적 시연을 통해 새로운 작업을 학습할 수 있도록 합니다. Figure 02는 더 높은 연산 및 인지 능력을 갖추고 있으며, 반복적이고 위험한 인간 노동을 대체하는 것을 목표로 합니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Figure 02 휴머노이드 로봇 | 산업용 휴머노이드 | Figure 02 | 자동차 제조, 물류, 창고 |
| Figure 03 휴머노이드 로봇 | 차세대 범용/가정용 | Figure 03 | 산업, 미래 가정 서비스 |

### 대표 제품

### 공급망 위치

- **상류 핵심 부품/소재**: NVIDIA GPU 연산, 모터/감속기, 센서 및 배터리 팩은 외부 구매 또는 맞춤 제작.
- **하류 고객/적용 시나리오**: BMW 스파르탄버그 공장, 물류 및 제조 기업.
- **주요 경쟁사/비교 대상**: Tesla Optimus, Boston Dynamics Atlas, Agility Robotics Digit, Apptronik Apollo.

### 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_figure_ai`
- 제품/플랫폼 엔터티: `ent_product_figure_ai_figure_02`, `ent_product_figure_ai_figure_03`
- 주요 관계:
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`)
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_03` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_03`)

### 참고 자료

1. [Figure AI 공식 웹사이트](https://www.figure.ai)
2. [Humanoid.guide Figure 02 사양](https://humanoid.guide/product/figure-02/)
3. [The Robot Report의 Figure 02 관련 보도](https://www.therobotreport.com/figure-02-advances-humanoid-robotics-frontier)
