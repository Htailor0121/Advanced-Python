class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def handle(self):
        print("accident occure.take detour")


try:
    raise Accident('"crash between two cars"')
except Accident as e:
    e.handle()

#     # Finally Keyword
# for the understanding
# try:
#     1 > 3
# except:
#     print("Something Went Wrong")
# else:
#     print("NOthing Going Wrong")
# finally:
#     print("The try...except block is finished")