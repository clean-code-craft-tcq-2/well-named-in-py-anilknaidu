from ColorPair25_Lib import *
import numpy as np
import matplotlib.pyplot as plt

def ColorPair25_GeneratePDF_Manual():
    cp25_table_rows = []
    cp25_table_text = []
    cp25_table_cell_colors = []
    cp25_columns = ["ColorCode","MajorColorName","MajorColor","MinorColorName","MinorColor"]

    for majorColor in MAJOR_COLORS:
        for minorColor in MINOR_COLORS:
            colorCode = get_pair_number_from_color(majorColor,minorColor)
            print("ColorCode: ",colorCode,"--> MajorColor: "+majorColor,"  MinorColor: "+minorColor)
            cp25_table_rows.append(colorCode)
            cp25_table_text.append([str(colorCode), majorColor,"",minorColor,""])
            if(minorColor =="Slate"):
                minorColor = "slategrey"
            cp25_table_cell_colors.append(['White',"White",majorColor,"White",minorColor])

    colorPair25_Fig, colorPair25_table_Axes = plt.subplots(figsize = (6,8))

    colorPair25_table_Axes.xaxis.set_visible(False) 
    colorPair25_table_Axes.yaxis.set_visible(False)

    colorPair25_NumMapTable = colorPair25_table_Axes.table(cellText=cp25_table_text,
                                        rowLabels=cp25_table_rows,
                                        colLabels=cp25_columns,
                                        cellColours=cp25_table_cell_colors,
                                        loc='top',
                                        bbox=[0,0,1,1])
    colorPair25_NumMapTable.scale(2, 2)
    colorPair25_plot_text = "Refer below table for ColorCode and corresponding Major and Minor Color"
    plt.gcf().text(0.03, 0.9, colorPair25_plot_text, fontsize=10)
    plt.savefig("ColorPair25_Manual_forReference.pdf",bbox_inches='tight')
    plt.show()