---
id: ent_component_sew_psf_servo_gearmotor
schema_version: 1
type: component
'title:': SEW-EURODRIVE PS.F
domain: 02_components
theoretical_depth: system
names:
  zh: SEW-EURODRIVE PS.F
  en: SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor
status: active
sources:
- id: src_sew_eurodrive_sew_psf_servo_gearmotor_official
  type: website
  url: https://www.sew-eurodrive.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# SEW-EURODRIVE PS.F / SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [SEW-EURODRIVE（赛威传动） / SEW-EURODRIVE](../../../appendices/appendix-d/companies/company_sew_eurodrive.md) |
| **产品类别** | 行星伺服减速电机 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [SEW-EURODRIVE（赛威传动） 官网](https://www.sew-eurodrive.com) |

## 产品概述

PS.F 与 PS.C 系列是 SEW-EURODRIVE 面向伺服应用推出的低背隙行星减速电机。PS.F 采用法兰空心轴/实心轴输出，PS.C 为 B5/B14 法兰实心轴输出，二者均可与 CMP 同步伺服电机组成紧凑驱动单元。

该系列减速比从 3 到 100 覆盖常用整数比，输出扭矩最高约 4,300 N·m，防护等级可达 IP65，配合 SEW 变频器可实现高精度、高动态的位置与扭矩控制。

## 产品图片

> SEW-EURODRIVE PS.F / PS.C 行星伺服减速电机 / SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor：请访问 [官方资料](https://www.sew-eurodrive.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3:1 – 100:1（整数比、细密分级） | 产品手册 |
| 额定输出扭矩 | 最高约 4,300 N·m（系列范围） | 产品手册 |
| 输入转速 | 最高 6,000 rpm | 产品手册 |
| 背隙 | ≤3 – 6 arcmin（系列/选项） | 产品手册 |
| 防护等级 | IP65（标准/可选） | 产品手册 |
| 安装方式 | B5/B14 法兰、实心轴、键槽 | 产品手册 |
| 效率 | 单级约 97% / 双级约 94% | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[SEW-EURODRIVE（赛威传动） / SEW-EURODRIVE](../../../appendices/appendix-d/companies/company_sew_eurodrive.md)
- **核心零部件/技术来源**：CMP 同步伺服电机、行星齿轮、轴承、密封件、制动器、编码器
- **下游应用/客户**：工业机器人、人形机器人关节、AGV 轮毂驱动、包装印刷设备

## 知识图谱节点与关系

- 零部件实体：`ent_component_sew_psf_servo_gearmotor`
- 制造商实体：`ent_company_sew_eurodrive`
- 关键关系：
  - `rel_ent_company_sew_eurodrive_manufactures_ent_component_sew_psf_servo_gearmotor`（`ent_company_sew_eurodrive` --> `manufactures` --> `ent_component_sew_psf_servo_gearmotor`）

## 应用场景

- **工业机器人**：机器人底座、肩部、腕部关节驱动
- **人形机器人**：髋、膝、肩等大扭矩关节
- **数控机床**：机床进给、刀库、转台
- **其他自动化**：物流输送、食品包装、纺织机械

## 竞争对比

| 对比项 | PS.F / PS.C 行星伺服减速电机 | Lenze g500 | Bonfiglioli 300M |
|--------|------------------------|---------------|---------------|
| 核心优势 | 模块化行星+伺服电机、全球服务 | 运动控制整体方案 | 重载行星、风电经验 |
| 背隙/精度 | ≤3–6 arcmin | 低背隙可选 | 工业级背隙 |
| 价格水平 | 中高端 | 中高端 | 中高端 |
| 交付周期 | 中等 | 中等 | 中等 |

## 选购与部署建议

根据机器人关节扭矩与转速选择 PS.F 或 PS.C；注意整数减速比与编码器分辨率的匹配，高速应用需校核热功率。

## 参考资料

1. [SEW-EURODRIVE（赛威传动） 官网](https://www.sew-eurodrive.com)
2. [SEW-EURODRIVE Servo Gearmotors](https://www.sew-eurodrive.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)