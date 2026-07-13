---
id: ent_product_phytium_s5000c
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 飞腾腾云 S5000C
  en: Phytium S5000C
aliases:
- 腾云 S5000C
- S5000C
status: active
sources:
- id: src_phytium_s5000c
  type: website
  url: https://www.phytium.com.cn/homepage/production/list/0
- title: 飞腾腾云 S 系列高性能服务器 CPU | 飞腾
- id: src_phytium_s5000c_detail
  type: website
  url: https://www.phytium.com.cn/homepage/production/13/
- title: 飞腾腾云 S5000C 高性能服务器 CPU | 飞腾
- id: src_sasac_s5000c
  type: website
  url: http://www.sasac.gov.cn/n4470048/n32559362/n35167919/n35167924/n35167949/c35256513/content.html
- title: “腾云 S5000C”新一代高性能服务器 CPU | 国务院国资委
- id: src_people_s5000c
  type: website
  url: http://828.people.com.cn/GB/459648/459651/index.html?article_id=265
- title: 飞腾公司：飞腾腾云 S5000C 高性能通用微处理器 | 人民网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 飞腾腾云 S5000C / Phytium S5000C

## 概述

飞腾腾云 S5000C 是飞腾信息技术有限公司推出的新一代高性能服务器 CPU，采用自主研发的 FTC862 处理器核心，兼容 ARMv8.2 指令集，面向计算服务器、存储服务器、AI 服务器、高端网安、行业级业务主机与大型互联网数据中心。该产品提供 16 核、32 核、64 核三种形态，支持 2–8 路多路扩展，集成 DDR5 内存控制器与 PCIe 5.0 高速接口，并支持 PSPA 1.0 安全架构。

## 工作原理 / 技术架构

S5000C 基于 ARMv8.2 超标量乱序执行微架构，单个芯片内集成多核 FTC862 核心、多级 Cache 与高速互连。64 核型号配置 32 MB 二级缓存与 32 MB 三级缓存，32 核型号配置 16 MB L2 与 16 MB L3。其存储器峰值带宽可通过 DDR5 通道数估算：

$$
B_{\max} = N_{\text{ch}} \times W_{\text{bus}} \times f_{\text{DDR5}}
$$

以 8 通道 DDR5-4800 为例，数据位宽 64 bit/通道，有效传输率为 4800 MT/s，则峰值带宽约为

$$
B_{\max} = 8 \times 8\ \text{B} \times 4.8\ \text{GT/s} = 307.2\ \text{GB/s}
$$

PCIe 5.0 每条 lane 单向速率为 32 GT/s，x16 链路单向带宽约 63 GB/s，较 PCIe 4.0 翻倍。

安全方面，S5000C 支持 PSPA 1.0（Phytium Security Platform Architecture），从物理、硬件、固件、运行环境与数据加密等层面提供全周期防护，并集成国密 SM2/SM3/SM4 算法加速。

## 关键参数表

| 参数 | 64 核型号 | 32 核型号 | 16 核型号 | 备注 |
|------|-----------|-----------|-----------|------|
| 核心架构 | FTC862 | FTC862 | FTC862 | 飞腾自研 |
| 指令集 | ARMv8.2 | ARMv8.2 | ARMv8.2 | 兼容 ARMv8.2 |
| 主频 | 2.1 GHz | 2.3 GHz | 2.1 GHz | 官方资料 |
| 二级缓存 | 32 MB | 16 MB | 8 MB | 官方资料 |
| 三级缓存 | 32 MB | 16 MB | 8 MB | 官方资料 |
| 内存控制器 | 8 个 DDR5 | 4 个 DDR5 | 2 个 DDR5 | 官方资料 |
| 高速 IO | PCIe 5.0 | PCIe 5.0 | PCIe 5.0 | 官方资料 |
| 多路支持 | 2–8 路 | 2–8 路 | 2–8 路 | 最多 128 核互联 |
| 安全架构 | PSPA 1.0 | PSPA 1.0 | PSPA 1.0 | 官方资料 |
| SPEC CPU 2006 单核整数 | 31.9 分 | 未公开 | 未公开 | 人民网 |
| SPEC CPU 2006 单核浮点 | 37.7 分 | 未公开 | 未公开 | 人民网 |
| SPEC CPU 2006 全芯片整数 | 1300 分 | 未公开 | 未公开 | 人民网 |
| SPEC CPU 2006 双路整数 | 2540 分 | 未公开 | 未公开 | 人民网 |

## 应用场景

- **政务与金融核心系统**：高安全、高可靠的服务器平台，支持国产化替代。
- **电信与 5G/6G 云网**：S5000C-M 衍生平台用于 5G 扩展型皮基站与通算智融合设备。
- **AI 智算中心**：作为 CPU 基座配合 AI 加速卡，支持 DeepSeek 等开源大模型本地化部署。
- **能源与交通**：电力调度、轨道交通信号与航空航天地面系统。
- **企业级存储与网安**：高端防火墙、存储控制器与网络安全设备。

## 供应链关系

飞腾腾云 S5000C 属于 **处理器芯片/服务器 CPU 层**，上游依赖 ARM 指令集授权、EDA 工具、晶圆代工（如台积电）与先进封装；中游由飞腾完成芯片设计、验证与 IP 整合；下游包括长城、浪潮、联想、同方等整机厂商，已推出超过 50 款服务器产品。飞腾构建了从指令系统、IP 核到芯片设计的全自主技术体系，并与 7000 多家生态伙伴完成软硬件适配。

## 来源与验证

- 飞腾官网 S5000C 产品列表：https://www.phytium.com.cn/homepage/production/list/0
- 飞腾官网 S5000C 详细规格：https://www.phytium.com.cn/homepage/production/13/
- 国务院国资委成果简介：http://www.sasac.gov.cn/n4470048/n32559362/n35167919/n35167924/n35167949/c35256513/content.html
- 人民网报道：http://828.people.com.cn/GB/459648/459651/index.html?article_id=265

16 核型号的具体缓存容量在公开资料中未完整披露，表中根据 64/32 核比例估算；SPEC 成绩由人民网报道引用飞腾官方数据。