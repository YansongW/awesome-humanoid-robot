---
id: ent_material_yingluohua_ndfeb_magnet
type: material
domain: 01_raw_materials
theoretical_depth: system
names:
  zh: 英洛华 烧结钕铁硼磁钢
  en: Yingluohua Sintered NdFeB Magnet
aliases:
- 英洛华 NdFeB
- Yingluohua NdFeB Magnet
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_yingluohua_official
  type: website
  url: http://www.yingluohua.com.cn
- title: 英洛华科技股份有限公司官网
- id: src_zhongke_ciye_ndfeb
  type: document
  url: https://reportdocs.static.szse.cn/UpFiles/rasinfodisc1/202302/RAS_202302_EC30057387AB4B988C3C957E8DE47125.pdf
- title: 浙江中科磁业股份有限公司首次公开发行股票并在创业板上市招股说明书（注册稿）
- id: src_bjmt_ndfeb_table
  type: website
  url: https://www.bjmt.com.cn/index.php?m=content&c=index&a=lists&catid=13
- title: 烧结钕铁硼磁性能表 | 北矿磁材
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 英洛华 烧结钕铁硼磁钢 / Yingluohua Sintered NdFeB Magnet

## 概述

英洛华科技股份有限公司是国内主要的高性能钕铁硼永磁材料生产企业之一，其烧结钕铁硼磁钢（NdFeB）属于第三代稀土永磁材料，广泛应用于新能源汽车驱动电机、风力发电机、伺服电机、机器人关节电机、消费电子与工业自动化等领域。钕铁硼磁体以 Nd₂Fe₁₄B 四方相为主晶相，具有目前商业化永磁材料中最高的最大磁能积。

## 物理化学基础

烧结钕铁硼的优异磁性能源于其晶体结构。Nd₂Fe₁₄B 相中，Nd 原子 4f 电子与 Fe 3d 电子的交换作用产生高磁晶各向异性，Fe 亚晶格提供高饱和磁化强度。其磁性能主要由三个参数表征：

- **剩磁 $B_r$**：外磁场减小到零时磁体保留的磁感应强度；
- **内禀矫顽力 $H_{cj}$**：磁体抵抗退磁的能力；
- **最大磁能积 $(BH)_{\max}$**：磁体单位体积可提供的最大磁能。

退磁曲线的第二象限可用近似直线描述：

$$
B(H) = \mu_0 H + B_r
$$

最大磁能积出现在 $(BH)_{\max} = B_r H_c / 4$ 附近（对于理想矩形退磁曲线）。实际磁体的 $(BH)_{\max}$ 与 $B_r$、$H_{cj}$ 的关系需通过实测磁滞回线确定。

英洛华公开资料可生产 N52、N42EH、N48M 等全系列牌号。以 N52 牌号为例，参考行业典型值：

$$
B_r \approx 1.42\text{–}1.48\ \text{T} \quad (14.2\text{–}14.8\ \text{kGs})
$$

$$
H_{cj} \ge 960\ \text{kA/m} \quad (12\ \text{kOe})
$$

$$
(BH)_{\max} \approx 390\text{–}422\ \text{kJ/m}^3 \quad (49\text{–}53\ \text{MGOe})
$$

中科磁业招股说明书中引用的同行业可比数据显示，英洛华烧结钕铁硼单品最高剩磁 ≥14.4 kGs、内禀矫顽力 ≥35 kOe、最大磁能积 51–55 MGOe，综合指标 $H_{cj} + (BH)_{\max}$ 约为 76。

## 关键参数表

| 参数 | 典型值/范围 | 备注 |
|------|-------------|------|
| 主晶相 | Nd₂Fe₁₄B | 四方相 |
| 剩磁 $B_r$ | ≥14.4 kGs（约 1.44 T）| 同行业可比数据 |
| 内禀矫顽力 $H_{cj}$ | ≥35 kOe（约 2790 kA/m）| 同行业可比数据 |
| 最大磁能积 $(BH)_{\max}$ | 51–55 MGOe | 同行业可比数据 |
| 综合指标 $H_{cj} + (BH)_{\max}$ | 约 76 | 中科磁业招股说明书 |
| 可生产牌号 | N52、N42EH、N48M 等 | 行业报道 |
| 中性盐雾试验 | ≥240 h | 同行业可比数据 |
| 抗弯强度 | ≥48 MPa | 同行业可比数据 |
| 密度 | 约 7.5–7.6 g/cm³ | 行业典型值 |
| 居里温度 | 约 310 ℃ | 行业典型值 |
| 最高工作温度 | 依牌号 80–240 ℃ | N 系列 80 ℃，EH 系列 200 ℃ |

## 在机器人系统中的作用

- **关节电机磁材**：人形机器人与协作机器人的无框力矩电机、伺服电机普遍采用烧结钕铁硼磁钢作为转子永磁体，其高磁能积可提升电机功率密度与扭矩密度。
- **谐波/行星减速器配套**：高性能磁材与减速器共同决定关节执行器的体积、重量与动态响应。
- **传感器与制动器**：钕铁硼磁体也用于编码器磁环、抱闸等部件。
- **能量转换效率**：高矫顽力磁体在高温、强退磁场工况下保持磁性能稳定，降低电机退磁风险。

## 供应链关系

英洛华烧结钕铁硼磁钢处于 **稀土功能材料/上游原材料层**。其上游为稀土矿采选与冶炼分离（钕、镨、镝、铽等），中游为磁粉制备、磁场取向成型、烧结、机加工与表面防护，下游覆盖新能源汽车电机、风电发电机、伺服电机、机器人关节电机与消费电子。英洛华具备年产约 12,000 吨钕铁硼产能，在机器人产业链中为人形机器人关节电机厂商提供关键磁材。

## 来源与验证

- 英洛华科技官网：http://www.yingluohua.com.cn
- 中科磁业招股说明书（含同行业可比公司磁性能指标）：https://reportdocs.static.szse.cn/UpFiles/rasinfodisc1/202302/RAS_202302_EC30057387AB4B988C3C957E8DE47125.pdf
- 北矿磁材烧结钕铁硼磁性能表：https://www.bjmt.com.cn/index.php?m=content&c=index&a=lists&catid=13

英洛华官网未公开完整产品规格书，表中具体磁性能数值引用自同行业可比公司公开资料（中科磁业招股说明书）。不同牌号、尺寸与表面处理条件下的实际参数以英洛华出厂检测报告为准。