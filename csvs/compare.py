import csv

def compare_csv_files():
    # Read data_human.csv into a list of dictionaries
    with open('data_LLMs.csv', 'r') as file:
        data_human = list(csv.DictReader(file))
    
    # Read sn_data_human.csv into a list of dictionaries
    with open('sn_data_LLMs.csv', 'r') as file:
        sn_data_human = list(csv.DictReader(file))
    
    # Compare each dictionary and show the differences
    count_diff = {}
    diffs = []
    for i, v in enumerate(data_human):
        for key, value in v.items():
            if value != sn_data_human[i][key]:
                if key in count_diff:
                    count_diff[key] += 1
                else:
                    count_diff[key] = 1
            diffs.append(abs(float(v['SS']) - float(sn_data_human[i]['SS'])))
    
    for key, count in count_diff.items():
        print(f"Column '{key}' is different {count} times.")

    print(max(diffs))

if __name__ == "__main__":
    compare_csv_files()