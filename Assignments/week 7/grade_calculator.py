import csv
import random

filename = "/Users/finjakoeppen/Desktop/UNI/Digital Media/Technical Basics I_2025 - Sheet1.csv"
output_filename = "updated_class_grades.csv"

try:
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        fieldnames = list(reader.fieldnames)

    weeks = [f"Week {i}" for i in range(1, 14) if i != 6]
    for week in weeks:
        if week not in fieldnames:
            fieldnames.append(week)
            for row in rows:
                row[week] = ''

    for row in rows:
        for week in weeks:
            value = row[week].strip() if row[week] else ''
            if value == "":
                row[week] = str(random.randint(0, 3))

    for row in rows:
        grades = []
        for week in weeks:
            value = row[week].strip()
            try:
                grade = int(value)
                grades.append(grade)
            except ValueError:
                pass

        # Total Points
        best_10 = sorted(grades, reverse=True)[:10]
        total_points = min(sum(best_10), 30)
        row["Total Points"] = str(total_points)

        # Average Points
        if grades:
            average_points = round(sum(grades) / len(grades), 2)
        else:
            average_points = 0
        row["Average Points"] = str(average_points)

    # Adding new columns
    if "Total Points" not in fieldnames:
        fieldnames.append("Total Points")
    if "Average Points" not in fieldnames:
        fieldnames.append("Average Points")

    # Creating new csv file
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        print(f"New file saved to: {output_filename}")

    # Bonus
    streams = set(row.get("Stream", "").strip() for row in rows)
    print("\n Average points per stream:")
    for stream in streams:
        if not stream:
            continue
        stream_rows = [row for row in rows if row.get("Stream", "").strip() == stream]
        if stream_rows:
            average = round(sum(float(row["Average Points"]) for row in stream_rows) / len(stream_rows), 2)
            print(f"  Stream {stream}: {average} points")

    # Average points per week
    print("\nAverage points per week:")
    for week in weeks:
        week_grades = []
        for row in rows:
            value = row[week].strip()
            if value.isdigit():
                week_grades.append(int(value))
        if week_grades:
            average = round(sum(week_grades) / len(week_grades), 2)
            print(f"  {week}: {average} points")

except FileNotFoundError:
    print(f"File {filename} not found!")
except Exception as e:
    print(f"An error occurred: {e}")
