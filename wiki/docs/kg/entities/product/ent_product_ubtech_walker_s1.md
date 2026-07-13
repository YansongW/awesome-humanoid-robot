---
id: ent_product_ubtech_walker_s1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 优必选 Walker S1
  en: UBTECH Walker S1
status: active
sources:
- id: src_ubtech_walker_s1_hukeji
  type: website
  url: http://www.hukeji.com/ruanjian/202410/13784.html
- title: 优必选新品 Walker S1 亮相，汽车工厂实训表现如何 - 虎科技
- id: src_ubtech_walker_s1_people
  type: website
  url: http://finance.people.com.cn/BIG5/n1/2025/0303/c1004-40429998.html
- title: 機器人產業“加速跑” 多機協作秀出新花樣 - 人民网
- id: src_ubtech_walker_s1_vzkoo
  type: website
  url: https://www.vzkoo.com/read/20250613479e75aae06aa1aec4f7d313.html
- title: 2025 年优必选研究报告 - 未来智库
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 优必选 Walker S1 / UBTECH Walker S1

## 概述

优必选 Walker S1 是深圳市优必选科技股份有限公司于 2024 年 10 月发布的工业级全尺寸人形机器人，身高 172 cm，体重 76 kg，全身 41 个自由度，负载行走能力 15 kg。Walker S1 面向汽车总装物流、搬运与质检等工业场景，目前已进入比亚迪、东风柳汽、吉利汽车、奥迪一汽等汽车工厂实训。

## 工作原理 / 技术架构

Walker S1 采用集成化头部设计，双耳鱼眼相机提供 3D 立体视觉，全身布置多路 RGBD 与鱼眼相机实现 360° 多模态感知。一体化关节采用创新型旋转驱动，峰值扭矩 250 N·m；第三代仿人灵巧手集成 6 个阵列式触觉压力传感器。

机器人控制基于优必选 ROSA 2.0 与多模态规划大模型，结合仿真与真实数据构建具身智能能力。双足动态平衡通过零力矩点（ZMP）与模型预测控制（MPC）实现：

$$
p_{ZMP} = \frac{\sum_i m_i (\ddot{z}_i + g) r_i - \sum_i m_i z_i \ddot{r}_i}{\sum_i m_i (\ddot{z}_i + g)}
$$

其中 $m_i$、$r_i$、$z_i$ 为各连杆质量与水平/垂直位置。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 身高 | 172 cm |
| 体重 | 76 kg |
| 全身自由度 | 41 |
| 灵巧手主动自由度 | 6 |
| 负载行走能力 | 15 kg |
| 一体化关节峰值扭矩 | 250 N·m |
| 感知系统 | 双耳鱼眼相机 + 多路 RGBD/鱼眼相机 |
| 视觉 | 3D 立体视觉，360° 多模态感知 |
| 操作系统 | ROSA 2.0 |
| AI 能力 | 多模态规划大模型、6D 位姿识别、毫米级质检 |
| 质检准确率 | >99%（车标/车灯检测） |

## 应用场景

- 汽车总装车间搬运与分拣
- 车灯、车标等零部件毫米级质检
- 无人物流车/无人叉车/智能制造系统协同
- 多机协同与群体智能产线

## 供应链关系

优必选 Walker S1 处于人形机器人整机层，上游自研一体化关节、伺服系统、灵巧手、视觉模组与控制器；中游为整机集成、运动控制与 AI 大模型；下游面向汽车制造商与工业集成商。Walker S1 是 Walker S 系列面向工业量产的旗舰型号之一，与 Walker S、Walker S Lite、Walker S2 构成产品矩阵。

## 来源与验证

参数来源于虎科技报道（http://www.hukeji.com/ruanjian/202410/13784.html）、人民网报道（http://finance.people.com.cn/BIG5/n1/2025/0303/c1004-40429998.html）与未来智库研报（https://www.vzkoo.com/read/20250613479e75aae06aa1aec4f7d313.html）。行走速度、续航等细节未在公开资料中完整披露，标注为“未公开”。