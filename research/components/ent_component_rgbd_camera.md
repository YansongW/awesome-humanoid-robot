---
$id: ent_component_rgbd_camera
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: RGB-D Camera
  zh: RGB-D相机
  ko: RGB-D 칩라
summary:
  en: A vision sensor that combines color imaging with per-pixel depth measurement, enabling 3D scene understanding for manipulation
    and navigation.
  zh: 融合彩色成像与逐像素深度测量的视觉传感器，为抓取操作与导航提供三维场景理解。
  ko: 컬러 영상과 픽셀별 깊이 정보를 결합하여 조작 및 납품을 위한 3D 장면 이해를 제공하는 비전 센서.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- component
- chapter_5
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
### 5.9.1 头部：RGB-D/双目/LiDAR/IMU 布局

人形机器人头部通常集成视觉和惯性传感器，用于环境感知、导航、交互和头部姿态估计。

!!! note "术语解释：头部感知、RGB-D 相机、宽视场、深度感知、头部姿态"
    - **头部感知（head perception）**：人形机器人头部传感器的配置与感知功能。
    - **RGB-D 相机（RGB-D camera）**：同时输出彩色图像和深度图像的相机。
    - **宽视场（wide field of view）**：相机能覆盖的大角度范围。
    - **深度感知（depth perception）**：获取场景三维距离信息的能力。
    - **头部姿态（head pose）**：头部坐标系相对于身体或世界坐标系的位姿。

典型头部配置包括：

- **RGB-D 或双目相机**：安装于面部或额头，用于物体识别、操作引导和场景理解。
- **广角/鱼眼相机**：用于导航和视觉里程计，覆盖机器人前方和侧方。
- **LiDAR**：部分平台在头部或躯干高处安装小型固态/MEMS LiDAR，用于大范围三维建图。
- **IMU**：安装在头部或颈部，测量头部运动，辅助图像稳定和视觉-惯性融合。

```mermaid
flowchart TD
    A["头部"] --> B["RGB-D/双目相机"]
    A --> C["广角相机"]
    A --> D["LiDAR"]
    A --> E["IMU"]
    B --> F["物体识别 / 操作"]
    C --> G["VIO / 导航"]
    D --> H["SLAM / 避障"]
    E --> I["头部姿态 / 防抖"]
```
