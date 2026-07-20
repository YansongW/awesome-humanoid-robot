# NVIDIA Jetson AGX Orin

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [NVIDIA / 엔비디아](../companies/company_nvidia.md) |
| **제품 카테고리** | 엣지 AI 컴퓨팅 모듈 |
| **출시일** | 2022년 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [NVIDIA Jetson Orin 페이지](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) |

## 제품 개요

NVIDIA Jetson AGX Orin은 자율 기계, 로봇 및 엣지 AI를 위한 고성능 컴퓨팅 모듈로, AI 연산 성능은 최대 275 TOPS(64 GB 버전)에 달하며, 이전 세대 Jetson AGX Xavier보다 8배 이상 향상되었습니다. 모듈은 NVIDIA Ampere 아키텍처 GPU, Arm Cortex-A78AE CPU 및 차세대 딥러닝/비전 가속기를 채택하여, 다중 고해상도 카메라, 라이다, IMU 등 센서의 고속 인터페이스를 지원합니다.

Jetson AGX Orin은 64 GB, 32 GB 및 산업용 버전의 세 가지 버전이 있으며, 전력 소비는 15W에서 60W 사이로 구성 가능하여 저전력 이동 로봇부터 고부하 산업 장비까지 다양한 요구를 충족합니다. 통합된 JetPack SDK, Isaac ROS 및 Isaac Sim 생태계는 휴머노이드 로봇, AMR, 드론 및 자율주행 프로토타입 개발을 위한 주류 컴퓨팅 플랫폼입니다.

## 제품 이미지

> NVIDIA Jetson AGX Orin: [공식 자료](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 크기 | 100 mm × 87 mm(모듈) | NVIDIA 공식 사이트 |
| AI 연산 성능 | 최대 275 TOPS(64 GB) | NVIDIA 공식 사이트 |
| GPU | 2048코어 NVIDIA Ampere 아키텍처 GPU, 64개 Tensor Core | NVIDIA 공식 사이트 |
| CPU | 12코어 Arm Cortex-A78AE v8.2 | NVIDIA 공식 사이트 |
| 메모리 | 64 GB / 32 GB LPDDR5, 204.8 GB/s | NVIDIA 공식 사이트 |
| DL 가속기 | 2× NVDLA v2 | NVIDIA 공식 사이트 |
| 비전 가속기 | 1× PVA v2 | NVIDIA 공식 사이트 |
| 카메라 인터페이스 | 16채널 MIPI CSI-2 | NVIDIA 공식 사이트 |
| 전력 소비 | 15 W – 60 W(구성 가능) | NVIDIA 공식 사이트 |
| 가격 | 미공개(개발자 키트 약 1,999 USD) | 제3자 참고 |

## 공급망 위치

- **제조사**: [NVIDIA / 엔비디아](../companies/company_nvidia.md)
- **핵심 부품/기술 출처**: 자체 개발 Ampere GPU, Arm CPU, NVDLA, PVA; 스토리지, PMIC, 캐리어 보드는 파트너사 제공.
- **하위 응용/고객**: 휴머노이드 로봇, AMR/AGV, 드론, 산업용 비전, 자율주행 프로토타입, 연구 및 교육.

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_nvidia_jetson_agx_orin`
- 제조사 엔터티: `ent_company_nvidia`
- 주요 관계:
  - `rel_ent_company_nvidia_manufactures_ent_component_nvidia_jetson_agx_orin`(`ent_company_nvidia` → `manufactures` → `ent_component_nvidia_jetson_agx_orin`)

## 응용 시나리오

- **휴머노이드 로봇 두뇌**: VLM/VLA 모델, SLAM, 동적 장애물 회피 및 정밀 손 제어 실행.
- **AMR/AGV**: 다중 카메라, 라이다 융합 인식 및 경로 계획.
- **산업용 비전 검사**: 엣지에서 실시간 결함 감지, 객체 인식 및 측정.
- **자율주행 프로토타입**: 승용차 및 무인 차량의 인식 및 의사 결정 검증 플랫폼.

## 경쟁 비교

| 비교 항목 | Jetson AGX Orin | Jetson Orin NX | Jetson AGX Xavier |
|-----------|-----------------|----------------|-------------------|
| AI 연산 성능 | 최대 275 TOPS | 최대 157 TOPS | 32 TOPS |
| 전력 소비 | 15–60 W | 10–40 W | 10–30 W |
| 메모리 | 64 GB LPDDR5 | 16 GB LPDDR5 | 16 GB LPDDR4 |
| 핵심 장점 | 최고 성능, 통합 생태계 | 작은 크기, 가성비 우수 | 성숙하고 안정적 |

## 참고 자료

1. [NVIDIA Jetson Orin 공식 페이지](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)
2. [NVIDIA Jetson AGX Orin Developer Kit](https://developer.nvidia.com/embedded/jetson-agx-orin-developer-kit)
3. [EEFOCUS – 휴머노이드 로봇 메인 칩 비교](https://www.eefocus.com/article/1821462.html)
4. [CSDN – Jetson 시리즈 연산 성능 비교](https://blog.csdn.net/qq_43298381/article/details/144167933)
