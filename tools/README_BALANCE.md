# 밸런스 시뮬레이터 사용법

간단한 스크립트로 카드 JSON을 읽어 각 카드의 파워 점수를 계산하고 비용 조정 제안을 생성합니다.

사용 예시:
```bash
python3 tools/balance_simulator.py data/CARDS.json
```

출력: `data/CARD_BALANCE_SUGGESTIONS.json` 파일로 저장됩니다.

조정 방침은 매우 단순하며, 실제 밸런스 작업은 시뮬레이션(시합 실행) 기반의 조정이 필요합니다.
