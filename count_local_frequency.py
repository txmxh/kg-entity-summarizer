def count_local_frequency(triples):
    # Calculate local frequency for each predicate
    lf = {}
    for _, p, _ in triples:
        lf[p] = lf.get(p, 0) + 1
    return lf