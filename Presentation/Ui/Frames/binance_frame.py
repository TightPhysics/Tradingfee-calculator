import customtkinter
import Domain.Interfaces.guiconst as const


class BinanceFrame:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

        self.app_instance.binance_frame = customtkinter.CTkFrame(self.app_instance, corner_radius=0,
                                                                 fg_color=const.color_transparent)
        self.app_instance.binance_frame.grid_columnconfigure(0, weight=1)
        self.app_instance.binance_frame_large_image_label = customtkinter.CTkLabel(self.app_instance.binance_frame, text="",
                                                                                   image=self.app_instance.large_test_image)
        self.app_instance.binance_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.app_instance.binance_frame_button_1 = customtkinter.CTkButton(self.app_instance.binance_frame, text="",
                                                                           image=self.app_instance.image_icon_image)
        self.app_instance.binance_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.app_instance.binance_frame_button_2 = customtkinter.CTkButton(self.app_instance.binance_frame, text="CTkButton",
                                                                           image=self.app_instance.image_icon_image,
                                                                           compound="right")
        self.app_instance.binance_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.app_instance.binance_frame_button_3 = customtkinter.CTkButton(self.app_instance.binance_frame, text="CTkButton",
                                                                           image=self.app_instance.image_icon_image,
                                                                           compound="top")
        self.app_instance.binance_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.app_instance.binance_frame_button_4 = customtkinter.CTkButton(self.app_instance.binance_frame, text="CTkButton",
                                                                           image=self.app_instance.image_icon_image,
                                                                           compound="bottom",
                                                                           anchor="w")
        self.app_instance.binance_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
