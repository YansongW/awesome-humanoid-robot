---
id: ent_company_rockchip
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 瑞芯微
  en: Rockchip
status: active
sources:
- id: src_rockchip_official
  type: website
  url: https://www.rock-chips.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 瑞芯微 / Rockchip

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 瑞芯微 |
| **英文名** | Rockchip |
| **总部** | 中国福建福州 |
| **成立时间** | 2001 年 |
| **官网** | [https://www.rock-chips.com](https://www.rock-chips.com) |
| **供应链环节** | AIoT SoC、机器人主控、工业平板、边缘 AI、多媒体 |
| **企业属性** | 上市公司（深圳证券交易所：603893） |
| **母公司/所属集团** | 无（Rockchip 为上市主体） |
| **数据来源** | 瑞芯微官网、RK3588 产品资料、公开新闻稿、行业研报 |

## 公司简介

瑞芯微（Rockchip）是中国领先的 AIoT 与多媒体 SoC 设计公司，产品覆盖平板电脑、智能电视盒子、工业控制、机器人与边缘 AI。其 RK3588 是旗舰级 AIoT 芯片，集成 6 TOPS NPU、8K 视频编解码与丰富接口，广泛应用于机器人主控、工业网关、NVR、智能商显与边缘 AI 盒子。瑞芯微提供 RKNN 工具链与 Linux/Android SDK，支持快速模型部署。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RK3588 系列 | 旗舰 AIoT / 机器人 SoC | RK3588 / RK3588S | 机器人主控、边缘 AI、NVR、工业 HMI、8K 商显 |
| RK3576 / RK3568 系列 | 中高端 AIoT SoC | RK3568 / RK3576 | 工业网关、智能相机、教育机器人、AIoT 终端 |

## 代表产品

### Rockchip RK3588

> Rockchip RK3588：请访问 [官方资料](https://www.rock-chips.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 8 nm LP | 瑞芯微公开资料 |
| CPU | 八核（4× Cortex-A76 @ 最高 2.4 GHz + 4× Cortex-A55） | 瑞芯微公开资料 |
| GPU | Arm Mali-G610 MC4（约 450 GFLOPS） | 瑞芯微公开资料 |
| NPU | 自研三核 NPU | 瑞芯微公开资料 |
| AI 算力 | 最高 6.0 TOPS INT8 | 瑞芯微公开资料 |
| 精度支持 | INT4/INT8/INT16/FP16/BF16/TF32 | 瑞芯微公开资料 |
| 视频 | 8K@60fps 解码、8K@30fps 编码、H.265/VP9/AVS2 | 瑞芯微公开资料 |
| ISP | 双 ISP，32 MP，支持 HDR & 3DNR | 瑞芯微公开资料 |
| 内存 | 支持 LPDDR4/LPDDR4x/LPDDR5，最高 32 GB | 瑞芯微公开资料 |
| 接口 | PCIe 3.0、USB 3.1、SATA 3.0、GbE、MIPI CSI/DSI、HDMI 2.1/DP/eDP | 瑞芯微公开资料 |
| 功耗 | 典型约 5–15 W（整板） | 瑞芯微公开资料 |
| 价格 | 开发板约 100–200 USD（参考价） | 瑞芯微公开资料 |

**技术亮点**：8 nm 旗舰 AIoT 芯片、6 TOPS NPU、8K 多媒体、多路相机、丰富扩展接口、RKNN 工具链、Linux/Android 生态成熟。

**应用场景**：**机器人主控**：多路相机感知、SLAM、路径规划与机械臂控制；**边缘 AI 盒子与 NVR**：8K 解码、多路视频分析与本地 AI 推理；**智能商显与自助终端**：多屏异显、触控交互与广告播放

### Rockchip RK3576

> Rockchip RK3576：请访问 [官方资料](https://www.rock-chips.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 未公开 | 瑞芯微公开资料 |
| CPU | 八核 Cortex-A72/A53 或更新架构 | 瑞芯微公开资料 |
| NPU | 约 6 TOPS | 瑞芯微公开资料 |
| 视频 | 4K/8K 解码 | 瑞芯微公开资料 |
| 接口 | PCIe、USB、GbE、MIPI CSI/DSI、HDMI | 瑞芯微公开资料 |
| 功耗 | 约 3–8 W | 瑞芯微公开资料 |
| 价格 | 未公开 | 瑞芯微公开资料 |

**技术亮点**：中高端 AIoT SoC，继承 RK3588 的 NPU 与多媒体能力，面向成本敏感型机器人与边缘设备。

**应用场景**：工业网关、教育机器人、智能相机、AIoT 终端。

## 供应链位置

- **上游关键零部件/材料**：台积电/中芯国际代工、ARM CPU/GPU IP、自研 NPU、LPDDR4x、eMMC、封测、载板
- **下游客户/应用场景**：机器人整机厂、工业平板/网关厂商、NVR/安防客户、商显与教育设备商、开发者
- **主要竞争对手/对标**：全志科技、联发科 Genio、高通 QCS、NVIDIA Jetson、Amlogic、海思

## 知识图谱节点与关系

- 公司实体：`ent_company_rockchip`
- 产品实体：`ent_product_rockchip_rk3588`、`ent_product_rockchip_rk3576`
- 零部件实体：`ent_component_rockchip_rk3588_soc`、`ent_component_rockchip_rk3576_soc`
- 关键关系：
  - `ent_company_rockchip` -- `manufactures` --> `ent_product_rockchip_rk3588`
  - `ent_company_rockchip` -- `manufactures` --> `ent_product_rockchip_rk3576`
  - `ent_company_rockchip` -- `manufactures` --> `ent_component_rockchip_rk3588_soc`
  - `ent_company_rockchip` -- `manufactures` --> `ent_component_rockchip_rk3576_soc`
  - `ent_product_rockchip_rk3588` -- `uses` --> `ent_component_rockchip_rk3588_soc`
  - `ent_product_rockchip_rk3576` -- `uses` --> `ent_component_rockchip_rk3576_soc`

## 参考资料

1. [瑞芯微官网](https://www.rock-chips.com)
2. [RK3588 产品页](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)
3. [Rockchip RKNN SDK](https://github.com/rockchip-linux/rknpu2)