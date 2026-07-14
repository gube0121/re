# Unity 프로토타입 템플릿 안내

이 폴더는 Unity에서 빠르게 프로토타입할 수 있는 최소 스케폴딩을 제공합니다.

구성
- `Assets/Scripts/CardModel.cs` : 카드 데이터 모델
- `Assets/Scripts/CardDataLoader.cs` : Resources의 `cards.json`을 읽어 로드
- `Assets/Scripts/GameManager.cs` : 간단한 게임 흐름 스텁
- `Assets/Resources/cards.json` : 카드 데이터(샘플 또는 전체 복사)

사용방법
1. Unity 허브로 새 2D 프로젝트 생성
2. 이 폴더의 `Assets` 내용을 프로젝트의 `Assets`로 복사
3. `GameManager` 스크립트를 빈 GameObject에 붙이고 실행

참고
- 현 상태는 최소 동작 예시입니다. 씬 구성(카드 프리팹, UI)은 유저가 편집해야 합니다.
