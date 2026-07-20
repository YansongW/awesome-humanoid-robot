# NVIDIA (엔비디아) / NVIDIA Corporation

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | NVIDIA (엔비디아) |
| **영문명** | NVIDIA Corporation |
| **본사** | 미국 캘리포니아주 산타클라라 |
| **설립 연도** | 1993 |
| **공식 웹사이트** | [https://www.nvidia.com](https://www.nvidia.com) |
| **공급망 단계** | AI 컴퓨팅 플랫폼, 로봇 소프트웨어/시뮬레이션, 칩 공급업체 |
| **기업 속성** | 상장 기업 (NASDAQ: NVDA) |
| **모회사/소속 그룹** | 없음 (NVIDIA Corporation이 상장 주체) |
| **데이터 출처** | NVIDIA 공식 웹사이트, Jetson/Isaac 공식 문서, 공개 보도자료 |

## 회사 소개

NVIDIA는 로봇 및 휴머노이드 로봇을 위해 Jetson 엣지 컴퓨팅, Isaac Sim 시뮬레이션, Isaac Lab 훈련 및 GR00T 휴머노이드 기반 모델을 제공하며, 물리적 AI의 핵심 지원자입니다.

Jetson Thor는 물리적 AI 및 휴머노이드 로봇 전용으로 설계되었으며, Blackwell GPU와 대용량 통합 메모리를 통합합니다. Isaac Sim은 고충실도 시뮬레이션과 합성 데이터를 제공하고, GR00T는 VLA 기반 모델을 제공합니다. 다수의 주요 휴머노이드 로봇 기업이 NVIDIA 플랫폼을 채택하고 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|-----------|----------|-----------|-----------|
| Jetson | 엣지 AI 컴퓨팅 모듈 | Jetson Thor / AGX Orin 등 | 로봇/휴머노이드 두뇌, 인식 추론 |
| Isaac Sim / Isaac Lab | 시뮬레이션 및 훈련 플랫폼 | Isaac Sim / Isaac Lab | Sim2Real, 디지털 트윈, 강화 학습 |
| Isaac GR00T | 휴머노이드 로봇 기반 모델 | GR00T N1.5 등 | VLA, 자연어 작업 실행 |

## 대표 제품

### NVIDIA Jetson Thor (T5000)

> NVIDIA Jetson Thor (T5000): [공식 자료](https://www.nvidia.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| AI 연산 성능 | 최대 2070 FP4 TFLOPS | NVIDIA 공식 |
| GPU 아키텍처 | NVIDIA Blackwell | NVIDIA 공식 |
| CPU | 14코어 Arm Neoverse-V3AE | NVIDIA 공식 |
| 메모리 | 128 GB LPDDR5X (273 GB/s) | NVIDIA 공식 |
| 네트워크 | 4×25 GbE | NVIDIA 공식 |
| 전력 소비 | 40–130 W 조정 가능 | NVIDIA 공식 |
| 크기 | 100 mm × 87 mm (모듈) | NVIDIA 공식 |
| 가격 | 개발자 키트 3,499 USD; 모듈 2,999 USD (1k 기준) | NVIDIA 공개 견적 |

**기술적 특징**: Blackwell GPU, 대용량 통합 메모리, 멀티모달 생성형 AI 및 VLA 모델 지원, 4×25GbE 고대역폭 센서 인터페이스, 휴머노이드 로봇 지향.

**적용 시나리오**: 휴머노이드 로봇 메인 컨트롤러, 자율 주행, 의료 로봇, 산업용 AMR.


### NVIDIA Isaac Sim

> NVIDIA Isaac Sim: [공식 자료](https://www.nvidia.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 기본 플랫폼 | NVIDIA Omniverse / PhysX | NVIDIA 공식 |
| 렌더링 | RTX 실시간 레이 트레이싱 | NVIDIA 공식 |
| 물리 엔진 | PhysX | NVIDIA 공식 |
| ROS 통합 | ROS 2 브리지 및 Isaac ROS | NVIDIA 공식 |
| 훈련 프레임워크 | Isaac Lab (강화 학습/모방 학습) | NVIDIA 공식 |
| 디지털 트윈 | USD 장면 및 센서 모델 지원 | NVIDIA 공식 |
| 배포 방식 | 로컬, 컨테이너, 클라우드 | NVIDIA 공식 |
| 가격 | 무료 (NVIDIA 계정/Omniverse 필요) | 공식 설명 |

**기술적 특징**: 포토리얼리스틱 시뮬레이션, PhysX 물리, Jetson/GR00T와 연결된 Sim2Real 프로세스, 대규모 합성 데이터 생성.

**적용 시나리오**: 휴머노이드 로봇 훈련, 디지털 트윈 공장, 센서 검증, 강화 학습 연구.


## 공급망 위치

- **상류 핵심 부품/소재**: TSMC 위탁 생산, 메모리, 센서 및 카메라 파트너, Omniverse 생태계.
- **하류 고객/적용 시나리오**: Tesla, Figure AI, Boston Dynamics, Agility Robotics, Apptronik, 1X Technologies 등 완성체 제조사 및 개발자.
- **주요 경쟁사/대상**: Qualcomm RB, Intel Movidius/AMD, 시뮬레이션 플랫폼 Gazebo/Unity/Unreal.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_nvidia`
- 제품/플랫폼 엔터티: `ent_software_platform_nvidia_jetson_thor`, `ent_software_platform_nvidia_isaac_sim`
- 주요 관계:
  - `rel_ent_company_nvidia_develops_ent_software_platform_nvidia_jetson_thor` (`ent_company_nvidia` → `develops` → `ent_software_platform_nvidia_jetson_thor`)
  - `rel_ent_company_nvidia_develops_ent_software_platform_nvidia_isaac_sim` (`ent_company_nvidia` → `develops` → `ent_software_platform_nvidia_isaac_sim`)

## 참고 자료

1. [NVIDIA 공식 웹사이트](https://www.nvidia.com)
2. [NVIDIA Jetson Thor 제품 페이지](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
3. [NVIDIA Isaac Sim 공식 페이지](https://developer.nvidia.com/isaac/sim)
