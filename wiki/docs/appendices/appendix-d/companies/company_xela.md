# XELA Robotics（日本）

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | XELA Robotics |
| **英文名** | XELA Robotics Inc. |
| **总部** | 日本东京（早稻田大学衍生企业） |
| **成立时间** | 2018 |
| **官网** | [https://www.xelarobotics.com](https://www.xelarobotics.com) |
| **供应链环节** | 高密度 3 轴触觉传感器、机器人电子皮肤、触觉集成方案 |
| **企业属性** | 私营企业、高新技术企业 |
| **母公司/所属集团** | 独立运营 |
| **数据来源** | XELA Robotics 官网、产品目录、Engineering.com 报道 |

## 公司简介

XELA Robotics 是 2018 年从日本早稻田大学走出来的机器人触觉传感技术公司，专注于为机器人提供“类人触觉”。公司核心产品 uSkin 是一款高密度三轴柔性触觉传感器，可测量 X/Y/Z 方向的力，并以柔软、耐用、极简布线的设计适配各种机器人夹爪与灵巧手。

XELA 不仅提供标准化传感器模组（uSkin Patch、uSkin Curved、uSkin Protect 系列），还提供定制集成服务，已将 uSkin 集成到 Robotiq、Weiss Robotics、Wonik Robotics、Tesollo DG-5F 等主流夹爪与机器人手中。其磁阻式传感原理与数字输出架构，使传感器在抗噪声、易布线与可扩展性方面具有显著优势。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 贴片式触觉传感器 | 通用平面 3 轴力传感 | uSPa 系列 | 电子皮肤、夹爪 |
| 指尖曲面传感器 | 机器人灵巧手指尖 | uSCu 系列 | 多指灵巧手 |
| 夹爪专用保护传感器 | 直接集成于商用夹爪 | uSPr 系列 | 工业夹爪 |
| 触觉集成方案 | 整机/夹爪定制集成 | Custom Integration | 人形机器人、工业机器人 |

## 代表产品

### XELA Robotics uSkin 高密度 3 轴触觉传感器

> XELA uSkin：请访问 [官方资料](https://www.xelarobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感原理 | 磁阻式 3 轴力传感 | 官网公开资料 |
| 感知维度 | X、Y、Z 三轴力 | 官网公开资料 |
| 传感点密度 | 4 mm × 4 mm（标准）；2026 年计划降至 2.5 mm × 2.5 mm | Engineering.com |
| 单个 taxel 法向力量程 | 最高 1500 gf（约 14.7 N） | XELA Catalog 2025 |
| 分辨率 | 0.1 gf（约 1 mN） | 官网公开资料 |
| 采样频率 | 500 Hz | 官网公开资料 |
| 输出方式 | 数字输出 | 官网公开资料 |
| 布线 | 最少 4 线即可读取全部传感器 | 产品手册 |
| 封装 | 柔软弹性体外壳，耐磨耐过载 | 官网公开资料 |
| 标准型号 | uSPa 11/21/22/44/46、uSCu、uSPr 系列 | 官网公开资料 |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：每个传感单元像摇杆一样独立测量三轴力，数字输出极大简化布线；柔软封装可贴合曲面，抗过载能力强，适配多种商用夹爪与灵巧手。

**应用场景**：人形机器人灵巧手、工业夹爪力控、物流分拣、农业采摘、医疗假肢、科研实验。

### XELA uSkin 指尖曲面传感器（uSCu）

> XELA uSkin Curved：请访问 [官方资料](https://www.xelarobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 三轴曲面触觉传感器 | 产品手册 |
| Taxels 数量 | 30（典型型号） | 经销商资料 |
| 设计用途 | 机器人灵巧手指尖 | 产品手册 |
| 特点 | 柔软皮肤、指尖贴合、自然人机交互 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：曲面设计更贴合机器人手指，提供更自然的接触几何，适合五指仿生灵巧手的全手触觉覆盖。

**应用场景**：五指仿生灵巧手、人形机器人、遥操作、精密抓取。

## 供应链位置

- **上游关键零部件/材料**：磁阻传感芯片、柔性弹性体、硅胶封装、微控制器、柔性 PCB
- **下游客户/应用场景**：人形机器人 OEM、协作机器人夹爪、物流仓储、农业机器人、科研院校
- **主要竞争对手/对标**：SynTouch、帕西尼感知科技、他山科技、力感科技

## 知识图谱节点与关系

- 公司实体：`ent_company_xela`
- 产品实体：`ent_product_xela_uskin`
- 零部件实体：`ent_component_xela_uskin_module`
- 关键关系：
  - `ent_company_xela` -- `manufactures` --> `ent_product_xela_uskin`
  - `ent_company_xela` -- `manufactures` --> `ent_component_xela_uskin_module`
  - `ent_product_xela_uskin` -- `uses` --> `ent_component_xela_uskin_module`

## 参考资料

1. [XELA Robotics 官网](https://www.xelarobotics.com)
2. [XELA Robotics 产品目录 2025](https://49063741.fs1.hubspotusercontent-na2.net/hubfs/49063741/XELA%20Robotics%20-%20Catalog%202025.pdf)
3. [Engineering.com – uSkin integrated into Tesollo DG-5F](https://www.engineering.com/uskin-tactile-sensors-integrated-into-tesollo-dg-5f-robot-hand/)
4. [XELA Robotics 技术页](https://xelarobotics.com/technology/)
5. [附录 D 产品目录](../index-products.md)