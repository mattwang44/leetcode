class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []
        for asteroid in asteroids:
            if not q:
                q.append(asteroid)
                continue

            while q and q[-1] > 0 and asteroid < 0:  # collide
                if abs(q[-1]) == abs(asteroid):
                    q.pop()
                    break

                asteroid = max(q.pop(), asteroid, key=lambda x: abs(x))

            else:
                q.append(asteroid)

        return list(q)
