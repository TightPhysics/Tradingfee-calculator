import os

import customtkinter
from PIL import Image

import Domain.Interfaces.guiconst as const


class BitgetFrame:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

        self.banner_image = customtkinter.CTkImage(Image.open(os.path.join(
            self.app_instance.image_path, "large_image_3_bitget_edit.png")), size=const.image_largesize)

        self.app_instance.bitget_frame = customtkinter.CTkFrame(
            self.app_instance, corner_radius=0,
            fg_color=const.color_transparent)
        self.app_instance.bitget_frame.grid_columnconfigure(0, weight=1)

        self.app_instance.bitget_frame_banner_image_label = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="",
            image=self.banner_image)
        self.app_instance.bitget_frame_banner_image_label.grid(row=0, column=0, padx=1, pady=20)

        # left side
        self.app_instance.bitget_frame.label1 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label1Text)
        self.app_instance.bitget_frame.label1.grid(row=1, column=0, padx=100, pady=0, sticky="w")

        self.app_instance.bitget_frame.entry1 = customtkinter.CTkEntry(
            self.app_instance.bitget_frame,
            placeholder_text=const.bitget_entryPlaceholder1)
        self.app_instance.bitget_frame.entry1.grid(row=2, column=0, padx=95, pady=0, sticky="w")

        self.app_instance.bitget_frame.label2 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label2Text)
        self.app_instance.bitget_frame.label2.grid(row=3, column=0, padx=100, pady=(10, 0), sticky="w")

        self.app_instance.bitget_frame.entry2 = customtkinter.CTkEntry(
            self.app_instance.bitget_frame,
            placeholder_text=const.bitget_entryPlaceholder2)
        self.app_instance.bitget_frame.entry2.grid(row=4, column=0, padx=95, pady=0, sticky="w")

        self.app_instance.bitget_frame.label3 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="Fee"
        )
        self.app_instance.bitget_frame.label3.grid(
            row=5, column=0, padx=100, pady=(10, 0), sticky="w")
        self.app_instance.bitget_frame.label3.grid_remove()

        self.app_instance.bitget_frame.entry3 = customtkinter.CTkEntry(
            self.app_instance.bitget_frame,
            placeholder_text="e.g.: 20% = 0.2"
        )
        self.app_instance.bitget_frame.entry3.grid(
            row=6, column=0, padx=95, pady=0, sticky="w")
        self.app_instance.bitget_frame.entry3.grid_remove()

        # right side
        self.app_instance.bitget_frame.label4 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label3Text)
        self.app_instance.bitget_frame.label4.grid(row=1, column=0, padx=195, pady=0, sticky="e")

        self.app_instance.bitget_frame.optionMenu = customtkinter.CTkOptionMenu(
            self.app_instance.bitget_frame,
            command=self.app_instance.gui_events.on_select_option_by_name,
            values=const.market)
        self.app_instance.bitget_frame.optionMenu.grid(row=2, column=0, padx=100, pady=0, sticky="e")

        self.app_instance.bitget_frame.optionMenu2 = customtkinter.CTkOptionMenu(
            self.app_instance.bitget_frame,
            command=self.app_instance.gui_events.on_select_option_by_name,
            values=const.makerortaker_list
        )
        self.app_instance.bitget_frame.optionMenu2.grid(row=4, column=0, padx=100, pady=0, sticky="e")

        self.app_instance.bitget_frame.label6 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="",
            text_color="red"
        )
        self.app_instance.bitget_frame.label6.grid(row=8, column=0, padx=20, pady=50, sticky="se")
        self.app_instance.bitget_frame.label6.grid_remove()

        # bottom menu
        self.app_instance.bitget_frame.grid_columnconfigure(0, weight=1)
        self.app_instance.bitget_frame.grid_rowconfigure(8, weight=1)

        self.app_instance.bitget_frame_button_3 = customtkinter.CTkButton(
            self.app_instance.bitget_frame,
            text="OK",
            command=self.app_instance.gui_events.on_ok_button_event,
            compound="bottom",
            anchor="s")
        self.app_instance.bitget_frame_button_3.grid(row=8, column=0, padx=20, pady=20, sticky="se")

        self.app_instance.bitget_frame.label5 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="Fee for you trade: ",
            compound="bottom",
            anchor="s"
        )
        self.app_instance.bitget_frame.label5.grid(row=8, column=0, padx=20, pady=20, sticky="sw")

        self.app_instance.bitget_frame.label5 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="",
            compound="bottom",
            anchor="s"
        )
        self.app_instance.bitget_frame.label5.grid(row=8, column=0, padx=130, pady=20, sticky="sw")
        self.app_instance.bitget_frame.label5.grid_remove()

        self.app_instance.bitget_frame.clipboard_button = customtkinter.CTkButton(
            self.app_instance.bitget_frame,
            border_spacing=0,
            width=10,
            height=20,
            text="",
            command=self.app_instance.gui_events.on_clipboard_event,
            image=self.app_instance.copy_symbol_image,
            compound="bottom",
            anchor="s",
            fg_color="transparent",
            bg_color="transparent",

        )
        self.app_instance.bitget_frame.clipboard_button.grid(row=8, column=0, padx=200, pady=20, sticky="se")

