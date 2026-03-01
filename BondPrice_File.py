import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    m_eff = m * ppy
    couponRate = couponRate / ppy
    y_eff = y / ppy

    t = np.arange(1, m_eff + 1)
    discount = 1 / (1 + y_eff) ** t

    price = np.sum(face * couponRate * discount) + face * discount[-1]

    return price
