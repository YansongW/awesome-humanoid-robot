---
id: ent_component_laifual_lss_32_100
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 来福 LSS-32-100-U-I 谐波减速器
  en: Laifual LSS-32-100-U-I Harmonic Reducer
sources:
- id: src_laifual_official
  type: website
- title: Laifual Official Website
  url: https://www.laifual.com
- id: src_laifual_baidu_baike
  type: website
- title: 浙江来福谐波传动股份有限公司（百度百科）
  url: https://baike.baidu.com/en/item/Zhejiang%20Laifual%20Drive%20Co.,%20Ltd./79327
- id: src_laifual_hannover_messe
  type: website
- title: Laifual Drive Hannover Messe Product Brochure
  url: https://www.messe.de/apollo/hannover_messe_2020/obs/Binary/A1008631/25783_43533_157595427891029100_aeid_205__265_atomfeld_205_265-139416811575957040.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Laifual product parameter tables and public brochures;
    values correspond to 100:1 ratio unless noted.
---


# 来福 LSS-32-100-U-I 谐波减速器 / Laifual LSS-32-100-U-I Harmonic Reducer

## 概述

来福 LSS-32-100-U-I 谐波减速器（Laifual LSS-32-100-U-I Harmonic Reducer）是浙江来福谐波传动股份有限公司（Laifual）生产的杯型标准谐波减速器，规格代号为 32，减速比 100:1，采用 U-I 型结构（带输入轴、标准杯形柔轮）。该产品以高刚性交叉滚子轴承支撑外部负载，具有结构紧凑、传动比大、背隙小、扭矩密度高等特点，广泛应用于工业机器人关节、协作机器人、人形机器人手臂与自动化转台。

## 工作原理 / 技术架构

谐波减速器基于谐波齿轮传动原理，由波发生器、柔轮（flexspline）与刚轮（circular spline）三个核心部件组成：

1. **波发生器**：通常为椭圆凸轮加柔性轴承，装入柔轮后使其产生可控弹性变形，形成长轴与短轴。
2. **柔轮**：薄壁杯形齿轮，外齿与刚轮内齿啮合。波发生器旋转时，柔轮长轴处齿逐次与刚轮啮合，实现减速输出。
3. **刚轮**：刚性内齿轮，通常固定于减速器外壳；柔轮则作为输出端。
4. **交叉滚子轴承**：集成于减速器输出端，承受径向、轴向与倾覆力矩，保证高刚性。

减速比 $i$ 由刚轮齿数 $z_c$ 与柔轮齿数 $z_f$ 的差值决定。对于标准双波谐波减速器：

$$
i = \frac{z_c}{z_c - z_f}
$$

当齿数差为 2 且减速比为 100:1 时，刚轮齿数约为 200，柔轮齿数约为 198。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 来福谐波 / Laifual | 公司官网 |
| 系列 | LSS（杯型标准结构） | 产品手册 |
| 规格 | 32 | Laifual LSS 参数表 |
| 减速比 | 50 / 80 / 100 / 120:1 | Laifual LSS 参数表 |
| 额定扭矩（2000 rpm 输入，100:1） | 137 N·m | Laifual LSS 参数表 |
| 启动停止容许扭矩（100:1） | 333 N·m | Laifual LSS 参数表 |
| 平均负载容许扭矩（100:1） | 216 N·m | Laifual LSS 参数表 |
| 瞬时最大扭矩（100:1） | 647 N·m | Laifual LSS 参数表 |
| 最高输入转速 | 4,800 rpm | Laifual LSS 参数表 |
| 背隙 | ≤ 20 arcsec | Laifual LSS 参数表 |
| 重量 | 3.11 kg | Laifual LSS 参数表 |
| 结构 | 杯型标准 + 高刚性交叉滚子轴承 | 产品手册 |
| 安装方式 | 刚轮固定 / 柔轮输出 | 产品手册 |
| 设计寿命 | 10,000 h | 行业参数 |
| 价格 | 未公开 | 需询价 |

注：上表中 100:1 减速比对应扭矩值为公开产品参数表所列；50/80/120:1 对应值不同，具体参见 Laifual 官方选型手册。

## 应用场景

- **工业机器人关节**：为六轴工业机器人提供高精度的旋转减速与扭矩放大。
- **人形机器人手臂**：在肩部、肘部、腕部关节中实现高扭矩密度与低背隙运动。
- **协作机器人**：利用低背隙、高刚性特性，保障人机协作中的安全与精度。
- **自动化转台与半导体设备**：提供精密分度与定位功能。
- **医疗机器人**：用于手术机械臂与康复机器人关节。

## 供应链关系

来福谐波（`ent_company_laifual`）是国产谐波减速器主要厂商之一，产品覆盖 LSS、LSG、LHT、LHD 等多个系列。LSS-32-100-U-I（`ent_component_laifual_lss_32_100`）是其标准杯型谐波减速器的代表型号。上游原材料包括合金钢、柔性轴承、润滑脂与铝合金；下游客户包括工业机器人、服务机器人、医疗设备与自动化设备厂商。来福谐波与绿的谐波、Harmonic Drive Systems、同川精密等形成竞争。在知识图谱中，来福同时制造 LSS-32-100-U-I 与 LHD-32-100-U-I 等型号。

## 来源与验证

- 来福谐波官网与公司简介确认其为国内批量生产高精密谐波减速器的企业，拥有 30,000 平方米标准厂房。
- 百度百科企业词条整理了来福谐波的产品系列（LSS/LSG/LSD/LSN/LHT/LHG/LHD/LHN）与技术特点。
- 公司参展手册（Hannover Messe）公开了 LSS-32 系列在 50/80/100/120:1 减速比下的额定扭矩、峰值扭矩、背隙、重量等参数。