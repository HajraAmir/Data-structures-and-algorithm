# process.py
class Process:
    def __init__(self, pid, name, burst_time):
        """Initialize a process with ID, name, and burst time."""
        self.pid = pid
        self.name = name
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def __repr__(self):
        return f"Process(pid={self.pid}, name='{self.name}', burst_time={self.burst_time}, remaining_time={self.remaining_time})"

# scheduler.py
class Scheduler:
    def __init__(self, processes, time_slice):
        """Initialize the scheduler with a list of processes and a time slice."""
        self.processes = processes
        self.time_slice = time_slice

    def assignProcessor(self):
        """Assign processes to the processor using Round-Robin scheduling."""
        print("Starting process scheduling...")

        while any(p.remaining_time > 0 for p in self.processes):
            for process in self.processes:
                if process.remaining_time > 0:
                    time_used = min(process.remaining_time, self.time_slice)
                    process.remaining_time -= time_used
                    print(f"Process {process.name} (PID: {process.pid}) executed for {time_used} time units. Remaining time: {process.remaining_time}")

        print("All processes have been completed.")

# main.py
from process import Process
from scheduler import Scheduler

if __name__ == "__main__":
    # List of processes with their PID, name, and burst time
    arr = [
        Process(1, "notepad", 20), 
        Process(13, "mp3player", 5), 
        Process(4, "bcc", 30), 
        Process(11, "explorer", 2)
    ]

    # Initialize the scheduler with the process list and a time slice of 5
    s = Scheduler(arr, 5)

    # Assign processes to the processor
    s.assignProcessor()
