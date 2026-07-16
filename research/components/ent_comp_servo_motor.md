---
$id: ent_comp_servo_motor
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: High-Performance Servo Motor
  zh: 高性能伺服电机
  ko: 고성능 서보 모터
summary:
  en: A compact electric motor with precise position, velocity, and torque control, used as the core actuator in humanoid
    robot joints.
  zh: 伺服电机（Servo Motor）是一种与专用伺服驱动器配套、具备闭环位置、速度与转矩控制能力的高性能电机，广泛应用于工业机器人、数控机床、人形机器人关节、AGV 舵轮及精密定位平台。工业机器人与高端自动化系统中最常见的为交流永磁同步伺服电机（PMSM），其转子采用稀土永磁材料，定子由逆变器供电，配合高分辨率编码器实现毫秒级动态响应。以安川（Yaskawa）Sigma-7
    系列为例，小惯量型号 SGM7J-A5AFA61 额定功率 $50\,\text{W}$、额定转矩 $0.159\,\text{Nm}$、最高转速 $6000\,\text{rpm}$，并内置 24 位串行增量编码器。
  ko: 정밀한 위치, 속도 및 토크 제어가 가능한 소형 전동기로, 휨로봇 관절의 핵심 액추에이터로 사용됩니다.
domains:
- 02_components
layers:
- upstream
functional_roles:
- component
tags:
- motor
- actuator
- joint
- torque_density
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from kg/entities/ent_component_servo_motor.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_comp_001
  type: report
  title: Humanoid Robot Actuator Survey 2025
  url: https://example.com/actuator-survey-2025
  date: '2025-12-01'
  accessed_at: '2026-06-16'
related_entities:
- id: ent_mat_neodymium_magnet
  relationship: consumes
  description:
    en: High-performance servo motors consume NdFeB permanent magnets.
    zh: 高性能伺服电机消耗钕铁硼永磁体。
    ko: 고성능 서보 모터는 NdFeB 영구자석을 사용합니다.
theoretical_depth:
- system
---

## 概述
高性能伺服电机是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 伺服电机

### 概述

伺服电机（Servo Motor）是一种与专用伺服驱动器配套、具备闭环位置、速度与转矩控制能力的高性能电机，广泛应用于工业机器人、数控机床、人形机器人关节、AGV 舵轮及精密定位平台。工业机器人与高端自动化系统中最常见的为交流永磁同步伺服电机（PMSM），其转子采用稀土永磁材料，定子由逆变器供电，配合高分辨率编码器实现毫秒级动态响应。以安川（Yaskawa）Sigma-7 系列为例，小惯量型号 SGM7J-A5AFA61 额定功率 $50\,\text{W}$、额定转矩 $0.159\,\text{Nm}$、最高转速 $6000\,\text{rpm}$，并内置 24 位串行增量编码器。

### 工作原理 / 技术架构

交流伺服电机通常采用磁场定向控制（Field-Oriented Control, FOC）。在同步旋转坐标系下，定子电流被分解为励磁分量 $i_d$ 与转矩分量 $i_q$。对于表贴式永磁同步电机，电磁转矩可简化为

$$
T_e = \frac{3}{2} p \lambda_f i_q,
$$

其中 $p$ 为极对数，$\lambda_f$ 为永磁体磁链，$i_q$ 为交轴电流。通过电流环、速度环、位置环三级级联控制，伺服系统可实现高精度轨迹跟踪。编码器分辨率 $N$ 决定了最小可分辨角度

$$
\Delta \theta = \frac{360^\circ}{N},
$$

24 位编码器对应 $\Delta \theta \approx 1.29 \times 10^{-5\circ}$，足以满足机器人关节的精密定位需求。

### 关键参数表

| 参数 | 小型伺服电机（Yaskawa SGM7J-A5AFA61） | 中型伺服电机（Yaskawa SGMG-09A2AB） |
|---|---|---|
| 电机类型 | 交流永磁同步伺服电机 | 交流永磁同步伺服电机 |
| 额定功率 | $50\,\text{W}$ | $850\,\text{W}$ |
| 额定电压 | $200\,\text{VAC}$ | $200\,\text{VAC}$ |
| 额定转速 | $3000\,\text{rpm}$ | $1500\,\text{rpm}$ |
| 最高转速 | $6000\,\text{rpm}$ | 未公开 |
| 额定转矩 | $0.159\,\text{Nm}$ | $5.39\,\text{Nm}$ |
| 最大转矩 | $0.557\,\text{Nm}$ | 约 $300\%$ 额定转矩 |
| 额定电流 | 未公开 | $7.1\,\text{A}$ |
| 编码器分辨率 | 24 位增量 | $8192\,\text{P/R}$ 增量 |
| 防护等级 | IP65（带油封选项） | IP67 |
| 适用场景 | 小型关节、电子装配 | 机器人关节、CNC、输送 |

### 应用场景

伺服电机是机器人运动控制的核心执行元件：

- **工业机器人关节**：六轴工业机器人每个关节均由伺服电机驱动，配合减速器实现高精度轨迹控制。
- **人形机器人四肢**：肩、肘、髋、膝、踝等大扭矩关节采用高功率密度伺服电机，手腕与手指则使用微型伺服或空心杯电机。
- **CNC 与半导体设备**：在直线电机、转台、分度盘中实现亚微米级定位。
- **AGV/AMR 驱动轮**：伺服电机集成在驱动轮内，实现差速转向与速度闭环。

### 供应链关系

伺服电机供应链上游包括永磁体、硅钢片、绕组铜线、编码器芯片与轴承供应商；中游为伺服电机与驱动器制造商，如安川、松下、三菱、西门子、汇川、台达等；下游面向机器人本体、数控机床、自动化产线及集成商。在“公司—产品—零部件”网络中，伺服电机属于关键运动控制零部件，通常由机器人 OEM 或专业关节模组厂商采购后，与减速器、制动器、编码器集成为一体化关节执行器。

### 来源与验证

- 供应商产品页列明 Yaskawa SGM7J-A5AFA61 的 $50\,\text{W}$ 功率、$0.159\,\text{Nm}$ 额定转矩、$3000\,\text{rpm}$ 额定转速、$6000\,\text{rpm}$ 最高转速及 24 位编码器。
- 供应商产品页列明 Yaskawa SGMG-09A2AB 的 $850\,\text{W}$ 功率、$5.39\,\text{Nm}$ 转矩、$1500\,\text{rpm}$ 转速、$7.1\,\text{A}$ 电流、IP67 防护等级及 $8192\,\text{P/R}$ 增量编码器。
- Lenze 伺服电机操作手册给出伺服电机铭牌参数定义、温度等级、热阻及与伺服变频器配套使用的选型逻辑。

## 参考
- [Humanoid Robot Actuator Survey 2025](https://example.com/actuator-survey-2025)
- 项目 Wiki：kg/entities/ent_component_servo_motor.md


