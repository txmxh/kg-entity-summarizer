from collections import Counter
from count_local_frequency import count_local_frequency
from triple_ranking import triple_ranking

def generate_entity_summary(triples, k=5):
    """
    Generate an entity summary based on Local Frequency of properties.
    """
    # Step 1: Count local frequency of each property
    lf = count_local_frequency(triples)
    
    # Step 2: Rank triples by local frequency (descending)
    ranked_triples = triple_ranking(triples, lf)
    
    # Step 3: Select top-k triples
    entity_summary = ranked_triples[:k]
    
    return entity_summary