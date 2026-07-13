---
id: ent_component_infineon_coolsic_mosfet
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: Infineon CoolSiC™ 碳化硅 MOSFET
  en: Infineon CoolSiC™ Silicon Carbide MOSFET
sources:
- id: src_infineon_coolsic_overview
  type: website
- title: CoolSiC™ MOSFET 1200 V - Infineon Technologies
  url: https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/
- id: src_infineon_an2025_10
  type: application_note
- title: Understanding and interpreting the CoolSiC™ MOSFET 1200 V datasheet
  url: https://www.infineon.com/assets/row/public/documents/60/42/infineon-an2025-10-understanding-and-interpreting-the-coolsic-mosfet-1200v-datasheet-applicationnotes-en.pdf
- id: src_infineon_ff55mr12w1m1h
  type: datasheet
- title: FF55MR12W1M1H_B70 1200 V CoolSiC™ MOSFET Half-Bridge Module
  url: https://www.infineon.com/cms/cn/product/power/mosfet/silicon-carbide/modules/ff55mr12w1m1h_b70/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
  review_notes: CoolSiC is a product family; parameters vary by discrete/module and
    voltage class. Values below represent representative 1200 V M1H/G2 ranges.
---


# Infineon CoolSiC™ 碳化硅 MOSFET / Infineon CoolSiC™ Silicon Carbide MOSFET

## 概述

Infineon CoolSiC™ 是英飞凌科技推出的碳化硅（SiC）沟槽栅 MOSFET 产品家族，涵盖 650 V、1200 V、2000 V 等电压等级，提供分立器件与功率模块两种形态。CoolSiC MOSFET 利用 SiC 宽禁带（WBG）材料特性，实现高击穿电场、高电子饱和漂移速度与高热导率，相较硅基 IGBT 可显著降低开关损耗与导通损耗，提升逆变器开关频率与功率密度。在人形机器人领域，CoolSiC 主要应用于关节电机驱动逆变器、电池管理 DC/DC 与车载/机载充电单元。

## 工作原理 / 技术架构

CoolSiC MOSFET 为单极型电压控制器件：当栅-源电压 $V_{GS}$ 超过阈值电压 $V_{GS(th)}$ 时，沟道导通，电子从源极经沟槽栅结构流向漏极，形成漏极电流 $I_D$。SiC 的临界击穿电场约为硅的 10 倍，允许更薄、更高掺杂的漂移区，从而在相同耐压下显著降低导通电阻 $R_{DS(on)}$。

关键电气关系：

- 导通损耗：
  $$P_{cond} = I_D^2 \cdot R_{DS(on)}$$

- 开关损耗（近似）：
  $$E_{sw} \approx \frac{1}{2} V_{DS} \cdot I_D \cdot (t_{rise} + t_{fall})$$
  由于 SiC 器件极间电容小、反向恢复电荷低，$E_{sw}$ 显著低于同等硅 IGBT。

- 最大结温：连续工作 175 °C，M1H/G2 系列在过载条件下可支持 200 °C（累计 100 h）。

CoolSiC M1H 采用非对称沟槽栅结构，优化了栅氧可靠性与体二极管鲁棒性；G2 代进一步降低 $R_{DS(on)}$ 并扩展栅压窗口，支持单极 0/+18 V 驱动。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 电压等级 | 650 V / 1200 V / 2000 V | Infineon 产品页 |
| 导通电阻 $R_{DS(on)}$ | 数 mΩ 至数百 mΩ（依封装/电流） | 产品系列 |
| 额定电流（模块） | 55 A – 560 A | 模块 datasheet |
| 栅-源阈值电压 $V_{GS(th)}$ | 约 4.0–4.5 V | M1H/G2 datasheet |
| 推荐开通栅压 | +15 V 至 +18 V | 应用笔记 |
| 推荐关断栅压 | -3 V 至 -5 V 或 0 V | M1H 应用笔记 |
| 最大静态栅-源电压 | +20 V / -7 V | 应用笔记 |
| 最大动态栅-源电压 | +23 V / -10 V（占空比 <1%） | 应用笔记 |
| 连续工作结温 | 175 °C | 应用笔记 |
| 过载工作结温（G2） | 200 °C（累计 100 h） | 应用笔记 |
| 短路耐受时间 | 2 µs（G2） | Mouser / Infineon |
| 封装形式 | TO-247-4、D²PAK、Easy 1B/2B、62 mm、EconoDUAL | 产品系列 |
| 典型应用拓扑 | 半桥 / 全桥逆变器、Buck/Boost DC-DC | 产品资料 |

## 应用场景

- **人形机器人关节驱动**：作为伺服逆变器主开关器件，提高电机动态响应与续航。
- **电动汽车电驱逆变器**：降低开关损耗，支持 800 V 高压平台。
- **光伏/储能变流器**：提升转换效率，减小磁性元件体积。
- **工业伺服与电源**：高开关频率实现高精度电流控制。

## 供应链关系

- **制造商**：Infineon Technologies AG（ent_company_infineon），德国功率半导体龙头。
- **上游关键物料**：SiC 衬底（Wolfspeed、SICC、Coherent）、外延片、封装陶瓷基板（AlN）、键合线。
- **下游整机集成**：电驱逆变器、机器人伺服驱动器、光伏/储能变流器 OEM。
- **竞争/对标**：STMicroelectronics STPOWER SiC、Wolfspeed、ROHM、Onsemi、Mitsubishi Electric。

## 来源与验证

- Infineon CoolSiC MOSFET 产品页：https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/
- Infineon 应用笔记 AN2025-10：https://www.infineon.com/assets/row/public/documents/60/42/infineon-an2025-10-understanding-and-interpreting-the-coolsic-mosfet-1200v-datasheet-applicationnotes-en.pdf
- FF55MR12W1M1H_B70 模块页：https://www.infineon.com/cms/cn/product/power/mosfet/silicon-carbide/modules/ff55mr12w1m1h_b70/