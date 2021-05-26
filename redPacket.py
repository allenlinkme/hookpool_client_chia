    def redPacket(self,people, money):
        if people > money or people == 0 or money == 0:
            return None
        result = []
        remain = people
        max_money = money / people * 2 #限制最大红包大小，不超过平均值得两倍
        for i in range(people):
            remain -= 1
            if remain > 0:
                m = random.randint(1, min(money - remain, max_money))
            else:
                m = money
            result.append(m)
            money -= m
        return result