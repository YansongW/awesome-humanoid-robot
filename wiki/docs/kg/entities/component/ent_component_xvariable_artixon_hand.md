---
id: ent_component_xvariable_artixon_hand
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 自变量 ArtiXon Hand 五指灵巧手
  en: Xvariable ArtiXon Hand Five-Finger Dexterous Hand
status: active
sources:
- id: src_xvariable_official
  type: website
- title: 自变量机器人官网
  url: https://x2robot.com
- id: src_xvariable_quanta2
  type: website
- title: 自变量量子 2 号产品页
  url: https://x2robot.com/product/quantum2
- id: src_ithome_artixon
  type: website
- title: IT之家 – 自变量机器人 ArtiXon Hand 报道
  url: https://www.ithome.com/0/970/360.htm
- id: src_yesky_artixon
  type: website
- title: 天极网 – 自变量机器人硬件实测
  url: https://wap.yesky.com/news/hotnews/290/353290.shtml
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official website and tech media reports; missing
    values marked as 未公开.
---


# 自变量 ArtiXon Hand 五指灵巧手 / Xvariable ArtiXon Hand Five-Finger Dexterous Hand

## 概述

ArtiXon Hand 是自变量机器人（Xvariable / X Square Robot）自研的五指灵巧手，搭载于旗舰型轮式仿人形机器人“量子 2 号（Quanta X2）”。该灵巧手具备 20 个自由度（含 15 个主动自由度），整手重量低于 1 kg，支持 100 Hz 实时扭矩闭环控制，最小力感知分辨率约 0.1 N，设计寿命超过 100 万次操作，面向家庭服务、工业组装与科研教育等精细操作场景。

## 工作原理 / 技术架构

ArtiXon Hand 采用机电一体化手指设计，每根手指由多个微型执行器、传动机构与力/扭矩传感器组成。控制系统以 100 Hz 频率对关节扭矩进行闭环调节，使手指在接触物体时能够根据力反馈调整抓握力。

指尖或关节处力传感器的输出信号经标定后可映射为接触力 $F$。对于电阻式/电容式柔性力传感器，力-电阻关系常近似为

$$
\frac{\Delta R}{R_0} = k \cdot F
$$

其中 $R_0$ 为无负载电阻，$k$ 为灵敏度系数。灵巧手的最小可分辨力 $\Delta F_{\min}$ 受传感器噪声与 ADC 分辨率限制：

$$
\Delta F_{\min} = \frac{V_{\text{noise}}}{S \cdot G}
$$

其中 $S$ 为传感器灵敏度，$G$ 为信号调理增益。公开报道指出 ArtiXon Hand 最小感知力为 0.1 N。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 自由度 | 20（含 15 主动 + 5 被动） | IT之家 / 腾讯新闻 |
| 整手重量 | < 1 kg | IT之家 / 天极网 |
| 实时力矩闭环频率 | 100 Hz | IT之家 |
| 最小力感知 | 0.1 N | IT之家 |
| 设计寿命 | > 100 万次操作 | 天极网 |
| 支持手势 | 31 类 | 天极网 |
| 拇指对掌 / 多指协同 | 支持 | 自变量官网 |
| 驱动方式 | 未公开（推测为微型电机+传动机构） | - |
| 指尖力 / 负载能力 | 未公开 | - |
| 工作电压 / 通信接口 | 未公开 | - |

## 应用场景

- **家庭服务**：晾衣服、纸巾更换、杂物收纳、饮品制作等精细家务。
- **工业组装**：线束整理、小零件装配、柔性抓取与插拔操作。
- **科研教育**：具身智能算法验证、遥操作数据收集。
- **商业服务**：酒店客房整理、新零售商品摆放。

## 供应链关系

- **上游**：微型电机、减速器、力传感器、柔性电子皮肤材料、控制器、结构件。
- **制造商**：`ent_company_xvariable` -- `manufactures` --> `ent_component_xvariable_artixon_hand`。
- **下游整机**：ArtiXon Hand 搭载于 Quanta X2，构成 `ent_product_xvariable_quanta_x2` -- `uses` --> `ent_component_xvariable_artixon_hand`。
- **客户**：工业制造、酒店服务、新零售、科研教育、家庭服务。
- **竞争对手/对标**：智元“临界点”灵巧手、宇树 Dexterous Hand、Astribot 灵巧手、Salma Linker Hand。

## 来源与验证

1. 自变量机器人官网：https://x2robot.com
2. 自变量量子 2 号产品页：https://x2robot.com/product/quantum2
3. IT之家报道：https://www.ithome.com/0/970/360.htm
4. 天极网报道：https://wap.yesky.com/news/hotnews/290/353290.shtml
5. 腾讯新闻 / NE时代等公开报道