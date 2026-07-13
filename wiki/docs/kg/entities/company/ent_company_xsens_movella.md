---
id: ent_company_xsens_movella
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Xsens（思旷）/ Movella
  en: Xsens / Movella
status: active
sources:
- id: src_ent_company_xsens_movella_1
  type: website
  url: https://xsens.com
- id: src_ent_company_xsens_movella_2
  type: website
  url: https://movella.com
- id: src_ent_company_xsens_movella_3
  type: website
  url: https://www.macnica.com/apac/galaxy/zh_tw/products-support/technical-articles/movella-xsens-mvn-link/
- id: src_ent_company_xsens_movella_4
  type: website
  url: https://www.mouser.cn/c/sensors/motion-position-sensors/imus-inertial-measurement-units/?b=Movella%20%2F%20Xsens
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Xsens（思旷）/ Movella

## 概述

Xsens（中文常称“思旷”）是全球领先的惯性运动追踪与动作捕捉技术公司，2000 年创立于荷兰恩斯赫德，2021 年随 mCube、Xsens、Kinduct 的整合并入 Movella Holdings，品牌继续作为 Movella 旗下的专业动捕与运动分析产品线运营。其产品覆盖工业级 IMU（MTi 系列）、全身惯性动作捕捉系统（MVN Link / Awinda）与运动分析软件（MVN Analyze / Animate），广泛应用于影视、体育科学、生物力学、汽车、自动驾驶与机器人研究。

## 工作原理 / 技术架构

Xsens 的核心技术是基于 MEMS 的惯性测量单元（IMU），每个 IMU 集成三轴加速度计、三轴陀螺仪与三轴磁力计，通过传感器融合算法（扩展卡尔曼滤波或互补滤波）估计姿态、航向与运动轨迹。MTi 系列可作为 IMU（原始惯性数据）、VRU（垂直参考单元）或 AHRS（航姿参考系统）使用，输出滚转、俯仰与航向角。

姿态更新的基本微分方程为

$$
\dot{q} = \frac{1}{2} q \otimes \omega
$$

其中 $q$ 为四元数姿态，$\omega$ 为角速度矢量。陀螺仪积分提供高频姿态更新，加速度计与磁力计提供低频绝对参考，用于修正漂移。

MVN Link 全身动捕系统采用 17 颗有线 IMU 与 1 颗道具传感器，配合 23 段、22 关节生物力学模型，以最高 240 Hz 更新率输出全身运动学数据，延迟约 20 ms，无线范围约 150 m，续航约 10 小时。

MTi 600 系列工业 IMU 典型规格为 9 轴、供电 4.5–24 VDC、工作温度 −40°C 至 +85°C、带宽 500 Hz，接口支持 CAN、RS-232、UART 与 USB。

## 关键参数表

| 参数项 | 数值/描述 | 备注/来源 |
|--------|-----------|-----------|
| 公司中文名 | Xsens（思旷） | 附录 D |
| 公司英文名 | Xsens / Movella Xsens | 附录 D |
| 成立时间 | 2000 年（Xsens）；Movella 2021 年整合 | 附录 D |
| 总部 | 荷兰恩斯赫德（Xsens）；美国（Movella Holdings） | 附录 D |
| 母公司 | Movella Holdings Inc. | 附录 D |
| 产品线 | MTi 工业 IMU、MVN 动捕套装、MVN Analyze/Animate 软件 | Xsens 官网 |
| MTi 600 系列轴数 | 9 轴（加速度计/陀螺仪/磁力计） | Mouser |
| MTi 600 供电 | 4.5–24 VDC | Mouser |
| MTi 600 工作温度 | −40°C 至 +85°C | Mouser |
| MTi 600 接口 | CAN、RS-232、UART、USB | Mouser |
| MVN Link 传感器数 | 17× 有线 IMU + 1 道具传感器 | Xsens 公开规格 |
| MVN Link 更新率 | 最高 240 Hz | Xsens 公开规格 |
| MVN Link 延迟 | 约 20 ms | Xsens / Macnica |
| MVN Link 无线范围 | 约 150 m | Xsens 公开规格 |
| MVN Link 续航 | 约 10 小时 | Xsens 公开规格 |
| MVN Link 生物力学模型 | 23 段、22 关节 | Macnica |
| 价格 | 企业询价 | 未公开 |

## 应用场景

- **机器人运动验证**：为人形机器人提供全身姿态参考，采集自然人体运动数据用于模仿学习。
- **影视与游戏动画**：MVN Link 用于高保真角色动画、虚拟拍摄与实时预演。
- **体育生物力学与康复**：步态分析、伤病预防、外骨骼控制研究。
- **自动驾驶与汽车**：IMU 与 GNSS 融合定位、车辆动力学测试。

## 供应链关系

Xsens/Movella 位于传感器与动捕系统供应环节。上游为 MEMS IMU 芯片、磁力计、陀螺仪、加速度计、Lycra 弹性面料、无线射频模块与传感器融合算法 IP；下游客户包括 Electronic Arts、NBC Universal、Netflix、Daimler、Siemens、Boston Dynamics、Tesla、500 余家职业运动队及机器人公司。在知识图谱中：

- `ent_company_xsens_movella` -- `manufactures` --> `ent_product_xsens_mvn_link`
- `ent_company_xsens_movella` -- `manufactures` --> `ent_product_xsens_mvn_awinda`
- `ent_product_xsens_mvn_link` -- `used_in` --> 机器人运动验证 / 影视动画 / 体育科学

## 来源与验证

- 公司背景、产品线与供应链关系参考附录 D `company_xsens.md`。
- MVN Link 的传感器数量、更新率、延迟、无线范围与续航来自 Xsens 公开规格及 Macnica Galaxy 技术资料。
- MTi 600 系列参数来自 Mouser 产品页汇总。