#!/usr/bin/env python3
"""간단 카드 밸런스 시뮬레이터
사용법: Python 3.8+에서 실행
  python3 tools/balance_simulator.py data/CARDS.json
출력: 콘솔에 카드 파워 점수와 권장 비용 조정 제안
"""
import json
import sys
import math
from pathlib import Path

def load_cards(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def score_card(card):
    # 간단한 가중치 기반 점수 산출
    atk = card.get('attack', 0)
    df = card.get('defense', 0)
    cost = card.get('cost', 0)
    risk = card.get('risk', 0)
    tags = card.get('tags', []) or []

    tag_bonus = 0
    if '뇌물' in tags or '화력' in tags:
        tag_bonus += 1.0
    if '증거' in tags or '검증' in tags:
        tag_bonus += 0.5

    score = atk * 1.2 + df * 1.0 - cost * 0.9 - risk * 1.5 + tag_bonus
    return round(score, 3)

def suggest_cost(card, score, target=2.5):
    # 점수가 목표에서 크면 비용을 올리고, 작으면 낮추자
    diff = score - target
    # 1점 차이에 대해 0.5 코스트 조정 제안
    adjust = -round(diff * 0.5)
    suggestion = card.get('cost', 0) + adjust
    suggestion = max(0, suggestion)
    return suggestion, adjust

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 tools/balance_simulator.py data/CARDS.json')
        return
    path = Path(sys.argv[1])
    data = load_cards(path)
    # data can be array or {"items": [...]}
    cards = data if isinstance(data, list) else data.get('items', [])

    results = []
    for c in cards:
        s = score_card(c)
        new_cost, adjust = suggest_cost(c, s)
        results.append({'id': c.get('id'), 'name': c.get('name'), 'score': s, 'current_cost': c.get('cost'), 'suggested_cost': new_cost, 'adjust': adjust})

    # 정렬 및 출력
    results.sort(key=lambda x: x['score'], reverse=True)
    print('Top 10 cards by score:')
    for r in results[:10]:
        print(f"#{r['id']:02d} {r['name']:20} score={r['score']:6} cost={r['current_cost']} -> suggested {r['suggested_cost']} (adj {r['adjust']})")

    # Save suggestions
    out = path.parent / 'CARD_BALANCE_SUGGESTIONS.json'
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print('\nSaved suggestions to', out)

if __name__ == '__main__':
    main()
