# Amphenol / Amphenol

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 암페놀 |
| **영문명** | Amphenol |
| **본사** | 미국 코네티컷주 월링포드 (Wallingford) |
| **설립 연도** | 1932 |
| **공식 웹사이트** | [https://www.amphenol.com](https://www.amphenol.com) |
| **공급망 단계** | 커넥터, 접속 부품, 안테나, 케이블 어셈블리 |
| **기업 속성** | 상장 기업 (NYSE: APH) |
| **모회사/소속 그룹** | 독립 상장 |
| **데이터 출처** | 공식 웹사이트, 연례 보고서, 제품 데이터시트 |

## 회사 소개

Amphenol은 세계 2위의 커넥터 제조업체로, 군사/항공, 통신, 자동차 및 산업 시장을 대상으로 제품을 공급합니다. 고밀도, 고신뢰성 커넥터 및 케이블 어셈블리는 로봇 컨트롤러, 센서, 서보 시스템 및 통신 모듈에 사용됩니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Minitek MicroSpace | 1.27 mm 컴팩트 커넥터 | Minitek MicroSpace | 자동차 전자, 로봇 컨트롤러 |
| M12 / M8 원형 커넥터 | 산업 통신 및 센서 | Amphenol M12 X-Code | 산업 자동화, 로봇 |
| RF 및 안테나 | 무선 연결 | 5G/IoT 안테나 | 이동 로봇, AGV/AMR |

## 대표 제품

### Amphenol Minitek MicroSpace 1.27 mm 와이어-투-보드 커넥터

> Amphenol Minitek MicroSpace 1.27 mm 와이어-투-보드 커넥터: [공식 자료](https://www.amphenol.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 핀 수 | 2 – 40 (선택 가능) | 공식 카탈로그 |
| 정격 전류 | 미공개 | 공식 데이터시트 |
| 정격 전압 | 미공개 | 공식 데이터시트 |
| 보호 등급 | IP20 | 제품 자료 |
| 피치 | 1.27 mm | 공식 카탈로그 |
| 적용 시나리오 | 자동차 전자, 로봇 컨트롤러, 센서 인터페이스 | 제품 자료 |
| 가격 | 미공개 | 미공개 |

**기술적 특징**: 1.27 mm 컴팩트 피치로 공간 제약이 있는 설계에 적합하며, 자동 조립 및 다양한 도금을 지원합니다.

**적용 시나리오**: 로봇 제어 보드, 모터 드라이브, BMS, 산업 컨트롤러, 차량용 ECU.

### Amphenol M12 X-Code 8핀 원형 커넥터

> Amphenol M12 X-Code 8핀 원형 커넥터: [공식 자료](https://www.amphenol.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 핀 수 | 8 | 공식 카탈로그 |
| 정격 전류 | 미공개 | 공식 데이터시트 |
| 정격 전압 | 미공개 | 공식 데이터시트 |
| 보호 등급 | IP67 | 제품 자료 |
| 전송 속도 | 10 GbE | 제품 자료 |
| 적용 시나리오 | 산업용 이더넷, 로봇 센서, 비전 시스템 | 제품 자료 |
| 가격 | 미공개 | 미공개 |

**기술적 특징**: M12 표준 인터페이스, 산업용 방수 및 방진, 고속 이더넷 및 고진동 환경 지원.

**적용 시나리오**: 협동 로봇, 산업용 로봇, AGV/AMR, 산업용 카메라, LiDAR.

## 공급망 위치

- **상류 핵심 부품/재료**: 구리 합금, 고성능 플라스틱, 도금 재료, 케이블, 자성 재료
- **하류 고객/적용 시나리오**: 자동차, 통신, 산업 자동화, 로봇, 항공 우주
- **주요 경쟁사/대비 대상**: TE Connectivity, Molex, Hirose, JAE, J.S.T.

## 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_amphenol`
- 제품 엔티티: `ent_product_amphenol_minitek_microspace`
- 부품 엔티티: `ent_component_amphenol_minitek_microspace`
- 주요 관계:
  - `rel_ent_company_amphenol_manufactures_ent_product_amphenol_minitek_microspace` (`ent_company_amphenol` → `manufactures` → `ent_product_amphenol_minitek_microspace`)
  - `rel_ent_company_amphenol_manufactures_ent_component_amphenol_minitek_microspace` (`ent_company_amphenol` → `manufactures` → `ent_component_amphenol_minitek_microspace`)

## 참고 자료

1. [공식 웹사이트](https://www.amphenol.com)
2. 제품 데이터시트 및 공개 기술 보도
3. [부록 D 제품 목록](../index-products.md)
