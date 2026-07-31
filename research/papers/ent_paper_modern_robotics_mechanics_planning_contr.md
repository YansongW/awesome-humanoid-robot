---
$id: ent_paper_modern_robotics_mechanics_planning_contr
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Modern Robotics: Mechanics, Planning, and Control'
  zh: 'Modern Robotics: Mechanics, Planning, and Control'
  ko: 'Modern Robotics: Mechanics, Planning, and Control'
summary:
  en: 'Modern Robotics - Northwestern Mechatronics Wiki Modern Robotics From Mech Jump to navigation Jump to search The Cambridge
    University Press cover. Institutions per source list: Northwestern University、Seoul National University.'
  zh: '《Modern Robotics: Mechanics, Planning, and Control》是由Kevin M. Lynch和Frank C. Park撰写的机器人学教材，由Cambridge University Press于2017年出版。该书以李群理论为核心，系统性地阐述了现代机器人学的力学、规划与控制，并提供了免费预印本和Coursera在线课程。'
  ko: 'Modern Robotics - Northwestern Mechatronics Wiki Modern Robotics From Mech Jump to navigation Jump to search The Cambridge
    University Press cover. Institutions per source list: Northwestern University、Seoul National University.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- modern
- robotics
- mechanics
- planning
- contr
- project_page_sourced
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: Full ingest from Yuanxq lab paper list row 715 (.staging/ingest_yuanxq). Tier B->page. Content compiled by DeepSeek
    from the fetched project page (https://hades.mech.northwestern.edu/index.php/Modern_Robotics). Institutions as given in
    the source list, not verified.
sources:
- id: src_001
  type: website
  title: Project page
  url: https://hades.mech.northwestern.edu/index.php/Modern_Robotics
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

这本教材由西北大学和首尔大学的课程笔记发展而来，旨在以清晰易懂的方式向本科生和研究人员传授机器人学的核心概念。它采用基于李群理论的现代方法，覆盖了从构型空间到轮式移动机器人的广泛主题。书中包含丰富的练习、视频和幻灯片等配套资源，并提供了多种格式的免费预印本供下载。

## 核心内容
### 教材概述
《Modern Robotics: Mechanics, Planning, and Control》由Kevin M. Lynch（西北大学）和Frank C. Park（首尔大学）合著，Cambridge University Press于2017年出版，ISBN为9781107156302。该书源自两校多年课程（首尔大学的M2794.0027 Introduction to Robotics和西北大学的ME 449 Robotic Manipulation）的讲义，其在线预印本与官方出版版本在章节、节和习题上保持一致。

### 核心内容与特色
- **现代方法**：教材以李群理论（Lie group theory）为基础，将现代运动学概念以本科生也能理解的方式呈现，被IEEE Control Systems Magazine书评誉为“注定成为该领域的经典”。
- **内容覆盖**：全书包含14个章节和4个附录，涵盖构型空间（Configuration Space）、刚体运动（Rigid-Body Motions）、正/逆运动学、速度运动学与静力学、闭链运动学、开链动力学、轨迹生成、运动规划、机器人控制、抓取与操作、轮式移动机器人等主题。附录包括有用公式总结、旋转的其他表示、Denavit-Hartenberg参数以及优化与拉格朗日乘子法。
- **配套资源**：提供练习习题（含解答）、线性代数复习、教学视频、课堂幻灯片、软件（如机器人运动学与动力学库）、仿真工具以及Coursera在线课程。

### 版本与获取
- **官方版本**：Cambridge University Press出版的硬皮版，排版、图表和校对更精细，被视为“官方”版本。可通过Amazon或Cambridge University Press购买。
- **免费预印本**：提供四种格式的免费下载，内容与页码与官方版完全相同，仅在页边距和字体大小上有所区别。包括带超链接的默认8.5x11英寸/A4版和平板版，以及不带超链接的大字体版和2up版（每页两页，适合节省纸张）。
- **翻译版本**：已有中文版（机械工业出版社）和韩文版（acorn Publishing Korea）。
- **版本更新**：当前为更新后的第一版（在线预印本日期为2019年12月，印刷版标记为“3rd printing 2019”或更新），包含对原第一版（2017年5月）的若干修正和少量补充。

## 参考
- https://hades.mech.northwestern.edu/index.php/Modern_Robotics
- https://github.com/ImChong/Robotics_Notebooks

## Overview

This textbook, developed from course notes at Northwestern University and Seoul National University, aims to teach the core concepts of robotics to undergraduates and researchers in a clear and accessible manner. It adopts a modern approach based on Lie group theory, covering a wide range of topics from configuration space to wheeled mobile robots. The book includes abundant supplementary resources such as exercises, videos, and slides, and offers free preprints in multiple formats for download.

## Content
### Textbook Overview
*Modern Robotics: Mechanics, Planning, and Control*, co-authored by Kevin M. Lynch (Northwestern University) and Frank C. Park (Seoul National University), was published by Cambridge University Press in 2017 with ISBN 9781107156302. The book originates from lecture notes of courses taught at both universities over several years (Seoul National University's M2794.0027 Introduction to Robotics and Northwestern University's ME 449 Robotic Manipulation). Its online preprint is consistent with the official published version in chapters, sections, and exercises.

### Core Content and Features
- **Modern Approach**: Based on Lie group theory, the textbook presents modern kinematics concepts in a way understandable to undergraduates. It has been hailed by an IEEE Control Systems Magazine review as "destined to become a classic in the field."
- **Content Coverage**: The book comprises 14 chapters and 4 appendices, covering topics such as Configuration Space, Rigid-Body Motions, Forward/Inverse Kinematics, Velocity Kinematics and Statics, Closed-Chain Kinematics, Open-Chain Dynamics, Trajectory Generation, Motion Planning, Robot Control, Grasping and Manipulation, and Wheeled Mobile Robots. Appendices include a summary of useful formulas, other representations of rotations, Denavit-Hartenberg parameters, and optimization with Lagrange multipliers.
- **Supplementary Resources**: Provides exercise problems (with solutions), linear algebra review, instructional videos, classroom slides, software (e.g., robot kinematics and dynamics libraries), simulation tools, and a Coursera online course.

### Versions and Access
- **Official Version**: A hardcover edition published by Cambridge University Press, with more refined typesetting, figures, and proofreading, considered the "official" version. Available for purchase via Amazon or Cambridge University Press.
- **Free Preprints**: Available for free download in four formats, with content and page numbers identical to the official version, differing only in margins and font size. Includes a default 8.5x11 inch/A4 version with hyperlinks and a tablet version, as well as a large-print version without hyperlinks and a 2up version (two pages per sheet, suitable for saving paper).
- **Translated Versions**: Chinese edition (China Machine Press) and Korean edition (acorn Publishing Korea) are available.
- **Version Updates**: The current version is an updated first edition (online preprint dated December 2019, print edition marked as "3rd printing 2019" or later), containing several corrections and minor additions to the original first edition (May 2017).

## 개요

이 교재는 노스웨스턴 대학교와 서울대학교의 강의 노트에서 발전하여, 학부생과 연구자에게 로봇공학의 핵심 개념을 명확하고 이해하기 쉽게 전달하는 것을 목표로 합니다. 리 군 이론(Lie group theory)에 기반한 현대적 접근 방식을 채택하며, 구성 공간(configuration space)에서부터 바퀴형 이동 로봇에 이르기까지 광범위한 주제를 다룹니다. 풍부한 연습 문제, 동영상, 슬라이드 등 보충 자료를 포함하며, 다양한 형식의 무료 사전 인쇄본을 다운로드할 수 있습니다.

## 핵심 내용
### 교재 개요
《Modern Robotics: Mechanics, Planning, and Control》은 Kevin M. Lynch(노스웨스턴 대학교)와 Frank C. Park(서울대학교)이 공동 저술하였으며, Cambridge University Press에서 2017년에 출판되었습니다(ISBN: 9781107156302). 이 책은 두 대학의 오랜 강의(서울대학교 M2794.0027 Introduction to Robotics 및 노스웨스턴 대학교 ME 449 Robotic Manipulation)에서 비롯된 강의 노트를 기반으로 하며, 온라인 사전 인쇄본은 공식 출판 버전과 장, 절, 연습 문제에서 일관성을 유지합니다.

### 핵심 내용 및 특징
- **현대적 접근법**: 교재는 리 군 이론(Lie group theory)을 기반으로 하여, 현대 운동학 개념을 학부생도 이해할 수 있는 방식으로 제시합니다. IEEE Control Systems Magazine의 서평에서는 "이 분야의 고전이 될 것"이라고 평가했습니다.
- **내용 범위**: 전체 14개 장과 4개의 부록으로 구성되며, 구성 공간(Configuration Space), 강체 운동(Rigid-Body Motions), 정/역기구학, 속도 기구학과 정역학, 폐쇄 사슬 기구학, 개방 사슬 동역학, 궤적 생성, 운동 계획, 로봇 제어, 파지 및 조작, 바퀴형 이동 로봇 등의 주제를 다룹니다. 부록에는 유용한 공식 요약, 회전의 다른 표현, Denavit-Hartenberg 매개변수, 최적화 및 라그랑주 승수법이 포함됩니다.
- **보충 자료**: 연습 문제(해답 포함), 선형 대수 복습, 교육용 동영상, 강의 슬라이드, 소프트웨어(로봇 기구학 및 동역학 라이브러리 등), 시뮬레이션 도구, Coursera 온라인 강좌를 제공합니다.

### 버전 및 획득 방법
- **공식 버전**: Cambridge University Press에서 출판한 하드커버판으로, 조판, 그림, 교정이 더 정교하여 "공식" 버전으로 간주됩니다. Amazon 또는 Cambridge University Press를 통해 구매할 수 있습니다.
- **무료 사전 인쇄본**: 네 가지 형식으로 무료 다운로드가 가능하며, 내용과 페이지 번호는 공식판과 완전히 동일하지만 여백과 글꼴 크기에서 차이가 있습니다. 하이퍼링크가 포함된 기본 8.5x11인치/A4판 및 태블릿판, 하이퍼링크가 없는 큰 글꼴판 및 2up판(한 페이지에 두 페이지 인쇄, 용지 절약에 적합)이 포함됩니다.
- **번역 버전**: 중국어판(기계공업출판사)과 한국어판(acorn Publishing Korea)이 있습니다.
- **버전 업데이트**: 현재는 업데이트된 제1판(온라인 사전 인쇄본 날짜는 2019년 12월, 인쇄판에는 "3rd printing 2019" 또는 그 이후로 표시)으로, 원래 제1판(2017년 5월)에 대한 여러 수정 사항과 소량의 추가 내용이 포함되어 있습니다.
