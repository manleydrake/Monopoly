import tkinter


class Main:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title('Properties')

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
        self.frame_16 = tkinter.Frame()

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
        self.frame_16.pack()

        self.med_button = tkinter.Button(self.frame_2, highlightbackground='purple', text='Mediterranean Ave', command=self.disp_med)
        self.baltic_button = tkinter.Button(self.frame_2, highlightbackground='purple', text='Baltic Ave', command=self.disp_baltic)
        self.oriental_button = tkinter.Button(self.frame_2, highlightbackground='#adffff', text='Oriental Ave', command=self.disp_oriental)
        self.vermont_button = tkinter.Button(self.frame_2, highlightbackground='#adffff', text='Vermont Ave', command=self.disp_vermont)
        self.connecticut_button = tkinter.Button(self.frame_2, highlightbackground='#adffff', text='Connecticut Ave', command=self.disp_connecticut)
        self.stcharles_button = tkinter.Button(self.frame_3, highlightbackground='magenta', text='St. Charles Place', command=self.disp_stcharles)
        self.states_button = tkinter.Button(self.frame_3, highlightbackground='magenta', text='States Ave', command=self.disp_states)
        self.virginia_button = tkinter.Button(self.frame_3, highlightbackground='magenta', text='Virginia Ave', command=self.disp_virginia)
        self.stjames_button = tkinter.Button(self.frame_3, highlightbackground='orange', text='St. James Place', command=self.disp_stjames)
        self.tennessee_button = tkinter.Button(self.frame_3, highlightbackground='orange', text='Tennessee Ave', command=self.disp_tennessee)
        self.newyork_button = tkinter.Button(self.frame_3, highlightbackground='orange', text='New York Ave', command=self.disp_newyork)
        self.kentucky_button = tkinter.Button(self.frame_4, highlightbackground='red', text='Kentucky Ave', command=self.disp_kentucky)
        self.indiana_button = tkinter.Button(self.frame_4, highlightbackground='red', text='Indiana Ave', command=self.disp_indiana)
        self.illinois_button = tkinter.Button(self.frame_4, highlightbackground='red', text='Illinois Ave', command=self.disp_illinois)
        self.atlantic_button = tkinter.Button(self.frame_4, highlightbackground='yellow', text='Atlantic Ave', command=self.disp_atlantic)
        self.ventnor_button = tkinter.Button(self.frame_4, highlightbackground='yellow', text='Ventnor Ave', command=self.disp_ventnor)
        self.marvin_button = tkinter.Button(self.frame_4, highlightbackground='yellow', text='Marvin Gardens', command=self.disp_marvin)
        self.pacific_button = tkinter.Button(self.frame_5, highlightbackground='#049d04', text='Pacific Ave', command=self.disp_pacific)
        self.ncarolina_button = tkinter.Button(self.frame_5, highlightbackground='#049d04', text='North Carolina Ave', command=self.disp_ncarolina)
        self.pennsylvania_button = tkinter.Button(self.frame_5, highlightbackground='#049d04', text='Pennsylvania Ave', command=self.disp_pennsylvania)
        self.parkplace_button = tkinter.Button(self.frame_5, highlightbackground='blue', text='Park Place', command=self.disp_parkplace)
        self.boardwalk_button = tkinter.Button(self.frame_5, highlightbackground='blue', text='Boardwalk', command=self.disp_boardwalk)
        self.readingrr_button = tkinter.Button(self.frame_6, highlightbackground='black', text='Reading Railroad', command=self.disp_readingrr)
        self.pennsylvaniarr_button = tkinter.Button(self.frame_6, highlightbackground='black', text='Pennsylvania Railroad', command=self.disp_pennsylvaniarr)
        self.borr_button = tkinter.Button(self.frame_6, highlightbackground='black', text='B. & O. Railroad', command=self.disp_borr)
        self.shortlinerr_button = tkinter.Button(self.frame_6, highlightbackground='black', text='Short Line Railroad', command=self.disp_shortlinerr)
        self.electricco_button = tkinter.Button(self.frame_6, highlightbackground='#c5c1d8', text='Electric Company', command=self.disp_electricco)
        self.waterworks_button = tkinter.Button(self.frame_6, highlightbackground='#c5c1d8', text='Water Works', command=self.disp_waterworks)

        self.spacing_1 = tkinter.Label(self.frame_1, text='\n')
        self.spacing_2 = tkinter.Label(self.frame_2, text='\n')
        self.spacing_3 = tkinter.Label(self.frame_3, text='\n')
        self.spacing_4 = tkinter.Label(self.frame_4, text='\n')
        self.spacing_5 = tkinter.Label(self.frame_5, text='\n')
        self.spacing_6 = tkinter.Label(self.frame_6, text='\n')
        self.spacing_7 = tkinter.Label(self.frame_7, text='\n\n\n')

        self.name = tkinter.Label(self.frame_8)
        self.rent = tkinter.Label(self.frame_9)
        self.one_house = tkinter.Label(self.frame_10)
        self.two_house = tkinter.Label(self.frame_11)
        self.three_house = tkinter.Label(self.frame_12)
        self.four_house = tkinter.Label(self.frame_13)
        self.hotel = tkinter.Label(self.frame_14)
        self.mortgage = tkinter.Label(self.frame_15)
        self.building_cost = tkinter.Label(self.frame_16)

        self.med_button.pack(side='left')
        self.baltic_button.pack(side='left')
        self.oriental_button.pack(side='left')
        self.vermont_button.pack(side='left')
        self.connecticut_button.pack(side='left')
        self.stcharles_button.pack(side='left')
        self.states_button.pack(side='left')
        self.virginia_button.pack(side='left')
        self.stjames_button.pack(side='left')
        self.tennessee_button.pack(side='left')
        self.newyork_button.pack(side='left')
        self.kentucky_button.pack(side='left')
        self.indiana_button.pack(side='left')
        self.illinois_button.pack(side='left')
        self.atlantic_button.pack(side='left')
        self.ventnor_button.pack(side='left')
        self.marvin_button.pack(side='left')
        self.pacific_button.pack(side='left')
        self.ncarolina_button.pack(side='left')
        self.pennsylvania_button.pack(side='left')
        self.parkplace_button.pack(side='left')
        self.boardwalk_button.pack(side='left')
        self.readingrr_button.pack(side='left')
        self.pennsylvaniarr_button.pack(side='left')
        self.borr_button.pack(side='left')
        self.shortlinerr_button.pack(side='left')
        self.electricco_button.pack(side='left')
        self.waterworks_button.pack(side='left')

        self.spacing_1.pack()
        self.spacing_2.pack()
        self.spacing_3.pack()
        self.spacing_4.pack()
        self.spacing_5.pack()
        self.spacing_6.pack()
        self.spacing_7.pack()

        self.name.pack()
        self.rent.pack()
        self.one_house.pack()
        self.two_house.pack()
        self.three_house.pack()
        self.four_house.pack()
        self.hotel.pack()
        self.mortgage.pack()
        self.building_cost.pack()

        tkinter.mainloop()

    def disp_med(self):
        self.name.configure(text='Mediterranean Ave', bg='purple', fg='white')
        self.rent.config(text='Rent: $2   ')
        self.one_house.config(text='With 1 house \t\t $10  ')
        self.two_house.config(text='With 2 houses\t\t $30  ')
        self.three_house.config(text='With 3 houses\t\t $90  ')
        self.four_house.config(text='With 4 houses\t\t $160 ')
        self.hotel.config(text='With hotel\t $250')
        self.mortgage.config(text='Mortgage: $30')
        self.building_cost.config(text='Building cost: $50')

    def disp_baltic(self):
        self.name.configure(text='Baltic Ave', bg='purple', fg='white')
        self.rent.config(text='Rent: $4')
        self.one_house.config(text='With 1 house \t\t $20  ')
        self.two_house.config(text='With 2 houses\t\t $60  ')
        self.three_house.config(text='With 3 houses\t\t $180 ')
        self.four_house.config(text='With 4 houses\t\t $320 ')
        self.hotel.config(text='With hotel\t $450')
        self.mortgage.config(text='Mortgage: $30')
        self.building_cost.config(text='Building cost: $50')

    def disp_oriental(self):
        self.name.configure(text='Oriental Ave', bg='#adffff', fg='black')
        self.rent.config(text='Rent: $6')
        self.one_house.config(text='With 1 house \t\t $30  ')
        self.two_house.config(text='With 2 houses\t\t $90  ')
        self.three_house.config(text='With 3 houses\t\t $270 ')
        self.four_house.config(text='With 4 houses\t\t $400 ')
        self.hotel.config(text='With hotel\t $550')
        self.mortgage.config(text='Mortgage: $50')
        self.building_cost.config(text='Building cost: $50')

    def disp_vermont(self):
        self.name.configure(text='Vermont Ave', bg='#adffff', fg='black')
        self.rent.config(text='Rent: $6')
        self.one_house.config(text='With 1 house \t\t $30  ')
        self.two_house.config(text='With 2 houses\t\t $90  ')
        self.three_house.config(text='With 3 houses\t\t $270 ')
        self.four_house.config(text='With 4 houses\t\t $400 ')
        self.hotel.config(text='With hotel\t $550')
        self.mortgage.config(text='Mortgage: $50')
        self.building_cost.config(text='Building cost: $50')

    def disp_connecticut(self):
        self.name.configure(text='Connecticut Ave', bg='#adffff', fg='black')
        self.rent.config(text='Rent: $8')
        self.one_house.config(text='With 1 house \t\t $40  ')
        self.two_house.config(text='With 2 houses\t\t $100 ')
        self.three_house.config(text='With 3 houses\t\t $300 ')
        self.four_house.config(text='With 4 houses\t\t $450 ')
        self.hotel.config(text='With hotel\t $600')
        self.mortgage.config(text='Mortgage: $50')
        self.building_cost.config(text='Building cost: $50')

    def disp_stcharles(self):
        self.name.configure(text='St. Charles Place', bg='magenta', fg='white')
        self.rent.config(text='$10')
        self.one_house.config(text='With 1 house \t\t $50  ')
        self.two_house.config(text='With 2 houses\t\t $150 ')
        self.three_house.config(text='With 3 houses\t\t $450 ')
        self.four_house.config(text='With 4 houses\t\t $625 ')
        self.hotel.config(text='With hotel\t $750')
        self.mortgage.config(text='Mortgage: $100')
        self.building_cost.config(text='Building cost: $100')

    def disp_states(self):
        self.name.configure(text='States Ave', bg='magenta', fg='white')
        self.rent.config(text='$10')
        self.one_house.config(text='With 1 house \t\t $50  ')
        self.two_house.config(text='With 2 houses\t\t $150 ')
        self.three_house.config(text='With 3 houses\t\t $450 ')
        self.four_house.config(text='With 4 houses\t\t $625 ')
        self.hotel.config(text='With hotel\t $750')
        self.mortgage.config(text='Mortgage: $100')
        self.building_cost.config(text='Building cost: $100')

    def disp_virginia(self):
        self.name.configure(text='Virginia Ave', bg='magenta', fg='white')
        self.rent.config(text='Rent: $12')
        self.one_house.config(text='With 1 house \t\t $60  ')
        self.two_house.config(text='With 2 houses\t\t $180 ')
        self.three_house.config(text='With 3 houses\t\t $500 ')
        self.four_house.config(text='With 4 houses\t\t $700 ')
        self.hotel.config(text='With hotel\t $900')
        self.mortgage.config(text='Mortgage: $80')
        self.building_cost.config(text='Building cost: $100')

    def disp_stjames(self):
        self.name.configure(text='St. James Place', bg='orange', fg='white')
        self.rent.config(text='Rent: $14')
        self.one_house.config(text='With 1 house \t\t $70  ')
        self.two_house.config(text='With 2 houses\t\t $200 ')
        self.three_house.config(text='With 3 houses\t\t $550 ')
        self.four_house.config(text='With 4 houses\t\t $750 ')
        self.hotel.config(text='With hotel\t $950')
        self.mortgage.config(text='Mortgage: $90')
        self.building_cost.config(text='Building cost: $100')

    def disp_tennessee(self):
        self.name.configure(text='Tennessee Ave', bg='orange', fg='white')
        self.rent.config(text='Rent: $14')
        self.one_house.config(text='With 1 house \t\t $70  ')
        self.two_house.config(text='With 2 houses\t\t $200 ')
        self.three_house.config(text='With 3 houses\t\t $550')
        self.four_house.config(text='With 4 houses\t\t $750 ')
        self.hotel.config(text='With hotel\t $950')
        self.mortgage.config(text='Mortgage: $90')
        self.building_cost.config(text='Building cost: $100')

    def disp_newyork(self):
        self.name.configure(text='New York Ave', bg='orange', fg='white')
        self.rent.config(text='Rent: $16')
        self.one_house.config(text='With 1 house \t\t $80  ')
        self.two_house.config(text='With 2 houses\t\t $220 ')
        self.three_house.config(text='With 3 houses\t\t $600 ')
        self.four_house.config(text='With 4 houses\t\t $800 ')
        self.hotel.config(text='With hotel\t $1000')
        self.mortgage.config(text='Mortgage: $100')
        self.building_cost.config(text='Building cost: $100')

    def disp_kentucky(self):
        self.name.configure(text='Kentucky Ave', bg='red', fg='white')
        self.rent.config(text='Rent: $18')
        self.one_house.config(text='With 1 house \t\t $90  ')
        self.two_house.config(text='With 2 houses\t\t $250 ')
        self.three_house.config(text='With 3 houses\t\t $700 ')
        self.four_house.config(text='With 4 houses\t\t $875 ')
        self.hotel.config(text='With hotel\t $1050')
        self.mortgage.config(text='Mortgage: $110')
        self.building_cost.config(text='Building cost: $150')

    def disp_indiana(self):
        self.name.configure(text='Indiana Ave', bg='red', fg='white')
        self.rent.config(text='Rent: $18')
        self.one_house.config(text='With 1 house \t\t $90  ')
        self.two_house.config(text='With 2 houses\t\t $250 ')
        self.three_house.config(text='With 3 houses\t\t $700 ')
        self.four_house.config(text='With 4 houses\t\t $875 ')
        self.hotel.config(text='With hotel\t $1050')
        self.mortgage.config(text='Mortgage: $110')
        self.building_cost.config(text='Building cost: $150')

    def disp_illinois(self):
        self.name.configure(text='Illinois Ave', bg='red', fg='white')
        self.rent.config(text='Rent: $20')
        self.one_house.config(text='With 1 house \t\t $100 ')
        self.two_house.config(text='With 2 houses\t\t $300 ')
        self.three_house.config(text='With 3 houses\t\t $750 ')
        self.four_house.config(text='With 4 houses\t\t $925')
        self.hotel.config(text='With hotel\t $1100')
        self.mortgage.config(text='Mortgage: $120')
        self.building_cost.config(text='Building cost: $150')

    def disp_atlantic(self):
        self.name.configure(text='Atlantic Ave', bg='yellow', fg='black')
        self.rent.config(text='Rent: $22')
        self.one_house.config(text='With 1 house \t\t $110 ')
        self.two_house.config(text='With 2 houses\t\t $330 ')
        self.three_house.config(text='With 3 houses\t\t $800 ')
        self.four_house.config(text='With 4 houses\t\t $975 ')
        self.hotel.config(text='With hotel\t $1150')
        self.mortgage.config(text='Mortgage: $130')
        self.building_cost.config(text='Building cost: $150')

    def disp_ventnor(self):
        self.name.configure(text='Ventnor Ave', bg='yellow', fg='black')
        self.rent.config(text='Rent: $22')
        self.one_house.config(text='With 1 house \t\t $110 ')
        self.two_house.config(text='With 2 houses\t\t $330 ')
        self.three_house.config(text='With 3 houses\t\t $800 ')
        self.four_house.config(text='With 4 houses\t\t $975 ')
        self.hotel.config(text='With hotel\t $1150')
        self.mortgage.config(text='Mortgage: $130')
        self.building_cost.config(text='Building cost: $150')

    def disp_marvin(self):
        self.name.configure(text='Marvin Gardens', bg='yellow', fg='black')
        self.rent.config(text='Rent: $24')
        self.one_house.config(text='With 1 house \t\t $120 ')
        self.two_house.config(text='With 2 houses\t\t $360 ')
        self.three_house.config(text='With 3 houses\t\t $850 ')
        self.four_house.config(text='With 4 houses\t\t $1025')
        self.hotel.config(text='With hotel\t $1200')
        self.mortgage.config(text='Mortgage: $140')
        self.building_cost.config(text='Building cost: $150')

    def disp_pacific(self):
        self.name.configure(text='Pacific Ave', bg='#049d04', fg='white')
        self.rent.config(text='Rent: $26')
        self.one_house.config(text='With 1 house \t\t $130 ')
        self.two_house.config(text='With 2 houses\t\t $390 ')
        self.three_house.config(text='With 3 houses\t\t $900 ')
        self.four_house.config(text='With 4 houses\t\t $1100')
        self.hotel.config(text='With hotel\t $1275')
        self.mortgage.config(text='Mortgage: $150')
        self.building_cost.config(text='Building cost: $200')

    def disp_ncarolina(self):
        self.name.configure(text='North Carolina Ave', bg='#049d04', fg='white')
        self.rent.config(text='Rent $26')
        self.one_house.config(text='With 1 house \t\t $130 ')
        self.two_house.config(text='With 2 houses\t\t $390 ')
        self.three_house.config(text='With 3 houses\t\t $900 ')
        self.four_house.config(text='With 4 houses\t\t $1100')
        self.hotel.config(text='With hotel\t $1275')
        self.mortgage.config(text='Mortgage: $150')
        self.building_cost.config(text='Building cost: $200')

    def disp_pennsylvania(self):
        self.name.configure(text='Pennsylvania Ave', bg='#049d04', fg='white')
        self.rent.config(text='Rent: $28')
        self.one_house.config(text='With 1 house \t\t $150 ')
        self.two_house.config(text='With 2 houses\t\t $450 ')
        self.three_house.config(text='With 3 houses\t\t $1000')
        self.four_house.config(text='With 4 houses\t\t $1200')
        self.hotel.config(text='With hotel\t $1400')
        self.mortgage.config(text='Mortgage: $160')
        self.building_cost.config(text='Building cost: $200')

    def disp_parkplace(self):
        self.name.configure(text='Park Place', bg='blue', fg='white')
        self.rent.config(text='Rent: $35')
        self.one_house.config(text='With 1 house \t\t $175 ')
        self.two_house.config(text='With 2 houses\t\t $500 ')
        self.three_house.config(text='With 3 houses\t\t $1100')
        self.four_house.config(text='With 4 houses\t\t $1300')
        self.hotel.config(text='With hotel\t $1500')
        self.mortgage.config(text='Mortgage: $175')
        self.building_cost.config(text='Building cost: $200')

    def disp_boardwalk(self):
        self.name.configure(text='Boardwalk', bg='blue', fg='white')
        self.rent.config(text='Rent: $50')
        self.one_house.config(text='With 1 house \t\t $200 ')
        self.two_house.config(text='With 2 houses\t\t $600 ')
        self.three_house.config(text='With 3 houses\t\t $1400')
        self.four_house.config(text='With 4 houses\t\t $1700')
        self.hotel.config(text='With hotel\t $2000')
        self.mortgage.config(text='Mortgage: $200')
        self.building_cost.config(text='Building cost: $200')

    def disp_readingrr(self):
        self.name.configure(text='Reading Railroad', bg='white', fg='black')
        self.rent.config(text='Rent:')
        self.one_house.config(text='1 railroad: \t$25 ')
        self.two_house.config(text='2 railroads:\t$50 ')
        self.three_house.config(text='3 railroads:\t$100')
        self.four_house.config(text='4 railroads:\t$200')
        self.hotel.config(text='')
        self.mortgage.config(text='Mortgage: 100')
        self.building_cost.config(text='')

    def disp_pennsylvaniarr(self):
        self.name.configure(text='Pennsylvania Railroad', bg='white', fg='black')
        self.rent.config(text='Rent:')
        self.one_house.config(text='1 railroad: \t$25 ')
        self.two_house.config(text='2 railroads:\t$50 ')
        self.three_house.config(text='3 railroads:\t$100')
        self.four_house.config(text='4 railroads:\t$200')
        self.hotel.config(text='')
        self.mortgage.config(text='Mortgage: 100')
        self.building_cost.config(text='')

    def disp_borr(self):
        self.name.configure(text='B. & O. Railroad', bg='white', fg='black')
        self.rent.config(text='Rent:')
        self.one_house.config(text='1 railroad: \t$25 ')
        self.two_house.config(text='2 railroads:\t$50 ')
        self.three_house.config(text='3 railroads:\t$100')
        self.four_house.config(text='4 railroads:\t$200')
        self.hotel.config(text='')
        self.mortgage.config(text='Mortgage: 100')
        self.building_cost.config(text='')

    def disp_shortlinerr(self):
        self.name.configure(text='Short Line Railroad', bg='white', fg='black')
        self.rent.config(text='Rent:')
        self.one_house.config(text='1 railroad: \t$25 ')
        self.two_house.config(text='2 railroads:\t$50 ')
        self.three_house.config(text='3 railroads:\t$100')
        self.four_house.config(text='4 railroads:\t$200')
        self.hotel.config(text='')
        self.mortgage.config(text='Mortgage: 100')
        self.building_cost.config(text='')

    def disp_electricco(self):
        self.name.configure(text='Electric Company', bg='white', fg='black')
        self.rent.config(text='\nIf one Utility is owned,')
        self.one_house.config(text='rent is 4 times the amount shown')
        self.two_house.config(text='on the dice.')
        self.three_house.config(text='If both Utilities are owned,')
        self.four_house.config(text='rent is 10 times the amount shown')
        self.hotel.config(text='on the dice.')
        self.mortgage.config(text='\nMortgage: 100')
        self.building_cost.config(text='')

    def disp_waterworks(self):
        self.name.configure(text='Water Works', bg='white', fg='black')
        self.rent.config(text='\nIf one Utility is owned,')
        self.one_house.config(text='rent is 4 times the amount shown')
        self.two_house.config(text='on the dice.')
        self.three_house.config(text='If both Utilities are owned,')
        self.four_house.config(text='rent is 10 times the amount shown')
        self.hotel.config(text='on the dice.')
        self.mortgage.config(text='\nMortgage: 100')
        self.building_cost.config(text='')


Main = Main()
