import subprocess

from tools import shortcuts

while True:
    choice = input(
        "\nChoose your opiton:\n"
        "0) Exit\n"
        "1) Install the GRUB bootloader\n"
        "Enter a number (default=0): "
    ).strip()

    if choice in ('0', ''):
        shortcuts.goodbye()

    elif choice == '1':
        import install_bootloader

    else:
        print("Incorrect value! Try again…")
        continue

    break
