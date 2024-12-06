from pathlib import Path

input = (Path(__file__).parent / "input.txt").read_text().strip()
input_order, input_updates = input.split("\n\n")

order = {tuple(map(int, line.split("|"))) for line in input_order.split("\n")}

result = 0
incorrect = []
for update in input_updates.split("\n"):
    update = list(map(int, update.split(",")))
    if all((a, b) in order for a, b in zip(update, update[1:])):
        result += update[len(update) // 2]
    else:
        incorrect.append(update)
print(result)


def fix_entry(entry):
    vs = set(entry)
    rules = {t for t in order if t[0] in vs and t[1] in vs}
    result = []
    while len(result) < len(entry):
        c = vs - set(result)
        for t in rules:
            c.discard(t[1])
        result.append(c.pop())
        rules = {t for t in rules if t[0] != result[-1]}
    return result


result = 0
for entry in incorrect:
    fixed_entry = fix_entry(entry)
    result += fixed_entry[len(fixed_entry) // 2]
print(result)
