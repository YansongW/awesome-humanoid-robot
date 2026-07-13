---
id: ent_company_hao_zhi
schema_version: 1
type: company
'title:': Hao Zhi Electromechanical
domain: 02_components
theoretical_depth: system
names:
  zh: 昊志机电
  en: Hao Zhi Electromechanical
status: active
sources:
- id: src_hao_zhi_official
  type: website
  url: http://www.haozhi.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 昊志机电 / Hao Zhi Electromechanical

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 昊志机电 |
| **英文名** | Hao Zhi Electromechanical |
| **总部** | 中国广州 |
| **成立时间** | 2006 |
| **官网** | [http://www.haozhi.cn](http://www.haozhi.cn) |
| **供应链环节** | 主轴电机 / 力矩电机 / 谐波减速器 / 关节模组 |
| **企业属性** | 上市公司（SZ.300503）、国内品牌 |
| **母公司/所属集团** | 广州市昊志机电股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

国内高端电主轴龙头，拓展力矩电机、谐波减速器与人形机器人关节模组。

昊志机电起家于数控机床电主轴，逐步拓展至直线电机、力矩电机、谐波减速器和机器人关节模组。公司在高转速、高精度电机与精密传动方面具备技术积累，面向人形机器人提供一体化关节与核心传动部件。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 电主轴 | 高端数控主轴 | DGZX 系列 | CNC、雕铣、磨削 |
| 力矩电机 | 直驱力矩电机 | DMP 系列 | 转台、机器人关节 |
| 谐波减速器 | 精密谐波 | G 系列、H 系列 | 协作机器人、人形机器人 |

## 代表产品

### 力矩电机 / Hao Zhi Direct-Drive Torque Motor

> 力矩电机：请访问 [官方资料](http://www.haozhi.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 外径 100–300 mm（系列范围） | 产品手册 |
| 重量 | 2–15 kg | 产品手册 |
| 额定扭矩 | 5–200 N·m | 产品手册 |
| 峰值扭矩 | 15–600 N·m | 产品手册 |
| 额定转速 | 50–300 rpm | 产品手册 |
| 编码器 | 23 位绝对值 | 产品手册 |
| 冷却方式 | 自然冷却 / 水冷 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：直驱无背隙、高刚性、高扭矩密度，适合机器人关节与精密转台直接驱动。

**应用场景**：人形机器人髋/肩/腰关节、CNC 转台、半导体设备、天文望远镜。

### 谐波减速器 / Hao Zhi Harmonic Drive

> 谐波减速器：请访问 [官方资料](http://www.haozhi.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 外径 32–100 mm（系列范围） | 产品手册 |
| 重量 | 0.1–1.5 kg | 产品手册 |
| 减速比 | 50–160:1 | 产品手册 |
| 额定扭矩 | 3.9–112 N·m | 产品手册 |
| 背隙 | ≤ 1 arc-min | 产品手册 |
| 最高输入转速 | 6,500 rpm | 产品手册 |
| 安装方式 | 杯型 / 帽型 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：自主齿形设计、高扭转刚度、低背隙，适配协作与人形机器人关节。

**应用场景**：协作机器人关节、人形机器人手臂/腿部、半导体转台、医疗机器人。

## 供应链位置

- **上游关键零部件/材料**：稀土永磁体、轴承、合金钢（柔轮/刚轮）、铜线、绝缘材料
- **下游客户/应用场景**：数控机床厂商、机器人整机厂、半导体设备、人形机器人 OEM
- **主要竞争对手/对标**：Harmonic Drive、绿的谐波、来福谐波、大族传动、新宝

## 知识图谱节点与关系

- 公司实体：`ent_company_hao_zhi`
- 产品/零部件实体：`ent_component_hao_zhi_torque_motor`, `ent_component_hao_zhi_harmonic_drive`
- 关键关系：
  - `ent_company_hao_zhi` -- `manufactures` --> `ent_component_hao_zhi_torque_motor`
  - `ent_company_hao_zhi` -- `manufactures` --> `ent_component_hao_zhi_harmonic_drive`

## 参考资料

1. [官网](http://www.haozhi.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）