---
id: ent_company_weihong
schema_version: 1
type: company
title: Weihong Electronic Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 维宏股份
  en: Weihong Electronic Technology
status: active
sources:
  - id: src_weihong_official
    type: website
    title: Weihong Official Website
    url: https://www.weihong.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 维宏股份 / Weihong Electronic Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 维宏股份 |
| **英文名** | Weihong Electronic Technology |
| **总部** | 中国上海 |
| **成立时间** | 2007 |
| **官网** | [https://www.weihong.com.cn](https://www.weihong.com.cn) |
| **供应链环节** | 运动控制器 / CNC 系统 / 伺服驱动 |
| **企业属性** | 国产品牌、上市公司（300508.SZ） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 维宏官网、产品手册、年报、WAIC 2026 报道 |

## 公司简介

维宏股份是中国运动控制与 CNC 系统领域的代表企业，专注于雕刻机、切割机、激光加工与数控机床控制系统。

公司以开放式运动控制平台为核心，提供从控制卡、一体机到伺服驱动的完整解决方案，在木工、广告、金属加工与 3C 行业拥有大量客户。维宏的 CNC 系统以高性价比、易二次开发与行业适配能力强著称，并逐步向工业机器人与人形机器人核心控制领域延伸。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| NK 系列运动控制器 | 多轴一体控制器 | NK300BX / NK280 | 雕刻、切割、CNC |
| 雕刻机控制系统 | 行业专用 CNC | NcStudio | 广告、木工、模具 |
| 伺服驱动 | 进给轴驱动 | 未公开 | 机床、机器人 |

## 代表产品

### NK300BX 运动控制器 / NK300BX Motion Controller

> NK300BX 运动控制器：请访问 [官方资料](https://www.weihong.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 多轴一体化运动控制器 | 维宏官网 |
| 控制轴数 | 最多 6 轴 | 产品手册 |
| 联动轴数 | 3/4/5 轴（视配置） | 产品手册 |
| 控制精度 | 0.001 mm（参考） | 产品手册 |
| 通信接口 | Ethernet / USB | 产品手册 |
| 编程语言 | G 代码 / 宏程序 | 产品手册 |
| 操作系统 | 嵌入式 Linux / Windows | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：集成度高、界面友好、支持多工艺包，适配雕刻切割与小型 CNC 设备。

**应用场景**：木工雕刻机、广告切割机、金属模具机、3C 加工设备。

### NcStudio 雕刻机控制系统 / NcStudio Engraving Control System

> NcStudio 控制系统：请访问 [官方资料](https://www.weihong.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | PC-based CNC 软件+控制卡 | 维宏官网 |
| 控制轴数 | 3–5 轴 | 产品手册 |
| 插补方式 | 直线/圆弧/样条 | 产品手册 |
| 接口 | PCI/PCIe/以太网 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：行业适配广泛、二次开发便捷，是国内雕刻机市场占有率较高的控制方案。

**应用场景**：广告雕刻、木工雕花、模具加工、玉石雕刻。

## 供应链位置

- **上游关键零部件/材料**：工业计算机、显示面板、FPGA/DSP、PCB、接插件、电容电阻。
- **下游客户/应用场景**：雕刻机/切割机制造商、机床厂、3C 加工、广告设备、木工机械。
- **主要竞争对手/对标**：柏楚电子、固高科技、西门子、发那科、三菱。

## 知识图谱节点与关系

- 公司实体：`ent_company_weihong`
- 产品实体：`ent_component_weihong_nk300bx`、`ent_component_weihong_ncstudio`
- 关键关系：
  - `ent_company_weihong` -- `manufactures` --> `ent_component_weihong_nk300bx`
  - `ent_company_weihong` -- `manufactures` --> `ent_component_weihong_ncstudio`

## 参考资料

1. [维宏股份官网](https://www.weihong.com.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 维宏股份年报与产品手册