# Formant 로봇 데이터 및 운영 플랫폼 / Formant Data & Operations Platform

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Formant](../companies/company_formant.md) |
| **제품 카테고리** | 로봇 데이터 플랫폼 / 원격 운영 / 원격 조작 |
| **출시일** | 2017년부터 지속적 업데이트 |
| **상태** | 상용 / 대규모 배포 |
| **공식 홈페이지/출처** | [Formant 공식 홈페이지](https://formant.io) |

## 제품 개요

Formant 데이터 및 운영 플랫폼은 로봇 개발사와 최종 기업을 위한 통합 RobOps 플랫폼입니다. 경량 Formant Agent를 통해 로봇은 수 분 내에 클라우드에 연결되어 원격 측정, 로그, 비디오, 지도, 알람, 원격 제어 및 차량대 분석을 원스톱으로 관리할 수 있습니다.

플랫폼은 ROS/ROS2, MQTT, REST API 등 다양한 연결 방식을 지원하며, 서로 다른 브랜드와 형태의 로봇과 호환됩니다. Formant는 "단일 패널"(single pane of glass)을 통해 이기종 차량대를 관리하여 운영 인력이 100:1 또는 그 이상의 로봇-인간 비율로 대규모 로봇 배포를 관리할 수 있도록 합니다.

2023년, Formant는 PickNik Robotics와 협력하여 MoveIt Pro를 통합함으로써 로봇 팔 원격 조작 및 배포 관리 지원을 더욱 확장했습니다.

## 제품 이미지

> Formant Platform: [공식 자료](https://formant.io)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 배포 형태 | 퍼블릭 클라우드 SaaS / 프라이빗 배포 | Formant 공식 홈페이지 |
| 연결 방식 | Formant Agent (단일 명령어 설치) | Formant 문서 |
| 지원 미들웨어 | ROS 1 / ROS 2, MQTT, REST API | 공개 자료 |
| 데이터 유형 | 원격 측정, 로그, 비디오, 포인트 클라우드, 지도, 알람 | Formant 문서 |
| 시각화 | 실시간 대시보드, 2D/3D 뷰, 히스토리 재생 | Formant 문서 |
| 원격 조작 | 브라우저 기반 원격 제어, 컨트롤러/API | 공개 자료 |
| 차량대 규모 | 수천 대 로봇 지원 | BMW i Ventures 뉴스 |
| 보안 규정 준수 | SOC 2, GDPR, 암호화 전송 | Formant 공식 홈페이지 |
| 가격 | 장치/데이터량 기반 구독 | 공식 문의 |

## 공급망 위치

- **제조사**: [Formant](../companies/company_formant.md)
- **핵심 부품/기술 출처**: AWS/Google Cloud/Azure 클라우드 인프라, ROS/ROS2, 비디오 코덱, WebRTC/네트워크 전송, 시계열 데이터베이스.
- **하위 응용/고객**: SoftBank Robotics, BP, Blue River Technology (John Deere), Burro, Knightscope, Scythe.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_formant_platform`
- 제조사 엔터티: `ent_company_formant`
- 주요 관계:
  - `rel_ent_company_formant_manufactures_ent_product_formant_platform` (`ent_company_formant` → `manufactures` → `ent_product_formant_platform`)

## 응용 시나리오

- **창고 AMR 차량대 모니터링**: 위치, 배터리, 작업 상태를 실시간으로 확인하고 이상 로봇을 신속하게 식별.
- **농업 로봇 원격 진단**: 비디오 및 원격 측정 재생을 통해 현장 고장의 근본 원인 분석.
- **청소 서비스 로봇 대규모 운영**: 다중 브랜드 로봇을 단일 패널로 관리하여 운영 비용 절감.
- **로봇 팔 원격 조작**: MoveIt Pro와 결합하여 복잡한 파지 작업의 수동 개입 및 디버깅 구현.

## 경쟁 비교

| 비교 항목 | Formant | InOrbit | Freedom Robotics |
|-----------|---------|---------|------------------|
| 포지셔닝 | 로봇 데이터 및 운영 플랫폼 | 로봇 운영 및 오케스트레이션 플랫폼 | 로봇 원격 제어 및 차량대 관리 |
| 핵심 강점 | 즉시 사용 가능, 강력한 데이터 시각화 | 오케스트레이션 및 상호 운용성 표준 지원 | 한 줄 코드 연결, 개발자 친화적 |
| 원격 조작 | 내장 | 내장 | 내장 |
| 상호 운용성 인증 | 비교적 유연 | InOrbit Connect | 비교적 유연 |
| 대표 고객 | 로봇 제조사 + 최종 기업 | 대기업 혼합 차량대 | 스타트업 로봇 회사 |

## 구매 및 배포 제안

- 자체 플랫폼을 구축하지 않고 신속하게 엔터프라이즈급 로봇 데이터 및 운영 역량을 확보하려는 팀에 적합.
- 배포 전 데이터 해외 이전 및 규정 준수 요구 사항을 평가하여 퍼블릭 클라우드 또는 프라이빗 배포 모드 선택.
- 소규모 로봇을 먼저 연결하여 데이터 대역폭, 알람 임계값 및 원격 조작 지연 시간을 검증할 것을 권장.

## 참고 자료

1. [Formant 공식 홈페이지](https://formant.io)
2. [BMW i Ventures – Formant 투자 뉴스](https://www.bmwiventures.com/news/operationalizing-robot-fleets-at-scale-our-lead-investment-in-formant)
3. [The Robot Report – Formant와 SoftBank 협력](https://www.therobotreport.com/formants-data-platform-comes-to-softbanks-cleaning-robots/)
4. [SignalFire – Formant 투자 블로그](https://www.signalfire.com/blog/formant-robotics-investor)
