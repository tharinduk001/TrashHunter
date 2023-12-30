'''
If any error while using the pyinstaller use the following command with pyinstaller
--collect-all pyfiglet
'''

import os
import shutil
import getpass
import msvcrt
import time
from rich.console import Console
from rich.text import Text
from termcolor import colored

os.system("cls")

source_exe_path = ".\\TrashHunter.pyw"
destination_directory = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
welcome_message = "\tTrashHunter, crafted by Tharindu Kalhara under the alias @kalharaCodes in 2024, is a Python-powered solution designed to streamline the process of cleaning unnecessary clutter from Windows systems. This tool empowers users to effortlessly reclaim valuable disk space by identifying and removing redundant files that may accumulate over time. TrashHunter's intuitive command-line interface offers a seamless experience, allowing users to execute effective cleanup operations with just a few simple commands. Developed with a focus on efficiency and user-friendliness, TrashHunter is your go-to companion for optimizing your Windows environment. Experience a cleaner and more responsive system by following the straightforward installation guide and unleash the potential of TrashHunter on your machine."
license = "\tBefore you embark on the journey of optimizing your Windows system with TrashHunter, it's crucial to familiarize yourself with the license agreement. TrashHunter is released under an open-source license, encouraging collaboration and transparency in its development. By proceeding with the installation, you confirm your acknowledgment and acceptance of the terms outlined in the license agreement.As part of the installation process, you will encounter a confirmation prompt to ensure that you are intentionally initiating the cleanup operation. This prompt serves as a safeguard against unintentional actions, ensuring that users are fully aware of the potential impact on their system. By responding affirmatively to the confirmation prompt, you signal your intent to utilize TrashHunter for its intended purpose—efficiently cleaning and optimizing your Windows environment. Your commitment to this confirmation underscores a conscious decision to leverage TrashHunter's capabilities responsibly and proactively contribute to a streamlined and clutter-free digital workspace."

end_banner_text = '''
   __ __     ____                             __      
  / //_/__ _/ / /  ___ ________ ________  ___/ /__ ___
 / ,< / _ `/ / _ \/ _ `/ __/ _ `/ __/ _ \/ _  / -_|_-<
/_/|_|\_,_/_/_//_/\_,_/_/  \_,_/\__/\___/\_,_/\__/___/
                                                      '''

welcome_banner_text = '''                                                                       
ooooo                     8       o    o                o               
  8                       8       8    8                8               
  8   oPYo. .oPYo. .oPYo. 8oPYo. o8oooo8 o    o odYo.  o8P .oPYo. oPYo. 
  8   8  `' .oooo8 Yb..   8    8  8    8 8    8 8' `8   8  8oooo8 8  `' 
  8   8     8    8   'Yb. 8    8  8    8 8    8 8   8   8  8.     8     
  8   8     `YooP8 `YooP' 8    8  8    8 `YooP' 8   8   8  `Yooo' 8     
::..::..:::::.....::.....:..:::..:..:::..:.....:..::..::..::.....:..::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''         

def print_colored_text(text, color='white', on_color='black', style=None):
    console = Console()
    styled_text = Text.from_markup(f"[{color} on {on_color}]{text}[/]{style or ''}")
    console.print(styled_text)


def copy(src, des):
    success_state = False
    print(colored("\nStaring Installation...", 'green'))
    time.sleep(0.5)
    try:
        if not os.path.exists(src):
            print(colored(f"\nInstallation failed. {src} not found", 'red'))
            return
        if not os.path.exists(des):
            os.makedirs(des)
        
        file_name = os.path.basename(src)
        des_path = os.path.join(des,file_name)

        if not os.path.exists(des_path):
            shutil.copy2(src,des_path)
            print(colored(f"\n{file_name} has successfully mounted at {des_path}.", 'green'))
            success_state = True
            time.sleep(0.5)
        else:
            print(colored("\nProgram already installed !", 'yellow'))
            success_state = True

    except Exception as e:
        print(colored(f"\nAn error occured {e}", 'red'))
        success_state = False
    finally:
        if not (success_state): 
            confirm_text = "\nInstallation process failed. Do you want to retry or quit [R/Q] : " 
            print(colored(confirm_text, 'red'),end='')
            confirm = input()

            if not(confirm.lower() == "r"):
                print(colored("Installation Aborted... Exiting Program....", 'red'))
                exit()
            else:
                copy(source_exe_path,destination_directory)
        else:
            print(colored("\nInstallation Successfully finished...\n", 'green', attrs=['bold']))
            print(colored("-------------------------------------------------------","cyan"))
            print_colored_text(text = end_banner_text,color='white',on_color="red")
            #print(colored(end_banner_text, 'cyan',attrs=['blink','bold']))
            print(colored("A product by Tharindu Kalhara @ kalharaCodes \nContcat us on kalharacodes@gmail.com \nAll the rights received.", 'cyan'))

            time.sleep(0.25)
                                                                                    

while True:
    print_colored_text(text = welcome_banner_text,color='red')
    print_colored_text(text = welcome_message,color='blue')
    
    print(colored("\nPress enter for continue installation...", 'red',attrs=['bold']))
    user_input = getpass.getpass("")

    if  user_input.strip():
        print("Enter key not pressed.")
    else:
        print(colored(license, 'blue'))
        confirm_text = "\nDo you want to agree and continue [y/n] : " 
        print(colored(confirm_text, 'red',attrs=['bold']),end='')
        confirm = input()

        if not(confirm.lower() == "y"):
            print(colored("\nInstallation Aborted. Exiting Program...", 'red'))
            break

        copy(source_exe_path,destination_directory)

        print(colored("\nPress any key to exit... ", 'blue'),end='')
        msvcrt.kbhit()
        key = msvcrt.getch()
        break
