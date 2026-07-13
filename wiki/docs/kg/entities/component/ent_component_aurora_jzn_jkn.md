---
id: ent_component_aurora_jzn_jkn
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 奥普光电/禹衡光学 JZN/JKN 系列光栅角度编码器
  en: Aurora Optics / Yuheng JZN/JKN Optical Angle Encoder
status: active
sources:
- id: src_yuheng_encoder
  type: website
  url: https://www.yu-heng.cn/
- id: src_aurora_optics
  type: website
  url: http://www.aoptek.com/
- id: src_dongfang_report
  type: white_paper
  url: https://pdf.dfcfw.com/pdf/H3_AP202210201579322747_1.pdf
- id: src_jiemian_news
  type: website
  url: https://www.jiemian.com/article/9576073.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 奥普光电/禹衡光学 JZN/JKN 系列光栅角度编码器

## 概述

JZN/JKN 系列光栅角度编码器由奥普光电（深交所：002338）控股子公司长春禹衡光学研制，是国产高端光栅编码器的代表性产品。该系列采用金属光栅与光电扫描技术，具备高精度、高可靠性与良好的环境适应性，公开披露的最高精度绝对式光栅编码器可达 **29 位**，产品通过 RoHS、CE、防爆及军工产品实验验证等多项认证，主要面向高端数控机床、伺服电机、机器人关节与航空航天测控。

## 工作原理 / 技术架构

光栅角度编码器通过读取金属或玻璃光栅圆盘上的刻线，将角位移转换为电脉冲或绝对位置码。JZN/JKN 系列采用光电扫描原理：光源（LED 或激光）照射金属光栅，透射/反射光经光电探测器转换为正交信号，再经信号处理电路输出角度信息。

对于绝对式编码器，单圈分辨能力由编码位数决定。29 位绝对式编码器每转可分辨的位置数为：

$$
N = 2^{29} = 536\,870\,912 \ \text{counts/rev}
$$

对应的角分辨率：

$$
\theta_{\text{res}} = \frac{360°}{2^{29}} = \frac{360 \times 3600''}{2^{29}} \approx 2.41 \times 10^{-3} \ \text{arcsec}
$$

实际系统精度受安装同心度、轴系跳动、热变形与电子细分误差影响，通常以角秒（arcsec）或角分（arcmin）标定。奥普光电公开称其产品精度达到“国内领先、国际同类先进”水平。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 奥普光电 / 长春禹衡光学 |
| 类型 | 高精度光栅角度编码器 |
| 扫描原理 | 光电 / 金属光栅扫描 |
| 最高分辨率 | 29 位绝对式（公司公开披露） |
| 精度等级 | 国内领先、国际同类先进 |
| 认证 | RoHS、CE、防爆、军工产品实验验证 |
| 工作温度 | 未公开 |
| 供电电压 | 未公开 |
| 通信接口 | 未公开 |
| 外壳直径 / 重量 | 未公开 |
| 价格 | 未公开 |

## 应用场景

- **高端数控机床**：转台、刀库与第四/五轴精密角度反馈。
- **伺服电机**：旋转位置与速度反馈，提升全闭环控制精度。
- **人形机器人关节**：关节角度高精度测量，支撑运动控制与力位混合控制。
- **航空航天/军工**：雷达天线座、光电经纬仪、精密转台的角度测量。

## 供应链关系

在公司—产品—零部件网络中，JZN/JKN 编码器处于**精密传感零部件层**：

- **上游**：光学玻璃/金属光栅、LED/激光光源、光电探测器、精密轴承、电子元器件。
- **自身位置**：`ent_company_aurora_optics -- manufactures --> ent_component_aurora_jzn_jkn`；`ent_component_aurora_jzn_jkn -- used_in --> ent_product_humanoid_robot_joint`。
- **下游**：高端数控系统、伺服驱动器、工业机器人、人形机器人关节模组及航空航天测控设备。

## 来源与验证

- 长春禹衡光学官网：https://www.yu-heng.cn/
- 奥普光电官网：http://www.aoptek.com/
- 东方财富证券研报：https://pdf.dfcfw.com/pdf/H3_AP202210201579322747_1.pdf
- 界面新闻关于 29 位绝对式编码器的报道：https://www.jiemian.com/article/9576073.html

29 位分辨率、金属光栅技术及国产替代定位均来自公开资料；具体型号的工作温度、供电、接口与机械尺寸未在公开渠道披露。