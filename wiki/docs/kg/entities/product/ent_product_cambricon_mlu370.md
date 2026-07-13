---
id: ent_product_cambricon_mlu370
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 寒武纪 思元 370
  en: Cambricon MLU370
aliases:
- 思元 370
- MLU370
status: active
sources:
- id: src_cambricon_mlu370_official
  type: website
  url: https://www.cambricon.com/index.php?m=content&c=index&a=lists&catid=360
- title: 思元370系列 - 寒武纪
- id: src_baike_mlu370_x8
  type: website
  url: https://baike.baidu.com/item/%E5%AF%92%E6%AD%A6%E7%BA%AA%20MLU370-X8/60369997
- title: 寒武纪 MLU370-X8 - 百度百科
- id: src_tencent_mlu370_x8
  type: website
  url: https://cloud.tencent.com/developer/article/1960822
- title: 双芯片四芯粒互联，寒武纪发布AI训练卡MLU370-X8
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 寒武纪 思元 370 / Cambricon MLU370

## 概述

思元 370（MLU370）是寒武纪科技（Cambricon）于 2021 年推出的第三代云端 AI 芯片，也是寒武纪首款采用 Chiplet（芯粒）技术的 AI 处理器。该芯片基于 7 nm 工艺，集成约 390 亿晶体管，峰值算力达 256 TOPS（INT8），并首次在国产云端 AI 芯片中支持 LPDDR5 高带宽内存。思元 370 面向训练与推理一体化场景，支持 MLU-Link 多芯互联技术，广泛应用于计算机视觉、自然语言处理、语音及大模型等领域。

## 工作原理 / 技术架构

### MLUarch03 架构
思元 370 基于寒武纪自研 MLUarch03 智能处理器架构，采用多芯粒集成：

- **计算单元**：大规模并行计算核心，支持张量、向量、标量运算；
- **精度支持**：INT8、INT16、FP16、BF16、FP32；
- **内存子系统**：支持 LPDDR5，内存带宽为上一代思元 270 的 3 倍，访存能效约为 GDDR6 的 1.5 倍。

峰值 INT8 算力可表示为：

$$
P_{\text{INT8}} = 256\ \text{TOPS}
$$

### Chiplet 与多芯互联
思元 370 采用 Chiplet 技术，单芯片内集成多个芯粒，通过片上互连实现高带宽数据交换。MLU-Link 技术支持：

- 卡内互联：同一加速卡内多颗芯片全互联；
- 卡间互联：通过 MLU-Link 桥接卡实现多卡高速互联。

以 MLU370-X8 为例，该卡集成双芯片四芯粒思元 370，每张卡可获得 200 GB/s 通讯吞吐性能，约为 PCIe 4.0 带宽的 3.1 倍。

### 软件栈
- **Cambricon NeuWare**：寒武纪基础软件平台；
- **MagicMind**：推理加速引擎，实现训推一体；
- **CNCL**：多卡通信库；
- **框架支持**：PyTorch、TensorFlow、PaddlePaddle 等；
- **典型模型**：ResNet、YOLOv3、Transformer、BERT 等。

## 关键参数表

### 思元 370 芯片

| 参数 | 数值 |
|------|------|
| 工艺制程 | 7 nm |
| 晶体管数量 | 约 390 亿 |
| 峰值 INT8 算力 | 256 TOPS |
| 内存类型 | LPDDR5 |
| 内存带宽 | 上一代 3 倍（相对思元 270） |
| 架构 | MLUarch03 |
| 支持精度 | INT8/16、FP16、BF16、FP32 |
| 多芯互联 | MLU-Link |

### MLU370-X8 训练加速卡

| 参数 | 数值 |
|------|------|
| 芯片配置 | 双芯片四芯粒思元 370 |
| 内存 | 48 GB LPDDR5 |
| FP32 训练算力 | 24 TFLOPS |
| INT8 推理算力 | 256 TOPS |
| 功耗 | 250 W（最大训练功耗） |
| 接口 | PCIe 4.0 ×16 |
| 卡型 | 全高全长双宽（FHFL-Dual-Slot） |
| MLU-Link 带宽 | 200 GB/s |
| 典型训练任务 | YOLOv3、Transformer、BERT、ResNet-101 |

## 应用场景

- **大模型训练与推理**：LLM、多模态模型、推荐系统；
- **计算机视觉**：图像分类、目标检测、语义分割；
- **自然语言处理**：机器翻译、文本生成、语义理解；
- **语音处理**：语音识别、语音合成；
- **机器人云端大脑**：为具身智能系统提供远端训练与推理算力。

## 供应链关系

思元 370 位于“AI 芯片设计—晶圆制造—服务器/智算中心”链条的芯片层：

- **芯片设计**：寒武纪科技（Cambricon）；
- **晶圆代工**：7 nm 工艺由台积电等外部代工厂制造；
- **封装**：采用 Chiplet 先进封装技术；
- **服务器厂商**：与浪潮、联想、新华三等国产服务器厂商合作；
- **下游客户**：互联网公司、科研院所、智算中心、自动驾驶与机器人企业。

## 来源与验证

- 寒武纪官网思元 370 系列页面（https://www.cambricon.com/index.php?m=content&c=index&a=lists&catid=360）
- 百度百科 MLU370-X8 词条
- 腾讯云/机器之心报道（2022-03-22）

> 注：思元 370 单芯片的具体核心数、LPDDR5 容量、TDP 等细节官方未完整披露；表中 MLU370-X8 参数来自官方公开资料。