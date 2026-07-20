# AMD / Advanced Micro Devices

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | AMD (Ultra Micro Semiconductor) |
| **English Name** | Advanced Micro Devices |
| **Headquarters** | Santa Clara, California, USA |
| **Founded** | 1969 |
| **Official Website** | [https://www.amd.com](https://www.amd.com) |
| **Supply Chain Role** | CPU/GPU/FPGA/AI Acceleration, Data Center, Edge AI Computing |
| **Enterprise Attribute** | Public Company (NASDAQ: AMD) |
| **Parent Company/Group** | None (AMD is the listed entity) |
| **Data Source** | AMD Official Website, Xilinx Official Website, Product Manuals, Public Press Releases |

## Company Profile

AMD is a world-leading semiconductor design and computing platform enterprise, with products covering CPU, GPU, FPGA, and adaptive computing. Through the acquisition of Xilinx, it has entered the AI acceleration and edge computing markets.

AMD provides diverse computing power for robotics and embodied intelligence: EPYC server CPUs for training and simulation; Instinct GPUs for large model training/inference; Ryzen AI processors integrating NPUs for edge-side AI; Xilinx Kria and Versal adaptive computing platforms offer low-latency, programmable AI inference and sensor fusion capabilities.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| EPYC | Data Center Server CPU | EPYC 9004 / 9005 Series | Cloud Computing, Training/Inference Servers |
| Instinct | Data Center AI GPU | MI300X / MI325X | Large Model Training/Inference, HPC |
| Ryzen AI | Edge AI PC/Embedded Processor | Ryzen AI 300 Series | Edge AI, Robot Main Controller |
| Xilinx Kria | Adaptive Edge AI Platform | Kria K26 / KR260 | Robot Vision, Industrial Control |
| Xilinx Versal | Adaptive Computing Acceleration Platform | Versal AI Edge Series | Autonomous Driving, Robot Perception |

## Representative Products

### AMD Ryzen AI (NPU Integrated Processor)

> AMD Ryzen AI: Please visit [Official Documentation](https://www.amd.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | Zen CPU + RDNA GPU + XDNA NPU | AMD Public Information |
| NPU Compute | Up to ~55 TOPS INT8 (Ryzen AI 300 Series) | AMD Public Information |
| CPU Cores | Up to 12 Cores Zen 5 | AMD Public Information |
| Process Node | 4 nm (Public Reports) | Public Reports |
| Memory | Supports LPDDR5X / DDR5 | AMD Public Information |
| Interfaces | USB4, PCIe, Display Output, etc. | AMD Public Information |
| Power Consumption | ~15–54 W | Public Reports |
| Price | Depends on OEM System | - |

**Technical Highlights**: CPU+GPU+NPU Tri-unity, XDNA Architecture NPU High Efficiency, Supports Windows AI and ONNX Runtime.

**Application Scenarios**: AI PC, Edge AI Box, Robot Edge-side Perception and Decision-making, Industrial HMI.

### AMD Xilinx Kria K26

> AMD Xilinx Kria K26: Please visit [Official Documentation](https://www.amd.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | Zynq UltraScale+ MPSoC | AMD/Xilinx Public Information |
| AI Compute | ~1.4 TOPS INT8 | AMD/Xilinx Public Information |
| CPU | Quad-core ARM Cortex-A53 + Dual-core Cortex-R5 | AMD/Xilinx Public Information |
| Interfaces | Multiple MIPI, USB, Gigabit Ethernet, GPIO | AMD/Xilinx Public Information |
| Power Consumption | ~5–15 W | Public Reports |
| Form Factor | SOM Module + Carrier Board | AMD/Xilinx Public Information |
| Price | ~199 USD starting (1k) | AMD Public Pricing |

**Technical Highlights**: FPGA+ARM Heterogeneous, Programmable Logic, Low-latency Sensor Interfaces, Industrial-grade Reliability.

**Application Scenarios**: Robot Vision, Industrial Inspection, Medical Imaging, Smart Retail, Edge AI.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC Foundry, Memory Partners, Packaging & Testing, EDA/IP, PCB/Passive Components.
- **Downstream Customers/Application Scenarios**: Data Centers, Cloud Computing Providers, OEM/ODM, Industrial Automation, Automotive Electronics, Robot Manufacturers, Research Institutes.
- **Main Competitors/Counterparts**: NVIDIA GPU/Platform, Intel Xeon/AI PC, Qualcomm Edge AI, Huawei Ascend, Horizon Robotics.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_amd`
- Product Entity: `ent_product_amd_ryzen_ai`
- Component Entity: `ent_component_amd_ryzen_ai_npu`
- Key Relationships:
  - `ent_company_amd` -- `manufactures` --> `ent_product_amd_ryzen_ai`
  - `ent_company_amd` -- `manufactures` --> `ent_component_amd_ryzen_ai_npu`
  - `ent_product_amd_ryzen_ai` -- `uses` --> `ent_component_amd_ryzen_ai_npu`

## References

1. [AMD Official Website](https://www.amd.com)
2. [AMD Ryzen AI Product Page](https://www.amd.com/en/processors/ryzen-ai)
3. [AMD Xilinx Kria Product Page](https://www.amd.com/en/products/system-on-modules/kria.html)
