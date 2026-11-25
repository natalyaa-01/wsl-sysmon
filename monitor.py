import time
import platform
import psutil
from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()

    
def get_system_table() -> Table:
    """Fetches current Linux system metrics and formats them into a Rich table."""
    sys_table = Table(title=f"WSL System Monitor ({platform.node()})", style="cyan") # platform.node() pulls network hostname of WSL instance
    
    sys_table.add_column("Resource", style="bold white", width=20)
    sys_table.add_column("Usage/Status", style="green", width=35)

    # 1. CPU Usage
    cpu_percent = psutil.cpu_percent(interval=None) # non-blocking since main loop handles 1s wait
    cpu_cores = psutil.cpu_count(logical=True) # number of CPU threads Windows is allocating to WSL2 virtual machine
    sys_table.add_row("CPU Load", f"{cpu_percent}% ({cpu_cores} logical cores (aka threads))")
    
    # 2. RAM Usage
    mem = psutil.virtual_memory()
    used_mem_gb = mem.used / (1024 ** 3)
    total_mem_gb = mem.total / (1024 ** 3)
    sys_table.add_row("Memory (RAM)", f"{mem.percent}% ({used_mem_gb:.2f}GB / {total_mem_gb:.2f}GB)")
    
    # 3. Root Disk Usage
    disk = psutil.disk_usage("/") # "/" indicates root directory of entire filesystem
    used_disk_gb = disk.used / (1024 ** 3)
    total_disk_gb = disk.total / (1024 ** 3)
    sys_table.add_row("Root Disk Space", f"{disk.percent}% ({used_disk_gb:.1f}GB / {total_disk_gb:.1f}GB)")
    
    # 4. Active Processes
    process_count = len(psutil.pids())
    sys_table.add_row("Active Processes", str(process_count))
    
    return sys_table


def main():
    """Executes the get_system_table() function and handles errors and exceptions."""
    console.print("[bold yellow]Starting WSL System Monitor... Press Ctrl+C to exit.[/bold yellow\n]")
    
    try:
        with Live(get_system_table(), refresh_per_second=1) as live:
            while True: # infinite monitoring loop that pauses for 1s between checks
                time.sleep(1)
                live.update(get_system_table())
    except KeyboardInterrupt: # program interrupted by user
        console.print("\b[bold red]Monitor stopped cleanly.[/bold red]")
        

if __name__ == "__main__":
    main()        