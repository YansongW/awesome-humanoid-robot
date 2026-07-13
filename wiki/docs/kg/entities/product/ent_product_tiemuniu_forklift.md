---
id: ent_product_tiemuniu_forklift
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 铁木牛无人叉车
  en: Tiemuniu Autonomous Forklift
status: active
sources:
- id: src_tiemuniu_promat2025
  type: article
  url: https://www.mybull.com/MediaCoverage/info.aspx?itemid=185
- title: 铁木牛智能机器科技有限公司 ProMAT 2025 报道
- id: src_tiemuniu_zhihu_promat
  type: article
  url: https://zhuanlan.zhihu.com/p/33117655309
- title: 铁木牛完美收官 2025 ProMAT
- id: src_tiemuniu_cemat2024
  type: article
  url: https://www.zhineng518.com/page119?article_id=9744&brd=1
- title: 聚焦 CeMAT 2024：铁木牛三大产品
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 铁木牛无人叉车 / Tiemuniu Autonomous Forklift

## 概述

铁木牛无人叉车是铁木牛机器人（MyBull）推出的室内外一体化无人驾驶平衡重叉车，可在仓库、工厂、物流园、机场、码头等场景完成货架存取、托盘堆码、牵引车接驳装卸等任务。该叉车基于多传感器融合定位导航与 3D-SLAM 技术，无需铺设磁条或反光板即可实现厘米级定位，并支持防爆等场景定制。

## 工作原理 / 技术架构

铁木牛无人叉车采用“多源感知 + 融合定位 + 运动规划”架构：

1. **感知层**：多线激光雷达、单线激光、视觉相机、超声波、光电与碰撞传感器共同感知托盘、货物与周围环境。
2. **定位层**：融合多线激光雷达、RTK-GNSS、IMU 惯性导航实现厘米级全局定位；3D-SLAM 构建并更新环境地图。
3. **决策与控制层**：基于感知结果自主完成找货、叉货、运货、放货、堆货等动作；通过 TS-R 机器人管控系统实现多机调度。
4. **安全层**：三层安全防护设计，包括自动报警、碰撞检测、坡道防溜坡与坡道辅助起步。

叉车负载能力可表示为额定起重量 $Q$ 与载荷重心距 $c$ 的关系，稳定性需满足

$$
Q\,c \le M_{\text{stab}},
$$

其中 $M_{\text{stab}}$ 为整车抗倾覆力矩。铁木牛公开资料中主要以 2 吨无人驾驶平衡重叉车为例。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 产品类型 | 室内外一体化无人驾驶平衡重叉车 |
| 额定负载（示例） | 2 T |
| 导航方式 | 多线激光雷达 + RTK + IMU + 视觉融合 |
| 定位精度 | 厘米级 |
| 叉取重复精度 | 高（具体数值未公开） |
| 工作场景 | 室内 / 室外一体化 |
| 防护选项 | 防爆认证（Ex） |
| 调度系统 | TS-R 机器人管控系统 / MaaS 运维 |
| 最大速度 / 爬坡能力 | 未公开 |
| 续航时间 | 未公开 |

## 应用场景

- **仓储物流**：货架存取、托盘堆码、入库出库。
- **汽车制造**：产线物料转运、牵引车接驳。
- **机场港口**：行李/集装箱水平搬运。
- **化工/能源**：防爆场景下的危险品搬运。
- **黑灯工厂**：与无人牵引车、平板车协同实现全流程无人化运输。

## 供应链关系

- **上游**：激光雷达、GNSS/RTK 模块、IMU、驱动电机、电池、控制器、叉车本体结构件供应商。
- **同层**：铁木牛机器人提供整车硬件、定位导航算法（“路霸”PNS）与调度软件，形成“云-管-端”无人物流方案。
- **下游**：物流仓储运营商、汽车/化工/港口等终端企业。

## 来源与验证

- 铁木牛 ProMAT 2025 官方报道：https://www.mybull.com/MediaCoverage/info.aspx?itemid=185
- 知乎 ProMAT 总结：https://zhuanlan.zhihu.com/p/33117655309
- CeMAT 2024 报道：https://www.zhineng518.com/page119?article_id=9744&brd=1