---
$id: ent_robot_system_figure_02
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Figure 02
  zh: Figure 02
  ko: 피규어 02
summary:
  en: Humanoid robot developed by Figure AI for logistics and manufacturing, featuring onboard vision-language models and
    16-degree-of-freedom hands.
  zh: 概述 Figure 02是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。
  ko: Figure AI가 물류 및 제조업용으로 개발한 휴인oid 로봇으로, 온보드 비전-언어 모델과 16자유도 손을 갖추고 있습니다.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- figure
- figure_02
- humanoid
- robot_system
- vla
- manipulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_figure_02.md by scripts/backfill_nonpaper_entries.py.
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
Figure 02是人形机器人领域的重要机器人系统。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Figure 02

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Figure AI](../companies/company_figure_ai.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2024 年 8 月 |
| **状态** | 企业试点/限量部署 |
| **官网/来源** | [Figure AI 官网](https://www.figure.ai) |

### 产品概述

Figure 02 是 Figure AI 推出的第二代通用人形机器人，面向工业制造与物流场景设计。整机采用哑光黑外观与集成式线缆布局，搭载 Figure 自研的 Helix VLA（Vision-Language-Action）AI 模型，能够在 200 Hz 频率下控制上半身，实现零样本抓取数千种未见过物体。

Figure 02 已在 BMW Spartanburg 等汽车制造基地进行实际任务验证，主要负责底盘装配、物料搬运等与人协作的工序。其双 NVIDIA RTX GPU 计算模块提供约 3 倍于 Figure 01 的端侧推理能力，6 颗 RGB 摄像头与多模态传感器支撑全天候环境感知。

### 产品图片

> Figure 02：请访问 [官方资料](https://www.figure.ai) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 168 cm（高） | 公开规格 |
| 重量 | 约 70 kg | 公开规格 |
| 自由度（整机） | 28 DOF（手部 16 DOF/对） | 公开规格 |
| 关键性能指标 | 手部负载 25 kg；整机搬运 20 kg | 公开规格 |
| 行走速度 | 约 1.2 m/s | 公开规格 |
| 续航 | 约 5 小时 | 公开规格 |
| 电池容量 | 2.25 kWh（躯干集成） | 公开规格 |
| 计算平台 | 双 NVIDIA RTX GPU 模块 | Figure AI |
| 价格 | 未公开（行业估计约 130,000 USD） | 第三方估计 |

### 供应链位置

- **制造商**：[Figure AI](../companies/company_figure_ai.md)
- **核心零部件/技术来源**：NVIDIA GPU 计算模块、自研 Helix VLA 模型、OpenAI 语音交互、6×RGB 摄像头与深度感知模块。
- **下游应用/客户**：BMW 制造基地、物流仓储、汽车装配线。

### 知识图谱节点与关系

- 产品实体：`ent_product_figure_ai_figure_02`
- 制造商实体：`ent_company_figure_ai`
- 关键关系：
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02`（`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`）

### 应用场景

- **汽车制造**：BMW Spartanburg 等基地执行底盘装配、线束安装与物料搬运。
- **仓储物流**：标准化箱体的分拣、搬运与产线补货。
- **工业协作**：与人类工人并肩完成需要灵巧双手的装配与检测任务。

### 竞争对比

| 对比项 | Figure 02 | Tesla Optimus Gen 3 | Agility Digit |
|--------|-----------|---------------------|---------------|
| 定位 | 工业制造人形 | 通用/工业人形 | 物流仓储人形 |
| AI 架构 | Helix VLA | FSD 衍生神经网络 | 专有感知/规划栈 |
| 续航 | 约 5 h | 约 2–4 h（估计） | 约 4 h |
| 核心优势 | 端侧 VLA、宝马部署、手部负载 | 制造规模目标、成本控制 | 物流部署成熟度 |

### 选购与部署建议

- Figure 02 当前以企业试点为主，建议直接联系 Figure AI 评估工厂场景可行性。
- 部署前需确认 Helix VLA 模型对目标工件的泛化能力，并规划训练数据收集流程。

### 参考资料

1. [Figure AI 官网](https://www.figure.ai)
2. [Robozaps – Figure 02 Review](https://blog.robozaps.com/b/figure-02-review)
3. [Humanoid.Guide – Figure 02](https://humanoid.guide/product/figure-02/)
4. [The Robot Report – Figure BMW Deployment](https://www.therobotreport.com)

## 参考
- [Figure AI Official Website](https://www.figure.ai/)
- [Built In — What Is Figure AI Building?](https://builtin.com/articles/figure-ai)
- 项目 Wiki：appendix-d/products/product_figure_02.md

## 개요
Figure 02는 휴머노이드 로봇 분야의 중요한 로봇 시스템입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 자세한 내용은 해당 자료를 참고하시기 바랍니다.

## 핵심 내용
### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Figure AI](../companies/company_figure_ai.md) |
| **제품 카테고리** | 범용 휴머노이드 로봇 |
| **출시일** | 2024년 8월 |
| **상태** | 기업 시범 운영/제한적 배포 |
| **공식 사이트/출처** | [Figure AI 공식 사이트](https://www.figure.ai) |

### 제품 개요

Figure 02는 Figure AI가 출시한 2세대 범용 휴머노이드 로봇으로, 산업 제조 및 물류 현장을 위해 설계되었습니다. 전체 기기는 무광 블랙 외관과 통합형 케이블 배치를 채택했으며, Figure 자체 개발 Helix VLA(비전-언어-행동) AI 모델을 탑재하여 상반기를 200Hz 주파수로 제어하며 수천 가지 미경험 물체를 제로샷으로 집을 수 있습니다.

Figure 02는 BMW Spartanburg 등 자동차 제조 현장에서 실제 작업 검증을 완료했으며, 주로 섀시 조립, 자재 운반 등 사람과 협업하는 공정을 담당합니다. 듀얼 NVIDIA RTX GPU 컴퓨팅 모듈은 Figure 01 대비 약 3배의 엣지 추론 성능을 제공하며, 6개의 RGB 카메라와 다중 모드 센서가 24시간 환경 인식을 지원합니다.

### 제품 이미지

> Figure 02: [공식 자료](https://www.figure.ai)를 방문하여 확인하세요.

### 사양 파라미터 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 168 cm(높이) | 공개 사양 |
| 무게 | 약 70 kg | 공개 사양 |
| 자유도(전체) | 28 DOF(손 16 DOF/쌍) | 공개 사양 |
| 주요 성능 지표 | 손 최대 하중 25 kg; 전체 운반 20 kg | 공개 사양 |
| 보행 속도 | 약 1.2 m/s | 공개 사양 |
| 배터리 지속 시간 | 약 5시간 | 공개 사양 |
| 배터리 용량 | 2.25 kWh(몸체 통합) | 공개 사양 |
| 컴퓨팅 플랫폼 | 듀얼 NVIDIA RTX GPU 모듈 | Figure AI |
| 가격 | 미공개(업계 추정 약 130,000 USD) | 제3자 추정 |

### 공급망 위치

- **제조사**: [Figure AI](../companies/company_figure_ai.md)
- **핵심 부품/기술 출처**: NVIDIA GPU 컴퓨팅 모듈, 자체 개발 Helix VLA 모델, OpenAI 음성 상호작용, 6×RGB 카메라 및 깊이 인식 모듈.
- **하위 응용/고객**: BMW 제조 현장, 물류 창고, 자동차 조립 라인.

### 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_figure_ai_figure_02`
- 제조사 엔터티: `ent_company_figure_ai`
- 주요 관계:
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02`(`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`)

### 응용 시나리오

- **자동차 제조**: BMW Spartanburg 등 현장에서 섀시 조립, 배선 설치 및 자재 운반 수행.
- **창고 물류**: 표준화된 상자의 분류, 운반 및 생산 라인 보충.
- **산업 협업**: 인간 작업자와 함께 정밀한 손 작업이 필요한 조립 및 검사 작업 수행.

### 경쟁 비교

| 비교 항목 | Figure 02 | Tesla Optimus Gen 3 | Agility Digit |
|--------|-----------|---------------------|---------------|
| 포지셔닝 | 산업 제조 휴머노이드 | 범용/산업 휴머노이드 | 물류 창고 휴머노이드 |
| AI 아키텍처 | Helix VLA | FSD 파생 신경망 | 전용 인식/계획 스택 |
| 배터리 지속 시간 | 약 5시간 | 약 2–4시간(추정) | 약 4시간 |
| 핵심 강점 | 엣지 VLA, BMW 배포, 손 하중 | 제조 규모 목표, 비용 관리 | 물류 배포 성숙도 |

### 구매 및 배포 권장 사항

- Figure 02는 현재 주로 기업 시범 운영 중심이므로, Figure AI에 직접 연락하여 공장 현장 적용 가능성을 평가하는 것이 좋습니다.
- 배포 전 Helix VLA 모델의 대상 작업물에 대한 일반화 능력을 확인하고, 훈련 데이터 수집 프로세스를 계획해야 합니다.

### 참고 자료

1. [Figure AI 공식 사이트](https://www.figure.ai)
2. [Robozaps – Figure 02 리뷰](https://blog.robozaps.com/b/figure-02-review)
3. [Humanoid.Guide – Figure 02](https://humanoid.guide/product/figure-02/)
4. [The Robot Report – Figure BMW 배포](https://www.therobotreport.com)
