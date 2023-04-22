import Domain.Interfaces.guiconst as const


def navigation_button(self, customtkinter, text, image, command, row):
    self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                               text=text,
                                               fg_color=const.color_transparent, text_color=("gray10", "gray90"),
                                               hover_color=("gray70", "gray30"),
                                               image=image, anchor="w", command=command)
    self.home_button.grid(row=row, column=0, sticky="ew")
