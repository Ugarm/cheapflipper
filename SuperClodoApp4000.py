import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from Scripts.bruteforce import regularBruteForce
from Scripts.customBruteforce import customBruteForce

class App:
    def __init__(self, master):
        self.master = master
        master.title("MEGA CLODO APP 4000")

        self.load_image()

        # REGULAR BRUTE FORCE
        self.label1 = tk.Label(master, text="Liste de mots de passe à tester (format txt):")
        self.label1.pack()

        self.password_file_entry = tk.Entry(master)
        self.password_file_entry.pack()

        self.label2 = tk.Label(master, text="Nom du fichier Excel:")
        self.label2.pack()

        self.excel_file_entry = tk.Entry(master)
        self.excel_file_entry.pack()

        self.regular_button = tk.Button(master, text="Forcer brusquement", command=self.start_regular_brute_force)
        self.regular_button.pack()

        # CUSTOM BRUTE FORCE
        self.label3 = tk.Label(master, text="Entrez des mots clés (séparés par des virgules):")
        self.label3.pack()

        self.passwords_entry = tk.Entry(master)
        self.passwords_entry.pack()

        self.label4 = tk.Label(master, text="Nom du fichier Excel (pour la force personnalisée):")
        self.label4.pack()

        self.custom_excel_file_entry = tk.Entry(master)  # Nouveau champ pour le fichier Excel
        self.custom_excel_file_entry.pack()

        self.label5 = tk.Label(master, text="Entrez le nombre d'itérations (1 = motclé1, 1000 = motclé1000):")
        self.label5.pack()

        self.iterations_entry = tk.Entry(master)
        self.iterations_entry.pack()

        self.label6 = tk.Label(master, text="Tester avec une majuscule au début ? (1 pour oui, 0 pour non):")
        self.label6.pack()

        self.uppercase_entry = tk.Entry(master)
        self.uppercase_entry.pack()

        self.custom_button = tk.Button(master, text="Forcer brusquement", command=self.start_custom_brute_force)
        self.custom_button.pack()

        # Output logs
        self.output_text = tk.Text(master, width=80, height=20, wrap=tk.WORD)
        self.output_text.pack(pady=(10, 0))

        self.ok_button = tk.Button(master, text="OK", command=self.close_window)
        self.ok_button.pack(pady=(5, 10))

    def load_image(self):
        """Charge et affiche l'image CheapFlipperLogo depuis le dossier Assets."""
        image_path = os.path.join("Assets", "CheapFlipperLogo.gif")  # Assurez-vous que l'extension est correcte
        print(image_path)
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # Créer un label pour afficher l'image
        self.image_label = tk.Label(self.master, image=self.photo)
        self.image_label.pack(pady=(10, 0))

    def log_output(self, message):
        """Insert message into the output text area."""
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)

    def start_regular_brute_force(self):
        password_list_file = self.password_file_entry.get().strip()
        excel_file_name = self.excel_file_entry.get().strip()

        # Append the file extensions if not already present
        if not password_list_file.endswith('.txt'):
            password_list_file += '.txt'
        if not excel_file_name.endswith('.xlsx'):
            excel_file_name += '.xlsx'

        if not password_list_file or not excel_file_name:
            messagebox.showerror("Input Error", "Veuillez remplir les deux champs.")
            return

        try:
            self.output_text.insert(tk.END, f"Démarrage de la force brute régulière sur {excel_file_name}...\n")
            regularBruteForce(excel_file_name, password_list_file, self.log_output)
            self.log_output("Force brute régulière terminée.")
        except Exception as e:
            self.output_text.insert(tk.END, f"Erreur : {str(e)}\n")
            messagebox.showerror("Erreur", str(e))

    def start_custom_brute_force(self):
        file_path = self.custom_excel_file_entry.get().strip()  # Utiliser le nouveau champ pour le fichier Excel
        decrypted_file_path = 'decrypted_file.xlsx'

        # Append the file extension if not already present
        if not file_path.endswith('.xlsx'):
            file_path += '.xlsx'

        iterations = int(self.iterations_entry.get())
        password_list_input = self.passwords_entry.get()
        password_list = [pw.strip() for pw in password_list_input.split(",")]
        do_upper_case_search = int(self.uppercase_entry.get())

        if not file_path or not password_list or iterations <= 0:
            messagebox.showerror("Input Error", "Veuillez remplir tous les champs correctement.")
            return

        try:
            self.output_text.insert(tk.END, f"Démarrage de la force brute personnalisée sur {file_path}...\n")
            customBruteForce(iterations, password_list, decrypted_file_path, file_path, do_upper_case_search, self.log_output)
            self.log_output("Forçage brutal custom terminé.")
        except Exception as e:
            self.output_text.insert(tk.END, f"Erreur : {str(e)}\n")
            messagebox.showerror("Erreur", str(e))

    def close_window(self):
        self.master.destroy()  # Closes the application


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
