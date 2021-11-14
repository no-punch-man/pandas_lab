import pandas as pd
import matplotlib.pyplot as plt
df_g = pd.read_excel(r'C:\Users\Anton\Downloads\students\students_info.xlsx')
df_ = pd.read_html(r'C:\Users\Anton\Downloads\students\results_ejudge.html')
df_m = df_[0]
df_g.rename(columns = {'login': 'User'}, inplace = True)
sorted_df_m = df_m.sort_values(by = 'User')
df_merged = pd.merge(df_g, sorted_df_m)

#task 1
width = 0.9
labels_f = [i + 1 for i in range(8)]
means_f = []
for i in range (8):
    if(i != 6):
        means_f.append(round(df_merged[df_merged.group_faculty == i + 1]['Solved'].mean()))
    else:
        means_f.append(0)


fig, ax = plt.subplots()
ax.bar(labels_f, means_f, width)
ax.set_title('Rounded number of solved tasks per faculty groups')
fig.savefig("Rounded number of solved tasks per faculty groups" + ".png")

means_o = []
labels_o = sorted(pd.unique(df_g['group_out']))
labels_o[6] = 37
labels_o.append(38)
for i in range (8):
    if(i != 6):
        means_o.append(round(df_merged[df_merged.group_out == i + 31]['Solved'].mean()))
    else:
        means_o.append(0)
        
fig, ax = plt.subplots()
ax.bar(labels_o, means_o, width)
ax.set_title('Rounded number of solved tasks per out groups')
fig.savefig("Rounded number of solved tasks per out groups" + ".png")

#task 2
smort = df_merged.loc[(df_merged.G > 10) | (df_merged.H > 10)]
where = pd.unique(smort['group_faculty'])
to_where = pd.unique(smort['group_out'])
print(where)
print(to_where)
