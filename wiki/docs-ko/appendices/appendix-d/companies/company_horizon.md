# Horizon Robotics / Horizon Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Horizon Robotics |
| **영문명** | Horizon Robotics |
| **본사** | 중국 베이징시 |
| **설립일** | 2015년 |
| **공식 홈페이지** | [https://www.horizon.ai](https://www.horizon.ai) |
| **공급망 단계** | 엣지 AI 칩, 스마트 드라이빙, 로봇 컴퓨팅, BPU 아키텍처 |
| **기업 속성** | 상장 기업 (HKEX: 9660), 국내 자율주행 칩 유니콘 |
| **모회사/소속 그룹** | 없음 (독립 상장 주체) |
| **데이터 출처** | Horizon Robotics 공식 홈페이지, 투자설명서, 공개 보도자료, 업계 보고서 |

## 회사 소개

Horizon Robotics는 중국을 선도하는 엣지 AI 칩 회사로, 자체 개발한 BPU 아키텍처를 핵심으로 스마트 드라이빙과 로봇에 고성능, 저전력 컴퓨팅 플랫폼을 제공합니다.

Horizon Robotics는 엣지 인공지능 칩 및 솔루션에 특화되어 있으며, 자체 개발한 BPU(Brain Processing Unit) 신경망 처리 아키텍처를 기반으로 Journey 시리즈 스마트 드라이빙 칩과 Horizon Mono/Pilot/SuperDrive 솔루션을 제공합니다. Journey 6 시리즈는 차세대 고급 자율주행 및 임베디드 인텔리전스 컴퓨팅을 대상으로 하며, 알고리즘과 칩의 협력 최적화를 강조합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Journey 스마트 드라이빙 칩 | ADAS 및 고급 자율주행 SoC | Journey 2/3/5/6 시리즈 | 승용차, 상용차 자율주행 |
| 로봇/임베디드 인텔리전스 컴퓨팅 | 로봇 인식 및 의사결정 컴퓨팅 플랫폼 | Journey 6 / 파생 로봇 솔루션 | 휴머노이드 로봇, AMR, 무인차 |
| 알고리즘 및 툴체인 | 인식/계획 알고리즘 및 개발 플랫폼 | Horizon SuperDrive / OpenExplorer | 스마트 드라이빙, 로봇 개발 |

## 대표 제품

### Horizon Robotics Journey 6

> Horizon Robotics Journey 6: [공식 자료](https://www.horizon.ai)를 방문하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 연산 성능 | Journey 6E: 128 TOPS; Journey 6P: 560 TOPS | Horizon Robotics 공개 자료 |
| BPU 아키텍처 | BPU 내쉬 (내쉬 아키텍처) | Horizon Robotics 공개 자료 |
| 공정 | 미공개 | - |
| CPU | 멀티코어 ARM Cortex-A78AE / 자체 개발 보안 코어 | 공개 보도 |
| ISP | 다중 고해상도 카메라 입력 지원 | Horizon Robotics 공개 자료 |
| 기능 안전 | ASIL-D / ASIL-B 등급 지원 | Horizon Robotics 공개 자료 |
| 인터페이스 | PCIe, Ethernet, MIPI CSI-2, CAN-FD | 제품 매뉴얼 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 고연산 BPU, 알고리즘-칩 협력 설계, 고급 자율주행 및 임베디드 인텔리전스를 위한 인식-의사결정 통합, 다중 센서 융합 지원.

**적용 시나리오**: 고급 스마트 드라이빙, 휴머노이드 로봇/AMR 인식 및 의사결정, 멀티모달 엣지 AI.

### Horizon Robotics Journey 5

> Horizon Robotics Journey 5: [공식 자료](https://www.horizon.ai)를 방문하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 연산 성능 | 128 TOPS | Horizon Robotics 공식 홈페이지 |
| BPU 아키텍처 | BPU 베이지안 | Horizon Robotics 공식 홈페이지 |
| CPU | 8코어 ARM Cortex-A55 / 듀얼코어 A76 | 공개 보도 |
| ISP | 16채널 카메라 입력 지원 | Horizon Robotics 공개 자료 |
| 전력 소비 | 약 30W | 공개 보도 |
| 기능 안전 | ASIL-B(D) 목표 | Horizon Robotics 공개 자료 |
| 양산 상태 | 양산 및 차량 탑재 완료 | Horizon Robotics 공개 자료 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 대규모 양산된 고연산 자율주행 칩, 개방형 툴체인, 주행-주차 통합 및 고속/도심 NOA 지원.

**적용 시나리오**: 승용차 ADAS/AD, 로봇 인식, 스마트 교통.

## 공급망 위치

- **상류 핵심 부품/소재**: 웨이퍼 파운드리 (TSMC/SMIC 등), 패키징 및 테스트, 메모리, ISP IP, 차량 인증 서비스.
- **하류 고객/적용 시나리오**: 폭스바겐, BYD, Li Auto, Changan 등 자동차 제조사; 로봇/무인차 솔루션 업체 및 개발자.
- **주요 경쟁사/대상**: NVIDIA Drive, Mobileye, Qualcomm Snapdragon Ride, Black Sesame Technologies, Huawei Ascend.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_horizon`
- 제품 엔터티: `ent_product_horizon_journey6`, `ent_product_horizon_journey5`
- 주요 관계:
  - `ent_company_horizon` -- `manufactures` --> `ent_product_horizon_journey6`
  - `ent_company_horizon` -- `manufactures` --> `ent_product_horizon_journey5`
  - `ent_product_horizon_journey6` -- `uses` --> `ent_component_bpu_nash`
  - `ent_product_horizon_journey5` -- `uses` --> `ent_component_bpu_bayes`

## 참고 자료

1. [공식 홈페이지](https://www.horizon.ai)
2. [Horizon Robotics 공식 홈페이지](https://www.horizon.ai)
3. Horizon Robotics 로봇 투자설명서 (HKEX: 9660)
