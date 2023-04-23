import os

import customtkinter
from PIL import Image

import Domain.Interfaces.guiconst as const
from Application.Common.Events.appearance_mode_event import change_appearance_mode_event


class NavigationFrame:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

        self.navigation_frame = customtkinter.CTkFrame(self.app_instance, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        image_path = os.path.join("test_images")

        self.app_instance.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "CustomTkinter_logo_single.png")),
            size=const.image_logoiconsize)

        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            master=self.navigation_frame,
            text=const.logoText,
            image=self.app_instance.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15,
                                       weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.app_instance.binance_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0,
            height=40,
            border_spacing=10,
            text=const.navigationButtonText1,
            fg_color=const.color_transparent,
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.app_instance.home_image, anchor="w",
            command=self.app_instance.gui_events.home_button_event)
        self.app_instance.binance_button.grid(row=1, column=0, sticky="ew")

        self.app_instance.bitget_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0,
            height=40,
            border_spacing=10, text=const.navigationButtonText2,
            fg_color=const.color_transparent,
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.app_instance.chat_image, anchor="w",
            command=self.app_instance.gui_events.frame_2_button_event)
        self.app_instance.bitget_button.grid(row=2, column=0, sticky="ew")

        self.app_instance.okx_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10, text=const.navigationButtonText3,
            fg_color=const.color_transparent,
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.app_instance.add_user_image, anchor="w",
            command=self.app_instance.gui_events.frame_3_button_event)
        self.app_instance.okx_button.grid(row=3, column=0, sticky="ew")

        self.app_instance.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                             values=["System", "Light", "Dark"],
                                                                             command=change_appearance_mode_event)
        self.app_instance.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
