from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = [int(item) for item in deadends]
        target = int(target)
        init = 0
        queue = [init]
        n_turn = 0
        visited = [0] * 10000
        visited[0] = 1
        if init in deadends:
            return -1
        if target == init:
            return 0
        while len(queue) != 0:
            n_turn += 1
            queue_size = len(queue)
            for k in range(queue_size):
                current = queue.pop(0)
                if current in deadends:
                    continue
                for i in range(4):
                    position_value = int((current / pow(10, i)) % 10)
                    tmp = int(current - position_value * pow(10, i))
                    for j in [-1, 1]:
                        child = int(((position_value + j) % 10) * pow(10, i) + tmp)
                        if child == target:
                            return n_turn
                        if (not child in deadends) and visited[child] == 0:
                            queue.append(child)
                            visited[child] = 1

        return -1


if __name__ == "__main__":
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    solution = Solution()
    n_turn = solution.openLock(deadends, target)
    print(n_turn),
