# 키엔스 SR-X100 AI 코드 리더 / Keyence SR-X100 AI Code Reader

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [키엔스 / Keyence](../companies/company_keyence.md) |
| **제품 카테고리** | 산업용 AI 코드 리더/비전 센서 |
| **출시일** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [키엔스 공식 홈페이지](https://www.keyence.com) |

## 제품 개요

키엔스 SR-X100은 표준형 140만 화소 AI 코드 리더로, CMOS 이미지 센서, 고휘도 적색 LED 조명 및 자동 초점 기구를 내장하여 QR 코드, DataMatrix, PDF417, Aztec 및 일반적인 1차원 바코드를 빠르게 읽을 수 있습니다.

SR-X100은 70 – 1000 mm의 판독 거리를 지원하며, 최소 QR 코드 해상도는 0.024 mm에 달합니다. 또한 Ethernet, RS-232C 및 USB 2.0 등 다양한 통신 인터페이스를 제공하며, EtherNet/IP, PROFINET, MC 프로토콜 및 OPC UA와 호환됩니다. IP65/IP67 보호 등급과 컴팩트한 본체(약 180 g)는 전자, 자동차, 물류 및 로봇 등 까다로운 산업 환경에 적합합니다.

## 제품 이미지

> Keyence SR-X100: [공식 자료](https://www.keyence.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 표준형 AI 코드 리더 | 공식 datasheet |
| 이미지 센서 | CMOS 이미지 센서 | 공식 datasheet |
| 화소 | 1360 × 1024 (140만 화소) | 공식 datasheet |
| 초점 | 자동 초점 | 공식 datasheet |
| 조명 광원 | 고휘도 적색 LED | 공식 datasheet |
| 표시기 광원 | 고휘도 녹색 LED | 공식 datasheet |
| 지원 2차원 코드 | QR, MicroQR, DataMatrix, PDF417, Aztec 등 | 공식 datasheet |
| 지원 1차원 코드 | CODE39, CODE128, EAN/UPC 등 | 공식 datasheet |
| 최소 해상도 (2차원 코드) | 0.024 mm | 공식 datasheet |
| 최소 해상도 (바코드) | 0.082 mm | 공식 datasheet |
| 판독 거리 | 70 – 1000 mm | 공식 datasheet |
| 시야 범위 | 74 mm × 55 mm (거리 300 mm 시) | 공식 datasheet |
| 제어 입력/출력 | 2점 입력 / 3점 출력 | 공식 datasheet |
| 통신 인터페이스 | Ethernet (100BASE-TX), RS-232C, USB 2.0 | 공식 datasheet |
| 지원 프로토콜 | TCP/IP, EtherNet/IP, PROFINET, MC 프로토콜, OPC UA 등 | 공식 datasheet |
| 전원 공급 | 24 VDC +25%/-20% | 공식 datasheet |
| 소비 전력 | 약 650 mA | 공식 datasheet |
| 보호 등급 | IP65 / IP67 | 공식 datasheet |
| 작동 온도 | 0℃ – +45℃ | 공식 datasheet |
| 무게 | 약 180 g | 공식 datasheet |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [키엔스 / Keyence](../companies/company_keyence.md)
- **핵심 부품/기술 출처**: 자체 개발 이미지 처리 알고리즘 및 자동 초점 기술; CMOS 센서, LED 조명, 광학 렌즈, 통신 칩은 외부 조달.
- **하위 응용/고객**: 전자 제조, 자동차, 물류 창고, 식품 의약품, 로봇 OEM.

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_keyence_sr_x100`
- 제조사 엔터티: `ent_company_keyence`
- 주요 관계:
  - `rel_ent_company_keyence_manufactures_ent_component_keyence_sr_x100` (`ent_company_keyence` → `manufactures` --> `ent_component_keyence_sr_x100`)

## 응용 시나리오

- **전자 제조**: PCB QR 코드 판독, SMT 추적, 부품 식별 인식.
- **물류 창고**: 패키지 바코드 고속 스캔, 분류 라인 대량 코드 판독.
- **자동차 추적**: 부품 레이저 마킹, 조립 공정 추적.
- **식품 의약품**: 포장 배치 번호, 유통기한 OCR 및 추적 관리.

## 경쟁 비교

| 비교 항목 | 키엔스 SR-X100 | Cognex DataMan 260 | 하이크로봇 MV-ID |
|--------|----------------|--------------------|------------------|
| 화소 | 140만 | 다중 모델 | 다중 모델 |
| 판독 거리 | 70 – 1000 mm | 모델에 따라 다름 | 모델에 따라 다름 |
| 최소 해상도 (2차원 코드) | 0.024 mm | 모델에 따라 다름 | 모델에 따라 다름 |
| 통신 프로토콜 | EtherNet/IP, PROFINET, OPC UA 등 | 풍부함 | 풍부함 |
| 보호 등급 | IP65/IP67 | IP65/IP67 | 모델에 따라 다름 |
| 핵심 장점 | 자동 초점, FA 생태계 통합 | 딥러닝 코드 판독 | 비용 우위, 현지화 |

## 선정 및 배포 제안

- 선정 시 바코드 유형, 최소 모듈 크기, 판독 거리 및 생산 라인 속도를 확인하고 현장 조명 및 진동 영향을 검증하십시오.
- 저대비, 반사 또는 손상된 바코드의 경우 내장 AI 필터 버전의 SR-X300 시리즈를 평가할 수 있습니다.

## 참고 자료

1. [키엔스 공식 홈페이지](https://www.keyence.com)
2. [키엔스 SR-X100 제품 페이지](https://www.keyence.com.cn/products/barcode/barcode-readers/sr-x/models/sr-x100/)
3. [키엔스 SR-X 시리즈 사양](https://www.keyence.com.my/products/barcode/barcode-readers/sr-x/specs/)
4. [부록 D 기업 디렉토리](../index-companies.md)
