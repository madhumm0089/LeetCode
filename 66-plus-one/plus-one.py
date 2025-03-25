class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string += str(i)
        res = str(int(string) + 1)
        res_list = []
        for i in res:
            res_list.append(int(i))

        return res_list