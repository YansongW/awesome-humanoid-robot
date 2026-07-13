---
id: ent_product_mech_mind_mech_eye_lsr_l
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 梅卡曼德 Mech-Eye LSR L
  en: Mech-Mind Mech-Eye LSR L Industrial 3D Camera
status: active
sources:
- id: src_mechmind_lsr_l_specs
  type: website
  url: https://docs.mech-mind.net/zh/eye-3d-camera/latest/hardware/specifications-lsr-l.html
- title: Mech-Eye LSR L 相机技术参数 - 梅卡曼德文档中心
- id: src_mechmind_product_page
  type: website
  url: https://www.mech-mind.com.cn/product/mech-eye-industrial-3D-camera.html
- title: Mech-Eye 工业级3D相机 - 梅卡曼德官网
- id: src_mechmind_manual
  type: website
  url: https://community-mech.oss-cn-shanghai.aliyuncs.com/%E7%9B%B8%E6%9C%BA%E7%A1%AC%E4%BB%B6/%E4%BA%A7%E5%93%81%E5%92%8C%E5%8F%82%E6%95%B0/Mech-Eye%E5%B7%A5%E4%B8%9A%E7%BA%A73D%E7%9B%B8%E6%9C%BA%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E4%B9%A6_V4.0.pdf
- title: Mech-Eye 工业级3D相机使用说明书 V4.0
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 梅卡曼德 Mech-Eye LSR L / Mech-Mind Mech-Eye LSR L Industrial 3D Camera

## 概述

Mech-Eye LSR L 是梅卡曼德（Mech-Mind）推出的工业级激光 3D 相机，面向远距离、大视野、强环境光干扰的机器人引导应用。该相机采用结构光/激光三角测量原理，可在 >30,000 lx 的环境光下获取完整、细致的彩色点云，适用于拆码垛、上下料、焊接引导与大型工件定位。

## 工作原理 / 技术架构

LSR L 通过投射激光结构光图案，并由双目相机捕捉物体表面图案形变，利用三角测量计算深度。对于基线长度为 \(B\)、焦距为 \(f\) 的双目系统，视差 \(d = x_L - x_R\) 与深度 \(Z\) 的关系为

\[
Z = \frac{B \cdot f}{d}
\]

空间分辨率随工作距离增加而降低。在距离 \(Z\) 处，像元尺寸为 \(p\) 时，横向分辨率近似为

\[
\delta x \approx \frac{Z \cdot p}{f}
\]

相机内置 2D 纹理相机，可输出 4000×3000 分辨率的 RGB 图像，与深度图配准后生成彩色点云。整机防护等级为 IP65，采用千兆以太网接口与 24 V DC 供电。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 推荐工作距离 | 1200–3000 mm |
| 对焦距离 | 1500 / 2500 mm |
| 近端视野 | \(1200 \times 1000\,\text{mm}\) @ 1.2 m |
| 远端视野 | \(3000 \times 2400\,\text{mm}\) @ 3.0 m |
| 深度图分辨率 | \(2048 \times 1536\) |
| RGB 图分辨率 | \(4000 \times 3000\) |
| Z 向单点重复精度（\(1\sigma\)） | \(0.5\,\text{mm}\) @ 3 m |
| VDI/VDE 测量精度 | \(1.0\,\text{mm}\) @ 3 m |
| 典型采集时间 | 0.5–0.9 s |
| 推荐暖机时间 | 30 min |
| 防护等级 | IP65 |
| 通信接口 | 千兆以太网 |
| 供电 | 24 V DC |

## 应用场景

- 大型工件上下料与机器看护
- 物流拆码垛与托盘识别
- 钢结构、船舶等焊接场景的视觉引导
- 汽车制造中的涂胶、装配定位
- 铸造、锻造等高温高反光环境下的 3D 检测

## 供应链关系

Mech-Eye LSR L 由梅卡曼德（雄安）机器人科技股份有限公司研发制造。上游包括激光器、工业相机传感器、光学镜头、FPGA/SoC 计算单元与结构件；中游为梅卡曼德自研的光学系统、标定算法与 Mech-Eye SDK；下游与 Mech-Vision 机器视觉软件、Mech-Viz 机器人编程软件及 Mech-DLK 深度学习软件配合，面向机器人集成商与终端制造企业。

## 来源与验证

参数直接引用梅卡曼德官方文档中心与产品手册。整机重量、尺寸、功耗等未在公开参数表中披露，标注为“未公开”。