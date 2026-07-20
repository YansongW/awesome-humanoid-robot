# Figure AI / Figure AI

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Figure AI |
| **영문명** | Figure AI |
| **본사** | 미국 캘리포니아주 서니베일 |
| **설립 시간** | 2022 |
| **공식 사이트** | [https://www.figure.ai](https://www.figure.ai) |
| **공급망 단계** | 휴머노이드 로봇 완제품 제조사, 임베디드 인텔리전스 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Figure AI 공식 사이트, 공개 투자 및 배치 보도, 제3자 사양 편집 |

## 회사 소개

Figure AI는 범용 휴머노이드 로봇에 특화된 스타트업으로, 산업 제조 현장을 주요 타겟으로 합니다. Figure 02는 이미 BMW 스파르탄버그 공장에서 시범 운영 중입니다.

Figure AI는 자체 개발한 Helix 다중 모드 AI 모델을 통해 로봇이 자연어 명령과 시각적 시연을 통해 새로운 작업을 학습할 수 있도록 합니다. Figure 02는 더 높은 연산 및 인식 능력을 갖추고 있으며, 반복적이고 위험한 인력 작업을 대체하는 것을 목표로 합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Figure 02 휴머노이드 로봇 | 산업용 휴머노이드 | Figure 02 | 자동차 제조, 물류, 창고 |
| Figure 03 휴머노이드 로봇 | 차세대 범용/가정용 | Figure 03 | 산업, 미래 가정 서비스 |

## 대표 제품

### Figure 02

> Figure 02: [공식 자료](https://www.figure.ai)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 168 cm (높이) | 공개 자료 |
| 무게 | 약 70 kg | 공개 자료 |
| 자유도 | 전신 28; 손 부문 별도 공개 없음 | Humanoid.guide 등 |
| 적재/토크 | 운반 약 20–25 kg | 공개 자료 |
| 속도/회전수 | 약 1.2 m/s (4.32 km/h) | 공개 자료 |
| 배터리 지속 시간 | 약 5시간 | 공개 자료 |
| 인터페이스/통신 | 듀얼 NVIDIA GPU 연산, 6×RGB 카메라, 음성 상호작용 | 공개 자료 |
| 가격 | 미공개 (시범 프로젝트 약 130,000 USD 추정) | 제3자 추정 |

**기술적 하이라이트**: Helix 다중 모드 AI, BMW 공장 배치 검증, 본체 일체형 배터리, 6×RGB 카메라 및 음성 상호작용, Figure 01 대비 3배 연산 성능.

**적용 시나리오**: 자동차 조립 라인 키팅, 자재 운반, 창고 분류.


### Figure 03

> Figure 03: [공식 자료](https://www.figure.ai)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 170 cm (높이) | 공개 보도 |
| 무게 | 약 60–70 kg | 공개 보도 |
| 자유도 | 40+; 손 부문 16×2 | 공개 보도 |
| 적재/토크 | 약 25 kg | 공개 보도 |
| 속도/회전수 | 약 1.2 m/s | 공개 보도 |
| 배터리 지속 시간 | 약 5+ 시간 (2.25 kWh) | 공개 보도 |
| 인터페이스/통신 | Helix VLA 모델, 음성 상호작용 | 공개 보도 |
| 가격 | 미공개 | - |

**기술적 하이라이트**: 더 높은 자유도의 손, 가정 및 산업을 위한 범용 설계, Helix VLA 엔드투엔드 추론.

**적용 시나리오**: 산업 제조, 미래 가정 지원, 소매 서비스.


## 공급망 위치

- **상류 핵심 부품/소재**: NVIDIA GPU 연산, 모터/감속기, 센서 및 배터리 팩 외부 구매 또는 맞춤 제작.
- **하류 고객/적용 시나리오**: BMW 스파르탄버그 공장, 물류 및 제조 기업.
- **주요 경쟁사/대상**: Tesla Optimus, Boston Dynamics Atlas, Agility Robotics Digit, Apptronik Apollo.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_figure_ai`
- 제품/플랫폼 엔터티: `ent_product_figure_ai_figure_02`, `ent_product_figure_ai_figure_03`
- 주요 관계:
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`)
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_03` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_03`)

## 참고 자료

1. [Figure AI 공식 사이트](https://www.figure.ai)
2. [Humanoid.guide Figure 02 사양](https://humanoid.guide/product/figure-02/)
3. [The Robot Report의 Figure 02 보도](https://www.therobotreport.com/figure-02-advances-humanoid-robotics-frontier)
