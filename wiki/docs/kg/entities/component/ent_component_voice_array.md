---
id: ent_component_voice_array
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 麦克风阵列
  en: Microphone Array (Voice Array)
status: active
sources:
- id: src_ent_component_voice_array_pal
  type: website
  url: https://docs.pal-robotics.com/25.01/hardware/microphone.html
- id: src_ent_component_voice_array_seeed
  type: website
  url: https://wiki.seeedstudio.com/cn/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/
- id: src_ent_component_voice_array_xmos
  type: document
  url: https://www.xmos.com/download/XVF3510-Product-Brief(1.0).pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 麦克风阵列 / Microphone Array (Voice Array)

## 概述

麦克风阵列（Microphone Array，亦称 Voice Array）是由多个按特定几何分布的麦克风组成的声学传感前端，配合波束成形（Beamforming）、声源到达方向估计（DOA）、回声消除（AEC）、噪声抑制（NS）和语音活动检测（VAD）等算法，实现远场拾音、声源定位、语音增强与说话人分离。在机器人与人形智能体中，麦克风阵列是语音交互、环境感知与人机协作的关键输入组件。

## 工作原理与技术架构

阵列利用不同麦克风接收同一声源信号的时间差（TDOA）进行空间滤波。对于间距为 $d$ 的两个麦克风，平面波入射角为 $\theta$ 时，到达时间差为：

$$
\tau = \frac{d \sin\theta}{c}
$$

其中 $c$ 为声速（空气中约 343 m/s）。通过 GCC-PHAT 等互相关算法估计 $\tau$ 后，可解算声源方位角 $\theta$。

波束成形通过为各通道分配复数权重 $w_i$ 形成方向性响应：

$$
Y(f) = \sum_{i=1}^{N} w_i(f) X_i(f)
$$

其中 $N$ 为麦克风数量，$X_i(f)$ 为第 $i$ 路频域信号。阵列增益与麦克风数量相关，理想情况下波束成形可提升信噪比约 $10\log_{10}N$ dB。

典型硬件由 MEMS 麦克风、多通道 ADC（或 PDM 接口）、DSP/FPGA/专用语音处理芯片（如 XMOS XVF3510）及 USB/I2S 接口组成。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 麦克风数量 | 2–8 通道（典型 4 通道环形） | 依应用 |
| 麦克风间距 | 40.5–71 mm（典型） | 线性/环形/矩形阵列 |
| 灵敏度 | -26 dBFS（全向，典型） | ReSpeaker Mic Array v2.0 |
| 信噪比 | 61 dB（典型） | ReSpeaker Mic Array v2.0 |
| 声学过载点 | 120 dBSPL | ReSpeaker Mic Array v2.0 |
| 频率响应 | 20 Hz – 20 kHz | 音频级 |
| 采样率 | 16 kHz / 48 kHz | 16 kHz 用于 ASR |
| 动态范围 | 95 dB（PAL Robotics 规格） | — |
| 拾音距离 | 最远 5 m | 远场语音 |
| 供电 | 5 V DC（USB 或扩展排针） | — |
| 功耗 | 170–180 mA @ 5 V | ReSpeaker |
| 尺寸 | 70 mm × 70 mm × 13.3 mm | ReSpeaker Mic Array v2.0 |
| 重量 | 70 g | ReSpeaker Mic Array v2.0 |
| 算法支持 | DOA、Beamforming、AEC、NS、AGC、VAD | — |
| 接口 | USB Audio / I2S / PDM | 依平台 |
| 价格 | 未公开 | 依型号 |

## 应用场景

- **服务与人形机器人**：语音唤醒、远场语音识别、声源定位、多轮对话。
- **智能音箱与家居**：360° 拾音、回声消除、噪声抑制。
- **会议系统**：多人语音分离、定向拾音、实时转写。
- **机器人巡检与安防**：异常声音检测、方向判定。

## 供应链关系

- **核心芯片/模组供应商**：XMOS（XVF3510/XVF3800 语音处理器）、Synaptics AudioSmart、Knowles、Infineon（MEMS 麦克风）、Seeed Studio（ReSpeaker 模组）。
- **上游关键物料**：MEMS 麦克风芯片、ADC/DAC、DSP/FPGA、PCB、结构件。
- **下游集成**：机器人整机厂、智能音箱厂商、会议设备商、车载语音方案商。
- **知识图谱关系**：
  - 麦克风阵列模组厂商 — `manufactures` → `ent_component_voice_array`
  - `ent_component_voice_array` — `used_in` → 人形机器人/服务机器人产品节点

## 来源与验证

- PAL Robotics 官方文档给出了其机器人搭载的 ReSpeaker Mic Array v2.0 的灵敏度（-26 dBFS）、SNR（61 dB）、AOP（120 dBSPL）、频率响应、动态范围（95 dB）、功耗、尺寸及重量。
- Seeed Studio ReSpeaker 4-Mic Array Wiki 说明了 4 通道环形阵列、3 m 半径拾音、VAD/DOA/KWS 算法支持及 5 V 供电。
- XMOS XVF3510 产品简报披露了双 PDM 麦克风接口、71 mm 间距、48 kHz USB/I2S、AEC/Beamforming/NS 等语音处理能力。