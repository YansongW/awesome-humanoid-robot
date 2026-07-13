# 自变量 Quanta X2 / Xvariable Quanta X2

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [自变量机器人 / Xvariable / X Square Robot](../companies/company_xvariable.md) |
| **产品类别** | 通用轮式仿人形机器人 |
| **发布时间** | 2025 年 8 月 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://x2robot.com](https://x2robot.com) |

## 产品概述

工业组装、线束整理、酒店纸巾换新、晾衣服、杂物收纳、制作饮品、科研教育。

自变量 Quanta X2（量子 2 号） 是 自变量机器人 的代表产品。百亿参数 WALL-A 端到端操作大模型、全身 62 DOF、±0.03 mm 重复定位、仿人五指灵巧手、跨任务跨场景泛化。主要规格包括：身高 164 cm；工作高度 0–2 m（尺寸）、未公开（重量）、全身 62 DOF；躯干 6 DOF；单手灵巧手 20 DOF（自由度）。

## 产品图片

![自变量 Quanta X2（量子 2 号）](https://x2robot-open.oss-cn-shenzhen.aliyuncs.com/quantum2_qiepian/x2/12_m.png)

> 图片来源：自变量机器人官网产品图。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 身高 164 cm；工作高度 0–2 m | 自变量官网 |
| 重量 | 未公开 | - |
| 自由度 | 全身 62 DOF；躯干 6 DOF；单手灵巧手 20 DOF | 自变量官网 |
| 负载/扭矩 | 单臂额定负载 6 kg；最大双臂负载 25 kg | 自变量官网 |
| 速度/转速 | 末端速度 1.8 m/s；底盘移动速度 1 m/s | 自变量官网 |
| 续航 | 未公开 | - |
| 接口/通信 | 2D 激光雷达、超声波×4、RGBD、3D-TOF、单点 TOF、红外；WALL-A 端到端大模型 | 自变量官网 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[自变量机器人 / Xvariable / X Square Robot](../companies/company_xvariable.md)
- **核心零部件/技术来源**：自研 WALL-A 大模型、关节、灵巧手、传感器、计算平台；外购电机、减速器、电池、相机模组。
- **下游应用/客户**：工业组装、线束整理、酒店纸巾换新、晾衣服、杂物收纳、制作饮品、科研教育。

## 知识图谱节点与关系

- 产品实体：`ent_product_xvariable_quanta_x2`
- 制造商实体：`ent_company_xvariable`
- 关键关系：
  - `rel_ent_company_xvariable_manufactures_ent_product_xvariable_quanta_x2`（`ent_company_xvariable` → `manufactures` → `ent_product_xvariable_quanta_x2`）
  - `ent_product_xvariable_quanta_x2` -- `uses` --> `ent_component_xvariable_artixon_hand`

## 应用场景

- **工业组装、线束整理、酒店纸巾换新、晾衣服、杂物收纳、制作饮品、科研教育。**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 通用轮式仿人形机器人 | 同类产品视具体场景而定 |
| 核心优势 | 百亿参数 WALL-A 端到端操作大模型、全身 62 DOF、±0.03 mm 重复定位、仿人五指灵巧手、跨任务跨场景泛化 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [自变量机器人官网](https://x2robot.com)
2. [Quanta X2 产品页](https://x2robot.com/product/quantum2)
3. [关于我们](https://x2robot.com/about)