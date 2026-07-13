# 芯原股份 / VeriSilicon

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 芯原股份 |
| **英文名** | VeriSilicon Holdings |
| **总部** | 中国上海市浦东新区 |
| **成立时间** | 2001 年 |
| **官网** | [https://www.verisilicon.com](https://www.verisilicon.com) |
| **供应链环节** | 芯片设计服务、半导体 IP、AI/视频/显示 IP |
| **企业属性** | 上市公司（科创板：688521） |
| **母公司/所属集团** | 无（独立上市主体） |
| **数据来源** | 芯原官网、年报、产品手册、公开新闻稿 |

## 公司简介

芯原股份是中国领先的芯片设计服务与半导体 IP 提供商，为全球客户提供一站式芯片定制与 IP 授权服务。

芯原拥有从芯片设计平台、视频/显示 IP、AI 加速 IP 到射频/接口 IP 的完整能力，其 VIP9000/VIP9400 系列神经网络处理器 IP 广泛应用于边缘 AI、智能汽车、物联网及机器人芯片。公司采用“轻设计”模式，不直接销售芯片，而是通过 IP 授权与芯片定制服务赋能客户。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| AI 处理器 IP | 神经网络加速器 IP | VIP9000 / VIP9400 / NPU IP | 边缘 AI、汽车、机器人 |
| 视频 IP | 视频编解码与 ISP | Hantro / Vivante ISP | 安防、汽车、消费电子 |
| 显示 IP | GPU/显示控制器 | Vivante GPU / DC | 移动、汽车、IoT |
| 芯片定制服务 | 一站式芯片设计 | 客户定制 SoC | 各行业 |

## 代表产品

### 芯原 VIP9000 系列 NPU IP

> 芯原 VIP9000：请访问 [官方资料](https://www.verisilicon.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 可配置神经网络处理器 IP | 芯原公开资料 |
| 算力 | 0.5–数百 TOPS（视配置） | 芯原公开资料 |
| 精度支持 | INT8 / INT16 / FP16 / BFloat16 | 芯原公开资料 |
| 模型支持 | TensorFlow / PyTorch / ONNX 等 | 芯原公开资料 |
| 总线接口 | AXI / AHB | 芯原公开资料 |
| 制程 | 客户可选（公开报道） | 公开报道 |
| 功耗 | 视客户实现而定 | 芯原公开资料 |
| 价格 | IP 授权，未公开 | - |

**技术亮点**：高度可配置 NPU IP、支持 Transformer 与大模型、与 ISP/GPU 协同、低功耗边缘 AI。

**应用场景**：智能手机、汽车 ADAS、安防 IPC、机器人端侧感知、AIoT。

### 芯原 Vivante GPU IP

> 芯原 Vivante GPU：请访问 [官方资料](https://www.verisilicon.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 可扩展 GPU / GPGPU IP | 芯原公开资料 |
| 性能 | 视配置从低端到车规高算力 | 芯原公开资料 |
| API 支持 | OpenGL ES / Vulkan / OpenCL 等 | 芯原公开资料 |
| 功能安全 | 部分 IP 支持 ASIL-B/D | 芯原公开资料 |
| 应用场景 | 显示、图形渲染、通用计算 | 芯原公开资料 |
| 价格 | IP 授权，未公开 | - |

**技术亮点**：小面积低功耗、汽车功能安全认证、与 NPU/ISP 形成完整视觉计算方案。

**应用场景**：车载信息娱乐、仪表盘、机器人 HMI、工业显示。

## 供应链位置

- **上游关键零部件/材料**：EDA 工具、IP 授权、晶圆代工合作伙伴、封测。
- **下游客户/应用场景**：芯片设计公司、IDM、Fabless、汽车电子、消费电子、机器人芯片厂商。
- **主要竞争对手/对标**：ARM Mali/Immortalis、Imagination PowerVR、Synopsys ARC NPU、Cadence Tensilica。

## 知识图谱节点与关系

- 公司实体：`ent_company_verisilicon`
- 产品实体：`ent_product_verisilicon_vip9000`
- 零部件实体：`ent_component_verisilicon_vip9000_npu`
- 关键关系：
  - `ent_company_verisilicon` -- `manufactures` --> `ent_product_verisilicon_vip9000`
  - `ent_company_verisilicon` -- `manufactures` --> `ent_component_verisilicon_vip9000_npu`
  - `ent_product_verisilicon_vip9000` -- `uses` --> `ent_component_verisilicon_vip9000_npu`

## 参考资料

1. [芯原股份官网](https://www.verisilicon.com)
2. [芯原 AI 处理器 IP](https://www.verisilicon.com/IPPortfolio/Artificial-Intelligence-IP.html)
3. 芯原股份 2024 年度报告