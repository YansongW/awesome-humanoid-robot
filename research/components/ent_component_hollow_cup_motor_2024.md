---
$id: ent_component_hollow_cup_motor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Hollow Cup Motor
  zh: 空心杯电机
  ko: Hollow Cup Motor
summary:
  en: Small, lightweight coreless DC motor used in dexterous robot hands and small joints.
  zh: 鼎智空心杯电机（Dingzhi Coreless Motor）是江苏雷利电机股份有限公司子公司鼎智科技生产的微型直流伺服电机，采用无铁芯转子（空心杯）结构，具有低转动惯量、无齿槽转矩、高响应速度与低电磁干扰等特性。该产品覆盖 Ø10–Ø42
    mm 多个系列，广泛应用于人形机器人灵巧手、医疗泵阀、无人机云台、安防摄像头、光学调焦与 3D 打印机等精密驱动场景。
  ko: 작고 가벼운 코어리스 DC 모터, 능숙한 로봇 손과 소형 관절에 사용.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- coreless_motor
- dexterous_hand
- hollow_cup_motor
- miniature
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from kg/entities/ent_component_dingzhi_coreless_motor.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Hollow Cup Motor
  url: https://en.wikipedia.org/wiki/Coreless_electric_motor
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
空心杯电机是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 鼎智空心杯电机 / Dingzhi Coreless Motor

### 概述

鼎智空心杯电机（Dingzhi Coreless Motor）是江苏雷利电机股份有限公司子公司鼎智科技生产的微型直流伺服电机，采用无铁芯转子（空心杯）结构，具有低转动惯量、无齿槽转矩、高响应速度与低电磁干扰等特性。该产品覆盖 Ø10–Ø42 mm 多个系列，广泛应用于人形机器人灵巧手、医疗泵阀、无人机云台、安防摄像头、光学调焦与 3D 打印机等精密驱动场景。

### 工作原理 / 技术架构

空心杯电机的核心特征在于转子无硅钢片铁芯，绕组呈自支撑的杯状结构，置于永磁定子磁场中：

1. **无铁芯转子**：消除了传统直流电机因齿槽效应引起的转矩脉动与铁损，显著降低转动惯量。
2. **高加速度**：低惯量使电机具备极快的加减速能力，机械时间常数通常小于 5 ms。
3. **低电磁干扰**：无铁芯结构减少了磁滞损耗与涡流损耗，运行平稳、噪声低。
4. **贵金属电刷 / 碳刷换向**：有刷型号采用贵金属或碳刷换向；无刷型号则通过电子换相实现更长寿命。

电机输出扭矩与电枢电流的关系由转矩常数 $K_t$ 决定：

$$
\tau = K_t \cdot I
$$

其中 $\tau$ 为输出扭矩，$I$ 为电枢电流。堵转扭矩（stall torque）对应最大允许电流下的极限扭矩，是灵巧手手指驱动的关键指标。

### 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 鼎智科技 / Dingzhi Technology | 公司官网 |
| 母公司 | 江苏雷利电机股份有限公司（SZ.300660） | 公开资料 |
| 产品系列 | 10 / 13 / 16 / 22 / 28 / 30 / 36 / 42 系列 | 行业研报 |
| 外径范围 | Ø10–Ø42 mm | 产品手册 |
| 额定电压 | 3–48 VDC（因型号而异） | 产品手册 |
| 空载转速 | 5,000–58,000 rpm（因型号而异） | 产品手册 / 行业研报 |
| 额定转速 | 28,500–31,000 rpm（10 系列示例） | 官网产品页 |
| 额定转矩 | 1.5 mN·m（10ZWWC25 示例） | 官网产品页 |
| 堵转扭矩 | 1–50 mNm（系列范围）；峰值 4.5 mN·m（10 系列示例） | 产品手册 |
| 效率 | ≥75–80% | 产品手册 |
| 换向方式 | 贵金属电刷 / 碳刷 / 无刷电子换相 | 产品手册 |
| 绝缘等级 | B 级（示例） | 官网产品页 |
| 重量 | 5–60 g（系列范围） | 产品手册 |
| 价格 | 未公开 | 需询价 |

注：鼎智官网公开了 10 系列无刷空心杯电机的具体型号参数（如 10ZWWC25），其他系列参数以产品手册与行业研报中的范围值为准。

### 应用场景

- **人形机器人灵巧手**：作为手指关节驱动电机，提供高响应、低惯量的屈曲/伸展运动。
- **医疗采血设备与泵阀**：利用低振动、低噪声特性，应用于注射泵、采血仪、微型阀门。
- **无人机云台与摄像头**：实现快速、精准的俯仰/横滚姿态调整。
- **光学调焦与 3D 打印机**：提供精密定位与快速往复运动。
- **安防摄像头**：驱动云台旋转与镜头变焦。

### 供应链关系

鼎智科技（`ent_company_dingzhi`）是江苏雷利控股子公司，专注精密微型步进电机、线性执行器与空心杯电机。空心杯电机（`ent_component_dingzhi_coreless_motor`）与丝杆电机（`ent_component_dingzhi_lead_screw`）共同构成公司机器人相关产品线。上游原材料包括硅钢片（定子）、铜线、磁材、轴承、塑料粒子与电子元器件；下游客户涵盖医疗器械、3D 打印、人形机器人、工业自动化与汽车电子厂商。鼎智科技与鸣志电器、美蓓亚、Faulhaber、江苏雷利、拓邦股份等形成竞争。

### 来源与验证

- 鼎智科技官网展示了空心杯电机产品线及其在机器人、医疗、光学等领域的应用。
- 鼎智 DINGS 10 系列无刷空心杯电机产品页提供了 10ZWWC25 等具体型号的额定电压、转速、转矩、效率等实测参数。
- 空心杯电机行业深度研究报告系统整理了鼎智 10/16/22/28/30/36/42 系列的外径、电压、空载转速范围等参数，并对比了国内外厂商竞争格局。

## 参考
- [Hollow Cup Motor](https://en.wikipedia.org/wiki/Coreless_electric_motor)
- 项目 Wiki：kg/entities/ent_component_dingzhi_coreless_motor.md

## Overview
Coreless motors are an important component in the humanoid robot field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Dingzhi Coreless Motor

### Overview

The Dingzhi Coreless Motor is a micro DC servo motor produced by Dingzhi Technology, a subsidiary of Jiangsu Leili Motor Co., Ltd. It features a coreless rotor (hollow cup) structure, offering characteristics such as low moment of inertia, no cogging torque, high response speed, and low electromagnetic interference. The product covers multiple series from Ø10 to Ø42 mm and is widely used in precision drive scenarios such as humanoid robot dexterous hands, medical pump valves, drone gimbals, security cameras, optical focusing, and 3D printers.

### Working Principle / Technical Architecture

The core feature of the coreless motor is that the rotor has no silicon steel sheet core, and the winding forms a self-supporting cup-shaped structure placed in the magnetic field of a permanent magnet stator:

1. **Coreless Rotor**: Eliminates torque ripple and iron loss caused by the cogging effect in traditional DC motors, significantly reducing the moment of inertia.
2. **High Acceleration**: The low inertia enables extremely fast acceleration and deceleration, with a mechanical time constant typically less than 5 ms.
3. **Low Electromagnetic Interference**: The coreless structure reduces hysteresis loss and eddy current loss, resulting in smooth operation and low noise.
4. **Precious Metal / Carbon Brush Commutation**: Brushed models use precious metal or carbon brush commutation; brushless models achieve longer life through electronic commutation.

The relationship between motor output torque and armature current is determined by the torque constant $K_t$:

$$
\tau = K_t \cdot I
$$

Where $\tau$ is the output torque and $I$ is the armature current. The stall torque corresponds to the maximum torque under the maximum allowable current and is a key indicator for dexterous hand finger actuation.

### Key Parameter Table

| Parameter | Value | Notes/Source |
|-----------|-------|--------------|
| Manufacturer | Dingzhi Technology | Company website |
| Parent Company | Jiangsu Leili Motor Co., Ltd. (SZ.300660) | Public information |
| Product Series | 10 / 13 / 16 / 22 / 28 / 30 / 36 / 42 Series | Industry research reports |
| Outer Diameter Range | Ø10–Ø42 mm | Product manual |
| Rated Voltage | 3–48 VDC (varies by model) | Product manual |
| No-Load Speed | 5,000–58,000 rpm (varies by model) | Product manual / Industry research reports |
| Rated Speed | 28,500–31,000 rpm (10 series example) | Official product page |
| Rated Torque | 1.5 mN·m (10ZWWC25 example) | Official product page |
| Stall Torque | 1–50 mNm (series range); Peak 4.5 mN·m (10 series example) | Product manual |
| Efficiency | ≥75–80% | Product manual |
| Commutation Method | Precious metal brushes / Carbon brushes / Brushless electronic commutation | Product manual |
| Insulation Class | Class B (example) | Official product page |
| Weight | 5–60 g (series range) | Product manual |
| Price | Not publicly disclosed | Requires inquiry |

Note: Dingzhi's official website discloses specific model parameters for the 10 series brushless coreless motor (e.g., 10ZWWC25). Parameters for other series are based on range values from product manuals and industry research reports.

### Application Scenarios

- **Humanoid Robot Dexterous Hands**: Serves as the drive motor for finger joints, providing high-response, low-inertia flexion/extension movements.
- **Medical Blood Collection Equipment and Pump Valves**: Utilizes low vibration and low noise characteristics for use in syringe pumps, blood analyzers, and micro valves.
- **Drone Gimbals and Cameras**: Enables fast and precise pitch/roll attitude adjustments.
- **Optical Focusing and 3D Printers**: Provides precise positioning and rapid reciprocating motion.
- **Security Cameras**: Drives gimbal rotation and lens zoom.

### Supply Chain Relationships

Dingzhi Technology (`ent_company_dingzhi`) is a controlled subsidiary of Jiangsu Leili, focusing on precision miniature stepper motors, linear actuators, and coreless motors. The coreless motor (`ent_component_dingzhi_coreless_motor`) and the lead screw motor (`ent_component_dingzhi_lead_screw`) together form the company's robot-related product line. Upstream raw materials include silicon steel sheets (stator), copper wire, magnetic materials, bearings, plastic particles, and electronic components; downstream customers cover medical devices, 3D printing, humanoid robots, industrial automation, and automotive electronics manufacturers. Dingzhi Technology competes with companies such as Moons' Industries, MinebeaMitsumi, Faulhaber, Jiangsu Leili, and Topband.

### Sources and Verification

- The Dingzhi Technology official website showcases the coreless motor product line and its applications in robotics, medical, optical, and other fields.
- The Dingzhi DINGS 10 series brushless coreless motor product page provides measured parameters such as rated voltage, speed, torque, and efficiency for specific models like 10ZWWC25.
- In-depth industry research reports on coreless motors systematically organize parameters such as outer diameter, voltage, and no-load speed range for the Dingzhi 10/16/22/28/30/36/42 series, and compare the competitive landscape of domestic and international manufacturers.

## 개요
코어리스 모터는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## Dingzhi 코어리스 모터

### 개요

Dingzhi 코어리스 모터는 장쑤 레이리 전기 주식회사(Jiangsu Leili Motor Co., Ltd.)의 자회사인 Dingzhi Technology에서 생산하는 초소형 DC 서보 모터로, 무철심 회전자(코어리스) 구조를 채택하여 낮은 관성 모멘트, 무코깅 토크, 높은 응답 속도 및 낮은 전자기 간섭 등의 특성을 갖습니다. 이 제품은 Ø10–Ø42 mm의 다양한 시리즈를 포괄하며, 휴머노이드 로봇의 정교한 손, 의료용 펌프 밸브, 드론 짐벌, 보안 카메라, 광학 줌 및 3D 프린터 등 정밀 구동 분야에 널리 적용됩니다.

### 작동 원리 / 기술 아키텍처

코어리스 모터의 핵심 특징은 회전자에 규소강판 철심이 없고, 권선이 자체 지지형 컵 구조를 이루어 영구 자석 고정자 자기장 내에 위치한다는 점입니다.

1. **무철심 회전자**: 기존 DC 모터에서 코깅 효과로 인한 토크 리플과 철손을 제거하여 관성 모멘트를 현저히 낮춥니다.
2. **고가속도**: 낮은 관성으로 인해 모터는 매우 빠른 가속 및 감속 능력을 가지며, 기계적 시정수는 일반적으로 5ms 미만입니다.
3. **낮은 전자기 간섭**: 무철심 구조는 히스테리시스 손실과 와전류 손실을 줄여 안정적인 작동과 낮은 소음을 제공합니다.
4. **귀금속 브러시 / 카본 브러시 정류**: 브러시형 모델은 귀금속 또는 카본 브러시 정류를 사용하며, 브러시리스 모델은 전자적 정류를 통해 더 긴 수명을 구현합니다.

모터 출력 토크와 전기자 전류의 관계는 토크 상수 $K_t$에 의해 결정됩니다.

$$
\tau = K_t \cdot I
$$

여기서 $\tau$는 출력 토크, $I$는 전기자 전류입니다. 스톨 토크는 최대 허용 전류에서의 한계 토크에 해당하며, 정교한 손의 손가락 구동에 중요한 지표입니다.

### 주요 파라미터 표

| 파라미터 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 제조사 | Dingzhi Technology | 회사 공식 웹사이트 |
| 모회사 | 장쑤 레이리 전기 주식회사 (SZ.300660) | 공개 자료 |
| 제품 시리즈 | 10 / 13 / 16 / 22 / 28 / 30 / 36 / 42 시리즈 | 업계 보고서 |
| 외경 범위 | Ø10–Ø42 mm | 제품 매뉴얼 |
| 정격 전압 | 3–48 VDC (모델에 따라 다름) | 제품 매뉴얼 |
| 무부하 속도 | 5,000–58,000 rpm (모델에 따라 다름) | 제품 매뉴얼 / 업계 보고서 |
| 정격 속도 | 28,500–31,000 rpm (10 시리즈 예시) | 공식 웹사이트 제품 페이지 |
| 정격 토크 | 1.5 mN·m (10ZWWC25 예시) | 공식 웹사이트 제품 페이지 |
| 스톨 토크 | 1–50 mNm (시리즈 범위); 피크 4.5 mN·m (10 시리즈 예시) | 제품 매뉴얼 |
| 효율 | ≥75–80% | 제품 매뉴얼 |
| 정류 방식 | 귀금속 브러시 / 카본 브러시 / 브러시리스 전자 정류 | 제품 매뉴얼 |
| 절연 등급 | B 등급 (예시) | 공식 웹사이트 제품 페이지 |
| 무게 | 5–60 g (시리즈 범위) | 제품 매뉴얼 |
| 가격 | 미공개 | 문의 필요 |

참고: Dingzhi 공식 웹사이트는 10 시리즈 브러시리스 코어리스 모터의 구체적인 모델 파라미터(예: 10ZWWC25)를 공개했으며, 다른 시리즈의 파라미터는 제품 매뉴얼 및 업계 보고서의 범위 값을 기준으로 합니다.

### 응용 분야

- **휴머노이드 로봇 정교한 손**: 손가락 관절 구동 모터로 사용되어 높은 응답성과 낮은 관성의 굴곡/신전 운동을 제공합니다.
- **의료용 채혈 장비 및 펌프 밸브**: 낮은 진동과 낮은 소음 특성을 활용하여 주사 펌프, 채혈기, 초소형 밸브에 적용됩니다.
- **드론 짐벌 및 카메라**: 빠르고 정밀한 피치/롤 자세 조정을 구현합니다.
- **광학 줌 및 3D 프린터**: 정밀 위치 결정과 빠른 왕복 운동을 제공합니다.
- **보안 카메라**: 짐벌 회전 및 렌즈 줌을 구동합니다.

### 공급망 관계

Dingzhi Technology(`ent_company_dingzhi`)는 장쑤 레이리 전기의 자회사로, 정밀 초소형 스테핑 모터, 리니어 액추에이터 및 코어리스 모터에 특화되어 있습니다. 코어리스 모터(`ent_component_dingzhi_coreless_motor`)와 리드 스크류 모터(`ent_component_dingzhi_lead_screw`)는 함께 회사의 로봇 관련 제품 라인을 구성합니다. 상류 원자재에는 규소강판(고정자), 동선, 자석 재료, 베어링, 플라스틱 입자 및 전자 부품이 포함됩니다. 하류 고객은 의료 기기, 3D 프린팅, 휴머노이드 로봇, 산업 자동화 및 자동차 전자 제조업체를 포괄합니다. Dingzhi Technology는 Moons' Industries, MinebeaMitsumi, Faulhaber, 장쑤 레이리 전기, Topband 등과 경쟁 관계에 있습니다.

### 출처 및 검증

- Dingzhi Technology 공식 웹사이트는 코어리스 모터 제품 라인과 로봇, 의료, 광학 분야에서의 응용을 보여줍니다.
- Dingzhi DINGS 10 시리즈 브러시리스 코어리스 모터 제품 페이지는 10ZWWC25 등 구체적인 모델의 정격 전압, 속도, 토크, 효율 등 실측 파라미터를 제공합니다.
- 코어리스 모터 업계 심층 연구 보고서는 Dingzhi 10/16/22/28/30/36/42 시리즈의 외경, 전압, 무부하 속도 범위 등의 파라미터를 체계적으로 정리하고 국내외 제조업체의 경쟁 구도를 비교했습니다.
