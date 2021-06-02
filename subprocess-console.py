import subprocess

def on_task_close():
    proc.kill()

'''def on_task_open():
    global proc
    import subprocess
    from subprocess import Popen, PIPE
'''

proc = subprocess.Popen(['full_dir', '-e', 'bash', '/*/*/OpenFOAM/QW'],
                        shell=True)