---
id: ent_company_qtech
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 丘钛科技
  en: Q-Tech
status: active
sources:
- id: src_qtech_official
  type: website
  url: https://www.qtechsmartvision.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 丘钛科技 / Q-Tech

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 丘钛科技 |
| **英文名** | Q-Tech |
| **总部** | 中国江苏昆山（运营总部），香港上市 |
| **成立时间** | 2007 |
| **官网** | [https://www.qtechsmartvision.com](https://www.qtechsmartvision.com) |
| **供应链环节** | 中高端摄像头模组、指纹识别模组、机器视觉、车载视觉 |
| **企业属性** | 上市公司（HKEX: 01478）、全球第三大智能手机摄像头模组封装测试企业 |
| **母公司/所属集团** | 独立上市（昆山丘钛微电子为全资子公司） |
| **数据来源** | 丘钛科技官网、招股书、公开产品资料 |

## 公司简介

丘钛科技（Q-Tech）是全球领先的智能移动终端中高端摄像头模组及指纹识别模组制造商，具备 COB、COF、MOB、MOC 等先进封装技术。公司产品覆盖 200 万像素至 1.08 亿像素，并积极布局车载、无人机、智能家居及工业机器人等机器视觉领域。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 智能手机摄像头模组 | 超薄/OIS/多摄 | 200MP–108MP 系列 | 智能手机、平板 |
| 3D 结构光/微云台模组 | 高阶功能模组 | 结构光、微云台 | 高端手机、机器人 |
| 车载/IoT 摄像头模组 | 车规级机器视觉 | ADAS、环视、舱内模组 | 智能汽车、无人机 |
| 指纹识别模组 | 电容/光学/屏下指纹 | 侧边/屏下指纹模组 | 智能手机、智能门锁 |

## 代表产品

### 丘钛科技机器视觉/车载摄像头模组

> 丘钛科技机器视觉/车载摄像头模组：请访问 [官方资料](https://www.qtechsmartvision.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 机器视觉/车规级摄像头模组 | 丘钛科技官网 |
| 分辨率 | 2MP / 5MP / 8MP 多型号 | 丘钛科技官网 |
| 传感器 | 1/2.8" – 1/2.3" CMOS | 丘钛科技官网 |
| 快门 | 全局快门 / 卷帘快门（可选） | 丘钛科技官网 |
| 视场角 | 120° / 140° / 定制 | 丘钛科技官网 |
| 接口 | MIPI / GMSL2 | 丘钛科技官网 |
| 防护等级 | IP67（车规型号） | 丘钛科技官网 |
| 工作温度 | -40℃ – +85℃ | 丘钛科技官网 |
| 供电 | 12 V DC（典型） | 丘钛科技官网 |
| 重量 | 约 30 – 80 g | 丘钛科技官网 |
| 价格 | 未公开 | - |

**技术亮点**：先进 COB/COF/MOB 封装、车规级可靠性、支持全局快门与高速串行接口，满足机器人与车载高动态场景。

**应用场景**：工业机器人视觉检测、无人机航拍、智能汽车环视/前视、服务机器人 SLAM。

### 丘钛科技 3D 结构光模组

> 丘钛科技 3D 结构光模组：请访问 [官方资料](https://www.qtechsmartvision.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 3D 结构光深度模组 | 公开资料 |
| 应用 | 人脸识别、机器人避障 | 公开资料 |
| 特色 | 国内率先量产 | 公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：高集成度 3D 结构光方案，支持高精度三维重建。

**应用场景**：手机 Face ID、机器人抓取、支付级人脸识别。

## 供应链位置

- **上游关键零部件/材料**：CMOS 图像传感器、镜头、音圈马达、FPC、驱动 IC、结构件
- **下游客户/应用场景**：智能手机 OEM、汽车 OEM/Tier1、无人机、机器人、IoT 厂商
- **主要竞争对手/对标**：舜宇光学、欧菲光、LG Innotek、三星电机、盛泰光电

## 知识图谱节点与关系

- 公司实体：`ent_company_qtech`
- 产品实体：`ent_product_qtech_machine_vision_camera_module`
- 零部件实体：`ent_component_qtech_camera_module_core`
- 关键关系：
  - `ent_company_qtech` -- `manufactures` --> `ent_product_qtech_machine_vision_camera_module`
  - `ent_company_qtech` -- `manufactures` --> `ent_component_qtech_camera_module_core`
  - `ent_product_qtech_machine_vision_camera_module` -- `uses` --> `ent_component_qtech_camera_module_core`

## 参考资料

1. [丘钛科技官网](https://www.qtechsmartvision.com)
2. [丘钛科技机器视觉/车载摄像头模组产品/资料页](https://www.qtechsmartvision.com/)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)