import heapq
from routing.router import Router

class DijkstraRouter(Router):
    def neighbors(self, chip, node):
        r, c = node
        moves = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        valid = []
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if chip.is_valid_cell(nr, nc):
                cell = chip.grid[nr][nc]
                if not cell.blocked:
                    valid.append((nr,nc))
        return valid

    def reconstruct(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()

        return path

    def find_path(self, chip, start, goal):
        open_set = []
        heapq.heappush(open_set,(0,start))
        came_from = {}
        g_score = {start:0}
        f_score = {
        }

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                return self.reconstruct(came_from,current)
            for neighbor in self.neighbors(chip,current):
                tentative = g_score[current] + 1
                if neighbor not in g_score or tentative < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative
                    f = tentative
                    f_score[neighbor] = f
                    heapq.heappush(open_set,(f,neighbor))

        return None