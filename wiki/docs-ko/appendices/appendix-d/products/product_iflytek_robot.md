# iFlytek 로봇

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [iFlytek / iFlytek](../companies/company_iflytek.md) |
| **제품 카테고리** | 구현 지능 로봇/서비스 로봇 |
| **출시 시간** | 2023–2024년 점진적으로 관련 솔루션 출시 |
| **상태** | 솔루션/협력 개발 중 |
| **공식 홈페이지/출처** | 본문 참고 자료 참조 |

## 제품 개요

iFlytek 로봇 솔루션은 iFlytek Spark 대형 모델과 로봇 슈퍼 브레인을 핵심으로 하며, 선도적인 음성 상호작용, 자연어 이해 및 다중 모드 인식 능력을 결합하여 서비스 로봇, 노인 돌봄, 교육, 안내 등 시나리오에 지능체 두뇌를 제공합니다. 회사는 운동 제어 및 완제품 측면에서 주로 파트너와 공동 개발하며, "두뇌"와 상호작용 능력 강화를 강조합니다.

## 제품 이미지

> iFlytek 로봇: [공식 자료](https://www.iflytek.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 핵심 능력 | 음성 인식, 자연어 이해, 다중 모드 상호작용, 작업 계획 | iFlytek 공식 홈페이지 |
| 두뇌 플랫폼 | iFlytek Spark 대형 모델 + 로봇 슈퍼 브레인 | iFlytek 공개 자료 |
| 음성 상호작용 | 원거리 음성 수집, 방언 인식, 다중 턴 대화 | iFlytek 공개 자료 |
| 시각 이해 | iFlytek Spark 다중 모드 능력 결합 | 공개 보도 |
| 운동 제어 | 완제품 파트너와 공동 개발 | 미공개 |
| 배포 방식 | 클라우드 + 엣지 | iFlytek 공식 홈페이지 |
| 대표 시나리오 | 안내, 돌봄, 교육, 의료 | 공개 보도 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [iFlytek / iFlytek](../companies/company_iflytek.md)
- **핵심 부품/기술 출처**: AI 칩/서버, 마이크 어레이, 카메라 모듈, 완제품 파트너.
- **하위 응용/고객**: 서비스 로봇 OEM, 노인 요양 기관, 교육 기관, 의료 기관, 전시장/행정.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_iflytek_robot`
- 제조사 엔터티: `ent_company_iflytek`
- 주요 관계:
  - `rel_ent_company_iflytek_manufactures_ent_product_iflytek_robot` (`ent_company_iflytek` → `manufactures` → `ent_product_iflytek_robot`)
  - `ent_product_iflytek_robot` -- `uses` --> `ent_product_iflytek_xinghuo`
  - `ent_product_iflytek_robot` -- `uses` --> `ent_component_voice_array`

## 응용 시나리오

- **전시장 안내**: 음성 및 시각 기반 환영, 설명, 질의응답.
- **노인 돌봄**: 감정 동반, 건강 알림, 긴급 호출 연동.
- **교육 상호작용**: AI 교사, 프로그래밍 교육, 어린이 동반.

## 경쟁 비교

| 비교 항목 | iFlytek 로봇 | SenseTime 구현 솔루션 | UBTECH Walker |
|--------|------|------|------|
| 핵심 강점 | 음성 상호작용 및 중국어 대형 모델 | 시각 및 다중 모드 | 완제품 및 운동 제어 |
| 모드 | 두뇌+생태 협력 | 모델+인식 솔루션 | 자체 개발 완제품 |
| 시나리오 | 서비스/노인 돌봄/교육 | 산업/서비스 | 교육/상업 |

## 구매 및 배포 권장 사항

- 연산 능력/정밀도/시나리오 요구 사항에 따라 해당 모델을 선택하고, 공식 지원 도구 체인 및 생태 호환성을 우선 고려하세요.
- 배포 전 전원 공급, 방열, 기계 인터페이스 및 통신 프로토콜이 완제품 요구 사항을 충족하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: iFlytek / iFlytek](../companies/company_iflytek.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [iFlytek / iFlytek 공식 제품/회사 페이지](https://www.iflytek.com)
2. [iFlytek 공식 홈페이지](https://www.iflytek.com)
3. iFlytek Spark 대형 모델 발표회
