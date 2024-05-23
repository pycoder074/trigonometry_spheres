import cos_values as cos
import sine_values as sin
import tan_values as tan
import subprocess
def installer(capture_output):
    # capture output used to see cli output in IDE shell
    subprocess.run('cmd /k python -m pip install -r requirements.txt', capture_output = capture_output)
    installer()

def run_sine():
    sin.main()

def run_tan():
    tan.main()

def run_cos():
    cos.main()
install = input('Would you like to install modules? (y/n) ')
match install:
    case 'y':
        cap_output = input('Capture output to shell? (y/n) ')
        match cap_output:
            case 'y':
                installer(capture_output = True)
            case 'n':
                installer(capture_output = False)
    case 'n':
        
        function = input('What graph would you like to see? \n 1) Sine \n 2) Cos \n 3) Tan \n')

        match function:
            case '1':
                run_sine()
            case '2':
                run_cos()
            case '3':
                run_tan()

            
