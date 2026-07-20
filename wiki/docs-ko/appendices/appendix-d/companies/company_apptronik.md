# Apptronik / Apptronik

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Apptronik |
| **영문명** | Apptronik |
| **본사** | 미국 텍사스주 오스틴 |
| **설립일** | 2016 |
| **공식 웹사이트** | [https://apptronik.com](https://apptronik.com) |
| **공급망 단계** | 범용 휴머노이드 로봇, NASA 협력 배경 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Apptronik 공식 웹사이트, Apollo 제품 페이지, 공개 투자 및 협력 보도 |

## 회사 소개

Apptronik은 NASA Valkyrie 프로젝트에서 성장했으며, Apollo는 산업 물류 및 제조를 대상으로 하며 모듈식 베이스와 핫스왑 배터리를 지원합니다.

Apollo는 모듈식 설계를 채택하여 상체를 이족 보행 다리, 바퀴형 베이스 또는 고정 기둥에 장착할 수 있어 다양한 작업 환경에 적응합니다. 회사는 Mercedes-Benz, GXO, NASA 등과 협력하여 시범 사업을 추진하고 있습니다.

Apptronik의 역사는 NASA의 Valkyrie 휴머노이드 로봇 프로젝트로 거슬러 올라가며, 팀은 우주 등급 액추에이터, 고출력 밀도 관절 및 안전 협력 제어 분야에서 경험을 축적했습니다. Apollo 완제품 외에도 Apptronik은 타사에 맞춤형 액추에이터 및 관절 모듈을 제공합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Apollo 휴머노이드 로봇 | 산업/물류 휴머노이드 | Apollo | 제조, 창고, 물류 |
| Apollo 소프트웨어 스택 | 작업 계획 및 인간-로봇 상호작용 | Apptronik SDK | 현장 배치, 신속한 작업 전환 |
| 로봇 액추에이터/관절 | 핵심 부품 | 맞춤형 액추에이터 | 타사 로봇, 우주 항공 |

## 대표 제품

### Apptronik Apollo

> Apptronik Apollo: [공식 자료](https://apptronik.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 173 cm (높이) | 공개 자료 |
| 무게 | 약 72.6–73 kg | 공개 자료 |
| 자유도 | 71 | 공개 자료 |
| 하중/토크 | 약 25 kg | 공개 자료 |
| 속도/회전 속도 | 약 3.4–5.4 km/h (출처에 따라 다름) | 공개 자료 |
| 배터리 지속 시간 | 배터리당 약 4시간, 핫스왑 지원으로 일 22시간 | 공개 자료 |
| 인터페이스/통신 | NVIDIA Jetson AGX Orin + Orin NX, Apptronik SDK | 공개 자료 |
| 가격 | 미공개 (대량 생산 목표 < 50,000 USD) | 공개 보도 |

**기술적 특징**: 높은 하중, 핫스왑 배터리, 모듈식 이동 베이스 (이족/바퀴/기둥), 힘 제어 안전 아키텍처, NASA 협력 배경.

**적용 시나리오**: 자동차 제조, 창고 운반, 물류 키팅, 우주 항공 및 지상 응용.

Apollo의 힘 제어 아키텍처와 모듈식 베이스는 작업 요구에 따라 이족 보행, 바퀴형 및 고정 기둥 사이를 전환할 수 있어 배치 및 개조 비용을 절감합니다. 소프트웨어 스택은 자연어 명령과 시각 유도 파지를 지원하여 비전문 운영자가 신속하게 배치할 수 있도록 합니다.

> 참고: Apollo는 현재 기업 시범 프로젝트를 통해서만 제공되며, 구체적인 견적은 Apptronik에 직접 문의해야 합니다.

## 공급망 위치

- **상류 핵심 부품/소재**: NVIDIA 컴퓨팅 플랫폼, 모터/선형 액추에이터, 센서, 구조 부품.
- **하류 고객/적용 시나리오**: Mercedes-Benz, GXO Logistics, NASA, Google.
- **주요 경쟁사/대상**: Tesla Optimus, Figure 02, Boston Dynamics Atlas, Agility Robotics Digit.

## 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_apptronik`
- 제품/플랫폼 엔티티: `ent_product_apptronik_apollo`
- 주요 관계:
  - `rel_ent_company_apptronik_manufactures_ent_product_apptronik_apollo` (`ent_company_apptronik` → `manufactures` → `ent_product_apptronik_apollo`)

## 참고 자료

1. [Apptronik 공식 웹사이트](https://apptronik.com)
2. [Apptronik Apollo 제품 페이지](https://apptronik.com/apollo)
3. [RoboZaps Apptronik Apollo 리뷰](https://blog.robozaps.com/b/apptronik-apollo-review)
