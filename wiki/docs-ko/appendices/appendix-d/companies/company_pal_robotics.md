# PAL Robotics / PAL Robotics

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | PAL Robotics |
| **영문명** | PAL Robotics |
| **본사** | 스페인 바르셀로나 |
| **설립 연도** | 2004 |
| **공식 웹사이트** | [https://pal-robotics.com](https://pal-robotics.com) |
| **공급망 단계** | 연구용 휴머노이드 로봇, 오픈소스 ROS 플랫폼, 서비스 로봇 |
| **기업 속성** | 민간 기업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | PAL Robotics 공식 웹사이트, TALOS 제품 페이지, 공식 데이터 시트 |

## 회사 소개

PAL Robotics는 유럽을 선도하는 서비스 및 연구용 로봇 기업으로, TALOS 이족 보행 휴머노이드 로봇은 높은 동적 제어, ROS/ROS 2 전 스택 오픈소스 및 산업용 토크 제어로 유명합니다.

TALOS는 AI, 머신러닝, 운동 제어 및 산업 4.0 연구를 대상으로 하며, 전 관절 토크 피드백, 2 kHz 제어 루프 및 EtherCAT 통신을 제공합니다. 또한 회사는 TIAGo, REEM-C 등의 플랫폼도 제공합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|-----------|----------|-----------|-----------|
| TALOS | 이족 보행 휴머노이드 연구 플랫폼 | TALOS | 산업 연구, AI 및 운동 제어 |
| TIAGo / REEM-C | 서비스/연구 로봇 | TIAGo / REEM-C | 인간-로봇 상호작용, 요양, 연구 |

## 대표 제품

### PAL Robotics TALOS

> PAL Robotics TALOS: [공식 자료](https://pal-robotics.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | 175 cm (높이) | PAL Robotics 제품 페이지 |
| 무게 | 95 kg | PAL Robotics 제품 페이지 |
| 자유도 | 32 (다리 6×2, 팔 7×2, 허리 2, 목 2, 그리퍼 1×2) | 공식 데이터 시트 |
| 부하/토크 | 한 팔 펼친 상태 6 kg | PAL Robotics 제품 페이지 |
| 속도/회전 속도 | 약 3 km/h | 제3자 종합 |
| 배터리 지속 시간 | 보행 1.5 h / 대기 3 h (1080 Wh) | 공식 데이터 시트 |
| 인터페이스/통신 | ROS / ROS 2, EtherCAT, Ubuntu LTS RT | 공식 데이터 시트 |
| 가격 | 요청 시 견적 | - |

**기술적 특징**: 전 토크 피드백 관절, 2 kHz 제어, ROS/ROS 2 오픈소스, 산업용 도구 조작, 맞춤형 헤드 및 그리퍼.

**응용 시나리오**: 로봇 연구, 운동 제어 알고리즘 검증, 산업 4.0 시연, 인간-로봇 상호작용 연구.

### PAL Robotics REEM-C

> PAL Robotics REEM-C: [공식 자료](https://pal-robotics.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | 약 165 cm (높이) | 공개 자료 |
| 무게 | 약 80 kg | 공개 자료 |
| 자유도 | 44 | 공개 자료 |
| 부하/토크 | 미공개 | - |
| 속도/회전 속도 | 미공개 | - |
| 배터리 지속 시간 | 미공개 | - |
| 인터페이스/통신 | ROS | 공개 자료 |
| 가격 | 요청 시 견적 | - |

**기술적 특징**: 초기 전신 휴머노이드 연구 플랫폼으로, TALOS의 하드웨어 및 ROS 제어 기반을 마련했습니다.

**응용 시나리오**: 인간-로봇 상호작용, 내비게이션 및 운동 연구.

## 공급망 위치

- **상류 핵심 부품/재료**: 모터/드라이브, 힘/토크 센서, 컴퓨팅 모듈, 구조 부품 및 배터리.
- **하류 고객/응용 시나리오**: 연구 기관 (Inria, NASA, DARPA), EU 연구 프로젝트, 서비스 로봇 고객.
- **주요 경쟁사/대상**: Boston Dynamics Atlas (연구/산업), 기타 연구용 휴머노이드 플랫폼.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_pal_robotics`
- 제품/플랫폼 엔터티: `ent_product_pal_robotics_talos`, `ent_product_pal_robotics_reem_c`
- 주요 관계:
  - `rel_ent_company_pal_robotics_manufactures_ent_product_pal_robotics_talos` (`ent_company_pal_robotics` → `manufactures` → `ent_product_pal_robotics_talos`)
  - `rel_ent_company_pal_robotics_manufactures_ent_product_pal_robotics_reem_c` (`ent_company_pal_robotics` → `manufactures` → `ent_product_pal_robotics_reem_c`)

## 참고 자료

1. [PAL Robotics 공식 웹사이트](https://pal-robotics.com)
2. [TALOS 제품 페이지](https://pal-robotics.com/robot/talos/)
3. [TALOS 공식 데이터 시트 PDF](https://pal-robotics.com/wp-content/uploads/2024/05/Datasheet-TALOS.pdf)
