import time
import os
from visualization.renderer import Renderer

class ConsoleRenderer(Renderer):
    """
    Console-based visualization for OpenDMF.
    Renders simulation snapshots one after another.
    """

    def __init__(self, delay=0.3, replay=False):
        
        self.delay = delay
        self.replay = replay
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    # -----------------------------------------
    # Render all snapshots
    # -----------------------------------------
    def render(self, history):
        
        total = len(history) - 1
        
        while True:
            for snapshot in history:

                self.clear_screen()

                self.render_snapshot(snapshot, total)

                time.sleep(self.delay)

            if not self.replay:
                break

    # -----------------------------------------
    # Render one snapshot
    # -----------------------------------------
    def render_snapshot(self, snapshot, total):
        #self.print_header(snapshot, total)
        #self.print_grid(snapshot)

        print("=" * 70)
        print("                  OpenDMF v0.3.1")
        print("             Console Visualization Engine")
        print("=" * 70)

        print()

        progress = self.progress_bar(snapshot.time, total)

        print(f"Simulation Time : {snapshot.time}")
        print(f"Progress        : [{progress}]")
        print(f"Renderer        : Console")
        print()

        print("-" * 60)

        for row in snapshot.grid:

            line = ""

            for cell in row:

                if cell.blocked:
                    line += " X "

                elif cell.droplet is not None:
                    line += " ● "

                else:
                    line += " . "

            print(line)

        print("-" * 70)
            
    # -----------------------------------------
    # Progress_Bar
    # -----------------------------------------
    
    def progress_bar(self, current, total, length=25):
        """
        Create a text progress bar.
        """
        if total == 0:
            return ""

        progress = current / total

        filled = int(length * progress)

        return "█" * filled + "-" * (length - filled)

    # -----------------------------------------
    # Summary
    # -----------------------------------------
    
    def show_summary(self, result):

        print("\n")
        print("=" * 60)
        print("Simulation Complete")
        print("=" * 60)
        print(f"Success           : {result.success}")
        print(f"Simulation Time   : {result.simulation_time}")
        print(f"Path Length       : {result.path_length}")
        print(f"Distance          : {result.distance}")
        print(f"Energy            : {result.energy}")
        print(f"Blocked Moves     : {result.blocked_moves}")
        print(f"Collisions        : {result.collisions}")
        print(f"Execution Time    : {result.execution_time:.6f} sec")