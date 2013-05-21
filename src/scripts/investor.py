#investor.py

InvestorUseMarker = ("InvestorUserMarker", "9073af82-f4a4-40d4-824d-e9af57aa81fc")

class Investor():
  @staticmethod
  def cash_out(card, x = 0, y = 0):
    mute()
    if card.orientation & Rot90 != Rot90:
      card.orientation ^= Rot90
      card.markers[InvestorUseMarker] += 1
      gainAmount = int(card.properties['resourcegain'])
      me.counters['cash'].value += gainAmount
      str = '{} for {}'.format(card,gainAmount)
      notify('{} cashs out {}'.format(me,str))
      maxUseCountProp = card.properties['maxusage']
      maxUseCount = int(maxUseCountProp)
      if maxUseCount > 0:
        mcount = _api.MarkerGetCount(card._id,InvestorUseMarker[0], InvestorUseMarker[1])
        if mcount >= maxUseCount:
          card.moveTo(me.piles['Discard'])
          notify('{} Bleeds {} dry'.format(me,card))
