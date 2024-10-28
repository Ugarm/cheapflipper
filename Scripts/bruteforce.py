import msoffcrypto
import openpyxl
import os
import Scripts.fetch_passwords as fetch_pw

def regularBruteForce(file_path, passwordListRoute, log_callback):
    
    file_path = 'testfile.xlsx'
    decrypted_file_path = 'decrypted_file.xlsx'
    passwordList = fetch_pw.fetchPasswordList(passwordListRoute)
    password_found = False
    data_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Data'))
    full_path = os.path.join(data_folder_path, file_path)

    for passwordIndex in passwordList:
        try:
            print(passwordIndex)
            with open(full_path, 'rb') as file:

                office_file = msoffcrypto.OfficeFile(file)
                office_file.load_key(password=passwordIndex)

                with open(decrypted_file_path, 'wb') as decrypted_file:
                    office_file.decrypt(decrypted_file)

            workbook = openpyxl.load_workbook(decrypted_file_path)
            sheet = workbook.active

            os.startfile(decrypted_file_path)
            print("Mot de passe :", passwordIndex)
            password_found = True

            break  

        except Exception as e:

            continue
    if password_found:
        log_callback(f"Found password: {passwordIndex}")

    if not password_found:
        print("No valid password found.")
