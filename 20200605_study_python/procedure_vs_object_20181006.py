def print_business_card(name, email, addr):
    print("name: %s " % name)
    print("E-mail: %s " % email)
    print("Office Address: %s " % addr)

name = ["kim yura", "jiwoonkg", "minsung"]
email1 = ["kim yura@naver.com", "jiwoonkg@naver.com", 'minsung@gmail.com']
addr = ["seoul", 'ggunggi', 'jeju']

print_business_card(name[1], email1[1], addr[1])


class business_card:
    def print_b_card(self, name, email, addr):
        print("name: %s " % name)
        print("E-mail: %s " % email)
        print("Office Address: %s " % addr)

a = business_card()
a.print_b_card('kim', 'kim@naver.com', 'seoul')



