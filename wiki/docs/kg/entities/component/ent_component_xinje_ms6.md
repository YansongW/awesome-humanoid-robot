---
id: ent_component_xinje_ms6
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 信捷 MS6 系列伺服电机
  en: Xinje MS6 Series Servo Motor
status: active
sources:
- id: src_ent_component_xinje_ms6_1
  type: website
  url: https://tudonghoatoancau.com/dong-co-servo-xinje-ms6h-130cs20b2-21p5/
- id: src_ent_component_xinje_ms6_2
  type: website
  url: https://www.manualslib.com/manual/3704849/Xinje-Ds5l2-Series.html
- id: src_ent_component_xinje_ms6_3
  type: website
  url: https://download.plcsystems.ru/Xinje/2022_servo_system_catalog.pdf
- id: src_ent_component_xinje_ms6_4
  type: website
  url: https://xsdautomatic.en.made-in-china.com/product/hmiYdjAUXspM/China-Xinje-Small-Control-System-Servo-Motor-Ds5l1-20p7-Pta-Ms6s-80CS30b1-20p7-750W-Ds5l1-Servo-Motor-Drive.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 信捷 MS6 系列伺服电机

## 概述

信捷（Xinje）MS6 系列伺服电机是配合 DS5 系列伺服驱动器使用的永磁同步伺服电机，面向通用自动化、机器人、包装、纺织、木工等场景。该系列在 MS5 基础上优化了磁路、结构与防护等级，标准配置 17 位编码器、可选 23 位编码器，法兰尺寸覆盖 40–265 mm，功率范围约 0.1–3 kW 乃至更高。

## 工作原理 / 技术架构

MS6 伺服电机为三相永磁同步电机（PMSM），由定子三相绕组与永磁转子构成。伺服驱动器通过矢量控制（FOC）对定子电流进行 $d$-$q$ 轴解耦，实现对转矩与磁链的独立控制。电磁转矩可表示为

$$
T = \frac{3}{2} p \left[ \psi_f i_q + (L_d - L_q) i_d i_q \right]
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$i_d$、$i_q$ 为直轴与交轴电流，$L_d$、$L_q$ 为对应电感。对于表贴式永磁电机，$L_d \approx L_q$，转矩主要由 $i_q$ 产生。

电机输出机械功率 $P_{out}$、额定转矩 $T_N$ 与额定转速 $n_N$ 满足

$$
P_{out} = \frac{T_N \cdot n_N}{9.549}
$$

式中 $P_{out}$ 单位为 W，$T_N$ 单位为 N·m，$n_N$ 单位为 r/min。

以 MS6S-80CS30B1-20P7 为例，额定功率 750 W、额定转速 3,000 r/min，其额定转矩为

$$
T_N = \frac{750 \times 9.549}{3000} \approx 2.39\ \mathrm{N\cdot m}
$$

与供应商公开参数一致。

## 关键参数表

| 参数项 | 典型值 | 备注/来源 |
|--------|--------|-----------|
| 电机系列 | MS6（永磁同步伺服电机） | Xinje 产品目录 |
| 配套驱动器 | DS5 系列（DS5C / DS5L1 / DS5L2 等） | 产品目录 |
| 功率范围 | 0.1–3 kW（系列覆盖，部分型号更高） | 产品目录 / 供应商 |
| 额定转速 | 2,000–3,000 r/min（常见） | 型号依赖 |
| 编码器分辨率 | 17 位标准 / 23 位可选 | 2022 伺服目录 |
| 防护等级 | IP66（MS6-40/60/80 机座）；IP67（MS6-B3/B4/MS6G） | DS5L2 用户手册 |
| MS6S-80CS30B1-20P7 | 750 W / 3000 rpm / 2.39 N·m | Made-in-China 产品页 |
| MS6H-130CS20B2-21P5 | 1.5 kW / 2000 rpm / 17 位编码器 / IP66 | Tự Động Hóa Toàn Cầu |
| 轴向/径向允许负载 | 因法兰尺寸而异（例如 80 机座径向 ≤392 N） | DS5L2 用户手册 |
| 价格 | 未公开 | 按型号询价 |

## 应用场景

- **工业机器人与协作机器人关节驱动**：作为中小功率关节电机，配合谐波/行星减速器实现精确位置与力矩控制。
- **自动化生产线**：包装、纺织、木工、3C 组装中的定位、追剪、飞剪等应用。
- **AGV/AMR 驱动轮**：低压伺服电机为移动机器人提供精准速度控制。
- **数控机床与电子制造**：主轴进给与工作台定位。

## 供应链关系

MS6 伺服电机由 `ent_company_xinje`（信捷电气）制造，通常与信捷 DS5 系列伺服驱动器配套销售。上游包括硅钢片、永磁体、漆包线、编码器、轴承与机壳；下游面向自动化设备制造商、机器人关节模组厂商与系统集成商。在知识图谱中，该零部件可作为机器人关节模组 `ent_component_*_joint_module` 的电机来源之一，也可直接用于中小型自动化设备。

## 来源与验证

- MS6 系列概述、编码器配置与防护等级参考 Xinje 2022 伺服系统目录与 DS5L2 用户手册。
- MS6S-80CS30B1-20P7 750 W 参数来自 Made-in-China 产品页；MS6H-130CS20B2-21P5 参数来自越南自动化供应商页面。
- 轴向/径向负载数据参考 DS5L2 用户手册中的电机选型章节。