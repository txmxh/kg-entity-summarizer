def triple_ranking(triples, lf):
    # Rank triples based on local frequency of their predicate (descending)
    ranked_triples = sorted(triples, key=lambda t: lf[t[1]], reverse=True)
    return ranked_triples