# 乐聚机器人 / Leju Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 乐聚机器人 |
| **영문명** | Leju Robotics |
| **본사** | 중국 선전 (창립 팀은 하얼빈 공업대학 출신) |
| **설립 시간** | 2016년 |
| **공식 사이트** | [https://www.lejurobot.com](https://www.lejurobot.com) |
| **공급망环节** | 완제품 OEM / 오픈소스 홍맹 휴머노이드 로봇 |
| **기업 속성** | 하얼빈 공업대학 배경, 오픈소스 생태계, 화웨이 파트너 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Leju 공식 사이트, IT之家, 36氪, 로봇 온라인 |

## 회사 소개

Leju Robotics는 하얼빈 공업대학 박사인 냥샤오쿤이 창립했으며, 고동적 휴머노이드 로봇과 산업화에 집중하고 있습니다.

회사는 선카이홍과 협력하여 중국 최초의 오픈소스 홍맹(KaihongOS) 기반 고동적 휴머노이드 로봇 KUAVO(夸父)를 출시했으며, "개봉 즉시 사용 가능"한 연구 플랫폼과 국산화 공급망을 강조합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| 고동적 휴머노이드 | 연구, 서비스, 산업 협력 | KUAVO 4 / 4 Pro | 연구 교육, 전시장, 산업 |
| 서비스 휴머노이드 | 안내, 인터랙션 | KUAVO MY | 전시장, 대형 마트, 은행 |

## 대표 제품

### KUAVO 4 Pro

> Leju KUAVO 4 Pro: [공식 자료](https://www.lejurobot.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 166 cm | aixzd.com / IT之家 |
| 무게 | 55 kg | aixzd.com |
| 자유도 | 30 DOF | IT之家 |
| 부하/토크 | 한쪽 다리 피크 토크 220 N·m | 샤오슝 AI 네트워크 |
| 속도/회전 속도 | 보행 5 km/h | aixzd.com |
| 배터리 지속 시간 | 약 1시간(6 Ah 배터리) | aixzd.com |
| 인터페이스/통신 | Wi-Fi, KaihongOS, ROS | 공개 보도 |
| 가격 | 미공개 | 문의 필요 |

**기술 하이라이트**: 오픈소스 홍맹 KaihongOS, 3단 몸통 디자인, Gemini-335L 양안 깊이 카메라, mid-360 라이다, NVIDIA Orin-NX 상위 컴퓨터.

**응용 시나리오**: 연구 플랫폼, 전시장 안내, 상업 서비스, 산업 협력 운반.

### KUAVO(초기 모델)

> Leju KUAVO: [공식 자료](https://www.lejurobot.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 미공개 | - |
| 무게 | 약 45 kg | 36氪 / 로봇 온라인 |
| 자유도 | 26 DOF | 로봇 온라인 |
| 부하/토크 | 미공개 | - |
| 속도/회전 속도 | 최대 4.6 km/h; 연속 점프 >20 cm | 36氪 |
| 배터리 지속 시간 | 미공개 | - |
| 인터페이스/통신 | 오픈소스 홍맹, SDK, 시뮬레이션 플랫폼 | IT之家 |
| 가격 | 약 수십만 위안 | 36氪 |

**기술 하이라이트**: 중국 최초로 점프 가능하고 다양한 지형에서 보행 가능한 오픈소스 홍맹 휴머노이드 로봇, 운동 컨트롤러 오픈소스.

**응용 시나리오**: 교육 연구, 특수 서비스, 가정 서비스 초기 검증.

## 공급망 위치

- **상류 핵심 부품/재료**: 선카이홍 KaihongOS, 오비중광 깊이 카메라, 헤사이/란워 라이다, 국산 모터 및 감속기.
- **하류 고객/응용 시나리오**: 대학, 화웨이 생태계 전시장, 은행, 공장.
- **주요 경쟁사/대상**: 위슈 G1, 푸리에 GR-1, 즈위안 A2.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_leju`
- 제품 엔터티: `ent_product_leju_kuavo_4pro`, `ent_product_leju_kuavo`
- 주요 관계:
  - `ent_company_leju` -- `manufactures` --> `ent_product_leju_kuavo_4pro`
  - `ent_company_leju` -- `manufactures` --> `ent_product_leju_kuavo`
  - `ent_product_leju_kuavo_4pro` -- `uses` --> `ent_component_orbbec_gemini335`

## 참고 자료

1. [Leju Robotics 공식 사이트](https://www.lejurobot.com)
2. [IT之家 – Leju KUAVO 연구용 버전 출시](https://www.ithome.com/0/800/849.htm)
3. [36氪 – Leju KUAVO 출시](https://so.html5.qq.com/page/real/search_news?docid=70000021_145656eac9b02752)
4. [aixzd.com – KUAVO 4 Pro 소개](https://aixzd.com/robot/kuavo-4pro)
5. [부록 D.4 주요 제품 Wiki](../index-products.md)
