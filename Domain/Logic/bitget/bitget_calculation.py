import Domain.Interfaces.guiconst as const


def calculate(entry, amount, market, fee):
    # this setup is only for maker fees
    if market == const.market[0]:
        fee = 0.02
        return float(entry) * float(amount) * (float(fee) / 100)
    elif market == const.market[1]:
        fee = 0.1
        return float(entry) * float(amount) * (float(fee) / 100)
    elif market == const.market[2]:
        return float(entry) * float(amount) * (float(fee) / 100)
