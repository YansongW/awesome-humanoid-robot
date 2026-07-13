---
id: ent_component_renishaw_resolute_readhead
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 雷尼绍 RESOLUTE 绝对式光栅读数头
  en: Renishaw RESOLUTE Absolute Optical Readhead
sources:
- id: src_renishaw_resolute_readhead_datasheet
  type: datasheet
- title: Renishaw RESOLUTE absolute optical encoder datasheet
  url: https://www.renishaw.com/en/resolute-absolute-encoder--9533
- id: src_renishaw_resolute_biss_pdf
  type: datasheet
- title: RESOLUTE absolute optical encoder with BiSS serial communications
  url: https://www.aska.com.pl/index.php/pobierz/download/pobierz/128/resolute_biss_l-9517-9448-02-aen.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from Renishaw public datasheets and distributor listings;
    missing values marked as 未公开.
---


# 雷尼绍 RESOLUTE 绝对式光栅读数头 / Renishaw RESOLUTE Absolute Optical Readhead

## 概述

雷尼绍 RESOLUTE 读数头是 RESOLUTE 真正绝对式光栅编码器系统的核心传感单元，负责读取直线栅尺或圆光栅上的绝对位置信息。该读数头采用单轨道绝对光学刻度，配合高速数字信号处理（DSP）成像与位置校验算法，可在开机瞬间输出绝对位置，无需电池备份或参考点回零。产品广泛应用于高精度数控机床、直线电机、半导体设备、机器人关节及三坐标测量机等领域。

## 工作原理与技术架构

RESOLUTE 读数头内部集成微型光学成像系统，其工作机理可概括为：

1. **单轨道绝对光学刻度照明**：读数头内置 LED 光源照射栅尺，栅尺采用 30 μm 名义节距的单轨道绝对编码图案。
2. **高速成像**：读数头相当于一部超高速微型数字相机，以高帧率拍摄栅尺图案，获取包含绝对位置信息的二维图像。
3. **DSP 位置解算**：专用数字信号处理器对图像进行实时解码，直接输出绝对位置字，分辨率可选 1 nm（线性）或 32 bit（旋转）。
4. **独立位置校验算法**：内置独立的位置校验算法持续监控每次读数，检测并抑制因污染、划痕或光学异常导致的错误位置输出，提升系统安全性。
5. **串行通信输出**：支持 BiSS C、DRIVE-CLiQ、FANUC、Mitsubishi、Panasonic、Yaskawa 等多种工业串行协议。

关键性能指标的理论关系如下：

- **分辨率与速度**：线性分辨率 $1~\text{nm}$ 时，最大读取速度仍可达 $100~\text{m/s}$；旋转分辨率 32 bit 时，最高转速可达 $36{,}000~\text{rev/min}$。
- **细分误差（SDE）**：$\pm 40~\text{nm}$，保证速度环控制平滑性。
- **抖动（Jitter）**：$<10~\text{nm RMS}$，确保位置稳定性。
- **最大刻度长度**：与位置字长相关，例如 36 bit 位置字配合 5 nm 分辨率可支持 10 m 刻度长度。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 真正绝对式光学读数头 | Renishaw datasheet |
| 栅尺节距 | 30 μm | Renishaw datasheet |
| 线性分辨率 | 最高 1 nm | 可选分辨率 |
| 旋转分辨率 | 最高 32 bit | 可选分辨率 |
| 最大读取速度 | 100 m/s | Renishaw datasheet |
| 最大转速 | 36 000 rev/min | 旋转应用 |
| 细分误差（SDE） | ±40 nm | Renishaw datasheet |
| 抖动 | <10 nm RMS | Renishaw datasheet |
| 串行接口 | BiSS C、DRIVE-CLiQ、FANUC、Mitsubishi、Panasonic、Yaskawa | 可选 |
| 防护等级 | IP64 | Renishaw datasheet |
| 工作温度 | 0 °C ~ +80 °C（标准型）| Renishaw datasheet |
| 扩展工作温度 | −40 °C ~ +80 °C（ETR 型）| 第三方集成资料 |
| 功能安全 | 可选 SIL2 / PL d | Renishaw datasheet |
| 兼容性 | RELA / RSLA / RTLA / RESA / REXA 栅尺 | Renishaw datasheet |
| 诊断工具 | 兼容 ADTa-100 | Renishaw datasheet |
| 价格 | 未公开 | - |

## 应用场景

- **高精度数控机床**：用于直线轴和旋转轴的全闭环位置反馈，实现亚微米级加工精度。
- **直线电机与磁悬浮平台**：高速度、高分辨率的位置反馈，支撑高速高精运动控制。
- **半导体设备**：光刻、晶圆检测等设备中的精密定位。
- **机器人关节**：为协作机器人和人形机器人提供绝对式关节角度反馈。
- **三坐标测量机与天文望远镜**：长行程、高精度的角度和直线测量。

## 供应链关系

- **上游**：LED 光源、CMOS 成像传感器、DSP/ASIC、光学透镜、电缆与连接器、精密机械壳体。
- **制造商**：雷尼绍（Renishaw）同时制造 RESOLUTE 读数头及配套栅尺，并通过关系 `ent_company_renishaw -- manufactures --> ent_component_renishaw_resolute_readhead` 记录于知识图谱。
- **下游**：机床 OEM、半导体设备商、机器人整机厂、测量仪器厂商。读数头通常与 `ent_product_renishaw_resolute_encoder` 系统中的栅尺配套使用，共同构成完整编码器系统。

## 来源与验证

主要参数来源于雷尼绍官方产品页及公开 datasheet，关键分销商页面（e-motionsupply、aska.com.pl）对 30 μm 节距、1 nm 分辨率、100 m/s 速度、±40 nm SDE、<10 nm RMS 抖动等数据进行了交叉验证。价格、具体型号命名规则及扩展温度范围由集成商资料补充，未公开项已标注。