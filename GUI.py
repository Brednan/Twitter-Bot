import tkinter
import Event_Manager
import threading

window = tkinter.Tk()
window.wm_title('Twitter Follow Bot')
window.geometry('600x800')
window.resizable(False, False)

def pop_up_msg(message):
    popup = tkinter.Tk()
    popup.wm_title('Error!')
    
    if(message == 'Something went wrong! Most likely there is something wrong with your combolist'):
        popup.geometry('830x100')
    else:
        popup.geometry('400x100')

    label = tkinter.Label(popup, text=message, font=('default', 17))
    label.place(x=10, y=10)
    popup.mainloop()


accs_tried = tkinter.Label(window, text='Tried:', font=('default', 17))
accs_tried.place(x=160, y=660)

working = tkinter.Label(window, text="Working:", font=('default', 17))
working.place(x=160, y=700)

failed = tkinter.Label(window, text="Failed:", font=('default', 17))
failed.place(x=160, y=740)


username_input_label = tkinter.Label(window, font=('default', 25), text='Target Username:')
username_input_label.place(x=100, y=10)
username_input = tkinter.Entry(window, font=('default', 25))
username_input.place(x=100, y=70)

account_list_label = tkinter.Label(window, font=('default', 20), text='Insert Accounts:')
account_list_label.place(x=25, y=200)
accounts_list = tkinter.Text(window, font=('default', 20), width=35, height=12)
accounts_list.place(x=25, y=250)

submit_button = tkinter.Button(window, font=('default', 20), text='Submit', command=lambda: threading.Thread(target=Event_Manager.handle_submission,args=(accounts_list.get('0.0', 'end-1c'), username_input.get(), accs_tried, working, failed, pop_up_msg)).start())
submit_button.place(x=20, y=650)

window.mainloop()