# 블랙세서미 인텔리전트 화산 A1000 / Black Sesame A1000

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [블랙세서미 인텔리전트 / Black Sesame](../companies/company_black_sesame.md) |
| **제품 카테고리** | 자율주행/로봇 AI 연산 칩 |
| **출시 시간** | 2020년 화산 A1000 출시 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | 블랙세서미 인텔리전트 공식 홈페이지, 홍콩 증시 투자설명서 |

## 제품 개요

블랙세서미 인텔리전트 화산 A1000은 고급 자율주행 및 지능형 로봇을 위해 설계된 고성능 AI 칩으로, 자체 개발 ISP, 신경망 처리 엔진 및 다중 센서 융합 기능을 통합합니다.

화산 A1000은 블랙세서미 자체 개발 NeuralIQ ISP 및 DynamAI NN 엔진을 채택하여, 다중 채널 고화질 카메라, 라이다 및 밀리미터파 레이더 연결을 지원하며, ASIL-B부터 ASIL-D까지의 기능 안전 목표를 갖추고 있습니다. 단일 칩 성능은 L2+부터 L3 수준의 자율주행 요구 사항을 충족할 수 있으며, 로봇의 다중 모드 인식 및 실시간 의사 결정을 위해 확장할 수도 있습니다.

## 제품 이미지

> 블랙세서미 인텔리전트 화산 A1000: [공식 자료](https://www.blacksesame.com.cn)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 프로세서 | 화산 A1000 | 블랙세서미 인텔리전트 공식 홈페이지 |
| 아키텍처 | NeuralIQ ISP + DynamAI NN | 블랙세서미 공개 자료 |
| 공정 | 16 nm | 공개 보도 |
| AI 성능 | INT8 약 58 TOPS | 블랙세서미 공개 자료 |
| CPU | ARM Cortex-A55 멀티코어 | 공개 보도 |
| ISP | 자체 개발 NeuralIQ, 다중 채널 고동적 범위 이미지 지원 | 블랙세서미 공개 자료 |
| 센서 인터페이스 | 다중 채널 카메라, 라이다, 밀리미터파 레이더 | 블랙세서미 공개 자료 |
| 기능 안전 | ASIL-B / ASIL-D (일부 모듈 목표) | 블랙세서미 공개 자료 |
| 전력 소비 | 약 15–25 W | 공개 보도 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [블랙세서미 인텔리전트 / Black Sesame](../companies/company_black_sesame.md)
- **핵심 부품/기술 출처**: 자체 개발 ISP/NN 아키텍처, 웨이퍼 파운드리, 차량용 메모리, 차량용 이더넷 PHY, 패키징 및 테스트, PCB.
- **하류 응용/고객**: 완성차 업체, Tier1, 자율주행 솔루션 업체, 로봇 완성차 업체, 센서 제조업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_black_sesame_a1000`
- 부품 엔터티: `ent_component_black_sesame_a1000_chip`
- 제조사 엔터티: `ent_company_black_sesame`
- 주요 관계:
  - `rel_ent_company_black_sesame_manufactures_ent_product_black_sesame_a1000` (`ent_company_black_sesame` → `manufactures` → `ent_product_black_sesame_a1000`)
  - `rel_ent_company_black_sesame_manufactures_ent_component_black_sesame_a1000_chip` (`ent_company_black_sesame` → `manufactures` → `ent_component_black_sesame_a1000_chip`)
  - `ent_product_black_sesame_a1000` -- `uses` --> `ent_component_black_sesame_a1000_chip`

## 응용 시나리오

- **자율주행 도메인 컨트롤러**: 메인 칩으로 환경 인식, 융합 위치 측정 및 경로 계획 구현.
- **로봇 인식 두뇌**: 카메라와 라이다 데이터를 융합하여 SLAM, 장애물 회피 및 조작 지원.
- **다중 센서 융합 플랫폼**: 무인 차량, 무인 배송, 휴머노이드 로봇 등 복잡한 시나리오에 사용.

## 경쟁 비교

| 비교 항목 | 화산 A1000 | Horizon Journey 5 | NVIDIA Orin |
|--------|------|------|------|
| 성능 | ~58 TOPS | ~128 TOPS | ~200–254 TOPS |
| 기능 안전 | ASIL-D 목표 | ASIL-B/D | ASIL-D |
| 생태계 | 블랙세서미 툴체인 | Horizon Tian Gong Kai Wu | NVIDIA DRIVE |

## 구매 및 배포 권장 사항

- 카메라, 레이더 인터페이스 수와 A1000의 적합성, 그리고 툴체인이 대상 알고리즘을 지원하는지 우선 평가하세요.
- 배포 전에 기능 안전 및 열 설계 검증을 완료하여 차량용/산업용 신뢰성 요구 사항을 충족하는지 확인하세요.
- 블랙세서미 공식 채널을 통해 최신 BSP, SDK 및 참조 설계를 확보하는 것을 권장합니다.

## 관련 항목

- [제조사: 블랙세서미 인텔리전트 / Black Sesame](../companies/company_black_sesame.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [블랙세서미 인텔리전트 공식 홈페이지](https://www.blacksesame.com.cn)
2. [블랙세서미 인텔리전트 화산 시리즈](https://www.blacksesame.com.cn/products/1.html)
3. 블랙세서미 인텔리전트 홍콩 증시 투자설명서
