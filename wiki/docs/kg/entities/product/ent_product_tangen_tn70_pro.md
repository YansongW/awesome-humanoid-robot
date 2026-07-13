---
id: ent_product_tangen_tn70_pro
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 汤恩 TN70-Pro 智能洗地机器人
  en: Taung TN70-Pro Intelligent Scrubber Robot
status: active
sources:
- id: src_taung_tn70_official
  type: website
  url: https://www.taung.cn/ProductsSt_sparkoztn70.html
- title: 商用清洁机器人 TN70 - 汤恩智能官网
- id: src_taung_tn70_leaderobot
  type: website
  url: https://www.leaderobot.com/news/558
- title: 汤恩科技清洁机器人入驻来福士商场 - 机器人大讲堂
- id: src_taung_company
  type: website
  url: https://www.taung.cn/
- title: 汤恩智能科技（上海）有限公司官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 汤恩 TN70-Pro 智能洗地机器人 / Taung TN70-Pro Intelligent Scrubber Robot

## 概述

TN70-Pro 是汤恩智能面向大型商用与工业场景推出的全自动智能清洁机器人，集扫地、洗地、吸尘、尘推与消杀功能于一体。该机器人采用视觉与激光融合导航定位，配备 70 L 清水箱与 50 L 污水箱，清洁效率可达 \(2040\,\text{m}^2/\text{h}\)，适用于商场、医院、车库、机场、车站与工厂等大面积复杂环境。

## 工作原理 / 技术架构

TN70-Pro 基于汤恩自研的视觉 + 激光融合 SLAM 算法，结合全景单目摄像头、激光雷达、深度相机、超声波、IMU 与电子防撞条实现厘米级定位与毫秒级动态避障。清洁系统由双滚刷、刷盘与吸水扒组成，对地压力 \(27\,\text{kg}\)，刷盘单位面积压力 \(13.2\,\text{g/cm}^2\)。

清洁效率可由下式估算：

\[
\eta = w \cdot v \cdot t
\]

其中 \(w\) 为清洁宽度，\(v\) 为运行速度，\(t\) 为作业时间。以清洁宽度 \(0.56\,\text{m}\)、自动速度 \(4\,\text{km/h}\) 估算，理论效率约为 \(2240\,\text{m}^2/\text{h}\)，与官方标称的 \(2040\,\text{m}^2/\text{h}\) 基本吻合（考虑转弯、避障等效率损失）。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 尺寸（长×宽×高） | \(1160 \times 228 \times 476\,\text{mm}\) |
| 重量（不含水） | 199 kg |
| 清洁宽度 | 560 mm |
| 吸耙宽度 | 810 mm |
| 清洁效率 | \(2040\,\text{m}^2/\text{h}\) |
| 最大速度 | \(1.2\,\text{m/s}\) |
| 自动行进速度 | \(4\,\text{km/h}\) |
| 爬坡能力 | 6% |
| 对地压力 | 27 kg |
| 刷盘单位面积压力 | \(13.2\,\text{g/cm}^2\) |
| 清水箱容积 | 70 L |
| 污水箱容积 | 50 L |
| 电池电压 / 容量 | DC 25.6 V / 100 Ah |
| 续航时间 | 4 h（洗地 3.5 h；尘推 10 h） |
| 导航方案 | 视觉 + 激光 |
| 传感器方案 | 全景单目摄像头、激光雷达、深度相机、超声波、IMU、电子防撞条 |
| 消杀接口 | 可选 |

## 应用场景

- 商业综合体、超市与写字楼
- 医院、学校等公共建筑
- 机场、高铁站、地铁站等交通枢纽
- 工厂车间与立体仓库
- 地下停车场

## 供应链关系

TN70-Pro 由汤恩智能科技（上海）有限公司研发制造。上游包括电池、电机、滚刷/吸水扒、激光雷达、深度相机、结构件与清洁剂；中游为汤恩自研的导航算法、机器人控制平台、3D-ToF 深度相机与高速单线激光雷达；下游面向物业管理公司、商业地产、工业客户与公共交通运营方。汤恩与德国卡赫（Kärcher）在供应链与产品设计上存在深度合作，并在全球建立制造基地与服务网络。

## 来源与验证

参数直接引用汤恩智能官网产品页及机器人大讲堂报道。充电时间、整机功率、噪音水平等未在公开资料中披露，标注为“未公开”。