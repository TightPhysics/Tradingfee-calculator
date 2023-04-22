import Presentation.Ui.Frames.NavigationFrame.NavigationListItem.navigation_list_items as navigation_list_items


def navigation_frame(self, customtkinter, const, change_appearance_mode_event):
    self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
    self.navigation_frame.grid(row=0, column=0, sticky="nsew")
    self.navigation_frame.grid_rowconfigure(4, weight=1)

    self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=const.logoText,
                                                         image=self.logo_image,
                                                         compound="left",
                                                         font=customtkinter.CTkFont(size=15, weight="bold"))
    self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

    navigation_list_items.navigation_button(self, customtkinter, text=const.navigationButtonText1, image=self.home_image, command=self.home)

    self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                               text=const.navigationButtonText1,
                                               fg_color=const.color_transparent, text_color=("gray10", "gray90"),
                                               hover_color=("gray70", "gray30"),
                                               image=self.home_image, anchor="w", command=self.home_button_event)
    self.home_button.grid(row=1, column=0, sticky="ew")

    self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                  border_spacing=10, text=const.navigationButtonText2,
                                                  fg_color=const.color_transparent, text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  image=self.chat_image, anchor="w",
                                                  command=self.frame_2_button_event)
    self.frame_2_button.grid(row=2, column=0, sticky="ew")

    self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                  border_spacing=10, text=const.navigationButtonText3,
                                                  fg_color=const.color_transparent, text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  image=self.add_user_image, anchor="w",
                                                  command=self.frame_3_button_event)
    self.frame_3_button.grid(row=3, column=0, sticky="ew")

    self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                            values=["System", "Light", "Dark"],
                                                            command=change_appearance_mode_event)
    self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")