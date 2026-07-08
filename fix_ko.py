import json
from pathlib import Path

p = Path('proposal_hu_icub_walking_2016.json')
data = json.loads(p.read_text(encoding='utf-8'))

ko_title = '다양한 시나리오에서의 iCub 인간형 로봇 보행: 구현 및 성능 분석'
ko_summary = '본 논문은 iCub 인간형 로봇에서 평지, 경사면, 계단 등 다양한 시나리오에서의 보행 동작을 처음으로 구현하고, 가변 질량 중심 높이를 갖는 오프라인 ZMP 기반 패턴 생성기, IPOPT 기반 역욕학 및 위치 제어를 사용하며 KoroiBot 핵심 성과 지표를 통해 성능을 평가한다.'
ko_icub_target_name = 'iCub 인간형 로봇'
ko_icub_desc = '완전한 iCub 인간형 로봇에서 보행 동작을 구현하고 평가한다.'
ko_heicub_target_name = 'HeiCub 축소형 인간형 로봇'

data['entry']['names']['ko'] = ko_title
data['entry']['summary']['ko'] = ko_summary

for re in data['entry']['related_entities']:
    if re['id'] == 'entity_icub_robot':
        re['description']['ko'] = ko_icub_desc

for rel in data['relationships']:
    if rel['target_id'] == 'entity_icub_robot':
        rel['target_name']['ko'] = ko_icub_target_name
        rel['description']['ko'] = ko_icub_desc
    elif rel['target_id'] == 'entity_heicub_robot':
        rel['target_name']['ko'] = ko_heicub_target_name

# Fix literal backslash-n in overview to actual newlines
overview = data['body']['overview']
data['body']['overview'] = overview.replace('\\n\\n', '\n\n').replace('\\n', '\n')

p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print('Done')
