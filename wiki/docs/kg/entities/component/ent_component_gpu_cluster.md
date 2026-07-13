---
id: ent_component_gpu_cluster
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: GPU 集群
  en: GPU Cluster
status: active
sources:
- id: src_nvidia_dgx_spark_datasheet
  type: website
  url: https://www.content.shi.com/cms-content/accelerator/media/pdfs/nvidia/nvidia-060425-dgx-spark-datasheet.pdf
- id: src_nvidia_dgx_spark_review
  type: website
  url: https://www.lmsys.org/blog/2025-10-13-nvidia-dgx-spark/
- id: src_dgx_spark_cluster_review
  type: website
  url: https://www.storagereview.com/review/nvidia-dgx-spark-cluster-review-distributed-inference-on-dell-gigabyte-and-hp
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# GPU 集群

## 概述

GPU 集群（GPU Cluster）是由多台配备图形处理器（GPU）或 AI 加速器的计算节点通过高速网络互连形成的分布式计算系统，用于承担机器人领域中大规模神经网络训练、具身智能（Embodied AI）仿真、数字孪生渲染以及多模态大模型推理等高并行度计算任务。以 NVIDIA DGX Spark 为代表的新一代桌面级 GPU 计算节点为例，单节点集成 NVIDIA GB10 Grace Blackwell 超级芯片，可提供高达 $1000\,\text{AI TOPS}$（FP4 稀疏）的峰值算力，并可通过 NVIDIA ConnectX 网络将两个节点互联，以流水线或张量并行的方式运行参数量达 $405\,\text{B}$ 级别的大模型。

## 工作原理 / 技术架构

GPU 集群的核心在于将大量矩阵运算卸载到高度并行的 GPU 计算核心上。对于机器人 AI 训练，常用的随机梯度下降（SGD）或强化学习（PPO）更新可表示为

$$
\theta_{t+1} = \theta_t - \eta \, \nabla_\theta \mathcal{L}(\theta_t; \mathcal{B}),
$$

其中 $\mathcal{B}$ 为来自仿真环境或真实采集的批量样本。GPU 集群将批量数据划分为多个子批量（micro-batches），各节点并行计算梯度后通过 all-reduce 操作聚合：

$$
\bar{g} = \frac{1}{N} \sum_{i=1}^{N} g_i.
$$

在模型推理阶段，集群可采用张量并行（Tensor Parallelism, TP）或流水线并行（Pipeline Parallelism, PP）。TP 将单层网络参数切分到不同 GPU，适合低延迟单请求场景；PP 将模型按层切分，适合高并发批处理请求。集群节点间通常通过 RDMA over Converged Ethernet（RoCE）或 InfiniBand 实现高带宽、低延迟通信。

## 关键参数表

| 参数 | 单节点示例（NVIDIA DGX Spark） | 集群配置示例 |
|---|---|---|
| 架构 | NVIDIA Grace Blackwell | 多节点分布式 |
| CPU | 20 核 Arm（10 Cortex-X925 + 10 Cortex-A725） | 每节点相同 |
| GPU | NVIDIA Blackwell 集成 GPU | 每节点 1× Blackwell |
| Tensor Core | 第五代 | 第五代 |
| AI 算力 | $1000\,\text{TOPS}$（FP4 稀疏） | 随节点数线性扩展 |
| 系统内存 | $128\,\text{GB}$ LPDDR5x 统一内存 | 聚合容量扩展 |
| 内存带宽 | $273\,\text{GB/s}$ | 节点间经网络聚合 |
| 网络 | NVIDIA ConnectX-7 SmartNIC，双 QSFP 共 $200\,\text{Gb/s}$ | 可扩展至更多节点 |
| 存储 | $1\text{–}4\,\text{TB}$ NVMe M.2 | 共享存储/NAS |
| 最大可运行模型 | $200\,\text{B}$ 参数（单节点） | $405\,\text{B}$ 参数（双节点） |
| 典型功耗 | 约 $140\,\text{W}$ TDP（GB10） | 依节点数线性增加 |

## 应用场景

GPU 集群在机器人产业链中的应用已从传统的视觉训练扩展到端到端具身智能：

- **策略网络训练**：在 Isaac Gym / Isaac Lab 等并行仿真环境中，利用 GPU 集群同时运行数千个机器人实例，加速强化学习与模仿学习。
- **多模态大模型推理**：为机器人提供视觉-语言-动作（VLA）模型的实时推理能力，如任务规划、场景理解与指令跟随。
- **数字孪生与渲染**：在 Omniverse 等平台上进行高保真物理仿真、传感器数据合成与合成数据生成。
- ** Sim-to-Real 迁移**：通过域随机化（Domain Randomization）在集群上生成大规模多样化数据，缩小仿真与现实之间的差异。

## 供应链关系

GPU 集群在供应链中属于“算力基础设施”层。上游为 GPU/AI 芯片设计商（如 NVIDIA、AMD、Intel）与晶圆代工方（TSMC、Samsung）；中游为服务器/工作站 OEM（Dell、HPE、联想、Supermicro）及云服务提供商（AWS、Azure、阿里云、华为云）；下游面向机器人 AI 算法公司、自动驾驶研发团队、高校研究所以及机器人本体制造商。机器人 OEM 通常不直接采购 GPU 集群，而是通过云租赁或购买本地训练节点来获取算力。

## 来源与验证

- NVIDIA DGX Spark 官方 datasheet 确认 GB10 芯片、$1000\,\text{TOPS}$ FP4 算力、$128\,\text{GB}$ 统一内存、ConnectX-7 网络及双节点 $405\,\text{B}$ 模型推理能力。
- LMSYS 评测文章详细分析 DGX Spark 的 $1\,\text{PFLOP}$ FP4 稀疏性能、内存带宽瓶颈及 TP/PP 配置选择。
- StorageReview 的集群评测提供多厂商 DGX Spark 节点在流水线并行下的实测吞吐量数据。