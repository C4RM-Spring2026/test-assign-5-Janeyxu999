import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    m_eff = m * ppy
    y_eff = y / ppy
    couponRate_eff = couponRate / ppy

    t = np.arange(1, m_eff + 1)
    discount = 1 / (1 + y_eff) ** t

    cf = np.full(m_eff, couponRate_eff * face, dtype = float)
    cf[-1] += face

    pvcf = cf * discount

    duration = np.sum(t * pvcf) / np.sum(pvcf)

    return duration
