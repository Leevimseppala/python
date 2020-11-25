itemlist = ["PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
            "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
            "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
            "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
            "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
            "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"]
categories = ["Muut", "Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]
for x in range(len(itemlist)):
    splitted = itemlist[x].split("_")
    print("Valmistaja:", splitted[0])
    print(f"Nimi ja malli: {splitted[1]} {splitted[2]}")
    splitted[7] = int(splitted[7])
    print("Kategoria:", categories[splitted[7]])
    print(f"Lisäyspäivämäärä: {splitted[5]}.{splitted[4]}.{splitted[3]}\n\n")
