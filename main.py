import subprocess

print(
    "\nWarning!\n"
    "This script is user-made and has been done to ease\n"
    "the installation process of Arch Linux (especially for the creator).\n"
    "Think twice before typing something!\n"
    "The script cannot fix mistakes you make."
)

print("\nMade by AskarBink.")

while True:
    choice = input(
        "\nChoose your opiton:\n"
        "0) Exit\n"
        "1) Install the GRUB bootloader\n"
        "Enter a number (default=0): "
    ).strip()

    if choice in ('0', ''):
        print("\nHave a beautiful time!\n")

    elif choice == '1':
        import install_bootloader

    else:
        print("Incorrect value! Try again…")
        continue

    break
