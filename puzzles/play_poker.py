# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Grading Notes
#
# Muliple correct answers will be accepted in cases
# where the best hand is ambiguous (for example, if
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

allranks = '23456789TJQKA'
redcards = [r + s for r in allranks for s in 'DH']
blackcards = [r + s for r in allranks for s in 'SC']


def allmax(iterable, key=None):
    """ Returns a list of all items equal to the max of the iterable"""
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

    max_num = max(iterable)
    max_list = []
    for itr in iterable:
        if itr == max_num:
            max_list.append(itr)

    return max_list


def best_wild_hand(hand):
    """Try all values for jokers in all 5-card selection"""
    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)


def replacements(card):
    """Return a list of all possible replacements for a card.
    There will be more than 1 only for wild cards."""
    if card == '?B': return blackcards


def best_hand(hand):
    return max(itertools.combinations(hand, 5), key=hand_rank)


def best_hand_test(hand):
    """ From a 7-card hand, return the best 5 card hand. """
    hn = hand_rank(hand)
    print(hn)
    return hn


# ------------------
# Provided Functions
#
# You may want to use some of the functions which
# you have already defined in the unit to write
# your best_hand function.


def hand_rank(hand):
    """ Return a value indicating the ranking of a hand. """

    ranks = []
    suit = same_suit(hand)
    if suit:
        ranks = card_ranks(suit)
    else:
        ranks = card_ranks(hand)
    print(ranks)

    # if straight(ranks) and flush(hand):
    if straight(ranks):
        # return (8, max(ranks))
        return create_map(ranks, hand)
    elif kind(4, ranks):
        # return (7, kind(4, ranks), kind(1, ranks))
        return create_map(ranks, hand)
    elif kind(3, ranks) and kind(2, ranks):
        # return (6, kind(3, ranks), kind(2, ranks))
        return create_map(ranks, hand)
    elif flush(hand):
        # return (5, ranks)
        return create_map(ranks, hand)
    elif straight(ranks):
        # return (4, max(ranks))
        return create_map(ranks, hand)
    elif kind(3, ranks):
        # return (3, kind(3, ranks), ranks)
        return create_map(ranks, hand)
    elif two_pair(ranks):
        # return (2, two_pair(ranks), ranks)
        return create_map(ranks, hand)
    elif kind(2, ranks):
        # return (1, kind(2, ranks), ranks)
        return create_map(ranks, hand)
    else:
        # return (0, ranks)
        return create_map(ranks, hand)


def create_map(ranks, hand):
    new_hand = []
    for r, s in hand:
        if r == 'T':
            if 10 in ranks:
                new_hand.append(r + s)
        elif r == 'J':
            if 11 in ranks:
                new_hand.append(r + s)
        elif r == 'K':
            if 12 in ranks:
                new_hand.append(r + s)
        elif r == 'Q':
            if 13 in ranks:
                new_hand.append(r + s)
        elif r == 'A':
            if 14 in ranks:
                new_hand.append(r + s)
        elif int(r) in ranks:
            new_hand.append(r + s)
    return new_hand


def same_suit(hand):
    """ Returns 5 same suit hands if found. """
    most_occ = None
    suits = [s for r, s in hand]
    for s in suits:
        if suits.count(s) > 4:
            most_occ = s
            break
    if most_occ:
        most_occ_suits = [a + b for a, b in hand if b == most_occ]
        return most_occ_suits
    else:
        return hand


def freq_hand(ranks, hand):
    """ Returns 5 same suit hands if found. """
    most_occ = None
    most_occ_cards = []
    cards = [r for r, s in hand]
    for r in cards:
        if cards.count(r) > 2:
            most_occ = r
            break
    if most_occ is not None:
        most_occ_cards = [a for a, b in hand if a == most_occ]
    else:
        return ranks

    if len(most_occ_cards) == 3:
        most_occ_cards.append(ranks[:2])
        return most_occ_cards
    elif len(most_occ_cards) == 4:
        most_occ_cards.append(ranks[:1])
        return most_occ_cards
    elif len(most_occ_cards) == 5:
        return most_occ_cards


def card_ranks(hand):
    """ Return a list of the ranks, sorted with higher first. """
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    print('-----')
    print(ranks)

    freq = freq_hand(ranks, hand)
    print('>>>')
    print(freq)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks[:5]


def flush(hand):
    """ Return True if all the cards have the same suit. """
    suits = [s for r, s in hand]
    return len(set(suits)) < 3


def straight(ranks):
    """Return True if the ordered
    ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    """Return the first rank that this hand has
    exactly n-of-a-kind of. Return None if there
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return True
    return None


def two_pair(ranks):
    """If there are two pair here, return the two
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


def test_best_hand():
    assert (best_hand("6C 7C 8C 9C TC 5C JS".split())
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

# print(test_best_hand())
# def sq(x): print('sq called', x); return x * x
# for x2 in (sq(x) for x in range(10) if x%2 == 0): pass    # example of generator expressions
