from math import sqrt


class Cards(object):
    def __init__(self):
        self.length = None
        self.width = None


class Envelopes(object):
    def __init__(self):
        self.length = None
        self.width = None


def card_in_envelope(envelope_number, card_number):
    if envelopes[envelope_number].length >= envelopes[envelope_number].width:
        current_envelope_width = envelopes[envelope_number].length
        current_envelope_length = envelopes[envelope_number].width
    else:
        current_envelope_width = envelopes[envelope_number].width
        current_envelope_length = envelopes[envelope_number].length
    if cards[card_number].length >= cards[card_number].width:
        current_card_width = cards[card_number].length
        current_card_length = cards[card_number].width
    else:
        current_card_width = cards[card_number].width
        current_card_length = cards[card_number].length
    if current_card_length <= current_envelope_length and current_card_width <= current_envelope_width:
        return True
    if current_envelope_length * current_envelope_width < current_card_length * current_card_width:
        return False
    if current_card_length ** 2 + current_card_width ** 2 > current_envelope_length ** 2 + current_envelope_width ** 2:
        return False
    card_diagonal = current_card_length ** 2 + current_card_width ** 2
    new_card_length = sqrt(abs(card_diagonal - current_envelope_width * current_envelope_width))
    new_card_width = sqrt(abs(card_diagonal - current_envelope_length * current_envelope_length))
    return current_envelope_width * current_envelope_length - new_card_length * new_card_width >= current_card_width * current_card_length * 2


def kun(v):
    if visit[v]:
        return False
    visit[v] = True
    for j in range(len(cards_in_envelope[v])):
        to = cards_in_envelope[v][j]
        if used[to] == -1 or kun(used[to]):
            used[to] = v
            return True
    return False


with open('../Individual_task/inputs/envelope_input.in', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/envelope_output.out', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    cards = [Cards() for _ in range(n)]
    for i in range(n):
        cards[i].length, cards[i].width = [float(j) for j in f_input.readline().split()]
    envelopes = [Envelopes() for _ in range(n)]
    for i in range(n):
        envelopes[i].length, envelopes[i].width = [float(j) for j in f_input.readline().split()]
    cards_in_envelope = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if card_in_envelope(j, i):
                cards_in_envelope[j].append(i)
    maximum = 0
    used = [-1 for _ in range(n)]
    for i in range(n):
        visit = [False for _ in range(n)]
        if kun(i):
            maximum += 1
    if maximum == n:
        print("YES", file=f_output)
    else:
        print("NO", maximum, sep="\n", file=f_output)
