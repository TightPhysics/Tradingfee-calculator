import ui.interfaces.guiconst as const
from ui.frames.binance_frame import binance_frame
from ui.frames.bitget_frame import bitget_frame
from ui.frames.okx_frame import okx_frame
import ui.frames.navigation_frame as navframe
import customtkinter
import os
from PIL import Image


def change_appearance_mode_event(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(const.titleText)
        self.geometry(const.geometry)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join("test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=const.image_logoiconsize)
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=const.image_largesize)
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=const.image_smallsize)
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=const.image_smallsize)
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=const.image_smallsize)
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=const.image_smallsize)

        # create navigation frame
        navframe.navigation_frame(self=self, customtkinter=customtkinter,
                                  change_appearance_mode_event=change_appearance_mode_event, const=const)

        # create home frame
        binance_frame(self=self, customtkinter=customtkinter, const=const)

        # create second frame
        bitget_frame(self=self, customtkinter=customtkinter, const=const)

        # create third frame
        okx_frame(self=self, customtkinter=customtkinter, const=const)

        # select default frame
        navframe.select_frame_by_name(self=self, const=const, name=const.navigationButtonText1)

    def home_button_event(self):
        navframe.select_frame_by_name(self=self, const=const, name=const.navigationButtonText1)

    def frame_2_button_event(self):
        navframe.select_frame_by_name(self=self, const=const, name=const.navigationButtonText2)

    def frame_3_button_event(self):
        navframe.select_frame_by_name(self=self, const=const, name=const.navigationButtonText3)
