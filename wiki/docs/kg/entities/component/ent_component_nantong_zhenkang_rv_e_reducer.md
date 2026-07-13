---
id: ent_component_nantong_zhenkang_rv_e_reducer
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 南通振康 RV-E 减速器
  en: Nantong Zhenkang RV-E Reducer
status: active
sources:
- id: src_nantong_zhenkang_company
  type: website
  url: https://www.zhenkang.com/page/230792_en.html
- id: src_zhenkang_rv_catalog
  type: website
  url: https://www.grandwelding.com/rv-reducer/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 南通振康 RV-E 减速器 / Nantong Zhenkang RV-E Reducer

## 概述

南通振康焊接机电有限公司是国内较早实现 RV 减速器批量生产的企业之一，其 ZKRV-E 系列减速器采用两级封闭式行星传动结构，专为工业机器人、焊接机器人、人形机器人重载关节及精密转台设计。该系列产品具有减速比范围宽、扭矩密度高、回程间隙小、抗冲击能力强等特点，是国产 RV 减速器的重要代表。

## 工作原理 / 技术架构

ZKRV-E 系列减速器由第一级渐开线行星齿轮减速与第二级摆线针轮行星减速组成：

1. **第一级减速**：伺服电机驱动中心轮，通过行星轮与行星架实现初步减速与扭矩放大。
2. **第二级减速**：行星架带动偏心曲轴，驱动摆线轮在针齿壳内作行星运动；摆线轮与针齿的多齿啮合（啮合率通常高于 80%）实现高精度、高刚性输出。

传动比定义为
\[
i = \frac{n_{\text{in}}}{n_{\text{out}}}
\]
输出扭矩与输入扭矩的关系为
\[
\tau_{\text{out}} = \tau_{\text{in}} \cdot i \cdot \eta
\]
其中 \(\eta\) 为传动效率，ZKRV-E 系列典型效率为 85%–95%。

回程间隙（backlash）是精密减速器的关键指标，ZKRV-E 系列公开指标为不大于 1 弧分，适用于机器人关节的高精度定位需求。

## 关键参数表

| 参数项 | ZKRV-20E | ZKRV-40E | ZKRV-80E | ZKRV-110E | ZKRV-160E | ZKRV-320E | ZKRV-450E |
|---|---|---|---|---|---|---|---|
| 额定扭矩 | 180 N·m | 400 N·m | 800 N·m | 1100 N·m | 1600 N·m | 3200 N·m | 4500 N·m |
| 允许加减速扭矩 | 450 N·m | 1000 N·m | 2000 N·m | 2750 N·m | 4000 N·m | 8000 N·m | 11250 N·m |
| 最大允许扭矩（急停） | 900 N·m | 2000 N·m | 4000 N·m | 5500 N·m | 8000 N·m | 16000 N·m | 22500 N·m |
| 减速比范围 | 81–161 | 81–153 | 81–153 | 81–161 | 81–171 | 81–185 | 81–171 |
| 最大输出转速 | 75 rpm | 70 rpm | 70 rpm | 50 rpm | 40 rpm | 35 rpm | 25 rpm |
| 回程间隙 | ≤1 arcmin | ≤1 arcmin | ≤1 arcmin | ≤1 arcmin | ≤1 arcmin | ≤1 arcmin | ≤1 arcmin |
| 重量 | 4.7 kg | 9.3 kg | 13.1 kg | 17.4 kg | 26.4 kg | 44.3 kg | 66.4 kg |

注：以上数据来自 ZKRV-E 系列公开性能表；具体型号的精确参数应以南通振康官方产品手册为准。

## 应用场景

- **工业机器人**：底座、肩部、腰部等重载关节的精密减速。
- **焊接机器人**：配合焊接送丝机与伺服电机，满足高负载、高重复定位需求。
- **人形机器人**：髋、膝等大扭矩关节的国产替代方案。
- **精密转台与雷达**：利用高刚性与低回程间隙实现精密角度定位。

## 供应链关系

- **上游**：轴承钢、摆线轮毛坯、针齿壳、曲轴、轴承、密封件、润滑脂。
- **制造商**：南通振康焊接机电有限公司设计并生产 ZKRV-E 系列。
- **下游**：工业机器人整机厂、焊接机器人集成商、人形机器人研发企业、精密机床与雷达制造商。
- **图谱位置**：`ent_company_nantong_zhenkang` → `manufactures` → `ent_component_nantong_zhenkang_rv_e_reducer`；该零部件常用于重载机器人关节，与电机、编码器共同构成执行器模组。

## 来源与验证

- 公司背景与产品线来自南通振康官网英文公司介绍页。
- ZKRV-E 系列性能参数表来自公开渠道发布的振康 RV 减速器性能资料。
- 附录 D 企业 Wiki 亦对其供应链位置进行了归纳。