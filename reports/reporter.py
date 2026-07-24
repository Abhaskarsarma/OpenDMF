class Reporter:
    """
    Generates formatted reports for OpenDMF experiments.
    """

    def print_summary(self, result):

        print()
        print("=" * 60)
        print("Experiment Summary")
        print("=" * 60)

        print(f"Success           : {result.success}")
        print(f"Simulation Time   : {result.simulation_time}")
        print(f"Path Length       : {result.path_length}")
        print(f"Distance          : {result.distance}")
        print(f"Energy            : {result.energy}")
        print(f"Total Moves       : {result.total_moves}")
        print(f"Successful Moves  : {result.successful_moves}")
        print(f"Blocked Moves     : {result.blocked_moves}")
        print(f"Collisions        : {result.collisions}")
        print(f"Execution Time    : {result.execution_time:.6f} sec")

        print("=" * 60)