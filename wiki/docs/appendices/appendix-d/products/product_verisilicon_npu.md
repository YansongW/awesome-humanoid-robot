# 芯原 VIP9000 NPU IP / VeriSilicon VIP9000

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [芯原股份 / VeriSilicon](../companies/company_verisilicon.md) |
| **产品类别** | 神经网络处理器 IP（NPU IP） |
| **发布时间** | VIP9000 系列持续迭代 |
| **状态** | 商用授权 |
| **官网/来源** | 芯原官网、产品手册 |

## 产品概述

芯原 VIP9000 系列是可配置、可扩展的神经网络处理器 IP，面向边缘 AI、智能汽车、消费电子及机器人芯片提供高效 AI 加速能力。

VIP9000 支持 INT8/INT16/FP16/BFloat16 等精度，可运行 CNN、Transformer 及大语言模型等主流网络。其高度可配置的硬件架构使客户能够根据算力、功耗与面积目标灵活定制，并与芯原的 ISP、GPU、视频编解码 IP 协同，构建端到端视觉与 AI 解决方案。

## 产品图片

> 芯原 VIP9000：请访问 [官方资料](https://www.verisilicon.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| IP 名称 | 芯原 VIP9000 系列 NPU | 芯原官网 |
| 类型 | 神经网络处理器 IP | 芯原公开资料 |
| 算力范围 | 0.5–数百 TOPS（视配置） | 芯原公开资料 |
| 精度支持 | INT8 / INT16 / FP16 / BFloat16 | 芯原公开资料 |
| 模型支持 | TensorFlow / PyTorch / ONNX 等 | 芯原公开资料 |
| 总线接口 | AXI / AHB | 芯原公开资料 |
| 制程 | 客户可选 | 公开报道 |
| 功耗 | 视客户实现而定 | 芯原公开资料 |
| 授权模式 | IP 授权 + 芯片定制服务 | 芯原公开资料 |
| 价格 | IP 授权，未公开 | - |

## 供应链位置

- **制造商**：[芯原股份 / VeriSilicon](../companies/company_verisilicon.md)
- **核心零部件/技术来源**：自研 NPU 微架构、EDA 工具、客户晶圆代工/封测。
- **下游应用/客户**：芯片设计公司、IDM、Fabless、汽车电子、消费电子、机器人芯片厂商。

## 知识图谱节点与关系

- 产品实体：`ent_product_verisilicon_vip9000`
- 零部件实体：`ent_component_verisilicon_vip9000_npu`
- 制造商实体：`ent_company_verisilicon`
- 关键关系：
  - `rel_ent_company_verisilicon_manufactures_ent_product_verisilicon_vip9000`（`ent_company_verisilicon` → `manufactures` --> `ent_product_verisilicon_vip9000`）
  - `rel_ent_company_verisilicon_manufactures_ent_component_verisilicon_vip9000_npu`（`ent_company_verisilicon` → `manufactures` --> `ent_component_verisilicon_vip9000_npu`）
  - `ent_product_verisilicon_vip9000` -- `uses` --> `ent_component_verisilicon_vip9000_npu`

## 应用场景

- **机器人端侧感知**：集成于机器人 SoC，实现视觉、语音与多模态 AI 推理。
- **智能汽车 ADAS**：用于前视、环视及舱内感知系统。
- **智能安防与 AIoT**：支持 IPC、门铃、可穿戴设备的高效 AI 视觉。

## 竞争对比

| 对比项 | 芯原 VIP9000 | ARM Ethos | Synopsys ARC NPU |
|--------|------|------|------|
| 类型 | NPU IP | NPU IP | NPU IP |
| 可配置性 | 高 | 中 | 高 |
| 生态协同 | ISP/GPU/视频 IP 协同 | ARM 生态 | Synopsys 生态 |
| 授权模式 | IP 授权 | IP 授权 | IP 授权 |

## 选购与部署建议

- 根据目标模型、算力与功耗预算选择 VIP9000 配置与总线接口。
- 评估模型量化与编译工具链对目标网络的适配效果。
- 建议通过芯原官方渠道获取 IP 评估包、参考设计与技术支持。

## 相关词条

- [制造商：芯原股份 / VeriSilicon](../companies/company_verisilicon.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [芯原股份官网](https://www.verisilicon.com)
2. [芯原 AI 处理器 IP](https://www.verisilicon.com/IPPortfolio/Artificial-Intelligence-IP.html)
3. 芯原股份 2024 年度报告