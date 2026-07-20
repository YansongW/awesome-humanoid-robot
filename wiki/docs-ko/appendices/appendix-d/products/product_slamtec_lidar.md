# SLAMTEC RPLIDAR A3 레이저 거리 측정 센서 / SLAMTEC RPLIDAR A3 Laser Range Scanner

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [SLAMTEC / SLAMTEC](../companies/company_slamtec.md) |
| **제품 카테고리** | 360° 2D 레이저 거리 측정 레이더 |
| **출시일** | 2018년부터 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [SLAMTEC 공식 홈페이지](https://www.slamtec.com) |

## 제품 개요

SLAMTEC RPLIDAR A3는 저비용, 고성능의 360° 2D 레이저 거리 측정 레이더입니다. 레이저 삼각 측정 원리와 자체 개발한 RPVision 3.0 고속 비전 거리 측정 엔진을 채택하여 샘플링 주파수는 최대 16,000회/초, 측정 반경은 최대 25m에 달합니다.

A3는 강화 모드와 실외 모드를 지원합니다. 강화 모드에서는 측정 반경과 샘플링 주파수가 최대치에 도달하며, 실외 모드에서는 더 강력한 태양광 간섭 저항 능력을 갖춥니다. 제품은 독창적인 광자기 융합(OPTMAG) 무선 전력 공급 및 광통신 기술을 채택하여 기존 슬립 링 마모 문제를 완전히 해결했으며, 수명은 최대 5년입니다. 4cm의 초슬림 본체와 190g의 무게로 서비스 로봇, 무인 차량, 대형 스크린 인터랙션 및 휴머노이드 로봇 내비게이션 등 다양한 시나리오에 매우 적합합니다.

## 제품 이미지

> SLAMTEC RPLIDAR A3: [공식 자료](https://www.slamtec.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 360° 2D 레이저 거리 측정 레이더 | 공식 datasheet |
| 거리 측정 원리 | 레이저 삼각 측정 | 공식 datasheet |
| 거리 측정 엔진 | RPVision 3.0 | 공식 datasheet |
| 스캔 각도 | 360° | 공식 datasheet |
| 측정 반경 | 25m (강화 모드 흰색 물체) / 20m (실외 모드 흰색 물체) | 공식 datasheet |
| 최소 측정 거리 | 0.2m | 공식 datasheet |
| 샘플링 주파수 | 16,000회/초 (강화 모드) / 10,000회/초 (실외 모드) | 공식 datasheet |
| 스캔 주파수 | 5 – 15Hz (일반 10Hz) | 공식 datasheet |
| 각도 분해능 | 0.225° | 공식 datasheet |
| 거리 측정 분해능 | ≤1% (≤12m); ≤2% (12m – 25m) | 공식 datasheet |
| 거리 측정 정밀도 | 1% (≤3m); 2% (3 – 5m); 2.5% (5 – 25m) | 공식 datasheet |
| 통신 인터페이스 | TTL UART | 공식 datasheet |
| 통신 보레이트 | 256,000 bps | 공식 datasheet |
| 공급 전압 | 5V | 공식 datasheet |
| 작동 전류 | 450 – 600mA | 공식 datasheet |
| 소비 전력 | 2.25 – 3W | 공식 datasheet |
| 크기 | 직경 76mm × 높이 41mm | 공식 datasheet |
| 무게 | 190g | 공식 datasheet |
| 작동 온도 | 0℃ – 40℃ | 공식 datasheet |
| 레이저 안전 등급 | Class 1 (인체 안전) | 공식 datasheet |
| 수명 | 광자기 융합 기술, 최대 5년 | 공식 datasheet |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [SLAMTEC / SLAMTEC](../companies/company_slamtec.md)
- **핵심 부품/기술 출처**: 자체 개발 RPVision 거리 측정 엔진, 광자기 융합 전력 공급 및 통신 기술; 레이저 발광기, 광전 검출기, 브러시리스 모터, 광학 렌즈, FPGA 외부 구매.
- **하위 응용/고객**: 서비스 로봇, 청소 로봇, 배송 로봇, 무인 차량, 휴머노이드 로봇, 대형 스크린 인터랙션, 측량 및 순찰.

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_slamtec_rplidar_a3`
- 제조사 엔터티: `ent_company_slamtec`
- 주요 관계:
  - `rel_ent_company_slamtec_manufactures_ent_component_slamtec_rplidar_a3` (`ent_company_slamtec` → `manufactures` --> `ent_component_slamtec_rplidar_a3`)

## 응용 시나리오

- **서비스 로봇**: 실내 내비게이션, 장애물 회피, SLAM 매핑 및 경로 계획.
- **휴머노이드 로봇**: 환경 인식, 위치 파악 및 매핑, 자율 보행.
- **무인 차량/AGV**: 저속 시나리오에서 장애물 감지 및 경계 인식.
- **대형 스크린 인터랙션**: 멀티 터치, 인터랙티브 프로젝션 및 공간 위치 파악.

## 경쟁 비교

| 비교 항목 | SLAMTEC RPLIDAR A3 | Hesai ET25 | RoboSense M1 Plus |
|--------|-----------------|-----------|------------------|
| 유형 | 2D 삼각 측정 레이더 | 반고체/차량 내 레이저 레이더 | 반고체 레이저 레이더 |
| 측정 반경 | 25m | 250m | 180m |
| 샘플링 주파수 | 16,000회/초 | >300만 포인트/초 | 미공개 |
| 시야각 | 360° (수평 단선) | 120°×25° | 미공개 |
| 가격 | 수백~수천 위안대 | 차량 규격 | 차량 규격 |
| 핵심 장점 | 저비용, 초슬림, 긴 수명 | 장거리 차량 규격, 차량 내 설치 | 차량 규격 양산 |

## 구매 및 배치 권장 사항

- 삼각 측정 레이더는 실외 강한 빛이나 어두운 색상 물체 시나리오에서 성능이 저하될 수 있으므로, 환경에 따라 강화 모드 또는 실외 모드를 선택해야 합니다.
- 설치 시 레이더 창이 가려지거나 먼지가 묻지 않도록 주의하고, 시동 전류 요구 사항을 충족하기 위해 5V 전원 공급이 안정적인지 확인해야 합니다.

## 참고 자료

1. [SLAMTEC 공식 홈페이지](https://www.slamtec.com)
2. [SLAMTEC RPLIDAR A3 제품 페이지](https://www.slamtec.com/cn/Lidar/A3)
3. [RPLIDAR A3M1 datasheet](https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LD310_SLAMTEC_rplidar_datasheet_A3M1_v1.9_cn.pdf)
4. [부록 D 기업 목록](../index-companies.md)
