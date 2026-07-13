---
id: ent_component_dingzhi_coreless_motor
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 鼎智空心杯电机
  en: Dingzhi Coreless Motor
sources:
- id: src_dingzhi_official
  type: website
- title: 鼎智科技官网
  url: https://www.dingzhimotion.com
- id: src_dingzhi_10_series
  type: website
- title: 鼎智 DINGS 10 系列无刷空心杯电机
  url: https://www.dingsmotion.cn/show/72-7-1.html
- id: src_coreless_motor_industry_report
  type: website
- title: 空心杯电机行业深度研究报告
  url: https://file.iyanbao.com/pdf/403f1-5b0745ad-508d-42bd-ae06-c3da1baca165.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official product pages and industry research reports;
    exact values vary by model and winding configuration.
---


# 鼎智空心杯电机 / Dingzhi Coreless Motor

## 概述

鼎智空心杯电机（Dingzhi Coreless Motor）是江苏雷利电机股份有限公司子公司鼎智科技生产的微型直流伺服电机，采用无铁芯转子（空心杯）结构，具有低转动惯量、无齿槽转矩、高响应速度与低电磁干扰等特性。该产品覆盖 Ø10–Ø42 mm 多个系列，广泛应用于人形机器人灵巧手、医疗泵阀、无人机云台、安防摄像头、光学调焦与 3D 打印机等精密驱动场景。

## 工作原理 / 技术架构

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

## 关键参数表

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

## 应用场景

- **人形机器人灵巧手**：作为手指关节驱动电机，提供高响应、低惯量的屈曲/伸展运动。
- **医疗采血设备与泵阀**：利用低振动、低噪声特性，应用于注射泵、采血仪、微型阀门。
- **无人机云台与摄像头**：实现快速、精准的俯仰/横滚姿态调整。
- **光学调焦与 3D 打印机**：提供精密定位与快速往复运动。
- **安防摄像头**：驱动云台旋转与镜头变焦。

## 供应链关系

鼎智科技（`ent_company_dingzhi`）是江苏雷利控股子公司，专注精密微型步进电机、线性执行器与空心杯电机。空心杯电机（`ent_component_dingzhi_coreless_motor`）与丝杆电机（`ent_component_dingzhi_lead_screw`）共同构成公司机器人相关产品线。上游原材料包括硅钢片（定子）、铜线、磁材、轴承、塑料粒子与电子元器件；下游客户涵盖医疗器械、3D 打印、人形机器人、工业自动化与汽车电子厂商。鼎智科技与鸣志电器、美蓓亚、Faulhaber、江苏雷利、拓邦股份等形成竞争。

## 来源与验证

- 鼎智科技官网展示了空心杯电机产品线及其在机器人、医疗、光学等领域的应用。
- 鼎智 DINGS 10 系列无刷空心杯电机产品页提供了 10ZWWC25 等具体型号的额定电压、转速、转矩、效率等实测参数。
- 空心杯电机行业深度研究报告系统整理了鼎智 10/16/22/28/30/36/42 系列的外径、电压、空载转速范围等参数，并对比了国内外厂商竞争格局。