
def select_frame_by_name(self, name, const):
    # set button color for selected button
    self.binance_button.configure(
        fg_color=("gray75", "gray25") if name == const.navigationButtons[2] else const.color_transparent)
    self.bitget_button.configure(
        fg_color=("gray75", "gray25") if name == const.navigationButtons[1] else const.color_transparent)
    self.okx_button.configure(
        fg_color=("gray75", "gray25") if name == const.navigationButtons[0] else const.color_transparent)

    # show selected frame
    if name == const.navigationButtonText1:
        self.binance_frame.grid(row=0, column=1, sticky="nsew")
    else:
        self.binance_frame.grid_forget()
    if name == const.navigationButtonText2:
        self.bitget_frame.grid(row=0, column=1, sticky="nsew")
    else:
        self.bitget_frame.grid_forget()
    if name == const.navigationButtonText3:
        self.third_frame.grid(row=0, column=1, sticky="nsew")
    else:
        self.third_frame.grid_forget()



def select_option_by_name(name):
    print(name)
