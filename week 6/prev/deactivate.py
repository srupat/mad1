import os

def deactivate_env():
    with open('.venv', 'r') as file:
        venv_name = file.readline().strip()

    os.system(f'deactivate')

    print(f'Virtual environment "{venv_name}" deactivated.')

if __name__ == "__main__":
    deactivate_env()
