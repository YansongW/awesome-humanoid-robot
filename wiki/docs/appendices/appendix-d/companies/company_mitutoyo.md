# 三丰 / Mitutoyo

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 三丰 |
| **英文名** | Mitutoyo |
| **总部** | 日本神奈川县川崎市 |
| **成立时间** | 1934 |
| **官网** | [https://www.mitutoyo.com](https://www.mitutoyo.com) |
| **供应链环节** | 精密测量设备、三坐标测量机、量具、传感器、工业软件 |
| **企业属性** | 全球计量与精密测量龙头、家族企业（未上市） |
| **母公司/所属集团** | 独立运营 |
| **数据来源** | Mitutoyo 官网、产品手册、经销商技术资料 |

## 公司简介

三丰（Mitutoyo）是全球知名的精密测量仪器制造商，产品覆盖游标卡尺、千分尺、三坐标测量机、影像测量仪、粗糙度/轮廓/圆度测量仪及传感器系统。CRYSTA-Apex 系列 CNC 三坐标测量机以其高精度、高速度与多传感器能力，被广泛应用于汽车、航空航天、电子及机器人零部件检测。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 三坐标测量机 | 高精度几何量测 | CRYSTA-Apex V 系列 | 汽车、航空、机器人 |
| 手持/数字量具 | 长度/角度测量 | 卡尺、千分尺、指示表 | 制造、检测 |
| 影像/形状测量 | 非接触与轮廓测量 | Quick Vision、FORMTRACER | 电子、模具 |
| 传感器与系统 | 测头、控制器、软件 | SP25M、UC480、MCOSMOS | CMM、产线 |

## 代表产品

### 三丰 CRYSTA-Apex V 系列 CNC 三坐标测量机

> 三丰 CRYSTA-Apex V 系列 CNC 三坐标测量机：请访问 [官方资料](https://www.mitutoyo.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | CNC 桥式三坐标测量机 | Mitutoyo 产品手册 |
| 测量范围 | 500×400×400 mm 至 2000×4000×1500 mm 多型号 | Mitutoyo 产品手册 |
| 长度测量误差 E0,MPE | (1.7 + 4L/1000) µm（SP25M，V544/776） | Mitutoyo 产品手册 |
| 分辨率 | 0.1 µm | Mitutoyo 产品手册 |
| 最大驱动速度 | 519 mm/s（3 轴合成） | Mitutoyo 产品手册 |
| 最大加速度 | 2309 mm/s² | Mitutoyo 产品手册 |
| 测头系统 | TP200 / SP25M / 光学/激光扫描测头 | Mitutoyo 产品手册 |
| 控制器 | UC480 | Mitutoyo 产品手册 |
| 温度补偿 | 16℃ – 26℃ 实时补偿 | Mitutoyo 产品手册 |
| 气源 | 0.4 MPa | Mitutoyo 产品手册 |
| 重量 | 约 542 kg（V544）/ 1675 kg（V776） | Mitutoyo 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高刚性气浮桥式结构、亚微米级精度、UC480 多传感器控制器、实时温度补偿与 IoT 质量管理接口。

**应用场景**：机器人关节/减速器几何检测、汽车零部件、航空航天结构件、模具、电子连接器检测。

### 三丰 Quick Vision ELF 影像测量仪

> 三丰 Quick Vision ELF 影像测量仪：请访问 [官方资料](https://www.mitutoyo.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | CNC 影像测量仪 | Mitutoyo 官网 |
| 特色 | 非接触高速测量 | Mitutoyo 官网 |
| 应用 | 电子、注塑件、小零件 | Mitutoyo 官网 |
| 价格 | 未公开 | - |

**技术亮点**：自动对焦、图像边缘检测，适合批量小尺寸零件检测。

**应用场景**：3C 结构件、连接器、医疗器械。

## 供应链位置

- **上游关键零部件/材料**：花岗石、气浮轴承、ABS 光栅尺、测头传感器、控制器、测量软件
- **下游客户/应用场景**：汽车、航空航天、电子、医疗器械、机器人零部件制造商
- **主要竞争对手/对标**：Hexagon、ZEISS、Wenzel、Nikon Metrology

## 知识图谱节点与关系

- 公司实体：`ent_company_mitutoyo`
- 产品实体：`ent_product_mitutoyo_crysta_apex_v`
- 零部件实体：`ent_component_mitutoyo_crysta_apex_cmm`
- 关键关系：
  - `ent_company_mitutoyo` -- `manufactures` --> `ent_product_mitutoyo_crysta_apex_v`
  - `ent_company_mitutoyo` -- `manufactures` --> `ent_component_mitutoyo_crysta_apex_cmm`
  - `ent_product_mitutoyo_crysta_apex_v` -- `uses` --> `ent_component_mitutoyo_crysta_apex_cmm`

## 参考资料

1. [三丰官网](https://www.mitutoyo.com)
2. [三丰 CRYSTA-Apex V 系列 CNC 三坐标测量机产品/资料页](https://www.mitutoyo.com.sg/sg-en/product/detail/crysta-apex-v-series)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)