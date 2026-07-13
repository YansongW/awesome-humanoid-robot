---
id: ent_product_renishaw_resolute_encoder
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 雷尼绍 RESOLUTE 绝对式光栅编码器
  en: Renishaw RESOLUTE Absolute Encoder
status: active
sources:
- id: src_ent_product_renishaw_resolute_encoder_official
  type: website
  url: https://www.renishaw.com/en/resolute-absolute-encoder--9533
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 雷尼绍 RESOLUTE 绝对式光栅编码器 / Renishaw RESOLUTE Absolute Encoder

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [雷尼绍 / Renishaw](../../../appendices/appendix-d/companies/company_renishaw.md) |
| **产品类别** | 绝对式光学编码器（直线/旋转） |
| **发布时间** | 持续在售/迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [雷尼绍 RESOLUTE 绝对式光栅编码器产品/资料页](https://www.renishaw.com/en/resolute-absolute-encoder--9533) |

## 产品概述

RESOLUTE 是雷尼绍推出的真正绝对式光学编码器系统，采用单轨 30 µm 栅距刻线与先进光学读数头，可在开机瞬间确定绝对位置。系统最高分辨率达 1 nm，最大速度 100 m/s，支持 BiSS C、DRIVE-CLiQ、FANUC、Mitsubishi 等多种串行接口，广泛用于高精度机床、机器人关节与半导体设备。

## 产品图片

> 雷尼绍 RESOLUTE 绝对式光栅编码器：请访问 [官方资料](https://www.renishaw.com/en/resolute-absolute-encoder--9533) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 真正绝对式光学编码器 | Renishaw datasheet |
| 栅距 | 30 µm | Renishaw datasheet |
| 分辨率 | 最高 1 nm | Renishaw datasheet |
| 精度 | ±1 µm/m（RELA）/ ±5 µm/m（RTLA） | Renishaw datasheet |
| 最大速度 | 最高 100 m/s | Renishaw datasheet |
| 细分误差（SDE） | ±40 nm | Renishaw datasheet |
| 抖动 | 7 nm RMS | Renishaw datasheet |
| 接口 | BiSS C / DRIVE-CLiQ / FANUC / Mitsubishi / Panasonic | Renishaw datasheet |
| 防护等级 | IP64 | Renishaw datasheet |
| 工作温度 | 0℃ – +55℃ | Renishaw datasheet |
| 功能安全 | 可选 SIL2 / PL d | Renishaw datasheet |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[雷尼绍 / Renishaw](../../../appendices/appendix-d/companies/company_renishaw.md)
- **核心零部件/技术来源**：光学读数头、玻璃/钢带/低膨胀合金栅尺、ASIC、电缆与连接器
- **下游应用/客户**：机床 OEM、机器人厂商、半导体设备、CMM 制造商、航空航天

## 知识图谱节点与关系

- 产品实体：`ent_product_renishaw_resolute_encoder`
- 零部件实体：`ent_component_renishaw_resolute_readhead`
- 制造商实体：`ent_company_renishaw`
- 关键关系：
  - `rel_ent_company_renishaw_manufactures_ent_product_renishaw_resolute_encoder`（`ent_company_renishaw` → `manufactures` → `ent_product_renishaw_resolute_encoder`）
  - `rel_ent_company_renishaw_manufactures_ent_component_renishaw_resolute_readhead`（`ent_company_renishaw` → `manufactures` → `ent_component_renishaw_resolute_readhead`）
  - `ent_product_renishaw_resolute_encoder` -- `uses` --> `ent_component_renishaw_resolute_readhead`

## 应用场景

- **高精度数控机床、直线电机、机器人关节、半导体设备、三坐标测量机、天文望远镜**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 见规格参数表 | 同类产品 | 同类产品 |
| 核心优势 | 官方公开性能指标 | 竞品公开指标 | 竞品公开指标 |
| 生态/服务 | 制造商官方支持 | 竞品生态 | 竞品生态 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：雷尼绍 / Renishaw](../../../appendices/appendix-d/companies/company_renishaw.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [雷尼绍官网](https://www.renishaw.com)
2. [雷尼绍 RESOLUTE 绝对式光栅编码器产品/资料页](https://www.renishaw.com/en/resolute-absolute-encoder--9533)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)