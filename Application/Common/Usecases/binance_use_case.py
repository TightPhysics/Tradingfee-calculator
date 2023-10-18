import Domain.Interfaces.guiconst as const
import Domain.Logic.frame_logic as frame_logic


class BinanceUseCase:
    def __init__(self, app_instance):
        self.frame_logic = frame_logic
        self.app_instance = app_instance

    def binance_navigation_button_event(self):
        self.frame_logic.select_frame_by_name(self=self.app_instance, name=const.navigationButtonText1, const=const)