# Napisac funkcje wykonujaca kopiowanie pliku, ktora pomija linie 
# rozpoczynajace sie od znaku '#' (linie z komentarzami)

def delete_comment(src_file, dst_file):
    file_first = open(src_file, "r")
    file_second = open(dst_file, "w")

    for line in file_first:
        if line[0] == '#':
            continue
        file_second.write(line)
    
    file_first.close()
    file_second.close()

if __name__ == "__main__":
    delete_comment("task001_input.txt", "task001_output.txt")
