# Sanctuary AI / Sanctuary AI

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Sanctuary AI |
| **영문명** | Sanctuary AI |
| **본사** | 캐나다 브리티시컬럼비아주 밴쿠버 |
| **설립일** | 2018 |
| **공식 사이트** | [https://www.sanctuary.ai](https://www.sanctuary.ai) |
| **공급망 단계** | 범용 휴머노이드 로봇, 임베디드 인텔리전스, AI 시스템 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Sanctuary AI 공식 사이트, The Robot Report, 제3자 사양 종합 |

## 회사 소개

Sanctuary AI는 범용 노동 로봇을 목표로 하며, Phoenix는 높은 자유도의 유압식 손과 Carbon AI 인지 시스템을 갖추고 있습니다.

Phoenix는 인간과 유사한 양손 촉각 인식과 원격 조작 데이터 폐쇄 루프를 강조하며, Carbon AI는 자연어를 물리적 동작으로 변환합니다. 회사는 Magna International 등 제조 파트너와 협력하여 시범 운영을 추진하고 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|------|
| Phoenix 휴머노이드 로봇 | 범용형 산업용 휴머노이드 | Phoenix Gen 8 / Gen 6 | 제조, 소매, 물류 |
| Carbon AI | 로봇 인지 시스템 | Carbon | 작업 학습, 추론, 인간-로봇 상호작용 |

## 대표 제품

### Sanctuary AI Phoenix Gen 8

> Sanctuary AI Phoenix Gen 8: [공식 자료](https://www.sanctuary.ai)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 170 cm (높이) | 공개 자료 |
| 무게 | 약 70 kg | 공개 자료 |
| 자유도 | 전신 44–75 (구성에 따라 다름); 손 20–21×2 | 공개 자료 |
| 적재/토크 | 약 25 kg; 한 손 정밀 조작 약 1.5 kg | 공개 자료 |
| 속도/회전수 | 약 4.8 km/h | 공개 자료 |
| 배터리 지속 시간 | 약 4시간 | 제3자 종합 |
| 인터페이스/통신 | 깊이/RGB 카메라, 힘/토크 및 촉각 센서, Carbon AI | 공개 자료 |
| 가격 | 미공개 (기업 문의) | - |

**기술적 특징**: 유압식 고자유도 손, 손끝 촉각 감도 약 5 mN, Carbon AI 자연어-동작 변환, 빠른 작업 학습 (<24 h).

**적용 시나리오**: 자동차 제조, 소매 계산, 자재 운반, 데이터 수집.


### Sanctuary AI Phoenix Gen 6

> Sanctuary AI Phoenix Gen 6: [공식 자료](https://www.sanctuary.ai)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 170 cm (높이) | The Robot Report |
| 무게 | 약 57.9 kg | The Robot Report |
| 자유도 | 손 20×2; 전신 미공개 | 공개 자료 |
| 적재/토크 | 약 20.5 kg | The Robot Report |
| 속도/회전수 | 약 3 mph (4.8 km/h) | The Robot Report |
| 배터리 지속 시간 | 미공개 | - |
| 인터페이스/통신 | Carbon AI, 촉각/시각 인식 | 공개 자료 |
| 가격 | 미공개 | - |

**기술적 특징**: Phoenix 플랫폼에 처음으로 양쪽 다리를 통합하여 전신 휴머노이드 형태와 양손 정밀 조작을 검증.

**적용 시나리오**: 초기 다중 산업 시나리오 검증, 데이터 수집 및 알고리즘 반복.

## 공급망 위치

- **상류 핵심 부품/재료**: 유압식 마이크로 밸브, 촉각 센서, 컴퓨팅 플랫폼, 구조 부품; Magna 제조 협력.
- **하류 고객/적용 시나리오**: Magna International, Canadian Tire, 자동차/소매 기업.
- **주요 경쟁사/대상**: Figure AI, Tesla Optimus, Apptronik Apollo, Agility Robotics Digit.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_sanctuary_ai`
- 제품/플랫폼 엔터티: `ent_product_sanctuary_ai_phoenix_gen8`, `ent_product_sanctuary_ai_phoenix_gen6`
- 주요 관계:
  - `rel_ent_company_sanctuary_ai_manufactures_ent_product_sanctuary_ai_phoenix_gen8` (`ent_company_sanctuary_ai` → `manufactures` → `ent_product_sanctuary_ai_phoenix_gen8`)
  - `rel_ent_company_sanctuary_ai_manufactures_ent_product_sanctuary_ai_phoenix_gen6` (`ent_company_sanctuary_ai` → `manufactures` → `ent_product_sanctuary_ai_phoenix_gen6`)

## 참고 자료

1. [Sanctuary AI 공식 사이트](https://www.sanctuary.ai)
2. [The Robot Report의 Phoenix 보도](https://www.therobotreport.com/sanctuary-ai-unveils-general-purpose-humanoid-robot/)
3. [RoboZaps Sanctuary AI Phoenix Review](https://blog.robozaps.com/b/sanctuary-ai-phoenix-review)
