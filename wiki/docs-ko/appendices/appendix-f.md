# 부록 F 지식 그래프 검색 예시

본 부록에서는 본 사이트(kg.rounds-tech.com)에서 지식 그래프를 검색하고 탐색하는 방법을 소개하며, 일반적인 질문에 대한 검색 경로를 제시합니다.

## F.1 사이트 구조 개요

| 진입점 | 주소 | 내용 |
|---|---|---|
| 홈페이지 | `/` | 분야 탐색, 유형 탐색, 추천 엔터티 |
| 검색 | `/search/` | 전체 텍스트 검색(이름, 요약, 본문, arXiv 번호) |
| 그래프 | `/graph/` | 전체 관계 네트워크 및 커뮤니티 클러스터링 시각화 |
| Wiki | `/wiki/` | 30개 장의 전문서 + 부록 |
| 엔터티 카드 | `/entry/<엔터티ID>/` | 개별 엔터티의 요약, 본문, 관계, 출처 |
| 유형 목록 | `/types/<유형>/` | 특정 유형의 모든 엔터티 |

## F.2 검색 팁

**키워드 검색**: `/search/`에서 중문 또는 영문 입력 가능, 예:

- `宇树` 또는 `Unitree` —— 회사, 제품 및 관련 논문 검색
- `2304.13705` —— arXiv 번호로 논문 직접 검색(예: ACT)
- `全身控制` —— 방법, 개념, 논문 장 절 검색

**유형별 필터링**: 검색 결과 페이지 상단의 유형 태그를 클릭하거나 URL 매개변수 사용:

```
/search/?type=paper            논문만 보기
/search/?type=company          회사만 보기
```

**분야별 필터링**: `domain` 매개변수 사용(홈페이지 분야 카드가 이 링크에 해당):

```
/search/?domain=07_ai_models_algorithms     AI 모델 및 알고리즘
/search/?domain=04_actuators                액추에이터
/search/?domain=11_applications_markets     응용 및 시장
```

매개변수 조합 가능: `/search/?domain=09_simulation_digital&type=benchmark`(시뮬레이션 분야의 평가 기준).

## F.3 그래프 페이지 사용법

- **전체 그래프 모드**: 커뮤니티(cluster)별로 색상이 지정된 엔터티 네트워크 표시, 확대/축소 및 드래그 가능.
- **단일 엔터티 서브그래프**: 엔터티 카드 페이지의 "관계 서브그래프"에서 1홉 이웃 확인 가능; 그래프 페이지 오른쪽 상단 검색창에서 특정 엔터티로 이동 가능.
- **관계 유형**: 연결선 레이블은 현지화되어 있음, 예: `is_based_on`(기반), `evaluates_on`(평가 대상), `uses_dataset`(데이터셋 사용).

## F.4 일반적인 질문 검색 경로

**"특정 방법의 원리와 출처는?"**
방법명 검색 → 엔터티 카드 진입 → "핵심 내용" 및 "참고" 출처 확인; 카드의 "발신 관계"에서 `has_prerequisite`가 선행 이론을 나열.

**"특정 기준/데이터셋이 어떤 작업에서 사용되었는가?"**
기준 엔터티 카드 진입 → "수신 관계"에서 `evaluates_on`(어떤 방법이 해당 기준에서 평가되었는지) 및 `uses_dataset`(어떤 작업이 데이터를 사용했는지) 확인.

**"특정 회사의 제품 및 공급망은?"**
회사 카드 진입 → `manufacturer_of`(제조한 제품), `supplies`/`sources_from`(공급 및 조달) 관계 확인; 공급망 전체 개요는 Wiki 제7장 및 부록 D 참조.

**"휴머노이드 로봇의 특정 주제에 대한 체계적 개요는?"**
먼저 Wiki 해당 장 확인(장 목록은 `/wiki/` 참조), 장 내에서 인용된 엔터티는 카드 페이지를 통해 추가 탐색 가능.

## F.5 엔터티 ID 명명 규칙

엔터티 ID는 `ent_<유형>_<이름>[_연도]` 형식으로 통일, 예:

- `ent_paper_action_chunking_transformer_2023` —— 논문
- `ent_method_whole_body_control` —— 방법
- `ent_company_unitree_robotics_2024` —— 회사
- `ent_standard_iso_13482_personal_care_robot_2014` —— 표준

관계 ID는 `rel_<소스엔터티ID>_<관계유형>_<대상엔터티ID>` 형식.

## F.6 프로그래밍 방식 접근

본 사이트는 정적 사이트이며, 그래프 데이터는 JSON 형식으로 공개:

```
/data/search-index.json   검색 인덱스(요약, 분야, 유형 태그 포함)
/data/relations.json      전체 노드 및 연결선
/data/clusters.json       커뮤니티 클러스터링 결과
/data/subgraphs/<엔터티ID>.json   단일 엔터티 1홉 서브그래프
```

`fetch`를 통해 직접 가져와 2차 개발에 사용 가능; 원본 데이터(YAML/Markdown)는 GitHub 저장소 `YansongW/awesome-humanoid-robot`에서 관리.
