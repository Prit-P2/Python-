
import sys

def combine(term1, term2):
    """Combines two terms if they differ by one bit."""
    diff = 0
    new_term = list(term1)
    for i in range(len(term1)):
        if term1[i] != term2[i]:
            diff += 1
            new_term[i] = '-'
    if diff == 1:
        return "".join(new_term)
    return None

def pi_to_str(pi):
    """Converts a prime implicant string to a human-readable variable expression."""
    res = ""
    if all(c == '-' for c in pi):
        return "1"
    for i, char in enumerate(pi):
        var = chr(ord('A') + i)
        if char == '1':
            res += var
        elif char == '0':
            res += var + "'"
    return res

def quine_mccluskey(num_vars, minterms):
    """
    Simplifies a boolean function using the Quine-McCluskey algorithm.
    """
    if not minterms:
        return "0"
    if len(minterms) == 2**num_vars:
        return "1"

    # Stage 1: Find Prime Implicants
    mt_bins = [bin(m)[2:].zfill(num_vars) for m in minterms]
    
    groups = {}
    for term in mt_bins:
        ones = term.count('1')
        if ones not in groups:
            groups[ones] = set()
        groups[ones].add(term)

    prime_implicants = set()
    
    while groups:
        next_groups = {}
        combined_terms = set()
        
        sorted_keys = sorted(groups.keys())
        for i in range(len(sorted_keys) - 1):
            key1 = sorted_keys[i]
            key2 = sorted_keys[i+1]
            if key2 == key1 + 1:
                for term1 in groups[key1]:
                    for term2 in groups[key2]:
                        combined = combine(term1, term2)
                        if combined:
                            if key1 not in next_groups:
                                next_groups[key1] = set()
                            next_groups[key1].add(combined)
                            combined_terms.add(term1)
                            combined_terms.add(term2)
        
        uncombined = set()
        for key in groups:
            uncombined.update(groups[key] - combined_terms)
        prime_implicants.update(uncombined)
        
        groups = next_groups

    # Stage 2: Prime Implicant Chart
    chart = {m: [] for m in minterms}
    pi_map = {} 
    for pi in prime_implicants:
        pi_map[pi] = []
        for m_idx, m_bin in enumerate(mt_bins):
            m = minterms[m_idx]
            covers = True
            for i in range(num_vars):
                if pi[i] != '-' and pi[i] != m_bin[i]:
                    covers = False
                    break
            if covers:
                chart[m].append(pi)
                if m not in pi_map[pi]:
                    pi_map[pi].append(m)

    # Stage 3: Select Minimal Cover (using a greedy approach)
    essential_pi = set()
    covered_minterms = set()

    for m in chart:
        if len(chart[m]) == 1:
            pi = chart[m][0]
            essential_pi.add(pi)
    
    for pi in essential_pi:
        covered_minterms.update(pi_map[pi])

    uncovered_minterms = set(minterms) - covered_minterms
    cover = set(essential_pi)
    
    remaining_pi = sorted(list(prime_implicants - essential_pi), key=lambda p: (len(pi_map[p]), -p.count('-')), reverse=True)

    while uncovered_minterms:
        best_pi = None
        # Find PI that covers the most uncovered minterms
        best_pi = max(remaining_pi, key=lambda pi: len(set(pi_map[pi]) & uncovered_minterms))
        
        if best_pi and len(set(pi_map[best_pi]) & uncovered_minterms) > 0:
            cover.add(best_pi)
            uncovered_minterms -= set(pi_map[best_pi])
        else:
            # No more progress can be made
            break

    return " + ".join(sorted([pi_to_str(pi) for pi in cover], key=lambda x: (len(x), x)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python kmap_solver.py <num_variables> [minterm1 minterm2 ...]")
        sys.exit(1)

    num_vars = int(sys.argv[1])
    minterms = [int(m) for m in sys.argv[2:]]
    
    result = quine_mccluskey(num_vars, minterms)
    print(result)
