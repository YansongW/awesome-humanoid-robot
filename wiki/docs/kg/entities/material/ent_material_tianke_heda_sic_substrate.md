---
id: ent_material_tianke_heda_sic_substrate
schema_version: 1
type: material
domain: 01_raw_materials
theoretical_depth: system
names:
  zh: 天科合达 碳化硅（SiC）衬底
  en: TanKeBlue Silicon Carbide Substrate
status: active
sources:
- id: src_tankeblue_official
  type: website
  url: https://www.tankeblue.com/
- title: 北京天科合达半导体股份有限公司官网
- id: src_tankeblue_8inch_donews
  type: website
  url: https://www.donews.com/news/detail/4/3282220.html
- title: 天科合达发布 8 英寸碳化硅衬底新产品 - DoNews
- id: src_tankeblue_industry_report
  type: website
  url: https://pdf.dfcfw.com/pdf/H3_AP202309141598504678_1.pdf
- title: SiC 行业深度报告：衬底与外延环节的材料+设备国产化机遇 - 东方财富
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 天科合达 碳化硅（SiC）衬底 / TanKeBlue Silicon Carbide Substrate

## 概述

碳化硅（SiC）是第三代宽禁带半导体材料，具有高击穿电场、高热导率、高电子饱和漂移速度等优异特性，是制造高功率、高频、高温电力电子器件与射频器件的核心基础材料。天科合达（TanKeBlue）是国内率先从事 4H-SiC 单晶衬底研发、生产和销售的国家级高新技术企业之一，产品覆盖 4 英寸、6 英寸与 8 英寸导电型及半绝缘型 SiC 衬底，并可提供 SiC 外延片一体化解决方案。

## 物理化学基础 / 本构关系

4H-SiC 为宽带隙半导体，禁带宽度

\[
E_g \approx 3.26\,\text{eV}
\]

临界击穿电场

\[
E_c \approx 2.2\,\text{MV/cm}
\]

热导率

\[
\kappa \approx 490\,\text{W}/(\text{m}\cdot\text{K})
\]

上述特性使 SiC 器件相比硅器件可在更高电压、更高温度与更高开关频率下工作。对于 SiC 功率器件，理想比导通电阻与击穿电压 \(V_B\) 满足

\[
R_{\text{on,sp}} \approx \frac{4 V_B^2}{\varepsilon_r \varepsilon_0 \mu E_c^3}
\]

其中 \(\varepsilon_r\) 为相对介电常数，\(\varepsilon_0\) 为真空介电常数，\(\mu\) 为载流子迁移率。SiC 的高 \(E_c\) 显著降低了高压器件的比导通电阻与开关损耗。

晶体质量由微管密度（MPD）、位错密度（EPD/TSD/BPD）、总厚度变化（TTV）、弯曲度（BOW）、翘曲度（WARP）与表面粗糙度（Ra）等指标共同表征。

## 关键参数表

| 参数 | 6 英寸导电型典型值 | 8 英寸导电型典型值 |
|------|---------------------|---------------------|
| 晶型 | 4H-SiC | 4H-SiC |
| 直径 | 150 mm | 200 mm（晶体直径可达 209 mm） |
| 导电类型 | n 型 | n 型 |
| 电阻率 | \(0.015\!\sim\!0.025\,\Omega\cdot\text{cm}\) | \(0.015\!\sim\!0.025\,\Omega\cdot\text{cm}\) |
| TTV（总厚度变化） | \(\le 6\,\mu\text{m}\) | \(\le 7\!\sim\!10\,\mu\text{m}\) |
| BOW（弯曲度，绝对值） | \(\le 30\,\mu\text{m}\) | 未公开 |
| WARP（翘曲度） | \(\le 40\,\mu\text{m}\) | 未公开 |
| 微管密度 | \(\le 2\,\text{cm}^{-2}\) | 未公开 |
| XRD 摇摆曲线半高宽 | \(< 20\,\text{arcsec}\) | \(< 20\,\text{arcsec}\) |
| 表面粗糙度 Ra | \(\le 0.2\,\text{nm}\) | 未公开 |

## 在机器人系统中的作用

SiC 衬底是机器人高功率密度电机驱动、车载充电器与 DC-DC 变换器的关键上游材料。基于 SiC 的 MOSFET 与 SBD 可显著降低逆变器开关损耗、缩小散热系统体积，从而提升人形机器人、AGV/AMR 与无人机的续航与功率密度。此外，SiC 器件在高温环境下仍能保持稳定工作，有助于简化机器人热管理设计。

## 供应链关系

天科合达衬底处于第三代半导体产业链最上游。其上游为 SiC 粉料、单晶生长炉与热场材料；中游为天科合达自身的晶体生长、切片、研磨抛光与清洗检测能力，并可进一步加工成 SiC 外延片；下游面向功率器件与射频器件制造厂商、外延片供应商及电机驱动/电源模块企业。天科合达已通过 IATF 16949:2016 车规级质量管理体系认证，产品销往日本、欧美等 20 多个国家和地区。

## 来源与验证

参数来自天科合达官网、8 英寸新品发布报道及东方财富行业研究报告。8 英寸产品的 BOW、WARP、微管密度、表面粗糙度等详细指标未在公开资料中完整披露，标注为“未公开”。