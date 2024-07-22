# class

def dance():
    print("--------Lets dance---------")

class OneBody:
    def __init__(self):
        self.finger_1 = "thumb"
        self.finger_2 = "middle_finger"
        self.finger_3 = "tiny_finger"

    def hand(self):
        print(self.finger_1)
        print(self.finger_2)
        self.lines = "live life king size"
    
    def face(self):
        eyes = "this is eyes"
        nose = "this is nose"
        self.hair = "these are hairs"

    def queen_hand(self):
        print("queen_hand")
        self.queen_lines = "live life queen size"

    def leg(self):
        print(self.finger_3)

    def head(self, to_do):
        print(to_do)  
        self.hand()
        self.leg()
        self.queen_hand()
        self.face()
        print(self.lines)
        print(self.queen_lines)
        print(self.hair)
        dance()

king_body_obj = OneBody()
king_body_obj1 = OneBody()
king_body_obj.hand()

queen_body_obj = OneBody()
queen_body_obj1 = OneBody()
queen_body_obj.queen_hand()

king_body_obj.queen_hand()
queen_body_obj.hand() 
to_do = "jump"
king_body_obj1.hand()
queen_body_obj1.queen_hand()
print(king_body_obj1.lines)
print(queen_body_obj1.queen_lines)
king_body_obj1.head(to_do)
queen_body_obj1.head(to_do)

print(king_body_obj1.lines)
print(queen_body_obj1.queen_lines)
