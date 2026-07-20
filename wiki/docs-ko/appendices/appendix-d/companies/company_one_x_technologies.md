# 1X Technologies / 1X Technologies

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 1X Technologies |
| **영문명** | 1X Technologies |
| **본사** | 노르웨이 Moss / 미국 캘리포니아주 산타클라라 |
| **설립 시간** | 2014 |
| **공식 홈페이지** | [https://www.1x.tech](https://www.1x.tech) |
| **공급망 단계** | 소비자용 휴머노이드 로봇, 구현 학습 |
| **기업 속성** | 스타트업 (OpenAI 등 투자) |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | 1X Technologies 공식 홈페이지, 공개 제품 페이지, 제3자 사양 종합 |

## 회사 소개

1X Technologies는 안전하고 가벼우며 가정용 범용 휴머노이드 로봇을 만드는 데 주력하며, 힘줄 구동과 연질 외피 디자인을 채택합니다.

1X의 제품에는 이족 보행 NEO와 바퀴형 양팔 EVE가 포함됩니다. NEO는 가정 안전, 저소음 및 자연스러운 상호작용을 강조하며, 1X Studio 원격 시연을 통해 구현 학습(embodied learning)을 수행합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|----------|----------|----------|----------|
| NEO | 이족 보행 가정용/상업용 휴머노이드 | NEO | 가사 서비스, 돌봄, 소매 |
| EVE | 바퀴형 양팔 로봇 | EVE | 상업 보안, 물류, 연구 |

## 대표 제품

### 1X NEO

> 1X NEO: [공식 자료](https://www.1x.tech)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|----------|------|-----------|
| 크기 | 약 167–168 cm (높이) | 공개 자료 |
| 무게 | 약 30 kg | 공개 자료 |
| 자유도 | 39 | HumanoidHub 종합 |
| 적재/토크 | 전체 운반 약 25 kg; 최대 들어올리기 약 70 kg | 공개 자료 |
| 속도/회전 속도 | 보행 약 1.4 m/s; 달리기 최대 약 6.2 m/s | 공개 자료 |
| 배터리 지속 시간 | 약 4시간 (842 Wh) | 공개 자료 |
| 인터페이스/통신 | 1X NEO Cortex (NVIDIA Jetson Thor), Wi-Fi/블루투스/5G | 공개 자료 |
| 가격 | 20,000 USD + 499 USD/월 구독; 계약금 200 USD | 공개 자료 |

**기술 하이라이트**: 힘줄 구동 Myofibers, 연질 외피 및 3D 격자 폴리머, 저소음, 가정용 안전 설계, 전문가 원격 조작 구현 학습.

**응용 시나리오**: 가사, 노인 돌봄, 경상업 서비스, 연구.


### 1X EVE

> 1X EVE: [공식 자료](https://www.1x.tech)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|----------|------|-----------|
| 크기 | 미공개 | - |
| 무게 | 미공개 | - |
| 자유도 | 미공개 | - |
| 적재/토크 | 미공개 | - |
| 속도/회전 속도 | 미공개 | - |
| 배터리 지속 시간 | 미공개 | - |
| 인터페이스/통신 | 바퀴형 이동, 양팔 조작 | 공개 설명 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 바퀴형 양팔 플랫폼으로, 상업 환경에서 순찰, 물품 배달 등의 작업을 수행할 수 있으며, NEO에 사전 데이터와 시나리오 검증을 제공합니다.

**응용 시나리오**: 상업 보안, 물류 지원, 연구.


## 공급망 위치

- **상류 핵심 부품/소재**: NVIDIA Jetson Thor 컴퓨팅, 힘줄 구동 액추에이터, 연질 재료, 비전 및 마이크 어레이.
- **하류 고객/응용 시나리오**: 가정 사용자, 요양 기관, 소매 및 보안 기업.
- **주요 경쟁사/대상**: Tesla Optimus, Figure 03, Apptronik Apollo.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_one_x_technologies`
- 제품/플랫폼 엔터티: `ent_product_one_x_technologies_neo`, `ent_product_one_x_technologies_eve`
- 주요 관계:
  - `rel_ent_company_one_x_technologies_manufactures_ent_product_one_x_technologies_neo` (`ent_company_one_x_technologies` → `manufactures` → `ent_product_one_x_technologies_neo`)
  - `rel_ent_company_one_x_technologies_manufactures_ent_product_one_x_technologies_eve` (`ent_company_one_x_technologies` → `manufactures` → `ent_product_one_x_technologies_eve`)

## 참고 자료

1. [1X Technologies 공식 홈페이지](https://www.1x.tech)
2. [HumanoidHub 1X NEO 사양](https://www.humanoidhub.ai/robots/1x-neo)
3. [RoboZaps 1X NEO 리뷰](https://blog.robozaps.com/b/1x-neo-review)
