import sys


def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            correct_cat_entries = 0
            intruder_doused_count = 0
            total_time_correct_cat = 0
            visits_duration = []

            for line in file:
                if line.strip() == 'END':
                    break

                parts = line.strip().split(',')
                cat_name, entry_time, exit_time = parts[0], int(parts[1]), int(parts[2])

                if cat_name == 'OURS':
                    correct_cat_entries += 1
                    total_time_correct_cat += exit_time - entry_time
                    visits_duration.append(exit_time - entry_time)
                else:
                    intruder_doused_count += 1

            if correct_cat_entries == 0:
                print("No entries for the correct cat in the log file.")
            else:
                average_duration = sum(visits_duration) / correct_cat_entries
                max_duration = max(visits_duration)
                min_duration = min(visits_duration)

                print("\nLog File Analysis")
                print("==================")
                print(f"Cat Visits: {correct_cat_entries}")
                print(f"Other Cats: {intruder_doused_count}")
                print(
                    f"Total Time in House: {total_time_correct_cat // 60} Hours, {total_time_correct_cat % 60} Minutes")
                print(f"Average Visit Length: {average_duration:.0f} Minutes")
                print(f"Longest Visit: {max_duration} Minutes")
                print(f"Shortest Visit: {min_duration} Minutes")

    except FileNotFoundError:
        print(f"Cannot open \"{file_path}\"!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        file_path = sys.argv[1]
        analyze_cat_shelter_log(file_path)

