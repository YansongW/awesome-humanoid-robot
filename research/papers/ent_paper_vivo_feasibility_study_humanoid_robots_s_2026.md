---
$id: ent_paper_vivo_feasibility_study_humanoid_robots_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: In vivo feasibility study of humanoid robots in surgery
  zh: In vivo feasibility study of humanoid robots in surgery
  ko: In vivo feasibility study of humanoid robots in surgery
summary:
  en: Recent advances in actuation, control and learning have rapidly pushed humanoid robots from a distant vision towards
    near-term real-world deployment. Healthcare is a particularly pressing domain, in which staffing shortages and increasing
    care demand are widening the gap between clinical workload and available skilled labour. Although current automation has
    largely focused on digital and.
  zh: 本文首次系统评估了当代人形机器人在腹腔镜手术中的可行性，由加州大学圣迭戈分校团队完成。作者开发了一套基于Unitree G1人形机器人的遥操作框架，通过虚拟远程运动中心（RCM）约束和逆映射控制算法，使用通用腕式器械完成了台架实验、干实验室用户研究以及两例活体猪胆囊切除术。核心贡献在于证明了人形机器人在体内手术中的技术可行性，同时定量揭示了其与达芬奇系统在延迟、工作空间和精度上的差距。
  ko: Recent advances in actuation, control and learning have rapidly pushed humanoid robots from a distant vision towards
    near-term real-world deployment. Healthcare is a particularly pressing domain, in which staffing shortages and increasing
    care demand are widening the gap between clinical workload and available skilled labour. Although current automation has
    largely focused on digital and.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- vivo
- feasibility
- study
- humanoid
- robots
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.07972 In vivo feasibility study of humanoid robots in surgery
  url: https://arxiv.org/abs/2607.07972
  date: '2026-07-08'
  accessed_at: '2026-08-05'
---

## 概述

本文首次系统评估了当代人形机器人在腹腔镜手术中的可行性，由加州大学圣迭戈分校团队完成。作者开发了一套基于Unitree G1人形机器人的遥操作框架，通过虚拟远程运动中心（RCM）约束和逆映射控制算法，使用通用腕式器械完成了台架实验、干实验室用户研究以及两例活体猪胆囊切除术。核心贡献在于证明了人形机器人在体内手术中的技术可行性，同时定量揭示了其与达芬奇系统在延迟、工作空间和精度上的差距。

## 它改变了什么

手术机器人领域长期被达芬奇这类专用平台垄断，其高购置成本、专有耗材和封闭架构限制了机器人手术向资源不足的医疗中心普及。本文真正改变的是将“通用人形机器人”这一非专用平台推入手术场景的讨论范畴——它不再只是概念验证，而是通过体内猪模型手术证明了这类平台至少能完成标准腹腔镜胆囊切除术。这打破了手术机器人必须从零定制设计的隐含假设，为低成本、可扩展的机器人手术方案开辟了可能性。

但更重要的是，本文没有停留在“能做”的层面，而是用定量数据划出了一条清醒的边界：人形机器人在控制延迟、工作空间可达性和精度上仍与达芬奇系统存在显著差距。这种“可行性证明+差距量化”的双重输出，让临床社区能基于事实判断人形机器人距离手术室落地还有多远，而不是被概念演示所迷惑。

## 方法拆解

### 系统架构
- 移动操作控制台包含两个主操作器（MTM）模块、脚踏板（控制器械进出离合器）、GOOVIS G3 Max立体头戴显示器，以及运行ROS2网络通信的控制工作站。
- 执行端为Unitree G1人形机器人，使用LivsMed ArtiSential非驱动腕式腹腔镜器械，通过定制安装座与人形手部接口，保留完整腕部关节活动度。

### 逆映射控制算法
- 器械被动几何用θ₁、θ₂（手柄相对角度）和θ₃、θ₄（工具尖端关节角度）参数化，其中θ₃ = kθ₁，θ₄ = kθ₂，传动比k = 2。
- 给定目标工具尖端位姿和RCM位置，通过最小化加权残差求解手柄位姿，残差包含位姿失配和被动角度惩罚项；θ_max设为45度，使用Trust-Region Reflective算法配合线性损失函数求解。

### RCM约束与校准
- 与达芬奇机械固定的RCM不同，人形平台创建虚拟RCM，通过机器人头部摄像头检测ArUco标记定位。
- 实际RCM位置因动物呼吸和机器人基座漂移而动态变化，采用时间滤波器处理估计值，大漂移时暂停手术重新校准。

### 运动精度评估
- 直线运动：使用PCA拟合最佳直线，报告垂直偏差RMS。
- 圆形运动：投影到最佳拟合平面，通过最小二乘估计圆心，报告径向偏差RMS和平面外偏差RMS。

### 用户研究设计
- 环转移任务：18名参与者（6名外科医生、12名新手），每人6次试验，四桩间距40 mm。
- FLS peg转移：13名医学培训参与者（8名初级、5名高级），传统300秒时间限制。
- 平衡FLS评分：S = 100(1 - (w·t' + (1-w)·e'))，w = 0.5，采用最小-最大归一化。

## 关键创新

**首次人形机器人体内手术**：本文完成了两例活体猪胆囊切除术，这是人形机器人在体内手术场景的首次报道。此前人形机器人在医疗领域的研究多限于台架或模拟环境，本文将其推进到活体动物模型，验证了在真实生理条件（呼吸运动、组织牵拉）下的操作可行性。

**虚拟RCM约束下的通用器械控制**：不同于达芬奇依赖机械RCM结构，本文通过视觉标记检测和逆映射算法实现虚拟RCM，使通用非驱动腕式器械能被人形机器人精确操控。这一设计决策的意义在于摆脱了对专用手术器械的依赖，为使用低成本、FDA批准的通用器械铺平了道路。

**差距量化的方法论贡献**：本文不仅展示了人形机器人的能力，还通过配对统计（如人形-dVRK加权误差Δ = -0.06 [-1.35, 1.23]，p = 0.922）和FLS评分对比，系统量化了其与达芬奇系统的差距。这种“可行性+差距”的双重输出为后续研究提供了可复现的评估框架。

## 实验与结果

### 台架实验
- 系统延迟：跟随者-领导者延迟约156 ms（120 FPS外部相机测量），控制回路延迟约24 ms，其中逆运动学计算每周期约11 ms。
- 运动精度：直线运动在约94 mm长度上实现1.30 ± 0.03 mm RMS正交偏差；圆形运动从命令的80 mm直径表现出10.40 ± 1.32 mm RMS径向偏差，离面误差1.23 ± 0.14 mm RMS。

### 环转移任务（总体，n=18）
| 平台 | 完成时间 (s) | 加权误差 |
|------|-------------|---------|
| 手动 | 64.22 ± 31.82 | 7.03 ± 4.88 |
| 人形 | 74.67 ± 39.22 | 4.53 ± 3.14 |
| dVRK | 43.01 ± 15.25 | 4.59 ± 2.53 |

配对统计显示：人形-手动加权误差Δ = -2.50 [-4.42, -0.58]，p = 0.014，d_z = 0.65；人形-dVRK加权误差Δ = -0.06 [-1.35, 1.23]，p = 0.922，d_z = 0.02。人形在误差上显著优于手动且与dVRK无显著差异，但时间显著慢于dVRK（Δ = 31.65 [17.22, 46.09]，p = 2.41e-04）。

### FLS peg转移（总体，n=13）
| 平台 | 完成时间 (s) | 总误差 | FLS评分 |
|------|-------------|--------|---------|
| 手动 | 877.8 ± 774.3 | 17.45 ± 16.80 | 70.47 ± 27.53 |
| 人形 | 560.1 ± 595.5 | 6.25 ± 6.36 | 85.39 ± 16.25 |
| da Vinci Xi | 118.2 ± 56.7 | 1.33 ± 1.23 | 97.67 ± 1.54 |

人形显著快于手动（Δ = -290.45 [-526.92, -53.98]，p = 0.021）且误差更低，但da Vinci Xi在时间和误差上均显著优于人形（时间Δ = -467.27 [-850.44, -84.10]，p = 9.77e-04）。

### 体内猪研究
两例胆囊切除术均完成，无中转开放手术。第二例手术时间从56:15缩短至31:59（由表内数值计算），机器人部署次数从8次降至4次（由表内数值计算），显示学习效应。

## 边界与局限

**校准敏感性**：商业器械未公开文档化，扩展运动链几何参数需手动测量，引入潜在校准误差；RCM控制对套管针定位精度高度敏感，ArUco检测小误差可沿运动链放大。

**工作空间受限**：人形机器人手臂跨度约450 mm，远小于成年人类的1.6-1.8 m，在干实验室环境中尤为明显，导致频繁重新定位。

**无菌挑战**：手套覆盖策略不能完全复制人类手术无菌工作流；当前商用人体形系统缺乏可高压灭菌组件，保持无菌仍是关键障碍。

**性能差距**：人形平台在FLS peg转移中仍明显慢于且不如da Vinci Xi准确；参与者报告延迟引入的控制反馈响应降低、控制界面不够直观。

**未做之事**：未评估更广泛手术类型、延长手术持续时间或更自主任务；未建立完全无菌集成的稳健协议；未使用开源腹腔镜器械。

## 工程启示

**复现优先核对**：先确认器械几何参数（θ₁-θ₄、传动比k = 2）的测量精度，这是逆映射控制的基础；RCM校准的ArUco标记检测误差会沿运动链放大，建议在套管针方向校准上投入更多验证。

**延迟预算**：系统延迟约156 ms中，逆运动学计算每周期约11 ms，控制回路约24 ms。若下游团队需要更低延迟，优先优化IK求解器（当前使用TRF算法）而非网络通信。

**最易踩坑**：RCM动态处理——动物呼吸和机器人基座漂移会导致RCM位置变化，时间滤波器虽能防止不安全扰动，但大漂移时需暂停手术重新校准。建议在实验前充分测试滤波参数，避免术中频繁中断。

**选型参考**：人形平台在环转移任务中误差与dVRK无显著差异（p = 0.922），但FLS peg转移中时间差距显著（Δ = -467.27 s）。若任务侧重精度而非速度，人形机器人可作为低成本替代方案；若需高吞吐量，达芬奇系统仍占优。

## Overview
Recent advances in actuation, control and learning have rapidly pushed humanoid robots from a distant vision towards near-term real-world deployment. Healthcare is a particularly pressing domain, in which staffing shortages and increasing care demand are widening the gap between clinical workload and available skilled labour. Although current automation has largely focused on digital and logistical tasks, much hospital work remains embodied, requiring mobility, manipulation and safe interaction in human-designed environments. Humanoid form factors offer unique potential, particularly for assisting with surgical tasks. Traditionally, robotic systems for surgery are purpose-built platforms such as Intuitive Surgical's da Vinci Surgical System, and it remains unclear how close current humanoid systems are to meeting the precision, control and safety requirements of minimally invasive surgery. Here we present a systematic evaluation of contemporary humanoid technology for laparoscopic surgical tasks. We develop a humanoid-based laparoscopic teleoperation framework using general-purpose instruments and assess its abilities through benchtop characterization, dry-laboratory user studies spanning diverse surgical experience levels and in vivo porcine studies. Across these evaluations, we quantify technical feasibility, task performance and clinical readiness relative to established surgical platforms. Together, our study provides an evidence-based assessment of current humanoid abilities and limitations for surgical applications, highlighting both their promise and key technical challenges that must be addressed before clinical deployment.

## 参考
- https://arxiv.org/abs/2607.07972

## 개요

본 논문은 캘리포니아 대학교 샌디에고 팀이 수행한, 현대 휴머노이드 로봇의 복강경 수술에서의 실행 가능성을 최초로 체계적으로 평가한 연구이다. 저자들은 Unitree G1 휴머노이드 로봇 기반의 원격 조작 프레임워크를 개발했으며, 가상 원격 중심점(RCM) 제약 및 역매핑 제어 알고리즘을 통해 범용 손목형 기기를 사용하여 벤치 실험, 건식 실험실 사용자 연구, 그리고 두 건의 생체 돼지 담낭 절제술을 완료했다. 핵심 기여는 휴머노이드 로봇의 체내 수술 기술적 실행 가능성을 입증하는 동시에, 다빈치 시스템과의 지연 시간, 작업 공간, 정밀도 격차를 정량적으로 규명한 것이다.

## 그것이 바꾼 것

수술 로봇 분야는 오랫동안 다빈치와 같은 전용 플랫폼이 독점해 왔으며, 높은 도입 비용, 독점 소모품, 폐쇄적 아키텍처는 로봇 수술이 자원이 부족한 의료 센터로 확산되는 것을 제한해 왔다. 본 논문이 실제로 바꾼 것은 '범용 휴머노이드 로봇'이라는 비전용 플랫폼을 수술 시나리오 논의 범주로 끌어올린 것이다. 이는 더 이상 개념 검증에 그치지 않고, 체내 돼지 모델 수술을 통해 이러한 플랫폼이 최소한 표준 복강경 담낭 절제술을 수행할 수 있음을 입증했다. 이는 수술 로봇이 반드시 처음부터 맞춤 설계되어야 한다는 암묵적 가정을 깨고, 저비용·확장 가능한 로봇 수술 솔루션의 가능성을 열었다.

하지만 더 중요한 것은, 본 논문이 '할 수 있다'는 수준에 머물지 않고 정량적 데이터로 냉철한 경계선을 그었다는 점이다. 휴머노이드 로봇은 제어 지연, 작업 공간 도달성, 정밀도에서 여전히 다빈치 시스템과 상당한 격차를 보인다. 이러한 '실행 가능성 입증 + 격차 정량화'의 이중 출력은 임상 커뮤니티가 개념 시연에 현혹되지 않고 사실에 기반하여 휴머노이드 로봇이 수술실 적용까지 얼마나 남았는지 판단할 수 있게 한다.

## 방법 분석

### 시스템 아키텍처
- 이동형 조작 콘솔은 두 개의 마스터 조작기(MTM) 모듈, 풋페달(기기 삽입/인출 클러치 제어), GOOVIS G3 Max 입체 헤드마운트 디스플레이, 그리고 ROS2 네트워크 통신을 실행하는 제어 워크스테이션으로 구성된다.
- 실행부는 Unitree G1 휴머노이드 로봇이며, LivsMed ArtiSential 비구동 손목형 복강경 기기를 맞춤형 마운트를 통해 휴머노이드 손과 인터페이스하여 완전한 손목 관절 운동 범위를 유지한다.

### 역매핑 제어 알고리즘
- 기기의 수동 기하학은 θ₁, θ₂(핸들 상대 각도) 및 θ₃, θ₄(도구 팁 관절 각도)로 매개변수화되며, 여기서 θ₃ = kθ₁, θ₄ = kθ₂, 전달비 k = 2이다.
- 목표 도구 팁 자세와 RCM 위치가 주어지면, 가중 잔차(자세 불일치 및 수동 각도 페널티 항 포함)를 최소화하여 핸들 자세를 해결한다. θ_max는 45도로 설정되며, Trust-Region Reflective 알고리즘과 선형 손실 함수를 사용하여 해를 구한다.

### RCM 제약 및 캘리브레이션
- 다빈치의 기계적 고정 RCM과 달리, 휴머노이드 플랫폼은 로봇 헤드 카메라가 ArUco 마커를 감지하여 위치를 파악하는 가상 RCM을 생성한다.
- 실제 RCM 위치는 동물 호흡과 로봇 베이스 드리프트로 인해 동적으로 변하며, 시간 필터로 추정치를 처리하고 큰 드리프트 발생 시 수술을 일시 중지하고 재캘리브레이션한다.

### 운동 정밀도 평가
- 직선 운동: PCA로 최적 직선을 피팅하고 수직 편차 RMS를 보고.
- 원형 운동: 최적 피팅 평면에 투영하고 최소제곱법으로 원심을 추정하여 반경 편차 RMS 및 평면 외 편차 RMS를 보고.

### 사용자 연구 설계
- 링 이동 과제: 18명의 참가자(외과의 6명, 초보자 12명), 각 6회 시행, 4개 페그 간격 40 mm.
- FLS 페그 이동: 13명의 의학 훈련 참가자(초급 8명, 고급 5명), 기존 300초 시간 제한.
- 균형 FLS 점수: S = 100(1 - (w·t' + (1-w)·e')), w = 0.5, 최소-최대 정규화 사용.

## 핵심 혁신

**최초의 휴머노이드 로봇 체내 수술**: 본 논문은 두 건의 생체 돼지 담낭 절제술을 완료했으며, 이는 휴머노이드 로봇의 체내 수술 시나리오 최초 보고이다. 이전 휴머노이드 로봇의 의료 분야 연구는 대부분 벤치 또는 시뮬레이션 환경에 국한되었으나, 본 논문은 이를 생체 동물 모델로 확장하여 실제 생리 조건(호흡 운동, 조직 견인)에서의 조작 실행 가능성을 검증했다.

**가상 RCM 제약 하의 범용 기기 제어**: 다빈치가 기계적 RCM 구조에 의존하는 것과 달리, 본 논문은 시각 마커 감지와 역매핑 알고리즘을 통해 가상 RCM을 구현하여 범용 비구동 손목형 기기를 휴머노이드 로봇이 정밀하게 조작할 수 있게 했다. 이 설계 결정의 의의는 전용 수술 기기에 대한 의존성을 제거하고, 저비용·FDA 승인 범용 기기 사용의 길을 열었다는 점이다.

**격차 정량화의 방법론적 기여**: 본 논문은 휴머노이드 로봇의 능력을 보여줄 뿐만 아니라, 짝지은 통계(예: 휴머노이드-dVRK 가중 오차 Δ = -0.06 [-1.35, 1.23], p = 0.922) 및 FLS 점수 비교를 통해 다빈치 시스템과의 격차를 체계적으로 정량화했다. 이러한 '실행 가능성 + 격차'의 이중 출력은 후속 연구를 위한 재현 가능한 평가 프레임워크를 제공한다.

## 실험 및 결과

### 벤치 실험
- 시스템 지연: 팔로워-리더 지연 약 156 ms(120 FPS 외부 카메라 측정), 제어 루프 지연 약 24 ms, 그중 역운동학 계산은 주기당 약 11 ms.
- 운동 정밀도: 직선 운동은 약 94 mm 길이에서 1.30 ± 0.03 mm RMS 직교 편차 달성; 원형 운동은 명령된 80 mm 직경에서 10.40 ± 1.32 mm RMS 반경 편차, 평면 외 오차 1.23 ± 0.14 mm RMS를 나타냄.

### 링 이동 과제(전체, n=18)
| 플랫폼 | 완료 시간 (s) | 가중 오차 |
|------|-------------|---------|
| 수동 | 64.22 ± 31.82 | 7.03 ± 4.88 |
| 휴머노이드 | 74.67 ± 39.22 | 4.53 ± 3.14 |
| dVRK | 43.01 ± 15.25 | 4.59 ± 2.53 |

짝지은 통계: 휴머노이드-수동 가중 오차 Δ = -2.50 [-4.42, -0.58], p = 0.014, d_z = 0.65; 휴머노이드-dVRK 가중 오차 Δ = -0.06 [-1.35, 1.23], p = 0.922, d_z = 0.02. 휴머노이드는 오차에서 수동보다 유의하게 우수했고 dVRK와 유의한 차이가 없었으나, 시간은 dVRK보다 유의하게 느렸다(Δ = 31.65 [17.22, 46.09], p = 2.41e-04).

### FLS 페그 이동(전체, n=13)
| 플랫폼 | 완료 시간 (s) | 총 오차 | FLS 점수 |
|------|-------------|--------|---------|
| 수동 | 877.8 ± 774.3 | 17.45 ± 16.80 | 70.47 ± 27.53 |
| 휴머노이드 | 560.1 ± 595.5 | 6.25 ± 6.36 | 85.39 ± 16.25 |
| da Vinci Xi | 118.2 ± 56.7 | 1.33 ± 1.23 | 97.67 ± 1.54 |

휴머노이드는 수동보다 유의하게 빨랐고(Δ = -290.45 [-526.92, -53.98], p = 0.021) 오차도 낮았지만, da Vinci Xi는 시간과 오차 모두에서 휴머노이드보다 유의하게 우수했다(시간 Δ = -467.27 [-850.44, -84.10], p = 9.77e-04).

### 생체 돼지 연구
두 건의 담낭 절제술 모두 개복 수술 전환 없이 완료되었다. 두 번째 수술 시간은 56:15에서 31:59로 단축되었고(표 내 수치로 계산), 로봇 배치 횟수는 8회에서 4회로 감소하여(표 내 수치로 계산) 학습 효과를 보여주었다.

## 경계 및 한계

**캘리브레이션 민감성**: 상용 기기는 문서화되지 않아 확장 운동 사슬 기하학 매개변수를 수동 측정해야 하며, 잠재적 캘리브레이션 오차가 발생한다. RCM 제어는 트로카 위치 결정 정밀도에 매우 민감하며, ArUco 감지의 작은 오차가 운동 사슬을 따라 증폭될 수 있다.

**작업 공간 제한**: 휴머노이드 로봇 팔의 작업 범위는 약 450 mm로 성인 인간의 1.6-1.8 m보다 훨씬 작아 건식 실험실 환경에서 특히 두드러지며, 잦은 재배치가 필요하다.

**무균 문제**: 장갑 커버링 전략은 인간 수술의 무균 작업 흐름을 완전히 복제할 수 없다. 현재 상용 휴머노이드 시스템은 고압멸균 가능한 부품이 부족하여 무균 유지가 여전히 핵심 장애물이다.

**성능 격차**: 휴머노이드 플랫폼은 FLS 페그 이동에서 여전히 da Vinci Xi보다 현저히 느리고 정확도도 낮다. 참가자들은 지연으로 인한 제어 피드백 응답 저하와 제어 인터페이스의 비직관성을 보고했다.

**수행하지 않은 것**: 더 광범위한 수술 유형, 장시간 수술 지속 또는 더 자율적인 작업은 평가하지 않았다. 완전한 무균 통합을 위한 견고한 프로토콜은 구축하지 않았다. 오픈소스 복강경 기기도 사용하지 않았다.

## 공학적 시사점

**재현 우선 확인 사항**: 먼저 기기 기하학 매개변수(θ₁-θ₄, 전달비 k = 2)의 측정 정밀도를 확인해야 하며, 이는 역매핑 제어의 기초이다. RCM 캘리브레이션의 ArUco 마커 감지 오차는 운동 사슬을 따라 증폭되므로, 트로카 방향 캘리브레이션에 더 많은 검증을 투자할 것을 권장한다.

**지연 예산**: 시스템 지연 약 156 ms 중 역운동학 계산은 주기당 약 11 ms, 제어 루프는 약 24 ms이다. 하위 팀이 더 낮은 지연이 필요하다면 네트워크 통신보다 IK 솔버(현재 TRF 알고리즘 사용) 최적화를 우선시하라.

**가장 빠지기 쉬운 함정**: RCM 동적 처리 — 동물 호흡과 로봇 베이스 드리프트는 RCM 위치 변화를 유발하며, 시간 필터가 안전하지 않은 교란을 방지하지만 큰 드리프트 시 수술을 일시 중지하고 재캘리브레이션해야 한다. 실험 전에 필터 매개변수를 충분히 테스트하여 수술 중 잦은 중단을 피할 것을 권장한다.

**선정 참고 사항**: 휴머노이드 플랫폼은 링 이동 과제에서 오차가 dVRK와 유의한 차이가 없었지만(p = 0.922), FLS 페그 이동에서는 시간 격차가 유의했다(Δ = -467.27 s). 작업이 속도보다 정밀도에 중점을 둔다면 휴머노이드 로봇은 저비용 대안이 될 수 있으며, 높은 처리량이 필요하다면 다빈치 시스템이 여전히 우위를 점한다.
