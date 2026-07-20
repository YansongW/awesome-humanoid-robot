# Infineon Technologies

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 인피니언 테크놀로지스 주식회사 |
| **영문명** | Infineon Technologies AG |
| **본사** | 독일 노이비베르크 (Neubiberg) |
| **설립일** | 1999년 (지멘스 반도체 부문에서 분사) |
| **공식 웹사이트** | [https://www.infineon.com](https://www.infineon.com) |
| **공급망 단계** | 전력 반도체, 센서, 마이크로컨트롤러, 보안 칩 |
| **기업 속성** | 상장 기업 (프랑크푸르트 증권거래소: IFX) |
| **모회사/소속 그룹** | 없음 (독립 상장) |
| **데이터 출처** | Infineon 공식 웹사이트 보도자료, CoolSiC 제품 페이지 |

## 회사 소개

인피니언은 글로벌 선도적인 반도체 솔루션 공급업체로, 자동차 전자 및 전력 반도체 시장 점유율에서 선두를 차지하고 있습니다.

CoolSiC™ 탄화규소 MOSFET 및 IGBT 모듈은 전기차 구동, 태양광 인버터, 에너지 저장 컨버터 및 산업용 드라이브에 널리 사용됩니다. 휴머노이드 로봇의 경우, 고효율 모터 구동 인버터와 전원 관리 칩은 배터리 지속 시간과 동적 응답성을 향상시키는 핵심 부품입니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 전력 MOSFET | 고효율 탄화규소 전력 소자 | CoolSiC™ MOSFET | 전기 구동 인버터, DC/DC, 충전기 |
| IGBT 모듈 | 중대전력 모터 구동 | HybridPACK / EconoDUAL | 신에너지 자동차, 산업용 드라이브 |
| 게이트 드라이버 | 전력 소자 구동 | EiceDRIVER | 인버터, 전원 공급 장치 |

## 대표 제품

### CoolSiC™ MOSFET 1200 V / 62 mm 모듈

![CoolSiC](https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/)

> 이미지 출처: Infineon 공식 웹사이트. 링크가 유효하지 않거나 누락된 경우, 공식 공개 이미지 URL로 대체하십시오.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 패키지 | 62 mm 하프 브리지 모듈 | Infineon 보도자료 |
| 전압 등급 | 1200 V / 2000 V | Infineon 보도자료 |
| 온 저항 | 1 mΩ / 2 mΩ / 5 mΩ 등 | Infineon 보도자료 |
| 정격 전류 | 180 A / 420 A / 560 A | Infineon 보도자료 |
| 동작 접합 온도 | 150 °C (연속) | Infineon 보도자료 |
| 토폴로지 | 하프 브리지 | Infineon 보도자료 |
| 가격 | 미공개 | 미공개 |

**기술 하이라이트**: M1H 트렌치 게이트 SiC MOSFET 기술 기반으로, 넓은 게이트 전압 창, 낮은 스위칭 손실 및 높은 전력 밀도를 제공하며, 250 kW 이상의 중전력 애플리케이션에 적합합니다.

**적용 시나리오**: 전기 구동 인버터, 에너지 저장 컨버터, 산업용 서보 드라이브, 휴머노이드 로봇 관절 모터 구동.

## 휴머노이드 로봇과의 연관성

- 배터리, 전력 반도체 및 첨단 소재는 휴머노이드 로봇이 장시간 배터리 지속 시간, 높은 동적 성능 및 경량화를 실현하기 위한 공통 기반입니다.
- 산업용 로봇 및 자동화 생산 라인은 휴머노이드 로봇의 완제품 조립, 테스트 및 양산에 재사용 가능한 제조 역량을 제공합니다.

## 공급망 위치

- **상류 핵심 부품/소재**: SiC 기판 (SICC, Wolfspeed), 에피택셜 웨이퍼, 패키징 소재, 실리콘 웨이퍼.
- **하류 고객/적용 시나리오**: 자동차 OEM, 태양광/에너지 저장 인버터 제조사, 산업 자동화 제조사.
- **주요 경쟁사/대응 기업**: STMicroelectronics, Wolfspeed, ROHM, Onsemi, Mitsubishi Electric.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_infineon`
- 제품 엔터티: `ent_component_infineon_coolsic_mosfet`
- 주요 관계:
  - `ent_company_infineon` -- `manufactures` --> `ent_component_infineon_coolsic_mosfet`

## 참고 자료

1. [Infineon 공식 웹사이트](https://www.infineon.com)
2. [Infineon CoolSiC MOSFET 제품 페이지](https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/)
3. [CoolSiC 62mm 모듈 보도자료](https://www.infineon.com/cms/en/about-infineon/press/market-news/2023/INFGIP202311-024.html)
