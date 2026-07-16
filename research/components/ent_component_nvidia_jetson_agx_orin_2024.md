---
$id: ent_component_nvidia_jetson_agx_orin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: NVIDIA Jetson AGX Orin
  zh: NVIDIA Jetson AGX Orin
  ko: NVIDIA Jetson AGX Orin
summary:
  en: Onboard GPU/ARM SoC widely used for VLA inference and perception in humanoid robots.
  zh: NVIDIA Jetson AGX Orin是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。
  ko: 휨로봇 VLA 추론 및 인식에 널리 사용되는 온보드 GPU/ARM SoC.
domains:
- 02_components
- 08_software_middleware
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- agx_orin
- component
- compute
- gpu
- jetson
- nvidia
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_jetson_agx_orin.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: NVIDIA Jetson AGX Orin
  url: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/
  date: '2024'
  accessed_at: '2026-07-02'
---


## 概述
NVIDIA Jetson AGX Orin是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## NVIDIA Jetson AGX Orin

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [NVIDIA / 英伟达](../companies/company_nvidia.md) |
| **产品类别** | 边缘 AI 计算模组 |
| **发布时间** | 2022 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [NVIDIA Jetson Orin 页面](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) |

### 产品概述

NVIDIA Jetson AGX Orin 是面向自主机器、机器人与边缘 AI 的高性能计算模组，AI 算力最高可达 275 TOPS（64 GB 版本），是上代 Jetson AGX Xavier 的 8 倍以上。模组采用 NVIDIA Ampere 架构 GPU、Arm Cortex-A78AE CPU 与新一代深度学习/视觉加速器，支持多路高分辨率摄像头、激光雷达、IMU 等传感器的高速接口。

Jetson AGX Orin 有 64 GB、32 GB 与工业版三个版本，功耗可在 15 W 至 60 W 之间配置，满足从低功耗移动机器人到高负载工业设备的不同需求。其统一的 JetPack SDK、Isaac ROS 与 Isaac Sim 生态，使其成为人形机器人、AMR、无人机与自动驾驶原型开发的主流计算平台。

### 产品图片

> NVIDIA Jetson AGX Orin：请访问 [官方资料](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 100 mm × 87 mm（模组） | NVIDIA 官网 |
| AI 算力 | 最高 275 TOPS（64 GB） | NVIDIA 官网 |
| GPU | 2048 核 NVIDIA Ampere 架构 GPU，64 个 Tensor Core | NVIDIA 官网 |
| CPU | 12 核 Arm Cortex-A78AE v8.2 | NVIDIA 官网 |
| 内存 | 64 GB / 32 GB LPDDR5，204.8 GB/s | NVIDIA 官网 |
| DL 加速器 | 2× NVDLA v2 | NVIDIA 官网 |
| 视觉加速器 | 1× PVA v2 | NVIDIA 官网 |
| 摄像头接口 | 16 通道 MIPI CSI-2 | NVIDIA 官网 |
| 功耗 | 15 W – 60 W（可配置） | NVIDIA 官网 |
| 价格 | 未公开（开发者套件约 1,999 USD） | 第三方参考 |

### 供应链位置

- **制造商**：[NVIDIA / 英伟达](../companies/company_nvidia.md)
- **核心零部件/技术来源**：自研 Ampere GPU、Arm CPU、NVDLA、PVA；存储、PMIC、载板由合作伙伴提供。
- **下游应用/客户**：人形机器人、AMR/AGV、无人机、工业视觉、自动驾驶原型、科研教育。

### 知识图谱节点与关系

- 零部件实体：`ent_component_nvidia_jetson_agx_orin`
- 制造商实体：`ent_company_nvidia`
- 关键关系：
  - `rel_ent_company_nvidia_manufactures_ent_component_nvidia_jetson_agx_orin`（`ent_company_nvidia` → `manufactures` → `ent_component_nvidia_jetson_agx_orin`）

### 应用场景

- **人形机器人大脑**：运行 VLM/VLA 模型、SLAM、动态避障与灵巧手控制。
- **AMR/AGV**：多摄像头、激光雷达融合感知与路径规划。
- **工业视觉检测**：边缘端实时缺陷检测、目标识别与测量。
- **自动驾驶原型**：乘用车与无人车的感知与决策验证平台。

### 竞争对比

| 对比项 | Jetson AGX Orin | Jetson Orin NX | Jetson AGX Xavier |
|--------|-----------------|----------------|-------------------|
| AI 算力 | 最高 275 TOPS | 最高 157 TOPS | 32 TOPS |
| 功耗 | 15–60 W | 10–40 W | 10–30 W |
| 内存 | 64 GB LPDDR5 | 16 GB LPDDR5 | 16 GB LPDDR4 |
| 核心优势 | 最高性能、统一生态 | 尺寸小、性价比高 | 成熟稳定 |

### 参考资料

1. [NVIDIA Jetson Orin 官方页面](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)
2. [NVIDIA Jetson AGX Orin Developer Kit](https://developer.nvidia.com/embedded/jetson-agx-orin-developer-kit)
3. [与非网 – 人形机器人主芯片对比](https://www.eefocus.com/article/1821462.html)
4. [CSDN – Jetson 系列算力对比](https://blog.csdn.net/qq_43298381/article/details/144167933)

## 参考
- [NVIDIA Jetson AGX Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/)
- 项目 Wiki：appendix-d/products/product_jetson_agx_orin.md

## 개요
NVIDIA Jetson AGX Orin은 휴머노이드 로봇 분야의 중요한 부품입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 자세한 내용을 확인할 수 있습니다.

## 핵심 내용
### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [NVIDIA / 엔비디아](../companies/company_nvidia.md) |
| **제품 카테고리** | 엣지 AI 컴퓨팅 모듈 |
| **출시일** | 2022년 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [NVIDIA Jetson Orin 페이지](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) |

### 제품 개요

NVIDIA Jetson AGX Orin은 자율 기계, 로봇 및 엣지 AI를 위한 고성능 컴퓨팅 모듈로, AI 연산 성능은 최대 275 TOPS(64 GB 버전)에 달하며, 이전 세대 Jetson AGX Xavier보다 8배 이상 향상되었습니다. 이 모듈은 NVIDIA Ampere 아키텍처 GPU, Arm Cortex-A78AE CPU 및 차세대 딥러닝/비전 가속기를 탑재하고 있으며, 다중 고해상도 카메라, 라이다, IMU 등 센서의 고속 인터페이스를 지원합니다.

Jetson AGX Orin은 64 GB, 32 GB 및 산업용 버전의 세 가지 버전으로 제공되며, 전력 소비는 15W에서 60W 사이로 구성 가능하여 저전력 이동 로봇부터 고부하 산업 장비까지 다양한 요구 사항을 충족합니다. 통합된 JetPack SDK, Isaac ROS 및 Isaac Sim 생태계를 통해 휴머노이드 로봇, AMR, 드론 및 자율주행 프로토타입 개발의 주요 컴퓨팅 플랫폼으로 자리 잡고 있습니다.

### 제품 이미지

> NVIDIA Jetson AGX Orin: [공식 자료](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)를 방문하여 확인하세요.

### 사양 파라미터 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 100 mm × 87 mm(모듈) | NVIDIA 공식 홈페이지 |
| AI 연산 성능 | 최대 275 TOPS(64 GB) | NVIDIA 공식 홈페이지 |
| GPU | 2048 코어 NVIDIA Ampere 아키텍처 GPU, 64개 Tensor Core | NVIDIA 공식 홈페이지 |
| CPU | 12코어 Arm Cortex-A78AE v8.2 | NVIDIA 공식 홈페이지 |
| 메모리 | 64 GB / 32 GB LPDDR5, 204.8 GB/s | NVIDIA 공식 홈페이지 |
| DL 가속기 | 2× NVDLA v2 | NVIDIA 공식 홈페이지 |
| 비전 가속기 | 1× PVA v2 | NVIDIA 공식 홈페이지 |
| 카메라 인터페이스 | 16채널 MIPI CSI-2 | NVIDIA 공식 홈페이지 |
| 전력 소비 | 15W – 60W(구성 가능) | NVIDIA 공식 홈페이지 |
| 가격 | 비공개(개발자 키트 약 1,999 USD) | 서드파티 참고 |

### 공급망 위치

- **제조사**: [NVIDIA / 엔비디아](../companies/company_nvidia.md)
- **핵심 부품/기술 출처**: 자체 개발 Ampere GPU, Arm CPU, NVDLA, PVA; 스토리지, PMIC, 캐리어 보드는 파트너사 제공.
- **하위 응용 분야/고객**: 휴머노이드 로봇, AMR/AGV, 드론, 산업용 비전, 자율주행 프로토타입, 연구 및 교육.

### 지식 그래프 노드 및 관계

- 부품 엔티티: `ent_component_nvidia_jetson_agx_orin`
- 제조사 엔티티: `ent_company_nvidia`
- 주요 관계:
  - `rel_ent_company_nvidia_manufactures_ent_component_nvidia_jetson_agx_orin`(`ent_company_nvidia` → `manufactures` → `ent_component_nvidia_jetson_agx_orin`)

### 응용 시나리오

- **휴머노이드 로봇 두뇌**: VLM/VLA 모델, SLAM, 동적 장애물 회피 및 정밀 손 제어 실행.
- **AMR/AGV**: 다중 카메라, 라이다 융합 인식 및 경로 계획.
- **산업용 비전 검사**: 엣지에서 실시간 결함 감지, 객체 인식 및 측정.
- **자율주행 프로토타입**: 승용차 및 무인 차량의 인식 및 의사 결정 검증 플랫폼.

### 경쟁 비교

| 비교 항목 | Jetson AGX Orin | Jetson Orin NX | Jetson AGX Xavier |
|--------|-----------------|----------------|-------------------|
| AI 연산 성능 | 최대 275 TOPS | 최대 157 TOPS | 32 TOPS |
| 전력 소비 | 15–60 W | 10–40 W | 10–30 W |
| 메모리 | 64 GB LPDDR5 | 16 GB LPDDR5 | 16 GB LPDDR4 |
| 핵심 장점 | 최고 성능, 통합 생태계 | 소형 크기, 가성비 우수 | 성숙하고 안정적 |

### 참고 자료

1. [NVIDIA Jetson Orin 공식 페이지](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)
2. [NVIDIA Jetson AGX Orin Developer Kit](https://developer.nvidia.com/embedded/jetson-agx-orin-developer-kit)
3. [EEFOCUS – 휴머노이드 로봇 메인 칩 비교](https://www.eefocus.com/article/1821462.html)
4. [CSDN – Jetson 시리즈 연산 성능 비교](https://blog.csdn.net/qq_43298381/article/details/144167933)
