# {{company_name_zh}} / {{company_name_en}}

> 本词条属于 [附录 D 企业/产品 Wiki](../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | {{company_name_zh}} |
| **英文名** | {{company_name_en}} |
| **总部** | {{hq}} |
| **成立时间** | {{founded}} |
| **官网** | `{{website}}` |
| **供应链环节** | {{tags}} |
| **企业属性** | {{attributes}} |
| **母公司/所属集团** | {{parent}} |
| **数据来源** | {{sources}} |

## 公司简介

{{one_sentence_positioning}}

{{company_description}}

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| {{product_line_1}} | {{positioning_1}} | {{representative_1}} | {{application_1}} |
| {{product_line_2}} | {{positioning_2}} | {{representative_2}} | {{application_2}} |

## 代表产品

### {{product_name_1}}

> 图片：请参见官方公开资料。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | {{dimension_1}} | {{source_1}} |
| 重量 | {{weight_1}} | {{source_1}} |
| 自由度 | {{dof_1}} | {{source_1}} |
| 负载/扭矩 | {{payload_1}} | {{source_1}} |
| 速度/转速 | {{speed_1}} | {{source_1}} |
| 续航 | {{endurance_1}} | {{source_1}} |
| 接口/通信 | {{interface_1}} | {{source_1}} |
| 价格 | {{price_1}} | {{source_1}} |

**技术亮点**：{{highlights_1}}

**应用场景**：{{applications_1}}

### {{product_name_2}}

> 图片：请参见官方公开资料。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | {{dimension_2}} | {{source_2}} |
| 重量 | {{weight_2}} | {{source_2}} |
| 自由度 | {{dof_2}} | {{source_2}} |
| 负载/扭矩 | {{payload_2}} | {{source_2}} |
| 速度/转速 | {{speed_2}} | {{source_2}} |
| 续航 | {{endurance_2}} | {{source_2}} |
| 接口/通信 | {{interface_2}} | {{source_2}} |
| 价格 | {{price_2}} | {{source_2}} |

**技术亮点**：{{highlights_2}}

**应用场景**：{{applications_2}}

## 供应链位置

- **上游关键零部件/材料**：{{upstream}}
- **下游客户/应用场景**：{{downstream}}
- **主要竞争对手/对标**：{{competitors}}

## 知识图谱节点与关系

- 公司实体：`ent_company_{{company_id}}`
- 产品实体：`ent_product_{{product_id_1}}`、`ent_product_{{product_id_2}}`
- 关键关系：
  - `ent_company_{{company_id}}` -- `manufactures` --> `ent_product_{{product_id_1}}`
  - `ent_product_{{product_id_1}}` -- `uses` --> `ent_component_xxx`
  - `ent_company_{{company_id}}` -- `supplies` --> `ent_company_xxx`

## 参考资料

1. 官网：`{{website}}`
2. WAIC 2026 参展报道：`{{waic_source}}`
3. 其他公开资料：`{{other_source}}`