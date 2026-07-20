# SEW-EURODRIVE PS.F / PS.C 유성 서보 감속기 / SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [SEW-EURODRIVE(세우 드라이브) / SEW-EURODRIVE](../companies/company_sew_eurodrive.md) |
| **제품 카테고리** | 유성 서보 감속기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [SEW-EURODRIVE(세우 드라이브) 공식 홈페이지](https://www.sew-eurodrive.com) |

## 제품 개요

PS.F 및 PS.C 시리즈는 SEW-EURODRIVE가 서보 애플리케이션을 위해 출시한 저백래시 유성 감속기입니다. PS.F는 플랜지 중공축/실축 출력을, PS.C는 B5/B14 플랜지 실축 출력을 제공하며, 둘 다 CMP 동기 서보 모터와 결합하여 컴팩트한 구동 유닛을 구성할 수 있습니다.

이 시리즈는 감속비 3에서 100까지 일반적인 정수비를 포괄하며, 최대 출력 토크는 약 4,300 N·m, 보호 등급은 IP65까지 가능하며, SEW 인버터와 함께 사용하면 고정밀, 고다이내믹 위치 및 토크 제어를 구현할 수 있습니다.

## 제품 이미지

> SEW-EURODRIVE PS.F / PS.C 유성 서보 감속기 / SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor: [공식 자료](https://www.sew-eurodrive.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3:1 – 100:1 (정수비, 세분화 등급) | 제품 매뉴얼 |
| 정격 출력 토크 | 최대 약 4,300 N·m (시리즈 범위) | 제품 매뉴얼 |
| 입력 회전 속도 | 최대 6,000 rpm | 제품 매뉴얼 |
| 백래시 | ≤3 – 6 arcmin (시리즈/옵션) | 제품 매뉴얼 |
| 보호 등급 | IP65 (표준/옵션) | 제품 매뉴얼 |
| 설치 방식 | B5/B14 플랜지, 실축, 키홈 | 제품 매뉴얼 |
| 효율 | 단단 약 97% / 2단 약 94% | 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [SEW-EURODRIVE(세우 드라이브) / SEW-EURODRIVE](../companies/company_sew_eurodrive.md)
- **핵심 부품/기술 출처**: CMP 동기 서보 모터, 유성 기어, 베어링, 실, 브레이크, 엔코더
- **하위 애플리케이션/고객**: 산업용 로봇, 휴머노이드 로봇 관절, AGV 휠 구동, 포장 인쇄 장비

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_sew_psf_servo_gearmotor`
- 제조사 엔터티: `ent_company_sew_eurodrive`
- 주요 관계:
  - `rel_ent_company_sew_eurodrive_manufactures_ent_component_sew_psf_servo_gearmotor` (`ent_company_sew_eurodrive` --> `manufactures` --> `ent_component_sew_psf_servo_gearmotor`)

## 애플리케이션 시나리오

- **산업용 로봇**: 로봇 베이스, 어깨, 손목 관절 구동
- **휴머노이드 로봇**: 엉덩이, 무릎, 어깨 등 고토크 관절
- **CNC 공작 기계**: 공작 기계 이송, 공구 매거진, 턴테이블
- **기타 자동화**: 물류 컨베이어, 식품 포장, 섬유 기계

## 경쟁 비교

| 비교 항목 | PS.F / PS.C 유성 서보 감속기 | Lenze g500 | Bonfiglioli 300M |
|--------|------------------------|---------------|---------------|
| 핵심 장점 | 모듈식 유성+서보 모터, 글로벌 서비스 | 모션 제어 통합 솔루션 | 중부하 유성, 풍력 경험 |
| 백래시/정밀도 | ≤3–6 arcmin | 저백래시 옵션 가능 | 산업용 백래시 |
| 가격 수준 | 중고급 | 중고급 | 중고급 |
| 납기 | 보통 | 보통 | 보통 |

## 구매 및 배치 권장 사항

로봇 관절 토크와 회전 속도에 따라 PS.F 또는 PS.C를 선택하십시오. 정수 감속비와 엔코더 분해능의 매칭에 주의해야 하며, 고속 애플리케이션에서는 열 출력을 검증해야 합니다.

## 참고 자료

1. [SEW-EURODRIVE(세우 드라이브) 공식 홈페이지](https://www.sew-eurodrive.com)
2. [SEW-EURODRIVE Servo Gearmotors](https://www.sew-eurodrive.com)
3. [WAIC 2026 참가 보고](https://www.worldrobotconference.com)
