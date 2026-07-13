# 舜宇光学 / Sunny Optical

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 舜宇光学 |
| **英文名** | Sunny Optical |
| **总部** | 中国浙江宁波（总部），香港上市 |
| **成立时间** | 1984 |
| **官网** | [https://www.sunnyoptical.com](https://www.sunnyoptical.com) |
| **供应链环节** | 光学镜头、摄像头模组、车载视觉、机器人视觉、激光雷达光学部件 |
| **企业属性** | 上市公司（HKEX: 2382）、全球领先综合光学制造商 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 舜宇光学官网、年报、公开产品资料 |

## 公司简介

舜宇光学科技（Sunny Optical）是全球领先的综合光学零件及产品制造商，业务覆盖手机、汽车、安防监控、机器人、AR/VR 等终端。公司具备从光学镜片、镜头到摄像头模组的一站式研发与制造能力，并深耕机器人视觉所需的 3D ToF、结构光与全景视觉模块。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 智能手机摄像头模组 | 中高端影像模组 | COB/COF 高清模组 | 手机、平板 |
| 车载摄像头模组 | ADAS/智能座舱视觉 | 前视/环视/舱内监控模组 | 智能汽车 |
| 机器人/IoT 视觉模组 | 3D ToF、结构光、全景视觉 | 机器人导引与避障模组 | 服务/工业机器人 |
| 激光雷达光学部件 | 发射/接收镜头与扫描模组 | LiDAR 镜头、RX/TX 模组 | 自动驾驶、机器人 |

## 代表产品

### 舜宇光学车载/机器人摄像头模组

> 舜宇光学车载/机器人摄像头模组：请访问 [官方资料](https://www.sunnyoptical.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 车规级摄像头模组 | 官方产品资料 |
| 分辨率 | 2MP / 3MP / 8MP 多型号 | 官方产品资料 |
| 传感器 | 1/2.7" – 1/2.3" CMOS | 官方产品资料 |
| 视场角 | 30° – 120°（因型号而异） | 官方产品资料 |
| 镜头 | 玻塑混合高解析力镜头 | 官方产品资料 |
| 接口 | GMSL2 / FPD-Link III / 同轴 | 官方产品资料 |
| 帧率 | 最高 60 fps（因分辨率与接口而异） | 官方产品资料 |
| 防护等级 | IP67 / IP69K | 官方产品资料 |
| 工作温度 | -40℃ – +85℃ | 官方产品资料 |
| 供电 | 12 V DC（典型） | 官方产品资料 |
| 重量 | 约 50 – 150 g | 官方产品资料 |
| 价格 | 未公开 | - |

**技术亮点**：舜宇自研镜头+模组一体化设计，车规级可靠性，支持高速长距离传输，适配机器人视觉、ADAS 与舱内监控多种场景。

**应用场景**：人形机器人/服务机器人视觉导引、自动驾驶感知、智能座舱 DMS/OMS、工业检测。

### 舜宇光学激光雷达扫描/接收模组

> 舜宇光学激光雷达扫描/接收模组：请访问 [官方资料](https://www.sunnyoptical.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | LiDAR 扫描/接收光学模组 | Sunny Automotive 官网 |
| 方案 | 机械/MEMS/3D Flash/OPA | Sunny Automotive 官网 |
| 应用 | 自动驾驶、机器人避障 | Sunny Automotive 官网 |
| 价格 | 未公开 | - |

**技术亮点**：覆盖多种 LiDAR 技术路线，提供发射/接收镜头与扫描模组一体化方案。

**应用场景**：自动驾驶感知、机器人导航、测绘。

## 供应链位置

- **上游关键零部件/材料**：CMOS 图像传感器、光学镜片、音圈马达、FPC/PCB、ISP 芯片、结构件
- **下游客户/应用场景**：智能手机 OEM、汽车 OEM/Tier1、机器人整机厂、AR/VR 厂商
- **主要竞争对手/对标**：欧菲光、丘钛科技、LG Innotek、三星电机、大立光

## 知识图谱节点与关系

- 公司实体：`ent_company_shunyu`
- 产品实体：`ent_product_shunyu_automotive_camera_module`
- 零部件实体：`ent_component_shunyu_camera_module_core`
- 关键关系：
  - `ent_company_shunyu` -- `manufactures` --> `ent_product_shunyu_automotive_camera_module`
  - `ent_company_shunyu` -- `manufactures` --> `ent_component_shunyu_camera_module_core`
  - `ent_product_shunyu_automotive_camera_module` -- `uses` --> `ent_component_shunyu_camera_module_core`

## 参考资料

1. [舜宇光学官网](https://www.sunnyoptical.com)
2. [舜宇光学车载/机器人摄像头模组产品/资料页](https://www.sunnyoptical.com/en/pro/009017006/index.html)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)