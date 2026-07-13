---
id: ent_component_hanwei_znx01
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 汉威 ZNX-01 柔性薄膜压力传感器
  en: Hanwei ZNX-01 Flexible Pressure Sensor
status: active
sources:
- id: src_hanwei_znx01_page
  type: website
  url: https://www.hwsensor.com/product/ZNX-01.html
- id: src_sensorexpert_znx01
  type: website
  url: https://www.sensorexpert.com.cn/product/znx01-flexible-pressure-sensor/
- id: src_hanwei_group_about
  type: website
  url: https://www.hwsensor.com/about/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 汉威 ZNX-01 柔性薄膜压力传感器 / Hanwei ZNX-01 Flexible Pressure Sensor

## 概述

ZNX-01 是汉威科技集团（Hanwei Electronics Group）旗下苏州能斯达电子科技有限公司推出的柔性薄膜压力传感器。该传感器基于压阻效应，采用纳米功能材料与柔性印刷工艺制造，厚度小于 0.5 mm，可贴附于复杂曲面，广泛应用于智能鞋垫、可穿戴设备、医疗健康、机器人触觉与工业检测等领域。

## 工作原理 / 技术架构

ZNX-01 为电阻式柔性压力传感器。传感层由纳米复合材料构成，未受压时材料内部导电网络稀疏，电阻较高；受压后导电通路增加，电阻随压力增大而降低。通过检测电阻变化即可反推压力大小。

电阻变化与压力的关系通常用经验幂律或分段线性模型近似：

$$
R(P) = R_0 \left(1 + k \, P\right)^{-1}
$$

其中 $R_0$ 为无负载电阻，$P$ 为施加压力，$k$ 为材料灵敏度系数。实际应用中需通过标定将电阻-压力曲线映射为力值。

对于圆形感测点，若接触面积为 $A$，则平均接触压力：

$$
P = \frac{F}{A}
$$

$F$ 为施加力。由于传感薄膜极薄，其力学耦合对机器人灵巧手或足部的顺应性影响很小。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 传感器类型 | 电阻式柔性薄膜压力传感器 |
| 厚度 | ≤ 0.45 mm |
| 量程（单点） | 0 ~ 10 kg |
| 响应点 | ≤ 400 g |
| 响应时间 | < 1 ms |
| 恢复时间 | < 15 ms |
| 重复性 | 良好（百万次以上循环） |
| 工作温度 | -20 °C ~ 60 °C |
| 供电电压 | DC 3.3 V（典型） |
| 输出信号 | 电阻变化，需配合分压/惠斯通电桥读取 |
| 封装形式 | 柔性 PET/PI 基底，可定制外形与阵列 |
| 接口 | FPC 引线或引线焊接 |

## 应用场景

- 机器人触觉：灵巧手抓取力反馈、足底压力分布检测；
- 智能鞋垫：步态分析、运动医学与康复评估；
- 可穿戴健康监测：心率、呼吸、体位压力检测；
- 汽车座椅：乘客存在检测与坐姿识别；
- 工业压力分布：模具贴合、密封性检测。

## 供应链关系

`ent_component_hanwei_znx01` 由汉威科技集团（`ent_company_hanwei`）通过子公司苏州能斯达电子科技研发与制造，属于柔性传感器/触觉感知零部件。其上游包括柔性基材（PET/PI）、纳米导电材料、银浆电极、FPC 等；向下直接应用于机器人灵巧手、智能鞋垫、医疗可穿戴与汽车座椅等整机或模组，可为 `ent_product_humanoid_robot_joint` 等执行单元提供接触力反馈，也可集成于人形机器人足部压力感知系统。

## 来源与验证

- 汉威科技集团官网 ZNX-01 产品页列出厚度 ≤0.45 mm、量程 10 kg、响应点 ≤400 g、响应/恢复时间、工作温度、循环寿命等核心参数。
- Sensor Expert 平台同样收录了 ZNX-01 的关键技术指标，与官方数据一致。
- 汉威科技集团官网关于页面说明了传感器业务布局及子公司能斯达的柔性传感器产品。
- 本条目未对未公开的灵敏度曲线、标定系数等参数进行臆测。