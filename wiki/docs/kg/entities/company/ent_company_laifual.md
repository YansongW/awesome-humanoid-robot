---
id: ent_company_laifual
schema_version: 1
type: company
'title:': Laifual
domain: 02_components
theoretical_depth: system
names:
  zh: 来福谐波
  en: Laifual
status: active
sources:
- id: src_laifual_official
  type: website
  url: https://www.laifual.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 来福谐波 / Laifual

# 来福谐波 / Laifual

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 来福谐波 |
| **英文名** | Laifual |
| **总部** | 中国浙江嵊州 |
| **成立时间** | 2013 |
| **官网** | [https://www.laifual.com](https://www.laifual.com) |
| **供应链环节** | 谐波减速器 / 行星减速器 / 关节模组 |
| **企业属性** | 国产品牌、国家高新技术企业 |
| **母公司/所属集团** | 无（独立） |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

国产谐波减速器主要厂商之一，产品覆盖 LSS/LSG/LHT/LHD 等多个系列。

来福谐波从事高精密谐波减速器和行星减速器的研发与制造，拥有 30,000 平方米标准厂房，产品广泛应用于工业机器人、服务机器人、医疗设备和高端自动化装备。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| LSS/LSG 杯型谐波 | 标准/高扭矩谐波减速器 | LSS-32 / LSG-32 | 机器人关节 |
| LHT/LHD 中空型 | 中空/超薄谐波减速器 | LHT-25 / LHD-32 | 协作/人形机器人 |

## 代表产品

### LSS-32-100-U-I 谐波减速器 / LSS-32-100-U-I Harmonic Reducer

> LSS-32-100-U-I 谐波减速器：请访问 [官方资料](https://www.laifual.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 规格 | 32 | Laifual LSS 参数表 |
| 减速比 | 50/80/100/120:1 | Laifual LSS 参数表 |
| 额定扭矩（2000rpm） | 76/118/137/137 N·m | Laifual LSS 参数表 |
| 启动停止容许扭矩 | 216/304/333/333 N·m | Laifual LSS 参数表 |
| 平均负载容许扭矩 | 108/167/216/216 N·m | Laifual LSS 参数表 |
| 瞬时最大扭矩 | 382/568/647/686 N·m | Laifual LSS 参数表 |
| 最高输入转速 | 4800 rpm | Laifual LSS 参数表 |
| 背隙 | ≤ 20 arcsec | Laifual LSS 参数表 |
| 重量 | 3.11 kg | Laifual LSS 参数表 |

**技术亮点**：杯型标准结构、高刚性交叉滚子轴承，承载力与寿命接近国际主流水平。

**应用场景**：工业机器人关节、人形机器人手臂、自动化转台。

### LHD-32-100-U-I 超薄谐波减速器 / LHD-32-100-U-I Ultra-thin Harmonic Reducer

> LHD-32-100-U-I 超薄谐波减速器：请访问 [官方资料](https://www.laifual.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 规格 | 32 | 来福产品页 |
| 减速比 | 50/80/100:1 | 来福产品页 |
| 额定扭矩 | 未公开 | - |
| 轴向长度 | LHD-I 较标准型缩短约 50% | 来福产品页 |
| 结构 | 超薄中空翻边 + 交叉滚子轴承 | 来福产品页 |
| 重量 | 未公开 | - |
| 背隙 | ≤ 20 arcsec | 来福产品页 |

**技术亮点**：超薄扁平设计，适合对轴向尺寸和重量敏感的机器人关节。

**应用场景**：协作机器人末端、人形机器人腕部、医疗机械臂。

## 供应链位置

- **上游关键零部件/材料**：合金钢、柔性轴承、润滑脂、铝合金
- **下游客户/应用场景**：工业机器人、服务机器人、医疗设备、自动化设备厂商
- **主要竞争对手/对标**：绿的谐波、Harmonic Drive Systems、同川精密

## 知识图谱节点与关系

- 公司实体：`ent_company_laifual`
- 产品实体：`ent_component_laifual_lss_32_100`、`ent_component_laifual_lhd_32_100`
- 关键关系：
  - `ent_company_laifual` -- `manufactures` --> `ent_component_laifual_lss_32_100`
  - `ent_company_laifual` -- `manufactures` --> `ent_component_laifual_lhd_32_100`

## 参考资料

1. [官网](https://www.laifual.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）