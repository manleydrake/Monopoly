import random
import tkinter


class Main:
    def __init__(self):

        self.players = int(input("How many players? \n"))

        def supplement():
            self.player_1_name = str(input("Player 1: "))
            self.player_1_piece = str(input("Player 1's piece: "))
            self.player_2_name = str(input("Player 2: "))
            self.player_2_piece = str(input("Player 2's piece: "))

            if self.players >= 3:
                self.player_3_name = str(input("Player 3: "))
                self.player_3_piece = str(input("Player 3's piece: "))
            if self.players >= 4:
                self.player_4_name = str(input("Player 4: "))
                self.player_4_piece = str(input("Player 4's piece: "))
            if self.players >= 5:
                self.player_5_name = str(input("Player 5: "))
                self.player_5_piece = str(input("Player 5's piece: "))
            if self.players >= 6:
                self.player_6_name = str(input("Player 6: "))
                self.player_6_piece = str(input("Player 6's piece: "))
            if self.players >= 7:
                self.player_7_name = str(input("Player 7: "))
                self.player_7_piece = str(input("Player 7's piece: "))
            if self.players >= 8:
                self.player_8_name = str(input("Player 8: "))
                self.player_8_piece = str(input("Player 8's piece: "))

            print("------------------------------------\n")

            print("Player 1: ", self.player_1_name, "\n   Piece: ", self.player_1_piece)
            print("\nPlayer 2: ", self.player_2_name, "\n   Piece: ", self.player_2_piece)

            if self.players >= 3:
                print("\nPlayer 3: ", self.player_3_name, "\n   Piece: ", self.player_3_piece)
            if self.players >= 4:
                print("\nPlayer 4: ", self.player_4_name, "\n   Piece: ", self.player_4_piece)
            if self.players >= 5:
                print("\nPlayer 5: ", self.player_5_name, "\n   Piece: ", self.player_5_piece)
            if self.players >= 6:
                print("\nPlayer 6: ", self.player_6_name, "\n   Piece: ", self.player_6_piece)
            if self.players >= 7:
                print("\nPlayer 7: ", self.player_7_name, "\n   Piece: ", self.player_7_piece)
            if self.players >= 8:
                print("\nPlayer 8: ", self.player_8_name, "\n   Piece: ", self.player_8_piece)

            print("\n------------------------------------")

        # supplement()

        self.x = 0

        self.main_window = tkinter.Tk()
        self.main_window.title('Monopoly')

        self.frame_1 = tkinter.Frame()
        self.frame_2 = tkinter.Frame()
        self.frame_3 = tkinter.Frame()
        self.frame_4 = tkinter.Frame()
        self.frame_5 = tkinter.Frame()
        self.frame_6 = tkinter.Frame()
        self.frame_7 = tkinter.Frame()
        self.frame_8 = tkinter.Frame()
        self.frame_9 = tkinter.Frame()
        self.frame_10 = tkinter.Frame()
        self.frame_11 = tkinter.Frame()
        self.frame_12 = tkinter.Frame()
        self.frame_13 = tkinter.Frame()
        self.frame_14 = tkinter.Frame()
        self.frame_15 = tkinter.Frame()

        self.dice_button = tkinter.Button(self.frame_2, text='Roll Dice', command=self.roll_dice)

        self.die1 = tkinter.Label(self.frame_1, text='\n\n\n\n')
        self.die2 = tkinter.Label(self.frame_1, text='\n\n\n\n')

        self.chance_button = tkinter.Button(self.frame_4, text='Chance',command=self.chance)
        self.chance_display = tkinter.Label(self.frame_3, text='\n\n\n\n\n\n')
        self.community_chest_button = tkinter.Button(self.frame_6, text='Community Chest', command=self.community_chest)
        self.community_chest_display = tkinter.Label(self.frame_5, text='\n\n\n\n\n\n')

        self.spacing_1 = tkinter.Label(self.frame_7, text='\n\n')

        self.amount_label = tkinter.Label(self.frame_8, text='$')
        self.amount_entry = tkinter.Entry(self.frame_8, width=10)
        self.payer_label = tkinter.Label(self.frame_8, text=' from ')
        self.payer_entry = tkinter.Entry(self.frame_8, width=10)
        self.receiver_label = tkinter.Label(self.frame_8, text=' to ')
        self.receiver_entry = tkinter.Entry(self.frame_8, width=10)
        self.pay_button = tkinter.Button(self.frame_9, text='Pay', command=self.pay)

        self.spacing_2 = tkinter.Label(self.frame_10, text='\n')

        self.player_1_label = tkinter.Label(self.frame_11, text='Player 1: $')
        self.player_1_money = tkinter.Label(self.frame_11, text='1500')
        self.player_2_label = tkinter.Label(self.frame_12, text='Player 2: $')
        self.player_2_money = tkinter.Label(self.frame_12, text='1500')
        self.player_3_label = tkinter.Label(self.frame_13, text='Player 3: $')
        self.player_3_money = tkinter.Label(self.frame_13, text='1500')
        self.player_4_label = tkinter.Label(self.frame_14, text='Player 4: $')
        self.player_4_money = tkinter.Label(self.frame_14, text='1500')
        self.player_5_label = tkinter.Label(self.frame_11, text='Player 5: $')
        self.player_5_money = tkinter.Label(self.frame_11, text='1500')
        self.player_6_label = tkinter.Label(self.frame_12, text='Player 6: $')
        self.player_6_money = tkinter.Label(self.frame_12, text='1500')
        self.player_7_label = tkinter.Label(self.frame_13, text='Player 7: $')
        self.player_7_money = tkinter.Label(self.frame_13, text='1500')
        self.player_8_label = tkinter.Label(self.frame_14, text='Player 8: $')
        self.player_8_money = tkinter.Label(self.frame_14, text='1500')
        self.free_parking_label = tkinter.Label(self.frame_15, text='Free Parking: $')
        self.free_parking_display = tkinter.Label(self.frame_15, text='500')

        self.dice_button.pack()
        self.die1.pack(side='left')
        self.die2.pack(side='right')

        self.chance_button.pack()
        self.chance_display.pack()

        self.community_chest_button.pack()
        self.community_chest_display.pack()

        self.spacing_1.pack()

        self.amount_label.pack(side='left')
        self.amount_entry.pack(side='left')
        self.payer_label.pack(side='left')
        self.payer_entry.pack(side='left')
        self.receiver_label.pack(side='left')
        self.receiver_entry.pack(side='left')
        self.pay_button.pack()

        self.spacing_2.pack()

        self.player_1_label.pack(side='left')
        self.player_1_money.pack(side='left')
        self.player_2_label.pack(side='left')
        self.player_2_money.pack(side='left')
        if self.players >= 3:
            self.player_3_label.pack(side='left')
            self.player_3_money.pack(side='left')
        if self.players >= 4:
            self.player_4_label.pack(side='left')
            self.player_4_money.pack(side='left')
        if self.players >= 5:
            self.player_5_label.pack(side='left')
            self.player_5_money.pack(side='left')
        if self.players >= 6:
            self.player_6_label.pack(side='left')
            self.player_6_money.pack(side='left')
        if self.players >= 7:
            self.player_7_label.pack(side='left')
            self.player_7_money.pack(side='left')
        if self.players >= 8:
            self.player_8_label.pack(side='left')
            self.player_8_money.pack(side='left')

        self.free_parking_label.pack(side='left')
        self.free_parking_display.pack(side='left')

        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        self.frame_7.pack()
        self.frame_8.pack()
        self.frame_9.pack()
        self.frame_10.pack()
        self.frame_11.pack()
        self.frame_12.pack()
        self.frame_13.pack()
        self.frame_14.pack()
        self.frame_15.pack()

        tkinter.mainloop()

    def roll_dice(self):

        response = random.randint(1, 6)
        answer = response
        if response == 1:
            answer = '________\n|             |\n|      .      |\n|             |\n|_______|'
        if response == 2:
            answer = '________\n|    .        |\n|             |\n|        .    |\n|_______|'
        if response == 3:
            answer = '________\n|    .        |\n|      .      |\n|        .    |\n|_______|'
        if response == 4:
            answer = '________\n|   .     .   |\n|             |\n|   .     .   |\n|_______|'
        if response == 5:
            answer = '________\n|   .     .   |\n|      .      |\n|   .     .   |\n|_______|'
        if response == 6:
            answer = '________\n|   .     .   |\n|   .     .   |\n|   .     .   |\n|_______|'

        self.die1.config(text=answer)

        response = random.randint(1, 6)
        if response == 1:
            answer = '________\n|             |\n|      .      |\n|             |\n|_______|'
        if response == 2:
            answer = '________\n|    .        |\n|             |\n|        .    |\n|_______|'
        if response == 3:
            answer = '________\n|    .        |\n|      .      |\n|        .    |\n|_______|'
        if response == 4:
            answer = '________\n|   .     .   |\n|             |\n|   .     .   |\n|_______|'
        if response == 5:
            answer = '________\n|   .     .   |\n|      .      |\n|   .     .   |\n|_______|'
        if response == 6:
            answer = '________\n|   .     .   |\n|   .     .   |\n|   .     .   |\n|_______|'

        self.die2.config(text=answer)

    def chance(self):
        chance_list = ['________________________________________________________\n\n\nAdvance to Go (Collect $200).\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nAdvance to Illinois Ave.\n\n\n________________________________________________________',
                       '________________________________________________________\n\nAdvance token to nearest Utility. If unowned, you\nmay buy it from the Bank.If owned, throw dice and\npay owner a total ten times the amount thrown.\n\n________________________________________________________',
                       '________________________________________________________\n\nAdvance token to the nearest Railroad and pay owner \ntwice the rental to which he/she is otherwise entitled.\nIf Railroad is unowned, you may buy it from the Bank.\n\n________________________________________________________',
                       '________________________________________________________\n\nAdvance token to the nearest Railroad and pay owner \ntwice the rental to which he/she is otherwise entitled.\nIf Railroad is unowned, you may buy it from the Bank.\n\n________________________________________________________',
                       '________________________________________________________\n\n\nAdvance to St. Charles Place –\nif you pass Go, collect $200.\n\n________________________________________________________',
                       '________________________________________________________\n\n\nBank pays you dividend of $50.\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nGet out of Jail free – this card may \nbe kept until needed, or traded/sold.\n\n________________________________________________________',
                       '________________________________________________________\n\n\nGo back 3 spaces.\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nGo directly to Jail – do not pass Go, do not collect $200.\n\n\n_________________________________________________________',
                       '________________________________________________________\n\n\nMake general repairs on all your property –\nfor each house pay $25 – for each hotel $100.\n\n________________________________________________________',
                       '________________________________________________________\n\n\nPay poor tax of $15.\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nTake a trip to Reading Railroad – if you pass Go collect $200.\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nTake a walk on the Boardwalk – advance token to Boardwalk.\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nYou have been elected chairman of\nthe board – pay each player $50. \n\n________________________________________________________',
                       '________________________________________________________\n\n\nYour building loan matures – collect $150.\n\n\n________________________________________________________',
                       '________________________________________________________\n\n\nYou have won a crossword competition - collect $100.\n\n\n________________________________________________________']
        import random
        chance_card = random.randint(0, 16)
        self.chance_display.config(text=chance_list[chance_card])

    def community_chest(self):
        community_chest_list = ['________________________________________________________\n\n\nAdvance to Go (Collect $200).\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nBank error in your favor – collect $75.\n\n\n________________________________________________________',
                                "________________________________________________________\n\n\nDoctor's fees – Pay $50.\n\n\n________________________________________________________",
                                '________________________________________________________\n\n\nGet out of jail free – this card may\nbe kept until needed, or sold.\n\n________________________________________________________',
                                '________________________________________________________\n\n\nGo to jail – go directly to jail – Do\nnot pass Go, do not collect $200.\n\n________________________________________________________',
                                '________________________________________________________\n\n\nIt is your birthday. Collect $10 from each player.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nGrand Opera Night – collect $50 from every\n player for opening night seats.\n\n________________________________________________________',
                                '________________________________________________________\n\n\nIncome Tax refund – collect $20.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nLife Insurance Matures – collect $100.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nPay Hospital Fees of $100.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nPay School Fees of $50.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nReceive $25 Consultancy Fee.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nYou are assessed for street repairs –\n$40 per house, $115 per hotel.\n\n________________________________________________________',
                                '________________________________________________________\n\n\nYou have won second prize in a beauty contest– collect $10.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nYou inherit $100.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nFrom sale of stock you get $50.\n\n\n________________________________________________________',
                                '________________________________________________________\n\n\nHoliday Fund matures - Receive $100.\n\n\n________________________________________________________']
        import random
        community_chest_card = random.randint(0, 16)
        self.community_chest_display.config(text=community_chest_list[community_chest_card])

    def pay(self):
        if self.x == 0:
            self.player_1 = 1500
            self.player_2 = 1500
            self.player_3 = 1500
            self.player_4 = 1500
            self.player_5 = 1500
            self.player_6 = 1500
            self.player_7 = 1500
            self.player_8 = 1500
            self.free_parking = 500

        self.x = 1

        amount = int(self.amount_entry.get())
        receiver = str(self.receiver_entry.get())
        payer = str(self.payer_entry.get())

        if receiver == "1":
            self.player_1 += amount
        if payer == "1":
            self.player_1 -= amount
        if receiver == "2":
            self.player_2 += amount
        if payer == "2":
            self.player_2 -= amount
        if receiver == "3":
            self.player_3 += amount
        if payer == "3":
            self.player_3 -= amount
        if receiver == "4":
            self.player_4 += amount
        if payer == "4":
            self.player_4 -= amount
        if receiver == "5":
            self.player_5 += amount
        if payer == "5":
            self.player_5 -= amount
        if receiver == "6":
            self.player_6 += amount
        if payer == "6":
            self.player_6 -= amount
        if receiver == "7":
            self.player_7 += amount
        if payer == "7":
            self.player_7 -= amount
        if receiver == "8":
            self.player_8 += amount
        if payer == "8":
            self.player_8 -= amount
        if receiver == "0" or receiver == "fp":
            self.free_parking += amount
        if payer == "0" or receiver == "fp":
            self.free_parking -= amount

        self.player_1_money.config(text=self.player_1)
        self.player_2_money.config(text=self.player_2)
        self.player_3_money.config(text=self.player_3)
        self.player_4_money.config(text=self.player_4)
        self.player_5_money.config(text=self.player_5)
        self.player_6_money.config(text=self.player_6)
        self.player_7_money.config(text=self.player_7)
        self.player_8_money.config(text=self.player_8)

        self.free_parking_display.config(text=self.free_parking)


Main = Main()
