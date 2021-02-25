# Hashcode 2020 

# =============================================================================
# File Data Extract
# =============================================================================
filename = ["e_so_many_books.txt",]


# =============================================================================
# '''["a_example.txt","b_read_on.txt","c_incunabula.txt","d_tough_choices.txt",
#             "e_so_many_books.txt","f_libraries_of_the_world.txt"]'''
# =============================================================================

for file in filename:

    with open(file,"r+") as f:
        data_set_example = f.read()
        f.close()
        
    data_set_example = data_set_example.split("\n")
    
    string = data_set_example[-1]
    while len(string) == 0:
        del data_set_example[-1]
        string = data_set_example[-1]
        
    
    for i in range(len(data_set_example)):
        data_set_example[i] = data_set_example[i].split(" ")
        data_set_example[i] = [int(data_set_example[i][j]) for j in range(len(data_set_example[i]))]

    lib_list = data_set_example[2:]
    s = data_set_example[1]
    
    new_lib_list = []
    
    def score_lib(lib,s):
      
        score = 0
        for i in range(len(lib[1])):
            score += s[lib[1][i]]
        return score
            
    def time_taken(lib, time):
        time_sign_up = lib[0][1]
        return time > time_sign_up
        
    
    
    for i in range(0, len(lib_list), 2):
        new_lib_list = new_lib_list + [[lib_list[i],lib_list[i+1]]]

    
    for i in range(len(new_lib_list)):
        new_lib_list[i] += [[score_lib(new_lib_list[i],s)]]
        
    
    
    lib_list = new_lib_list[:]
    new_lib_list.sort(key = lambda x:sum(x[2]), reverse = True)
    
 
    total_time = data_set_example[0][-1]
    
    total_score = 0
    
    dupe_lib = new_lib_list[:]
    
    def re_score(lib,s):
        score = 0
        books_used = []
        for i in range(len(lib[1])):
            score += s[lib[1][i]]
            if s[lib[1][i]] != 0:
                books_used += [lib[1][i]]
            s[lib[1][i]] = 0
        return score, s, books_used
    
    
    
    
    def library_index(libs, new_libs):
        return new_libs.index(libs)
    
    
    
    books_scanned = []
    books_length = len(books_scanned)
    libs_used = []
    while len(dupe_lib) > 0:
        time = time_taken(dupe_lib[0], total_time)
        if time == True and total_time > 0:
            total_time -= (dupe_lib[0][0][1] + float(dupe_lib[0][0][0]/dupe_lib[0][0][2]))
            lib_score = re_score(dupe_lib[0],s)
            s = lib_score[1]
            books_scanned = books_scanned + [lib_score[2]]
            if len(books_scanned) > books_length:
                libs_used += [library_index(dupe_lib[0],lib_list)]
            lib_score = lib_score[0]          
            total_score += lib_score
        dupe_lib = dupe_lib[1:]
        books_length = len(books_scanned)
        print(total_score)
        

# =============================================================================
#     print(books_scanned)
#     print(libs_used)
# =============================================================================
    print(total_score)
    print()
    # =============================================================================
    # Output Format
    # =============================================================================
    
    f = open("submissionfile_" + file ,"w+")
    f.write(str(len(libs_used)) + "\n")
    for i in range(len(libs_used)):
        f.write(str(libs_used[i]) + " " + str(len(books_scanned[i])) + "\n")
        for j in range(len(books_scanned[i])):       
            f.write(str(books_scanned[i][j]) + " ")
        f.write("\n")
    f.close()
    
    



