---
$id: ent_component_six_axis_force_torque_sensor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Six Axis Force Torque Sensor
  zh: 六维力传感器
  ko: Six Axis Force Torque Sensor
summary:
  en: Sensor measuring forces and torques in all six degrees of freedom, critical for force-controlled manipulation.
  zh: 神源生 MLL 系列六维力传感器 / Shenyuansheng MLL Series 6-Axis Force Sensor
  ko: 6자유도의 힘과 토크를 측정하는 센서, 힘 제어 조작에 필수적.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- force_control
- force_torque_sensor
- sensor
- six_axis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_shenyuan_6axis_sensor.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Six Axis Force Torque Sensor
  url: https://en.wikipedia.org/wiki/Force-sensing_resistor
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
六维力传感器是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 神源生 MLL 系列六维力传感器 / Shenyuansheng MLL Series 6-Axis Force Sensor

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [神源生科技 / Shenyuansheng](../companies/company_shenyuan.md) |
| **产品类别** | 铝合金模拟量六维力/力矩传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [神源生 MLL 系列六维力传感器产品/资料页](http://www.nbit6d.com/product/687.html) |

### 产品概述

神源生 MLL 系列是针对科学仪器、精密测试及机器人应用设计的铝合金模拟量六维力传感器，可同时测量正交三方向的力与力矩。产品具有高刚度、高分辨率与低耦合误差特点，可选配 NST 系列数据采集器实现数字输出与实时分析。

### 产品图片

> 神源生 MLL 系列六维力传感器：请访问 [官方资料](http://www.nbit6d.com/product/687.html) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 铝合金模拟量六维力传感器 | 神源生官网 |
| 力测量范围（Fx/Fy/Fz） | 50 / 50 / 100 N（典型型号） | 神源生官网 |
| 力矩测量范围（Mx/My/Mz） | 2 / 2 / 4 Nm（典型型号） | 神源生官网 |
| 精度 | ≤ 0.5% FS | 神源生官网 |
| 分辨率 | 24 bit（配合采集器） | 神源生官网 |
| 过载能力 | ≥ 300% FS | 神源生官网 |
| 耦合误差 | ≤ 2% FS | 神源生官网 |
| 供电 | 5 – 24 VDC | 神源生官网 |
| 输出 | 模拟量 / USB / RS485（配采集器） | 神源生官网 |
| 采样频率 | 最高 1000 Hz | 神源生官网 |
| 工作温度 | 0℃ – +60℃ | 神源生官网 |
| 重量 | 约 200 g（因型号而异） | 神源生官网 |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[神源生科技 / Shenyuansheng](../companies/company_shenyuan.md)
- **核心零部件/技术来源**：航空铝合金、应变片、信号调理芯片、电缆与接插件
- **下游应用/客户**：协作机器人、人形机器人、医疗机器人、航空航天测试、高校科研

### 知识图谱节点与关系

- 产品实体：`ent_product_shenyuan_mll_6axis_sensor`
- 零部件实体：`ent_component_shenyuan_mll_sensor_core`
- 制造商实体：`ent_company_shenyuan`
- 关键关系：
  - `rel_ent_company_shenyuan_manufactures_ent_product_shenyuan_mll_6axis_sensor`（`ent_company_shenyuan` → `manufactures` → `ent_product_shenyuan_mll_6axis_sensor`）
  - `rel_ent_company_shenyuan_manufactures_ent_component_shenyuan_mll_sensor_core`（`ent_company_shenyuan` → `manufactures` → `ent_component_shenyuan_mll_sensor_core`）
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

### 应用场景

- **协作机器人拖动示教、人形机器人手腕/脚踝力控、医疗手术力反馈、3C 装配、科学实验**

### 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 见规格参数表 | 同类产品 | 同类产品 |
| 核心优势 | 官方公开性能指标 | 竞品公开指标 | 竞品公开指标 |
| 生态/服务 | 制造商官方支持 | 竞品生态 | 竞品生态 |

### 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

### 相关词条

- [制造商：神源生科技 / Shenyuansheng](../companies/company_shenyuan.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

### 参考资料

1. [神源生科技官网](https://www.shenyuansheng.com)
2. [神源生 MLL 系列六维力传感器产品/资料页](http://www.nbit6d.com/product/687.html)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../index-companies.md)

## 参考
- [Six Axis Force Torque Sensor](https://en.wikipedia.org/wiki/Force-sensing_resistor)
- 项目 Wiki：appendix-d/products/product_shenyuan_6axis_sensor.md

## Overview
The six-axis force sensor is an important component in the field of humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Shenyuansheng MLL Series 6-Axis Force Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Shenyuansheng Technology / Shenyuansheng](../companies/company_shenyuan.md) |
| **Product Category** | Aluminum alloy analog six-axis force/torque sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [Shenyuansheng MLL Series 6-Axis Force Sensor Product/Data Page](http://www.nbit6d.com/product/687.html) |

### Product Overview

The Shenyuansheng MLL series is an aluminum alloy analog six-axis force sensor designed for scientific instruments, precision testing, and robot applications. It can simultaneously measure forces and torques in three orthogonal directions. The product features high stiffness, high resolution, and low coupling error, and can be optionally paired with the NST series data acquisition unit for digital output and real-time analysis.

### Product Image

> Shenyuansheng MLL Series 6-Axis Force Sensor: Please visit the [official page](http://www.nbit6d.com/product/687.html) for details.

### Specification Parameter Table

| Specification Item | Value | Notes/Source |
|--------------------|-------|--------------|
| Type | Aluminum alloy analog six-axis force sensor | Shenyuansheng official website |
| Force measurement range (Fx/Fy/Fz) | 50 / 50 / 100 N (typical model) | Shenyuansheng official website |
| Torque measurement range (Mx/My/Mz) | 2 / 2 / 4 Nm (typical model) | Shenyuansheng official website |
| Accuracy | ≤ 0.5% FS | Shenyuansheng official website |
| Resolution | 24 bit (with data acquisition unit) | Shenyuansheng official website |
| Overload capacity | ≥ 300% FS | Shenyuansheng official website |
| Coupling error | ≤ 2% FS | Shenyuansheng official website |
| Power supply | 5 – 24 VDC | Shenyuansheng official website |
| Output | Analog / USB / RS485 (with data acquisition unit) | Shenyuansheng official website |
| Sampling frequency | Up to 1000 Hz | Shenyuansheng official website |
| Operating temperature | 0°C – +60°C | Shenyuansheng official website |
| Weight | Approx. 200 g (varies by model) | Shenyuansheng official website |
| Price | Not disclosed | - |

### Supply Chain Position

- **Manufacturer**: [Shenyuansheng Technology / Shenyuansheng](../companies/company_shenyuan.md)
- **Core components/technology sources**: Aviation aluminum alloy, strain gauges, signal conditioning chips, cables and connectors
- **Downstream applications/customers**: Collaborative robots, humanoid robots, medical robots, aerospace testing, university research

### Knowledge Graph Nodes and Relationships

- Product entity: `ent_product_shenyuan_mll_6axis_sensor`
- Component entity: `ent_component_shenyuan_mll_sensor_core`
- Manufacturer entity: `ent_company_shenyuan`
- Key relationships:
  - `rel_ent_company_shenyuan_manufactures_ent_product_shenyuan_mll_6axis_sensor` (`ent_company_shenyuan` → `manufactures` → `ent_product_shenyuan_mll_6axis_sensor`)
  - `rel_ent_company_shenyuan_manufactures_ent_component_shenyuan_mll_sensor_core` (`ent_company_shenyuan` → `manufactures` → `ent_component_shenyuan_mll_sensor_core`)
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

### Application Scenarios

- **Collaborative robot drag teaching, humanoid robot wrist/ankle force control, medical surgical force feedback, 3C assembly, scientific experiments**

### Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | See specification table | Similar product | Similar product |
| Core advantage | Official public performance indicators | Competitor public indicators | Competitor public indicators |
| Ecosystem/Service | Manufacturer official support | Competitor ecosystem | Competitor ecosystem |

### Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Confirm interface, power supply, heat dissipation, mechanical installation, and ambient temperature range compatibility before deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

### Related Entries

- [Manufacturer: Shenyuansheng Technology / Shenyuansheng](../companies/company_shenyuan.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

### References

1. [Shenyuansheng Technology Official Website](https://www.shenyuansheng.com)
2. [Shenyuansheng MLL Series 6-Axis Force Sensor Product/Data Page](http://www.nbit6d.com/product/687.html)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)

## 개요
6축 힘 센서는 휴머노이드 로봇 분야의 중요한 부품입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## 신위안성 MLL 시리즈 6축 힘 센서 / Shenyuansheng MLL Series 6-Axis Force Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [신위안성 기술 / Shenyuansheng](../companies/company_shenyuan.md) |
| **제품 카테고리** | 알루미늄 합금 아날로그 6축 힘/토크 센서 |
| **출시 시간** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [신위안성 MLL 시리즈 6축 힘 센서 제품/자료 페이지](http://www.nbit6d.com/product/687.html) |

### 제품 개요

신위안성 MLL 시리즈는 과학 기기, 정밀 테스트 및 로봇 응용을 위해 설계된 알루미늄 합금 아날로그 6축 힘 센서로, 직교하는 세 방향의 힘과 토크를 동시에 측정할 수 있습니다. 이 제품은 높은 강성, 높은 분해능 및 낮은 결합 오차 특성을 가지며, NST 시리즈 데이터 수집기를 선택하여 디지털 출력 및 실시간 분석을 구현할 수 있습니다.

### 제품 이미지

> 신위안성 MLL 시리즈 6축 힘 센서: [공식 자료](http://www.nbit6d.com/product/687.html)를 방문하여 확인하십시오.

### 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 알루미늄 합금 아날로그 6축 힘 센서 | 신위안성 공식 사이트 |
| 힘 측정 범위 (Fx/Fy/Fz) | 50 / 50 / 100 N (대표 모델) | 신위안성 공식 사이트 |
| 토크 측정 범위 (Mx/My/Mz) | 2 / 2 / 4 Nm (대표 모델) | 신위안성 공식 사이트 |
| 정밀도 | ≤ 0.5% FS | 신위안성 공식 사이트 |
| 분해능 | 24 bit (수집기 연동 시) | 신위안성 공식 사이트 |
| 과부하 용량 | ≥ 300% FS | 신위안성 공식 사이트 |
| 결합 오차 | ≤ 2% FS | 신위안성 공식 사이트 |
| 전원 공급 | 5 – 24 VDC | 신위안성 공식 사이트 |
| 출력 | 아날로그 / USB / RS485 (수집기 연동 시) | 신위안성 공식 사이트 |
| 샘플링 주파수 | 최대 1000 Hz | 신위안성 공식 사이트 |
| 작동 온도 | 0℃ – +60℃ | 신위안성 공식 사이트 |
| 무게 | 약 200 g (모델에 따라 다름) | 신위안성 공식 사이트 |
| 가격 | 미공개 | - |

### 공급망 위치

- **제조사**: [신위안성 기술 / Shenyuansheng](../companies/company_shenyuan.md)
- **핵심 부품/기술 출처**: 항공 알루미늄 합금, 스트레인 게이지, 신호 조정 칩, 케이블 및 커넥터
- **하류 응용/고객**: 협동 로봇, 휴머노이드 로봇, 의료 로봇, 항공우주 테스트, 대학 연구

### 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_shenyuan_mll_6axis_sensor`
- 부품 엔터티: `ent_component_shenyuan_mll_sensor_core`
- 제조사 엔터티: `ent_company_shenyuan`
- 주요 관계:
  - `rel_ent_company_shenyuan_manufactures_ent_product_shenyuan_mll_6axis_sensor` (`ent_company_shenyuan` → `manufactures` → `ent_product_shenyuan_mll_6axis_sensor`)
  - `rel_ent_company_shenyuan_manufactures_ent_component_shenyuan_mll_sensor_core` (`ent_company_shenyuan` → `manufactures` → `ent_component_shenyuan_mll_sensor_core`)
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

### 응용 시나리오

- **협동 로봇 드래그 티칭, 휴머노이드 로봇 손목/발목 힘 제어, 의료 수술 힘 피드백, 3C 조립, 과학 실험**

### 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

### 구매 및 배포 권장 사항

- 목표 응용의 분해능, 측정 범위, 정밀도 또는 연산 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전에 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

### 관련 항목

- [제조사: 신위안성 기술 / Shenyuansheng](../companies/company_shenyuan.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

### 참고 자료

1. [신위안성 기술 공식 사이트](https://www.shenyuansheng.com)
2. [신위안성 MLL 시리즈 6축 힘 센서 제품/자료 페이지](http://www.nbit6d.com/product/687.html)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
