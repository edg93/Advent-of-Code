def parse_input(filename):
    with open(filename) as f:
        rules_raw, messages = f.read().split("\n\n")

    rules = {}
    for line in rules_raw.splitlines():
        idx, rest = line.split(": ")
        idx = int(idx)
        if '"' in rest:
            rules[idx] = rest.replace('"', '')
        else:
            rules[idx] = [
                list(map(int, option.split()))
                for option in rest.split(" | ")
            ]

    return rules, messages.splitlines()

def count_matches(rules, messages):
    def match(rule_id, message):
        """
        Returns a set of suffixes remaining after matching rule_id
        against the start of message.
        """
        rule = rules[rule_id]

        # Literal rule
        if isinstance(rule, str):
            if message.startswith(rule):
                return {message[len(rule):]}
            return set()

        # Non-literal
        remainders = set()
        for option in rule:
            current = {message}
            for subrule in option:
                next_current = set()
                for m in current:
                    next_current |= match(subrule, m)
                current = next_current
                if not current:
                    break
            remainders |= current

        return remainders

    count = 0
    for msg in messages:
        if "" in match(0, msg):
            count += 1
        
    return count


def solve(filename):
    # -------- Part 1 --------
    rules, messages = parse_input(filename)
    part1 = count_matches(rules, messages)

    # -------- Part 2 --------
    # Modify rules 8 and 11 *only*
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    part2 = count_matches(rules, messages)

    return part1, part2


for file in ["AoC2020_19_ex.txt", "AoC2020_19_data.txt"]:
    p1, p2 = solve(file)
    print(file)
    print("Part 1:", p1)
    print("Part 2:", p2)
    print()
