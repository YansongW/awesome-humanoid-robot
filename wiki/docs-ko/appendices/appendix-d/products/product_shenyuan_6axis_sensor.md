# 신위안성 MLL 시리즈 6축 힘 센서 / Shenyuansheng MLL Series 6-Axis Force Sensor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [신위안성 과학기술 / Shenyuansheng](../companies/company_shenyuan.md) |
| **제품 카테고리** | 알루미늄 합금 아날로그 6축 힘/토크 센서 |
| **출시 시간** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [신위안성 MLL 시리즈 6축 힘 센서 제품/자료 페이지](http://www.nbit6d.com/product/687.html) |

## 제품 개요

신위안성 MLL 시리즈는 과학 기기, 정밀 테스트 및 로봇 응용 분야를 위해 설계된 알루미늄 합금 아날로그 6축 힘 센서로, 직교하는 세 방향의 힘과 토크를 동시에 측정할 수 있습니다. 제품은 높은 강성, 높은 분해능 및 낮은 결합 오차 특성을 가지며, NST 시리즈 데이터 수집기를 선택하여 디지털 출력 및 실시간 분석을 구현할 수 있습니다.

## 제품 이미지

> 신위안성 MLL 시리즈 6축 힘 센서: [공식 자료](http://www.nbit6d.com/product/687.html)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 알루미늄 합금 아날로그 6축 힘 센서 | 신위안성 공식 홈페이지 |
| 힘 측정 범위 (Fx/Fy/Fz) | 50 / 50 / 100 N (대표 모델) | 신위안성 공식 홈페이지 |
| 토크 측정 범위 (Mx/My/Mz) | 2 / 2 / 4 Nm (대표 모델) | 신위안성 공식 홈페이지 |
| 정밀도 | ≤ 0.5% FS | 신위안성 공식 홈페이지 |
| 분해능 | 24 bit (수집기 연동 시) | 신위안성 공식 홈페이지 |
| 과부하 용량 | ≥ 300% FS | 신위안성 공식 홈페이지 |
| 결합 오차 | ≤ 2% FS | 신위안성 공식 홈페이지 |
| 전원 공급 | 5 – 24 VDC | 신위안성 공식 홈페이지 |
| 출력 | 아날로그 / USB / RS485 (수집기 연동 시) | 신위안성 공식 홈페이지 |
| 샘플링 주파수 | 최대 1000 Hz | 신위안성 공식 홈페이지 |
| 작동 온도 | 0℃ – +60℃ | 신위안성 공식 홈페이지 |
| 무게 | 약 200 g (모델에 따라 다름) | 신위안성 공식 홈페이지 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [신위안성 과학기술 / Shenyuansheng](../companies/company_shenyuan.md)
- **핵심 부품/기술 출처**: 항공 알루미늄 합금, 스트레인 게이지, 신호 조정 칩, 케이블 및 커넥터
- **하류 응용/고객**: 협동 로봇, 휴머노이드 로봇, 의료 로봇, 항공우주 테스트, 대학 연구

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_shenyuan_mll_6axis_sensor`
- 부품 엔터티: `ent_component_shenyuan_mll_sensor_core`
- 제조사 엔터티: `ent_company_shenyuan`
- 주요 관계:
  - `rel_ent_company_shenyuan_manufactures_ent_product_shenyuan_mll_6axis_sensor` (`ent_company_shenyuan` → `manufactures` → `ent_product_shenyuan_mll_6axis_sensor`)
  - `rel_ent_company_shenyuan_manufactures_ent_component_shenyuan_mll_sensor_core` (`ent_company_shenyuan` → `manufactures` → `ent_component_shenyuan_mll_sensor_core`)
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

## 응용 시나리오

- **협동 로봇 드래그 티칭, 휴머노이드 로봇 손목/발목 힘 제어, 의료 수술 힘 피드백, 3C 조립, 과학 실험**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 권장 사항

- 목표 응용 분야의 분해능, 측정 범위, 정밀도 또는 연산 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 신위안성 과학기술 / Shenyuansheng](../companies/company_shenyuan.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [신위안성 과학기술 공식 홈페이지](https://www.shenyuansheng.com)
2. [신위안성 MLL 시리즈 6축 힘 센서 제품/자료 페이지](http://www.nbit6d.com/product/687.html)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
