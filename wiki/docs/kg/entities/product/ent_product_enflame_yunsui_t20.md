---
id: ent_product_enflame_yunsui_t20
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 燧原科技 云燧 T20 训练加速卡
  en: Enflame CloudBlazer Yunsui T20 Training Accelerator
status: active
sources:
- id: src_enflame_t20_official
  type: website
  url: http://www.enflame-tech.com/cloudblazer-t2x/t20
- id: src_enflame_t20_event
  type: website
  url: https://www.enflame-tech.com/events/productlaunch-t20
- id: src_eefocus_t20_t21
  type: website
  url: https://www.eefocus.com/article/498969.html
- id: src_zhiding_t20
  type: website
  url: https://m.zhiding.cn/article/3135203.htm
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---



# 燧原科技 云燧 T20 训练加速卡 / Enflame CloudBlazer Yunsui T20 Training Accelerator

## 概述

云燧 T20 是燧原科技（Enflame）推出的第二代人工智能训练加速卡，基于自研邃思® 2.0（DTU 2.0）芯片，面向数据中心与智算中心的大规模深度学习训练任务。该产品采用全高全长 PCIe 卡形态，支持多精度计算、HBM2E 高带宽显存与燧原自研 GCU-LARE® 互联技术，可单机多卡或多机千卡扩展，适用于计算机视觉、自然语言处理、推荐系统等 AI 模型训练场景。

## 工作原理 / 技术架构

云燧 T20 基于邃思 2.0 的 GCU-CARA 全域计算架构，集成计算引擎、数据引擎与互联引擎。计算引擎支持 FP32、TF32、FP16/BF16 与 INT8 等多种精度；显存子系统采用 HBM2E 堆叠存储，通过 2.5D 封装与逻辑芯片互联；多卡之间通过 GCU-LARE 高速通道进行点对点通信，支持机内 4 卡/8 卡全互联及跨机柜扩展。

单精度张量 TF32 峰值算力可按下式理解：

$$
\text{TF32}_{\text{peak}} = N_{\text{MAC}} \cdot f_{\text{clk}} \cdot 2
$$

其中 $N_{\text{MAC}}$ 为乘法累加单元数量，$f_{\text{clk}}$ 为芯片主频。邃思 2.0 芯片单精度 FP32 峰值算力 40 TFLOPS、TF32 峰值算力 160 TFLOPS；在 T20 PCIe 卡形态下，与非网报道其功耗与频率有所调整，对应 FP32 33.6 TFLOPS、TF32 134.4 TFLOPS。

单卡 HBM2E 带宽：

$$
B_{\text{HBM2E}} = 1.8\ \text{TB/s}
$$

GCU-LARE 单端口双向互联带宽：

$$
B_{\text{LARE}} = 300\ \text{GB/s}
$$

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 产品形态 | 全高全长 PCIe 训练加速卡 |
| 核心芯片 | 邃思® 2.0（DTU 2.0） |
| 架构 | GCU-CARA 全域计算架构 |
| 制程工艺 | 格芯 12 nm FinFET |
| 封装尺寸 | 57.5 mm × 57.5 mm（芯片） |
| FP32 峰值算力 | 33.6 TFLOPS（T20，eefocus）；部分报道 40 TFLOPS（芯片峰值） |
| TF32 峰值算力 | 134.4 TFLOPS（T20，eefocus）；部分报道 160 TFLOPS（芯片峰值） |
| FP16/BF16 峰值算力 | 134.4 TFLOPS（T20，eefocus） |
| INT8 峰值算力 | 268.8 TOPS（T20，eefocus） |
| 显存类型 | HBM2E |
| 显存容量 | 最高 64 GB |
| 显存带宽 | 1.8 TB/s |
| 互联技术 | GCU-LARE®，单端口双向 300 GB/s |
| 互联端口数 | 6 个（邃思 2.0 芯片级） |
| 板卡功耗 | 300 W（T20，eefocus） |
| 软件平台 | 驭算 TopsRider（支持 PyTorch、TensorFlow、PaddlePaddle 等） |
| 典型应用 | CV、NLP、推荐系统、强化学习模型训练 |

## 应用场景

- 大规模图像分类、目标检测与语义分割模型训练；
- 大语言模型（LLM）预训练与微调；
- 推荐系统、广告排序与搜索排序模型训练；
- 强化学习与科学计算；
- 智算中心、互联网、金融、智慧城市等行业的 AI 训练集群。

## 供应链关系

`ent_product_enflame_yunsui_t20` 由 `ent_company_enflame`（燧原科技）设计，属于云端 AI 训练加速卡产品节点。其上游依赖格芯 12 nm 晶圆代工、HBM2E 显存（三星/海力士）、2.5D 封装（日月光）、PCB 与散热模组等；通过 `ent_component_lidar`、服务器整机厂商与智算中心集成商向下交付，构成“芯片—加速卡—集群—云/数据中心”产业链。燧原同时提供驭算软件栈，实现硬件与深度学习框架的协同优化。

## 来源与验证

- 燧原科技官网云燧 T20 产品页确认其为基于邃思 2.0 的第二代训练加速卡，具备多精度算力、HBM2E 显存、GCU-LARE 互联与驭算软件平台。
- 燧原科技“芯云长天”发布会页面说明 T20/T21 于 2021 年 7 月 7 日发布，并介绍了 GCU-CARA 架构与 GCU-LARE 互联。
- 与非网文章对 T20 与 T21 做了规格区分：T20 为 PCIe 卡、功耗 300 W，FP32 33.6 TFLOPS、TF32 134.4 TFLOPS、HBM2E 64 GB、互联 300 GB/s。
- 至顶网报道侧重邃思 2.0 芯片峰值 FP32 40 TFLOPS / TF32 160 TFLOPS、HBM2E 64 GB / 1.8 TB/s。
- 本条目对 T20 卡级与芯片级峰值算力的差异进行了标注，未对未公开的 TDP 细节、制程节点等作臆测。