def select_frame_by_name(self, name, const):
    # set button color for selected button
    self.home_button.configure(
        fg_color=("gray75", "gray25") if name == const.navigationButtonText1 else const.color_transparent)
    self.frame_2_button.configure(
        fg_color=("gray75", "gray25") if name == const.navigationButtonText2 else const.color_transparent)
    self.frame_3_button.configure(
        fg_color=("gray75", "gray25") if name == const.navigationButtonText3 else const.color_transparent)

    # show selected frame
    if name == const.navigationButtonText1:
        self.home_frame.grid(row=0, column=1, sticky="nsew")
    else:
        self.home_frame.grid_forget()
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
