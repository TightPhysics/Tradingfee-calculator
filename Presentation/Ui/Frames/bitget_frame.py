from Domain.Logic.bitget.bitget_market_selection import select_option_by_name


def bitget_frame(self, customtkinter, const):
    self.bitget_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=const.color_transparent)
    self.bitget_frame.grid_columnconfigure(0, weight=1)
    self.bitget_frame_large_image_label = customtkinter.CTkLabel(self.bitget_frame, text="",
                                                                 image=self.large_test_image)
    self.bitget_frame_large_image_label.grid(row=0, column=0, padx=1, pady=1)

    # left side
    self.bitget_frame.label1 = customtkinter.CTkLabel(self.bitget_frame, text=const.bitget_label1Text)
    self.bitget_frame.label1.grid(row=1, column=0, padx=55, pady=0, sticky="w")

    self.bitget_frame.entry1 = customtkinter.CTkEntry(self.bitget_frame,
                                                      placeholder_text=const.bitget_entryPlaceholder1)
    self.bitget_frame.entry1.grid(row=2, column=0, padx=50, pady=0, sticky="w")

    self.bitget_frame.label2 = customtkinter.CTkLabel(self.bitget_frame, text=const.bitget_label2Text)
    self.bitget_frame.label2.grid(row=3, column=0, padx=50, pady=(10, 0), sticky="w")

    self.bitget_frame.entry2 = customtkinter.CTkEntry(self.bitget_frame,
                                                      placeholder_text=const.bitget_entryPlaceholder1)
    self.bitget_frame.entry2.grid(row=4, column=0, padx=50, pady=0, sticky="w")

    self.bitget_frame_button_3 = customtkinter.CTkButton(self.bitget_frame, text="OK", compound="top")
    self.bitget_frame_button_3.grid(row=5, column=0, padx=50, pady=20, sticky="w")

    # right side
    self.bitget_frame.label3 = customtkinter.CTkLabel(self.bitget_frame, text=const.bitget_label3Text)
    self.bitget_frame.label3.grid(row=1, column=0, padx=145, pady=0, sticky="e")

    market = ["Futures", "Spot"]
    self.bitget_frame.optionMenu = customtkinter.CTkOptionMenu(self.bitget_frame,
                                                               command=select_option_by_name, values=market)
    self.bitget_frame.optionMenu.grid(row=2, column=0, padx=50, pady=0, sticky="e")
