## Simulation
## double pointer


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def _reverse_substr(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)

        for cur_idx in range(0, len(res), 2 * k):
            res[cur_idx : cur_idx + k] = _reverse_substr(res[cur_idx : cur_idx + k])

        return "".join(res)
