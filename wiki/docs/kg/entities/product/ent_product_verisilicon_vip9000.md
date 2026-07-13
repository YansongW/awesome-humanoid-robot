---
id: ent_product_verisilicon_vip9000
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 芯原 VIP9000
  en: VeriSilicon VIP9000
aliases:
- VIP9000
status: active
sources:
- id: src_verisilicon_vip9000_asilb
  type: website
  url: https://www.verisilicon.com/en/PressRelease/VIP9000NanoOi-FS
- title: VeriSilicon’s NPU IP VIP9000NanoOi-FS has achieved ISO 26262 ASIL B certification
- id: src_verisilicon_100m
  type: website
  url: https://www.edge-ai-vision.com/2024/02/verisilicon-npu-ip-is-shipped-in-over-100-million-ai-enabled-chips-worldwide/
- title: VeriSilicon NPU IP is Shipped In Over 100 Million AI-enabled Chips Worldwide
- id: src_autochips_ac8025
  type: website
  url: https://anysilicon.com/autochips-integrated-multiple-verisilicons-ips-in-its-intelligent-cockpit-domain-control-soc/
- title: AutoChips integrated multiple VeriSilicon's IPs in its intelligent cockpit
    domain control SoC
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 芯原 VIP9000 / VeriSilicon VIP9000

## 概述

VIP9000 是芯原股份（VeriSilicon，688521.SH）推出的可配置神经网络处理器（NPU）IP 系列，面向嵌入式 AI、智能手机、平板、智能电视、汽车电子、安防监控、机器人及边缘服务器等应用。该系列采用可编程、可扩展、低功耗架构，支持 Transformer、CNN、LLM 等多种网络，并可通过 FLEXA 技术与芯原 ISP、视频编解码 IP 形成低延迟 AI-ISP/AI-Video 子系统。截至 2024 年底，芯原 NPU IP 已集成于超过 1.4 亿颗 AI 芯片，服务 90 余家客户。

## 工作原理 / 技术架构

### 可编程 NPU 架构
VIP9000 采用“通用可编程 NPU 架构”，核心由向量引擎（Vector Engine）与张量引擎（Tensor Engine）组成，可灵活处理各类神经网络层：

- **算子支持**：卷积、全连接、注意力、归一化、激活等；
- **精度支持**：INT8、INT4、FP16、BF16（具体配置可定制）；
- **量化与压缩**：4-bit 量化与模型压缩技术，降低带宽占用；
- **Tiling 技术**：将大特征图分块调度，减少外部 DDR 访问，提高实时性与稳定性。

峰值算力由配置决定。以 AutoChips AC8025 座舱 SoC 集成的 VIP9000 为例，其 INT8 算力为 1.2 TOPS；高端配置可达数十 TOPS。

### 软件栈
VIP9000 配套完整软件生态：

- **Acuity 工具链**：模型转换、量化、图优化；
- **框架支持**：PyTorch、TensorFlow、ONNX；
- **API**：OpenVX 1.3、OpenCL 3.0 / 1.2 Full Profile、OpenVX Neural Network Extension；
- **运行时**：支持 LLM、AIGC、Stable Diffusion、Llama 2 等模型在嵌入式设备部署。

### 功能安全
VIP9000NanoOi-FS 子系列通过 SGS-TÜV Saar ISO 26262 ASIL B 功能安全认证，支持确定性延迟（deterministic latency），适用于 ADAS、舱内监控（DMS/OMS）等汽车安全相关应用。

### 与 ISP/视频子系统协同
通过 FLEXA 接口，VIP9000 可与芯原 ISP、视频编码器直接互联，无需 DDR 中转，形成 AI-ISP/AI-Video 流水线：

$$
\text{ISP} \xrightarrow{\text{FLEXA}} \text{NPU} \xrightarrow{\text{FLEXA}} \text{Video Encoder}
$$

该架构显著降低内存带宽与延迟，适用于机器人视觉前端、智能座舱等场景。

## 关键参数表

| 参数 | 典型值 / 范围 |
|------|--------------|
| 产品类型 | 可配置神经网络处理器 IP |
| 架构 | 向量引擎 + 张量引擎 |
| 支持网络 | CNN、Transformer、LLM、AIGC |
| 支持精度 | INT8、INT4、FP16、BF16（可配置） |
| 典型 INT8 算力 | 1.2 TOPS（AC8025 座舱 SoC 示例）至数十 TOPS |
| 模型量化 | 4-bit 量化与压缩 |
| 软件栈 | Acuity、PyTorch、TensorFlow、ONNX |
| API | OpenVX 1.3、OpenCL 3.0 / 1.2 |
| 功能安全 | VIP9000NanoOi-FS 通过 ISO 26262 ASIL B |
| 配套技术 | FLEXA（与 ISP/视频编码器零 DDR 互联） |
| 累计出货量 | 约 1.4 亿颗 AI 芯片（截至 2024 年底） |

## 应用场景

- **智能机器人**：人形机器人/服务机器人的视觉感知、目标检测、语义分割；
- **汽车电子**：ADAS、驾驶员监控（DMS）、乘员监控（OMS）、智能座舱；
- **消费电子**：智能手机 AI 摄影、平板语音助手、智能电视画质增强；
- **安防监控**：人脸识别、行为分析、视频结构化；
- **边缘服务器**：轻量级 LLM 推理与 AIGC 任务。

## 供应链关系

VIP9000 位于“半导体 IP—SoC 设计—整机”链条的 IP 层：

- **IP 提供商**：芯原股份（VeriSilicon）；
- **被授权方**：全球 90 余家芯片设计公司，集成于 140 余款 AI SoC；
- **典型集成案例**：AutoChips AC8025 座舱 SoC、多家机器人/安防/手机 SoC；
- **下游整机**：机器人、汽车、手机、平板、安防摄像头等终端。

## 来源与验证

- VeriSilicon 官方新闻稿《VIP9000NanoOi-FS achieves ISO 26262 ASIL B certification》（2025-12-02）
- Edge AI Vision 报道《VeriSilicon NPU IP is Shipped In Over 100 Million AI-enabled Chips Worldwide》
- AnySilicon / AutoChips AC8025 集成报道

> 注：VIP9000 为可配置 IP，具体算力、面积、功耗由 licensee 定制，表中给出典型参考值而非固定规格。