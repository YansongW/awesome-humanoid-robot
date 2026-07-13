# Xsens MVN Link / Xsens MVN Link

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Xsens / Movella](../companies/company_xsens.md) |
| **产品类别** | 高端惯性动作捕捉套装 |
| **发布时间** | 持续迭代，当前为 MVN 系列最新代 |
| **状态** | 商用 |
| **官网/来源** | [Xsens 官网](https://xsens.com) |

## 产品概述

Xsens MVN Link 是 Movella Xsens 产品线中的旗舰惯性动作捕捉系统，采用紧身 Lycra 套装设计，内置 17 颗有线高精度 IMU 传感器，通过无线接收器与 MVN Analyze / MVN Animate 软件配合，实现全身高精度动作捕捉。

MVN Link 以磁干扰免疫、低延迟（约 20 ms）、高更新率（最高 240 Hz）和出色的户外/现场可用性著称。其 23 段、22 关节的生物力学模型可提供关节角度、质心、节段速度等完整运动学数据，定位漂移在无外部辅助时约为 1%。

在机器人领域，MVN Link 被广泛用于人形机器人运动控制验证、仿生动作数据采集、外骨骼控制研究以及人机协作安全性评估。

## 产品图片

> Xsens MVN Link：请访问 [官方资料](https://xsens.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感器数量 | 17× 有线 IMU + 1 道具传感器 | Xsens 公开规格 |
| 更新率 | 最高 240 Hz | Xsens 公开规格 |
| 延迟 | 约 20 ms | Xsens 公开规格 |
| 无线范围 | 约 150 m | Xsens 公开规格 |
| 续航 | 约 10 小时 | Xsens 公开规格 |
| 生物力学模型 | 23 段、22 关节 | Macnica Galaxy 技术资料 |
| 定位漂移 | 约 1%（无外部辅助） | Macnica Galaxy 技术资料 |
| GNSS | 可选 GPS 天线 | Xsens 公开规格 |
| 手指追踪 | 兼容 Xsens Metagloves / Manus | Xsens 公开规格 |
| 价格 | 企业询价 | 官方渠道 |

## 供应链位置

- **制造商**：[Xsens / Movella](../companies/company_xsens.md)
- **核心零部件/技术来源**：MEMS IMU 芯片、磁力计、陀螺仪、加速度计、Lycra 弹性面料、无线射频模块、传感器融合算法 IP、MVN 软件。
- **下游应用/客户**：Electronic Arts、NBC Universal、Netflix、Daimler、Siemens、500+ 职业运动队、影视工作室、科研机构、机器人公司。

## 知识图谱节点与关系

- 产品实体：`ent_product_xsens_mvn_link`
- 制造商实体：`ent_company_xsens_movella`
- 关键关系：
  - `rel_ent_company_xsens_movella_manufactures_ent_product_xsens_mvn_link`（`ent_company_xsens_movella` → `manufactures` → `ent_product_xsens_mvn_link`）

## 应用场景

- **高端影视与虚拟制作**：高保真角色动画、虚拟拍摄、实时预演。
- **职业体育生物力学**：动作技术分析、伤病预防、康复评估。
- **医学与康复研究**：步态分析、神经康复、假肢/外骨骼评估。
- **机器人运动验证**：人形机器人运动轨迹对比、控制算法验证、数字人驱动。

## 竞争对比

| 对比项 | Xsens MVN Link | Rokoko Smartsuit Pro II | Vicon（光学） |
|--------|---------------|------------------------|--------------|
| 定位 | 高端惯性动捕 | 高性价比惯性动捕 | 高端光学动捕 |
| 传感器 | 17× 有线 IMU | 17–19× 无线 IMU | 红外相机阵列 |
| 更新率 | 最高 240 Hz | 200 fps | 最高 2000+ fps |
| 使用环境 | 室内外均可 | 室内外均可 | 需要受控光照与标定场地 |
| 价格 | 企业询价 | 约 2,745 USD 起 | 较高 |

## 选购与部署建议

- 适合对数据精度、磁干扰免疫与长时间采集有严格要求的专业用户。
- 需要准确的生物力学分析时，建议配合测力台、EMG 等第三方设备同步采集。
- 用于机器人数据采集时，需根据目标机器人骨架调整 MVN 生物力学模型导出参数。

## 参考资料

1. [Xsens 官网](https://xsens.com)
2. [Movella 官网](https://movella.com)
3. [Macnica Galaxy – Xsens MVN Link 技术介绍](https://www.macnica.com/apac/galaxy/zh_tw/products-support/technical-articles/movella-xsens-mvn-link/)
4. [Xsens MVN Awinda 产品页](https://shop.movella.com/us/product-lines/motion-capture/products/xsens-mvn-awinda)