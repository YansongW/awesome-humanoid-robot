---
id: ent_product_estun_servo
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 埃斯顿交流伺服系统（PRONET / EM3A 系列）
  en: Estun AC Servo System (PRONET / EM3A Series)
status: active
sources:
- id: src_estun_official
  type: website
  url: https://www.estun.com/
- id: src_estun_em3a
  type: website
  url: https://www.estun.com/xgltysfdj/371.html
- id: src_gongkong_pronet
  type: website
  url: http://www.gongkong.com/product/201412/77788.html
- id: src_pronet_pdf
  type: white_paper
  url: https://document.technique-achat.com/ESTUN/Documentation_technique_Pronet-.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 埃斯顿交流伺服系统（PRONET / EM3A 系列）

## 概述

埃斯顿交流伺服系统是南京埃斯顿自动化股份有限公司（深交所：002747）的核心运动控制产品，涵盖 PRONET 系列伺服驱动器与 EM3A/EMJ/EMG/EML 系列伺服电机。该系统功率覆盖 50 W 至 75 kW，支持位置、速度、转矩及总线控制模式，广泛应用于工业机器人、数控机床、锂电设备、半导体设备及人形机器人关节驱动。

## 工作原理 / 技术架构

埃斯顿伺服系统采用永磁同步电机（PMSM）矢量控制，通过电流环、速度环与位置环三级闭环实现高精度运动控制。驱动器对电机定子电流进行解耦，分别控制励磁分量 $i_d$ 与转矩分量 $i_q$，输出电磁转矩：

$$
T_e = \frac{3}{2} p \left[ \psi_f i_q + (L_d - L_q) i_d i_q \right]
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$L_d$、$L_q$ 为直轴与交轴电感。对于表贴式永磁电机，通常 $L_d \approx L_q$，转矩可近似为：

$$
T_e \approx \frac{3}{2} p \psi_f i_q = K_t \cdot i_q
$$

$K_t$ 为转矩常数。系统支持电流前馈、加速度前馈、在线惯量识别与自动增益调整，可有效抑制低频振动并提升动态响应。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 南京埃斯顿自动化股份有限公司 |
| 产品形态 | 伺服驱动器 + 伺服电机 |
| 功率范围 | 50 W – 75 kW（系列范围） |
| 电压等级 | 单相/三相 100 V、200 V、400 V |
| 控制模式 | 位置 / 速度 / 转矩 / 总线 |
| 通信协议 | EtherCAT、Modbus、CANopen、POWERLINK、PROFIBUS |
| 编码器 | 17 位串行绝对值编码器、20/23 位绝对值/增量编码器、2500 P/R 编码器、旋转变压器 |
| 响应频率 | 1.6 kHz（ProNet 系列公开指标） |
| 电机转速 | 额定 2000–3000 r/min，最高 5000–7000 r/min（视型号） |
| 防护等级 | IP65（电机典型） |
| 认证 | CE、UL |
| 价格 | 未公开 |

## 应用场景

- **工业机器人**：六轴机器人、SCARA、协作机器人关节驱动。
- **数控机床**：进给轴、主轴高精度定位与轮廓控制。
- **人形机器人零部件**：谐波减速器配套的无框力矩电机、关节模组驱动。
- **新能源与 3C**：锂电卷绕、叠片、固晶机、包装机械。

## 供应链关系

在公司—产品—零部件网络中，埃斯顿伺服系统处于**运动控制产品层**：

- **上游**：稀土永磁材料（钕铁硼）、功率芯片、编码器、轴承、铸件、电子元器件。
- **自身位置**：`ent_company_estun -- manufactures --> ent_product_estun_servo`；`ent_product_estun_servo -- uses --> ent_component_magnetic_steel`。
- **下游**：工业机器人本体、数控机床、人形机器人整机厂、自动化产线集成商。

## 来源与验证

- 埃斯顿自动化官网：https://www.estun.com/
- 埃斯顿 EM3A 系列产品页：https://www.estun.com/xgltysfdj/371.html
- 中国工控网 ProNet 介绍：http://www.gongkong.com/product/201412/77788.html
- ESTUN ProNet 技术文档 PDF：https://document.technique-achat.com/ESTUN/Documentation_technique_Pronet-.pdf

功率范围、电压等级、通信协议、编码器类型与响应频率均来自官方及授权渠道公开资料；具体型号价格需通过埃斯顿销售确认。