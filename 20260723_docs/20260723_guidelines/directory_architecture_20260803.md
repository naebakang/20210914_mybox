# directory_architecture.md

first, 20260727
last, 20260728
editor, naebakang

## See also
@my_merge_algorithm.md

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

# build_up/

- 1회성 코드(기존과 로직이 달라져서 .csv, .yaml 파일의 내용를 변경하는 등)는 여기에 생성.
- 메인 로직과 연관 없는 코드는 여기에 생성.

# configs/env.py

- 보조 config 파일.
- python 데이터 타입 형태(list, tuple, ...)의 값 기록.
- pyinstall 사용해서 배포할 때, 숨기고 싶은 값 기록.

# configs/set_project.yaml

- 메인 config 파일.
- 이미 실행되고 있는 코드에 실시간으로 변경하고 싶은 값 기록.

# datamini/

- 프로젝트 내부에서만 공유하는 데이터 저장.

# src/app/basket/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 프로젝트 코드 내부에서 돌아다니는 정형화된 데이터를 기록한다.

# src/app/function/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 python 기본 라이브러리, pip 으로 설치한 라이브러리만 import 할 수 있다.
- 각 모듈은 특정한 설정이 없는 단순도구이다.

# src/app/object/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 설정 값이 필요한 Infrastructure 이다.

# src/app/procedure/

- .py 확장자를 갖는 python 모듈을 저장한다.
- 각 모듈은 목표하고자 하는 절차를 구현한다.

# src/app/procedure/app.py

- 프로젝트의 최상단 껍데기 모듈이다.

# src/app/procedure/container.py


*20260803
container.py 부터 진행하면 된다.

*
코드 디펜드 개념, container 넣어야한다.
basket 등 각 폴더에 어떤 모듈이 위치해야 하는지 정의
function
- python 기본 모듈 or pip 를 통해 설치한 모듈만 import 한다.
- 현재 프로젝트에서 생성된 모듈은 import 하지 않는다.


## Rules

- 프로젝트 버전 업데이트는 @my_merge_algorithm.md 에 명시되어 있는 'release' branch 에서 진행.
- 프로젝트 버전은 `set_project.yaml`의 `name.version`에 저장.
- 형식은 `YYYYMMDD_vNNN`(오늘 날짜 + 0으로 채운 3자리 카운터, 예: `20260721_v001`).
- 카운터는 날짜가 바뀌면 `001`로 리셋되고, 같은 날짜 안에서 커밋할 때마다 1씩 증가한다(날짜와 무관하게 계속 누적되는 카운터가 아님).
- 이 과정은 @githooks/ 에 저장된 git 훅으로 자동화돼 있다 (`.git/hooks/` 자체는 git이 추적하지 않으므로, 이 파일들을 로컬에 복사해서 사용한다):
  - `githooks/pre-commit`: `set_project.yaml`에서 현재 버전을 읽고, 위 리셋/증가 규칙에 따라 다음 버전을 계산해서 다시 써넣은 뒤, 그 변경사항이 같은 커밋에 포함되도록 `git add`한다.
  - `githooks/post-commit`: 방금 커밋된 버전 문자열을 읽어서, 그 커밋을 가리키는 동일한 이름의 git tag를 생성한다.
- `set_project.yaml`의 `name.version`은 @githooks/ 에 저장된 git 훅 으로 관리한다.
