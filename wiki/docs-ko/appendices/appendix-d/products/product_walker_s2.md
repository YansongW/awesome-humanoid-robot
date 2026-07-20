# UBTECH Walker S2 / UBTECH Walker S2

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [UBTECH / UBTECH](../companies/company_ubtech.md) |
| **제품 카테고리** | 산업용 휴머노이드 로봇 |
| **출시 시기** | 2024–2025년 |
| **상태** | 양산/기업 납품 |
| **공식 홈페이지/출처** | [UBTECH 상용 공식 홈페이지](https://www.commercial.ubtrobot.com/) |

## 제품 개요

UBTECH Walker S2는 Walker 산업용 휴머노이드 로봇 시리즈의 2세대 제품으로, 자동차 제조, 3C 전자 및 물류 창고 현장을 위해 설계되었습니다. 본체는 52개의 자유도를 가지며, 양팔 최대 탑재 하중은 15kg이고, 4세대 5지 다관절 손과 ±162° 허리 회전을 탑재하여 박스 개봉, 자재 투입, 품질 검사, 도장 등 복잡한 산업 동작을 수행할 수 있습니다.

Walker S2의 핵심 장점은 자체 배터리 핫 스왑 시스템으로, 3분 이내에 배터리 교체가 가능하여 거의 24시간 연속 작업이 가능합니다. 감지 시스템에는 양안 입체 시각, 심층 LiDAR, 6축 힘 센서 및 IMU가 포함되며, ROSA 2.0 운영 체제와 멀티모달 대형 모델을 탑재하여 다기 협업 및 MES 시스템 연동을 지원합니다. Walker S2는 NIO, BYD, Airbus 등 고객의 생산 라인 또는 시범 프로젝트에 배치되어 검증되었습니다.

## 제품 이미지

> UBTECH Walker S2: [공식 자료](https://www.commercial.ubtrobot.com/)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 176cm (높이) | 공개 사양 |
| 무게 | 약 70–75kg | 구성별 상이 |
| 자유도 (본체) | 52 DOF | 공개 사양 |
| 주요 성능 지표 | 양팔 최대 탑재 하중 15kg; 허리 회전 ±162° | 공개 사양 |
| 보행 속도 | 약 2m/s (7.2km/h) | 공개 사양 |
| 배터리 지속 시간 | 약 2시간; 핫 스왑 배터리 지원 | 공개 사양 |
| 컴퓨팅 플랫폼 | X86 + NVIDIA Jetson Orin | RBTX 제품 페이지 |
| 가격 | 미공개 (업계 추정 68,000–120,000 USD) | 제3자 추정 |

## 공급망 위치

- **제조사**: [UBTECH / UBTECH](../companies/company_ubtech.md)
- **핵심 부품/기술 출처**: 자체 개발 일체형 관절, NVIDIA Jetson Orin 컴퓨팅 플랫폼, 양안 입체 시각, 심층 LiDAR, 다관절 손; 일부 감속기, 모터는 외부 구매.
- **하류 응용/고객**: NIO, BYD, Airbus, 사우디/싱가포르/일본 시범 프로젝트.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ubtech_walker_s2`
- 제조사 엔터티: `ent_company_ubtech`
- 주요 관계:
  - `rel_ent_company_ubtech_manufactures_ent_product_ubtech_walker_s2` (`ent_company_ubtech` → `manufactures` → `ent_product_ubtech_walker_s2`)

## 응용 시나리오

- **자동차 제조**: NIO, BYD 등 공장에서 외관 품질 검사, 내장 조립, 안전벨트 검사 및 자재 운반 수행.
- **3C 전자**: 정밀 조립, 나사 체결, 부품 삽입 및 AOI 재검사 보조.
- **상업용 전시**: 전시장 설명, 쇼핑몰 안내 및 브랜드 행사 인터랙티브 전시.

## 경쟁 비교

| 비교 항목 | UBTECH Walker S2 | Tesla Optimus Gen 3 | Figure 02 |
|--------|------------------|---------------------|-----------|
| 포지셔닝 | 산업용 휴머노이드 | 범용/산업용 휴머노이드 | 산업 제조 휴머노이드 |
| 본체 DOF | 52 | 28+ 몸통 + 22×2 손 | 28 |
| 양팔 탑재 하중 | 15kg | 약 20kg | 25kg |
| 핵심 강점 | 공장 배치 사례, 핫 스왑 배터리, 다관절 손 | 비용 목표, AI 데이터 | Helix VLA, BMW 배치 |

## 구매 및 배치 권장 사항

- 자동차/3C 제조 기업은 Walker S2와 기존 MES/AGV 시스템의 연동 능력을 중점적으로 평가해야 합니다.
- 24시간 연속 작업 이점을 활용하기 위해 배터리 핫 스왑 스테이션 및 다기 협업 스케줄링 방안을 계획하는 것이 좋습니다.

## 참고 자료

1. [UBTECH 상용 공식 홈페이지](https://www.commercial.ubtrobot.com/)
2. [Robozaps – UBTECH Walker S Review](https://blog.robozaps.com/b/ubtech-walker-s-review)
3. [Humanoid.Guide – Walker S2](https://humanoid.guide/product/walker-s2/)
4. [RBTX – UBTECH Walker S2 제품 페이지](https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2)
