#定义商品类


class Program:
    def __init__(self,name,price,number):
        self.name = name
        self.price = price
        self.number = number

#输出标准化

    def __str__(self) -> str:
        return f"商品名:{self.name}|价格:{self.price}|数量:{self.number}"

#修改类

    def update_program(self, price = None, number = None):
        if price is not None:
            self.price = price
        if number is not None:
            self.number = number

#购物车系统

class Bag:
    Bag_ver = 1.0
    def __init__(self):
        self.shop_bag = []

#添加系统

    def add_shop(self):
        name = input("请输入要加入的商品")
        for s in self.shop_bag:
            if s.name == name:
                print("该商品已存在，请勿重复添加")
                return
        price = input("请设置商品价格")
        number = input("请设置商品数量")
        pro = Program(name,price,number)
        self.shop_bag.append(pro)
        print("添加成功!")
        return

#修改系统
    def update_shop(self):
        name = input("请输入要修改信息的商品")
        for s in self.shop_bag:
            if s.name == name:
                price = input("请输入要修改的价格:")
                number = input("请输入要修改的数量:")
                s.update_program(price,number)
                return
        print("该商品不存在")
        return
#对于删除商品
    def remove_shop(self):
        name =input("请输入要删除的商品")
        for s in self.shop_bag:
            if s.name == name:
                self.shop_bag.remove(s)
                print("删除成功！")
                return
        print("商品不存在")
        return



#对于查询商品
    def seek_shop(self):
        name = input("请输入要查询的商品:")
        for s in self.shop_bag:
            if s.name == name:
                print(s)
                return
        print("未查询到该商品")
        return

#对于查询全部商品
    def seek_all_shop(self):
        for s in self.shop_bag:
            print(s)


    def run (self):
        while True:
            print("欢迎使用购物车系统")
            print(f"欢迎使用购物车系统 v{Bag.Bag_ver}")
            print("#############################################")
            print("#1.添加 2.修改 3.删除 4.查询指定 5.查询所有 6.退出#")
            print("#############################################")
            act = input("请输入行动代码")
            try:
                match act:
                    case "1":
                        Bag.add_shop(self)
                    case "2":
                        Bag.update_shop(self)
                    case "3":
                        Bag.remove_shop(self)
                    case "4":
                        Bag.seek_shop(self)
                    case "5":
                        Bag.seek_all_shop(self)
                    case "6":
                        break
                    case _:
                        print("输入错误")

            except Exception:
                print("运行错误,请联系管理员")



if __name__ == "__main__":
    x = Bag()
    x.run()


