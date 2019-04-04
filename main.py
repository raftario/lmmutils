from nbt import nbt


def list_items(file, sort=True):
    items = [
        tag["K"].__str__().replace("", "").replace(" ", "")
        for tag in file["FML"]["ItemData"].tags
        if "lotr:item" in tag["K"].__str__()
    ]
    if sort: items.sort()
    return items


def list_axes(items): return [item for item in items if "lotr:item.axe" in item]


def main():
    file = input("level.dat [level.dat] : ") or "level.dat"
    nbt_file = nbt.NBTFile(file, "rb")

    items = list_items(nbt_file)
    axes = list_axes(items)

    for item in items:
        print(item)
    for axe in axes:
        print(axe)


if __name__ == "__main__":
    main()
