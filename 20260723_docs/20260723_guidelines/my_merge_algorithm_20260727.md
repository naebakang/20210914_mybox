# my_merge_algorithm.md

first, 20220125
last, 20260727
editor, naebakang

## See also
@my_merge_algorithm.png

## Principles
- 단순하게 간다.
- 개발 단계 코드와 출시 단계 코드가 완전 다르다고 가정한다.
- 3가지 branch를 만든다.
- @my_merge_algorithm.png 를 참고한다.

## Branch
1. master
2. dev
3. release

## master
- checkout master
- 개발 진행
- 잘 돌아가는걸 확인한다(test).

## dev
- checkout dev
- merge --no-ff master
- 구동에 영향이 없는 파일 삭제('build_up/' 삭제 등)
- 서비스에 필요한 모든 수정 완료
- 잘 돌아가는걸 확인한다(test).

## release
- checkout release
- merge --no-ff dev
- tag v000
- 출시/배포

checkout master
이후 반복.
