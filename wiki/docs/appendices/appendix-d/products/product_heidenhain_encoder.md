# 海德汉 EQI 1131 感应式多圈旋转编码器 / Heidenhain EQI 1131 Inductive Multi-turn Rotary Encoder

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [海德汉 / Heidenhain](../companies/company_heidenhain.md) |
| **产品类别** | 无内置轴承绝对式多圈旋转编码器 |
| **发布时间** | 现役主力 |
| **状态** | 量产/商用 |
| **官网/来源** | [海德汉官网](https://www.heidenhain.com) |

## 产品概述

海德汉 EQI 1131 属于 ECI/EQI 1100 系列感应式旋转编码器平台，是一款无内置轴承的绝对式多圈旋转编码器。该产品采用感应扫描原理，对污染、油污和振动具有优异的抗干扰能力，特别适合高动态、高可靠性的伺服电机反馈应用。

EQI 1131 每圈分辨率 19 bit，多圈计数 12 bit（4096 圈），系统精度 ±120"，最高轴速可达 12,000 rpm，支持 EnDat 3.0 接口与 HMC 2 单电缆技术，并可满足 SIL 2 / PL d 功能安全要求（外部措施可达 SIL 3 / PL e）。

## 产品图片

> Heidenhain EQI 1131：请访问 [官方资料](https://www.heidenhain.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 无内置轴承绝对式多圈旋转编码器 | 官方 datasheet |
| 扫描原理 | 感应式扫描 | 官方 datasheet |
| 每圈位置数 | 524,288（19 bit） | 官方 datasheet |
| 圈数 | 4096（12 bit） | 官方 datasheet |
| 系统精度 | ±120" | 官方 datasheet |
| 最高轴速 | ≤ 12,000 rpm | 官方 datasheet |
| 轴向公差 | ±0.5 mm | 官方 datasheet |
| 工作温度 | -20℃ 至 +115℃ | 官方 datasheet |
| 外部温度传感器 | KTY / PT1000 | 官方 datasheet |
| 接口 | EnDat 3.0 / HMC 2 单电缆 | 官方 datasheet |
| 功能安全 | SIL 2 / PL d（外部措施可达 SIL 3 / PL e） | 官方 datasheet |
| 外壳直径 | 约 37 mm | 官方 datasheet |
| 抗振动 | 定子 400 m/s² / 转子 600 m/s² | 官方 datasheet |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[海德汉 / Heidenhain](../companies/company_heidenhain.md)
- **核心零部件/技术来源**：自研感应扫描 ASIC、EnDat 接口与功能安全算法；高精度光栅材料、半导体芯片、结构件外购。
- **下游应用/客户**：高端伺服电机、工业机器人、人形机器人关节、数控机床、半导体设备、医疗影像。

## 知识图谱节点与关系

- 零部件实体：`ent_component_heidenhain_eqi_1131`
- 制造商实体：`ent_company_heidenhain`
- 关键关系：
  - `rel_ent_company_heidenhain_manufactures_ent_component_heidenhain_eqi_1131`（`ent_company_heidenhain` → `manufactures` --> `ent_component_heidenhain_eqi_1131`）

## 应用场景

- **伺服电机反馈**：高动态电机转速与位置闭环控制。
- **人形机器人关节**：关节角度与速度高精度反馈。
- **数控机床主轴**：高速主轴定位与同步控制。
- **半导体/医疗设备**：精密旋转台与运动平台反馈。

## 竞争对比

| 对比项 | 海德汉 EQI 1131 | 奥普光电 JZN/JKN | 多摩川 TS5700 |
|--------|-----------------|------------------|---------------|
| 扫描原理 | 感应式 | 光电/金属光栅 | 磁性/光电 |
| 分辨率 | 19 bit/圈 + 12 bit 圈数 | 最高 29 位绝对式 | 因型号而异 |
| 系统精度 | ±120" | 国内领先 | 因型号而异 |
| 功能安全 | SIL 2/3 | 未公开 | 部分型号支持 |
| 接口 | EnDat 3.0 / HMC 2 | 未公开 | 多协议 |
| 核心优势 | 国际品牌、功能安全、单电缆 | 国产替代、价格优势 | 稳定可靠 |

## 选购与部署建议

- 部署前需确认电机轴尺寸、定位孔规格、EnDat 接口版本与驱动器兼容性。
- 感应式编码器虽抗污染能力强，但仍需避免强磁场干扰并保证定转子安装气隙在规定范围。

## 参考资料

1. [海德汉官网](https://www.heidenhain.com)
2. [海德汉 ECI/EQI 1100 datasheet](https://www.heidenhain.de/fileadmin/pdf/zh_CN/Broschueren/BR_Rotary_Encoder_Platform_ECI_EQI_ID1465030_zh.pdf)
3. [海德汉中国 – ECI/EQI 1100 产品页](https://www.heidenhain.com.cn/%E4%BA%A7%E5%93%81/%E7%BC%96%E7%A0%81%E5%99%A8/%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8/%E5%86%85%E9%83%A8%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8/eci/ebi/eqi-1100%E7%B3%BB%E5%88%97)
4. [附录 D 企业目录](../index-companies.md)