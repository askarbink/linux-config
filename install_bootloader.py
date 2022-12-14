#!/usr/bin/env python

import subprocess

from tools import system_info

is_dual_boot = system_info.is_dual_boot()


print("\nYou should run this script right after you did “arch-chroot”.")


# Bootloader ID

repeat = False

while True:
    if not repeat:
        bootloader_id = input(
            "\nBootloader ID "
            '(default="Linux Boot Manager", don’t use quotes): '
        ).strip()
    else:
        bootloader_id = input(
            "\nBootloader ID "
            '(default="Linux Boot Manager", DO NOT USE QUOTES!): '

        ).strip()

    if not bootloader_id:
        bootloader_id = "Linux Boot Manager"

    elif '"' in bootloader_id:
        print("Incorrect value! Try again…")
        repeat = True
        continue

    break


# Confirmation

print(
    "\nOverview:\n"
    f"Bootloader ID: {bootloader_id}\n"
    f"Detected Windows: {is_dual_boot}"
)

while True:
    confirmation = input(
        "\nProceed with installation? [Y/n]: "
    ).strip().lower()

    if confirmation in ('y', 'yes', ''):
        print("\nStarting installation!")

    elif confirmation in ('n', 'no'):
        print("\nHave a beautiful time!\n")
        exit()

    else:
        print("Incorrect value! Try again…")
        continue

    break


# Root Password

print(
    "\nYou need to set your root password in order to be able to log in."
)

subprocess.run('passwd', shell=True)


# Package Installation

packages = ['efibootmgr', 'grub', 'networkmanager']

if is_dual_boot:
    # packages += ['dosfstools', 'mtools', 'ntfs-3g']
    packages.append('ntfs-3g')

subprocess.run(f'pacman -S {" ".join(packages)}', shell=True)


# Autostarting Network Manager

subprocess.run('systemctl enable NetworkManager', shell=True)


# GRUB Installation

subprocess.run(
    'grub-install '
    '--target=x86_64-efi '
    '--efi-directory=/boot '
    f'--bootloader-id="{bootloader_id}"',
    shell=True
)

subprocess.run('grub-mkconfig -o /boot/grub/grub.cfg', shell=True)


# Success Message

print(
    "\nDone!\n"
    "Now you need to reboot and then log in as “root” (it is the login).\n"
)
