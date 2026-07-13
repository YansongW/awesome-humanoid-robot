---
id: ent_product_sanhua_actuator
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 三花智控 仿生机器人机电执行器
  en: Sanhua Bionic Robot Electromechanical Actuator
status: active
sources:
- id: src_sanhua_2025_report
  type: website
  url: https://finance.sina.com.cn/stock/relnews/cn/2025-03-31/doc-inerqfen1007904.shtml
- id: src_sanhua_163_capacity
  type: website
  url: https://www.163.com/dy/article/KDNDAS3E05568W0A.html?spss=dy_author
- id: src_sanhua_qq_goldman
  type: website
  url: https://view.inews.qq.com/a/20251112A01DMB00
- id: src_sanhua_eeo_thailand
  type: website
  url: http://www.eeo.com.cn/2026/0405/828781.shtml
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 三花智控 仿生机器人机电执行器 / Sanhua Bionic Robot Electromechanical Actuator

## 概述

三花智控（Sanhua Intelligent Controls）依托其在制冷空调控制元器件、新能源汽车热管理系统及精密制造领域的技术积累，积极布局人形机器人仿生机电执行器（Bionic Robot Electromechanical Actuator）。该执行器产品主要面向人形机器人关节，集成伺服电机、减速机构、编码器、控制器与传感器，形成一体化旋转或线性执行单元。截至 2024–2025 年公开披露信息，三花智控已与国内外多家头部人形机器人企业开展合作，并在泰国、墨西哥等地规划相应产能。

## 工作原理 / 技术架构

仿生机器人机电执行器本质为一体化关节模组，其功能是将电能转换为可控的机械运动。典型旋转执行器由永磁同步电机、谐波减速器/行星减速器、双编码器、力矩传感器与驱动控制器组成；线性执行器则通过电机驱动丝杠/滚柱丝杠将旋转运动转换为直线运动。

旋转执行器输出力矩可写为：

$$
\tau_{\text{out}} = \eta \, N \, \tau_{\text{motor}}
$$

其中 $N$ 为减速比，$\eta$ 为传动效率。线性执行器输出推力为：

$$
F_{\text{out}} = \frac{2\pi \, \eta \, \tau_{\text{motor}}}{p}
$$

$p$ 为丝杠导程。控制器通过 FOC 与阻抗/导纳控制算法实现关节的位置、速度与力矩闭环，并支持整机运动控制指令。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 产品类型 | 一体化仿生机器人机电执行器（旋转/线性） |
| 额定功率 | 未公开 |
| 峰值扭矩 | 未公开 |
| 减速机构 | 谐波减速器 / 行星减速器 / 滚柱丝杠（依具体型号） |
| 电机类型 | 永磁同步电机（PMSM） |
| 编码器 | 多圈绝对值编码器 / 双编码器（未公开具体型号） |
| 力矩/力传感器 | 可选配六维力/力矩传感器 |
| 控制接口 | CAN / EtherCAT / 私有协议（未公开） |
| 冷却方式 | 自然冷却或强制风冷（未公开） |
| 应用对象 | 人形机器人肩、肘、髋、膝、踝等关节 |
| 量产规划 | 泰国、墨西哥等海外基地（媒体报道） |

## 应用场景

- 人形机器人全身关节驱动，实现站立、行走、操作等动作；
- 协作机器人与工业机械臂关节模组；
- 仿生机器人、四足机器人高动态关节；
- 新能源汽车执行机构与智能底盘部件（公司既有业务延伸）。

## 供应链关系

`ent_product_sanhua_actuator` 由 `ent_company_sanhua`（浙江三花智控股份有限公司）研发与制造，属于人形机器人整机下游的核心子系统/产品节点。其上游依赖 `ent_component_delta_ecma` 等伺服电机、`ent_component_heidenhain_eqi_1131` 等编码器、谐波减速器、力矩传感器、轴承、壳体与控制器 PCB；向下供应给人形机器人整机厂商。三花智控同时是 `ent_product_sanhua_thermal_management` 等热管理产品线的制造商，具备为机器人提供热管理+执行器集成方案的潜力。

## 来源与验证

- 新浪财经报道称，三花智控 2024 年年报披露其聚焦仿生机器人机电执行器，继续配合客户进行全系列产品研发、试制、迭代、送样，并积极布局海外生产。
- 网易号文章梳理了三花智控 2024 年 1 月与杭州钱塘新区签订《三花智控未来产业中心项目投资协议书》，计划总投资不低于 38 亿元建设机器人机电执行器和域控制器研发及生产基地。
- 腾讯新闻援引高盛研报指出，三花智控在泰国购买约 20 万平方米土地专项用于仿人机器人执行器组装，并已启动泰国基地产能。
- 经济观察网报道，三花智控泰国春武里府人形机器人零部件工厂已于 2026 年 2 月获批，主要生产机电执行器；墨西哥工厂已于 2025 年三季度投产。
- 由于三花智控未公开执行器的额定功率、峰值扭矩、减速比、质量等具体性能参数，表中相应项标注为“未公开”，未作臆测。