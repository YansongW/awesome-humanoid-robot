---
$id: ent_paper_frame_floor_aligned_representa_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video'
  zh: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video'
  ko: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video'
summary:
  en: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  zh: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  ko: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- frame
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.23094v1.
sources:
- id: src_001
  type: paper
  title: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2503.23094
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video project page'
  url: https://vcai.mpi-inf.mpg.de/projects/FRAME/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric motion capture with a head-mounted body-facing stereo camera is crucial for VR and AR applications but presents significant challenges such as heavy occlusions and limited annotated real-world data. Existing methods rely on synthetic pretraining and struggle to generate smooth and accurate predictions in real-world settings, particularly for lower limbs. Our work addresses these limitations by introducing a lightweight VR-based data collection setup with on-board, real-time 6D pose tracking. Using this setup, we collected the most extensive real-world dataset for ego-facing ego-mounted cameras to date in size and motion variability. Effectively integrating this multimodal input -- device pose and camera feeds -- is challenging due to the differing characteristics of each data source. To address this, we propose FRAME, a simple yet effective architecture that combines device pose and camera feeds for state-of-the-art body pose prediction through geometrically sound multimodal integration and can run at 300 FPS on modern hardware. Lastly, we showcase a novel training strategy to enhance the model's generalization capabilities. Our approach exploits the problem's geometric properties, yielding high-quality motion capture free from common artifacts in prior works. Qualitative and quantitative evaluations, along with extensive comparisons, demonstrate the effectiveness of our method. Data, code, and CAD designs will be available at https://vcai.mpi-inf.mpg.de/projects/FRAME/

## 核心内容
Egocentric motion capture with a head-mounted body-facing stereo camera is crucial for VR and AR applications but presents significant challenges such as heavy occlusions and limited annotated real-world data. Existing methods rely on synthetic pretraining and struggle to generate smooth and accurate predictions in real-world settings, particularly for lower limbs. Our work addresses these limitations by introducing a lightweight VR-based data collection setup with on-board, real-time 6D pose tracking. Using this setup, we collected the most extensive real-world dataset for ego-facing ego-mounted cameras to date in size and motion variability. Effectively integrating this multimodal input -- device pose and camera feeds -- is challenging due to the differing characteristics of each data source. To address this, we propose FRAME, a simple yet effective architecture that combines device pose and camera feeds for state-of-the-art body pose prediction through geometrically sound multimodal integration and can run at 300 FPS on modern hardware. Lastly, we showcase a novel training strategy to enhance the model's generalization capabilities. Our approach exploits the problem's geometric properties, yielding high-quality motion capture free from common artifacts in prior works. Qualitative and quantitative evaluations, along with extensive comparisons, demonstrate the effectiveness of our method. Data, code, and CAD designs will be available at https://vcai.mpi-inf.mpg.de/projects/FRAME/

## 参考
- http://arxiv.org/abs/2503.23094v1

