# Figure 02

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Figure AI](../companies/company_figure_ai.md) |
| **제품 카테고리** | 범용 휴머노이드 로봇 |
| **출시일** | 2024년 8월 |
| **상태** | 기업 시범/제한적 배포 |
| **공식 사이트/출처** | [Figure AI 공식 사이트](https://www.figure.ai) |

## 제품 개요

Figure 02는 Figure AI가 출시한 2세대 범용 휴머노이드 로봇으로, 산업 제조 및 물류 현장을 대상으로 설계되었습니다. 본체는 무광 블랙 외관과 통합형 케이블 배치를 채택했으며, Figure 자체 개발 Helix VLA(Vision-Language-Action) AI 모델을 탑재하여 200Hz 주파수로 상반신을 제어하고, 수천 가지 미경험 물체를 제로샷으로 집을 수 있습니다.

Figure 02는 BMW Spartanburg 등 자동차 제조 현장에서 실제 작업 검증을 완료했으며, 주로 섀시 조립, 자재 운반 등 사람과 협업하는 공정을 담당합니다. 듀얼 NVIDIA RTX GPU 컴퓨팅 모듈은 Figure 01 대비 약 3배의 엣지 추론 성능을 제공하며, 6개의 RGB 카메라와 다중 모드 센서가 24시간 환경 인식을 지원합니다.

## 제품 이미지

> Figure 02: [공식 자료](https://www.figure.ai)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 168 cm(높이) | 공개 사양 |
| 무게 | 약 70 kg | 공개 사양 |
| 자유도(본체) | 28 DOF(손 16 DOF/쌍) | 공개 사양 |
| 주요 성능 지표 | 손 부하 25 kg; 본체 운반 20 kg | 공개 사양 |
| 보행 속도 | 약 1.2 m/s | 공개 사양 |
| 배터리 지속 시간 | 약 5시간 | 공개 사양 |
| 배터리 용량 | 2.25 kWh(본체 통합) | 공개 사양 |
| 컴퓨팅 플랫폼 | 듀얼 NVIDIA RTX GPU 모듈 | Figure AI |
| 가격 | 미공개(업계 추정 약 130,000 USD) | 제3자 추정 |

## 공급망 위치

- **제조사**: [Figure AI](../companies/company_figure_ai.md)
- **핵심 부품/기술 출처**: NVIDIA GPU 컴퓨팅 모듈, 자체 개발 Helix VLA 모델, OpenAI 음성 인터랙션, 6×RGB 카메라 및 깊이 인식 모듈.
- **하위 응용/고객**: BMW 제조 현장, 물류 창고, 자동차 조립 라인.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_figure_ai_figure_02`
- 제조사 엔터티: `ent_company_figure_ai`
- 주요 관계:
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02`(`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`)

## 응용 시나리오

- **자동차 제조**: BMW Spartanburg 등 현장에서 섀시 조립, 와이어 하네스 설치 및 자재 운반 수행.
- **창고 물류**: 표준화된 상자의 분류, 운반 및 생산 라인 보충.
- **산업 협업**: 인간 작업자와 함께 정밀한 손 작업이 필요한 조립 및 검사 작업 수행.

## 경쟁 비교

| 비교 항목 | Figure 02 | Tesla Optimus Gen 3 | Agility Digit |
|--------|-----------|---------------------|---------------|
| 포지셔닝 | 산업 제조 휴머노이드 | 범용/산업 휴머노이드 | 물류 창고 휴머노이드 |
| AI 아키텍처 | Helix VLA | FSD 파생 신경망 | 독점 인식/계획 스택 |
| 배터리 지속 시간 | 약 5시간 | 약 2–4시간(추정) | 약 4시간 |
| 핵심 강점 | 엣지 VLA, BMW 배포, 손 부하 | 제조 규모 목표, 비용 관리 | 물류 배포 성숙도 |

## 구매 및 배포 권장 사항

- Figure 02는 현재 주로 기업 시범 단계에 있으므로, Figure AI에 직접 연락하여 공장 현장 적용 가능성을 평가하는 것이 좋습니다.
- 배포 전 Helix VLA 모델의 대상 작업물에 대한 일반화 능력을 확인하고, 훈련 데이터 수집 프로세스를 계획해야 합니다.

## 참고 자료

1. [Figure AI 공식 사이트](https://www.figure.ai)
2. [Robozaps – Figure 02 Review](https://blog.robozaps.com/b/figure-02-review)
3. [Humanoid.Guide – Figure 02](https://humanoid.guide/product/figure-02/)
4. [The Robot Report – Figure BMW Deployment](https://www.therobotreport.com)
