---
id: ent_product_efort_yobot_w1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 埃夫特 Yobot W1
  en: Efort Yobot W1
status: active
sources:
- id: src_efort_yobot_w1_10jqka
  type: website
  url: https://stock.10jqka.com.cn/20250302/c666402451.shtml
- title: 智能机器人，“上新” - 同花顺
- id: src_efort_yobot_w1_ahchanye
  type: website
  url: https://www.ahchanye.com/zixun/52362.html
- title: 芜湖首款人形机器人发布 - 安徽产业网
- id: src_efort_yobot_w1_hangyan
  type: website
  url: https://www.hangyan.co/charts/3587431244398331877
- title: 埃夫特 Yobot W1 人形机器人 - 行研数据
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 埃夫特 Yobot W1 / Efort Yobot W1

## 概述

埃夫特 Yobot W1 是埃夫特智能装备股份有限公司（Efort）与启智（芜湖）智能机器人有限公司于 2025 年 2 月联合发布的第一代轮式人形机器人。Yobot W1 采用双轮移动底盘与上半身人形结构，全身 32 个自由度，搭载埃夫特自研的智能机器人通用技术底座 Openmind OS，面向汽车总装物流、康养、医院与家庭服务等场景。

## 工作原理 / 技术架构

Yobot W1 以双轮差速驱动实现移动，通过底盘回转实现原地掉头，上半身保留双臂与灵巧操作能力。机器人搭载 Openmind OS 操作系统，配套墨斗 IDE 集成开发环境与 EBox 全国产芯片控制系统，支持机器视觉、AI 算法与实时运动控制的融合开发。

移动底盘速度 $v$ 与左右轮角速度 $\omega_L$、$\omega_R$ 的关系为：

$$
v = \frac{r(\omega_L + \omega_R)}{2}, \quad \omega = \frac{r(\omega_R - \omega_L)}{L}
$$

其中 $r$ 为轮半径，$L$ 为轮距，$\omega$ 为机器人自转角速度。该结构兼顾通过性与运行稳定性。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 类型 | 轮式人形机器人 |
| 全身自由度 | 32 |
| 移动方式 | 双轮差速底盘 |
| 转向方式 | 底盘快速回转，原地掉头 |
| 操作系统 | Openmind OS |
| 开发环境 | 墨斗 IDE |
| 控制系统 | EBox（全国产芯片） |
| 灵巧手 | 自研灵巧手 |
| 感知能力 | 三维空间精准感知 |
| 身高/体重/续航 | 未公开 |
| 最大移动速度 | 未公开 |

## 应用场景

- 汽车总装物流搬运与分拣
- 工厂巡检与安防
- 康养与医院陪护辅助
- 家居服务（远期规划）

## 供应链关系

埃夫特位于工业机器人与人形机器人整机层，上游采购/自研伺服电机、减速器、控制器、传感器与移动底盘；中游为机器人本体、操作系统与算法平台；下游面向汽车、新能源、3C 等行业集成商与终端用户。Yobot W1 与 Yobot R1（双足）共同构成埃夫人形机器人产品矩阵，依托埃夫特在工业机器人领域的供应链积累。

## 来源与验证

参数来源于同花顺报道（https://stock.10jqka.com.cn/20250302/c666402451.shtml）、安徽产业网（https://www.ahchanye.com/zixun/52362.html）及行研数据（https://www.hangyan.co/charts/3587431244398331877）。由于产品处于首发阶段，埃夫特尚未公开完整 datasheet，身高、体重、续航、速度等参数标注为“未公开”。