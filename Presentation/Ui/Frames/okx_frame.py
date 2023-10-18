import customtkinter
import Domain.Interfaces.guiconst as const


class OKXFrame:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

        self.app_instance.third_frame = customtkinter.CTkFrame(self.app_instance, corner_radius=0,
                                                               fg_color=const.color_transparent)