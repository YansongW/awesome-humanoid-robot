---
id: ent_component_phytium_s5000c_cpu
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 飞腾腾云 S5000C 处理器
  en: Phytium Tengyun S5000C CPU
sources:
- id: src_phytium_official
  type: website
- title: '"飞腾官网"'
  url: https://www.phytium.com.cn
- id: src_phytium_serverflow
  type: website
- title: '"Phytium S5000C 服务器处理器特性"'
  url: https://serverflow.ru/blog/stati/kitayskie-cpu-feiteng-phytium-novye-arm-chipy-dlya-desktopa-i-serverov/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 飞腾腾云 S5000C 处理器 / Phytium Tengyun S5000C CPU

## 概述

飞腾腾云 S5000C 是天津飞腾信息技术有限公司推出的高性能服务器 CPU，基于 ARMv8.2 架构的自研 FTC862 核心，面向国产服务器、云计算、智算中心以及工业控制与机器人后台训练等场景，是中国电子信息产业集团（CEC）自主可控算力底座的重要组成部分。

## 工作原理 / 技术架构

S5000C 采用 FTC862 高性能乱序执行核心，兼容 ARMv8.2-A 指令集，支持硬件虚拟化、SMMU、国产 SM2/SM3/SM4 密码算法与 PSPA 1.0 安全架构。处理器最多可提供 64 核 128 线程，共享大容量 L3 Cache（32 MB，64 核型号），通过多路互连技术扩展为多路服务器。内存控制器支持 DDR5-4800 ECC REG，64 核型号为 8 通道，32/16 核型号为 4 通道。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 架构 | ARMv8.2-A，自研 FTC862 核心 | 飞腾公开资料 |
| 制程 | 16 nm（TSMC） | 公开报道 |
| 核心/线程配置 | 16C/32T、32C/64T、64C/128T | 公开报道 |
| 主频 | 64 核 2.1 GHz；32/16 核 2.3 GHz | 公开报道 |
| L3 Cache | 32 MB（64 核型号） | 公开报道 |
| 内存支持 | DDR5-4800 ECC REG | 公开报道 |
| 内存通道/容量 | 8 通道 / 1 TB（64 核）；4 通道 / 512 GB（32/16 核） | 公开报道 |
| 安全特性 | SM2/SM3/SM4、PSPA 1.0 | 飞腾公开资料 |
| TDP | 150–400 W（视型号） | 公开报道 |
| 价格 | 未公开 | - |

## 应用场景

国产服务器、云计算与虚拟化、数据库与大数据、智算中心训练/推理节点、机器人后台训练与仿真平台、工业控制。

## 供应链关系

飞腾（`ent_company_phytium`）作为 CEC 控股企业，由晶圆代工厂、封测厂、内存与主板厂商构成上游；下游客户覆盖政府、金融、电信、能源、轨交及机器人整机厂，与华为鲲鹏、海光、龙芯、兆芯等形成国产 CPU 竞争格局。

## 来源与验证

- 飞腾官网：https://www.phytium.com.cn
- Phytium S5000C 技术报道：https://serverflow.ru/blog/stati/kitayskie-cpu-feiteng-phytium-novye-arm-chipy-dlya-desktopa-i-serverov/