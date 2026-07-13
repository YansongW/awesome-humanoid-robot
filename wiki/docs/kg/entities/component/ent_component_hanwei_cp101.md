---
id: ent_component_hanwei_cp101
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 汉威科技 CP101 柔性微压力传感器
  en: Hanwei Technology CP101 Flexible Micro-Pressure Sensor
status: active
sources:
- id: src_ent_component_hanwei_cp101_1
  type: website
  url: https://www.hanwei.cn/product/cp101rxcgq/
- id: src_ent_component_hanwei_cp101_2
  type: website
  url: http://mp.weixin.qq.com/s?__biz=MzA5NjYyNDQwMQ==&mid=2650361566&idx=2&sn=c3754fc30615d2da47023191acbdc66d
- id: src_ent_component_hanwei_cp101_3
  type: website
  url: https://www.hanwei.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 汉威科技 CP101 柔性微压力传感器 / Hanwei Technology CP101 Flexible Micro-Pressure Sensor

## 概述

汉威科技 CP101 是一款基于柔性纳米功能材料的微压力传感器，厚度不足 0.3 mm，可贴附于复杂曲面，用于模拟人类皮肤的触觉感知能力。该传感器能够检测 5 mN 至 10 N 范围内的法向压力，响应时间低于 100 ms，输出为电阻/电流型信号，主要应用于智能机器人电子皮肤、灵巧手触觉、可穿戴设备、医疗健康监测及人机交互界面。CP101 由汉威科技集团（深交所：300007）生产，该公司在气体传感器与柔性触觉传感器领域处于国内领先地位。

## 工作原理 / 技术架构

CP101 采用压阻式传感机理：柔性敏感层中嵌入导电纳米材料网络，当外界压力 $F$ 作用于有效面积 $A$ 时，材料产生形变并引起导电通路变化，从而导致电阻 $R$ 改变。压力与电阻变化的关系可近似表示为

$$
\frac{\Delta R}{R_0} = GF \cdot \varepsilon = GF \cdot \frac{\Delta L}{L}
$$

其中 $GF$ 为应变因子，$R_0$ 为无负载原始阻值。传感器输出端在恒定测试电压 $V$ 下产生电流 $I = V/R$，通过测量电流变化即可反演接触压力 $p = F/A$。汉威科技公开数据显示 CP101 灵敏度可达 0.1 kPa，能够感知约 0.1 g 的微力刺激。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 传感器类型 | 柔性微压力传感器（压阻式） | 汉威官网 |
| 测量压力范围 | 5 mN – 10 000 mN（5 mN – 10 N） | 汉威官网 |
| 测试电压 | DC 0.1 – 4 V | 汉威官网 |
| 输出电流 | 10 μA – 30 mA | 汉威官网 |
| 原始阻值 | 2 – 5 kΩ | 汉威官网 |
| 响应时间 | ＜ 100 ms | 汉威官网 |
| 灵敏度 | 约 0.1 kPa（公开研报） | 行业研报 |
| 传感点密度 | 可集成约 100 个传感点/cm² | 公开研报 |
| 厚度 | ＜ 0.3 mm | 公开研报 |
| 弯折寿命 | ＞ 100 万次 | 公开研报 |
| 工作温度 | 16 – 55 °C | 汉威官网 |
| 工作湿度 | ＜ 80% RH | 汉威官网 |
| 稳定性 | 疲劳测试 50 万次 | 汉威官网 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人电子皮肤**：覆盖机器人手指、手掌、手臂等接触区域，实现抓取力反馈与碰撞检测。
- **智能机器人灵巧手**：用于鸡蛋、豆腐等易损物品的“零损伤”抓取，支持力控与滑移检测。
- **可穿戴设备**：脉搏、心率、足底压力等生理信号监测。
- **医疗健康**：假肢触觉反馈、康复训练压力分布测量。

## 供应链关系

- **制造商**：汉威科技集团股份有限公司 / Hanwei Technology（`ent_company_hanwei`）。
- **上游关键零部件/材料**：纳米敏感材料、柔性基材（PI/PET）、导电油墨、MEMS 工艺、封装材料。
- **下游客户/应用场景**：人形机器人整机厂、智能机器人灵巧手厂商、可穿戴设备商、医疗康复设备商。
- **竞争/对标**：柯力传感柔性压力产品、福莱新材、他山科技、慧闻科技、国际厂商如 Tekscan、Pressure Profile Systems。
- **知识图谱关系**：`ent_company_hanwei` — `manufactures` → `ent_component_hanwei_cp101`；`ent_component_hanwei_cp101` — `used_in` → `ent_product_humanoid_robot_skin`。

## 来源与验证

1. [汉威科技 CP101 柔性微压力传感器官方产品页](https://www.hanwei.cn/product/cp101rxcgq/)
2. [汉威科技柔性触觉传感器技术分析（公众号文章）](http://mp.weixin.qq.com/s?__biz=MzA5NjYyNDQwMQ==&mid=2650361566&idx=2&sn=c3754fc30615d2da47023191acbdc66d)
3. [汉威科技官网](https://www.hanwei.cn)
4. [附录 D 企业 Wiki：汉威科技](../../../appendices/appendix-d/companies/company_hanwei.md)