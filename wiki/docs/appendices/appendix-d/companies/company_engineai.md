# 众擎机器人 / EngineAI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 众擎机器人 |
| **英文名** | EngineAI |
| **总部** | 中国广东深圳 |
| **成立时间** | 2023 年 |
| **官网** | [https://www.engineai.com.cn](https://www.engineai.com.cn) |
| **供应链环节** | 整机 OEM / 通用人形机器人 |
| **企业属性** | 高动态、开源、拟人步态 |
| **母公司/所属集团** | 无 |
| **数据来源** | 众擎官网、官方 FAQ、量子位/机器人大讲堂 |

## 公司简介

众擎机器人以高动态运动与全栈自研关节为核心，面向科研教育与工业制造提供开放型人形机器人平台。

众擎已发布 PM01 轻量型开源人形机器人与 SE01 全尺寸拟人步态人形机器人。PM01 身高 1.38 m、体重约 42 kg，全身自由度 ≥23，腰部可实现 320° 旋转；SE01 身高 1.7 m、体重约 55 kg，全身 32 个自由度，采用航空级铝合金，强调自然步态与长寿命。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 轻量开源人形 | 科研教育、算法验证 | PM01 | 高校、实验室、开发者 |
| 全尺寸通用人形 | 工业与家庭场景 | SE01 | 智能制造、仓储、服务 |

## 代表产品

### EngineAI PM01

![EngineAI PM01](https://cn-engineai-1304599088.cos.ap-guangzhou.myqcloud.com/uploads/upload/images/20251029/668bd44456c24b778a8c7d824e42d858.png)

> 图片来源：EngineAI 官网产品图。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 站立 1400(H)×535.55(W)×252.66(D) mm | EngineAI 官网 |
| 重量 | 商业版约 42 kg；教育版约 43 kg | EngineAI 官网 |
| 自由度 | 商业版 23 DOF；教育版 24 DOF | EngineAI 官网 |
| 负载/扭矩 | 膝关节峰值扭矩 145 N·m（Q90H 电机） | EngineAI 官网 |
| 速度/转速 | 移动速度 ＞2 m/s（硬件支持） | EngineAI 官网 |
| 续航 | 约 2 小时（10000 mAh 快拆电池） | EngineAI 官网 |
| 接口/通信 | 教育版支持二次开发，搭载 NVIDIA Jetson Orin NX (16G) | EngineAI 官网 |
| 价格 | 商用版 8.8 万元（含税） | 官方 FAQ |

**技术亮点**：全栈自研一体化关节、腰部 ＞300° 旋转、开源训练/部署代码、手持遥控、交互屏

**应用场景**：科研教育算法验证、工业制造二次开发、商业展示与舞蹈表演。

### EngineAI SE01

> EngineAI SE01：请访问 [官方资料](https://www.engineai.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 170 cm（高） | 公开报道 |
| 重量 | 约 55 kg | 公开报道 |
| 自由度 | 32 DOF | 公开报道 |
| 负载/扭矩 | 膝关节最大扭矩 186 N·m | 机器人经销商资料 |
| 速度/转速 | 常态行走 2 m/s | 公开报道 |
| 续航 | 约 2 小时 | 公开报道 |
| 接口/通信 | Intel RealSense D435、360° 激光雷达、6 颗高清摄像头 | 公开报道 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：航空级铝材、拟人自然步态、多层规划算法、5–10 年设计寿命

**应用场景**：工业制造、仓储巡检、家庭服务等复杂场景。

## 供应链位置

- **上游关键零部件/材料**：自研 Q90H/Q25H 一体化关节电机、行星/谐波减速器、电机；Intel RealSense、NVIDIA Jetson、电池。
- **下游客户/应用场景**：高校科研、开发者、工业制造企业、商业展示。
- **主要竞争对手/对标**：宇树 G1/H1、智元机器人、傅利叶 GR 系列

## 知识图谱节点与关系

- 公司实体：`ent_company_engineai`
- 产品实体：`ent_product_engineai_pm01`
- 零部件实体：`ent_component_engineai_q90h`
- 关键关系：
  - `ent_company_engineai` -- `manufactures` --> `ent_product_engineai_pm01`
  - `ent_company_engineai` -- `manufactures` --> `ent_component_engineai_q90h`
  - `ent_product_engineai_pm01` -- `uses` --> `ent_component_engineai_q90h`

## 参考资料

1. [EngineAI PM01 产品页](https://www.engineai.com.cn/product-pm01.html)
2. [EngineAI SE01 产品页](https://en.engineai.com.cn/product-se01)
3. [众擎机器人 FAQ](https://www.engineai.com.cn/about-news-media/23.html)