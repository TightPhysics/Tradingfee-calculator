import customtkinter
import Domain.Interfaces.guiconst as const
from Domain.Logic.bitget.bitget_market_selection import select_option_by_name
from Domain.Logic.bitget.bitget_market_selection import is_custom_selected


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

        self.app_instance.bitget_frame.label3 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text="Fee"
        )
        self.app_instance.bitget_frame.label3.grid(
            row=5, column=0, padx=50, pady=(10, 0), sticky="w")
        self.app_instance.bitget_frame.label3.grid_remove()

        self.app_instance.bitget_frame.entry3 = customtkinter.CTkEntry(
            self.app_instance.bitget_frame,
            placeholder_text="e.g.: 20% = 0.2"
        )
        self.app_instance.bitget_frame.entry3.grid(
            row=6, column=0, padx=50, pady=0, sticky="w")
        self.app_instance.bitget_frame.entry3.grid_remove()

        # right side
        self.app_instance.bitget_frame.label4 = customtkinter.CTkLabel(
            self.app_instance.bitget_frame,
            text=const.bitget_label3Text)
        self.app_instance.bitget_frame.label4.grid(row=1, column=0, padx=145, pady=0, sticky="e")

        self.app_instance.bitget_frame.optionMenu = customtkinter.CTkOptionMenu(
            self.app_instance.bitget_frame,
            command=self.app_instance.gui_events.select_option_by_name,
            values=const.market)
        self.app_instance.bitget_frame.optionMenu.grid(row=2, column=0, padx=50, pady=0, sticky="e")

        # main buttons
        max_rows = self.app_instance.bitget_frame.grid_size()[1]
        self.app_instance.bitget_frame.grid_columnconfigure(0, weight=1)
        self.app_instance.bitget_frame.grid_rowconfigure(8, weight=1)

        self.app_instance.bitget_frame_button_3 = customtkinter.CTkButton(
            self.app_instance.bitget_frame,
            text="OK",
            compound="bottom",
            anchor="s")
        self.app_instance.bitget_frame_button_3.grid(row=8, column=0, padx=20, pady=20, sticky="se",)
