import sys
import click
from docker import DockerClient

@click.command()
@click.argument('pid')
def cli(pid):
    """Find Docker container for a given PID."""

    def get_processes():
        for container in dc.containers.list():
            for process in container.top()['Processes']:
                process.append(container.name)
                yield process

    dc = DockerClient(base_url='unix:///var/run/docker.sock')   ## TODO make this configurable
    processes = {p[1]:p for p in get_processes()}
    
    if pid in processes:
        print(processes[pid][8])
    else:
        print(f"pid {pid} not found in any running Docker container.")
        sys.exit(-1)
