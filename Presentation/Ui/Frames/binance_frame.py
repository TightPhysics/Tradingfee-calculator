def binance_frame(self, customtkinter, const):
    self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=const.color_transparent)
    self.home_frame.grid_columnconfigure(0, weight=1)
    self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                               image=self.large_test_image)
    self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

    self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
    self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
    self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
                                                       image=self.image_icon_image, compound="right")
    self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
    self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
                                                       image=self.image_icon_image, compound="top")
    self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
    self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
                                                       image=self.image_icon_image, compound="bottom", anchor="w")
    self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

