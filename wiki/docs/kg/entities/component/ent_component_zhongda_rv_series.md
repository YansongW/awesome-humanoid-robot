---
id: ent_component_zhongda_rv_series
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: 中大力德 RVE/RVC 系列 RV 减速器
  en: Zhongda Smart Transmission RVE/RVC Series RV Reducer
sources:
- id: src_zhongda_official
  type: website
- title: Zhongda Smart Transmission Official Website
  url: https://www.zd-drivers.com
- id: src_dongfang_rv_report
  type: report
- title: 环动科技招股书 / 东方财富 RV 减速器行业数据
  url: https://pdf.dfcfw.com/pdf/H3_AP202403191627111620_1.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  review_notes: RVE/RVC is a product series; exact per-model values vary. Data below
    are representative range values from public prospectus and company manual.
---


# 中大力德 RVE/RVC 系列 RV 减速器 / Zhongda Smart Transmission RVE/RVC Series RV Reducer

## 概述

中大力德 RVE/RVC 系列是国产 RV 减速器产品线，覆盖工业机器人重载关节与精密转台应用。RVE 系列为常规中空/实心轴 RV 减速器，RVC 系列为紧凑型中空结构，二者均采用两级摆线行星减速原理，具有大减速比、高刚性、抗冲击能力强等特点。该系列产品已实现批量供货，是国产机器人传动核心部件的重要选项之一。

## 工作原理 / 技术架构

RVE/RVC 系列采用标准 RV（Rotary Vector）减速原理：

1. **第一级行星减速**：输入太阳轮驱动 3 个行星轮，行星轮带动偏心曲柄轴旋转。
2. **第二级摆线针轮减速**：两片相位差 180° 的摆线轮与针齿壳内针齿啮合，实现大减速比输出。
3. **输出机构**：摆线轮自转经曲柄轴传递给输出盘，输出盘内置主轴承承受外部负载。

总传动比为两级减速比乘积：
$$i = i_{planetary} \cdot i_{cycloidal}$$
其中摆线针轮级传动比 $i_{cycloidal} = \frac{Z_p}{Z_p - Z_c}$，$Z_p$ 为针齿数，$Z_c$ 为摆线轮齿数。

输出扭矩：
$$T_{out} = \eta \cdot i \cdot T_{in}$$
典型传动效率 $\eta$ > 78%。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 系列 | RVE / RVC | 中大力德 |
| 传动比范围 | 26 – 192.4:1 | 环动科技招股书 |
| 额定扭矩范围 | 58.8 – 4900 N·m | 环动科技招股书 |
| 背隙 | < 1.5 arcmin | 环动科技招股书 |
| 传动误差 | < 90 arcsec | 环动科技招股书 |
| 额定效率 | > 78% | 环动科技招股书 |
| 结构 | 两级摆线行星 + 内置主轴承 | 中大力德年报 |
| 重量（具体型号） | 未公开 | - |
| 噪声（系列典型） | < 75 dB(A) | 行业公开资料 |
| 额定寿命（系列典型） | 6000 h（额定工况） | RV 减速器通用指标 |

## 应用场景

- **工业机器人 J1–J3 关节**：基座、大臂、肩部等重载高刚性位置。
- **人形机器人腰/髋关节**：配合大扭矩电机实现稳定站立与行走。
- **CNC 转台与焊接变位机**：利用高刚性、大扭矩与低背隙特性。
- **重型自动化设备**：输送、码垛与装配线中的精密旋转驱动。

## 供应链关系

- **制造商**：中大力德 Zhongda Smart Transmission（ent_company_zhongda），浙江慈溪上市公司。
- **上游关键物料**：合金钢、轴承、润滑脂、齿轮毛坯、铝材。
- **下游整机集成**：宇树科技、智元机器人、埃斯顿、埃夫特等工业机器人与人形机器人 OEM。
- **竞争/对标**：Nabtesco RV 系列、双环传动 SHPR 系列、绿的谐波（谐波减速器）、秦川机床。

## 来源与验证

- 中大力德官网：https://www.zd-drivers.com
- 东方财富 RV 减速器行业研报（引用环动科技招股书）：https://pdf.dfcfw.com/pdf/H3_AP202403191627111620_1.pdf