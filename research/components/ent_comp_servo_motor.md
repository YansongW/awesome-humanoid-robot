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

## Overview
High-performance servo motors are critical components in the field of humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Servo Motor

### Overview

A servo motor is a high-performance motor paired with a dedicated servo drive, capable of closed-loop position, speed, and torque control. It is widely used in industrial robots, CNC machine tools, humanoid robot joints, AGV steering wheels, and precision positioning platforms. The most common type in industrial robots and high-end automation systems is the AC permanent magnet synchronous servo motor (PMSM). Its rotor uses rare-earth permanent magnet materials, the stator is powered by an inverter, and it works with a high-resolution encoder to achieve millisecond-level dynamic response. Taking the Yaskawa Sigma-7 series as an example, the low-inertia model SGM7J-A5AFA61 has a rated power of $50\,\text{W}$, a rated torque of $0.159\,\text{Nm}$, a maximum speed of $6000\,\text{rpm}$, and a built-in 24-bit serial incremental encoder.

### Working Principle / Technical Architecture

AC servo motors typically use Field-Oriented Control (FOC). In the synchronous rotating coordinate system, the stator current is decomposed into the excitation component $i_d$ and the torque component $i_q$. For a surface-mounted permanent magnet synchronous motor, the electromagnetic torque can be simplified as

$$
T_e = \frac{3}{2} p \lambda_f i_q,
$$

where $p$ is the number of pole pairs, $\lambda_f$ is the permanent magnet flux linkage, and $i_q$ is the quadrature-axis current. Through a three-level cascade control of current loop, speed loop, and position loop, the servo system can achieve high-precision trajectory tracking. The encoder resolution $N$ determines the minimum resolvable angle

$$
\Delta \theta = \frac{360^\circ}{N},
$$

A 24-bit encoder corresponds to $\Delta \theta \approx 1.29 \times 10^{-5\circ}$, which is sufficient for the precision positioning needs of robot joints.

### Key Parameter Table

| Parameter | Small Servo Motor (Yaskawa SGM7J-A5AFA61) | Medium Servo Motor (Yaskawa SGMG-09A2AB) |
|---|---|---|
| Motor Type | AC Permanent Magnet Synchronous Servo Motor | AC Permanent Magnet Synchronous Servo Motor |
| Rated Power | $50\,\text{W}$ | $850\,\text{W}$ |
| Rated Voltage | $200\,\text{VAC}$ | $200\,\text{VAC}$ |
| Rated Speed | $3000\,\text{rpm}$ | $1500\,\text{rpm}$ |
| Maximum Speed | $6000\,\text{rpm}$ | Not disclosed |
| Rated Torque | $0.159\,\text{Nm}$ | $5.39\,\text{Nm}$ |
| Maximum Torque | $0.557\,\text{Nm}$ | Approx. $300\%$ of rated torque |
| Rated Current | Not disclosed | $7.1\,\text{A}$ |
| Encoder Resolution | 24-bit incremental | $8192\,\text{P/R}$ incremental |
| Protection Rating | IP65 (with oil seal option) | IP67 |
| Application Scenarios | Small joints, electronic assembly | Robot joints, CNC, conveyors |

### Application Scenarios

Servo motors are the core actuation components in robot motion control:

- **Industrial Robot Joints**: Each joint of a six-axis industrial robot is driven by a servo motor, working with a reducer to achieve high-precision trajectory control.
- **Humanoid Robot Limbs**: High-torque joints such as shoulders, elbows, hips, knees, and ankles use high-power-density servo motors, while wrists and fingers use micro servo or coreless motors.
- **CNC and Semiconductor Equipment**: Achieve sub-micron positioning in linear motors, rotary tables, and indexing heads.
- **AGV/AMR Drive Wheels**: Servo motors are integrated into drive wheels to enable differential steering and speed closed-loop control.

### Supply Chain Relationships

The upstream of the servo motor supply chain includes suppliers of permanent magnets, silicon steel sheets, winding copper wires, encoder chips, and bearings; the midstream consists of servo motor and drive manufacturers such as Yaskawa, Panasonic, Mitsubishi, Siemens, Inovance, and Delta; the downstream targets robot bodies, CNC machine tools, automation production lines, and integrators. In the "Company-Product-Component" network, servo motors are key motion control components, typically purchased by robot OEMs or specialized joint module manufacturers and integrated with reducers, brakes, and encoders into integrated joint actuators.

### Sources and Verification

- The supplier product page lists the Yaskawa SGM7J-A5AFA61 with $50\,\text{W}$ power, $0.159\,\text{Nm}$ rated torque, $3000\,\text{rpm}$ rated speed, $6000\,\text{rpm}$ maximum speed, and a 24-bit encoder.
- The supplier product page lists the Yaskawa SGMG-09A2AB with $850\,\text{W}$ power, $5.39\,\text{Nm}$ torque, $1500\,\text{rpm}$ speed, $7.1\,\text{A}$ current, IP67 protection rating, and $8192\,\text{P/R}$ incremental encoder.
- The Lenze servo motor operation manual provides definitions of servo motor nameplate parameters, temperature classes, thermal resistance, and selection logic for use with servo drives.

## 개요
고성능 서보 모터는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## 서보 모터

### 개요

서보 모터(Servo Motor)는 전용 서보 드라이버와 함께 사용되며, 폐루프 위치, 속도 및 토크 제어 기능을 갖춘 고성능 모터입니다. 산업용 로봇, CNC 공작기계, 휴머노이드 로봇 관절, AGV 조향 휠 및 정밀 위치 결정 플랫폼에 널리 사용됩니다. 산업용 로봇과 고급 자동화 시스템에서 가장 흔한 것은 교류 영구자석 동기 서보 모터(PMSM)로, 회전자는 희토류 영구자석 재료를 사용하고, 고정자는 인버터로 전원을 공급받으며, 고분해능 엔코더와 함께 밀리초 단위의 동적 응답을 구현합니다. Yaskawa Sigma-7 시리즈를 예로 들면, 소형 관성 모델 SGM7J-A5AFA61의 정격 출력은 $50\,\text{W}$, 정격 토크는 $0.159\,\text{Nm}$, 최고 회전수는 $6000\,\text{rpm}$이며, 24비트 직렬 증분 엔코더가 내장되어 있습니다.

### 작동 원리 / 기술 아키텍처

교류 서보 모터는 일반적으로 자속 기준 제어(Field-Oriented Control, FOC)를 사용합니다. 동기 회전 좌표계에서 고정자 전류는 여자 성분 $i_d$와 토크 성분 $i_q$로 분해됩니다. 표면 부착형 영구자석 동기 모터의 경우, 전자기 토크는 다음과 같이 단순화됩니다.

$$
T_e = \frac{3}{2} p \lambda_f i_q,
$$

여기서 $p$는 극 쌍수, $\lambda_f$는 영구자석 자속, $i_q$는 직교축 전류입니다. 전류 루프, 속도 루프, 위치 루프의 3단계 종속 제어를 통해 서보 시스템은 고정밀 궤적 추종을 구현할 수 있습니다. 엔코더 분해능 $N$은 최소 분해 가능 각도를 결정합니다.

$$
\Delta \theta = \frac{360^\circ}{N},
$$

24비트 엔코더는 $\Delta \theta \approx 1.29 \times 10^{-5\circ}$에 해당하며, 로봇 관절의 정밀 위치 결정 요구 사항을 충족하기에 충분합니다.

### 주요 파라미터 표

| 파라미터 | 소형 서보 모터 (Yaskawa SGM7J-A5AFA61) | 중형 서보 모터 (Yaskawa SGMG-09A2AB) |
|---|---|---|
| 모터 유형 | 교류 영구자석 동기 서보 모터 | 교류 영구자석 동기 서보 모터 |
| 정격 출력 | $50\,\text{W}$ | $850\,\text{W}$ |
| 정격 전압 | $200\,\text{VAC}$ | $200\,\text{VAC}$ |
| 정격 회전수 | $3000\,\text{rpm}$ | $1500\,\text{rpm}$ |
| 최고 회전수 | $6000\,\text{rpm}$ | 미공개 |
| 정격 토크 | $0.159\,\text{Nm}$ | $5.39\,\text{Nm}$ |
| 최대 토크 | $0.557\,\text{Nm}$ | 약 $300\%$ 정격 토크 |
| 정격 전류 | 미공개 | $7.1\,\text{A}$ |
| 엔코더 분해능 | 24비트 증분 | $8192\,\text{P/R}$ 증분 |
| 보호 등급 | IP65 (오일 씰 옵션 포함) | IP67 |
| 적용 분야 | 소형 관절, 전자 조립 | 로봇 관절, CNC, 컨베이어 |

### 적용 분야

서보 모터는 로봇 운동 제어의 핵심 실행 요소입니다.

- **산업용 로봇 관절**: 6축 산업용 로봇의 각 관절은 서보 모터로 구동되며, 감속기와 함께 고정밀 궤적 제어를 구현합니다.
- **휴머노이드 로봇 사지**: 어깨, 팔꿈치, 엉덩이, 무릎, 발목 등 고토크 관절은 고출력 밀도 서보 모터를 사용하고, 손목과 손가락은 초소형 서보 모터 또는 코어리스 모터를 사용합니다.
- **CNC 및 반도체 장비**: 리니어 모터, 회전 테이블, 인덱스 테이블에서 서브마이크로미터 수준의 위치 결정을 구현합니다.
- **AGV/AMR 구동 휠**: 서보 모터가 구동 휠 내에 통합되어 차동 조향과 속도 폐루프를 구현합니다.

### 공급망 관계

서보 모터 공급망의 상류에는 영구자석, 규소 강판, 권선 동선, 엔코더 칩 및 베어링 공급업체가 포함됩니다. 중류는 서보 모터 및 드라이버 제조업체로, Yaskawa, Panasonic, Mitsubishi, Siemens, Inovance, Delta 등이 있습니다. 하류는 로봇 본체, CNC 공작기계, 자동화 생산 라인 및 시스템 통합 업체를 대상으로 합니다. "회사-제품-부품" 네트워크에서 서보 모터는 핵심 운동 제어 부품에 속하며, 일반적으로 로봇 OEM 또는 전문 관절 모듈 업체가 구매하여 감속기, 브레이크, 엔코더와 통합된 일체형 관절 액추에이터로 조립됩니다.

### 출처 및 검증

- 공급업체 제품 페이지에는 Yaskawa SGM7J-A5AFA61의 $50\,\text{W}$ 출력, $0.159\,\text{Nm}$ 정격 토크, $3000\,\text{rpm}$ 정격 회전수, $6000\,\text{rpm}$ 최고 회전수 및 24비트 엔코더가 명시되어 있습니다.
- 공급업체 제품 페이지에는 Yaskawa SGMG-09A2AB의 $850\,\text{W}$ 출력, $5.39\,\text{Nm}$ 토크, $1500\,\text{rpm}$ 회전수, $7.1\,\text{A}$ 전류, IP67 보호 등급 및 $8192\,\text{P/R}$ 증분 엔코더가 명시되어 있습니다.
- Lenze 서보 모터 작동 매뉴얼에는 서보 모터 명판 파라미터 정의, 온도 등급, 열 저항 및 서보 인버터와 함께 사용하기 위한 선정 로직이 제공됩니다.
