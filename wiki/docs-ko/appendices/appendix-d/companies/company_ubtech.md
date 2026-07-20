# UBTECH Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 우비쉰 테크놀로지 |
| **영문명** | UBTECH Robotics |
| **본사** | 중국 선전 |
| **설립일** | 2012년 |
| **공식 웹사이트** | [https://www.ubtrobot.com](https://www.ubtrobot.com) / [commercial.ubtrobot.com](https://www.commercial.ubtrobot.com/) |
| **공급망 단계** | 완제품 OEM / 산업용 및 서비스용 휴머노이드 로봇 |
| **기업 속성** | 상장 기업 (홍콩거래소 09880.HK), 국가급 전문화·정밀화·특성화·혁신형 "작은 거인" |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | UBTECH 공식 웹사이트, 홍콩거래소 공시, IT之家, WAIC 공개 보도 |

## 회사 소개

UBTECH은 중국에서 가장 먼저 휴머노이드 로봇의 상업적 양산을 실현한 기업 중 하나로, "휴머노이드 로봇 풀스택 기술 + 산업 솔루션" 제공업체로 자리매김하고 있습니다.

회사는 교육 서비스 로봇에서 출발하여 점차 인공지능 교육, 물류, 헬스케어 및 산업 제조 분야로 확장했습니다. 2023년 홍콩거래소 상장 후, UBTECH은 Walker 시리즈를 신에너지 자동차 최종 조립, 3C 제조 등 현장에서 대규모로 도입하는 데 주력하며 "휴머노이드 로봇 공장 진입" 전략을 제시했습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 산업용 휴머노이드 | 7×24시간 생산 라인 작업, 자동 배터리 교체 | Walker S / S1 / S2 | 자동차 최종 조립, 3C 조립, 물류 분류 |
| 서비스용 휴머노이드 | 안내, 교육 연구 | Walker X / Alpha 시리즈 | 전시장, 교육, 연구 |

## 대표 제품

### Walker S2

> UBTECH Walker S2: [공식 자료](https://www.ubtrobot.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 176 cm | 제3자 딜러 자료 |
| 무게 | 약 70 kg | 제3자 딜러 자료 |
| 자유도 | 52 DOF | Humanoid.Guide / 딜러 자료 |
| 하중/토크 | 양팔 하중 15 kg, 한 손 7 kg | 딜러 공개 사양 |
| 속도/회전수 | 최대 2 m/s (약 7.2 km/h) | 공개 보도 |
| 배터리 지속 시간 | 약 2–2.5 h | 딜러 자료 |
| 인터페이스/통신 | Wi-Fi | 딜러 자료 |
| 가격 | 미공개 | 문의 필요 |

**기술적 특징**: 4세대 생체 모방 양팔, 자동 핫스왑 배터리 시스템 (공식 주장 3분 내 배터리 교체 완료), BrainNet 2.0 + Co-Agent 다중 모드 작업 계획.

**적용 시나리오**: 자동차 공장 분류 및 운반, 생산 라인 상하차, 야간 연속 작업 등.

### Walker S1

> UBTECH Walker S1: [공식 자료](https://www.ubtrobot.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 172 cm | 공개 보도 |
| 무게 | 약 65 kg | 공개 보도 |
| 자유도 | 미공개 | - |
| 하중/토크 | 미공개 | - |
| 속도/회전수 | 미공개 | - |
| 배터리 지속 시간 | 미공개 | - |
| 인터페이스/통신 | 미공개 | - |
| 가격 | 미공개 | 문의 필요 |

**기술적 특징**: 산업 현장을 위한 초기 배치 플랫폼으로, Walker S2와 일부 운동 제어 및 인식 아키텍처를 공유합니다.

**적용 시나리오**: 신에너지 자동차 생산 라인 실습, 3C 공장 협력 운반.

## 공급망 위치

- **상류 핵심 부품/소재**: 자체 개발 서보 모터 및 관절 모듈, 외부 구매 하모닉 감속기, 힘 센서, 배터리, 구조 부품 ([제7장 공급업체 지도](../../../chapters/chapter-07.md) 참조).
- **하류 고객/적용 시나리오**: BYD, Foxconn, Airbus, Texas Instruments 등 제조 고객; 교육, 전시장, 헬스케어 기관.
- **주요 경쟁사/비교 대상**: Tesla Optimus, Figure 02, Unitree H1, Fourier GR 시리즈.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_ubtech`
- 제품 엔터티: `ent_product_ubtech_walker_s2`, `ent_product_ubtech_walker_s1`
- 주요 관계:
  - `ent_company_ubtech` -- `manufactures` --> `ent_product_ubtech_walker_s2`
  - `ent_company_ubtech` -- `manufactures` --> `ent_product_ubtech_walker_s1`
  - `ent_product_ubtech_walker_s2` -- `uses` --> `ent_component_lithium_battery`

## 참고 자료

1. [UBTECH 공식 웹사이트](https://www.ubtrobot.com)
2. [UBTECH 상업용 로봇 공식 웹사이트](https://www.commercial.ubtrobot.com/)
3. [IT之家 – UBTECH Walker S2 보도](https://www.ithome.com)
4. [Humanoid.Guide – UBTECH Walker S2](https://humanoid.guide/product/walker-s2/)
5. [부록 D.4 주요 제품 Wiki](../index-products.md)
