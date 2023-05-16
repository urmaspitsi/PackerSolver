from ..package_item import PackageItem

# source: https://etslogistika.ee/en/land-transportation/

def Pallet_EUR(height: float) -> PackageItem:
  return PackageItem(width=120, height=height, length=80)

def Pallet_FIN(height: float) -> PackageItem:
  return PackageItem(width=120, height=height, length=100)

