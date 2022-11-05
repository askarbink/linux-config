import subprocess


def get_cpu_vendor() -> str:
    """
    Return values:
    - “Authentic AMD”
    - “GenuineIntel”
    """

    cpu_info = open('/proc/cpuinfo')

    for line in cpu_info.readlines():
        if line.startswith('vendor_id'):
            return line.split()[-1]


def get_gpu_vendor() -> str:
    """
    Return values:
    - “ATI”
    - “Intel”
    - “NVIDIA”
    """

    gpu_info = subprocess.getoutput('lspci | grep VGA')

    return gpu_info.split()[4]


def is_dual_boot() -> bool:
    """
    Returns a Boolean value based on the presence of Windows partitions.
    """

    patterns = (
        ['100M', 'EFI', 'System'],
        ['16M', 'Microsoft', 'reserved'],
        ['Microsoft', 'basic', 'data']
    )

    matches = len(patterns) * [False]

    partition_info = subprocess.getstatusoutput('sudo fdisk -l')

    if partition_info[0] != 0:
        partition_info = subprocess.getstatusoutput('fdisk -l')

    for line in partition_info[1].split('\n'):
        end = line.split()[-3:]

        for i in range(len(patterns)):
            matches[i] += (end == patterns[i])

        if all(matches):
            return True

    return False
