from core.analyzer import DxfAnalyzer


def main():

    analyzer = DxfAnalyzer()

    result = analyzer.analyze("G:\\Laserdaten\\ZZ Sonstiges\\Inlays\\Karton Inlay - AuftNr=K269632 K=595x405x395 V=450x341x77 zs=482x395mm.dxf")

    print()
    print("=== DXF Analyse ===")
    print()

    print(f"Entities gesamt       : {result.total_entities}")
    print(f"Texte                 : {result.text_count}")
    print(f"Dimensionen           : {result.dimension_count}")
    print(f"Geschlossene Konturen : {result.closed_polylines}")
    print(f"Offene Konturen       : {result.open_polylines}")
    print(f"Null-Längen-Linien    : {result.zero_length_lines}")

    print()
    print("Layer:")

    for layer in sorted(result.layers):
        print(f"  - {layer}")

    print()
    print("Entity-Typen:")

    for entity_type, count in sorted(result.entity_counts.items()):
        print(f"  {entity_type:<20} {count}")

    print("\nIssues:")
    for issue in result.issues:
        print(f"[{issue.severity}] {issue.message}")

if __name__ == "__main__":
    main()

## This is a sample Python script.
#
## Press Umschalt+F10 to execute it or replace it with your code.
## Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
#
#
## Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
#
#import ezdxf
#
#doc = ezdxf.readfile("G:\\Laserdaten\\ZZ Sonstiges\\Inlays\\Karton Inlay - AuftNr=K269632 K=595x405x395 V=450x341x77 zs=482x395mm.dxf")
#
#print("DXF geladen")
#
#msp = doc.modelspace()
#
#for entity in msp:
#    print(entity.dxftype())
#
## See PyCharm help at https://www.jetbrains.com/help/pycharm/
#