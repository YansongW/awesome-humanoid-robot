# Open Robotics / Open Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Open Robotics |
| **영문명** | Open Robotics |
| **본사** | 미국 캘리포니아주 마운틴뷰 |
| **설립 시간** | 2012 |
| **공식 홈페이지** | [https://www.openrobotics.org](https://www.openrobotics.org) |
| **공급망 단계** | 오픈소스 로봇 소프트웨어 플랫폼, 미들웨어, 시뮬레이션 |
| **기업 속성** | 비영리 재단(OSRF) + Intrinsic 인수 상업 자회사 |
| **모회사/소속 그룹** | Open Source Robotics Foundation(OSRF) |
| **데이터 출처** | Open Robotics 공식 홈페이지, ROS 및 Gazebo 공식 문서 |

## 회사 소개

Open Robotics는 ROS, ROS 2, Gazebo 시뮬레이터 및 Open-RMF를 유지 관리하며, 글로벌 로봇 소프트웨어의 사실상 표준입니다.

ROS/ROS 2는 로봇 미들웨어, 알고리즘 라이브러리 및 툴체인을 제공합니다. Gazebo는 고충실도 3D 물리 시뮬레이션을 제공합니다. Open-RMF는 다중 로봇 플릿을 조정합니다. 대부분의 휴머노이드 로봇 프로젝트는 이러한 오픈소스 플랫폼에 의존합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| ROS 2 | 로봇 운영체제 2세대 | ROS 2 Jazzy 등 | 미들웨어, 내비게이션, 제어, 인식 |
| Gazebo | 3D 물리 시뮬레이터 | Gazebo Harmonic/Ionic | 로봇 시뮬레이션, Sim2Real, 센서 검증 |
| Open-RMF | 로봇 미들웨어 프레임워크 | Open-RMF | 다중 로봇 스케줄링 및 협업 |

## 대표 제품

### ROS 2

> ROS 2: [공식 자료](https://www.openrobotics.org)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 버전 | Jazzy Jalisco(LTS, 2024) 등 | ROS 공식 문서 |
| 라이선스 | Apache 2.0 / BSD | 공식 저장소 |
| 통신 미들웨어 | DDS(기본 eProsima Fast DDS) | 공식 문서 |
| 지원 언어 | C++ / Python | 공식 문서 |
| 지원 플랫폼 | Linux, RTOS, 임베디드 | 공식 문서 |
| 실시간성 | 실시간 제어 지원(플랫폼 및 RMW에 따라 다름) | 공식 문서 |
| 핵심 생태계 | Nav2, MoveIt 2, ros2_control, rviz2 | 공식 문서 |
| 가격 | 무료 오픈소스 | - |

**기술 하이라이트**: 분산 아키텍처, DDS 통신, 크로스 플랫폼 지원, 방대한 알고리즘 및 도구 생태계, 대부분의 휴머노이드 로봇에 채택됨.

**응용 시나리오**: 로봇 소프트웨어 개발, 내비게이션, 조작, 시뮬레이션에서 실제 배포까지.


### Gazebo

> Gazebo: [공식 자료](https://www.openrobotics.org)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 버전 | Harmonic / Ionic 등 | Gazebo 공식 |
| 라이선스 | Apache 2.0 | 공식 저장소 |
| 물리 엔진 | ODE, Bullet, DART, Simbody | 공식 문서 |
| 렌더링 | OGRE | 공식 문서 |
| 모델 형식 | SDF, URDF | 공식 문서 |
| ROS 통합 | ros_gz_bridge 및 네이티브 플러그인 | 공식 문서 |
| 센서 시뮬레이션 | 카메라, LiDAR, IMU, 깊이 카메라, GPS 등 | 공식 문서 |
| 가격 | 무료 오픈소스 | - |

**기술 하이라이트**: 다중 물리 엔진 지원, 고품질 센서 시뮬레이션, ROS/ROS 2와의 긴밀한 통합, Sim2Real 연구에 널리 사용됨.

**응용 시나리오**: 로봇 알고리즘 검증, 디지털 트윈, 강화 학습 훈련, 센서 모델 테스트.


## 공급망 위치

- **상류 핵심 부품/재료**: DDS 구현, 물리 엔진, 그래픽 렌더링, 운영체제 및 컴파일 툴체인.
- **하류 고객/응용 시나리오**: 거의 모든 휴머노이드 로봇 OEM, 연구 기관, 자율주행 및 물류 로봇 기업.
- **주요 경쟁사/대응 제품**: NVIDIA Isaac Sim, Unity, Unreal Engine, CoppeliaSim, Webots.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_open_robotics`
- 제품/플랫폼 엔터티: `ent_software_platform_open_robotics_ros2`, `ent_software_platform_open_robotics_gazebo`
- 주요 관계:
  - `rel_ent_company_open_robotics_develops_ent_software_platform_open_robotics_ros2`(`ent_company_open_robotics` → `develops` → `ent_software_platform_open_robotics_ros2`)
  - `rel_ent_company_open_robotics_develops_ent_software_platform_open_robotics_gazebo`(`ent_company_open_robotics` → `develops` → `ent_software_platform_open_robotics_gazebo`)

## 참고 자료

1. [Open Robotics 공식 홈페이지](https://www.openrobotics.org)
2. [ROS 2 공식 문서](https://docs.ros.org/en/rolling/)
3. [Gazebo 공식 문서](https://gazebosim.org/home)
