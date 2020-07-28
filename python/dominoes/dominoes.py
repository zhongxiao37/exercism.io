from collections import Counter, namedtuple

Chain = namedtuple('Chain', 'chain, remaining_dominoes')

def can_chain(dominoes):
    if len(dominoes) == 0:
        return []

    if check_if_exists_single_dominoes(dominoes):
        return None
    
    chains = []
    chains.append(Chain([dominoes[0]], dominoes[1:]))
    for chn in chains:
        while len(chn.remaining_dominoes) != 0:
            candiates = candiate_dominoes(chn)
            if len(candiates) == 0:
                break
            elif len(candiates) > 1:
                # if there are more than one candiates for next domino
                # create a new chain for it and add it `chains`
                for cand in candiates[1:]:
                    new_remaining_dominoes = chn.remaining_dominoes.copy()
                    new_remaining_dominoes.remove(cand)
                    if cand[1] == chn.chain[-1][1]:
                        cand = (cand[1], cand[0])
                    new_chain = chn.chain.copy()
                    new_chain.append(cand)
                    chains.append(Chain(new_chain, new_remaining_dominoes))
                
            cand = candiates[0]
            chn.remaining_dominoes.remove(cand)
            if cand[1] == chn.chain[-1][1]:
                cand = (cand[1], cand[0])
            chn.chain.append(cand)
    
    chains = [chn for chn in chains if len(chn.remaining_dominoes) == 0]
    if len(chains) == 0:
        return None
    else:
        return chains[0].chain

def candiate_dominoes(chain):
    last_domino = chain.chain[-1][1]
    return [dom for dom in chain.remaining_dominoes if last_domino in dom]

def check_if_exists_single_dominoes(dominoes):
    all_numbers = []
    for (a, b) in dominoes:
        all_numbers.append(a)
        all_numbers.append(b)
    
    num_counts = Counter(all_numbers)
    if any(e % 2 == 1 for e in num_counts.values()):
        return True
    
    return False