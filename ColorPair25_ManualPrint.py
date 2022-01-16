from ColorPair25_Lib import *
import numpy as np
import matplotlib.pyplot as plt

cp25_rows = []
cp25_table_text = []
cp25_colors = []

for majcolor in MAJOR_COLORS:
    for mincolor in MINOR_COLORS:
         cp25_rows.append(get_pair_number_from_color(majcolor,mincolor))
         cp25_table_text.append([get_pair_number_from_color(majcolor,mincolor),majcolor,"",mincolor,""])
         if(mincolor =="Slate"):
             mincolor = "slategrey"
         cp25_colors.append(['w',"w",majcolor,"w",mincolor])
cp25_columns = ["ColorCode","MajorColorName","MajorColor","MinorColorName","MinorColor"]

print(cp25_table_text)
print(cp25_rows)

fig, ax = plt.subplots(figsize = (6,8))

ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)

colorPair25_NumMapTable = ax.table(cellText=cp25_table_text,
                                    rowLabels=cp25_rows,
                                    colLabels=cp25_columns,
                                    cellColours=cp25_colors,
                                    loc='top',
                                    bbox=[0,0,1,1])
#plt.subplots_adjust(top=0.7,bottom=0.01)
colorPair25_NumMapTable.scale(1.5, 2)
textstr = "Refer below manual for ColorCode and corresponding Major and Minor Color"
plt.gcf().text(0.03, 0.9, textstr, fontsize=10)
plt.savefig("plotted.pdf",bbox_inches='tight')
plt.show()