from Scripts.brutescript import bruteRetardedPw, bruteUppercase



def customBruteForce(itérations, passwordList, decrypted_file_path, file_path, doUpperCaseSearch, log_output):
    print('entered')
    if doUpperCaseSearch == 1 :
        print('do upper case search')
        bruteRetardedPw(itérations, passwordList, decrypted_file_path, file_path, log_output)
        bruteUppercase(itérations, passwordList, decrypted_file_path, file_path, log_output)

    else: 
        print('no upper case search')
        bruteRetardedPw(itérations, passwordList, decrypted_file_path, file_path, log_output)
