---
$id: ent_component_harmonic_reducer_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Harmonic Reducer
  zh: 谐波减速器
  ko: Harmonic Reducer
summary:
  en: Compact precision gearbox with high reduction ratio and near-zero backlash, widely used in robot rotary joints.
  zh: 谐波减速器（Harmonic Drive）是一种基于柔性齿轮弹性变形原理的精密减速装置，由波发生器（Wave Generator）、柔性齿轮（Flexspline）和刚性内齿圈（Circular Spline）组成。其核心优势为零背隙、高减速比、高扭矩密度和高定位精度，广泛应用于工业机器人、协作机器人、人形机器人关节、数控机床转台、半导体设备及医疗机器人。
  ko: 고감속비와 근접 제로 백래시를 가진 컴팩트한 정밀 기어박스, 로봇 회전 관절에 널리 사용.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- gearbox
- harmonic_reducer
- precision
- rotary_joint
- strain_wave
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from kg/entities/ent_component_harmonic_drive.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Harmonic Reducer
  url: https://en.wikipedia.org/wiki/Harmonic_drive
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
谐波减速器是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 谐波减速器 / Harmonic Drive

### 概述

谐波减速器（Harmonic Drive）是一种基于柔性齿轮弹性变形原理的精密减速装置，由波发生器（Wave Generator）、柔性齿轮（Flexspline）和刚性内齿圈（Circular Spline）组成。其核心优势为零背隙、高减速比、高扭矩密度和高定位精度，广泛应用于工业机器人、协作机器人、人形机器人关节、数控机床转台、半导体设备及医疗机器人。

### 工作原理与技术架构

波发生器为椭圆形凸轮，外圈装有薄壁轴承；其旋转使柔性齿轮发生周期性椭圆变形。柔性齿轮外齿与刚性内齿圈啮合，由于两者齿数相差通常 2 齿，柔性齿轮每转一周，相对刚轮只转过 2 个齿距，从而实现大减速比。

减速比可表示为：

$$
i = \frac{N_f}{N_c - N_f}
$$

其中 $N_c$ 为刚轮齿数，$N_f$ 为柔轮齿数。以 CSF-32-100-2UH 为例，$i=100:1$。

输出转矩与输入转矩的关系为：

$$
T_{\text{out}} = i \cdot T_{\text{in}} \cdot \eta
$$

其中 $\eta$ 为传动效率，谐波减速器典型效率约为 80%–90%。扭转刚度通常用分段线性模型描述：在 $T_1$ 以内为 $K_1$，$T_1$–$T_2$ 之间为 $K_2$，大于 $T_2$ 为 $K_3$。

### 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 代表型号 | CSF-32-100-2UH | Harmonic Drive Systems |
| 规格尺寸 | Size 32 | 外径约 110 mm |
| 减速比 | 30:1 – 160:1（系列范围） | 本表取 100:1 |
| 额定扭矩 L10 | 137 N·m | CSF-32-100-2UH |
| 平均扭矩限值 | 216 N·m | — |
| 反复峰值扭矩 | 333 N·m | — |
| 瞬时峰值扭矩 | 647 N·m | — |
| 最高输入转速 | 3500 rpm | — |
| 标准精度 | ≤1 arcmin | — |
| 背隙 | 接近零 | 谐波传动特性 |
| 扭转刚度 K1/K2/K3 | 67,000 / 110,000 / 120,000 N·m/rad | — |
| 允许弯矩负载 | 313 N·m | — |
| 径向动态承载 | 15,000 N | — |
| 重量 | 3.2 kg | CSF-32-100-2UH |
| 润滑 | 专用润滑脂 | — |
| 价格 | 未公开 | 需询价 |

### 应用场景

- **工业机器人**：六轴机器人腕部、小臂关节的高精度减速。
- **协作机器人与人形机器人**：肩部、肘部、髋部、腕部关节的力矩放大与精密定位。
- **数控机床**：第四/五轴转台、分度头。
- **半导体与医疗**：晶圆转台、手术机器人关节。

### 供应链关系

- **主要制造商**：Harmonic Drive Systems（日本）、绿的谐波（Leaderdrive，中国）、来福谐波（Laifu，中国）等。
- **上游关键物料**：合金钢（柔轮/刚轮）、交叉滚子轴承、专用润滑脂、铝壳。
- **下游集成**：工业机器人 OEM、人形机器人整机厂、数控机床厂、半导体设备商、医疗机器人厂商。
- **知识图谱关系**：
  - `ent_company_harmonic_drive` — `manufactures` → `ent_component_harmonic_drive`
  - `ent_product_estun_robot` — `uses` → `ent_component_harmonic_drive`

### 来源与验证

- Harmonic Drive Systems 官网为品牌与产品系列来源。
- Electromate 产品页给出 CSF-32-50-2A-GR 的尺寸、重量（0.89 kg）、减速比 50:1、最大连续扭矩 76 N·m、最高输入转速 7000 rpm、精度 <1 arcmin。
- Tradebearings 技术规格页给出 CSF-32-100-2UH 的额定扭矩 137 N·m、反复峰值扭矩 333 N·m、瞬时峰值扭矩 647 N·m、扭转刚度、允许弯矩及重量 3.2 kg。
- 附录 D Wiki 确认了谐波减速器在机器人关节中的供应链位置。

## 参考
- [Harmonic Reducer](https://en.wikipedia.org/wiki/Harmonic_drive)
- 项目 Wiki：kg/entities/ent_component_harmonic_drive.md

## Overview
Harmonic drives are a critical component in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Harmonic Drive

### Overview

A harmonic drive is a precision reduction device based on the principle of elastic deformation of a flexible gear. It consists of a wave generator, a flexspline, and a circular spline. Its core advantages include zero backlash, high reduction ratio, high torque density, and high positioning accuracy. It is widely used in industrial robots, collaborative robots, humanoid robot joints, CNC machine tool rotary tables, semiconductor equipment, and medical robots.

### Working Principle and Technical Architecture

The wave generator is an elliptical cam with a thin-walled bearing on its outer circumference; its rotation causes periodic elliptical deformation of the flexspline. The external teeth of the flexspline mesh with the internal teeth of the circular spline. Since the tooth count difference between the two is typically 2 teeth, for each full rotation of the flexspline, it advances only 2 tooth pitches relative to the circular spline, thereby achieving a large reduction ratio.

The reduction ratio can be expressed as:

$$
i = \frac{N_f}{N_c - N_f}
$$

where $N_c$ is the number of teeth on the circular spline and $N_f$ is the number of teeth on the flexspline. Taking the CSF-32-100-2UH as an example, $i=100:1$.

The relationship between output torque and input torque is:

$$
T_{\text{out}} = i \cdot T_{\text{in}} \cdot \eta
$$

where $\eta$ is the transmission efficiency. The typical efficiency of a harmonic drive is approximately 80%–90%. Torsional stiffness is usually described by a piecewise linear model: $K_1$ within $T_1$, $K_2$ between $T_1$ and $T_2$, and $K_3$ above $T_2$.

### Key Parameter Table

| Parameter | Value/Range | Notes |
|-----------|-------------|-------|
| Representative Model | CSF-32-100-2UH | Harmonic Drive Systems |
| Size | Size 32 | Outer diameter approx. 110 mm |
| Reduction Ratio | 30:1 – 160:1 (series range) | 100:1 used in this table |
| Rated Torque L10 | 137 N·m | CSF-32-100-2UH |
| Average Torque Limit | 216 N·m | — |
| Repeated Peak Torque | 333 N·m | — |
| Instantaneous Peak Torque | 647 N·m | — |
| Maximum Input Speed | 3500 rpm | — |
| Standard Accuracy | ≤1 arcmin | — |
| Backlash | Near zero | Characteristic of harmonic drive |
| Torsional Stiffness K1/K2/K3 | 67,000 / 110,000 / 120,000 N·m/rad | — |
| Allowable Moment Load | 313 N·m | — |
| Radial Dynamic Load Capacity | 15,000 N | — |
| Weight | 3.2 kg | CSF-32-100-2UH |
| Lubrication | Special grease | — |
| Price | Not disclosed | Requires inquiry |

### Application Scenarios

- **Industrial Robots**: High-precision reduction in the wrists and forearm joints of six-axis robots.
- **Collaborative Robots and Humanoid Robots**: Torque amplification and precision positioning in shoulder, elbow, hip, and wrist joints.
- **CNC Machine Tools**: Fourth/fifth-axis rotary tables and indexing heads.
- **Semiconductor and Medical**: Wafer rotary tables and surgical robot joints.

### Supply Chain Relationships

- **Major Manufacturers**: Harmonic Drive Systems (Japan), Leaderdrive (China), Laifu (China), etc.
- **Key Upstream Materials**: Alloy steel (flexspline/circular spline), cross roller bearings, special grease, aluminum housing.
- **Downstream Integration**: Industrial robot OEMs, humanoid robot integrators, CNC machine tool manufacturers, semiconductor equipment suppliers, medical robot manufacturers.
- **Knowledge Graph Relationships**:
  - `ent_company_harmonic_drive` — `manufactures` → `ent_component_harmonic_drive`
  - `ent_product_estun_robot` — `uses` → `ent_component_harmonic_drive`

### Sources and Verification

- The Harmonic Drive Systems official website is the source for the brand and product series.
- The Electromate product page provides dimensions, weight (0.89 kg), reduction ratio 50:1, maximum continuous torque 76 N·m, maximum input speed 7000 rpm, and accuracy <1 arcmin for the CSF-32-50-2A-GR.
- The Tradebearings technical specification page provides the rated torque of 137 N·m, repeated peak torque of 333 N·m, instantaneous peak torque of 647 N·m, torsional stiffness, allowable moment load, and weight of 3.2 kg for the CSF-32-100-2UH.
- Appendix D Wiki confirms the supply chain position of harmonic drives in robot joints.

## 개요
하모닉 드라이브는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## 하모닉 드라이브 / Harmonic Drive

### 개요

하모닉 드라이브(Harmonic Drive)는 유연 기어의 탄성 변형 원리를 기반으로 한 정밀 감속 장치로, 웨이브 제너레이터(Wave Generator), 플렉스 스플라인(Flexspline), 리지드 서큘러 스플라인(Circular Spline)으로 구성됩니다. 핵심 장점은 제로 백래시, 높은 감속비, 높은 토크 밀도 및 높은 위치 정밀도로, 산업용 로봇, 협동 로봇, 휴머노이드 로봇 관절, CNC 공작 기계 턴테이블, 반도체 장비 및 의료 로봇에 널리 사용됩니다.

### 작동 원리 및 기술 구조

웨이브 제너레이터는 타원형 캠으로, 외부에 박벽 베어링이 장착되어 있습니다. 회전 시 플렉스 스플라인에 주기적인 타원 변형을 발생시킵니다. 플렉스 스플라인의 외부 치형은 리지드 서큘러 스플라인과 맞물리며, 두 기어의 치수 차이는 일반적으로 2개입니다. 플렉스 스플라인이 한 바퀴 회전할 때마다 서큘러 스플라인에 대해 2개의 피치만 회전하므로 큰 감속비를 구현합니다.

감속비는 다음과 같이 표현됩니다.

$$
i = \frac{N_f}{N_c - N_f}
$$

여기서 $N_c$는 서큘러 스플라인의 치수, $N_f$는 플렉스 스플라인의 치수입니다. CSF-32-100-2UH를 예로 들면, $i=100:1$입니다.

출력 토크와 입력 토크의 관계는 다음과 같습니다.

$$
T_{\text{out}} = i \cdot T_{\text{in}} \cdot \eta
$$

여기서 $\eta$는 전달 효율이며, 하모닉 드라이브의 일반적인 효율은 약 80%–90%입니다. 비틀림 강성은 일반적으로 구분 선형 모델로 설명됩니다. $T_1$ 이내에서는 $K_1$, $T_1$–$T_2$ 사이에서는 $K_2$, $T_2$ 초과 시 $K_3$입니다.

### 주요 파라미터 표

| 파라미터 항목 | 값/범위 | 비고 |
|--------|-----------|------|
| 대표 모델 | CSF-32-100-2UH | Harmonic Drive Systems |
| 규격 크기 | Size 32 | 외경 약 110 mm |
| 감속비 | 30:1 – 160:1 (시리즈 범위) | 본 표는 100:1 기준 |
| 정격 토크 L10 | 137 N·m | CSF-32-100-2UH |
| 평균 토크 한계 | 216 N·m | — |
| 반복 피크 토크 | 333 N·m | — |
| 순간 피크 토크 | 647 N·m | — |
| 최대 입력 회전 속도 | 3500 rpm | — |
| 표준 정밀도 | ≤1 arcmin | — |
| 백래시 | 거의 0에 가까움 | 하모닉 드라이브 특성 |
| 비틀림 강성 K1/K2/K3 | 67,000 / 110,000 / 120,000 N·m/rad | — |
| 허용 굽힘 모멘트 하중 | 313 N·m | — |
| 반경 방향 동적 하중 | 15,000 N | — |
| 무게 | 3.2 kg | CSF-32-100-2UH |
| 윤활 | 전용 그리스 | — |
| 가격 | 비공개 | 문의 필요 |

### 적용 분야

- **산업용 로봇**: 6축 로봇 손목, 소매 관절의 고정밀 감속.
- **협동 로봇 및 휴머노이드 로봇**: 어깨, 팔꿈치, 엉덩이, 손목 관절의 토크 증폭 및 정밀 위치 제어.
- **CNC 공작 기계**: 4/5축 턴테이블, 인덱싱 헤드.
- **반도체 및 의료**: 웨이퍼 턴테이블, 수술 로봇 관절.

### 공급망 관계

- **주요 제조사**: Harmonic Drive Systems (일본), 绿的谐波 (Leaderdrive, 중국), 来福谐波 (Laifu, 중국) 등.
- **상류 핵심 자재**: 합금강 (플렉스 스플라인/서큘러 스플라인), 크로스 롤러 베어링, 전용 그리스, 알루미늄 하우징.
- **하류 통합**: 산업용 로봇 OEM, 휴머노이드 로봇 완제품 제조사, CNC 공작 기계 제조사, 반도체 장비 업체, 의료 로봇 제조사.
- **지식 그래프 관계**:
  - `ent_company_harmonic_drive` — `manufactures` → `ent_component_harmonic_drive`
  - `ent_product_estun_robot` — `uses` → `ent_component_harmonic_drive`

### 출처 및 검증

- Harmonic Drive Systems 공식 웹사이트는 브랜드 및 제품 시리즈 출처입니다.
- Electromate 제품 페이지는 CSF-32-50-2A-GR의 크기, 무게(0.89 kg), 감속비 50:1, 최대 연속 토크 76 N·m, 최대 입력 회전 속도 7000 rpm, 정밀도 <1 arcmin을 제공합니다.
- Tradebearings 기술 사양 페이지는 CSF-32-100-2UH의 정격 토크 137 N·m, 반복 피크 토크 333 N·m, 순간 피크 토크 647 N·m, 비틀림 강성, 허용 굽힘 모멘트 및 무게 3.2 kg을 제공합니다.
- 부록 D Wiki는 로봇 관절에서 하모닉 드라이브의 공급망 위치를 확인합니다.
