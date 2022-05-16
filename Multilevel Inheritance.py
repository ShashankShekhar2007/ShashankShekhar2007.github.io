class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def can_dance(self):
        return f"I can Dance {self.dance} number of times."


class Grandson(Son):
    dance = 6
    # def can_dance(self):
    #     return (f"Yooooooo!!!!!!!!! I can Dance {self.dance} number of times.")


ram = Grandson()
print(ram.can_dance())
print(ram.basketball)

print('********************************************************************************')


class Pocket_Device:
    circuit = 1
    price = 2000

    def price_printer(self):
        return f"The Price is {self.price}"


class Phone(Pocket_Device):
    circuit = 3
    display = 1080
    price = 8000


class Electronic_device(Phone):
    circuit = 2
    price = 14000


i_phone = Phone()
i_pod = Pocket_Device()
tv = Electronic_device()
print(tv.price_printer())
print(i_pod.circuit)

print(tv.display)
print(i_phone.price_printer())
