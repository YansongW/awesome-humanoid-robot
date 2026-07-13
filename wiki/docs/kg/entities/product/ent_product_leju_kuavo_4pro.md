---
id: ent_product_leju_kuavo_4pro
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 乐聚 KUAVO 4 Pro
  en: Leju KUAVO 4 Pro
status: active
sources:
- id: src_leju_kuavo4pro_official
  type: website
  url: https://www.lejurobot.com/zh
- title: 乐聚机器人官网 - KUAVO 4 Pro
- id: src_leju_kuavo4pro_pconline
  type: website
  url: https://www.pconline.com.cn/zhizao/qiye/310013.html
- title: 乐聚（深圳）机器人技术有限公司企业详情 - 太平洋科技
- id: src_leju_kuavo4pro_szgov
  type: website
  url: https://tzb.sz.gov.cn/xwzx/gzdt/gqgz/content/post_1607427.html
- title: “能跑、能跳、能干活！”——人形机器人从实验室走进生活 - 深圳统战
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 乐聚 KUAVO 4 Pro / Leju KUAVO 4 Pro

## 概述

乐聚 KUAVO 4 Pro 是乐聚机器人推出的全尺寸高动态人形机器人，搭载深开鸿 KaihongOS（开源鸿蒙），属于 KUAVO“夸父”系列第四代升级产品。该机型在硬件上优化手臂性能、关节散热、续航与传感器配置，在软件上首创全身动量控制算法，面向工业智造、商业服务、科研探索等场景。

## 工作原理 / 技术架构

KUAVO 4 Pro 采用全尺寸双足构型，主体为航空级铝合金，全身自由度 40+。运动控制器全面开源，可接入轨迹规划、反馈控制、状态估计等模块。步态算法适配沙地、草地等地形，支持 20 cm 跳跃高度。操作系统层面，KaihongOS 的分布式软总线技术使机器人本体与周边设备实现数据互联与协同。

全身动量控制通过优化质心（CoM）与角动量分配，提高动态稳定性：

$$
\dot{\mathbf{h}} = \sum_i \mathbf{f}_i \times (\mathbf{r}_i - \mathbf{r}_{CoM}) + \boldsymbol{\tau}_i
$$

其中 $\mathbf{h}$ 为机器人总角动量，$\mathbf{f}_i$、$\boldsymbol{\tau}_i$ 为各接触点力与力矩。该算法相关成果发表于国际机器人期刊 RAL。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 产品定位 | 全尺寸高动态人形机器人 |
| 身高 | 约 1.47 m |
| 全身自由度 | 40+ |
| 操作系统 | KaihongOS（开源鸿蒙） |
| 主体材料 | 航空级铝合金 |
| 关节散热 | 优化热管理 |
| 传感器配置 | 深度摄像头及多种可扩展传感器 |
| 跳跃高度 | 约 20 cm（系列能力） |
| 控制架构 | 运动控制器全面开源 |
| 续航 | 未公开 |
| 行走速度 | 未公开 |

## 应用场景

- 工业制造中的柔性搬运与巡检
- 商业服务场景的迎宾、讲解与展示
- 科研教育与具身智能算法验证
- 康养陪护与家庭服务（远期规划）

## 供应链关系

乐聚机器人位于人形机器人整机层，上游自研一体化关节、运动控制算法与控制器，采购电机、减速器、传感器、电池与计算平台；中游为整机集成与操作系统适配；下游面向工业客户、科研院校与商业服务集成商。KUAVO 4 Pro 与 KUAVO 5/5-W、ROBAN 2、AELOS 开源鸿蒙版共同构成乐聚产品矩阵。

## 来源与验证

参数来源于乐聚机器人官网（https://www.lejurobot.com/zh）、太平洋科技企业详情（https://www.pconline.com.cn/zhizao/qiye/310013.html）及深圳统战部报道（https://tzb.sz.gov.cn/xwzx/gzdt/gqgz/content/post_1607427.html）。官网未公开 KUAVO 4 Pro 完整 datasheet，续航、速度等参数标注为“未公开”。