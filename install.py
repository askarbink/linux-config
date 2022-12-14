#!/usr/bin/env python

import os
import subprocess

from tools import shortcuts, system_info

while True:
    timezone = input(
        "\nTimezone:\n"
        "(You can watch them in /usr/share/zoneinfo)\n"
    ).strip()

    if not os.path.isfile(f'/usr/share/zoneinfo/{timezone}'):
        print("Incorrect value! Try again…")
        continue

    print(f"Selected: {timezone}")
    break

while True:
    dual_boot = input("\nDual boot with Windows? [y/N]: ").strip().lower()

    if dual_boot in ('n', 'no', ''):
        dual_boot = 'No'

    elif dual_boot in ('y', 'yes'):
        dual_boot = 'Yes'

    else:
        print("Incorrect value! Try again…")
        continue

    print(f"Selected: {dual_boot}")
    break

while True:
    desktop = input(
        "\nDesktop:\n"
        "1) None\n"
        "2) i3\n"
        "3) GNOME\n"
        "4) KDE Plasma\n"
        "Enter a number (default=1): "
    ).strip()

    if desktop in ('1', ''):
        desktop = 'i3'

    elif desktop == '2':
        desktop = 'GNOME'

    elif desktop == '3':
        desktop = 'KDE Plasma'

    else:
        print("Incorrect value! Try again…")
        continue

    print(f"Selected: {desktop}")
    break

hostname = input("\nHostname: ")

username = input("\nUsername: ")


print(
    "\nOverview:\n"
    f"Timezone: {timezone}\n"
    f"Dual boot: {dual_boot}\n"
    f"Desktop: {desktop}\n"
    f"Hostname: {hostname}\n"
    f"Username: {username}"
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

if False:
    subprocess.run(
        f'ln -sf /usr/share/zoneinfo/{timezone} /etc/localtime',
        shell=True
    )
    subprocess.run('hwclock --systohc', shell=True)

    packages = [
        'base-devel',
        'efibootmgr',
        'grub',
        'linux-zen-headers',
        'neovim',
        'networkmanager'
    ]

    if False:
        packages.append('amd-ucode')
    elif False:
        packages.append('intel-ucode')

    if dual_boot == 'Yes':
        packages += ['ntfs-3g', 'os-prober']

    if False:
        packages.append('bluez')
    if False:
        packages.append('cups')

    subprocess.run(f'pacman -S {" ".join(packages)}', shell=True)
    subprocess.run('', shell=True)


# subprocess.call('passwd')
