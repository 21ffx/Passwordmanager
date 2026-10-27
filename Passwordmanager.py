#ToDo:

#json file für saved passwords die dann wieder laden beim start der app
#password generator mit konfigurierbarer länge und optionen (zahlen, sonderzeichen, großbuchstaben)
#Passwort stärke prüfen
#Einträge editieren und löschen
#Verschlüsselung und sichere Anmeldung


import customtkinter as ctk


username = 'fx'
password = '123'

password_entries = []

def enter_pressed(event=None):
    current_action()

def login():
    global current_action

    username_get = username_entry.get()
    password_get = password_entry.get()
    
    if username_get == username and password_get ==password:

        login_frame.pack_forget()
        home_frame.pack(fill='both', expand=True)

        current_action = new_passwords

        return

    else:
        ctk.CTkLabel(login_frame,
                     text='Wrong Username or Password'
                     ).place(relx = 0.5, rely=0.5, anchor='center')

def new_passwords():
    webapp = pwmanager_webapp_entry.get()
    username = pwmanager_user_entry.get()
    password = pwmanager_pw_entry.get()

    if webapp and username and password:
        entry = {
            'website': webapp,
            'username': username,
            'password': password
        }

        password_entries.append(entry)

        pwmanager_webapp_entry.delete(0, 'end')
        pwmanager_user_entry.delete(0, 'end')
        pwmanager_pw_entry.delete(0, 'end')

        refresh_password_list()

        
    else:
        print('wrong')

def refresh_password_list():

    for widget in saved_passwords_frame.winfo_children():
        widget.destroy()

    for entry in password_entries:
        password_frame = ctk.CTkFrame(saved_passwords_frame)

        password_frame.pack(
            fill='x',
            padx=5,
            pady=5
        )

        website_label = ctk.CTkLabel(
            password_frame,
            text=entry['website'],
            width=150,
            anchor='w'
        )
        
        website_label.pack(
            side='left',
            padx = 10)

        username_label = ctk.CTkLabel(
            password_frame,
            text=entry['username'],
            width=150,
            anchor='w'
        )

        username_label.pack(
            side='left',
            padx=10
        )


        password_label = ctk.CTkLabel(
            password_frame,
            text='********',
            width=120
        )

        password_label.pack(
            side='left',
            padx=10
        )
        
        

#App settings
app = ctk.CTk()
app.title('Passwordmanager')
app.geometry('720x480')

ctk.set_appearance_mode('dark')


#Login
current_action = login

login_frame = ctk.CTkFrame(app)
login_frame.pack(fill= 'both', expand=True)

ctk.CTkLabel(login_frame, text='Login').pack(pady=10)


username_entry = ctk.CTkEntry(master=login_frame, 
                              placeholder_text='Username')
password_entry = ctk.CTkEntry(master=login_frame, 
                              placeholder_text='Password')

username_entry.pack(pady=5)
password_entry.pack(pady=5)

#Login Button
btn_enter = ctk.CTkButton(master= login_frame, 
                    text='Enter',
                    corner_radius=32,
                    fg_color='#4158D0',
                    hover_color="#540CC7",
                    border_color='#FFFFFF',
                    border_width=2,
                    command=login)

btn_enter.place(relx=0.5, rely=0.3, anchor='center')








#pwmanager
home_frame = ctk.CTkFrame(app)

ctk.CTkLabel(home_frame,
                text='Homescreen').pack(pady=10)

#pwmanager new passwords
ctk.CTkLabel(home_frame,
             text='New Passwords').place(relx = 0.15,
                                          rely=0.2,
                                          anchor= 'center')

pwmanager_webapp_entry = ctk.CTkEntry(master=home_frame,
             placeholder_text='Website/App')

pwmanager_user_entry = ctk.CTkEntry(master=home_frame,
                          placeholder_text='Username')

pwmanager_pw_entry = ctk.CTkEntry(master=home_frame,
                        placeholder_text='Password')

pwmanager_webapp_entry.place(relx = 0.15,
                   rely = 0.3,
                   anchor= 'center')
pwmanager_user_entry.place(relx = 0.15,
                 rely = 0.37,
                 anchor = 'center')
pwmanager_pw_entry.place(relx = 0.15,
                rely = 0.44,
                anchor = 'center')

#pwmanager button
btn_enter = ctk.CTkButton(master= home_frame, 
                    text='Add',
                    corner_radius=32,
                    fg_color='#4158D0',
                    hover_color="#540CC7",
                    border_color='#FFFFFF',
                    border_width=2,
                    command=new_passwords)

btn_enter.place(relx=0.15, rely=0.54, anchor='center')








#Gen PW
ctk.CTkLabel(home_frame,
             text='Generate Password').place(relx = 0.85,
                                             rely = 0.2,
                                             anchor = 'center')

ctk.CTkLabel(home_frame,
             text='Gen PW').place(relx = 0.85,
                            rely = 0.3,
                            anchor = 'center')





#Saved PW

ctk.CTkLabel(
    home_frame,
    text='Saved Passwords'
).place(
    relx=0.15,
    rely=0.62,
    anchor='center'
)


saved_passwords_frame = ctk.CTkScrollableFrame(
    home_frame,
    width=400,
    height=120
)

saved_passwords_frame.place(
    relx=0.15,
    rely=0.82,
    anchor='center'
)









app.bind('<Return>', enter_pressed)

app.mainloop()


