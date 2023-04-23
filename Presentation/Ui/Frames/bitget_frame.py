import customtkinter
import Domain.Interfaces.guiconst as const
from Domain.Logic.bitget.bitget_market_selection import select_option_by_name


class BitgetFrame:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

        self.app_instance.bitget_frame = customtkinter.CTkFrame(
            self.app_instance, corner_radius=0,
            fg_color=const.color_transparent)
        self.app_instance.bitget_frame.grid_columnconfigure(0, weight=1)

        self.app_instance.bitget_frame_large_image_label = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="",
            image=self.app_instance.large_test_image)
        self.app_instance.bitget_frame_large_image_label.grid(row=0, column=0, padx=1, pady=1)

        # left side
        self.app_instance.bitget_frame.label1 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label1Text)
        self.app_instance.bitget_frame.label1.grid(row=1, column=0, padx=55, pady=0, sticky="w")

        self.app_instance.bitget_frame.entry1 = customtkinter.CTkEntry(
            self.app_instance.bitget_frame,
            placeholder_text=const.bitget_entryPlaceholder1)
        self.app_instance.bitget_frame.entry1.grid(row=2, column=0, padx=50, pady=0, sticky="w")

        self.app_instance.bitget_frame.label2 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label2Text)
        self.app_instance.bitget_frame.label2.grid(row=3, column=0, padx=50, pady=(10, 0), sticky="w")

        self.app_instance.bitget_frame.entry2 = customtkinter.CTkEntry(
            self.app_instance.bitget_frame,
            placeholder_text=const.bitget_entryPlaceholder1)
        self.app_instance.bitget_frame.entry2.grid(row=4, column=0, padx=50, pady=0, sticky="w")

        self.app_instance.bitget_frame_button_3 = customtkinter.CTkButton(
            self.app_instance.bitget_frame, text="OK",
            compound="top")
        self.app_instance.bitget_frame_button_3.grid(row=5, column=0, padx=50, pady=20, sticky="w")

        # right side
        self.app_instance.bitget_frame.label3 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label3Text)
        self.app_instance.bitget_frame.label3.grid(row=1, column=0, padx=145, pady=0, sticky="e")

        market = ["Futures", "Spot"]
        self.app_instance.bitget_frame.optionMenu = customtkinter.CTkOptionMenu(
            self.app_instance.bitget_frame,
            command=select_option_by_name,
            values=market)
        self.app_instance.bitget_frame.optionMenu.grid(row=2, column=0, padx=50, pady=0, sticky="e")
