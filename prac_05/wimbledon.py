"""
CP1404
Wimbledon
"""
filename = "wimbledon.csv"


def main():
    results = find_results(filename)
    win_to_count, countries = convert_results(results)
    print_results(win_to_count, countries)


def find_results(filename):
    results = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            results.append(parts)
    return results


def convert_results(results):
    win_to_count = {}
    countries = set()
    for result in results:
        countries.add(result[1])
        try:
            win_to_count[result[2]] += 1
        except KeyError:
            win_to_count[result[2]] = 1
    return win_to_count, countries


def print_results( win_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in win_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
