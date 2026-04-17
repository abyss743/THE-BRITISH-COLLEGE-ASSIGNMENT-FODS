from pathlib import Path
import csv
import sys

CSV_FILE = Path("records.csv")          # Please change the path according to your folder

def display_students() -> None:
    try:
        with CSV_FILE.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            
            if reader.fieldnames:
                reader.fieldnames = [col.lstrip('\ufeff') for col in reader.fieldnames]
            
            required = {'student_name', 'roll_no', 'program', 'year', 'group'}
            actual = set(reader.fieldnames) if reader.fieldnames else set()
            
            if not required.issubset(actual):
                missing = required - actual
                print(f"Error: Missing required columns in CSV: {missing}")
                print(f"Available columns : {reader.fieldnames}")
                print("\nTip: Open your CSV in Notepad++ or VS Code and save as UTF-8 (without BOM)")
                sys.exit(1)

            print(f"{'Name':<20} {'Roll':<10} {'Program':<15} {'Year':<6} {'Group':<8}")
            print("-" * 65)

            # Process and display rows
            row_count = 0
            for row in reader:
                try:
                    print(
                        f"{row['student_name']:<20} "
                        f"{row['roll_no']:<10} "
                        f"{row['program']:<15} "
                        f"{row['year']:<6} "
                        f"{row['group']:<8}"
                    )
                    row_count += 1
                except KeyError as e:
                    print(f"Warning: Missing data in row {row_count + 1} → {e}")
                    continue
                except Exception as row_err:
                    print(f"Error processing row {row_count + 1}: {row_err}")
                    continue

            print(f"\nTotal students displayed: {row_count}")

    except FileNotFoundError:
        print(f"❌ File not found: {CSV_FILE.resolve()}")
        print("Solutions:")
        print("   1. Make sure records.csv exists at the path above")
        print("   2. Or change CSV_FILE to the correct location")
        print("   3. Recommended: Use relative path (Option 3)")

    except PermissionError:
        print(f"❌ Permission denied when reading: {CSV_FILE}")

    except csv.Error as e:
        print(f"❌ CSV format error: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Student Records Viewer Started...\n")
    display_students()
