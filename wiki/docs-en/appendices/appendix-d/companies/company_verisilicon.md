# VeriSilicon Holdings

> This entry belongs to [Appendix D: Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 芯原股份 |
| **English Name** | VeriSilicon Holdings |
| **Headquarters** | Pudong New Area, Shanghai, China |
| **Founded** | 2001 |
| **Website** | [https://www.verisilicon.com](https://www.verisilicon.com) |
| **Supply Chain Role** | Chip Design Services, Semiconductor IP, AI/Video/Display IP |
| **Company Type** | Listed Company (STAR Market: 688521) |
| **Parent Company/Group** | None (Independent listed entity) |
| **Data Source** | VeriSilicon official website, annual reports, product manuals, public press releases |

## Company Overview

VeriSilicon Holdings is a leading chip design service and semiconductor IP provider in China, offering one-stop chip customization and IP licensing services to global customers.

VeriSilicon possesses a complete capability ranging from chip design platforms, video/display IP, AI acceleration IP, to RF/interface IP. Its VIP9000/VIP9400 series neural network processor IP is widely used in edge AI, smart vehicles, IoT, and robotics chips. The company adopts a "light design" model, not directly selling chips, but empowering customers through IP licensing and chip customization services.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| AI Processor IP | Neural Network Accelerator IP | VIP9000 / VIP9400 / NPU IP | Edge AI, Automotive, Robotics |
| Video IP | Video Codec & ISP | Hantro / Vivante ISP | Security, Automotive, Consumer Electronics |
| Display IP | GPU/Display Controller | Vivante GPU / DC | Mobile, Automotive, IoT |
| Chip Customization Service | One-stop Chip Design | Customer Custom SoC | Various Industries |

## Representative Products

### VeriSilicon VIP9000 Series NPU IP

> VeriSilicon VIP9000: Please visit [Official Documentation](https://www.verisilicon.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Architecture | Configurable Neural Network Processor IP | VeriSilicon Public Information |
| Compute Power | 0.5–Hundreds of TOPS (depending on configuration) | VeriSilicon Public Information |
| Precision Support | INT8 / INT16 / FP16 / BFloat16 | VeriSilicon Public Information |
| Model Support | TensorFlow / PyTorch / ONNX, etc. | VeriSilicon Public Information |
| Bus Interface | AXI / AHB | VeriSilicon Public Information |
| Process Node | Customer Selectable (public reports) | Public Reports |
| Power Consumption | Depends on customer implementation | VeriSilicon Public Information |
| Price | IP licensing, not disclosed | - |

**Technical Highlights**: Highly configurable NPU IP, supports Transformer and large models, co-processing with ISP/GPU, low-power edge AI.

**Application Scenarios**: Smartphones, Automotive ADAS, Security IPC, Robotic Edge Perception, AIoT.

### VeriSilicon Vivante GPU IP

> VeriSilicon Vivante GPU: Please visit [Official Documentation](https://www.verisilicon.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Architecture | Scalable GPU / GPGPU IP | VeriSilicon Public Information |
| Performance | Ranges from low-end to automotive-grade high compute power depending on configuration | VeriSilicon Public Information |
| API Support | OpenGL ES / Vulkan / OpenCL, etc. | VeriSilicon Public Information |
| Functional Safety | Some IP supports ASIL-B/D | VeriSilicon Public Information |
| Application Scenarios | Display, Graphics Rendering, General Purpose Computing | VeriSilicon Public Information |
| Price | IP licensing, not disclosed | - |

**Technical Highlights**: Small area, low power, automotive functional safety certification, forms a complete visual computing solution with NPU/ISP.

**Application Scenarios**: In-vehicle Infotainment, Instrument Clusters, Robot HMI, Industrial Displays.

## Supply Chain Position

- **Upstream Key Components/Materials**: EDA tools, IP licensing, foundry partners, packaging and testing.
- **Downstream Customers/Application Scenarios**: Chip design companies, IDMs, Fabless, automotive electronics, consumer electronics, robotics chip manufacturers.
- **Main Competitors/Peers**: ARM Mali/Immortalis, Imagination PowerVR, Synopsys ARC NPU, Cadence Tensilica.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_verisilicon`
- Product Entity: `ent_product_verisilicon_vip9000`
- Component Entity: `ent_component_verisilicon_vip9000_npu`
- Key Relationships:
  - `ent_company_verisilicon` -- `manufactures` --> `ent_product_verisilicon_vip9000`
  - `ent_company_verisilicon` -- `manufactures` --> `ent_component_verisilicon_vip9000_npu`
  - `ent_product_verisilicon_vip9000` -- `uses` --> `ent_component_verisilicon_vip9000_npu`

## References

1. [VeriSilicon Official Website](https://www.verisilicon.com)
2. [VeriSilicon AI Processor IP](https://www.verisilicon.com/IPPortfolio/Artificial-Intelligence-IP.html)
3. VeriSilicon Holdings 2024 Annual Report
