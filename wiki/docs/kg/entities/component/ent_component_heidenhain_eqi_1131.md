---
id: ent_component_heidenhain_eqi_1131
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 海德汉 EQI 1131 绝对式旋转编码器
  en: HEIDENHAIN EQI 1131 Absolute Rotary Encoder
status: active
sources:
- id: src_heidenhain_eqi1131_pi
  type: website
  url: https://www.heidenhain.com/fileadmin/pdb/media/pdfs/EQI_1131__PI_0601-2.pdf
- id: src_heidenhain_eqi1131_page
  type: website
  url: https://www.heidenhain.com/en/products/encoders/rotary-encoders/eqi-1131
- id: src_br_endat_safety
  type: website
  url: https://www.br-automation.com/en/products/product-overview/encoder-modules/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 海德汉 EQI 1131 绝对式旋转编码器 / HEIDENHAIN EQI 1131 Absolute Rotary Encoder

## 概述

EQI 1131 是 HEIDENHAIN 推出的无内置轴承绝对式旋转编码器，采用感应扫描原理与纯串行 EnDat 2.2 接口，专为功能安全要求较高的伺服驱动与机器人关节设计。该系列提供单圈与多圈版本，单圈分辨率可达 19 bit，多圈圈数计数 12 bit（4096 圈），并满足 SIL 3 / PL e 等级要求，可直接用于安全扭矩关闭（STO/Safe torque off）等应用。

## 工作原理 / 技术架构

EQI 1131 通过感应式扫描测量转轴角位置，转轴上安装编码盘，定子绕组产生激励磁场并在编码盘处感应出周期性信号。输出信号经内部数字处理后以 EnDat 2.2 双向串行接口传输位置、报警与温度信息。

编码器分辨率 $R$ 与可分辨最小角度 $\theta_{\min}$ 的关系为：

$$
\theta_{\min} = \frac{360^\circ}{2^R}
$$

对于 19-bit 单圈编码器：

$$
\theta_{\min} = \frac{360^\circ}{2^{19}} \approx 0.000687^\circ \approx 2.47''
$$

多圈编码器的总位置字长为：

$$
R_{\text{total}} = R_{\text{single}} + R_{\text{multi}} = 19 + 12 = 31\ \text{bit}
$$

对应可记录的圈数 $2^{12} = 4096$ 圈。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 编码器类型 | 绝对式旋转编码器，无内置轴承 |
| 扫描原理 | 感应式扫描 |
| 接口 | 串行 EnDat 2.2（纯串行） |
| 单圈分辨率 | 19 bit |
| 多圈圈数 | 12 bit（4096 圈） |
| 系统精度 | ±120″ |
| 最高机械转速 | 12000 rpm |
| 功能安全 | SIL 3 / PL e（符合 IEC 61508 / ISO 13849） |
| 轴径 | 6 mm（可选锥轴） |
| 外径 | 37 mm |
| 防护等级 | IP40（IP64 可选） |
| 工作温度 | 0 °C ~ 60 °C（扩展温度范围可选） |
| 供电电压 | DC 3.6 V ~ 14 V |
| 连接方式 | 8 芯电缆或 M12 连接器 |
| 典型应用 | 伺服电机、机器人关节、CNC 主轴 |

## 应用场景

- 高性能伺服电机的绝对位置反馈；
- 机器人关节电机与减速器后端的位置与速度闭环；
- 功能安全场合的 SIL 3 级角度反馈（如协作机器人、AGV 驱动轮）；
- 数控机床主轴与进给轴的位置测量。

## 供应链关系

`ent_component_heidenhain_eqi_1131` 由制造商 `ent_company_heidenhain` 生产，属于传感器/编码器类别节点。该编码器向上依赖半导体芯片、感应线圈、磁导编码盘、连接器与电缆等零部件；向下装配于伺服电机、机器人关节与数控系统中，常与 `ent_component_delta_ecma` 等伺服电机及 `ent_product_humanoid_robot_joint` 等关节模组配套使用。

## 来源与验证

- HEIDENHAIN 官方产品信息 PDF（EQI 1131 PI 0601-2）明确列出单圈 19 bit、多圈 12 bit、EnDat 2.2、SIL 3/PL e、转速 12000 rpm、系统精度 ±120″ 等参数。
- HEIDENHAIN 官网 EQI 1131 产品页确认外径 37 mm、轴径 6 mm 等机械尺寸。
- B&R EnDat 2.2 安全编码器资料佐证了 EnDat 2.2 在 SIL 3 伺服系统中的应用。
- 未公开项（如扩展温度范围、特定电缆长度）未作臆测。