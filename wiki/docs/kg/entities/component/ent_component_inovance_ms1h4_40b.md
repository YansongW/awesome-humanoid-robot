---
id: ent_component_inovance_ms1h4_40b
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 汇川 MS1H4-40B30CB 伺服电机
  en: Inovance MS1H4-40B30CB Servo Motor
sources:
- id: src_inovance_official
  type: website
- title: '"Inovance 官网"'
  url: https://www.inovance.com
- id: src_inovance_alibaba
  type: website
- title: '"INOVANCE MS1H4-40B30CB 产品页"'
  url: https://www.alibaba.com/product-detail/Inovance-MS1H4-40B30CB-A331R-Servo-Motor_1601600478163.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 汇川 MS1H4-40B30CB 伺服电机 / Inovance MS1H4-40B30CB Servo Motor

## 概述

MS1H4-40B30CB 是汇川技术 MS1 系列小惯量伺服电机，机座号 40 mm，额定功率 400 W，额定转速 3000 rpm，搭配 SV660/SV680 系列伺服驱动器，适用于机器人小关节、SCARA、协作机器人手臂及 3C 自动化高速定位场景。

## 工作原理 / 技术架构

电机为永磁同步伺服电机（PMSM），转子采用稀土永磁材料，定子由变频器供电产生旋转磁场。额定扭矩与功率、转速的关系为：

$$T_{\text{rated}} = \frac{60 P_{\text{rated}}}{2\pi n_{\text{rated}}} = \frac{9.55 P_{\text{rated}}}{n_{\text{rated}}}$$

代入 400 W、3000 rpm 可得 $T_{\text{rated}} \approx 1.27\,\text{N·m}$。H4 机型最大转矩约为额定转矩的 3.5 倍，峰值约 4.4 N·m。编码器采用多圈绝对值编码器（18 位），断电后可保存位置，无需回零。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 机座号 | 40 mm | 汇川手册 |
| 额定功率 | 400 W | 汇川/经销商资料 |
| 额定转速 | 3000 rpm | 汇川手册 |
| 最高转速 | 6000 rpm | 汇川官网 |
| 额定扭矩 | 1.27 N·m | 经销商公开资料 |
| 最大扭矩 | 约 3.5 倍额定扭矩 | 汇川手册 |
| 转子惯量 | 0.43 kg·cm² | 汇川手册 |
| 编码器 | 18 位多圈绝对值 | 汇川手册 |
| 防护等级 | IP67 | 汇川手册 |
| 额定电压 | 220 VAC | 经销商资料 |

## 应用场景

SCARA、协作机器人关节、人形机器人手臂、3C 自动化、锂电设备。

## 供应链关系

汇川技术（`ent_company_inovance`）制造 MS1H4-40B30CB 伺服电机，并与同厂 SV680P/SV660 伺服驱动器组成伺服系统；下游客户覆盖工业机器人、人形机器人与新能源装备厂商。

## 来源与验证

- Inovance 官网：https://www.inovance.com
- 经销商产品页：https://www.alibaba.com/product-detail/Inovance-MS1H4-40B30CB-A331R-Servo-Motor_1601600478163.html