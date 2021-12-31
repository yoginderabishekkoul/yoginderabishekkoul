

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def search_block_string_in_file(file_name, string_to_search):
    Start = string_to_search
    End = "}"
    started = False
    collected_lines = []

    with open(file_name, "r") as fp:
        for i, line in enumerate(fp.readlines()):
            if Start in line.rstrip():
                started = True
                print("started at line", i)  # counts from zero !
                continue

            if started:
                collected_lines.append((i, line.rstrip()))
                if line.rstrip() == End:
                    started = False
                    print("end at line", i)
    return collected_lines

def main():
    #string_to_search = input("string_to_search: ")
    #file_name="fix_gw_logs_for_fullgrep_script.log"
    #Lines=search_string_in_file(file_name, string_to_search)
    #for line in Lines:
    #    print(line)
    string_to_search = input("string_to_search: ")
    file_name="lse_gw_logs_for_order_chain_script.log"
    Lines = search_string_in_file(file_name, string_to_search)
    Lines1=search_block_string_in_file(file_name, string_to_search)
    for line in Lines1:
        print(line)


if __name__ == '__main__':
    main()