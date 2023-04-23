import Domain.Logic.frame_logic as frame_logic
import Domain.Interfaces.guiconst as const


class GuiEvent:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

    def dynamic_button_events(self):
        for i in const.navigationButtons:
            frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=i)

    def home_button_event(self):
        frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=const.navigationButtonText1)

    def frame_2_button_event(self):
        frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=const.navigationButtonText2)

    def frame_3_button_event(self):
        frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=const.navigationButtonText3)
