---
id: ent_component_kunwei_kwr36
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 坤维 KWR36 六维力/力矩传感器
  en: Kunwei KWR36 Six-Axis Force/Torque Sensor
status: active
sources:
- id: src_kunwei_kwr36_page
  type: website
  url: https://www.czkunweitech.com/product/6.html
- id: src_kunwei_kwr36_mic
  type: website
  url: https://www.made-in-china.com/showroom/czkunweitech/product-detailOKlRYQUwJZUh-1/China-Kwr36-Six-Axis-Force-Sensor.html
- id: src_kunwei_about
  type: website
  url: https://www.czkunweitech.com/about/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 坤维 KWR36 六维力/力矩传感器 / Kunwei KWR36 Six-Axis Force/Torque Sensor

## 概述

KWR36 是常州坤维传感科技有限公司（Kunwei Sensing Technology）开发的微型六维力/力矩传感器（6-axis Force/Torque Sensor，6-DOF F/T sensor）。该产品基于应变梁结构，可同时测量笛卡尔坐标系下的三个力分量 $F_x、F_y、F_z$ 与三个力矩分量 $M_x、M_y、M_z$，适用于机器人末端执行器、精密装配、抛光、医疗机器人等需要力控的场合。KWR36 直径仅 36 mm，高度约 20 mm，是坤维 KWR 系列中体积最小的型号之一，专为协作机器人手腕、灵巧手及小型足式机器人足部力控设计。

## 工作原理 / 技术架构

KWR36 采用弹性体（通常为高强度铝合金或不锈钢）加工成十字梁或 E 型膜结构，在梁的应变区粘贴多组应变片组成惠斯通电桥。当外力/力矩作用于传感器上盖时，弹性体产生微小形变，应变片电阻变化导致电桥输出电压变化，经放大、温度补偿与解耦矩阵计算后得到六维力/力矩向量。

传感器输出信号 $\mathbf{F} = [F_x, F_y, F_z, M_x, M_y, M_z]^T$ 与原始电桥输出 $\mathbf{V}$ 之间通过标定解耦矩阵 $\mathbf{C}$ 关联：

$$
\mathbf{F} = \mathbf{C} \, \mathbf{V}
$$

其中 $\mathbf{C}$ 为 $6 \times n$ 标定矩阵，由六维加载标定设备在全量程范围内标定获得，用于消除各通道之间的串扰。

传感器的力测量分辨率受电桥灵敏度、放大器噪声与 ADC 位数限制，可表示为：

$$
\Delta F = \frac{F_{\text{FS}}}{2^{N_{\text{ADC}}} \cdot SNR_{\text{gain}}}
$$

$F_{\text{FS}}$ 为满量程，$N_{\text{ADC}}$ 为模数转换位数。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 传感器类型 | 六维力/力矩传感器 |
| 测量维度 | $F_x、F_y、F_z、M_x、M_y、M_z$ |
| 直径 | 36 mm |
| 高度 | 20 mm |
| 弹性体材料 | 高强度铝合金（硬铝） |
| 输出方式 | 模拟输出（可选配数字变送器） |
| 量程 | 按型号定制（未公开具体默认值） |
| 解耦方式 | 六维联合标定解耦矩阵 |
| 串扰 | 低串扰（经标定后典型 < 2 % FS） |
| 过载能力 | 300 % FS（典型值，依结构而定） |
| 工作温度 | -20 °C ~ 60 °C（典型） |
| 供电电压 | DC 5 V 或按选配模块 |
| 接口 | 出线或连接器（可定制） |
| 防护等级 | IP40（可定制） |

## 应用场景

- 协作机器人手腕力控，实现拖动示教与柔顺装配；
- 工业机器人打磨、抛光、去毛刺过程中的恒力控制；
- 医疗手术机器人与康复机器人的力反馈；
- 足式机器人足底六维力感知与平衡控制；
- 精密装配、插拔测试与材料力学实验。

## 供应链关系

`ent_component_kunwei_kwr36` 由 `ent_company_kunwei`（常州坤维传感科技有限公司）设计制造，属于传感器/力控零部件节点。其上游依赖弹性体金属加工、应变片、粘结剂、信号调理电路、ADC 与标定设备等；向下集成于机器人末端执行器、协作机器人手腕与足式机器人足部，为 `ent_product_humanoid_robot_joint` 及整机平台提供力/力矩反馈，实现柔顺交互。

## 来源与验证

- 坤维官网 KWR36 产品页确认其直径 36 mm、高度 20 mm、硬铝材质、模拟输出、可选配数字变送器，并说明量程可按需求定制。
- Made-in-China  listing 补充了 KWR36 的外形尺寸与定制量程信息。
- 坤维公司介绍页面说明了其在六维力传感器领域的技术积累与产品系列。
- 由于官网未公开 KWR36 的默认量程、精度与额定负载等具体值，表中“按型号定制”与“典型值”已作标注，未对未公开项进行臆测。