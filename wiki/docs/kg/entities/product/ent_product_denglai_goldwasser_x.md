---
id: ent_product_denglai_goldwasser_x
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 登临科技 Goldwasser X
  en: Denglai Goldwasser X
aliases:
- Goldwasser X
status: active
sources:
- id: src_denglai_goldwasser_official
  type: website
  url: https://www.denglai.com.cn/
- title: 登临科技 Goldwasser 产品页
- id: src_paddlepaddle_goldwasser
  type: website
  url: https://www.paddlepaddle.org.cn/support/news?action=detail&id=2516
- title: 百度飞桨适配登临GPU+ 系列芯片
- id: src_equalocean_denglai
  type: website
  url: https://equalocean.com/news/2023071119880-denglin-technology-completes-series-c-financing-advance-general-purpose-gpu
- title: Denglin Technology Completes Series C Financing to Advance General-purpose
    GPU
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 登临科技 Goldwasser X / Denglai Goldwasser X

## 概述

Goldwasser X 是登临科技（Denglai Technology / Shanghai Denglin Technology）推出的 GPU+ 系列 AI 加速卡产品，基于登临自研的“GPU+”软件定义片内异构计算架构。该系列产品是国内较早实现规模量产的 GPGPU 高性能通用人工智能加速器之一，兼容 CUDA/OpenCL 编程生态，面向云端推理与训练、边缘计算等场景。

## 工作原理 / 技术架构

### GPU+ 架构
登临科技提出的 GPU+ 是一种“软件定义的片内异构计算架构”（software-defined on-chip heterogeneous architecture based on GPGPU），其核心思想是在单芯片内部实现任务调度与算力分配，而非依赖系统级异构：

- **片内异构**：将通用 GPU 的灵活性与 ASIC 的高效率结合；
- **高计算密度**：在更高抽象维度上进行调度，提升计算密度；
- **降低带宽依赖**：通过架构创新减少对外部内存带宽的依赖；
- **能效比提升**：官方称相对传统 GPU 可提供 3 倍以上能效。

### 软件生态
Goldwasser 系列兼容 CUDA/OpenCL 编程接口，支持：

- 主流深度学习框架：PyTorch、TensorFlow、PaddlePaddle、ONNX、Caffe2；
- 自研 Hamming 工具链：提供模型迁移、编译优化、性能调优；
- 同一 SDK：云端与边缘侧采用同一套 SDK，降低跨平台开发成本。

### 精度与算力
Goldwasser 系列支持 INT8、FP16、FP32 等精度。典型配置如下：

| 型号 | 形态 | 功耗 | INT8 算力 |
|------|------|------|-----------|
| Goldwasser UL | 边缘计算卡/MXM | 25–35 W | 32–64 TOPS |
| Goldwasser L | 半高半长 PCIe 卡 | 40–70 W | 128–256 TOPS |
| Goldwasser XL | 全高全长 PCIe 卡 | 未公开 | 512 TOPS |

峰值能效可近似为：

$$
\eta_{\text{Goldwasser-L}} = \frac{128\ \text{TOPS}}{70\ \text{W}} \approx 1.83\ \text{TOPS/W}
$$

百度飞桨实测中，Goldwasser 在 40 W TDP 下输出 128 TOPS 算力。

## 关键参数表

| 参数 | 数值 / 范围 |
|------|-------------|
| 产品系列 | Goldwasser（高凛）系列 |
| 架构 | GPU+ 软件定义片内异构架构 |
| 编程接口 | CUDA/OpenCL 兼容 |
| 支持精度 | INT8、FP16、FP32 |
| 边缘卡 Goldwasser UL | 25–35 W，32–64 TOPS INT8 |
| 服务器卡 Goldwasser L | 40–70 W，128–256 TOPS INT8 |
| 旗舰卡 Goldwasser XL | 512 TOPS INT8（功耗未公开） |
| 工具链 | Hamming SDK |
| 框架支持 | PyTorch、TensorFlow、PaddlePaddle、ONNX、Caffe2 |

## 应用场景

- **视频分析**：智能安防、视频审核、行为识别；
- **智慧城市**：交通监控、城市管理、事件检测；
- **自然语言处理**：搜索推荐、智能客服、内容推荐；
- **自动驾驶/机器人**：感知算法推理、云端训练；
- **边缘 AI**：工厂质检、智慧网点、安全生产。

## 供应链关系

Goldwasser X 位于“AI 芯片设计—服务器/边缘设备—行业应用”链条的芯片层：

- **芯片设计**：登临科技（上海登临科技有限公司）；
- **晶圆代工**：工艺信息未公开；
- **服务器合作**：与浪潮信息 AIStation、研华科技等完成适配互认证；
- **框架合作**：百度飞桨等国产框架完成适配；
- **下游应用**：智慧城市、安防、互联网、汽车、机器人等行业客户。

## 来源与验证

- 登临科技官网 Goldwasser 产品页（https://www.denglai.com.cn/）
- 百度飞桨适配报道（2021-07-22）
- EqualOcean 融资与公司报道（2023-07-11）

> 注：登临科技官方未公开 Goldwasser X 单型号的完整 datasheet。表中“Goldwasser X”按系列公开资料整理，具体型号（UL/L/XL）的显存容量、PCIe 版本、TDP、核心数等细节部分未公开。