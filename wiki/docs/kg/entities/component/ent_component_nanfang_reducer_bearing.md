---
id: ent_component_nanfang_reducer_bearing
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 南方精工减速器配套轴承
  en: Nanfang Precision Reducer Bearing
sources:
- id: src_nanfang_official
  type: website
- title: 南方精工官网
  url: http://www.nanfangbearing.com
- id: src_robot_bearing_report
  type: report
- title: 轴承行业专题分析：机器人带来全新机遇
  url: https://finance.sina.com.cn/stock/stockzmt/2023-08-01/doc-imzesvcy0118599.shtml
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Nanfang Precision company profile and industry
    reports; detailed model-level parameters are not fully disclosed and marked as
    未公开.
---


# 南方精工减速器配套轴承 / Nanfang Precision Reducer Bearing

## 概述

南方精工减速器配套轴承是江苏南方精工股份有限公司面向工业机器人与人形机器人减速器开发的专用轴承产品。该系列轴承针对 RV 减速器与谐波减速器的高倾覆力矩、高刚性与高精度要求设计，结构形式包括薄壁角接触轴承、交叉滚子轴承等，用于支撑减速器输出轴与关节旋转部位。

## 工作原理与技术架构

减速器配套轴承在机器人关节中承担以下功能：

1. **支撑旋转轴**：承受径向、轴向及倾覆力矩复合载荷，保证减速器输出轴的旋转精度。
2. **保持系统刚性**：高刚度轴承可降低关节在负载作用下的弹性变形，提高末端定位精度。
3. **精度传递**：轴承精度等级达到 P5/P4，与减速器输出精度匹配，减少传动误差。
4. **长寿命设计**：针对机器人关节频繁启停、往复运动的工况，优化轴承沟道几何与保持架设计，目标寿命 $L_{10} \ge 10{,}000~\text{h}$。

典型结构：

- **RV 减速器**：主支撑常用薄壁角接触球轴承（接触角约 40°），偏心轴处用圆锥滚子轴承，摆线轮处用圆柱滚子/滚针保持架组件。
- **谐波减速器**：输出端采用交叉滚子轴承（刚性轴承），波发生器处采用柔性轴承。

轴承刚度 $k$ 与滚道接触变形 $δ$、载荷 $F$ 的关系可近似表示为：

$$
k = \frac{\partial F}{\partial \delta}
$$

高刚度设计通过增大滚动体数量、优化接触角及预紧实现。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 适配减速器类型 | RV 减速器 / 谐波减速器 | 南方精工产品手册 |
| 主要结构 | 薄壁角接触轴承 / 交叉滚子轴承 | 南方精工产品手册 |
| 精度等级 | P5 / P4 | 南方精工产品手册 |
| 额定动载荷 | 依型号 | 南方精工产品手册 |
| 刚度 | 高刚性 | 南方精工产品手册 |
| 目标寿命 | $L_{10} \ge 10{,}000~\text{h}$ | 南方精工产品手册 |
| 材质 | 轴承钢 GCr15 | 南方精工产品手册 |
| 润滑方式 | 油脂 / 油润滑 | 南方精工产品手册 |
| 尺寸范围 | 未公开 | - |
| 价格 | 未公开 | - |

注：南方精工未公开减速器配套轴承的完整型号、尺寸范围及载荷-寿命数据表，上表为产品系列级参数。

## 应用场景

- **工业机器人基座/腕部**：RV/谐波减速器主轴承支撑。
- **人形机器人髋/肩/腰关节**：高倾覆力矩场景下的旋转关节支撑。
- **协作机器人关节**：轻量化、高精度的减速器输出端支撑。
- **数控机床转台**：交叉滚子轴承用于高精度旋转工作台。
- **自动化产线**：高负载、高刚性旋转机构。

## 供应链关系

- **上游**：轴承钢 GCr15、滚针/钢球、保持架、润滑油/脂、热处理与磨加工设备。
- **制造商**：南方精工（Jiangsu Nanfang Precision）通过关系 `ent_company_nanfang_precision -- manufactures --> ent_component_nanfang_reducer_bearing` 记录于知识图谱。
- **下游**：机器人减速器厂商、人形机器人整机厂、汽车变速箱厂商、工业设备制造商。主要竞争对手包括 INA、NTN、IKO、洛阳轴承、五洲新春等。

## 来源与验证

产品定位、适配类型、结构形式、精度等级及目标寿命来自南方精工企业 Wiki 与产品手册。具体型号尺寸、额定动载荷及价格未在公开渠道披露，已标注为未公开。