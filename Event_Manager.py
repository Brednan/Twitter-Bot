from bot import *
import threading

class T(Exception):
    pass

def split_accounts(accounts):
    accounts_filtered = [item.split(':') for item in accounts.split(',')]

    list_of_accs = []
    for i in accounts_filtered:
        list_of_accs.append({"username":i[0].strip(), "password":i[1].strip()})

    return list_of_accs


def handle_submission(accounts, target_name, accs_tried, working_accs, failed_accs, popup_msg):
    tried_int = 0
    working_int = 0
    failed_int = 0
    
    working_accs.config(text=f'Working: {working_int}')
    failed_accs.config(text=f'Failed: {failed_int}')

    try:
        if len(target_name.strip()) > 0:
            accs_list = split_accounts(accounts)
            for i in accs_list:
                try:
                    bot_procedure(i['username'], i['password'], target_name)
                    working_int = working_int + 1
                    working_accs.config(text=f'Working: {working_int}')
                except Exception as e:
                    failed_int = failed_int + 1
                    failed_accs.config(text= f'Failed: {failed_int}')
                    print(e)
                finally:
                    tried_int = tried_int + 1
                    accs_tried.config(text= f'Tried: {tried_int}')
        else:
            raise T

    except IndexError:
        popup_msg('Something went wrong! Most likely there is something wrong with your combolist')
        print("Something went wrong! Most likely there is something wrong with your combolist")
    except T:
        popup_msg('You must include the target name!')
    except:
        popup_msg('There was an unknown error!')
        print("There was an unkown error!")


def bot_procedure(user, password, target_user):
    driver = initialize()
    try:
        go_to_login_page(driver)
    except:
        go_to_login_page_alternative(driver)
    insert_email(driver, user)
    insert_password(driver, password)
    find_person(driver, target_user)
    follow_person(driver)
    quit(driver)