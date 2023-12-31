# TrashHunter
![Capture](https://github.com/tharinduk001/TrashHunter/assets/136310961/a75e5ac3-513e-4191-9c67-eb0bb83954cb)

This is a python based software that can be used to clean the tempory files in windows 10/11 operating systems whcih causes slowness and performance reduce. So this is the initial version of the software and feel free to download and try it out completely free !

If you find any bugs or errors in this program please update in the issues section or you can directly email me.

You can clone the source code or also download the setup.exe.



## Features

- Compatible with Windows 7/8/8.1/10/11
- Lightweight
- Fast 
- Easy installation
- Speed up the computer by 5x
- Standalone


## Usage
* You need to install ***python 3.8*** or upper version inorder to use the tool. You can download *latest* python version from here : [click here to download python latest version](https://www.python.org/downloads/)

* Then you need to install the dependancies that requires for the tool. The requirements are listed down in the ***requirements.txt***

* The required libraries are :
    1. altgraph==0.17.4
    2. markdown-it-py==3.0.0
    3. mdurl==0.1.2
    4. pyarmor.cli.core==5.4.3
    5. Pygments==2.17.2
    6. pyinstaller-hooks-contrib==2023.11
    7. pywin32-ctypes==0.2.2
    8. schedule==1.2.1
    9. setuptools==69.0.3
    10. termcolor==2.4.0
    11. rich

**You can directly install the dependancies by running the following command in your cli**

```
pip install -r requirements.txt
```

* Then There are two python files are available. They are **_TrashHunterRunner.py_** and **_TrashHunter.py_**

* The main file that you want run is **_TrashHunterRunner.py_**. It is the main entry point to the program and the **_TrashHunter.py_** is the class file which contains the business logic of the program. 


## Run Locally

Clone the project

```bash
  git clone https://github.com/tharinduk001/TrashHunter.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the program
```bash
  python TrashHunterRunner.py 
```


## Deployment

To deploy this project (to create a exe)

Install the pyinstaller library to create an executable file. 

```bash
  pip install pyinstaller
```

```bash
  pyinstaller TrashHunterRunner.py --icon=icon.ico --clean   
```

## Installation

* You can run the executable direcly which has created by pyinstaller. 

    **_Note_ :-** _You need to place the Trashhunter.pyw file in the executable (TrashCleanerRunner.exe) directory._

* **OR** You can download the setup file from the releases and just run and install it.

![TrashHunter](https://github.com/tharinduk001/TrashHunter/assets/136310961/c99f6ede-e88a-4e89-ae08-4469793b1b88)


## FAQ

#### What is going on behind the project ?

What is done by the TrashHunter is simply is : cleaning the temporary files which oftently storing in the **_/temp_** folders.

#### It is safe to use the program ? 

Yes it is 100% safer both to **_OS_** and **_User privacy._**


## Screenshots

![App Screenshot](https://github.com/tharinduk001/TrashHunter/assets/136310961/59024c1d-5b5b-4726-b272-703a1e70c9a1)


![App Screenshot](https://github.com/tharinduk001/TrashHunter/assets/136310961/d646fb3a-cd89-4909-9de1-29e139c1f05c)



## Downloads
* [![TrashHunter V1.0](https://img.shields.io/badge/TrashHunterV1.0-red)](https://github.com/tharinduk001/TrashHunter/releases/download/TrashHunter_V1.0/TrashCleaner.exe)

## Contributing

Contributions are always welcome!

Please fork this repository and do new evolvements!

Please adhere to this project's `code of conduct`.


## Support

For support, email tharindukalhara73@gmail.com or join our Facebook channel https://facebook.com/profile.php?id=61554805956789 Subscribe us on YouTube https://youtube.com/@kalharaCodes?si=UcrPp9CwVN--gp_5_sub_confirmation=1


## Feedback

If you have any feedback, please reach out to us at tharindukalhara73@gmail.com 




