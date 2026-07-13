---
id: ent_component_casting_die
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 压铸模具
  en: Casting Die
status: active
sources:
- id: src_ent_component_casting_die_1
  type: website
  url: https://haichen-dcm.com/aluminum-alloy-die-casting-mold/
- id: src_ent_component_casting_die_2
  type: website
  url: https://seller.alibaba.com/blogs/2026/southeast-asia/machinery/tool-steel-mold-selection-guide-alibaba-b2b
- id: src_ent_component_casting_die_3
  type: website
  url: https://aobosteel.com/h13-vs-p20-steel/
- id: src_ent_component_casting_die_4
  type: website
  url: https://www.sanonchina.com/global-comparison-of-die-casting-mold-steels/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 压铸模具

## 概述

压铸模具（die casting die）是在高压下将熔融金属（通常为铝合金、镁合金或锌合金）注入精密型腔并快速凝固成形的工具。它是机器人结构件、电机外壳、关节壳体等金属零件批量生产的核心工艺装备，直接影响零件尺寸精度、表面质量、组织致密度与生产成本。

## 工作原理 / 技术架构

压铸过程包括合模、压射、保压、冷却、开模与顶出。熔融金属在压射冲头推动下以高速（30–60 m/s）通过浇口进入型腔，并在高压（60–90 MPa，冷室机典型值）下保持至凝固。模具承受的锁模力必须大于金属压力在分型面上的胀模力：

$$
F_{clamp} \ge p_{inj} \cdot A_{projected}
$$

其中 $p_{inj}$ 为压射比压，$A_{projected}$ 为铸件在分型面上的投影面积。

压铸模通常由定模（cover die）与动模（ejector die）组成，内部包含型腔、型芯、浇道、溢流槽、排气槽与冷却水道。模具材料需具备高温强度、抗热疲劳、耐磨与导热性能。铝合金压铸模常用 H13（4Cr5MoSiV1 / 1.2344 / SKD61）热作模具钢，经热处理后硬度达到 HRC 48–52。

模具热平衡对生产节拍与铸件质量至关重要。冷却水带走的热量 $Q$ 可近似表示为

$$
Q = \dot{m} c_p (T_{out} - T_{in})
$$

其中 $\dot{m}$ 为冷却水质量流量，$c_p$ 为比热容，$T_{out}-T_{in}$ 为进出水温差。合理设计随形冷却水道可缩短冷却时间、减少热节与变形。

## 关键参数表

| 参数项 | 典型值 | 备注/来源 |
|--------|--------|-----------|
| 常用材料 | H13 / SKD61 / 1.2344 / 4Cr5MoSiV1 | 热作模具钢 |
| 型腔硬度 | HRC 48–52（常见）；最高 HRC 56–60 | Haichen / vacfurnace |
| 压射比压 | 60–90 MPa（铝合金冷室机） | Haichen / Jinchen |
| 锁模力需求 | 按 $p_{inj} \cdot A_{projected}$ 计算 | 工程公式 |
| 模具工作温度 | 150–250°C（铝合金）；230–280°C（型腔表面峰值） | 多源公开资料 |
| 铸件浇注温度 | 670–710°C（铝合金 ADC12） | Jinchen Precision |
| 表面粗糙度 | Ra 0.8–3.2 µm（机加工面）；型腔可抛光至镜面 | ABIS Mould |
| 尺寸公差 | ISO-2768 M 级（压铸件常见） | CNBENKY |
| 模具寿命 | 5–10 万次（普通）至 50–100 万次（高端长寿命模具） | 视材料、涂层与维护 |
| 价格 | 未公开 | 按结构复杂度与寿命要求报价 |

## 应用场景

- **人形机器人结构件**：铝合金压铸用于躯干框架、关节壳体、手臂连杆，兼顾轻量化与结构刚度。
- **电机与减速器外壳**：压铸铝合金电机壳体提供散热鳍片与安装接口。
- **新能源汽车零部件**：电池托盘、电机壳体、控制器壳体等大规模压铸生产。
- **3C 电子与家电**：笔记本电脑外壳、灯具散热件等薄壁精密件。

## 供应链关系

压铸模具位于制造装备层级。上游为模具钢（H13 等）、热处理、涂层（PVD/CVD/激光熔覆）、刀具与加工服务；中游为专业模具设计与制造厂商；下游为压铸加工厂与机器人/汽车零部件 OEM。在人形机器人供应链中，压铸件由结构件供应商交付给机器人整机厂（如 CASBOT、LimX Dynamics、Pacsini 等），其质量直接影响整机组装精度与可靠性。

## 来源与验证

- 压铸模具材料、工艺参数与失效模式参考 Haichen DCM 技术文章。
- 模具钢分类与硬度数据参考 Alibaba B2B 工具钢选型指南。
- H13 与 P20 的选型对比及铝合金压铸参数参考 Aobo Steel 与 Sanon China 技术资料。