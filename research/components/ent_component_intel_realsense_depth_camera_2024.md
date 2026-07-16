---
$id: ent_component_intel_realsense_depth_camera_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Intel RealSense Depth Camera
  zh: Intel RealSense 深度相机
  ko: Intel RealSense 깊이 칩차
summary:
  en: RGB-D stereo camera widely used for head, wrist, and torso perception in humanoids.
  zh: Intel RealSense 深度相机是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。
  ko: 휨로봇의 머리, 손목, 몸통 인식에 널리 사용되는 RGB-D 스테레오 칩차.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- camera
- component
- depth
- realsense
- sensor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_intel.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Intel RealSense Depth Camera
  url: https://www.intelrealsense.com/
  date: '2024'
  accessed_at: '2026-07-02'
---


## 概述
Intel RealSense 深度相机是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 英特尔 / Intel

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 英特尔 |
| **英文名** | Intel |
| **总部** | 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 1968 |
| **官网** | [https://www.intel.com](https://www.intel.com) |
| **供应链环节** | 深度视觉传感器、计算平台、AI 推理硬件 |
| **企业属性** | 上市公司（NASDAQ: INTC）、跨国半导体与计算企业 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、产品 datasheet、第三方评测 |

### 公司简介

Intel 是全球最大的半导体与计算平台公司之一，其 RealSense 系列深度相机在机器人视觉与学术研究中拥有广泛生态。

Intel RealSense 产品线覆盖立体视觉、结构光、LiDAR 等多种深度感知技术，提供集成 RGB-D、IMU 与视觉处理器的模块化方案。产品被广泛应用于服务机器人、AMR、工业检测、3D 扫描与虚拟现实等领域，并依托开源 librealsense SDK 与 ROS/ROS 2 社区形成完整开发者生态。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RealSense D400 系列 | 立体深度相机 | D455 / D435i / D405 | 机器人导航、避障、SLAM、3D 扫描 |
| RealSense D500 / 新平台 | 新一代深度感知 | D515 / D555 等 | 增强现实、数字孪生、智能设备 |

### 代表产品

#### Intel RealSense D455

> Intel RealSense D455：请访问 [官方资料](https://www.intel.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 124 mm × 26 mm × 29 mm | 官方 datasheet |
| 重量 | 约 120 g | 第三方评测 |
| 深度技术 | 主动 IR 立体视觉 | 官方 datasheet |
| 深度 FOV | 87° × 58° | 官方 datasheet |
| 深度分辨率/帧率 | 最高 1280×720 @ 90 fps | 官方 datasheet |
| RGB 分辨率 | 最高 1280×800 @ 30 fps | 官方 datasheet |
| 理想量程 | 0.6 m – 6 m | 官方 datasheet |
| 深度精度 | <2% @ 4 m | 官方 datasheet |
| IMU | 集成 6 轴 IMU | 官方 datasheet |
| 接口 | USB-C 3.1 Gen 1 | 官方 datasheet |
| 价格 | 约 USD 299 | 公开市场参考 |

**技术亮点**：95 mm 基线、全局快门、集成 IMU、宽视场角，适合室内外机器人导航与动态场景感知。

**应用场景**：人形机器人头部/躯干视觉、AMR 避障、3D 扫描、工业检测、学术研究。

#### Intel RealSense D435i

> Intel RealSense D435i：请访问 [官方资料](https://www.intel.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 90 mm × 25 mm × 25 mm | 官方 datasheet |
| 重量 | 约 72 g | 第三方评测 |
| 深度技术 | 主动 IR 立体视觉 | 官方 datasheet |
| 深度 FOV | 87° × 58° | 官方 datasheet |
| 深度分辨率/帧率 | 最高 1280×720 @ 90 fps | 官方 datasheet |
| RGB 分辨率 | 最高 1920×1080 @ 30 fps | 官方 datasheet |
| 理想量程 | 0.1 m – 10 m | 官方 datasheet |
| 深度精度 | <2% @ 2 m | 官方 datasheet |
| IMU | 集成 Bosch BMI055 | 官方 datasheet |
| 接口 | USB-C 3.1 | 官方 datasheet |
| 价格 | 约 USD 199 | 公开市场参考 |

**技术亮点**：体积更小、成本更低，集成 IMU，适合对尺寸和预算敏感的机器人平台。

**应用场景**：无人机、小型 AMR、协作机器人视觉、教育与研究。

### 供应链位置

- **上游关键零部件/材料**：CMOS 图像传感器、红外激光器、视觉处理器 ASIC、光学镜片
- **下游客户/应用场景**：服务机器人、AMR/AGV、人形机器人、工业检测、3D 扫描设备、科研教育机构
- **主要竞争对手/对标**：奥比中光、Stereolabs、Azure Kinect、海康机器人、图漾科技

### 知识图谱节点与关系

- 公司实体：`ent_company_intel`
- 产品实体：`ent_component_intel_realsense_d455`
- 产品实体：`ent_component_intel_realsense_d435i`
- 关键关系：
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d455`
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d435i`

### 参考资料

1. [官网](https://www.intel.com)
2. [产品资料与公开报道](https://www.intel.com)
3. [附录 D 产品目录](../index-products.md)

## 参考
- [Intel RealSense Depth Camera](https://www.intelrealsense.com/)
- 项目 Wiki：appendix-d/companies/company_intel.md

## 개요
Intel RealSense 깊이 카메라는 휴머노이드 로봇 분야의 중요한 부품입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## 인텔 / Intel

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 기업 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 인텔 |
| **영문명** | Intel |
| **본사** | 미국 캘리포니아주 산타클라라 |
| **설립 연도** | 1968 |
| **공식 웹사이트** | [https://www.intel.com](https://www.intel.com) |
| **공급망 단계** | 깊이 시각 센서, 컴퓨팅 플랫폼, AI 추론 하드웨어 |
| **기업 속성** | 상장 기업 (NASDAQ: INTC), 다국적 반도체 및 컴퓨팅 기업 |
| **모회사/소속 그룹** | 독립 상장 |
| **데이터 출처** | 공식 웹사이트, 제품 데이터시트, 서드파티 평가 |

### 기업 소개

Intel은 세계 최대의 반도체 및 컴퓨팅 플랫폼 기업 중 하나이며, RealSense 시리즈 깊이 카메라는 로봇 비전 및 학술 연구 분야에서 광범위한 생태계를 보유하고 있습니다.

Intel RealSense 제품 라인은 스테레오 비전, 구조광, LiDAR 등 다양한 깊이 인식 기술을 포괄하며, RGB-D, IMU 및 비전 프로세서를 통합한 모듈식 솔루션을 제공합니다. 이 제품은 서비스 로봇, AMR, 산업 검사, 3D 스캐닝 및 가상 현실 등 다양한 분야에 널리 사용되며, 오픈 소스 librealsense SDK 및 ROS/ROS 2 커뮤니티를 기반으로 완전한 개발자 생태계를 형성하고 있습니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| RealSense D400 시리즈 | 스테레오 깊이 카메라 | D455 / D435i / D405 | 로봇 내비게이션, 장애물 회피, SLAM, 3D 스캐닝 |
| RealSense D500 / 신규 플랫폼 | 차세대 깊이 인식 | D515 / D555 등 | 증강 현실, 디지털 트윈, 스마트 기기 |

### 대표 제품

### 공급망 위치

- **상류 핵심 부품/소재**: CMOS 이미지 센서, 적외선 레이저, 비전 프로세서 ASIC, 광학 렌즈
- **하류 고객/응용 시나리오**: 서비스 로봇, AMR/AGV, 휴머노이드 로봇, 산업 검사, 3D 스캐닝 장비, 연구 교육 기관
- **주요 경쟁사/대응 기업**: 오비중광, Stereolabs, Azure Kinect, 하이크로봇, 투양테크놀로지

### 지식 그래프 노드 및 관계

- 기업 엔티티: `ent_company_intel`
- 제품 엔티티: `ent_component_intel_realsense_d455`
- 제품 엔티티: `ent_component_intel_realsense_d435i`
- 주요 관계:
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d455`
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d435i`

### 참고 자료

1. [공식 웹사이트](https://www.intel.com)
2. [제품 자료 및 공개 보도](https://www.intel.com)
3. [부록 D 제품 목록](../index-products.md)
