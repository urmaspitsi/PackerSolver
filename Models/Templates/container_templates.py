from ..container_item import ContainerItem

##########################################################################
# 1. Containers
##########################################################################

# source: https://etslogistika.ee/teadmiseks/konteinerite-parameetrid/

def DryCargo20() -> ContainerItem:
  return ContainerItem(width=235, height=239, length=590)

def DryCargo20Upgraded() -> ContainerItem:
  return ContainerItem(width=235, height=260, length=590)

def DryCargo40() -> ContainerItem:
  return ContainerItem(width=235, height=239, length=1203)

def HighCube40() -> ContainerItem:
  return ContainerItem(width=235, height=269, length=1203)

def HighCubePalletWide45() -> ContainerItem:
  return ContainerItem(width=242, height=269, length=1355)

def HardTop20() -> ContainerItem:
  return ContainerItem(width=234, height=239, length=590)

def HardTop40() -> ContainerItem:
  return ContainerItem(width=235, height=239, length=1205)

def Refrigeration20() -> ContainerItem:
  return ContainerItem(width=229, height=216, length=540)

def Refrigeration40() -> ContainerItem:
  return ContainerItem(width=229, height=250, length=1159)

def OpenTop20() -> ContainerItem:
  return ContainerItem(width=235, height=239, length=590)

def OpenTop40() -> ContainerItem:
  return ContainerItem(width=235, height=235, length=1205)


##########################################################################
# 2. Trucks
##########################################################################

# source: https://etslogistika.ee/en/types-trucks-trailers/

def SemiTrailer() -> ContainerItem:
  '''
    Semi-trailer can capacitate up to 33 EUR pallets or 26 FIN pallets
  '''
  return ContainerItem(width=245, height=270, length=1360)

def SaddleTrailer() -> ContainerItem:
  '''
    The truck consists of a saddle truck and two separate parts of trailers: saddle trailer + trailer.
    Full trailer can capacitate either 38 EUR pallets or 30 FIN pallets.
  '''
  return ContainerItem(width=245, height=290, length=730)

def Trailer() -> ContainerItem:
  '''
    The truck consists of a saddle truck and two separate parts of trailers: saddle trailer + trailer.
    Full trailer can capacitate either 38 EUR pallets or 30 FIN pallets.
  '''
  return ContainerItem(width=245, height=290, length=810)

def JumboTrailer() -> ContainerItem:
  '''
    The car consists of a saddle truck and a jumbo trailer (13,6 x 2,45 x 3m) 
     (the first 4 meters of the jumbo trailer has lower height of 2,6m).
    The jumbo trailer can capacitate up to 33 EUR pallets or 26 FIN pallets,
    out of which 23 EUR or 18 FIN pallets can be loaded up to 3 meters in height.
  '''
  return ContainerItem(width=245, height=300, length=1360)


def RefrigeratedTrailer() -> ContainerItem:
  '''
    The refrigerated truck consists of a saddle truck and a semi-trailer (equipped with cooling system).
    The refrigerated trailer can capacitate up to 33 EUR pallets or 26 FIN pallets.
  '''
  return ContainerItem(width=246, height=265, length=1341)

def TailLiftTruck() -> ContainerItem:
  '''
    The refrigerated truck consists of a saddle truck and a semi-trailer (equipped with cooling system).
    Tail-lift truck can capacitate up to 18-20 EUR pallets or 14-16 FIN pallets.
  '''
  return ContainerItem(width=245, height=250, length=900)

