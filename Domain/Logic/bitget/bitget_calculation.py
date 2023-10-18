import Domain.Interfaces.guiconst as const


def calculate(entry, amount, market, fee, mkortk) -> float:
    # this setup is only for maker fees  - 0 maker, 1 taker
    if market == const.market[0] and mkortk == const.makerortaker_list[0]:
        fee = 0.02
        return float(entry) * float(amount) * (float(fee) / 100)
    elif market == const.market[1] and mkortk == const.makerortaker_list[0]:
        fee = 0.1
        return float(entry) * float(amount) * (float(fee) / 100)
    elif market == const.market[2]:
        return float(entry) * float(amount) * (float(fee) / 100)
    elif market == const.market[0] and mkortk == const.makerortaker_list[1]:
        fee = 0.06
        return float(entry) * float(amount) * (float(fee) / 100)
    elif market == const.market[1] and mkortk == const.makerortaker_list[1]:
        fee = 0.5
        return float(entry) * float(amount) * (float(fee) / 100)
