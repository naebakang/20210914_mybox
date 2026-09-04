# directory_architecture.md

first, 20260727
last, 20260810
editor, naebakang

## Directory
build_up/
configs/
-env.py
-set_project.yaml
datamini/
etc/
-githooks/
--post-commit
--pre-commit
-changelog.md
src/
-app/
--basket/
--function/
--object/
--procedure/
--app.py
--container.py
tests/
LIVE.sh
main.py

## build_up/

- 1회성 코드(기존과 로직이 달라져서 .csv, .yaml 파일의 내용를 변경하는 등)는 여기에 생성.
- 메인 로직과 연관 없는 코드는 여기에 생성.

## configs/env.py

- 보조 config 파일.
- python 데이터 타입 형태(list, tuple, ...)의 값 기록.
- pyinstall 사용해서 배포할 때, 숨기고 싶은 값 기록.

## configs/set_project.yaml

- 메인 config 파일.
- 이미 실행되고 있는 코드에 실시간으로 변경하고 싶은 값 기록.

## datamini/

- 프로젝트 내부에서만 공유하는 데이터 저장.

## src/app/basket/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 프로젝트 코드 내부에서 돌아다니는 정형화된 데이터를 기록한다.

## src/app/function/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 python 기본 라이브러리, pip 으로 설치한 라이브러리만 import 할 수 있다.
- 각 모듈은 현재 프로젝트에서 생성된 모듈은 import 하지 않는다.
- 각 모듈은 특정한 설정값이 없이, 단순계산하는 도구이다.

## src/app/object/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 설정 값이 필요한 Infrastructure 이다.

## src/app/procedure/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 목표하고자 하는 절차를 구현한다.

## src/app/procedure/app.py

- 프로젝트의 최상단 껍데기 모듈이다.

## src/app/procedure/container.py

- 'from dependency_injector import containers, providers' 사용한다.
- 'src/app/function/' 에 있는 모듈을 제외하고, 나머지 모듈들의 의존성을 여기서 정의한다.

## tests/

- 테스트 진행하면서 필요한 파일을 저장한다.
