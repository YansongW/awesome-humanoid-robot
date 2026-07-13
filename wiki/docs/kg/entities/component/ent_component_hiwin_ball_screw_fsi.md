---
id: ent_component_hiwin_ball_screw_fsi
schema_version: 1
type: component
'title:': HIWIN FSI 转造级滚珠丝杠
domain: 02_components
theoretical_depth: system
names:
  zh: HIWIN FSI 转造级滚珠丝杠
  en: HIWIN FSI Rolled Ball Screw
status: active
sources:
- id: src_hiwin_hiwin_ball_screw_fsi_official
  type: website
  url: https://www.hiwin.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# HIWIN FSI 转造级滚珠丝杠 / HIWIN FSI Rolled Ball Screw

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [上银科技 / HIWIN](../../../appendices/appendix-d/companies/company_hiwin.md) |
| **产品类别** | 滚珠丝杠 / 直线传动 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [上银科技 官网](https://www.hiwin.com) |

## 产品概述

HIWIN FSI 系列为转造级滚珠丝杠，以双切边法兰单螺母和零背隙预紧选项为特点。以 R16-5T3 为例，丝杠直径 16 mm、导程 5 mm，转造精度等级 C7，适用于一般自动化与成本敏感的线性定位场合。

FSI 系列最大长度可达约 3,000 mm，Dm-N 值最高约 220,000，可搭配 HIWIN HG/EG 线性滑轨与伺服电机构成 KK 线性模组或人形机器人线性关节。研磨级可选 C5/C3，满足更高精度需求。

## 产品图片

> HIWIN FSI 转造级滚珠丝杠 / HIWIN FSI Rolled Ball Screw：请访问 [官方资料](https://www.hiwin.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 丝杠直径 | 16 mm | 产品手册 |
| 导程 | 5 mm / 10 mm（可选） | 产品手册 |
| 精度等级 | C7（转造）；C5/C3 研磨可选 | 产品手册 |
| 最大长度 | 约 3,000 mm（转造，依规格） | 产品手册 |
| 轴向间隙 | P0 零背隙（预紧可选） | 产品手册 |
| 螺母型式 | 双切边法兰单螺母（FSI） | 产品手册 |
| Dm-N 值 | 最高约 220,000 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[上银科技 / HIWIN](../../../appendices/appendix-d/companies/company_hiwin.md)
- **核心零部件/技术来源**：轴承钢螺杆、钢珠、螺母、密封件、预紧垫片、润滑脂、电机
- **下游应用/客户**：CNC 机床、自动化设备、人形机器人线性关节、半导体、医疗

## 知识图谱节点与关系

- 零部件实体：`ent_component_hiwin_ball_screw_fsi`
- 制造商实体：`ent_company_hiwin`
- 关键关系：
  - `rel_ent_company_hiwin_manufactures_ent_component_hiwin_ball_screw_fsi`（`ent_company_hiwin` --> `manufactures` --> `ent_component_hiwin_ball_screw_fsi`）

## 应用场景

- **工业机器人**：工业机器人线性模组、末端执行器驱动
- **人形机器人**：线性关节、躯干/腿部伸缩模组
- **数控机床**：CNC 机床进给轴、雕刻机
- **其他自动化**：半导体搬运、3C 检测、医疗定位

## 竞争对比

| 对比项 | FSI 滚珠丝杠 | THK LM Guide | NSK Ball Screw |
|--------|------------------------|---------------|---------------|
| 核心优势 | 性价比、完整线性运动方案 | 导轨发明者、品牌 | 轴承/丝杠协同 |
| 背隙/精度 | C7（转造）/ C5/C3（研磨） | 导轨精度 P/SP/UP | C3–C10 |
| 价格水平 | 中端 | 高端 | 高端 |
| 交付周期 | 较短 | 中等 | 中等 |

## 选购与部署建议

一般定位选 C7 转造级即可满足；高精度或长寿命场景建议升级 C5/C3 研磨级并配合预紧螺母。

## 参考资料

1. [上银科技 官网](https://www.hiwin.com)
2. [HIWIN Ballscrews](https://www.hiwin.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)