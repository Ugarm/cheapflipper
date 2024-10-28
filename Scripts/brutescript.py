import msoffcrypto
import openpyxl
import os

def bruteUppercase(itérations, passwordList, decrypted_file_path, file_path, log_callback) :
    data_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Data'))
    password_found = False
    for x in range (itérations):
        for passwordIndex in passwordList:
            pw = passwordIndex.title() + str(x)
            full_path = os.path.join(data_folder_path, file_path)
            print(pw)
            try:
                with open(full_path, 'rb') as file:

                    office_file = msoffcrypto.OfficeFile(file)
                    office_file.load_key(password=pw)

                    with open(decrypted_file_path, 'wb') as decrypted_file:
                        office_file.decrypt(decrypted_file)

                workbook = openpyxl.load_workbook(decrypted_file_path)
                sheet = workbook.active

                os.startfile(decrypted_file_path)
                print("Mot de passe :", pw)
                password_found = True
                break  

            except Exception as e:

                continue
        if password_found : 
            log_callback(f"Mot de passe trouvé: {pw}")
            break
          

        if not password_found:
            print("No valid password found.") 

def bruteRetardedPw(itérations, passwordList, decrypted_file_path, file_path, log_callback):
    data_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Data'))
    password_found = False
    for x in range (itérations):
        for passwordIndex in passwordList:
            pw = passwordIndex + str(x)
            full_path = os.path.join(data_folder_path, file_path)
            print(pw)
            print(full_path)
            try:
                with open(full_path, 'rb') as file:
    
                    office_file = msoffcrypto.OfficeFile(file)
                    office_file.load_key(password=pw)

                    with open(decrypted_file_path, 'wb') as decrypted_file:
                        office_file.decrypt(decrypted_file)

                workbook = openpyxl.load_workbook(decrypted_file_path)
                sheet = workbook.active

                os.startfile(decrypted_file_path)
                print("Mot de passe :", pw)
                password_found = True
                break 
            

            except Exception as e:

                continue

        if password_found : 
            log_callback(f"Found password: {pw}")
            break
            

        if not password_found:
            
            continue