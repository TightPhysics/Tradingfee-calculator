import Domain.Logic.frame_logic as frame_logic
import Domain.Interfaces.guiconst as const
from Application.Common.Usecases import binance_use_case, bitget_use_case, okx_use_case, main_frame_use_case


class GuiEvent:
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance
        self.bitget_usecase = bitget_use_case.BitgetUseCase(app_instance)
        self.binance_usecase = binance_use_case.BinanceUseCase(app_instance)
        self.okx_usecase = okx_use_case.OKXUseCase(app_instance)
        self.frame_usecase = main_frame_use_case.FrameUseCase(app_instance)

    # navigation menu events
    def dynamic_button_events(self):
        for i in const.navigationButtons:
            frame_logic.select_frame_by_name(self=self.app_instance, const=const, name=i)

    def on_binance_navigation_button_event(self):
        self.binance_usecase.binance_navigation_button_event()

    def on_bitget_navigation_button_event(self):
        self.bitget_usecase.bitget_navigation_button_event()

    def okx_navigation_button_event(self):
        self.okx_usecase.okx_navigation_button_event()

    # bitget_frame events
    def on_select_option_by_name(self, name):
        self.frame_usecase.select_option_by_name(name)

    def on_ok_button_event(self):
        self.bitget_usecase.ok_button_event()

    def on_clipboard_event(self):
        self.bitget_usecase.clipboard_event()
