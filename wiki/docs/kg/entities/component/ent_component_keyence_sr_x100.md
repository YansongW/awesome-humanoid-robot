---
id: ent_component_keyence_sr_x100
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 基恩士 SR-X100 工业读码器
  en: Keyence SR-X100 Industrial Code Reader
status: active
sources:
- id: src_keyence_sr_x100_eu
  type: website
  url: https://www.keyence.eu/products/barcode/barcode-readers/sr-x/models/sr-x100/
- id: src_keyence_sr_x100_datasheet
  type: website
  url: https://www.eurosensor.com/img/pdf/keyence-sr-x100-pdf-736.pdf
- id: src_keyence_sr_x100_automationpioneer
  type: website
  url: https://www.automationpioneer.com/product/keyence-sr-x100-autofocus-code-reader-srx100/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 基恩士 SR-X100 工业读码器

## 概述

Keyence SR-X100 是基恩士（Keyence）推出的紧凑型自动对焦一维/二维条码读取器，属于 SR-X 系列标准型产品。该读码器采用 $1360 \times 1024$ 像素的 CMOS 图像传感器（约 140 万像素），内置高强度红色 LED 照明与绿色激光指示器，支持 QR、DataMatrix、PDF417、Code 128 等主流条码与二维码类型。SR-X100 通过自动对焦可在 $70\,\text{mm}$ 至 $1000\,\text{mm}$ 的读取距离范围内稳定解码，最小分辨率达到二维 $0.024\,\text{mm}$、一维 $0.082\,\text{mm}$，适用于制造追溯、包装检测与物流分拣等场景。

## 工作原理 / 技术架构

SR-X100 的工作流程包括光学成像、自动对焦、照明控制与解码四个环节。CMOS 传感器以全局快门方式捕获条码图像，红色 LED 提供均匀漫反射照明，绿色激光用于对准指示。自动对焦机构根据安装高度与条码尺寸调整镜头焦距，使不同工作距离下的条码均处于景深范围内。图像经内部图像处理引擎进行二值化、畸变校正、对比度增强后，由解码算法识别条码符号。

在光学系统中，视野（Field of View, FOV）与读取距离 $d$、镜头焦距 $f$ 及传感器尺寸相关。SR-X100 在 $300\,\text{mm}$ 距离处的标称视野为 $74 \times 55\,\text{mm}$。其最小可分辨条码尺寸 $w_{\min}$ 受像素尺寸与奈奎斯特采样定理限制：

$$
w_{\min} \approx \frac{\text{FOV}_{\text{width}}}{N_{\text{width}}} \cdot n_{\text{pix-per-module}},
$$

其中 $N_{\text{width}}$ 为传感器水平像素数，$n_{\text{pix-per-module}}$ 为每个条码模块所需的最小像素数。SR-X100 二维最小分辨率 $0.024\,\text{mm}$ 意味着每个模块可由数个像素表示，确保解码可靠性。

## 关键参数表

| 参数 | 规格 |
|---|---|
| 型号 | SR-X100 |
| 传感器类型 | CMOS 图像传感器 |
| 像素数 | $1360 \times 1024$（约 140 万像素） |
| 对焦方式 | 自动对焦 |
| 照明光源 | 高强度红色 LED |
| 指示光源 | 高强度绿色 LED |
| 支持码制 | QR、MicroQR、DataMatrix、PDF417、Code 39/128/93、GS1 系列等 |
| 最小分辨率（2D） | $0.024\,\text{mm}$ |
| 最小分辨率（1D） | $0.082\,\text{mm}$ |
| 读取距离 | $70\,\text{mm}$ – $1000\,\text{mm}$ |
| 视野 | $74 \times 55\,\text{mm}$（距离 $300\,\text{mm}$ 处） |
| 控制输入 | 2 路双向电压输入 |
| 控制输出 | 3 路 Photo MOS 继电器输出 |
| 串行通信 | RS-232C，速率 $600$ – $115200\,\text{bps}$ |
| 以太网 | IEEE 802.3 100BASE-TX，支持 PROFINET、EtherNet/IP、OPC UA 等 |
| USB | USB 2.0 High Speed |
| 供电 | $24\,\text{VDC}$（$+25\%/-20\%$），约 $650\,\text{mA}$ |
| 防护等级 | IP65/IP67（需安装 USB 端口盖） |
| 工作温度 | $0^\circ\text{C}$ – $+45^\circ\text{C}$ |
| 重量 | 约 $180\,\text{g}$ |

## 应用场景

SR-X100 在机器人与自动化系统中的典型应用包括：

- **制造过程追溯**：在装配线工位读取零部件或托盘上的二维码，实现 MES 级生产数据绑定。
- **包装标签验证**：在食品、医药、3C 包装线上验证条码可读性与内容正确性。
- **物流分拣**：在传送带或机器人拣选工位识别包裹条码，辅助 AGV/机械臂完成分拣。
- **DPM 码读取**：读取激光蚀刻或点阵打标在金属、塑料表面的直接部件标识码。

## 供应链关系

基恩士作为工业传感器与机器视觉设备的原始制造商，位于自动化零部件供应链上游。SR-X100 通过基恩士直销网络或授权经销商销往全球，下游客户包括汽车、电子、食品、医药行业的设备制造商与系统集成商。在机器人系统中，SR-X100 通常作为末端或固定式视觉模块，与 PLC、机器人控制器及上位 MES 系统对接，是“感知—决策—执行”闭环中的感知节点。

## 来源与验证

- Keyence 欧洲官网 SR-X100 规格页完整列出传感器像素、自动对焦、码制支持、最小分辨率、读取距离、I/O、通信接口、电源与环境参数。
- Eurosensor 提供的 SR-X100 datasheet（PDF）与官网规格一致，并补充了系统 ROM 重写次数（100000 次）及 USB 盖与防护等级说明。
- Automation Pioneer 产品页提供了通信速度、协议与电气额定值的详细对照表。