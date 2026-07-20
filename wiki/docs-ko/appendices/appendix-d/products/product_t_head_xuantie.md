# 평두거 현철 C920 / T-Head Xuantie C920

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 파라미터는 공식 공개 자료 기준이며, 누락 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [평두거 반도체 / T-Head](../companies/company_t_head.md) |
| **제품 카테고리** | RISC-V 고성능 프로세서 IP |
| **출시 시기** | 현철 C920은 차세대 고성능 RISC-V 프로세서 |
| **상태** | 상용 라이선스 |
| **공식 사이트/출처** | 평두거 공식 사이트, 알리바바 클라우드 치펑 컨퍼런스 자료 |

## 제품 개요

평두거 현철 C920은 평두거 반도체가 출시한 고성능 RISC-V 애플리케이션 프로세서 IP로, 엣지 AI, 산업 제어, 로봇 및 AIoT 등의 시나리오를 대상으로 합니다.

현철 C920은 RV64GC 명령어 세트를 기반으로 RISC-V Vector 1.0 확장을 지원하며, 12단 비순차 슈퍼스칼라 파이프라인을 채택하여 높은 클럭, 높은 연산 성능 및 우수한 전력 효율을 제공합니다. 개방형 RISC-V 생태계와 맞춤형 특성을 통해 칩 고객은 로봇 제어, 비전 처리 및 AI 추론 등의 작업에 대해 심층 최적화를 수행할 수 있습니다.

## 제품 이미지

> 평두거 현철 C920: [공식 자료](https://www.t-head.cn)를 방문하여 확인하세요.

## 사양 파라미터 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 프로세서 IP | 현철 C920 | 평두거 공식 사이트 |
| 명령어 세트 | RISC-V RV64GC + Vector 1.0 | 평두거 공개 자료 |
| 마이크로아키텍처 | 12단 비순차 슈퍼스칼라 | 평두거 공개 자료 |
| 클럭 속도 | 최대 3 GHz (공개 보도 기준) | 공개 보도 |
| 연산 성능 | 미공개 | - |
| 캐시 | 다중 레벨 캐시 지원 | 평두거 공개 자료 |
| 버스 인터페이스 | AXI / ACE | 평두거 공개 자료 |
| 확장 지원 | AI 가속기, 보안 확장 통합 가능 | 평두거 공개 자료 |
| 전력 소비 | 구체적인 구현에 따라 다름 | 평두거 공개 자료 |
| 가격 | IP 라이선스, 미공개 | - |

## 공급망 위치

- **제조사**: [평두거 반도체 / T-Head](../companies/company_t_head.md)
- **핵심 부품/기술 출처**: 자체 개발 RISC-V 코어, EDA 도구, 라이선스 고객 웨이퍼 파운드리/패키징 테스트.
- **하위 응용/고객**: 칩 설계 회사, AIoT 업체, 자동차 전자, 산업 제어, 로봇 칩 업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_t_head_xuantie_c920`
- 부품 엔터티: `ent_component_t_head_xuantie_c920_ip`
- 제조사 엔터티: `ent_company_t_head`
- 주요 관계:
  - `rel_ent_company_t_head_manufactures_ent_product_t_head_xuantie_c920` (`ent_company_t_head` → `manufactures` → `ent_product_t_head_xuantie_c920`)
  - `rel_ent_company_t_head_manufactures_ent_component_t_head_xuantie_c920_ip` (`ent_company_t_head` → `manufactures` → `ent_component_t_head_xuantie_c920_ip`)
  - `ent_product_t_head_xuantie_c920` -- `uses` --> `ent_component_t_head_xuantie_c920_ip`

## 응용 시나리오

- **로봇 메인 컨트롤러 MCU/MPU**: 로봇의 모션 제어, 통신 및 작업 스케줄링을 위한 핵심 프로세서.
- **엣지 AI 컴퓨팅**: NPU 통합 후 디바이스 측 이미지 인식, 음성 처리 및 센서 퓨전에 사용.
- **산업 제어 및 AIoT**: 스마트 제조, 스마트 홈, 웨어러블 디바이스에 고효율 컴퓨팅 제공.

## 경쟁 비교

| 비교 항목 | 현철 C920 | ARM Cortex-A78 | SiFive P550 |
|--------|------|------|------|
| 명령어 세트 | RISC-V | ARM | RISC-V |
| 생태계 | 평두거/오픈소스 RISC-V | ARM 성숙 생태계 | SiFive 생태계 |
| 맞춤화 | 높음 | 중간 | 높음 |
| 라이선스 모델 | IP 라이선스 | IP 라이선스 | IP 라이선스 |

## 구매 및 배포 권장 사항

- 대상 소프트웨어 스택의 RISC-V Vector 및 권한 아키텍처 지원 여부를 평가하세요.
- 성능, 전력 소비 및 면적 목표에 따라 C920 구성을 선택하고 AI 가속기 통합 공간을 확보하세요.
- 평두거 공식 채널을 통해 IP 패키지, 레퍼런스 디자인 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 평두거 반도체 / T-Head](../companies/company_t_head.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [평두거 공식 사이트](https://www.t-head.cn)
2. [평두거 현철 시리즈](https://www.t-head.cn/product/)
3. 알리바바 클라우드 치펑 컨퍼런스 공개 자료
